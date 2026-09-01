# Model Escalation Protocol — Autorização Obrigatória

> ⚠️ REGRA INVIOLÁVEL: Nunca trocar para um modelo mais caro sem autorização explícita de Galvão.

---

## Hierarquia de Modelos (custo crescente)

```
Nível 1 — Primário do agente   (ex: Qwen2.5-Coder $0.07 | Haiku $0.80 | DeepSeek R1 $0.55)
Nível 2 — Fallback intermediário (ex: DeepSeek V3 $0.27 | Sonnet $3.00)
Nível 3 — Fallback premium      (ex: Sonnet $3.00 | Gemini 2.5 Pro $10.00)
Nível 4 — Local (gratuito)      (Ollama qwen3.5:9b — emergência)
```

Fallbacks (Nível 2+) são acionados **automaticamente apenas em falhas técnicas** (timeout, rate limit, erro de API).  
Troca por **complexidade da tarefa** → requer autorização humana.

---

## Quando pedir autorização

Antes de qualquer troca voluntária de modelo, avalie:

| Sinal | Ação |
|---|---|
| Task é boilerplate / CRUD / ajuste simples | ✅ Continua no modelo primário |
| Task é feature nova, refactor médio | ✅ Continua no modelo primário |
| Você travou após 2 tentativas no primário | 🔔 **Pede autorização** |
| Task envolve decisão arquitetural crítica | 🔔 **Pede autorização** |
| Bug em produção que você não consegue diagnosticar | 🔔 **Pede autorização** |
| Análise de segurança crítica | 🔔 **Pede autorização** |

---

## Como pedir autorização (template obrigatório)

```
Galvão, preciso de autorização para escalar o modelo nesta tarefa.

📋 Tarefa: [descrição em 1-2 linhas]
🤔 Motivo: [por que o modelo atual não é suficiente]
📈 Modelo solicitado: [nome do modelo]
💰 Custo estimado: [ex: ~$0.55/1M tokens vs $0.07/1M atual]
⏱️ Impacto: [ex: +$0.48/1M, estimativa +$0.02 nesta task]

Autoriza? (Sim / Não / Tenta mais uma vez com o modelo atual)
```

---

## Respostas possíveis de Galvão

- **"Sim" / "Autorizado" / "Pode"** → troca o modelo e executa
- **"Não" / "Tenta no atual"** → continua no primário, entrega o melhor possível e reporta limitações
- **Sem resposta em 5min** → continua no primário (nunca troca sem resposta)

---

## Escalação alternativa: delegar ao agente certo

Antes de pedir para subir de modelo, considere:

> "Essa task seria melhor com um agente diferente?"

| Se a task é... | Delegar para |
|---|---|
| Decisão arquitetural | Steve Rogers |
| Estratégia de produto | Stephen Strange |
| Análise de dados complexa | Visão |
| Design de solução | Steve Rogers + Wanda |

Delegar ao agente certo (que já tem o modelo adequado como primário) é **sempre preferível** a escalar modelo.

---

## Registro de escalações

Ao final de cada escalação (aprovada ou negada), registre em `memory/YYYY-MM-DD.md`:

```
## Escalação de Modelo
- Task: [descrição]
- Modelo solicitado: [modelo]
- Decisão: Aprovada / Negada
- Motivo: [motivo da decisão]
- Resultado: [o que foi entregue]
```

Isso ajuda Galvão a identificar padrões e ajustar a matriz de modelos se necessário.
