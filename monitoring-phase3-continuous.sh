#!/bin/bash
# Monitoramento contínuo de Phase 3 — Coleta diária de métricas Caveman

set -e

METRICS_DIR="$HOME/.openclaw/workspace/phase3-metrics"
mkdir -p "$METRICS_DIR"

TIMESTAMP=$(date -u +"%Y-%m-%d %H:%M:%S")
DATE=$(date +"%Y-%m-%d")
METRICS_FILE="$METRICS_DIR/metrics-$DATE.json"

echo "[PHASE3-MONITOR] $TIMESTAMP — Coletando métricas..."

# 1. Bridge health & compression ratio
BRIDGE_STATE=$(curl -s http://localhost:3033/state 2>/dev/null || echo '{}')

# 2. Extrair métricas
COMPRESSION_RATIO=$(echo "$BRIDGE_STATE" | python3 -c "import sys, json; d=json.load(sys.stdin); print(d.get('lastCompressionRatio', 'N/A'))" 2>/dev/null || echo "0.0")
REQUEST_COUNT=$(echo "$BRIDGE_STATE" | python3 -c "import sys, json; d=json.load(sys.stdin); print(d.get('requestCount', 0))" 2>/dev/null || echo "0")
ERROR_COUNT=$(echo "$BRIDGE_STATE" | python3 -c "import sys, json; d=json.load(sys.stdin); print(d.get('errorCount', 0))" 2>/dev/null || echo "0")
LAST_REQUEST=$(echo "$BRIDGE_STATE" | python3 -c "import sys, json; d=json.load(sys.stdin); print(d.get('lastRequestTime', 0))" 2>/dev/null || echo "0")

# 3. Estatísticas dos logs
BRIDGE_LOG="/tmp/jarvis-bridge.log"
if [ -f "$BRIDGE_LOG" ]; then
  CAVEMAN_COMPRESSIONS=$(tail -1000 "$BRIDGE_LOG" 2>/dev/null | grep -c "\[CAVEMAN\]" || echo "0")
  CAVEMAN_ERRORS=$(tail -1000 "$BRIDGE_LOG" 2>/dev/null | grep -c "ERROR\|error" || echo "0")
  TTS_CALLS=$(tail -1000 "$BRIDGE_LOG" 2>/dev/null | grep -c "TTS:" || echo "0")
else
  CAVEMAN_COMPRESSIONS=0
  CAVEMAN_ERRORS=0
  TTS_CALLS=0
fi

# 4. Gravar métricas em JSON
cat > "$METRICS_FILE" << EOF
{
  "timestamp": "$TIMESTAMP",
  "date": "$DATE",
  "bridge": {
    "compression_ratio": $COMPRESSION_RATIO,
    "request_count": $REQUEST_COUNT,
    "error_count": $ERROR_COUNT,
    "last_request_ms": $LAST_REQUEST,
    "health": "$([ $ERROR_COUNT -eq 0 ] && echo 'OK' || echo 'DEGRADED')"
  },
  "caveman": {
    "compressions_in_log": $CAVEMAN_COMPRESSIONS,
    "errors_in_log": $CAVEMAN_ERRORS
  },
  "tts": {
    "calls": $TTS_CALLS
  }
}
EOF

echo "[PHASE3-MONITOR] ✅ Métricas gravadas: $METRICS_FILE"

# 5. Resumo para console
echo "[PHASE3-MONITOR] Summary for $DATE:"
echo "  Compression ratio: $COMPRESSION_RATIO%"
echo "  Requests today: $REQUEST_COUNT"
echo "  Errors: $ERROR_COUNT"
echo "  Caveman calls: $CAVEMAN_COMPRESSIONS"
echo "  TTS calls: $TTS_CALLS"

# 6. Se compression_ratio = 0, alertar
if [ "$COMPRESSION_RATIO" = "0.0" ] || [ "$COMPRESSION_RATIO" = "0" ]; then
  echo "[PHASE3-MONITOR] ⚠️  WARNING: Compression ratio é 0 — validar com code review real"
fi
