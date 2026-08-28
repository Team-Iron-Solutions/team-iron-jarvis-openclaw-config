# Wildream App — Project Hub

**Status:** 🟡 **ANÁLISE PRD EM PROGRESSO**  
**Data de Criação:** 28 de agosto de 2026  
**Cliente:** Wildream  
**PM:** Stephen Strange  
**Tech Lead:** Jarvis  

---

## 📋 O Projeto

**Wild Dream App** é um aplicativo mobile de aprendizagem de inglês baseado em:
- Repetição espaçada (flashcards inteligentes)
- Prática de frases reais em inglês
- IA para conversação, pronúncia e vocabulário
- Suporte humano via professores (versão Pro)

**Modelo:** Free (essencial) + Pro (IA + suporte)  
**Plataformas:** iOS + Android (cross-platform)  
**Timeline:** A definir (provavelmente 8-12 semanas para MVP)

---

## 🎯 Objetivos Principais

1. Aumentar frequência de estudo dos alunos
2. Aplicar repetição espaçada para retenção
3. Permitir criar/revisar banco próprio de frases
4. Usar IA para developing speaking, vocabulário, feedback
5. Criar experiência Pro com valor claro
6. Gerar dados de engajamento para administração
7. Base tecnológica escalável para B2B futuro

---

## 👥 Públicos

| Perfil | Features | Objetivo |
|--------|----------|----------|
| **Aluno Free** | Flashcards, repetição espaçada, progresso | Estudar grátis, criar hábito |
| **Aluno Pro** | +IA (áudio, pronúncia, conversação, vocabulário), suporte professor | Praticar com IA, feedback, suporte |
| **Professor** | Chat de suporte, criação de tarefas | Atender e motivar alunos Pro |
| **Admin** | Dashboard completo (usuários, planos, métricas) | Gerenciar operação |

---

## 🚀 MVP — Funcionalidades Críticas

### Free (Lançamento)
- ✅ Cadastro/login
- ✅ Teste de nível CEFR (opcional)
- ✅ Flashcards com repetição espaçada
- ✅ Criar/editar frases
- ✅ Traduções
- ✅ Metas diárias
- ✅ Progresso/histórico
- ✅ Troféus + streaks

### Pro (Lançamento +)
- ✅ Áudio gerado por IA
- ✅ Análise de pronúncia (palavra por palavra)
- ✅ Feedback gramatical
- ✅ Conversação por texto com IA
- ✅ Conversação por voz com IA
- ✅ Geração de vocabulário
- ✅ Tarefas do professor
- ✅ Suporte via chat com professor

---

## 💰 Monetização

| Plano | Preço (Sugerido) | Ajustável |
|-------|------------------|-----------|
| Free | R$ 0 | — |
| Pro Mensal | R$ 29,90 | ✓ |
| Pro Anual | R$ 299,00 | ✓ |

**Gateway:** Cartão + Mercado Pago  
**Controle:** Configurável no painel admin  
**Proteção:** Franquias de IA para manter margem

---

## 🤖 Componentes de IA (Pro)

### Conversação
- Cenários: Job Interview, Travel, Restaurant, Casual, etc.
- Contexto: IA conduz conversas realistas
- Feedback: Correção durante a conversa (não punitivo)
- Nível: Configurável pelo aluno

### Pronunciação & Gramática
- Análise palavra por palavra
- Identifica dificuldades
- Feedback orientado para erros relevantes
- Sem exigir perfeição nativa

### Vocabulário
- Geração por tema (Food, Business, Travel, etc)
- Tradução + áudio
- Futuro: Integração automática em flashcards

---

## 🎮 Gamificação

- ✗ Sem ranking entre alunos (MVP)
- ✓ Troféus individuais
- ✓ Streaks (dias consecutivos)
- ✓ Conquistas (por quantidade, desafios)
- ✓ Pontuação/XP (para Pro)

---

## 📊 Painel Administrativo

**Visibilidade:**
- Total de alunos, Free vs Pro
- Status de pagamento
- Quantidade de professores
- Frases revisadas, tempo de uso
- Engajamento, frequência
- Uso de recursos de IA
- Parâmetros editáveis (metas, regras, preços)

---

## 🛣️ Roadmap Futuro: Wild Dream for Business

Arquitetura preparada para B2B:
- Contas corporativas (empresa + RH)
- Funcionários vinculados
- Trilhas por função (Sales, Customer Service, Leadership, Tech, Meetings)
- Relatórios por equipe/departamento
- IA especializada por contexto profissional
- Licenças por número de usuários

---

## 📝 Princípios de Design

- **Mobile-first**
- **Visual:** Moderno, premium, limpo
- **UX:** Poucos elementos por tela
- **Ação:** Principal sempre evidente
- **Simplicidade:** Aluno não precisa entender o algoritmo
- **Feedback IA:** Claro, acionável, não punitivo
- **Diferenciação:** Free útil, Pro claramente superior

---

## ⚙️ Diretrizes Técnicas

**Cross-platform:** iOS + Android (Flutter recomendado)

**Backend:**
- Autenticação segura
- Banco de dados (frases, histórico, usuários)
- Engine de repetição espaçada
- Integração com IA (audio, conversação, feedback)
- Sistema de pagamentos (Mercado Pago)
- Notificações (push, webhooks)

**Arquitetura:**
- Sistema de permissões (Free/Pro/Professor/Admin)
- Registro de eventos (revisão, erro/acerto, áudio, etc)
- Escalável para B2B futuro
- Segurança: dados, consentimento, credenciais, pagamentos

---

## 🔍 Decisões Pendentes

- [ ] Metas diárias para B2, C1, C2
- [ ] Limite mensal de IA para Pro
- [ ] Teste de nível: interno vs externo?
- [ ] Provedor de IA/voz (OpenAI? Google? Local?)
- [ ] Gateway de pagamento final
- [ ] Política de cancelamento/renovação
- [ ] Identidade visual final

---

## ✅ Critério de Sucesso MVP

### Pergunta Norteadora
*"Se um aluno abre o app pela manhã, ele deve:*
1. *Saber imediatamente o que estudar*
2. *Conseguir revisar frases sem fricção*
3. *Perceber seu progresso*
4. *Ter uma razão clara para voltar amanhã"*

---

## 📚 Documentação

| Arquivo | Status | Link |
|---------|--------|------|
| **PRD Completo** | ✅ | `WILDREAM_APP_PRD_V1.0.md` |
| **Análise PM** | 🟡 Aguardando | `PRD-Analysis-Response.md` |
| **Tech Spec** | ⏳ Futuro | `TECHNICAL-SPECIFICATION.md` |
| **Design System** | ⏳ Futuro | `DESIGN-SYSTEM.md` |
| **Sprint Planning** | ⏳ Futuro | `SPRINT-PLANNING.md` |

---

## 📅 Timeline

| Data | Milestone |
|------|-----------|
| **28/08** | ✅ PRD finalizado, request análise |
| **02/09** | 🟡 Análise PM esperada |
| **02-03/09** | ⏳ Galvão valida recomendações |
| **03/09+** | ⏳ Kickoff técnico (arquitetura, sprints) |
| **~10-12 semanas** | ⏳ MVP lançamento (estimado) |

---

## 👥 Equipe

| Papel | Pessoa | Responsabilidade |
|-------|--------|------------------|
| **Cliente** | Wildream | Definições, validações |
| **PM** | Stephen Strange | Análise, priorização, roadmap |
| **Tech Lead** | Jarvis | Arquitetura, decisões técnicas |
| **Dev Lead** | Tony Stark (estimado) | Implementação, code review |

---

## 🔗 Referências Rápidas

**Arquivo original:** `Wild_Dream_App_PRD_v1.0.docx`  
**Diretório:** `/Users/teamironsolutions/.openclaw/workspace/projects/wildream/`  
**Obsidian:** `Wildream-Project-Hub.md`  
**MEMORY.md:** Seção "Wildream App Project" (long-term memory)

---

## 📝 Notas

- PRD extraído e convertido para markdown (28/08)
- Aguardando análise profunda de Stephen Strange
- Após análise, será necessário validar decisões técnicas pendentes
- Timeline agressiva (8-12 semanas) pode requerer ajustes após descoberta

---

_Hub do projeto criado por Jarvis • 28 de agosto de 2026_  
_Última atualização: 28/08/2026 11:26_
