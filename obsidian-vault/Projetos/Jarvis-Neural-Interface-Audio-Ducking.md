# Jarvis Neural Interface — Audio Ducking

**Projeto:** Jarvis Neural Interface  
**Arquivo:** `jarvis-bridge-v4.js`  
**Data:** 23/08/2026  
**Branch:** `fix/ducking-compound-threshold`

---

## O que é Audio Ducking

Ducking é a técnica de reduzir o volume do Spotify temporariamente enquanto o Jarvis fala (TTS), e restaurá-lo logo depois. O afplay (que toca o TTS) não é afetado — roda sempre no volume cheio do sistema.

---

## Fluxo Completo — clap_phrase

| Momento | Volume Spotify | O que acontece |
|---|---|---|
| Antes de `playSpotify()` | forçado para `preduckedSpotifyVolume` (100) | garante que a música inicia no volume correto |
| Música tocando (3s) | **100** | `sleep(3000)` — janela de música em volume cheio |
| `duckVolume()` dentro de `say()` | lê 100 → salva 100 → seta **40** | DUCK_RATIO = 0.4 |
| Jarvis falando (TTS) | **40** | música baixa, Jarvis audível |
| `unDuckVolume()` após TTS | restaura para **100** | `preduckedSpotifyVolume` |

---

## Variáveis e Constantes

```js
const DUCK_RATIO = 0.4;           // Spotify cai para 40% durante TTS
let preduckedSpotifyVolume = 100; // volume salvo antes do duck (default: 100)
```

---

## Funções Principais

### `duckVolume()`
- Lê o volume atual do Spotify
- **Só salva** `preduckedSpotifyVolume` se o volume atual está **acima do threshold** (50)
  - Evita compound ducking: se já está em 40%, não salva 40 como "original"
  - `duckThreshold = Math.floor(100 * DUCK_RATIO) + 10 = 50`
- Seta volume para `preduckedSpotifyVolume * DUCK_RATIO`

### `unDuckVolume()`
- Restaura o volume do Spotify para `preduckedSpotifyVolume`

### `restoreSpotifyVolume()` — chamada no startup
- Garante que o Spotify não ficou preso em volume ducked após restart do bridge
- Threshold: `vol < 70` (qualquer volume abaixo de 70 é suspeito)
- Restaura para `max(preduckedSpotifyVolume, 80)` — mínimo de 80 garantido

---

## Bugs Corrigidos (23/08/2026)

### Bug 1 — Compound Ducking
**Problema:** `listen/start` chamava `duckVolume()` e depois `say()` chamava `duckVolume()` novamente.  
- 1ª chamada: salva 100, seta 40  
- 2ª chamada: lia 40, salvava **40** como "original", setava 16  
- `unDuckVolume()` restaurava para 40, não para 100  

**Fix:** `duckVolume()` só atualiza `preduckedSpotifyVolume` se volume > threshold (50).

### Bug 2 — Threshold errado no startup
**Problema:** `restoreSpotifyVolume()` verificava `vol < 30`.  
Com `DUCK_RATIO = 0.4`, volume ducked = 40 — nunca passava no teste.  

**Fix:** threshold `30 → 70`, mínimo garantido de 80 no restore.

### Bug 3 — Música iniciando baixa no clap_phrase
**Problema:** `playSpotify()` iniciava a música no volume em que o Spotify estava (poderia ser 40 de duck anterior).  

**Fix:** antes de `playSpotify()`, força `set sound volume to ${preduckedSpotifyVolume}`.

---

## Arquitetura de Audio

```
[Spotify]  ←── volume controlado por AppleScript (ducking)
[afplay]   ←── TTS do Jarvis, toca no volume cheio do sistema (não afetado)
[Bridge]   ←── orquestra duck/unduck via say() + duckVolume()/unDuckVolume()
```

---

## Links

- Branch: `fix/ducking-compound-threshold`
- Repositório: `Team-Iron-Solutions/jarvis-neural-interface`
- Bridge: `jarvis-neural-interface/bridge/jarvis-bridge-v4.js`
