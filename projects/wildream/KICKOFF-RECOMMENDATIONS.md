# Wildream — Recomendações para Kickoff (03/09+)

**Preparado por:** Jarvis (Tech Lead) + Stephen Strange (PM)  
**Data:** 28 de agosto de 2026  
**Status:** ⏳ AGUARDANDO VALIDAÇÃO GALVÃO  

---

## TL;DR — As Decisões Críticas Antes do Kickoff

Se Galvão decidir prosseguir com Wildream, **estas são as 5 decisões não-negociáveis antes de 03/09:**

1. ✅ **Escopo real:** Cortar ~5-6 features do MVP original (ver Seção 1)
2. ✅ **Algoritmo de repetição:** Usar SM-2 ou FSRS (tempo, não contagem)
3. ✅ **Metas diárias:** Revisar com base pedagógica (A1 = 20-30, não 150)
4. ✅ **Validação:** 5 entrevistas com usuários + protótipo Figma ANTES do dev
5. ✅ **Conteúdo:** Definir plano de frases iniciais (200/nível CEFR mínimo)

---

## 1. Escopo MVP Realista (10-12 Semanas)

### O Problema
O PRD original propõe 17 itens de prioridade incluindo conversação por voz + pronúncia detalhada + chat com professores + admin completo. Isso é 6-9 meses de trabalho, não 10-12 semanas.

### Solução: MVP Revisado

**ENTRA no MVP:**
- ✅ Cadastro / Login / Auth
- ✅ Onboarding + Teste de Nível (20 perguntas curadas)
- ✅ Banco de frases inicial (conteúdo pré-carregado)
- ✅ CRUD de frases (criar, editar, pesquisar)
- ✅ **Flashcards + Repetição Espaçada REAL (SM-2)**
- ✅ Metas diárias configuráveis
- ✅ Progresso + histórico + streak
- ✅ Troféus básicos (5-6 conquistas)
- ✅ Free/Pro + acesso diferenciado
- ✅ Pagamento (Mercado Pago)
- ✅ Notificações push essenciais
- ✅ **Áudio das frases por IA (Pro)**
- ✅ **Conversação por TEXTO com IA (Pro)**
- ✅ **Pronúncia básica (Pro)** — gravação + feedback simples
- ✅ Admin mínimo (usuários, planos, receita, parâmetros)
- ✅ Suporte: Ticket assíncrono (formulário → resposta email/push 24-48h)

**SAI do MVP → V1.1:**
- ❌ Conversação por VOZ (risco técnico alto, custo alto)
- ❌ Pronúncia palavra-a-palavra (detalhada)
- ❌ Geração de vocabulário por IA
- ❌ Chat com professores (fila, interface real)
- ❌ Dashboards de admin completos

### Impacto
- Escopo cai ~30%
- Risco de atraso cai drasticamente
- MVP no prazo: provável vs possível
- Qualidade do core (flashcards + repetição) fica excelente

---

## 2. Algoritmo de Repetição Espaçada — CRÍTICO

### O Problema
PRD atual: "Próximas 10/20/30/50 frases" = repetição por frequência, não por tempo.

Isso NÃO é repetição espaçada. Repetição espaçada real é SM-2 ou FSRS — baseada em dias/horas.

**Exemplo do problema:**
- Usuário faz 200 flashcards numa sessão e para por 3 dias
- Sem algoritmo de tempo, as frases não reaparecem no momento certo
- Aprendizado não ocorre
- Produto não entrega a value proposition

### Solução

**Usar SM-2 (Spaced Repetition Algorithm 2):**
- Open-source, bem documentado, pedagógico
- Intervalo = dias (1d, 3d, 7d, 14d, 30d+)
- Ajusta automaticamente baseado no desempenho do usuário
- Implementação: ~300 linhas de código

**Alternativa avançada: FSRS (Free Spaced Repetition Scheduler):**
- Estado da arte (2021+)
- Machine learning para otimizar intervalos
- Mais complexo, mas melhor retenção

**Recomendação:** SM-2 no MVP (simples, pronto). FSRS no V1.2 se quiser otimização posterior.

**Implementação:**
1. Backend: calcular próximo intervalo baseado em resposta + desempenho anterior
2. BD: armazenar (dataUltima, intervaloProxima, qualidade)
3. Frontend: mostrar apenas frases vencidas (intervalo passou)

**Não fazer:**
- ❌ "Próximas 50 frases" — isso é gamificação, não repetição espaçada
- ❌ Cronômetro fixo (ex: revisar a cada 24h) — ignora o desempenho do usuário

---

## 3. Metas Diárias — Revisar com Base Pedagógica

### O Problema
A1 = 150 frases/dia.

Um iniciante completo não consegue 150 frases em 30 minutos. Resultado: fracasso no Day 1, abandono no Day 2.

### Recomendação

**Nova escala de metas:**
- **A1 (Iniciante):** 20-30 frases/dia (~ 10-15 min)
- **A2 (Elementar):** 30-50 frases/dia (~ 15-25 min)
- **B1 (Intermediário):** 50-80 frases/dia (~ 25-40 min)
- **B2+ (Avançado):** Configurável pelo admin (50-100+)

**Lógica:** Iniciante precisa de sucesso rápido e hábito. Intermediário já tem momentum. Avançado quer desafio.

**Validar:** Antes do lançamento, rodar esses números com 5-10 alunos reais. Ajustar se necessário.

**Implementar:** Campo editável no admin para cada nível (permite A/B test posterior).

---

## 4. Validação com Usuários — ANTES do Desenvolvimento

### Timing
**Isso precisa acontecer entre 28/08 e 02/09 — ANTES do kickoff de 03/09.**

### O Quê Fazer

1. **Recrutar 5-10 potenciais usuários:**
   - Podem ser alunos atuais da Wildream ou encontrados em grupos de aprendizagem de inglês
   - Mínimo: 2 iniciantes (A1), 2 intermediários (B1), 1 avançado

2. **Preparar protótipo Figma navegável:**
   - Onboarding completo
   - 1 sessão de flashcards
   - Tela de progresso
   - Oferta de Pro

3. **Roteiro de entrevista (30 min por pessoa):**
   - "O que você achou ao abrir? Entendeu o que faz?"
   - "Você usaria isso todos os dias?"
   - "Qual seria o maior problema?"
   - "Você pagaria R$ 29,90/mês por isso? Por quê?"

4. **Documentar insights:**
   - Usar/não usar? Frequência estimada?
   - Preço está ok?
   - Features faltando?
   - Barreiras de atrito?

### Por Quê Isso Importa
Sem validação, há risco real de:
- Lançar algo que ninguém quer
- Descobrir bloqueadores técnicos no meio do dev
- Encontrar "o Wildream já existe" (Duolingo, Busuu, etc.)
- Preço está errado
- UI é confusa

### Saída
Documento com 5-10 insights validados. Se >70% das respostas foram "sim, usaria", prosseguir com kickoff.

---

## 5. Conteúdo Inicial — Banco de Frases

### O Problema
PRD não especifica quem cria as frases iniciais. Sem conteúdo, o app está vazio no lançamento.

### Recomendação

**Antes do kickoff:**

1. **Definir volume:**
   - Mínimo: 200 frases por nível CEFR (A1, A2, B1, B2+)
   - Total: ~800 frases no lançamento
   - Ideal: 400-500 por nível (2.000 total)

2. **Organização:**
   - Por nível (A1-C1)
   - Por categoria: Everyday, Business, Travel, Food, etc. (4-5 categorias no MVP)
   - Por dificuldade dentro do nível

3. **Responsável:**
   - ❓ Wildream tem professores que podem curar?
   - ❓ Ou gerar via IA (GPT) + review humano?
   - ❓ Ou comprar pronto de um banco de dados pedagógico?

4. **Timeline:**
   - Precisa estar pronto na **semana 2 do desenvolvimento** (para testes)
   - Se gerar por IA: 2-3 dias + review humano

5. **Atributos de cada frase:**
   ```json
   {
     "id": "uuid",
     "texto_en": "Hello, how are you?",
     "traducao_pt": "Olá, como você está?",
     "nivel": "A1",
     "categoria": "Everyday",
     "audio_url": "s3://...", (preenchido depois pelo backend)
     "criado_em": "2026-08-28"
   }
   ```

### Decisão de KickOff
**Pergunta para Galvão:** Há banco de frases ou material existente, ou partimos do zero?

---

## 6. Decisões Técnicas Restantes

### 6.1 Provedor de IA/Voz
**O que precisa:** TTS (áudio), STT (transcrição), LLM (conversação), speech-to-text para pronúncia.

**Opções:**
- **OpenAI:** Whisper (STT) + GPT-4o (conversação) + TTS — custo ~$0.015-0.02 por frase
- **Google Cloud:** Speech-to-Text + Generative AI + Text-to-Speech — custo similar
- **Local (Ollama):** LLM local (qwen3.5) + Whisper.cpp — custo zero, mas mais complexo

**Recomendação:** OpenAI para MVP (integração rápida, qualidade alta). Avaliar local/Google em V1.1 baseado em custo real.

### 6.2 Gateway de Pagamento
**PRD menciona:** Mercado Pago (recomendado para Brasil).

**Validar:**
- Taxa de transação
- Suporte a assinatura (não apenas one-time)
- Webhooks para cancelamento/renovação
- Documentação para Flutter

**Ação:** Antes do kickoff, Tech Lead (Tony Stark?) faz spike de integração Mercado Pago com Flutter.

### 6.3 Teste de Nível CEFR
**Opções:**
1. **Interno:** 20-30 perguntas curadas, mapeadas ao CEFR (simples, custa 1-2 dias)
2. **Externo:** API de serviço de avaliação CEFR (caro, mas validado)
3. **IA:** Chatbot que faz perguntas adaptativas (mais complexo)

**Recomendação:** Interno no MVP (perguntas curadas). Se validação com usuários mostrar falta de acurácia, migrar para API externo no V1.1.

### 6.4 Offline
**Decisão:** Flashcards pré-baixados funcionam offline. Features de IA requerem conexão (ok, com mensagem clara).

**Implementação:** Sincronização local + quando conectar, push de mudanças.

### 6.5 Franquia de IA
**Sem isso, pricing fica errado.**

**Simulação (suposição):**
- Conversação por texto: $0.001 por sessão (GPT mini)
- Pronúncia: $0.003 por análise (Whisper + LLM pequeno)
- TTS: $0.002 por frase
- Usuário Pro médio: 30 sessões convo/mês + 100 análises pronúncia + 300 frases

**Custo estimado por Pro/mês:** $0.30 + $0.30 + $0.60 = ~$1.20

**Margem com R$ 29,90:** 29,90 - 1,20 (IA) - ~5,00 (processamento/servidor/suporte) = ~$23,70/mês por usuário = 79% gross margin. Viável.

**Decisão:** Antes do kickoff, calcular o cenário real com APIs escolhidas. Se custo > 20% do revenue, redefinir limites ou modelo de monetização.

---

## 7. KPIs de Sucesso MVP

**Sem métricas, não existe critério de lançamento.**

### Recomendação

**Definir ANTES do kickoff:**

| KPI | Meta | Por Quê |
|-----|------|--------|
| **Retenção D7** | ≥ 40% | Indica hábito (ao menos voltam uma semana depois) |
| **Retenção D30** | ≥ 20% | Indica retenção de longo prazo |
| **Conversão Free→Pro** | ≥ 5% (mês 1), ≥ 10% (mês 3) | A value prop do Pro é clara o suficiente? |
| **DAU/MAU** | ≥ 30% | Indica uso regular (não só uma vez) |
| **Streak médio** | ≥ 5 dias | Hábito formado? |
| **Churn Pro mensal** | ≤ 10% | Pro viável economicamente? |
| **NPS** | ≥ 40 | Produto recomendável? |
| **Session time** | 10-20 min (alvo) | Está dentro da expectativa de usuário? |

### Saída
Document essas métricas no Confluence/Obsidian. **Lançamento = quando ≥ 4 dessas 8 métricas atingem a meta.**

---

## 8. Checklist de Validação Pre-Kickoff (Galvão)

Antes de 03/09, Galvão precisa confirmar:

- [ ] **Escopo:** Concorda com MVP revisado (saem conversação voz, pronúncia detalhada, chat professor)?
- [ ] **Algoritmo:** SM-2 ou FSRS para repetição espaçada (não contagem)?
- [ ] **Metas:** Novo scaling (A1 = 20-30, não 150)?
- [ ] **Validação:** Autoriza 5-10 entrevistas com potenciais usuários + protótipo Figma?
- [ ] **Conteúdo:** Há banco de frases ou parte do zero? Quem cria?
- [ ] **Respostas:** Responde as 9 perguntas críticas de Stephen (vol. usuários, banco de dados, professores, orçamento IA, etc.)?
- [ ] **KPIs:** Concorda com métricas de sucesso propostas?
- [ ] **Timeline:** 10-12 semanas é factível?
- [ ] **Budget:** Há orçamento confirmado?
- [ ] **Go/No-Go:** Decisão final de prosseguir com kickoff 03/09?

---

## 9. Próximos Passos

### Imediatamente (28-29/08)
1. Galvão lê esta recomendação + análise de Stephen
2. Galvão responde checklist acima
3. Jarvis agenda entrevistas com usuários

### Semana 1 (30/08-02/09)
1. Executar 5-10 entrevistas + protótipo Figma
2. Coletar insights
3. Galvão valida recomendações de escopo

### Kickoff (03/09)
1. ✅ Escopo definido
2. ✅ Algoritmo de repetição definido
3. ✅ Conteúdo inicial planeado
4. ✅ Tech Lead (Tony Stark?) começa arquitetura
5. ✅ Dev squad alocado

---

## 10. Risco de Não Seguir Essas Recomendações

Se prosseguirmos com PRD original (17 features, 10-12 semanas, sem validação):

**Cenário 1 — Atraso:**
- Semana 12 chega, faltam 4-5 features
- Lançamento empurrado para semana 18
- Budget estoura

**Cenário 2 — Qualidade comprometida:**
- Tudo lançado, mas com bugs
- Retenção D7 cai para 20% (esperado ≥ 40%)
- Necessário refactoring urgente em V1.1

**Cenário 3 — Falta de Validação:**
- Lançamos sem saber se usuários querem
- Ninguém usa (ou poucas pessoas)
- Descobrir tarde que conversação por voz não funciona bem
- Time desgastado

**Cenário 4 — Monetização Errada:**
- Custo de IA é maior que esperado
- Margem em 5%, não 80%
- Modelo de negócio quebrado
- Precisa reprecificar de emergência (churn em Pro)

---

## 11. Versão Alternativa — "Launch Even Faster"

Se Galvão quer lançar AINDA MAIS rápido (6-8 semanas):

**MVP Mini (6 semanas):**
- Cadastro + onboarding
- Flashcards + repetição espaçada SM-2
- Metas + progresso + streak
- Free/Pro (sem IA, só pagamento)
- Notificações

**V1.0 (sem IA no lançamento):**
- Depois, quando validar que o core funciona, adicionar IA

**Vantagem:** Risco drasticamente reduzido, lançamento rápido, aprende com usuários.

**Desvantagem:** Free é mais "fraco", menos diferenciação vs Duolingo/Busuu.

**Recomendação:** Só se o cliente insistir em speed over differentiation.

---

## Conclusão

O Wildream tem conceito sólido. A diferença entre sucesso e fracasso é:

1. **Honestidade sobre escopo** (o MVP de hoje é V1.0 em 12 semanas, não V2.0)
2. **Validação com usuários** (antes de dev, não depois)
3. **Algoritmo pedagógico correto** (repetição espaçada real)
4. **Métricas claras** (sabemos quando funciona)

Com essas 4 coisas, Wildream tem chance real de ser um produto que alunos de inglês vão amar.

Sem elas, é mais uma app abandoned em 6 meses.

---

**Pronto para kickoff quando Galvão confirmar.**

— Jarvis + Stephen Strange
28 de agosto de 2026
