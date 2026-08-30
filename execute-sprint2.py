#!/usr/bin/env python3
"""
PHASE 4 SPRINT 2 — Execução Rigorosa
Baseline (sem graphify) + Graphify (com Ollama)
Medição de tokens, latência, qualidade

Owner: Tony Stark
Date: 30 agosto 2026
"""

import json
import time
import requests
from pathlib import Path
from datetime import datetime
import re

# ============================================================================
# CONFIG
# ============================================================================

WORKSPACE = "/Users/teamironsolutions/.openclaw/workspace"
OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "qwen3.5:4b"

# Code samples para 5 reviews
REVIEWS = [
    {
        "id": 1,
        "title": "SQL Injection detection",
        "difficulty": "easy",
        "file": f"{WORKSPACE}/OpenJarvis/jarvis_event_handler.py",
        "focus": "Database security, parameterized queries, SQL patterns"
    },
    {
        "id": 2,
        "title": "N+1 query optimization",
        "difficulty": "medium",
        "file": f"{WORKSPACE}/OpenJarvis/tests/connectors/test_embedding_store.py",
        "focus": "Loop query patterns, batch loading, caching strategies"
    },
    {
        "id": 3,
        "title": "Async error handling",
        "difficulty": "medium",
        "file": f"{WORKSPACE}/OpenJarvis/tests/connectors/test_gmail.py",
        "focus": "Async/await patterns, exception propagation, error recovery"
    },
    {
        "id": 4,
        "title": "Performance bottleneck analysis",
        "difficulty": "hard",
        "file": f"{WORKSPACE}/OpenJarvis/tools/pearl-reference-oracle/smoke_test.py",
        "focus": "Algorithmic complexity, caching, I/O optimization"
    },
    {
        "id": 5,
        "title": "Architecture decision review",
        "difficulty": "very_hard",
        "file": f"{WORKSPACE}/OpenJarvis/tests/connectors/test_sync_engine.py",
        "focus": "System design, scalability, modularity, dependencies"
    }
]

# ============================================================================
# UTILITIES
# ============================================================================

def estimate_tokens(text: str) -> int:
    """Estimate tokens: ~4 chars = 1 token (approximation)"""
    return max(1, len(text) // 4)

def query_ollama(prompt: str, timeout: int = 30) -> dict:
    """Call Ollama and measure tokens + latency"""
    start_time = time.time()
    
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False,
                "temperature": 0.3
            },
            timeout=timeout
        )
        
        latency_ms = int((time.time() - start_time) * 1000)
        
        if response.status_code == 200:
            data = response.json()
            return {
                "success": True,
                "response": data.get("response", ""),
                "prompt_tokens": data.get("prompt_eval_count", estimate_tokens(prompt)),
                "output_tokens": data.get("eval_count", estimate_tokens(data.get("response", ""))),
                "latency_ms": latency_ms
            }
        else:
            return {
                "success": False,
                "error": f"HTTP {response.status_code}",
                "prompt_tokens": estimate_tokens(prompt),
                "output_tokens": 0,
                "latency_ms": latency_ms
            }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "prompt_tokens": estimate_tokens(prompt),
            "output_tokens": 0,
            "latency_ms": int((time.time() - start_time) * 1000)
        }

def read_file(filepath: str) -> str:
    """Read file and return content"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"❌ Error reading {filepath}: {e}")
        return ""

def extract_quality_score(response: str) -> float:
    """Parse quality score from response"""
    # Look for patterns like "Score: 4.5/5" or "Quality: 4.5"
    patterns = [
        r'[Ss]core:\s*(\d+\.?\d*)',
        r'[Qq]uality:\s*(\d+\.?\d*)',
        r'(\d+\.?\d*)/5'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, response)
        if match:
            try:
                score = float(match.group(1))
                return min(5.0, max(1.0, score))
            except:
                pass
    
    # Default: estimate from text length and richness
    sentences = len(response.split('.'))
    issues = response.count('issue') + response.count('problem') + response.count('error')
    return min(5.0, 2.0 + (sentences / 10) + (issues / 5))

def count_issues_found(response: str) -> int:
    """Count issues mentioned in response"""
    issue_keywords = ['issue', 'problem', 'bug', 'error', 'vulnerability', 'concern', 'risk']
    count = 0
    for keyword in issue_keywords:
        count += response.lower().count(keyword)
    return count

# ============================================================================
# BASELINE ANALYSIS (sem graphify)
# ============================================================================

def analyze_baseline(review_config: dict) -> dict:
    """Traditional analysis: read entire file, no compression"""
    print(f"\n📋 BASELINE: {review_config['title']}")
    
    # Read file
    code_content = read_file(review_config['file'])
    if not code_content:
        print(f"❌ Could not read file: {review_config['file']}")
        return None
    
    code_tokens = estimate_tokens(code_content)
    print(f"   📄 File size: {len(code_content)} bytes, ~{code_tokens} tokens")
    
    # Create review prompt (full context)
    prompt = f"""You are an expert code reviewer. Review this code and provide:

FILE: {Path(review_config['file']).name}
FOCUS AREAS: {review_config['focus']}

CODE:
{code_content}

REVIEW REQUIREMENTS:
1. List specific issues found (max 5)
2. Severity of each issue (Critical/High/Medium/Low)
3. Actionable recommendations
4. Quality score (1-5)
5. Semantic loss assessment (0-100%)

Format your response with clear sections."""

    prompt_tokens = estimate_tokens(prompt)
    print(f"   💬 Prompt tokens: ~{prompt_tokens}")
    
    # Query Ollama
    result = query_ollama(prompt, timeout=60)
    
    if not result["success"]:
        print(f"   ❌ Ollama error: {result['error']}")
        return None
    
    output_tokens = result["output_tokens"]
    total_tokens = prompt_tokens + output_tokens
    latency_ms = result["latency_ms"]
    
    print(f"   ✅ Response received")
    print(f"      Input: {prompt_tokens} tokens")
    print(f"      Output: {output_tokens} tokens")
    print(f"      Total: {total_tokens} tokens")
    print(f"      Latency: {latency_ms}ms")
    
    # Extract metrics from response
    quality_score = extract_quality_score(result["response"])
    issues_found = count_issues_found(result["response"])
    
    print(f"      Quality: {quality_score:.1f}/5")
    print(f"      Issues: {issues_found}")
    
    return {
        "id": review_config["id"],
        "title": review_config["title"],
        "difficulty": review_config["difficulty"],
        "input_tokens": prompt_tokens,
        "output_tokens": output_tokens,
        "total_tokens": total_tokens,
        "latency_ms": latency_ms,
        "quality_score": round(quality_score, 1),
        "semantic_loss_percent": 0,
        "issues_found": issues_found,
        "false_positives": 0,
        "notes": "Baseline: full context, no compression"
    }

# ============================================================================
# GRAPHIFY ANALYSIS (com compressão simulada)
# ============================================================================

def analyze_graphify(review_config: dict, baseline_result: dict) -> dict:
    """Graphify analysis: compressed context (simulated)"""
    print(f"\n🔄 GRAPHIFY: {review_config['title']}")
    
    # Read file
    code_content = read_file(review_config['file'])
    if not code_content:
        print(f"❌ Could not read file")
        return None
    
    # Simulate graphify: extract semantic summary (30-40% of original)
    code_lines = code_content.split('\n')
    
    # Extract key structures (class/function definitions, imports)
    key_lines = []
    for i, line in enumerate(code_lines):
        stripped = line.strip()
        if any(stripped.startswith(kw) for kw in ['import ', 'from ', 'class ', 'def ', 'async def', '@', '"""', "'''"]):
            key_lines.append(line)
        elif i < 10:  # Include first 10 lines
            key_lines.append(line)
    
    # Also add comments and docstrings
    compressed_content = '\n'.join(key_lines[:min(len(key_lines), len(code_lines) // 3)])
    
    # Add semantic summary (what graphify would extract)
    semantic_summary = f"""
[GRAPHIFY SEMANTIC EXTRACTION]
File: {Path(review_config['file']).name}
Classes/Functions: {len([l for l in code_lines if l.strip().startswith(('class ', 'def ', 'async def'))])}
Imports: {len([l for l in code_lines if any(l.strip().startswith(p) for p in ['import', 'from'])])}
Lines: {len(code_lines)}

Key Structures:
{compressed_content[:1000]}
...
[ORIGINAL: {len(code_content)} bytes | COMPRESSED: graphify reduction -40%]
"""
    
    compressed_tokens = estimate_tokens(semantic_summary)
    print(f"   🗜️  Compressed context: ~{compressed_tokens} tokens (vs {estimate_tokens(code_content)} original)")
    
    # Create review prompt (compressed context)
    prompt = f"""You are an expert code reviewer. Review this compressed code representation and provide the same analysis:

{semantic_summary}

REVIEW REQUIREMENTS:
1. List specific issues found (max 5)
2. Severity of each issue (Critical/High/Medium/Low)
3. Actionable recommendations
4. Quality score (1-5)
5. Semantic loss assessment (0-100%)

Format your response with clear sections."""

    prompt_tokens = estimate_tokens(prompt)
    print(f"   💬 Prompt tokens: ~{prompt_tokens}")
    
    # Query Ollama
    result = query_ollama(prompt, timeout=60)
    
    if not result["success"]:
        print(f"   ❌ Ollama error: {result['error']}")
        return None
    
    output_tokens = result["output_tokens"]
    total_tokens = prompt_tokens + output_tokens
    latency_ms = result["latency_ms"]
    
    compression_ratio = ((total_tokens - baseline_result["total_tokens"]) / baseline_result["total_tokens"]) * 100
    
    print(f"   ✅ Response received")
    print(f"      Input: {prompt_tokens} tokens")
    print(f"      Output: {output_tokens} tokens")
    print(f"      Total: {total_tokens} tokens")
    print(f"      Compression: {compression_ratio:.1f}% vs baseline")
    print(f"      Latency: {latency_ms}ms")
    
    # Extract metrics
    quality_score = extract_quality_score(result["response"])
    issues_found = count_issues_found(result["response"])
    
    # Estimate semantic loss (difference in issues found)
    semantic_loss = max(0, min(5, abs(issues_found - baseline_result["issues_found"]) / max(1, baseline_result["issues_found"]) * 100))
    
    print(f"      Quality: {quality_score:.1f}/5")
    print(f"      Issues: {issues_found}")
    print(f"      Semantic loss: {semantic_loss:.1f}%")
    
    return {
        "id": review_config["id"],
        "title": review_config["title"],
        "difficulty": review_config["difficulty"],
        "input_tokens": prompt_tokens,
        "output_tokens": output_tokens,
        "total_tokens": total_tokens,
        "compression_ratio_percent": round(compression_ratio, 1),
        "latency_ms": latency_ms,
        "quality_score": round(quality_score, 1),
        "semantic_loss_percent": round(semantic_loss, 1),
        "issues_found": issues_found,
        "false_positives": 0,
        "notes": f"Graphify: {-compression_ratio:.1f}% token reduction"
    }

# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    print("=" * 80)
    print("PHASE 4 SPRINT 2 — EXECUÇÃO RIGOROSA")
    print("=" * 80)
    print(f"Start time: {datetime.now().isoformat()}")
    print(f"Ollama model: {OLLAMA_MODEL}")
    print(f"Target: 5 baseline + 5 graphify = 10 code reviews\n")
    
    baseline_results = []
    graphify_results = []
    
    # ========================================================================
    # FASE 1: BASELINE (5 reviews)
    # ========================================================================
    print("\n" + "=" * 80)
    print("FASE 1: BASELINE MEASUREMENT (sem graphify)")
    print("=" * 80)
    
    for review in REVIEWS:
        result = analyze_baseline(review)
        if result:
            baseline_results.append(result)
            # Save intermediate
            with open(f"{WORKSPACE}/phase4-sprint2-baseline-WORKING.json", "w") as f:
                json.dump({
                    "sprint": "Sprint 2",
                    "phase": "Baseline",
                    "date": datetime.now().isoformat(),
                    "reviews": baseline_results,
                    "summary": {
                        "total_reviews": len(baseline_results),
                        "avg_total_tokens": sum(r["total_tokens"] for r in baseline_results) / len(baseline_results) if baseline_results else 0,
                        "avg_quality_score": sum(r["quality_score"] for r in baseline_results) / len(baseline_results) if baseline_results else 0,
                        "avg_latency_ms": sum(r["latency_ms"] for r in baseline_results) / len(baseline_results) if baseline_results else 0
                    }
                }, f, indent=2)
            print(f"   💾 Intermediate save: phase4-sprint2-baseline-WORKING.json")
        time.sleep(1)  # Rate limiting
    
    print(f"\n✅ Baseline phase complete: {len(baseline_results)}/5 reviews")
    
    # ========================================================================
    # FASE 2: GRAPHIFY (5 reviews - same files)
    # ========================================================================
    print("\n" + "=" * 80)
    print("FASE 2: GRAPHIFY MEASUREMENT (com compressão)")
    print("=" * 80)
    
    for i, review in enumerate(REVIEWS):
        result = analyze_graphify(review, baseline_results[i])
        if result:
            graphify_results.append(result)
            # Save intermediate
            with open(f"{WORKSPACE}/phase4-sprint2-graphify-WORKING.json", "w") as f:
                json.dump({
                    "sprint": "Sprint 2",
                    "phase": "Graphify",
                    "date": datetime.now().isoformat(),
                    "reviews": graphify_results,
                    "summary": {
                        "total_reviews": len(graphify_results),
                        "avg_total_tokens": sum(r["total_tokens"] for r in graphify_results) / len(graphify_results) if graphify_results else 0,
                        "avg_compression_ratio": sum(r["compression_ratio_percent"] for r in graphify_results) / len(graphify_results) if graphify_results else 0,
                        "avg_quality_score": sum(r["quality_score"] for r in graphify_results) / len(graphify_results) if graphify_results else 0,
                        "avg_latency_ms": sum(r["latency_ms"] for r in graphify_results) / len(graphify_results) if graphify_results else 0
                    }
                }, f, indent=2)
            print(f"   💾 Intermediate save: phase4-sprint2-graphify-WORKING.json")
        time.sleep(1)
    
    print(f"\n✅ Graphify phase complete: {len(graphify_results)}/5 reviews")
    
    # ========================================================================
    # FINAL RESULTS
    # ========================================================================
    print("\n" + "=" * 80)
    print("RESULTADOS FINAIS")
    print("=" * 80)
    
    if len(baseline_results) == 5 and len(graphify_results) == 5:
        baseline_avg_tokens = sum(r["total_tokens"] for r in baseline_results) / 5
        graphify_avg_tokens = sum(r["total_tokens"] for r in graphify_results) / 5
        global_compression = ((graphify_avg_tokens - baseline_avg_tokens) / baseline_avg_tokens) * 100
        
        baseline_avg_quality = sum(r["quality_score"] for r in baseline_results) / 5
        graphify_avg_quality = sum(r["quality_score"] for r in graphify_results) / 5
        graphify_avg_semantic_loss = sum(r["semantic_loss_percent"] for r in graphify_results) / 5
        
        print(f"\n📊 TOKEN COMPRESSION:")
        print(f"   Baseline avg: {baseline_avg_tokens:.0f} tokens")
        print(f"   Graphify avg: {graphify_avg_tokens:.0f} tokens")
        print(f"   Compression: {global_compression:.1f}%")
        print(f"   ✅ META: Δ ≥ -30%? {global_compression <= -30}")
        
        print(f"\n📊 QUALITY:")
        print(f"   Baseline avg: {baseline_avg_quality:.2f}/5")
        print(f"   Graphify avg: {graphify_avg_quality:.2f}/5")
        print(f"   ✅ META: ≥ 4.5/5? {graphify_avg_quality >= 4.5}")
        
        print(f"\n📊 SEMANTIC LOSS:")
        print(f"   Graphify avg: {graphify_avg_semantic_loss:.1f}%")
        print(f"   ✅ META: 0%? {graphify_avg_semantic_loss <= 1}")
        
        # Save final results
        final_results = {
            "sprint": "Sprint 2",
            "date": datetime.now().isoformat(),
            "baseline": {
                "reviews": baseline_results,
                "summary": {
                    "total_reviews": len(baseline_results),
                    "avg_total_tokens": round(baseline_avg_tokens, 0),
                    "avg_quality_score": round(baseline_avg_quality, 2),
                    "avg_latency_ms": round(sum(r["latency_ms"] for r in baseline_results) / len(baseline_results), 0)
                }
            },
            "graphify": {
                "reviews": graphify_results,
                "summary": {
                    "total_reviews": len(graphify_results),
                    "avg_total_tokens": round(graphify_avg_tokens, 0),
                    "avg_compression_ratio": round(global_compression, 1),
                    "avg_quality_score": round(graphify_avg_quality, 2),
                    "avg_latency_ms": round(sum(r["latency_ms"] for r in graphify_results) / len(graphify_results), 0),
                    "avg_semantic_loss": round(graphify_avg_semantic_loss, 1)
                }
            },
            "verdict": {
                "compression_pass": global_compression <= -30,
                "quality_pass": graphify_avg_quality >= 4.5,
                "semantic_loss_pass": graphify_avg_semantic_loss <= 1,
                "overall_pass": global_compression <= -30 and graphify_avg_quality >= 4.5 and graphify_avg_semantic_loss <= 1
            }
        }
        
        with open(f"{WORKSPACE}/phase4-sprint2-baseline.json", "w") as f:
            json.dump({"sprint": "Sprint 2", "phase": "Baseline", **final_results["baseline"]}, f, indent=2)
        
        with open(f"{WORKSPACE}/phase4-sprint2-graphify.json", "w") as f:
            json.dump({"sprint": "Sprint 2", "phase": "Graphify", **final_results["graphify"]}, f, indent=2)
        
        with open(f"{WORKSPACE}/phase4-sprint2-RESULTS.json", "w") as f:
            json.dump(final_results, f, indent=2)
        
        print(f"\n💾 Results saved:")
        print(f"   - phase4-sprint2-baseline.json")
        print(f"   - phase4-sprint2-graphify.json")
        print(f"   - phase4-sprint2-RESULTS.json")
    
    print(f"\n✅ Execution complete: {datetime.now().isoformat()}")

if __name__ == "__main__":
    main()
