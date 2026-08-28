# Phase 4 — Contexto Técnico para Steve Rogers

**Para:** Steve Rogers (Arquiteto)  
**De:** Jarvis + Galvão  
**Data:** 26 de agosto de 2026, 14:15 GMT-3  
**Urgência:** Review de arquitetura antes de Sprint 2


---

## 📚 Referência: Conceitos de AST e Tree-Sitter

Para entender os fundamentos de tree-sitter, AST puro, e semântica:

→ **[[AST-TreeSitter-Semantica.md]]** (Obsidian)

Este documento explica:
- Por que tree-sitter é sempre AST puro (zero LLM)
- Trade-offs entre estrutura (tree-sitter) e semântica (Ollama)
- Como Graphifyy combina ambos
- Exemplos práticos com código

**Ideal para:**
- Entender por que --skip-semantic não funcionou em Sprint 1
- Validar por que qwen3.5:4b é suficiente
- Documentar arquitetura para futuros agentes

---

## 🎯 O Problema

**Baseline:** Quando agentes fazem code review, carregam MUITO contexto:

```python
# Tony Stark fazendo code review
→ read api/routes.js (2000 tokens)
→ read api/middleware.js (1500 tokens)
→ read types/index.ts (1000 tokens)
→ ... (5-10 mais arquivos)
→ TOTAL: 10.000+ tokens POR REVIEW

# Frequência: 3 agentes × 2 reviews/dia × 20 dias = 120 reviews/mês
# = 1.2M tokens/mês gasto APENAS em context loading
```

**Objetivo Phase 4:** Reduzir esse "context loading tax" via knowledge graphs.

---

## ✅ Solução Proposta

### Arquitetura (Current)

```
┌─────────────────────────────────────────┐
│ Repo (Node.js, Python, Dart, etc)       │
├─────────────────────────────────────────┤
│ Graphifyy (tree-sitter AST extractor)   │ ← Parse código
├─────────────────────────────────────────┤
│ Ollama Local (qwen3.5:4b)               │ ← Semantic extraction
├─────────────────────────────────────────┤
│ graph.json (500MB avg)                  │ ← Queryable cache
├─────────────────────────────────────────┤
│ Agent (Tony, Bruce, Steve, etc)         │
└─────────────────────────────────────────┘
       ↓
   graphify explain "Class"
   graphify path "A" "B"
   graphify query "type:function"
       ↓
   (200-500 tokens vs 2000-10000)
```

### Stack Decisões

| Decisão | Opção Selecionada | Razão |
|---|---|---|
| **LLM backend** | Ollama local | Zero custo, offline, nativo em graphifyy |
| **Modelo LLM** | qwen3.5:4b | Balanço qualidade/velocidade (3.4GB) |
| **Graph storage** | JSON local | Simples, cacheável, no git (com .gitignore) |
| **Query interface** | CLI (`graphify explain`) | Direto, shell-friendly, sem wrapper |
| **Integração agentes** | Via `exec()` calls | Nativo OpenClaw, sem mudança de infra |

### Alternativas Rejeitadas

| Alternativa | Por Que Não |
|---|---|
| **OpenAI API** | Custo (~$0.01-0.05/grafo), dependência externa |
| **LM Studio** | Funciona mas Ollama já disponível, menos integrado |
| **Code2vec** | Menos semântica, mais viés de embedding |
| **Custom AST** | Muito esforço, Graphifyy já battle-tested |
| **Joern** | Foco em vulnerabilities, não em navegação de código |

---

## 📊 Trade-offs Phase 4

### ✅ Benefícios

| Benefício | Medida | Impacto |
|---|---|---|
| **Token reduction** | -50-95% por review | -$0.46/mês por agente |
| **Latência** | -50-60% (menos tokens) | Reviews 2x mais rápidos |
| **Escalabilidade** | Linear c/ agentes | 6 agentes = 6x economia |
| **Offline** | Zero dependência | Funciona sem internet |
| **Costo operacional** | $0 | Ollama local, sem APIs |

### ⚠️ Riscos

| Risco | Probabilidade | Impacto | Mitigação |
|---|---|---|---|
| **Tree-sitter parsing fail** | Baixa | Médio | Fallback para `read` |
| **Grafo desatualizado** | Média | Médio | `graphify update` automático ou manual |
| **Ollama crash** | Baixa | Alto | Monitorar, fallback simples read |
| **Graph cresce muito** | Baixa | Médio | Comprimir ou split por module |
| **Agentes não adotam** | Média | Alto | Playbook claro, incentivos |

### 💰 Custo vs Benefício

**Setup (uma vez):**
- Python 3.12: 2 min
- Graphifyy: 1 min
- Per-repo graph build: 15-30 min (Ollama)
- Total: ~30-45 min por repo, parallelizável

**Ongoing:**
- Graph update: 5-10 min quando mudança major
- Zero API costs
- Minimal maintenance

**ROI (break-even):**
- 5 reviews com graphify vs 5 sem = economiza ~$2.30 no mês
- Com 120 reviews/mês = -$55/mês por agente
- 6 agentes = -$330/mês (-$3,960/ano)

---

## 🏗️ Questões Arquiteturais para Steve

1. **Multi-repo support?**
   - Agentes precisam revisar múltiplos repos?
   - Precisa de central graph store ou por-repo?

2. **Incremental updates?**
   - Quando grafo fica obsoleto?
   - Auto-rebuild ou manual trigger?

3. **Integration points?**
   - Envolver em `openclaw agent` natively?
   - Ou agentes descobrem `graphify-env` + comandos?

4. **Failure modes?**
   - Se Ollama cair, agents caem também?
   - Precisa circuit breaker?

5. **Scale?**
   - Repos >100k LOC, Ollama aguenta?
   - Split em microservices ou fica local?

6. **Quality gates?**
   - Como validar que graphify está entregando qualidade?
   - Teste automático?

---

## 📋 Sprint 1 Status (Real-time)

```
Graphifyy em execução AGORA
├─ Input: OpenJarvis (12,961 Python files, 1.5GB)
├─ Backend: Ollama qwen3.5:4b (local)
├─ Started: 14:07 GMT-3
├─ Duration: ~20 min
├─ ETA: 5-10 min mais
└─ Purpose: Proof of concept, validar performance
```

**Quando terminar:**
1. ✅ Medir tempo de build
2. ✅ Medir tamanho graph.json
3. ✅ Testar 10 queries (`explain`, `path`, `query`)
4. ✅ Medir token reduction real vs estimado

**Resultado esperado:**
- Graph buildado em <30 min ✅
- Queries <5s latência ✅
- Token reduction -50-80% ✅

---

## 🎯 Decisão Necessária (para Steve)

**Nível de confiança:**
- 🟢 **GO** — Arquitetura sólida, prosseguir Sprint 2
- 🟡 **CAUTION** — Ajustes recomendados antes de rollout
- 🔴 **STOP** — Risco alto, repensar approach

**Esperamos:** Análise decisiva (não genérica), com recomendações específicas.

---

## 📁 Documentação de Referência

- `GRAPHIFY-PHASE4.md` — estratégia geral (5 sprints)
- `OLLAMA-GRAPHIFY-INTEGRATION.md` — setup técnico
- `PHASE4-AGENT-PLAYBOOK.md` — como agentes usam
- `PHASE4-STATUS.md` — status agregado

---

**Próxima ação:** Steve fornece análise → Jarvis + Galvão refinam plano → Sprint 2 procede (ou pivota).
