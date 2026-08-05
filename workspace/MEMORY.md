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
- **Bridge:** v3.2 via LaunchAgent, porta 3033, HTTP + WebSocket
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
