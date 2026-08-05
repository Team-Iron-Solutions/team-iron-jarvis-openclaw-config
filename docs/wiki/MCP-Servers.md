# 🔌 MCP Servers

Model Context Protocol servers integrados — ferramentas que seus agentes podem usar.

---

## 📦 Servidores Configurados (3)

### 1️⃣ Memory — Contexto Persistente

**Função:** Agentes salvam e recuperam contexto entre runs

**Ferramentas (9):**
- `memory__add_observations` — registrar insights
- `memory__create_entities` — criar entidades (pessoas, projetos, decisões)
- `memory__create_relations` — conectar entidades (grafo de conhecimento)
- `memory__delete_entities` — remover
- `memory__search_nodes` — buscar contexto
- `memory__open_nodes` — abrir entidades
- `memory__read_graph` — ver grafo completo
- `memory__delete_observations` — remover insights
- `memory__delete_relations` — remover conexões

**Use Cases:**
```bash
# Salvar decisão arquiteural
openclaw agent --agent steve-rogers --message "
Documenta que decidimos usar PostgreSQL + Redis
pra este projeto porque...
(use memory__create_entities e memory__create_relations)
"

# Recuperar contexto
openclaw agent --agent tony-stark --message "
Qual foi a decisão que fizemos sobre autenticação?
(procure em memory)
"
```

**Status:** ✅ Configurado e operacional

---

### 2️⃣ Filesystem — Leitura/Escrita Local

**Função:** Agentes leem e escrevem arquivos do workspace

**Ferramentas (6):**
- `filesystem__read_file` — ler código/docs
- `filesystem__write_file` — criar/editar arquivos
- `filesystem__list_directory` — explorar estrutura
- `filesystem__search_files` — grep/busca
- `filesystem__create_directory` — organizar workspace
- `filesystem__move_file` — refatorar/renomear

**Escopo:** `/Users/teamironsolutions/.openclaw/workspace`

**Use Cases:**
```bash
# Code review
openclaw agent --agent tony-stark --message "
Revise o arquivo app.js (filesystem__read_file)
"

# Criar novo arquivo
openclaw agent --agent steve-rogers --message "
Crie um arquivo ARCHITECTURE.md documentando a decisão
(use filesystem__write_file)
"

# Buscar padrões
openclaw agent --agent natasha-romanoff --message "
Procure por todos os arquivos de test no workspace
(use filesystem__search_files)
"
```

**Status:** ✅ Configurado e operacional

---

### 3️⃣ GitHub — Repositórios e Código

**Função:** Agentes trabalham com GitHub (repos, issues, PRs, code)

**Ferramentas (26):**

**Repos:**
- `github__create_repository` — criar novo repo
- `github__fork_repository` — fazer fork
- `github__search_repositories` — buscar repos

**Issues:**
- `github__create_issue` — abrir issue
- `github__get_issue` — obter detalhes
- `github__list_issues` — listar issues
- `github__update_issue` — atualizar status
- `github__add_issue_comment` — comentar

**Pull Requests:**
- `github__create_pull_request` — abrir PR
- `github__get_pull_request` — detalhes PR
- `github__list_pull_requests` — listar PRs
- `github__get_pull_request_comments` — ler comentários
- `github__create_pull_request_review` — fazer review
- `github__merge_pull_request` — fazer merge
- `github__update_pull_request_branch` — sincronizar branch

**Code:**
- `github__get_file_contents` — ler arquivo
- `github__create_or_update_file` — criar/editar arquivo
- `github__push_files` — fazer commit
- `github__search_code` — buscar código
- `github__list_commits` — ver histórico
- `github__get_pull_request_status` — status CI/CD
- `github__search_users` — buscar usuários
- `github__search_issues` — buscar issues

**Use Cases:**
```bash
# Criar repo
openclaw agent --agent tony-stark --message "
Crie um repositório chamado 'auth-module'
com descrição 'Módulo de autenticação reutilizável'
"

# Abrir issue
openclaw agent --agent stephen-strange --message "
Abra uma issue pra implementar OAuth2
"

# Code review + merge
openclaw agent --agent tony-stark --message "
Revise o PR #42 em nosso repo,
se está bom, faz merge.
"

# Search code
openclaw agent --agent natasha-romanoff --message "
Procure por todos os TODO comments
em todo nosso código no GitHub
"
```

**Autenticação:** Requer `GITHUB_TOKEN`  
**Status:** ✅ Configurado (se token foi setado)

---

## 🚀 Adicionar Mais Servidores

### PostgreSQL (Data Queries)

```bash
export DATABASE_URL="postgresql://user:pass@localhost/db"

openclaw mcp add postgres \
  --command npx \
  --arg -y \
  --arg @modelcontextprotocol/server-postgres \
  --env DATABASE_URL="$DATABASE_URL"

openclaw mcp probe postgres
```

**Use:** Visão executa queries diretamente

```bash
openclaw agent --agent visao --message "
Quantos usuários ativos temos?
(use postgres MCP)
"
```

---

### Slack (Team Communication)

```bash
export SLACK_BOT_TOKEN="xoxb-..."

openclaw mcp add slack \
  --command npx \
  --arg -y \
  --arg @modelcontextprotocol/server-slack \
  --env SLACK_BOT_TOKEN="$SLACK_BOT_TOKEN"
```

**Use:** Agentes mandam mensagens no Slack

---

### Notion (Documentação)

```bash
export NOTION_API_KEY="secret_..."

openclaw mcp add notion \
  --command npx \
  --arg -y \
  --arg @modelcontextprotocol/server-notion \
  --env NOTION_API_KEY="$NOTION_API_KEY"
```

---

## 🔧 Gerenciar Servidores MCP

### Listar todos
```bash
openclaw mcp list
```

### Ver detalhes
```bash
openclaw mcp show github
openclaw mcp status --verbose
```

### Validar saúde
```bash
openclaw mcp doctor --probe
```

### Remover
```bash
openclaw mcp unset postgres
```

### Atualizar
```bash
openclaw mcp configure github --timeout 30 --include 'search_*'
```

---

## 📊 Tool Filters (Segurança)

Você pode restringir quais ferramentas cada MCP servidor expõe:

```bash
openclaw mcp add github \
  --include 'create_issue,get_issue,list_issues' \
  --exclude 'delete_*'
```

**Include only:** Whitelist de ferramentas  
**Exclude:** Blacklist de ferramentas

---

## 🔐 Credentials & Secrets

**NÃO commite secrets!** Armazene:

```bash
# Local file (não versionado)
echo "ghp_YYYY" > ~/.openclaw/.github-token
chmod 600 ~/.openclaw/.github-token

# Ou env variable
export GITHUB_TOKEN="ghp_YYYY"

# Depois use em config:
export GITHUB_TOKEN=$(cat ~/.openclaw/.github-token)
```

---

## 📈 Monitoring

```bash
# Ver logs de MCP
openclaw gateway --verbose

# Trace uma chamada
GIT_TRACE=1 openclaw agent --agent tony-stark --message "..."

# Diagnosticar problema
openclaw mcp doctor postgres --probe --verbose
```

---

## 🎓 Exemplos Completos

### Workflow: Criar Repo + Issue + Pull Request

```bash
# 1. Steve (design)
openclaw agent --agent steve-rogers --message "
Desenhe a arquitetura pra módulo de autenticação
(salve em memory)
"

# 2. Tony (implementação)
openclaw agent --agent tony-stark --message "
1. Crie um repo chamado 'auth-module' no GitHub (github__create_repository)
2. Abra uma issue descrevendo a implementação
3. Crie um branch 'feature/oauth2'
"

# 3. Tony (development)
openclaw agent --agent tony-stark --message "
Crie um arquivo app.js básico e faça push (github__push_files)
"

# 4. Natasha (testing)
openclaw agent --agent natasha-romanoff --message "
Veja os commits no GitHub e escreva testes
"

# 5. Tony (merge)
openclaw agent --agent tony-stark --message "
Revise a PR, aprove e faz merge se está bom
"
```

### Workflow: Data Analysis

```bash
# 1. Query database
openclaw agent --agent visao --message "
Qual é o padrão de acesso mais comum?
(use postgres MCP)
"

# 2. Document findings
openclaw agent --agent visao --message "
Crie um arquivo ANALYSIS.md documentando os findings
(use filesystem__write_file)
"

# 3. Push pra GitHub
openclaw agent --agent visao --message "
Faça commit de ANALYSIS.md no GitHub
(use github__push_files)
"
```

---

## 🔗 Recursos

- **MCP Protocol:** https://modelcontextprotocol.io
- **GitHub API Docs:** https://docs.github.com/rest
- **OpenClaw MCP Docs:** https://docs.openclaw.ai/cli/mcp

---

**Próximo?** Veja [System Architecture](System-Architecture) pra entender como tudo se integra!

---

**Last Updated:** 2026-08-05
