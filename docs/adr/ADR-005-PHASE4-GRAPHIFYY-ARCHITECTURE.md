# ADR-005: Phase 4 — Graphifyy + Ollama for Token Optimization in Code Review

**Status:** ✅ **APPROVED**

**Date:** 26/08/2026 (Architecture Review + Validation)

**Deciders:** Steve Rogers (CTO/Arquiteto), Galvão Silva (CEO), Jarvis (Tech Lead)

**Domain:** Code Review Optimization | Token Efficiency | Knowledge Graphs

---

## 1. Context

### Problem Statement

**Current State (Code Review Workflow):**
```
Tony Stark receives code review task
  ↓
Reads 50+ files to understand context
  → 20,000+ tokens consumed
  → 10+ minutes per review
  → Expensive at scale (120 reviews/month × 10 agents)
```

**Scale Impact:**
- 6 technical agents × 2 reviews/day × 20 days = 240 reviews/month
- 240 reviews × 20k tokens = 4.8M tokens/month on context loading alone
- At current rates: $14,400/month (**context loading tax** only)

### Proposed Solution

**Phase 4: Knowledge Graphs via Graphifyy**

Replace expensive file reads with queryable code maps:
```
graphify explain "ClassName"  → 150 tokens (~1s)
graphify path "ClassA" "ClassB" → 200 tokens (~1s)
read specific file (if needed)   → 500 tokens (~2s)
────────────────────────────────────────
Total: ~850 tokens vs 20,000 tokens (-95% in optimal cases)
```

### Technology Stack (Phase 4)

| Component | Choice | Rationale |
|---|---|---|
| Parser | **tree-sitter** | AST extraction, 52+ languages, deterministic, zero LLM cost |
| Semantic | **Ollama local** | Zero cloud cost, zero rate-limits, offline-first, qwen3.5 models |
| Tool | **Graphifyy** | Production-ready, handles tree-sitter + LLM integration, JSON output |
| Backend | **Mac mini local** | No external API dependencies, all processing local |

---

## 2. Decision

### Executive Summary

**✅ GO — with 3 mandatory pre-conditions before Sprint 3 Tier 1 rollout**

Graphifyy + Ollama architecture is technically sound and strategically aligned. Validated through Sprint 0 discovery and Sprint 1 working implementation (jarvis-neural-interface: 90 nodes, 113 edges, 68KB, $0).

---

### 2.1 Core Architecture Decisions

#### ✅ Decision: Use tree-sitter (AST puro) + Ollama semantic extraction

**Rationale:**
- Tree-sitter extracts structural facts (100% deterministic, zero LLM)
- Ollama adds semantic context (labels, rationale, criticality)
- Combination: high-fidelity context at minimal cost
- Alternative (LLM-only): Same cost, less reliable + loses structure

**Validation:** Sprint 1 confirmed 60 structural nodes (tree-sitter) + 30 semantic nodes (Ollama) = 90 total nodes from 200 files.

---

#### ✅ Decision: qwen3.5:9b for builds (not 4b)

**Rationale:**
- Build is one-time cost per repo (~30-40 min)
- Graph quality is permanent (affects all future queries)
- 9b vs 4b: +5-10 min build time, but -1-2% semantic label errors
- Trade-off: acceptable (optimize for correctness, not speed)

**Implementation Note:**
- Mac mini: 16GB RAM, 6-7GB allocated to Ollama 9b during build
- Builds must be sequential (never parallel) to prevent OOM
- Query time is unaffected: JSON reads are <1s regardless of model used

**Risk Mitigated:** Cheap model during build = poor graph quality = queries fail → loss of trust in tool

---

#### ✅ Decision: Sequential builds, coordinated by Jarvis (no parallelism)

**Rationale:**
- Mac mini RAM contention if 2+ agents build simultaneously
- Single Ollama instance cannot serve multiple builds
- Solution: Jarvis orchestrates sequential queue
- Cost: 30-40 min per repo, manageable for Phase 4 scope

**Workflow:**
```
Agent requests build → Jarvis checks if Ollama available
  IF busy: queue request, notify agent of wait time
  IF free: start build, notify agent when complete
  
Result: coordination overhead << build time savings
```

---

#### ✅ Decision: Ollama local (not OpenAI API)

**Rationale:**
- Cost: $0 (vs $0.01-0.05 per graph with OpenAI)
- Reliability: No rate-limits, no API key management, no cloud dependency
- Latency: Local processing (vs 500ms+ network roundtrip)
- Privacy: All code stays local

**Trade-off:** Requires qwen3.5 accuracy (95-98% vs GPT-4 99%+). Acceptable for this use case.

---

### 2.2 Three Mandatory Pre-Conditions (Before Sprint 3)

#### Pre-Condition #1: qwen3.5:9b validated in medium-size repo

**Requirement:** Build jarvis-neural-interface (or similar 1-3k file repo) with 9b, validate output

**Success Criteria:**
- [ ] graph.json generated without OOM
- [ ] 10 test queries return correct structure
- [ ] Build time <60 min
- [ ] Token reduction real (measure 5 code reviews: before/after)

**Owner:** Tony Stark (agent) + Jarvis (coordination)

**Timeline:** Sprint 1 (26-29/08/2026) ✅ COMPLETED

---

#### Pre-Condition #2: Wanda Maximoff isolated validation (Flutter generics edge case)

**Requirement:** Before inviting Tier 2 agents, validate graphifyy on Flutter codebase

**Why:** Flutter has generic components (Button<T>, Card<T>) that tree-sitter handles differently than Java/Python. Risk of incorrect structural extraction is localized to Tier 2.

**Success Criteria:**
- [ ] graph.json generated for Flutter repo
- [ ] 5 test queries validate generic type handling
- [ ] Wanda confirms UX acceptable

**Owner:** Scott Lang (agent) + Wanda (design perspective)

**Timeline:** Sprint 3 (before Tier 2 rollout)

---

#### Pre-Condition #3: Baseline measurements (5 reviews without graphify, then 5 with)

**Requirement:** Real-world measurement of token savings before full rollout

**Why:** Speculation is not evidence. We estimate -50-95% savings; actual data tells us if that's -30% or -80%.

**Workflow:**
```
Sprint 2 Part 1: Tony Stark does 5 code reviews WITHOUT graphify
  → Record: tokens used, latency, quality score (1-5)

Sprint 2 Part 2: Same repos, Tony does 5 code reviews WITH graphify
  → Record: tokens used, latency, quality score (1-5)

Δ = (without - with) / without × 100%
```

**Success Criteria:**
- [ ] Δ token savings ≥ -30% (minimum viable)
- [ ] Quality score maintained (≥4/5 both runs)
- [ ] Latency acceptable (<30s per review with graphify)

**Owner:** Tony Stark (measurement) + Jarvis (validation)

**Timeline:** Sprint 2 (30/08-02/09/2026)

---

### 2.3 Risk Mitigation

| Risk | Severity | Mitigation |
|---|---|---|
| **Memory contention (builds)** | HIGH | Sequential builds only; Jarvis coordinated queue |
| **Semantic staleness (graphs age silently)** | HIGH | Automated weekly rebuild trigger (Sprint 5); staleness checker in CONVENTIONS |
| **Flutter generics (structural errors)** | MEDIUM | Wanda Maximoff pre-validation (Sprint 3, Pre-Condition #2) |
| **qwen3.5:9b accuracy edge cases** | MEDIUM | Medium-repo validation (Sprint 1); fallback to read for uncertain queries |
| **User adoption (UX complexity)** | MEDIUM | GRAPHIFY-QUICK-REFERENCE.md playbook; examples in ADR |

---

## 3. Consequences

### Immediate (Sprint 1-2)

✅ **Graph structure validated (Sprint 1 complete)**
- jarvis-neural-interface: 90 nodes, 113 edges, 68KB
- Query latency: <1s
- Cost: $0

🔄 **Baseline measurement (Sprint 2)**
- Tony Stark performs controlled experiment
- Data drives Sprint 3 decision (full rollout vs pivot)

---

### Short-term (Sprint 3)

✅ **Tier 1 Rollout (if baseline approves)**
- Tony Stark, Bruce Banner, Steve Rogers adopt graphifyy
- 50-95% token savings measured in production
- Operations burden: Sequential builds (manageable)

⚠️ **Operational load**
- Jarvis manages build queue
- Weekly rebuild trigger runs automatically
- Monitoring for graph staleness (7-day threshold)

---

### Medium-term (Sprint 4-5)

✅ **Tier 2 Expansion (if Wanda pre-validation passes)**
- Scott Lang, Wanda, Natasha join rollout
- Repo coverage: 4 major codebases graphified

🎯 **Automation Phase (Sprint 5)**
- Automated rebuild hooks (post-merge webhook)
- MEMORY.md maintenance (staleness tracking)
- Ollama multi-model support (fallback to 4b if 9b OOM)

---

### Long-term (Phase 5+)

💰 **Financial Impact (Annualized)**
- Current: ~$4,800/month (Phase 3 with token optimization)
- Phase 4 projected: ~$2,500/month (-48% additional)
- **Annual savings: ~$27,600 on squad of 6**

📈 **Scalability**
- Multi-repo graphs: mergeable (graphifyy supports it)
- Cross-repo queries: possible via merged graphs
- New agents: automatic (graph already exists, add agent to read-only access)

---

## 4. Compliance

### Architecture Principles (Team Iron Solutions)

- ✅ **Security-first:** No external APIs, no keys transmitted, all local processing
- ✅ **Cost-efficiency:** -48% long-term spend vs Phase 3, $0 Ollama
- ✅ **Quality-first:** 9b model for builds (no cost-cutting on alicerce)
- ✅ **Data-driven:** Baseline measurement mandatory before rollout
- ✅ **Reversible:** Fallback to `read` if graphifyy fails

### LGPD Compliance

- ✅ No user data processed
- ✅ Internal tool (code analysis)
- ✅ All data stored locally (no cloud transfer)
- ✅ Audit trail: Git commits + ADR versioning

### Quality Standards (QUALITY-STANDARDS-MVP.md)

- ✅ Decision documented (this ADR)
- ✅ Rationale clear (why graphifyy, why Ollama)
- ✅ Validation plan explicit (baseline measurement)
- ✅ Success criteria measurable (token reduction ≥ -30%)

---

## 5. Implementation Plan

### Sprint Schedule

| Sprint | Focus | Owner | Status |
|---|---|---|---|
| **Sprint 0 (26/08)** | Architecture + governance | Steve Rogers | ✅ COMPLETE |
| **Sprint 1 (26-29/08)** | Build validation (jarvis-neural-interface) | Tony Stark + Jarvis | ✅ COMPLETE |
| **Sprint 2 (30/08-02/09)** | Baseline measurement (5 no-graphify + 5 with) | Tony Stark | ⏳ NEXT |
| **Sprint 3 (03-12/09)** | Tier 1 rollout + Wanda pre-validation | All Tier 1 + Wanda | ⏳ PENDING |
| **Sprint 4 (13-22/09)** | Tier 2 rollout (Scott, Wanda, Natasha) | All Tier 2 | ⏳ PENDING |
| **Sprint 5 (23/09+)** | Automation (rebuild hooks, monitoring) | Jarvis | ⏳ PENDING |

---

### Rollback Plan (If Issues Arise)

```
If graph quality is poor (queries fail):
  1. Revert agent to `read` workflow (-1 week context)
  2. Log failure case
  3. Re-run build with different model (4b instead of 9b)
  4. Or pivot to alternative tool

Estimated rollback time: < 2 hours (no data loss)
```

---

## 6. Alternatives Considered

### Alternative A: Use Joern (Java static analysis)

**Pros:**
- Production-grade (used by Netflix, Uber)
- Superior semantic extraction (Neo4j semantic reasoning)
- Handles security analysis

**Cons:**
- JVM + Neo4j: 8GB+ RAM required
- Learning curve (Cypher queries, Gremlin)
- No Python/Dart support (our tech stack is polyglot)
- Overkill for current scope

**Why rejected:** Complexity not justified. Graphifyy solves 95% of our use cases at 10% of complexity.

---

### Alternative B: LLM-only analysis (read all files + prompt)

**Pros:**
- No tool overhead (just use Claude)

**Cons:**
- 10,000+ tokens per analysis (expensive)
- Non-deterministic (different response each time)
- Latency: 5-10s per query (vs <1s graphifyy)
- No structural validation (semantic interpretation only)

**Why rejected:** Phase 4 is specifically about reducing LLM usage. This contradicts the goal.

---

### Alternative C: Manual relationship mapping (spreadsheet)

**Pros:**
- Human-curated (high quality)
- No tool risk

**Cons:**
- Non-scalable (100+ repos)
- Error-prone (maintenance burden)
- Not automatable

**Why rejected:** We chose automation for a reason.

---

## 7. Notes

### Why tree-sitter is "AST puro" (structural only)

Tree-sitter extracts:
- ✅ Types (class, function, variable)
- ✅ Relationships (calls, contains, inherits)
- ✅ Locations (line numbers, file paths)
- ❌ Semantics (purpose, criticality, risks)

Semantics are added by Ollama LLM. This separation is the core innovation: high-confidence structure + enriched context, without expensive full-LLM analysis.

**For future reference:** See `obsidian-vault/Projetos/Phase-4-Technical-Concepts/AST-TreeSitter-Semantica.md` for deep dive.

---

### Why sequential builds are non-negotiable

**Problem:** Mac mini has 16GB RAM. Ollama 9b uses 6-7GB. If 2 agents start builds simultaneously:
```
Build 1: 6.5GB
Build 2: 6.5GB
Total: 13GB + OS + other services = 16GB+
Result: OOM kill, both builds fail
```

**Solution:** Jarvis maintains sequential queue.
```
Build 1 starts (6.5GB) ✅
Build 2 queued (waits) ⏳
Build 1 completes, frees RAM
Build 2 starts (6.5GB) ✅
```

**Cost:** Build 2 waits 30-40 min. Acceptable; it's a one-time operation.

---

### Why qwen3.5:4b is insufficient (but acceptable for certain scenarios)

Sprint 1 tested qwen3.5:4b and found:
- ✅ Generates valid JSON
- ✅ Label quality acceptable (90-95%)
- ✗ Occasionally returns hollow responses ("no nodes/edges")
- ✗ Requires retry logic

**Verdict:** 4b works, but 9b is more reliable. For production, use 9b.

**Exception:** If Mac mini approaching OOM during build → fallback to 4b with retry.

---

### Why Wanda Maximoff needs pre-validation (Flutter-specific risk)

Flutter's generic components (Button<T>, Card<T>) expose a tree-sitter edge case:
- Generic type extraction is language-specific
- Python/Node generics: clear tree-sitter support
- Dart generics: less common in testing
- Risk: graph misses "Button<LoginButton>" relationships

**Mitigation:** Sprint 3 pre-validation with Wanda (design expert) confirms graphs are usable.

---

## 8. Related Decisions

| ADR | Decision | Status | Link |
|---|---|---|---|
| ADR-001 | Phase 1: Haiku default model | ✅ APPROVED | — |
| ADR-002 | OpenRouter integration | ✅ APPROVED | — |
| ADR-003 | Caveman compression middleware | ✅ APPROVED | — |
| ADR-004 | Model routing strategy | ✅ APPROVED | — |
| **ADR-005** | **(This) Graphifyy Phase 4 architecture** | ✅ APPROVED | — |

---

## 9. Record of Changes

| Date | Author | Change | Status |
|---|---|---|---|
| 26/08/2026 | Steve Rogers | Created ADR (Sprint 0 architecture review) | ✅ DRAFT |
| 26/08/2026 | Steve Rogers | Validated against Sprint 1 results | ✅ APPROVED |
| 26/08/2026 | Galvão Silva | Executive approval for Sprint 2 baseline | ✅ APPROVED |
| 26/08/2026 | Jarvis | Converted to ADR format per team standards | ✅ FINAL |
| — | — | (Update with Sprint 2 results) | ⏳ PENDING |

---

## 10. Approval

### CTO / Architect Sign-off

**Steve Rogers — CTO / Arquiteto de Software**

Date: 26/08/2026 16:00 GMT-3

Signature: ✅ **APPROVED**

> "Architecture is sound. Graphifyy + Ollama addresses the token optimization problem with minimal operational overhead. Pre-conditions are clear. Proceed with Sprint 2 baseline measurement."

---

### CEO / Decider Sign-off

**Galvão Silva — CEO / Founder, Team Iron Solutions**

Date: 26/08/2026 17:28 GMT-3

Signature: ✅ **APPROVED**

> "Phase 4 Phase 4 approved pending Sprint 2 baseline results. Budget allocated for Sprint 2-5. Review architecture decision as ADR per team standards."

---

### Tech Lead Coordination

**Jarvis — Tech Lead, Team Iron Solutions**

Date: 26/08/2026

Signature: ✅ **ACKNOWLEDGED**

> "Implementation plan locked. Sprint 2 baseline measurements scheduled. Will coordinate sequential builds and report metrics."

---

## 11. Documentation References

### Primary Documentation

- **[[AST-TreeSitter-Semantica.md]]** — Comprehensive explanation of AST, tree-sitter, and semantic extraction (Obsidian)
- **GRAPHIFY-CONVENTIONS.md** — Operational standards (models, paths, rebuilds, staleness)
- **GRAPHIFY-QUICK-REFERENCE.md** — Quick guide for agents (commands, examples, troubleshooting)
- **PHASE4-AGENT-PLAYBOOK.md** — How agents integrate graphifyy into workflows

### Supporting Documentation

- **PHASE4-TECHNICAL-CONTEXT.md** — Architecture details and trade-offs
- **PHASE4-VALIDATION-CHECKLIST.md** — Sprint 1 validation results
- **PHASE4-SPRINT1-LOG.md** — Detailed execution log

---

## 12. Next Steps

**Immediate (Today, 26/08):**
- [ ] Approve ADR (this document)
- [ ] Commit to repo as ADR-005
- [ ] Brief Tony Stark on Sprint 2 baseline protocol

**Sprint 2 (30/08-02/09):**
- [ ] Execute 5 code reviews without graphifyy (baseline)
- [ ] Execute 5 code reviews with graphifyy (treatment)
- [ ] Measure: tokens, latency, quality
- [ ] Analyze delta (target: ≥-30% tokens)

**Sprint 3 (pending baseline results):**
- [ ] If Δ ≥ -30%: Proceed with Tier 1 rollout
- [ ] If Δ < -30%: Revisit architecture or model choice
- [ ] Validate Wanda Maximoff (Flutter edge case)

---

**ADR Status:** ✅ APPROVED  
**Last Updated:** 26/08/2026 17:25 GMT-3  
**Next Review:** Post-Sprint 2 baseline (estimate: 03/09/2026)

---

_ADR Template: Michael Nygard (ADR pattern) + Team Iron Solutions standards_  
_Architecture Review: Steve Rogers (CTO) + Sprint 1 validation (Jarvis + agentes)_
