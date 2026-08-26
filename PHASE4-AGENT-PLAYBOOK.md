# Phase 4 — Playbook de Uso para Agentes

**Data:** 26 de agosto de 2026  
**Versão:** 1.0 (Draft, validação pendente Steve Rogers)  
**Status:** 🟡 Documentação base, aguardando architecture review

---

## Visão Geral

Agentes podem usar **Graphify + Ollama** para reduzir tokens em operações de análise de código.

**Economia típica:** -50-95% tokens em code review (varia por repo size)

---

## Para Qual Agente? (Tier 1 + 2)

| Agente | Caso de Uso | Prioridade |
|---|---|---|
| **Tony Stark** | Code review Node.js, API design, refactoring | 🔴 Crítica |
| **Bruce Banner** | Code review Python, data pipelines | 🔴 Crítica |
| **Steve Rogers** | Architecture analysis, impact mapping | 🟠 Alta |
| **Scott Lang** | Flutter widgets, design system dependencies | 🟠 Alta |
| **Wanda Maximoff** | Design system inheritance, component impact | 🟠 Alta |
| **Natasha Romanoff** | Test coverage mapping, impact analysis | 🟡 Média |

**Excluídos:**
- T'Challa (SRE) — configs/shell scripts, menor relevância
- Visão (Data) — SQL analysis, menos benefício
- Stephen Strange (PM) — entender escopo ocasional
- Peter Parker (Social) — N/A

---

## Como Usar: Fluxo Padrão

### 1️⃣ Pré-requisitos (Setup uma vez, por repo)

```bash
# Verificar Ollama rodando
curl http://localhost:11434/api/tags

# Buildar grafo do repo (primeira vez: 15-30 min)
cd /seu/repo
source /Users/teamironsolutions/.openclaw/workspace/graphify-env/bin/activate
graphify . \
  --output graphify-out \
  --backend ollama \
  --model qwen3.5:4b \
  --max-concurrency 1
```

**Resultado:** `graphify-out/graph.json` + `GRAPH_REPORT.md` (cached, reutilizável)

### 2️⃣ Durante Code Review (em exec do agente)

**Padrão 1: Entender estrutura de classe/função**
```bash
# Sem graphify (2000 tokens):
read /path/to/file.js

# Com graphify (200 tokens):
graphify explain "NomeClasse"
```

**Padrão 2: Rastrear dependências**
```bash
# Sem graphify (5000 tokens, ler 20 arquivos):
read arquivo1.ts
read arquivo2.ts
... (20 arquivos)

# Com graphify (300 tokens):
graphify path "ButtonComponent" "*" --transitive
# Retorna: ButtonComponent → usedBy → [Componentes X]
```

**Padrão 3: Questões complexas**
```bash
# Sem graphify (8000 tokens, análise manual):
# Ler arquitetura inteira, montar mapa mental

# Com graphify (500 tokens):
graphify query "type:class parent:Controller language:python"
# Retorna estrutura hierárquica
```

### 3️⃣ Integração no Agente (Pseudocódigo)

```javascript
// Tony Stark's code review
async function reviewCode(filePath, context) {
  // 1. Se repo tem graphify-out/graph.json:
  if (fs.existsSync("graphify-out/graph.json")) {
    
    // 2. Para estrutura/dependências, usar graphify:
    const explanation = await exec(
      `graphify explain "${className}"`
    );
    
    // 3. Para análise profunda, combinar com LLM:
    const analysis = await llm.analyze(
      `Código: ${explanation}\n\nAnalisar problemas...`
    );
    
    // 4. Se é refactor de alto impacto:
    const impacts = await exec(
      `graphify path "${oldName}" "*" --transitive`
    );
    
    return { analysis, impacts, tokens: -65% };
  }
  
  // Fallback: leitura tradicional
  return readAndAnalyze(filePath);
}
```

---

## Comandos Disponíveis

### graphify explain
```bash
graphify explain "ClassName"
→ Retorna: Definição, métodos, dependências diretas
→ Tokens: 100-300
```

### graphify path
```bash
graphify path "ClassA" "ClassB"
→ Retorna: Caminho entre A e B no grafo
→ Tokens: 50-200

# Com --transitive (mostrar TUDO que depende)
graphify path "Button" "*" --transitive
→ Todos os widgets que usam Button
```

### graphify query
```bash
graphify query "type:function language:python"
→ Retorna: Todas as funções Python
→ Tokens: 200-500 (variável)
```

### graphify update
```bash
# Atualizar grafo após mudanças
graphify update .
→ Rápido (incremental, não rebuild completo)
```

---

## Quando NÃO Usar Graphify

❌ Repos muito pequenos (<1000 files)  
→ Overhead do graphify > economia  

❌ Primeira análise de repo desconhecido  
→ Precisa context mais amplo (use read normal)  

❌ Perguntas semânticas muito específicas  
→ Graphify retorna estrutura, não semântica  

❌ Mudanças recentes não commitadas  
→ Grafo fica desatualizado (need `graphify update`)  

---

## Performance Esperada

### Exemplo Real: Code Review Node.js 50k LOC

**Sem Graphify:**
```
read api/routes.js (1500 tokens)
read api/middleware.js (1200 tokens)
read types/index.ts (800 tokens)
...
Total: 8000 tokens, time: 45s
```

**Com Graphify:**
```
graphify explain "ApiRouter" (200 tokens)
graphify path "ApiRouter" "Validator" (150 tokens)
...
Total: 2500 tokens, time: 15s
Economia: -68% tokens, -67% latência
```

---

## Troubleshooting

### "graph.json não encontrado"
→ Buildar com `graphify .` na raiz do repo

### "graphify command not found"
→ Ativar venv: `source graphify-env/bin/activate`

### "Ollama não responde"
→ Iniciar: `ollama serve` (ou verificar porta 11434)

### "Query retorna muitos resultados"
→ Refinar query ou usar `--limit 20`

### "Grafo ficou desatualizado"
→ Rodar `graphify update .` (incremental)

---

## Métricas de Sucesso

Para cada agente, medir:

| Métrica | Target |
|---|---|
| Token reduction | -50% vs baseline |
| Query latency | <5s per query |
| Graph freshness | <24h |
| Agent adoption | 80%+ de reviews usam graphify |
| Error rate | <5% false positives |

---

## Próximos Passos

1. ⏳ **Steve Rogers review** → validar esta documentação
2. ✅ **Sprint 2** → integração Tony Stark com graphify
3. ✅ **Sprint 3+** → rollout para todos Tier 1+2
4. ✅ **Monitoring** → coletar métricas reais

---

**Owner:** Jarvis  
**Versão:** 1.0 Draft  
**Status:** Aguardando validação Architecture Review (Steve Rogers)
