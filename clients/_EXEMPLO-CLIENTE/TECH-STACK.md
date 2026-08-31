# TECH-STACK.md — Acme Corp

---

## Mobile (Flutter)

| Tecnologia | Versão | Notas |
|---|---|---|
| Flutter | 3.24.x | SDK principal |
| Dart | 3.5.x | |
| flutter_riverpod | 2.5.x | State management |
| go_router | 14.x | Navegação |
| dio | 5.x | HTTP client |
| cached_network_image | 3.x | Imagens remotas |
| flutter_dotenv | 5.x | Env variables |
| hive | 2.x | Local storage |
| freezed | 2.x | Imutabilidade |
| json_serializable | 4.x | JSON parsing |

## Backend (API)

| Tecnologia | Versão | Notas |
|---|---|---|
| Node.js | 20.x LTS | Runtime |
| Express | 4.x | Framework HTTP |
| PostgreSQL | 16.x | Banco principal |
| Redis | 7.x | Cache e sessões |
| Prisma | 5.x | ORM |
| JWT | — | Autenticação |

## Infraestrutura

| Serviço | Uso |
|---|---|
| AWS (ECS Fargate) | Backend em produção |
| RDS (PostgreSQL) | Banco em produção |
| ElastiCache | Redis em produção |
| GitHub Actions | CI/CD |
| Docker | Containerização |

## Ambientes

| Ambiente | URL |
|---|---|
| Dev | http://localhost:3000 |
| Staging | https://api-staging.acme-app.com |
| Production | https://api.acme-app.com |

## Gerenciador de pacotes

- Flutter: `pub` (pubspec.yaml — sempre commitar pubspec.lock)
- Backend: `npm` (package-lock.json — sempre commitar)
