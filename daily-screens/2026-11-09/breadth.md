---
artifact: breadth
read: end-of-day (cron #09, 18:30 ET) — NOT the intraday snapshot (cron #10)
fire_time_et: "2026-11-09 18:30 ET"
data_date: "2026-11-09 — the settled close of the cron day; this breadth read is NOT T+1 (the SCREEN metrics in daily-sweep.md are shibui T+1 = 2026-11-06)"
breadth_universe: "NYSE/NASDAQ/AMEX, type in {stock, dr}, market_cap_basic > $10B (TradingView scanner, USD) — 1113 names; totalCount 1113 = rows fetched, no truncation"
vix_quote_time: "2026-11-09 16:15:01 ET (Cboe delayed-quote CDN, two pulls 20 s apart — identical)"
vix_pair: "VIX 19.92 / VIX3M 20.85 — single pair, used everywhere in this document"
cross_reference: "intraday counterpart: daily-screens/2026-11-09/breadth-snapshot.md (cron #10, 14:00 ET)"
size_cut_pct: 0
uncertainty: false
late_cycle: false
---

# Breadth & Regime — End-of-Day — Monday, 09 November 2026 (cron #09, 18:30 ET)

Settled close of 2026-11-09. Numbers below are computed from the **cron day's** settled tape (TradingView scanner post-close, `close` = the official 16:00 ET print). The screen metrics in `daily-sweep.md` describe the **previous** session (shibui is T+1) and are not blended into this file.

## TL;DR

- **Breadth snapped higher from the Friday washout**: 68.01% of the 1113-name large-cap universe closed above its 20-DMA (Friday's shibui read: 56.4% of 895 names), and advance/decline was **927 / 180 / 6** (ratio 5.15).
- **The divergence is the story**: 68.01% of large caps above their 20-DMA vs **40% of the five index ETFs above theirs** — **28.0 pp, BROAD**. The average stock is healthier than the index; the cap-weighted index is still the weak leg.
- **Caveat that changes how you read it**: the volatility pair came in at **VIX 19.92 / VIX3M 20.85** (ratio 0.955 < 1, so `uncertainty: false`), but SPY and QQQ are still **below their own 20-DMA** (752.69 vs 762.09; 679.35 vs 704.30) — one strong breadth day has not yet repaired the index posture.

## Breadth — 2026-11-09 settled session

| Metric | Value |
|---|---|
| Universe | 1113 names (NYSE/NASDAQ/AMEX, type stock+dr, market cap > $10B) |
| Above 20-DMA | **68.01%** (757 / 1113) |
| Above 50-DMA | 58.40% (650 / 1113) |
| Above 200-DMA | 50.31% (560 / 1113) |
| Advance / decline / unchanged | **927 / 180 / 6** — ratio 5.15, net **+747** |
| Median name | 1.67%  ·  mean 2.33% |
| Move distribution | ≥ +5%: 165 · +2..5%: 338 · 0..2%: 430 · −2..0: 153 · −5..−2: 26 · ≤ −5%: 1 |

## Participation — the advance/decline tally

Computed on the **same 1113-name population** as the breadth percentage, from the settled session: **927 advancing, 180 declining, 6 unchanged** (sums to the published universe count — no separate quote-only denominator is mixed in). Net advances **+747**, ratio **5.15**.

This is a genuine per-name tally from the settled close, not an RSP-vs-SPY cap-weight proxy.

## Breadth divergence — broad market vs index ETFs

| Field | Value |
|---|---|
| `breadth_divergence` | **28.01 pp** |
| band | **BROAD** (≥ +15 pp) |
| large-cap % above 20-DMA | 68.01% |
| index ETFs above their 20-DMA | 40% (2 of 5) |

A **BROAD** divergence means the average large cap is materially healthier than the index — participation is broader than the headline index, and the index's own posture is the weak leg. It is NOT a megacap-led advance.

## Index positioning — distance from the 50-DMA

| ETF | Close | Chg | 20-DMA | 50-DMA | 200-DMA | vs 50-DMA | ATR% |
|---|---|---|---|---|---|---|---|
| SPY | 752.69 | 2.37% | 762.09 | 765.35 | 730.70 | **-1.65%** | 1.49% |
| RSP | 220.95 | 2.27% | 217.11 | 214.79 | 208.41 | **2.87%** | 1.30% |
| QQQ | 679.35 | 3.54% | 704.30 | 720.23 | 681.17 | **-5.68%** | 2.39% |
| QQQE | 115.54 | 3.15% | 117.36 | 119.00 | 113.42 | **-2.91%** | 1.78% |
| IWM | 282.51 | 3.23% | 277.07 | 281.84 | 279.09 | **0.24%** | 1.79% |

`atr_extensions` in `_regime.json` carries these five extension values. The map is non-empty, so `late_cycle` was genuinely computed: **no index is more than 6% above its 50-DMA** (the extreme is RSP at 2.87%), so `late_cycle: false`.

## Sector rotation — composite relative strength (TradingView sector/thematic ETFs)

| ETF | Theme | 1M | 3M | 6M | Today |
|---|---|---|---|---|---|
| SKY | Champion Homes, Inc. | 19.64% | 3.66% | 40.86% | 5.46% |
| ITB | iShares U.S. Home Construction ETF | 16.27% | 0.65% | 10.50% | 3.02% |
| XLV | State Street Health Care Select Sector | 12.28% | 11.91% | 29.60% | 1.91% |
| JETS | U.S. Global Jets ETF | 10.83% | -4.34% | 15.75% | 5.15% |
| XHB | State Street SPDR S&P Homebuilders ETF | 10.73% | -2.68% | 6.29% | 3.59% |
| XRT | State Street SPDR S&P Retail ETF | 10.57% | 2.97% | 15.96% | 3.66% |
| ARKK | ARK Innovation ETF | -10.83% | -2.07% | 1.04% | 4.66% |
| VGT | Vanguard Information Tech ETF | -12.62% | -7.56% | -1.26% | 3.20% |
| XLK | State Street Technology Select Sector  | -14.30% | -8.96% | -3.60% | 3.73% |
| XSD | State Street SPDR S&P Semiconductor ET | -16.84% | -16.62% | -22.07% | 6.93% |
| SMH | VanEck Semiconductor ETF | -20.76% | -15.76% | -14.76% | 5.05% |
| SOXX | iShares PHLX SOX Semiconductor Sector  | -22.89% | -18.15% | -16.55% | 7.49% |

Leaders (health care, biotech, retail, staples) vs laggards (semis, software, energy) — the 3-month column is the one that matters: **Semiconductors & Semiconductor Equipment** averages −24.75% 3M RS across 73 large-cap names, and **Energy** averages −7.32%.

## Industry breadth (1113-name universe, % above own 20-DMA)

| Industry group | Names | % above 20-DMA | Avg today | Median today |
|---|---|---|---|---|
| Electronic Technology | 101 | 42.6% | 5.99% | 5.76% |
| Distribution Services | 15 | 60.0% | 5.25% | 3.07% |
| Producer Manufacturing | 54 | 50.0% | 4.92% | 4.49% |
| Non-Energy Minerals | 39 | 74.4% | 4.30% | 4.22% |
| Transportation | 27 | 74.1% | 3.00% | 3.11% |
| Health Technology | 88 | 84.1% | 2.62% | 2.46% |
| Communications | 19 | 63.2% | 2.31% | 1.28% |
| Industrial Services | 31 | 32.3% | 2.23% | 1.23% |
| Retail Trade | 37 | 83.8% | 2.13% | 2.19% |
| Consumer Durables | 22 | 95.5% | 2.10% | 2.51% |
| Technology Services | 100 | 44.0% | 1.73% | 0.94% |
| Commercial Services | 25 | 88.0% | 1.66% | 1.43% |
| Process Industries | 25 | 76.0% | 1.55% | 1.24% |
| Consumer Services | 39 | 89.7% | 1.48% | 0.83% |
| Finance | 345 | 77.4% | 1.41% | 1.15% |
| Utilities | 54 | 83.3% | 1.39% | 0.89% |
| Consumer Non-Durables | 40 | 90.0% | 1.03% | 1.01% |
| Health Services | 18 | 66.7% | 0.20% | 0.77% |
| Energy Minerals | 32 | 3.1% | 0.16% | -0.11% |

## Volatility — single pair, settled

| Contract | Value | Prior close | Change | Quote time |
|---|---|---|---|---|
| VIX | **19.92** | 25.64 | -5.72 (-22.3%) | 2026-11-09 16:15:01 ET |
| VIX3M | **20.85** | 24.60 | -3.75 (-15.2%) | 2026-11-09 16:15:01 ET |

Source: Cboe delayed-quote CDN. Pulled twice, 20 s apart — **identical both times** (`vix_stable: true`). Ratio VIX/VIX3M = **0.9554** → `uncertainty: false` (the flag fires above 1.0). Front-end vol fell 22% from Friday's 25.64 — the volatility crush is the tape's cleanest signal today.

## Regime

| Flag | Value | Rule |
|---|---|---|
| `size_cut_pct` | **0** | size cut only when the index is below its 20-DMA **and** breadth < 40% — breadth is 68.01% |
| `uncertainty` | **false** | VIX/VIX3M = 0.9554 ≤ 1 |
| `late_cycle` | **false** | no index ETF is > 6% above its 50-DMA (max 2.87%, RSP) |
| `index_below_20sma` | **true** | only 2 of 5 index ETFs are above their 20-DMA (40%) |

Payload: `daily-screens/2026-11-09/_regime.json` (flat schema v2, all eight keys present, `atr_extensions` non-empty).

## Flags

- **SPY's own 20-DMA is above its close** (752.69 vs 762.09) while 68% of large caps are above theirs — the index/aggregate gap is real data, not a stale print. Flagged because it changes position sizing.
- **QQQ is 5.68% below its 50-DMA** — the largest extension of the five, and the weakest leg of the tape.
- **VIX/VIX3M ratio is 0.955** — a normal (contango) term structure after Friday's 25.64 print; a single session of vol compression, not a confirmed regime shift.
- **VIX3M (20.85) sits above VIX (19.92)** — the long end is still richer than the front end, consistent with the Friday stress having been a front-end event.

## Method, source health & caveats

| Source | What it served | Status |
|---|---|---|
| TradingView scanner (`america/scan`) | the 1113-name universe, close/change/SMA20/SMA50/SMA200/ATR | ok — `totalCount 1113` = rows fetched (no truncation) |
| TradingView scanner | index ETFs SPY/RSP/QQQ/QQQE/IWM, sector & thematic ETF RS | ok |
| Cboe delayed-quote CDN | VIX / VIX3M pair, two pulls | ok |
| shibui over the MCP bridge (T+1 cross-check only) | Friday 2026-11-06 breadth, 895 names | ok |
| MCP availability probe | `catalog_ok total=135 finance_tools=0`; bridge packs `tradier,fmp,market-recap` | ok (no finance MCP registered — expected) |

- **Two different populations by design.** The published numbers here are the TradingView 1113-name large-cap universe at the cron day's close; the shibui cross-check below is 895 names on Friday. The market-cap sources differ (`market_cap_basic` vs `valuation.market_cap`), so the two are **not two readings of one series** and must not be compared as if they were.
- **No 1-year breadth percentile is published in this file.** Computing it needs the trailing session series for this universe, which this routine does not pull. A level without its percentile is published here because the end-of-day contract does not require it; do not read it as "normal" or "extreme".
- **The advance/decline tally is computed on the breadth population**, so advancing + declining + unchanged equals the published universe count (1113). No quote-only denominator is mixed in.
- **Day-alignment assertion passed**: SPY's implied previous close from the scanner (752.69 / 1.0237 = 735.27) matches shibui's settled 2026-11-06 close (735.29); QQQ matches exactly (656.10). The scanner is on the 2026-11-09 session, not a stale one.

## Cross-check — shibui, T+1 (data date 2026-11-06)

shibui had not yet ingested 2026-11-09 at the 18:30 ET fire, so its newest settled session is **2026-11-06**. It is published as a cross-check, not as the number of record.

| Metric | TradingView (11-09 close, 1113 names) | shibui (11-06, 895 names) |
|---|---|---|
| % above 20-DMA | 68.01% | 56.42% |
| index ETFs above 20-DMA | 40% (2/5) | 0% (0/5) |
| index ETFs above 50-DMA | 40% (2/5) | 20% (1/5) |
| SPY vs 50-DMA | -1.65% | -3.97% |
| RSP vs 50-DMA | 2.87% | 0.59% |
| QQQ vs 50-DMA | -5.68% | -9.00% |
| QQQE vs 50-DMA | -2.91% | -5.98% |
| IWM vs 50-DMA | 0.24% | -2.99% |

The Friday shibui read is the pre-rally picture (56.42% above the 20-DMA, every index ETF below its 20-DMA, QQQ −9.00% under its 50-DMA). Today's TradingView read is the post-rally picture of the SAME market. The improvement is the story of 2026-11-09.
