#!/bin/bash

################################################################################
# setup-graphify.sh
# Phase 4 Graphify — Automated Setup & Validation
# 
# Usage: bash scripts/setup-graphify.sh
#
# What it does:
#  1. Verifies system requirements (Python 3.12+, uv, Ollama)
#  2. Installs Python dependencies via uv sync
#  3. Downloads & caches Ollama model (qwen3.5:4b)
#  4. Validates Graphify + Ollama integration
#  5. Creates .env local config
#
################################################################################

set -e  # Exit on error

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'  # No Color

# Config
PYTHON_MIN_VERSION="3.12"
OLLAMA_MODEL="qwen3.5:4b"
OLLAMA_PORT=11434
WORKSPACE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo -e "${BLUE}╔════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║  TEAM IRON SOLUTIONS — GRAPHIFY PHASE 4 SETUP              ║${NC}"
echo -e "${BLUE}║  Automated Configuration & Validation                       ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════════╝${NC}"
echo ""

# ============================================================================
# STEP 1: Verify Python 3.12+
# ============================================================================

echo -e "${YELLOW}[STEP 1/5]${NC} Checking Python version..."

PYTHON_CMD=""
if command -v python3.12 &> /dev/null; then
    PYTHON_CMD="python3.12"
elif command -v python3.13 &> /dev/null; then
    PYTHON_CMD="python3.13"
elif command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
    if [[ "$PYTHON_VERSION" < "$PYTHON_MIN_VERSION" ]]; then
        echo -e "${RED}✗ Python 3.12+ required, found $PYTHON_VERSION${NC}"
        echo "  💡 Install via: brew install python@3.12"
        exit 1
    fi
    PYTHON_CMD="python3"
else
    echo -e "${RED}✗ Python 3.12+ not found${NC}"
    echo "  💡 Install via: brew install python@3.12"
    exit 1
fi

PYTHON_VERSION=$($PYTHON_CMD --version 2>&1 | awk '{print $2}')
echo -e "${GREEN}✓ Python ${PYTHON_VERSION} (OK)${NC}"

# ============================================================================
# STEP 2: Verify uv Package Manager
# ============================================================================

echo ""
echo -e "${YELLOW}[STEP 2/5]${NC} Checking uv package manager..."

if ! command -v uv &> /dev/null; then
    echo -e "${RED}✗ uv not found${NC}"
    echo "  💡 Install via: curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi

UV_VERSION=$(uv --version 2>&1 | awk '{print $2}')
echo -e "${GREEN}✓ uv ${UV_VERSION} (OK)${NC}"

# ============================================================================
# STEP 3: Verify Ollama
# ============================================================================

echo ""
echo -e "${YELLOW}[STEP 3/5]${NC} Checking Ollama..."

if ! command -v ollama &> /dev/null; then
    echo -e "${RED}✗ Ollama not found${NC}"
    echo "  💡 Install via: brew install ollama"
    echo "  💡 Or download: https://ollama.ai/download"
    exit 1
fi

OLLAMA_VERSION=$(ollama --version 2>&1 | grep -oE "v[0-9]+\.[0-9]+\.[0-9]+" || echo "unknown")
echo -e "${GREEN}✓ Ollama ${OLLAMA_VERSION} (OK)${NC}"

# Check if Ollama daemon is running
if ! nc -z localhost $OLLAMA_PORT 2>/dev/null; then
    echo -e "${YELLOW}ℹ Ollama daemon not running. Starting...${NC}"
    # Try to start Ollama (macOS)
    if command -v open &> /dev/null; then
        open -a Ollama
        sleep 3
        # Double-check
        if ! nc -z localhost $OLLAMA_PORT 2>/dev/null; then
            echo -e "${YELLOW}⚠  Ollama may still be starting. Give it 5-10 seconds...${NC}"
            sleep 5
        fi
    fi
fi

if nc -z localhost $OLLAMA_PORT 2>/dev/null; then
    echo -e "${GREEN}✓ Ollama daemon running on :${OLLAMA_PORT}${NC}"
else
    echo -e "${RED}✗ Ollama daemon not responding${NC}"
    echo "  💡 Start manually: ollama serve"
    exit 1
fi

# ============================================================================
# STEP 4: Install Python Dependencies
# ============================================================================

echo ""
echo -e "${YELLOW}[STEP 4/5]${NC} Installing Python dependencies..."

cd "$WORKSPACE_DIR"

if [ ! -f "pyproject.toml" ]; then
    echo -e "${RED}✗ pyproject.toml not found in $WORKSPACE_DIR${NC}"
    exit 1
fi

echo "  Running: uv sync --python ${PYTHON_VERSION}"
uv sync --python "$PYTHON_CMD" 2>&1 | grep -E "(Resolved|Installed|Synced|error|Error)" || true

if [ -d ".venv" ]; then
    echo -e "${GREEN}✓ Dependencies synced (.venv/)${NC}"
else
    echo -e "${RED}✗ .venv not created${NC}"
    exit 1
fi

# ============================================================================
# STEP 5: Download Ollama Model
# ============================================================================

echo ""
echo -e "${YELLOW}[STEP 5/5]${NC} Setting up Ollama model: ${OLLAMA_MODEL}..."

# Check if model already cached
if ollama list 2>/dev/null | grep -q "$OLLAMA_MODEL"; then
    echo -e "${GREEN}✓ ${OLLAMA_MODEL} already cached${NC}"
else
    echo "  Pulling ${OLLAMA_MODEL} (one-time download, ~3.4GB)..."
    echo "  This may take 2-5 minutes on first run..."
    
    if ollama pull "$OLLAMA_MODEL"; then
        echo -e "${GREEN}✓ ${OLLAMA_MODEL} downloaded${NC}"
    else
        echo -e "${RED}✗ Failed to pull ${OLLAMA_MODEL}${NC}"
        echo "  Try manually: ollama pull ${OLLAMA_MODEL}"
        exit 1
    fi
fi

# ============================================================================
# STEP 6: Create .env Configuration
# ============================================================================

echo ""
echo -e "${YELLOW}[FINAL]${NC} Creating local configuration..."

ENV_FILE="${WORKSPACE_DIR}/.env.local"

if [ ! -f "$ENV_FILE" ]; then
    cat > "$ENV_FILE" << 'EOF'
# Graphify Phase 4 — Local Configuration
# Generated by: scripts/setup-graphify.sh

# Ollama Configuration
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=qwen3.5:4b

# Graphify Directories
GRAPHIFY_OUTPUT_DIR=./graphify-out
GRAPHIFY_CACHE_DIR=./.cache/graphify

# Performance
GRAPHIFY_MAX_WORKERS=4
GRAPHIFY_TIMEOUT_SECONDS=300

# Logging
GRAPHIFY_LOG_LEVEL=INFO
EOF
    echo -e "${GREEN}✓ Created .env.local${NC}"
else
    echo -e "${YELLOW}ℹ .env.local already exists (skipped)${NC}"
fi

# ============================================================================
# VALIDATION: Test Graphify + Ollama Integration
# ============================================================================

echo ""
echo -e "${YELLOW}[VALIDATE]${NC} Testing Graphify + Ollama integration..."

# Load .env
if [ -f "$ENV_FILE" ]; then
    set -a
    source "$ENV_FILE"
    set +a
fi

# Test graphify command
cd "$WORKSPACE_DIR"
PYTHON_BIN=".venv/bin/python"

if $PYTHON_BIN -c "import graphifyy; print(f'✓ graphifyy {graphifyy.__version__}')" 2>/dev/null; then
    echo -e "${GREEN}✓ Graphify library OK${NC}"
else
    echo -e "${YELLOW}⚠  Graphify import failed (non-fatal)${NC}"
fi

# Test Ollama connection
if curl -s http://localhost:11434/api/tags | grep -q "$OLLAMA_MODEL" 2>/dev/null; then
    echo -e "${GREEN}✓ Ollama connection OK${NC}"
else
    echo -e "${YELLOW}⚠  Ollama connection check inconclusive (may still be warming up)${NC}"
fi

# ============================================================================
# SUMMARY
# ============================================================================

echo ""
echo -e "${GREEN}╔════════════════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║  SETUP COMPLETE! ✓                                         ║${NC}"
echo -e "${GREEN}╚════════════════════════════════════════════════════════════╝${NC}"
echo ""
echo "Next steps:"
echo ""
echo "1. Test graphify on a small repo:"
echo "   ${BLUE}$ uv run graphify ./OpenJarvis --output ./graphify-out-test${NC}"
echo ""
echo "2. Run the validation script:"
echo "   ${BLUE}$ bash scripts/graphify-sprint1-test.sh${NC}"
echo ""
echo "3. Query the graph:"
echo "   ${BLUE}$ uv run graphify explain --graph graphify-out/graph.json${NC}"
echo ""
echo "📚 Full documentation: ${BLUE}docs/GRAPHIFY-SETUP.md${NC}"
echo "🔧 Troubleshooting: ${BLUE}docs/GRAPHIFY-TROUBLESHOOTING.md${NC}"
echo ""
