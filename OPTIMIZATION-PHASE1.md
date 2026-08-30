# OPTIMIZATION-PHASE1.md
# Token Economy & Performance — Phase 1

**Status:** 🟢 ATIVA desde 01/08/2026  
**Objetivo:** ~60-70% redução de custo sem sacrificar qualidade  
**Revisado:** 30/08/2026 (reconstruído após remoção acidental)

---

## 💰 Por Que Isso Importa

| Cenário | Custo/mês |
|---------|-----------|
| Tudo em Sonnet (all-Sonnet) | ~$1,500+ |
| Phase 1 (Haiku default) | ~$290-390 |
| **Economia** | **~$1,100-1,200/mês** |

---

## 🤖 Matriz de Modelos por Agente

| Agente | Papel | Modelo Default | Usa Sonnet Quando |
|--------|-------|---------------|-------------------|
| **Jarvis** | CTO / Orquestrador | Haiku | Auditoria, arquitetura, análise de risco, git cleanup complexo |
| **Tony Stark** | Backend Node.js + Tech Lead | Haiku | Code review complexo, decisões de arquitetura de API |
| **Bruce Banner** | Backend Python | Haiku | Análise de performance, algoritmos complexos |
| **Steve Rogers** | Arquiteto de Software | **Sonnet SEMPRE** | É o agente de arquitetura — Sonnet por definição |
| **Stephen Strange** | Product Manager | **Sonnet SEMPRE** | É o agente de product strategy — Sonnet por definição |
| **Visão** | Data Engineer / IA | Haiku | Pipelines complexos, modelagem de dados |
| **Wanda Maximoff** | Product Designer / UX | Haiku | Decisões de design system críticas |
| **T'Challa** | SRE Engineer | Haiku | Incidents críticos, mudanças de infraestrutura |
| **Scott Lang** | Flutter Developer | Haiku | Arquitetura mobile complexa |
| **Natasha Romanoff** | QA Engineer | Haiku | Análise de cobertura de testes crítica |
| **Peter Parker** | Content / Social Media | Haiku | Raramente — conteúdo é domínio do Haiku |

---

## 📋 14 Estratégias de Otimização

### Grupo 1: Seleção de Modelo

**1. Haiku como default**
- Haiku: $0.80/1M tokens
- Sonnet: $3.00/1M tokens (4x mais caro)
- Regra: tenta Haiku primeiro, sobe só se necessário
- **Regra de troca:** NUNCA trocar automaticamente. Sempre perguntar: "Galvão, essa tarefa tem risco de erro se feita raso — recomendo Sonnet. Autoriza?"

**2. Sonnet para decisões arquiteturais**
- Steve Rogers: sempre Sonnet (é arquiteto)
- Stephen Strange: sempre Sonnet (é PM)
- Jarvis: Sonnet para auditoria git, análise de estrutura, decisões de onde arquivos devem ficar

**3. Thinking mode seletivo**
- `thinking: medium` apenas para arquitetura e security
- `thinking: none` para tasks rotineiras
- Não ativar thinking em heartbeats, respostas simples, lookups

---

### Grupo 2: Gerenciamento de Contexto

**4. Sem context bloat**
- Load ONLY: SOUL.md, USER.md, IDENTITY.md, memory/YYYY-MM-DD.md
- Pull prior context on-demand: `memory_search()` + `memory_get()`
- Nunca carregar MEMORY.md inteiro a menos que necessário

**5. Memory search antes de ler arquivos**
- Sempre `memory_search()` antes de `read()`
- Só lê o arquivo se a busca não resolver
- Pull targeted via `memory_get(lines=X-Y)` para seções específicas

**6. Daily notes separadas do MEMORY.md**
- `memory/YYYY-MM-DD.md` = logs raw do dia
- `MEMORY.md` = memória curada de longo prazo
- Não jogar tudo no MEMORY.md — é para fatos duráveis

---

### Grupo 3: Rate Limits e Batching

**7. Rate limits mínimos**
- 5 segundos entre API calls
- 10 segundos entre web searches
- Máximo 5 searches por batch, depois pausa de 2 minutos
- Se 429: STOP, espera 5 minutos, retry

**8. Batching de requests**
- 1 request para 10 leads, não 10 requests separados
- Agrupar tasks similares em um único prompt
- Não fazer loop de requests quando batch é possível

**9. Cron para tasks repetitivas**
- Daily digests via cron, não heartbeat
- Checks periódicos via scheduled jobs
- Não re-executar manualmente o que pode ser automatizado

---

### Grupo 4: Compressão de Contexto (Phase 3 — Caveman)

**10. Caveman Middleware**
- Arquivo: `caveman-middleware-esm.js`
- Comprime contexto antes de enviar para o modelo
- Resultado validado: **-45% tokens** (meta era -30%)
- Quality score: 5.0/5.0 sem perda semântica
- Integração: `jarvis-bridge-v4.js`
- Documentação: `docs/CAVEMAN-INTEGRATION.md`

**11. Compressão seletiva**
- Caveman não comprime tudo — é inteligente
- Preserva informação crítica, comprime redundância
- Ideal para code reviews e análises longas

---

### Grupo 5: Knowledge Graphs (Phase 4 — Graphify)

**12. Graphify para code review**
- Python env: `pyproject.toml` + `uv.lock`
- Setup: `scripts/setup-graphify.sh`
- Resultado validado por agente:
  - Flutter (Scott): **-89.9%** tokens (melhor resultado)
  - Peter Parker (docs): -69.36%
  - Visão (SQL/data): -66.3%
  - T'Challa (IaC): -58.78%
  - Steve Rogers (arch): -55.6%
  - Wanda (design): -55.0%
  - Natasha (tests): -50.0%
  - Bruce (Python): -47.5%
  - Tony (Node.js): -43.1%

**13. Graphify é melhor para código declarativo**
- Flutter, React, design tokens: comprime muito (estrutura previsível)
- Python/Node.js imperativo: comprime menos (lógica variável)
- Não usar Graphify para conteúdo não-código (Peter Parker)

---

### Grupo 6: OpenRouter

**14. OpenRouter para fallback e alternativas**
- Permite trocar de provedor sem mudar código
- Útil para comparar modelos por custo/qualidade
- Configurar em `config/openclaw.template.json`
- Documentação: pendente (gap identificado em 30/08/2026)

---

## 📊 Estimativa de Custo (50M tokens/mês)

| Componente | Custo/mês |
|------------|-----------|
| Squad (10 agentes) com Haiku | ~$190 |
| Jarvis + infra | ~$100-200 |
| **Total estimado** | **~$290-390** |
| Sem otimização (all-Sonnet) | ~$1,500+ |
| **Economia total** | **~73-75%** |

### Com Phase 3 (Caveman, -45%):
- Economia adicional: ~$85/mês por squad
- Anual: ~$1,020/ano por squad

### Com Phase 4 (Graphify, -59.5% avg):
- Economia adicional: ~$3,960/ano por squad
- Total acumulado Phase 1+3+4: ~$5,000+/ano

---

## ✅ Checklist por Sessão

Antes de chamar qualquer agente ou executar qualquer task:

- [ ] Essa task precisa de Sonnet ou Haiku resolve?
- [ ] Se dúvida → pergunto ao Galvão antes de trocar
- [ ] Estou batching ou fazendo requests sequenciais desnecessários?
- [ ] Preciso carregar contexto ou memory_search() resolve?
- [ ] Task repetitiva? → considerar cron ao invés de manual

---

## 🔒 Regras Invioláveis

1. **NUNCA trocar de modelo sem perguntar ao Galvão primeiro**
2. **NUNCA declarar "está certo" sem verificar** (lição 30/08)
3. **NUNCA commitar direto na develop** — sempre PR
4. **SEMPRE preservar localmente** o que for removido do git

---

## 📎 Arquivos Relacionados

| Arquivo | Conteúdo |
|---------|----------|
| `SOUL.md` | Regras de model selection (resumo) |
| `MEMORY.md` | Histórico de decisões e resultados |
| `docs/CAVEMAN-INTEGRATION.md` | Phase 3 — integração do middleware |
| `docs/GRAPHIFY-OVERVIEW.md` | Phase 4 — visão geral |
| `docs/GRAPHIFY-SETUP.md` | Phase 4 — instalação |
| `docs/GRAPHIFY-CHEATSHEET.md` | Phase 4 — referência rápida |
| `caveman-middleware-esm.js` | Phase 3 — código do middleware |
| `scripts/setup-graphify.sh` | Phase 4 — setup automatizado |
| `pyproject.toml` | Phase 4 — dependências Python |

---

*Reconstruído em 30/08/2026 a partir de MEMORY.md, SOUL.md e histórico de sessão.*  
*Original criado em 01/08/2026.*
