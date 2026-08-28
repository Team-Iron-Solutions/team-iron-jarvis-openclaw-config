# Controlled HUD STT Test — Step by Step

**Do not deviate — follow exactly. We're collecting evidence, not just testing.**

## Setup
1. Open http://localhost:3033/hud in browser
2. Ensure microphone is working and browser has permission
3. Open browser DevTools (F12) → Console tab
4. Have a clock visible to measure timing

## Test Sequence

### Test 1: Wake Word Detection (3 attempts)
**Goal:** Verify wake word detection triggers consistently

```
Attempt 1a:
  - Say: "Jarvis" (clear, normal volume, 1 second pause)
  - OBSERVE: Does HUD change color? (should go green/listening)
  - RECORD: Yes/No, any console errors?

Attempt 1b: (wait 5 seconds, repeat)
  - Say: "Jarvis"
  - RECORD: Yes/No

Attempt 1c: (wait 5 seconds, repeat)  
  - Say: "Jarvis"
  - RECORD: Yes/No

Summary: ___ / 3 successful detections
```

### Test 2: Listening Duration (single attempt)
**Goal:** Measure how long HUD listens after "Jarvis"

```
Attempt 2a:
  - Say: "Jarvis"
  - Note the exact time (use clock)
  - Wait 3 seconds (stay silent)
  - Say question: "qual é a data de hoje"
  - Note when HUD stops listening (color changes or "Processando" appears)
  - Calculate: listening_duration = (question_time - wake_time)
  
Expected: ≥4 seconds
Actual: ___ seconds

Console errors? (copy any red errors)
_______________
```

### Test 3: Processing & Response (single attempt)
**Goal:** Does agent receive command and respond?

```
Attempt 3a:
  - Say: "Jarvis, olá"
  - OBSERVE: Does it transition to "Processando"?
  - OBSERVE: Does audio play back (TTS)?
  - OBSERVE: Does HUD return to "Ouvindo"?

Processing state appeared? Yes/No
Audio played? Yes/No
Returned to listening? Yes/No

Any WS errors in console?
_______________
```

## Data Collection

**In another terminal, run:**
```bash
tail -f /Users/teamironsolutions/.openclaw/workspace/.tmp/openclaw-spikes/hud-stt-diagnostics/bridge-logs.txt
```

**Copy any ERROR or WARN lines**

When test is complete, press CTRL+C on the tail and notify Jarvis.

---

**Do not proceed to next test until previous is documented.**
