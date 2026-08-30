#!/bin/bash
# Phase 5 Daily KPI Report — T'Challa SRE
# Cron: 0 23 * * * (20:00 GMT-3 = 23:00 UTC)
# Owner: T'Challa

set -e
WORKSPACE="/Users/teamironsolutions/.openclaw/workspace"
LOG="$WORKSPACE/logs/phase5-cron.log"
REPORT_FILE="$WORKSPACE/phase5-daily-report-tmp.txt"

mkdir -p "$WORKSPACE/logs"

echo "[$(TZ='America/Sao_Paulo' date '+%Y-%m-%d %H:%M:%S %Z')] Phase 5 daily report starting..." >> "$LOG"

# Collect metrics
python3 "$WORKSPACE/phase5-kpi-collect.py" > "$REPORT_FILE" 2>&1
EXIT_CODE=$?

echo "[$(TZ='America/Sao_Paulo' date '+%Y-%m-%d %H:%M:%S %Z')] Metrics collected (exit=$EXIT_CODE)" >> "$LOG"

# Read report text for agent message
REPORT_TEXT=$(cat "$REPORT_FILE")

# Send to Jarvis via openclaw agent CLI
/Users/teamironsolutions/.nvm/versions/node/v24.18.0/bin/openclaw agent \
  --agent main \
  --message "$(cat "$REPORT_FILE")" \
  2>> "$LOG" && echo "Sent to Jarvis OK" >> "$LOG" || echo "Agent send failed" >> "$LOG"

echo "[$(TZ='America/Sao_Paulo' date '+%Y-%m-%d %H:%M:%S %Z')] Done." >> "$LOG"

# Note: WhatsApp (+5511982768454) not configured in this OpenClaw instance.
# Reports go to Jarvis (agent:main:hud) who can relay to Galvão via available channel.
