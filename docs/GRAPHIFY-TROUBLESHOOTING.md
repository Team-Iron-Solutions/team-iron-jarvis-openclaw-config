# Graphify Phase 4 — Troubleshooting Guide

**Last Updated:** 27 de agosto de 2026  
**Common Issues:** 8  
**FAQ:** Yes (at end)

---

## 🔴 Critical Issues

### ❌ "ollama: command not found"

**Problem:** Ollama is not installed or not in PATH  
**Impact:** Setup fails at Step 3

**Solutions:**

```bash
# Option 1: Homebrew (recommended)
brew install ollama

# Option 2: Download from ollama.ai
open https://ollama.ai/download

# Option 3: Verify installation
which ollama
ollama --version
```

**If still fails:** Restart terminal and try again (PATH update needed)

---

### ❌ "Ollama daemon not responding on :11434"

**Problem:** Ollama process is not running  
**Impact:** Setup fails at Step 3, cannot pull models

**Solutions:**

```bash
# Option 1: Start Ollama (macOS/GUI)
open -a Ollama

# Option 2: Start Ollama (CLI)
ollama serve

# Option 3: Verify it's listening
curl http://localhost:11434/api/tags

# Option 4: Check if port is in use
lsof -i :11434

# Option 5: Use a different port
export OLLAMA_HOST=http://localhost:12345
ollama serve
```

**Pro tip:** On macOS, you can add Ollama to Login Items (Ollama app → Preferences) so it starts automatically.

---

### ❌ "Failed to pull qwen3.5:4b"

**Problem:** Model download failed (network, disk space, or Ollama error)  
**Impact:** Setup fails at Step 5

**Diagnostics:**

```bash
# Check network
ping 8.8.8.8

# Check disk space (need ~5GB free)
df -h

# Check Ollama logs
tail -f ~/.ollama/logs/server.log 2>/dev/null || echo "No logs found"

# Check Ollama is responding
curl -I http://localhost:11434
```

**Solutions:**

```bash
# Option 1: Retry pull
ollama pull qwen3.5:4b

# Option 2: Use smaller model temporarily
ollama pull qwen3.5:2b

# Option 3: Manual model placement
# (Skip — stick with `ollama pull`)

# Option 4: Check if model is partially cached
ollama list | grep qwen3.5
```

**If stuck:** Try `ollama list` to see what's cached, then choose the best option:
- If nothing cached → Try pull again with fresh internet
- If 2b cached → Use that and upgrade later
- If 9b cached → Use that (might need more RAM, but works)

---

### ❌ "uv: command not found"

**Problem:** `uv` package manager not installed  
**Impact:** Setup fails at Step 2

**Solutions:**

```bash
# Official installation
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or homebrew
brew install uv

# Verify
uv --version

# If still "command not found", add to PATH
export PATH="$HOME/.local/bin:$PATH"
```

---

## 🟠 Common Issues

### ⚠️ "Python 3.12 not found"

**Problem:** Python 3.12+ is not installed  
**Impact:** `uv sync` fails

**Solutions:**

```bash
# Check available versions
python3 --version
python3.12 --version
python3.13 --version

# Install Python 3.12
brew install python@3.12

# Or use pyenv
brew install pyenv
pyenv install 3.12.13
pyenv global 3.12.13

# Verify
python3.12 --version
```

---

### ⚠️ ".venv not created after uv sync"

**Problem:** `uv sync` ran but `.venv` directory is missing  
**Impact:** Cannot run graphify commands

**Diagnostics:**

```bash
# Check what uv synced
ls -la .venv/

# Check uv config
uv config

# Check Python setup
uv venv --python 3.12
```

**Solutions:**

```bash
# Force recreate
rm -rf .venv .uv
uv sync --python 3.12 --force

# Or manual venv
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

### ⚠️ "graphify command not found after setup"

**Problem:** graphify installed but not in PATH  
**Impact:** `graphify` command fails

**Solutions:**

```bash
# Option 1: Use uv run (recommended)
uv run graphify --help

# Option 2: Activate venv manually
source .venv/bin/activate
graphify --help

# Option 3: Full path
.venv/bin/graphify --help
```

---

### ⚠️ "Ollama out of memory (OOM)"

**Problem:** Using `qwen3.5:9b` with <8GB available RAM  
**Symptoms:** Ollama crashes, graphify hangs, or OS becomes sluggish

**Solutions:**

```bash
# Option 1: Switch to smaller model (RECOMMENDED)
export OLLAMA_MODEL=qwen3.5:4b
ollama pull qwen3.5:4b
# Restart graphify

# Option 2: Check available RAM
free -h  # Linux
vm_stat  # macOS

# Option 3: Kill other apps using RAM
# Close browser, Docker, other memory-heavy apps
top -l1 | grep "used"  # Check memory on macOS

# Option 4: Use 2b model if necessary
export OLLAMA_MODEL=qwen3.5:2b
```

**Why it happens:**
- 9b model needs ~6-7GB RAM
- If you have <8GB total, the OS + apps + Ollama = crash
- 4b model needs only ~4-5GB (safe choice)

---

### ⚠️ "graphify build takes >30 minutes"

**Problem:** Graph building is too slow  
**Typical causes:** Large codebase, high-quality model, or single worker

**Diagnostics:**

```bash
# Check if it's stuck (not just slow)
ps aux | grep graphify
ps aux | grep ollama

# Monitor progress
tail -f /tmp/graphify*.log

# Check memory usage
top
```

**Solutions:**

```bash
# Option 1: Use faster model (recommended)
export OLLAMA_MODEL=qwen3.5:2b
# Re-run graphify

# Option 2: Increase workers (up to CPU count)
export GRAPHIFY_MAX_WORKERS=8  # or 16 if you have many cores

# Option 3: Exclude large directories
graphify . \
  --exclude node_modules,dist,build,.git,venv \
  --output ./my-graph

# Option 4: Increase timeout
export GRAPHIFY_TIMEOUT_SECONDS=600  # 10 minutes
```

**Performance tuning:**
- `2b` model: 2-5 min per 10k files
- `4b` model: 5-10 min per 10k files (default)
- `9b` model: 10-30 min per 10k files

---

## 🟡 Warnings (Not Critical)

### ℹ️ ".env.local already exists"

**Message:** "ℹ .env.local already exists (skipped)"  
**Status:** ✅ This is fine!

**Explanation:** Your existing `.env.local` wasn't overwritten. If you want to update it:

```bash
# Compare with template
diff .env.local .env.example

# Or manually merge
cat .env.example
# Then edit .env.local to add any new keys
```

---

### ℹ️ "Ollama may still be starting"

**Message:** "⚠ Ollama may still be starting. Give it 5-10 seconds..."  
**Status:** ⚠️ Usually OK, but may slow down first run

**Explanation:** Ollama daemon started but isn't fully ready yet. The setup script waits and retries.

**If it persists:** Wait 10 seconds, then run setup again.

---

## ❓ FAQ

### Q: Do I need to run setup.sh every time?

**A:** No — only on first clone. The lock files ensure reproducibility.

```bash
# First clone: run setup
bash scripts/setup-graphify.sh

# Later: just sync (if dependencies change)
uv sync
```

---

### Q: Can I use a different Ollama model?

**A:** Yes! Edit `.env.local`:

```bash
# Before:
OLLAMA_MODEL=qwen3.5:4b

# After:
OLLAMA_MODEL=llama3.2:3b

# Then pull it
ollama pull llama3.2:3b

# Graphify uses the new model automatically
```

---

### Q: What if I don't have Ollama?

**A:** You can still use graphify with AST-only mode:

```bash
# Disable semantic extraction
uv run graphify . \
  --output ./my-graph \
  --skip-semantic
```

**Tradeoff:** No semantic labels, but 3x faster and zero Ollama dependency.

---

### Q: How much disk space do I need?

**A:** ~5GB minimum:
- Python environment: ~500MB
- Ollama model (4b): ~3.4GB
- Workspace + graphs: ~1GB
- Breathing room: ~100MB

Use `df -h` to check. If tight, use `qwen3.5:2b` (2.7GB model).

---

### Q: Can I move the Ollama cache?

**A:** Yes, set `OLLAMA_MODELS`:

```bash
# Store models on external drive
export OLLAMA_MODELS=/Volumes/external-drive/ollama-models
ollama pull qwen3.5:4b

# .env.local
OLLAMA_MODELS=/Volumes/external-drive/ollama-models
```

---

### Q: What if setup.sh fails mysteriously?

**A:** Collect debug info:

```bash
# Run with verbose output
bash -x scripts/setup-graphify.sh 2>&1 | tee setup-debug.log

# Check system info
uname -a
python3 --version
uv --version
ollama --version
df -h

# Check network
curl -I https://ollama.ai

# File an issue with these details
# https://github.com/Team-Iron-Solutions/team-iron-workspace/issues
```

---

### Q: Does Graphify work offline?

**A:** Mostly! But:
- First run requires download (qwen model)
- After that, fully offline ✅

---

### Q: Can multiple people share one Ollama?

**A:** Yes — but configure network:

```bash
# Person A: Ollama on network
export OLLAMA_HOST=0.0.0.0:11434  # Listen on all interfaces
ollama serve

# Person B: Connect to Person A's Ollama
export OLLAMA_HOST=http://person-a-ip:11434
uv run graphify .
```

---

## 🆘 Still Stuck?

1. **Read:** `GRAPHIFY-PHASE4.md` for deep dive
2. **Check:** Previous issues for similar symptoms
3. **Search:** https://github.com/Team-Iron-Solutions/team-iron-workspace/issues
4. **Ask:** File a new issue with:
   - `bash -x scripts/setup-graphify.sh 2>&1 | tee debug.log` output
   - System info (`uname -a`, `python --version`, etc.)
   - What you tried

---

**Made with ❤️ by Team Iron Solutions**  
_Transformamos Tecnologia em Vantagem Competitiva_
