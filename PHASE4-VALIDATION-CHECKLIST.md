# Phase 4 Sprint 1 — Validation Checklist

**Data:** 26 de agosto de 2026  
**Próximo:** Executar quando `graphify-out-phase4/graph.json` existir  

---

## ✅ Build Validation

### graph.json existe?
- [ ] Arquivo criado
- [ ] Size: _________ MB
- [ ] Format válido (parseável como JSON)

```bash
# Testar
cd OpenJarvis
ls -lh graphify-out-phase4/graph.json
head -c 500 graphify-out-phase4/graph.json | python -m json.tool
```

### Outro output?
- [ ] `GRAPH_REPORT.md` gerado?
- [ ] `graph.html` (visualization)?
- [ ] Cache AST (`cache/ast/`)?

---

## 📊 Performance Metrics

### Build Performance
- [ ] Build time: _________ segundos
- [ ] Files processed: _________ (esperado: ~12k)
- [ ] Semantic extraction: SUCCESS / PARTIAL / FAILED
- [ ] Tree-sitter parse rate: _________ files/sec

```bash
# Medir tempo na próxima vez
time graphify . --backend ollama --model qwen3.5:4b
```

### Graph Stats
- [ ] Total nodes: _________
- [ ] Total edges: _________
- [ ] Graph density: _________ %
- [ ] Largest component: _________ nodes

```bash
# Extrair stats de graph.json
python3 -c "
import json
with open('graphify-out-phase4/graph.json') as f:
    g = json.load(f)
    print(f'Nodes: {len(g[\"nodes\"])}')
    print(f'Edges: {len(g[\"edges\"])}')
"
```

---

## 🧪 Query Tests (Sample 10)

### Test 1: graphify explain
```bash
graphify explain "main"
# ✅ Retorna? ________
# Tokens estimado: ________
# vs read archivo: ________
# Economia: _______%
```

### Test 2: graphify path
```bash
graphify path "ClassA" "ClassB"
# ✅ Caminho encontrado?
# ✅ Transitive works?
```

### Test 3: graphify query
```bash
graphify query "type:function language:python"
# ✅ Retorna resultados?
# Contagem: _________
```

### Tests 4-10: Seu próprio teste
```bash
graphify explain "_______"
→ Tokens: ______ vs read: ______ (economia: _____%)

graphify path "_______" "_______"
→ Success? ____

graphify query "_______"
→ Resultados: _____
```

---

## 📈 Token Reduction Real

### Code Review Simulation

**Cenário:** Review de componente principal

```python
# SEM Graphify
read arquivo1.py  # 1200 tokens
read arquivo2.py  # 1100 tokens
read arquivo3.py  # 900 tokens
read arquivo4.py  # 850 tokens
read arquivo5.py  # 750 tokens
TOTAL: 4,800 tokens
Time: 45s

# COM Graphify
graphify explain "MainComponent"  # 250 tokens
graphify path "MainComponent" "*"  # 180 tokens
TOTAL: 430 tokens
Time: 8s

# RESULTADO
Economia: -91% tokens (-$0.003)
Latência: -82% tempo
```

### Metrics to Record
- [ ] Arquivo/componente testado: _________
- [ ] Tokens COM graphify: _________
- [ ] Tokens SEM graphify: _________
- [ ] % economia: _________%
- [ ] Latência COM: _________ s
- [ ] Latência SEM: _________ s

---

## ⚠️ Quality Checks

### Semantic Accuracy
Para cada `graphify explain` teste, validar manualmente:
- [ ] Informação retornada está correta?
- [ ] Alguma dependência missing?
- [ ] False positives?

### Fallback Behavior
```bash
# Testar comportamento sem Ollama
pkill ollama
graphify explain "Class"
# ✅ Graceful failure? ________
# ✅ Útil mesmo sem semantic? ________
```

### Incremental Updates
```bash
# Fazer mudança ao arquivo
echo "# comment" >> src/main.py

# Update graph
graphify update .

# Verificar se atualizado
graphify explain "main"
# ✅ Mudança refletida? ________
```

---

## 🔄 Comparison vs Baseline

| Métrica | Target | Resultado | Status |
|---|---|---|---|
| Build time | <30 min | _________ | ✅/❌ |
| Graph size | 100-500MB | _________ | ✅/❌ |
| Query latency | <5s | _________ | ✅/❌ |
| Token economy | -50% avg | _________ % | ✅/❌ |
| Parse success | >95% | _________ % | ✅/❌ |

---

## 📋 Sign-off

### Validação Completa?
- [ ] Todos testes passaram
- [ ] Métricas dentro de target
- [ ] Documentação atualizada
- [ ] Resultados commitados

### Próximas Fases OK?
- [ ] Steve Rogers review completado
- [ ] Playbook validado
- [ ] Sprint 2 pronto (Tony Stark integration)

### Decisão: GO / CAUTION / STOP
```
DECISÃO: [ ] GO → prosseguir Sprint 2 hoje
         [ ] CAUTION → ajustes primeiro
         [ ] STOP → repensar approach
```

---

**Owner:** Jarvis  
**Executor:** Você (quando graph.json existir)  
**Tempo estimado:** 10-15 minutos
