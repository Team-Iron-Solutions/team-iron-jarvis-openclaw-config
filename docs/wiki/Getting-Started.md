# 🚀 Getting Started

Como replicar o ambiente OpenClaw completo em 5 minutos.

---

## ✅ Pré-requisitos

- **Node.js 20+** — [Instalar](https://nodejs.org)
- **npm** (incluído com Node.js)
- **macOS**, **Linux** ou **Windows (WSL2)**
- **Git**
- ~500MB de espaço em disco

---

## 📥 Passo 1: Clone o Repositório

```bash
git clone https://github.com/Team-Iron-Solutions/team-iron-jarvis-openclaw-config.git
cd team-iron-jarvis-openclaw-config
chmod +x setup.sh
```

**Resultado esperado:**
```
📁 team-iron-jarvis-openclaw-config/
   ├── setup.sh
   ├── README.md
   ├── config/
   └── workspace/
```

---

## 🚀 Passo 2: Execute o Setup

```bash
./setup.sh
```

**O que ele faz automaticamente:**
- ✅ Verifica Node.js / npm
- ✅ Instala OpenClaw globalmente
- ✅ Cria `~/.openclaw/workspace`
- ✅ Copia arquivos de configuração
- ✅ Configura 3 servidores MCP (memory, filesystem, github)
- ✅ Valida setup

**Tempo:** ~2 minutos

---

## 🔑 Passo 3: Configure GitHub Token (Opcional mas Recomendado)

Para usar GitHub MCP (criar/atualizar repos, issues, PRs):

### 3.1 Crie um Token

1. Acesse: https://github.com/settings/tokens/new
2. **Token name:** `openclaw-agents`
3. **Scopes:** 
   - ✅ `repo` (read/write repositories)
   - ✅ `read:org` (read organizations)
   - ✅ `user:email`
4. **Expiration:** 90 days
5. Clique **Generate**

### 3.2 Configure no OpenClaw

```bash
export GITHUB_TOKEN=ghp_YOUR_TOKEN_HERE

openclaw mcp add github \
  --command npx \
  --arg -y \
  --arg @modelcontextprotocol/server-github \
  --env GITHUB_TOKEN="$GITHUB_TOKEN"
```

**Validar:**
```bash
openclaw mcp probe github
# Deve retornar: 26 tools
```

---

## ⚙️ Passo 4: Inicie o Gateway

```bash
# Terminal 1 — Gateway
openclaw gateway --port 18789
```

**Esperado:**
```
✅ Gateway listening on port 18789
✅ WebSocket: wss://localhost:18789
```

---

## 🤖 Passo 5: Teste um Agente

```bash
# Terminal 2 — Agente
openclaw agent --agent tony-stark --message "Olá, quem você é?"
```

**Esperado:**
```
Tony Stark: Sou Tony Stark, Backend Node.js e Tech Lead...
```

---

## ✨ Passo 6: Use os Agentes

### Agente Principal (Jarvis - CTO)
```bash
openclaw agent --agent main --message "Qual é a arquitetura do sistema?"
```

### Backend Team
```bash
openclaw agent --agent tony-stark --message "Revise este código Node.js"
openclaw agent --agent bruce-banner --message "Otimize este query Python"
```

### Arquitetura & Strategy
```bash
openclaw agent --agent steve-rogers --message "Designe uma arquitetura pra 1M req/dia"
openclaw agent --agent stephen-strange --message "Qual é nossa roadmap?"
```

### Data & Design
```bash
openclaw agent --agent visao --message "Analise esses dados"
openclaw agent --agent wanda-maximoff --message "Desenhe um novo dashboard"
```

---

## 🔌 MCP Servers Já Configurados

Seus agentes já podem usar:

| Servidor | Ferramentas | Exemplo |
|----------|-------------|---------|
| **memory** | 9 | Salvar decisões, buscar contexto |
| **filesystem** | 6 | Ler/escrever código, explorar workspace |
| **github** | 26 | Criar repos, issues, PRs, commits |

**Exemplo completo:**
```bash
openclaw agent --agent tony-stark --message "
Crie um repositório em GitHub chamado 'meu-projeto',
e documenta que é um 'Projeto exemplo Team Iron'.
"
```

---

## 🎯 Próximos Passos

### Configuração Adicional

1. **Adicionar mais MCP servers:**
   ```bash
   openclaw mcp add postgres --command npx ...
   openclaw mcp add slack --command npx ...
   ```

2. **Customizar agentes:**
   - Edite `~/.openclaw/workspace/SOUL.md` para mudar identidade
   - Edite `~/.openclaw/workspace/AGENTS.md` para overview

3. **Ativar canais de mensagem:**
   - Telegram, WhatsApp, Discord, etc
   - [Documentação de canais](../../../docs/gateway/channels)

### Aprender Mais

- **[System Architecture](System-Architecture)** — Entenda os componentes
- **[10 Agents Overview](Agents-Overview)** — Conheça cada agente
- **[Agent Playbooks](Agent-Playbooks)** — Excellence guidelines

---

## ✅ Checklist de Setup

- [ ] Node.js 20+ instalado
- [ ] Repositório clonado
- [ ] `setup.sh` executado com sucesso
- [ ] Gateway rodando na porta 18789
- [ ] Agente testado (ex: tony-stark)
- [ ] GitHub token configurado (optional)
- [ ] MCP servers validados com `openclaw mcp status`

---

## 🐛 Problemas Comuns

**OpenClaw command not found:**
```bash
npm install -g openclaw
```

**Gateway já rodando:**
```bash
lsof -i :18789
kill -9 <PID>
openclaw gateway --port 18789
```

**MCP server fail:**
```bash
openclaw mcp doctor --probe
# Verifica cada servidor
```

👉 Mais em [Troubleshooting](Troubleshooting)

---

## 🎓 Exemplo Workflow

```bash
# Terminal 1: Gateway
openclaw gateway --port 18789

# Terminal 2: Trabalhar com um agente
openclaw agent --agent tony-stark --message "
Revise este código Node.js:

app.get('/users', async (req, res) => {
  const users = await db.query('SELECT * FROM users WHERE status = ?', [req.query.status]);
  res.json(users);
});

Identifique problemas N+1, segurança e performance.
"

# Terminal 3: Outro agente em paralelo
openclaw agent --agent visao --message "
Qual é o tamanho médio da tabela 'users' em nosso banco?
E qual é o padrão de acesso mais comum?
"
```

---

**Próximo?** Explore [System Architecture](System-Architecture) pra entender como tudo funciona!

---

**Last Updated:** 2026-08-05
