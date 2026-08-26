#!/bin/bash
# Graphify Phase 4 — Sprint 1 Test Script
# Executar APÓS Python 3.12 estar instalado

set -e

echo "=== GRAPHIFY PHASE 4 — SPRINT 1 TEST ==="
echo "Data: $(date '+%Y-%m-%d %H:%M:%S')"
echo ""

# Setup pyenv
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

echo "📌 Python version check..."
pyenv global 3.12.0
python3 --version

echo ""
echo "📦 Installing graphifyy..."
pip install graphifyy --quiet
echo "✅ graphifyy installed"

echo ""
echo "=== TEST 1: OpenJarvis (Python — 12k files) ==="
cd /Users/teamironsolutions/.openclaw/workspace/OpenJarvis

echo "🏗️  Building graph (this may take 5-10 minutes)..."
START=$(date +%s)

graphify . --output graphify-out-phase4 2>&1 | tee /tmp/graphify-test1.log

END=$(date +%s)
BUILD_TIME=$((END - START))

echo "✅ Build time: ${BUILD_TIME}s"

# Métricas
if [ -f "graphify-out-phase4/graph.json" ]; then
  GRAPH_SIZE=$(du -h "graphify-out-phase4/graph.json" | cut -f1)
  echo "📊 Graph size: $GRAPH_SIZE"
  
  # Count nodes/edges
  NODES=$(grep -o '"nodes"' graphify-out-phase4/graph.json | wc -l)
  echo "📊 Approx nodes: $NODES"
fi

echo ""
echo "=== TEST 2: Workspace TypeScript (10k files) ==="
cd /Users/teamironsolutions/.openclaw/workspace

echo "🏗️  Building graph..."
START=$(date +%s)

graphify . --output graphify-out-workspace --exclude node_modules,dist,build,.git 2>&1 | tee /tmp/graphify-test2.log

END=$(date +%s)
BUILD_TIME=$((END - START))

echo "✅ Build time: ${BUILD_TIME}s"

if [ -f "graphify-out-workspace/graph.json" ]; then
  GRAPH_SIZE=$(du -h "graphify-out-workspace/graph.json" | cut -f1)
  echo "📊 Graph size: $GRAPH_SIZE"
fi

echo ""
echo "=== TESTE SAMPLE QUERIES ==="
cd /Users/teamironsolutions/.openclaw/workspace/OpenJarvis

echo "Query 1: graphify explain"
# graphify explain "main" 2>/dev/null | head -20

echo ""
echo "=== SPRINT 1 COMPLETE ==="
echo "Logs: /tmp/graphify-test*.log"
echo "Graphs: ./graphify-out-* directories"
