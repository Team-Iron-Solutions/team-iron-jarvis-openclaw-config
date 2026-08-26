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

### Phase 4 — Graphify + Ollama (19/08 → 26/08/2026)
**Objetivo:** Reduzir contexto carregado durante code review via knowledge graphs  
**Agentes:** Tony Stark, Bruce Banner, Steve Rogers, Scott Lang, Wanda, Natasha (Tier 1+2)  
**Economia estimada:** -50-95% de tokens (variável por repo size, -$3,960/ano para squad)  
**Status:** 🟡 **Sprint 1 EM CONCLUSÃO** (26/08 13:43-14:20)  
**Branch:** `feat/graphify-phase4` (3 commits: setup, ollama-integration, documentation-suite)

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
