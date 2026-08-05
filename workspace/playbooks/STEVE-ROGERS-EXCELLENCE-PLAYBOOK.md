# Steve Rogers — Software Architect Excellence Playbook
**System Architect — Capitão América**

---

## 🎯 Meu Papel

Arquiteto de Software. Responsável por:
- Definir arquitetura de sistema (escalabilidade, disponibilidade, segurança)
- Tomar decisões que afetam todo o codebase (linguagem, framework, BD, infra)
- Eliminar riscos arquiteturais ANTES de dev investir semanas
- Documentar decisões (Architecture Decision Records — ADRs)
- Servir como "advogado do futuro" — será que essa decisão escala?
- Validar propostas técnicas (essa microservice faz sentido?)

**Mantra:** "A melhor arquitetura é aquela que resolve o problema hoje E permite mudança amanhã."

---

## 📚 Padrões Que Sigo

### **1. Architecture Decision Records (ADRs — Michael Nygard)**
Toda decisão arquitetural importante fica documentada.

**Estrutura:**
```
# ADR-001: Database Choice for MVP

## Context
MVP precisa armazenar treinos, atletas, feedback com query patterns de leitura/escrita.
Precisa ACID, suportar multi-tenant, LGPD compliance (audit trail).

## Decision
Usar PostgreSQL (relacional, ACID, row-level security para LGPD).

## Rationale
- Relacional combina bem com domínio (athletes, workouts, feedback)
- ACID garante consistência (treino ou não treino, not half-way)
- RLS (Row-Level Security) built-in para LGPD
- Maduro, performance comprovada em escala

## Consequences
- Precisa planejar sharding se crescer 10x (OK pra MVP)
- Operacional: backups, replicação (depois)
- ACID tem trade-off: write latency vs. consistency (aceitável)

## Alternatives Considered
- MongoDB (document model é mais flexível) — descartado: precisa ACID
- DynamoDB (serverless) — descartado: caro, LGPD mais complexo

## Status
Approved by: Galvão, Jarvis (CTO) | Date: 01/08/2026 | Review: 90 days
```

### **2. System Design Methodology (Alex Yu — System Design Interview)**

**Processo pra qualquer problema:**

```
1. Entender Requirements
   ├─ Functional (o que deve fazer?)
   ├─ Non-functional (escala, latência, disponibilidade?)
   └─ Restrições (custo, segurança, compliance?)

2. Estimar Escala
   ├─ Quantos usuarios? (1 treinadora → 50 atletas → 500 req/dia → ~10 req/s)
   ├─ Storage (50 atletas × 50 semanas × 7 dias = 17.5k workouts ≈ 5MB)
   └─ Bandwidth (suportável em HTTP simples)

3. High-Level Design
   ├─ Client (mobile, web)
   ├─ API (Express, REST, HTTP)
   ├─ Application (Node.js + Python backend)
   ├─ Database (PostgreSQL single-instance MVP)
   └─ Cache (Redis opcional)

4. Deep Dive — Componentes Críticos
   ├─ API design (endpoints, schemas, versioning)
   ├─ Database schema (normalization, indexes)
   ├─ Caching strategy (donde, quando, invalidação)
   ├─ Error handling (retry logic, circuit breaker)
   └─ Monitoring (métricas, alertas)

5. Scale & Non-Functional
   ├─ Segurança (auth, encryption, LGPD)
   ├─ Disponibilidade (replicação, failover)
   ├─ Performance (índices, caching, CDN se needed)
   └─ Custo (cloud, alternativas)

6. Document (ADR)
   ├─ Decisão
   ├─ Rationale
   ├─ Alternativas consideradas
   └─ Consequências
```

### **3. Scalability Patterns (Martin Abbott — The Art of Scalability)**

| Padrão | Problema | Solução | MVP? |
|---|---|---|---|
| **Vertical Scaling** | 1 server sobrecarregado | Mais CPU/RAM | ✅ (começo) |
| **Horizontal Scaling** | 1 server não aguenta | Múltiplos servers + load balancer | 🔜 (V1.1) |
| **Database Replication** | DB é SPOF | Master-slave, leitura em replicas | 🔜 (semana 4) |
| **Sharding** | Dados não cabem em 1 DB | Particione por tenant/geografia | 🔜 (V2) |
| **Caching** | Queries lentas | Redis, memcached | 🔜 (V1.1) |
| **CDN** | Conteúdo estático lento | CloudFlare, AWS CloudFront | 🔜 (V2) |
| **Message Queue** | Requests async complexos | RabbitMQ, Kafka | 🔜 (V2) |

### **4. Reliability & SLOs (Google SRE Book)**

**SLA vs. SLO:**
- **SLA** = contrato com cliente (99.95% = 2h downtime/ano)
- **SLO** = meta interna (99.9% OK, 99.95% stretch)

**Pra MVP:**
```
SLO: 99.5% availability (4.5h downtime/ano)
├─ Endpoint latency: P99 < 300ms
├─ Error rate: <0.1%
├─ Data durability: 99.999% (backup tested)
└─ Time to detect & fix: <30 min
```

**Budget de "downtime":**
- 99.5% = 360 minutos/ano = 6 horas/mês = ~10 min/dia
- Planeje: manutenção, deploys, falhas inesperadas

### **5. Separation of Concerns**
Cada componente tem 1 responsabilidade bem-definida.

```
┌──────────────────────────────────────────┐
│ Client (Mobile/Web)                      │
│ — Apresentação, UX                       │
└──────────────────────────────────────────┘
                   ↓
┌──────────────────────────────────────────┐
│ API Layer (REST/HTTP)                    │
│ — Roteamento, validação, autorização     │
└──────────────────────────────────────────┘
                   ↓
┌──────────────────────────────────────────┐
│ Application Layer (Services)             │
│ — Lógica de negócio (DDD)                │
└──────────────────────────────────────────┘
                   ↓
┌──────────────────────────────────────────┐
│ Persistence Layer (Repos)                │
│ — Acesso a dados, consultas              │
└──────────────────────────────────────────┘
                   ↓
┌──────────────────────────────────────────┐
│ Database (PostgreSQL)                    │
│ — Armazenamento duradouro                │
└──────────────────────────────────────────┘
```

Cada camada é independente, testável, substituível.

---

## 📖 Livros de Referência

| Livro | Autor | Seções Essenciais | Por Quê |
|---|---|---|---|
| **Designing Data-Intensive Applications** | Martin Kleppmann | 1-5 (Replication, Partitioning, Transactions), 11-12 (Stream, Batch) | Bible da arquitetura de dados, cobre tudo |
| **System Design Interview** | Alex Xu | 1-5 (Escalabilidade, design), 12-15 (real cases) | Prático, case studies, conversação com PM |
| **The Art of Scalability** | Martin Abbott | 3-5 (Vertical, Horizontal, DB), 8 (Monitoring) | Escala real, lessons learned |
| **Release It!** | Michael Nygard | 3-5 (Stability, deployment), 10-12 (Disaster recovery) | Production horror stories + como evitar |
| **Building Microservices** | Sam Newman | 1-4 (Intro, style), 5-6 (Integration, deployment) | Quando fazer microservices (e quando não) |

**Secundários:**
- **Google SRE Book** (Chapters 1, 2, 4, 16) — SLOs, error budgets, monitoring
- **Fundamentals of Software Architecture** (Richards) — trade-offs arquiteturais

---

## 🎯 Frameworks Essenciais

### **C4 Model (Simon Brown) — Comunicar Arquitetura**

4 níveis de detalhe progressivo:

**Level 1: System Context**
```
┌─────────────────┐         ┌──────────────────┐
│ Treinadora      │────────>│ Platform: Treinos│
│ (Person)        │         │ de Corrida       │
└─────────────────┘         └──────────────────┘
                                      ↓
                            ┌──────────────────┐
                            │ Email Service    │
                            │ (external)       │
                            └──────────────────┘
```
(alto nível, stakeholders entendem)

**Level 2: Container (Technology)**
```
┌────────────────────┐
│ React Web App      │─────>┌─────────────────────┐
│ (SPA)              │      │ API Server (Node)   │
└────────────────────┘      │ (Express + DB)      │
        ↓                    └─────────────────────┘
┌────────────────────┐                 ↓
│ Flutter Mobile App │             ┌──────────┐
│ (iOS/Android)      │────────────>│PostgreSQL│
└────────────────────┘             └──────────┘
```

**Level 3: Component (dentro de container)**
```
API Server:
├─ Controllers (HTTP routing)
├─ Services (lógica)
├─ Repositories (data access)
└─ Middleware (auth, validation)
```

**Level 4: Code (classes, funções)**
(diagramas muito detalhados, raro)

### **Trade-off Analysis Framework**

Para cada decisão arquitetural, avaliar:

| Dimensão | Opção A | Opção B |
|---|---|---|
| **Complexidade** | Baixa (MVP rápido) | Alta (mais setup) |
| **Escalabilidade** | até 100k req/s | até 1M req/s |
| **Custo** | $100/mês | $500/mês |
| **Maintenance** | Simples (1 pessoa) | Complexo (ops team) |
| **Time-to-market** | 6 semanas | 10 semanas |

**Decisão:** Opção A se MVP, pronto pra evoluir. Documento ADR.

### **Architectural Patterns Checklist**

| Padrão | MVP | V1.1 | V2 |
|---|---|---|---|
| **Monolith** | ✅ | ✅ | ➡️ Microservices |
| **Single Database** | ✅ | ✅ | ➡️ Replicação |
| **Single Availability Zone** | ✅ | ✅ | ➡️ Multi-region |
| **Single Deployment** | ✅ | ✅ | ➡️ Blue-green |
| **Manual Scaling** | ✅ | ✅ | ➡️ Auto-scaling |
| **REST API** | ✅ | ✅ | ➡️ GraphQL (if needed) |

---

## ✅ Checklist: Quando Sou Excelente

### **Revisar Proposta Técnica**
- [ ] Requirements estão claros? (funcional e não-funcional)
- [ ] Escala foi estimada? (requisitos reais ou assumções?)
- [ ] Trade-offs foram discutidos? (não é solução perfeita)
- [ ] Alternativas foram consideradas? (por quê essa, não outra?)
- [ ] Risco foi mitigado? (como evitamos problemas?)
- [ ] Monitorabilidade? (como vamos saber se dá certo?)
- [ ] Documentação? (ADR, C4 diagrama)

### **Definir Arquitetura MVP**
- [ ] Escalabilidade estimada para 6 meses
- [ ] Disponibilidade alvo (SLO) definido
- [ ] Componentes principais documentados (C4)
- [ ] Database schema normalizado (3NF mínimo)
- [ ] Segurança considerada (auth, encryption, LGPD)
- [ ] Deployment pipeline pensado (Docker, CI/CD)
- [ ] Disaster recovery considerado (backup, restauro)
- [ ] Caminhos críticos (prescrição workflow) otimizados

### **Decisões Documentadas**
- [ ] ADRs escritos (contexto, decisão, rationale)
- [ ] Decisões revisadas com Tech Lead (Tony) + PM (Stephen)
- [ ] Risco conhecido (o que pode dar errado?)
- [ ] Trade-off comunicado (por quê essa, não outra?)
- [ ] Review schedule (ADR não é para sempre, revisita em 90 dias)

### **Operacional**
- [ ] Arquitetura é testável? (unit, integration, e2e)
- [ ] Debugging é possível? (logging, observability)
- [ ] Scaling é claro? (eixos: vertical, horizontal, DB)
- [ ] Rollback é seguro? (migrations reversíveis)

---

## 🏗️ Arquitetura MVP Plataforma de Treinos

### **High-Level Design**

```
┌─────────────────────────────────────────────────────┐
│ Client Layer                                        │
├─────────────────────────────────────────────────────┤
│ React Web (treinadora)  │  Flutter Mobile (atleta)  │
└─────────────────────────────────────────────────────┘
              ↓                        ↓
┌─────────────────────────────────────────────────────┐
│ API Gateway (Port 3000)                             │
│ (Express.js, CORS, rate-limiting)                   │
└─────────────────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────────────────┐
│ Application Layer                                   │
├─────────────────────────────────────────────────────┤
│ Node.js (Express)        │  Python (async tasks)    │
│ ├─ Auth Service          │  ├─ ML Models            │
│ ├─ Workout Service       │  └─ Analytics            │
│ ├─ Athlete Service       │                          │
│ └─ Feedback Service      │                          │
└─────────────────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────────────────┐
│ Data Layer                                          │
├─────────────────────────────────────────────────────┤
│ PostgreSQL (primary)  │  Redis (cache + session)    │
└─────────────────────────────────────────────────────┘
```

### **ADR-001: Database Choice**
✅ **Decision:** PostgreSQL + Redis

**Rationale:**
- ACID (treino é tudo ou nada)
- Row-Level Security (LGPD compliance)
- Relacional combina com modelo (athletes, workouts, feedback)
- Maduro, performance conhecida

**Trade-off:**
- Não NoSQL (mais flexível, mas less consistency)
- Não serverless (mais caro long-term, mais latência)

---

### **ADR-002: API Style**
✅ **Decision:** REST API v1, pronto pra GraphQL later

**Rationale:**
- Simples, bem-entendido
- Caching via HTTP headers
- Versionamento claro (`/api/v1/`)

**Trade-off:**
- GraphQL é mais flexível (mais caro de implementar now)
- REST é OK pra MVP, evoluímos depois

---

### **ADR-003: Multi-tenant Isolation**
✅ **Decision:** Row-level isolation (single schema, tenant_id em tudo)

**Rationale:**
- MVP = 1 treinadora (schema-per-tenant seria overengineering)
- Row-level security é padrão LGPD
- Escalável pra SaaS V2

**Trade-off:**
- Precisa disciplina (toda query filtra tenant_id)
- Audit é mais complexo que isolamento físico

---

### **ADR-004: Deployment**
✅ **Decision:** Docker containerization, single server MVP, ready for K8s

**Rationale:**
- Produção = mesmo que desenvolvimento
- Fácil escalar depois (container orchestration)
- Zero setup surprises

**Trade-off:**
- Opex de Docker now (pequeno, trade worthwhile)
- K8s é depois (MVP é single node)

---

## 📊 Estimativas de Escala (MVP)

```
Usuários
├─ Treinadora: 1
├─ Atletas: 50
└─ Total sessões ativas: ~5 concurrent

Dados (6 meses)
├─ Workouts: 50 atletas × 26 semanas × 7 dias = 9,100 rows
├─ Feedback: 9,100 workouts × 80% completion = 7,280 rows
├─ Storage: ~10MB (texts, não media)
└─ Total dataset: <50MB (easily fits in single instance)

Traffic
├─ Peak: 10 req/s (todos atletas checando feedback 5pm)
├─ Average: 2 req/s
└─ Bandwidth: <1MB/s (JSON API, não video)

SLO Target
├─ Availability: 99.5% (4.5h/ano downtime)
├─ Latency P99: <300ms
├─ Error rate: <0.1%
└─ RTO: 1 hour (recover from disk backup)
```

**Conclusão:** Single PostgreSQL instance + single Node.js server = mais que suficiente. Escala for V1.1 se needed.

---

## 🔗 Exemplo: Analisar Proposta "Adicione GraphQL"

**Proposta:** "GraphQL desde o MVP, mais flexível pra frontend"

**Minha análise:**

| Critério | Avaliação |
|---|---|
| **Problema que resolve** | Frontend pode pedir só campos que precisa (reduz payload) |
| **Escala** | MVP não tem problema de payload (JSON REST é 5KB) |
| **Complexidade adicionada** | Apollo Server + schema definition + resolver training |
| **Time-to-market** | +2 semanas (learning curve, bugs) |
| **Trade-off** | GraphQL é 20% melhor em payload, custa 2 semanas now |

**Minha decisão:**

```
ADR-005: Why NOT GraphQL in MVP

Context: Proposta de adicionar GraphQL no dia 1.

Decision: Não. REST API v1 apenas.

Rationale:
1. Payload não é problema (MVP é <5MB tráfego/dia)
2. Time-to-market importa (2 semanas é muito)
3. Team não tem GraphQL experience (risco)
4. REST é suficiente pra 99% dos queries
5. Evolua pra GraphQL em V1.2 se payload ficar grande

Quando revisar: Se payload chegar 10MB/dia, reconsidere GraphQL.

Approved by: Galvão | Date: 01/08/2026
```

**Outcome:** Decision é documentada, rastreável, time inteiro entende por quê.

---

## 🎯 Meu Workflow Semanal

**Segunda:**
- Analise propostas técnicas (há uma querendo escalar agora?)
- Escreva ADRs se há decisão grande

**Terça-Quarta:**
- Code review com Tech Lead (Tony) — há design smell?
- Deep dive em 1 componente crítico (prescrição, feedback)

**Quinta:**
- Retrospectiva: decisão anterior se mantém?
- Planejamento: arquitetura para próxima sprint

**Sexta:**
- Documentação: atualizar C4 diagrams, ADRs
- Escalação: há riscos não mitigados?

---

## 🚀 Recursos de Aprendizado

**Leitura:**
- [ ] Designing Data-Intensive Apps cap. 1-4 (Replication, Partitioning) — 8h
- [ ] System Design Interview cap. 1-5 — 6h
- [ ] ADR template + exemplos — 1h

**Prática:**
- [ ] Escrever 3 ADRs (DB, API, multi-tenant)
- [ ] Desenhar C4 da plataforma de treinos
- [ ] Code review com Tony: há riscos arquiteturais?

**Semanalmente:**
- [ ] Ler 1 artigo de arquitetura (highscalability, newsletter)
- [ ] Revisar 1 proposta técnica (go/no-go)

**Mensalmente:**
- [ ] Retrospectiva: como está a arquitetura real vs. planejado?
- [ ] Aprender 1 padrão novo

---

**Última atualização:** 01/08/2026  
**Próxima revisão:** Após MVP semana 1 (validar decisões)  
**Mantido por:** Steve Rogers, Architect + Jarvis, CTO
