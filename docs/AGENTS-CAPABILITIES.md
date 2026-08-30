# AGENT-CAPABILITIES.md — Matrix de Capacidades dos Agentes

> Referência rápida para análise de compatibilidade de ferramentas e integrações.
> Atualizar sempre que um agente ganhar novos acessos ou ferramentas.

---

## Capacidades Universais (todos os agentes)

| Capacidade | Ferramenta | Notas |
|---|---|---|
| Ler arquivos | `read` | Qualquer arquivo no workspace |
| Escrever arquivos | `write`, `edit` | Workspace e repos configurados |
| Executar shell | `exec` | Node, Python, CLI tools instalados no Mac mini |
| Buscar web | `web_search`, `web_fetch` | Sujeito a rate limits |
| Memória | `memory_search`, `memory_get` | MEMORY.md + daily notes |
| GitHub | `github__*` | Repos da Team-Iron-Solutions |
| Subagentes | `sessions_spawn` | Delegar tarefas paralelas |
| Cron | `cron` | Agendar tarefas periódicas |

---

## Matrix por Agente

### 1. Tony Stark 🔴 — Backend Node.js + Tech Lead
| Capacidade | ✅/❌ | Notas |
|---|---|---|
| exec (Node.js, npm, shell) | ✅ | Principal runtime |
| Leitura de código | ✅ | JS/TS, JSON, YAML |
| Code review via grafo (Graphify) | ✅ | Ideal para repos grandes |
| GitHub PRs e issues | ✅ | Tech Lead — aprovação de PRs |
| Deploy / CI | ✅ | Scripts de build e deploy |
| Banco de dados (SQL/NoSQL) | ✅ | Via scripts Node |
| APIs externas | ✅ | Com autorização do Galvão |

### 2. Bruce Banner 🟢 — Backend Python
| Capacidade | ✅/❌ | Notas |
|---|---|---|
| exec (Python 3.x, pip, venv) | ✅ | Python 3.9 disponível no Mac |
| Leitura de código | ✅ | Python, SQL, configs |
| Code review via grafo (Graphify) | ✅ | Ideal para data pipelines |
| Jupyter / notebooks | ✅ | Via exec |
| Análise de dados | ✅ | pandas, numpy, etc. |
| APIs ML (OpenAI, Anthropic) | ✅ | Com autorização |

### 3. Steve Rogers 🔵 — Arquiteto de Software
| Capacidade | ✅/❌ | Notas |
|---|---|---|
| Modelo: Sonnet (sempre) | ✅ | Decisões de arquitetura exigem reasoning |
| Leitura de código e docs | ✅ | Para análise de impacto |
| Graphify (visão de grafo) | ✅ | Ideal para mapear arquitetura de sistemas |
| Diagramas (Mermaid, PlantUML) | ✅ | Via canvas ou arquivos |
| Criação de ADRs | ✅ | Architecture Decision Records |
| exec | ✅ | Para validar dependências |

### 4. Stephen Strange 🟣 — Product Manager
| Capacidade | ✅/❌ | Notas |
|---|---|---|
| Modelo: Sonnet (decisões estratégicas) | ✅ | |
| Notion | ✅ | Via skill Notion |
| GitHub Issues / Projects | ✅ | Gestão de backlog |
| Graphify (escopo técnico) | ⚠️ | Útil ocasionalmente — entender impacto de features |
| exec | ✅ | Leitura de métricas, scripts de análise |
| Calendário | ✅ | Via sessão principal |

### 5. Visão 🔮 — Data Engineer / IA Aplicada
| Capacidade | ✅/❌ | Notas |
|---|---|---|
| exec (Python, SQL, shell) | ✅ | Data pipelines |
| Graphify | ✅ | Mapear relações entre datasets e modelos |
| APIs de ML | ✅ | Com autorização |
| Leitura de CSVs, JSONs, Parquet | ✅ | |
| Notebooks Jupyter | ✅ | Via exec |

### 6. Wanda Maximoff ✨ — Product Designer / UX
| Capacidade | ✅/❌ | Notas |
|---|---|---|
| Leitura de código (CSS, Dart, JSX) | ✅ | Para inspecionar design system |
| Graphify | ✅ | Mapear dependências de componentes UI |
| image_generate | ✅ | Mockups e conceitos visuais |
| canvas (HTML) | ✅ | Protótipos interativos |
| Figma (via web_fetch) | ⚠️ | Leitura apenas, sem escrita direta |
| exec | ✅ | Inspecionar tokens de design |

### 7. T'Challa 🐈⬛ — SRE Engineer
| Capacidade | ✅/❌ | Notas |
|---|---|---|
| exec (shell, systemd, launchctl) | ✅ | Infraestrutura do Mac mini |
| LaunchAgents / plist | ✅ | Gerenciamento de serviços |
| Logs e monitoramento | ✅ | tail, grep, análise de logs |
| Graphify | ⚠️ | Útil para mapear dependências de serviços |
| GitHub Actions / CI | ✅ | Pipelines de deploy |
| Certificados e segurança | ✅ | Com autorização explícita |

### 8. Scott Lang 🐜 — Flutter Developer
| Capacidade | ✅/❌ | Notas |
|---|---|---|
| exec (Flutter, Dart, pub) | ✅ | `flutter run`, `dart analyze` |
| Leitura de código Dart/Flutter | ✅ | |
| Graphify | ✅ | Ideal para mapear widget tree e providers |
| image (assets mobile) | ✅ | Análise de imagens/assets |
| Simuladores iOS/Android | ⚠️ | Via exec, depende de setup |
| pub.dev (web_fetch) | ✅ | Pesquisa de packages |

### 9. Natasha Romanoff 🕷️ — QA Engineer
| Capacidade | ✅/❌ | Notas |
|---|---|---|
| exec (jest, pytest, flutter test) | ✅ | Execução de testes |
| Leitura de código e testes | ✅ | |
| Graphify | ✅ | Mapear cobertura e impacto de mudanças |
| GitHub PRs (review) | ✅ | Quality gates |
| Relatórios de cobertura | ✅ | Via exec |

### 10. Peter Parker 🕸️ — Conteúdo / Social Media
| Capacidade | ✅/❌ | Notas |
|---|---|---|
| web_search / web_fetch | ✅ | Pesquisa de tendências |
| image_generate | ✅ | Assets visuais para posts |
| music_generate | ✅ | Jingles / áudio para reels |
| Graphify | ❌ | Não trabalha com código |
| GitHub | ⚠️ | Leitura apenas (changelog para conteúdo) |
| APIs de redes sociais | ⚠️ | Com autorização explícita do Galvão |

---

## Ferramentas Instaladas no Mac mini

```
Runtime:    Node.js v24.18.0 (nvm)
            Python 3.9 (system) + venvs
Shell:      zsh
CLI tools:  git, curl, flutter (verificar), dart
TTS:        edge-tts (pt-BR-AntonioNeural), ElevenLabs Otto
Audio:      afplay (sistema)
```

## Ferramentas Pendentes de Instalação

| Ferramenta | Para quem | Status |
|---|---|---|
| Graphify (`graphifyy`) | Tony, Bruce, Steve, Scott, Wanda, Natasha | ⏳ Pendente — Phase 4 |
| Flutter SDK | Scott Lang | ⚠️ Verificar instalação |

---

> **Regra:** Antes de dizer que uma ferramenta é incompatível com um agente,
> verificar esta matrix. Se o agente tem `exec`, provavelmente consegue usar
> qualquer CLI — a pergunta é se faz sentido, não se é tecnicamente possível.
