# Deployment Guide — OpenClaw Multi-Servidor

Guia completo para instalar o OpenClaw da Team Iron Solutions em qualquer servidor, incluindo VPS Linux (Hostinger, DigitalOcean, AWS EC2, etc.) e macOS.

---

## Arquitetura: Central Brain + Remote Nodes

```
┌──────────────────────────────────────────────────────┐
│           SERVIDOR CENTRAL (VPS ou Mac mini)          │
│                                                       │
│  OpenClaw Gateway :18789                              │
│  ├── Jarvis (orquestrador)                            │
│  ├── Tony Stark (Backend Node.js)                     │
│  ├── Scott Lang (Flutter)                             │
│  └── ... (todos os agentes)                          │
│                                                       │
│  workspace/clients/                                   │
│  ├── cliente-a/ → STANDARDS.md, TECH-STACK.md         │
│  ├── cliente-b/ → ...                                 │
│  └── ...                                              │
└───────────────┬──────────────────────────────────────┘
                │ OpenClaw Node Protocol
      ┌─────────┼──────────────────┐
      ▼         ▼                  ▼
 ┌─────────┐ ┌─────────┐ ┌─────────┐
 │ Mac/Win │ │  Linux  │ │  Mac    │
 │ Cliente │ │ Cliente │ │ Cliente │
 │    A    │ │    B    │ │    C    │
 │  repo   │ │  repo   │ │  repo   │
 └─────────┘ └─────────┘ └─────────┘
```

**O cérebro (agentes, memória, sessões) fica no servidor central.
As máquinas dos clientes são apenas executores.**

---

## Opção A: VPS Linux (Hostinger, DigitalOcean, etc.)

### Requisitos mínimos

| Recurso | Mínimo | Recomendado |
|---|---|---|
| RAM | 2 GB | 4-8 GB |
| CPU | 2 vCPU | 4 vCPU |
| Disco | 20 GB | 40 GB SSD |
| OS | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |
| Node.js | 20 LTS | 20 LTS |

### Passo a passo

#### 1. Criar VPS

Na Hostinger (ou outro provider):
- Ubuntu 22.04 LTS
- Plano KVM2+ (8 GB RAM ideal para 4+ clientes simultâneos)
- Anote o IP do servidor

#### 2. Configurar acesso SSH

```bash
# No seu Mac local
ssh-keygen -t ed25519 -C "team-iron@vps"
ssh-copy-id root@SEU_IP_VPS

# Teste
ssh root@SEU_IP_VPS
```

#### 3. Configuração inicial do servidor

```bash
# No VPS, como root
apt update && apt upgrade -y

# Criar usuário dedicado
adduser openclaw
usermod -aG sudo openclaw

# Configurar SSH para o novo usuário
mkdir -p /home/openclaw/.ssh
cp ~/.ssh/authorized_keys /home/openclaw/.ssh/
chown -R openclaw:openclaw /home/openclaw/.ssh
chmod 700 /home/openclaw/.ssh

# Mudar para usuário openclaw
su - openclaw
```

#### 4. Clonar e instalar

```bash
# Como usuário openclaw
git clone https://github.com/Team-Iron-Solutions/team-iron-jarvis-openclaw-config.git
cd team-iron-jarvis-openclaw-config
chmod +x setup.sh
./setup.sh
```

#### 5. Configurar secrets

```bash
nano ~/.openclaw/openclaw.json
# Preencher:
# - OPENROUTER_API_KEY ou ANTHROPIC_API_KEY
# - OPENCLAW_GATEWAY_TOKEN (string segura qualquer)
# - GITHUB_TOKEN
```

#### 6. Abrir porta no firewall

```bash
sudo ufw allow OpenSSH
sudo ufw allow 18789/tcp    # OpenClaw Gateway
sudo ufw enable
sudo ufw status
```

#### 7. Verificar serviço

```bash
sudo systemctl status openclaw-gateway
journalctl -u openclaw-gateway -f

# Teste local
curl http://localhost:18789/health
```

#### 8. Acessar remotamente

```bash
# Do seu Mac local
curl http://SEU_IP_VPS:18789/health
```

> 🔐 **Segurança:** Em produção, coloque o Gateway atrás de um reverse proxy (nginx) com HTTPS/TLS. Ver seção "Segurança Avançada".

---

## Opção B: Mac mini (setup atual)

O setup existente já está configurado. Para replicar em um novo Mac:

```bash
git clone https://github.com/Team-Iron-Solutions/team-iron-jarvis-openclaw-config.git
cd team-iron-jarvis-openclaw-config
chmod +x setup.sh
./setup.sh
```

O script detecta macOS automaticamente e instala o LaunchAgent.

---

## Conectar Máquinas dos Clientes como Nodes

Cada máquina de cliente se conecta ao servidor central como um **node OpenClaw**.

### No servidor central (obter pairing code)

```bash
# Gerar código de pairing para o node do cliente
openclaw nodes new --name node-cliente-a
# → Anota o pairing code gerado
```

### Na máquina do cliente

```bash
# Instalar OpenClaw
npm install -g openclaw

# Fazer pairing com o servidor central
openclaw node pair --gateway http://SEU_IP_VPS:18789 --code PAIRING_CODE
# ou via QR code no OpenClaw Office
```

### Verificar nodes conectados (no servidor)

```bash
openclaw nodes list
# → node-cliente-a  ✅ Online
# → node-cliente-b  ✅ Online
```

### Testar execução no node

```bash
# Do servidor, executar no node do cliente A
openclaw exec --node node-cliente-a "pwd && ls"
```

---

## Onboarding de Novo Cliente

```bash
# 1. Criar pasta do cliente
cp -r workspace/clients/_TEMPLATE workspace/clients/nome-do-cliente

# 2. Preencher os arquivos
nano workspace/clients/nome-do-cliente/STANDARDS.md
nano workspace/clients/nome-do-cliente/TECH-STACK.md
nano workspace/clients/nome-do-cliente/CODING-RULES.md
nano workspace/clients/nome-do-cliente/CONTEXT.md

# 3. Conectar a máquina do cliente como node
openclaw nodes new --name node-nome-do-cliente

# 4. Fazer pairing na máquina do cliente (ver seção acima)

# 5. Testar dispatch de task (ver TASK-DISPATCH-PROTOCOL.md)
```

---

## Segurança Avançada (produção)

### HTTPS com nginx + Let's Encrypt

```bash
# Instalar nginx e certbot
sudo apt install -y nginx certbot python3-certbot-nginx

# Configurar nginx como reverse proxy
sudo nano /etc/nginx/sites-available/openclaw
```

```nginx
server {
    server_name openclaw.seudominio.com;

    location / {
        proxy_pass http://localhost:18789;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```

```bash
sudo ln -s /etc/nginx/sites-available/openclaw /etc/nginx/sites-enabled/
sudo certbot --nginx -d openclaw.seudominio.com
sudo systemctl restart nginx
```

### Autenticação obrigatória no Gateway

Garanta que `OPENCLAW_GATEWAY_TOKEN` está configurado no `openclaw.json`. Sem token, o Gateway rejeita conexões externas.

---

## Troubleshooting

### Gateway não sobe no Linux

```bash
# Ver logs
journalctl -u openclaw-gateway -n 50 --no-pager

# Reiniciar
sudo systemctl restart openclaw-gateway

# Verificar se porta está ocupada
sudo ss -tlnp | grep 18789
```

### Node não conecta ao servidor

```bash
# Verificar se Gateway está acessível
curl http://IP_SERVIDOR:18789/health

# Verificar firewall
sudo ufw status

# No node, re-fazer pairing
openclaw node unpair
openclaw node pair --gateway http://IP_SERVIDOR:18789 --code NOVO_CODE
```

### Memória alta no servidor

```bash
# Ver uso por processo
htop

# Agentes consomem mais memória durante execução longa
# Considerar upgrade de RAM se > 80% constante
```

---

## Referências

- [OpenClaw Docs](https://docs.openclaw.ai)
- [Task Dispatch Protocol](./TASK-DISPATCH-PROTOCOL.md)
- [Clients — estrutura e templates](../clients/README.md)
