# 👥 Clients — Padrões por Cliente

Cada pasta aqui representa **um cliente** com suas próprias regras, stack tecnológica e padrões de codificação.

Os agentes **lêem esses arquivos obrigatoriamente** antes de executar qualquer tarefa para um cliente.

---

## Estrutura

```
clients/
├── README.md                   # Este arquivo
├── _TEMPLATE/                  # Template para novos clientes
│   ├── STANDARDS.md            # Padrões de codificação
│   ├── TECH-STACK.md           # Tecnologias e versões
│   ├── CODING-RULES.md         # Regras específicas obrigatórias
│   └── CONTEXT.md              # Contexto do projeto
│
├── _EXEMPLO-CLIENTE/           # Exemplo preenchido
│   └── ...
│
├── cliente-acme/               # Seu primeiro cliente real
│   └── ...
└── cliente-xyz/
    └── ...
```

---

## Onboarding de novo cliente

```bash
# 1. Copia o template
cp -r clients/_TEMPLATE clients/NOME-DO-CLIENTE

# 2. Edita cada arquivo com as regras do cliente
# 3. Faz commit
# 4. Agentes já respeitam automaticamente via protocolo de dispatch
```

---

## Como os agentes usam isso

Ver: `docs/TASK-DISPATCH-PROTOCOL.md`

A regra básica: **toda task enviada para um agente deve incluir o caminho do cliente**.
O agente lê o STANDARDS.md antes de qualquer execução.
