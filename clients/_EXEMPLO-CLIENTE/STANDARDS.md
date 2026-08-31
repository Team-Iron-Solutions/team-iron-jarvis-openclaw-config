# STANDARDS.md — Acme Corp

> ⚠️ LEITURA OBRIGATÓRIA antes de qualquer tarefa.

---

## Identificação

- **Cliente:** Acme Corporation
- **Projeto:** AcmeApp — app de gestão de pedidos
- **Node OpenClaw:** `node-acme`
- **Repositório:** https://github.com/acme-corp/acme-app
- **Atualizado em:** 2026-08-31
- **Responsável:** Galvão / Team Iron Solutions

---

## Nível de Qualidade

| Critério | Exigência |
|---|---|
| Code review | Obrigatório — todo PR |
| Cobertura de testes | ≥ 75% em lógica de negócio |
| Lint | Zero warnings (flutter analyze) |
| CI/CD | GitHub Actions |
| Branch strategy | Gitflow (main, develop, feature/*, fix/*) |

---

## Idioma & Comunicação

- **Idioma do código:** Inglês (variáveis, funções, comentários, commits)
- **Idioma da documentação interna:** Português
- **Commits:** Conventional Commits em inglês

---

## Regras de Segurança

- Nenhuma chave API hardcoded — usar `flutter_dotenv`
- Todas as chamadas de API validam o token antes de executar
- Dados sensíveis (CPF, cartão) nunca em logs

---

## Convenções de Nomenclatura

```
Widgets:      PascalCase  → ProductCard, CheckoutScreen
Variables:    camelCase   → userName, orderTotal
Files:        snake_case  → product_card.dart, checkout_screen.dart
Constants:    kCamelCase  → kApiBaseUrl, kMaxRetries (Flutter convention)
```

---

## Regras Específicas do Cliente

1. Toda tela nova deve ter sua própria pasta: `lib/features/<feature>/`
2. State management: **Riverpod** — não usar Provider ou Bloc
3. Navegação: **go_router** — não usar Navigator diretamente
4. Imagens: sempre usar `CachedNetworkImage` (nunca `Image.network`)

---

## Checklist do Agente (antes de qualquer entrega)

- [ ] Li STANDARDS.md completo
- [ ] Li TECH-STACK.md (versões corretas)
- [ ] Li CODING-RULES.md
- [ ] Código segue nomenclatura snake_case para arquivos, camelCase para variáveis
- [ ] Usei Riverpod para state, go_router para navegação
- [ ] Zero secrets no código
- [ ] `flutter analyze` sem erros
