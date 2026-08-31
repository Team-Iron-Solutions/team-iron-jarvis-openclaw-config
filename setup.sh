#!/bin/bash
set -e

# ============================================================
# Team Iron Solutions - OpenClaw Setup Script
# Multi-OS: macOS (arm64/x86) + Linux (Ubuntu/Debian)
# ============================================================

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
OPENCLAW_HOME="$HOME/.openclaw"
WORKSPACE_DIR="$OPENCLAW_HOME/workspace"

# ── Detect OS ───────────────────────────────────────────────
OS="unknown"
ARCH=$(uname -m)
if [[ "$OSTYPE" == "darwin"* ]]; then
  OS="macos"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
  OS="linux"
fi

echo "🚀 Team Iron Solutions - OpenClaw Setup"
echo "========================================"
echo "   OS: $OS ($ARCH)"
echo "   Workspace: $WORKSPACE_DIR"
echo ""

# ── 1. System Dependencies (Linux only) ─────────────────────
if [[ "$OS" == "linux" ]]; then
  echo "📦 Installing system dependencies..."
  sudo apt-get update -qq
  sudo apt-get install -y -qq curl git build-essential
  echo "✅ System dependencies ready"
  echo ""
fi

# ── 2. Node.js via nvm ──────────────────────────────────────
echo "📋 Checking Node.js..."

if ! command -v node &> /dev/null; then
  echo "⚙️  Installing Node.js via nvm..."
  curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
  # Source nvm for this session
  export NVM_DIR="$HOME/.nvm"
  [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
  nvm install --lts
  nvm use --lts
  echo "✅ Node.js $(node --version) via nvm"
else
  echo "✅ Node $(node --version)"
fi

if ! command -v npm &> /dev/null; then
  echo "❌ npm not found after Node.js install"
  exit 1
fi

# ── 3. Install OpenClaw ─────────────────────────────────────
echo ""
echo "📦 Installing OpenClaw..."
npm install -g openclaw 2>/dev/null || {
  echo "ℹ️ OpenClaw may already be installed"
}

if ! command -v openclaw &> /dev/null; then
  echo "❌ OpenClaw installation failed"
  exit 1
fi

echo "✅ OpenClaw $(openclaw --version 2>/dev/null || echo 'installed')"

# ── 4. Create directories ───────────────────────────────────
echo ""
echo "📁 Creating directories..."
mkdir -p "$WORKSPACE_DIR"
mkdir -p "$OPENCLAW_HOME/skills"
mkdir -p "$WORKSPACE_DIR/clients"
mkdir -p "$WORKSPACE_DIR/memory"

# ── 5. Copy workspace files ─────────────────────────────────
echo ""
echo "📋 Copying workspace configuration..."
for f in SOUL.md AGENTS.md IDENTITY.md USER.md TOOLS.md HEARTBEAT.md; do
  if [ -f "$SCRIPT_DIR/workspace/$f" ]; then
    cp -v "$SCRIPT_DIR/workspace/$f" "$WORKSPACE_DIR/"
  else
    echo "ℹ️  $f not found in repo (optional)"
  fi
done

# Copy MEMORY.md only if destination doesn't exist (preserve live memory)
if [ ! -f "$WORKSPACE_DIR/MEMORY.md" ]; then
  cp -v "$SCRIPT_DIR/workspace/MEMORY.md" "$WORKSPACE_DIR/" 2>/dev/null || echo "ℹ️ MEMORY.md not found"
else
  echo "ℹ️ MEMORY.md already exists (not overwriting)"
fi

# ── 6. Copy clients template ────────────────────────────────
echo ""
echo "👥 Setting up clients directory..."
if [ -d "$SCRIPT_DIR/clients" ]; then
  cp -r "$SCRIPT_DIR/clients" "$WORKSPACE_DIR/"
  echo "✅ Clients directory copied"
else
  mkdir -p "$WORKSPACE_DIR/clients"
  echo "ℹ️ Clients directory created (populate with client configs)"
fi

# ── 7. Copy docs & protocols ────────────────────────────────
if [ -d "$SCRIPT_DIR/docs" ]; then
  mkdir -p "$WORKSPACE_DIR/docs"
  cp -r "$SCRIPT_DIR/docs/"* "$WORKSPACE_DIR/docs/" 2>/dev/null || true
  echo "✅ Docs copied"
fi

# ── 8. Setup OpenClaw configuration ─────────────────────────
echo ""
echo "⚙️  Setting up OpenClaw configuration..."

if [ ! -f "$OPENCLAW_HOME/openclaw.json" ]; then
  echo "Creating openclaw.json from template..."
  cp "$SCRIPT_DIR/config/openclaw.template.json" "$OPENCLAW_HOME/openclaw.json"
  echo "✅ Configuration created at $OPENCLAW_HOME/openclaw.json"
  echo "⚠️  EDIT IT NOW and fill in your secrets (tokens, keys)"
else
  echo "ℹ️  openclaw.json already exists (not overwriting)"
fi

# ── 9. MCP Servers ──────────────────────────────────────────
echo ""
echo "🔌 Setting up MCP servers..."

openclaw mcp add memory \
  --command npx \
  --arg -y \
  --arg @modelcontextprotocol/server-memory \
  --no-probe 2>/dev/null && echo "✅ Memory MCP added" || echo "ℹ️  Memory MCP already configured"

openclaw mcp add filesystem \
  --command npx \
  --arg -y \
  --arg @modelcontextprotocol/server-filesystem \
  --arg "$WORKSPACE_DIR" \
  --include 'read_file,list_directory,write_file,search_files,create_directory,move_file,delete_file' \
  --no-probe 2>/dev/null && echo "✅ Filesystem MCP added" || echo "ℹ️  Filesystem MCP already configured"

echo ""
echo "🐙 GitHub MCP:"
if [ -z "$GITHUB_TOKEN" ]; then
  echo "⚠️  GITHUB_TOKEN not set — skipping"
  echo "   Later: export GITHUB_TOKEN=ghp_... && openclaw mcp add github \\"
  echo "          --command npx --arg -y --arg @modelcontextprotocol/server-github \\"
  echo "          --env GITHUB_TOKEN=\"\$GITHUB_TOKEN\""
else
  openclaw mcp add github \
    --command npx \
    --arg -y \
    --arg @modelcontextprotocol/server-github \
    --env GITHUB_TOKEN="$GITHUB_TOKEN" \
    --no-probe 2>/dev/null && echo "✅ GitHub MCP added" || echo "ℹ️  GitHub MCP already configured"
fi

# ── 10. Service Manager (macOS LaunchAgent / Linux systemd) ──
echo ""
echo "⚙️  Setting up Gateway service..."

if [[ "$OS" == "macos" ]]; then
  _setup_macos_launchagent
elif [[ "$OS" == "linux" ]]; then
  _setup_linux_systemd
fi

# ── macOS helper ─────────────────────────────────────────────
_setup_macos_launchagent() {
  PLIST_DIR="$HOME/Library/LaunchAgents"
  PLIST_FILE="$PLIST_DIR/ai.openclaw.gateway.plist"
  OPENCLAW_BIN=$(which openclaw)

  mkdir -p "$PLIST_DIR"

  if [ ! -f "$PLIST_FILE" ]; then
    cat > "$PLIST_FILE" <<PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>ai.openclaw.gateway</string>
  <key>ProgramArguments</key>
  <array>
    <string>$OPENCLAW_BIN</string>
    <string>gateway</string>
    <string>--port</string>
    <string>18789</string>
  </array>
  <key>WorkingDirectory</key>
  <string>$WORKSPACE_DIR</string>
  <key>RunAtLoad</key>
  <true/>
  <key>KeepAlive</key>
  <true/>
  <key>StandardOutPath</key>
  <string>/tmp/openclaw-gateway.log</string>
  <key>StandardErrorPath</key>
  <string>/tmp/openclaw-gateway-error.log</string>
</dict>
</plist>
PLIST
    launchctl load "$PLIST_FILE" 2>/dev/null && echo "✅ LaunchAgent installed & started" || echo "⚠️  LaunchAgent created (load manually: launchctl load $PLIST_FILE)"
  else
    echo "ℹ️  LaunchAgent already exists"
  fi
}

# ── Linux helper ─────────────────────────────────────────────
_setup_linux_systemd() {
  SERVICE_FILE="/etc/systemd/system/openclaw-gateway.service"
  OPENCLAW_BIN=$(which openclaw)
  CURRENT_USER=$(whoami)

  if [ ! -f "$SERVICE_FILE" ]; then
    sudo tee "$SERVICE_FILE" > /dev/null <<SERVICE
[Unit]
Description=OpenClaw Gateway - Team Iron Solutions
After=network.target

[Service]
Type=simple
User=$CURRENT_USER
WorkingDirectory=$WORKSPACE_DIR
ExecStart=$OPENCLAW_BIN gateway --port 18789
Restart=always
RestartSec=5
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
SERVICE

    sudo systemctl daemon-reload
    sudo systemctl enable openclaw-gateway
    sudo systemctl start openclaw-gateway
    echo "✅ systemd service installed & started"
    echo "   Logs: journalctl -u openclaw-gateway -f"
  else
    echo "ℹ️  systemd service already exists"
    sudo systemctl restart openclaw-gateway
    echo "ℹ️  Service restarted"
  fi
}

# ── 11. Validate ─────────────────────────────────────────────
echo ""
echo "✅ Validating MCP servers..."
openclaw mcp status || true

# ── 12. Done ─────────────────────────────────────────────────
echo ""
echo "🎉 Setup Complete!"
echo "========================================"
echo ""
echo "📋 Required next steps:"
echo ""
echo "  1. Add your secrets to: $OPENCLAW_HOME/openclaw.json"
echo "     - OPENROUTER_API_KEY or ANTHROPIC_API_KEY"
echo "     - OPENCLAW_GATEWAY_TOKEN (any secure string)"
echo "     - GITHUB_TOKEN (if using GitHub MCP)"
echo ""
echo "  2. Configure client standards:"
echo "     cp $WORKSPACE_DIR/clients/_TEMPLATE/* $WORKSPACE_DIR/clients/MY-CLIENT/"
echo "     # Edit STANDARDS.md, TECH-STACK.md, CODING-RULES.md"
echo ""
if [[ "$OS" == "linux" ]]; then
echo "  3. Check gateway status:"
echo "     sudo systemctl status openclaw-gateway"
echo "     journalctl -u openclaw-gateway -f"
echo ""
echo "  4. Open firewall port (if remote access needed):"
echo "     sudo ufw allow 18789/tcp"
echo ""
fi
echo "  📖 Full guide: docs/DEPLOYMENT-GUIDE.md"
echo ""
echo "  🔗 OpenClaw docs: https://docs.openclaw.ai"
echo ""
echo "Built with ❤️  Team Iron Solutions"
