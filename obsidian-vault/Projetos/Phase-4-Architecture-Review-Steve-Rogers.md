# Phase 4 — Architecture Review (Steve Rogers - Assinado)

**Autor:** Steve Rogers — CTO / Arquiteto de Software  
**Data:** 26 de agosto de 2026  
**Status:** ✅ ASSINADO | FINAL  
**Sessão:** agent:steve:main (agente real do time)  

---

## 🎯 Veredicto Executivo

> **GO — com 4 pré-condições obrigatórias antes do Sprint 3**

Graphifyy + Ollama é a arquitetura correta. A análise preliminar está tecnicamente correta em todos os pontos críticos.

---

## ✅ Validação Completa

- ✅ **Viabilidade Técnica:** Tree-sitter + LLM semântico (Ollama local) é abordagem certa
- ✅ **Riscos Identificados:** Gargalo memória (build apenas), qualidade LLM, staleness, cold start
- ✅ **Integração OpenClaw:** `exec` direto, sem middleware
- ✅ **Alternativas:** Graphifyy vs Joern (Joern overkill)
- ✅ **3 Ajustes Críticos:** Modelo 9b, repo médio (não OpenJarvis), GRAPHIFY-CONVENTIONS.md

---

## 🔧 Refinamentos de Steve

### 1. Gargalo de Memória (ALTO)
- ✅ Contenção é SÓ durante *build*, não queries (JSON local)
- **Ação:** Builds sequenciais (nunca paralelos), coordenados por Jarvis

### 2. Wanda Maximoff é Caso Especial
- Design system tem componentes com nomes genéricos (Button, Card, Text)
- LLM 9b pode gerar labels pouco discriminativos
- **Ação:** Testar isolado antes de Tier 2

### 3. Baseline é OBRIGATÓRIO
- Não opcional — sem baseline não há evidência, só alegação
- **Protocolo:** 5 code reviews SEM graphify (antes Sprint 2), depois 5 COM graphify
- Decisão Sprint 3 baseada em dados reais, não estimativas

### 4. Risco Maior = Staleness Silenciosa
- Grafo envelhece com PRs/mudanças
- **Ação:** Rebuild automático não é otimização, é requisito operacional
- Sem isso, investimento Phase 4 deprecia silenciosamente

---

## 📋 4 Pré-condições para Sprint 3

Antes de Tier 1 rollout:

1. ✅ **GRAPHIFY-CONVENTIONS.md** criado (Sprint 0)
2. ✅ **Build em repo médio** com qwen3.5:9b validado (Sprint 1)
3. ✅ **Baseline coletado** — 5 reviews reais sem graphify (Sprint 2)
4. ✅ **Rebuild automation** definida (manual inicialmente, ok)

---

## 🗂️ Conteúdo Mínimo GRAPHIFY-CONVENTIONS.md

```
1. PATH PADRÃO: ~/repos/{nome-repo}/graphify-out/
2. MODELO: qwen3.5:9b (builds) | NUNCA 2b em produção
3. REBUILD TRIGGER: pós-merge main/master (manual até automação)
4. BUILDS: sequenciais, coordenados por Jarvis (não paralelos)
5. QUERY PADRÃO: graphify explain → graphify path → read
6. GRAFO STALE: ≥7 dias = STALE (avisar antes de usar)
7. REPOS MAPEADOS: tabela nome → path → data último build
```

---

## 📊 Métricas de Sucesso

| Métrica | Baseline | Target | Quando |
|---|---|---|---|
| Tokens/session | Medir Sprint 2 | -50% | Após Sprint 3 |
| Latência (s) | Medir Sprint 2 | -40% | Após Sprint 3 |
| Qualidade análise | Avaliação humana | Igual+ | Após Sprint 3 |
| Adoção Tier 1 | 0% | 100% em ≥80% reviews | Semana 2 Sprint 3 |
| Staleness máx | N/A | ≤7 dias | Contínuo |
| Falsos positivos | N/A | ≤5% | 20 queries validadas |

---

## 🔐 Assinatura

> **Eu, Steve Rogers, CTO e Arquiteto de Software do Team Iron Solutions, valido esta arquitetura.**
>
> Graphifyy + Ollama local é a decisão correta para Phase 4. Análise preliminar está tecnicamente correta e estrategicamente alinhada: local-first, zero custo incremental, qualidade antes de velocidade.
>
> **Veredicto: GO — com as 4 pré-condições listadas acima.**
>
> O maior risco não é técnico. É operacional: grafos que envelhecem silenciosamente. Automatize o rebuild desde o primeiro dia.
>
> *"A melhor arquitetura resolve o problema hoje E permite mudança amanhã."*

— **Steve Rogers** | CTO | Team Iron Solutions | 26/08/2026

---

## 📌 Próximas Ações

- [ ] Sprint 0: Criar GRAPHIFY-CONVENTIONS.md
- [ ] Sprint 1: Build em repo médio (jarvis-neural-interface) com qwen3.5:9b
- [ ] Sprint 2: Tony Stark spike + baseline measurement
- [ ] Sprint 3: Tier 1 rollout (Tony, Bruce, Steve)
- [ ] Sprint 4: Tier 2 (Scott, Natasha, Wanda isolado)
- [ ] Sprint 5: Automation + monitoring

---

**Documento arquivado em Obsidian: 26/08/2026 14:34 GMT-3**
