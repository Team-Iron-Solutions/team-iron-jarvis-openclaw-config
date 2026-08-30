# Phase 4 Sprint 3 — Natasha Tier 2 Setup

## Test Suite Inventory & Selection

### OpenJarvis Test Structure (47 modules)
```
tests/
├── agents/          (50+ files) → Complex agent orchestration
├── channels/        (35+ files) → Multi-channel integration  
├── connectors/      (45+ files) → Protocol/API connectors
├── core/            (20+ files) → Core engine tests
├── engine/          (27+ files) → Execution engine
├── evals/           (35+ files) → Evaluation & metrics
├── integration/     (6+ files)  → Cross-module integration
├── learning/        (35+ files) → ML/learning pipeline
├── mcp/             (13+ files) → Protocol implementation
├── memory/          (17+ files) → State management
├── security/        (22+ files) → Auth/security
├── server/          (32+ files) → API server
└── ... 35 more
```

### Claw3D Test Structure
```
tests/
├── unit/            (174+ files) → Unit test suites
├── e2e/             (12+ files)  → End-to-end tests
└── fixtures/        → Test data
```

---

## **10 Test Suite Reviews — Natasha's Selection**

| # | Test Suite | Framework | Complexity | Focus Area | LOC |
|---|-----------|-----------|-----------|-----------|-----|
| 1 | agents/* | pytest | HARD | Multi-agent orchestration | 5000+ |
| 2 | channels/* | pytest | HARD | Channel integration patterns | 4000+ |
| 3 | connectors/* | pytest | MEDIUM | Protocol connectors | 4500+ |
| 4 | core/* | pytest | MEDIUM | Core engine coverage | 2000+ |
| 5 | integration/* | pytest | MEDIUM | Cross-module integration | 2000+ |
| 6 | security/* | pytest | HARD | Security/auth testing | 2500+ |
| 7 | Claw3D/tests/unit/* | vitest | MEDIUM | Frontend unit tests | 3000+ |
| 8 | Claw3D/tests/e2e/* | vitest | MEDIUM | E2E test patterns | 1500+ |
| 9 | conftest.py + fixtures | pytest | HARD | Test infra & fixtures | 1000+ |
| 10 | memory/* | pytest | MEDIUM | State/memory tests | 2000+ |

**Total Test LOC:** ~27,500 lines  
**Mix:** 4 HARD, 6 MEDIUM (good for Tier 2 validation)

---

## Execution Plan

### Phase 1: Build Knowledge Graphs
- Graph: OpenJarvis tests/ directory
- Graph: Claw3D tests/ directory
- Estimated time: 20-30 min per graph

### Phase 2: Execute 10 Reviews
- Baseline (without graphify): read full test files, measure tokens
- With Graphify: query graphs, measure compression
- Per review: ~3-5 min

### Phase 3: Collect Metrics
- Token compression (input + output)
- Latency (ms)
- Quality score (1-5 scale based on insight depth)
- Issues found (coverage gaps, anti-patterns)

### Phase 4: Report
- JSON metrics (format matching Bruce/Steve)
- Markdown analysis + recommendations
- Success criteria check: -35% compression, 4.5/5 quality

---

## Success Criteria

✅ Compression ≥ -35%  
✅ Quality ≥ 4.5/5  
✅ Zero critical bugs in analysis  
✅ Latency < 10s per review

**Timeline:** 30/08 (setup) - 31/08 (execution) - 02/09 (report)

