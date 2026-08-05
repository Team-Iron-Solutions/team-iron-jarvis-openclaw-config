#!/bin/bash
set -e

# Team Iron Solutions - OpenClaw Setup Script
# Replicates the complete OpenClaw environment on a new server

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
OPENCLAW_HOME="$HOME/.openclaw"
WORKSPACE_DIR="$OPENCLAW_HOME/workspace"

echo "🚀 Team Iron Solutions - OpenClaw Setup"
echo "========================================"

# 1. Check Prerequisites
echo ""
echo "📋 Checking prerequisites..."

if ! command -v node &> /dev/null; then
    echo "❌ Node.js not found. Install from https://nodejs.org/"
    exit 1
fi

if ! command -v npm &> /dev/null; then
    echo "❌ npm not found"
    exit 1
fi

echo "✅ Node $(node --version)"
echo "✅ npm $(npm --version)"

# 2. Install/Update OpenClaw
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

# 3. Create OpenClaw directories
echo ""
echo "📁 Creating directories..."
mkdir -p "$WORKSPACE_DIR"
mkdir -p "$OPENCLAW_HOME/skills"

# 4. Copy workspace files
echo ""
echo "📋 Copying workspace configuration..."
cp -v "$SCRIPT_DIR/workspace/SOUL.md" "$WORKSPACE_DIR/" 2>/dev/null || echo "⚠️ SOUL.md not found"
cp -v "$SCRIPT_DIR/workspace/AGENTS.md" "$WORKSPACE_DIR/" 2>/dev/null || echo "⚠️ AGENTS.md not found"
cp -v "$SCRIPT_DIR/workspace/MEMORY.md" "$WORKSPACE_DIR/" 2>/dev/null || echo "⚠️ MEMORY.md not found"
cp -v "$SCRIPT_DIR/workspace/IDENTITY.md" "$WORKSPACE_DIR/" 2>/dev/null || echo "⚠️ IDENTITY.md not found"
cp -v "$SCRIPT_DIR/workspace/USER.md" "$WORKSPACE_DIR/" 2>/dev/null || echo "⚠️ USER.md not found"
cp -v "$SCRIPT_DIR/workspace/TOOLS.md" "$WORKSPACE_DIR/" 2>/dev/null || echo "⚠️ TOOLS.md not found"

# 5. Copy playbooks
echo ""
echo "📚 Copying playbooks..."
mkdir -p "$WORKSPACE_DIR/playbooks"
if [ -d "$SCRIPT_DIR/workspace/playbooks" ]; then
    cp -v "$SCRIPT_DIR/workspace/playbooks"/*.md "$WORKSPACE_DIR/playbooks/" 2>/dev/null || true
    echo "✅ Playbooks copied"
else
    echo "ℹ️ No playbooks directory found"
fi

# 6. Setup OpenClaw configuration
echo ""
echo "⚙️ Setting up OpenClaw configuration..."

if [ ! -f "$OPENCLAW_HOME/openclaw.json" ]; then
    echo "Creating openclaw.json from template..."
    cp "$SCRIPT_DIR/config/openclaw.template.json" "$OPENCLAW_HOME/openclaw.json"
    echo "✅ Configuration created at $OPENCLAW_HOME/openclaw.json"
else
    echo "ℹ️ openclaw.json already exists (not overwriting)"
fi

# 7. Setup MCP servers
echo ""
echo "🔌 Setting up MCP servers..."
echo "Installing: memory, filesystem, github"

openclaw mcp add memory \
  --command npx \
  --arg -y \
  --arg @modelcontextprotocol/server-memory \
  --no-probe 2>/dev/null && echo "✅ Memory MCP added" || echo "ℹ️ Memory MCP already configured"

openclaw mcp add filesystem \
  --command npx \
  --arg -y \
  --arg @modelcontextprotocol/server-filesystem \
  --arg "$WORKSPACE_DIR" \
  --include 'read_file,list_directory,write_file,search_files,create_directory,move_file,delete_file' \
  --no-probe 2>/dev/null && echo "✅ Filesystem MCP added" || echo "ℹ️ Filesystem MCP already configured"

# 8. GitHub MCP (requires token)
echo ""
echo "🐙 GitHub MCP Configuration"
if [ -z "$GITHUB_TOKEN" ]; then
    echo "⚠️  GITHUB_TOKEN not set"
    echo ""
    echo "To enable GitHub MCP:"
    echo "  1. Create token at https://github.com/settings/tokens/new"
    echo "  2. Set: export GITHUB_TOKEN=ghp_..."
    echo "  3. Run: openclaw mcp add github --command npx --arg -y --arg @modelcontextprotocol/server-github --env GITHUB_TOKEN=\"\$GITHUB_TOKEN\""
else
    openclaw mcp add github \
      --command npx \
      --arg -y \
      --arg @modelcontextprotocol/server-github \
      --env GITHUB_TOKEN="$GITHUB_TOKEN" \
      --no-probe 2>/dev/null && echo "✅ GitHub MCP added" || echo "ℹ️ GitHub MCP already configured"
fi

# 9. Validate setup
echo ""
echo "✅ Validating MCP servers..."
openclaw mcp status || true

# 10. Final instructions
echo ""
echo "🎉 Setup Complete!"
echo "========================================"
echo ""
echo "📋 Next steps:"
echo ""
echo "1. Review and customize workspace files:"
echo "   - $WORKSPACE_DIR/SOUL.md"
echo "   - $WORKSPACE_DIR/AGENTS.md"
echo "   - $WORKSPACE_DIR/MEMORY.md"
echo "   - $WORKSPACE_DIR/USER.md"
echo ""
echo "2. Configure secrets (NOT in repo):"
echo "   - GATEWAY_TOKEN for remote gateways"
echo "   - GITHUB_TOKEN for GitHub MCP"
echo ""
echo "3. Start Gateway:"
echo "   openclaw gateway --port 18789"
echo ""
echo "4. Start agents:"
echo "   openclaw agent --agent main"
echo ""
echo "📚 Documentation:"
echo "   - OpenClaw: https://docs.openclaw.ai"
echo "   - Setup guide: $SCRIPT_DIR/README.md"
echo ""
