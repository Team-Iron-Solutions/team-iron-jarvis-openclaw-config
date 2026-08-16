import express from "express";
import { WebSocketServer } from "ws";
import path from "path";
import { fileURLToPath } from "url";
import fetch from "node-fetch";
import { spawn } from "child_process";
import fs from "fs";
import os from "os";
import CavemanMiddleware from "./caveman-middleware-esm.js";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const app = express();
const wss = new WebSocketServer({ noServer: true });
const caveman = new CavemanMiddleware({ mode: 'aggressive', verbose: true });

const OPENCLAW_GATEWAY = "http://127.0.0.1:18789";

// Path do binário openclaw (nvm)
const OPENCLAW_BIN = '/Users/teamironsolutions/.nvm/versions/node/v24.18.0/bin/openclaw';

// Sessão dedicada ao HUD — separada da sessão main para não interferir no webchat
// Usa a mesma identidade (agent main) mas session-key própria → tem MEMORY.md + workspace + Obsidian
const HUD_SESSION_KEY = 'hud';

// ── MODOS DE RESPOSTA ────────────────────────────────────────────────────────
//
//  RÁPIDO  (padrão)          haiku + thinking:off    ~6s
//  NORMAL  "Jarvis, pensa"   haiku + thinking:medium ~15s
//  TÉCNICO "modo técnico"    sonnet + thinking:medium ~30s
//
// Triggers são detectados na mensagem e removidos antes de enviar ao agente.
// ─────────────────────────────────────────────────────────────────────────────

const MODES = [
  {
    triggers: ['modo técnico', 'modo sonnet', 'modo expert'],
    model: 'sonnet', thinking: 'medium', label: 'TÉCNICO'
  },
  {
    triggers: ['pensa nisso', 'pensa bem', 'modo normal', 'analisa isso'],
    model: 'haiku', thinking: 'medium', label: 'NORMAL'
  }
];

function resolveMode(text) {
  const lower = text.toLowerCase();
  for (const mode of MODES) {
    for (const trigger of mode.triggers) {
      if (lower.includes(trigger)) {
        const clean = text.replace(new RegExp(trigger, 'gi'), '').replace(/,\s*$/, '').trim();
        return { model: mode.model, thinking: mode.thinking, label: mode.label, message: clean };
      }
    }
  }
  return { model: 'haiku', thinking: 'off', label: 'RÁPIDO', message: text };
}

// Chama o agente real com sessão persistente do HUD
// O agente tem acesso a: MEMORY.md, SOUL.md, USER.md, workspace, Obsidian vault
// Instrução de voz embutida na mensagem: resposta curta e natural para TTS
async function callJarvisAgent(rawMessage) {
  const { model, thinking, label, message } = resolveMode(rawMessage);
  console.log(`🧠 Modo: ${label} (${model}, thinking:${thinking})`);

  // Compress input with Caveman before sending to OpenClaw
  let compressed = await caveman.compressInput(message);
  const compressedMessage = compressed.message;
  const compressionRatio = compressed.metadata.compression_ratio;
  console.log(`[CAVEMAN] Input compression: -${compressionRatio}%`);

  const voicePrompt = `[HUD Voice — responda em 1 a 2 frases curtas, sem markdown, texto puro para TTS. Seja conciso como JARVIS dos filmes.]\n\n${compressedMessage}`;

  return new Promise((resolve, reject) => {
    const proc = spawn(OPENCLAW_BIN, [
      'agent',
      '--agent', 'main',
      '--session-key', HUD_SESSION_KEY,
      '--model', model,
      '--thinking', thinking,
      '--message', voicePrompt
    ], {
      env: {
        ...process.env,
        PATH: `/Users/teamironsolutions/.nvm/versions/node/v24.18.0/bin:${process.env.PATH}`
      }
    });

    let stdout = '';
    let stderr = '';

    proc.stdout.on('data', d => stdout += d);
    proc.stderr.on('data', d => stderr += d);

    proc.on('close', (code) => {
      const reply = stdout.trim();
      if (reply) {
        // Remove markdown residual (**, *, #, `) se o agente produzir
        const clean = reply
          .replace(/[*_`#]/g, '')
          .replace(/\n+/g, ' ')
          .trim();
        // Track compression stats
        global.lastCompressionRatio = compressionRatio;
        resolve(clean);
      } else {
        reject(new Error(`Agent exited ${code}: ${stderr.trim()}`));
      }
    });

    proc.on('error', reject);
  });
}

// "Should I Stay or Should I Go" — The Clash (URI verificada)
const SPOTIFY_TRACK_URI = 'spotify:track:39shmbIHICJ2Wxnk1fPSdz';
const SPOTIFY_CLI = '/Applications/Spotify.app/Contents/MacOS/spotify_cli';

// ElevenLabs Otto
const ELEVEN_VOICE_ID = 'ycxdm1PRMs962FxyyuJ0';
const ELEVEN_MODEL    = 'eleven_turbo_v2_5';
const ELEVEN_API_KEY  = (() => {
  try {
    const cfg = JSON.parse(fs.readFileSync(os.homedir() + '/.openclaw/openclaw.json', 'utf8'));
    return cfg?.messages?.tts?.providers?.elevenlabs?.apiKey || '';
  } catch { return ''; }
})();
console.log('🔑 ElevenLabs key:', ELEVEN_API_KEY ? ELEVEN_API_KEY.slice(0,8) + '...' : 'NOT FOUND');

let musicProcess = null;
let preduckedSpotifyVolume = 100; // volume do Spotify antes do duck

// ── HELPERS ──────────────────────────────────────

function broadcastToClients(data) {
  wss.clients.forEach((client) => {
    if (client.readyState === 1) {
      client.send(JSON.stringify(data));
    }
  });
}

function sleep(ms) {
  return new Promise(r => setTimeout(r, ms));
}

// Audio Ducking — reduz o volume do SPOTIFY (não do sistema)
// O TTS (afplay) toca no volume cheio do sistema, sem ser afetado
const DUCK_RATIO = 0.4; // Spotify cai para 40% enquanto Jarvis fala

async function duckVolume() {
  const out = await runAppleScript('tell application "Spotify" to get sound volume');
  const current = parseInt(out) || 100;
  preduckedSpotifyVolume = current < 30 ? 80 : current; // floor para evitar loop
  await runAppleScript(`tell application "Spotify" to set sound volume to ${Math.floor(preduckedSpotifyVolume * DUCK_RATIO)}`);
}

async function unDuckVolume() {
  await runAppleScript(`tell application "Spotify" to set sound volume to ${preduckedSpotifyVolume}`);
}

// ElevenLabs TTS — Otto voice (with audio ducking)
// Estratégia: gera o áudio PRIMEIRO, só então duca o volume e toca
// Elimina a pausa silenciosa causada por geração de áudio com volume baixo
async function say(text) {
  let tmpFile = null;

  try {
    // ── 1. GERA O ÁUDIO (sem duck ainda) ─────────────────────────────────────
    if (ELEVEN_API_KEY) {
      try {
        const controller = new AbortController();
        const timeout = setTimeout(() => controller.abort(), 8000);
        const res = await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${ELEVEN_VOICE_ID}`, {
          method: 'POST',
          signal: controller.signal,
          headers: { 'xi-api-key': ELEVEN_API_KEY, 'Content-Type': 'application/json' },
          body: JSON.stringify({
            text, model_id: ELEVEN_MODEL,
            voice_settings: { stability: 0.5, similarity_boost: 0.8, style: 0.2, use_speaker_boost: true }
          })
        });
        clearTimeout(timeout);
        if (res.ok) {
          tmpFile = os.tmpdir() + '/jarvis-tts-' + Date.now() + '.mp3';
          fs.writeFileSync(tmpFile, Buffer.from(await res.arrayBuffer()));
          console.log('🔊 TTS: ElevenLabs OK');
        } else {
          console.warn(`⚠️ ElevenLabs HTTP ${res.status}, falling back`);
        }
      } catch (err) {
        console.warn('⚠️ ElevenLabs failed, falling back:', err.message);
      }
    }

    // Fallback: edge-tts AntonioNeural
    if (!tmpFile) {
      console.log('🔊 TTS: generating via edge-tts AntonioNeural...');
      tmpFile = os.tmpdir() + '/jarvis-tts-fallback-' + Date.now() + '.mp3';
      await new Promise((resolve) => {
        const proc = spawn('/Users/teamironsolutions/Library/Python/3.9/bin/edge-tts', [
          '--voice', 'pt-BR-AntonioNeural', '--text', text, '--write-media', tmpFile
        ]);
        proc.on('close', resolve);
        proc.on('error', resolve);
      });
    }

    // ── 2. ÁUDIO PRONTO → duca, sinaliza HUD (pausa STT), toca ──────────────
    await duckVolume();
    broadcastToClients({ type: 'speaking' }); // HUD pausa o microfone
    console.log('🔊 TTS: playing...');
    await new Promise((resolve) => {
      const proc = spawn('afplay', [tmpFile]);
      proc.on('close', resolve);
      proc.on('error', resolve);
    });

  } finally {
    if (tmpFile) fs.unlink(tmpFile, () => {});
    // Retoma Spotify se afplay o pausou, depois restaura volume
    const state = await runAppleScript('tell application "Spotify" to get player state');
    if (state === 'paused') await runAppleScript('tell application "Spotify" to play');
    await unDuckVolume();
    broadcastToClients({ type: 'idle' }); // HUD reativa o microfone
    console.log('🔊 TTS: done, Spotify volume restored');
  }
}

async function testGatewayConnection() {
  try {
    const res = await fetch(`${OPENCLAW_GATEWAY}/health`);
    if (res.ok) console.log("✅ OpenClaw Gateway connected");
  } catch (err) {
    console.error("❌ OpenClaw Gateway not responding:", err.message);
  }
}

// ── ROUTES ───────────────────────────────────────

app.use(express.json());

app.get("/health", (req, res) => {
  res.json({ ok: true });
});

// Serve HUD
app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "hud-jarvis-v2.html"));
});

// ── /send — process voice command ──
app.post("/send", async (req, res) => {
  const { text } = req.body;
  if (!text) return res.status(400).json({ error: "text required" });

  console.log(`💬 Command: "${text}"`);
  broadcastToClients({ type: "processing", transcript: text });

  try {
    // Chamar o agente real (sessão main) — com MEMORY.md, Obsidian vault, workspace completo
    const reply = await callJarvisAgent(text);

    console.log(`🤖 Jarvis: "${reply}"`);
    broadcastToClients({ type: 'response', response: reply });
    res.json({ ok: true, response: reply });
    await say(reply);
    broadcastToClients({ type: 'idle' });

  } catch (err) {
    console.error('LLM error:', err.message);
    const fallback = 'Desculpe, senhor. Estou com dificuldades técnicas no momento.';
    broadcastToClients({ type: 'response', response: fallback });
    res.json({ ok: true, response: fallback });
    await say(fallback);
    broadcastToClients({ type: 'idle' });
  }
});

// ── /wake — wake word triggered ──
app.post("/wake", async (req, res) => {
  const { wakeId } = req.body;
  console.log(`🎙️ Wake triggered: ${wakeId}`);

  // Responde APÓS o TTS terminar — o HUD só inicia o cmdRec depois que o Jarvis parou de falar
  try {
    if (wakeId === "clap_phrase") {
      broadcastToClients({ type: "wake_special" });
      console.log('🎵 Playing via Spotify...');
      await playSpotify(SPOTIFY_TRACK_URI);
      await sleep(1200);
      console.log('🔊 Wake TTS: saudação especial...');
      await say("Bom dia, senhor. Bem-vindo de volta. Estou às suas ordens.");
      broadcastToClients({ type: "wake_done" });

    } else if (wakeId === "jarvis") {
      broadcastToClients({ type: "wake_simple" });
      console.log('🔊 Wake TTS: jarvis...');
      await say("Sim, senhor?");
      broadcastToClients({ type: "wake_done" });

    } else if (wakeId === "ei_jarvis") {
      broadcastToClients({ type: "wake_simple" });
      console.log('🔊 Wake TTS: ei_jarvis...');
      await say("Sim, senhor. Estou aqui.");
      broadcastToClients({ type: "wake_done" });
    }
  } catch (err) {
    console.error(`❌ Wake TTS error (${wakeId}):`, err.message);
  }

  res.json({ ok: true }); // Responde após TTS — HUD conta 4500ms a partir daqui
});

// ── /music/stop — stop Spotify ──
app.post("/music/stop", async (req, res) => {
  await runAppleScript('tell application "Spotify" to pause');
  console.log("🎵 Spotify paused");
  res.json({ ok: true });
});

// ── HELPERS ──
function runAppleScript(script) {
  return new Promise((resolve) => {
    const proc = spawn('osascript', ['-e', script]);
    let out = '';
    proc.stdout.on('data', d => out += d);
    proc.on('close', () => resolve(out.trim()));
    proc.on('error', resolve);
  });
}

async function playSpotify(uri) {
  return new Promise((resolve) => {
    const proc = spawn(SPOTIFY_CLI, ['play', uri]);
    proc.on('close', resolve);
    proc.on('error', resolve);
  });
}

// ── SERVER ───────────────────────────────────────

const server = app.listen(3033, () => {
  console.log("🌐 Jarvis Bridge v4 listening on :3033");
  testGatewayConnection();
});

server.on("upgrade", (request, socket, head) => {
  if (request.url === "/stream") {
    wss.handleUpgrade(request, socket, head, (ws) => {
      console.log("✅ WebSocket client connected");
      ws.send(JSON.stringify({ type: "connected" }));
    });
  }
});
