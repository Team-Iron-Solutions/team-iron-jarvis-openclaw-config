# EXCELLENCE-CHECKLIST — Validação de Qualidade ao Finalizar Tarefas

**Status:** ✅ LIVE (02/08/2026)  
**Uso:** Todos os agentes executam este checklist antes de marcar tarefa como "done"  
**Tempo esperado:** 5-10 minutos por tarefa

---

## Overview

Este checklist consolida os padrões de excelência dos 7 playbooks. Cada agente executa a seção relevante ao seu papel antes de finalizar uma tarefa.

**Golden Rule:** Se a tarefa não passa no checklist, não é done ainda.

---

## 🟡 UNIVERSAL — Todos os Agentes

### Clareza & Documentação
- [ ] Tarefa está claramente definida (scope, entregáveis)
- [ ] Decisões importantes estão documentadas (por quê escolheu isso?)
- [ ] Há exemplos concretos (não abstratos demais)
- [ ] Qualquer follow-up ou "aberto" está identificado
- [ ] Links/referências: PRD, ADR, código, Figma, etc.

### Qualidade Técnica Geral
- [ ] Código/artefato é legível (alguém consegue ler em 5 min?)
- [ ] Sem magic numbers, strings hardcoded, ou TODO comments órfãos
- [ ] Erros tratados explicitamente (não "deixa quebrar")
- [ ] Performance foi considerada (não é O(N²) quando poderia ser O(N log N))
- [ ] Segurança: sem SQL injection, secrets hardcoded, ou CORS abertos

### Comunicação
- [ ] Resultado é comunicado claramente (resumo executivo de 2-3 linhas)
- [ ] Bloqueadores/dependências estão explícitos
- [ ] Próximos passos são claros (quem faz quê depois?)
- [ ] Feedback de colega foi solicitado/incorporado (não trabalha sozinho)

---

## 🟦 BACKEND — Tony Stark, Bruce Banner

### Architecture & Design
- [ ] Segue Domain-Driven Design (ou explicita por quê não)
  - Entidades refletem realidade (não BD schema)
  - Value objects encapsulam regras (HR, Pace, etc)
  - Repositórios isolam dados
  - Services orquestram lógica

- [ ] SOLID Principles aplicados
  - [ ] Single Responsibility — classe tem 1 razão de mudança?
  - [ ] Open/Closed — posso adicionar tipo novo sem mexer em 5 arquivos?
  - [ ] Liskov Substitution — subtipo não quebra contrato?
  - [ ] Interface Segregation — interfaces não têm 20 métodos?
  - [ ] Dependency Inversion — injeto abstrações, não concreto?

- [ ] REST API Design (se for endpoint)
  - [ ] Substantivos, não verbos (POST /workouts, não POST /createWorkout)
  - [ ] Status HTTP corretos (201 Created, 400 Bad Request, 404 Not Found, 422 Unprocessable Entity)
  - [ ] Versionamento claro (/api/v1/...)
  - [ ] Responses estruturados (não raw data)

### Testing & Validation
- [ ] Unit tests existem (lógica de negócio testada)
  - [ ] Coverage >90% na lógica crítica (SonarQube padrão)
  - [ ] Casos edge cobertos (boundary conditions, null, etc)
  - [ ] Tests têm nomes claros ("test_prescribe_workout_with_valid_input")

- [ ] Integration tests existem (API + BD)
  - [ ] Testa fluxo end-to-end
  - [ ] Usa test database (não production)
  - [ ] Cleanup/teardown adequado

- [ ] Error handling testado
  - [ ] Exceções levantadas corretamente
  - [ ] Erros têm contexto (não genérico "error")
  - [ ] Retry logic funciona (se aplicável)

### Performance
- [ ] N+1 queries identificadas e resolvidas
  - [ ] JOINs/relationships são explícitas
  - [ ] Batch queries quando apropriado
  - [ ] Índices no BD estão presentes

- [ ] Caching estratégico
  - [ ] Redis usado onde faz sentido (não cache everything)
  - [ ] TTLs sensatos (não cache por sempre)
  - [ ] Invalidação clara (quando é obsoleto?)

- [ ] Benchmarks/profiling executados
  - [ ] P95 latência medida (<100ms target)
  - [ ] Memory profiling (não memory leak)
  - [ ] Resultados documentados

### Code Review Readiness
- [ ] Código é self-documenting (nomes claros)
- [ ] Comments explicam "por quê", não "o quê"
- [ ] Refatorações grandes têm issue/ADR
- [ ] Está pronto para ser revisado por colega

---

## 🟨 ARCHITECTURE — Steve Rogers

### Decisão Arquitetural
- [ ] ADR (Architecture Decision Record) foi criado/atualizado
  - [ ] Context claro (por que esse problema?)
  - [ ] Decision explícita (o quê escolhemos?)
  - [ ] Rationale sólido (por quê essa escolha?)
  - [ ] Consequences documentadas (trade-offs?)
  - [ ] Alternativas consideradas (por que não X ou Y?)
  - [ ] Status (Approved, Pending, Superseded)

- [ ] Trade-offs explícitos
  - [ ] Performance vs. Consistency (ACID? Eventual?)
  - [ ] Cost vs. Reliability (single-instance? HA?)
  - [ ] Complexity vs. Flexibility (monolith? Microservices?)
  - [ ] Cada trade-off tem rationale

### Scalability & Non-Functional Requirements
- [ ] Escala foi estimada
  - [ ] Usuários/atletas: quantos?
  - [ ] Requests/segundo: estimado
  - [ ] Storage: calculado
  - [ ] Tudo baseado em dados, não achismo

- [ ] Non-functional requirements validados
  - [ ] Availability target (99.5%? 99.9%?)
  - [ ] Latency target (P95 <100ms?)
  - [ ] Throughput target (1000 req/s?)
  - [ ] Compliance/security (LGPD?)

- [ ] Escalabilidade foi validada
  - [ ] Pode escalar verticalmente (mais CPU/RAM)?
  - [ ] Pode escalar horizontalmente (load balancing)?
  - [ ] Database sharding foi considerado?
  - [ ] Caching strategy é clara?

### Security & Compliance
- [ ] Segurança foi considerada (não é afterthought)
  - [ ] Authentication clara (JWT? OAuth?)
  - [ ] Authorization granular (row-level security?)
  - [ ] Encryption in transit (HTTPS? TLS?)
  - [ ] Encryption at rest (DB credentials, tokens?)

- [ ] LGPD compliance foi verificada
  - [ ] Audit trail: quem acessou quê, quando?
  - [ ] Data isolation: cada athlete só vê seus dados?
  - [ ] Consent logging: usuário consentiu?
  - [ ] Right to be forgotten: pode deletar dados?

### Documentation
- [ ] Diagrama de arquitetura existe
  - [ ] Alto nível (componentes principais)
  - [ ] Fluxos de dados claros (request → API → DB)
  - [ ] Tecnologias explícitas (Node.js, PostgreSQL, Redis)

- [ ] Decisões são rastreáveis
  - [ ] Cada decisão tem um ADR
  - [ ] Links entre ADRs (dependências)
  - [ ] Histórico claro (que versões superaram outras?)

---

## 🟩 PRODUCT — Stephen Strange

### PRD & Requirements
- [ ] PRD está claro e completo
  - [ ] Problem statement: por quê existe esse problema?
  - [ ] Personas identificadas (Maria, treinadora em VO2max)
  - [ ] User stories têm AC específicos (testáveis)
  - [ ] Success metrics definidos (SMART)
  - [ ] Riscos e abertos listados

- [ ] Priorização é clara
  - [ ] Must-have vs. Nice-to-have está explícito
  - [ ] Dependências técnicas são conhecidas
  - [ ] Timeline é realista
  - [ ] Stakeholders foram informados

### User Research & Validation
- [ ] Assumções foram validadas
  - [ ] Entrevistei ≥5 usuários (não adivinhei)
  - [ ] Prototipei antes de dev investir (Figma, Typeform)
  - [ ] Feedback foi incorporado (quais mudanças?)

- [ ] Jobs to Be Done foram identificados
  - [ ] "Treinadora quer prescrever semana em <10 min com zero retrabalho"
  - [ ] Não é "feature frenzy" (features vs. jobs)

### OKRs & Metrics
- [ ] OKRs foram definidos (trimestral)
  - [ ] Objetivo qualitativo (O: "Fácil prescrição")
  - [ ] Key Results quantificáveis (KR1, KR2, KR3)
  - [ ] Cada KR é measurable (analytics disponível?)

- [ ] Métricas de saúde do produto estão claras
  - [ ] North Star identificada (≥80% feedback registration by day 90?)
  - [ ] Leading indicators (prescrição time)
  - [ ] Lagging indicators (retention, NPS)
  - [ ] Cadência de review (semanal, mensal?)

### Roadmap & Go/No-Go
- [ ] Roadmap está planejado
  - [ ] MVP claro (3-4 épicos, não 20)
  - [ ] V1.1 e V1.2 já vislumbrados
  - [ ] Cada epic tem North Star

- [ ] Decisão é clear (Go/No-Go)
  - [ ] Bloqueadores foram identificados (PRD-ESCLARECIMENTOS-BLOQUEADORES.md?)
  - [ ] Go condicional tem ações em semana 0
  - [ ] Stakeholder(s) aprovaram

---

## 🟪 DESIGN — Wanda Maximoff

### Design System
- [ ] Design system foi criado/atualizado
  - [ ] Cores documentadas (primary, secondary, accent, grays)
  - [ ] Tipografia clara (font family, sizes, weights, line-height)
  - [ ] Spacing tokens (8px grid, margin, padding)
  - [ ] Componentes documentados (Button, Input, Card, etc)

- [ ] Componentes são reutilizáveis
  - [ ] Segue Atomic Design (atoms, molecules, organisms)
  - [ ] Variantes claras (primary button, secondary button, danger button)
  - [ ] States documentados (default, hover, active, disabled)

### Wireframes & Prototypes
- [ ] Wireframe/protótipo foi criado
  - [ ] Figma file com estrutura clara (pages, components, variants)
  - [ ] Interações documentadas (click → modal, scroll → tab)
  - [ ] Mobile-first (responsivo em 320px, 768px, 1920px)

- [ ] Múltiplas direções foram exploradas
  - [ ] ≥2 direções de design (exploração, não just 1)
  - [ ] Justificativa para cada direção
  - [ ] Pro/cons documentados

### UX & Usability
- [ ] UX foi testada
  - [ ] Usability test com ≥3 usuários reais
  - [ ] Task: completar ação em <2 min (prescrição de treino)
  - [ ] Feedback coletado (confusão, cliques, etc)
  - [ ] Mudanças implementadas baseado em feedback

- [ ] Accessibility foi considerada
  - [ ] WCAG 2.1 AA standards (color contrast, labels, etc)
  - [ ] Keyboard navigation funciona
  - [ ] Screen reader compatible (ARIA labels)

- [ ] Performance foi validada
  - [ ] Lighthouse score >90 (design assets)
  - [ ] Responsive em todos os breakpoints
  - [ ] Touch targets ≥44x44px (mobile)

### Handoff for Development
- [ ] Specs foram criadas
  - [ ] Componente dimensions (exato pixel spacing)
  - [ ] Typography specs (font, size, weight, line-height)
  - [ ] Color values (RGB, HEX, ou design token)
  - [ ] Behavior (hover, click, animation timing)

- [ ] Assets foram exportados
  - [ ] Icons (SVG, 1x/2x, accessible)
  - [ ] Illustrations (SVG ou high-res PNG)
  - [ ] Mockups (para marketing, PRs, etc)

- [ ] Figma file está organized
  - [ ] Pages clara (Components, Pages, Archive)
  - [ ] Naming convention consistente
  - [ ] Links para PRD/requirements

---

## 🟥 SRE — T'Challa

### Infrastructure & Deployment
- [ ] Infraestrutura foi desenhada
  - [ ] Componentes principais documentados (compute, storage, networking)
  - [ ] Deployment pipeline clara (dev → staging → production)
  - [ ] CI/CD foi configurado (GitHub Actions? GitLab CI?)
  - [ ] Infrastructure as Code (Terraform? CloudFormation?)

- [ ] Zero-downtime deployment foi considerado
  - [ ] Blue-green deployment? Canary release?
  - [ ] Database migrations são backward-compatible?
  - [ ] Rollback strategy é clara?

### Monitoring & Alerting
- [ ] Monitoring foi configurado
  - [ ] Métricas críticas são coletadas (latency, error rate, CPU, memory)
  - [ ] Dashboards existem (health overview)
  - [ ] Alertas estão configurados (P95 latency > 200ms? Error rate > 1%?)
  - [ ] Runbooks documentados (o que fazer quando alerta toca?)

- [ ] Log centralization foi implementado
  - [ ] Logs são estruturados (JSON, não plain text)
  - [ ] Timestamp, level, context em cada log
  - [ ] Busca funciona (find erros em produção?)

### LGPD Compliance
- [ ] Audit logging foi implementado
  - [ ] Quem acessou quê, quando, de onde?
  - [ ] Mudanças em dados sensíveis são registradas
  - [ ] Audit trail é imutável

- [ ] Data isolation foi validada
  - [ ] Cada athlete vê apenas seus dados
  - [ ] Row-level security (RLS) está em lugar
  - [ ] Query filters de tenant_id em TUDO

- [ ] Encryption foi implementado
  - [ ] In transit: HTTPS, TLS 1.2+
  - [ ] At rest: BD credentials, tokens, senhas
  - [ ] Key rotation está automatizado?

### Disaster Recovery
- [ ] Backups foram configurados
  - [ ] Daily backups (automated)
  - [ ] Restoration foi testada (pode recuperar?)
  - [ ] RTO (Recovery Time Objective) é claro (1h? 4h?)
  - [ ] RPO (Recovery Point Objective) é claro (1h de perda de dados?)

- [ ] Failover foi testado
  - [ ] Database replication está ativa
  - [ ] Failover é automático ou manual?
  - [ ] Teste: matar instância, vê se falha?

---

## 🟣 DATA & AI — Visão

### Data Pipeline
- [ ] Data pipeline foi desenhado
  - [ ] Source: de onde vêm os dados? (Garmin, manual input, etc)
  - [ ] Transform: como são processados? (agregação, limpeza, enriquecimento)
  - [ ] Load: onde vão? (warehouse, analytics DB, cache)
  - [ ] Latência esperada: quão fresco são os dados?

- [ ] ETL está implementado
  - [ ] Cada etapa é testada (não quebra silenciosamente)
  - [ ] Data quality checks estão em lugar (null checks, outliers, etc)
  - [ ] Alertas se pipeline falha
  - [ ] Logs/debugging claros (onde falhou?)

### Analytics Database
- [ ] Schema foi desenhado
  - [ ] Tabelas refletem entidades (athletes, workouts, sessions)
  - [ ] Dimensões & facts claros (star schema)
  - [ ] Índices em lugar (não é scan table inteira)
  - [ ] Particionamento se necessário (by date, athlete?)

- [ ] Queries foram otimizadas
  - [ ] Sem N+1 queries
  - [ ] Agregações pré-computadas (onde faz sentido)
  - [ ] View ou materialized view para dashboards frequentes?

### Machine Learning Models
- [ ] Modelo foi definido
  - [ ] Problem: o que estamos predizendo? (sobrecarga? performance?)
  - [ ] Features: que dados usamos? (HR, pace, duration, etc)
  - [ ] Target: o quê predizemos? (continuo ou categórico?)
  - [ ] Success metric: como avaliamos? (accuracy, precision, recall, AUC?)

- [ ] Modelo foi treinado & validado
  - [ ] Train/test split foi feito (não treina em test data)
  - [ ] Cross-validation executada (K-fold? Stratified?)
  - [ ] Baseline foi comparado (modelo melhor que achismo?)
  - [ ] Feature importance foi analisado (que features importam?)

- [ ] Modelo foi prototipado
  - [ ] Código é reproduzível (não no Jupyter só)
  - [ ] Pode ser retreinado facilmente
  - [ ] Hyperparameter tuning foi feito
  - [ ] Documentado: assumptions, limitations, retraining cadence

### Analytics Dashboards
- [ ] Dashboards foram criados
  - [ ] Métrica principal clara (North Star é visível?)
  - [ ] Filtros de athletic (by athlete? by time period?)
  - [ ] Visualizações apropriadas (não bar chart de tudo)
  - [ ] Atualização é automática (não manual refresh)

- [ ] Dashboards contam história
  - [ ] Cada painel tem título claro
  - [ ] Insights são óbvios (não requer interpretação)
  - [ ] Ações são claras ("treinadora vê que atleta está sobrecarregado, prescreve descanso")

---

## 🟠 CROSS-FUNCTIONAL — Todos os Agentes

### Team Collaboration
- [ ] Feedback foi solicitado
  - [ ] Code review pedido (não merged sem aprovação)
  - [ ] Design review com PM/UX (se aplicável)
  - [ ] Tech review com Arquiteto (se crítico)

- [ ] Bloqueadores foram comunicados
  - [ ] Dependência em outro agente? Comunicou?
  - [ ] Risco arquitetural? Escalou para Steve Rogers?
  - [ ] Decisão de produto? Escalou para Stephen Strange?

### Definition of Done (MVP)
- [ ] Tarefa está em "Done" apenas se:
  - ✅ Código/artefato está completo
  - ✅ Passou no checklist relevante (Backend, Design, etc)
  - ✅ Feedback incorporado
  - ✅ Bloqueadores resolvidos
  - ✅ Próximos passos são claros
  - ✅ Documentação existe (README, docs, ADR, PRD, etc)

---

## Como Usar Este Checklist

### Por Agente

**Backend (Tony, Bruce):**
Use seções: UNIVERSAL + BACKEND + CROSS-FUNCTIONAL

**Architecture (Steve):**
Use seções: UNIVERSAL + ARCHITECTURE + CROSS-FUNCTIONAL

**Product (Stephen):**
Use seções: UNIVERSAL + PRODUCT + CROSS-FUNCTIONAL

**Design (Wanda):**
Use seções: UNIVERSAL + DESIGN + CROSS-FUNCTIONAL

**SRE (T'Challa):**
Use seções: UNIVERSAL + SRE + CROSS-FUNCTIONAL

**Data & AI (Visão):**
Use seções: UNIVERSAL + DATA & AI + CROSS-FUNCTIONAL

### Workflow

**Ao finalizar tarefa:**
1. Copie a seção relevante do checklist
2. Execute cada item (check when done)
3. Se algum item é "? unclear", aprofunde
4. Se passa em TODOS os items, marca como Done
5. Se falha em algum, volta pra tarefa (não é done ainda)

### Feedback Loop

**Sprint Retro:**
- Cada agente revisa seu checklist
- "O que foi fácil? Difícil?"
- Atualiza checklist para sprints futuros

---

## Métricas de Sucesso (MVP)

| Métrica | Target | Como Medir |
|---|---|---|
| **Code Quality** | SonarQube ≥85%, Coverage >90% | CI pipeline |
| **Performance** | P95 <100ms em endpoints críticos | APM (Datadog, New Relic) |
| **Reliability** | Zero bugs in production | Bug tracking (Jira, GitHub issues) |
| **Design UX** | Usability test <2 min, NPS >7 | User testing sessions |
| **LGPD Compliance** | 100% audit trail, row-level isolation | Compliance checklist |
| **On-time Delivery** | 95% tasks done on time | Sprint velocity |

---

## Exemplos de "Done" vs. "Not Done"

### ✅ DONE (Tony Stark — API Endpoint)
- [ ] ✅ Endpoint POST /api/v1/athletes/:id/workouts
- [ ] ✅ Unit tests (valid input, invalid input, edge cases) — 100% coverage
- [ ] ✅ Integration test (API + DB + notification)
- [ ] ✅ Error handling (400, 404, 422 com meaningful messages)
- [ ] ✅ DDD applied (Workout entity, PrescribeWorkoutService)
- [ ] ✅ Performance: P95 = 45ms (medido)
- [ ] ✅ Code review aprovado por Steve Rogers
- [ ] ✅ ADR "Multi-tenant data isolation" referenciado
- [ ] ✅ Próximo: Bruce integra com Garmin (Epic A.3)

### ❌ NOT DONE (Tony Stark — API Endpoint)
- ❌ Endpoint funciona "sometimes" (teste local só)
- ❌ Sem unit tests ("vou testar manual")
- ❌ Error handling: "if error, throw" (não é específico)
- ❌ Copy-paste code de outro endpoint (não DDD)
- ❌ Sem medição de performance
- ❌ Sem code review
- ❌ TODO comments por todo lado ("TODO: validar depois")

---

## Última Atualização

**Data:** 02/08/2026  
**Status:** ✅ READY TO USE  
**Próxima revisão:** Após Sprint 1 retro (22/08/2026)  
**Mantido por:** Jarvis, CTO

---

### Anexo: Quick Reference by Role

**Tony Stark (Backend):** UNIVERSAL → BACKEND → CROSS-FUNCTIONAL (15 min)  
**Steve Rogers (Architect):** UNIVERSAL → ARCHITECTURE → CROSS-FUNCTIONAL (20 min)  
**Stephen Strange (PM):** UNIVERSAL → PRODUCT → CROSS-FUNCTIONAL (15 min)  
**Bruce Banner (Backend Python):** UNIVERSAL → BACKEND → CROSS-FUNCTIONAL (15 min)  
**Wanda Maximoff (Designer):** UNIVERSAL → DESIGN → CROSS-FUNCTIONAL (20 min)  
**T'Challa (SRE):** UNIVERSAL → SRE → CROSS-FUNCTIONAL (20 min)  
**Visão (Data & AI):** UNIVERSAL → DATA & AI → CROSS-FUNCTIONAL (20 min)  

---

**Use este checklist toda vez que marcar uma tarefa como DONE.**  
**Se não passa, não é done ainda.**  
**Qualidade sobre velocidade.**
