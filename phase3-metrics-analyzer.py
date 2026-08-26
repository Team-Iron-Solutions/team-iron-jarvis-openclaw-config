#!/usr/bin/env python3
"""
Phase 3 Metrics Analyzer — Analisa dados armazenados em phase3-metrics/
Gera relatórios, dashboards, e alertas
"""

import json
import os
from datetime import datetime
from pathlib import Path
from statistics import mean, stdev
import sys

METRICS_DIR = Path(os.path.expanduser("~/.openclaw/workspace/phase3-metrics"))

def load_all_metrics():
    """Carrega todos os arquivos JSON de métricas"""
    metrics = {}
    
    if not METRICS_DIR.exists():
        print(f"❌ Diretório {METRICS_DIR} não existe")
        return metrics
    
    for json_file in sorted(METRICS_DIR.glob("metrics-*.json")):
        try:
            with open(json_file) as f:
                data = json.load(f)
                date = data.get("date", json_file.stem.replace("metrics-", ""))
                metrics[date] = data
        except json.JSONDecodeError as e:
            print(f"⚠️  Erro ao ler {json_file}: {e}")
    
    return metrics

def analyze_compression(metrics):
    """Analisa tendência de compressão"""
    compression_ratios = []
    dates = []
    
    for date in sorted(metrics.keys()):
        ratio = metrics[date]["bridge"].get("compression_ratio")
        if ratio is not None and ratio > 0:
            compression_ratios.append(float(ratio))
            dates.append(date)
    
    if not compression_ratios:
        return {
            "count": 0,
            "avg": 0,
            "min": 0,
            "max": 0,
            "stdev": 0,
            "trend": "Sem dados com compressão >0%",
            "dates": [],
            "ratios": []
        }
    
    return {
        "count": len(compression_ratios),
        "avg": mean(compression_ratios),
        "min": min(compression_ratios),
        "max": max(compression_ratios),
        "stdev": stdev(compression_ratios) if len(compression_ratios) > 1 else 0,
        "trend": "📈 Crescente" if compression_ratios[-1] > compression_ratios[0] else "📉 Decrescente" if compression_ratios[-1] < compression_ratios[0] else "➡️ Estável",
        "dates": dates,
        "ratios": compression_ratios
    }

def analyze_health(metrics):
    """Analisa saúde do bridge"""
    health_stats = {}
    
    for date in sorted(metrics.keys()):
        health = metrics[date]["bridge"].get("health", "UNKNOWN")
        errors = metrics[date]["bridge"].get("error_count", 0)
        health_stats[date] = {"status": health, "errors": errors}
    
    total_errors = sum(h["errors"] for h in health_stats.values())
    ok_days = sum(1 for h in health_stats.values() if h["status"] == "OK")
    
    return {
        "total_days": len(health_stats),
        "ok_days": ok_days,
        "degraded_days": len(health_stats) - ok_days,
        "total_errors": total_errors,
        "uptime_pct": (ok_days / len(health_stats) * 100) if health_stats else 0,
        "by_date": health_stats
    }

def analyze_requests(metrics):
    """Analisa volume de requisições"""
    request_counts = []
    tts_calls = []
    
    for date in sorted(metrics.keys()):
        request_counts.append(metrics[date]["bridge"].get("request_count", 0))
        tts_calls.append(metrics[date]["tts"].get("calls", 0))
    
    return {
        "total_requests": sum(request_counts),
        "avg_requests_per_day": mean(request_counts) if request_counts else 0,
        "total_tts_calls": sum(tts_calls),
        "avg_tts_per_day": mean(tts_calls) if tts_calls else 0
    }

def generate_markdown_report(metrics):
    """Gera relatório em Markdown"""
    if not metrics:
        return "# Phase 3 Metrics — Sem dados ainda\n\nAguardando primeira coleta diária..."
    
    compression = analyze_compression(metrics)
    health = analyze_health(metrics)
    requests = analyze_requests(metrics)
    
    report = f"""# 📊 Phase 3 Token Economy — Relatório de Métricas

**Data de geração:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**Período:** {min(metrics.keys())} a {max(metrics.keys())}  
**Dias com dados:** {len(metrics)}

---

## 📈 Compressão Caveman

| Métrica | Valor |
|---|---|
| **Média** | {compression['avg']:.2f}% |
| **Mínima** | {compression['min']:.2f}% |
| **Máxima** | {compression['max']:.2f}% |
| **Tendência** | {compression['trend']} |
| **Desvio padrão** | {compression['stdev']:.2f}% |
| **Dias com compressão** | {compression['count']} |

### Histórico
"""
    
    if compression["dates"]:
        for date, ratio in zip(compression["dates"], compression["ratios"]):
            report += f"- **{date}:** {ratio:.1f}%\n"
    else:
        report += "- Sem dados de compressão (prompts muito curtos?)\n"
    
    report += f"""
---

## 🏥 Saúde do Bridge

| Métrica | Valor |
|---|---|
| **Dias OK** | {health['ok_days']}/{health['total_days']} ✅ |
| **Dias Degradados** | {health['degraded_days']} ⚠️ |
| **Uptime** | {health['uptime_pct']:.1f}% |
| **Erros totais** | {health['total_errors']} |

### Status por Data
"""
    
    for date, status in sorted(health["by_date"].items()):
        emoji = "✅" if status["status"] == "OK" else "⚠️"
        report += f"- {date}: {emoji} {status['status']} ({status['errors']} erros)\n"
    
    report += f"""
---

## 📊 Volume de Requisições

| Métrica | Valor |
|---|---|
| **Total requisições** | {int(requests['total_requests'])} |
| **Média por dia** | {requests['avg_requests_per_day']:.1f} |
| **Total chamadas TTS** | {int(requests['total_tts_calls'])} |
| **Média TTS por dia** | {requests['avg_tts_per_day']:.1f} |

---

## ⚠️ Alertas

"""
    
    alerts = []
    
    if compression["avg"] == 0:
        alerts.append("🔴 **Compressão zerada** — Só prompts tiny sendo testados (HUD). Aguardando workload real.")
    elif compression["avg"] < 15:
        alerts.append("🟡 **Compressão baixa** — Verificar se Caveman está ativo. Esperado: 30-45%")
    elif compression["avg"] > 60:
        alerts.append("🟢 **Compressão excepcional** — Melhor que estimado! Validado.")
    
    if health["uptime_pct"] < 99:
        alerts.append(f"🟡 **Uptime baixo** — {health['uptime_pct']:.1f}%. Investigar dias degradados.")
    
    if health["total_errors"] > 0:
        alerts.append(f"🟡 **Erros detectados** — {health['total_errors']} total. Revisar logs.")
    
    if not alerts:
        alerts.append("🟢 **Tudo normal** — Sem alertas.")
    
    for alert in alerts:
        report += f"- {alert}\n"
    
    report += f"""
---

## 📋 Recomendações

"""
    
    if compression["avg"] == 0:
        report += "1. **Executar code review real** — Validar Phase 3 com prompts >500 tokens\n"
    
    if len(metrics) < 3:
        report += "2. **Coletar mais dados** — Precisa 7 dias para tendência confiável\n"
    
    if health["uptime_pct"] == 100 and compression["avg"] > 20:
        report += "3. **Phase 3 validada** — Proceder com Phase 4 Graphify\n"
    
    report += f"""
---

**Próxima atualização:** Amanhã às 02:00 (cron job diário)  
**Dados brutos:** `{METRICS_DIR}/`
"""
    
    return report

def generate_html_dashboard(metrics):
    """Gera dashboard HTML interativo"""
    if not metrics:
        return "<h1>Sem dados ainda</h1>"
    
    compression = analyze_compression(metrics)
    health = analyze_health(metrics)
    requests = analyze_requests(metrics)
    
    # Preparar dados para chart
    compression_data = json.dumps({
        "dates": compression["dates"],
        "ratios": compression["ratios"]
    })
    
    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Phase 3 — Dashboard de Métricas</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 100%);
            color: #e0e0e0;
            padding: 40px;
            min-height: 100vh;
        }}
        .container {{
            max-width: 1400px;
            margin: 0 auto;
        }}
        h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
            color: #00d4ff;
            text-shadow: 0 0 20px rgba(0, 212, 255, 0.5);
        }}
        .timestamp {{
            color: #888;
            font-size: 0.9em;
            margin-bottom: 40px;
        }}
        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-bottom: 40px;
        }}
        .card {{
            background: rgba(30, 40, 70, 0.8);
            border: 1px solid rgba(0, 212, 255, 0.2);
            border-radius: 8px;
            padding: 20px;
            backdrop-filter: blur(10px);
        }}
        .card h3 {{
            color: #00d4ff;
            font-size: 1.2em;
            margin-bottom: 15px;
        }}
        .metric {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 0;
            border-bottom: 1px solid rgba(100, 120, 150, 0.2);
        }}
        .metric:last-child {{
            border-bottom: none;
        }}
        .metric-label {{
            color: #aaa;
        }}
        .metric-value {{
            color: #00ff88;
            font-weight: bold;
            font-size: 1.2em;
        }}
        .status-ok {{
            color: #00ff88;
        }}
        .status-warn {{
            color: #ffaa00;
        }}
        .status-error {{
            color: #ff4444;
        }}
        .chart-container {{
            background: rgba(30, 40, 70, 0.8);
            border: 1px solid rgba(0, 212, 255, 0.2);
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 40px;
            backdrop-filter: blur(10px);
        }}
        .alert {{
            padding: 15px;
            border-radius: 6px;
            margin-bottom: 10px;
            border-left: 4px solid;
        }}
        .alert-error {{
            background: rgba(255, 68, 68, 0.1);
            border-left-color: #ff4444;
            color: #ff8888;
        }}
        .alert-warn {{
            background: rgba(255, 170, 0, 0.1);
            border-left-color: #ffaa00;
            color: #ffbb55;
        }}
        .alert-info {{
            background: rgba(0, 212, 255, 0.1);
            border-left-color: #00d4ff;
            color: #55ddff;
        }}
        .alert-success {{
            background: rgba(0, 255, 136, 0.1);
            border-left-color: #00ff88;
            color: #55ffbb;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🔗 Phase 3 — Dashboard de Métricas Caveman</h1>
        <div class="timestamp">Gerado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</div>
        
        <div class="grid">
            <div class="card">
                <h3>📈 Compressão</h3>
                <div class="metric">
                    <span class="metric-label">Média</span>
                    <span class="metric-value">{compression['avg']:.1f}%</span>
                </div>
                <div class="metric">
                    <span class="metric-label">Min/Max</span>
                    <span class="metric-value">{compression['min']:.1f}% / {compression['max']:.1f}%</span>
                </div>
                <div class="metric">
                    <span class="metric-label">Tendência</span>
                    <span class="metric-value">{compression['trend']}</span>
                </div>
            </div>
            
            <div class="card">
                <h3>🏥 Saúde do Bridge</h3>
                <div class="metric">
                    <span class="metric-label">Uptime</span>
                    <span class="metric-value status-ok">{health['uptime_pct']:.1f}%</span>
                </div>
                <div class="metric">
                    <span class="metric-label">Dias OK/Total</span>
                    <span class="metric-value">{health['ok_days']}/{health['total_days']}</span>
                </div>
                <div class="metric">
                    <span class="metric-label">Erros</span>
                    <span class="metric-value">{health['total_errors']}</span>
                </div>
            </div>
            
            <div class="card">
                <h3>📊 Volume</h3>
                <div class="metric">
                    <span class="metric-label">Total Requisições</span>
                    <span class="metric-value">{int(requests['total_requests'])}</span>
                </div>
                <div class="metric">
                    <span class="metric-label">Chamadas TTS</span>
                    <span class="metric-value">{int(requests['total_tts_calls'])}</span>
                </div>
                <div class="metric">
                    <span class="metric-label">Média/dia</span>
                    <span class="metric-value">{requests['avg_requests_per_day']:.1f}</span>
                </div>
            </div>
        </div>
        
        <div class="chart-container">
            <h3>📉 Compressão ao Longo do Tempo</h3>
            <canvas id="compressionChart"></canvas>
        </div>
        
        <h2 style="color: #00d4ff; margin-bottom: 20px;">⚠️ Alertas & Status</h2>
        <div id="alerts"></div>
    </div>
    
    <script>
        const compressionData = {compression_data};
        
        // Gráfico de compressão
        if (compressionData.dates && compressionData.dates.length > 0) {{
            const ctx = document.getElementById('compressionChart').getContext('2d');
            new Chart(ctx, {{
                type: 'line',
                data: {{
                    labels: compressionData.dates,
                    datasets: [{{
                        label: 'Compression Ratio (%)',
                        data: compressionData.ratios,
                        borderColor: '#00ff88',
                        backgroundColor: 'rgba(0, 255, 136, 0.1)',
                        borderWidth: 2,
                        fill: true,
                        tension: 0.4,
                        pointBackgroundColor: '#00ff88',
                        pointBorderColor: '#fff',
                        pointRadius: 5
                    }}]
                }},
                options: {{
                    responsive: true,
                    plugins: {{
                        legend: {{
                            labels: {{ color: '#e0e0e0' }}
                        }}
                    }},
                    scales: {{
                        y: {{
                            beginAtZero: true,
                            max: 100,
                            ticks: {{ color: '#aaa' }},
                            grid: {{ color: 'rgba(100, 120, 150, 0.1)' }}
                        }},
                        x: {{
                            ticks: {{ color: '#aaa' }},
                            grid: {{ color: 'rgba(100, 120, 150, 0.1)' }}
                        }}
                    }}
                }}
            }});
        }}
        
        // Alertas dinâmicos
        const alertsDiv = document.getElementById('alerts');
        const alerts = [
            {{ type: 'info', msg: 'Phase 3 monitoramento ativo desde 19/08/2026' }},
            {{ type: {'"success"' if compression['avg'] > 0 else '"warn"'}, msg: 'Compressão média: {compression['avg']:.1f}%' }},
            {{ type: {'"success"' if health['uptime_pct'] == 100 else '"warn"'}, msg: 'Uptime: {health['uptime_pct']:.1f}%' }}
        ];
        
        alerts.forEach(alert => {{
            const div = document.createElement('div');
            div.className = `alert alert-${{alert.type}}`;
            div.textContent = alert.msg;
            alertsDiv.appendChild(div);
        }});
    </script>
</body>
</html>
"""
    return html

def main():
    """Main"""
    if len(sys.argv) > 1:
        command = sys.argv[1]
    else:
        command = "report"
    
    metrics = load_all_metrics()
    
    if command == "report":
        print(generate_markdown_report(metrics))
    
    elif command == "html":
        html_path = METRICS_DIR.parent / "phase3-dashboard.html"
        with open(html_path, "w") as f:
            f.write(generate_html_dashboard(metrics))
        print(f"✅ Dashboard salvo: {html_path}")
        print(f"Abrir em browser: file://{html_path}")
    
    elif command == "json":
        compression = analyze_compression(metrics)
        health = analyze_health(metrics)
        requests = analyze_requests(metrics)
        summary = {
            "compression": compression,
            "health": health,
            "requests": requests,
            "generated_at": datetime.now().isoformat()
        }
        print(json.dumps(summary, indent=2))
    
    else:
        print("Uso: python3 phase3-metrics-analyzer.py [report|html|json]")

if __name__ == "__main__":
    main()
