#!/bin/bash
# HUD STT Diagnostic Test — Collect logs during manual interaction

LOG_DIR="/Users/teamironsolutions/.openclaw/workspace/.tmp/openclaw-spikes/hud-stt-diagnostics"
LOG_FILE="$LOG_DIR/bridge-logs.txt"
BRIDGE_SCRIPT="/Users/teamironsolutions/.openclaw/workspace/jarvis-neural-interface/bridge/jarvis-bridge-v4.js"

echo "🔍 Starting HUD STT Diagnostic Test"
echo "Log file: $LOG_FILE"
echo ""

# Clean previous logs
> "$LOG_FILE"

# Start bridge with verbose logging
echo "[$(date)] Bridge starting with verbose logging..." >> "$LOG_FILE"
node "$BRIDGE_SCRIPT" >> "$LOG_FILE" 2>&1 &
BRIDGE_PID=$!
echo "Bridge PID: $BRIDGE_PID"

# Wait for bridge to be ready
sleep 3

echo ""
echo "🎤 Bridge is now running. Ready for manual testing:"
echo ""
echo "1. Open http://localhost:3033/hud in browser"
echo "2. Grant microphone permission"
echo "3. Test scenarios:"
echo "   - Say 'Jarvis' → observe wake detection"
echo "   - Say 'Jarvis' + question → measure listening time"
echo "   - Say 'Jarvis, ei' → test alternate trigger"
echo ""
echo "4. Watch this log in another terminal:"
echo "   tail -f $LOG_FILE"
echo ""
echo "5. When done testing, press ENTER to stop logging and collect data"
echo ""

# Wait for user input
read -p "Press ENTER when done testing..."

# Stop bridge
kill $BRIDGE_PID 2>/dev/null
wait $BRIDGE_PID 2>/dev/null

echo ""
echo "✓ Test complete. Logs saved to $LOG_FILE"
echo ""
echo "Analyzing..."
grep -i "error\|failed\|reject\|abort\|timeout" "$LOG_FILE" | head -20 | while read line; do
  echo "⚠️  $line"
done
