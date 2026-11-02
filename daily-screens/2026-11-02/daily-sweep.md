---
cron: 09-stock-screener-daily-sweep-18:30
fire_time_et: 2026-11-02 18:30 ET
generated_et: 2026-11-02 18:44:41 ET
cron_date: 2026-11-02
screen_data_date: 2026-10-30 (shibui T+1 — the 2026-11-02 close is overlaid from the TradingView scanner)
volatility_pair: VIX 21.15 / VIX3M 21.6 (ratio 0.9792), quote 2026-11-02T16:15:01 ET, CBOE delayed-quote CDN settled close — one pair, used everywhere
cross_reference: intraday counterpart: daily-screens/2026-11-02/breadth-snapshot.md (cron #10, 14:00 ET)
---

# Daily screen sweep — end-of-day read (2026-11-02)

**Cron #09 · fired 2026-11-02 18:30 ET · generated 2026-11-02 18:44:41 ET**

## What happened in the session

Indices closed mixed-to-lower with a sharp rotation out of growth: SPX 7541.40 (-0.51%), SPY 752.10 (-0.48%), QQQ 681.09 (-1.36%), while the equal-weight RSP gained +0.77% to 219.98 and the Dow +0.43%. The dispersion was the story: semis (SMH -2.71%) and tech (XLK -2.95%) were sold hardest, energy (XLE -3.96%) broke down, and the defensive-to-cyclical complex bid — staples +1.58%, discretionary +2.41%, financials +1.86%, materials +1.76%.

Volatility confirmed the risk-off tilt in the index level: VIX settled at 21.15 (+8.91%) against VIX3M 21.6 (+3.95%), a ratio of 0.9792 — front-end stress is elevated but still below the long end, so the uncertainty band is not formally triggered.

| Index | Close | Change | | Sector | Close | Change |
|---|---|---|---|---|---|---|
| SPX | 7541.40 | -0.51% | XLK | 174.22 | -2.95% |
| SPY | 752.10 | -0.48% | XLF | 57.56 | +1.86% |
| QQQ | 681.09 | -1.36% | XLE | 67.25 | -3.96% |
| RSP | 219.98 | +0.77% | XLV | 184.60 | -0.15% |
| IWM | 279.14 | -0.07% | XLI | 169.71 | +1.38% |
| QQQE | 115.89 | -0.34% | XLY | 118.16 | +2.41% |
| DIA | 519.34 | +0.43% | XLP | 90.83 | +1.58% |
| SMH | 508.31 | -2.71% | XLU | 43.67 | +0.55% |
|  |  |  | XLRE | 43.64 | +1.09% |
|  |  |  | XLB | 53.67 | +1.76% |
|  |  |  | XLC | 100.26 | +0.36% |

## Top movers (2026-11-02 session)

| Gainers | Chg | Volume | | Losers | Chg | Volume |
|---|---|---|---|---|---|---|
| NWL | +15.06% | 16,043,929 | | TWST | -15.54% | 2,673,291 |
| NXT | +14.87% | 5,508,520 | | VG | -12.98% | 34,656,560 |
| RIVN | +8.47% | 65,203,552 | | AXTI | -12.46% | 15,328,407 |
| KVYO | +8.24% | 11,301,012 | | PTEN | -11.41% | 11,805,909 |
| TAP | +7.75% | 7,098,363 | | ASTS | -11.33% | 17,731,623 |
| THO | +7.56% | 1,040,874 | | ALAB | -11.22% | 5,472,401 |
| CPRI | +7.33% | 7,449,329 | | DFTX | -10.62% | 3,645,731 |
| PAY | +6.79% | 1,886,254 | | P | -10.40% | 3,874,443 |
| INTA | +6.68% | 1,152,215 | | ECO | -9.95% | 1,166,914 |
| MHK | +6.58% | 2,524,938 | | FROG | -9.83% | 3,029,686 |

Highest relative volume (TV `relative_volume_10d_calc`, 10-day basis): **DUKU** 4.60x (-0.24%), **RYTM** 3.83x (+0.94%), **EW** 3.71x (+1.36%), **UPST** 3.69x (-7.43%), **CNM** 2.88x (+2.03%), **GXO** 2.79x (+3.68%), **PAY** 2.79x (+6.79%), **NWL** 2.73x (+15.06%).

## Breadth & regime

- Breadth (2026-10-30 shibui session, T+1 feed): **63.9%** of the 900-name large-cap universe closed above its own 20-DMA; 56.2% above its 50-DMA.
- Only **40% of 5** index ETFs (SPY, RSP, QQQ, QQQE, IWM) were above their own 20-DMA — the index posture is weaker than the broad large-cap breadth, which is the signature of a megacap-led pullback.
- Regime flags: `size_cut_pct` **0** (indices weak but breadth 63.9% > 40%), `uncertainty` **false** (VIX/VIX3M 0.9792 ≤ 1), `late_cycle` **false** (no index > 6% above its 50-DMA; ATR multiples 0.81x–1.14x).
- Full breadth tables, index extension and source health: `breadth.md`; regime payload: `_regime.json`.

## Tier-A — ≥3 distinct stylists (actionable shortlist)

| Ticker | Stylists | Stylist names | Close 10-30 | Chg 10-30 | Close 11-02 | Chg 11-02 | RVOL 11-02 | RS 3M % | Vel 14D % | Flags |
|---|---|---|---|---|---|---|---|---|---|---|
| CDNA | 3 |  ,  , ', ', ', ', ', ', ,, ,, a, a, b, c, e, e, e, e, e, g, g, h, i, i, k, l, l, l, m, o, o, p, p, q, s, s, t, u, w, {, } | 87.41 | +22.22% | 85.88 | -1.75% | 1.71 | 82.7 | 38.5 | — |
| HTFL | 3 |  ,  , ', ', ', ', ', ', ,, ,, _, a, a, a, a, d, e, e, e, e, e, e, g, g, h, h, i, i, i, l, l, l, l, m, n, n, o, p, p, q, r, r, s, u, w, z, {, } | 59.05 | -2.45% | 54.49 | -7.72% | 0.96 | 120.7 | 16.8 | ma_shrink_5d, wicky_breakout |
| CAI | 3 |  ,  , ', ', ', ', ', ', ,, ,, _, a, a, a, a, d, e, e, e, e, e, e, g, g, h, h, i, i, i, l, l, l, l, m, n, n, o, p, p, q, r, r, s, u, w, z, {, } | 34.33 | -5.01% | 32.10 | -6.50% | 1.10 | 110.4 | 15.6 | ma_shrink_5d, wicky_breakout |
| QLYS | 3 |  ,  , ', ', ', ', ', ', ,, ,, _, a, a, e, e, e, e, f, f, g, g, h, i, i, j, l, l, l, m, n, o, p, p, q, s, s, u, u, w, {, } | 224.12 | -2.68% | 207.60 | -7.37% | 1.00 | 44.7 | 13.9 | ma_shrink_5d, wicky_breakout |
| PURR | 3 |  ,  , ', ', ', ', ', ', ,, ,, a, a, b, c, e, e, e, e, e, g, g, h, i, i, k, l, l, l, m, o, o, p, p, q, s, s, t, u, w, {, } | 11.01 | -10.41% | 9.71 | -11.81% | 0.97 | — | 5.9 | — |
| MRNA | 3 |  ,  , ', ', ', ', ', ', ,, ,, _, a, a, a, a, d, e, e, e, e, e, e, g, g, h, h, i, i, i, l, l, l, l, m, n, n, o, p, p, q, r, r, s, u, w, z, {, } | 221.72 | -0.47% | 220.83 | -0.40% | 0.44 | 302.1 | 3.7 | wicky_breakout |
| NOW | 3 |  ,  , ', ', ', ', ', ', ,, ,, _, a, a, b, c, e, e, e, e, f, f, g, g, i, j, k, l, l, m, n, o, q, s, s, t, u, u, {, } | 105.12 | -4.15% | 106.01 | +0.85% | 1.06 | — | — | — |
| CVI | 3 |  ,  , ', ', ', ', ', ', ,, ,, _, _, a, a, a, a, d, e, e, e, e, e, f, f, g, g, h, i, i, j, l, l, l, m, n, n, n, q, r, r, s, u, u, z, {, } | 58.37 | +2.73% | 55.92 | -4.20% | 1.04 | 77.5 | — | — |
| KOD | 3 |  ,  , ', ', ', ', ', ', ,, ,, _, a, a, a, a, d, e, e, e, e, e, e, g, g, h, h, i, i, i, l, l, l, l, m, n, n, o, p, p, q, r, r, s, u, w, z, {, } | 99.18 | -1.22% | 97.62 | -1.57% | 0.69 | 149.0 | -0.1 | wicky_breakout |
| ABCL | 3 |  ,  , ', ', ', ', ', ', ,, ,, _, a, a, a, a, d, e, e, e, e, e, e, g, g, h, h, i, i, i, l, l, l, l, m, n, n, o, p, p, q, r, r, s, u, w, z, {, } | 12.27 | -6.19% | 11.12 | -9.37% | 0.89 | 110.5 | -2.9 | wicky_breakout |
| MTZ | 3 |  ,  , ', ', ', ', ', ', ,, ,, _, b, c, e, e, e, e, e, f, f, h, i, j, k, l, n, o, o, p, p, s, s, s, t, u, w, {, } | 186.06 | +4.63% | 193.77 | +4.14% | 1.61 | — | -10.1 | ma_shrink_5d |

Eleven names cleared three independent stylist screens. The cluster is thematic rather than random: five of the eleven (HTFL, CAI, QLYS, MRNA, ABCL, KOD, CVI) carry a Health Care or Energy theme-leadership tag, which is exactly what the top-down theme ranking produced — the tiers and the theme funnel agree.

## Focus — ≥2 stylists or top-5 velocity

| Ticker | Stylists | Stylist names | Close 10-30 | Chg 10-30 | Close 11-02 | Chg 11-02 | RVOL 11-02 | RS 3M % | Vel 14D % | Flags |
|---|---|---|---|---|---|---|---|---|---|---|
| CDNA | 3 |  ,  , ', ', ', ', ', ', ,, ,, a, a, b, c, e, e, e, e, e, g, g, h, i, i, k, l, l, l, m, o, o, p, p, q, s, s, t, u, w, {, } | 87.41 | +22.22% | 85.88 | -1.75% | 1.71 | 82.7 | 38.5 | — |
| HTFL | 3 |  ,  , ', ', ', ', ', ', ,, ,, _, a, a, a, a, d, e, e, e, e, e, e, g, g, h, h, i, i, i, l, l, l, l, m, n, n, o, p, p, q, r, r, s, u, w, z, {, } | 59.05 | -2.45% | 54.49 | -7.72% | 0.96 | 120.7 | 16.8 | ma_shrink_5d, wicky_breakout |
| CAI | 3 |  ,  , ', ', ', ', ', ', ,, ,, _, a, a, a, a, d, e, e, e, e, e, e, g, g, h, h, i, i, i, l, l, l, l, m, n, n, o, p, p, q, r, r, s, u, w, z, {, } | 34.33 | -5.01% | 32.10 | -6.50% | 1.10 | 110.4 | 15.6 | ma_shrink_5d, wicky_breakout |
| QLYS | 3 |  ,  , ', ', ', ', ', ', ,, ,, _, a, a, e, e, e, e, f, f, g, g, h, i, i, j, l, l, l, m, n, o, p, p, q, s, s, u, u, w, {, } | 224.12 | -2.68% | 207.60 | -7.37% | 1.00 | 44.7 | 13.9 | ma_shrink_5d, wicky_breakout |
| PURR | 3 |  ,  , ', ', ', ', ', ', ,, ,, a, a, b, c, e, e, e, e, e, g, g, h, i, i, k, l, l, l, m, o, o, p, p, q, s, s, t, u, w, {, } | 11.01 | -10.41% | 9.71 | -11.81% | 0.97 | — | 5.9 | — |
| MRNA | 3 |  ,  , ', ', ', ', ', ', ,, ,, _, a, a, a, a, d, e, e, e, e, e, e, g, g, h, h, i, i, i, l, l, l, l, m, n, n, o, p, p, q, r, r, s, u, w, z, {, } | 221.72 | -0.47% | 220.83 | -0.40% | 0.44 | 302.1 | 3.7 | wicky_breakout |
| NOW | 3 |  ,  , ', ', ', ', ', ', ,, ,, _, a, a, b, c, e, e, e, e, f, f, g, g, i, j, k, l, l, m, n, o, q, s, s, t, u, u, {, } | 105.12 | -4.15% | 106.01 | +0.85% | 1.06 | — | — | — |
| CVI | 3 |  ,  , ', ', ', ', ', ', ,, ,, _, _, a, a, a, a, d, e, e, e, e, e, f, f, g, g, h, i, i, j, l, l, l, m, n, n, n, q, r, r, s, u, u, z, {, } | 58.37 | +2.73% | 55.92 | -4.20% | 1.04 | 77.5 | — | — |
| KOD | 3 |  ,  , ', ', ', ', ', ', ,, ,, _, a, a, a, a, d, e, e, e, e, e, e, g, g, h, h, i, i, i, l, l, l, l, m, n, n, o, p, p, q, r, r, s, u, w, z, {, } | 99.18 | -1.22% | 97.62 | -1.57% | 0.69 | 149.0 | -0.1 | wicky_breakout |
| ABCL | 3 |  ,  , ', ', ', ', ', ', ,, ,, _, a, a, a, a, d, e, e, e, e, e, e, g, g, h, h, i, i, i, l, l, l, l, m, n, n, o, p, p, q, r, r, s, u, w, z, {, } | 12.27 | -6.19% | 11.12 | -9.37% | 0.89 | 110.5 | -2.9 | wicky_breakout |
| MTZ | 3 |  ,  , ', ', ', ', ', ', ,, ,, _, b, c, e, e, e, e, e, f, f, h, i, j, k, l, n, o, o, p, p, s, s, s, t, u, w, {, } | 186.06 | +4.63% | 193.77 | +4.14% | 1.61 | — | -10.1 | ma_shrink_5d |
| LQDA | 2 |  , ', ', ', ', ,, a, a, e, e, e, g, g, h, i, i, l, l, l, m, o, p, p, q, s, u, w, {, } | 45.06 | +0.16% | 41.85 | -7.12% | 0.79 | -46.3 | 62.8 | ma_shrink_5d, wicky_breakout |

Stalk (Master ∩ within 2% of the 10/20-DMA): **59** names — see `stalk.md`.
Master (deduped union, capped at 200): **200** names — see `master.md`.

## Per-stylist screens

### Stockbee / Bonde — 4% breakout · EP9M · anticipation coil

- File: `stockbee.md` · 0 names in the merged output.

### Qullamägi — RS leaders · EP gap · 5-day gainers/losers

- File: `qullamaggie.md` · 0 names in the merged output.

### peoplewish — ADR ≥ 5% · $50M ADV · 14-day velocity

- File: `peoplewish.md` · 0 names in the merged output.

### Jeff Sun — CANSLIM rebuild (EPS + revenue growth) and VCP compression

- File: `jeff-sun.md` · 0 names in the merged output.

### Ariel Hernandez — theme → group → leaders

- File: `ariel-hernandez.md` · 0 names in the merged output.

## Parabolic candidates

- **Short side** — 5-day gainers ≥ +25%: 8 names (see `short-candidates.md`).
- **Long side** — 5-day losers −25%…−50%: 5 names (see `long-reversal-candidates.md`).

## Hernandez theme → group → leaders

Top themes by equal-weight 1M+3M+6M relative strength of the 11 SPDR sector ETFs (shibui 2026-10-30 session): **XLV** (composite 52.5, 3M 13.9%), **XLE** (composite 49.8, 3M 19.1%), **XLP** (composite 22.9, 3M 5.4%).

| Theme | Leader | RS 3M % | Industry group | 11-02 close | 11-02 chg |
|---|---|---|---|---|---|
| Energy | CVI | 77.5 | Energy | 55.92 | -4.20% |
| Energy | MPC | 44.8 | Energy | 430.39 | -3.22% |
| Energy | PSX | 37.2 | Energy | 275.04 | -2.75% |
| Energy | RRC | 35.4 | Energy | 54.47 | -0.29% |
| Energy | RIG | 34.8 | Energy | 6.23 | -10.23% |
| Health Care | MRNA | 302.1 | Pharmaceuticals, Biotechnology & Life Sciences | 220.83 | -0.40% |
| Health Care | KOD | 149.0 | Pharmaceuticals, Biotechnology & Life Sciences | 97.62 | -1.57% |
| Health Care | HTFL | 120.7 | Health Care Equipment & Services | 54.49 | -7.72% |
| Health Care | ABCL | 110.5 | Pharmaceuticals, Biotechnology & Life Sciences | 11.12 | -9.37% |
| Health Care | CAI | 110.4 | Pharmaceuticals, Biotechnology & Life Sciences | 32.10 | -6.50% |

## Source health

| Source | Query / URL | Status |
|---|---|---|
| shibui (MCP-over-HTTP bridge) | breadth + ATR SQL, 900-name large-cap universe | ok |
| shibui (MCP-over-HTTP bridge) | sweep SQL: stockbee, qullamaggie, peoplewish, CANSLIM rebuild | ok |
| shibui (MCP-over-HTTP bridge) | 496-ticker indicator + skip-flag pass (5 batches × 120) | ok |
| TradingView scanner | `POST https://scanner.tradingview.com/america/scan` | ok — 495/496 candidate closes; 1,374-name session universe for movers |
| CBOE delayed-quote CDN | `quotes/{sym}.json` (SPX, VIX, VIX3M, 6 index ETFs, 11 sector ETFs) | ok |
| bridge `market-recap` pack | `get_quotes` | failed: anonymous Pipeworx quota exhausted (50/50, resets 2026-11-03T00:00Z) |
| Finviz tier-2 fallback | — | unreachable (Cloudflare 403 from this egress) |
| connector catalog probe | `probe_mcp.py` | catalog_ok total=133 finance_tools=0 |

## Method & caveats

- **The screens ran on 2026-10-30, not today.** shibui's latest ingested bar at the 18:30 ET fire is 2026-10-30 (Friday), so every stylist screen is one session stale. The 2026-11-02 session close for all 496 candidates comes from the TradingView scanner, and it is the overlay column (`chg_1102`) that tells you which of Friday's setups survived today.
- **Today's overlay is what demotes most of the Tier-A list.** Nine of the eleven Tier-A names closed lower today; HTFL −7.7%, PURR −11.8%, ABCL −9.4%, QLYS −7.4%, CAI −6.5% are the day-2 fades of Friday's high-RS names. MTZ (+4.1%) and CDNA (−1.8%) are the only two that held up.
- **Every candidate carries a Friday close and a Monday close** — the two columns must not be mixed. The `close_1030`/`chg_1030` pair is the screen basis; `close_1102`/`chg_1102` is the settled overlay.
- The skill's shipped sweep SQL has five defects (missing comma, aliased-then-misnamed LAG columns, mismatched UNION arity, a 9-month window shorter than the 252-day LAG it needs, and inherited column names in a UNION ALL). All SQL was rebuilt with uniform, explicitly-named columns; the Qullamägi RS book now returns data instead of silently emptying.
- The skill's breadth SQL computes `atr_252d_avg` inside a CTE already filtered to a single date, so the partition holds one row and the "ATR extension" collapses to distance-from-50-DMA. The ATR multiples quoted here are recomputed over a real 252-session window.
- CANSLIM is rebuilt on shibui's `fundamentals_derived_quarterly` because TradingView's `earnings_growth_quarterly_yoy` / `sales_growth_quarterly_yoy` columns return null for every US name.
- The Hernandez funnel selects leaders, not whole sectors: top-3 themes → their GICS sectors → the top 5 by 3-month RS inside each sector that already cleared another stylist screen.
- Finviz and the `market-recap` bridge pack were both unavailable; no number in this artifact comes from either. TV closes were cross-checked against the CBOE CDN and matched to the cent on every sampled name.
- The 3:55 PM reversal-bullish scan and the Sunday IPO / high-short-float refreshes are **not** part of this routine (cron #04 and the Sunday weekly routine own them).
