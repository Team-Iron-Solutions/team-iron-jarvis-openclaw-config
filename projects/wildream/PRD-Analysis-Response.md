# Análise PRD Wildream — Stephen Strange
**Data:** 28 de agosto de 2026
**Versão PRD analisada:** 1.0
**Autor:** Stephen Strange — Product Manager, Team Iron Solutions

---

> **TL;DR:** O PRD tem uma visão clara, um princípio central excelente e boas decisões de produto. O problema é escopo: ele descreve um produto de 6-9 meses como se fosse entregável em 10-12 semanas. Com ajustes cirúrgicos de escopo e a definição de KPIs mensuráveis, o Wildream tem potencial real.

---

## ✅ Pontos Fortes

### 1. Princípio Central é Ouro
> *"O aplicativo não deve tentar substituir o curso. Ele deve aumentar a frequência de contato do aluno com o inglês entre as aulas."*

Isso é Jobs to Be Done na essência. O produto tem razão de existir bem definida, não compete com o núcleo do negócio (professores/cursos) e resolve um problema real de comportamento: consistência de estudo. Poucas equipes chegam ao MVP com esse nível de clareza de propósito.

### 2. Free Tier Genuinamente Útil
A decisão de fazer o Free com funcionalidade real (repetição espaçada + metas + progresso + troféus) é estrategicamente correta. Free como teaser gera frustração e abandono. Free como produto gera word-of-mouth e conversão orgânica de qualidade.

### 3. Critério de Sucesso da Seção 19
A pergunta norteadora é excelente:
1. Saber o que estudar
2. Revisar sem fricção
3. Perceber progresso
4. Ter razão para voltar amanhã

Isso é um mini user journey que qualquer decisão de design pode ser testada contra. Manter isso visível durante o desenvolvimento.

### 4. Algoritmo Parametrizável
Não engessar as regras de repetição espaçada em código é uma decisão de produto madura. Permite ajuste baseado em dados sem novo deploy. Aprovado.

### 5. Seção 18 — Decisões a Validar
O fato de o PRD listar explicitamente o que ainda NÃO está decidido mostra maturidade. Muitos PRDs escondem incertezas. Aqui estão expostas. Isso facilita planejamento técnico honesto.

### 6. Gamificação sem Ranking no MVP
Ranking entre usuários no início é armadilha: cria pressão negativa, desfavorece novos usuários e pode causar abandono precoce. A decisão de usar troféus individuais + streaks é mais segura e pedagogicamente mais saudável.

### 7. 4 Perfis de Acesso Bem Definidos
Aluno Free, Aluno Pro, Professor, Admin — cada um com objetivo claro. Isso simplifica decisões de autorização e UX.

### 8. Monetização Configurável por Admin
Permitir alterar preços, planos e limites de IA sem redeploy do app é arquitetura correta. Isso viabiliza testes de preço e ajuste de margem conforme o custo de IA se torna conhecido.

---

## ⚠️ Fraquezas / Riscos

### 1. 🔴 CRÍTICO — Escopo do MVP é Irreal para 10-12 Semanas
**Problema:** O MVP lista 17 itens de prioridade incluindo: Flutter + iOS + Android + backend + repetição espaçada + IA de áudio + análise de pronúncia + conversação por texto e voz + suporte de professores + área administrativa + Mercado Pago + notificações. Isso não é MVP — é um produto completo.

**Impacto:** Risco altíssimo de atraso, qualidade comprometida em tudo, lançamento com bugs sérios ou cancelamento parcial de features na última hora.

**Recomendação:** Cortar pelo menos 4-5 features do MVP e empurrar para V1.1. Detalho na seção de Priorização.

---

### 2. 🔴 CRÍTICO — Metas Diárias para A1 São Pedagógicamente Problemáticas
**Problema:** A1 = 150 frases/dia. Um iniciante completo, em uma sessão de 15-20 minutos, provavelmente consegue 20-40 frases. 150 frases/dia implica 45-90+ minutos de estudo diário para quem mal sabe escrever "Hello".

**Impacto:** O usuário que mais precisa de encorajamento (iniciante A1) será o primeiro a sentir que "não consegue cumprir a meta" e abandonar. Alta probabilidade de churn precoce.

**Recomendação:** Revisar as metas com pedagogo ou dados de referência de Anki/Duolingo. Sugestão inicial: A1: 20-30 frases/dia, A2: 30-50/dia, B1: 50-80/dia. Deixar configurável pelo admin como backup.

---

### 3. 🔴 CRÍTICO — Algoritmo de Repetição Espaçada Baseado em Contagem, Não em Tempo
**Problema:** O PRD define repetição espaçada como "próximas 10/20/30/50 frases". Isso não é repetição espaçada — é repetição por frequência dentro da sessão. Repetição espaçada real é baseada em **intervalos de tempo** (horas/dias), como no SM-2 ou FSRS. Um usuário que faz 200 revisões numa sessão e para por 3 dias não terá a frase aparecendo no momento certo.

**Impacto:** O produto pode não entregar o benefício de retenção prometido, comprometendo o core value proposition.

**Recomendação:** Usar algoritmo SM-2 ou FSRS (open-source, bem documentados). Os intervalos do PRD (10/20/30/50) podem ser usados para priorização dentro de uma sessão, mas o agendamento de revisões deve ser por tempo (ex: "revisar em 1 dia", "revisar em 3 dias", "revisar em 1 semana").

---

### 4. 🟠 ALTO — Custo de IA Pode Destruir a Margem do Pro
**Problema:** Com R$ 29,90/mês por usuário Pro, e sem limites definidos, um usuário ativo de conversação por voz pode facilmente custar R$ 15-25/mês em APIs de IA (OpenAI Whisper + GPT-4o + TTS). Isso zera ou inverte a margem.

**Impacto:** Produto inviável economicamente com crescimento.

**Recomendação:** Antes do kickoff técnico, calcular o custo médio estimado por usuário Pro com as APIs consideradas. Definir franquia mensal (ex: 30 sessões de conversação, 500 análises de pronúncia). Documentar no PRD na Seção 13.

---

### 5. 🟠 ALTO — Suporte de Professores no MVP é Complexidade Operacional Desnecessária
**Problema:** Professores em fila requerem: sistema de fila + onboarding de professores + SLA de resposta + controle de qualidade + custo operacional variável + interface de professor testada. Isso é um produto dentro do produto.

**Impacto:** Distrai a equipe do core (flashcards + IA), adiciona complexidade de suporte humano antes de saber se os usuários vão querer isso.

**Recomendação:** Substituir no MVP por suporte assíncrono simples (formulário/ticket com resposta em 48h por email). Lançar a feature de chat com professor no V1.1, quando o volume de Pro justificar o investimento operacional.

---

### 6. 🟠 ALTO — Banco de Frases Inicial Não Mencionado
**Problema:** Para o sistema de repetição espaçada funcionar no Day 1, precisa haver frases pré-carregadas. Quem cria isso? Quantas? Por nível? Por categoria? Isso é trabalho editorial/pedagógico substancial que simplesmente não aparece no PRD.

**Impacto:** Sem conteúdo inicial, o onboarding do Free vira: "crie suas frases". Isso é barreira de entrada alta demais para um iniciante. O app parece vazio.

**Recomendação:** Definir, antes do kickoff: volume mínimo de frases por nível (ex: 300 por nível CEFR), categorias iniciais, responsável pela criação, e se há curadoria humana ou geração por IA.

---

### 7. 🟠 ALTO — Conversação por Voz no MVP É Feature de Alto Risco
**Problema:** Conversação por voz envolve: STT em tempo real, processamento de latência, resposta de LLM, TTS, UX de push-to-talk ou VAD (voice activity detection), tratamento de ruído ambiente, e fluxo de erro quando não entende. São 3-4 sistemas integrados com latência sensível ao usuário.

**Impacto:** Feature complexa, cara, com UX difícil de acertar. Se lançada com qualidade ruim, prejudica a percepção do Pro.

**Recomendação:** MVP só com conversação por texto. Conversação por voz no V1.1 quando o fluxo de texto já estiver validado e os custos conhecidos.

---

### 8. 🟡 MÉDIO — Área Administrativa Completa no MVP
**Problema:** A seção 12 lista 11 métricas e gerenciamentos diferentes na área admin. Para um MVP, isso é trabalho significativo que não gera valor direto para o usuário final.

**Impacto:** Usa capacidade técnica que poderia ir para o core do produto.

**Recomendação:** Admin MVP = (1) listagem de usuários, (2) gestão de planos/permissões, (3) métricas básicas (total de usuários, Free vs Pro, receita). Dashboards completos de engajamento no V1.1.

---

### 9. 🟡 MÉDIO — Sem KPIs Definidos
**Problema:** O PRD tem critérios qualitativos (pergunta norteadora) mas sem métricas quantitativas. Não há: taxa de conversão Free→Pro alvo, retenção D7/D30 alvo, DAU/MAU, churn aceitável, NPS, receita no mês 3.

**Impacto:** Sem KPIs, a equipe não sabe quando o MVP "funcionou". Há risco de perseguir perfeccionismo sem critério de lançamento ou, ao contrário, lançar antes de validar product-market fit.

**Recomendação:** Definir pelo menos 3 métricas de sucesso para o MVP com metas numéricas. Ver seção de Recomendações.

---

### 10. 🟡 MÉDIO — Teste de Nível Sem Especificação Técnica
**Problema:** "Perguntas padronizadas + futuramente apoio de IA." Quem cria as perguntas? Quantas? Como são mapeadas ao CEFR? A acurácia de nivelamento afeta diretamente as metas diárias, que por sua vez afetam engajamento.

**Impacto:** Teste mal calibrado = metas erradas = experiência ruim no Day 1 para todos os usuários.

**Recomendação:** Definir se o teste será interno (20-30 perguntas curadas) ou via API de terceiros (ex: Duolingo-like ou serviço de avaliação CEFR). Isso precisa estar decidido antes do kickoff.

---

### 11. 🟡 MÉDIO — Estratégia Offline Ausente
**Problema:** O PRD não menciona se o app funciona offline. Para flashcards de revisão diária, offline é quase obrigatório (usuário no metrô, avião, área sem conexão).

**Impacto:** DAU cai em cenários de baixa conectividade. Isso é comum no público-alvo brasileiro.

**Recomendação:** Definir quais features funcionam offline (mínimo: revisar frases já baixadas, marcar progresso localmente e sincronizar depois).

---

## 🤔 Dúvidas para Galvão / Equipe

### 1. Qual o volume de usuários esperado no lançamento?
Isso impacta diretamente a escolha de infraestrutura e o custo de IA estimado. 500 usuários Pro vs 5.000 são cenários muito diferentes.

### 2. A Wildream já tem alunos ativos em cursos presenciais/online?
Se sim: há migração planejada? Isso adiciona workload significativo (importação de dados, notificações de launch, suporte à transição).

### 3. Há banco de frases ou material pedagógico já existente?
Se já existe conteúdo (listas de vocabulário, frases do curso, materiais dos professores), isso acelera muito o onboarding de conteúdo. Se não, quem cria e quando?

### 4. Quantos professores estarão disponíveis no lançamento e com qual SLA de resposta?
Sem isso, não é possível dimensionar o sistema de fila e o prometido "suporte de professor" pode se tornar um passivo de experiência.

### 5. Qual é o orçamento máximo mensal para APIs de IA (OpenAI, Google, etc.)?
Isso define diretamente os limites de franquia do Pro. Sem esse número, o pricing pode estar errado.

### 6. O app é complemento ao curso Wildream ou produto standalone (qualquer pessoa pode comprar)?
Se for standalone: o onboarding precisa ser completamente autoexplicativo. Se for complemento: pode assumir que o usuário já tem um professor humano como âncora.

### 7. Houve alguma validação com usuários reais (entrevistas, protótipo, beta)?
O mantra é: validar antes de dev investir. Qual é o nível de validação atual? Há dados de que os usuários pagariam R$ 29,90/mês por isso?

### 8. O chat com professor é síncrono (resposta imediata) ou assíncrono (resposta em horas)?
Isso muda completamente a arquitetura técnica e as expectativas do usuário Pro.

### 9. A identidade visual está definida? Existe Figma?
Flutter precisa de um design system para começar. Sem design pronto, o desenvolvimento começa "no escuro" e gera retrabalho.

### 10. B2B: é intenção real de negócio ou especulativa?
A resposta muda a decisão de arquitetura. "Arquitetar para B2B" sem intenção real pode ser over-engineering custoso.

---

## 💡 Recomendações

### 1. Cortar Escopo do MVP — Regra do "O Quê Não Pode Faltar"
**Antes:** 17 features de prioridade no MVP, incluindo conversação por voz, pronúncia palavra a palavra, professores, admin completo.
**Depois:** MVP foca no loop central: revisar frases → perceber progresso → querer voltar. Tudo o mais é V1.1+.
**Razão:** Produto que faz 5 coisas excelentemente é melhor que produto que faz 15 coisas mediocremente.

### 2. Definir KPIs de Sucesso Antes do Kickoff
**Antes:** Critério qualitativo (pergunta norteadora).
**Depois:** KPIs concretos. Sugestão:
- **Retenção D7:** ≥ 40% dos usuários retornam após 7 dias
- **Conversão Free→Pro:** ≥ 5% no mês 1, ≥ 10% no mês 3
- **DAU/MAU:** ≥ 30% (indica hábito)
- **Streak médio:** ≥ 5 dias consecutivos
- **Churn mensal Pro:** ≤ 10%
**Razão:** Sem números, não existe critério de lançamento nem aprendizado pós-MVP.

### 3. Corrigir o Algoritmo de Repetição Espaçada
**Antes:** Intervalo por contagem de frases (próximas 10/20/30/50).
**Depois:** Intervalo por tempo (SM-2 ou FSRS — bibliotecas open-source maduras). Os intervalos do PRD atual podem ser usados como priorização dentro da sessão do dia.
**Razão:** O core value proposition do produto é repetição espaçada eficaz. Se isso estiver errado, o produto não entrega o que promete.

### 4. Revisar Metas Diárias com Base Pedagógica
**Antes:** A1 = 150 frases/dia.
**Depois:** A1 = 20-30 frases/dia, A2 = 30-50, B1 = 50-80, B2+ = configurável.
**Razão:** Meta alcançável gera sucesso → dopamina → retorno. Meta impossível gera fracasso → abandono.

### 5. Substituir Suporte por Professor (MVP) por Ticket Assíncrono
**Antes:** Chat em fila com professores disponíveis no MVP.
**Depois:** Formulário de dúvida com resposta via email/push em 24-48h. Sistema de chat com professor entra no V1.1.
**Razão:** Menos complexidade técnica, menos risco operacional, valida se os usuários Pro realmente usam esse canal antes de investir em uma interface completa.

### 6. Definir Conteúdo Inicial Antes do Kickoff Técnico
**Antes:** Não mencionado no PRD.
**Depois:** Criar plano de conteúdo: mínimo 200 frases por nível CEFR (A1/A2/B1/B2), organizadas por categoria. Responsável definido. Data de entrega: semana 2 do projeto.
**Razão:** Sem conteúdo, o app está vazio no lançamento.

### 7. Conversação por Voz → V1.1
**Antes:** Conversação por texto e voz no MVP.
**Depois:** Conversação por texto no MVP. Voz no V1.1.
**Razão:** Reduz complexidade técnica, custo de API e UX risk. A conversação por texto já valida o modelo de IA antes de adicionar a camada de voz.

### 8. Definir Franquia de IA Antes do Desenvolvimento
**Antes:** "Controlar consumo de IA por limites para proteger margem."
**Depois:** Número específico (ex: 60 sessões de conversação/mês, 200 análises de pronúncia/mês no plano Pro mensal). Simulação de custo por usuário.
**Razão:** Sem isso, a equipe de backend não sabe como implementar o controle, e o pricing pode estar errado.

### 9. Definir Estratégia Offline Mínima
**Antes:** Não mencionado.
**Depois:** Flashcards de revisão do dia funcionam offline. Progresso local sincroniza quando reconectar. Features de IA requerem conexão (ok, com mensagem clara).
**Razão:** Consistência de uso depende de funcionar no metrô, no ônibus, nos "buracos" de conectividade.

---

## 📊 Proposta de Priorização Revisada

### MVP Real — 10-12 Semanas (Flutter + Backend + iOS + Android)

**Semanas 1-2: Fundação**
1. ✅ Cadastro / Login / Auth
2. ✅ Onboarding + Teste de Nível básico (20 perguntas curadas, resultado CEFR)
3. ✅ Banco de frases inicial (conteúdo pré-carregado por nível/categoria)
4. ✅ CRUD de frases (criar, editar, pesquisar)

**Semanas 3-5: Core Loop**
5. ✅ Flashcards + Repetição Espaçada (algoritmo SM-2 real, baseado em tempo)
6. ✅ Metas diárias (baseadas no nível CEFR)
7. ✅ Progresso do dia + histórico

**Semanas 5-6: Engajamento**
8. ✅ Streak de dias consecutivos
9. ✅ Troféus básicos (5-6 conquistas principais)
10. ✅ Notificações push essenciais (lembrete diário)

**Semanas 6-8: Monetização**
11. ✅ Free/Pro + controle de acesso por perfil
12. ✅ Pagamento: assinatura Pro (Mercado Pago)
13. ✅ Áudio das frases por IA (Pro — TTS simples)

**Semanas 8-10: IA Texto (Pro)**
14. ✅ Conversação por texto com IA (cenários pré-definidos)
15. ✅ Análise de pronúncia básica (gravação + feedback simples — pode ser STT + score)

**Semanas 10-12: Admin + Ajustes**
16. ✅ Admin básico (usuários, planos, receita, parâmetros)
17. ✅ Testes de integração, QA, ajustes de UX
18. ✅ Submissão às stores (App Store + Google Play)

---

### V1.1 — Pós-Lançamento (baseado em aprendizados do MVP)
- Conversação por voz com IA
- Análise de pronúncia palavra a palavra (mais detalhada)
- Geração de vocabulário por IA
- Chat com professores (versão real, com fila)
- Gamificação avançada (mais troféus, XP)
- Admin com dashboards de engajamento completos
- Feedback gramatical avançado

### V2.0 — Wild Dream for Business (quando B2B for decisão validada)
- Contas corporativas, painel RH, trilhas por função, licenciamento

---

## ✍️ Observações Finais

### Sobre o Produto em Si
O Wildream tem um conceito sólido. O mercado de aprendizagem de inglês no Brasil é enorme, e há espaço para um produto que genuinamente resolve a consistência de estudo — não apenas gamificação vazia. O princípio central ("aumentar frequência de contato, não substituir o curso") é diferenciador se mantido com disciplina durante o desenvolvimento.

### Sobre a Decisão de Escopo
A maior ameaça ao sucesso do Wildream não é a tecnologia — é a tentação de lançar tudo ao mesmo tempo e lançar tudo pela metade. **Um app excelente de flashcards + repetição espaçada real já seria um produto valioso.** A IA e os professores tornam o Pro valioso, mas o Free precisa ser forte o suficiente para criar o hábito.

### Sobre Validação
O mantra é validar assumções com usuários antes de dev investir. Antes do kickoff de 03/09, recomendo fortemente: 5 entrevistas com alunos da Wildream (ou potenciais usuários) com um protótipo navegável no Figma, focando em: (1) eles entenderam o valor? (2) usariam diariamente? (3) pagariam R$ 29,90/mês?

### Sobre o Algoritmo de Repetição Espaçada
Este é o coração pedagógico do produto. Vale uma conversa técnica separada antes do kickoff para decidir entre SM-2 (clássico, simples) e FSRS (estado da arte, open-source). Errar aqui compromete o core value prop.

### Sobre B2B
Minha recomendação: **não arquitetar para B2B no MVP**. Arquitetar para multi-tenant com isolamento de dados sim (boa prática), mas não criar entidades de "empresa", "RH", "trilhas por função" agora. B2B é uma decisão de produto que precisa de validação própria. Evite o over-engineering especulativo.

---

**Este documento está pronto para revisão do Galvão.**
Qualquer ponto que precise de aprofundamento ou divergência, é só acionar.

— **Stephen Strange**
Product Manager, Team Iron Solutions
28 de agosto de 2026

---
*Análise baseada em WILDREAM_APP_PRD_V1.0.md • PRD-Analysis-Request.md*
