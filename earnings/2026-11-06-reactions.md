# Earnings reaction scanner — 2026-11-06

- Cron: `0 8 * * 1-5` America/New_York (weekdays, 08:00 ET)
- Fire time (ET): 2026-11-06 08:23:15 Fri
- Run type: `scheduled_scan`
- Source: TradingView public screener (`scanner.tradingview.com/<market>/scan`);
  Yahoo chart API as the independent reference-close source.
- Method: 4 passes (US top-200 mcap, US prior-session movers, EU/UK movers,
  ASX movers). Volume floor 10,000 on every pass; `country` filter for
  primary listings; exchange drop-list applied.
- artifact_contract: REACTION_ARTIFACT_V2
- ref_close_source: yahoo_chart_daily (Yahoo Finance daily chart bars; the base
  every published row is measured against)
- Status: `ok`

## TL;DR

- 0 AMC reactions, 198 pre-market gaps, 72 without extended-hours data; 29 EU/UK and 25 ASX movers.
- Biggest US extended-hours move: FROG PRE_GAP (22.96%).
- Biggest EU/UK move: TEP (-17.85%, france).
- Biggest ASX move: DVP (-10.13%).
- EU/AU earnings-driven tagging is keyword-based on headlines (best-effort).

## Actionable read

- **Move vs this name's own history.** The `Move vs avg daily` column divides the
  reaction by the name's own mean absolute daily move over its last
  20 completed sessions. A -27% move in a name that averages +-3% is a
  different event from a -8% move in a name that averages +-7%.
- **US-listed and tradeable vs foreign-only.** 213 published US rows are on a
  US venue; 5 more foreign reactions have a US ADR line
  (the `US tradeable` column carries the ticker); 49 are foreign-only and
  cannot be bought directly by a US reader.
- **Not yet fully priced — US (hypothesis, not a recommendation).**
  ABNB — +14.32%, 1.89% mean absolute daily move over the last 20 completed sessions, 7.6x that average, reference close 176.37 dated 2026-11-04, US access: US-listed, the move now (+14.32%) is larger than the move it follows (-3.54%); the reaction is still being repriced. Hypothesis only: this artifact states no
  direction and no trade.
- **Not yet fully priced — EU/UK (hypothesis, not a recommendation).**
  BTS_B — +16.09%, 0.94% mean absolute daily move over the last 20 completed sessions, 17.1x that average, reference close 230.00 dated 2026-11-05, US access: none, the move now (+16.09%) is larger than the move it follows (+3.37%); the reaction is still being repriced. Hypothesis only: this artifact states no
  direction and no trade.
- **Not yet fully priced — AU (ASX) (hypothesis, not a recommendation).**
  SGM — -7.22%, 2.50% mean absolute daily move over the last 20 completed sessions, 2.9x that average, reference close 21.18 dated 2026-11-04, US access: none, the move now (-7.22%) is larger than the move it follows (+1.05%); the reaction is still being repriced. Hypothesis only: this artifact states no
  direction and no trade.

## US — Headline table

| Ticker | Venue | Close | Chg % | Pre-mkt % | Post-mkt % | Move vs avg daily | Ref close | Ref source | Ref asof | US tradeable | Last earnings | Tag | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FROG | NASDAQ | 74.62 | -13.57 | 22.96 | — | 5.1x | 86.34 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-06 (92d ago) | PRE_GAP | Y | Q3 2026 results (5 Nov after close): revenue $179.2M, +31% YoY; cloud revenue $101.5M, +60%; FY26 revenue guidance raised to $680-682M |
| NET | NYSE | 244.51 | -8.28 | 18.86 | — | 4.9x | 266.58 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-06 (92d ago) | PRE_GAP | Y | Q3 2026 results (5 Nov after close): revenue $782.5M, +39% YoY vs $739.7M est; GAAP operating loss $67.9M; Q4 revenue guided $845-846M |
| LASR | NASDAQ | 29.34 | -11.06 | 16.56 | — | 4.7x | 32.99 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-06 (92d ago) | PRE_GAP | Y | Q3 2026 results (5 Nov after close): revenue $73.8M beat $68M est; adj. EPS $0.16 vs $0.06 est (GAAP net loss $7.2M); Q4 revenue guided $84-90M |
| IREN | NASDAQ | 18.03 | -16.95 | 16.03 | — | 2.4x | 21.71 | yahoo_chart_daily | 2026-11-04 | US-listed (ADR) | 2026-08-27 (71d ago) | PRE_GAP | Y | Q1 FY27 results (5 Nov after close): revenue $228M, +66% QoQ; AI Cloud revenue $200M (nearly tripled); Horizon 1 live for Microsoft with NVIDIA Exemplar status; >$4B ARR target slips to Jan/Feb 2027 |
| VCEL | NASDAQ | 51.78 | 13.85 | 15.86 | — | 5.2x | 45.48 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-07-30 (99d ago) | PRE_GAP | Y | Q3 2026 results (5 Nov after close): EPS $0.27 vs $0.06 est (+382% surprise); revenue and EPS beat; full-year guidance raised |
| ABNB | NASDAQ | 170.13 | -3.54 | 14.32 | — | 7.6x | 176.37 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-11-05 (1d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| DIOD | NASDAQ | 68.36 | -13.97 | 12.93 | — | 3.2x | 79.46 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-05 (93d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CIFR | NASDAQ | 5.55 | -14.62 | 11.53 | — | 1.4x | 6.50 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-11-02 (4d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FLY | NASDAQ | 15.175 | -11.57 | 11.30 | — | 2.5x | 17.16 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-11 (87d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SITM | NASDAQ | 355 | -11.97 | 11.28 | — | 2.1x | 403.27 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-11-04 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LRCX | NASDAQ | 185.2 | -16.36 | 10.96 | — | 2.6x | 221.43 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-21 (16d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| INOD | NASDAQ | 38.62 | -10.81 | 10.82 | — | 1.9x | 43.30 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-06 (92d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CRDO | NASDAQ | 112.33 | -17.71 | 10.20 | — | 1.5x | 136.50 | yahoo_chart_daily | 2026-11-04 | US-listed (ADR) | 2026-09-01 (66d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BE | NYSE | 167.52 | -16.41 | 9.96 | — | 1.6x | 200.40 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-22 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NBIS | NASDAQ | 120.37 | -14.94 | 9.86 | — | 1.6x | 141.52 | yahoo_chart_daily | 2026-11-04 | US-listed (ADR) | 2026-08-12 (86d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ICHR | NASDAQ | 28.03 | -16.85 | 9.70 | — | 1.7x | 33.71 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-11-02 (4d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SNDK | NASDAQ | 806.43 | -22.26 | 9.62 | — | 1.7x | 1037.40 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-29 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| APLD | NASDAQ | 14.17 | -14.69 | 9.53 | — | 1.4x | 16.61 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-07 (30d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PENG | NASDAQ | 37.22 | -23.02 | 9.52 | — | 1.3x | 48.35 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-06 (31d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MRVL | NASDAQ | 133.55 | -16.43 | 9.46 | — | 1.7x | 159.80 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-27 (71d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| UCTT | NASDAQ | 37.2 | -15.53 | 9.46 | — | 1.5x | 44.04 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-27 (10d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| COHR | NYSE | 169.76 | -12.98 | 9.38 | — | 1.8x | 195.09 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-11-04 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MXL | NASDAQ | 44.31 | -22.06 | 9.33 | — | 1.3x | 56.85 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-22 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LITE | NASDAQ | 509.7 | -18.68 | 9.28 | — | 1.5x | 626.75 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-11-02 (4d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CECO | AMEX | 37.66 | -17.05 | 9.24 | — | 1.7x | 45.40 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-10 (88d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ONTO | NYSE | 155.99 | -15.60 | 8.99 | — | 1.7x | 184.82 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-06 (92d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AEHR | NASDAQ | 49.16 | -19.20 | 8.87 | — | 1.2x | 60.84 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-07-14 (115d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TSEM | NASDAQ | 130.99 | -11.97 | 8.82 | — | 1.6x | 148.80 | yahoo_chart_daily | 2026-11-04 | US-listed (ADR) | 2026-11-02 (4d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FORM | NASDAQ | 71.76 | -15.81 | 8.75 | — | 1.3x | 85.24 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-28 (9d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AXTI | NASDAQ | 36.72 | -22.76 | 8.74 | — | 1.1x | 47.54 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-29 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TER | NASDAQ | 212.74 | -15.24 | 8.50 | — | 1.8x | 250.99 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-27 (10d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ALAB | NASDAQ | 179.47 | -19.62 | 8.41 | — | 1.6x | 223.27 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-11-03 (3d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| VICR | NASDAQ | 135.1 | -15.07 | 8.32 | — | 1.1x | 159.07 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-20 (17d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FPS | NYSE | 18.21 | -18.85 | 8.18 | — | 1.1x | 22.44 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-09-15 (52d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FSLY | NASDAQ | 15.38 | -26.88 | 8.13 | — | 1.3x | 21.04 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-11-04 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SEI | NYSE | 50.55 | -12.30 | 8.09 | — | 1.3x | 57.64 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-11-04 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| IONQ | NYSE | 26.43 | -10.53 | 8.02 | — | 1.6x | 29.54 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-05 (93d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PLPC | NASDAQ | 252.03 | -11.63 | 7.93 | — | 1.7x | 285.20 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-28 (9d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| DELL | NYSE | 316.91 | -14.89 | 7.92 | — | 1.5x | 372.36 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-09-01 (66d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| WULF | NASDAQ | 10.08 | -13.85 | 7.84 | — | 1.2x | 11.70 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-11-06 (0d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMAT | NASDAQ | 319.25 | -13.58 | 7.82 | — | 2.0x | 369.40 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-13 (85d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CHRN | NASDAQ | 10.16 | -15.68 | 7.78 | — | 1.1x | 12.05 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-15 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FN | NYSE | 292.97 | -14.25 | 7.76 | — | 1.4x | 341.64 | yahoo_chart_daily | 2026-11-04 | US-listed (ADR) | 2026-11-02 (4d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMD | NASDAQ | 404.4 | -17.26 | 7.74 | — | 1.7x | 488.78 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-11-03 (3d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ACMR | NASDAQ | 39.31 | -11.52 | 7.73 | — | 1.7x | 44.43 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-11-05 (1d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MTSI | NASDAQ | 190.35 | -18.35 | 7.73 | — | 1.5x | 233.13 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-06 (92d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SMTC | NASDAQ | 91.54 | -17.50 | 7.60 | — | 1.1x | 110.96 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-25 (73d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMKR | NASDAQ | 30.49 | -14.50 | 7.58 | — | 1.6x | 35.66 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-26 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| STX | NASDAQ | 466.53 | -16.25 | 7.50 | — | 1.6x | 557.06 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-27 (10d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| COHU | NASDAQ | 34.9 | -20.65 | 7.48 | — | 1.2x | 43.98 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-28 (9d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TTMI | NASDAQ | 62.22 | -15.21 | 7.46 | — | 1.0x | 73.38 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-22 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| OKLO | NYSE | 19.2 | -13.20 | 7.40 | — | 1.8x | 22.12 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-07 (91d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| WDC | NASDAQ | 267.63 | -17.35 | 7.27 | — | 1.4x | 323.83 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-22 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| VRT | NYSE | 176.73 | -14.02 | 7.24 | — | 1.4x | 205.55 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-28 (9d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MU | NASDAQ | 656.39 | -17.46 | 7.23 | — | 1.6x | 795.23 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-09-30 (37d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| STRL | NASDAQ | 244.34 | -13.86 | 7.23 | — | 1.3x | 283.66 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-28 (9d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ALGM | NASDAQ | 26.8 | -14.24 | 7.09 | — | 1.5x | 31.25 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-29 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CIEN | NYSE | 230.81 | -15.22 | 7.01 | — | 1.1x | 272.24 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-09-03 (64d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CLS | NYSE | 205.64 | -13.02 | 6.98 | — | 1.2x | 236.41 | yahoo_chart_daily | 2026-11-04 | US-listed (ADR) | 2026-10-26 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RMBS | NASDAQ | 69.68 | -15.95 | 6.92 | — | 1.6x | 82.90 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-26 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| HPE | NYSE | 44.16 | -11.84 | 6.91 | — | 1.5x | 50.09 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-09-02 (65d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FLEX | NASDAQ | 66.73 | -13.61 | 6.86 | — | 1.3x | 77.24 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-28 (9d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| KLAC | NASDAQ | 129.8 | -13.35 | 6.85 | — | 1.8x | 149.79 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-28 (9d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GENB | NASDAQ | 12.57 | -11.23 | 6.84 | — | 1.2x | 14.16 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-06 (92d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| P | NYSE | 93.44 | -16.40 | 6.70 | — | 1.3x | 111.77 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-26 (72d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CORZ | NASDAQ | 11.38 | -10.82 | 6.68 | — | 1.1x | 12.76 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-07-28 (101d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FRVO | NASDAQ | 7.79 | -12.47 | 6.68 | — | 1.1x | 8.90 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-12 (86d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| EROC | NYSE | 6.64 | -16.37 | 6.63 | — | 1.0x | 7.94 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-11 (87d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BTDR | NASDAQ | 5.31 | -18.68 | 6.51 | — | 1.0x | 6.53 | yahoo_chart_daily | 2026-11-04 | US-listed (ADR) | 2026-08-10 (88d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| KLIC | NASDAQ | 59.83 | -12.58 | 6.47 | — | 1.7x | 68.44 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-05 (93d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RBRK | NYSE | 105.74 | -11.14 | 6.44 | — | 1.8x | 118.99 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-27 (71d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| DOCN | NYSE | 70.7 | -15.85 | 6.44 | — | 1.2x | 84.02 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-11-03 (3d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FIX | NYSE | 964.94 | -11.58 | 6.38 | — | 1.2x | 1091.31 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-22 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CHTR | NASDAQ | 125.86 | 4.67 | -6.25 | — | 2.2x | 120.25 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-11-06 (0d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| VSAT | NASDAQ | 59.38 | -11.09 | 6.10 | — | 1.3x | 66.79 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-04 (94d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CLSK | NASDAQ | 5.68 | -16.47 | 5.93 | — | 1.0x | 6.80 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-06 (92d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| VSH | NYSE | 22.02 | -14.78 | 5.90 | — | 1.2x | 25.84 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-11-04 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GLW | NYSE | 103.43 | -12.92 | 5.87 | — | 1.7x | 118.77 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-27 (10d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MNST | NASDAQ | 47.83 | -1.89 | -5.86 | — | 3.8x | 48.75 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-11-05 (1d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NVTS | NASDAQ | 7.86 | -15.76 | 5.86 | — | 1.0x | 9.33 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-11-03 (3d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| IESC | NASDAQ | 145.58 | -13.89 | 5.78 | — | 1.3x | 169.07 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-07-31 (98d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MPWR | NASDAQ | 1131.43 | -10.28 | 5.63 | — | 1.6x | 1261.08 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-29 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| WOLF | NYSE | 20.36 | -10.66 | 5.60 | — | 0.9x | 22.79 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-11-04 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AEIS | NASDAQ | 185.66 | -12.24 | 5.57 | — | 1.2x | 211.56 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-11-02 (4d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ANET | NYSE | 159.16 | -10.82 | 5.55 | — | 1.4x | 178.48 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-11-03 (3d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| INFQ | NYSE | 7.44 | -13.08 | 5.38 | — | 1.0x | 8.56 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-12 (86d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ADEA | NASDAQ | 14.82 | -12.44 | 5.26 | — | 1.2x | 16.93 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-11-02 (4d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MARA | NASDAQ | 5.875 | -14.48 | 5.20 | — | 1.0x | 6.87 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-06 (92d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LBRT | NYSE | 11.35 | -13.69 | 5.17 | — | 1.1x | 13.15 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-21 (16d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| POWL | NASDAQ | 125.06 | -12.61 | 5.15 | — | 1.2x | 143.10 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-03 (95d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| VIAV | NASDAQ | 26.3 | -10.48 | 5.09 | — | 0.9x | 29.38 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-11-04 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BELFA | NASDAQ | 154.76 | -11.15 | 5.00 | — | 1.4x | 174.19 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-28 (9d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LUNR | NASDAQ | 8.62 | -13.19 | 4.99 | — | 1.0x | 9.93 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-13 (85d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SNOW | NYSE | 269.54 | -7.25 | 4.96 | — | 1.6x | 290.60 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-09-02 (65d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CBRS | NASDAQ | 81.71 | -11.04 | 4.92 | — | 0.9x | 91.85 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-12 (86d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NVT | NYSE | 98.38 | -12.80 | 4.90 | — | 1.0x | 112.82 | yahoo_chart_daily | 2026-11-04 | US-listed (ADR) | 2026-10-30 (7d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| INTC | NASDAQ | 52.25 | -10.33 | 4.88 | — | 1.0x | 58.27 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-29 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ENTG | NASDAQ | 124.75 | -12.68 | 4.85 | — | 1.0x | 142.87 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-29 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| IPGP | NASDAQ | 62.03 | -11.52 | 4.79 | — | 1.7x | 70.11 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-11-03 (3d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| XE | NASDAQ | 9 | -10.45 | 4.78 | — | 1.1x | 10.05 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-13 (85d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CRWD | NASDAQ | 217.2 | -9.88 | 4.77 | — | 1.5x | 241.00 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-26 (72d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SPCX | NASDAQ | 123.62 | -9.05 | 4.69 | — | 1.5x | 135.92 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-20 (17d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PWR | NYSE | 509.06 | -12.30 | 4.68 | — | 1.2x | 580.44 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-29 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RKLB | NASDAQ | 45.99 | -12.18 | 4.59 | — | 1.0x | 52.37 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-10 (88d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| U | NYSE | 48.8 | 14.93 | 4.51 | — | 1.3x | 42.46 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-06 (92d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AAOI | NASDAQ | 46.89 | -20.89 | 4.50 | — | 0.7x | 59.27 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-06 (92d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AVGO | NASDAQ | 291.53 | -10.43 | 4.49 | — | 1.7x | 325.48 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-09-02 (65d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ERAS | NASDAQ | 13.27 | -11.00 | 4.47 | — | 1.3x | 14.91 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-11 (87d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RGTI | NASDAQ | 9.85 | -12.13 | 4.26 | — | 1.0x | 11.21 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-06 (92d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMPX | NYSE | 7.52 | -11.22 | 4.24 | — | 0.9x | 8.47 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-04 (94d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CGNX | NASDAQ | 47.495 | -10.49 | 4.22 | — | 1.3x | 53.06 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-11-04 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GRAL | NASDAQ | 119.13 | -17.08 | 4.09 | — | 0.8x | 143.66 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-11-04 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| VOYG | NYSE | 20.33 | -11.92 | 4.08 | — | 1.0x | 23.08 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-11-02 (4d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PANW | NASDAQ | 314.67 | -9.59 | 4.07 | — | 1.2x | 348.04 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-09-01 (66d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LGN | NASDAQ | 25.41 | -20.92 | 4.05 | — | 0.7x | 32.13 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-13 (85d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NVDA | NASDAQ | 181.6 | -9.26 | 4.04 | — | 1.8x | 200.13 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-26 (72d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TXG | NASDAQ | 58.06 | -14.01 | -3.98 | — | 0.7x | 67.52 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-06 (92d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| QBTS | NASDAQ | 9.05 | -12.81 | 3.98 | — | 0.9x | 10.38 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-06 (92d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ETN | NYSE | 327.02 | -7.38 | 3.97 | — | 1.2x | 353.08 | yahoo_chart_daily | 2026-11-04 | US-listed (ADR) | 2026-11-03 (3d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ON | NASDAQ | 63.01 | -11.55 | 3.95 | — | 1.3x | 71.24 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-11-02 (4d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| QUBT | NASDAQ | 5.63 | -12.44 | 3.91 | — | 1.0x | 6.43 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-10 (88d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| APH | NYSE | 71.64 | -9.33 | 3.78 | — | 1.3x | 79.01 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-28 (9d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PRIM | NYSE | 59.56 | -12.99 | 3.74 | — | 0.8x | 68.45 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-11-03 (3d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RDW | NYSE | 6.19 | -19.82 | 3.71 | — | 0.8x | 7.72 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-11-04 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GENI | NYSE | 5.92 | -15.55 | -3.70 | — | 1.0x | 7.01 | yahoo_chart_daily | 2026-11-04 | US-listed (ADR) | 2026-08-06 (92d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LIFE | NASDAQ | 32.62 | -12.15 | 3.67 | — | 1.1x | 37.13 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-11-02 (4d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CAI | NASDAQ | 26.03 | -21.64 | 3.65 | — | 1.0x | 33.22 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-11-04 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| VISN | NASDAQ | 5.405 | -16.07 | 3.61 | — | 1.6x | 6.44 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-11-05 (1d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| VYX | NYSE | 9.86 | 4.56 | -3.45 | — | 0.9x | 9.43 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-05 (93d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ADP | NASDAQ | 307.14 | 1.19 | -3.35 | — | 2.0x | 303.54 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-28 (9d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SPOT | NYSE | 614.41 | -2.11 | -3.34 | — | 1.4x | 627.66 | yahoo_chart_daily | 2026-11-04 | US-listed (ADR) | 2026-10-22 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TXN | NASDAQ | 278.15 | -10.70 | 3.32 | — | 1.5x | 311.49 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-21 (16d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SMMT | NASDAQ | 14.19 | -12.24 | 3.24 | — | 0.7x | 16.17 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-11-04 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ABSI | NASDAQ | 9.39 | -10.40 | 3.19 | — | 0.5x | 10.48 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-11 (87d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| VERX | NASDAQ | 17.59 | 10.49 | -3.18 | — | 1.1x | 15.92 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-11-04 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| DGII | NASDAQ | 62.34 | -14.11 | 3.14 | — | 1.1x | 72.58 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-05 (93d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PI | NASDAQ | 161.06 | -10.67 | 3.07 | — | 1.0x | 180.30 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-28 (9d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GOOGN | NASDAQ | 41.62 | -1.28 | 3.05 | — | 2.1x | 42.16 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-28 (9d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ADI | NASDAQ | 361.01 | -11.13 | 3.04 | — | 1.2x | 406.24 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-19 (79d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| POWI | NASDAQ | 38.84 | -17.01 | 3.04 | — | 0.9x | 46.80 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-11-04 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RVMD | NASDAQ | 177.65 | -11.04 | 3.01 | — | 1.0x | 199.70 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-11-04 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AZN | NYSE | 186.85 | -1.14 | -2.99 | — | 1.7x | 189.01 | yahoo_chart_daily | 2026-11-04 | US-listed (ADR) | 2026-10-30 (7d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| OKTA | NASDAQ | 171.16 | -10.41 | 2.99 | — | 0.7x | 191.05 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-26 (72d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CEG | NASDAQ | 239.65 | -2.47 | 2.95 | — | 1.2x | 245.72 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-06 (92d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CMCSA | NASDAQ | 24.95 | 0.40 | -2.93 | — | 1.6x | 24.85 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-22 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SLS | NASDAQ | 7.88 | -13.79 | 2.92 | — | 0.5x | 9.14 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-11 (87d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SEZL | NASDAQ | 155 | 13.40 | -2.91 | — | 0.7x | 136.69 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-11-04 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ORCL | NYSE | 115.16 | -6.93 | 2.90 | — | 0.7x | 123.73 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-09-10 (57d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ARDT | NYSE | 15.9 | 22.40 | -2.89 | — | 0.8x | 12.99 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-11-04 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GEV | NYSE | 770.51 | -7.48 | 2.86 | — | 0.8x | 832.83 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-28 (9d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ADBE | NASDAQ | 246.44 | -0.82 | -2.80 | — | 1.4x | 248.48 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-09-10 (57d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RYN | NYSE | 21.91 | 8.63 | -2.78 | — | 1.4x | 20.17 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-11-04 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| QCOM | NASDAQ | 156.75 | -9.49 | 2.77 | — | 1.0x | 173.19 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-11-04 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BAM | NYSE | 52.46 | -3.05 | 2.74 | — | 1.4x | 54.11 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-11-06 (0d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CRCT | NASDAQ | 9.25 | 4.17 | -2.70 | — | 0.6x | 8.88 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-11-03 (3d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| DASH | NASDAQ | 179.92 | -9.40 | -2.69 | — | 0.8x | 198.59 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-29 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MDLZ | NASDAQ | 66.82 | -0.83 | -2.68 | — | 1.5x | 67.38 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-29 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FTNT | NASDAQ | 122.51 | -5.32 | 2.64 | — | 0.7x | 129.39 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-28 (9d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| UPBD | NASDAQ | 24.88 | 3.07 | 2.57 | — | 0.7x | 24.14 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-29 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ACN | NYSE | 265.16 | 0.34 | -2.56 | — | 1.0x | 264.27 | yahoo_chart_daily | 2026-11-04 | US-listed (ADR) | 2026-10-01 (36d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NWS | NASDAQ | 28.97 | -13.24 | 2.52 | — | 1.3x | 33.39 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-11-04 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TGLS | NYSE | 45.13 | 5.42 | -2.50 | — | 1.1x | 42.81 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-11-05 (1d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| IBKR | NASDAQ | 72.73 | -6.61 | 2.50 | — | 1.0x | 77.88 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-15 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PEP | NASDAQ | 142.71 | 0.20 | -2.46 | — | 1.7x | 142.42 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-08 (29d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BMY | NYSE | 63.13 | -1.65 | -2.44 | — | 1.2x | 64.19 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-29 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CRM | NYSE | 222.41 | -2.07 | -2.43 | — | 1.4x | 227.11 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-26 (72d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SYK | NYSE | 335.08 | -1.35 | -2.43 | — | 1.0x | 339.65 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-29 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CAT | NYSE | 553.64 | -6.37 | 2.42 | — | 0.9x | 591.30 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-29 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ROK | NYSE | 381.05 | -14.15 | 2.41 | — | 1.2x | 443.88 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-11-05 (1d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| HD | NYSE | 349.94 | -1.55 | -2.41 | — | 1.4x | 355.44 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-18 (80d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NFLX | NASDAQ | 65.56 | -1.25 | -2.41 | — | 1.4x | 66.39 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-20 (17d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MO | NYSE | 77.58 | -0.55 | -2.40 | — | 1.8x | 78.01 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-29 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PFE | NYSE | 29.88 | -2.96 | -2.39 | — | 1.8x | 30.79 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-11-03 (3d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MOS | NYSE | 22.33 | 3.28 | -2.37 | — | 0.8x | 21.62 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-11-03 (3d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LYNX | NYSE | 11.34 | 20.77 | 2.37 | — | 0.5x | 9.39 | yahoo_chart_daily | 2026-11-04 | US-listed | — | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| WS | NYSE | 35.9 | -11.31 | -2.37 | — | 0.9x | 40.48 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-06 (31d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| WMT | NASDAQ | 127.72 | -1.12 | -2.36 | — | 1.6x | 129.17 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-20 (78d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| JCI | NYSE | 131.46 | -6.45 | 2.31 | — | 0.9x | 140.53 | yahoo_chart_daily | 2026-11-04 | US-listed (ADR) | 2026-10-27 (10d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MRNA | NASDAQ | 241.46 | -6.55 | 2.29 | — | 0.5x | 258.38 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-11-06 (0d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SHW | NYSE | 349.01 | -3.99 | -2.24 | — | 1.0x | 363.50 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-27 (10d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RACE | NYSE | 422.4 | -2.32 | -2.21 | — | 1.7x | 432.45 | yahoo_chart_daily | 2026-11-04 | US-listed (ADR) | 2026-11-03 (3d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CL | NYSE | 98.69 | -0.07 | -2.20 | — | 1.3x | 98.76 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-30 (7d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| USB | NYSE | 59.75 | -2.10 | 2.18 | — | 1.7x | 61.03 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-15 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| V | NYSE | 422.59 | -3.20 | -2.17 | — | 1.5x | 436.57 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-27 (10d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PRDO | NASDAQ | 26.55 | -11.47 | 2.15 | — | 1.2x | 29.99 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-06 (92d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| KKR | NYSE | 98.3 | -3.00 | -2.14 | — | 1.0x | 101.34 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-07-30 (99d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| IBRX | NASDAQ | 8.01 | -10.30 | 2.12 | — | 0.5x | 8.93 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-04 (94d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MA | NYSE | 655.92 | -2.49 | -2.12 | — | 1.5x | 672.68 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-29 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RELY | NASDAQ | 21.545 | -20.44 | 2.11 | — | 0.7x | 27.08 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-11-04 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LIN | NASDAQ | 521.23 | -0.67 | -2.10 | — | 2.4x | 524.74 | yahoo_chart_daily | 2026-11-04 | US-listed (ADR) | 2026-10-29 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PM | NYSE | 201.5 | -4.63 | -2.08 | — | 1.4x | 211.28 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-10-21 (16d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| INTU | NASDAQ | 354.84 | -0.50 | -2.07 | — | 0.9x | 356.64 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-08-25 (73d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MCD | NYSE | 278.04 | -0.78 | -2.06 | — | 1.5x | 280.22 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-11-04 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SEDG | NASDAQ | 26.2 | -12.72 | 2.06 | — | 0.5x | 30.02 | yahoo_chart_daily | 2026-11-04 | US-listed (ADR) | 2026-11-04 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TTAM | NYSE | 11.68 | -18.32 | 2.05 | — | 0.8x | 14.30 | yahoo_chart_daily | 2026-11-04 | US-listed (ADR) | 2026-11-04 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMGN | NASDAQ | 460.28 | -3.80 | -2.04 | — | 1.3x | 478.48 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-11-03 (3d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AGI | NYSE | 31.08 | 3.60 | -2.03 | — | 0.7x | 30.00 | yahoo_chart_daily | 2026-11-04 | US-listed (ADR) | 2026-10-28 (9d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PLTR | NASDAQ | 154.99 | -9.73 | 2.01 | — | 0.8x | 171.70 | yahoo_chart_daily | 2026-11-04 | US-listed | 2026-11-02 (4d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |

## US — QUIET one-liners

| Ticker | Venue | Chg % | Pre-mkt % | Post-mkt % | Move vs avg daily | Ref close | Ref source | Ref asof | US tradeable | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|
| TMUS | NASDAQ | 0.89 | -1.99 | — | 0.4x | 159.17 | yahoo_chart_daily | 2026-11-04 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| TWST | NASDAQ | -15.41 | 1.98 | — | 2.5x | 142.58 | yahoo_chart_daily | 2026-11-04 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| BFLY | NYSE | -10.34 | 1.98 | — | 2.0x | 6.77 | yahoo_chart_daily | 2026-11-04 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| MDT | NYSE | -0.11 | -1.96 | — | 0.1x | 104.96 | yahoo_chart_daily | 2026-11-04 | US-listed (ADR) | — | no catalyst lookup (outside the per-run budget) |
| BKNG | NASDAQ | -1.32 | -1.91 | — | 0.6x | 170.97 | yahoo_chart_daily | 2026-11-04 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| ASST | NASDAQ | -10.17 | 1.89 | — | 1.7x | 22.92 | yahoo_chart_daily | 2026-11-04 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| DIS | NYSE | -1.45 | -1.89 | — | 1.3x | 118.95 | yahoo_chart_daily | 2026-11-04 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| COKE | NASDAQ | 4.07 | -1.87 | — | 2.2x | 204.18 | yahoo_chart_daily | 2026-11-04 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| RAL | NYSE | -12.22 | 1.86 | — | 4.3x | 71.58 | yahoo_chart_daily | 2026-11-04 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| PG | NYSE | -0.13 | -1.86 | — | 0.1x | 167.32 | yahoo_chart_daily | 2026-11-04 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| TRV | NYSE | -1.55 | -1.86 | — | 1.3x | 409.25 | yahoo_chart_daily | 2026-11-04 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| COST | NASDAQ | 1.83 | -1.82 | — | 1.4x | 1046.47 | yahoo_chart_daily | 2026-11-04 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| ISRG | NASDAQ | -2.82 | -1.82 | — | 1.5x | 482.10 | yahoo_chart_daily | 2026-11-04 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| ABBV | NYSE | -2.24 | -1.82 | — | 1.7x | 294.83 | yahoo_chart_daily | 2026-11-04 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| STRA | NASDAQ | -21.33 | -1.81 | — | 8.9x | 74.32 | yahoo_chart_daily | 2026-11-04 | US-listed | — | no catalyst lookup (outside the per-run budget) |

## EU/UK — Headline table

| Ticker | Market | Venue | Close | Chg % | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TEP | france | EURONEXT | 66.38 | -17.85 | EUR | 10.8x | 80.80 | yahoo_chart_daily | 2026-11-05 | none | 2026-07-30 | Y | Teleperformance Q3 2026 results (Q3 earnings call on the tape) - shares sold off hard on the print, -16.7% by 12:59 CET; no headline detail captured in the lookup budget |
| BTS_B | sweden | OMXSTO | 267 | +16.09 | SEK | 17.1x | 230.00 | yahoo_chart_daily | 2026-11-05 | none | 2026-08-14 | Y | Interim report Jan-Sep 2026 (6 Nov 06:30 CET): strongest Q3 in company history; net sales MSEK 716, +13% organic; EBITA +79% to MSEK 81; EPS SEK 2.12; FY26 EBITA guided significantly better than 2025 |
| MOVE | switzerland | SIX | 107.8 | -12.50 | CHF | 12.0x | 123.20 | yahoo_chart_daily | 2026-11-05 | none | 2026-09-09 | Y | FY2026 guidance cut (5 Nov 17:45 CET): revenue growth now ~9% in constant currency (from 10-14%) and adj. EBITDA margin in line with 2025 (from ~+50bps) on softer US healthcare; 2024-27 mid-term outlook reiterated |
| ATT | sweden | OMXSTO | 126 | +12.20 | SEK | 10.6x | 112.30 | yahoo_chart_daily | 2026-11-05 | none | 2026-08-20 | — | no catalyst lookup (outside the per-run budget) |
| HEX | norway | OSL | 11.61 | +9.84 | NOK | 6.5x | 10.57 | yahoo_chart_daily | 2026-11-05 | none | 2026-08-06 | — | no catalyst lookup (outside the per-run budget) |
| MDV | poland | GPW | 105.2 | +8.23 | PLN | 3.7x | 97.20 | yahoo_chart_daily | 2026-11-05 | none | 2026-08-07 | — | no catalyst lookup (outside the per-run budget) |
| INISS_B | sweden | OMXSTO | 75.6 | +8.00 | SEK | 4.4x | 70.00 | yahoo_chart_daily | 2026-11-05 | none | 2026-11-05 | — | no catalyst lookup (outside the per-run budget) |
| GL9 | ireland | EURONEXT | 19.57 | -7.78 | EUR | 3.7x | 21.22 | yahoo_chart_daily | 2026-11-05 | none | 2026-08-06 | — | no catalyst lookup (outside the per-run budget) |
| MTG_B | sweden | OMXSTO | 102.2 | -7.09 | SEK | 3.7x | 110.00 | yahoo_chart_daily | 2026-11-05 | none | 2026-07-21 | — | no catalyst lookup (outside the per-run budget) |
| HAYPP | sweden | OMXSTO | 149.8 | -7.07 | SEK | 3.9x | 161.20 | yahoo_chart_daily | 2026-11-05 | none | 2026-08-12 | — | no catalyst lookup (outside the per-run budget) |
| SEA1 | norway | OSL | 24.45 | -7.03 | NOK | 4.4x | 26.30 | yahoo_chart_daily | 2026-11-05 | none | 2026-08-14 | — | no catalyst lookup (outside the per-run budget) |
| TBCG | uk | LSE | 5100 | +6.87 | GBX | 3.4x | 4772.00 | yahoo_chart_daily | 2026-11-05 | none | 2026-08-06 | — | no catalyst lookup (outside the per-run budget) |
| SIVE | sweden | OMXSTO | 16.11 | +6.69 | SEK | 1.3x | 15.10 | yahoo_chart_daily | 2026-11-05 | none | 2026-08-27 | — | no catalyst lookup (outside the per-run budget) |
| PKN | poland | GPW | 131.48 | -6.57 | PLN | 4.5x | 140.72 | yahoo_chart_daily | 2026-11-05 | none | 2026-08-05 | — | no catalyst lookup (outside the per-run budget) |
| HAG | germany | XETR | 77.32 | -6.37 | EUR | 3.3x | 82.58 | yahoo_chart_daily | 2026-11-05 | none | 2026-07-30 | — | no catalyst lookup (outside the per-run budget) |
| OVH | france | EURONEXT | 14.07 | +6.35 | EUR | 1.4x | 13.23 | yahoo_chart_daily | 2026-11-05 | ADR (OTC:OVHFF) | 2026-10-20 | — | no catalyst lookup (outside the per-run budget) |
| EMG | uk | LSE | 301.2 | -6.34 | GBX | 3.8x | 321.60 | yahoo_chart_daily | 2026-11-05 | none | 2026-07-28 | — | no catalyst lookup (outside the per-run budget) |
| PLT | norway | OSL | 12.2 | -6.30 | NOK | 2.0x | 13.02 | yahoo_chart_daily | 2026-11-05 | none | 2026-08-06 | — | no catalyst lookup (outside the per-run budget) |
| DOM | sweden | OMXSTO | 23.2 | -6.00 | SEK | 1.9x | 24.68 | yahoo_chart_daily | 2026-11-05 | none | 2026-10-22 | — | no catalyst lookup (outside the per-run budget) |
| AF | france | EURONEXT | 13.375 | +5.86 | EUR | 2.6x | 12.63 | yahoo_chart_daily | 2026-11-05 | none | 2026-07-30 | — | no catalyst lookup (outside the per-run budget) |
| SOFF | norway | OSL | 68.4 | -5.79 | NOK | 4.3x | 72.60 | yahoo_chart_daily | 2026-11-05 | none | 2026-11-04 | — | no catalyst lookup (outside the per-run budget) |
| ACT0 | germany | XETR | 139 | -5.57 | EUR | 2.4x | 147.20 | yahoo_chart_daily | 2026-11-05 | none | 2026-10-29 | — | no catalyst lookup (outside the per-run budget) |
| DNO | norway | OSL | 20.08 | -5.55 | NOK | 2.6x | 21.26 | yahoo_chart_daily | 2026-11-05 | ADR (OTC:DTNOF) | 2026-10-29 | — | no catalyst lookup (outside the per-run budget) |
| AMS2 | austria | VIE | 16.35 | +5.14 | EUR | 1.4x | 15.55 | yahoo_chart_daily | 2026-11-05 | none | 2026-08-04 | — | no catalyst lookup (outside the per-run budget) |
| AIXA | germany | SWB | 30.35 | +5.09 | EUR | 1.1x | 28.93 | yahoo_chart_daily | 2026-11-05 | none | 2026-10-29 | — | no catalyst lookup (outside the per-run budget) |
| CAMBI | norway | OSL | 22.6 | -5.04 | NOK | 3.3x | 23.80 | yahoo_chart_daily | 2026-11-05 | none | 2026-11-03 | — | no catalyst lookup (outside the per-run budget) |
| DIG | poland | GPW | 294 | +5.00 | PLN | 1.5x | 280.00 | yahoo_chart_daily | 2026-11-05 | none | 2026-09-07 | — | no catalyst lookup (outside the per-run budget) |
| AKAST | norway | OSL | 10.78 | -4.94 | NOK | 2.7x | 11.34 | yahoo_chart_daily | 2026-11-05 | none | 2026-08-21 | — | no catalyst lookup (outside the per-run budget) |
| YUBICO | sweden | OMXSTO | 162.2 | -4.92 | SEK | 1.0x | 170.60 | yahoo_chart_daily | 2026-11-05 | ADR (OTC:YUBCF) | 2026-08-06 | — | no catalyst lookup (outside the per-run budget) |

## AU (ASX) — Headline table

| Ticker | Venue | Close | Chg % | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DVP | ASX | 3.55 | -10.13 | AUD | 2.6x | 3.95 | yahoo_chart_daily | 2026-11-04 | none | 2026-03-08 | N | no fresh catalyst found - no 6 Nov company announcement (latest: revised securities trading policy, 2 Nov); copper-zinc miner's drop looks sector/commodity-driven, not earnings |
| WA1 | ASX | 7.96 | -9.85 | AUD | 1.9x | 8.83 | yahoo_chart_daily | 2026-11-04 | none | 2026-09-18 | N | Substantial holder notice lodged 7:51pm Thursday - no company announcement; copper/uranium name |
| VUL | ASX | 1.115 | -9.72 | AUD | 1.7x | 1.24 | yahoo_chart_daily | 2026-11-04 | none | 2026-09-08 | — | no catalyst lookup (outside the per-run budget) |
| WBT | ASX | 2.14 | -8.55 | AUD | 1.7x | 2.34 | yahoo_chart_daily | 2026-11-04 | none | 2026-08-28 | — | no catalyst lookup (outside the per-run budget) |
| SRL | ASX | 11.58 | -8.24 | AUD | 1.5x | 12.62 | yahoo_chart_daily | 2026-11-04 | none | 2026-09-07 | — | no catalyst lookup (outside the per-run budget) |
| MLX | ASX | 1.52 | -8.16 | AUD | 1.7x | 1.66 | yahoo_chart_daily | 2026-11-04 | none | 2026-08-27 | — | no catalyst lookup (outside the per-run budget) |
| FFM | ASX | 1.32 | -8.01 | AUD | 2.0x | 1.44 | yahoo_chart_daily | 2026-11-04 | none | 2026-09-17 | — | no catalyst lookup (outside the per-run budget) |
| SGM | ASX | 19.65 | -7.22 | AUD | 2.9x | 21.18 | yahoo_chart_daily | 2026-11-04 | none | 2026-08-17 | — | no catalyst lookup (outside the per-run budget) |
| SLX | ASX | 2.97 | -7.19 | AUD | 1.5x | 3.20 | yahoo_chart_daily | 2026-11-04 | none | 2026-08-27 | — | no catalyst lookup (outside the per-run budget) |
| GNG | ASX | 6.75 | -7.02 | AUD | 2.1x | 7.26 | yahoo_chart_daily | 2026-11-04 | none | 2026-08-23 | — | no catalyst lookup (outside the per-run budget) |
| IMD | ASX | 3.2 | -6.98 | AUD | 2.8x | 3.44 | yahoo_chart_daily | 2026-11-04 | none | 2026-08-16 | — | no catalyst lookup (outside the per-run budget) |
| SXE | ASX | 3.53 | -6.86 | AUD | 1.7x | 3.79 | yahoo_chart_daily | 2026-11-04 | none | 2026-08-17 | — | no catalyst lookup (outside the per-run budget) |
| DUR | ASX | 1.885 | -6.68 | AUD | 2.2x | 2.02 | yahoo_chart_daily | 2026-11-04 | none | 2026-08-25 | — | no catalyst lookup (outside the per-run budget) |
| CU6 | ASX | 1.495 | -6.56 | AUD | 1.4x | 1.60 | yahoo_chart_daily | 2026-11-04 | none | 2026-08-26 | — | no catalyst lookup (outside the per-run budget) |
| MSB | ASX | 2.03 | -6.45 | AUD | 1.5x | 2.17 | yahoo_chart_daily | 2026-11-04 | none | 2026-08-26 | — | no catalyst lookup (outside the per-run budget) |
| ELV | ASX | 3.34 | -6.44 | AUD | 1.3x | 3.57 | yahoo_chart_daily | 2026-11-04 | none | 2026-08-27 | — | no catalyst lookup (outside the per-run budget) |
| PNR | ASX | 3.06 | -6.42 | AUD | 1.5x | 3.27 | yahoo_chart_daily | 2026-11-04 | none | 2026-09-28 | — | no catalyst lookup (outside the per-run budget) |
| SKS | ASX | 5.25 | -6.25 | AUD | 1.2x | 5.60 | yahoo_chart_daily | 2026-11-04 | none | 2026-08-17 | — | no catalyst lookup (outside the per-run budget) |
| C79 | ASX | 6.19 | -5.93 | AUD | 1.9x | 6.58 | yahoo_chart_daily | 2026-11-04 | none | 2026-08-09 | — | no catalyst lookup (outside the per-run budget) |
| IGO | ASX | 4.96 | -5.88 | AUD | 1.8x | 5.27 | yahoo_chart_daily | 2026-11-04 | ADR (OTC:IIDDY) | 2026-08-25 | — | no catalyst lookup (outside the per-run budget) |
| SFR | ASX | 19.11 | -5.82 | AUD | 1.9x | 20.29 | yahoo_chart_daily | 2026-11-04 | none | 2026-08-25 | — | no catalyst lookup (outside the per-run budget) |
| ZIP | ASX | 2.02 | -5.61 | AUD | 0.9x | 2.14 | yahoo_chart_daily | 2026-11-04 | ADR (OTC:ZIZTF) | 2026-08-19 | — | no catalyst lookup (outside the per-run budget) |
| NXT | ASX | 10.4 | +5.58 | AUD | 0.7x | 9.85 | yahoo_chart_daily | 2026-11-04 | none | 2026-08-27 | — | no catalyst lookup (outside the per-run budget) |
| SDR | ASX | 3.41 | -5.54 | AUD | 1.6x | 3.61 | yahoo_chart_daily | 2026-11-04 | none | 2026-08-24 | — | no catalyst lookup (outside the per-run budget) |
| 4DX | ASX | 2.28 | -5.39 | AUD | 0.9x | 2.41 | yahoo_chart_daily | 2026-11-04 | none | 2026-08-27 | — | no catalyst lookup (outside the per-run budget) |

## Source health

- scanner_calls: 41 | scanner_errors: 0
- pipeline_version: 2026-11-06.2 | self-healed at start of run from 2026-11-06.1 to 2026-11-06.2 via connector (the cron's fetch served a stale copy)
- et_clock: zoneinfo America/New_York (DST-aware; a fixed UTC-4 mislabels every winter fire)
- premarket_window: 04:00-09:30 ET, resolved with zoneinfo (09:00-14:30 UTC in winter, 08:00-13:30 UTC in summer)
- session_selection: by DATE and order, never by a modal time-of-day. Yahoo stamps a daily bar at the session open, so the ET stamp of the SAME session shifts by one hour across a DST boundary; a modal filter kept the OLDER bars and discarded the NEWEST ones, which rolled the base back to the prior-prior session (66 US + 21 ASX rows lost on 2026-11-03, 24 of 25 ASX rows lost on 2026-11-04).
- yahoo_calls: 279 | yahoo_429: 0 | yahoo_errors: 2
- reference_close (screener vs Yahoo, resolved BEFORE the tables were built): agree=267 mismatch=0 unverified=2 stale_reference=0
  method: the screener's implied reference close (close / (1 + change/100)) is compared
  with Yahoo's own reference close. A match proves the move was measured against the
  TRUE prior close; a mismatch means the row sits on a STALE reference (phantom move).
  Coverage: every row of the US headline, US QUIET, EU/UK and ASX tables is checked.
  Yahoo bar mode: {"closed": 238, "live": 29} (closed = last completed session bar;
  live = in-progress EU/UK session bar, which is what a weekday 08:00 ET EU move needs)
  live drift between the screener snapshot and the later Yahoo print: median=0.00pp max=0.63pp (expected on a live market)
- rows_dropped_stale_ref: 0 (rows whose screener-implied reference close disagreed with Yahoo's by more than 0.5%; they are dropped, not published)
- rows_dropped_unresolved_ref: 2 (rows whose reference close could not be resolved from Yahoo at all - the base of the move is unverifiable, so the row is dropped rather than published with a '—' base)
- us_premarket_check (Yahoo 1-min pre/post feed vs the screener pre-market column, base = the IMMEDIATELY prior session's close): checked=10 within_1pp=9 within_3pp=10 unavailable=0
- markets_with_lt5_rows: ['uk:egreater=2', 'france:egreater=4', 'netherlands:egreater=3', 'belgium:egreater=1', 'portugal:egreater=0', 'portugal:less=2', 'ireland:egreater=1', 'ireland:less=2', 'italy:egreater=2', 'switzerland:egreater=0', 'spain:egreater=2', 'spain:less=4', 'denmark:egreater=3', 'finland:egreater=1', 'poland:egreater=3', 'austria:egreater=1', 'austria:less=4', 'greece:egreater=0', 'greece:less=3']
  NOTE: this fires per market AND direction, so it is NOT a coverage-failure signal on
  its own. A 'less' count of 0-3 means almost nothing fell more than 2.5% that session
  (a broad up-day); a small 'egreater' count usually means a small market with few
  names above the $1B market-cap floor. Check the median change before calling it a gap.
- filters: volume>10000 (removes stale-reference rows), country=home for EU/UK/AU,
  exchange drop-list for US, US venue allow-list, US preferred (slash ticker) excluded
- volume_floor_note: volume>10000 removes MOST stale-reference rows, but a row can
  still sit on a stale reference when its only volume came from one thin day (verified
  2026-10-26: LSE 50GP cleared the floor on 12,000 shares dated 2026-10-15 while Yahoo
  showed no bar for the scan date). The reference-close cross-check is what catches
  those; rows that fail it are dropped from the tables, not published.
- us_preferred_dropped: 59
- bod_no_extended_hours: 72 (deferred to the next scan; not in the headline table)
- earnings_source: screener `earnings_release_date` (last FULL report) + `earnings_release_next_date` (next scheduled)
- earnings_caveat: `earnings_release_date` does NOT capture preliminary, guidance or
  restructuring releases. On 2026-10-23 LKQ fell 22.47% on a preliminary Q3 miss while
  the field still read 2026-07-30. ALWAYS confirm the earnings-driven flag against the
  headline itself; the calendar field is a screen, not a verdict.
- us_line_index: ok (US-listed lines for the 18 foreign home countries, both scanner types; the `US tradeable` column is ADR / US-listed / none)
- catalyst_note: Catalyst lookups: 5 US + 3 EU + 2 AU = 10 per run, the skill's cap.
- catalyst_budget: 5 US + 3 EU + 2 AU = 10 lookups per run
- one_table_rule: each name appears exactly once, in exactly one table, with its
  catalyst in that row's last column. There is no separate catalysts section.
- data_date: US regular session close of the prior trading day; extended-hours columns
  carry the prior session's prints
- deprecations: mcp__tradingview-advanced__*, mcp__tradingview__*, mcp__financekit__*,
  mcp__stocktwits__* are ABSENT in Cloud sessions (tool_search 0 hits; connector catalog
  holds only media + credential tools). The public screener replaces them.

- degraded_sources: 1
  (the chat reply's `errors:` MUST equal this number - one entry per degraded
  source, not one per run)
  1. yahoo_chart_api.reference_close_unresolved — BRK.A: the reference close could not be resolved (429 or a bad body)

## Audit line

`earnings-reaction target=earnings-reactions:2026-11-06 candidates=451 amc_reactions=0 pre_gaps=198 eu_reactions=29 asx_reactions=25 catalyst_lookups=10 bod=72 rows_dropped_stale_ref=0 rows_dropped_unresolved_ref=2 degraded_sources=1`
