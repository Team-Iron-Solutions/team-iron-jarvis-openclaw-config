# Graphifyy — Quick Reference Guide

**Versão:** 1.0  
**Data:** 26 de agosto de 2026  
**Para:** Todos os agentes (Tony, Bruce, Steve, Scott, Wanda, Natasha)

---

## 🚀 Quick Start (30 segundos)

```bash
# 1. Ativar ambiente
source ~/.openclaw/workspace/graphify-env/bin/activate

# 2. Ver documentação de uma classe
graphify explain "NomeClasse"

# 3. Ver caminho entre classes
graphify path "ClasseA" "ClasseB"

# 4. Sair
deactivate
```

---

## 📚 O Que É Graph.json?

**Graph.json** = mapa estrutural comprimido do seu repo

- ✅ 68KB por ~200 files (jarvis-neural-interface)
- ✅ 90 nodes, 113 edges (relações mapeadas)
- ✅ Queryável em <1 segundo
- ✅ Gerado uma vez, reutilizado para sempre

**vs. sem graphify:**
```
Read 50 files = 10,000+ tokens, 5 min
graphify query = 150 tokens, 1 segundo
Economia: -98% tokens, -99% tempo
```

---

## 🔍 Comandos Principais

### graphify explain (Explicar classe/função)

```bash
graphify explain "AudioBuffer"
```

**Output:**
```
Node: AudioBuffer
  Type: class
  Source: jarvis-show/jarvis-show.py L113
  Connections: 6
  - Chama: __init__(), add(), get_copy()
  - Chamada por: initAudio()
  - Descrição: Thread-safe circular audio buffer
```

**Use quando:** precisa entender estrutura de uma classe

---

### graphify path (Caminho entre classes)

```bash
graphify path "DatabaseConnection" "Logger"
```

**Output:**
```
Shortest path: DatabaseConnection → Query → Logger
Hops: 2
```

**Use quando:** precisa entender impacto de mudança (o que quebra se mudar ClasseA?)

---

### graphify query (Buscar por tipo)

```bash
graphify query "type:function language:python"
```

**Output:**
```
Encontrados: 45 functions em Python
- get_user()
- process_payment()
- validate_input()
...
```

**Use quando:** precisa listar todas functions/classes de um tipo

---

## 🎯 Quando Usar Graphifyy vs Read

| Situação | Usar | Tokens |
|---|---|---|
| Entender estrutura geral | `graphify explain` | 150 |
| Impacto de mudança | `graphify path` | 200 |
| Ler código específico | `read arquivo.js` | 500+ |
| Análise profunda | `read` + `graphify` | 1000+ |

**Regra:** `graphify` primeiro, depois `read` se necessário.

---

## 🔄 Rebuild (Quando Atualizar o Grafo)

### Automático (eles fazem)

Jarvis monitora repositórios. Se novo build é necessário:

```bash
graphify update /path/to/repo
```

### Manual (você solicita)

Se mudou muito código:

```bash
cd ~/repos/nome-repo
source ~/.openclaw/workspace/graphify-env/bin/activate
graphify . --backend ollama --model qwen3.5:4b --max-concurrency 1
```

**ETA:** ~30 min

---

## ⚙️ Troubleshooting

### "graphify command not found"

```bash
source ~/.openclaw/workspace/graphify-env/bin/activate
```

### "Ollama não responde"

```bash
curl http://localhost:11434/api/tags
# Se falhar, Ollama não está rodando
# Solução: `ollama serve &`
```

### "Graph.json muito velho (>7 dias)"

⚠️ **AVISO:** Grafo pode estar desatualizado

```bash
# Rebuild
graphify update /path/to/repo

# Ou solicitar a Jarvis
# mensagem: "Jarvis, rebuild grafo de {repo}"
```

---

## 📊 Repos Conhecidos (Sprint 1+)

| Repo | Nodes | Path | Comando |
|---|---|---|---|
| jarvis-neural-interface | 90 | `~/repos/jarvis-neural-interface` | `graphify explain "AudioBuffer"` |
| OpenJarvis | TBD | `~/.openclaw/workspace/OpenJarvis` | TBD (Sprint 2) |

---

## 🧠 Conceitos-Chave

**AST (Abstract Syntax Tree)**
- Mapa estrutural do código (tipos, funções, relações)
- Extraído por tree-sitter (zero LLM)
- 100% determinístico

**Tree-Sitter**
- Parser que gera AST
- 52+ linguagens suportadas
- Rápido, offline, sem LLM

**Semântica**
- Significado do código (propósito, criticidade)
- Adicionada por Ollama (LLM local)
- Opcional, mas útil para contexto

**Para entender profundamente:** [[AST-TreeSitter-Semantica.md]]

---

## 🎓 Exemplos de Workflow

### Exemplo 1: Code Review de Query()

```
Task: Revisar mudança em DatabaseConnection.query()

1️⃣ graphify explain "DatabaseConnection.query"
   → Vê estrutura, métodos, quem chama

2️⃣ graphify path "DatabaseConnection.query" "*"
   → Vê impacto em cascata

3️⃣ read database/connection.py (se detalhe)
   → Lê código específico se necessário

4️⃣ Revisa + aprova
```

### Exemplo 2: Entender Novo Componente

```
Task: Entender como novo componente Flutter funciona

1️⃣ graphify query "type:class language:dart"
   → Vê todas as classes

2️⃣ graphify explain "NovoComponente"
   → Vê estrutura, dependências

3️⃣ graphify path "NovoComponente" "State"
   → Vê como integra

4️⃣ read component_novo.dart (se detalhe)
```

---

## 📞 Suporte

**Dúvida sobre graphify?**
→ Mensagem a Jarvis: "Jarvis, dúvida graphify: ..."

**Precisa de rebuild?**
→ Mensagem a Jarvis: "Jarvis, rebuild grafo de {repo}"

**Conceito não entendi?**
→ Ler: [[AST-TreeSitter-Semantica.md]]

---

## ✅ Checklist para Novo Repo

Quando adicionar novo repo a Phase 4:

- [ ] Path: `~/repos/{nome}` ou similar
- [ ] Build: `graphify . --backend ollama --model qwen3.5:4b`
- [ ] Resultado: graph.json gerado
- [ ] Query teste: `graphify explain {ClassName}`
- [ ] Adicionar tabela de repos em [[GRAPHIFY-CONVENTIONS.md]]
- [ ] Notificar agentes sobre disponibilidade

---

**Última atualização:** 26/08/2026 — Sprint 1 validado  
**Próxima:** Sprint 2 — Baseline com Tony Stark
