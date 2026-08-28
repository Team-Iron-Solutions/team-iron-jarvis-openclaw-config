# GRAPHIFY-PHASE4.md — Otimização de Contexto via Knowledge Graphs

**Data de planejamento:** 19 de agosto de 2026  
**Status:** 🟡 Planejado (esperando aprovação + implementação)  
**Modelo base para decisão:** Sonnet (estratégico) + pesquisa com Haiku

---

## Visão Geral

Implementar [Graphify](https://github.com/Graphify-Labs/graphify) para reduzir token consumption quando agentes precisam analisar codebases grandes. Em vez de carregar arquivos inteiros (`read arquivo.dart` = 2000+ tokens), query um grafo: `graphify explain "ComponenteX"` = 200 tokens.

**Ferramenta:** Open-source, local-first, suporta ~40 linguagens via tree-sitter AST  
**Custo:** Instalação única + ~10 min de build do grafo por repo  
**Ganho estimado:** -40-60% de tokens para operações de code review/análise  
**Aplicabilidade:** 6 de 10 agentes (todos os técnicos)

---

## Agentes Beneficiários

### Tier 1 — Alto Impacto (código é o trabalho)
| Agente | Caso de uso | Economia estimada |
|---|---|---|
| **Tony Stark** | Code review Node.js, análise de APIs, refactoring | -50% (frequente) |
| **Bruce Banner** | Code review Python, data pipelines, debugging | -50% (frequente) |
| **Steve Rogers** | Mapear arquitetura de sistemas, análise de impacto | -40% (ocasional) |

### Tier 2 — Médio Impacto (código misto)
| Agente | Caso de uso | Economia estimada |
|---|---|---|
| **Scott Lang** | Flutter widgets, providers, state management | -45% (frequente) |
| **Wanda Maximoff** | Design system, componentes reutilizáveis, dependencies | -35% (frequente) |
| **Natasha Romanoff** | Mapear testes, cobertura, impacto de mudanças | -40% (ocasional) |

### Tier 3 — Baixo Impacto (não trabalha com código)
| Agente | Caso de uso |
|---|---|
| **T'Challa** | Shell scripts, configs — grafo útil mas menor escala |
| **Visão** | SQL, análise — grafo ajuda com schema mapping |
| **Stephen Strange** | PM — apenas quando precisa entender escopo técnico |
| **Peter Parker** | Social media — N/A |

---

## Fluxo de Trabalho

### Fase 1: Setup (por repo, uma vez)

```bash
# 1. Instalar Graphify
uv tool install graphifyy
# ou
pipx install graphifyy

# 2. Registrar como skill (opcional, para Claude Code/Cursor)
graphify install

# 3. Mapear repo
cd ~/repos/seu-repo
graphify .
# Gera:
#   graphify-out/graph.html (visual)
#   graphify-out/GRAPH_REPORT.md (destaques)
#   graphify-out/graph.json (queryável)
```

### Fase 2: Uso em operações de código

**Antes (without Graphify):**
```
Tony Stark: "Revisa api/routes.js"
→ `read api/routes.js` (1500 tokens)
→ Carrega TUDO, inclusive imports, comentários, código morto
```

**Depois (with Graphify):**
```
Tony Stark: "Explica como APIRouter conecta a RequestValidationError"
→ exec: graphify explain "APIRouter"
→ "APIRouter uses RequestValidationError [INFERRED]"
  "APIRouter.get() method [EXTRACTED]"
  "Connections: 47 → retorna só as relevantes" (150 tokens)
```

**Outro exemplo:**
```
Scott Lang: "Qual é o impacto de mudar ButtonComponent?"
→ exec: graphify path "ButtonComponent" "*" (transitive)
→ Retorna todos os widgets que herdam/usam ButtonComponent
→ Economia: evita ler 20 arquivos (10.000 tokens) para descobrir
```

---

## Estimativa de Economia

### Cenário 1: Code Review Monolítico (Node.js 50k LOC)

| Operação | Sem Graphify | Com Graphify | Economia |
|---|---|---|---|
| Entender estrutura (1 chamada) | 3.000 tokens | 400 tokens | -87% |
| Analisar rota específica (5 chamadas) | 7.500 tokens | 1.000 tokens | -87% |
| Traçar caminho crítico (1 chamada) | 2.000 tokens | 300 tokens | -85% |
| **Total por session** | 12.500 | 1.700 | **-86%** |

### Cenário 2: Flutter Design System Review

| Operação | Sem Graphify | Com Graphify | Economia |
|---|---|---|---|
| Listar componentes que usam Theme | 4.000 tokens | 200 tokens | -95% |
| Traçar impacto de mudança em Button | 5.000 tokens | 300 tokens | -94% |
| Entender inheritances de widgets | 3.000 tokens | 400 tokens | -87% |
| **Total por session** | 12.000 | 900 | **-93%** |

### Agregado (estimado para squad)

**Premissas:**
- Code review: 3 agents × 2 sessions/dia × 20 dias/mês = 120 sessions
- Contexto médio por session: 8.000 tokens
- Economia média com Graphify: -60%

```
Sem Graphify: 120 sessions × 8.000 tokens = 960.000 tokens/mês (Tier 1)
Com Graphify: 120 sessions × 3.200 tokens = 384.000 tokens/mês
Economia: -576.000 tokens/mês (-60%)

Custo em $$ (Haiku @ $0.80/1M):
Sem: $0.77/mês
Com: $0.31/mês
Economia: -$0.46/mês
```

**Nota:** Ganho maior quando repos crescem. Repos pequenos (<5k LOC) ganham -30-40%. Repos grandes (50k+ LOC) ganham -80-95%.

---

## Plano de Implementação

### Sprint 1 — Setup (Dia 1-2)
- [ ] Instalar Graphify no Mac mini
- [ ] Testar build de grafo com 2 repos (node-backend, flutter-mobile)
- [ ] Documentar performance de build (tempo, tamanho do JSON)

### Sprint 2 — Integração Tony Stark (Dia 3-5)
- [ ] Mapear repos relevantes (backend principal)
- [ ] Criar spike: code review Antes/Depois com Graphify
- [ ] Documentar benefício real vs. estimado

### Sprint 3 — Rollout Tier 1 (Dia 6-10)
- [ ] Expandir para Bruce Banner (Python repos)
- [ ] Expandir para Steve Rogers (análise de arquitetura)
- [ ] Criar playbook: "Quando usar graphify query vs. read"

### Sprint 4 — Rollout Tier 2 (Dia 11-20)
- [ ] Scott Lang (Flutter)
- [ ] Wanda Maximoff (design system)
- [ ] Natasha Romanoff (test mapping)

### Sprint 5 — Monitoring (Dia 21+)
- [ ] Coletar métricas de economia real
- [ ] Ajustar prioridades conforme dados
- [ ] Atualizar MEMORY.md com resultados

---

## Integração com Ferramentas OpenClaw

### Via `exec` (recomendado)

```js
// Agentes podem rodar isso diretamente:
exec({
  command: `cd /path/to/repo && graphify explain "NomeClasse"`
})
```

### Triggers
- Code review iniciado → sugerir `graphify explain` para classes-chave
- Impacto analysis → sugerir `graphify path A B` para traçar dependências
- Architecture review → sugerir `graphify query` para questões complexas

### Cache
- `graph.json` é cache permanente (reutilizável até próxima mudança no repo)
- Regen quando: nova branch mergeada, arquivo deletado, refactoring major

---

## Requisitos & Dependências

### Instalação
```bash
python3 -m pip install graphifyy
# ou
uv tool install graphifyy
```

**Compatível com:** macOS, Linux, Windows  
**Python:** 3.9+ (temos 3.9 no Mac mini)  
**Disco:** ~50-200MB por repo (JSON graph)

### Linguagens Suportadas
✅ JavaScript/TypeScript (Node.js)  
✅ Python  
✅ Dart/Flutter  
✅ CSS/SCSS  
✅ SQL  
✅ Go  
✅ ~35 mais (tree-sitter)

### Limitações Conhecidas
- Tree-sitter: determinístico, 100% local, mas pode ter false positives em código muito obscuro
- Primeira build leva 5-10 min em repos grandes (50k LOC)
- Atualizações do grafo não são automáticas — precisa rodar `graphify .` novamente

---

## Métricas de Sucesso

| Métrica | Target | Validação |
|---|---|---|
| Token savings (code review) | -50% vs. baseline | Coletar antes/depois em 10 sessions |
| Agent adoption (Tier 1) | 100% | Todos 3 usando em 80%+ de reviews |
| Graph build time (avg) | <10 min | Medir em 3+ repos |
| False positive rate | <5% | Validar 20 `graphify explain` vs. source |

---

## Riscos & Mitigações

| Risco | Probabilidade | Impacto | Mitigação |
|---|---|---|---|
| Tree-sitter parsing fail | Baixa | Medio | Fallback para `read` completo |
| Graph grow muito grande | Baixa | Baixo | Comprimir JSON ou split por module |
| Agentes desistem (UX complexa) | Média | Alto | Criar playbook claro, exemplos |
| Manutenção de grafo esquecida | Média | Médio | Lembrete no cron (semanal recompile) |

---

## Próximos Passos

1. **Aprovação:** Galvão confirma interesse (você já fez ✅)
2. **Spike:** Implementar Sprint 1 em paralelo com tarefas normais
3. **Decision point:** Dia 5 — dados reais vs. estimativas? Prosseguir ou ajustar?

---

## Referências

### Conceitos Técnicos
📚 **[[AST-TreeSitter-Semantica.md]]** — Explicação completa sobre AST, tree-sitter, e o que significa "AST puro"
- Ideal para: Entender por que tree-sitter não usa LLM
- Ideal para: Trade-offs entre semântica (LLM) vs estrutura (tree-sitter)
- Ideal para: Validar decisões de arquitetura Phase 4

### Documentação Externa
- **GitHub:** https://github.com/Graphify-Labs/graphify
- **Docs:** https://graphify.com (early access)
- **PyPI:** https://pypi.org/project/graphifyy/
- **Tree-Sitter:** https://tree-sitter.github.io/
- **Community:** https://discord.gg/598Ad9zQZ

### Documentação Interna Phase 4
- **GRAPHIFY-CONVENTIONS.md** — Padrões operacionais (modelos, paths, rebuilds)
- **PHASE4-AGENT-PLAYBOOK.md** — Como agentes usam graphify
- **PHASE4-VALIDATION-CHECKLIST.md** — Testes e métricas
- **PHASE4-SPRINT1-LOG.md** — Log de execução Sprint 1

---

**Owner:** Jarvis  
**Last updated:** 26/08/2026 (Sprint 1 completo)  
**Status:** ✅ Sprint 1 Validado | 🔄 Sprint 2 Próximo
