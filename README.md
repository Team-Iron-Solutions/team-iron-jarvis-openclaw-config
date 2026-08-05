# 🦾 OpenClaw Configuration - Team Iron Solutions

Infrastructure as Code para replicar o ambiente completo de OpenClaw, agentes, playbooks e MCP servers da Team Iron Solutions em qualquer servidor.

**Status:** ✅ Production-ready (agosto 2026)

---

## 🎯 O que está incluído

- ✅ **10 Agentes Configurados** (Tony Stark, Bruce Banner, Steve Rogers, etc.)
- ✅ **Playbooks de Excelência** — padrões operacionais para cada agente
- ✅ **Workspace Completo** — SOUL.md, AGENTS.md, MEMORY.md, documentação
- ✅ **3 Servidores MCP** — memory, filesystem, github
- ✅ **Script de Setup Automatizado** — replica tudo em minutos
- ✅ **Infrastructure as Code** — versione e replique com segurança

---

## 🚀 Quick Start

### 1. Clone o repositório
```bash
git clone https://github.com/teamironsolutions/openclaw-config.git
cd openclaw-config
chmod +x setup.sh
```

### 2. Execute setup (automatizado)
```bash
./setup.sh
```

**O que ele faz:**
- ✅ Verifica Node.js / npm
- ✅ Instala OpenClaw globalmente
- ✅ Cria `~/.openclaw/workspace`
- ✅ Copia arquivos de configuração
- ✅ Configura 3 servidores MCP
- ✅ Valida setup

### 3. Configure Secrets (fora do repo)

**GitHub Token** — necessário para MCP GitHub:
```bash
# 1. Crie em https://github.com/settings/tokens/new
#    Permissões: repo, read:org, user:email
# 2. Configure:
export GITHUB_TOKEN=ghp_...
# 3. Setup MCP:
openclaw mcp add github \
  --command npx --arg -y --arg @modelcontextprotocol/server-github \
  --env GITHUB_TOKEN="$GITHUB_TOKEN"
```

**Gateway Token** (se usar remote gateway):
```bash
export GATEWAY_TOKEN=your_token_here
```

### 4. Inicie o Gateway
```bash
openclaw gateway --port 18789
# ou em background:
openclaw gateway --port 18789 > /tmp/openclaw.log 2>&1 &
```

### 5. Teste um agente
```bash
openclaw agent --agent main --message "Olá, qual é meu nome?"
```

---

## 📁 Estrutura do Repositório

```
.
├── README.md                      # Este arquivo
├── setup.sh                       # Script de replicação (automation)
├── .gitignore                     # Segurança (sem secrets!)
│
├── config/
│   ├── openclaw.template.json     # Template config (sem secrets)
│   └── mcp/                       # Definições MCP
│
└── workspace/
    ├── SOUL.md                    # Identidade & tom (Jarvis)
    ├── AGENTS.md                  # Workspace overview
    ├── MEMORY.md                  # Long-term memory (durable)
    ├── IDENTITY.md                # Avatar & appearance
    ├── USER.md                    # Quem é Galvão
    ├── TOOLS.md                   # Notas locais (cameras, hosts, etc)
    │
    └── playbooks/
        ├── TONY-STARK-EXCELLENCE-PLAYBOOK.md
        ├── BRUCE-BANNER-EXCELLENCE-PLAYBOOK.md
        ├── STEVE-ROGERS-EXCELLENCE-PLAYBOOK.md
        ├── STEPHEN-STRANGE-EXCELLENCE-PLAYBOOK.md
        ├── VISAO-DATA-IA-EXCELLENCE-PLAYBOOK.md
        ├── WANDA-MAXIMOFF-EXCELLENCE-PLAYBOOK.md
        ├── TCHALLA-SRE-EXCELLENCE-PLAYBOOK.md
        ├── SCOTT-LANG-EXCELLENCE-PLAYBOOK.md
        ├── NATASHA-ROMANOFF-EXCELLENCE-PLAYBOOK.md
        └── PETER-PARKER-EXCELLENCE-PLAYBOOK.md
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

## 🐛 Troubleshooting

### OpenClaw command not found
```bash
npm install -g openclaw
```

### MCP server failed to start
```bash
openclaw mcp doctor --probe --verbose
# Verifica cada servidor
```

### GitHub token invalid
```bash
# 1. Verifica se token é válido em https://github.com/settings/tokens
# 2. Recria token se expirou
# 3. Re-configura:
export GITHUB_TOKEN=ghp_novo...
openclaw mcp unset github
openclaw mcp add github --command npx --arg -y --arg @modelcontextprotocol/server-github --env GITHUB_TOKEN="$GITHUB_TOKEN"
```

### Gateway won't start on port
```bash
# Use port diferente:
openclaw gateway --port 28789

# Ou libera porta:
lsof -i :18789
kill -9 <PID>
```

---

## 🤝 Customização

### Mudar modelo padrão

Edit `config/openclaw.template.json`:
```json
"agents": {
  "defaults": {
    "model": "anthropic/claude-sonnet-4-6"  // Troca haiku por sonnet
  }
}
```

### Adicionar novo agente

1. Cria workspace:
   ```bash
   mkdir -p workspace/<NOME>
   ```

2. Copia template:
   ```bash
   cp workspace/SOUL.md workspace/<NOME>/
   ```

3. Edita identidade:
   ```bash
   # Edita workspace/<NOME>/IDENTITY.md
   ```

4. Registra em `config/openclaw.template.json`:
   ```json
   {
     "id": "novo-agent",
     "name": "Novo Agent",
     "description": "..."
   }
   ```

### Conectar outro servidor

**Remote Gateway** (outro host):
```bash
openclaw mcp serve --url wss://remote-gateway:18789 --token-file ~/.openclaw/gateway.token
```

---

## 📚 Referências

- **OpenClaw Docs:** https://docs.openclaw.ai
- **MCP Protocol:** https://modelcontextprotocol.io
- **GitHub API:** https://docs.github.com/en/rest

---

## 📝 Versionamento

Versão dessa config: **2026-08-05**

Updates:
- ✅ 2026-08-05: MCP GitHub integrado
- ✅ 2026-08-04: 10 agentes completos + playbooks
- ✅ 2026-08-01: Phase 1 economia de tokens (Haiku default)
- ✅ 2026-07-18: Voice & HUD fully integrated

---

## 💬 Suporte

Problemas? Documentação completa em: `/Users/teamironsolutions/.openclaw/workspace/`

Ou consulte os agentes:
```bash
# Arquitetura
openclaw agent --agent steve-rogers --message "Como replicar isso em 3 ambientes?"

# Tech lead review
openclaw agent --agent tony-stark --message "Isso tá bom pra production?"
```

---

**Built with ❤️ by Team Iron Solutions**  
Transformamos Tecnologia em Vantagem Competitiva
