# STANDARDS.md — [NOME DO CLIENTE]

> ⚠️ LEITURA OBRIGATÓRIA: Este arquivo define os padrões que DEVEM ser seguidos em todo trabalho para este cliente. Não há exceções.

---

## Identificação

- **Cliente:** [Nome do cliente]
- **Projeto:** [Nome do projeto / app]
- **Node OpenClaw:** [nome do node: ex. `node-cliente-acme`]
- **Repositório:** [URL do repo]
- **Atualizado em:** [YYYY-MM-DD]
- **Responsável:** [Nome do tech lead / contato]

---

## Nível de Qualidade

| Critério | Exigência |
|---|---|
| Code review | [Obrigatório / Opcional] |
| Cobertura de testes | [Ex: ≥ 80%] |
| Lint | [Obrigatório com zero warnings] |
| CI/CD | [GitHub Actions / GitLab CI / etc] |
| Branch strategy | [Gitflow / trunk-based / etc] |

---

## Idioma & Comunicação

- **Idioma do código:** [Ex: inglês — variáveis, funções, comentários]
- **Idioma da documentação:** [Ex: português]
- **Commits:** [Convenção: ex. Conventional Commits em inglês]

---

## Regras de Segurança

- [ ] Nenhuma chave/secret em código — usar variáveis de ambiente
- [ ] Validação de entrada em toda API pública
- [ ] [Outras regras de segurança do cliente]

---

## Convenções de Nomenclatura

```
Variáveis:    [camelCase / snake_case / PascalCase]
Funções:      [camelCase / snake_case]
Classes:      [PascalCase]
Arquivos:     [kebab-case / camelCase / PascalCase]
Constantes:   [UPPER_SNAKE_CASE]
```

---

## Estrutura de Commits

```
[tipo](escopo): descrição curta

Tipos: feat, fix, docs, style, refactor, test, chore
Exemplos:
  feat(auth): add JWT refresh token
  fix(api): correct pagination offset
  test(user): add unit tests for user service
```

---

## Regras Específicas do Cliente

> Adicione aqui qualquer regra que não se encaixa nas categorias acima.

1. [Regra 1]
2. [Regra 2]
3. [Regra 3]

---

## Checklist do Agente (antes de qualquer entrega)

- [ ] Li e entendi este STANDARDS.md completo
- [ ] Li TECH-STACK.md (versões e libs corretas)
- [ ] Li CODING-RULES.md (regras obrigatórias)
- [ ] Código segue nomenclatura definida
- [ ] Zero secrets/tokens no código
- [ ] Testes incluídos (quando aplicável)
- [ ] Commits seguem convenção
