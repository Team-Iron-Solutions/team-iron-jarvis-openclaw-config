# Infra Changes — 05/09/2026

Mudanças aplicadas em produção (Mac mini de Team) e documentadas no IaC.

---

## 1. Modelo primário dos agentes — Haiku (200k ctx)

**Problema:** Qwen-2.5-Coder-32B tem 32k tokens de contexto. Sessões longas travavam com context overflow.

**Solução:** Haiku (200k ctx) como primário. Qwen como fallback para sessões novas e limpas.

| Agentes | Primary | Fallbacks |
|---|---|---|
| Tony, Bruce, Scott, Natasha, T'Challa, Visão | `anthropic/claude-haiku-4-5` | Qwen → DeepSeek V3 → auto |
| Steve Rogers | `anthropic/claude-sonnet-4-6` | DeepSeek R1 → auto |
| Stephen Strange | `openrouter/deepseek/deepseek-r1` | Sonnet → auto |
| Wanda, Peter | `anthropic/claude-haiku-4-5` | openrouter/auto → Gemini |
| Jarvis (main) | `anthropic/claude-haiku-4-5` | openrouter/haiku → auto → Gemini |

**Providers registrados** (fix `Unknown model` após 2026.8.1):
```json
"models": {
  "providers": {
    "anthropic": { "models": [haiku-4-5, sonnet-4-6, sonnet-5] },
    "google": { "models": [gemini-3.1-pro-preview] },
    "openrouter": { "params": { "provider": { "sort": "price" } } }
  }
}
```

---

## 2. Heartbeat — desabilitado em 10 agentes

**Problema:** 12 agentes × 30min = 576 turns/dia de heartbeat. Maioria retornava NO_REPLY.

**Solução:** Heartbeat apenas no `main`. Agentes de trabalho respondem on-demand.

```json
"agents": {
  "defaults": {
    "heartbeat": { "every": "30m", "lightContext": true, "isolatedSession": true }
  },
  "entries": {
    "main": { "heartbeat": { "every": "30m", "lightContext": true, "isolatedSession": true } }
    // demais agentes: sem heartbeat definido = não rodam
  }
}
```

**Economia:** -91% turns de heartbeat (576 → 48/dia)

---

## 3. Critical Task Reminder — otimizado

**Antes:** 8×/dia batendo na sessão main (207k tokens de contexto por run)
**Depois:** 3×/dia (07h, 13h, 19h) em sessão isolada (~2k tokens por run)

**Economia:** ~95% tokens do reminder

---

## 4. Canal Telegram configurado

**Configuração:**
```json
"channels": {
  "telegram": {
    "enabled": true,
    "tokenFile": "~/.openclaw/telegram.token",
    "dmPolicy": "allowlist",
    "allowFrom": ["${TELEGRAM_CHAT_ID}"]
  }
}
```

**Binding:**
```json
"bindings": [
  { "type": "route", "agentId": "main", "match": { "channel": "telegram" } }
]
```

**Setup:**
1. Criar bot via @BotFather no Telegram
2. Salvar token: `echo "TOKEN" > ~/.openclaw/telegram.token && chmod 600 ~/.openclaw/telegram.token`
3. Descobrir Chat ID via @userinfobot
4. Configurar `allowFrom` com o Chat ID
5. Fazer pairing: mandar msg pro bot → `openclaw pairing approve telegram <CODE>`

---

## 5. Automações reconfiguradas

| Automação | Antes | Depois |
|---|---|---|
| `phase5-daily-kpi-report` | Webhook localhost (falhava) | Telegram 20h, executa script real |
| `phase3-monitoring-daily` | WhatsApp sem número (falhava) | Telegram, lê métricas do workspace |
| `critical-task-reminder` | 8×/dia, sessão main | 3×/dia, isolated session |

---

## 6. Thresholds Phase 5B (06/09/2026)

Tony Stark e Bruce Banner ajustados para -40% (código imperativo vs declarativo):

```python
AGENT_COMPRESSION_MIN = {
    "Tony Stark": -40.0,   # Node.js imperativo
    "Bruce Banner": -40.0, # Python imperativo
}
```

Arquivo: `workspace/phase5-kpi-collect.py`
