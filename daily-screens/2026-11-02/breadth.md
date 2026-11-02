---
fire_time_et: 2026-11-02 18:30 ET
data_date: 2026-10-30 (shibui breadth feed; T+1 — shibui has not ingested the 2026-11-02 session)
breadth_universe: NYSE/NASDAQ/AMEX, market_cap > $10B, close > $3, 900 names
vix_quote_time: 2026-11-02T16:15:01 ET (CBOE delayed-quote CDN, settled cash close; VIX3M 2026-11-02T16:15:01 ET)
cross_reference: intraday counterpart: daily-screens/2026-11-02/breadth-snapshot.md (cron #10, 14:00 ET)
volatility_pair: VIX 21.15 / VIX3M 21.6 (ratio 0.9792) — single pair, used everywhere in this file
---

# Breadth & regime — end-of-day read

**Cron #09 stock_screener_daily_sweep_18_30** · fire 2026-11-02 18:30 ET · generated 2026-11-02 18:37:12 ET

## Self-description

| Field | Value |
|---|---|
| Fire time (ET) | 2026-11-02 18:30 ET |
| Breadth data date | 2026-10-30 — shibui feed is **T+1**; the 2026-11-02 session is not yet ingested |
| Breadth universe | NYSE/NASDAQ/AMEX, market cap > $10B, close > $3 — **900 names** |
| % above 20-DMA | **63.89%** |
| % above 50-DMA | 56.22% |
| Index ETFs above their own 20-DMA | 40% of 5 (SPY, RSP, QQQ, QQQE, IWM) |
| VIX / VIX3M | 21.15 / 21.6 = 0.9792 (+8.91% / +3.95%) |
| VIX quote time / feed | 2026-11-02T16:15:01 ET · CBOE delayed-quote CDN (settled close) |
| Cross-reference | intraday counterpart: daily-screens/2026-11-02/breadth-snapshot.md (cron #10, 14:00 ET) |

> The breadth percentages describe the **2026-10-30** session (shibui's latest ingested bar). The volatility pair is the **2026-11-02** settled close — one pair only, quoted consistently throughout this artifact. The two are one session apart by construction, not by accident.

## Regime flags (skill contract)

| Flag | Value | Meaning |
|---|---|---|
| `size_cut_pct` | 0 | 50 only when the indices sit below their 20-DMA **and** large-cap breadth < 40% |
| `uncertainty` | false | VIX/VIX3M > 1.0 (front-end stress vs the long end) |
| `late_cycle` | false | any index ETF more than 6% above its 50-DMA |

Size-cut is **not** triggered: the index ETFs are in a weak posture (only 40% of the 5 sit above their 20-DMA on 2026-10-30) but large-cap breadth is 63.9%, well above the 40% gate.

## Index extension (shibui, 2026-10-30)

| Symbol | Close | SMA20 | SMA50 | ATR% | ATR% 252d median | % vs SMA50 | ATR ext. multiple |
|---|---|---|---|---|---|---|---|
| SPY | 755.72 | 770.47 | 767.49 | 1.022 | 7.715 | -1.53 | 0.946 |
| RSP | 218.31 | 214.89 | 215.05 | 0.937 | 2.074 | 1.52 | 0.900 |
| QQQ | 690.49 | 728.19 | 725.00 | 1.841 | 10.403 | -4.76 | 1.143 |
| QQQE | 116.29 | 119.50 | 119.94 | 1.395 | 1.446 | -3.04 | 1.079 |
| IWM | 279.33 | 277.41 | 284.27 | 1.367 | 4.543 | -1.74 | 0.813 |

No index ETF is more than 6% above its 50-DMA, so `late_cycle` is false. The ATR-extension multiples (current ATR% ÷ 252-session median ATR%) run 0.81x–1.14x — no stretched index.

## Session close for reference (2026-11-02, CBOE delayed-quote CDN)

| Symbol | Close | Change | | Symbol | Close | Change |
|---|---|---|---|---|---|---|
| _SPX 7541.40 -0.51% |  | XLK 174.22 -2.95% |  |
| SPY 752.10 -0.48% |  | XLF 57.56 +1.86% |  |
| QQQ 681.09 -1.36% |  | XLE 67.25 -3.96% |  |
| RSP 219.98 +0.77% |  | XLV 184.60 -0.15% |  |
| IWM 279.14 -0.07% |  | XLI 169.71 +1.38% |  |
| QQQE 115.89 -0.34% |  | XLY 118.16 +2.41% |  |
| DIA 519.34 +0.43% |  | XLP 90.83 +1.58% |  |
| SMH 508.31 -2.71% |  | XLU 43.67 +0.55% |  |
|  | |  | XLRE 43.64 +1.09% |  |
|  | |  | XLB 53.67 +1.76% |  |
|  | |  | XLC 100.26 +0.36% |  |

VIX 21.15 (+8.91%) · VIX3M 21.6 (+3.95%) · ratio 0.9792 · quote time 2026-11-02T16:15:01 ET.

## Source health

| Source | Query / URL | Status |
|---|---|---|
| shibui (MCP bridge) | breadth + ATR SQL, data_date 2026-10-30 | ok |
| shibui (MCP bridge) | 496-ticker indicator/flag pass, data_date 2026-10-30 | ok |
| shibui (MCP bridge) | sweep SQL — stockbee / qullamaggie / peoplewish / CANSLIM | ok |
| TradingView scanner | `POST https://scanner.tradingview.com/america/scan` — 495/496 candidate closes for 2026-11-02 | ok (1 miss: KVUE) |
| CBOE delayed-quote CDN | `https://cdn.cboe.com/api/global/delayed_quotes/quotes/{sym}.json` | ok |
| bridge `market-recap` pack | `get_quotes` | failed: anonymous Pipeworx quota exhausted (50/50) — not a missing source |
| Finviz tier-2 fallback | — | unreachable (Cloudflare 403 from this egress) |

## Method

- Breadth = share of the large-cap universe trading above its own 20-DMA on the shibui session (900 names, NYSE/NASDAQ/AMEX, market cap > $10B, close > $3).
- Index extension uses shibui's `technical_indicators` (sma_20, sma_50, atr_14) joined to `stock_quotes` on (symbol, date).
- The skill's own `compute_regime()` is used verbatim so the flags here and in `_regime.json` cannot drift apart.
- The skill's shipped breadth SQL computes `atr_252d_avg` inside a CTE already filtered to one date, so its partition holds a single row; the true ATR multiple is recomputed here over a real 252-session window.
