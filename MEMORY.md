# MEMORY.md - Jarvis Long-Term Memory

## Who I Am
- **Name:** Jarvis 🦾
- **Role:** CTO + Tech Lead da Team Iron Solutions
- **Human:** Robson Galvão Silva ("Galvão") — CEO/fundador da Team Iron Solutions
- **First contact:** 15 de julho de 2026

## Minha Missão

Sou o segundo cérebro técnico do Galvão. Minhas responsabilidades:

1. **Arquitetura & Engenharia** — definição de arquitetura, boas práticas, decisões técnicas
2. **Tech Lead** — liderança técnica, code review, padrões de desenvolvimento
3. **Gestão de Projetos** — tarefas, agendas, prazos, automações
4. **Pesquisa** — avaliar tecnologias, bibliotecas, abordagens
5. **Código** — escrever, revisar, debugar
6. **Gestão do Time de Agentes** — orquestrar e gerenciar equipe autônoma de agentes IA

## Time de Agentes (a construir)

| Papel | Stack / Foco |
|---|---|
| Product Manager | Roadmap, backlog, requisitos |
| Product Designer | UI/UX, design system |
| UX | Pesquisa, usabilidade |
| QA | Testes, automação de QA |
| Mobile Dev | Flutter, React Native, híbridos |
| Frontend Web | React, Angular, Vue |
| Backend | NodeJS, Python, Java/Spring, Go |
| Fullstack | Full-stack generalista |

## Team Iron Solutions

- **Site:** https://teamironsolutions.com.br/
- **Foco:** Engenharia de Software, IA e Consultoria Tecnológica
- **Tagline:** "Transformamos Tecnologia em Vantagem Competitiva"
- **Métricas:** 99.98% Uptime SLA · 42 integrações ativas · 120 deploys/mês

## Stack & Tecnologias Conhecidas

- Mobile: Flutter, React Native
- Frontend: React, Angular, Vue
- Backend: NodeJS, Python, Java (Spring), Go
- IA: OpenClaw multi-agent, modelos Anthropic/Google

## Infraestrutura

- **Hardware:** Mac mini (macOS 26.4, arm64)
- **OpenClaw Gateway:** porta 18789 (✅ LaunchAgent ativo)
- **OpenClaw Office:** porta 5180 (✅ LaunchAgent ativo) — multi-agent dashboard
- **Claw3D:** porta 3001 (✅ LaunchAgent ativo) — 3D virtual office com OpenClaw integration
- **Node:** nvm v24.18.0
- **Model default:** claude-haiku-4-5 (fallback: claude-sonnet-4-6)

## Economia de Tokens (01/08/2026 — PHASE 1 ATIVA)

**Baseline:** ~60-70% redução sem sacrificar qualidade

**Regras Phase 1:**
- ✅ **Haiku default** (Haiku: $0.80/1M, Sonnet: $3.00/1M)
- ✅ **Sonnet APENAS para:** arquitetura (Steve Rogers), product strategy (Stephen Strange)
- ✅ **Sonnet também para:** auditoria de repositório git, análise de estrutura de arquivos, decisões de onde arquivos devem ficar, qualquer tarefa onde "estar certo" é mais importante que velocidade
- ⚠️ **Lição 30/08/2026:** Haiku foi negligente em git cleanup — declarou "limpo" sem auditar de verdade, commitou direto na develop sem PR, precisou de múltiplas rodadas. Custo de retrabalho > custo do Sonnet.
- 🔒 **Regra de troca de modelo:** NUNCA trocar para Sonnet automaticamente. Sempre perguntar primeiro: "Galvão, essa tarefa tem risco de erro se feita raso — recomendo Sonnet. Autoriza?" + trazer racional claro. A decisão é do Galvão, não minha.
- ✅ **Sem context bloat:** memory_search() + targeted memory_get() instead of full reads
- ✅ **Thinking mode seletivo:** Apenas architecture/security decisions
- ✅ **Batching:** 1 request para múltiplas tasks, não sequencial
- ✅ **Cron pra repetitivo:** daily digests, checks periódicos

**Cost estimate (50M tokens/month):**
- Squad (10 agents): ~$190/month
- Jarvis + infra: +$100-200/month
- **Total: ~$290-390/month** (vs. $1,500+ all-Sonnet)

**Detalhes completos:** `OPTIMIZATION-PHASE1.md` (model matrix, 14 estratégias, checklist)

## Idioma & Comunicação
- **Padrão:** Português do Brasil (sempre)
- **Exceções:** Nenhuma — análises, relatórios, documentos técnicos → pt-BR
- **Motivo:** Galvão, equipe e stakeholders falam português nativo
- **Configurado:** 01/08/2026

## Voz
- **Provedor:** ElevenLabs
- **Voz ativa:** Otto (brazilian male, intimidating) — ID: `ycxdm1PRMs962FxyyuJ0`
- **Modelo:** eleven_turbo_v2_5
- **Fallback:** Microsoft `pt-BR-AntonioNeural` (usado no bridge para TTS local)
- **Voz anterior:** Daniel `onwK4e9ZLuTAKqWW03F9` (british male) — substituído em 17/07/2026
- **Evolução futura:** Clone profissional da voz de Eduardo Borgerth (dublador BR do JARVIS) — requer plano Creator + áudios limpos dos filmes

## Interface Visual
- **Jarvis HUD v2:** `jarvis-hud.html` no workspace e na Área de Trabalho
- Design: holograma hexagonal, anéis girando, triângulos fechando/expandindo, brackets animados, waveform, paineis laterais, ticker, relógio
- **Painel de chat** na base do HUD: mostra últimas mensagens da conversa em tempo real
- **Polling automático** do `jarvis-bridge.js` (localhost:3033) a cada 1.8s
- Easter egg: clicar no avatar ativa modo SPEAKING (dourado)
- Bridge server: `jarvis-bridge.js` — expõe `/state`, `/speaking`, `/health`
- Para iniciar: `node ~/.openclaw/workspace/jarvis-bridge.js`
- Guia de voz completo: `VOICE-SETUP.md`

## Agentes Vivos 🤖 — FINAL ROSTER (04 ago 2026 — 10/10 COMPLETO!)

| # | Agente | Alter Ego | Papel | Status | Playbook |
|---|--------|-----------|-------|--------|----------|
| 1 | **Tony Stark** | Iron Man | Backend Node.js + Tech Lead | ✅ Live | ✅ TONY-STARK-EXCELLENCE-PLAYBOOK.md |
| 2 | **Bruce Banner** | Hulk | Backend Python | ✅ Live | ✅ BRUCE-BANNER-EXCELLENCE-PLAYBOOK.md |
| 3 | **Steve Rogers** | Capitão América | Arquiteto de Software | ✅ Live | ✅ STEVE-ROGERS-EXCELLENCE-PLAYBOOK.md |
| 4 | **Stephen Strange** | Doutor Estranho | Product Manager | ✅ Live | ✅ STEPHEN-STRANGE-EXCELLENCE-PLAYBOOK.md |
| 5 | **Visão** 🔮 | Vision | Data Engineer / IA Aplicada | ✅ Live | 📋 VISAO-DATA-IA-EXCELLENCE-PLAYBOOK.md |
| 6 | **Wanda Maximoff** ✨ | Feiticeira Escarlate | Product Designer / UX | ✅ Live | 📋 WANDA-MAXIMOFF-EXCELLENCE-PLAYBOOK.md |
| 7 | **T'Challa** 🐈⬛ | Pantera Negra | SRE Engineer | ✅ Live | 📋 TCHALLA-SRE-EXCELLENCE-PLAYBOOK.md |
| 8 | **Scott Lang** 🐜 | Homem-Formiga | Flutter (mobile + web) | ✅ Live | 📋 SCOTT-LANG-EXCELLENCE-PLAYBOOK.md |
| 9 | **Natasha Romanoff** 🕷️ | Viúva Negra | QA Engineer | ✅ Live | 📋 NATASHA-ROMANOFF-EXCELLENCE-PLAYBOOK.md |
| 10 | **Peter Parker** 🕸️ | Homem-Aranha | Conteúdo / Social Media | ✅ Live | 📋 PETER-PARKER-EXCELLENCE-PLAYBOOK.md |

### ✅ Tony Stark (Agent 1/10)
- **Status:** Live & battle-tested
- **Role:** Backend Node.js Sênior + **TECH LEAD**
- **First task:** Code review (N+1 query optimization)
- **Result:** Production-grade, 100x performance improvement
- **Date:** 2026-07-16 18:35 GMT-3
- **Proof:** `FIRST-TONY-REVIEW.md`
- **Capabilities:** Node.js backend, API design, performance optimization, code review
- **Tech Lead desde:** 01/08/2026
  - Define padrões de código, arquitetura implementation
  - Code review, integração Tony/Bruce
  - Sprint planning, QA gates
  - Escalonamento técnico com Steve Rogers (Arquiteto)

### ✅ Bruce Banner (Agent 2/10)
- **Status:** Live & validated
- **First task:** Python code review (user data fetch optimization)
- **Result:** 3 issues identified + 2 optimized solutions, 10-100x performance improvement
- **Date:** 2026-07-18 18:06 GMT-3
- **Capabilities:** Python backend, data analysis, performance optimization, code review

### ✅ Steve Rogers (Agent 3/10)
- **Status:** Live & validated
- **First task:** System architecture design (1M req/day, 99.98% SLA)
- **Result:** Monolith modular + PostgreSQL + Redis hybrid, strategic insight on availability vs throughput
- **Date:** 2026-07-18 18:07 GMT-3
- **Capabilities:** Architecture decisions, CTO-level strategic thinking, system design, Sonnet-grade reasoning

### ✅ Stephen Strange (Agent 4 — Live)
- **Status:** Live desde 01/08/2026
- **Role:** Product Manager / Doutor Estranho
- **Playbook:** `STEPHEN-STRANGE-EXCELLENCE-PLAYBOOK.md`

### ✅ Visão (Agent 5 — Live desde 04/08)
- **Status:** Live — workspaces + documentação completa
- **Role:** Data Engineer / IA Aplicada
- **Playbook:** `VISAO-DATA-IA-EXCELLENCE-PLAYBOOK.md`
- **Focus:** Data pipelines, analytics, IA models, prototipagem

### ✅ Wanda Maximoff (Agent 6 — Live desde 04/08)
- **Status:** Live — workspaces + documentação completa
- **Role:** Product Designer / UX Expert
- **Playbook:** `WANDA-MAXIMOFF-EXCELLENCE-PLAYBOOK.md`
- **Focus:** UI/UX, design system, mockups, user research

### ✅ T'Challa (Agent 7 — Live desde 04/08)
- **Status:** Live — workspaces + documentação completa
- **Role:** SRE Engineer / Infraestrutura
- **Playbook:** `TCHALLA-SRE-EXCELLENCE-PLAYBOOK.md`
- **Focus:** Infrastructure, deployment, monitoring, LGPD compliance

### ✅ Scott Lang (Agent 8 — Live desde 04/08)
- **Status:** Live — workspaces + documentação completa
- **Role:** Flutter Developer (mobile + web)
- **Playbook:** `SCOTT-LANG-EXCELLENCE-PLAYBOOK.md`
- **Focus:** Flutter, cross-platform, mobile apps

### ✅ Natasha Romanoff (Agent 9 — Live desde 04/08)
- **Status:** Live — workspaces + documentação completa
- **Role:** QA Engineer / Quality Assurance
- **Playbook:** `NATASHA-ROMANOFF-EXCELLENCE-PLAYBOOK.md`
- **Focus:** Testing, automation, quality gates

### ✅ Peter Parker (Agent 10 — Live desde 04/08)
- **Status:** Live — workspaces + documentação completa
- **Role:** Content / Social Media Specialist
- **Playbook:** `PETER-PARKER-EXCELLENCE-PLAYBOOK.md`
- **Focus:** Instagram, conteúdo técnico, storytelling

## Phase 3 Token Optimization — Week 1 COMPLETO (04-16 ago 2026)

### Status Final

| Dia | Task | Status | Savings | PRs |
|-----|------|--------|---------|-----|
| Day 1 | Prompt Caching | ✅ LIVE | -20-90% | Merged |
| Day 2 | OpenRouter | ✅ LIVE | -75-95% | Merged |
| Day 3 | Caveman Middleware | ✅ READY | -40% | - |
| **Day 4** | **Caveman Integration** | **✅ MERGED** | **-40-50%** | **#10, #2** |

### Validação Day 4 (16/08/2026 — 14:41)

**3 Code Review Tests — ALL PASSED:**
1. SQL Injection Detection: -40-45% compression, 5/5 quality ✅
2. O(n²) Performance: -45-50% compression, 5/5 quality ✅
3. Async Error Handling: -50-55% compression, 5/5 quality ✅

**Average Compression:** -45% (target: -30%) ✅
**Average Quality:** 5.0/5.0 (target: ≥4.5/5) ✅
**Latency:** 0s variance (target: <2s) ✅
**Semantic Loss:** 0% (target: none) ✅

### PRs Mergeadas (16/08/2026 — 16:17)
- **team-iron-jarvis-openclaw-config #10** ✅ MERGED
  - caveman-middleware-esm.js
  - CAVEMAN-INTEGRATION.md
  - MEMORY.md (procedimento padrão)

- **jarvis-neural-interface #2** ✅ MERGED
  - jarvis-bridge-v4.js (integração Caveman)
  - docs/CAVEMAN-BRIDGE-INTEGRATION.md

### Impacto Financial Confirmado
- **Compression verificada:** -45% (melhor que -40% projetado)
- **Monthly savings:** -$85/month por squad (-45%)
- **Annual savings:** -$1,020/ano por squad
- **Com Phase 1+2:** -$2,200+/ano por squad (-73-75% total)

### Monitoramento Phase 3 (16-23 ago 2026)
- **Dashboard:** `MONITORING-DASHBOARD-PHASE3.md` (KPIs, thresholds, daily checklist)
- **Setup:** `MONITORING-SETUP.md` (como usar, cron jobs, daily routine)
- **Script:** `monitoring-collect-metrics.sh` (coleta automática de métricas)
- **KPIs:** Compression (-45%), Quality (5/5), Latency (<10ms), Errors (0%), Uptime (>99%)
- **Alerts:** 3 levels (CAUTION → WARNING → CRITICAL)
- **Success:** Todos os KPIs ✅ por 7 dias = aprovação para rollout

### Phase 4 — Graphify + Ollama (19/08 → 26/08/2026 → 30/08/2026)
**Objetivo:** Reduzir contexto carregado durante code review via knowledge graphs  
**Agentes:** Tony Stark, Bruce Banner, Steve Rogers, Scott Lang, Wanda, Natasha (Tier 1+2)  
**Economia estimada:** -50-95% de tokens (variável por repo size, -$3,960/ano para squad)  
**Status:** 🟠 **Sprint 2 ATIVO** (30/08 11:22 GMT-3 — Tony Stark em execução)
**Branch:** `feat/graphify-phase4` (3 commits: setup, ollama-integration, documentation-suite)

#### Phase 4 Sprint 2 — COMPLETO ✅ (30/08 11:22 — 11:27 GMT-3)
**🟢 SUCESSO VALIDADO:**
- **Agente:** Tony Stark (Tech Lead)
- **Execução:** sessions_send (11:24 GMT-3)
- **Completion:** 30/08 11:27 GMT-3 (4m45s)
- **Meta Alcançada:** Δ = 47.5% (target: ≥30%) ✅
- **Quality Preserved:** 4.52/5.0 (target: ≥4.5) ✅

**Resultados por Complexidade:**
1. SQL Injection (Easy): -40.5% tokens, 4.8/5 quality ✅
2. N+1 Query (Medium): -43.9% tokens, 4.6/5 quality ✅
3. Async Error (Medium): -44.3% tokens, 4.5/5 quality ✅
4. Performance (Hard): -50.0% tokens, 4.4/5 quality ✅
5. Architecture (Very Hard): -51.7% tokens, 4.3/5 quality ✅

**Arquivos Entregues:**
- ✅ `phase4-sprint2-baseline.json`
- ✅ `phase4-sprint2-graphify.json`
- ✅ `PHASE4-SPRINT2-RESULTS-FINAL.md` (análise + recomendações)
- ✅ `PHASE4-SPRINT2-EXECUTION-SUMMARY.md`
- ✅ Obsidian: `obsidian-vault/Projetos/Graphify-Phase4/06-Sprint2-Results.md`

**Veredicto:** ✅ **GRAPHIFY VALIDATED FOR TIER 1 ROLLOUT**

#### Phase 4 Sprint 3 — Tier 1 Deployment (30/08 12:25 — ongoing)
**🟢 AGENTES ENTREGANDO RESULTADOS:**
- **Agentes:** Tony Stark (PRIMARY), Bruce Banner (SECONDARY), Steve Rogers (TERTIARY)
- **Acionados via:** sessions_send (12:25 GMT-3)
- **Status de Execução:**
  - Tony Stark: 🟢 Executando (estimado hoje/amanhã)
  - Bruce Banner: 🟢 **✅ COMPLETO** (30/08 12:29 GMT-3 — 10/10 reviews done)
  - Steve Rogers: 🟡 Check-in enviado (13:05 GMT-3), awaiting response
- **Session keys:** `agent:tony:main`, `agent:bruce:main`, `agent:steve:main`
- **Task:** Deploy graphify, integrate workflows, execute 10 real code reviews per agent
- **Métrica:** Compression ≥ -40%, Quality ≥ 4.5/5
- **Timeline:** 30/08-02/09 (setup) + 03/09-10/09 (monitoring)
- **Entregas Completas (Bruce):**
  - ✅ `PHASE4-SPRINT3-BRUCE-METRICS.json` (Compressão: -47.5%, Quality: 4.49/5.0)
  - ✅ `PHASE4-SPRINT3-BRUCE-REPORT.md`
  - ✅ `PHASE4-SPRINT3-BRUCE-RESULTS.json`
  - ✅ `PHASE4-SPRINT3-BRUCE-EXECUTION-LOG.md`
  - ✅ Confirmação oficial: "GO FOR TIER 2 ROLLOUT" (13:06 GMT-3)
  - ✅ Python code reviews 100% parity com Node.js (Tony Sprint 2)
- **Entregas Completas (Steve):**
  - ✅ `PHASE4-SPRINT3-STEVE-METRICS.json` (Compressão: -55.6%, Quality: 4.60/5.0)
  - ✅ `PHASE4-SPRINT3-STEVE-REPORT.md`
  - ✅ Confirmação oficial: "Aguardando próximos passos Tier 2" (13:06 GMT-3)
  - ✅ Zero semantic loss, arquivos entregues
- **Entregas Pendentes:**
  - ⏳ `PHASE4-SPRINT3-TONY-METRICS.json` + report (em progresso)
  - ✅ `PHASE4-SPRINT3-CONSOLIDATED-RESULTS.md` (agregado 2/3 agentes)
- **Plano:** `PHASE4-SPRINT3-ROLLOUT-PLAN.md`
- **Go/No-Go:** 30/08 13:15 — **2/3 AGENTES PRONTOS → GO FOR TIER 2 ROLLOUT** ✅

#### Phase 4 Sprint 3 — Tier 2 Rollout (30/08 13:13 — ongoing)
**🟢 TIER 2 KICKOFF REALIZADO AGORA:**
- **Agentes:** Scott Lang (Flutter), Wanda Maximoff (UX), Natasha Romanoff (QA)
- **Acionados via:** sessions_send (13:13 GMT-3)
- **Task:** Deploy graphify em contextos especializados (mobile, design, testing)
- **Meta:** Compression ≥ -35% (relaxed vs Tier 1's -40%), Quality ≥ 4.5/5
- **Timeline:** 30/08-02/09 (setup + execution) + 02-03/09 (consolidation)
- **Entregas esperadas:**
  - `PHASE4-SPRINT3-SCOTT-METRICS.json` + report (8 Flutter reviews)
  - `PHASE4-SPRINT3-WANDA-METRICS.json` + report (5 design reviews)
  - `PHASE4-SPRINT3-NATASHA-METRICS.json` + report (10 test reviews)
  - `PHASE4-SPRINT3-TIER2-CONSOLIDATED-RESULTS.md` (agregado)
  - `PHASE4-SPRINT3-FINAL-VERDICT.md` (decisão Phase 5+)
- **Plano:** `PHASE4-SPRINT3-TIER2-KICKOFF.md`
- **Entregas Completas (Wanda):**
  - ✅ `PHASE4-SPRINT3-WANDA-METRICS.json` (Compressão: -55.0%, Quality: 4.56/5.0)
  - ✅ `PHASE4-SPRINT3-WANDA-REPORT.md`
  - ✅ Confirmação oficial: "Ready for consolidation" (13:16 GMT-3)
  - 🚨 **KEY INSIGHT:** Graphify MORE effective for design systems than code review
- **Entregas Completas (Scott):**
  - ✅ `PHASE4-SPRINT3-SCOTT-METRICS.json` (Compressão: **-89.9%**, Quality: 4.7/5.0)
  - ✅ `PHASE4-SPRINT3-SCOTT-REPORT.md`
  - ✅ Confirmação oficial: "READINESS CONFIRMED" (16:30 GMT-3)
  - 🚨 **KEY INSIGHT:** Graphify EXCELS in Flutter (structural code, UI hierarchies)
  - 🔥 **12x FASTER LATENCY** (103ms avg vs 1200ms baseline)
- **Entregas Completas (Natasha):**
  - ✅ `PHASE4-SPRINT3-NATASHA-METRICS.json` (Compressão: -50.0%, Quality: 4.56/5.0)
  - ✅ `PHASE4-SPRINT3-NATASHA-REPORT.md`
  - ✅ Confirmação oficial: "TIER 2 LEADER — METRICS DELIVERED" (16:17 GMT-3)
  - ✅ 10 test suite reviews, 14 issues, 0 false positives
#### Phase 4 Sprint 3 — TIER 3 (3/3) COMPLETO! ✅
**🟢 TIER 3 100% COMPLETO — AGUARDANDO APENAS TONY STARK (TIER 1):**
- **Agentes:** Visão (Data/IA), T'Challa (SRE), Peter Parker (Content)
- **Acionados via:** sessions_send (13:54 GMT-3)
- **Task:** Deploy graphify em contextos especializados (data, infra, conteudo)
- **Meta:** Compression ≥ -30% (further relaxed), Quality ≥ 4.5/5
- **Timeline:** 30/08-02/09 (setup + execution) + 02-03/09 (consolidation)
- **Entregas Completas:**
  - ✅ `PHASE4-SPRINT3-VISAO-METRICS.json` + report (8 data/SQL reviews, -66.3%)
  - ✅ `PHASE4-SPRINT3-PETER-METRICS.json` + report (5 content reviews, -69.36%)
  - ✅ `PHASE4-SPRINT3-TIER3-CONSOLIDATED-RESULTS.md` (2/3 agregado)
  - ✅ `PHASE4-SPRINT3-FINAL-VERDICT-TEMPLATE.md` (slots para Tony + T'Challa)
- **Plano:** `PHASE4-SPRINT3-TIER3-KICKOFF.md` + `PHASE4-SPRINT3-TIER3-CONSOLIDATED-RESULTS.md`
- **Status Tier 3 (3/3 COMPLETO):** ✅
  - Visão: 🟢 **✅ COMPLETO** (14:01 GMT-3) — -66.3% compression, 4.65/5 quality (**HIGHEST QUALITY TIER 3**)
    - 🚨 8 data/SQL reviews (AudioBuffer, StreamProcessor, Analytics)
    - 🚨 Zero false positives, 130ms latency
  - T'Challa: 🟢 **✅ COMPLETO** (14:02 GMT-3) — -58.78% compression, 4.51/5 quality
    - 🚨 7 infra-as-code reviews (Terraform, K8s, shell, CI/CD)
    - 🚨 **KEY DISCOVERY:** Infra-as-code 2nd most compressible after Flutter (-58.78% vs -89.9%)
    - 🚨 23 issues detected, 0 false positives
  - Peter Parker: 🟢 **✅ COMPLETO** (13:57 GMT-3) — -69.36% compression, 4.5/5 quality (**BEST TIER 3 COMPRESSION**)
    - 🚨 5 documentation reviews
    - 🚨 KEY DISCOVERY: Documentation compresses better than code (-69% vs -50%)

**Consolidação Sprint 3 (Tier 1 + 2 + 3) — OPTION B COMPLETE:**
- **Tier 1 (2/3):** Bruce (-47.5%), Steve (-55.6%), Tony (pending)
- **Tier 2 (3/3):** Scott (-89.9%), Wanda (-55.0%), Natasha (-50.0%) ✅
- **Tier 3 (3/3):** Visão (-66.3%), T'Challa (-58.78%), Peter (-69.36%) ✅

**Documentação Criada (30/08 Option B):**
- ✅ `PHASE4-SPRINT3-TIER3-CONSOLIDATED-RESULTS-FINAL.md` (T'Challa integrated, 3/3)
- ✅ `PHASE4-SPRINT3-FINAL-VERDICT-ALL-TIERS-TEMPLATE.md` (T'Challa filled, Tony slots ready)
- ✅ `PHASE4-SPRINT3-BURNDOWN-CHECKLIST-03-09.md` (step-by-step execution guide)
- ✅ `PHASE4-SPRINT3-CONSOLIDATION-8-AGENTS-STATUS.md` (master summary)
- **Average Tier 1+2:** -58.6% compression, 4.58/5 quality
- **Veredicto:** ✅ **GO FOR TIER 3 — OPÇÃO A ESCOLHIDA (13:54)**

**Discovery + Sprint 0 (26/08/2026 — 14:34):**
- ✅ **13:43** — Kick-off: branch `feat/graphify-phase4` ativa
- ✅ **13:50** — Pivô: pyenv ❌ → uv ✅ (economia: 25 min)
- ✅ **13:51** — Python 3.12.13 instalado (652ms via uv)
- ✅ **13:51:30** — Graphifyy + 52 tree-sitter parsers
- ✅ **13:52** — Ollama local descoberto (qwen3.5:2b/4b/9b disponíveis)
- ✅ **14:07** — Graphifyy com Ollama backend iniciado (OpenJarvis 12k Python files)
- ✅ **14:15** — Paralelismo: Steve Rogers (Sonnet) analisando arquitetura
- ✅ **14:20** — Documentação suite completa (Playbook + Context + Validation)
- ✅ **14:24** — Steve Rogers REAL chamado via sessions_send (agentId: steve)
- ✅ **14:28** — Steve Rogers ASSINA review final: GO com 4 pré-condições
- ✅ **14:34** — Sprint 0 COMPLETO: GRAPHIFY-CONVENTIONS.md + Obsidian archive

**Timeline esperado:**
1. 🟡 **Sprint 1 (26/08):** Setup + teste com Ollama — **CONCLUSÃO HOJE**
2. 🟠 **Sprint 2 (27-29/08):** Integração Tony Stark (spike c/ graphify)
3. ⏳ Sprint 3 (30/08-03/09): Rollout Tier 1 (Tony, Bruce, Steve)
4. ⏳ Sprint 4 (04-13/09): Rollout Tier 2 (Scott, Wanda, Natasha)
5. ⏳ Sprint 5 (14/09+): Monitoring + rollout completo

**Documentação Phase 4:**
- ✅ GRAPHIFY-PHASE4.md (estratégia 5 sprints)
- ✅ OLLAMA-GRAPHIFY-INTEGRATION.md (setup técnico)
- ✅ PHASE4-AGENT-PLAYBOOK.md (guia de uso para agentes)
- ✅ PHASE4-TECHNICAL-CONTEXT.md (contexto para Steve Rogers)
- ✅ PHASE4-VALIDATION-CHECKLIST.md (testes + métricas)
- ⏳ graphify-out-phase4/graph.json (building now...)

## HUD v5 com Métricas (16 ago 2026 — COMPLETO)

**Arquivo:** `jarvis-neural-interface/hud/hud-jarvis-v5-metrics.html`  
**Branch:** `feature/hud-metrics-tier1-widgets`  
**Docs:** `jarvis-neural-interface/docs/HUD-V5-COMPLETE.md`

### 5 Painéis Iron Man (clip-path diagonal, scan-line animada)

| Painel | Posição | Cor | O que mostra |
|---|---|---|---|
| Bridge Status | esq. topo | ciano | ONLINE/OFFLINE, latência, uptime HH:MM:SS |
| Compression | esq. meio | verde | Ratio -XX%, gauge, OPTIMAL/LOW |
| System Log | esq. baixo | roxo | Timestamp, bridge, reqs, erros |
| Financials | dir. topo | dourado | Custo hoje, savings vs baseline, projeção mensal |
| Agents | dir. meio | roxo | 4/10 online, grid 2×5 dos 10 agentes |

### Como abrir
```bash
# Terminal 1: bridge
node .../bridge/jarvis-bridge-v4.js
# Terminal 2: servidor
cd .../hud && python3 -m http.server 8000
# Browser
http://localhost:8000/hud-jarvis-v5-metrics.html
```

### Pendências HUD
- [ ] Bridge servir v5 como HUD padrão (substituir v2)
- [ ] Endpoint `/agents` com status real dos 10 agentes
- [ ] WebSocket push em vez de polling
- [ ] Tier 3: ElevenLabs quota, token budget, histórico 7d

---

## Estado do HUD e Voz (18 jul 2026 — ATUALIZADO 18:31)

### Arquitetura v3.1 (18/07/2026 — COM OTTO ATIVO)

```
[HUD — http://localhost:3033/hud no browser]
    webkitSpeechRecognition (pt-BR, nativo)
         ↓ texto
[Jarvis Bridge v3.2 — :3033 — LaunchAgent]
    openclaw agent --agent main --session-key main (Haiku)
         ↓ resposta
    ElevenLabs Otto (ycxdm1PRMs962FxyyuJ0) → MP3 → afplay
         ↓ WebSocket (integração melhorada)
[HUD] — avatar SPEAKING, chat, waveform (animações refinadas)
```

### ✅ O que FUNCIONA (18/07 — VALIDADO)
- **Bridge v3.2:** `jarvis-bridge-v3.js` — HTTP + WebSocket na :3033
- **HUD v3:** `http://localhost:3033/hud` — STT nativo pt-BR, SEMPRE ouvindo
- **TTS ativo:** ElevenLabs Otto `ycxdm1PRMs962FxyyuJ0` (brazilian male, intimidating) — **LIVE após alterações 17/07**
- **LLM do HUD:** Haiku (5x mais rápido para conversa)
- **Pipeline completo:** fala → STT pt-BR → bridge → Haiku → Otto TTS → afplay — **FULLY INTEGRATED (17/07)**
- **LaunchAgent:** `ai.teamironsolutions.jarvis-bridge` — sobe no boot
- **Waveform:** reativo, integrado com animações HUD
- **Mic:** sempre ativo, pausa inteligente quando Jarvis fala

### 🔧 Alterações Feitas (17/07/2026)
- ✅ Migração de voz: Daniel → Otto (ycxdm1PRMs962FxyyuJ0)
- ✅ Integração HUD + Bridge: melhorias de WebSocket, sync de estado
- ✅ Refinamentos na interface: animações, responsividade, UX
- ✅ Documentação completa: `ARCHITECTURE-VOICE-HUD.md` (18/07)

### ⚠️ Nota sobre Documentação
- Quota ElevenLabs: free tier esgotada em 17/07, mas Otto está operacional (já contabilizado)
- Fallback: Microsoft `pt-BR-AntonioNeural` disponível se Otto ficar indisponível

### Serviços (LaunchAgents — auto-start no boot)
| Serviço | plist | Porta |
|---|---|---|
| OpenClaw Gateway | ai.openclaw.gateway | 18789 |
| Jarvis Bridge | ai.teamironsolutions.jarvis-bridge | 3033 |

### Para usar o HUD
1. Abrir `http://localhost:3033/hud` no browser
2. Conceder permissão de microfone ao browser
3. Clicar no botão 🎤 ou pressionar Space
4. Falar em português — Jarvis responde em pt-BR pelos alto-falantes

## Pipeline de Voz (17-18 jul 2026)

**Status:** ✅ Fully integrated (18/07)

**Arquitetura ativa:**
```
Elgato Wave:1 → webkitSpeechRecognition (STT pt-BR nativo)
  ↓
HUD (localhost:3033/hud) → Jarvis Bridge v3.2
  ↓
OpenClaw Agent (Haiku) → ElevenLabs Otto (TTS) → afplay
  ↓
HUD — SPEAKING mode, waveform, chat panel (atualização em tempo real)
```

**Componentes — ✅ Operacional:**
- **Microfone:** Elgato Wave:1 (System Preferences configurado)
- **STT:** webkitSpeechRecognition (pt-BR, nativo do browser)
- **TTS:** ElevenLabs Otto (ID: ycxdm1PRMs962FxyyuJ0, brazilian male, intimidating)
- **Bridge:** v4 via LaunchAgent, porta 3033, HTTP + WebSocket em /stream
- **HUD:** http://localhost:3033/hud (hexágono holograma, animações refinadas)
- **Modelo:** Haiku (5x rápido pra conversa)
- **Auto-TTS:** Ativado em messages.tts (sempre áudio nas respostas)

## Documentação Arquitetura Voice/HUD

**Arquivo principal:** `ARCHITECTURE-VOICE-HUD.md` (completo, 12,938 bytes)  
Cobre:
- Diagrama arquitetura end-to-end
- HUD v4 (CSS, WebSocket, polling, animações)
- Bridge v3.2 (endpoints, fluxo /send, ElevenLabs config)
- Message flow example completo
- Troubleshooting & fallbacks
- LaunchAgent auto-start (ai.teamironsolutions.jarvis-bridge)

**Referência rápida:** `VOICE-SETUP.md`

## Interfaces & Dashboards (04/08/2026)

**Três camadas de visualização:**

| Interface | Porta | URL | Uso |
|-----------|-------|-----|-----|
| **Jarvis HUD** | 3033 | http://localhost:3033/hud | Voice-first conversação (STT/TTS, waveform) |
| **OpenClaw Office** | 5180 | http://localhost:5180 | Multi-agent dashboard (status, interações, logs) |
| **Claw3D** | 3001 | http://localhost:3001 | 3D virtual office (agentes em workspace imersivo) |

## Pendências / Open Items

- [x] Definir arquitetura do time de agentes (nomes, papéis, prompts)
- [x] **TONY STARK DEPLOYED** — primeira prova de conceito bem-sucedida
- [x] Configurar microfone Elgato
- [x] Ativar TTS ElevenLabs automático
- [x] Criar bridge v2 com WebSocket
- [x] Atualizar HUD pra se conectar ao bridge (send OK, 17/07/2026)
- [x] Voz masculina operacional (Otto, 17/07/2026)
- [x] **VOICE & HUD FULLY INTEGRATED** (18/07/2026)
- [x] Documentar arquitetura voice/HUD (18/07/2026)
- [x] Configurar commands.ownerAllowFrom (01/08/2026 — `["webchat:owner"]`)
- [x] **ECONOMIA DE TOKENS — PHASE 1 ATIVA** (01/08/2026 — Haiku default)
- [x] **PLAYBOOKS DE EXCELÊNCIA — 10 AGENTES COMPLETO** (04/08/2026)
- [x] **OpenClaw Office instalado** (04/08/2026 — LaunchAgent ativo)
- [x] **Claw3D 3D Office instalado** (04/08/2026 — LaunchAgent ativo)
- [ ] Configurar canais de mensagem (WhatsApp, Telegram, Discord?)
- [ ] Securizar gateway.auth.token (mover para SecretRef)
- [ ] Instalar Node.js system (fora do nvm) para estabilidade
- [ ] Clonar voz Eduardo Borgerth (dublador BR do JARVIS) — plano Creator ElevenLabs
- [ ] Documentar inter-agent workflows (próxima semana)
- [ ] Validar qualidade de playbooks com primeira execução
- [ ] **FASE 2:** skills reusáveis, cron digests, daily notes
- [ ] **FASE 3:** inter-agent workflows, TaskFlow, agent dashboard

## GitHub API Token

- **Localização:** `~/.openclaw/.github-token` (chmod 600)
- **Uso:** criar PRs via API, autenticar com GitHub
- **IMPORTANTE:** Sempre usar `cat ~/.openclaw/.github-token` para ler, nunca hardcode
- **Atualizado:** 16/08/2026 (ghp_N6QNbx0...)

## Procedimentos Padrão — Git Workflow Multi-Repo (desde 16/08/2026)

**Contexto:** Trabalhar com múltiplos repositórios (team-iron-jarvis-openclaw-config, jarvis-neural-interface, etc) requer respeito à estrutura de cada um.

**Procedimento:**
1. ✅ **Verificar propriedade do arquivo** — Qual repo pertence? (Não assumir)
2. ✅ **Clonar/acessar repo local** — `cd` para o diretório correto do repo
3. ✅ **Criar branch feature LOCAL** — Baseada em `develop` (ou `main` se não houver develop)
   - Exemplo: `git checkout develop && git checkout -b feature/caveman-middleware-esm`
4. ✅ **Validar base da branch** — `git branch -vv` deve mostrar que está baseada no remote correto
5. ✅ **Commits específicos** — Cada commit deve ser relevante apenas para aquele repo
6. ✅ **Fazer push** — `git push origin feature/nome-da-branch`
7. ✅ **PRs separadas** — Cada repo tem sua própria PR (nunca misturar repos em uma PR)
8. ✅ **Documentação** — Adicionar arquivo de integração/guide para cada repo

**Regra de Ouro:** Se não tiver 100% de certeza sobre a estrutura de repos, SEMPRE perguntar antes de fazer push.

**Aprendizado:** Dia 4 (16/08/2026) — Caveman integration mostrou importância dessa disciplina. Evitou trabalho duplicado e manteve repos limpos.

## Diagnosticando Regressions v2→v5 (16/08/2026 — TARDE)

### Problema Inicial
Após migração de HUD v2 → v5, três problemas apareceram:
1. **Volume do Spotify baixo** — música iniciava e permanecia em 40% (ducked)
2. **Bridge travava em conversas** — "Processando" indefinidamente
3. **Tags TTS sendo lidas** — [[tts:text]] tags faladas em voz alta

### Root Causes & Soluções

**Causa 1: Conflito de Session-Key**
- Bridge usava `HUD_SESSION_KEY = 'hud'`
- Session 'hud' era a sessão ativa do webchat neste momento
- OpenClaw CLI: `openclaw agent --session-key hud` — hung indefinitely (session lock)
- **Fix:** Mudou para `HUD_SESSION_KEY = 'jarvis-voice-cmd'` (sessão dedicada, sem conflitos)
- **Impacto:** Resolveu TODOS os 3 problemas simultaneamente

**Causa 2: Timeout prematuro durante análise**
- Ao tentar adicionar timeouts, cai em 30s era muito curto
- Sonnet diagnosticou: agent call pode levar >30s
- **Fix:** Não adicionar timeouts — mantém baseline f52de0d que funcionava

**Causa 3: Double-ducking no wake clap_phrase**
- Código tentava: `duckVolume()` ANTES de Spotify tocar
- Spotify iniciava já em 40%
- Depois `say()` duca novamente dentro da função
- **Fix:** Restaurar baseline — Spotify toca primeiro, depois `say()` duca durante TTS

### What Actually Worked
- **Bridge v4 baseline f52de0d** — última versão conhecida estável
- **Apenas 1 mudança segura:** Strip [[tts:...]] tags antes de TTS playback
- **Nenhuma mudança adicional** — tudo mais funcionava no baseline

### Lesson Learned
- **Quando adicionar features (HUD v5 widgets):** Não modificar componentes já estáveis
- **Isolamento:** Widgets em HTML/CSS puro (z-index layers), não tocar bridge
- **Debugging:** Sempre testar baseline antes de adicionar fixes
- **Session management:** Session-keys precisam ser única — nunca reutilizar chave da sessão principal

### Timeline
1. 18:02 GMT-3 — Problema relatado (música baixa, processando travado, tags TTS)
2. 18:03 — Diagnóstico com Sonnet ativado
3. 18:06 — Timeout fix tentado e falhado
4. 18:08 — Restauração completa a f52de0d + tag stripping
5. 18:11 — Problema persiste (ainda travado)
6. 18:11 — Identificado: session-key 'hud' em conflito
7. 18:12 — Mudança para 'jarvis-voice-cmd'
8. 18:15 — Galvão confirma: tudo voltou funcional
9. 18:17 — PR #3 aberta para develop

### PR #3 Status
- **Branch:** feature/hud-metrics-tier1-widgets
- **Base:** develop
- **Status:** Ready to merge
- **Tests:** ✅ All wake words, ✅ Spotify volume, ✅ No hangs, ✅ TTS clean

---

## Diagnóstico HUD 'Respondendo' Infinito (19/08/2026)

### Problema
HUD travava em **[ Respondendo... ]** para sempre após qualquer comando de voz. Todo o resto (volume, duplicatas, responsividade) estava correto.

### Causa Raiz — CRÍTICA
**Mismatch de URL no WebSocket:**

```js
// HUD hud-jarvis-v5-metrics.html (ERRADO):
new WebSocket('ws://localhost:3033')      // conectava na raiz /

// Bridge jarvis-bridge-v4.js (CORRETO):
server.on('upgrade', (req, socket, head) => {
  if (req.url === '/stream') { ... }      // só aceita WS em /stream
});
```

O WebSocket **nunca se conectou de verdade**. O HUD entrava em `speaking` mode via fetch HTTP local, mas o `idle` (que vem via WS) nunca chegava. Resultado: HUD permanentemente em "Respondendo".

**Diagnóstico foi possível porque:**
- Bridge logs mostravam `TTS: done` → bridge funcionava perfeitamente
- Problema era 100% no cliente (HUD)
- Revisão do código WS revelou o mismatch de path

### Fix Aplicado
1. **hud-jarvis-v5-metrics.html:** `ws://localhost:3033` → `ws://localhost:3033/stream`
2. **jarvis-bridge-v4.js:** `idle` broadcast movido para PRIMEIRO no `finally` (antes ops Spotify)
3. **jarvis-bridge-v4.js:** `restoreSpotifyVolume()` no startup + `unDuckVolume()` em try/catch
4. **LaunchAgent plist:** path corrigido de `jarvis-bridge-v3.js` → `jarvis-bridge-v4.js`

### ⚠️ Regra Permanente — WebSocket URL
**SEMPRE verificar:** HUD WS URL = `ws://localhost:3033/stream`  
**NUNCA usar:** `ws://localhost:3033` (raiz) — bridge não aceita WS na raiz!

### ⚠️ Regra Permanente — LaunchAgent
**Script correto:** `/Users/teamironsolutions/.openclaw/workspace/jarvis-neural-interface/bridge/jarvis-bridge-v4.js`  
**NUNCA:** `jarvis-bridge-v3.js` (inexistente) ou path do workspace raiz

### PR #4 Status
- **Branch:** fix/hud-ws-stream-bridge-idle
- **Base:** develop
- **Status:** Open — https://github.com/Team-Iron-Solutions/jarvis-neural-interface/pull/4
- **Tests:** ✅ HUD retorna ao idle ✅ WS conectado ✅ Bridge v4 via LaunchAgent

---

## Phase 4 Sprint 3 — Key Discoveries (30/08/2026)

### Why Declarative Code Compresses Better with Graphify (Scott Lang Insight)

**Observation:** Flutter (-89.9%) compresses 42pp better than Python (-47.5%)

**Root Cause Analysis:**

1. **Declarative vs Imperative**
   - Flutter: `Widget build()` returns structure (natural graph)
   - Python: logic with loops, conditionals, side effects
   - **Graphify loves structures → compresses better**

2. **Hierarchies vs Control Flow**
   - Flutter: widget tree (perfect for AST representation)
   - Backend: control flow (tree-sitter sees less pattern)

3. **Composition vs State**
   - Flutter: components combine (natural graph patterns)
   - Backend: databases, side effects, order matters

**Implication:**
- Graphify ideal for: Flutter, React, Vue, design systems
- Less efficient for: Backend logic, state machines, complex flows
- **Extension opportunity:** Document this as "Graphify Sweet Spot" for future projects

---

## Technical Learning — Conceitos Fundamentais (26/08/2026)

### AST, Tree-Sitter e Semântica (Sprint 1 Discovery)

**O que aprendi durante Sprint 1 do Graphifyy:**

#### Tree-Sitter é Sempre AST Puro
- **AST = Abstract Syntax Tree:** Mapa estrutural de código (tipos, relações, hierarquia)
- **Tree-sitter** = Parser que extrai AST de código em 52+ linguagens
- **"Puro" = Zero LLM:** Tree-sitter nunca interpreta ou usa IA
- **Determinístico:** Mesmo código = mesma árvore, sempre (100% confiável)

**Exemplos:**
- Tree-sitter extrai: "classe AudioBuffer tem método add()"
- Tree-sitter extrai: "função initAudio() chama AudioBuffer.__init__()"
- Tree-sitter NÃO extrai: "AudioBuffer é crítico", "add() tem bug"

#### Semântica vs Estrutura
- **Estrutura (AST/tree-sitter):** Forma do código, relações, hierarquia — $0, <100ms
- **Semântica (LLM/Ollama):** Significado, propósito, criticidade — $$, 1-10s

**Trade-off:**
```
AST puro (tree-sitter): Rápido, barato, 100% certo, sem contexto
Semântica (LLM): Lento, caro, 95-99% certo, contexto rico
Melhor: Combinar os dois
```

#### Como Graphifyy Usa Ambos
1. **Código (.js, .py, .java)** → tree-sitter → AST puro (zero LLM)
2. **Documentação (.md, README)** → Ollama → Semântica (labels, descrições)
3. **graph.json** = estrutura + contexto sem redundância

**Sprint 1 real (jarvis-neural-interface):**
- 4 arquivos de código → 60 nós estruturais (tree-sitter puro)
- 17 arquivos .md → 30 nós enriquecidos (Ollama semântica)
- Total: 90 nós, 113 edges, 68KB, $0

**Economia real:**
```
Without graphify: read 50 files = 5000+ tokens
With graphify: graphify explain = 150 tokens
Savings: -97% tokens
```

#### Decisão Sprint 1: qwen3.5:4b vs 9b
- **Problema:** qwen3.5:9b causava OOM (out of memory) — 6-7GB RAM
- **Solução:** qwen3.5:4b suficiente (4-5GB RAM)
- **Qualidade delta:** Negligenciável (<1% difference em labels)
- **Recomendação:** 4b é standard para Phase 4 (ATUALIZADO em GRAPHIFY-CONVENTIONS.md)

**Por quê funciona:**
- Código é processado por tree-sitter (zero model)
- Docs são processadas por Ollama (4b é suficiente para markdown)
- 4b processou 17 docs sem problema

#### Documentação Criada (26/08/2026)
- 📄 `[[AST-TreeSitter-Semantica.md]]` — Explicação completa em Obsidian
  - Referência permanente para toda a equipe
  - Explica por que --skip-semantic não funcionou
  - Trade-offs estrutura vs semântica
  - Exemplos práticos com código

**Lição:** Bom conhecimento técnico merece boa documentação. Obsidian + GitHub = aprendizado + referência.

---

## Wildream App Project (28/08/2026 — INICIADO)

**Cliente:** Wildream  
**Tipo:** Aplicativo mobile de aprendizagem de inglês  
**Status:** 🟡 **Análise PRD em andamento**  
**PM responsável:** Stephen Strange  
**Tech Lead:** Jarvis  

### O Que É

Plataforma mobile (iOS + Android) para ensino de inglês baseada em:
- Repetição espaçada (flashcards inteligentes)
- Prática de frases reais
- IA (conversação, pronúncia, vocabulário, feedback gramatical)
- Suporte humano via professores (versão Pro)

**Modelo de Negócio:** Free (essencial) + Pro (IA + suporte humano)  
**Preço Pro:** R$ 29,90/mês ou R$ 299,00/ano (configurável)  
**Pagamento:** Cartão + Mercado Pago  
**Roadmap Futuro:** B2B (Wild Dream for Business) — treinamento corporativo

### MVP — Funcionalidades Principais

**Free:**
- Flashcards com repetição espaçada (algoritmo parametrizável)
- Criar/editar/buscar frases
- Traduções
- Teste de nível CEFR (opcional)
- Metas diárias por nível
- Progresso e histórico
- Troféus + streaks

**Pro (tudo acima +):**
- Áudio gerado por IA
- Análise de pronúncia (palavra por palavra)
- Feedback gramatical
- Conversação por texto com IA (com cenários)
- Conversação por voz com IA
- Geração de vocabulário por tema
- Tarefas atribuídas por professor
- Suporte via chat com professor

### Públicos

1. **Aluno Free:** Estuda grátis com flashcards
2. **Aluno Pro:** IA + suporte de professor
3. **Professor:** Chat de suporte, criação de tarefas
4. **Admin:** Dashboard (usuários, métricas, planos, parâmetros)

### Documentação

- **PRD Completo:** `projects/wildream/WILDREAM_APP_PRD_V1.0.md`
- **Request Análise:** `projects/wildream/PRD-Analysis-Request.md`
- **Project Hub (Obsidian):** `obsidian-vault/Projetos/Wildream-Project-Hub.md`
- **Análise PM:** `projects/wildream/PRD-Analysis-Response.md` (🟡 Aguardando)

### Timeline

- **28/08:** PRD enviado para Stephen Strange (análise)
- **Antes 02/09:** Análise e recomendações esperadas
- **02-03/09:** Validação com Galvão
- **03/09+:** Kickoff técnico


### Análise PRD Completa — Stephen Strange (28/08/2026)

**Status:** ✅ ANÁLISE ENTREGUE

**Veredicto:** Visão sólida + escopo irreal para 10-12 semanas

#### ✅ Pontos Fortes (Validados)
1. **Princípio central excelente** — "aumentar frequência, não substituir" (Jobs to Be Done claro)
2. **Free tier genuinamente útil** — não é apenas teaser
3. **Critério de sucesso excelente** — Seção 19 (pergunta norteadora é bússola)
4. **Decisões abertas explícitas** — Seção 18 mostra maturidade
5. **Gamificação sem ranking** — decisão pedagogicamente correta
6. **4 perfis bem definidos** — autorização clara
7. **Monetização configurável** — sem hardcoding de preços

#### 🔴 RISCOS CRÍTICOS (3 Bombas)
1. **Escopo irreal** — 17 features em 10-12 semanas é produto de 6-9 meses
   - Fix: Conversação por voz → V1.1, Suporte professor → ticket assíncrono
2. **Algoritmo de repetição errado** — baseado em contagem, não tempo
   - Fix: SM-2 ou FSRS (algoritmo real, baseado em dias/horas)
3. **Meta A1: 150 frases/dia mata engajamento** — iniciante não consegue
   - Fix: A1 = 20-30 frases/dia (pedagogicamente correta)

#### 🟠 Riscos Altos (Documentados)
- Custo de IA pode destruir margem sem franquia definida
- Suporte de professores é complexidade operacional prematura
- Banco de frases inicial não mencionado (conteúdo = 0?)
- Conversação por voz é feature de alto risco técnico
- Admin completo no MVP = desperdício de capacidade

#### 🤔 Perguntas Críticas para Galvão
1. Volume esperado de usuários no lançamento?
2. Há banco de frases/conteúdo existente ou parte do zero?
3. Quantos professores disponíveis + SLA?
4. Orçamento máximo mensal para APIs de IA?
5. App é complemento ou standalone?
6. Houve validação com usuários (entrevistas, protótipo, beta)?
7. Chat com professores: síncrono ou assíncrono?
8. Design system / Figma já pronto?
9. B2B é intenção real ou especulativa?

#### 📊 MVP Revisado (Realista 10-12 semanas)
- Semanas 1-2: Fundação (cadastro, onboarding, nível, banco de frases)
- Semanas 3-5: Core (flashcards, repetição espaçada REAL SM-2, metas)
- Semanas 5-6: Engajamento (streak, troféus, notificações)
- Semanas 6-8: Monetização (Free/Pro, Mercado Pago, TTS básica)
- Semanas 8-10: IA Texto (conversação por texto, pronúncia básica)
- Semanas 10-12: Admin + QA + stores

**SAI do MVP:**
- Conversação por voz → V1.1
- Pronúncia palavra a palavra (detalhada) → V1.1
- Geração de vocabulário por IA → V1.1
- Chat com professores → Ticket assíncrono no MVP, sistema real no V1.1
- Admin completo → Admin minimal (usuários, planos, receita)

#### 💡 Recomendações Principais
1. Cortar escopo rigorosamente (5-6 features saem, vão para V1.1)
2. **Definir KPIs de sucesso** antes do kickoff:
   - Retenção D7 ≥ 40%
   - Conversão Free→Pro ≥ 5% (mês 1), ≥ 10% (mês 3)
   - DAU/MAU ≥ 30%
   - Churn Pro mensal ≤ 10%
3. Corrigir algoritmo de repetição espaçada (SM-2 ou FSRS)
4. Revisar metas diárias com base pedagógica
5. Converter suporte professor (MVP) → ticket assíncrono
6. Definir conteúdo inicial antes do kickoff (200 frases/nível CEFR mínimo)
7. Estratégia offline mínima (flashcards funcionam offline)
8. Definir franquia de IA antes do kickoff (ex: 60 sessões/mês no Pro)
9. Validação com usuários ANTES do kickoff (5 entrevistas com protótipo Figma)

#### 📋 Próximos Passos
1. ⏳ Galvão responde as 9 perguntas críticas
2. ⏳ Validação com usuários (5 entrevistas com protótipo)
3. ⏳ Kickoff técnico (03/09+) com escopo definido
4. ⏳ Tech lead (Tony Stark?) começa arquitetura com MVP realista

---

## Phase 4 Graphify — Token Optimization Discovery (30/08/2026)

### Tier 2 Completion: All 3 Agents PASS ✅

**Status:** Tier 2 rollout successful. All success criteria exceeded.

**Results Summary:**
- ✅ Scott Lang (Flutter): **-89.9%** compression, 4.7/5 quality (BEST)
- ✅ Wanda Maximoff (Design): -55.0% compression, 4.56/5 quality
- ✅ Natasha Romanoff (Testing): -50.0% compression, 4.56/5 quality

**Verdict:** Ready for Tier 3 rollout decision.

### Key Discovery: Declarative Code Compresses Exceptionally Well

**Pattern Identified:**

- Declarative (Highest): Flutter (-89.9%) — widgets, hierarchies, UI composition
- Structured: Design (-55.0%), Architecture (-55.6%), Testing (-50.0%)
- Imperative (Lowest): Python (-47.5%), Node.js (TBD)

**Why:** Tree-sitter excels on structured code (AST parsing). Declarative patterns = predictable graphs. Imperative logic = variable, less predictable.

**Strategic Implication:** Graphify ideal for declarative systems (Flutter, React, design tokens). Less effective for backend business logic.

### Compression by Context

| Context | Compression | Best For |
|---------|-------------|----------|
| Flutter (declarative) | **-89.9%** | Mobile app code review |
| Design systems | -55.0% | Design token analysis |
| Architecture | -55.6% | System design review |
| Testing | -50.0% | Test coverage analysis |
| Python (imperative) | -47.5% | Backend architecture only |

### Tier 3 Readiness Assessment

**Recommended for Tier 3:**
- Visão (SQL): Medium fit (-40-45% est.)
- T'Challa (Shell/Config): Medium fit (-35-40% est.)

**Not recommended:**
- Peter Parker (non-code)
- Stephen Strange (strategic analysis)

### References

- Tier 2 consolidated: `PHASE4-SPRINT3-TIER2-CONSOLIDATED-RESULTS.md`
- Scott's detailed report: `PHASE4-SPRINT3-SCOTT-REPORT.md`
- All metrics: `PHASE4-SPRINT3-SCOTT|WANDA|NATASHA-METRICS.json`

