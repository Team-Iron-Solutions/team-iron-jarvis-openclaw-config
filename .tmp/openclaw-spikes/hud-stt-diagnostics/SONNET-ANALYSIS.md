# HUD v5-Metrics — Análise de Bugs Críticos (Sonnet)

**Data:** 2026-08-20  
**Modelo:** anthropic/claude-sonnet-4-6  
**Arquivos analisados:**
- `hud-jarvis-v5-metrics.html` (linhas 1414–1664)
- `jarvis-bridge-v4.js` (linhas completas)

---

## Resumo Executivo

Foram identificados **5 bugs**, sendo 2 críticos e 3 de alta prioridade. O hang em `[Processando...]` é causado por ausência de timeout no agente. A janela de escuta curta é causada por um timer de 2200ms **redundante** (o TTS já terminou quando o timer começa). Os outros bugs são de sincronização de estado.

---

## Fluxo Completo Traçado

```
[Wake "Jarvis" detectado]
  → wakeRec.onresult → onWakeDetected('jarvis', 'wr2')
  → wakeLocked=true → stopWakeListener()
  → POST /wake (await fetch — bloqueia HUD!)
    → Bridge: broadcastToClients({type:'wake_simple'})
    → Bridge: await say("Sim, senhor?")
      → gera TTS ElevenLabs (~1-3s)
      → duckVolume()
      → broadcastToClients({type:'speaking'}) ← HUD: isSpeaking=true
      → afplay (~1-2s de playback)
      → finally: broadcastToClients({type:'idle'}) ← HUD: startWakeListener() (não inicia — wakeLocked ainda true)
      → finally: unDuckVolume()
    → broadcastToClients({type:'wake_done'})
    → res.json({ok:true}) ← HTTP resolve retorna para HUD
  ← fetch resolve
  → setTimeout(2200ms)  ← *** BUG-2: redundante, TTS já terminou ***
    → wakeLocked=false
    → setTimeout(400ms)
      → startCommandListen() → cmdRec.start()

[Usuário fala]
  → cmdRec.onresult → text capturado
  → cmdProcessing=true
  → setMode('processing')
  → POST /send (await fetch — pode travar para sempre)
    → Bridge: broadcastToClients({type:'processing'})
    → await callJarvisAgent(text) ← *** BUG-1: SEM TIMEOUT ***
    → res.json({ok:true, response:reply})  ← HTTP resolve
    → broadcastToClients({type:'speaking'}) ← *** BUG-3: duplicate ***
    → await say(reply)
      → broadcastToClients({type:'speaking'}) ← duplicate
      → afplay
      → finally: broadcastToClients({type:'idle'}) ← idle #1
    → broadcastToClients({type:'idle'}) ← *** BUG-3: idle #2 duplicate ***
  ← HUD fetch resolve → setMode('speaking') → stopWakeListener()
  ← HUD WS idle #1 → startWakeListener()
  ← HUD WS idle #2 → startWakeListener() (guard previne duplo)
```

---

## Bugs Identificados

---

### 🔴 BUG-1 (CRÍTICO): Sem timeout em `callJarvisAgent()` → hang infinito

**Sintoma:** HUD trava em `[Processando...]`, nunca responde.

**Arquivo:** `jarvis-bridge-v4.js`  
**Localização:** Função `callJarvisAgent()`, dentro do `new Promise()`

**Código atual (linhas ~99–130):**
```javascript
return new Promise((resolve, reject) => {
  const proc = spawn(OPENCLAW_BIN, [
    'agent', '--agent', 'main',
    '--session-key', HUD_SESSION_KEY,
    '--model', model, '--thinking', thinking,
    '--message', voicePrompt
  ], { env: { ...process.env, PATH: `...` } });

  let stdout = '';
  let stderr = '';

  proc.stdout.on('data', d => stdout += d);
  proc.stderr.on('data', d => stderr += d);

  proc.on('close', (code) => {      // ← ÚNICO path de resolução
    const reply = stdout.trim();
    if (reply) resolve(clean);
    else reject(new Error(`Agent exited ${code}: ${stderr.trim()}`));
  });

  proc.on('error', reject);
  // ❌ SEM TIMEOUT — se openclaw travar, Promise nunca resolve
});
```

**Root cause:** Se o OpenClaw gateway estiver lento, o modelo demorar demais, ou o processo travar (e.g., rate limit, sessão bloqueada), o `proc.close` nunca dispara. O `/send` route fica bloqueado, sem `res.json()` enviado, sem WS `idle` enviado. HUD fica em `[Processando...]` indefinidamente.

**Fix exato:**
```javascript
return new Promise((resolve, reject) => {
  const proc = spawn(OPENCLAW_BIN, [
    'agent', '--agent', 'main',
    '--session-key', HUD_SESSION_KEY,
    '--model', model, '--thinking', thinking,
    '--message', voicePrompt
  ], { env: { ...process.env, PATH: `/Users/teamironsolutions/.nvm/versions/node/v24.18.0/bin:${process.env.PATH}` } });

  let stdout = '';
  let stderr = '';

  // ✅ Timeout de 45s — mata o processo e rejeita a Promise
  const killTimer = setTimeout(() => {
    proc.kill('SIGTERM');
    reject(new Error('Agent timeout after 45s'));
  }, 45000);

  proc.stdout.on('data', d => stdout += d);
  proc.stderr.on('data', d => stderr += d);

  proc.on('close', (code) => {
    clearTimeout(killTimer); // ✅ Limpa o timer se fechou normalmente
    if (code !== 0) metricsState.errorCount++;
    const reply = stdout.trim();
    if (reply) {
      const clean = reply
        .replace(/\[\[tts[^\]]*\]\]|\[\[\/tts[^\]]*\]\]/g, '')
        .replace(/[*_`#]/g, '')
        .replace(/\n+/g, ' ')
        .trim();
      global.lastCompressionRatio = compressionRatio;
      resolve(clean);
    } else {
      reject(new Error(`Agent exited ${code}: ${stderr.trim()}`));
    }
  });

  proc.on('error', (err) => { clearTimeout(killTimer); reject(err); });
});
```

---

### 🔴 BUG-2 (CRÍTICO): Timer de 2200ms redundante → janela de escuta efetivamente −2600ms

**Sintoma:** Usuário ouve "Sim, senhor?" e fica em silêncio aguardando, mas o HUD só abre o microfone 2600ms depois.

**Arquivo:** `hud-jarvis-v5-metrics.html`  
**Localização:** Função `onWakeDetected()`, o `setTimeout` após o `await fetch('/wake')`

**Código atual:**
```javascript
async function onWakeDetected(wakeId, wrRef){
  // ...
  try{
    await fetch('http://localhost:3033/wake', {   // ← bloqueia até TTS terminar
      method:'POST', headers:{'Content-Type':'application/json'},
      body:JSON.stringify({wakeId})
    });
  }catch(e){ console.warn('Wake call failed:', e); }

  setTimeout(()=>{          // ← ❌ começa APÓS TTS já ter terminado
    wakeLocked=false;
    setMode('idle');
    setTimeout(()=>{ startCommandListen(); },400);
  }, wakeId==='clap_phrase' ? 4500 : 2200);  // ← 2200ms completamente redundantes
}
```

**Root cause:** O `/wake` route do bridge só responde HTTP **depois** que `await say()` completa (TTS + playback). Então o `fetch` só resolve quando o áudio já terminou. O timer de 2200ms foi provavelmente calibrado para uma versão anterior onde o `/wake` respondia imediatamente. Hoje, o TTS já acabou quando o timer começa → 2200ms + 400ms = **2.6 segundos de silêncio absoluto** após Jarvis terminar de falar, antes do microfone abrir.

**Timeline real:**
```
t=0    "Jarvis" detectado
t=0.1  fetch /wake inicia
t=1.5  TTS gerado (ElevenLabs ~1-3s)
t=2.5  "Sim, senhor?" toca e termina (~1s de áudio)
t=2.5  fetch /wake resolve ← HTTP response chega
t=4.7  wakeLocked=false (2200ms depois)  ← silêncio total
t=5.1  cmdRec.start() (400ms depois)    ← mic abre finalmente
```

**Fix exato (mudar apenas o valor do delay):**
```javascript
// ANTES:
}, wakeId==='clap_phrase' ? 4500 : 2200);

// DEPOIS:
}, wakeId==='clap_phrase' ? 500 : 200);
```

Justificativa: Como o TTS já terminou quando o fetch resolve, apenas ~200ms são necessários para o sistema de áudio "assentar" e o usuário tomar um respiro. Para `clap_phrase`, 500ms são suficientes (a música Spotify continua tocando de fundo).

---

### 🟠 BUG-3 (ALTO): Duplo broadcast de `speaking` e `idle` no `/send` route

**Sintoma:** Estado do HUD oscila, `startWakeListener()` é chamado duas vezes — possível race condition em browsers lentos. Não é o bug principal do hang, mas cria ruído de estado.

**Arquivo:** `jarvis-bridge-v4.js`  
**Localização:** Route `/send`, dentro do bloco `try` e `catch`

**Código atual:**
```javascript
// No route /send:
const reply = await callJarvisAgent(text);
res.json({ ok: true, response: reply });
broadcastToClients({ type: 'speaking' }); // ← broadcast #1 (no route)
await say(reply);                         // say() já faz speaking + idle internamente
broadcastToClients({ type: 'idle' });     // ← broadcast #3 (no route — redundante)
```

**Dentro de `say()`:**
```javascript
broadcastToClients({ type: 'speaking' }); // ← broadcast #2 (inside say)
await afplay(tmpFile);
// finally:
broadcastToClients({ type: 'idle' });     // ← broadcast #2 (inside say)
```

**Sequência recebida pelo HUD:**
```
speaking → speaking → idle → idle
```

O segundo `idle` causa uma segunda chamada a `startWakeListener()`, que o guard (`if wakeRunning`) previne de iniciar duplo. Mas o HUD faz `setMode('idle')` duas vezes, e em browsers com timing instável pode criar flickers.

**Fix exato — remover os broadcasts redundantes do `/send` route:**
```javascript
// No route /send try block — REMOVER as linhas marcadas:
const reply = await callJarvisAgent(text);
res.json({ ok: true, response: reply });
// ❌ REMOVER: broadcastToClients({ type: 'speaking' });
await say(reply);
// ❌ REMOVER: broadcastToClients({ type: 'idle' });

// No route /send catch block — REMOVER as linhas marcadas:
res.json({ ok: true, response: fallback });
// ❌ REMOVER: broadcastToClients({ type: 'speaking' });
await say(fallback);
// ❌ REMOVER: broadcastToClients({ type: 'idle' });
```

`say()` já gerencia os broadcasts corretamente.

---

### 🟠 BUG-4 (ALTO): `cmdRec.onend` sem recovery → wake listener "vai a óbito"

**Sintoma:** Após timeout do cmdRec sem speech (sem `no-speech` error em alguns browsers), o HUD fica em idle sem listener ativo. Precisa de refresh para recuperar.

**Arquivo:** `hud-jarvis-v5-metrics.html`  
**Localização:** Handler `cmdRec.onend`

**Código atual:**
```javascript
cmdRec.onend=()=>{ cmdListening=false; };
// ❌ SEM recovery — se onend disparar sem onerror (ex: Chrome em algumas condições),
// wake listener nunca reinicia
```

**Root cause:** O Web Speech API em alguns contextos dispara `onend` sem disparar `onerror` quando não há speech detectado. O `cmdRec.onerror` tem recovery (`setTimeout(()=>startWakeListener(),500)`), mas `cmdRec.onend` não tem. Resultado: `cmdListening=false`, `wakeRunning=false`, `wakeLocked=false` — tudo false, mas nenhum listener ativo.

**Fix exato:**
```javascript
cmdRec.onend=()=>{ 
  cmdListening=false;
  // ✅ Recovery: se não está processando (nenhum fetch em andamento), reinicia wake listener
  if(!cmdProcessing) setTimeout(()=>startWakeListener(), 600);
};
```

---

### 🟡 BUG-5 (MÉDIO): `wakeRec.onresult` itera de `i=0` ao invés de `event.resultIndex`

**Sintoma:** Falsos positivos de wake word — "Jarvis" detectado do nada, sem o usuário falar, especialmente depois de sessões longas.

**Arquivo:** `hud-jarvis-v5-metrics.html`  
**Localização:** Handler `wakeRec.onresult`

**Código atual:**
```javascript
wakeRec.onresult=(event)=>{
  if(wakeLocked||isSpeaking) return;
  let combined='';
  for(let i=0;i<event.results.length;i++)  // ← i=0: acumula TUDO desde o início da sessão
    combined+=event.results[i][0].transcript.toLowerCase();
  for(const wp of WAKE_PHRASES){
    if(combined.includes(wp.phrase)){
      onWakeDetected(wp.id, wp.wr);
      break;
    }
  }
};
```

**Root cause:** Com `continuous=true` e `interimResults=true`, `event.results` acumula todos os resultados da sessão (não limpa entre restarts se o browser reutilizar o objeto). Iterar de `i=0` significa que "Jarvis" dito há 10 minutos ainda está no `combined`. Na prática, `wakeRec.stop()` + `wakeRec.start()` reinicia o histórico na maioria dos browsers — mas isso é comportamento não-garantido pela API.

**Fix exato:**
```javascript
wakeRec.onresult=(event)=>{
  if(wakeLocked||isSpeaking) return;
  // ✅ Verifica apenas resultados NOVOS (desde o último processado)
  let combined='';
  for(let i=event.resultIndex;i<event.results.length;i++)
    combined+=event.results[i][0].transcript.toLowerCase();
  for(const wp of WAKE_PHRASES){
    if(combined.includes(wp.phrase)){
      onWakeDetected(wp.id, wp.wr);
      break;
    }
  }
};
```

---

## Ordem de Prioridade dos Fixes

| Prioridade | Bug | Sintoma | Arquivo | Fix |
|---|---|---|---|---|
| 1 | BUG-1 | Hang infinito em `[Processando...]` | `jarvis-bridge-v4.js` | Adicionar timeout 45s no `callJarvisAgent()` |
| 2 | BUG-2 | Janela de escuta 2600ms curta/atrasada | `hud-jarvis-v5-metrics.html` | Mudar `2200` → `200` no `onWakeDetected` |
| 3 | BUG-4 | Wake listener morre sem recovery | `hud-jarvis-v5-metrics.html` | Adicionar `startWakeListener()` no `cmdRec.onend` |
| 4 | BUG-3 | Duplo speaking/idle no `/send` | `jarvis-bridge-v4.js` | Remover broadcasts redundantes do route |
| 5 | BUG-5 | Falsos positivos de wake word | `hud-jarvis-v5-metrics.html` | Mudar `i=0` → `i=event.resultIndex` |

---

## Patch Consolidado

### Arquivo 1: `hud-jarvis-v5-metrics.html`

**Patch A — BUG-2: reduz timer de wake→listen**
```diff
-  }, wakeId==='clap_phrase' ? 4500 : 2200);
+  }, wakeId==='clap_phrase' ? 500 : 200);
```

**Patch B — BUG-4: recovery no cmdRec.onend**
```diff
-cmdRec.onend=()=>{ cmdListening=false; };
+cmdRec.onend=()=>{
+  cmdListening=false;
+  if(!cmdProcessing) setTimeout(()=>startWakeListener(), 600);
+};
```

**Patch C — BUG-5: usar resultIndex no wakeRec.onresult**
```diff
-  for(let i=0;i<event.results.length;i++) combined+=event.results[i][0].transcript.toLowerCase();
+  for(let i=event.resultIndex;i<event.results.length;i++) combined+=event.results[i][0].transcript.toLowerCase();
```

---

### Arquivo 2: `jarvis-bridge-v4.js`

**Patch D — BUG-1: timeout em callJarvisAgent()**
```diff
   return new Promise((resolve, reject) => {
     const proc = spawn(OPENCLAW_BIN, [
       'agent', '--agent', 'main',
       '--session-key', HUD_SESSION_KEY,
       '--model', model, '--thinking', thinking,
       '--message', voicePrompt
     ], { env: { ...process.env, PATH: `/Users/teamironsolutions/.nvm/versions/node/v24.18.0/bin:${process.env.PATH}` } });

     let stdout = '';
     let stderr = '';

+    const killTimer = setTimeout(() => {
+      proc.kill('SIGTERM');
+      reject(new Error('Agent timeout after 45s'));
+    }, 45000);

     proc.stdout.on('data', d => stdout += d);
     proc.stderr.on('data', d => stderr += d);

     proc.on('close', (code) => {
+      clearTimeout(killTimer);
       if (code !== 0) metricsState.errorCount++;
       const reply = stdout.trim();
       if (reply) {
         const clean = reply
           .replace(/\[\[tts[^\]]*\]\]|\[\[\/tts[^\]]*\]\]/g, '')
           .replace(/[*_`#]/g, '')
           .replace(/\n+/g, ' ')
           .trim();
         global.lastCompressionRatio = compressionRatio;
         resolve(clean);
       } else {
         reject(new Error(`Agent exited ${code}: ${stderr.trim()}`));
       }
     });

-    proc.on('error', reject);
+    proc.on('error', (err) => { clearTimeout(killTimer); reject(err); });
   });
```

**Patch E — BUG-3: remover broadcasts redundantes do /send route**
```diff
     const reply = await callJarvisAgent(text);
     res.json({ ok: true, response: reply });
-    broadcastToClients({ type: 'speaking' });
     await say(reply);
-    broadcastToClients({ type: 'idle' });

   } catch (err) {
     const fallback = 'Desculpe, senhor. Estou com dificuldades técnicas no momento.';
     broadcastToClients({ type: 'response', response: fallback });
     res.json({ ok: true, response: fallback });
-    broadcastToClients({ type: 'speaking' });
     await say(fallback);
-    broadcastToClients({ type: 'idle' });
```

---

## Notas Adicionais

### Por que `continuous=true` no cmdRec piorou as coisas

A tentativa anterior de adicionar `continuous=true` ao `cmdRec` falhou porque:
1. Com `continuous=true`, `onresult` dispara múltiplas vezes (resultados parciais + finais)
2. O guard `cmdProcessing=true` bloqueia resultados subsequentes, mas o fetch já foi feito com o texto parcial
3. O cmdRec nunca termina sozinho → `cmdListening` nunca vira `false` → wake listener nunca reinicia

A solução correta para janela longa **não é `continuous=true`** — é reduzir o delay (BUG-2). `cmdRec` sem `continuous` funciona corretamente: captura uma frase completa e encerra.

### Por que o bridge precisa reiniciar quando o HUD trava

O `jarvisState.isBusy = true` nunca é resetado se a rota `/send` travar antes do `finally`. Considerar adicionar um `try/finally` ao bloco do route:
```javascript
app.post("/send", async (req, res) => {
  // ...
  try {
    // ... lógica atual
  } catch(err) {
    // ... fallback atual
  } finally {
    // Garante reset do estado mesmo em casos extremos
    jarvisState.isBusy = false;
    jarvisState.status = 'online';
    jarvisState.currentTask = null;
  }
});
```
