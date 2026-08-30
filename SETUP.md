# SETUP.md — Team Iron Solutions
# Guia Completo de Instalação em Nova Máquina

**Tempo estimado:** 30-45 minutos  
**Sistema:** macOS (arm64 recomendado)  
**Resultado:** Ambiente completo com OpenClaw + 10 agentes + OpenRouter + Caveman + Graphify

---

## Pré-requisitos

| Ferramenta | Versão mínima | Instalação |
|-----------|--------------|------------|
| Node.js | v20+ | `nvm install 24` |
| npm | v10+ | incluso no Node |
| Python | 3.12+ | `brew install python@3.12` |
| uv | latest | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| Ollama | latest | https://ollama.ai/download |
| git | v2.30+ | `brew install git` |

### Verificar pré-requisitos

```bash
node --version    # v24.x.x
npm --version     # 10.x.x
python3 --version # 3.12.x
uv --version      # uv x.x.x
ollama --version  # ollama version x.x.x
git --version     # git version 2.x.x
```

---

## Parte 1 — OpenClaw

### 1.1 Instalar OpenClaw

```bash
npm install -g openclaw
openclaw --version
```

### 1.2 Onboarding inicial

```bash
openclaw onboard
```

Siga o fluxo interativo. Selecione **Anthropic** como provedor principal.

Você precisará de:
- **Anthropic API key** → https://console.anthropic.com/keys

### 1.3 Clonar este repositório

```bash
git clone https://github.com/Team-Iron-Solutions/team-iron-jarvis-openclaw-config.git \
  ~/.openclaw/workspace
```

> ⚠️ O workspace do OpenClaw deve estar em `~/.openclaw/workspace`.  
> Se já existe um workspace, faça backup antes de clonar.

### 1.4 Copiar e configurar o template

```bash
cp ~/.openclaw/workspace/config/openclaw.template.json ~/.openclaw/openclaw.json
```

Edite `~/.openclaw/openclaw.json` e substitua os placeholders:

| Placeholder | Valor |
|-------------|-------|
| `${OPENROUTER_API_KEY}` | Sua key do OpenRouter |
| `${GITHUB_TOKEN}` | Seu token do GitHub |
| `${OPEN…OKEN}` | Gateway auth token (gere um: `openssl rand -hex 32`) |
| `${ELEVENLABS_VOICE_ID}` | ID da voz ElevenLabs (opcional) |

### 1.5 Iniciar o Gateway

```bash
openclaw gateway start
openclaw status
```

Verifique que o Gateway está rodando na porta `18789`.

---

## Parte 2 — OpenRouter (Phase 2 Token Optimization)

OpenRouter é o fallback de modelos — aciona automaticamente quando Anthropic está indisponível ou para rotear para modelos mais baratos.

### 2.1 Obter API key

Acesse: https://openrouter.ai/keys

### 2.2 Configurar no OpenClaw

```bash
echo "sk-or-v1-..." | openclaw models auth paste-api-key --provider openrouter
```

### 2.3 Verificar

```bash
openclaw models auth list
# Deve aparecer: openrouter:manual (openrouter/api_key)
```

### 2.4 Testar

```bash
openclaw infer model run --local \
  --model openrouter/anthropic/claude-haiku-4-5 \
  --prompt "Reply: OPENROUTER_OK"
```

> 📖 Documentação completa: `docs/OPENROUTER-SETUP.md`

---

## Parte 3 — Caveman Middleware (Phase 3 Token Optimization)

Caveman comprime prompts antes de enviar ao modelo — -45% tokens sem perda de qualidade.

### 3.1 O middleware já está no repo

```bash
ls ~/.openclaw/workspace/caveman-middleware-esm.js
# caveman-middleware-esm.js ✅
```

### 3.2 Integração via jarvis-bridge

Caveman é usado pelo `jarvis-bridge-v4.js` (projeto `jarvis-neural-interface`):

```javascript
import CavemanMiddleware from './caveman-middleware-esm.js';

const caveman = new CavemanMiddleware({ mode: 'aggressive', verbose: true });

async function callAgent(rawMessage) {
  const compressed = await caveman.compressInput(rawMessage);
  // send compressed.message to OpenClaw instead of rawMessage
  console.log(`Compression: -${compressed.metadata.compression_ratio}%`);
}
```

### 3.3 Modos disponíveis

| Modo | Compressão | Uso |
|------|-----------|-----|
| `aggressive` | ~-45% | Default — code reviews, análises |
| `moderate` | ~-30% | Tasks onde precisão é crítica |
| `conservative` | ~-10% | Mínimo — apenas whitespace |

> 📖 Documentação completa: `docs/CAVEMAN-INTEGRATION.md`

---

## Parte 4 — Graphify (Phase 4 Token Optimization)

Graphify converte código em knowledge graphs (AST) antes de enviar ao agente — -40 a -90% tokens dependendo do tipo de código.

### 4.1 Setup automatizado

```bash
cd ~/.openclaw/workspace
bash scripts/setup-graphify.sh
```

O script irá:
1. ✅ Verificar Python 3.12+ e uv
2. ✅ Instalar dependências Python (`graphifyy`, `tree-sitter`, `ollama`)
3. ✅ Baixar modelo Ollama (`qwen3.5:4b`)
4. ✅ Validar integração Graphify + Ollama
5. ✅ Criar `.env` local

### 4.2 Setup manual (se o script falhar)

```bash
cd ~/.openclaw/workspace

# Instalar uv (se não tiver)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Instalar dependências Python
uv sync

# Baixar modelo Ollama
ollama pull qwen3.5:4b

# Verificar
uv run python -c "import graphifyy; print('Graphify OK')"
```

### 4.3 Resultado esperado por tipo de código

| Contexto | Compressão |
|----------|-----------|
| Flutter / declarativo | -89.9% |
| Documentação | -69.4% |
| SQL / Data | -66.3% |
| IaC / Terraform | -58.8% |
| Arquitetura | -55.6% |
| Python / imperativo | -47.5% |
| Node.js / imperativo | -43.1% |

> 📖 Documentação completa: `docs/GRAPHIFY-SETUP.md` e `docs/GRAPHIFY-OVERVIEW.md`

---

## Parte 5 — Agentes

### 5.1 Verificar agentes configurados

```bash
openclaw agents list
```

Deve listar 11 agentes: `main` (Jarvis) + 10 do squad.

### 5.2 Playbooks por agente

Cada agente tem seu playbook em `agents-workspaces/<nome>/EXCELLENCE-PLAYBOOK.md`.

```bash
ls ~/.openclaw/workspace/agents-workspaces/
# bruce/ natasha/ peter/ scott/ stephen/
# steve/ tchalla/ tony/ visao/ wanda/
```

### 5.3 Testar um agente

```bash
openclaw chat --agent tony-stark "Faça um code review rápido: const x = 1; console.log(x)"
```

---

## Parte 6 — Verificação Final

```bash
# Gateway rodando?
openclaw status

# Modelos disponíveis?
openclaw models list | grep -E "haiku|sonnet|openrouter"

# OpenRouter configurado?
openclaw models auth list | grep openrouter

# Agentes OK?
openclaw agents list | wc -l  # deve retornar 11+

# Graphify OK?
cd ~/.openclaw/workspace
uv run python -c "import graphifyy; print('✅ Graphify ready')"

# Caveman OK?
node -e "import('./caveman-middleware-esm.js').then(m => console.log('✅ Caveman ready'))"
```

---

## Estrutura do Repositório

```
~/.openclaw/workspace/
│
├── AGENTS.md              ← Instruções do agente (lido pelo Gateway)
├── SOUL.md                ← Personalidade e tom
├── MEMORY.md              ← Memória de longo prazo
├── IDENTITY.md            ← Nome, emoji, avatar
├── TOOLS.md               ← Notas de ferramentas locais
├── USER.md                ← Contexto do usuário
├── HEARTBEAT.md           ← Checklist de heartbeat
├── TOKEN-OPTIMIZATION.md  ← Guia completo de economia de tokens
├── README.md              ← Documentação do repo
├── SETUP.md               ← Este arquivo
│
├── caveman-middleware-esm.js  ← Phase 3: compressão de contexto
├── setup.sh                   ← Script de setup geral
├── pyproject.toml             ← Dependências Python (Graphify)
├── uv.lock                    ← Lock file Python
├── package-lock.json          ← Lock file Node
│
├── agents-workspaces/     ← Playbooks por agente (10 agentes)
│   ├── tony/
│   ├── bruce/
│   └── ...
│
├── config/
│   └── openclaw.template.json  ← Template de configuração
│
├── docs/                  ← Documentação técnica
│   ├── CAVEMAN-INTEGRATION.md
│   ├── OPENROUTER-SETUP.md
│   ├── GRAPHIFY-SETUP.md
│   ├── GRAPHIFY-OVERVIEW.md
│   ├── GRAPHIFY-CHEATSHEET.md
│   ├── TOKEN-OPTIMIZATION.md
│   ├── adr/               ← Architecture Decision Records
│   └── wiki/              ← Wiki do projeto
│
├── scripts/
│   └── setup-graphify.sh  ← Setup automatizado do Graphify
│
└── shared/
    └── EXCELLENCE-CHECKLIST.md
```

---

## Troubleshooting

### Gateway não inicia

```bash
openclaw gateway status
openclaw doctor
```

### OpenRouter retorna 401

```bash
# Verificar key configurada
openclaw models auth list

# Reconfigurar
echo "sk-or-v1-..." | openclaw models auth paste-api-key --provider openrouter
```

### Graphify falha ao instalar

```bash
# Verificar Python version
python3 --version  # deve ser 3.12+

# Reinstalar uv e sync
curl -LsSf https://astral.sh/uv/install.sh | sh
cd ~/.openclaw/workspace && uv sync
```

### Ollama não encontrado

```bash
# Instalar Ollama
open https://ollama.ai/download

# Ou via brew
brew install ollama

# Iniciar serviço
ollama serve &
ollama pull qwen3.5:4b
```

---

## Economia de Tokens (resumo)

| Otimização | Economia | Status |
|-----------|----------|--------|
| Phase 1: Haiku default | -60% vs all-Sonnet | ✅ Ativo |
| Phase 2: OpenRouter fallback | -75-95% quando acionado | ✅ Configurado |
| Phase 3: Caveman compression | -45% por request | ✅ Live |
| Phase 4: Graphify knowledge graphs | -43 a -90% em code review | ✅ Live |
| **Total combinado** | **~73-85%** | ✅ |

> 📖 Detalhes completos: `TOKEN-OPTIMIZATION.md`

---

*Mantido por: Jarvis 🦾 — Team Iron Solutions*  
*Última atualização: 30/08/2026*
