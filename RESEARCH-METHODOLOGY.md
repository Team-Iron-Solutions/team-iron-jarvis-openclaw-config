# RESEARCH-METHODOLOGY.md — Como Pesquisar Antes de Concluir

> Criado em 19/08/2026 após análises rasas sobre Graphify na estratégia de tokens.
> Seguir este documento antes de recomendar, descartar ou avaliar qualquer ferramenta,
> tecnologia, abordagem ou estratégia.

---

## O Problema que Este Doc Resolve

Análises rápidas levam a conclusões erradas:
- "É incompatível" (sem verificar se a limitação é real ou assumida)
- "Só serve para X" (sem pensar nos outros casos de uso)
- "Não se aplica ao nosso stack" (sem checar capacidades reais dos agentes)

---

## Checklist de Pesquisa

### Nível 1 — Rápido (Haiku, <5 min)
Use quando a pergunta é simples ou já há contexto suficiente.

- [ ] Conferi o nome correto da ferramenta/tecnologia? (typos matam pesquisas)
- [ ] Li a descrição oficial, não só o título?
- [ ] A limitação que identifiquei é **verificada** ou **assumida**?
- [ ] Consultei `AGENT-CAPABILITIES.md` antes de dizer "incompatível"?
- [ ] Considerei **todos** os agentes relevantes, não só os óbvios?
- [ ] A análise desafia a primeira conclusão que surgiu?

**Se alguma resposta for "não" → pare, reconheça e vá para Nível 2.**

---

### Nível 2 — Profundo (Sonnet + autorização do Galvão)
Use quando:
- A análise Nível 1 revelou gaps
- O tema é estratégico (custos, arquitetura, segurança, stack)
- A primeira conclusão pode estar errada mas não tenho certeza
- O impacto de errar é alto

**Antes de iniciar Nível 2, dizer:**
> "Minha análise inicial é superficial. Posso fazer uma pesquisa mais aprofundada
> com Sonnet — vai levar mais tempo e custar mais tokens. Autoriza?"

#### Passos do Nível 2

1. **Pesquisa do nome/produto**
   - Buscar variações de ortografia
   - Verificar GitHub, site oficial, PyPI/npm
   - Checar quando foi lançado (ferramenta pode ser nova)

2. **Separar camadas da ferramenta**
   - UI/integração (como Claude Code, Cursor) ≠ núcleo (CLI, API, lib)
   - O núcleo geralmente é mais portável do que parece

3. **Verificar compatibilidade real**
   - Consultar `AGENT-CAPABILITIES.md`
   - Se agente tem `exec` → provavelmente consegue usar qualquer CLI
   - Testar com spike se necessário (`sessions_spawn` modo isolado)

4. **Mapear todos os beneficiários**
   - Listar TODOS os agentes e perguntar: faz sentido para este?
   - Listar todos os repos/projetos atuais
   - Considerar casos de uso futuros

5. **Avaliar custo-benefício honesto**
   - Ganho estimado (tokens, tempo, qualidade)
   - Custo de implementação
   - Manutenção
   - Alternativas existentes

6. **Documentar conclusão com evidências**
   - O que foi verificado vs. o que foi assumido
   - Fontes consultadas
   - Próximos passos concretos

---

## Quando Reconhecer que a Análise é Rasa

Sinais de alerta:
- A conclusão veio em menos de 30 segundos
- Usou palavras como "provavelmente", "acredito", "deve ser" sem verificar
- Não checou o nome exato da ferramenta
- Limitou o escopo sem justificativa (só backend, só um agente, etc.)
- A conclusão confirma o que parecia óbvio de início

**Resposta correta:** parar, admitir, e perguntar se vale aprofundar.

---

## Template de Resposta Honesta

Quando a análise está incompleta:

```
Minha análise inicial aponta para [X], mas reconheço que não verifiquei [Y] e [Z].
Para uma avaliação confiável, preciso pesquisar mais fundo — isso exige Sonnet
e aproximadamente [tempo estimado]. Autoriza?
```

---

## Histórico de Aprendizados

| Data | Caso | Erro | Lição |
|---|---|---|---|
| 19/08/2026 | Graphify na estratégia de tokens | Não pesquisei pelo nome correto ("Graphyfi" vs "Graphify") | Sempre verificar ortografia antes de concluir "não existe" |
| 19/08/2026 | Graphify + Anthropic models | Confundi integração UI (Claude Code) com compatibilidade real | Separar camadas: UI/integração ≠ núcleo da ferramenta |
| 19/08/2026 | Graphify para frontend | Limitei para "apenas backend" sem justificativa | Sempre perguntar: "e para os outros agentes?" antes de concluir |
