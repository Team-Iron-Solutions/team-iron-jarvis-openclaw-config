# Phase 4 — Sprint 1 Discovery & Pivô

**Data:** 26 de agosto de 2026  
**Status:** 🟡 EM PROGRESSO  
**Decisão Crítica:** OpenJarvis FALHOU → Pivô para jarvis-neural-interface

---

## 🔴 OpenJarvis Build — FALHOU

### Tentativa 1: Ollama qwen3.5:4b
- **Repo:** OpenJarvis (12,961 Python files, 1.5GB)
- **Backend:** Ollama local
- **Modelo:** qwen3.5:4b
- **Resultado:** ❌ FALHOU
- **Evidência:** Cache semântico criado, mas graph.json final não gerado
- **Tempo:** ~40 min, sem retorno de sucesso

### Lição Aprendida

OpenJarvis é **GRANDE DEMAIS** para primeiro teste:
- 12k files = processamento muito longo
- Difícil diagnosticar falha (qual arquivo causou erro?)
- Sem feedback rápido (não sabemos se modelo está certo até fim)

**Steve Rogers estava certo:** "Um spike deve ser rápido, reversível e isolado."

---

## 🟢 PIVÔ: jarvis-neural-interface

### Por que este repo

| Critério | jarvis-neural-interface |
|---|---|
| Size | ~200-500 files (vs 12k) |
| Language | Node.js (familiar a Tony) |
| Nomenclatura | Descritiva (classes com nomes claros) |
| Dependências | Tem múltiplas relações para testar `graphify path` |
| Tempo build | ~5-10 min (vs 30+ min) |

**Resultado esperado:** Graph.json em <10 min, validação rápida, aprendizado antes de escalizar.

---

## 📋 Sprint 1 — Novo Plano

### Etapa 1: Build com qwen3.5:9b (RECOMENDADO)

```bash
cd ~/.openclaw/workspace/jarvis-neural-interface
source ~/.openclaw/workspace/graphify-env/bin/activate

# Steve Rogers diz: use 9b, não 4b
graphify . \
  --output graphify-out \
  --backend ollama \
  --model qwen3.5:9b \
  --max-concurrency 1
```

**ETA:** 8-12 min build
**Esperado:** graph.json < 50MB

### Etapa 2: Validação com Checklist

Ver `PHASE4-VALIDATION-CHECKLIST.md`:
- [ ] graph.json existe?
- [ ] Size < 100MB?
- [ ] Parseable como JSON?
- [ ] 10 test queries funcionam?
- [ ] Token reduction real vs estimado?

### Etapa 3: Decisão

Se sucesso → prosseguir Sprint 2 (Tony Stark baseline)  
Se falha → ajustar e iterar

---

## ⚙️ Próxima Ação

**Paralelo:**
1. OpenJarvis v2 ainda rodando (tentativa 2)
2. Você quer que eu inicie jarvis-neural-interface build AGORA?

**Resultado esperado:**
- Rápido feedback (10 min vs 40 min)
- Validação do approach antes de escalar
- Data point para decisão Sprint 3
