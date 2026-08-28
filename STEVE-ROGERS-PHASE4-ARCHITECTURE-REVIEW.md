# Phase 4 — Architecture Review

**Autor:** Steve Rogers (Arquiteto de Software)  
**Data:** 26 de agosto de 2026  
**Solicitado por:** Jarvis + Galvão  
**Escopo:** Graphifyy + Ollama para otimização de contexto em code review

---

## Veredicto Direto

> **Arquitetura sólida. Direção correta. Três ajustes críticos antes do rollout.**

A combinação Graphifyy + Ollama local é tecnicamente viável e estrategicamente alinhada com a filosofia do time (local-first, zero custo incremental, sem dependências externas). Mas há riscos reais que precisam ser endereçados antes do Sprint 3.

---

## 1. Viabilidade Técnica

### ✅ O que está certo

**Stack de extração (tree-sitter + LLM semantic)** é a abordagem correta para 2026. Tree-sitter é determinístico, rápido e suporta as linguagens do time (JS/TS, Python, Dart). A camada semântica via LLM (Ollama) adiciona contexto que AST puro não captura — nomes de conceitos, relações implícitas, padrões arquiteturais.

**Ollama local** elimina os dois maiores riscos de soluções cloud: custo variável e latência de rede. Para um squad de agentes que faz code review várias vezes ao dia, isso é não negociável.

### ⚠️ Riscos Identificados

**Risco 1 — Gargalo de Memória (ALTO)**  
Ollama rodando `qwen3.5:4b` consome ~4-5GB de RAM. O Mac mini tem limitações. Se dois agentes acionarem extração simultânea (Tony + Bruce ao mesmo tempo), há risco de contenção de memória e swap. **Mitigação:** Graph build é one-time; queries no grafo existente são só `cat graph.json | grep`. O gargalo é real apenas no momento de *build*, não de *uso*.

**Risco 2 — Qualidade Semântica do qwen3.5:4b (MÉDIO)**  
Para *naming communities* e *semantic extraction* em Python complexo, um modelo 4B pode gerar labels genéricos ("Classe de utilidade", "Handler genérico"). A qualidade do grafo depende diretamente da qualidade do LLM. **Mitigação:** Usar `qwen3.5:9b` para builds — mais lento, mas qualidade superior. Usar `qwen3.5:2b` seria erro.

**Risco 3 — Staleness do Grafo (MÉDIO)**  
Graphifyy gera snapshot estático. Em repos com PRs frequentes (Tony mergeia feature, Bruce adiciona módulo), o grafo envelhece em horas. Se os agentes consultarem um grafo desatualizado, as relações estarão erradas. **Mitigação:** Rebuild automático pós-merge (hook no CI ou trigger manual).

**Risco 4 — Cold Start (BAIXO, mas visível)**  
Primeiro build de 12k files com Ollama local levou >20 min. Isso não escala para 6+ repos. **Mitigação:** Build incremental (Graphifyy suporta `graphify update`) — mudanças só reprocessam arquivos alterados, não o repo inteiro.

---

## 2. Integração com OpenClaw

### Padrão recomendado: `exec` direto, sem wrapper

Os agentes têm acesso nativo ao `exec`. A integração mais simples e confiável é:

```bash
# No playbook de cada agente:
source ~/.openclaw/workspace/graphify-env/bin/activate
graphify explain "NomeClasse" --path /repos/meu-repo/graphify-out
```

**Não precisa de middleware** para a fase atual. Middleware adicionaria complexidade sem benefício real enquanto o squad ainda está aprendendo a usar o grafo.

### Fluxo de integração recomendado (3 etapas)

```
Agente recebe tarefa de code review
        ↓
Etapa 1: graphify explain "EntidadePrincipal"
         → Contexto estrutural (~300 tokens)
        ↓
Etapa 2: graphify path "EntidadeA" "EntidadeB" (se necessário)
         → Impacto de mudança (~200 tokens)
        ↓
Etapa 3: read arquivo.ts (apenas se precisar ver código específico)
         → Contexto cirúrgico, não full file
```

**Regra prática:** Graphify primeiro, `read` depois — nunca o inverso.

### Impacto na latência

| Operação | Sem Graphify | Com Graphify |
|---|---|---|
| Entender estrutura de classe | `read` 3-5 arquivos (~8s, ~6k tokens) | `graphify explain` (~0.5s, ~300 tokens) |
| Mapear impacto de mudança | Manual/iterativo (~30s, ~15k tokens) | `graphify path` (~1s, ~400 tokens) |
| Code review completo (rota) | ~45s, ~12k tokens | ~15s, ~3k tokens |

**Latência de query no grafo existente é <1s** (leitura de JSON local). O Ollama só é acionado durante o *build*, não durante as queries.

---

## 3. Alternativas Comparadas

| Solução | Qualidade | Custo Setup | Manutenção | Fit para o time |
|---|---|---|---|---|
| **Graphifyy + Ollama** | ⭐⭐⭐⭐ | Baixo | Médio | ✅ Alto |
| Joern (Scala/graph DB) | ⭐⭐⭐⭐⭐ | **Muito alto** | Alto | ❌ Overkill |
| code2vec (embeddings) | ⭐⭐⭐ | Médio | Alto | ⚠️ Requer infra |
| Custom tree-sitter | ⭐⭐⭐ | Médio | **Muito alto** | ❌ Reinventa roda |
| ctags/universal-ctags | ⭐⭐ | Muito baixo | Baixo | ⚠️ Sem semântica |

**Conclusão:** Graphifyy é a escolha certa. Joern seria superior tecnicamente, mas requer JVM, Neo4j ou TinkerPop, e expertise em Gremlin/Cypher — complexidade injustificável para o ROI atual. O time não tem perfil SRE dedicado ao grafo.

---

## 4. Roadmap — Análise dos 5 Sprints

### O que está bem planejado ✅
- Sequência Tier 1 antes de Tier 2 (certo — valida com os que mais precisam)
- Decision point no Dia 5 (certo — não fazer rollout cego)
- Build one-time por repo (certo — não rebuild por sessão)

### O que mudar ⚠️

**Sprint 1 — Trocar repo de teste**  
OpenJarvis (12k Python files, 1.5GB) é grande demais para um *spike*. Escolha um repo de tamanho médio (1k-5k files) para o primeiro build. Valide a qualidade do grafo antes de ir para repos grandes.

**Sprint 2 — Adicionar baseline measurement**  
Antes de Tony usar graphify, medir 3 code reviews reais sem graphify (tokens usados, latência). Sem baseline, "economia de -75%" é alegação, não evidência.

**Sprint 4 — Wanda tem caso diferente dos outros Tier 2**  
Design system tem componentes com nomes genéricos (`Button`, `Card`, `Text`). Graphify pode ter dificuldade com naming se o LLM não entender o contexto de design. Testar antes de incluir no rollout automaticamente.

**Adicionar Sprint 0 (ausente no plano)**  
Antes de qualquer rollout, definir o "grafo padrão" por repo: quais repos cada agente usa, onde ficam os graphify-out/, como são nomeados. Sem isso, cada agente vai criar convenções diferentes.

### Sequência ideal revisada

```
Sprint 0 (Dia 0): Padronizar: repos, paths, convenções de nomes
Sprint 1 (Dia 1-2): Build grafo em repo MÉDIO (não OpenJarvis)
Sprint 2 (Dia 3-5): Tony Stark spike com baseline measurement
Sprint 3 (Dia 6-10): Tier 1 completo (Tony, Bruce, Steve)
Sprint 4 (Dia 11-20): Tier 2 com validação individual (Scott, Natasha, Wanda por último)
Sprint 5 (Dia 21+): Rebuild automation + monitoring
```

---

## 5. Recomendações

### Imediato (esta sessão)

1. **Trocar modelo de `qwen3.5:4b` para `qwen3.5:9b`** no build do grafo. Sim, é mais lento — mas build é one-time. Qualidade do grafo determina qualidade de todas as queries futuras. Não economize no momento errado.

2. **Adicionar `GRAPHIFY-CONVENTIONS.md`** ao workspace antes do Sprint 2: onde ficam os grafos, como são nomeados, quem rebuilda, trigger de rebuild.

3. **Escolher repo menor para Sprint 1** (ex: `jarvis-neural-interface` ou outro com 200-2k files). Valide a abordagem antes de escalar.

### Médio prazo (Sprint 3-4)

4. **Automatizar rebuild pós-merge** — cron semanal ou hook no CI que roda `graphify update` no repo principal. Sem isso, os grafos vão ficar desatualizados silenciosamente.

5. **Não distribuir Ollama por agente** — um único Ollama serve o squad inteiro. Builds são sequenciais (um por vez), queries são instantâneas. Arquitetura hub-and-spoke, não peer-to-peer.

### Métrica de sucesso (clara e mensurável)

```
Métrica primária: Tokens por sessão de code review
  Baseline: medir 10 reviews sem graphify
  Target: -50% no Tier 1 após Sprint 3
  Validação: comparar token counts reais (OpenClaw logs)

Métrica secundária: Qualidade de análise (não sacrificar pela economia)
  Método: Galvão avalia 5 reviews pré e 5 pós graphify
  Target: qualidade igual ou superior
```

---

## Conclusão

**Arquitetura aprovada com condicionantes.** Graphifyy + Ollama é a combinação certa. Antes do Sprint 3, resolver:

1. Modelo → `qwen3.5:9b` para builds
2. Repo de teste → tamanho médio, não OpenJarvis
3. Padronização → `GRAPHIFY-CONVENTIONS.md` antes do rollout
4. Baseline → medir antes de otimizar

O maior risco não é técnico. É o grafo envelhecer sem ninguém perceber. **Automatize o rebuild desde o início.**

---

*— Steve Rogers | Arquiteto de Software | Team Iron Solutions*
