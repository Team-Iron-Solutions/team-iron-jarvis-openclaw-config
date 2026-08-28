# Ollama + Graphify Integration

**Data:** 26 de agosto de 2026  
**Status:** ✅ Testando em produção  

---

## Por Que Ollama?

**Critério de Escolha:**
1. ✅ Localmente hospedado (offline, sem dependência externa)
2. ✅ Sem custos (roda no Mac mini, zero API calls)
3. ✅ Nativo no Graphifyy (suporte oficial)
4. ✅ Modelos disponíveis (qwen3.5, llama3.2)
5. ✅ Já instalado no Mac mini

**Alternativas Rejeitadas:**
- ❌ OpenAI API — custa $, requer chave, dependência externa
- ❌ LM Studio — alternativa, mas Ollama já disponível
- ❌ Modo AST-only — funciona, mas perde semantic extraction

---

## Setup (Já Feito)

### 1. Ollama instalado
```
✅ /usr/local/bin/ollama v0.33.0
✅ Modelos disponíveis:
  - qwen3.5:9b (6.6 GB, melhor qualidade)
  - qwen3.5:4b (3.4 GB, recomendado)
  - qwen3.5:2b (2.7 GB, mais rápido)
  - llama3.2:3b (2.0 GB, alternativa)
```

### 2. Graphifyy com Ollama
```bash
# Instalação
uv pip install graphifyy

# Uso
graphify . \
  --output output_dir \
  --backend ollama \
  --model qwen3.5:4b \
  --max-concurrency 1
```

---

## Performance Esperada

| Métrica | Valor |
|---|---|
| **First run (12k files)** | 20-30 min |
| **Subsequent runs (incremental)** | 5-10 min |
| **Per-file semantic extraction** | 2-5s (via Ollama) |
| **Graph query latency** | <100ms |
| **Total tokens used** | 0 API tokens (local) |

---

## Integração com Agentes

### Tony Stark (Code Review)

**Workflow:**
```
1. Galvão: "Tony, revisa api/routes.js"
2. Tony: 
   - Executa: graphify explain "ApiRouter"
   - Obtém: < 500 tokens (vs 2000 sem grafo)
   - Economia: -75%
3. Resultado: Análise profunda, contexto comprimido
```

### Teste Comparativo
```bash
# Sem Graphify
openclaw agent --agent tony --prompt "Revisa api/routes.js"
→ read api/routes.js → 2000 tokens
→ Analisa, time: 45s

# Com Graphify + Ollama
openclaw agent --agent tony --prompt "Usa graphify explain para API Router"
→ graphify explain "ApiRouter" → 500 tokens
→ Análise, time: 20s
→ Economia: -75% tokens, -56% latência
```

---

## Troubleshooting

### Problema: "OPENAI_API_KEY error"
**Solução:** Use `--backend ollama --model qwen3.5:4b` (ignora OpenAI)

### Problema: Ollama não responde
**Verificação:**
```bash
curl http://localhost:11434/api/tags
# Se falhar, inicie Ollama:
ollama serve
```

### Problema: Grafo muito grande (>100MB)
**Otimizações:**
- Use `qwen3.5:2b` em vez de `4b` (mais rápido)
- Aumente `--max-concurrency` (padrão: 1)
- Considere split por módulo

---

## Roadmap Fase 4

| Sprint | Objetivo | LLM |
|---|---|---|
| 1 | Setup + test repo | ✅ Ollama |
| 2 | Tony Stark integration | ✅ Ollama |
| 3 | Tier 1 rollout (Tony, Bruce, Steve) | ✅ Ollama |
| 4 | Tier 2 rollout (Scott, Wanda, Natasha) | ✅ Ollama |
| 5 | Monitoring + full deployment | ✅ Ollama |

**Custo total Phase 4:** $0 (Ollama local)

---

## Arquivos Relacionados

- `GRAPHIFY-PHASE4.md` — planejamento estratégico
- `GRAPHIFY-PHASE4-SPRINT1-LOG.md` — log desta sessão
- `PHASE4-STATUS.md` — status agregado
- `graphify-env/` — virtual environment com graphifyy

---

**Decisão final:** Ollama é a solução ideal — local, grátis, nativo, sem complexidade.
