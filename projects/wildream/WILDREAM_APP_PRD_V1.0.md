# WILD DREAM APP
## PRODUCT REQUIREMENTS DOCUMENT
**Versão 1.0 • Agosto de 2026**

---

## Visão do Produto

Uma plataforma mobile de aprendizagem de inglês baseada em repetição espaçada, prática de frases, inteligência artificial, conversação, vocabulário e acompanhamento humano. O produto terá uma experiência Free e uma experiência Pro.

---

## 1. Resumo Executivo

O Wild Dream App será um aplicativo para iOS e Android criado para transformar o estudo de inglês em uma rotina simples, mensurável e contínua. O núcleo gratuito será baseado em flashcards e repetição espaçada, permitindo que o aluno pratique frases reais em inglês, veja traduções e acompanhe sua evolução.

A versão Pro adicionará recursos de inteligência artificial, conversação por texto e voz, análise de pronúncia palavra por palavra, feedback gramatical, geração de vocabulário, desafios e suporte de professores reais.

### Princípio Central
O aplicativo não deve tentar substituir o curso. Ele deve aumentar a frequência de contato do aluno com o inglês entre as aulas e transformar estudo em hábito.

---

## 2. Objetivos do Produto

1. Aumentar a frequência de estudo dos alunos.
2. Aplicar repetição espaçada para melhorar retenção de frases e vocabulário.
3. Permitir que o aluno crie e revise seu próprio banco de frases.
4. Usar IA para desenvolver speaking, vocabulário e feedback.
5. Criar uma experiência Pro com maior profundidade e acompanhamento.
6. Gerar dados de engajamento e progresso para a administração.
7. Criar uma base tecnológica que futuramente possa atender empresas (B2B).

---

## 3. Público e Perfis de Acesso

| Perfil | Acesso | Objetivo |
|--------|--------|----------|
| Aluno Free | Recursos essenciais de estudo | Revisar frases, criar frases, acompanhar metas e progresso |
| Aluno Pro | Todos os recursos + IA + suporte | Praticar speaking, vocabulário, pronúncia, desafios e receber suporte |
| Professor | Área de atendimento | Responder dúvidas e criar/atribuir tarefas para alunos Pro |
| Administrador | Controle global | Gerenciar usuários, planos, professores, uso e indicadores |

---

## 4. Modelo Free x Pro

| Funcionalidade | Free | Pro |
|---|---|---|
| Cadastro e teste de nível | ✓ | ✓ |
| Flashcards / repetição espaçada | ✓ | ✓ |
| Criar próprias frases | ✓ | ✓ |
| Revisão e tradução | ✓ | ✓ |
| Metas e progresso | ✓ | ✓ |
| Troféus e streaks | ✓ | ✓ |
| Áudio por IA da frase | — | ✓ |
| Análise de pronúncia | — | ✓ |
| Feedback gramatical | — | ✓ |
| Conversação por texto | — | ✓ |
| Conversação por voz | — | ✓ |
| Geração de vocabulário por IA | — | ✓ |
| Atividades personalizadas por professor | — | ✓ |
| Suporte de professores | — | ✓ |

---

## 5. Onboarding e Teste de Nível

- **Cadastro:** nome, e-mail, senha e número de celular.
- **Teste de nível:** Opcional no onboarding: "Você quer fazer o teste?" → Sim / Não.
- **Tecnologia:** Perguntas padronizadas + futuramente apoio de IA.
- **Resultado:** Estimativa do nível CEFR: A1, A2, B1, B2 ou C1/C2.
- **Uso:** Nível serve para sugerir meta diária de revisão.

### Metas Iniciais Definidas
- **A1:** 150 frases/dia
- **A2:** 100 frases/dia
- **B1:** 50 frases/dia
- **B2 e C1/C2:** Configuráveis pelo administrador

---

## 6. Núcleo: Repetição Espaçada

O aluno revisa frases e classifica seu próprio desempenho. O sistema calcula a próxima aparição da frase.

| Resposta | Regra Inicial |
|---|---|
| ❌ Errei | Priorizar novamente dentro das próximas 10 frases |
| 😓 Difícil | Priorizar dentro das próximas 20 frases |
| 🙂 Bom | Priorizar dentro das próximas 30 frases |
| 😎 Fácil | Priorizar dentro das próximas 50 frases |

### Características
- O algoritmo deverá ser **parametrizável**. Esses intervalos são o comportamento inicial, não uma regra rígida.
- Quando houver poucas frases disponíveis, o sistema deverá encaixar a revisão da melhor forma possível.
- O aluno pode **adicionar suas próprias frases**.
- O aluno pode **pesquisar/adicionar frases**.
- **Categorias** são opcionais e podem ser usadas como tags simples (Daily English, Business English).
- O sistema deve **registrar histórico** de cada revisão e desempenho por frase.

---

## 7. Fluxo de Revisão de uma Frase

1. Mostrar a frase em inglês.
2. **Free:** aluno lê e faz sua própria revisão. **Pro:** pode ouvir o áudio gerado por IA.
3. **Pro:** aluno grava sua fala e recebe análise de pronúncia palavra por palavra.
4. Exibir tradução em português.
5. **Pro:** apresentar feedback de gramática e pronúncia.
6. Aluno seleciona: Errei, Difícil, Bom ou Fácil.
7. Algoritmo agenda a próxima revisão.

---

## 8. Inteligência Artificial — Pro

### 8.1 Conversação
- **Formato:** Texto e voz.
- **Cenários:** Job Interview, Business Meeting, Travel, Restaurant, Hotel, Casual Conversation etc.
- **Comportamento:** IA conduz a conversa de forma contextual.
- **Feedback:** IA corrige erros relevantes durante a conversa (sem excesso de rigidez).
- **Configuração:** Nível de rigor da correção deve ser configurável pelo aluno.

### 8.2 Vocabulário
- **Temas:** Food, Travel, Business English, Street, Work etc.
- **Geração:** IA gera palavras e/ou frases com tradução e áudio.
- **Uso:** Aluno pede, por exemplo, "20 palavras de Business English para reuniões".
- **Futuro:** Geração poderá alimentar diretamente o banco de flashcards do aluno.

### 8.3 Pronúncia e Gramática
- **Pronúncia:** Análise palavra por palavra.
- **Identificação:** Palavras com maior dificuldade.
- **Feedback:** Após a tentativa, orientado para erros que impactam compreensão.
- **Abordagem:** Sem exigir linguagem nativa perfeita.

---

## 9. Suporte Humano e Professores — Pro

- O Pro terá acesso a um **chat de suporte** com professores disponíveis.
- **Modelo:** Não há necessariamente um professor fixo por aluno.
- **Atendimento:** Solicitações atendidas por professores disponíveis em fila/caixa de entrada.
- **Exemplo:** Aluno pergunta sobre Past Perfect → professor analisa e fornece orientação curta e prática.
- **Tarefas:** Professores podem criar/atribuir tarefas personalizadas para alunos Pro.
- **Acompanhamento:** Sistema permite rastrear tarefas pendentes e respostas.

---

## 10. Home do Aluno

A tela inicial deve ser simples e orientada à ação. O aluno deve entender em poucos segundos o que precisa fazer hoje.

**Elementos:**
- Nível atual
- Frases revisadas hoje
- Frases restantes para a meta
- Meta diária
- Progresso do dia
- Streak/dias consecutivos
- Tarefa da semana
- Atividades de listening recomendadas, com links externos
- Acesso rápido a Revisar, Vocabulário, Conversação e Troféus

---

## 11. Gamificação

- **Sem ranking** entre alunos no MVP.
- **Troféus** individuais.
- **Streaks** por dias consecutivos.
- **Conquistas** por quantidade de frases revisadas.
- **Conquistas** por desafios e conversações com IA.
- **Sistema de pontuação/XP** poderá ser usado na progressão Pro.

---

## 12. Área Administrativa

Deve incluir visualização de:
- Quantidade total de alunos
- Alunos Free x Pro
- Status de pagamento
- Quantidade de professores
- Frases revisadas
- Tempo de uso/tela
- Engajamento e frequência
- Uso dos recursos de IA
- Gerenciamento de planos e permissões
- Gestão de parâmetros do sistema (metas, regras da repetição espaçada)

---

## 13. Monetização

### Preço Inicial Sugerido
- **Pro mensal:** R$ 29,90
- **Pro anual:** R$ 299,00
- Valores devem ser **configuráveis** no painel administrativo.

### Pagamento
- Cartão de crédito
- Gateway: Mercado Pago

### Arquitetura
- Deve permitir alterar preços, planos, limites de IA e benefícios sem alterar o aplicativo inteiro.
- **Franquias de IA:** Controlar consumo de IA por limites para proteger margem do produto.

---

## 14. Diretrizes Técnicas do MVP

- **Plataformas:** Aplicativos iOS e Android desde o lançamento.
- **Arquitetura:** Preferência por cross-platform (Flutter recomendado).
- **Backend:** Autenticação, BD, regras de repetição, pagamentos, notificações, integração com IA.
- **Permissões:** Por perfil (Free, Pro, Professor, Admin).
- **Eventos:** Registro de revisão, erro/acerto, tempo de uso, áudio, conversação, atividade, troféus.
- **Escalabilidade:** Preparada para versão B2B futura.
- **Segurança:** Proteção de dados, consentimento, gestão segura de credenciais e pagamentos (requisitos obrigatórios).

---

## 15. MVP — Prioridade de Lançamento

1. Cadastro/login
2. Teste de nível opcional
3. Criação e edição de frases
4. Flashcards e repetição espaçada
5. Tradução das frases
6. Metas diárias
7. Progresso e histórico
8. Troféus e streak
9. Free/Pro e controle de acesso
10. Pagamento/assinatura Pro
11. IA de áudio, pronúncia e feedback
12. Conversação IA por texto e voz
13. Vocabulário IA
14. Área de suporte com professores
15. Criação de tarefas para Pro
16. Área administrativa básica
17. Notificações essenciais

---

## 16. Roadmap Futuro — Wild Dream for Business

A arquitetura deve permitir, futuramente, transformar o produto em plataforma corporativa.

- **Contas corporativas:** Organizações/empresas.
- **Painel de RH:** Gestor/RH próprio.
- **Vínculo:** Funcionários à empresa.
- **Relatórios:** Uso, progresso, frequência.
- **Trilhas:** Por função (Sales, Customer Service, Leadership, Technology, Meetings).
- **IA especializada:** Agentes por contexto profissional.
- **Metas:** Corporativas e acompanhamento por equipe.
- **Licenças:** Por número de funcionários.

---

## 17. Princípios de UX e Produto

- **Mobile-first.**
- **Visual:** Moderno, premium, limpo e fácil de usar.
- **Navegação:** Poucos elementos por tela.
- **Ação principal:** Sempre evidente.
- **Aprendizado:** Aluno não precisa entender o algoritmo para usá-lo.
- **Feedback IA:** Claro e acionável.
- **Notificações:** Evitar excesso que distraia do estudo.
- **Free vs Pro:** Free deve ser realmente útil; Pro claramente mais valioso.

---

## 18. Decisões a Validar Antes do Desenvolvimento

- Definir metas diárias de B2, C1 e C2
- Definir limites mensais de uso de IA no Pro
- Definir se teste de nível será criado internamente ou por serviço externo
- Definir provedor de IA/voz
- Definir gateway de pagamento final
- Definir política de cancelamento e renovação
- Definir identidade visual final do aplicativo

---

## 19. Critério de Sucesso do MVP

### Pergunta Norteadora
Se um aluno abrir o app pela manhã, ele deve:
1. Saber imediatamente o que estudar
2. Conseguir revisar frases **sem fricção**
3. **Perceber seu progresso**
4. Ter uma razão clara para **voltar amanhã**

---

_Documento extraído de Wild_Dream_App_PRD_v1.0.docx • 28 de agosto de 2026_
