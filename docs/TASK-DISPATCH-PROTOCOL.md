# Task Dispatch Protocol — Client Context Injection

> Protocolo obrigatório para garantir que as regras de cada cliente sejam SEMPRE respeitadas pelos agentes.

---

## O Problema

Cada cliente tem padrões distintos: stack diferente, regras de nomenclatura diferentes, arquitetura diferente. Sem injeção de contexto, agentes podem entregar código que não segue as regras do cliente.

**Solução:** Todo task dispatch inclui o contexto do cliente. O agente **sempre** lê os arquivos de padrões antes de executar.

---

## Protocolo Padrão de Dispatch

### Template de Task

```
[CLIENTE: <nome>]
[NODE: <nome-do-node>]
[AGENTE: <nome-do-agente>]

📋 CONTEXTO OBRIGATÓRIO (leia ANTES de qualquer ação):
- clients/<nome-do-cliente>/STANDARDS.md
- clients/<nome-do-cliente>/TECH-STACK.md
- clients/<nome-do-cliente>/CODING-RULES.md

🎯 TASK:
<Descrição da task>

📁 REPOSITÓRIO: <URL ou path no node>
🌿 BRANCH: <branch de trabalho>
✅ CRITÉRIOS DE ACEITAÇÃO:
1. <critério 1>
2. <critério 2>
```

---

## Exemplos Práticos

### Exemplo 1: Feature nova (Scott Lang / Flutter)

```
[CLIENTE: acme-corp]
[NODE: node-acme]
[AGENTE: Scott Lang]

📋 CONTEXTO OBRIGATÓRIO:
- clients/acme-corp/STANDARDS.md
- clients/acme-corp/TECH-STACK.md
- clients/acme-corp/CODING-RULES.md

🎯 TASK:
Implementar tela de histórico de pedidos conforme design em 
clients/acme-corp/designs/order-history.png

📁 REPOSITÓRIO: https://github.com/acme-corp/acme-app
🌿 BRANCH: feature/order-history
✅ CRITÉRIOS DE ACEITAÇÃO:
1. Usa Riverpod para state (StateNotifierProvider)
2. Usa go_router para navegação
3. CachedNetworkImage para imagens dos produtos
4. flutter analyze sem erros
5. Testes de widget para os 3 estados: loading, empty, populated
```

### Exemplo 2: Code review (Tony Stark / Node.js)

```
[CLIENTE: xyz-fintech]
[NODE: node-xyz]
[AGENTE: Tony Stark]

📋 CONTEXTO OBRIGATÓRIO:
- clients/xyz-fintech/STANDARDS.md
- clients/xyz-fintech/TECH-STACK.md
- clients/xyz-fintech/CODING-RULES.md

🎯 TASK:
Code review do PR #47 — Implementação de pagamento PIX
https://github.com/xyz-fintech/backend/pull/47

⚠️ ATENÇÃO ESPECIAL:
- Este cliente é fintech: regras de segurança são críticas
- Verificar especialmente: validação de entrada, tratamento de erros, logs sem dados sensíveis
```

### Exemplo 3: Bug fix urgente (Bruce Banner / Python)

```
[CLIENTE: beta-saude]
[NODE: node-beta-saude]
[AGENTE: Bruce Banner]

📋 CONTEXTO OBRIGATÓRIO:
- clients/beta-saude/STANDARDS.md
- clients/beta-saude/TECH-STACK.md

🎯 TASK: [URGENTE] Bug em produção
Endpoint /api/reports retornando 500 aleatório.
Logs: clients/beta-saude/logs/2026-08-31-error.log
Repro: chamar GET /api/reports com date_range > 90 dias

✅ CRITÉRIOS:
1. Identificar root cause
2. Fix com teste que garante não-regressão
3. PR pronto para review
```

---

## Regras do Protocolo

### Obrigatório

1. **Sempre nomear o cliente** — nenhuma task sem `[CLIENTE: ...]`
2. **Sempre listar os arquivos de contexto** — agentes devem confirmar que leram
3. **Sempre especificar o node** — para exec no lugar certo
4. **Critérios de aceitação claros** — o que é "done"?

### Boas práticas

- Para tasks de segurança, sempre adicionar `⚠️ ATENÇÃO ESPECIAL` com riscos específicos
- Para tasks de múltiplos arquivos, listar os principais afetados
- Para tasks urgentes, marcar `[URGENTE]` no título

### Proibido

- ❌ Dispatch sem contexto de cliente
- ❌ Task vaga sem critérios de aceitação
- ❌ Passar credenciais/secrets na task (usar variáveis de ambiente no node)

---

## Fluxo de Verificação do Agente

O agente deve confirmar no início da execução:

```
✅ Li STANDARDS.md do cliente [X]
✅ Li TECH-STACK.md do cliente [X]  
✅ Conectando no node [Y]
✅ Stack utilizada: [Z]
✅ Iniciando task...
```

Se o agente não confirmar isso, reenvie a task com instrução explícita:
> "Antes de qualquer código, confirme que leu os arquivos de contexto."

---

## Automação (futura)

Para times maiores, Jarvis pode automatizar o dispatch:
```bash
# Futuro: script helper
./scripts/dispatch-task.sh \
  --client acme-corp \
  --agent scott-lang \
  --node node-acme \
  --task "Implementar tela X" \
  --branch feature/tela-x
```

---

## Referência Rápida — Agentes por Tipo de Task

| Task | Agente primário | Agente backup |
|---|---|---|
| Flutter / Mobile | Scott Lang | Wanda (se design-heavy) |
| Node.js Backend | Tony Stark | — |
| Python Backend | Bruce Banner | — |
| Arquitetura | Steve Rogers | Tony Stark |
| Code Review | Tony Stark | Bruce Banner |
| QA / Testes | Natasha Romanoff | — |
| Infra / Deploy | T'Challa | — |
| Design / UX | Wanda Maximoff | — |
| Product / Roadmap | Stephen Strange | — |
| Data / IA | Visão | — |
