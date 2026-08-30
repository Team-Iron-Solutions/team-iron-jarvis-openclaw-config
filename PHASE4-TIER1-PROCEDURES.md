# Phase 4 — Tier 1 Deployment Day-to-Day Procedures

**Owner:** T'Challa (SRE) + Tony Stark (Tech Lead)  
**Valid:** 30/08/2026 - 06/09/2026 (7 days)  
**Status:** 🟡 Ready for 30/08 09:00 deployment

---

## 📅 Daily Schedule

### 09:00 — Morning Health Check
```
[ ] Ollama service running
    curl http://localhost:11434/api/tags | head -10
    
[ ] Graphify pipeline accessible
    python3 PHASE4-SPRINT2-SIMULATED.py --test
    
[ ] Tier 1 agents available
    Check agent session status
    
[ ] Previous day's metrics collected
    ls -la metrics/daily*.json | tail -5
    
Report to team:
  ✅ All systems green → Continue
  ⚠️ Any issues → Debug and fix before allowing reviews
```

### 09:30 — Agent Configuration Check
```
For each Tier 1 agent (Tony, Bruce, Steve):

[ ] Graphify enabled in config
[ ] Ollama model qwen3.5:9b available
[ ] Max graph size configured (1000KB default)
[ ] Monitoring dashboard accessible

Command:
  cat $AGENT_WORKSPACE/config.json | grep -A5 graphify
```

### 10:00 — Code Reviews Start
```
First 3 reviews of the day:
[ ] Tony Stark — 1-2 reviews
[ ] Bruce Banner — 1-2 reviews
[ ] Steve Rogers — 0-1 reviews (lighter load)

Monitor each review:
[ ] Compression ratio collected
[ ] Quality score recorded
[ ] Latency measured
[ ] Errors logged

First review metrics should match Sprint 2:
  Compression: -85% to -92%
  Quality: 4.0-4.3/5
  Latency: 1-2s
```

### 14:00 — Midday Check
```
Metrics so far (after 4h of reviews):
[ ] Expected reviews: 8-12 total
[ ] Compression maintaining target?
[ ] Quality scores acceptable?
[ ] Any errors or anomalies?

If any metric failing:
  🔴 → Investigate immediately
  ⚠️ → Note for end-of-day review
  ✅ → Continue normal
```

### 18:00 — Evening Metrics Collection

```
Collect and record:
[ ] Total code reviews completed today
    Expected: 15-20 reviews/day for Tier 1
    
[ ] Compression ratio (daily average)
    Expected: ≥-85%
    Target: -87-92%
    
[ ] Quality score (daily average)
    Expected: ≥4.0/5
    Target: 4.1-4.3/5
    
[ ] Latency p95 (99th percentile)
    Expected: <2s
    Target: 1.2-1.5s
    
[ ] Total errors
    Expected: 0
    Target: 0-2 max

Command:
  python3 collect_daily_metrics.py
  python3 generate_metrics_report.py
  cat metrics/daily_$(date +%Y-%m-%d).json
```

### 19:00 — Daily Validation Report

```
Generate and review:
[ ] KPI validation (all 4 metrics)
[ ] Daily status (🟢 HEALTHY / 🟡 ACCEPTABLE / 🔴 NEEDS ATTENTION)
[ ] Recommended actions (if any metric failing)
[ ] Graphs/charts (compression trend, quality trend)

Report template:
  Day: 1/7
  Date: 30/08/2026
  Status: 🟢 HEALTHY
  Reviews: 18
  Compression: -88.3% (✅ PASS)
  Quality: 4.2/5 (✅ PASS)
  Latency: 1.5s (✅ PASS)
  Errors: 0 (✅ PASS)
  Actions: None — all systems nominal
```

### 20:00 — Team Standup
```
Brief sync (5-10 min):
[ ] Tier 1 deployment status
[ ] Any blockers or issues?
[ ] Metrics tracking to target?
[ ] Anything to communicate to leadership?

Report format:
  ✅ Day 1 complete, all KPIs passing
  📊 11 reviews, -87.9% compression, 4.1/5 quality
  ⚠️ Steve Rogers latency 2.1s (slightly high, acceptable)
  🚀 Ready for Day 2
```

---

## 🚨 Incident Response Procedure

### If Compression Fails (<-85%)

**Symptom:** 
```
Compression ratio: -75%, -80% (below -85% target)
```

**Diagnosis (30 min):**
```
1. Check graph size:
   - Is graph >1500KB? (Should be <1000KB)
   - Sample 5 code reviews, measure graph sizes
   
2. Check Ollama:
   - Is Ollama responding normally?
   - Check response times, error rates
   
3. Check code characteristics:
   - Are we analyzing larger repos/files?
   - Has file complexity changed?
```

**Response (immediate):**
```
Option A (Quick fix):
  1. Reduce max_graph_size_kb: 1000 → 500
  2. Re-run 1 code review
  3. Check compression ratio
  4. If ≥-85% → Continue with 500KB limit
  
Option B (Model optimization):
  1. Downgrade to qwen3.5:2b (smaller, faster)
  2. Expect slight quality loss (~0.1-0.2 points)
  3. Re-test 1 review
  4. If acceptable → Switch all agents
  
Option C (Full rollback):
  1. Disable graphify: enabled = false
  2. Return to Phase 3 (no graph)
  3. Maintain Phase 1-3 savings (-73%)
  4. Schedule investigation in separate sprint
```

### If Quality Drops (<4.0/5)

**Symptom:**
```
Quality score: 3.8/5, 3.5/5 (below 4.0 target)
```

**Diagnosis (30 min):**
```
1. Check baseline reviews:
   - Compare graph-based reviews vs Sprint 2
   - Are findings quality-equivalent?
   
2. Check Ollama output:
   - Are semantic labels accurate?
   - Is LLM response garbled?
   
3. Check real issues:
   - Did the code reviewed actually have quality issues?
   - Are our quality scores calibrated correctly?
```

**Response (immediate):**
```
Option A (Validation):
  1. Have human QA verify 5 reviews
  2. If reviews are actually good → Relax target to 3.8/5
  3. If reviews missing issues → Issue with graph/Ollama
  
Option B (Model change):
  1. Upgrade to qwen3.5:14b (if latency acceptable)
  2. Expect +0.1-0.2 quality improvement
  3. Re-test 5 reviews
  
Option C (Full rollback):
  1. Disable graphify (revert to Phase 3)
  2. Investigate issue separately
  3. Keep Phase 1-3 savings
```

### If Latency Too High (>2.5s)

**Symptom:**
```
Latency p95: 2.5s, 3.0s (above 2.0s target, barely acceptable)
```

**Diagnosis (15 min):**
```
1. Check Ollama:
   - Is model loaded in memory? (ollama list)
   - Any GPU issues? (nvidia-smi)
   
2. Check network:
   - Is localhost:11434 accessible?
   - Any network latency?
   
3. Check graph build:
   - How long does graph_build take?
   - Is it the bottleneck?
```

**Response (immediate):**
```
Option A (Model downgrade):
  1. Switch to qwen3.5:2b (faster, 4GB vs 6.5GB)
  2. Expect latency: 0.8-1.2s (improved)
  3. Expect quality: -0.1/5 (slight loss)
  4. Worth tradeoff if p95 > 2.5s
  
Option B (Optimization):
  1. Enable graph caching (don't rebuild every time)
  2. Parallelize graph building (if multiple reviews)
  3. Re-test latency
  
Option C (Adjust target):
  1. If latency 2-2.5s and acceptable for team:
  2. Adjust target to 2.5s instead of 2.0s
  3. Document tradeoff
```

### If Errors Accumulate (>5/day)

**Symptom:**
```
Errors: 6, 8, 10+ per day (above 5 tolerance)
```

**Diagnosis (30 min):**
```
1. What errors?
   - Ollama timeout?
   - File not found?
   - Encoding issues?
   - Permission denied?
   
2. Where?
   - In graph building?
   - In Ollama API?
   - In storage?
   
3. Pattern?
   - Same error repeating?
   - Different errors?
   - Random or systematic?
```

**Response (immediate):**
```
Option A (Fix root cause):
  1. Identify error pattern
  2. Deploy fix (example: fix file encoding)
  3. Restart agents
  4. Re-test
  
Option B (Mitigate):
  1. Add retry logic (3 retries, 5s backoff)
  2. Graceful fallback (graph fails → use Phase 3)
  3. Log all errors for post-mortem
  
Option C (Pause):
  1. If errors >15/day and unresolvable:
  2. Pause Tier 1 deployment
  3. Revert to Phase 3
  4. Schedule investigation
```

---

## ✅ Daily Checklist Template

```
📅 Date: ___/08/2026
🎯 Day: _ / 7

🟢 HEALTH CHECK (09:00)
[ ] Ollama running
[ ] Graph pipeline OK
[ ] Agents available
[ ] Previous metrics collected

🔍 AGENT STATUS (09:30)
[ ] Tony Stark configured
[ ] Bruce Banner configured
[ ] Steve Rogers configured

📊 CODE REVIEWS (10:00-18:00)
[ ] Reviews completed: __/20 target
[ ] Compression: __% (target: ≥-85%)
[ ] Quality: __/5 (target: ≥4.0)
[ ] Latency: __ms (target: <2000ms)
[ ] Errors: __ (target: <5)

✅ KPI VALIDATION (18:00)
[ ] Compression: ✅ PASS / ⚠️ WARN / ❌ FAIL
[ ] Quality: ✅ PASS / ⚠️ WARN / ❌ FAIL
[ ] Latency: ✅ PASS / ⚠️ WARN / ❌ FAIL
[ ] Errors: ✅ PASS / ⚠️ WARN / ❌ FAIL

🚨 INCIDENTS
[ ] None
[ ] Compression issue — Action: ___
[ ] Quality issue — Action: ___
[ ] Latency issue — Action: ___
[ ] Error incident — Action: ___

📝 NOTES
___________________________________________

🎯 TOMORROW
[ ] Continue normal operations
[ ] Watch for: ___________
[ ] Action items: ___________
```

---

## 📞 Escalation Path

**Level 1 — Routine (SRE on duty)**
```
- Metrics collection
- Daily validation
- Minor optimizations
- Documentation updates
Owner: T'Challa
Response: <1 hour
```

**Level 2 — Alert (Tech Lead + SRE)**
```
- Any KPI failing
- Latency >2.5s consistently
- Errors >5/day
- Compression <-80%
Owner: Tony Stark + T'Challa
Response: <30 min
```

**Level 3 — Critical (Full team)**
```
- Deployment failure
- Multiple agents failing
- Data corruption
- Rollback needed
Owner: Tony Stark, Steve Rogers, T'Challa, Jarvis
Response: <15 min
```

---

## 📊 Success Metrics Reminder

### Daily Target
```
✅ Compression: -87% average
✅ Quality: 4.1/5 average
✅ Latency p95: 1.5s average
✅ Errors: 0-1 per day
```

### 7-Day Target (Cumulative)
```
✅ 5+ days with compression ≥-85%
✅ ≥80% of reviews with quality ≥4.0/5
✅ ≥90% of reviews with latency <2s
✅ Zero errors 5+ days
```

### Go/No-Go Decision (06/09)
```
🟢 GO if:   All 4 KPIs pass 5+ days
🟡 MIXED if: 3 KPIs pass 5+ days
🔴 NO-GO if: <3 KPIs pass
```

---

## 🚀 Daily Report Example (Day 1)

```
DATE: 30/08/2026 (Day 1 of 7)
TIME: 19:00 GMT-3

STATUS: 🟡 ACCEPTABLE (3/4 KPIs passing)

METRICS:
  Reviews: 11 completed
  Compression: -87.9% ✅ PASS
  Quality: 4.1/5 ✅ PASS
  Latency p95: 2.1s ⚠️ WARN (slightly high)
  Errors: 0 ✅ PASS

AGENT BREAKDOWN:
  Tony Stark: 5 reviews, -88.5%, 4.3/5, 1.2s ✅
  Bruce Banner: 4 reviews, -89.2%, 4.1/5, 1.15s ✅
  Steve Rogers: 2 reviews, -86.0%, 4.0/5, 2.1s ⚠️

ACTIONS:
  🔧 Monitor Steve Rogers latency (architecture reviews naturally slower)
  ✅ No critical issues, continue Day 2

OUTLOOK:
  🚀 Deployment on track
  📈 Trending toward 7-day success
  ⚠️ Keep eye on latency for Steve (acceptable but high)
```

---

**Procedures Valid:** 30/08/2026 - 06/09/2026  
**Next Review:** 06/09/2026 (7-day validation complete)  
**Owner:** T'Challa (SRE) + Tony Stark (Tech Lead)

🚀 **READY FOR TIER 1 DEPLOYMENT**
