# 🦾 Team Iron Solutions — OpenClaw Config

Infrastructure as Code para replicar o ambiente completo de OpenClaw, agentes, playbooks e MCP servers da Team Iron Solutions em qualquer servidor — macOS ou Linux/VPS.

**Status:** ✅ Production-ready (agosto 2026) · **Multi-OS:** macOS + Linux ✅ · **Multi-cliente:** ✅

---

## 🎯 O que está incluído

- ✅ **10 Agentes Configurados** (Tony Stark, Bruce Banner, Steve Rogers, etc.)
- ✅ **Playbooks de Excelência** — padrões operacionais para cada agente
- ✅ **Workspace Completo** — SOUL.md, AGENTS.md, MEMORY.md, documentação
- ✅ **3 Servidores MCP** — memory, filesystem, github
- ✅ **Script de Setup Multi-OS** — macOS (LaunchAgent) + Linux (systemd)
- ✅ **Suporte Multi-Cliente** — padrões isolados por cliente (STANDARDS, TECH-STACK, CODING-RULES)
- ✅ **Task Dispatch Protocol** — garantia de que regras do cliente são sempre respeitadas
- ✅ **Infrastructure as Code** — versione e replique com segurança

---

## 🚀 Quick Start

```bash
# 1. Clone
git clone https://github.com/Team-Iron-Solutions/team-iron-jarvis-openclaw-config.git \
  ~/.openclaw/workspace

# 2. Copiar config template
cp ~/.openclaw/workspace/config/openclaw.template.json ~/.openclaw/openclaw.json
# Edite ~/.openclaw/openclaw.json e substitua os placeholders

# 3. Setup completo
cd ~/.openclaw/workspace
bash setup.sh
bash scripts/setup-graphify.sh

# 4. Configurar OpenRouter (fallback de modelos)
echo "sk-or-v1-..." | openclaw models auth paste-api-key --provider openrouter

# 5. Iniciar Gateway
openclaw gateway start
openclaw status
```

📖 **Guia detalhado:** [`SETUP.md`](./SETUP.md) — instalação completa em 30-45 min.

---

## 🎯 O que está incluído

### Agentes (10)

| Agente | Alter Ego | Papel | Modelo |
|--------|-----------|-------|--------|
| **Jarvis** | Iron Man AI | CTO / Orquestrador | Haiku |
| **Tony Stark** | Iron Man | Backend Node.js + Tech Lead | Haiku |
| **Bruce Banner** | Hulk | Backend Python | Haiku |
| **Steve Rogers** | Capitão América | Arquiteto de Software | **Sonnet** |
| **Stephen Strange** | Doutor Estranho | Product Manager | **Sonnet** |
| **Visão** | Vision | Data Engineer / IA | Haiku |
| **Wanda Maximoff** | Feiticeira Escarlate | Product Designer / UX | Haiku |
| **T'Challa** | Pantera Negra | SRE Engineer | Haiku |
| **Scott Lang** | Homem-Formiga | Flutter Developer | Haiku |
| **Natasha Romanoff** | Viúva Negra | QA Engineer | Haiku |
| **Peter Parker** | Homem-Aranha | Content / Social Media | Haiku |

### Token Optimization (73-85% economia)

| Fase | Tecnologia | Economia | Status |
|------|-----------|----------|--------|
| **Phase 1** | Haiku default, Sonnet seletivo | -60% vs all-Sonnet | ✅ Ativo |
| **Phase 2** | OpenRouter fallback chain | -75-95% quando acionado | ✅ Configurado |
| **Phase 3** | Caveman compression middleware | -45% por request | ✅ Live |
| **Phase 4** | Graphify knowledge graphs | -43 a -90% em code review | ✅ Live |

📖 **Detalhes:** [`TOKEN-OPTIMIZATION.md`](./TOKEN-OPTIMIZATION.md)

---

## 📁 Estrutura do Repositório

```
.
├── README.md                        # Este arquivo
├── setup.sh                         # Setup multi-OS (macOS + Linux)
├── .gitignore                       # Segurança (sem secrets!)
│
├── config/
│   └── openclaw.template.json         # Template config (sem secrets)
│
├── clients/                         # 🕑 Padrões por cliente
│   ├── README.md
│   ├── _TEMPLATE/                     # Template para novos clientes
│   │   ├── STANDARDS.md               # Padrões de codificação
│   │   ├── TECH-STACK.md              # Tecnologias e versões
│   │   ├── CODING-RULES.md            # Regras obrigatórias
│   │   └── CONTEXT.md                 # Contexto do projeto
│   └── _EXEMPLO-CLIENTE/              # Exemplo preenchido (Acme Corp)
│
├── docs/                            # 📖 Documentação operacional
│   ├── DEPLOYMENT-GUIDE.md            # Como fazer deploy em VPS/Mac
│   └── TASK-DISPATCH-PROTOCOL.md      # Como enviar tasks com contexto
│
├── agents-workspaces/               # Workspaces individuais dos agentes
│   ├── tony/
│   ├── bruce/
│   ├── steve/
│   └── ... (10 agentes)
│
└── workspace/                       # Workspace do Jarvis (main)
    ├── SOUL.md
    ├── AGENTS.md
    ├── MEMORY.md
    ├── IDENTITY.md
    ├── USER.md
    └── TOOLS.md
```

---

## 🔐 Segurança & Secrets

⚠️ **NUNCA commite secrets!** O `.gitignore` protege:
- `openclaw.json` (local)
- `.github-token`
- `*.token` files
- `.env*`

**Setup Seguro:**
1. Clone repositório ✅
2. Rode `setup.sh` (cria config vazio)
3. Adicione secrets em `~/.openclaw/openclaw.json` LOCALMENTE
4. Configure env vars: `export GITHUB_TOKEN=...`

---

## 🔌 MCP Servers Configurados

| Servidor | Ferramentas | Uso |
|----------|-------------|-----|
| **memory** | 9 | Contexto persistente, grafo de conhecimento |
| **filesystem** | 6 | Ler/escrever código, explorar workspace |
| **github** | 26 | Repos, issues, PRs, code search, commits |

### Adicionar mais servidores

```bash
# PostgreSQL (data queries)
openclaw mcp add postgres \
  --command npx --arg -y --arg @modelcontextprotocol/server-postgres \
  --env DATABASE_URL="postgresql://user:pass@localhost/db"

# Slack (team messages)
openclaw mcp add slack \
  --command npx --arg -y --arg @modelcontextprotocol/server-slack \
  --env SLACK_BOT_TOKEN="xoxb-..."

# Usar novo servidor
openclaw mcp probe postgres --json
```

---

## 👥 10 Agentes Pré-configurados

Cada agente tem seu próprio **workspace**, **identidade**, **playbook de excelência** e **responsabilidades específicas**:

| Agent | Alter Ego | Role | Stack |
|-------|-----------|------|-------|
| Tony Stark | Iron Man | Backend Node.js + Tech Lead | Node.js, API design, code review |
| Bruce Banner | Hulk | Backend Python | Python, data analysis, optimization |
| Steve Rogers | Capitão América | Architect | System design, CTO-level strategy |
| Stephen Strange | Doutor Estranho | Product Manager | Roadmap, requirements, vision |
| Visão | Vision | Data Engineer / IA | Pipelines, analytics, ML |
| Wanda Maximoff | Scarlet Witch | Product Designer / UX | UI/UX, design system, research |
| T'Challa | Black Panther | SRE Engineer | Infrastructure, deployment, LGPD |
| Scott Lang | Ant-Man | Flutter Developer | Mobile, cross-platform, web |
| Natasha Romanoff | Black Widow | QA Engineer | Testing, automation, quality gates |
| Peter Parker | Spider-Man | Content / Social Media | Instagram, blog, storytelling |

**Cada um tem:**
- `workspace/<NAME>/EXCELLENCE-PLAYBOOK.md` — padrões de operação
- `workspace/<NAME>/IDENTITY.md` — quem é esse agente
- `workspace/<NAME>/USER.md` — contexto de trabalho
- MCP access para memory, filesystem, github

---

## 📊 Validar Setup

```bash
# Ver tudo configurado
openclaw mcp status

# Provar que funciona (conecta aos servers)
openclaw mcp doctor --probe

# Testar um agente
openclaw agent --agent tony-stark --message "Revise este código Node.js"

# Ver log do Gateway
tail -f /tmp/openclaw.log
```

---

## 🔄 Atualizar Configuração

Após pull de updates:

```bash
# Re-run setup (non-destructive)
./setup.sh

# Ou setup específico:
openclaw mcp reload          # Recarrega servidores MCP
openclaw skills load         # Recarrega skills
openclaw gateway restart     # Reinicia gateway
```

---

## ⚙️ Configuração

### Template (`config/openclaw.template.json`)

Copie para `~/.openclaw/openclaw.json` e substitua os placeholders:

```json
{
  "env": {
    "OPENROUTER_API_KEY": "sk-or-v1-..."
  },
  "agents": {
    "defaults": {
      "model": {
        "primary": "anthropic/claude-haiku-4-5",
        "fallbacks": [
          "openrouter/anthropic/claude-haiku-4-5",
          "openrouter/auto",
          "google/gemini-3.1-pro-preview"
        ]
      }
    }
  }
}
```

### MCP Servers

| Servidor | Ferramentas | Uso |
|----------|-------------|-----|
| **memory** | 9 | Contexto persistente, knowledge graph |
| **filesystem** | 6 | Ler/escrever arquivos |
| **github** | 26 | Repos, PRs, issues, code search |

---

## 🔐 Segurança

**Nunca commitar secrets!** O `.gitignore` protege:
- `~/.openclaw/openclaw.json` (config local com keys)
- `.env`, `.env.local`
- `memory/` (daily notes pessoais)
- `obsidian-vault/` (wiki pessoal)
- `python-code-reviews/` (artefatos Graphify)

```bash
# Secrets ficam APENAS em:
~/.openclaw/openclaw.json   ← local, nunca no git
```

---

## 🌐 Multi-Servidor: Central Brain + Remote Nodes

Este IaC suporta o modelo onde o servidor central (VPS ou Mac mini) roda todos os agentes, e máquinas dos clientes se conectam como **nodes remotos**.

```
Servidor Central (Hostinger VPS / Mac mini)
├── Jarvis + 10 agentes (cérebro)
└── clients/ (padrões isolados por cliente)
        ↓ OpenClaw Node Protocol
├── node-cliente-a  → repo/projetos do Cliente A
├── node-cliente-b  → repo/projetos do Cliente B
└── node-cliente-c  → repo/projetos do Cliente C
```

**Cada cliente tem:**
- Node dedicado com seu ambiente e repos
- Pasta `clients/<nome>/` com seus padrões isolados
- Agentes que respeitam suas regras via Task Dispatch Protocol

**Guia completo:** [docs/DEPLOYMENT-GUIDE.md](./docs/DEPLOYMENT-GUIDE.md)
**Padrões por cliente:** [clients/README.md](./clients/README.md)
**Como enviar tasks:** [docs/TASK-DISPATCH-PROTOCOL.md](./docs/TASK-DISPATCH-PROTOCOL.md)

---

## 📚 Referências

- **OpenClaw Docs:** https://docs.openclaw.ai
- **MCP Protocol:** https://modelcontextprotocol.io
- **GitHub API:** https://docs.github.com/en/rest

---

## 📝 Versionamento

| Documento | Conteúdo |
|-----------|---------|
| [`SETUP.md`](./SETUP.md) | Instalação completa em nova máquina |
| [`TOKEN-OPTIMIZATION.md`](./TOKEN-OPTIMIZATION.md) | Estratégia de economia de tokens |
| [`docs/OPENROUTER-SETUP.md`](./docs/OPENROUTER-SETUP.md) | Configurar OpenRouter |
| [`docs/CAVEMAN-INTEGRATION.md`](./docs/CAVEMAN-INTEGRATION.md) | Integrar Caveman middleware |
| [`docs/GRAPHIFY-SETUP.md`](./docs/GRAPHIFY-SETUP.md) | Instalar e configurar Graphify |
| [`docs/GRAPHIFY-OVERVIEW.md`](./docs/GRAPHIFY-OVERVIEW.md) | Como o Graphify funciona |
| [`docs/adr/`](./docs/adr/) | Architecture Decision Records |

---

## 📊 Histórico de Versões

| Data | Versão | O que mudou |
|------|--------|-------------|
| 30/08/2026 | v2.0.0 | Repo profissionalizado: cleanup completo, SETUP.md, OpenRouter, Caveman fixes, Graphify |
| 16/08/2026 | v1.4.0 | Phase 3: Caveman middleware (-45% tokens) |
| 04/08/2026 | v1.3.0 | 10 agentes completos + playbooks |
| 01/08/2026 | v1.2.0 | Phase 1: Haiku default, economia de tokens |
| 18/07/2026 | v1.1.0 | Voice + HUD integrados |
| 15/07/2026 | v1.0.0 | Primeira versão — Jarvis online |

---

**Built with ❤️ by Team Iron Solutions**  
*Transformamos Tecnologia em Vantagem Competitiva*
