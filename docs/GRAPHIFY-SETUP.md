# Graphify Phase 4 — Setup Guide

**Last Updated:** 27 de agosto de 2026  
**Status:** ✅ Production Ready  
**Audience:** All developers cloning the workspace

---

## 🚀 Quick Start (5 minutes)

```bash
# 1. Run automated setup
bash scripts/setup-graphify.sh

# 2. Verify everything works
uv run graphify ./OpenJarvis --output ./graphify-out-test

# 3. Query the graph
uv run graphify explain --graph graphify-out-test/graph.json
```

Done! ✅

---

## 📋 What Gets Installed

| Component | Version | Size | Purpose |
|-----------|---------|------|---------|
| **graphifyy** | ≥0.9.50 | ~10MB | Knowledge graph builder (52 language parsers) |
| **tree-sitter** | ≥0.20.0 | ~5MB | Code parsing via AST |
| **ollama** | Latest | — | Local LLM for semantic extraction |
| **qwen3.5:4b** | Latest | 3.4GB | Semantic model (cached, one-time download) |

**Total Setup Time:** ~15 minutes (first run includes Ollama model download)  
**Space Required:** ~5GB (pyenv + Ollama model cache)

---

## 🔍 Manual Setup (if automated fails)

### Prerequisites

```bash
# 1. Python 3.12+
python3.12 --version  # Should be ≥3.12

# 2. uv package manager
uv --version          # Should be ≥0.2.0

# 3. Ollama
ollama --version      # Should be installed
ollama serve          # Start daemon (runs in background)
```

### Installation Steps

```bash
# 1. Clone the repository
git clone https://github.com/Team-Iron-Solutions/team-iron-workspace.git
cd team-iron-workspace

# 2. Checkout feature branch
git checkout feat/graphify-phase4

# 3. Sync Python environment
uv sync --python 3.12

# 4. Download Ollama model
ollama pull qwen3.5:4b

# 5. Create local config
cp .env.example .env.local
# Edit .env.local if using non-default Ollama settings

# 6. Verify installation
uv run graphify --version
```

---

## ✅ Validation Checklist

Run this after setup to ensure everything works:

```bash
# 1. Python environment
uv run python --version          # Should be 3.12.x or 3.13.x

# 2. Graphify library
uv run graphify --help           # Should show usage

# 3. Ollama connection
curl http://localhost:11434/api/tags | grep qwen3.5

# 4. Test small codebase (2-5 minutes)
uv run graphify ./jarvis-neural-interface --output ./graphify-out-test

# 5. Inspect graph output
ls -lh ./graphify-out-test/graph.json

# 6. Run query
uv run graphify explain --graph ./graphify-out-test/graph.json
```

If all pass → ✅ You're good to go!

---

## 📚 Project Structure

```
workspace/
├── pyproject.toml              # Dependencies (graphifyy, tree-sitter, ollama)
├── uv.lock                     # Lock file (pinned versions)
├── .env.example                # Configuration template
├── scripts/
│   ├── setup-graphify.sh       # Automated setup
│   └── graphify-sprint1-test.sh # Validation tests
├── docs/
│   ├── GRAPHIFY-SETUP.md       # This file
│   ├── GRAPHIFY-TROUBLESHOOTING.md
│   ├── GRAPHIFY-PHASE4.md      # Architecture & strategy
│   └── adr/ADR-005-PHASE4-GRAPHIFYY-ARCHITECTURE.md
└── GRAPHIFY-*.md               # Reference documentation
```

---

## 🔧 Configuration

### Default Settings (.env.local)

```bash
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=qwen3.5:4b         # Recommended: balance of speed & quality
GRAPHIFY_MAX_WORKERS=4          # Parallel AST parsing
GRAPHIFY_TIMEOUT_SECONDS=300    # 5 minute timeout per repo
```

### Alternative Ollama Models

| Model | Size | Speed | Quality | Best For |
|-------|------|-------|---------|----------|
| **qwen3.5:2b** | 2.7GB | ⚡⚡⚡ | ⭐⭐ | Fast CI/CD pipelines |
| **qwen3.5:4b** | 3.4GB | ⚡⚡ | ⭐⭐⭐ | **Recommended** |
| **qwen3.5:9b** | 6.6GB | ⚡ | ⭐⭐⭐⭐ | Deep analysis (needs 8GB+ RAM) |
| **llama3.2:3b** | 2.0GB | ⚡⚡⚡ | ⭐⭐ | Alternative |

To switch models:

```bash
# Edit .env.local
OLLAMA_MODEL=qwen3.5:9b

# Pull the model (one-time)
ollama pull qwen3.5:9b

# Graphify will use the new model automatically
```

---

## 🏃 Usage Examples

### Build a Knowledge Graph

```bash
# For a single repository
uv run graphify ./OpenJarvis --output ./my-graph

# Exclude node_modules, build artifacts
uv run graphify . \
  --exclude node_modules,dist,build,.git \
  --output ./my-graph

# With semantic extraction (default, uses Ollama)
# (already enabled by default)
```

### Query the Graph

```bash
# Explain an entity
uv run graphify explain --graph ./my-graph/graph.json "main"

# Find related code
uv run graphify find --graph ./my-graph/graph.json "AudioBuffer"

# Export to JSON
uv run graphify export --graph ./my-graph/graph.json --format json
```

### Integrate with Code Review

**Tony Stark's Review Tool** will automatically:
1. Call `graphify .` on your PR repo
2. Use the graph to provide context-aware code review
3. Cache graphs for subsequent runs

No manual steps needed — just merge & deploy!

---

## 📊 Performance Expectations

On a typical codebase (10k-50k files):

| Operation | Time | Memory |
|-----------|------|--------|
| **AST parsing** | 2-5 min | 500MB |
| **Semantic extraction** | 3-10 min | 4-6GB (Ollama) |
| **Total build** | 5-15 min | — |
| **Graph file size** | 50-500KB | — |

To speed up:
- Use `qwen3.5:2b` instead of 4b (3x faster)
- Exclude large dirs: `--exclude node_modules,dist,build`
- Increase `GRAPHIFY_MAX_WORKERS` (up to CPU count)

---

## 🔗 Next Steps

1. **Read the architecture:** `docs/adr/ADR-005-PHASE4-GRAPHIFYY-ARCHITECTURE.md`
2. **Understand AST + Semantics:** `GRAPHIFY-PHASE4.md`
3. **Troubleshoot issues:** `docs/GRAPHIFY-TROUBLESHOOTING.md`
4. **Join the project:** See README.md for contribution guidelines

---

## 💬 Questions?

- Check **GRAPHIFY-TROUBLESHOOTING.md** for common issues
- Read **MEMORY.md** for team context on Phase 4
- File an issue: https://github.com/Team-Iron-Solutions/team-iron-workspace/issues

---

**Made with ❤️ by Team Iron Solutions**  
_Transformamos Tecnologia em Vantagem Competitiva_
