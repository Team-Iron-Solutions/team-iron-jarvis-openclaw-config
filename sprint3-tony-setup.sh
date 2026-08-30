#!/bin/bash
# Phase 4 Sprint 3 — Tony Stark Setup
# Activate graphify-env, validate tools, prepare for 10 code reviews

set -e

WORKSPACE="/Users/teamironsolutions/.openclaw/workspace"
cd "$WORKSPACE"

echo "=========================================="
echo "PHASE 4 SPRINT 3 — TONY SETUP"
echo "=========================================="

# Activate graphify-env
echo "✅ Activating graphify-env..."
source graphify-env/bin/activate 2>/dev/null || {
    echo "❌ graphify-env not found. Creating..."
    python3 -m venv graphify-env
    source graphify-env/bin/activate
}

# Verify Python
echo "✅ Python: $(python3 --version)"

# Install/verify graphify
echo "✅ Checking graphify..."
python3 -m pip install -q graphify 2>/dev/null || echo "⚠️ graphify not installable via pip"

# Verify Ollama
echo "✅ Checking Ollama..."
curl -s http://localhost:11434/api/tags > /dev/null && echo "✅ Ollama responding" || echo "⚠️ Ollama not responding (may not be critical)"

# Check repos
echo "✅ Checking repos..."
[ -d "jarvis-neural-interface" ] && echo "   ✅ jarvis-neural-interface found"
[ -d "OpenJarvis" ] && echo "   ✅ OpenJarvis found"

# List available code files for reviews
echo ""
echo "📋 Available code files for review:"
find jarvis-neural-interface -name "*.js" -o -name "*.ts" 2>/dev/null | head -10
find OpenJarvis -name "*.py" 2>/dev/null | head -5

echo ""
echo "=========================================="
echo "✅ Setup Complete — Ready for Sprint 3"
echo "=========================================="
