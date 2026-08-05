# ❓ FAQ — Perguntas Frequentes

---

## 🚀 Setup & Installation

### P: Quanto tempo leva pra setup?
**R:** ~5 minutos com `./setup.sh`

### P: Funciona em Windows?
**R:** Sim, com WSL2 (Windows Subsystem for Linux 2)
```bash
wsl --install
# Depois siga Getting Started normalmente
```

### P: Posso rodar em Docker?
**R:** Sim! Você pode containerizar o setup

### P: Preciso de internet?
**R:** Sim, pra:
- Instalar OpenClaw via npm
- Conectar a GitHub (se usar MCP GitHub)
- Download de MCP servers

---

## 👥 Agentes

### P: Posso criar novos agentes?
**R:** Sim! Adicione em `config/openclaw.template.json`:
```json
{
  "id": "novo-agent",
  "name": "Novo Agente",
  "description": "..."
}
```

### P: Como agentes se comunicam?
**R:** Via:
- **Memory MCP** — contexto compartilhado
- **Filesystem** — ler/escrever arquivos
- **GitHub** — issues, PRs, discussões

### P: Qual agente usar pra X?
**R:**
- Backend Node.js → **Tony Stark**
- Backend Python → **Bruce Banner**
- Arquitetura → **Steve Rogers**
- Product → **Stephen Strange**
- Data/IA → **Visão**
- Design/UX → **Wanda Maximoff**
- Infrastructure → **T'Challa**
- Mobile → **Scott Lang**
- Testing → **Natasha Romanoff**
- Content → **Peter Parker**

### P: Agentes funcionam 24/7?
**R:** Enquanto o Gateway estiver rodando, sim

---

## 🔌 MCP & Integrations

### P: Preciso configurar GitHub?
**R:** É opcional mas recomendado pra usar GitHub MCP (26 ferramentas)

### P: Posso adicionar outros MCP servers?
**R:** Sim!
```bash
openclaw mcp add <nome> --command ... --arg ...
```

### P: Como adiciono PostgreSQL?
**R:** Veja [MCP Servers](MCP-Servers) seção "PostgreSQL"

### P: O que é MCP?
**R:** Model Context Protocol — padrão pra LLMs acessarem ferramentas externas

---

## 💰 Custo & Performance

### P: Quanto custa rodar isso?
**R:** Depende do modelo:
- **Haiku:** $0.80/1M tokens (padrão — cheap)
- **Sonnet:** $3.00/1M tokens (só pra architecture/strategy)

**Estimativa mensal:** ~$300-400 pra 10 agentes ativos

### P: Como otimizar custo?
**R:** Phase 1 (ativa):
- Haiku default
- Sonnet APENAS pra Steve Rogers (arquitetura) + Stephen Strange (strategy)
- Thinking mode seletivo
- Batching de requests

Veja `OPTIMIZATION-PHASE1.md` no workspace

### P: Posso usar modelos open-source?
**R:** Sim! Configure Ollama, llama.cpp, etc em `openclaw.json`

---

## 🐛 Troubleshooting

### P: Gateway não inicia
**R:**
```bash
# Verifique porta
lsof -i :18789

# Se ocupada, use outra
openclaw gateway --port 28789

# Ou libera
kill -9 <PID>
```

### P: MCP server falha
**R:**
```bash
openclaw mcp doctor --probe
# Mostra qual servidor tem problema
```

### P: Agente sem resposta
**R:** 
- Verifique se Gateway está rodando
- Veja logs: `openclaw gateway --verbose`
- Teste connectivity: `openclaw agent --agent main --message "oi"`

### P: Token GitHub expirou
**R:**
1. Crie novo em https://github.com/settings/tokens/new
2. Configure:
```bash
export GITHUB_TOKEN=ghp_NOVO
openclaw mcp unset github
openclaw mcp add github --env GITHUB_TOKEN="$GITHUB_TOKEN"
```

### P: Memory MCP não salva
**R:** Memory é in-memory (não persistente entre restarts)

---

## 📊 Monitoramento

### P: Como ver o que agentes estão fazendo?
**R:**
```bash
# Veja logs detalhados
openclaw gateway --verbose

# Ou trace uma call
GIT_TRACE=1 openclaw agent --agent tony-stark --message "..."
```

### P: Posso auditar actions?
**R:** Sim, GitHub MCP registra tudo (commits, PRs, issues)

---

## 🔐 Segurança

### P: Preciso proteger secrets?
**R:** **SIM!** Nunca commite:
- `openclaw.json` com tokens
- `.github-token`
- `.env` files
- Database credentials

`.gitignore` protege automaticamente

### P: Como armazenar secrets seguro?
**R:**
```bash
# Opção 1: Arquivo local (não versionado)
echo "ghp_XXX" > ~/.openclaw/.github-token
chmod 600 ~/.openclaw/.github-token

# Opção 2: Environment variable
export GITHUB_TOKEN="ghp_XXX"

# Opção 3: Vault/secrets manager
```

### P: Posso restricionar qual agent usa qual MCP?
**R:** Não nativamente, mas você pode usar tool filters

---

## 🌍 Multi-Servidor

### P: Posso rodar em 2+ servidores?
**R:** Sim! Setup é idêntico:
```bash
git clone <repo>
./setup.sh
# Pronto
```

### P: Como compartilhar context entre servidores?
**R:**
- Memory MCP — salva em local server (não compartilhado por padrão)
- GitHub — repositório central
- Filesystem — rsync, NFS, ou commit pra GitHub

---

## 📈 Scaling

### P: Como escalar pra 50 agentes?
**R:**
1. Configure Kubernetes/Docker Compose
2. MCP servers em containers
3. PostgreSQL + Redis compartilhado
4. Memory MCP persistido em DB (customização)

### P: Máximo de agentes simultâneos?
**R:** Depende de:
- Poder de processamento
- Model provider rate limits
- Token budget

**Prático:** 10-20 agentes simultâneos por servidor

---

## 🎓 Learning

### P: Como aprender OpenClaw?
**R:** 
1. Leia [Getting Started](Getting-Started)
2. Explore [System Architecture](System-Architecture)
3. Consulte [OpenClaw Docs](https://docs.openclaw.ai)
4. Use agentes pra aprender:
```bash
openclaw agent --agent steve-rogers --message "Explique como funciona OpenClaw"
```

### P: Onde encontro documentação detalhada?
**R:**
- OpenClaw Docs: https://docs.openclaw.ai
- Wiki desse repo: [Home](Home)
- Workspace: `~/.openclaw/workspace/`

---

## 🤝 Contribuindo

### P: Posso contribuir com melhorias?
**R:** Sim! 
1. Fork o repositório
2. Crie branch `feature/xyz`
3. Submit pull request
4. Team revisa (Tony) + aprova (Steve)

### P: Posso compartilhar meus agents?
**R:** Sim! Abra uma issue ou PR

---

## 📞 Suporte

### Não encontrou resposta aqui?

1. **Procure em:** [Troubleshooting](Troubleshooting)
2. **Consulte agentes:**
   ```bash
   openclaw agent --agent steve-rogers --message "Como faço XYZ?"
   ```
3. **OpenClaw Docs:** https://docs.openclaw.ai
4. **GitHub Issues:** https://github.com/Team-Iron-Solutions/team-iron-jarvis-openclaw-config/issues

---

**Last Updated:** 2026-08-05
