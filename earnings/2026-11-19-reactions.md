# Earnings reaction scanner — 2026-11-19

- Cron: `0 8 * * 1-5` America/New_York (weekdays, 08:00 ET)
- Fire time (ET): 2026-11-19 08:16:06 Thu
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

- 0 AMC reactions, 133 pre-market gaps, 165 without extended-hours data; 30 EU/UK and 3 ASX movers, 19 APAC/Gulf movers.
- Pass B2 (the US pre-market gap scan) met the filter on 37 names (35 up, 2 down); 15 were already a Pass A/B row and are recorded as dedupes, and 22 reached a table.
- Biggest US extended-hours move: SLS PRE_GAP (20.89%).
- Biggest EU/UK move: SOI (+17.18%, france).
- Biggest ASX move: MLX (-10.39%).
- Biggest APAC/Gulf move: HRME (+34.88%, indonesia).
- 0 of the 30 EU/UK rows are SETTLED and 30 are LIVE (mid-session). The 12:15 ET settlement pass publishes where those
  live moves actually closed.
- EU/AU/APAC earnings-driven tagging is keyword-based on headlines (best-effort). A row
  whose lookup was not performed carries NO verdict — only a researched row does.

## Actionable read

- **Move vs this name's own history.** The `Move vs avg daily` column divides the
  reaction by the name's own mean absolute daily move over its last
  20 completed sessions. A -27% move in a name that averages +-3% is a
  different event from a -8% move in a name that averages +-7%.
- **US-listed and tradeable vs foreign-only.** 148 published US rows are on a
  US venue; 2 more foreign reactions have a US ADR line
  (the `US tradeable` column carries the ticker); 27 are foreign-only and
  cannot be bought directly by a US reader.
- **Not yet fully priced — US (hypothesis, not a recommendation).**
  MANU — -7.53%, 1.61% mean absolute daily move over the last 20 completed sessions, 4.7x that average, reference close 21.68 dated 2026-11-17, US access: US-listed, the move now (-7.53%) is larger than the move it follows (+1.01%); the reaction is still being repriced. Hypothesis only: this artifact states no
  direction and no trade.
- **Not yet fully priced — EU/UK (hypothesis, not a recommendation).**
  OROX — -14.47%, 0.91% mean absolute daily move over the last 20 completed sessions, 16.0x that average, reference close 11.06 dated 2026-11-18, US access: none, the move now (-14.47%) is larger than the move it follows (-0.54%); the reaction is still being repriced. Hypothesis only: this artifact states no
  direction and no trade.
- **Not yet fully priced — AU (ASX) (hypothesis, not a recommendation).**
  RIC — -8.24%, 1.16% mean absolute daily move over the last 20 completed sessions, 7.1x that average, reference close 2.67 dated 2026-11-17, US access: none, the move now (-8.24%) is larger than the move it follows (-1.48%); the reaction is still being repriced. Hypothesis only: this artifact states no
  direction and no trade.

## US — Headline table

| Ticker | Venue | Close | Chg % | Pre-mkt % | Post-mkt % | Move vs avg daily | Ref close | Ref source | Ref asof | US tradeable | Last earnings | Tag | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SLS | NASDAQ | 17.95 | -6.27 | -20.89 | — | 1.6x | 19.15 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-12 (7d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-12 (Nasdaq earnings calendar; no headline lookup) |
| PANW | NASDAQ | 339.92 | 9.90 | 9.64 | — | 2.9x | 309.29 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-18 (1d ago) | PRE_GAP | Y | Q1 FY2027 results (reported 2026-11-18): revenue USD3.44bn, up 39% y/y, NGS ARR USD9.73bn, up 66%, RPO USD21.0bn, up 35%, non-GAAP EPS USD1.05 vs a USD0.97 FactSet consensus, FY27 guidance raised to USD14.52-14.57bn revenue and USD4.26-4.30 EPS, and the USD4.5bn Applied Compute acquisition announced |
| ASTS | NASDAQ | 25.49 | -7.61 | 9.45 | — | 1.5x | 27.59 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-09 (10d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| COHR | NYSE | 212.84 | 0.94 | 7.62 | — | 1.2x | 210.86 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-04 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MANU | NYSE | 21.9 | 1.01 | -7.53 | — | 4.7x | 21.68 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-19 (0d ago) | PRE_GAP | Y | Q1 FY2027 results (reported 2026-11-19): revenue GBP146.1m, up 4.1% y/y, adjusted EBITDA GBP27.5m vs GBP26.9m, but an operating loss of GBP3.0m against a GBP13.0m profit and a basic loss per share of 10.50p vs 3.85p; FY27 guidance of GBP740-760m revenue and GBP205-225m adjusted EBITDA reiterated |
| BE | NYSE | 170.98 | -1.43 | 7.33 | — | 1.1x | 173.46 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-10-22 (28d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| UMAC | AMEX | 9.61 | -4.28 | 7.28 | — | 1.1x | 10.04 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-05 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CRSR | NASDAQ | 11.64 | 4.21 | 7.22 | — | 2.1x | 11.17 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-05 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SHAZ | NASDAQ | 21.99 | -2.66 | 7.05 | — | 0.8x | 22.59 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-16 (3d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-16 (Nasdaq earnings calendar; no headline lookup), consensus EPS ($1.47) |
| EROC | NYSE | 7.35 | -2.78 | 6.80 | — | 1.0x | 7.56 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-12 (7d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-12 (Nasdaq earnings calendar; no headline lookup), consensus EPS ($0.01) |
| NBIS | NASDAQ | 106.96 | 0.87 | 6.76 | — | 0.9x | 106.03 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-12 (7d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-12 (Nasdaq earnings calendar; no headline lookup), consensus EPS ($0.61) |
| AXTI | NASDAQ | 35.61 | -2.22 | 6.68 | — | 0.8x | 36.42 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-10-29 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| HUT | NASDAQ | 57.19 | 5.97 | 6.66 | — | 0.9x | 53.97 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-04 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CRWD | NASDAQ | 237.03 | 7.95 | 6.62 | — | 2.2x | 219.58 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-08-26 (85d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| STX | NASDAQ | 515.9 | 2.28 | 6.61 | — | 1.4x | 504.40 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-10-27 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| P | NYSE | 100.74 | -1.03 | 6.49 | — | 1.5x | 101.79 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-18 (1d ago) | PRE_GAP | Y | Q3 FY2027 results (reported 2026-11-18): revenue USD1.46bn, up 51% y/y, non-GAAP EPS USD0.86 vs a USD0.77 estimate, record USD345m non-GAAP operating income at a 23.6% margin, and FY27 revenue guidance raised to USD5.20-5.21bn for a third straight quarter |
| CIFR | NASDAQ | 6.57 | 2.34 | 6.24 | — | 0.8x | 6.42 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-02 (17d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CRWV | NASDAQ | 47.83 | -4.13 | 6.17 | — | 0.9x | 49.89 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-10 (9d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AEHR | NASDAQ | 49.48 | -0.52 | 6.10 | — | 0.8x | 49.74 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-02 (17d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AAOI | NASDAQ | 40.79 | -9.80 | 5.87 | — | 0.8x | 45.22 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-05 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| IREN | NASDAQ | 15.24 | -3.57 | 5.84 | — | 0.8x | 15.80 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-05 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| WSM | NYSE | 260.09 | 4.02 | 5.79 | — | 2.5x | 250.05 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-19 (0d ago) | PRE_GAP | Y | Q3 FY2026 results (reported 2026-11-19): net revenues USD1,991.2m, up 5.8% y/y, comparable brand revenue up 5.1%, operating margin 17.4% and non-GAAP diluted EPS of USD2.19, up 11.7% (GAAP USD2.38), with every brand and channel posting a positive comp |
| WYFI | NASDAQ | 8.51 | 0.00 | 5.76 | — | 0.7x | 8.51 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-10 (9d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RIOT | NASDAQ | 18.24 | 6.98 | 5.76 | — | 1.0x | 17.05 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-04 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PS | NYSE | 40.6 | -6.41 | 5.73 | — | 1.4x | 43.38 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-02 (17d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BRUN | NASDAQ | 4.54 | -2.99 | 5.73 | — | 0.6x | 4.68 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-12 (7d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-12 (Nasdaq earnings calendar; no headline lookup), consensus EPS ($0.17) |
| WDC | NASDAQ | 288.19 | 1.72 | 5.67 | — | 1.2x | 283.33 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-10-22 (28d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NET | NYSE | 300.91 | 5.66 | 5.67 | — | 1.2x | 284.80 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-05 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PL | NYSE | 12.05 | -3.52 | 5.64 | — | 1.3x | 12.49 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-09-03 (77d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RBRK | NYSE | 110 | 9.26 | 5.45 | — | 1.5x | 100.68 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-08-27 (84d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| WULF | NASDAQ | 12 | 2.83 | 5.42 | — | 0.9x | 11.67 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-06 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SATL | NASDAQ | 2.895 | -1.19 | 5.35 | — | 0.8x | 2.93 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-10 (9d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FPS | NYSE | 21.7 | 2.36 | 5.30 | — | 0.7x | 21.20 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-12 (7d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-12 (Nasdaq earnings calendar; no headline lookup), consensus EPS $0.18 |
| FLNC | NASDAQ | 4.03 | -1.23 | 5.26 | — | 1.0x | 4.08 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-08-05 (106d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ALAB | NASDAQ | 216.75 | 2.43 | 5.22 | — | 0.9x | 211.60 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-03 (16d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| APLD | NASDAQ | 14.45 | 1.62 | 5.19 | — | 0.8x | 14.22 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-10-07 (43d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GLXY | NASDAQ | 13.32 | 2.23 | 5.16 | — | 0.7x | 13.03 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-10-27 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SNDK | NASDAQ | 776.22 | -2.64 | 5.12 | — | n/a | 797.24 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-10-29 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| POET | NASDAQ | 4.25 | -3.41 | 5.10 | — | 0.8x | 4.40 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-16 (3d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-16 (Nasdaq earnings calendar; no headline lookup), consensus EPS ($0.07) |
| INIO | NASDAQ | 13.59 | -0.80 | 5.00 | — | 0.8x | 13.70 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-10-27 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| COHU | NASDAQ | 42.19 | 4.40 | 5.00 | — | 0.9x | 40.41 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-10-28 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MXL | NASDAQ | 49.53 | -3.68 | 4.99 | — | 0.7x | 51.42 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-10-22 (28d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ASST | NASDAQ | 17.15 | -5.20 | 4.96 | — | 0.9x | 18.09 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-06 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| OUST | NASDAQ | 29.3 | -3.87 | 4.95 | — | 0.8x | 30.48 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-03 (16d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MU | NASDAQ | 705.27 | -1.00 | 4.91 | — | 1.0x | 712.42 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-09-30 (50d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMKR | NASDAQ | 35.29 | 3.64 | 4.85 | — | 1.0x | 34.05 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-10-26 (24d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FLY | NASDAQ | 20.45 | -4.66 | 4.79 | — | 0.6x | 21.45 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-10 (9d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TTMI | NASDAQ | 69.41 | 4.00 | 4.74 | — | 0.7x | 66.74 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-10-22 (28d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| DELL | NYSE | 313.11 | -3.00 | 4.70 | — | 0.9x | 322.79 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-09-01 (79d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CORZ | NASDAQ | 14.05 | 4.00 | 4.70 | — | 0.8x | 13.51 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-05 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NTSK | NASDAQ | 23.505 | 12.73 | 4.66 | — | 1.1x | 20.85 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-09-02 (78d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| INTC | NASDAQ | 54.67 | -0.91 | 4.65 | — | 0.9x | 55.17 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-10-29 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| OKTA | NASDAQ | 195.61 | 12.07 | 4.63 | — | 1.2x | 174.54 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-08-26 (85d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RKLB | NASDAQ | 53.07 | -3.60 | 4.58 | — | 0.8x | 55.05 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-09 (10d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CAMT | NASDAQ | 98.42 | 3.64 | 4.52 | — | 1.0x | 94.96 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-04 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NVTS | NASDAQ | 7.3 | -3.95 | 4.52 | — | 0.7x | 7.60 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-03 (16d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ZS | NASDAQ | 197.83 | 6.83 | 4.33 | — | 1.6x | 185.19 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-09-03 (77d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LRCX | NASDAQ | 211.67 | 0.47 | 4.30 | — | 1.0x | 210.69 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-10-21 (29d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MRVL | NASDAQ | 145.54 | -2.15 | 4.29 | — | 0.7x | 148.74 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-08-27 (84d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MSTR | NASDAQ | 90.32 | -6.40 | 4.20 | — | 1.1x | 96.50 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-10-29 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RPD | NASDAQ | 15.34 | 12.55 | 4.17 | — | 1.0x | 13.63 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-04 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| QBTS | NASDAQ | 7.69 | -4.83 | 4.16 | — | 0.7x | 8.08 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-10 (9d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| IONQ | NYSE | 23.48 | -5.48 | 4.00 | — | 0.7x | 24.84 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-05 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BELFB | NASDAQ | 225.64 | 3.41 | 3.93 | — | 1.0x | 218.20 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-10-28 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GOOG | NASDAQ | 279.2 | 0.58 | 3.91 | — | 2.1x | 277.60 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-10-28 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LGN | NASDAQ | 36.08 | 3.53 | 3.88 | — | 0.6x | 34.85 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-12 (7d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-12 (Nasdaq earnings calendar; no headline lookup), consensus EPS $0.50 |
| KLAC | NASDAQ | 144.88 | 0.22 | 3.88 | — | 0.9x | 144.56 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-10-28 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GLW | NYSE | 108.15 | -0.31 | 3.87 | — | 1.0x | 108.49 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-10-27 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GOOGL | NASDAQ | 282.44 | 0.80 | 3.86 | — | 1.9x | 280.20 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-10-28 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LUNR | NASDAQ | 10.12 | -8.37 | 3.85 | — | 0.6x | 11.04 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-12 (7d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-12 (Nasdaq earnings calendar; no headline lookup), consensus EPS ($0.12) |
| ABSI | NASDAQ | 8.18 | 7.92 | 3.79 | — | 0.5x | 7.58 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-12 (7d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-12 (Nasdaq earnings calendar; no headline lookup), consensus EPS ($0.14) |
| FTNT | NASDAQ | 131.81 | 5.87 | 3.73 | — | 1.0x | 124.50 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-10-28 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FIX | NYSE | 1140.59 | 3.78 | 3.70 | — | 0.7x | 1099.02 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-10-22 (28d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FSLY | NASDAQ | 17.9 | 12.58 | 3.69 | — | 0.6x | 15.90 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-04 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| S | NYSE | 23.34 | 10.35 | 3.68 | — | 1.0x | 21.15 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-08-27 (84d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BELFA | NASDAQ | 174.71 | 3.43 | 3.61 | — | 0.9x | 168.91 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-10-28 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ANET | NYSE | 193.94 | 4.03 | 3.51 | — | 0.8x | 186.42 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-03 (16d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| COIN | NASDAQ | 110.51 | -3.92 | 3.47 | — | 0.9x | 115.02 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-10-29 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AGX | NYSE | 303.96 | 3.65 | 3.47 | — | 0.8x | 293.25 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-09-02 (78d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SNOW | NYSE | 279.62 | 2.45 | 3.47 | — | 1.2x | 272.94 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-09-02 (78d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SAIL | NASDAQ | 22.25 | 10.26 | 3.37 | — | 0.9x | 20.18 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-09-09 (71d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CAKE | NASDAQ | 120.05 | 7.23 | -3.37 | — | 1.2x | 111.96 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-10-27 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GEV | NYSE | 772.22 | -0.99 | 3.31 | — | 1.0x | 779.91 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-10-28 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CHKP | NASDAQ | 154.03 | 3.80 | 3.23 | — | 1.9x | 148.39 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-02 (17d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GNRC | NYSE | 205.45 | 9.87 | 3.19 | — | 0.9x | 187.00 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-10-28 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ORCL | NYSE | 113.89 | -0.97 | 3.12 | — | 0.8x | 115.00 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-09-10 (70d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SNPS | NASDAQ | 434.01 | -0.34 | 3.11 | — | 1.5x | 435.51 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-08-26 (85d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| HLIT | NASDAQ | 10.74 | 4.78 | 3.07 | — | 1.2x | 10.25 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-02 (17d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CBRS | NASDAQ | 94.15 | -9.63 | 3.07 | — | 0.5x | 104.18 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-12 (7d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-12 (Nasdaq earnings calendar; no headline lookup), consensus EPS ($0.13) |
| QLYS | NASDAQ | 197.24 | 12.92 | 3.05 | — | 0.7x | 174.67 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-09 (10d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TWST | NASDAQ | 116.35 | 3.88 | 3.01 | — | 0.5x | 112.00 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-12 (7d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-12 (Nasdaq earnings calendar; no headline lookup), consensus EPS ($0.43) |
| BLSH | NYSE | 20.36 | 5.66 | 3.00 | — | 0.6x | 19.27 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-18 (1d ago) | PRE_GAP | Y | Q3 2026 results (reported 2026-11-18): adjusted revenue USD84.4m, up 10% y/y and above the ~USD80.2m consensus, adjusted EBITDA USD35.6m at a 42% margin, diluted EPS USD3.57 on an IFRS basis driven by a USD598.4m digital-asset fair-value gain, and a new USD300m share repurchase authorization |
| MOD | NYSE | 137.88 | 6.28 | 2.99 | — | 0.5x | 129.73 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-03 (16d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BL | NASDAQ | 24.68 | -8.08 | 2.96 | — | 0.8x | 26.85 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-05 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TENB | NASDAQ | 44.68 | 15.75 | 2.95 | — | 0.7x | 38.60 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-10-28 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| XMTR | NASDAQ | 120.48 | 4.81 | 2.93 | — | 0.8x | 114.95 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-03 (16d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMD | NASDAQ | 530.14 | 5.31 | 2.83 | — | 0.5x | 503.41 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-03 (16d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GRAL | NASDAQ | 102.1 | -3.57 | 2.82 | — | 0.6x | 105.88 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-04 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AVGO | NASDAQ | 354.05 | 3.64 | 2.82 | — | 0.7x | 341.60 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-09-02 (78d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PWR | NYSE | 602.6 | 0.68 | 2.79 | — | 0.7x | 598.53 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-10-29 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TXN | NASDAQ | 292.43 | -1.16 | 2.79 | — | 1.1x | 295.86 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-10-21 (29d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| IBKR | NASDAQ | 76.45 | -0.01 | 2.77 | — | 1.1x | 76.46 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-10-15 (35d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MCK | NYSE | 1084.43 | -0.66 | -2.66 | — | 2.0x | 1091.67 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-04 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ADI | NASDAQ | 381.98 | -0.44 | 2.66 | — | 0.9x | 383.67 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-08-19 (92d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| KRMN | NYSE | 34.19 | -3.83 | 2.66 | — | 0.4x | 35.55 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-05 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| UUUU | AMEX | 5.64 | -4.89 | 2.66 | — | 0.6x | 5.93 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-04 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AGLT | NASDAQ | 6.85 | -4.46 | 2.63 | — | 0.4x | 7.17 | yahoo_chart_daily | 2026-11-17 | US-listed | — | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| APH | NYSE | 76.33 | -0.04 | 2.62 | — | 0.9x | 76.36 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-10-28 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PLTR | NASDAQ | 156.67 | 0.07 | 2.62 | — | 1.1x | 156.56 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-02 (17d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ERO | NYSE | 23.92 | -11.54 | 2.59 | — | 0.7x | 27.04 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-02 (17d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| DT | NYSE | 45.35 | 5.00 | 2.51 | — | 0.9x | 43.19 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-03 (16d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BB | NYSE | 8.56 | 4.90 | 2.45 | — | 0.6x | 8.16 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-09-24 (56d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GOOGN | NASDAQ | 41.44 | 0.63 | 2.44 | — | 1.6x | 41.18 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-10-28 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CDNS | NASDAQ | 305.82 | -0.37 | 2.36 | — | 1.0x | 306.97 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-10-26 (24d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| QCOM | NASDAQ | 159.81 | -4.12 | 2.35 | — | 0.7x | 166.67 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-04 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMZN | NASDAQ | 267.74 | 3.82 | 2.33 | — | 1.2x | 257.89 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-10-29 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ATI | NYSE | 180.87 | 3.87 | 2.28 | — | 0.7x | 174.13 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-10-29 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TTWO | NASDAQ | 216.61 | 6.22 | -2.28 | — | 0.8x | 203.93 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-09 (10d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FIGR | NASDAQ | 26.06 | 5.42 | 2.26 | — | 0.5x | 24.72 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-12 (7d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-12 (Nasdaq earnings calendar; no headline lookup), consensus EPS $0.31 |
| SHOP | NASDAQ | 139.42 | -1.75 | 2.25 | — | 0.8x | 141.90 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-03 (16d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AKAM | NASDAQ | 91.7 | 8.34 | 2.24 | — | 0.7x | 84.64 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-05 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GWRE | NYSE | 139.85 | -3.83 | 2.22 | — | 0.8x | 145.42 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-09-03 (77d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BFLY | NYSE | 6.08 | 5.74 | 2.14 | — | 0.4x | 5.75 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-10-29 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TTD | NASDAQ | 15.52 | 3.95 | 2.13 | — | 0.7x | 14.93 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-09 (10d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SKYD | NYSE | 6.63 | -4.19 | 2.11 | — | 0.7x | 6.92 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-09 (10d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LFTO | NASDAQ | 24 | 5.82 | 2.08 | — | 0.4x | 22.68 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-12 (7d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-12 (Nasdaq earnings calendar; no headline lookup), consensus EPS $0.17 |
| TSLA | NASDAQ | 383.72 | 0.95 | 2.08 | — | 0.8x | 380.11 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-10-21 (29d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| VG | NYSE | 12.04 | -3.68 | 2.08 | — | 0.6x | 12.50 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-10 (9d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CAT | NYSE | 558.77 | -2.11 | 2.05 | — | 0.7x | 570.79 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-10-29 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LIME | NASDAQ | 19.05 | -7.12 | 2.05 | — | 0.4x | 20.51 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-03 (16d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FUN | NYSE | 11.81 | 7.76 | 2.03 | — | 0.4x | 10.96 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-05 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| HAFN | NYSE | 8.92 | -3.88 | 2.02 | — | 0.8x | 9.28 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-18 (1d ago) | PRE_GAP | Y | Q3 2026 results (reported 2026-11-18): net profit of USD170.8m for the three months ended 30 September 2026, and a special interim dividend of 20.4m TORM shares announced alongside the three and nine months results |
| CEG | NASDAQ | 262.74 | -1.99 | 2.02 | — | 0.7x | 268.07 | yahoo_chart_daily | 2026-11-17 | US-listed | 2026-11-09 (10d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |

## US — QUIET one-liners

| Ticker | Venue | Chg % | Pre-mkt % | Post-mkt % | Move vs avg daily | Ref close | Ref source | Ref asof | US tradeable | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ETN | NYSE | 0.36 | 1.97 | — | 0.1x | 337.11 | yahoo_chart_daily | 2026-11-17 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| GENI | NYSE | 3.38 | -1.96 | — | 1.0x | 5.91 | yahoo_chart_daily | 2026-11-17 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| CSCO | NASDAQ | 2.18 | 1.95 | — | 0.9x | 95.11 | yahoo_chart_daily | 2026-11-17 | US-listed | — | Q4 2026 results, report date 2026-11-12 (Nasdaq earnings calendar; no headline lookup), consensus EPS $1.15 |
| JCI | NYSE | 1.54 | 1.94 | — | 0.6x | 136.32 | yahoo_chart_daily | 2026-11-17 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| NTCT | NASDAQ | 6.07 | 1.92 | — | 2.4x | 31.45 | yahoo_chart_daily | 2026-11-17 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| PRCT | NASDAQ | 5.89 | -1.87 | — | 2.1x | 23.78 | yahoo_chart_daily | 2026-11-17 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| EMR | NYSE | 1.79 | 1.85 | — | 1.1x | 159.15 | yahoo_chart_daily | 2026-11-17 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| SCCO | NYSE | -5.93 | 1.85 | — | 2.0x | 155.42 | yahoo_chart_daily | 2026-11-17 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| SDGR | NASDAQ | 6.00 | 1.84 | — | 1.1x | 25.66 | yahoo_chart_daily | 2026-11-17 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| LMND | NYSE | -4.07 | 1.83 | — | 1.1x | 41.01 | yahoo_chart_daily | 2026-11-17 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| UPBD | NASDAQ | 6.72 | -1.82 | — | 1.8x | 24.72 | yahoo_chart_daily | 2026-11-17 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| APP | NASDAQ | -2.01 | 1.81 | — | 0.4x | 398.94 | yahoo_chart_daily | 2026-11-17 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| FFIV | NASDAQ | 5.21 | 1.81 | — | 1.7x | 305.15 | yahoo_chart_daily | 2026-11-17 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| SPOT | NYSE | 0.64 | -1.79 | — | 0.3x | 602.01 | yahoo_chart_daily | 2026-11-17 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| GS | NYSE | -0.49 | 1.76 | — | 0.3x | 877.52 | yahoo_chart_daily | 2026-11-17 | US-listed | — | no catalyst lookup (outside the per-run budget) |

## EU/UK — Headline table

| Ticker | Market | Venue | Close | Chg % | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | Session asof | Settle | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SOI | france | EURONEXT | 114.3 | +17.18 | EUR | 3.3x | 97.54 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | live | none | 2026-11-18 (1d ago) | — | no catalyst lookup (outside the per-run budget) |
| OROX | italy | MIL | 9.46 | -14.47 | EUR | 16.0x | 11.06 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | live | none | — | — | no catalyst lookup (outside the per-run budget) |
| ATS | austria | VIE | 125 | +9.84 | EUR | 1.7x | 113.80 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | live | none | 2026-11-05 (14d ago) | N | no fresh catalyst found - no company-specific release found for 19 November; the move tracks the European AI and semiconductor rally after the Nvidia Q3 beat and the Anthropic IPO debut, and the 19 November voting-rights notification is a filing rather than a catalyst |
| KEOC | sweden | OMXSTO | 6.15 | +9.24 | SEK | 2.5x | 5.63 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | live | none | 2026-08-31 (80d ago) | N | PetroUrdaneta stake raised from 24% to 40% after the USD22.15m closing installment for the remaining 40% of Odebrecht E&P España was paid on 17 November; the Q3 interim report is due 24 November |
| BETCO_DKK | denmark | OMXCOP | 38.7 | -8.62 | DKK | 4.2x | 42.35 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | live | none | 2026-11-18 (1d ago) | — | no catalyst lookup (outside the per-run budget) |
| OHB | germany | XETR | 184 | +8.11 | EUR | 1.7x | 170.20 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | live | US line (OTC:OHBTF) | 2026-11-12 (7d ago) | — | no catalyst lookup (outside the per-run budget) |
| FMM_B | sweden | OMXSTO | 116 | +7.91 | SEK | 4.6x | 107.50 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | live | none | 2026-11-05 (14d ago) | — | no catalyst lookup (outside the per-run budget) |
| FG | sweden | OMXSTO | 15.1 | -7.81 | SEK | 2.5x | 16.38 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | live | none | 2026-11-12 (7d ago) | — | no catalyst lookup (outside the per-run budget) |
| TRUE_B | sweden | OMXSTO | 24.94 | +7.45 | SEK | 2.3x | 23.21 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | live | none | 2026-11-03 (16d ago) | — | no catalyst lookup (outside the per-run budget) |
| ART | spain | BME | 29.1 | +6.99 | EUR | 4.2x | 27.20 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | live | ADR (OTC:SURRY) | 2026-07-28 (114d ago) | — | no catalyst lookup (outside the per-run budget) |
| INVP | uk | LSE | 561 | -6.42 | GBX | 5.7x | 599.50 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | live | none | 2026-11-19 (0d ago) | — | no catalyst lookup (outside the per-run budget) |
| AIXA | germany | GETTEX | 33.75 | +6.13 | EUR | 1.5x | 31.88 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | live | none | 2026-10-29 (21d ago) | — | no catalyst lookup (outside the per-run budget) |
| BREE | uk | LSE | 301.8 | -5.92 | GBX | 4.8x | 320.80 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | live | none | 2026-07-29 (113d ago) | — | no catalyst lookup (outside the per-run budget) |
| SSPG | uk | LSE | 179.9 | -5.07 | GBX | 2.7x | 189.50 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | live | none | 2026-05-19 (184d ago) | N | no fresh catalyst found - no dated company release found for 19 November; the move follows the prior session 8.6% rebound and FY26 results are due 8 December |
| SLR | spain | BME | 14.215 | -5.04 | EUR | 1.7x | 14.97 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | live | none | 2026-11-19 (0d ago) | Y | 9M 2026 results (reported 2026-11-19): 9M revenue doubled to EUR260m, EBITDA EUR298.8m, up 30% and equal to 90% of the FY target, and net profit EUR177.9m, up 26%, on record output of +56%; EUR336m was invested in plants and batteries, part-funded by a EUR299.9m private placement, with capacity at 3.25GW heading to 3.52GW by year-end |
| IQMX | finland | OMXHEX | 6.45 | +4.96 | EUR | 1.2x | 6.14 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | live | none | 2026-11-05 (14d ago) | — | no catalyst lookup (outside the per-run budget) |
| BAB | uk | LSE | 1022.8385 | +4.91 | GBX | 2.7x | 975.00 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | live | none | 2026-11-19 (0d ago) | — | no catalyst lookup (outside the per-run budget) |
| NANO | france | EURONEXT | 25.22 | +4.73 | EUR | 1.3x | 24.08 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | live | US line (NASDAQ:NA) | 2026-09-24 (56d ago) | — | no catalyst lookup (outside the per-run budget) |
| IFCN | switzerland | SIX | 164 | +4.73 | CHF | 1.8x | 156.60 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | live | none | 2026-07-30 (112d ago) | — | no catalyst lookup (outside the per-run budget) |
| POS | austria | VIE | 33.8 | +4.64 | EUR | 3.6x | 32.30 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | live | none | 2026-08-27 (84d ago) | — | no catalyst lookup (outside the per-run budget) |
| ALO | france | EURONEXT | 8.874 | -4.62 | EUR | 1.5x | 9.30 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | live | none | 2026-11-17 (2d ago) | — | no catalyst lookup (outside the per-run budget) |
| BEAN | switzerland | SIX | 771.5 | +4.61 | CHF | 2.7x | 737.50 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | live | none | 2026-07-20 (122d ago) | — | no catalyst lookup (outside the per-run budget) |
| ASM | netherlands | EURONEXT | 700.6 | +4.57 | EUR | 1.4x | 670.00 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | live | US line (OTC:ASMXF) | 2026-10-27 (23d ago) | — | no catalyst lookup (outside the per-run budget) |
| PHM | spain | BME | 59.4 | -4.27 | EUR | 2.2x | 62.05 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | live | none | 2026-10-29 (21d ago) | — | no catalyst lookup (outside the per-run budget) |
| ADP | france | EURONEXT | 119.9 | +4.26 | EUR | 4.4x | 115.00 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | live | US line (OTC:AEOXF) | 2026-07-29 (113d ago) | — | no catalyst lookup (outside the per-run budget) |
| DEZ | germany | XETR | 7.985 | +4.24 | EUR | 1.3x | 7.66 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | live | none | 2026-11-05 (14d ago) | — | no catalyst lookup (outside the per-run budget) |
| SFSN | switzerland | SIX | 146.2 | +4.13 | CHF | 5.9x | 140.40 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | live | none | 2026-07-23 (119d ago) | — | no catalyst lookup (outside the per-run budget) |
| GRE | spain | BME | 58.2 | -4.12 | EUR | 1.3x | 60.70 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | live | none | 2026-09-16 (64d ago) | — | pending catalyst lookup |
| ASML | netherlands | EURONEXT | 1312.6 | +4.11 | EUR | 1.5x | 1260.80 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | live | ADR (NASDAQ:ASML) | 2026-10-14 (36d ago) | N | no fresh earnings event - the move tracks the European AI and semiconductor rebound after Nvidia Q3 beat and the Anthropic IPO debut, helped by a Bernstein upgrade of 2026-2027 wafer fabrication equipment spending (USD156bn for 2026, USD217bn for 2027) and ASML weekly buyback disclosure of about 326,000 shares bought back 9-13 November; US export-control rules remain an overhang |
| ACT0 | germany | XETR | 144.2 | -3.99 | EUR | 1.2x | 150.20 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | live | none | 2026-10-28 (22d ago) | — | no catalyst lookup (outside the per-run budget) |

## AU (ASX) — Headline table

| Ticker | Venue | Close | Chg % | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | Session asof | Settle | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MLX | ASX | 1.38 | -10.39 | AUD | 2.2x | 1.54 | yahoo_chart_daily | 2026-11-17 | 2026-11-19 | settled | none | 2026-08-27 (84d ago) | — | no catalyst lookup (outside the per-run budget) |
| C79 | ASX | 6.7 | +9.30 | AUD | 3.0x | 6.13 | yahoo_chart_daily | 2026-11-17 | 2026-11-19 | settled | none | 2026-08-09 (102d ago) | N | Pre-AGM trading update (19 November): FY27 July-October revenue USD36.7m, up 27% on the prior corresponding period, samples processed 4.91m, up 43% with a record 1.36m in October, 15 new PhotonAssay lease agreements taking contracted units to 97 and the deployed fleet to 51, and FY27 guidance reaffirmed at USD108-118m revenue and USD35-42m EBITDA |
| RIC | ASX | 2.45 | -8.24 | AUD | 7.1x | 2.67 | yahoo_chart_daily | 2026-11-17 | 2026-11-19 | settled | none | 2026-08-20 (91d ago) | N | AGM CEO and Managing Director address (18 November): FY26 underlying EBITDA USD157.8m, up 61.8% on nine months of Incitec Pivot Fertilisers, operating cash flow USD122.4m, headline leverage 0.85x and a fully franked 10.45c final dividend, with the FY27 growth outlook left unchanged but Ingredients flagged as the recovery proof point after a USD31.8m NovaqPro write-off |

## APAC/Gulf — Headline table

| Ticker | Market | Venue | Close | Chg % | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | Session asof | Settle | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| HRME | indonesia | IDX | 58 | +34.88 | IDR | 3.6x | 43.00 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| PTSP | indonesia | IDX | 2670 | +24.77 | IDR | 2.7x | 2140.00 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| IFSH | indonesia | IDX | 910 | +24.66 | IDR | 4.7x | 730.00 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| 301348 | china | SZSE | 21.66 | +20.00 | CNY | 6.0x | 18.05 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| 301010 | china | SZSE | 19.92 | -20.00 | CNY | 3.4x | 24.90 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| 688801 | china | SSE | 364.33 | -20.00 | CNY | 2.3x | 455.41 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| VEEFIN | india | NSE | 298.05 | +20.00 | INR | 4.4x | 248.38 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| KESARPE | india | BSE | 11.26 | -19.97 | INR | 2.9x | 14.07 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| TINNARUBR | india | BSE | 989.95 | +19.65 | INR | 6.1x | 827.35 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| SENA | thailand | SET | 1.3 | -9.72 | THB | 8.9x | 1.44 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| ATM | newzealand | NZX | 8.01 | -9.70 | NZD | 5.8x | 8.87 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | settled | none | 2026-08-16 (95d ago) | N | 2026 Annual Meeting Chair speech and CEO address (19 November): FY26 revenue NZD1,974.9m, up 12.4%, and underlying net profit NZD235.8m, up 7.0%, but FY27 revenue growth is now guided to mid single digit with the first half slightly down as China-label infant milk formula recovers more slowly after the 4Q26 supply chain disruption left offtake near 50% of pre-disruption levels |
| NOBLE | thailand | SET | 1.22 | +7.96 | THB | 3.7x | 1.13 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | settled | US line (OTC:NBHEF) | 2026-11-13 (6d ago) | Y | Q3 and 9M 2026 results (reported 2026-11-13): real estate sales revenue THB2,331m, up 45% y/y, and Q3 presales THB3,906m, up 391%, but a net loss of THB483m on pricing actions to clear inventory; the board has since approved a THB800-900m rights offering at THB1.35-1.65 per share |
| JTS | thailand | SET | 13.1 | +7.82 | THB | 1.8x | 12.15 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| 4144 | ksa | TADAWUL | 73 | -5.13 | SAR | 1.1x | 76.95 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| 8200 | ksa | TADAWUL | 28 | -5.08 | SAR | 1.5x | 29.50 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | settled | none | 2026-11-01 (18d ago) | — | no catalyst lookup (outside the per-run budget) |
| FRW | newzealand | NZX | 13.32 | +4.06 | NZD | 3.0x | 12.80 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | settled | none | 2026-08-17 (94d ago) | N | no fresh catalyst found - no dated company release found for 19 November; the last company disclosure was the Q1 FY27 trading update at the Annual Shareholders Meeting, with revenue up 17.6% and NPAT up 12.0% |
| Z74 | singapore | SGX | 4.2 | +3.96 | SGD | 3.2x | 4.04 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | settled | none | 2026-11-13 (6d ago) | — | no catalyst lookup (outside the per-run budget) |
| AWX | singapore | SGX | 6.3 | -3.82 | SGD | 0.7x | 6.55 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | settled | none | 2026-08-12 (99d ago) | — | no catalyst lookup (outside the per-run budget) |
| Z77 | singapore | SGX | 4.17 | +3.22 | SGD | 2.6x | 4.04 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | settled | none | 2026-11-13 (6d ago) | — | no catalyst lookup (outside the per-run budget) |

## Source health

- scanner_calls: 57 | scanner_errors: 0
- markets_scanned: US + 17 EU/UK + ASX + 7 APAC/Gulf (india, thailand, indonesia, china, singapore, newzealand, ksa)
- pipeline_version: 2026-11-16.2
- et_clock: zoneinfo America/New_York (DST-aware; a fixed UTC-4 mislabels every winter fire)
- premarket_window: 04:00-09:30 ET, resolved with zoneinfo (09:00-14:30 UTC in winter, 08:00-13:30 UTC in summer)
- session_selection: by DATE and order, never by a modal time-of-day. Yahoo stamps a daily bar at the session open, so the ET stamp of the SAME session shifts by one hour across a DST boundary; a modal filter kept the OLDER bars and discarded the NEWEST ones, which rolled the base back to the prior-prior session (66 US + 21 ASX rows lost on 2026-11-03, 24 of 25 ASX rows lost on 2026-11-04).
- yahoo_calls: 213 | yahoo_429: 0 | yahoo_errors: 0 | yahoo_breaker: closed
- reference_close (screener vs Yahoo, resolved BEFORE the tables were built): agree=200 mismatch=3 unverified=0 stale_reference=3
  method: the screener's implied reference close (close / (1 + change/100)) is compared
  with Yahoo's own reference close. A match proves the move was measured against the
  TRUE prior close; a mismatch means the row sits on a STALE reference (phantom move).
  Coverage: every row of the US headline, US QUIET, EU/UK and ASX tables is checked.
  Yahoo bar mode: {"closed": 170, "live": 30} (closed = last completed session bar;
  live = in-progress EU/UK session bar, which is what a weekday 08:00 ET EU move needs)
  live drift between the screener snapshot and the later Yahoo print: median=0.00pp max=1.42pp (expected on a live market)
- cross_check mismatches: [{"region": "US", "symbol": "AMAT", "tv": -0.15, "yahoo": 0.879, "delta": -1.029, "ref_delta_pct": 0.879, "tv_implied_ref": 352.3, "yahoo_ref": 349.23, "yahoo_date": "2026-11-18", "yahoo_ref_date": "2026-11-17", "verdict": "stale_reference"}, {"region": "AU", "symbol": "CMW.AX", "tv": 422.857, "yahoo": 1.449, "delta": 421.408, "ref_delta_pct": -79.71, "tv_implied_ref": 0.35, "yahoo_ref": 1.725, "yahoo_date": "2026-11-17", "yahoo_ref_date": "2026-11-16", "verdict": "stale_reference"}, {"region": "ksa", "symbol": "3008.SR", "tv": 1015.842, "yahoo": -4.729, "delta": 1020.571, "ref_delta_pct": -91.462, "tv_implied_ref": 1.01, "yahoo_ref": 11.8295, "yahoo_date": "2026-11-19", "yahoo_ref_date": "2026-11-18", "verdict": "stale_reference"}]
- rows_dropped_stale_ref: 3 (rows whose screener-implied reference close disagreed with Yahoo's by more than 0.5%; they are dropped, not published)
- rows_dropped_unresolved_ref: 0 (rows whose reference close could not be resolved from Yahoo at all - the base of the move is unverifiable, so the row is dropped rather than published with a '—' base)
- us_premarket_check (Yahoo 1-min pre/post feed vs the screener pre-market column, base = the IMMEDIATELY prior session's close): checked=10 within_1pp=7 within_3pp=9 unavailable=0
  us_premarket outliers (>3pp; thin pre-market books, not a screener error): [{"symbol": "UMAC", "tv": 7.284, "yahoo": 11.341, "delta": 4.057, "yahoo_asof": "08:14"}]
- markets_with_lt5_rows: ['france:less=4', 'netherlands:egreater=3', 'netherlands:less=0', 'belgium:egreater=1', 'belgium:less=2', 'portugal:egreater=0', 'portugal:less=0', 'ireland:egreater=0', 'ireland:less=0', 'italy:egreater=2', 'italy:less=2', 'switzerland:less=3', 'spain:egreater=2', 'norway:less=1', 'denmark:egreater=1', 'denmark:less=1', 'finland:egreater=1', 'finland:less=1', 'poland:less=3', 'austria:egreater=2', 'austria:less=1', 'greece:egreater=1', 'greece:less=0', 'singapore:egreater=3', 'singapore:less=2', 'newzealand:egreater=1', 'newzealand:less=2', 'ksa:egreater=2']
  NOTE: this fires per market AND direction, so it is NOT a coverage-failure signal on
  its own. A 'less' count of 0-3 means almost nothing fell more than 2.5% that session
  (a broad up-day); a small 'egreater' count usually means a small market with few
  names above the $1B market-cap floor. Check the median change before calling it a gap.
- filters: volume>10000 (removes stale-reference rows), country=home for EU/UK/AU,
  exchange drop-list for US, US venue allow-list, US preferred (slash ticker) excluded
- pass_b2 (US pre-market gap scan - "gapped today, flat yesterday"): candidates=37 deduped_against_pass_a_b=15 published=22 (up=35 down=2)
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
- bod_no_extended_hours: 165 (deferred to the next scan; not in the headline table)
- earnings_source: screener `earnings_release_date` (last FULL report) + `earnings_release_next_date` (next scheduled)
- earnings_caveat: `earnings_release_date` does NOT capture preliminary, guidance or
  restructuring releases. On 2026-10-23 LKQ fell 22.47% on a preliminary Q3 miss while
  the field still read 2026-07-30. ALWAYS confirm the earnings-driven flag against the
  headline itself; the calendar field is a screen, not a verdict.
- us_line_index: ok (US-listed lines for the 25 foreign home countries, both scanner types; the `US tradeable` column is ADR / US-listed / none)
- catalyst_note: Catalyst lookups: 6 US + 5 EU + 2 AU + 3 APAC/Gulf = 16 per run - the skill's cap, allocated by the evidence gap.
- catalyst_merge: region-matched - a row may only use a catalog entry from its OWN region;
  the same ticker on another venue is a different company and is not used.
- catalyst_budget: 6 US + 5 EU + 2 AU + 3 APAC/Gulf = 16 lookups per run (cap 16), allocated by the evidence gap: the US slice covers the rows whose earnings event can still explain today's move, the EU/AU/APAC floors are never squeezed because no bulk calendar reaches those markets, and whatever the US slice does not need goes to the region with the most unexplained rows
- earnings_calendar: Nasdaq public earnings calendar (calls=8 errors=0 symbols=976) - the source of record for the US earnings date, and the ranking key for the search budget
- earnings_field_stale_rows: 2 (the screener's earnings_release_date disagreed with the calendar; the calendar's date is published)
- earnings_field_stale_detail: [{"ticker": "MANU", "screener": "2026-09-23", "calendar": "2026-11-19"}, {"ticker": "WSM", "screener": "2026-08-26", "calendar": "2026-11-19"}]
- earnings_dates: the published `Last earnings` date by source - catalog (researched) 8, calendar 14, asx 0, screener 163. The chain is researched -> calendar (US) -> ASX feed (AU) -> the screener's field, which is the FALLBACK and the one that lags (2026-11-12: NBIS carried the previous quarter's date on the morning it reported, and MEKO, NORBT and FG carried July and August dates on the morning they all reported).
- asx_announcements: 6 results-classified announcement(s) for the last ASX session (calls=1 errors=0); the announcement date IS the report date, and the meeting/AGM/offer/assay headlines are excluded because they are not reports
- earnings_date_quality: 4 of 20 markets publish a FRESH earnings date (median age <= 14d); the table below gives each market's rows, the rows with NO date at all, the median age of the published date and the rows within 7 and 30 days - the reader sees the input quality instead of trusting it
| market | rows | no date | median age | <=7d | <=30d |
|---|---|---|---|---|---|
| au | 3 | 0 | 91d | 0 | 0 |
| austria | 2 | 0 | 84d | 0 | 1 |
| china | 3 | 3 | n/a | 0 | 0 |
| denmark | 1 | 0 | 1d | 1 | 1 |
| finland | 1 | 0 | 14d | 0 | 1 |
| france | 4 | 0 | 56d | 2 | 2 |
| germany | 4 | 0 | 21d | 1 | 4 |
| india | 3 | 3 | n/a | 0 | 0 |
| indonesia | 3 | 3 | n/a | 0 | 0 |
| italy | 1 | 1 | n/a | 0 | 0 |
| ksa | 2 | 1 | 18d | 0 | 1 |
| netherlands | 2 | 0 | 36d | 0 | 1 |
| newzealand | 2 | 0 | 95d | 0 | 0 |
| singapore | 3 | 0 | 6d | 2 | 2 |
| spain | 4 | 0 | 64d | 1 | 2 |
| sweden | 4 | 0 | 16d | 1 | 3 |
| switzerland | 3 | 0 | 119d | 0 | 0 |
| thailand | 3 | 2 | 6d | 1 | 1 |
| uk | 4 | 0 | 113d | 2 | 2 |
| us | 133 | 1 | 17d | 20 | 110 |
- earnings_tiers: fresh=2 near=4 (fresh = the report is dated on the scan date, near = the previous session)
- one_table_rule: each name appears exactly once, in exactly one table, with its
  catalyst in that row's last column. There is no separate catalysts section.
- data_date: US regular session close of the prior trading day; extended-hours columns
  carry the prior session's prints
- settlement_state: 22 settled, 30 live (a live row's move is a mid-session snapshot, not the session's result)
- rows_per_market (EU/UK, cap 4/market): {'france': 4, 'italy': 4, 'austria': 3, 'sweden': 4, 'denmark': 2, 'germany': 4, 'spain': 4, 'uk': 4, 'finland': 2, 'switzerland': 4, 'netherlands': 3, 'poland': 4, 'belgium': 3, 'norway': 4, 'greece': 1} — the cap stops one thin market taking the table; the EU/UK table was 28% Sweden over nine runs (73 of 264 rows) while Belgium and Greece never appeared once.
- rows_per_market (APAC/Gulf, cap 3/market): {'ksa': 3, 'indonesia': 3, 'china': 3, 'india': 3, 'thailand': 3, 'newzealand': 2, 'singapore': 3}
- deprecations: mcp__tradingview-advanced__*, mcp__tradingview__*, mcp__financekit__*,
  mcp__stocktwits__* are ABSENT in Cloud sessions (tool_search 0 hits; connector catalog
  holds only media + credential tools). The public screener replaces them.

- degraded_sources: 0
  (none - every source answered for every published row)

## Audit line

`earnings-reaction target=earnings-reactions:2026-11-19 candidates=577 amc_reactions=0 pre_gaps=133 eu_reactions=30 asx_reactions=3 apac_reactions=19 catalyst_lookups=16 bod=165 pass_b2_candidates=37 pass_b2_dedup=15 pass_b2_published=22 earnings_calendar_rows=976 earnings_tiers_fresh=2 earnings_tiers_near=4 earnings_field_stale_rows=2 earnings_dates_catalog=8 earnings_dates_asx=0 asx_ann_rows=6 rows_dropped_stale_ref=3 rows_dropped_unresolved_ref=0 degraded_sources=0`
