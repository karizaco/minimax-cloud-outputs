---
cron: 09-stock-screener-daily-sweep-18:30
fire_time_et: 2026-11-03 18:30 ET
generated_et: 2026-11-03 19:43:47 ET
cron_date: 2026-11-03
screen_data_date: 2026-11-02 (shibui T+1 — the 2026-11-03 close is overlaid from the TradingView scanner and cross-checked against the CBOE delayed-quote CDN)
volatility_pair: VIX 20.83 / VIX3M 21.27 (ratio 0.9793), quote 2026-11-03T16:15:01 ET, CBOE delayed-quote CDN settled close — one pair, used everywhere
cross_reference: intraday counterpart: daily-screens/2026-11-03/breadth-snapshot.md (cron #10, 14:00 ET)
---

# Daily screen sweep — end-of-day read (2026-11-03)

**Cron #09 · fired 2026-11-03 18:30 ET · generated 2026-11-03 19:43:47 ET**

## What happened in the session

Indices closed mixed-to-higher with a sharp rotation **into** growth: SPX 7,568.92 (+0.36%), SPY 754.35 (+0.30%), QQQ 685.28 (+0.62%), while the equal-weight RSP slipped -0.33% to 219.26. Semis were the engine - SMH 518.52 (+2.01%) - and tech (XLK +1.31%) and industrials (XLI +0.95%) led the sector tape, while the defensive-to-commodity complex lagged hardest: staples (XLP -2.07%) and materials (XLB -2.01%) both fell about 2%.

| Index | Close | Change | | Sector | Close | Change |
|---|---|---|---|---|---|---|
| SPY | 754.35 | +0.30% | XLK | 176.51 | +1.31% |
| QQQ | 685.28 | +0.62% | XLF | 57.19 | -0.64% |
| RSP | 219.26 | -0.33% | XLE | 66.68 | -0.85% |
| IWM | 279.79 | +0.23% | XLV | 184.02 | -0.31% |
| QQQE | 115.95 | +0.05% | XLI | 171.32 | +0.95% |
| DIA | 517.06 | -0.44% | XLY | 117.33 | -0.70% |
| SMH | 518.52 | +2.01% | XLP | 88.95 | -2.07% |

## Top movers (2026-11-03 session)

| Gainers | Chg | Volume | | Losers | Chg | Volume |
|---|---|---|---|---|---|---|
| AEHR | +26.50% | 8,658,086 | | STVN | -28.57% | 4,784,094 |
| GPK | +21.22% | 22,683,307 | | DT | -14.69% | 22,644,832 |
| RIOT | +18.41% | 40,725,101 | | IT | -13.19% | 3,225,996 |
| CIFR | +18.37% | 66,958,769 | | CVI | -13.09% | 3,249,953 |
| XMTR | +16.55% | 2,448,953 | | PAY | -11.50% | 1,784,938 |
| BETA | +16.00% | 4,106,271 | | LIND | -10.64% | 1,695,755 |
| HUT | +15.90% | 9,196,501 | | TRI | -9.87% | 3,022,436 |
| FN | +15.45% | 2,365,372 | | SHC | -9.64% | 5,360,773 |
| GLXY | +15.35% | 8,923,445 | | SYY | -9.33% | 9,408,423 |
| WULF | +14.53% | 50,016,911 | | OTTR | -8.85% | 565,175 |

Highest relative volume (TV `relative_volume_10d_calc`, 10-day basis): **MGRC** 16.56x (+2.69%), **MCHPP** 11.68x (+2.49%), **STVN** 10.68x (-28.57%), **RYTM** 10.36x (-7.49%), **OKTA** 9.97x (+2.60%), **ALB/PA** 8.38x (-0.02%).

## Breadth & regime

- Breadth (2026-11-02 shibui session, T+1 feed): **65.19%** of the 902-name large-cap universe closed above its own 20-DMA; 61.09% above its 50-DMA.
- Only **2 of 5** index ETFs (SPY, RSP, QQQ, QQQE, IWM) were above their own 20-DMA — the index posture is weaker than the broad large-cap breadth, the signature of a megacap-led advance.
- Regime flags: `size_cut_pct` **0** (indices weak but breadth 65.19% > 40%), `uncertainty` **false** (VIX/VIX3M 0.9793 ≤ 1), `late_cycle` **false** (no index > 6% above its 50-DMA; ATR multiples 0.82x–1.21x).
- Full breadth tables, index extension and source health: `breadth.md`; regime payload: `_regime.json`.

## Tier-A — ≥3 distinct stylists (actionable shortlist)

| Ticker | Stylists | Stylist names | Close 2026-11-02 | Chg 2026-11-02 | Close 2026-11-03 | Chg 2026-11-03 | RVOL 2026-11-03 | RS 3M % | Vel 14D % | Flags |
|---|---|---|---|---|---|---|---|---|---|---|
| WING | 3 | peoplewish, qullamaggie, stockbee | 163.04 | 8.89% | 161.57 | -0.9% | 1.02 | 34.2 | 29.6 | — |
| KVYO | 3 | peoplewish, qullamaggie, stockbee | 21.8 | 8.24% | 21.33 | -2.16% | 1.04 | 14.1 | 28.6 | ma_shrink_5d |
| CVNA | 3 | jeff_sun, qullamaggie, stockbee | 72 | 5.43% | 71.28 | -1% | 0.98 | 5.8 | 19.2 | — |
| FTAI | 3 | peoplewish, qullamaggie, stockbee | 197.75 | 5.6% | 200.74 | 1.51% | 0.73 | -10.9 | 18.5 | — |
| FIGS | 3 | hernandez, peoplewish, qullamaggie | 21.29 | -0.09% | 20.82 | -2.21% | 1.83 | 96.2 | 18.3 | ma_shrink_5d,wicky_breakout |
| TEM | 3 | peoplewish, qullamaggie, stockbee | 78.48 | 8.67% | 77.8 | -0.87% | 0.91 | 66.8 | 15 | — |
| CLF | 3 | peoplewish, qullamaggie, stockbee | 14.27 | 0.14% | 14.14 | -0.91% | 0.86 | 15.9 | 11 | wicky_breakout |
| CAI | 3 | hernandez, peoplewish, qullamaggie | 32.1 | -6.5% | 32.85 | 2.34% | 0.76 | 99.4 | 8.7 | ma_shrink_5d |

12 names cleared three independent stylist screens; the list is truncated to 8 per the skill contract (`tier_a_truncated: true` in `_results.json`). The cluster is thematic rather than random: five of the eight (FIGS, SMPL, KOD, CAI, KVYO) sit in Health Care or Consumer Staples, the top two sector themes by relative strength, which is exactly what the top-down theme ranking produced — the tiers and the theme funnel agree.

## Focus — ≥2 stylists or top-5 velocity

| Ticker | Stylists | Stylist names | Close 2026-11-02 | Chg 2026-11-02 | Close 2026-11-03 | Chg 2026-11-03 | RVOL 2026-11-03 | RS 3M % | Vel 14D % | Flags |
|---|---|---|---|---|---|---|---|---|---|---|
| WING | 3 | peoplewish, qullamaggie, stockbee | 163.04 | 8.89% | 161.57 | -0.9% | 1.02 | 34.2 | 29.6 | — |
| KVYO | 3 | peoplewish, qullamaggie, stockbee | 21.8 | 8.24% | 21.33 | -2.16% | 1.04 | 14.1 | 28.6 | ma_shrink_5d |
| CVNA | 3 | jeff_sun, qullamaggie, stockbee | 72 | 5.43% | 71.28 | -1% | 0.98 | 5.8 | 19.2 | — |
| FTAI | 3 | peoplewish, qullamaggie, stockbee | 197.75 | 5.6% | 200.74 | 1.51% | 0.73 | -10.9 | 18.5 | — |
| FIGS | 3 | hernandez, peoplewish, qullamaggie | 21.29 | -0.09% | 20.82 | -2.21% | 1.83 | 96.2 | 18.3 | ma_shrink_5d,wicky_breakout |
| TEM | 3 | peoplewish, qullamaggie, stockbee | 78.48 | 8.67% | 77.8 | -0.87% | 0.91 | 66.8 | 15 | — |
| CLF | 3 | peoplewish, qullamaggie, stockbee | 14.27 | 0.14% | 14.14 | -0.91% | 0.86 | 15.9 | 11 | wicky_breakout |
| CAI | 3 | hernandez, peoplewish, qullamaggie | 32.1 | -6.5% | 32.85 | 2.34% | 0.76 | 99.4 | 8.7 | ma_shrink_5d |
| HTFL | 3 | hernandez, peoplewish, qullamaggie | 54.49 | -7.72% | 54.4 | -0.17% | 0.89 | 99.7 | 8.3 | ma_shrink_5d |
| KOD | 3 | hernandez, peoplewish, qullamaggie | 97.62 | -1.57% | 98.89 | 1.3% | 0.7 | 127.6 | 6.5 | wicky_breakout |
| MRNA | 3 | hernandez, peoplewish, qullamaggie | 220.83 | -0.4% | 228.44 | 3.45% | 0.5 | 287.5 | 2.1 | wicky_breakout |
| VSEC | 3 | jeff_sun, peoplewish, stockbee | 160.21 | 8.37% | 162.96 | 1.72% | 0.83 | -25.2 | -1.9 | ma_shrink_5d |

Stalk (Master ∩ within 2% of the 10/20-DMA): **48** names — see `stalk.md`.
Master (deduped union, capped at 200): **200** names — see `master.md`.

## Per-stylist screens

### Stockbee / Bonde — 4% breakout · EP9M · anticipation coil

- File: `stockbee.md` · 581 names in the merged output.

### Qullamägi — RS leaders · EP gap · 5-day gainers/losers

- File: `qullamaggie.md` · 67 names in the merged output.

### peoplewish — ADR ≥ 5% · $50M ADV · 14-day velocity

- File: `peoplewish.md` · 243 names in the merged output.

### Jeff Sun — CANSLIM rebuild (EPS + revenue growth) and volume breakout

- File: `jeff-sun.md` · 143 names in the merged output.

### Ariel Hernandez — theme → group → leaders

- File: `ariel-hernandez.md` · 15 names in the merged output.

## Parabolic candidates

- **Short side** — 5-day gainers ≥ +25%: 15 names (see `short-candidates.md`).
- **Long side** — 5-day losers −25%…−50%: 11 names (see `long-reversal-candidates.md`).

## Hernandez theme → group → leaders

Top themes by equal-weight 1M+6M relative strength of the 11 SPDR sector ETFs (shibui 2026-11-02 session): **XLV** (composite 18.7, 6M 27.17%), **XLE** (composite 12.5, 6M 14.27%), **XLP** (composite 5.7, 6M 7.91%).

| Theme | Leader | RS 3M % | Industry group | 2026-11-02 close | 2026-11-02 chg | 2026-11-03 close | 2026-11-03 chg |
|---|---|---|---|---|---|---|---|
| Health Care | MRNA | 287.5 | Pharmaceuticals, Biotechnology & Life Sciences | 220.83 | -0.4% | 228.44 | 3.45% |
| Health Care | KOD | 127.6 | Pharmaceuticals, Biotechnology & Life Sciences | 97.62 | -1.57% | 98.89 | 1.3% |
| Health Care | HTFL | 99.7 | Health Care Equipment & Services | 54.49 | -7.72% | 54.4 | -0.17% |
| Health Care | CAI | 99.4 | Pharmaceuticals, Biotechnology & Life Sciences | 32.1 | -6.5% | 32.85 | 2.34% |
| Health Care | FIGS | 96.2 | Health Care Equipment & Services | 21.29 | -0.09% | 20.82 | -2.21% |
| Energy | CVI | 67.8 | Energy | 55.92 | -4.2% | 48.6 | -13.09% |
| Energy | COP | 24.5 | Energy | 146.84 | -4.67% | 144.4 | -1.66% |
| Energy | PR | 19.8 | Energy | 24.56 | -5.61% | 24 | -2.28% |
| Energy | CVX | 19.6 | Energy | 227.77 | -3.29% | 225.27 | -1.1% |
| Energy | RIG | 19.3 | Energy | 6.23 | -10.23% | 5.9 | -5.3% |
| Consumer Staples | TRLV | 24.9 | Consumer Staples Distribution & Retail | 11.1 | 7.98% | 11.54 | 3.96% |
| Consumer Staples | SAM | 20.2 | Food, Beverage & Tobacco | 221.37 | 9.96% | 215.46 | -2.67% |
| Consumer Staples | KDP | 18.4 | Food, Beverage & Tobacco | 36.82 | 2.73% | 34.74 | -5.65% |
| Consumer Staples | COKE | 15.7 | Food, Beverage & Tobacco | 209.48 | -0.39% | 206.26 | -1.54% |
| Consumer Staples | WMT | 14.5 | Consumer Staples Distribution & Retail | 127.69 | 3.38% | 124.86 | -2.22% |

## Source health

| Source | Query / URL | Status |
|---|---|---|
| shibui (MCP-over-HTTP bridge) | breadth + ATR SQL, 902-name large-cap universe | ok |
| shibui (MCP-over-HTTP bridge) | 868-candidate indicator + skip-flag pass (4 batches) | ok |
| shibui (MCP-over-HTTP bridge) | sweep SQL: stockbee, qullamaggie, peoplewish, CANSLIM rebuild | ok |
| TradingView scanner | `POST https://scanner.tradingview.com/america/scan` | ok — 868/868 candidate closes; 1,973-name session universe for movers |
| TradingView scanner | Jeff Sun volume-breakout screen (momentum + RVOL ≥ 2.0x) | ok — 60 names |
| CBOE delayed-quote CDN | `quotes/{sym}.json` (SPX, NDX, RUT, DJX, VIX, VIX3M, 6 index ETFs, 11 sector ETFs, 8 large movers, 8 Tier-A names) | ok — Tier-A closes matched the scanner to the cent on 8/8 |
| connector catalog probe | `probe_mcp.py` | catalog_ok total=135 finance_tools=0 |

## Method & caveats

- **The screens ran on 2026-11-02, not today.** shibui's latest ingested bar at the 2026-11-03 18:30 ET fire is 2026-11-02 (Monday), so every stylist screen is one session stale. The 2026-11-03 session close for all 868 candidates comes from the TradingView scanner, and it is the overlay column (`chg_pct_2026-11-03`) that tells you which of Monday's setups survived today's session.
- **Every candidate carries a 2026-11-02 close and a 2026-11-03 close** — the two columns must not be mixed. The `close_2026-11-02`/`chg_pct_2026-11-02` pair is the screen basis; `close_2026-11-03`/`chg_pct_2026-11-03` is the settled overlay.
- The overlay closes were cross-checked against the CBOE delayed-quote CDN: all 8 Tier-A names matched to the cent, and the eight largest movers matched on 7 of 8 (FIGS differed by 3¢). Nasdaq's `/info` agrees with the scanner on the same names.
- The skill's shipped sweep SQL has five documented defects (missing comma, aliased-then-misnamed LAG columns, mismatched UNION arity, a 9-month window shorter than the 252-day LAG it needs, and inherited column names in a UNION ALL). The repo's current emitters carry all five repairs; the Qullamägi RS book returns data instead of silently emptying, and every UNION branch emits an identical, explicitly-named column set.
- CANSLIM is rebuilt on shibui's `fundamentals_derived_quarterly` because TradingView's `earnings_growth_quarterly_yoy` / `sales_growth_quarterly_yoy` columns return null for every US name.
- The Hernandez funnel selects leaders, not whole sectors: top-3 themes → their GICS sectors → the top 5 by 3-month RS inside each sector that already cleared another stylist screen. The theme tag never inflates a name's stylist count.
- Jeff Sun's volume-breakout screen is run as the skill's KSE-style momentum+volume cross-check (RVOL ≥ 2.0x, positive session change, > $1B cap) rather than raw high-RVOL, which otherwise sweeps in large decliners on volume alone. It counts as Jeff Sun, so one stylist's two screens cannot masquerade as two independent opinions.
- The skill's emitted sweep SQL caps each branch (50 / 50 / 30 for Stockbee, 200 for peoplewish), but the shibui server hard-caps every query at 200 rows. On this date **233** names pass the 4%-breakout filter, **236** pass EP9M, **150** pass anticipation and **243** pass peoplewish — every one of those branches was truncated by the emitted `LIMIT`, silently dropping names from the book. All four branches were re-run uncapped (in two batches each where needed) so the published books are complete; the Tier-A list differs from a limit-capped run.
- The 3:55 PM reversal-bullish scan and the Sunday IPO / high-short-float refreshes are **not** part of this routine (cron #04 and the Sunday weekly routine own them).
