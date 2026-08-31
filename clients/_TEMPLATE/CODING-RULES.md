# CODING-RULES.md — [NOME DO CLIENTE]

> Regras de codificação obrigatórias. Estas regras são NON-NEGOTIABLE.
> Qualquer entrega que viole estas regras deve ser rejeitada e refeita.

---

## Regras Gerais

### 🔴 PROIBIDO (breaking rules — bloqueia merge)
- [ ] Nenhum `console.log` / `print` em produção sem logging estruturado
- [ ] Nenhum código comentado deixado para trás
- [ ] Nenhuma credencial, token ou senha hardcoded
- [ ] Nenhum `TODO` sem issue linkada
- [ ] [Regra específica do cliente]

### 🟡 OBRIGATÓRIO (quality rules — causa reprovação em review)
- [ ] Funções com mais de 30 linhas precisam de justificativa
- [ ] Variáveis com nomes descritivos (sem `x`, `tmp`, `data` genérico)
- [ ] Tratamento de erros em toda chamada async
- [ ] [Regra específica do cliente]

### 🟢 PREFERIDO (style guidelines — sugestão, não bloqueio)
- [ ] Early return para reduzir aninhamento
- [ ] Funções pequenas com única responsabilidade
- [ ] [Preferência do cliente]

---

## Padrões de Código por Linguagem

### [Linguagem principal — ex: Dart/Flutter]

```
// ✅ Correto
final userName = user.name;

// ❌ Errado
var x = user.name;
```

### [Segunda linguagem — ex: Node.js]

```javascript
// ✅ Correto — async/await com tratamento de erro
try {
  const result = await fetchUser(id);
  return result;
} catch (error) {
  logger.error('fetchUser failed', { id, error });
  throw new AppError('USER_NOT_FOUND', error);
}

// ❌ Errado — promise sem catch, erro silencioso
fetchUser(id).then(result => result);
```

---

## Padrão de Testes

- **Framework:** [Jest / Pytest / etc]
- **Cobertura mínima:** [ex: 80%]
- **O que testar:** Toda lógica de negócio, toda API pública
- **O que não testar:** UI trivial, getters simples

```
// Exemplo de estrutura de teste esperada
describe('UserService', () => {
  it('should return user when ID exists', ...)
  it('should throw NOT_FOUND when ID is invalid', ...)
  it('should handle database errors gracefully', ...)
})
```

---

## Padrão de PR

Todo PR deve conter:
- [ ] Descrição clara do que foi feito e por quê
- [ ] Link para issue/ticket relacionado
- [ ] Screenshots (se mudança visual)
- [ ] Checklist de testes rodados
- [ ] Nenhum arquivo desnecessário (.DS_Store, *.log, etc.)

---

## Regras Extras do Cliente

> Documente aqui qualquer regra muito específica deste cliente que não se encaixa acima.

1. [Regra específica 1]
2. [Regra específica 2]
