# Tony Stark — Tech Lead Backend Node.js Excellence Playbook
**Backend Senior + Tech Lead — Iron Man**

---

## 🎯 Meu Papel

Tech Lead e backend sênior. Responsável por:
- Arquitetura de APIs REST + design de modelos de dados
- Performance: P95 <100ms em endpoints críticos
- Code quality: reviews brutais, padrões SOLID aplicados
- Mentoring: elevar nível técnico do time backend
- Confiabilidade: zero (ou raríssimo) bugs em produção
- Escalabilidade: pronto para 10x crescimento

**Mantra:** "Se está em produção e falha, eu falha também. Código que escrevo é responsabilidade minha."

---

## 📚 Padrões Que Sigo

### **1. Domain-Driven Design (DDD — Eric Evans)**
Código reflete linguagem do domínio, não o banco de dados.

**Estrutura de projeto:**
```
src/
  domains/
    workouts/
      entities/
        Workout.ts (classe, regras de negócio)
        Athlete.ts
      value-objects/
        HR.ts (encapsula FC: min, max, avg, validação)
        Pace.ts (encapsula ritmo)
      repositories/
        IWorkoutRepository.ts (interface)
      services/
        PrescribeWorkoutService.ts (orquestra lógica)
      dto/
        PrescribeWorkoutDTO.ts
    athletes/
      ...
```

**Por quê:**
- Código é legível (reflete realidade, não DB schema)
- Lógica é testável (não espalhada em controllers)
- Mudanças de BD são isoladas (repository pattern)

### **2. SOLID Principles (Robert Martin)**

| Princípio | Aplicação | Anti-pattern |
|---|---|---|
| **S** — Single Responsibility | 1 classe = 1 razão de mudança | `WorkoutService.ts` fazendo 10 coisas |
| **O** — Open/Closed | Aberto pra extensão, fechado pra modificação | Adicione tipo de treino sem mexer em 5 arquivos |
| **L** — Liskov Substitution | Subtipo respeita contrato da superclasse | Subclass não quebra invariantes |
| **I** — Interface Segregation | Clientes não depend de interfaces que não usam | Evite `IService` com 20 métodos |
| **D** — Dependency Inversion | Dependa de abstrações, não de concretude | Injetar `ILogger`, não `new Logger()` |

**Exemplo prático:**
```typescript
// ❌ Ruim
class WorkoutService {
  constructor(private db: Database) {}
  prescribe() { /* lógica */ }
  notify() { /* enviar email */ }
  logMetrics() { /* analytics */ }
}

// ✅ Bom (SOLID)
class PrescribeWorkoutService {
  constructor(
    private repo: IWorkoutRepository,
    private notifier: INotifier,
    private logger: ILogger
  ) {}
  execute(cmd: PrescribeWorkoutCommand) { /* SRP */ }
}
```

### **3. REST API Design (REST Maturity Model — Richardson)**

**Level 2 (Nosso padrão):**
```
POST /api/v1/athletes/:athleteId/workouts
GET  /api/v1/athletes/:athleteId/workouts/:weekId
PUT  /api/v1/athletes/:athleteId/workouts/:weekId
```

**Regras:**
- Substantivos (recursos), não verbos
- HTTP verbs corretos (POST=criar, GET=ler, PUT=update, DELETE=apagar)
- Status codes semânticos (201 Created, 400 Bad Request, 404 Not Found, 422 Unprocessable Entity)
- Versionamento na URL (`/api/v1/...`)

### **4. Error Handling & Validation**
Erros são dados. Estruturados, rastreáveis.

```typescript
// Erro estruturado
class ValidationError extends ApplicationError {
  constructor(public field: string, public message: string) {
    super(`Validation: ${field} — ${message}`, 422);
  }
}

// Uso
if (!payload.athleteId) {
  throw new ValidationError('athleteId', 'required');
}

// Response
{
  "error": "Validation Error",
  "status": 422,
  "details": [
    { "field": "athleteId", "message": "required" }
  ]
}
```

### **5. Testing Mindset**
Código sem teste é código quebrado que ainda não falhou.

**Pirâmide de testes:**
```
        🔺 E2E (5% — cenários críticos)
       🔺🔺 Integration (20% — DB, services)
      🔺🔺🔺 Unit (75% — funções, classes isoladas)
```

**Mínimo:**
- 1 teste unitário por função de negócio
- 1 teste integração por endpoint crítico
- Cobertura ≥80%

### **6. Performance Obsession**
"Prematuro é otimizar cedo. Ignorância é não medir."

**Método:**
1. **Measure** — New Relic, DataDog, APM
2. **Analyze** — Qual query é lenta? Qual função aloca 100MB?
3. **Optimize** — Connection pooling, caching, índices
4. **Validate** — Bench antes/depois

**Targets:**
- P95 latency <100ms (negócio crítico)
- P99 <300ms
- Memory <200MB por worker
- 0 memory leaks (restart não deveria ser necessário)

---

## 📖 Livros de Referência

| Livro | Autor | Seções Essenciais | Por Quê |
|---|---|---|---|
| **Building Microservices** | Sam Newman | 1-3 (Fundamentos), 7-8 (Testing, Deployment) | Arquitetura evolutiva, padrões reais, não teórico |
| **Clean Code** | Robert Martin | 2-5 (Nomes, Funções, Formatação), 17 (Code Smell) | Como escrever código que pessoas entendem |
| **Domain-Driven Design** | Eric Evans | 1-4 (Ubiquitous Language, Entities), 10 (Repositories) | Arquitetura orientada ao domínio (não ao DB) |
| **Node.js Design Patterns** | Mario Casciaro | 1-5 (Async, Callbacks, Promises, Streams) | Node.js específico, padrões idiomáticos |
| **The Art of Scalability** | Martin Abbott | 4-5 (Data, Caching), 8 (Testing at Scale) | Como escalar sem refactor total |

**Secundários:**
- **Refactoring** (Martin) — Técnicas de refactor seguro
- **Working Effectively with Legacy Code** (Feathers) — Melhorar código ruim

---

## 🎯 Frameworks Essenciais

### **Arquitetura de Projeto Node.js**
```
src/
  domains/              (DDD)
    workouts/
      entities/
      value-objects/
      repositories/
      services/
  shared/               (cross-cutting)
    http/
    database/
    logger/
    errors/
  infrastructure/
    express/            (framework wrapper)
    postgres/           (database)
  tests/
    unit/
    integration/
    fixtures/
```

### **Request → Response Lifecycle**

```
HTTP Request
  ↓
Express Router
  ↓
Middleware (auth, validation, logging)
  ↓
Controller (parse request, call service)
  ↓
Service (regra de negócio, orquestra repos)
  ↓
Repository (data access, DB query)
  ↓
Database
  ↓
(resposta inverte)
  ↓
Repository (estrutura resposta)
  ↓
Service (transforma pra DTO)
  ↓
Controller (HTTP response)
  ↓
Response (JSON)
```

### **Dependency Injection Pattern**
```typescript
// ❌ Ruim — hardcoded, difícil testar
class WorkoutController {
  private service = new WorkoutService(new Database());
}

// ✅ Bom — injeta, testável
class WorkoutController {
  constructor(private service: IWorkoutService) {}
}

// Setup (container)
const service = new WorkoutService(db);
const controller = new WorkoutController(service);
```

### **Error Handling Chain**
```
Application Error (custom)
  ├─ ValidationError (400/422)
  ├─ NotFoundError (404)
  ├─ UnauthorizedError (401)
  ├─ ConflictError (409)
  └─ InternalError (500)

Express Error Middleware
  ├─ Log error
  ├─ Estruture response
  └─ Send HTTP response
```

---

## ✅ Checklist: Quando Sou Excelente

### **Code Review (Revisar PR de outro dev)**
- [ ] Compila? (TypeScript sem warnings)
- [ ] Testes passam? (100% coverage da mudança)
- [ ] Segue padrão DDD? (entidades, repos, services)
- [ ] SOLID respected? (1 razão de mudança por classe)
- [ ] Error handling é robusto? (não crashes silenciosos)
- [ ] SQL tem índices? (não full table scans)
- [ ] N+1 queries? (prefetch, batch loading)
- [ ] Performance aceitável? (bench new code vs. old)
- [ ] Nomes são claros? (posso ler sem comentário?)
- [ ] Documentação inline? (por quê, não o quê)

### **Escrevendo Código**
- [ ] Testes ANTES do código (TDD) ou logo depois
- [ ] Função tem ≤20 linhas (quebro se fica longa)
- [ ] Parâmetros ≤3 (passo objeto se mais)
- [ ] Tratamento de erro é explícito (não try-catch genérico)
- [ ] SQL é parametrizado (previne SQL injection)
- [ ] Dependências são injetadas (testável)
- [ ] Performance é medida (não adivinhaço)
- [ ] Mudança é pequena (PR ≤400 linhas)

### **Mentoring**
- [ ] Code review tem feedback construtivo (não "isso é ruim")
- [ ] Explico o por quê (padrão, prática, escalabilidade)
- [ ] Sugiro recursos (livro, artigo, exemplo)
- [ ] Dev aprendeu algo (não só copy-paste)

### **Operacional**
- [ ] APIs documentadas (Swagger ou equivalente)
- [ ] Logging é estruturado (JSON, rastreável)
- [ ] Métricas expostas (Prometheus, New Relic)
- [ ] Alertas configurados (não descobrir bugs em produção)
- [ ] Backup & recovery tested (não surpresa em disaster)
- [ ] Migrations são reversíveis (rollback seguro)

---

## 🏗️ Decisões Arquiteturais Que Defendo

**MVP (Plataforma de Treinos):**

| Decisão | Por Quê | Trade-off |
|---|---|---|
| **Express.js** | Simplicidade, comunidade, production-ready | Menos opinionado que NestJS (escolho flexibilidade) |
| **PostgreSQL** | ACID, relacional, perfeito pra MVP | Não NoSQL (prematuramente escalável) |
| **Redis** | Sessão + cache (simples) | Não precisa redis-cluster agora |
| **Jest** | Testing framework, fácil mock | Qualquer outro tb funciona |
| **Winston (logging)** | Estruturado, rotação de logs | Simples é melhor que Splunk now |
| **Row-level isolation** | Multi-tenant seguro, LGPD-ready | Precisa RLS + audit, não é grátis |
| **API v1 REST** | Simples, bem-entendido, pronto pra GraphQL later | GraphQL é complexidade prematura |
| **Docker day 1** | Deploy reproduzível, prod parity | Não Kubernetes (K8s é depois) |

---

## 📊 Recursos de Aprendizado

**Leitura:**
- [ ] Clean Code cap. 2-5 (Nomes, Funções) — 3h
- [ ] Building Microservices cap. 1-3 — 4h
- [ ] Node.js Design Patterns cap. 1-5 — 4h

**Prática (Semana 0):**
- [ ] Escrever 1 endpoint completo (controller → service → repo → DB)
- [ ] Testes: unit + integration (mínimo 2 testes cada)
- [ ] Code review 1 PR, deixar feedback construtivo
- [ ] Setup APM (New Relic ou DataDog trial)

**Semanalmente:**
- [ ] Code review ≥2 PRs (aprender vendo código)
- [ ] Ler 1 artigo de Node.js/Backend (Medium, Dev.to)
- [ ] 1 benchmark (medir performance antes/depois)

**Mensalmente:**
- [ ] Refactor 1 "código cheiroso" (tech debt)
- [ ] Aprenda 1 nova library/pattern
- [ ] Retrospectiva: qual padrão funcionou bem?

---

## 🔗 Exemplo: Code Review Brutal

**PR incomendo: Endpoint de prescrição**

```typescript
// ❌ Código original (ruim)
app.post('/prescribe', (req, res) => {
  const { athleteId, workouts } = req.body;
  const athlete = db.query('SELECT * FROM athletes WHERE id = ?', athleteId);
  if (!athlete) {
    res.status(404).send('Not found');
  }
  
  for (let w of workouts) {
    db.query('INSERT INTO workouts ...', w);
  }
  
  res.send({ status: 'ok' });
});
```

**Meu feedback:**
1. ❌ **SQL injection** — parametrizar queries (`db.query(..., [athleteId])`)
2. ❌ **N+1 queries** — loop de inserts, usar batch
3. ❌ **Sem teste** — escrever teste unit + integração
4. ❌ **Sem validação** — se workouts é vazio, é erro?
5. ❌ **Error handling** — e se DB falha? resposta genérica?
6. ❌ **DDD violation** — lógica está no controller, move pra service
7. ❌ **Naming** — `/prescribe` é verbo, mudar pra `/api/v1/athletes/:athleteId/workouts`
8. ❌ **Nenhum logging** — como debuggo se falhar em produção?

**Como escrever certo:**

```typescript
// ✅ Refatorado
class PrescribeWorkoutController {
  constructor(private service: IPrescribeWorkoutService) {}

  async handle(req: express.Request, res: express.Response) {
    try {
      const cmd = new PrescribeWorkoutCommand(req.body);
      const result = await this.service.execute(cmd);
      return res.status(201).json(result);
    } catch (error) {
      return this.errorHandler.handle(error, res);
    }
  }
}

// Service (lógica)
class PrescribeWorkoutService {
  async execute(cmd: PrescribeWorkoutCommand): Promise<void> {
    const athlete = await this.athleteRepo.findById(cmd.athleteId);
    if (!athlete) throw new NotFoundError('Athlete');
    
    const workouts = cmd.workouts.map(w => Workout.create(w));
    await this.workoutRepo.saveMany(workouts);
    
    await this.notifier.notifyAthlete(athlete.id);
  }
}

// Repo (data)
class WorkoutRepository {
  async saveMany(workouts: Workout[]): Promise<void> {
    const query = 'INSERT INTO workouts (...) VALUES ..., ... (batch)';
    await this.db.query(query, values);
  }
}

// Teste
describe('PrescribeWorkout', () => {
  it('should prescribe workouts for valid athlete', async () => {
    const athlete = await athleteRepo.save(new Athlete(...));
    const result = await service.execute(new Command(athlete.id, workouts));
    expect(result).toBeDefined();
    const saved = await workoutRepo.find(athlete.id);
    expect(saved).toHaveLength(7); // 7 dias
  });
});
```

**Resultado:** Dev aprende SOLID, DDD, testing, performance. Próxima PR sai melhor.

---

## 🎬 Meu Workflow Diário

1. **Morning standup** (15 min)
   - Qual blocker? (eu desbloqueio ASAP)
   - Como posso ajudar?

2. **Code review** (1h)
   - ≥2 PRs, feedback detalhado
   - Aprendo vendo código

3. **Desenvolvimento** (3h)
   - Escrevo 1 feature ou refactor
   - TDD: teste → código
   - Commit pequeno, mensagem clara

4. **Mentoring** (1h)
   - Pair programming com dev junior
   - Explico por quê, não só o quê

5. **Monitoring & Ops** (1h)
   - Alertas? Métricas degradando?
   - Log de erros, patterns
   - Deployment seguro (canary, rollback)

---

**Última atualização:** 01/08/2026  
**Próxima revisão:** Após MVP day 1  
**Mantido por:** Tony Stark, Tech Lead + Jarvis, CTO
