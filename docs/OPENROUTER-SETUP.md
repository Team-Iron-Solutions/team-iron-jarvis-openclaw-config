# OpenRouter — Setup Guide

**Objetivo:** Configurar OpenRouter como fallback para redução de custo (Phase 2)  
**Economia estimada:** -75-95% quando fallback é acionado  
**Ref:** `TOKEN-OPTIMIZATION.md` (estratégia completa)

---

## Por Que OpenRouter?

- **Uma API key** para acessar Anthropic, Google, Mistral, DeepSeek e mais
- **Fallback automático** quando Anthropic está indisponível
- **`openrouter/auto`** roteia para o modelo mais barato disponível
- **`sort: "price"`** prioriza fornecedores mais baratos para mesmo modelo

---

## Setup (Nova Máquina)

### 1. Criar API Key

Acesse: https://openrouter.ai/keys

### 2. Configurar no OpenClaw

```bash
echo "<sua-key>" | openclaw models auth paste-api-key --provider openrouter
```

Confirme que foi salvo:
```bash
openclaw models auth list
# Deve aparecer: openrouter:manual (openrouter/api_key)
```

### 3. Verificar funcionamento

```bash
openclaw infer model run --local \
  --model openrouter/anthropic/claude-haiku-4-5 \
  --prompt "Reply with exactly: OPENROUTER_OK"
```

---

## Estratégia de Fallback (config/openclaw.template.json)

```json
"model": {
  "primary": "anthropic/claude-haiku-4-5",
  "fallbacks": [
    "openrouter/anthropic/claude-haiku-4-5",
    "openrouter/auto",
    "google/gemini-3.1-pro-preview"
  ]
}
```

**Ordem de prioridade:**
1. `anthropic/claude-haiku-4-5` — direto na Anthropic (padrão)
2. `openrouter/anthropic/claude-haiku-4-5` — mesmo modelo via OpenRouter (mais barato)
3. `openrouter/auto` — modelo mais barato disponível no momento
4. `google/gemini-3.1-pro-preview` — último recurso

---

## Modelos Úteis via OpenRouter

| Ref | Uso |
|-----|-----|
| `openrouter/anthropic/claude-haiku-4-5` | Haiku via OpenRouter (fallback principal) |
| `openrouter/anthropic/claude-sonnet-4-6` | Sonnet via OpenRouter (Steve/Strange fallback) |
| `openrouter/auto` | Roteamento automático para mais barato |
| `openrouter/openrouter/fusion` | Paralelo + síntese (para decisões críticas) |
| `openrouter/deepseek/deepseek-v4-flash` | Alternativa ultra-barata |

---

## Variáveis de Ambiente

```bash
# ~/.openclaw/openclaw.json (NÃO commitar)
{
  "env": {
    "OPENROUTER_API_KEY": "sk-or-v1-..."
  }
}
```

> **⚠️ NUNCA commitar a API key.** Ela fica em `~/.openclaw/openclaw.json` (local only).  
> O template em `config/openclaw.template.json` usa `${OPENROUTER_API_KEY}` como placeholder.

---

## Configuração Avançada (provider routing)

```json
"models": {
  "providers": {
    "openrouter": {
      "params": {
        "provider": {
          "sort": "price",
          "data_collection": "deny"
        }
      }
    }
  }
}
```

- `sort: "price"` → prioriza fornecedores mais baratos para o mesmo modelo
- `data_collection: "deny"` → não permite que OpenRouter use requests para treino

---

*Configurado em 30/08/2026.*
