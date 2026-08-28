# Spike: HUD STT Issues — Diagnostic Plan

**Date:** 2026-08-20 12:28 GMT-3  
**Issue:** Wake word inconsistent, listening time short, processing fails  
**Scope:** Reproduce + collect logs + identify root cause (no code changes)

## Question

Why is the HUD experiencing:
1. Wake word detection inconsistent (sometimes detects "Jarvis", sometimes doesn't)
2. Listening window too short (not enough time to say full question)
3. Processing hangs (says "Processando..." but never responds)

## Method

### Phase 1: State Audit
- [ ] HUD version in use (v2 vs v5)
- [ ] Bridge status and version
- [ ] LaunchAgent config
- [ ] Network connectivity (WS, HTTP)

### Phase 2: Instrumentation
- [ ] Enable verbose logging on bridge
- [ ] Monitor bridge logs in real-time during HUD interaction
- [ ] Capture browser console logs
- [ ] Trace STT lifecycle (start → interim → final → abort/end)

### Phase 3: Controlled Test
- [ ] Test 1: Say "Jarvis" — observe wake detection
- [ ] Test 2: Say "Jarvis" + question — observe listening time
- [ ] Test 3: Say "Jarvis" + wait + question — test async handling
- [ ] Test 4: Check WebSocket message flow

### Phase 4: Analysis
- [ ] Correlate browser logs ↔ bridge logs ↔ agent response
- [ ] Identify bottleneck (STT timeout, bridge queue, agent timeout, WS delivery)
- [ ] Determine if it's:
  - Configuration (continuous, interimResults, timeout settings)
  - Race condition (timing between wake/command recognition)
  - Integration (bridge not forwarding correctly)
  - Network (WS not delivering idle state)

## Expected Output

- `SPIKE-LOGS.txt` — raw logs from test runs
- `SPIKE-ANALYSIS.md` — root cause with evidence
- `SPIKE-VERDICT.md` — recommendation on next steps
