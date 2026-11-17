# Earnings reaction scanner — 2026-11-17

- Cron: `0 8 * * 1-5` America/New_York (weekdays, 08:00 ET)
- Fire time (ET): 2026-11-17 08:13:52 Tue
- Run type: `scheduled_scan`
- Source: TradingView public screener (`scanner.tradingview.com/<market>/scan`);
  Yahoo chart API as the independent reference-close source.
- Method: 6 passes (US top-200 mcap, US prior-session movers, US pre-market gaps,
  EU/UK movers, ASX movers, APAC/Gulf movers). Volume floor 10,000 on every session-volume
  pass; Pass B2 floors PRE-market volume at 10,000 shares; `country` filter for
  primary listings; exchange drop-list applied.
- artifact_contract: REACTION_ARTIFACT_V2
- settlement_state: every foreign row carries a `Settle` cell - `live` when the row's
  session bar is an in-progress bar, `settled` when it is a completed session. The
  EU/UK session is still OPEN at the 08:00 ET fire (it closes 11:30 ET in winter), so
  its rows read `live`: the move is a mid-session snapshot, not the session's result.
- ref_close_source: yahoo_chart_daily (Yahoo Finance daily chart bars; the base
  every published row is measured against)
- Status: `ok`

## TL;DR

- 0 AMC reactions, 70 pre-market gaps, 87 without extended-hours data; 30 EU/UK and 4 ASX movers, 21 APAC/Gulf movers.
- Pass B2 (the US pre-market gap scan) met the filter on 10 names (9 up, 1 down); 6 were already a Pass A/B row and are recorded as dedupes, and 4 reached a table.
- Biggest US extended-hours move: RCAT PRE_GAP (33.42%).
- Biggest EU/UK move: XTB (-16.36%, poland).
- Biggest ASX move: CAT (-16.57%).
- Biggest APAC/Gulf move: AREA (+34.67%, indonesia).
- 0 of the 30 EU/UK rows are SETTLED and 30 are LIVE (mid-session). The 12:15 ET settlement pass publishes where those
  live moves actually closed.
- EU/AU/APAC earnings-driven tagging is keyword-based on headlines (best-effort). A row
  whose lookup was not performed carries NO verdict — only a researched row does.

## Actionable read

- **Move vs this name's own history.** The `Move vs avg daily` column divides the
  reaction by the name's own mean absolute daily move over its last
  20 completed sessions. A -27% move in a name that averages +-3% is a
  different event from a -8% move in a name that averages +-7%.
- **US-listed and tradeable vs foreign-only.** 85 published US rows are on a
  US venue; 0 more foreign reactions have a US ADR line
  (the `US tradeable` column carries the ticker); 30 are foreign-only and
  cannot be bought directly by a US reader.
- **Not yet fully priced — US (hypothesis, not a recommendation).**
  RCAT — -33.42%, 6.17% mean absolute daily move over the last 20 completed sessions, 5.4x that average, reference close 3.80 dated 2026-11-13, US access: US-listed, the move now (-33.42%) is larger than the move it follows (-7.11%); the reaction is still being repriced. Hypothesis only: this artifact states no
  direction and no trade.
- **Not yet fully priced — EU/UK (hypothesis, not a recommendation).**
  XTB — -16.36%, 2.03% mean absolute daily move over the last 20 completed sessions, 8.1x that average, reference close 139.72 dated 2026-11-16, US access: none, the move now (-16.36%) is larger than the move it follows (+0.45%); the reaction is still being repriced. Hypothesis only: this artifact states no
  direction and no trade.
- **Not yet fully priced — AU (ASX) (hypothesis, not a recommendation).**
  IPH — -13.42%, 2.06% mean absolute daily move over the last 20 completed sessions, 6.5x that average, reference close 3.95 dated 2026-11-15, US access: none, the move now (-13.42%) is larger than the move it follows (-1.25%); the reaction is still being repriced. Hypothesis only: this artifact states no
  direction and no trade.

## US — Headline table

| Ticker | Venue | Close | Chg % | Pre-mkt % | Post-mkt % | Move vs avg daily | Ref close | Ref source | Ref asof | US tradeable | Last earnings | Tag | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RCAT | NASDAQ | 3.53 | -7.11 | -33.42 | — | 5.4x | 3.80 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-11-16 (1d ago) | PRE_GAP | Y | Q3 2026 results (reported 2026-11-16, after the close): revenue $11.8m vs ~$40.7m consensus, net loss $0.26/sh vs -$0.20 expected, gross margin 0.6% on scrap and warranty costs; the FY2026 revenue target is WITHDRAWN after contract awards slipped and the FANG drone missed the Drone Dominance II final |
| LUCK | NYSE | 3.32 | -3.77 | 14.29 | — | 2.9x | 3.45 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-11-05 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| COHR | NYSE | 203.43 | -6.75 | 9.28 | — | 1.4x | 218.15 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-11-04 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AAOI | NASDAQ | 45.16 | -9.48 | 8.53 | — | 1.1x | 49.89 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-11-05 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CAI | NASDAQ | 21 | -8.85 | 7.14 | — | 1.7x | 23.04 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-11-04 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SLS | NASDAQ | 7.47 | -4.96 | 7.10 | — | 1.4x | 7.86 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-11-12 (5d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-12 (Nasdaq earnings calendar; no headline lookup) |
| KURA | NASDAQ | 7.09 | -8.75 | 6.56 | — | 1.4x | 7.77 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-11-10 (7d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-10 (Nasdaq earnings calendar; no headline lookup), consensus EPS ($0.83) |
| LITE | NASDAQ | 546 | -8.48 | 5.57 | — | 0.8x | 596.62 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-11-02 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MRVL | NASDAQ | 145.36 | -7.27 | 5.10 | — | 0.8x | 156.76 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-08-27 (82d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TEM | NASDAQ | 64.76 | -9.55 | 5.00 | — | 0.9x | 71.60 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-11-02 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NTRA | NASDAQ | 288.48 | -9.59 | 4.71 | — | 1.3x | 319.09 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-11-05 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ALAB | NASDAQ | 202.34 | -8.79 | 4.69 | — | 0.8x | 221.83 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-11-03 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CRDO | NASDAQ | 120.71 | -8.21 | 4.48 | — | 0.6x | 131.51 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-09-01 (77d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CIEN | NYSE | 257.56 | -8.19 | 4.05 | — | 0.6x | 280.54 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-09-03 (75d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MBGL | NYSE | 24.04 | 3.26 | -4.03 | — | 1.7x | 23.28 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-11-12 (5d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-12 (Nasdaq earnings calendar; no headline lookup), consensus EPS $0.38 |
| TTMI | NASDAQ | 68.25 | -7.87 | 4.03 | — | 0.5x | 74.08 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-10-22 (26d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BUUU | NASDAQ | 5.5 | 3.38 | -4.00 | — | 0.4x | 5.32 | yahoo_chart_daily | 2026-11-13 | US-listed | — | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| STDN | NYSE | 9.33 | -11.56 | 3.97 | — | 1.0x | 10.55 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-11-12 (5d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-12 (Nasdaq earnings calendar; no headline lookup), consensus EPS ($0.13) |
| PRG | NYSE | 39.61 | 3.20 | -3.94 | — | 1.1x | 38.38 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-10-28 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TSEM | NASDAQ | 133.42 | -9.17 | 3.92 | — | 0.6x | 146.89 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-11-02 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SMTC | NASDAQ | 105.3 | -8.11 | 3.88 | — | 0.5x | 114.59 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-08-25 (84d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ACMR | NASDAQ | 44 | -8.24 | 3.39 | — | 0.6x | 47.95 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-11-05 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FORM | NASDAQ | 81.14 | -7.30 | 3.36 | — | 0.4x | 87.53 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-10-28 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FPS | NYSE | 20.57 | -7.01 | 3.31 | — | 0.4x | 22.12 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-11-12 (5d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-12 (Nasdaq earnings calendar; no headline lookup), consensus EPS $0.18 |
| SECZ | NYSE | 7.33 | -9.28 | 3.27 | — | 0.5x | 8.08 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-11-09 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| VICR | NASDAQ | 146.52 | -7.88 | 3.26 | — | 0.5x | 159.05 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-10-20 (28d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RYTM | NASDAQ | 107.48 | -6.56 | -3.24 | — | 0.8x | 115.02 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-11-03 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PENG | NASDAQ | 44.22 | -6.63 | 3.23 | — | 0.4x | 47.36 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-10-06 (42d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AEHR | NASDAQ | 50.98 | -10.53 | 3.18 | — | 0.4x | 56.98 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-11-02 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ALGM | NASDAQ | 28.11 | -6.70 | 3.17 | — | 0.6x | 30.13 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-10-29 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NBIS | NASDAQ | 107.13 | -7.55 | 3.09 | — | 0.4x | 115.88 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-11-12 (5d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-12 (Nasdaq earnings calendar; no headline lookup), consensus EPS ($0.61) |
| MXL | NASDAQ | 51.97 | -6.83 | 2.94 | — | 0.4x | 55.78 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-10-22 (26d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GLW | NYSE | 106.17 | -6.93 | 2.93 | — | 0.7x | 114.08 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-10-27 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CVS | NYSE | 88.59 | -0.85 | -2.89 | — | 1.4x | 89.35 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-11-04 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| STRL | NASDAQ | 275.13 | -5.90 | 2.86 | — | 0.5x | 292.39 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-10-28 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| UCTT | NASDAQ | 42.87 | -7.51 | 2.85 | — | 0.4x | 46.35 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-10-27 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| EROC | NYSE | 7.49 | -10.94 | 2.80 | — | 0.3x | 8.41 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-11-12 (5d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-12 (Nasdaq earnings calendar; no headline lookup), consensus EPS ($0.01) |
| AMKR | NASDAQ | 34.05 | -5.70 | 2.79 | — | 0.5x | 36.11 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-10-26 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| OUST | NASDAQ | 31.23 | -6.72 | 2.79 | — | 0.4x | 33.48 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-11-03 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BLLN | NASDAQ | 96.31 | -8.41 | 2.74 | — | 1.3x | 105.15 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-11-04 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CAMT | NASDAQ | 93.25 | -8.34 | 2.73 | — | 0.5x | 101.73 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-11-04 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| VIAV | NASDAQ | 28.73 | -6.48 | 2.68 | — | 0.4x | 30.72 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-11-04 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BE | NYSE | 177.28 | -7.66 | 2.66 | — | 0.4x | 191.99 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-10-22 (26d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PRAX | NASDAQ | 310.27 | -5.44 | 2.65 | — | 0.6x | 328.13 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-11-09 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TER | NASDAQ | 231.9 | -7.07 | 2.64 | — | 0.5x | 249.55 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-10-27 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| UNH | NYSE | 412.02 | 1.12 | -2.61 | — | 2.3x | 407.46 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-10-13 (35d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ICHR | NASDAQ | 33.65 | -5.80 | 2.53 | — | 0.4x | 35.72 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-11-02 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MP | NYSE | 36.09 | -6.89 | 2.52 | — | 0.7x | 38.76 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-11-05 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NXT | NASDAQ | 89.31 | -6.02 | 2.45 | — | 0.5x | 95.03 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-10-28 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| HUBS | NYSE | 231.98 | 6.78 | -2.43 | — | 0.7x | 217.25 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-11-04 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ANET | NYSE | 187.02 | -5.21 | 2.40 | — | 0.5x | 197.29 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-11-03 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GRAL | NASDAQ | 105.6 | -8.88 | 2.38 | — | 0.4x | 115.89 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-11-04 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BELFB | NASDAQ | 208.24 | -7.65 | 2.31 | — | 0.5x | 225.49 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-10-28 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RCI | NYSE | 34.65 | 4.24 | -2.28 | — | 1.2x | 33.24 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-10-23 (25d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| IREN | NASDAQ | 16.39 | -9.80 | 2.23 | — | 0.3x | 18.17 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-11-05 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| URGN | NASDAQ | 28.1 | 7.33 | 2.17 | — | 0.6x | 26.18 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-11-04 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MPWR | NASDAQ | 1314 | -5.50 | 2.14 | — | 0.4x | 1390.54 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-10-29 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SMCI | NASDAQ | 25.025 | -6.85 | 2.14 | — | 0.4x | 26.87 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-11-03 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CRM | NYSE | 214.83 | -1.38 | -2.14 | — | 1.4x | 217.84 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-08-26 (83d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CORZ | NASDAQ | 13.58 | -6.47 | 2.14 | — | 0.4x | 14.52 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-11-05 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SKYD | NYSE | 7.04 | -6.38 | 2.13 | — | 0.7x | 7.52 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-11-09 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| DIS | NYSE | 118.7 | -0.23 | -2.13 | — | 2.0x | 118.97 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-11-17 (0d ago) | PRE_GAP | Y | FY26 Q4 and full-year results (reported 2026-11-17, 06:30 ET): adjusted EPS $1.77 vs $1.67 consensus, revenue $25.9bn vs $25.2bn est (16% y/y), FY26 adjusted EPS $7.02, +18%; FY27 guidance targets double-digit adjusted-EPS growth, $11bn free cash flow and $9bn of buybacks, plus $3bn of cost savings by FY2029 |
| APLD | NASDAQ | 14.58 | -8.70 | 2.13 | — | 0.3x | 15.97 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-10-07 (41d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| STX | NASDAQ | 499 | -5.54 | 2.10 | — | 0.4x | 528.29 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-10-27 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ABSI | NASDAQ | 7.475 | -11.54 | 2.07 | — | 0.3x | 8.45 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-11-12 (5d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-12 (Nasdaq earnings calendar; no headline lookup), consensus EPS ($0.14) |
| LASR | NASDAQ | 37.82 | -8.32 | 2.06 | — | 0.4x | 41.25 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-11-05 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMD | NASDAQ | 504.28 | -5.58 | 2.05 | — | 0.3x | 534.06 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-11-03 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| QNT | NASDAQ | 31.75 | -10.31 | 2.05 | — | 0.3x | 35.40 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-11-05 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| INOD | NASDAQ | 32.59 | -8.09 | 2.03 | — | 0.4x | 35.46 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-11-05 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| DFTX | NASDAQ | 30.16 | -5.99 | 2.00 | — | 0.5x | 32.08 | yahoo_chart_daily | 2026-11-13 | US-listed | 2026-11-09 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |

## US — QUIET one-liners

| Ticker | Venue | Chg % | Pre-mkt % | Post-mkt % | Move vs avg daily | Ref close | Ref source | Ref asof | US tradeable | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PEP | NASDAQ | 0.68 | -1.99 | — | 0.5x | 145.44 | yahoo_chart_daily | 2026-11-13 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| GLXY | NASDAQ | -8.62 | 1.98 | — | 1.0x | 14.38 | yahoo_chart_daily | 2026-11-13 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| KLAC | NASDAQ | -5.49 | 1.91 | — | 1.2x | 152.32 | yahoo_chart_daily | 2026-11-13 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| NVTS | NASDAQ | -11.96 | 1.90 | — | 1.8x | 8.95 | yahoo_chart_daily | 2026-11-13 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| ALB | NYSE | -5.74 | 1.89 | — | 2.5x | 93.53 | yahoo_chart_daily | 2026-11-13 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| LRCX | NASDAQ | -6.68 | 1.86 | — | 1.4x | 225.92 | yahoo_chart_daily | 2026-11-13 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| WOLF | NYSE | -8.78 | 1.85 | — | 1.3x | 24.83 | yahoo_chart_daily | 2026-11-13 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| APH | NYSE | -3.58 | 1.84 | — | 1.1x | 78.23 | yahoo_chart_daily | 2026-11-13 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| WDC | NASDAQ | -4.98 | 1.83 | — | 0.9x | 295.65 | yahoo_chart_daily | 2026-11-13 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| MRNA | NASDAQ | -3.63 | 1.82 | — | 0.8x | 223.37 | yahoo_chart_daily | 2026-11-13 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| ADI | NASDAQ | -3.72 | 1.78 | — | 1.2x | 397.97 | yahoo_chart_daily | 2026-11-13 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| HD | NYSE | -0.34 | -1.78 | — | 0.2x | 348.69 | yahoo_chart_daily | 2026-11-13 | US-listed | — | Q4 2026 results, report date today (Nasdaq earnings calendar; no headline lookup), consensus EPS $3.86 |
| TTWO | NASDAQ | -6.30 | 1.78 | — | 2.6x | 227.82 | yahoo_chart_daily | 2026-11-13 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| CSCO | NASDAQ | -1.17 | 1.78 | — | 0.5x | 95.64 | yahoo_chart_daily | 2026-11-13 | US-listed | — | Q4 2026 results, report date 2026-11-12 (Nasdaq earnings calendar; no headline lookup), consensus EPS $1.15 |
| CNC | NYSE | 4.91 | -1.78 | — | 1.9x | 71.27 | yahoo_chart_daily | 2026-11-13 | US-listed | — | no catalyst lookup (outside the per-run budget) |

## EU/UK — Headline table

| Ticker | Market | Venue | Close | Chg % | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | Session asof | Settle | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| XTB | poland | GPW | 116.86 | -16.36 | PLN | 8.1x | 139.72 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | live | none | 2026-10-28 (20d ago) | — | no catalyst lookup (outside the per-run budget) |
| AVIO | italy | MIL | 39.38 | +15.48 | EUR | 6.0x | 34.10 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | live | US line (OTC:AVVOF) | 2026-03-12 (250d ago) | — | no catalyst lookup (outside the per-run budget) |
| TECN | switzerland | SIX | 230.6 | -7.32 | CHF | 4.5x | 248.80 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | live | none | 2026-08-11 (98d ago) | — | no catalyst lookup (outside the per-run budget) |
| CBF | poland | GPW | 213 | +7.04 | PLN | 7.7x | 199.00 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | live | none | 2026-11-16 (1d ago) | — | no catalyst lookup (outside the per-run budget) |
| GOMX | sweden | OMXSTO | 13.77 | -6.96 | SEK | 1.7x | 14.80 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | live | none | 2026-08-26 (83d ago) | — | no catalyst lookup (outside the per-run budget) |
| ZZ_B | sweden | OMXSTO | 119.4 | +6.42 | SEK | 3.2x | 112.20 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | live | none | 2026-11-17 (0d ago) | Y | Q3 2026 interim report (reported 2026-11-17, 08:00 CET): revenue SEK 940.5m, +20% (+23% in local currency), EBITDA SEK 168.5m, +54% at a 17.9% margin, net income SEK 122.0m, EPS SEK 3.10; management calls the FY 20% growth target challenging; acquires Uzesta |
| ROB | poland | GPW | 26.55 | -6.18 | PLN | 6.4x | 28.30 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | live | none | — | — | no catalyst lookup (outside the per-run budget) |
| SEYE | sweden | OMXSTO | 48 | +6.05 | SEK | 2.3x | 45.26 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | live | none | 2026-11-17 (0d ago) | Y | Q3 2026 interim report (reported 2026-11-17, 07:00 CET): first positive EBIT at SEK 5m, organic growth 33%, net sales +36%, EBITDA +SEK 22.6m, EPS -0.24; SEK 40m/yr of OPEX to be cut and a SEK 100m mirror-integrated Interior Sensing order signed; first quarter reported on IFRS |
| WWI | norway | OSL | 946 | +5.46 | NOK | 3.6x | 897.00 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | live | none | 2026-11-04 (13d ago) | — | pending catalyst lookup |
| OVH | france | EURONEXT | 14.05 | -5.39 | EUR | 1.3x | 14.85 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | live | US line (OTC:OVHFF) | 2026-10-20 (28d ago) | — | no catalyst lookup (outside the per-run budget) |
| CDR | poland | GPW | 266 | -5.27 | PLN | 4.0x | 280.80 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | live | none | 2026-09-02 (76d ago) | N | no fresh catalyst found - Q3 2026 results are due on 24 Nov 2026; the shares fell with a -1.04% WIG20 session in which CD Projekt RED, KGHM, Orlen and the energy names led the decline |
| VU | france | EURONEXT | 149.8 | -5.25 | EUR | 2.1x | 158.10 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | live | none | 2026-09-21 (57d ago) | — | no catalyst lookup (outside the per-run budget) |
| WWIB | norway | OSL | 899 | +5.02 | NOK | 3.1x | 856.00 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | live | none | 2026-11-04 (13d ago) | — | no catalyst lookup (outside the per-run budget) |
| MORROW | sweden | OMXSTO | 17.18 | -4.87 | SEK | 2.9x | 18.06 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | live | none | 2026-11-12 (5d ago) | — | pending catalyst lookup |
| NANO | france | EURONEXT | 25.1 | -4.64 | EUR | 1.1x | 26.32 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | live | US line (NASDAQ:NA) | 2026-09-24 (54d ago) | — | no catalyst lookup (outside the per-run budget) |
| ENAV | italy | MIL | 5.49 | -4.52 | EUR | 4.1x | 5.75 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | live | none | 2026-08-03 (106d ago) | — | no catalyst lookup (outside the per-run budget) |
| PLT | norway | OSL | 11.82 | -4.37 | NOK | 1.2x | 12.36 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | live | none | 2026-08-06 (103d ago) | — | no catalyst lookup (outside the per-run budget) |
| NORBT | norway | OSL | 168.8 | -4.36 | NOK | 1.8x | 176.50 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | live | none | 2026-11-12 (5d ago) | Y | Q3 2026 results (reported 2026-11-12): revenue NOK 676.7m beat the NOK 638m consensus, statutory EPS NOK 1.12 missed by 14%, extra dividend of NOK 2.00 declared - the shares traded ex-dividend today, which accounts for part of the 4.25% fall |
| RMS | france | EURONEXT | 1291 | -4.33 | EUR | 2.7x | 1349.50 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | live | none | 2026-07-29 (111d ago) | — | pending catalyst lookup |
| DBK | germany | XETR | 31.58 | -4.06 | EUR | 1.9x | 32.91 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | live | none | 2026-10-28 (20d ago) | N | 'Inside Deutsche Bank' leaked-document investigation (Der Spiegel/FT/NYT/Le Monde consortium, 15m records on Russian oligarch, Trump and Epstein dealings) - shares fell 5-6% in Frankfurt, the biggest drop since April 2025; the bank says the matters date back decades with no meaningful financial impact; an MEP has called for CEO Christian Sewing to testify |
| MONC | italy | MIL | 41.8 | -3.93 | EUR | 2.3x | 43.51 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | live | none | 2026-07-22 (118d ago) | — | no catalyst lookup (outside the per-run budget) |
| ACE | italy | MIL | 19.53 | -3.89 | EUR | 4.0x | 20.32 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | live | none | 2026-11-13 (4d ago) | — | no catalyst lookup (outside the per-run budget) |
| GUBRA | denmark | OMXCOP | 290 | -3.85 | DKK | 1.6x | 301.60 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | live | none | 2026-08-20 (89d ago) | — | no catalyst lookup (outside the per-run budget) |
| FGP | uk | LSE | 224.4096 | -3.69 | GBX | 3.2x | 233.00 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | live | none | 2026-11-17 (0d ago) | Y | H1 FY2027 results (reported 2026-11-17): adjusted EPS 8.4p vs 9.9p (-15%), Open Access adjusted operating profit collapsed to GBP 0.8m from GBP 16.3m on ~GBP 8m of Stirling launch costs, group adjusted revenue +21% to GBP 1.01bn; interim DPS raised to 2.3p, a further GBP 50m buyback announced, FY27 flat adjusted-EPS guidance maintained; Panmure cut its target to 265p |
| IDR | spain | BME | 55.6 | -3.64 | EUR | 1.6x | 57.70 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | live | none | 2026-10-29 (19d ago) | — | no catalyst lookup (outside the per-run budget) |
| ACT0 | germany | XETR | 155.4 | +3.60 | EUR | 1.1x | 150.00 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | live | none | 2026-10-28 (20d ago) | — | no catalyst lookup (outside the per-run budget) |
| EYDAP | greece | ATHEX | 14.18 | +3.50 | EUR | 3.5x | 13.70 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | live | none | 2026-09-24 (54d ago) | — | no catalyst lookup (outside the per-run budget) |
| ZEAL | denmark | OMXCOP | 231.5 | -3.46 | DKK | 2.5x | 239.80 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | live | none | 2026-11-12 (5d ago) | — | no catalyst lookup (outside the per-run budget) |
| LXS | germany | XETR | 12.67 | -3.43 | EUR | 2.3x | 13.12 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | live | none | 2026-11-05 (12d ago) | — | no catalyst lookup (outside the per-run budget) |
| ZEG | uk | LSE | 1792 | +3.34 | GBX | 1.8x | 1734.00 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | live | none | 2026-11-17 (0d ago) | — | no catalyst lookup (outside the per-run budget) |

## AU (ASX) — Headline table

| Ticker | Venue | Close | Chg % | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | Session asof | Settle | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CAT | ASX | 3.02 | -16.57 | AUD | 5.4x | 3.62 | yahoo_chart_daily | 2026-11-15 | 2026-11-17 | settled | US line (OTC:BLCAF) | 2026-11-15 (2d ago) | — | no catalyst lookup (outside the per-run budget) |
| IPH | ASX | 3.42 | -13.42 | AUD | 6.5x | 3.95 | yahoo_chart_daily | 2026-11-15 | 2026-11-17 | settled | none | 2026-08-19 (90d ago) | N | FY27 trading update at today's AGM (announced 09:42 AEDT, 17 Nov): four-month revenue A$221.5m, -8.4%, underlying EBITDA A$62.6m, -13.4% (like-for-like revenue -1.2%, EBITDA -4.2%; ANZ like-for-like EBITDA -7.2%); FY26 statutory NPAT A$80.4m and dividends +5.5% to 38.5cps |
| SRL | ASX | 10.76 | -11.00 | AUD | 1.9x | 12.09 | yahoo_chart_daily | 2026-11-15 | 2026-11-17 | settled | none | 2026-09-07 (71d ago) | N | no fresh catalyst found - no ASX announcement since the 16 Nov afternoon; the shares fell 11.0% to A$10.76 in an ASX-wide selloff; the live drivers remain the conditional US$400m US defence-linked loan and the Mount Ridley scandium project |
| MAF | ASX | 4.22 | -9.44 | AUD | 3.5x | 4.66 | yahoo_chart_daily | 2026-11-15 | 2026-11-17 | settled | none | 2026-08-19 (90d ago) | — | no catalyst lookup (outside the per-run budget) |

## APAC/Gulf — Headline table

| Ticker | Market | Venue | Close | Chg % | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | Session asof | Settle | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AREA | indonesia | IDX | 268 | +34.67 | IDR | 4.7x | 199.00 | yahoo_chart_daily | 2026-11-15 | 2026-11-16 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| TRIN | indonesia | IDX | 179 | +34.59 | IDR | 3.5x | 133.00 | yahoo_chart_daily | 2026-11-15 | 2026-11-16 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| MGNA | indonesia | IDX | 218 | +34.57 | IDR | 5.8x | 162.00 | yahoo_chart_daily | 2026-11-15 | 2026-11-16 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| 301288 | china | SZSE | 20.14 | +20.02 | CNY | 5.2x | 16.78 | yahoo_chart_daily | 2026-11-15 | 2026-11-16 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| 301209 | china | SZSE | 52.96 | +20.01 | CNY | 2.9x | 44.13 | yahoo_chart_daily | 2026-11-15 | 2026-11-16 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| 301391 | china | SZSE | 38.88 | +20.00 | CNY | 4.5x | 32.40 | yahoo_chart_daily | 2026-11-15 | 2026-11-16 | settled | none | 2026-04-29 (202d ago) | — | no catalyst lookup (outside the per-run budget) |
| MODTHREAD | india | NSE | 55.92 | +20.00 | INR | 7.5x | 46.60 | yahoo_chart_daily | 2026-11-15 | 2026-11-16 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| BALAXI | india | NSE | 26.47 | +19.99 | INR | 5.5x | 22.06 | yahoo_chart_daily | 2026-11-15 | 2026-11-16 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| SALASAR | india | BSE | 5.77 | +19.96 | INR | 5.6x | 4.81 | yahoo_chart_daily | 2026-11-15 | 2026-11-16 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| BEC | thailand | SET | 1.89 | +13.17 | THB | 9.0x | 1.67 | yahoo_chart_daily | 2026-11-15 | 2026-11-16 | settled | none | 2026-11-13 (4d ago) | N | no fresh catalyst found - the Q3 2026 financial statement was filed with the SET on 13 Nov; today the shares rebounded 13.2% to THB 1.89 off the THB 1.67 52-week low set on 16 Nov, on 9.37m shares, with no company news found |
| MIM | singapore | SGX | 1.09 | -12.10 | SGD | 1.5x | 1.24 | yahoo_chart_daily | 2026-11-15 | 2026-11-16 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| SSP | thailand | SET | 6.62 | -10.78 | THB | 4.6x | 7.42 | yahoo_chart_daily | 2026-11-15 | 2026-11-16 | settled | none | 2026-11-11 (6d ago) | Y | Q3 2026 results (reported 2026-11-11): Q3 net profit THB 327.8m, +438% q/q, normalised profit THB 208.7m; 9M profit THB 652.8m, +94.2%, flattered by a THB 402.8m one-off gain on the Yamaga solar sale - the shares fell 10.8% today with no new company news |
| DDD | thailand | SET | 4.06 | -9.78 | THB | 6.1x | 4.50 | yahoo_chart_daily | 2026-11-15 | 2026-11-16 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| G92 | singapore | SGX | 1.15 | -8.00 | SGD | 3.1x | 1.25 | yahoo_chart_daily | 2026-11-15 | 2026-11-16 | settled | none | 2026-11-12 (5d ago) | — | no catalyst lookup (outside the per-run budget) |
| 9557 | ksa | TADAWUL | 230 | -8.00 | SAR | 3.1x | 250.00 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| 8200 | ksa | TADAWUL | 28.94 | +7.90 | SAR | 2.4x | 26.82 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | settled | none | 2026-11-01 (16d ago) | — | no catalyst lookup (outside the per-run budget) |
| 4082 | ksa | TADAWUL | 8.12 | +6.56 | SAR | 2.6x | 7.62 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| EB5 | singapore | SGX | 3.03 | +6.32 | SGD | 1.8x | 2.85 | yahoo_chart_daily | 2026-11-15 | 2026-11-16 | settled | none | 2026-08-13 (96d ago) | — | no catalyst lookup (outside the per-run budget) |
| VSL | newzealand | NZX | 6.85 | -3.52 | NZD | 2.0x | 7.10 | yahoo_chart_daily | 2026-11-15 | 2026-11-16 | settled | none | 2026-08-24 (85d ago) | N | no fresh catalyst found - no company announcement (FY26 results in August, AGM 21 Oct); the shares fell 3.5% to NZ$6.85 with the NZX distribution-services sector while the NZX 50 closed flat |
| SPG | newzealand | NZX | 1.095 | -3.10 | NZD | 1.9x | 1.13 | yahoo_chart_daily | 2026-11-15 | 2026-11-16 | settled | none | 2025-11-25 (357d ago) | — | pending catalyst lookup |
| SAN | newzealand | NZX | 7.07 | +2.91 | NZD | 1.5x | 6.87 | yahoo_chart_daily | 2026-11-15 | 2026-11-16 | settled | none | 2026-11-16 (1d ago) | — | no catalyst lookup (outside the per-run budget) |

## Source health

- scanner_calls: 57 | scanner_errors: 0
- markets_scanned: US + 17 EU/UK + ASX + 7 APAC/Gulf (india, thailand, indonesia, china, singapore, newzealand, ksa)
- pipeline_version: 2026-11-16.2
- et_clock: zoneinfo America/New_York (DST-aware; a fixed UTC-4 mislabels every winter fire)
- premarket_window: 04:00-09:30 ET, resolved with zoneinfo (09:00-14:30 UTC in winter, 08:00-13:30 UTC in summer)
- session_selection: by DATE and order, never by a modal time-of-day. Yahoo stamps a daily bar at the session open, so the ET stamp of the SAME session shifts by one hour across a DST boundary; a modal filter kept the OLDER bars and discarded the NEWEST ones, which rolled the base back to the prior-prior session (66 US + 21 ASX rows lost on 2026-11-03, 24 of 25 ASX rows lost on 2026-11-04).
- yahoo_calls: 150 | yahoo_429: 0 | yahoo_errors: 0 | yahoo_breaker: closed
- reference_close (screener vs Yahoo, resolved BEFORE the tables were built): agree=140 mismatch=0 unverified=0 stale_reference=0
  method: the screener's implied reference close (close / (1 + change/100)) is compared
  with Yahoo's own reference close. A match proves the move was measured against the
  TRUE prior close; a mismatch means the row sits on a STALE reference (phantom move).
  Coverage: every row of the US headline, US QUIET, EU/UK and ASX tables is checked.
  Yahoo bar mode: {"closed": 110, "live": 30} (closed = last completed session bar;
  live = in-progress EU/UK session bar, which is what a weekday 08:00 ET EU move needs)
  live drift between the screener snapshot and the later Yahoo print: median=0.00pp max=1.28pp (expected on a live market)
- rows_dropped_stale_ref: 0 (rows whose screener-implied reference close disagreed with Yahoo's by more than 0.5%; they are dropped, not published)
- rows_dropped_unresolved_ref: 0 (rows whose reference close could not be resolved from Yahoo at all - the base of the move is unverifiable, so the row is dropped rather than published with a '—' base)
- us_premarket_check (Yahoo 1-min pre/post feed vs the screener pre-market column, base = the IMMEDIATELY prior session's close): checked=10 within_1pp=8 within_3pp=10 unavailable=0
- markets_with_lt5_rows: ['uk:egreater=1', 'germany:egreater=1', 'france:egreater=2', 'netherlands:egreater=0', 'netherlands:less=0', 'belgium:egreater=0', 'belgium:less=2', 'portugal:egreater=0', 'portugal:less=0', 'ireland:egreater=0', 'ireland:less=0', 'italy:egreater=2', 'switzerland:egreater=0', 'switzerland:less=2', 'spain:egreater=0', 'spain:less=1', 'denmark:egreater=0', 'finland:egreater=0', 'finland:less=2', 'poland:egreater=2', 'austria:egreater=0', 'austria:less=1', 'greece:egreater=1', 'greece:less=0', 'singapore:egreater=2', 'newzealand:egreater=1', 'newzealand:less=4']
  NOTE: this fires per market AND direction, so it is NOT a coverage-failure signal on
  its own. A 'less' count of 0-3 means almost nothing fell more than 2.5% that session
  (a broad up-day); a small 'egreater' count usually means a small market with few
  names above the $1B market-cap floor. Check the median change before calling it a gap.
- filters: volume>10000 (removes stale-reference rows), country=home for EU/UK/AU,
  exchange drop-list for US, US venue allow-list, US preferred (slash ticker) excluded
- pass_b2 (US pre-market gap scan - "gapped today, flat yesterday"): candidates=10 deduped_against_pass_a_b=6 published=4 (up=9 down=1)
  filter: US venues, market_cap_basic > $200,000,000, close > $2, |premarket_change| >= 5.0%, premarket_volume >= 10,000 shares; two scans (up and down) because a scanner filter is AND-ed
  why it exists: on 2026-11-13 a name that was FLAT in the prior session and is not a $20bn mega-cap fell through Pass A and Pass B, so LFTO (+30.63% on the day) and SBC (+37.64%) were both missed by the routine that exists to catch same-session earnings reactions
  column measurement (2026-11-15, market `america`, US stocks): `premarket_change` and `premarket_volume` are available as BOTH a column and a FILTER (an unknown field returns 200 with zero rows, so the counts are the proof); `gap` also exists but it is the REGULAR SESSION OPEN gap, which is not knowable at the 08:00 ET fire, so `premarket_change` is the column used
  the pre-market volume floor is a DIFFERENT measure from the session-volume floor: at the 08:00 ET fire the regular session has not opened, so `volume` is 0 for every candidate and no session-volume filter is applied to this pass
- volume_floor_note: volume>10000 removes MOST stale-reference rows, but a row can
  still sit on a stale reference when its only volume came from one thin day (verified
  2026-10-26: LSE 50GP cleared the floor on 12,000 shares dated 2026-10-15 while Yahoo
  showed no bar for the scan date). The reference-close cross-check is what catches
  those; rows that fail it are dropped from the tables, not published.
- us_preferred_dropped: 59
- bod_no_extended_hours: 87 (deferred to the next scan; not in the headline table)
- earnings_source: screener `earnings_release_date` (last FULL report) + `earnings_release_next_date` (next scheduled)
- earnings_caveat: `earnings_release_date` does NOT capture preliminary, guidance or
  restructuring releases. On 2026-10-23 LKQ fell 22.47% on a preliminary Q3 miss while
  the field still read 2026-07-30. ALWAYS confirm the earnings-driven flag against the
  headline itself; the calendar field is a screen, not a verdict.
- us_line_index: ok (US-listed lines for the 25 foreign home countries, both scanner types; the `US tradeable` column is ADR / US-listed / none)
- catalyst_note: Catalyst lookups: 2 US + 9 EU + 2 AU + 3 APAC/Gulf = 16 per run - the skill's cap, allocated by the evidence gap.
- catalyst_merge: region-matched - a row may only use a catalog entry from its OWN region;
  the same ticker on another venue is a different company and is not used.
- catalyst_budget: 2 US + 9 EU + 2 AU + 3 APAC/Gulf = 16 lookups per run (cap 16), allocated by the evidence gap: the US slice covers the rows whose earnings event can still explain today's move, the EU/AU/APAC floors are never squeezed because no bulk calendar reaches those markets, and whatever the US slice does not need goes to the region with the most unexplained rows
- earnings_calendar: Nasdaq public earnings calendar (calls=8 errors=0 symbols=1073) - the source of record for the US earnings date, and the ranking key for the search budget
- earnings_field_stale_rows: 0 (the screener's earnings_release_date disagreed with the calendar; the calendar's date is published)
- earnings_dates: the published `Last earnings` date by source - catalog (researched) 7, calendar 8, asx 0, screener 110. The chain is researched -> calendar (US) -> ASX feed (AU) -> the screener's field, which is the FALLBACK and the one that lags (2026-11-12: NBIS carried the previous quarter's date on the morning it reported, and MEKO, NORBT and FG carried July and August dates on the morning they all reported).
- asx_announcements: 6 results-classified announcement(s) for the last ASX session (calls=1 errors=0); the announcement date IS the report date, and the meeting/AGM/offer/assay headlines are excluded because they are not reports
- earnings_date_quality: 5 of 20 markets publish a FRESH earnings date (median age <= 14d); the table below gives each market's rows, the rows with NO date at all, the median age of the published date and the rows within 7 and 30 days - the reader sees the input quality instead of trusting it
| market | rows | no date | median age | <=7d | <=30d |
|---|---|---|---|---|---|
| au | 4 | 0 | 90d | 1 | 1 |
| china | 3 | 2 | 202d | 0 | 0 |
| denmark | 2 | 0 | 89d | 1 | 1 |
| france | 4 | 0 | 57d | 0 | 1 |
| germany | 3 | 0 | 20d | 0 | 3 |
| greece | 1 | 0 | 54d | 0 | 0 |
| india | 3 | 3 | n/a | 0 | 0 |
| indonesia | 3 | 3 | n/a | 0 | 0 |
| italy | 4 | 0 | 118d | 1 | 1 |
| ksa | 3 | 2 | 16d | 0 | 1 |
| newzealand | 3 | 0 | 85d | 1 | 1 |
| norway | 4 | 0 | 13d | 1 | 3 |
| poland | 4 | 1 | 20d | 1 | 2 |
| singapore | 3 | 1 | 96d | 1 | 1 |
| spain | 1 | 0 | 19d | 0 | 1 |
| sweden | 4 | 0 | 5d | 3 | 3 |
| switzerland | 1 | 0 | 98d | 0 | 0 |
| thailand | 3 | 1 | 6d | 2 | 2 |
| uk | 2 | 0 | 0d | 2 | 2 |
| us | 70 | 1 | 14d | 10 | 61 |
- earnings_tiers: fresh=1 near=1 (fresh = the report is dated on the scan date, near = the previous session)
- one_table_rule: each name appears exactly once, in exactly one table, with its
  catalyst in that row's last column. There is no separate catalysts section.
- data_date: US regular session close of the prior trading day; extended-hours columns
  carry the prior session's prints
- settlement_state: 25 settled, 30 live (a live row's move is a mid-session snapshot, not the session's result)
- rows_per_market (EU/UK, cap 4/market): {'poland': 4, 'italy': 4, 'switzerland': 2, 'sweden': 4, 'norway': 4, 'france': 4, 'germany': 4, 'denmark': 4, 'uk': 4, 'spain': 1, 'greece': 1, 'austria': 1, 'finland': 2, 'belgium': 2} — the cap stops one thin market taking the table; the EU/UK table was 28% Sweden over nine runs (73 of 264 rows) while Belgium and Greece never appeared once.
- rows_per_market (APAC/Gulf, cap 3/market): {'indonesia': 3, 'china': 3, 'india': 3, 'thailand': 3, 'singapore': 3, 'ksa': 3, 'newzealand': 3}
- deprecations: mcp__tradingview-advanced__*, mcp__tradingview__*, mcp__financekit__*,
  mcp__stocktwits__* are ABSENT in Cloud sessions (tool_search 0 hits; connector catalog
  holds only media + credential tools). The public screener replaces them.

- degraded_sources: 0
  (none - every source answered for every published row)

## Audit line

`earnings-reaction target=earnings-reactions:2026-11-17 candidates=436 amc_reactions=0 pre_gaps=70 eu_reactions=30 asx_reactions=4 apac_reactions=20 catalyst_lookups=16 bod=87 pass_b2_candidates=10 pass_b2_dedup=6 pass_b2_published=4 earnings_calendar_rows=1073 earnings_tiers_fresh=1 earnings_tiers_near=1 earnings_field_stale_rows=0 earnings_dates_catalog=7 earnings_dates_asx=0 asx_ann_rows=6 rows_dropped_stale_ref=0 rows_dropped_unresolved_ref=0 degraded_sources=0`
