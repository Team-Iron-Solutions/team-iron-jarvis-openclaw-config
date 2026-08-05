# 🦾 Team Iron Solutions - OpenClaw Wiki

Bem-vindo à wiki oficial do **team-iron-jarvis-openclaw-config**!

Essa é a documentação completa da arquitetura OpenClaw, agentes, playbooks e MCP servers da Team Iron Solutions.

---

## 📋 Índice Rápido

### 🚀 Começar
- **[Getting Started](Getting-Started)** — Setup em 5 minutos
- **[FAQ](FAQ)** — Perguntas frequentes
- **[Troubleshooting](Troubleshooting)** — Resolvendo problemas

### 🏗️ Arquitetura
- **[System Architecture](System-Architecture)** — Visão geral técnica
- **[Infrastructure](Infrastructure)** — Componentes (Gateway, Office, Claw3D)
- **[Voice & HUD](Voice-and-HUD)** — Pipeline de voz integrado

### 👥 Agentes
- **[10 Agents Overview](Agents-Overview)** — Quem são e o que fazem
- **[Agent Playbooks](Agent-Playbooks)** — Excellence guidelines
- **[Inter-Agent Workflows](Inter-Agent-Workflows)** — Como trabalham juntos

### 🔌 Integrations
- **[MCP Servers](MCP-Servers)** — memory, filesystem, github
- **[Channels](Channels)** — WhatsApp, Discord, Telegram, etc
- **[Adding New Tools](Adding-New-Tools)** — Expandir capacidades

### 📊 Operations
- **[Monitoring](Monitoring)** — Health checks e logs
- **[Scaling](Scaling)** — Multi-servidor, clusters
- **[Security](Security)** — Secrets, auth, compliance

### 🎓 Advanced
- **[Token Optimization](Token-Optimization)** — Phase 1 (Haiku-first)
- **[Custom Skills](Custom-Skills)** — Criar skills reusáveis
- **[CI/CD](CI-CD)** — Automação e testes

---

## 🎯 Versão

**Production OpenClaw Setup**
- **Version:** 2026-08-05
- **Status:** ✅ Production-ready
- **Agents:** 10/10 live
- **MCP Servers:** 3 configured (memory, filesystem, github)

---

## 🚀 Quick Start (TL;DR)

```bash
# Clone o repositório
git clone https://github.com/Team-Iron-Solutions/team-iron-jarvis-openclaw-config.git
cd team-iron-jarvis-openclaw-config

# Execute setup
chmod +x setup.sh
./setup.sh

# Configure token GitHub (opcional mas recomendado)
export GITHUB_TOKEN=***
openclaw mcp add github ...

# Teste um agente
openclaw agent --agent tony-stark --message "Olá!"
```

👉 **Quer mais detalhes?** Veja [Getting Started](Getting-Started)

---

## 📚 Documentação Completa

### Por Caso de Uso

**Quero...**
- ✅ **Replicar o ambiente** → [Getting Started](Getting-Started)
- ✅ **Entender a arquitetura** → [System Architecture](System-Architecture)
- ✅ **Usar os agentes** → [10 Agents Overview](Agents-Overview)
- ✅ **Integrar novo MCP** → [MCP Servers](MCP-Servers)
- ✅ **Monitorar saúde** → [Monitoring](Monitoring)
- ✅ **Escalar para produção** → [Scaling](Scaling)
- ✅ **Resolver problema** → [Troubleshooting](Troubleshooting)

### Por Papel

**Eu sou...**
- 👨‍💼 **Operador/DevOps** → [Getting Started](Getting-Started) → [Infrastructure](Infrastructure) → [Monitoring](Monitoring)
- 👨‍💻 **Desenvolvedor** → [System Architecture](System-Architecture) → [Adding New Tools](Adding-New-Tools) → [Custom Skills](Custom-Skills)
- 🏗️ **Arquiteto** → [System Architecture](System-Architecture) → [Inter-Agent Workflows](Inter-Agent-Workflows) → [Scaling](Scaling)
- 🤖 **Prompt Engineer** → [Agent Playbooks](Agent-Playbooks) → [Custom Skills](Custom-Skills)

---

## 🔗 Links Externos

- **OpenClaw Docs:** https://docs.openclaw.ai
- **GitHub Repo:** https://github.com/Team-Iron-Solutions/team-iron-jarvis-openclaw-config
- **Team Iron Solutions:** https://teamironsolutions.com.br
- **MCP Protocol:** https://modelcontextprotocol.io

---

## 📞 Suporte

**Perguntas?**
1. Procure em [FAQ](FAQ)
2. Veja [Troubleshooting](Troubleshooting)
3. Consulte os agentes:
   ```bash
   openclaw agent --agent steve-rogers --message "Como funciona XYZ?"
   openclaw agent --agent tony-stark --message "Isso tá bom pra production?"
   ```

---

**Last Updated:** 2026-08-05  
**Maintained by:** Team Iron Solutions 🦾
