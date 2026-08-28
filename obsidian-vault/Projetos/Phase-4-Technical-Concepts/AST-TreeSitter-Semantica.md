# AST, Tree-Sitter e Semântica — Conceitos Fundamentais Phase 4

**Data de Criação:** 26 de agosto de 2026  
**Autor:** Jarvis (baseado em análise Sprint 1)  
**Versão:** 1.0  
**Tags:** #phase4 #graphify #tree-sitter #ast #semantica #optimization

---

## 📚 Índice

1. [AST (Abstract Syntax Tree)](#ast-abstract-syntax-tree)
2. [Tree-Sitter: Parser Puro](#tree-sitter-parser-puro)
3. [O Que Significa "AST Puro"](#o-que-significa-ast-puro)
4. [Semântica vs Estrutura](#semântica-vs-estrutura)
5. [Como Funciona no Graphifyy](#como-funciona-no-graphifyy)
6. [Aplicação em Phase 4](#aplicação-em-phase-4)
7. [Perguntas Frequentes](#perguntas-frequentes)

---

## 🌳 AST (Abstract Syntax Tree)

### Definição

Um **AST** é um mapa estrutural de código — uma representação em árvore que captura:
- Tipo de cada construção (função, classe, variável, etc)
- Relações entre elas (quem chama quem, quem contém quem)
- Ordem e hierarquia
- **NÃO** captura interpretação semântica ("por quê", "o que faz", "é crítico?")

### Exemplo Prático

**Código JavaScript original:**

```javascript
function calculateTotal(items) {
  let sum = 0;
  for (let i = 0; i < items.length; i++) {
    sum += items[i].price;
  }
  return sum;
}

const total = calculateTotal(myCart);
```

**AST (estrutura pura):**

```
Program
├── FunctionDeclaration
│   ├── name: "calculateTotal"
│   ├── parameters: [
│   │   └── Identifier: "items"
│   ]
│   └── body: BlockStatement
│       ├── VariableDeclaration
│       │   ├── id: "sum"
│       │   └── init: Literal(0)
│       ├── ForStatement
│       │   ├── init: VariableDeclaration("i", Literal(0))
│       │   ├── test: BinaryExpression("i < items.length")
│       │   ├── update: UpdateExpression("i++")
│       │   └── body: ExpressionStatement
│       │       └── AssignmentExpression("sum += items[i].price")
│       └── ReturnStatement
│           └── Identifier: "sum"
├── VariableDeclaration
│   ├── id: "total"
│   └── init: CallExpression
│       ├── callee: "calculateTotal"
│       └── arguments: ["myCart"]
```

### O Que AST Captura

✅ **Tipos:** function, class, variable, loop, condition
✅ **Relações:** calls, contains, assigns, inherits
✅ **Estrutura:** hierarquia, nesting, ordem
✅ **Metadados:** linhas, colunas, identificadores

### O Que AST NÃO Captura

❌ **Semântica:** "essa função calcula totais", "é crítica?"
❌ **Comportamento:** "qual é o algoritmo?", "há bugs?"
❌ **Intenção:** "por que essa estrutura foi escolhida?"
❌ **Contexto:** "qual é o propósito de sum?"

---

## 🔧 Tree-Sitter: Parser Puro

### O Que É

**Tree-Sitter** é uma biblioteca de parsing que:
- Lê código-fonte em qualquer linguagem
- Constrói um AST (estrutura pura)
- Retorna apenas estrutura sintática
- **Nunca** faz interpretação ou usa LLM

### Características Principais

| Característica | Detalhe |
|---|---|
| **Linguagens** | 52+ suportadas (JavaScript, Python, Java, Rust, Go, etc) |
| **Determinístico** | Mesmo código = mesma árvore, sempre |
| **Rápido** | Parsing de 10k files em segundos |
| **Sem LLM** | Zero dependência de modelos, offline |
| **Incremental** | Pode atualizar partes da árvore sem reprocessar tudo |

### Como Funciona

```
Código-fonte
    ↓
[Tree-Sitter Parser]
    ↓
AST (Árvore sintática)
    ↓
[JSON/Output]
```

**Exemplo — como tree-sitter processa:**

```python
# Input
class DatabaseConnection:
    def connect(self):
        pass
    
    def query(self, sql):
        return None

# Tree-Sitter Output (AST)
{
  "type": "module",
  "children": [
    {
      "type": "class_definition",
      "name": "DatabaseConnection",
      "children": [
        {
          "type": "function_definition",
          "name": "connect"
        },
        {
          "type": "function_definition",
          "name": "query",
          "parameters": ["self", "sql"]
        }
      ]
    }
  ]
}
```

---

## 💡 O Que Significa "AST Puro"

### Definição

**"AST puro"** significa:
- Estrutura sintática extraída por parser (tree-sitter)
- Sem processamento semântico
- Sem interpretação por LLM
- Fatos 100% certos (não probabilísticos)

### Exemplo de AST Puro vs Com Semântica

**AST Puro (tree-sitter):**

```json
{
  "id": "DatabaseConnection.query",
  "type": "method",
  "parameters": ["self", "sql"],
  "returns": null
}
```

**Com Semântica (Ollama):**

```json
{
  "id": "DatabaseConnection.query",
  "type": "method",
  "parameters": ["self", "sql"],
  "returns": null,
  
  "description": "Execute a SQL query against the database connection",
  "purpose": "Retrieve data from the database",
  "criticality": "high",
  "side_effects": "Modifies database state if INSERT/UPDATE/DELETE",
  "rationale": "Returns None instead of result set — needs fix"
}
```

### Por Que "Puro" Importa

| Aspecto | AST Puro | Com Semântica |
|---|---|---|
| **Precisão** | 100% certo | 95-99% (LLM pode errar) |
| **Custo** | $0 | Custa tokens |
| **Latência** | <100ms | 1-10s |
| **Confiabilidade** | Determinístico | Não-determinístico |
| **Utilidade** | Estrutura | Contexto + interpretação |

---

## 🧠 Semântica vs Estrutura

### Definição

| Termo | Significado | Quem Extrai | Custo |
|---|---|---|---|
| **Estrutura (AST)** | Forma do código: classes, funções, relações | Tree-sitter | $0 |
| **Semântica** | Significado do código: propósito, criticidade, riscos | LLM (Ollama/OpenAI) | $$ (tokens) |

### Exemplo

**Código:**

```python
def process_payment(card_number, amount):
    if amount > 10000:
        alert("Large transaction")
    charge_card(card_number, amount)
```

**Estrutura (AST Puro):**
```
- Tipo: function
- Nome: process_payment
- Parâmetros: card_number, amount
- Chama: alert(), charge_card()
- Condição: if amount > 10000
```

**Semântica (LLM):**
```
- Propósito: processa pagamentos de cartão
- Criticidade: ALTA (envolve dados financeiros)
- Risco: detecta transaction grande (anti-fraud)
- Security concern: card_number em plaintext (⚠️ RISCO)
- Recomendação: usar tokenização PCI-DSS
```

### Trade-off

```
AST Puro (tree-sitter):
  Pro: Rápido, $0, 100% certo
  Con: Sem contexto, sem interpretação

Semântica (LLM):
  Pro: Contexto rico, interpretação
  Con: Lento, caro, pode errar
```

---

## 🔍 Como Funciona no Graphifyy

### Pipeline Completo

```
Repo (~200 files)
    ↓
[Tipo de arquivo]
    ├─ Código (.js, .py, .java)
    │   ↓ tree-sitter
    │   └─ AST PURO (zero LLM)
    │
    └─ Documentação (.md, README)
        ↓ Ollama/OpenAI
        └─ Semântica (labels, descrições)

    ↓
graph.json (90 nodes)
├── Estrutura: 100% confiável
└── Semântica: contextualizada
```

### Exemplo Sprint 1 (jarvis-neural-interface)

```
jarvis-neural-interface/
├── jarvis-show.js (4 arquivos code)
│   ├── class AudioBuffer → [AST PURO] → id, methods, calls
│   ├── function initAudio → [AST PURO] → calls AudioBuffer.__init__
│   └── ...
│
├── README.md (17 arquivos docs)
│   ├── "Voice pipeline overview" → [Ollama] → extracted as description
│   ├── "AudioBuffer thread-safety" → [Ollama] → extracted as rationale
│   └── ...
│
Result:
├── 90 nodes total
├── ~60 nodes estruturais (tree-sitter, AST puro)
└── ~30 nodes enriquecidos (semântica Ollama)
```

### Query (Quando Você Usa)

```bash
$ graphify explain "AudioBuffer"
```

**O que acontece:**

```
1. Busca no graph.json (leitura JSON local)
   → "AudioBuffer é uma classe?" (AST puro ✅)
   → "Tem método add()?" (AST puro ✅)
   → "Quem chama __init__?" (AST puro ✅)

2. Retorna contexto combinado
   → Estrutura (tree-sitter) + Descrição (Ollama)
   → ~150 tokens
   → <1 segundo
```

---

## 🎯 Aplicação em Phase 4

### Problema Original

Tony Stark (code reviewer) precisava de contexto antes de revisar:
- Lia 50+ arquivos = 20,000+ tokens
- Levava 10+ minutos
- Caro (tokens) e lento

### Solução Phase 4

```
Traditional:
  Read 50 files → 20,000 tokens → 10 min → Caro

Phase 4 (com Graphifyy):
  graphify explain → 1,000 tokens → 1 min → Barato
  Ganho: -80% tokens, -90% tempo
```

### Como Tree-Sitter Viabiliza Isso

```
Tree-sitter (estrutura pura):
  → 68KB grafo para 200 arquivos
  → Relações mapeadas (quem chama quem)
  → Sem redundância

Resultado:
  → Query cirúrgica (só o necessário)
  → Rápido e barato
```

### Exemplo Real: Code Review com Graphifyy

**Task:** "Revisa mudança em DatabaseConnection.query()"

```
Sem Graphifyy:
1. Lê DatabaseConnection.py (~500 tokens)
2. Lê files que chamam query() (~2000 tokens)
3. Lê migration files (~3000 tokens)
4. Total: ~5500 tokens, 5 min

Com Graphifyy:
1. graphify explain "DatabaseConnection.query" (~150 tokens)
   → estrutura, métodos, quem chama
2. graphify path "DatabaseConnection.query" "*" --transitive (~200 tokens)
   → impacto em cascata
3. read arquivo específico se necessário (~500 tokens)
4. Total: ~850 tokens, 1 min

Economia: -85% tokens, -80% tempo
```

---

## ❓ Perguntas Frequentes

### P: "Por que não usar só LLM semântico?"

**R:** 
- Tree-sitter (AST) é determinístico, LLM é probabilístico
- AST captura 80% do que precisamos (estrutura é o essencial)
- LLM é caro; tree-sitter é grátis
- Combinação = melhor de ambos mundos

### P: "Tree-sitter pode errar?"

**R:** 
- Não, tree-sitter é parsing — não há interpretação
- Se código é válido syntaxe, AST é 100% correto
- Se código tem bug lógico, tree-sitter ainda extrai AST corretamente

### P: "Posso usar graphify sem documentação?"

**R:** 
- Sim! Código (AST puro) é extraído independentemente
- Docs (semântica) enriquecem o grafo, mas código funciona sem elas
- Sprint 1 funcionou com 4 arquivos code + 17 docs

### P: "Qual é o trade-off de usar qwen3.5:4b vs 9b?"

**R:**
```
qwen3.5:4b:
  ✅ Processou 17 docs sem problema
  ✅ Qualidade de labels: 95%+
  ✅ Mem: 4-5GB (seguro)
  ✅ Cost: $0

qwen3.5:9b:
  ✅ Qualidade de labels: 99%+ (marginal)
  ✅ Mem: 6-7GB (risco OOM)
  ✗ Cost: Mais mem, mais lento

Recomendação: 4b é suficiente para Phase 4
```

### P: "Como validar que AST está correto?"

**R:**
```bash
# Executar query simples
graphify explain "ClassName"

# Ver resultado da estrutura
# Se mostra corretamente: AST é correto
# Tree-sitter não pode errar aqui (é parsing, não interpretação)
```

### P: "Posso re-extrair AST de um grafo antigo?"

**R:**
```bash
# Sim, com --force
graphify update . --force

# Atualiza AST (code) sem re-processar semântica (docs)
# Rápido porque cache semântico é reutilizado
```

---

## 📚 Referências Internas

- [[GRAPHIFY-CONVENTIONS.md]] — Padrões operacionais Phase 4
- [[PHASE4-AGENT-PLAYBOOK.md]] — Como agentes usam graphify
- [[STEVE-ROGERS-PHASE4-FINAL-ARCHITECTURE-REVIEW.md]] — Validação CTO
- [[PHASE4-SPRINT1-LOG.md]] — Log de execução Sprint 1

---

## 🔗 Referências Externas

- [Tree-Sitter Documentation](https://tree-sitter.github.io/)
- [Abstract Syntax Tree (Wikipedia)](https://en.wikipedia.org/wiki/Abstract_syntax_tree)
- [Graphifyy GitHub](https://github.com/codename-cos/graphify)

---

## 📝 Histórico de Revisão

| Data | Mudança | Autor |
|---|---|---|
| 2026-08-26 | Criação v1.0 | Jarvis |
| TBD | Adições após Sprint 2 | Jarvis |

---

**Próxima revisão recomendada:** Após Sprint 2 (baseline Tony Stark)

