# 🔍 Git Audit — Cleanup Proposal

**Date:** 30/08/2026  
**Status:** AUDIT PHASE (awaiting approval)

---

## 📊 CATEGORIZAÇÃO DE ARQUIVOS EM `develop`

### ✅ CATEGORY A: DEVE FICAR (Core Infrastructure + Setup)

**Razão:** Necessário pra reproduzir ambiente em nova máquina

```
✅ AGENTS.md, SOUL.md, MEMORY.md, IDENTITY.md, USER.md, TOOLS.md, HEARTBEAT.md
   (Workspace core — define comportamento dos agentes)

✅ agents-workspaces/*/EXCELLENCE-PLAYBOOK.md
   (Playbooks de cada agente — parte da IaC)

✅ agents-workspaces/*/SOUL.md
   (Identidade de cada agente — parte da IaC)

✅ config/openclaw.template.json
   (Template de configuração — necessário pra setup)

✅ docs/
   (Deployment guides, setup instructions)

✅ scripts/setup-graphify.sh, setup.sh
   (Scripts de setup — necessários)

✅ CAVEMAN-INTEGRATION.md
   (Documentação Phase 3 — técnica)

✅ DEPLOYMENT-GUIDE-PHASE4-5.md
   (Novo — guia de deploy, necessário)

✅ GRAPHIFY-CONVENTIONS.md
   (Convenções técnicas — referência pra desenvolvimento)

✅ README.md
   (Entry point do repo)
```

**Total:** ~25 files (KEEP)

---

### ❌ CATEGORY B: NÃO DEVERIA ESTAR (Métricas + Relatórios + Gestão)

**Razão:** São artefatos operacionais, não IaC. Devem ir pra Obsidian ou serem deletados.

```
❌ PHASE4-SPRINT3-*-METRICS.json
   (Métricas de projeto específico — go to Obsidian)

❌ PHASE4-SPRINT3-*-REPORT.md
   (Relatórios detalhados — go to Obsidian)

❌ PHASE4-SPRINT3-*-EXECUTION-LOG.md
   (Logs de execução — go to Obsidian ou delete)

❌ PHASE4-SPRINT2-*.json, PHASE4-SPRINT2-*.md
   (Sprint histórico — go to Obsidian)

❌ AGENDA-GALVAO-*.md
   (Agenda pessoal — delete, já em Obsidian)

❌ PENDENCIAS-*.md
   (Gestão de tarefas — delete, já em MEMORY.md)

❌ memory/2026-08-*.md
   (Daily notes — personal, devem ser .gitignored)

❌ phase3-metrics/*.json
   (Histórico de métricas — go to .gitignored metrics/)

❌ monitoring-logs/*.json
   (Logs de monitoramento — go to .gitignored metrics/)

❌ openclaw-workspace-state.json
   (State file — delete, not reproducible)

❌ projects/wildream/*.md
   (Análise de projeto — go to Obsidian)

❌ .tmp/openclaw-spikes/*
   (Spike temporário — delete)

❌ PHASE4-*-STATUS.md, *-SUMMARY.md, *-CHECKLIST.md
   (Status operacional — go to Obsidian ou daily notes)

❌ PHASE4-PR-INSTRUCTIONS.md, DAY4-PR-INSTRUCTIONS.md
   (Instruções de operação — go to Obsidian)

❌ STEVE-ROGERS-PHASE4-*.md
   (Relatório específico — go to Obsidian)

❌ phase3-metrics-analyzer.py, phase3-summary.sh
   (Scripts de análise temporários — delete)

❌ monitoring-phase3-continuous.sh
   (Monitoramento histórico — delete)

❌ graphify-sprint1-test.sh
   (Script de teste temporário — delete)
```

**Total:** ~60+ files (DELETE or move to Obsidian)

---

### 🤔 CATEGORY C: INDEFINIDO (Necessita Sua Decisão)

**Razão:** Pode ser técnico (ficar) ou operacional (ir pra Obsidian)

```
🤔 GRAPHIFY-PHASE4.md
   (Overview técnico ou relatório? — IaC: SIM, Relatório: NÃO)

🤔 GRAPHIFY-QUICK-REFERENCE.md
   (Referência técnica ou cheat sheet? — IaC: SIM, Cheat: NÃO)

🤔 PHASE4-DOCUMENTATION-INDEX.md
   (Índice — útil pra novo dev? SIM, mas deve estar em docs/)

🤔 PHASE4-TECHNICAL-CONTEXT.md
   (Contexto técnico — útil pra entender Phase 4)

🤔 PHASE3-SPIKE-LOG.md
   (Spike descoberta — arquivo histórico)

🤔 RESEARCH-METHODOLOGY.md
   (Metodologia de research — útil pra futuro desenvolvimento?)

🤔 PHASE4-AGENT-PLAYBOOK.md
   (Playbook — já existe agents-workspaces/*/EXCELLENCE-PLAYBOOK.md?)

🤔 OLLAMA-GRAPHIFY-INTEGRATION.md
   (Integração técnica — pode ficar se for próximo passo)

🤔 obsidian-vault/Projetos/*.md
   (Arquivos do Obsidian que foram commitados — DEVE SER .GITIGNORED)
```

**Total:** ~10 files (decidir caso a caso)

---

## 📋 CLEANUP PLAN (Proposta)

### Phase 1: DELETE (Certo que não deveria estar)
```bash
# Spikes temporários
rm -rf .tmp/

# State files
rm openclaw-workspace-state.json

# Scripts temporários
rm phase3-metrics-analyzer.py phase3-summary.sh monitoring-phase3-continuous.sh graphify-sprint1-test.sh

# Agendas pessoais (já em Obsidian)
rm AGENDA-GALVAO-*.md

# Pendências (já em MEMORY.md)
rm PENDENCIAS-*.md
```

### Phase 2: MOVE TO OBSIDIAN (Via Obsidian sync, depois commit delete)
```bash
# Métricas (já organized em Obsidian/Projetos/Graphify-Phase4/)
rm -rf PHASE4-SPRINT3-*-METRICS.json
rm -rf PHASE4-SPRINT3-*-REPORT.md
rm -rf PHASE4-SPRINT2-*

# Daily notes (pessoais)
rm -rf memory/2026-08-*.md

# Histórico de métricas
rm -rf phase3-metrics/
rm -rf monitoring-logs/

# Análise Wildream (já em Obsidian)
rm -rf projects/wildream/
```

### Phase 3: .GITIGNORE (Nunca mais committem)
```gitignore
# Daily notes
memory/

# Métricas e logs
metrics/
phase3-metrics/
monitoring-logs/
*.metrics.json

# Estado operacional
*.state.json
*.log

# Obsidian (wiki pessoal)
obsidian-vault/

# Spikes temporários
.tmp/

# Relatórios operacionais
AGENDA-*.md
PENDENCIAS-*.md
*-SUMMARY.md
*-STATUS.md (exceto docs/)
```

### Phase 4: REVIEW (Casos indefinidos — sua decisão)
```
🤔 GRAPHIFY-*.md (2-3 files)
🤔 PHASE4-TECHNICAL-CONTEXT.md
🤔 PHASE4-DOCUMENTATION-INDEX.md
🤔 OLLAMA-GRAPHIFY-INTEGRATION.md
```

---

## 📊 IMPACTO

**Antes:** 150+ files (muito lixo)  
**Depois:** ~50 files (only IaC + setup guides)  
**Reduction:** -66% (files), -80% (noise)

**Result:**
- Claro o que é "infrastructure as code"
- Novo dev não se perde em 150 arquivos
- Repo é reproducible de verdade
- Obsidian é a single source of truth pra documentação/aprendizado

---

## ✅ PRÓXIMOS PASSOS

**Você decide:**

**OPÇÃO A:** Execute tudo (delete + move + gitignore)
**OPÇÃO B:** Execute Phase 1+3 apenas (delete + gitignore, keep reports pra agora)
**OPÇÃO C:** Execute Phase 1+3, depois revise Phase 4 manualmente

**Tempo:**
- A: 10 minutos
- B: 5 minutos
- C: 15 minutos

---

**Qual você quer?** (Espero sua resposta dessa vez. 🙏)
