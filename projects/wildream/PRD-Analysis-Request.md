# Wildream App PRD — Analysis Request

**Para:** Stephen Strange (Product Manager)  
**De:** Jarvis (Tech Lead)  
**Data:** 28 de agosto de 2026  
**Status:** ⏳ AWAITING ANALYSIS  

---

## 📋 O que pedimos

Leia **atentamente** o PRD do Wildream App (abaixo) e:

1. **Identifique pontos fortes** — O que está bem pensado, o que é realista
2. **Identifique fraquezas** — O que pode ser ambíguo, arriscado ou impraticável
3. **Faça apontamentos** — Sugestões de mudança, clarificação ou priorização
4. **Traga dúvidas** — Qualquer coisa que não fique clara no documento
5. **Recomende ajustes** — Para o MVP ser mais realista/alcançável

---

## 📊 Contexto do Projeto

- **Cliente:** Wildream
- **Produto:** Aplicativo mobile de aprendizagem de inglês (iOS + Android)
- **Modelo:** Free + Pro (assinatura)
- **Timeline:** A definir (provavelmente 8-12 semanas para MVP)
- **Stack:** Mobile-first, cross-platform (recomendado Flutter)
- **Tecnologias:** IA (conversação, pronúncia, vocabulário), pagamentos, notificações

---

## 📄 PRD Completo

[Veja WILDREAM_APP_PRD_V1.0.md neste mesmo diretório]

### Resumo Executivo
Uma plataforma mobile de aprendizagem de inglês baseada em:
- Repetição espaçada (flashcards)
- Prática de frases
- IA para conversação, pronúncia, vocabulário
- Suporte humano (professores) na versão Pro

### Públicos
- **Aluno Free:** Flashcards + repetição espaçada
- **Aluno Pro:** +IA, conversação, pronúncia, feedback, suporte de professor
- **Professor:** Suporte ao aluno, criação de tarefas
- **Admin:** Painel de controle (usuários, métricas, planos)

### Funcionalidades Principais (MVP)

#### Free
- Cadastro/login
- Teste de nível (CEFR)
- Flashcards com repetição espaçada
- Criar/editar frases
- Traduções
- Metas diárias
- Histórico e progresso
- Troféus e streaks

#### Pro (tudo acima +)
- Áudio gerado por IA
- Análise de pronúncia (palavra por palavra)
- Feedback gramatical
- Conversação por texto com IA
- Conversação por voz com IA
- Geração de vocabulário
- Tarefas atribuídas por professor
- Suporte via chat com professor

### Monetização
- **Pro mensal:** R$ 29,90
- **Pro anual:** R$ 299,00
- **Controle:** Configurável no painel admin (permite A/B tests)
- **Gatewap:** Cartão de crédito + Mercado Pago

### Roadmap Futuro
- **Wild Dream for Business:** versão corporativa (B2B) com:
  - Contas de empresas
  - Painel de RH
  - Trilhas por função profissional
  - Relatórios agregados

---

## ⚠️ Pontos para Análise

Abaixo estão as áreas onde esperamos sua análise crítica:

### 1. **Escopo do MVP**
- O MVP está bem equilibrado ou tá tentando fazer muito?
- Quais features são realmente essenciais vs "nice-to-have"?
- A priorização faz sentido?

### 2. **Modelo de IA**
- Conversação + pronúncia + vocabulário — é viável num MVP?
- Qual provedor de IA faz mais sentido? (OpenAI, Google, local Ollama?)
- Custos de IA podem comprometer a margem Pro?

### 3. **Suporte Humano (Professores)**
- Como escalar atendimento de professores com base de alunos crescendo?
- Fazer fila de professores no MVP é a estratégia certa?
- Ou seria melhor lançar apenas IA no MVP e adicionar professores no V1.1?

### 4. **Monetização**
- R$ 29,90/mês é competitivo? Está validado com mercado?
- Limite de IA por mês (franquia) — qual número é realista?
- Será que a metade dos users nem conseguem ativar Pro no lançamento?

### 5. **Métricas e Sucesso**
- A "pergunta norteadora" é boa, mas como vamos medir o MVP realmente funcionou?
- Quais são os KPIs específicos?

### 6. **Riscos Técnicos**
- Escalabilidade de notificações (muitos alunos, muitos streamming)
- Segurança de dados de áudio/voz
- Integração com Mercado Pago (qual complexidade?)

### 7. **Roadmap B2B**
- Faz sentido arquitetar para B2B desde o começo, ou pode causar over-engineering?
- A empresa tem intenção real de virar B2B, ou é especulativa?

---

## 📝 Formato de Resposta

Pedimos que você traga sua análise como:

```markdown
# Análise PRD Wildream — Stephen Strange

## ✅ Pontos Fortes
1. [Ponto forte 1]
2. [Ponto forte 2]
...

## ⚠️ Fraquezas / Riscos
1. **Título:** Descrição, impacto, recomendação

## 🤔 Dúvidas
1. **Pergunta 1:** Contexto
2. **Pergunta 2:** Contexto

## 💡 Recomendações
1. **Título da mudança:** Antes / Depois, razão

## 📊 Proposta de Ajustes ao MVP
[Ajustes prioritários, por ordem]

## ✍️ Observações Finais
[Qualquer coisa adicional]
```

---

## 📅 Timeline Esperada

- **28/08 (hoje):** Você recebe este documento
- **Antes de 02/09:** Suas análises estarão prontas
- **02-03/09:** Galvão valida suas recomendações + faz pivot se necessário
- **03/09+:** Kickoff técnico (arquitetura, tech stack, sprints)

---

## 🔗 Arquivos do Projeto

```
/Users/teamironsolutions/.openclaw/workspace/projects/wildream/
├── Wild_Dream_App_PRD_v1.0.docx (original)
├── WILDREAM_APP_PRD_V1.0.md (markdown extraída)
├── PRD-Analysis-Request.md (este arquivo)
├── PRD-Analysis-Response.md (seu documento, quando pronto)
├── obsidian-wildream-project.md (Obsidian — contexto do projeto)
└── progress.md (histórico de decisões e aprendizados)
```

---

## 📞 Contato

Qualquer dúvida: pergunte ao Jarvis (message ao agentId: `stephen`).

---

**Obrigado pela análise cuidadosa, Stephen. Essa é a qualidade que o Wildream merece.**

—  Jarvis  
Tech Lead, Team Iron Solutions  
28 de agosto de 2026
