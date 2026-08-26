#!/bin/bash
# Phase 3 Metrics Summary — Quick overview after cron collections

METRICS_DIR="$HOME/.openclaw/workspace/phase3-metrics"

echo "📊 PHASE 3 METRICS SUMMARY"
echo "=========================="
echo

# Contar arquivos
FILE_COUNT=$(ls "$METRICS_DIR"/metrics-*.json 2>/dev/null | wc -l)
echo "Arquivos de métricas coletados: $FILE_COUNT"
echo

# Últimas compressões com valor > 0
echo "Últimas compressões (>0%):"
for file in $(ls -t "$METRICS_DIR"/metrics-*.json 2>/dev/null | head -7); do
  RATIO=$(python3 -c "import json; d=json.load(open('$file')); print(d.get('bridge', {}).get('compression_ratio', 0))" 2>/dev/null)
  DATE=$(basename "$file" | sed 's/metrics-//;s/.json//')
  
  if [ "$RATIO" != "0.0" ] && [ "$RATIO" != "0" ]; then
    echo "  $DATE: ${RATIO}%"
  fi
done
echo

# Saúde geral
OK_COUNT=$(python3 -c "
import json
import os
from pathlib import Path

metrics_dir = Path('$METRICS_DIR')
ok_count = 0
total = 0

for f in metrics_dir.glob('metrics-*.json'):
    try:
        with open(f) as fp:
            d = json.load(fp)
            total += 1
            if d.get('bridge', {}).get('health') == 'OK':
                ok_count += 1
    except: pass

print(f'{ok_count}/{total}')
" 2>/dev/null || echo "?/?")

echo "Bridge Health: $OK_COUNT"
echo

# Recomendação
echo "📋 Recomendação:"
if [ "$FILE_COUNT" -lt 3 ]; then
  echo "  ⏳ Coletando baseline... continue monitorando"
elif [ "$FILE_COUNT" -lt 7 ]; then
  echo "  🟡 Cerca de $(($FILE_COUNT)) dias de dados. Aguarde 7 dias para análise confiável"
else
  echo "  ✅ 7+ dias de dados. Rodar análise completa: python3 phase3-metrics-analyzer.py report"
fi
echo

echo "Dashboard HTML: file://$HOME/.openclaw/workspace/phase3-dashboard.html"
echo "Atualizar: python3 $HOME/.openclaw/workspace/phase3-metrics-analyzer.py html"
