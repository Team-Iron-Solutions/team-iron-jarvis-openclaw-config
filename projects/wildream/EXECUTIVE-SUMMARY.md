# Wildream App — Executive Summary

**Para:** Galvão  
**De:** Jarvis (Tech Lead) + Stephen Strange (PM)  
**Data:** 28 de agosto de 2026  
**Status:** ✅ ANÁLISE COMPLETA — AGUARDANDO DECISÃO  

---

## Em 30 Segundos

**O Wildream tem um conceito pedagógico sólido** (repetição espaçada + hábito). **Mas o PRD original descreve ~6-9 meses de trabalho como se fosse 10-12 semanas.**

**Recomendação:** Cortar ~5 features, validar com usuários (5-10 entrevistas), e lançar um MVP focado que funciona bem — em vez de um MVP com tudo que não funciona em nada.

**Decisão:** Segue em frente com kickoff 03/09 ou pausa para reavaliar?

---

## Análise de Stephen Strange — Os 3 Riscos Críticos

Stephen fez análise profunda do PRD e identificou 3 riscos que precisam ser desarmados antes de qualquer kickoff:

### 🔴 Risco 1: Escopo Irreal

**Problema:** O PRD lista 17 features de prioridade, incluindo conversação por voz, pronúncia palavra-a-palavra, suporte de professores, e admin completo — tudo em 10-12 semanas.

**Realidade técnica:** Isso é um produto de 6-9 meses com squad experiente. 10-12 semanas é possível apenas se cortarmos 4-5 features e foco no core.

**Fix:** MVP revisado com 12 features (conversação por voz sai, conversação por texto fica). Pronúncia detalhada vai para V1.1. Chat com professor vira ticket assíncrono.

**Impacto:** Risco de atraso cai 70%. MVP no prazo: provável vs possível.

### 🔴 Risco 2: Algoritmo de Repetição Espaçada Está Errado

**Problema:** PRD define repetição como "próximas 10/20/30/50 frases" — isso é frequência dentro da sessão, não repetição espaçada real.

**Realidade pedagógica:** Repetição espaçada real é SM-2 ou FSRS, baseada em **dias/horas**, não contagem de frases. Um usuário que faz 200 flashcards numa hora e para por 3 dias nunca verá as frases no momento certo.

**Impacto:** O produto pode não entregar a value proposition (retenção de vocabulário via repetição espaçada).

**Fix:** Usar SM-2 (simples, open-source) no MVP. FSRS em V1.2 se quiser otimização posterior.

### 🔴 Risco 3: Meta de A1 (150 frases/dia) Mata Engajamento

**Problema:** Um iniciante completo consegue fazer 20-40 frases em 15-20 minutos, não 150.

**Resultado:** Usuário abre o app, vê que precisa fazer 150 frases/dia para cumprir a meta, realiza que não consegue em 1 dia e abandona.

**Impacto:** Churn precoce em D2-D3. Usuário que mais precisa de encorajamento é o primeiro a desistir.

**Fix:** Novo scaling: A1 = 20-30 frases/dia (10-15 min), A2 = 30-50, B1 = 50-80. Pedagógico e alcançável.

---

## MVP Revisado — O Que Entra, O Que Sai

### ✅ MVP (Entra no lançamento — 10-12 semanas)

**Fundação:** Cadastro, login, onboarding, teste de nível, banco de frases  
**Core:** Flashcards, repetição espaçada SM-2, metas diárias, metas, progresso, streak  
**Engajamento:** Troféus básicos, notificações push  
**Monetização:** Free/Pro, pagamento Mercado Pago  
**IA Pro:** Áudio das frases (TTS), conversação por TEXTO, pronúncia básica  
**Admin:** Mínimo (usuários, planos, receita, parâmetros)  
**Suporte:** Ticket assíncrono (formulário → resposta email 24-48h)

**Total:** ~12 features focadas no core.

### ❌ V1.1 (Sai do MVP)

- Conversação por VOZ (complexidade alta, custo alto)
- Pronúncia palavra-a-palavra (detalhada)
- Geração de vocabulário por IA
- Chat com professores (fila real, interface)
- Admin com dashboards completos

---

## As 5 Decisões Não-Negociáveis Antes de Kickoff

Se Galvão decide prosseguir, estas são as 5 decisões que precisam estar fechadas **antes de 03/09**:

1. **Escopo:** Concorda em cortar conversação por voz, pronúncia detalhada, e chat professor (MVP)?
2. **Algoritmo:** Usar SM-2 para repetição espaçada (baseado em tempo, não contagem)?
3. **Metas:** Revisar para A1 = 20-30 frases/dia (pedagógico, não 150)?
4. **Validação:** Autoriza 5-10 entrevistas com potenciais usuários + protótipo Figma?
5. **Conteúdo:** Há banco de frases existente ou parte do zero? Quem cria?

---

## As 9 Perguntas Críticas para Galvão Responder

Stephen também listou 9 perguntas que precisam de resposta antes do kickoff:

1. **Volume esperado:** Quantos usuários no lançamento? (Isso impacta infraestrutura e custo de IA)
2. **Conteúdo:** Há banco de frases da Wildream ou parte do zero?
3. **Professores:** Quantos estarão disponíveis no lançamento? Qual SLA de resposta?
4. **Orçamento IA:** Qual é o máximo que pode gastar/mês em APIs de IA?
5. **Modelo:** App é complemento ao curso ou standalone?
6. **Validação:** Houve entrevistas com usuários? Protótipo testado?
7. **Suporte:** Chat com professor é síncrono (imediato) ou assíncrono (24h)?
8. **Design:** Design system / Figma já pronto?
9. **B2B:** Wild Dream for Business é intenção real de negócio ou especulativa?

---

## Recomendações de Priorização

**Por nível de urgência:**

### 🔴 CRÍTICO (antes do kickoff)
- Cortar escopo (conversação voz, pronúncia detalhada, professores chat)
- Definir algoritmo de repetição espaçada (SM-2)
- Revisar metas diárias (A1 = 20-30, não 150)
- Fazer validação com usuários (5-10 entrevistas + protótipo)
- Galvão responder as 9 perguntas críticas
- Definir KPIs de sucesso (retenção D7 ≥ 40%, conversão Free→Pro ≥ 5%, etc.)

### 🟠 ALTO (durante kickoff)
- Definir provedor de IA (OpenAI recomendado, local/Google em V1.1)
- Fazer spike: integração Mercado Pago + Flutter
- Definir teste de nível (interno vs externo)
- Planejar conteúdo inicial (200 frases/nível CEFR)
- Calcular franquia de IA (custo por usuário Pro)

### 🟡 MÉDIO (semana 1 dev)
- Design system / Figma finalizado
- Onboarding completo prototipado
- Banco de dados inicial começado

---

## Cronograma Recomendado

| Data | Milestone | Owner |
|------|-----------|-------|
| **28-29/08** | Galvão lê análise + responde 9 perguntas | Galvão |
| **30/08-02/09** | Entrevistas com usuários + validação protótipo | Jarvis + Galvão |
| **02/09** | Stephen valida aprendizados de entrevistas | Stephen |
| **03/09** | Kickoff técnico (escopo, stack, sprints) | Time |
| **03-05/09** | Semana 1: Arquitetura + CRUD base | Tony Stark (Tech Lead estimado) |
| **06-12/09** | Semanas 2-3: Core (flashcards + repetição SM-2) | Squad |
| **13-16/09** | Semanas 4-5: Monetização + Free/Pro | Squad |
| **17-19/09** | Semana 6: IA (conversação texto, pronúncia básica) | Squad |
| **20-23/09** | Semana 7: Admin + integrações | Squad |
| **24-26/09** | Semana 8: QA + correções | Squad |
| **27-28/09** | Semana 9: Ajustes finais + stores (Apple/Google) | Squad |
| **~29/09** | 🚀 MVP Lançamento | Squad |

**Timeline total:** ~4 semanas de análise/validação + 9 semanas de dev = 13 semanas até lançamento.

---

## Risco de Não Seguir Essas Recomendações

| Cenário | Probabilidade | Impacto | Mitigação |
|---------|---------------|--------|-----------|
| **Atraso** (faltam features na semana 12) | 70% | Alto (reputa, custo) | Cortar escopo agora |
| **Qualidade baixa** (bugs, UX ruim) | 60% | Alto (retenção cai) | Validação com usuários |
| **Algoritmo errado** (sem retenção real) | 40% | Crítico (produto falha) | Usar SM-2 confirmado |
| **Monetização quebrada** (custo IA > margem) | 30% | Alto (modelo inviável) | Definir franquia IA agora |
| **Ninguém quer** (sem PMF) | 20% (baixo) | Crítico (produto morre) | Validação com usuários |

---

## Recomendação Final

### ✅ Segue em Frente? SIM, com Condições

**O Wildream tem conceito bom.** A diferença entre sucesso e fracasso não é tecnologia — é disciplina:

1. ✅ **Ser honesto sobre escopo** (MVP de 12 semanas, não V2.0 em 12 semanas)
2. ✅ **Validar com usuários** (antes de dev, não depois)
3. ✅ **Algoritmo pedagógico correto** (SM-2, não contagem)
4. ✅ **Métricas claras** (quando sabemos que funcionou)

### 📋 Checklist de Aprovação (Galvão)

Antes de confirmar kickoff 03/09:

- [ ] Leu análise completa de Stephen Strange
- [ ] Leu recomendações de kickoff
- [ ] Concorda com MVP revisado (sem conversação voz, pronúncia detalhada, chat professor)
- [ ] Respondeu as 9 perguntas críticas
- [ ] Autorizou validação com usuários (5-10 entrevistas)
- [ ] Definiu KPIs de sucesso
- [ ] Confirmou timeline (4 semanas análise + 9 semanas dev)
- [ ] Confirmou orçamento
- [ ] ✅ **GO para kickoff 03/09**

---

## Documentos Complementares

| Documento | Localização | O Quê Contém |
|-----------|-------------|--------------|
| **PRD Completo** | `WILDREAM_APP_PRD_V1.0.md` | Visão original, todas as features, roadmap |
| **Análise Crítica** | `PRD-Analysis-Response.md` | Análise de Stephen, riscos, recomendações |
| **Recomendações Kickoff** | `KICKOFF-RECOMMENDATIONS.md` | Decisões específicas, MVP revisado, checklists |
| **Project Hub (Obsidian)** | `obsidian-vault/Projetos/Wildream-Project-Hub.md` | Hub central do projeto, histórico, timeline |

---

## Próximos Passos

1. **Galvão lê tudo** (30 min)
2. **Galvão responde checklist** (15 min)
3. **Se GO:** Jarvis agenda entrevistas com usuários (30/08-02/09)
4. **Se NOT YET:** Galvão indica o quê precisa ser revisto

---

## Contato

Qualquer dúvida sobre a análise: pergunte.

Qualquer dúvida técnica: Tony Stark (quando alocado).

Qualquer dúvida de produto: Stephen Strange.

---

**Pronto para a conversa quando Galvão voltar do treino.**

— Jarvis  
28 de agosto de 2026
