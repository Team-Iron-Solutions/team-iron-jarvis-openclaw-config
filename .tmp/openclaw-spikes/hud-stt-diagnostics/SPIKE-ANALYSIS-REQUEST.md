# HUD v5-Metrics Analysis — Deep Code Review

## Problem Statement

**User:** Galvão (team CEO)  
**Date:** 2026-08-20 12:30 GMT-3  
**Status:** HUD v5-metrics broken, v2-fixed also broken  

### Symptoms (Observed by User)
1. **Wake word detection inconsistent** — sometimes detects "Jarvis", sometimes doesn't
2. **Listening window too short** — not enough time to say full question after wake word
3. **Processing hangs** — says "[Processando...]" but never responds, or takes very long time
4. **Bridge tray reset multiple times** — indicating possible state/timing issues

### Prior Attempts (Failed)
- Added `continuous=true` and `interimResults=true` to cmdRec
- Reduced wake→listen timeout from 2.2s to 1.2s
- Both made things worse

---

## Code to Review

### 1. **hud-jarvis-v5-metrics.html** (lines 1414-1600)

**Wake Detection Flow:**
- `wakeRec` (continuous, interimResults, not optional)
- Phrase matching: `['jarvis', 'ei jarvis', 'acorda criança papai chegou']`
- On match → `onWakeDetected(wakeId, wrRef)` (line 1559)

**Transition to Command Listening:**
- `onWakeDetected()` sets `wakeLocked=true`
- Waits 2.2s (jarvis) or 4.5s (clap_phrase) **inside wakeLocked**
- Then calls `startCommandListen()` which does `cmdRec.start()`

**Command Recognition (cmdRec):**
- Line 1414: NO `continuous=true`, NO `interimResults=true`
- Default STT behavior: **stops after first ~2-3 seconds of speech, or on pause**
- `onresult` (line 1428): raw transcript, no multi-part handling
- `onend` (line 1456): just sets `cmdListening=false`

**WebSocket State Sync (lines 1590-1605):**
- Listens for `type: 'speaking'` → sets `isSpeaking=true` → stops wake listener
- Listens for `type: 'idle'` → sets `isSpeaking=false` → restarts wake listener
- But **no explicit resync of `cmdListening` state** when idle arrives

### 2. **jarvis-bridge-v4.js** (lines 344-428)

**Command POST (line 384-443):**
```javascript
app.post("/send", async (req, res) => {
  // 1. broadcastToClients({ type: "processing" })
  // 2. Call callJarvisAgent(text)
  // 3. await say(reply) — sends { type: 'speaking' } at start, { type: 'idle' } when done
  // 4. broadcastToClients({ type: 'idle' }) after say() completes
```

**say() function (lines 158-210):**
- Generates TTS (ElevenLabs + fallback edge-tts)
- Ducks Spotify volume
- **Broadcasts { type: 'speaking' } before afplay**
- **Broadcasts { type: 'idle' } in finally block**
- Restores Spotify volume in finally

**Potential Issues:**
- `say()` flow: duck → broadcast speaking → play → broadcast idle → unduck
- If `afplay` hangs or TTS generation fails, entire flow blocks
- WebSocket broadcast might not reach client if connection is unstable

---

## Hypothesis: Why It's Broken

### Hypothesis A: Wake Word Detection Failing
**Cause:** `wakeRec` might be **stopping itself** after match and not restarting  
**Evidence:** `wakeRec.onend` (line 1486) has logic to restart, BUT:
```javascript
wakeRec.onend=()=>{ 
  wakeRunning=false; 
  if(!wakeLocked&&!cmdListening&&!isSpeaking) 
    setTimeout(startWakeListener,1000); 
};
```
If `wakeLocked` is true (which it is after onWakeDetected fires), then wakeRec never restarts.

### Hypothesis B: Listening Time Too Short  
**Cause:** `cmdRec` has no `continuous=true`  
**Evidence:** Web Speech API default:
- `continuous=false` → stops after first speech phrase or ~5 seconds of silence
- User says "Jarvis" → wake detected → `wakeLocked=true`
- Wait 2.2s → `startCommandListen()` calls `cmdRec.start()`
- User waits 1s before speaking → STT times out waiting for first phoneme
- **Or** user starts speaking, but STT stops after first 2-3 seconds if they pause for breath

### Hypothesis C: Processing Hangs
**Cause:** Mismatch between client expectation and server behavior
1. Client sends POST /send → waits for response
2. Bridge calls `callJarvisAgent()` → spawns openclaw process
3. If openclaw is slow or blocked, entire /send route blocks
4. Client shows "Processando..." forever
5. WebSocket idle never arrives (because route hasn't completed)

---

## Questions to Investigate

1. **cmdRec State Machine:**
   - Is `cmdRec` getting `aborted` error and failing silently?
   - Does `onresult` ever fire?
   - Does `onend` ever fire?

2. **WebSocket Timing:**
   - Are idle/speaking messages actually arriving at client?
   - Is there a race: client updates state before idle arrives?

3. **wake/command Transition:**
   - Is the 2.2s wait actually happening?
   - Does `startCommandListen()` actually call `cmdRec.start()` without error?

4. **openclaw Agent:**
   - Is the agent call slow? (timeout > 30s?)
   - Is HUD_SESSION_KEY blocking on something?

---

## Recommendation for Sonnet Analysis

Focus on:

1. **STT Lifecycle** — trace wake detection → listening → command handling
   - Add guard rails and logging
   - Ensure continuous mode OR proper timeout handling

2. **State Sync** — HUD state vs Bridge state must match
   - cmdListening, wakeRunning, isSpeaking must be synchronized
   - WebSocket must deliver EVERY message

3. **Error Handling** — find where it silently fails
   - cmdRec error codes (aborted, no-speech, network-error)
   - TTS generation timeout (8s)
   - openclaw spawn timeout

4. **Blocking Calls** — identify if /send route is blocking
   - Add timeout to callJarvisAgent (30s max)
   - Add timeout to TTS (15s max)
   - Non-blocking route to avoid client hanging

---

## Artifacts for Analysis

- `hud-jarvis-v5-metrics.html` — full code (lines 1414-1650 are critical)
- `jarvis-bridge-v4.js` — full code (lines 158-443 are critical)
- Browser console logs (user didn't provide yet)
- Bridge logs (not captured yet)

---

**Sonnet: Analyze the code, identify the bugs, and suggest specific fixes (not just refactoring).**
