# 📋 Pendências — Team Iron Solutions (29 agosto 2026)

**Status Geral:** 🟡 **Em execução normal**  
**Blockers críticos:** 0  
**Timeline visibility:** 100% (até kickoff 03/09)

---

## 🔴 CRÍTICAS (Antes de 03/09)

### 1. ✋ Galvão: Responder 9 Perguntas Wildream
**Deadline:** 02/09 18:00 (4 dias)  
**Tempo:** ~30 minutos  
**Impacto:** BLOQUEADOR — define scope final de Wildream MVP  
**Arquivo:** `obsidian-vault/Projetos/Wildream/04-9-Perguntas-Criticas.md`

**As 9 perguntas:**
1. Volume de usuários esperado no lançamento?
2. Banco de frases existente ou start from zero?
3. Quantos professores + SLA?
4. Orçamento máximo/mês para IA?
5. App é complemento ao curso ou standalone?
6. Houve validação com usuários (entrevistas, protótipo)?
7. Chat com professores: síncrono ou assíncrono?
8. Design system / Figma já pronto?
9. B2B é intenção real ou especulativa?

**Por que importa:**
- Cada pergunta impacta timeline, custo, ou escopo
- Respostas desbloqueiam kickoff técnico 03/09
- Sem respostas, team fica com incerteza

---

### 2. ⚡ Stephen Strange: Validar Respostas Galvão
**Dependency:** Após Galvão responder (02/09)  
**Tempo:** 30 minutos  
**Entrega:** Validação + recomendações  
**Por que:** Confirma que scope é realista para 10-12 semanas

---

### 3. 🧪 User Validation (Opcional mas Recomendado)
**Deadline:** 02/09 23:59  
**Tempo:** 2-3 horas (5-10 entrevistas)  
**Dono:** Jarvis + Galvão  
**Impacto:** Valida desempenho do MVP antes de dev

**O quê testar:**
- Protótipo Figma das 5 features principais
- Value proposition ("aumentar frequência, não substituir")
- Pricing (R$ 29,90/mês aceitável?)
- Free tier (suficiente pra engajar?)

**Por que:** Reduz risco de MVP miss target market

---

### 4. 📅 Team Alignment Meeting
**Quando:** 02/09 evening ou 03/09 morning (09:00)  
**Duração:** 1 hora  
**Participants:** Galvão, Jarvis, Stephen Strange, Tony Stark, Steve Rogers, Scott Lang, Wanda, Natasha  
**Agenda:**
- Confirmar scope final (baseado em respostas Galvão)
- Validar timeline (10-12 semanas realista?)
- Alocar recursos (quem faz o quê)
- Comunicar blockers/risks
- Lock kickoff para 03/09 14:00

---

### 5. 🎯 KICKOFF TÉCNICO WILDREAM
**Quando:** 03/09 14:00 GMT-3 ✅ **LOCKED**  
**Duração:** 2 horas  
**Dono:** Tony Stark (Tech Lead)  
**Agenda:**
- Revisão arquitetura (Steve Rogers)
- Timeline detalhada por semana (Tony)
- Allocation final (quem, quando, quanto)
- Tech decisions (SM-2 vs FSRS, design system, stack)
- Primeiro sprint (semana 1)

**Status:** Pronto quando acima ✅

---

## 🟠 ALTOS (Próximas 2 semanas)

### 6. 💻 Wildream Development Kick (03/09+)
**Fase 1:** Fundação (03-05/09)  
**O quê:**
- [ ] Setup repositórios (backend Node/Python, frontend Flutter)
- [ ] Database schema (PostgreSQL)
- [ ] CI/CD pipelines (GitHub Actions)
- [ ] Auth system (email + SSO)
- [ ] Onboarding flow

**Owner:** Tony Stark + Steve Rogers  
**ETA:** Semana 1 (03-05/09) ✅

---

### 7. 📐 Design System Finalize (Wanda)
**Deadline:** 06/09 09:00  
**O quê:**
- [ ] Figma finalizado (5 screens principais)
- [ ] Component library pronto
- [ ] Design tokens definidos
- [ ] Mobile specs (safe areas, responsiveness)

**Owner:** Wanda Maximoff  
**Impacto:** Scott Lang bloqueia sem isso (semana 2)

---

### 8. 🔧 Phase 4 Sprint 2 (Graphify)
**Quando:** 27-29/08 (ongoing)  
**O quê:** Tony Stark integra graphify com código real  
**Status:** 🟡 Em progresso  
**ETA:** Pronto para Tier 1 rollout (30/08-03/09)

---

## 🟡 MÉDIOS (Agosto-Setembro)

### 9. 📊 Monitoring Phase 3 + Phase 4
**Timeline:** 16/08-ongoing  
**O quê:**
- [ ] KPI dashboard funcional
- [ ] Alerts (caution/warning/critical)
- [ ] Daily checklist rodando
- [ ] Metrics validadas por 7 dias

**Owner:** T'Challa + Jarvis  
**Status:** Phase 3 ✅ Validado, Phase 4 🟡 Pending

---

### 10. 🗣️ Agent Communication Tests
**Quando:** After Phase 4 Tier 1 rollout  
**O quê:** Testar workflows entre agentes
- [ ] Tony ↔ Bruce code review workflow
- [ ] Tony ↔ Steve architecture escalation
- [ ] Stephen ↔ Wanda product design feedback

**Owner:** Jarvis  
**Impact:** Validar inter-agent collaboration

---

### 11. 📱 HUD v5 Deployment
**Status:** 🟡 PR #4 aberto, em revisão  
**O quê:**
- [ ] Merge feature/hud-ws-stream-bridge-idle
- [ ] Test WS conecta corretamente
- [ ] Deploy v5 como padrão (substituir v2)
- [ ] Validar com voz + visualização

**Owner:** Jarvis  
**ETA:** Before 03/09

---

## 🟢 BAIXOS (Later — Nice-to-have)

### 12. 🎓 Squad Training Sessions
**Quando:** After kickoff (03/09+)  
**O quê:** Cada agente familiarizado com playbook + workflow  
**Owner:** Jarvis  
**Time per agent:** 30 min

---

### 13. 📚 Inter-Agent Workflow Documentation
**Quando:** September  
**O quê:** Documentar patterns de collaboration (Tony+Bruce, Stephen+Wanda, etc)  
**Owner:** Jarvis  
**Impact:** Referência para future projects

---

### 14. 🔐 Gateway Security Hardening
**Deadline:** Nenhum (nice-to-have)  
**O quê:**
- [ ] Movr gateway.auth.token → SecretRef
- [ ] Rate limiting ativo
- [ ] TLS opcional para external access

**Owner:** T'Challa  
**Time:** 2-3 horas

---

### 15. 🎙️ Voice Clone (Eduardo Borgerth)
**Deadline:** Nenhum (future enhancement)  
**O quê:** Clonar voz profissional do dublador BR de JARVIS  
**Owner:** Jarvis (coordenação)  
**Cost:** Plano Creator ElevenLabs + áudios limpos  
**Status:** 📋 Planned, not urgent

---

### 16. 💬 Messaging Channels Integration
**Deadline:** Nenhum (future)  
**O quê:** WhatsApp, Telegram, Discord, Slack  
**Owner:** T'Challa + Jarvis  
**Status:** 📋 Planned, not urgent

---

## 📊 Resumo por Timeline

### 🔴 CRÍTICAS (Próximos 4 dias — até 02/09)
```
[ ] Galvão responde 9 perguntas (30/08-02/09)
[ ] Stephen Strange valida respostas (02/09)
[ ] User validation (opcional, 30/08-02/09)
[ ] Team alignment meeting (02/09 eve or 03/09 morning)
[ ] Kickoff técnico (03/09 14:00) ✅ LOCKED
```

### 🟠 ALTOS (Semana 1 dev — 03-09/09)
```
[ ] Wildream dev Fase 1 inicia (03/09)
[ ] Design system finalize (06/09)
[ ] Phase 4 Sprint 2 complete (29/08-03/09)
[ ] HUD v5 deploy (before 03/09)
```

### 🟡 MÉDIOS (Setembro+)
```
[ ] Phase 4 Tier 1 rollout (03/09+)
[ ] Monitoring dashboards (ongoing)
[ ] Agent communication tests (after rollout)
```

### 🟢 BAIXOS (September+)
```
[ ] Squad training
[ ] Inter-agent docs
[ ] Security hardening (nice-to-have)
[ ] Voice clone (future)
[ ] Messaging channels (future)
```

---

## ⚠️ Riscos & Assumções

### Risk 1: Delay em respostas de Galvão
**Se:** Respostas chegam depois de 02/09 evening  
**Então:** Kickoff atrasa para 10/09, MVP atrasa 1 semana  
**Mitigation:** Galvão já tem docs, 30 min pra responder

### Risk 2: Validação com usuários descobre MVP miss
**Se:** Usuários pedem features que cortamos para scope  
**Então:** Decidir: addback feature ou stick com MVP  
**Mitigation:** Documentação clara de "por quê foi cortado"

### Risk 3: Design system não pronto no prazo
**Se:** Wanda entrega design depois de 06/09  
**Então:** Scott bloqueia (não tem specs)  
**Mitigation:** Começar design 48h antes (01/09 idealmente)

### Risk 4: Phase 4 encontra problema técnico
**Se:** Graphify falha com repo grande  
**Então:** Rollback para Phase 3, Phase 4 vira Phase 2.5  
**Mitigation:** Testes extensivos em Sprint 2 (27-29/08)

---

## 📞 Quem Faz O Quê

| Owner | Responsabilidade | Status |
|-------|------------------|--------|
| **Galvão** | Responder 9 perguntas | ⏳ TODO (30/08-02/09) |
| **Stephen Strange** | Validar respostas | ⏳ TODO (02/09) |
| **Jarvis** | Coordenar user validation | 🟡 Pronto pra executar |
| **Tony Stark** | Tech lead Wildream + Phase 4 | 🟡 Pronto |
| **Steve Rogers** | Arquitetura Wildream | ✅ Pronto |
| **Wanda Maximoff** | Design system Wildream | 🟡 Pronto (start 01/09) |
| **Scott Lang** | Flutter Wildream | ✅ Pronto (start semana 2) |
| **Bruce Banner** | Backend Python | ✅ Pronto |
| **Natasha Romanoff** | QA Wildream | ✅ Pronto |
| **T'Challa** | Infra/DevOps | ✅ Pronto |
| **Visão** | Analytics/Data | ✅ Pronto |
| **Peter Parker** | Launch content (later) | ✅ Pronto |

---

## ✅ Checklist de Go/No-Go para Kickoff 03/09

- [ ] Galvão respondeu 9 perguntas
- [ ] Stephen validou respostas
- [ ] Scope final bloqueado (sem mais mudanças)
- [ ] Timeline realista para 10-12 semanas confirmada
- [ ] Team allocation final aprovada
- [ ] Design system kickoff agendado (01/09)
- [ ] Repositórios criados (ou ready to create)
- [ ] CI/CD template pronto
- [ ] QA plan approved
- [ ] ✅ **READY TO KICKOFF 03/09 14:00**

---

## 💾 Referências

**Para Galvão:** `obsidian-vault/Projetos/Wildream/04-9-Perguntas-Criticas.md`  
**Para Stephen:** `obsidian-vault/Projetos/Wildream/PRD-Analysis.md`  
**Timeline:** `obsidian-vault/Projetos/Wildream/05-Cronograma.md`  
**Overall:** `RELATORIO-FINAL-OBSIDIAN-29-08-2026.md`

---

**Status Geral:** 🟡 **Executando conforme plano**  
**Blockers Críticos:** 0  
**Next Blocker Window:** Respostas Galvão (30/08-02/09)

🚀 **Tudo pronto para kickoff 03/09!**
