# TOKEN-OPTIMIZATION.md
# Guia Completo de Economia de Tokens — Team Iron Solutions

**Status:** 🟢 ATIVO  
**Criado:** 01/08/2026 | **Revisado:** 30/08/2026  
**Objetivo:** ~60-85% redução de custo sem sacrificar qualidade

---

## 💰 Por Que Isso Importa

| Cenário | Custo/mês |
|---------|-----------|
| Tudo em Sonnet (sem otimização) | ~$1,500+ |
| Phase 1 (Haiku default) | ~$290-390 |
| Phase 3 + Caveman (-45%) | ~$210-280 |
| Phase 4 + Graphify (-59.5%) | ~$170-220 |
| **Economia total acumulada** | **~73-85%** |

---

## 🤖 Matriz de Modelos por Agente

| Agente | Papel | Modelo Default | Usa Sonnet Quando |
|--------|-------|---------------|-------------------|
| **Jarvis** | CTO / Orquestrador | Haiku | Auditoria, arquitetura, análise de risco, git cleanup complexo |
| **Tony Stark** | Backend Node.js + Tech Lead | Haiku | Code review complexo, decisões de API |
| **Bruce Banner** | Backend Python | Haiku | Performance avançada, algoritmos |
| **Steve Rogers** | Arquiteto de Software | **Sonnet SEMPRE** | É o agente de arquitetura |
| **Stephen Strange** | Product Manager | **Sonnet SEMPRE** | É o agente de product strategy |
| **Visão** | Data Engineer / IA | Haiku | Pipelines complexos |
| **Wanda Maximoff** | Product Designer / UX | Haiku | Decisões críticas de design system |
| **T'Challa** | SRE Engineer | Haiku | Incidents críticos, mudanças de infra |
| **Scott Lang** | Flutter Developer | Haiku | Arquitetura mobile complexa |
| **Natasha Romanoff** | QA Engineer | Haiku | Análise crítica de cobertura |
| **Peter Parker** | Content / Social Media | Haiku | Raramente necessário |

### 🔒 Regra de Troca de Modelo
**NUNCA trocar automaticamente.** Sempre perguntar:
> "Galvão, essa tarefa tem risco de erro se feita raso — recomendo Sonnet. Autoriza?"

A decisão é do Galvão, não do agente.

---

## 📋 Estratégias de Otimização

### 🔵 Grupo 1: Seleção de Modelo

**1. Haiku como default**
- Haiku: $0.80/1M tokens | Sonnet: $3.00/1M tokens (4x mais caro)
- Regra: tenta Haiku primeiro, sobe só se necessário e autorizado

**2. Sonnet apenas para decisões de alto risco**
- Steve Rogers e Stephen Strange: sempre Sonnet (papéis exigem)
- Jarvis: Sonnet para auditoria, estrutura de repo, decisões arquiteturais
- Lição 30/08/2026: Haiku declarou repo "limpo" sem auditar — custo de retrabalho superou custo do Sonnet

**3. Thinking mode seletivo**
- `thinking: medium` apenas para arquitetura e segurança
- `thinking: none` para tasks rotineiras e heartbeats

---

### 🔵 Grupo 2: Gerenciamento de Contexto

**4. System Prompts LEAN por agente (82-85% economia)**
- Cada agente: 300-400 tokens (vs. 2,000+ com playbook inline)
- 10 agentes × 350 tokens = 3,500 tokens total (vs. 20,000+)
- Estrutura: identity + responsabilidades + frameworks (nomes) + checklist rápido (8-12 items) + referência ao playbook

**5. Playbooks carregados sob demanda**
- Agente usa system prompt lean para tasks simples
- Consulta playbook apenas quando precisa detalhe específico:
  ```
  memory_get("TONY-STARK-EXCELLENCE-PLAYBOOK.md", from=150, lines=40)
  ```
- Média: +500-800 tokens por consulta (não 2,000 inline)

**6. Memory search antes de ler arquivos**
- Sempre `memory_search()` antes de `read()`
- `memory_get(lines=X-Y)` para seções específicas
- Nunca carregar MEMORY.md inteiro sem necessidade

---

### 🔵 Grupo 3: Rate Limits e Batching

**7. Rate limits mínimos**
- 5 segundos entre API calls
- 10 segundos entre web searches
- Máximo 5 searches por batch → pausa de 2 minutos
- Se 429: STOP, espera 5 minutos, retry

**8. Batching de requests**
- 1 request para N tasks similares, não N requests sequenciais
- Agrupar análises, reviews, e lookups em um único prompt quando possível

**9. Cron para tasks repetitivas**
- Daily digests, checks periódicos → cron jobs (não heartbeat manual)
- Não re-executar manualmente o que pode ser agendado

---

### 🔵 Grupo 4: Compressão de Contexto — Phase 3 (Caveman)

**10. Caveman Middleware**
- Arquivo: `caveman-middleware-esm.js`
- Comprime input antes de enviar ao modelo
- **Resultado validado:** -45% tokens (meta era -30%) | Quality: 5.0/5.0
- Integração: `jarvis-bridge-v4.js` (jarvis-neural-interface)
- Documentação: `docs/CAVEMAN-INTEGRATION.md`

**11. Compressão seletiva**
- Preserva informação crítica, elimina redundância
- Ideal para code reviews e análises longas
- Economia mensal confirmada: ~$85/mês por squad (~$1,020/ano)

---

### 🔵 Grupo 5: Knowledge Graphs — Phase 4 (Graphify)

**12. Graphify para code review**
- Converte código em grafos AST antes de enviar ao modelo
- Setup: `scripts/setup-graphify.sh` | Deps: `pyproject.toml`
- Documentação: `docs/GRAPHIFY-SETUP.md`, `docs/GRAPHIFY-OVERVIEW.md`

**13. Resultados validados por agente (Sprint 3)**

| Agente | Contexto | Compressão | Qualidade |
|--------|----------|------------|-----------|
| Scott Lang | Flutter (declarativo) | **-89.9%** | 4.7/5 |
| Peter Parker | Documentação | -69.36% | 4.5/5 |
| Visão | SQL/Data | -66.3% | 4.65/5 |
| T'Challa | IaC/Infra | -58.78% | 4.51/5 |
| Steve Rogers | Arquitetura | -55.6% | 4.60/5 |
| Wanda Maximoff | Design systems | -55.0% | 4.56/5 |
| Natasha Romanoff | Testes | -50.0% | 4.56/5 |
| Bruce Banner | Python imperativo | -47.5% | 4.49/5 |
| Tony Stark | Node.js imperativo | -43.1% | 4.5/5 |
| **Média** | | **-59.5%** | **4.57/5** |

**Insight:** código declarativo (Flutter, design tokens) comprime muito mais que imperativo (Python, Node.js).

**14. Economia estimada Graphify**
- Economia adicional: ~$3,960/ano por squad
- Total acumulado Phase 1+3+4: ~$5,000+/ano

---

### 🔵 Grupo 6: OpenRouter

**15. OpenRouter para alternativas de provedor**
- Permite trocar de provedor sem mudar código
- Útil para comparar custo/qualidade entre modelos
- Configurar em `config/openclaw.template.json`
- ⚠️ Documentação técnica de integração: **pendente**

---

## ✅ Checklist por Sessão (Jarvis)

Antes de executar qualquer task:
- [ ] Haiku resolve ou preciso de Sonnet? Se Sonnet → **perguntar ao Galvão primeiro**
- [ ] Estou batching ou fazendo requests sequenciais?
- [ ] `memory_search()` resolve ou preciso ler arquivo?
- [ ] Task repetitiva? → cron em vez de manual
- [ ] Se remover arquivo do git → preservar em `.local/` **E** Obsidian

---

## 🔒 Regras Invioláveis

1. **NUNCA trocar de modelo sem autorização do Galvão**
2. **NUNCA declarar "está certo/limpo" sem verificar** (lição 30/08)
3. **NUNCA commitar direto na develop** — sempre branch + PR
4. **SEMPRE preservar em `.local/` + Obsidian** o que for removido do git
5. **NUNCA apresentar análise rasa como definitiva** — dizer que precisa ir mais fundo

---

## 📊 Estimativa de Custo (50M tokens/mês)

| Componente | Custo/mês |
|------------|-----------|
| Squad (10 agentes) Haiku | ~$190 |
| Jarvis + infra | ~$100-200 |
| **Total Phase 1** | **~$290-390** |
| Com Phase 3 (Caveman -45%) | ~$210-280 |
| Com Phase 4 (Graphify -59.5%) | ~$170-220 |

---

## 📎 Arquivos Relacionados

| Arquivo | Conteúdo |
|---------|----------|
| `SOUL.md` | Regras de model selection (resumo operacional) |
| `MEMORY.md` | Histórico de decisões e resultados por fase |
| `docs/CAVEMAN-INTEGRATION.md` | Phase 3 — integração do middleware |
| `docs/GRAPHIFY-OVERVIEW.md` | Phase 4 — visão geral e arquitetura |
| `docs/GRAPHIFY-SETUP.md` | Phase 4 — instalação passo a passo |
| `docs/GRAPHIFY-CHEATSHEET.md` | Phase 4 — referência rápida |
| `docs/PLAYBOOKS-TOKEN-EFFICIENCY-STRATEGY.md` | Estratégia de lazy-loading de playbooks |
| `caveman-middleware-esm.js` | Phase 3 — código do middleware |
| `scripts/setup-graphify.sh` | Phase 4 — setup automatizado |
| `pyproject.toml` | Phase 4 — dependências Python |
| `agents-workspaces/*/EXCELLENCE-PLAYBOOK.md` | Playbooks por agente |

---

*Criado em 01/08/2026. Reconstruído em 30/08/2026 a partir de MEMORY.md, SOUL.md, PLAYBOOKS-TOKEN-EFFICIENCY-STRATEGY.md e histórico de sessão.*
