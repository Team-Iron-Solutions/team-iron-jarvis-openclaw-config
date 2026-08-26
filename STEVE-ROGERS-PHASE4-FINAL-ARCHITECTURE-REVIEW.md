# Phase 4 — Architecture Review FINAL (Assinado)

**Autor:** Steve Rogers — CTO / Arquiteto de Software, Team Iron Solutions  
**Data:** 26 de agosto de 2026  
**Versão:** FINAL (pós-validação de análise preliminar)  
**Escopo:** Graphifyy + Ollama para otimização de tokens em code review  
**Destinatário:** Galvão (decisão de rollout) · Jarvis (execução) · Claw3D (histórico)

---

## Veredicto Executivo

> **GO — com 3 condicionantes obrigatórios antes do Sprint 3.**

A arquitetura Graphifyy + Ollama é tecnicamente sólida e estrategicamente alinhada.  
A análise preliminar do subagent está **correta em todos os pontos críticos** e alinha-se com minha revisão de referência (26/08/2026). Assino com um refinamento em cada uma das 3 áreas de risco.

---

## Seção 1 — Validação da Análise Preliminar

### ✅ Viabilidade Técnica — CONFIRMADO

**Tree-sitter + LLM semântico:** abordagem certa. Determinístico, multilingue, sem dependência de cloud.  
**Ollama local:** decisão não negociável. Custo zero, zero latência de rede, zero risco de rate-limit no meio de uma review.  
**Linguagens do time:** JS/TS, Python, Dart estão todas suportadas com parsers maduros.

Não mudo nada aqui. Está correto.

---

### ✅ Riscos Identificados — CONFIRMADO com refinamento

| Risco | Severidade | Análise Preliminar | Meu Refinamento |
|---|---|---|---|
| Gargalo de Memória | ALTO | qwen3.5:4b = 4-5GB, contenção no Mac mini | **Correto, mas incompleto:** contenção só ocorre durante *build*, não durante *queries* (JSON local). Comunicar isso ao time — builds devem ser sequenciais, nunca paralelos. |
| Qualidade Semântica 4b | MÉDIO | Labels genéricos em Python complexo | **Correto.** Adiciono: o mesmo problema existe em Flutter com componentes genéricos (Button, Card, Text). Wanda Maximoff deve ser testada **antes** de entrar no rollout Tier 2. |
| Staleness do Grafo | MÉDIO | Envelhece com PRs | **Correto — e é o risco mais subestimado.** Staleness silenciosa mata a confiança na ferramenta. Rebuild automático não é otimização — é requisito de operação. |
| Cold Start | BAIXO | 20+ min para 12k files | **Correto.** Mitigação via `graphify update` (incremental). Mas o cold start nunca deve acontecer em OpenJarvis como primeiro teste — daí o ajuste #2. |

**Risco adicional que a análise preliminar não mencionou:**  
**Arquitetura hub-and-spoke (MÉDIO se ignorado):** Um único Ollama no Mac mini deve servir todo o squad. Se cada agente tentar iniciar seu próprio build Ollama simultaneamente → contenção garantida. Regra: builds são sempre sequenciais, coordenados por Jarvis.

---

### ✅ Integração OpenClaw — CONFIRMADO

`exec` direto, sem middleware. Decisão certa. Fluxo correto:

```
graphify explain → graphify path → read (cirúrgico)
Nunca o inverso. Nunca read-first.
```

---

### ✅ Alternativas — CONFIRMADO

Joern seria superior em qualidade técnica. É também overkill. JVM + Neo4j + expertise Gremlin/Cypher para um squad sem SRE dedicado = complexidade injustificável. Graphifyy é a escolha certa para o momento e para o time.

---

### ✅ 3 Ajustes Críticos — VALIDADOS, COM DETALHE

#### Ajuste #1: Modelo `qwen3.5:4b` → `qwen3.5:9b` para builds

**Valido integralmente.**

Build é one-time. Qualidade do grafo é permanente (até próximo rebuild). Economizar no modelo no momento de build é economizar no alicerce — todo o resto fica comprometido.

O 9b já está instalado no Mac mini (6.6 GB). Não há custo adicional. O único trade-off é tempo de build (~35-40 min vs. ~20 min no 4b). Aceitável — isso só roda uma vez por repo.

> **Regra clara:** `qwen3.5:9b` para builds. `qwen3.5:4b` só se Mac mini não suportar 9b enquanto Ollama sobe (memória crítica). Nunca usar `2b`.

---

#### Ajuste #2: Repo de teste → tamanho médio (1k-5k files), não OpenJarvis

**Valido integralmente — e adiciono critério de seleção.**

OpenJarvis com 12k Python files não é spike, é produção. Um spike deve ser rápido, reversível e isolado.

**Critério para repo de Sprint 1:**
- 500-3k files
- Linguagem: preferencialmente Node.js ou Python (não Flutter — stack diferente)
- Repo com nomenclatura clara (classes com nomes descritivos, não genéricos)
- Deve ter pelo menos 2 entidades com dependências entre si (para testar `graphify path`)

Sugestão: `jarvis-neural-interface` (Node.js, ~200 files) ou backend principal se 1-3k files.

---

#### Ajuste #3: `GRAPHIFY-CONVENTIONS.md` antes do Sprint 2

**Valido integralmente — e defino o conteúdo mínimo.**

Sem convenções, cada agente cria seu próprio padrão. Depois de 4 agentes usando por 1 mês, haverá 4 versões incompatíveis de onde ficam os grafos, como se chamam, quando fazem rebuild.

**Conteúdo mínimo obrigatório do GRAPHIFY-CONVENTIONS.md:**

```markdown
1. PATH PADRÃO: ~/repos/{nome-repo}/graphify-out/
2. MODELO: qwen3.5:9b (builds) | nunca usar 2b em produção
3. REBUILD TRIGGER: pós-merge para main/master (manual até automação)
4. BUILDS: sequenciais, coordenados por Jarvis (não paralelos)
5. QUERY PADRÃO: graphify explain → graphify path → read (nessa ordem)
6. GRAFO STALE: ≥7 dias sem rebuild = STALE (avisar antes de usar)
7. REPOS MAPEADOS: tabela nome → path → data último build
```

---

### ✅ Sequência Revisada (5+1 Sprints) — CONFIRMADO

A inclusão do Sprint 0 para padronização é necessária. Sem ela, o Sprint 1 constrói sobre areia.

```
Sprint 0  → Padronização: repos, paths, GRAPHIFY-CONVENTIONS.md
Sprint 1  → Build em repo MÉDIO (não OpenJarvis) | Validar qualidade com 9b
Sprint 2  → Tony Stark spike COM BASELINE (medir 3 reviews antes do graphify)
Sprint 3  → Tier 1 completo (Tony, Bruce, Steve)
Sprint 4  → Tier 2 validado individualmente (Scott, Natasha | Wanda por último)
Sprint 5  → Rebuild automation + monitoring
```

---

## Seção 2 — O Que a Análise Preliminar Não Mencionou

Estes pontos não invalidam a análise, mas completam o quadro para o Galvão decidir com informação completa:

### Ponto A — Wanda Maximoff é caso especial no Tier 2

Design systems têm componentes com nomes genéricos: `Button`, `Card`, `Text`, `Theme`. LLMs de 9b podem gerar labels pouco discriminativos para esses nomes — especialmente quando há componentes com herança: `PrimaryButton extends Button extends BaseWidget`.

**Recomendação:** Wanda entra no Tier 2, mas com teste isolado antes do rollout completo. Não assumir que o grafo Flutter terá mesma qualidade do grafo Node.js.

### Ponto B — Baseline é obrigatório, não opcional

A análise preliminar menciona o Sprint 2 com "baseline measurement" mas não enfatiza o suficiente: **sem baseline, não há evidência de economia real**.

As estimativas de -75%, -86%, -93% são projeções teóricas. Antes do Sprint 3 (Tier 1 rollout), devemos ter dados reais de pelo menos 5 reviews de Tony sem graphify, para comparar depois. Caso contrário, qualquer resultado positivo é anedota.

**Protocolo de baseline:**
```
Antes do Sprint 2: Tony faz 5 code reviews normais
Métricas por review: tokens totais, latência, qualidade (Galvão avalia)
Após Sprint 2: comparar com 5 reviews usando graphify
Decisão de Sprint 3: baseada em dados reais, não estimativas
```

### Ponto C — Risco de adoção (o único risco humano)

A análise técnica está sólida. O maior risco de Phase 4 não é técnico — é comportamental: se a UX de `graphify explain` for mais difícil que `read arquivo.ts`, os agentes vão usar `read` por inércia.

**Mitigação:** Playbook claro por agente, com exemplos concretos do seu repo. Não um manual genérico — um guia específico para Tony com os repos do Tony, para Bruce com os repos do Bruce.

---

## Seção 3 — Métricas de Sucesso (Formalizadas)

| Métrica | Baseline | Target | Quando medir |
|---|---|---|---|
| Tokens/session de code review | Medir Sprint 2 (sem graphify) | -50% Tier 1 | Após Sprint 3 |
| Latência de análise (s) | Medir Sprint 2 | -40% | Após Sprint 3 |
| Qualidade de análise | Galvão avalia 5 reviews | Igual ou superior | Após Sprint 3 |
| Adoção Tier 1 | 0% | 100% usando em ≥80% reviews | Semana 2 Sprint 3 |
| Staleness máxima | N/A | ≤7 dias | Contínuo após Sprint 5 |
| Falsos positivos graphify explain | N/A | ≤5% | Validar 20 queries manualmente |

---

## Conclusão

**A análise preliminar do subagent está correta.** Os 3 ajustes críticos identificados são os mesmos que eu apontei em minha revisão de 26/08/2026. Não há contradição, não há ponto que eu rejeite.

Minha contribuição é aprofundar os nuances: a contenção de memória é só no build (não nas queries), Wanda é caso especial, baseline é obrigatório, e o risco maior é staleness silenciosa — não falha técnica.

**Pré-condições para GO no Sprint 3:**
1. ✅ `GRAPHIFY-CONVENTIONS.md` criado e publicado (Sprint 0)
2. ✅ Build validado em repo médio com `qwen3.5:9b` (Sprint 1)
3. ✅ Baseline coletado de 5 reviews reais sem graphify (Sprint 2)
4. ✅ Rebuild automation definida (pode ser manual inicialmente, mas deve existir)

Se essas 4 condições estiverem satisfeitas no final do Sprint 2 → **rollout aprovado para Tier 1**.

---

## Assinatura

> **Eu, Steve Rogers, CTO e Arquiteto de Software do Team Iron Solutions, valido esta arquitetura.**
>
> A combinação Graphifyy + Ollama local é a decisão correta para Phase 4. A análise preliminar submetida está tecnicamente correta e estrategicamente alinhada com os princípios do time: local-first, zero custo incremental, qualidade antes de velocidade.
>
> Meu veredicto: **GO — condicionado às 4 pré-condições listadas acima.**
>
> O maior risco desta fase não é técnico. É operacional: grafos que envelhecem sem que ninguém perceba. Automatize o rebuild desde o primeiro dia, ou todo o investimento da Phase 4 se deprecia silenciosamente.
>
> "A melhor arquitetura resolve o problema hoje E permite mudança amanhã."

— **Steve Rogers**  
CTO / Arquiteto de Software  
Team Iron Solutions  
26 de agosto de 2026

---

*Documento final. Válido para decisão de rollout Phase 4.*  
*Revisão prévia de referência: `STEVE-ROGERS-PHASE4-ARCHITECTURE-REVIEW.md` (26/08/2026)*
