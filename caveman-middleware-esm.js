/**
 * CAVEMAN COMPRESSION MIDDLEWARE (ESM version)
 * Reduces token usage by ~40% with aggressive text compression
 */

class CavemanMiddleware {
  constructor(options = {}) {
    this.mode = options.mode || 'aggressive';
    this.verbose = options.verbose || false;
  }

  async compressInput(message, tools = null, systemPrompt = null) {
    const startTokens = this._estimateTokens(message);
    const compressed = {
      message: this._compressText(message, true),
      tools,
      system_prompt: systemPrompt,
      metadata: {
        original_tokens: startTokens,
        compressed_tokens: 0,
        compression_ratio: 0
      }
    };

    const endTokens = this._estimateTokens(
      compressed.message + (systemPrompt || '')
    );
    compressed.metadata.compressed_tokens = endTokens;
    compressed.metadata.compression_ratio = (
      (startTokens - endTokens) / startTokens * 100
    ).toFixed(1);

    if (this.verbose) {
      console.log(`[CAVEMAN] Input: ${startTokens} → ${endTokens} tokens (-${compressed.metadata.compression_ratio}%)`);
    }

    return compressed;
  }

  async compressOutput(response) {
    if (typeof response === 'string') {
      return this._compressText(response, false);
    }
    return {
      ...response,
      text: response.text ? this._compressText(response.text, false) : response.text
    };
  }

  _compressText(text, isPrompt) {
    if (!text) return '';

    let result = text
      // Remove excessive whitespace
      .replace(/\s+/g, ' ')
      // Remove common filler
      .replace(/\b(actually|basically|essentially|literally|quite|rather|somewhat)\b/gi, '')
      .replace(/\b(you know|i think|in my opinion|seems like)\b/gi, '')
      // Collapse repeated phrases
      .replace(/\b(\w+)(\s+\1)+\b/g, '$1');

    if (!isPrompt) {
      // Remove markdown from output
      result = result
        .replace(/\*\*/g, '')
        .replace(/^[-*]\s/gm, '')
        .replace(/#+\s/g, '');
    }

    return result.trim().slice(0, 2000);
  }

  _estimateTokens(text) {
    if (!text) return 0;
    // Rough estimate: 1 token ≈ 4 chars for English
    return Math.ceil(text.length / 4);
  }
}

export default CavemanMiddleware;
