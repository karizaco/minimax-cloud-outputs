---
artifact: breadth
read: end-of-day (cron #09, 18:30 ET) — NOT the intraday snapshot (cron #10)
fire_time_et: "2026-11-10 18:30 ET"
data_date: "2026-11-10 — the settled close of the cron day; this breadth read is NOT T+1 (the SCREEN metrics in daily-sweep.md are shibui T+1 = 2026-11-09)"
breadth_universe: "NYSE/NASDAQ/AMEX, type in {stock, dr}, market_cap_basic > $10B (TradingView scanner, USD) — 1114 names; totalCount 1114 = rows fetched, no truncation"
vix_quote_time: "2026-11-10 16:15:01 ET (Cboe delayed-quote CDN, two pulls 20 s apart — identical)"
vix_pair: "VIX 19.46 / VIX3M 20.64 — single pair, used everywhere in this document"
cross_reference: "intraday counterpart: daily-screens/2026-11-10/breadth-snapshot.md (cron #10, 14:00 ET)"
size_cut_pct: 0
uncertainty: false
late_cycle: false
---

# Breadth & Regime — End-of-Day — Tuesday, 10 November 2026 (cron #09, 18:30 ET)

Settled close of 2026-11-10. Numbers below are computed from the **cron day's** settled tape (TradingView scanner post-close, `close` = the official 16:00 ET print). The screen metrics in `daily-sweep.md` describe the **previous** session (shibui is T+1) and are not blended into this file.

## TL;DR

- **Breadth gave back Friday's repair**: 62.03% of the 1114-name large-cap universe closed above its 20-DMA (the 2026-11-09 read was 68.01% of 1113 names), and advance/decline was **428 / 678 / 8** (ratio 0.63).
- **The divergence is still the story**: 62.03% of large caps above their 20-DMA vs **40% of the five index ETFs above theirs** — **+22.0 pp, BROAD**. The average stock is still healthier than the index.
- **Caveat that changes how you read it**: the volatility pair came in at **VIX 19.46 / VIX3M 20.64** (ratio 0.9428 < 1, so `uncertainty: false`), but QQQ is **-6.20% below its own 50-DMA** — the weakest leg of the tape is now further from its trend than on any day this month.

## Breadth — 2026-11-10 settled session

| Metric | Value |
|---|---|
| Universe | 1114 names (NYSE/NASDAQ/AMEX, type stock+dr, market cap > $10B) |
| Above 20-DMA | **62.03%** (691 / 1114) |
| Above 50-DMA | 53.68% (598 / 1114) |
| Above 200-DMA | 49.55% (552 / 1114) |
| Advance / decline / unchanged | **428 / 678 / 8** — ratio 0.63, net **-250** |
| Median name | -0.31%  ·  mean -0.50% |
| Move distribution | ≥ +5%: 5 · +2..5%: 66 · 0..2%: 365 · −2..0: 498 · −5..−2: 149 · ≤ −5%: 31 |

## Participation — the advance/decline tally

Computed on the **same 1114-name population** as the breadth percentage, from the settled session: **428 advancing, 678 declining, 8 unchanged** (sums to the published universe count — no separate quote-only denominator is mixed in). Net advances **-250**, ratio **0.63**.

This is a genuine per-name tally from the settled close, not an RSP-vs-SPY cap-weight proxy.

## Breadth divergence — broad market vs index ETFs

| Field | Value |
|---|---|
| `breadth_divergence` | **+22.03 pp** |
| band | **BROAD** (≥ +15 pp) |
| large-cap % above 20-DMA | 62.03% |
| index ETFs above their 20-DMA | 40% (2 of 5) |

A **BROAD** divergence means the average large cap is materially healthier than the index — participation is broader than the headline index, and the index's own posture is the weak leg. It is NOT a megacap-led advance.

## Index positioning — distance from the 50-DMA

| ETF | Close | Chg | 20-DMA | 50-DMA | 200-DMA | vs 50-DMA | ATR% |
|---|---|---|---|---|---|---|---|
| SPY | 749.92 | -0.37% | 760.69 | 765.00 | 730.99 | **-1.97%** | 1.46% |
| QQQ | 674.76 | -0.68% | 700.86 | 719.39 | 681.42 | **-6.20%** | 2.38% |
| RSP | 220.88 | -0.03% | 217.49 | 214.82 | 208.51 | **+2.82%** | 1.28% |
| QQQE | 115.12 | -0.36% | 117.09 | 118.87 | 113.47 | **-3.15%** | 1.75% |
| IWM | 280.58 | -0.68% | 277.27 | 281.58 | 279.17 | **-0.35%** | 1.79% |

`atr_extensions` in `_regime.json` carries these five extension values. The map is non-empty, so `late_cycle` was genuinely computed: **no index is more than 6% above its 50-DMA** (the extreme is RSP at +2.82%), so `late_cycle: false`.

## Volatility — single pair, settled

| Contract | Value | Prior close | Change | Quote time |
|---|---|---|---|---|
| VIX | **19.46** | 19.92 | -0.46 (-2.3%) | 2026-11-10 16:15:01 ET |
| VIX3M | **20.64** | 20.85 | -0.21 (-1.0%) | 2026-11-10 16:15:01 ET |

Source: Cboe delayed-quote CDN. Pulled twice, 20 s apart — **identical both times** (`vix_stable: true`). Ratio VIX/VIX3M = **0.9428** → `uncertainty: false` (the flag fires above 1.0). Front-end vol fell only -2.3% from Monday's 19.92 — the Monday vol crush did not extend, and the term structure is still in contango.

## Regime

| Flag | Value | Rule |
|---|---|---|
| `size_cut_pct` | **0** | size cut only when the index is below its 20-DMA **and** breadth < 40% — breadth is 62.03% |
| `uncertainty` | **false** | VIX/VIX3M = 0.9428 ≤ 1 |
| `late_cycle` | **false** | no index ETF is > 6% above its 50-DMA (max +2.82%, RSP) |
| `index_below_20sma` | **true** | only 2 of 5 index ETFs are above their 20-DMA (40%) |

Payload: `daily-screens/2026-11-10/_regime.json` (flat schema v2, all eight keys present, `atr_extensions` non-empty).

## Flags

- **QQQ is -6.20% below its 50-DMA** — the largest extension of the five, and the weakest leg of the tape. It is also the only index below both its 20-DMA and its 200-DMA.
- **QQQE is -3.15% below its 50-DMA** — the second leg of the same weakness, and the equal-weight tech book is not participating either.
- **Advance/decline is 0.63** (428 up vs 678 down) — a negative tape, and it moved against Friday's 5.15. Breadth at 62.03% is still above the 40% size-cut trigger, but the direction has turned.
- **VIX/VIX3M ratio is 0.9428** — normal contango, but the VIX only fell -2.3% on a day the index ETFs fell, so the volatility market did not price the breadth deterioration.

## Method, source health & caveats

| Source | What it served | Status |
|---|---|---|
| TradingView scanner (`america/scan`) | the 1114-name universe, close/change/SMA20/SMA50/SMA200/ATR, index ETFs, sector RS | ok — `totalCount 1114` = rows fetched (no truncation) |
| TradingView scanner | the FRESH screen book (4% breakout, EP9M, 10% gap, volume breakout) on the same settled bar | ok — 3820-name universe, totalCount asserted |
| Cboe delayed-quote CDN | VIX / VIX3M pair, two pulls | ok |
| shibui over the MCP bridge (T+1 cross-check only) | 2026-11-09 breadth, 911 names | ok |
| MCP availability probe | `catalog_ok total=135 finance_tools=0`; bridge packs `tradier,fmp,market-recap` | ok (no finance MCP registered — expected) |

- **Two different populations by design.** The published numbers here are the TradingView 1114-name large-cap universe at the cron day's close; the shibui cross-check below is 911 names on 2026-11-09. The market-cap sources differ (`market_cap_basic` vs `valuation.market_cap`), so the two are **not two readings of one series** and must not be compared as if they were.
- **No 1-year breadth percentile is published in this file.** Computing it needs the trailing session series for this universe, which this routine does not pull. A level without its percentile is published here because the end-of-day contract does not require it; do not read it as "normal" or "extreme".
- **The advance/decline tally is computed on the breadth population**, so advancing + declining + unchanged equals the published universe count (1114). No quote-only denominator is mixed in.
- **Day-alignment assertion passed**: SPY's implied previous close from the scanner (749.92 / 0.9963 = 752.69) matches shibui's settled 2026-11-09 close (752.69); QQQ matches exactly (679.35). The scanner is on the 2026-11-10 session, not a stale one.

## Cross-check — shibui, T+1 (data date 2026-11-09)

shibui had not yet ingested 2026-11-10 at the 18:30 ET fire, so its newest settled session is **2026-11-09**. It is published as a cross-check, not as the number of record.

| Metric | TradingView (11-10 close, 1114 names) | shibui (11-09, 911 names) |
|---|---|---|
| % above 20-DMA | 62.03% | 67.84% |
| index ETFs above 20-DMA | 40% (2/5) | 40% (2/5) |
| index ETFs above 50-DMA | 20% (1/5) | 40% (2/5) |
| SPY vs 50-DMA | -1.97% | -1.65% |
| RSP vs 50-DMA | +2.82% | +2.87% |
| QQQ vs 50-DMA | -6.20% | -5.68% |
| QQQE vs 50-DMA | -3.15% | -2.91% |
| IWM vs 50-DMA | -0.35% | +0.24% |

The two reads are one trading session apart and describe the same market at two points in time: Monday's shibui read was the post-rally picture (67.84% above the 20-DMA), today's TradingView read is what the breadth gave back (62.03%, and a negative advance/decline line). The index ETFs' 50-DMA extensions are essentially unchanged and slightly WORSE for QQQ (-6.20% vs -5.68%), which is the one number that moved in the direction that matters.
