# 🦾 Team Iron Solutions — OpenClaw Config

> Infrastructure as Code para replicar o ambiente completo de OpenClaw com 10 agentes, economia de tokens de 73-85% e integração de knowledge graphs.

**Status:** ✅ Production-ready | **Última atualização:** 30/08/2026

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
~/.openclaw/workspace/
│
├── 📄 AGENTS.md              ← Instruções do agente (lido pelo Gateway)
├── 📄 SOUL.md                ← Personalidade e tom
├── 📄 MEMORY.md              ← Memória de longo prazo
├── 📄 IDENTITY.md            ← Nome, emoji, avatar
├── 📄 TOOLS.md               ← Notas de ferramentas locais
├── 📄 USER.md                ← Contexto do usuário (Galvão)
├── 📄 HEARTBEAT.md           ← Checklist de heartbeat
│
├── 📄 SETUP.md               ← Guia de instalação em nova máquina
├── 📄 TOKEN-OPTIMIZATION.md  ← Estratégia completa de economia de tokens
├── 📄 README.md              ← Este arquivo
│
├── 🔧 caveman-middleware-esm.js  ← Phase 3: compressão de contexto (-45%)
├── 🔧 setup.sh                   ← Script de setup geral
├── 🔧 package-lock.json          ← Lock Node.js
├── 🔧 pyproject.toml             ← Dependências Python (Graphify)
├── 🔧 uv.lock                    ← Lock Python
│
├── 📁 agents-workspaces/     ← Playbooks por agente
│   ├── tony/EXCELLENCE-PLAYBOOK.md
│   ├── bruce/EXCELLENCE-PLAYBOOK.md
│   ├── steve/EXCELLENCE-PLAYBOOK.md
│   ├── stephen/EXCELLENCE-PLAYBOOK.md
│   ├── visao/EXCELLENCE-PLAYBOOK.md
│   ├── wanda/EXCELLENCE-PLAYBOOK.md
│   ├── tchalla/EXCELLENCE-PLAYBOOK.md
│   ├── scott/EXCELLENCE-PLAYBOOK.md
│   ├── natasha/EXCELLENCE-PLAYBOOK.md
│   └── peter/EXCELLENCE-PLAYBOOK.md
│
├── 📁 config/
│   └── openclaw.template.json    ← Template de configuração (sem secrets)
│
├── 📁 docs/
│   ├── CAVEMAN-INTEGRATION.md    ← Phase 3: guia de integração
│   ├── OPENROUTER-SETUP.md       ← Phase 2: setup OpenRouter
│   ├── GRAPHIFY-OVERVIEW.md      ← Phase 4: visão geral
│   ├── GRAPHIFY-SETUP.md         ← Phase 4: instalação
│   ├── GRAPHIFY-CHEATSHEET.md    ← Phase 4: referência rápida
│   ├── AGENTS-CAPABILITIES.md    ← Capacidades dos agentes
│   ├── adr/                      ← Architecture Decision Records
│   └── wiki/                     ← Wiki do projeto
│
└── 📁 scripts/
    └── setup-graphify.sh         ← Setup automatizado do Graphify
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

## 📚 Documentação

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
