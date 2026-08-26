# GRAPHIFY-CONVENTIONS.md

**Padrões Operacionais — Phase 4 Token Optimization**

**Versão:** 1.0  
**Data de Publicação:** 26 de agosto de 2026  
**Autorizado por:** Steve Rogers (CTO)  
**Status:** ✅ ATIVO desde Sprint 0  

---

## 📋 Seção 1 — Path Padrão

Todos os grafos (`graphify-out/`) são armazenados no **raiz do repositório**:

```bash
~/repos/{nome-repo}/
├── src/
├── tests/
├── graphify-out/          # ← PADRÃO (gerado por `graphify .`)
│   ├── graph.json         # Arquivo principal (queryável)
│   ├── GRAPH_REPORT.md    # Sumário do grafo
│   ├── graph.html         # Visualização (opcional)
│   └── cache/             # Cache AST (não commitado)
└── .gitignore            # graphify-out/cache/ ignorado
```

**Por quê este padrão?**
- Simples: `graphify .` automaticamente cria em `./graphify-out`
- Consistente: qualquer agente encontra no mesmo lugar
- Isolado: não polui raiz do repo, fácil de limpar

---

## 🧠 Seção 2 — Modelo LLM (Obrigatório)

### Build (Geração do Grafo)

```bash
graphify . \
  --backend ollama \
  --model qwen3.5:9b \
  --max-concurrency 1
```

**Regra crítica (Steve Rogers):**
- ✅ **qwen3.5:9b** — recomendado para produção (qualidade máxima)
- ⚠️ **qwen3.5:4b** — SÓ se memória crítica durante build
- ❌ **qwen3.5:2b** — NUNCA em produção (labels genéricos)

**Justificativa:** Build é one-time. Qualidade do grafo é permanente. Economizar no modelo neste momento = economizar no alicerce.

### Query (Uso do Grafo)

Queries executadas contra `graph.json` **não** usam LLM — são leitura direta do JSON. Modelo LLM é acionado SÓ durante build.

---

## 🔄 Seção 3 — Rebuild Trigger

### Quando Rebuildar

**Trigger Obrigatório:** Após merge para `main` ou `master`

```bash
# Após PR mergeada
git checkout main
git pull
cd ~/repos/{nome-repo}
source ~/.openclaw/workspace/graphify-env/bin/activate
graphify update .  # Incremental — só reprocessa mudanças
```

**Trigger Opcional:** Mudanças major (refactoring grande, nova arquitetura)

### Timing

- **Durante:** Imediatamente após merge (max 1 hora de lag)
- **Frequência:** Mínimo 1x/semana, ideal 1x/dia para repos ativos
- **Parallelismo:** NUNCA paralelo — ver seção 4

### Manual vs Automático

| Fase | Modo | Ação |
|---|---|---|
| Sprint 0-1 | Manual | Jarvis ou dev rebuild quando notificado |
| Sprint 2+ | Manual | Trigger de merge (webhook ou cron) |
| Sprint 5+ | Automático | CI/CD hook pós-merge |

---

## ⚡ Seção 4 — Builds: Sequenciais, Coordenação Jarvis

**Regra Crítica:** Apenas 1 build por vez no Mac mini.

```
❌ NUNCA FAZER:
- Tony builds Node repo
- Bruce builds Python repo (simultâneo)
→ Contenção Ollama, swap memory, build falha

✅ SEMPRE FAZER:
- Tony solicita build → Jarvis coordena
- Build 1 completa → Jarvis inicia build 2
- Agentes aguardam resultado (push-based)
```

### Coordenação

**Quando agente precisa novo grafo:**

1. Agente: mensagem via sessions_send para Jarvis
   ```
   "Jarvis, rebuild grafo de {nome-repo} com qwen3.5:9b"
   ```

2. Jarvis: verifica se outro build rodando
   - Se NÃO: inicia build imediatamente
   - Se SIM: queue para próximo slot

3. Jarvis: notifica agente quando pronto
   ```
   "Graph rebuilt: {repo}, nodes=X, edges=Y, time=Zs"
   ```

### Memória Esperada Durante Build

```
qwen3.5:9b durante build: ~6-7 GB RAM
qwen3.5:4b durante build: ~4-5 GB RAM

Mac mini disponível: ~16 GB total
Reservado (sistema, outros serviços): ~6-8 GB

Limite seguro: não iniciar novo build se <3 GB livre
```

---

## 🔍 Seção 5 — Query Padrão (Agentes)

### Fluxo Correto de Análise

**NUNCA read-first. SEMPRE graphify-first.**

```
Agente recebe task: "Revisa feature XYZ"
    ↓
1️⃣ graphify explain "ClassePrincipal"
    → Estrutura, dependências diretas (~300 tokens)
    ↓
2️⃣ graphify path "ClasseA" "ClasseB" (se necessário)
    → Impacto de mudança, transitividade (~200 tokens)
    ↓
3️⃣ read arquivo.ts (só se preciso ver código específico)
    → Contexto cirúrgico, validação (~500 tokens)

TOTAL: ~1000 tokens (vs 5000+ sem graphify)
```

### Comandos Disponíveis

```bash
# Explicação de classe/função
graphify explain "NomeEntidade" --path ~/repos/{repo}/graphify-out

# Caminho entre duas entidades (direto ou transitivo)
graphify path "ClasseA" "ClasseB"
graphify path "Button" "*" --transitive  # Tudo que depende de Button

# Query estrutural
graphify query "type:function language:python"
graphify query "parent:Controller"

# Atualizar grafo (incremental)
graphify update .
```

### Latência Esperada

| Operação | Tempo |
|---|---|
| graphify explain | <1s |
| graphify path | <2s |
| graphify query | <5s |
| read arquivo.ts | 2-5s |
| Total review | ~15-20s (vs 45s sem graphify) |

---

## 📅 Seção 6 — Staleness (Grafo Desatualizado)

### Checklist de Freshness

```
✅ FRESCO (use confiante):
   - Gerado nos últimos 7 dias
   - Última commit no grafo é recente

⚠️ ENVELHECIDO (use com cuidado):
   - 7-14 dias sem rebuild
   - Avise antes de usar ("grafo pode estar desatualizado")

🔴 OBSOLETO (rebuild obrigatório):
   - >14 dias sem rebuild
   - Novos arquivos adicionados (não no grafo)
   - Refactoring major ocorreu
```

### Como Verificar

```bash
# Data de geração
ls -lh ~/repos/{repo}/graphify-out/graph.json

# Último commit relevante
cd ~/repos/{repo}
git log --oneline -n 1

# Se diferença > 7 dias, rebuild
graphify update .
```

### Aviso Automático

Quando agente consulta grafo com >7 dias de idade:

```
⚠️ ATENÇÃO: Grafo de {repo} tem {X} dias (última rebuild {data})
   Pode estar desatualizado. Rebuild? (sim/não)
```

---

## 🗂️ Seção 7 — Repos Mapeados

**Tabela de registros (atualizar conforme novos repos entram)**

| Repo | Path | Agente Proprietário | Status | Último Build | Modelo |
|---|---|---|---|---|---|
| jarvis-neural-interface | `~/repos/jarvis-neural-interface` | Tony Stark | ✅ Ativo | 2026-08-26 14:30 | qwen3.5:9b |
| OpenJarvis | `~/.openclaw/workspace/OpenJarvis` | Bruce Banner | 🔄 Testing | 2026-08-26 (building) | qwen3.5:9b |
| team-iron-backend | (TBD) | Tony Stark | ⏳ Planned | N/A | qwen3.5:9b |
| design-system-flutter | (TBD) | Wanda Maximoff | ⏳ Planned | N/A | qwen3.5:9b |

**Adicionar novos repos conforme descobertos.**

---

## 🚨 Troubleshooting

### "graphify command not found"
```bash
source ~/.openclaw/workspace/graphify-env/bin/activate
```

### "Ollama não responde"
```bash
curl http://localhost:11434/api/tags
# Se falhar:
ollama serve &
```

### "Graph.json muito grande"
```bash
# Comprimir
cd ~/repos/{repo}/graphify-out
gzip graph.json → graph.json.gz

# Ou split por módulo (future optimization)
```

### "Rebuild levou >1 hora"
```bash
# Cancelar e verificar Ollama
pkill graphify
ollama list
# Pode estar usando modelo errado ou mem issue
```

---

## 📝 Changelog

| Data | Mudança | Autor |
|---|---|---|
| 2026-08-26 | Versão 1.0 inicial | Steve Rogers (CTO) |
| (TBD) | Automated rebuild hooks | Jarvis |
| (TBD) | Multi-model strategy | (Arquitetura) |

---

## 🔐 Autorização & Responsabilidade

- **CTO Approval:** Steve Rogers ✅ 26/08/2026
- **Maintained by:** Jarvis (Tech Lead)
- **Escalation:** Steve Rogers (CTO) se violações

**Violações comuns:**
- ❌ Usar qwen3.5:2b em produção → escalate
- ❌ Builds paralelos → escalate
- ❌ Grafo com >21 dias sem rebuild → notify + rebuild automático

---

**Este documento é referência obrigatória para Phase 4. Todas padrões acima são não-negociáveis até Sprint 5 (revisão).**
