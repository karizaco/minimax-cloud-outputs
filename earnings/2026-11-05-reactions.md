# Earnings reaction scanner — 2026-11-05

- Cron: `0 8 * * 1-5` America/New_York (weekdays, 08:00 ET)
- Fire time (ET): 2026-11-05 08:22:31 Thu
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

- 0 AMC reactions, 164 pre-market gaps, 88 without extended-hours data; 30 EU/UK and 15 ASX movers.
- Biggest US extended-hours move: SEZL PRE_GAP (29.49%).
- Biggest EU/UK move: YUBICO (+31.21%, sweden).
- Biggest ASX move: CYL (+18.34%).
- EU/AU earnings-driven tagging is keyword-based on headlines (best-effort).

## Actionable read

- **Move vs this name's own history.** The `Move vs avg daily` column divides the
  reaction by the name's own mean absolute daily move over its last
  20 completed sessions. A -27% move in a name that averages +-3% is a
  different event from a -8% move in a name that averages +-7%.
- **US-listed and tradeable vs foreign-only.** 179 published US rows are on a
  US venue; 7 more foreign reactions have a US ADR line
  (the `US tradeable` column carries the ticker); 38 are foreign-only and
  cannot be bought directly by a US reader.
- **Not yet fully priced — US (hypothesis, not a recommendation).**
  TRIP — -20.69%, 2.08% mean absolute daily move over the last 20 completed sessions, 10.0x that average, reference close 9.44 dated 2026-11-03, US access: US-listed, the move now (-20.69%) is larger than the move it follows (+8.05%); the reaction is still being repriced. Hypothesis only: this artifact states no
  direction and no trade.
- **Not yet fully priced — EU/UK (hypothesis, not a recommendation).**
  CAMX — +9.77%, 0.83% mean absolute daily move over the last 20 completed sessions, 11.7x that average, reference close 665.00 dated 2026-11-04, US access: none, the move now (+9.77%) is larger than the move it follows (-1.84%); the reaction is still being repriced. Hypothesis only: this artifact states no
  direction and no trade.
- **Not yet fully priced — AU (ASX) (hypothesis, not a recommendation).**
  NEU — +17.49%, 2.81% mean absolute daily move over the last 20 completed sessions, 6.2x that average, reference close 19.78 dated 2026-11-03, US access: none, the move now (+17.49%) is larger than the move it follows (-4.26%); the reaction is still being repriced. Hypothesis only: this artifact states no
  direction and no trade.

## US — Headline table

| Ticker | Venue | Close | Chg % | Pre-mkt % | Post-mkt % | Move vs avg daily | Ref close | Ref source | Ref asof | US tradeable | Last earnings | Tag | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SEZL | NASDAQ | 136.69 | 11.65 | 29.49 | — | 7.7x | 122.43 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-11-04 (1d ago) | PRE_GAP | Y | Q3 2026 beat, reported Nov 4 after the close: adj EPS $1.37 vs $1.29 est, revenue $166.5M vs $154.9M est, FY26 revenue-growth guide ~42.5% and FY27 adj EPS guide $7.20 vs $6.65 est |
| APP | NASDAQ | 271.75 | 10.69 | 21.47 | — | 7.0x | 245.51 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-11-04 (1d ago) | PRE_GAP | Y | Record Q3 2026, reported Nov 4 after the close: EPS $4.30 vs $4.03 est, revenue $2.18B up 55% y/y, adj EBITDA $1.84B, Q4 revenue guide $2.365-2.395B, buyback authorisation raised to $3.6B |
| LYNX | NYSE | 9.39 | -19.81 | 20.98 | — | 5.2x | 11.71 | yahoo_chart_daily | 2026-11-03 | US-listed | — | PRE_GAP | Y | Q3 FY2026 results, Nov 4 at 4:15 p.m. ET: EPS $0.15 vs $0.08 est, revenue $194.4M up 90.4% y/y, backlog more than doubled; Baird upgraded to Outperform with an $18 target on Nov 5 |
| TRIP | NASDAQ | 10.2 | 8.05 | -20.69 | — | 10.0x | 9.44 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-11-05 (0d ago) | PRE_GAP | Y | Q3 2026 results posted pre-open on Nov 5 at 7:05 a.m. ET with the call at 8:30 a.m. ET; the screener earnings field still read 2026-08-06, so the headline carries the flag |
| FOUR | NYSE | 44.82 | 8.03 | -15.19 | — | 6.1x | 41.49 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-08-06 (91d ago) | PRE_GAP | Y | Shift4 Q3 2026 results released before the open on Nov 5; the screener earnings field still read 2026-08-06, so the headline carries the flag |
| ALNT | NASDAQ | 79.56 | -9.61 | 13.35 | — | 3.4x | 88.02 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-11-04 (1d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ZG | NASDAQ | 34.45 | 9.89 | -11.95 | — | 3.6x | 31.35 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-11-04 (1d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LMAT | NASDAQ | 87.92 | 9.08 | -10.41 | — | 5.3x | 80.60 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-11-04 (1d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| QCOM | NASDAQ | 173.19 | 5.33 | -10.39 | — | 4.3x | 164.43 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-11-04 (1d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MELI | NASDAQ | 1739.88 | 4.68 | -8.67 | — | 4.9x | 1662.16 | yahoo_chart_daily | 2026-11-03 | US-listed (ADR) | 2026-11-04 (1d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| Z | NASDAQ | 33.9 | 9.43 | -8.55 | — | 2.5x | 30.98 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-11-04 (1d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ENOV | NYSE | 24.42 | 16.90 | 8.52 | — | 2.3x | 20.89 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-08-06 (91d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PH | NYSE | 910.19 | -3.68 | 7.67 | — | 4.3x | 944.99 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-08-06 (91d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| VCEL | NASDAQ | 45.48 | 10.68 | 7.50 | — | 3.2x | 41.09 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-07-30 (98d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ARHS | NASDAQ | 13.15 | 9.04 | -7.30 | — | 2.2x | 12.06 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-08-06 (91d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MXL | NASDAQ | 56.85 | -11.13 | -7.25 | — | 1.2x | 63.97 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-10-22 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| EXPE | NASDAQ | 315.88 | 10.54 | -7.25 | — | 2.4x | 285.77 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-11-04 (1d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NVAX | NASDAQ | 10.65 | 10.02 | 7.04 | — | 1.4x | 9.68 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-08-06 (91d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BUUU | NASDAQ | 6.32 | -14.36 | -7.00 | — | 1.0x | 7.38 | yahoo_chart_daily | 2026-11-03 | US-listed (ADR) | — | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RGC | NASDAQ | 5.42 | -11.87 | 6.57 | — | 0.9x | 6.15 | yahoo_chart_daily | 2026-11-03 | US-listed (ADR) | — | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SNDK | NASDAQ | 1037.4 | -7.91 | -6.32 | — | 1.3x | 1126.52 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-10-29 (7d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AEHR | NASDAQ | 60.84 | -6.56 | -6.31 | — | 0.9x | 65.11 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-07-14 (114d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LIME | NASDAQ | 18.39 | -27.83 | 6.31 | — | 1.1x | 25.48 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-11-03 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| OUST | NASDAQ | 33.54 | 15.73 | -6.05 | — | 1.1x | 28.98 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-11-03 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AXTI | NASDAQ | 47.54 | -7.38 | -5.97 | — | 0.9x | 51.33 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-10-29 (7d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SMTC | NASDAQ | 110.96 | -12.92 | -5.79 | — | 1.0x | 127.42 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-08-25 (72d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ACCV | NASDAQ | 11.7 | -17.08 | -5.73 | — | 1.0x | 14.11 | yahoo_chart_daily | 2026-11-03 | US-listed | — | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| VICR | NASDAQ | 159.07 | -11.14 | -5.70 | — | 0.9x | 179.01 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-10-20 (16d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BE | NYSE | 200.4 | -6.36 | -5.64 | — | 1.0x | 214.01 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-10-22 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FORM | NASDAQ | 85.24 | -11.93 | -5.62 | — | 0.9x | 96.79 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-10-28 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PLPC | NASDAQ | 285.2 | -8.45 | -5.58 | — | 1.4x | 311.51 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-10-28 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| EROC | NYSE | 7.94 | -11.38 | -5.52 | — | 0.9x | 8.96 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-08-11 (86d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| DELL | NYSE | 372.36 | -8.82 | -5.33 | — | 1.2x | 408.40 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-09-01 (65d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CIEN | NYSE | 272.24 | -9.28 | -5.21 | — | 0.9x | 300.08 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-09-03 (63d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ICHR | NASDAQ | 33.71 | -7.72 | -5.07 | — | 1.0x | 36.53 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-11-02 (3d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LRCX | NASDAQ | 221.43 | -4.03 | -4.90 | — | 1.4x | 230.72 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-10-21 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PENG | NASDAQ | 48.35 | -9.10 | -4.86 | — | 0.8x | 53.19 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-10-06 (30d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| UCTT | NASDAQ | 44.04 | -8.29 | -4.86 | — | 0.9x | 48.02 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-10-27 (9d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| STX | NASDAQ | 557.06 | -8.13 | -4.86 | — | 1.2x | 606.38 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-10-27 (9d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NVTS | NASDAQ | 9.33 | 9.00 | -4.82 | — | 0.9x | 8.56 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-11-03 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| STRL | NASDAQ | 283.66 | -21.46 | -4.82 | — | 1.0x | 361.15 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-10-28 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| OGC | NYSE | 25.78 | 9.19 | 4.77 | — | 1.7x | 23.61 | yahoo_chart_daily | 2026-11-03 | US-listed (ADR) | 2026-11-04 (1d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| WDC | NASDAQ | 323.83 | -6.77 | -4.77 | — | 1.1x | 347.35 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-10-22 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LITE | NASDAQ | 626.75 | -7.85 | -4.72 | — | 0.8x | 680.16 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-11-02 (3d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMAT | NASDAQ | 369.4 | -3.28 | -4.71 | — | 1.4x | 381.92 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-08-13 (84d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| IREN | NASDAQ | 21.71 | -11.24 | -4.69 | — | 0.8x | 24.46 | yahoo_chart_daily | 2026-11-03 | US-listed (ADR) | 2026-08-27 (70d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FLEX | NASDAQ | 77.24 | -12.33 | -4.62 | — | 0.9x | 88.10 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-10-28 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TTMI | NASDAQ | 73.38 | -10.11 | -4.61 | — | 0.6x | 81.63 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-10-22 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMD | NASDAQ | 488.78 | 1.01 | -4.56 | — | 1.2x | 483.90 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-11-03 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MU | NASDAQ | 795.23 | -7.00 | -4.55 | — | 1.2x | 855.10 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-09-30 (36d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FIX | NYSE | 1091.31 | -15.08 | -4.51 | — | 0.9x | 1285.13 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-10-22 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| COHU | NASDAQ | 43.98 | -12.09 | -4.50 | — | 0.9x | 50.03 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-10-28 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CRDO | NASDAQ | 136.5 | -9.55 | -4.48 | — | 0.8x | 150.91 | yahoo_chart_daily | 2026-11-03 | US-listed (ADR) | 2026-09-01 (65d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MRVL | NASDAQ | 159.8 | -7.08 | -4.41 | — | 0.9x | 171.97 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-08-27 (70d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AAOI | NASDAQ | 59.27 | -7.35 | -4.40 | — | 0.7x | 63.97 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-08-06 (91d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LGN | NASDAQ | 32.13 | -17.95 | -4.28 | — | 0.9x | 39.16 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-08-13 (84d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ALGM | NASDAQ | 31.25 | -7.16 | -4.26 | — | 1.1x | 33.66 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-10-29 (7d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| KGS | NYSE | 41.26 | -11.35 | 4.22 | — | 1.3x | 46.54 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-08-06 (91d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FPS | NYSE | 22.44 | -17.32 | -4.19 | — | 0.7x | 27.14 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-09-15 (51d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CIFR | NASDAQ | 6.5 | -19.95 | -4.14 | — | 0.6x | 8.12 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-11-02 (3d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NVT | NYSE | 112.82 | -12.72 | -4.12 | — | 1.0x | 129.26 | yahoo_chart_daily | 2026-11-03 | US-listed (ADR) | 2026-10-30 (6d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ULCC | NASDAQ | 7.09 | 9.58 | 4.09 | — | 0.7x | 6.47 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-10-28 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TPL | NYSE | 287.65 | -13.36 | 4.07 | — | 2.0x | 332.00 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-11-04 (1d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| DXPE | NASDAQ | 158.38 | -11.76 | -4.02 | — | 1.3x | 179.49 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-08-05 (92d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TER | NASDAQ | 250.99 | -6.82 | -3.98 | — | 1.0x | 269.35 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-10-27 (9d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NET | NYSE | 266.58 | -2.57 | -3.92 | — | 1.1x | 273.62 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-08-06 (91d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BELFB | NASDAQ | 217.43 | -8.82 | -3.87 | — | 1.2x | 238.45 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-10-28 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NBIS | NASDAQ | 141.52 | -6.67 | -3.87 | — | 0.7x | 151.64 | yahoo_chart_daily | 2026-11-03 | US-listed (ADR) | 2026-08-12 (85d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| KLAC | NASDAQ | 149.79 | -4.10 | -3.84 | — | 1.2x | 156.20 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-10-28 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| VRT | NYSE | 205.55 | -12.89 | -3.81 | — | 0.9x | 235.97 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-10-28 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CRWV | NASDAQ | 48.42 | -9.90 | -3.80 | — | 0.6x | 53.74 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-08-11 (86d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| APLD | NASDAQ | 16.61 | -6.74 | -3.78 | — | 0.6x | 17.81 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-10-07 (29d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMBQ | NYSE | 41.54 | -7.03 | -3.71 | — | 1.0x | 44.68 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-08-11 (86d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GEV | NYSE | 832.83 | -9.30 | -3.64 | — | 1.1x | 918.20 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-10-28 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ANET | NYSE | 178.48 | 5.04 | -3.63 | — | 1.0x | 169.91 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-11-03 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MOH | NYSE | 226.42 | 8.93 | 3.60 | — | 1.6x | 207.85 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-10-21 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CLS | NYSE | 236.41 | -9.05 | -3.56 | — | 0.7x | 259.94 | yahoo_chart_daily | 2026-11-03 | US-listed (ADR) | 2026-10-26 (10d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| HUT | NASDAQ | 48.94 | -23.23 | -3.56 | — | 0.5x | 63.75 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-11-04 (1d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ONTO | NYSE | 184.82 | -8.68 | -3.55 | — | 0.8x | 202.39 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-08-06 (91d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GLW | NYSE | 118.77 | -5.84 | -3.51 | — | 1.2x | 126.14 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-10-27 (9d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| DOCN | NYSE | 84.02 | -7.16 | -3.50 | — | 0.7x | 90.50 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-11-03 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ONDS | NASDAQ | 5.27 | -8.98 | -3.42 | — | 0.9x | 5.79 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-08-13 (84d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| OSCR | NYSE | 35.19 | 8.58 | -3.38 | — | 1.4x | 32.41 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-08-06 (91d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TSEM | NASDAQ | 148.8 | -8.75 | -3.34 | — | 0.7x | 163.06 | yahoo_chart_daily | 2026-11-03 | US-listed (ADR) | 2026-11-02 (3d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ESLT | NASDAQ | 703.46 | -7.03 | -3.33 | — | 1.3x | 756.62 | yahoo_chart_daily | 2026-11-03 | US-listed (ADR) | 2026-08-11 (86d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| POWL | NASDAQ | 143.1 | -12.39 | -3.33 | — | 0.9x | 163.34 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-08-03 (94d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| INIO | NASDAQ | 14.74 | -19.50 | -3.32 | — | 0.6x | 18.31 | yahoo_chart_daily | 2026-11-03 | US-listed (ADR) | 2026-10-27 (9d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SANM | NASDAQ | 143.77 | -12.60 | -3.32 | — | 0.8x | 164.49 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-07-27 (101d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| HCA | NYSE | 510.7 | 10.34 | 3.22 | — | 1.6x | 462.86 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-10-27 (9d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MOD | NYSE | 98.56 | -21.43 | -3.19 | — | 0.7x | 125.45 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-11-03 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| UBER | NYSE | 69.87 | 4.91 | 3.18 | — | 2.0x | 66.60 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-11-04 (1d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GLXY | NASDAQ | 13.97 | -16.99 | -3.13 | — | 0.4x | 16.83 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-10-27 (9d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ADI | NASDAQ | 406.24 | -3.23 | -3.13 | — | 1.6x | 419.79 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-08-19 (78d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GPGI | NYSE | 12.78 | 9.42 | -3.13 | — | 1.0x | 11.68 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-08-06 (91d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CLMT | NASDAQ | 43.6 | -7.88 | 3.10 | — | 1.0x | 47.33 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-08-07 (90d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LMND | NYSE | 45.9 | 11.03 | 3.05 | — | 1.1x | 41.34 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-07-29 (99d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CI | NYSE | 305.41 | 3.37 | 3.03 | — | 2.0x | 295.44 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-11-05 (0d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CSCO | NASDAQ | 103.61 | 0.62 | -3.00 | — | 1.7x | 102.97 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-08-12 (85d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LASR | NASDAQ | 32.99 | -9.64 | -3.00 | — | 1.0x | 36.51 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-08-06 (91d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BELFA | NASDAQ | 174.19 | -9.28 | -2.98 | — | 1.0x | 192.00 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-10-28 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AGX | NYSE | 290.66 | -16.53 | -2.98 | — | 0.9x | 348.24 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-09-02 (64d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NN | NASDAQ | 8.76 | -11.07 | -2.97 | — | 0.5x | 9.85 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-08-11 (86d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SKE | NYSE | 29.37 | 9.55 | 2.96 | — | 0.9x | 26.81 | yahoo_chart_daily | 2026-11-03 | US-listed (ADR) | 2026-08-13 (84d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CNQ | NYSE | 49.64 | -7.39 | 2.94 | — | 1.8x | 53.60 | yahoo_chart_daily | 2026-11-03 | US-listed (ADR) | 2026-08-06 (91d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CRWD | NASDAQ | 241 | -1.50 | -2.91 | — | 1.0x | 244.68 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-08-26 (71d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| WULF | NASDAQ | 11.7 | -6.62 | -2.91 | — | 0.5x | 12.53 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-08-05 (92d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TRMB | NASDAQ | 54.25 | -17.31 | 2.91 | — | 1.3x | 65.61 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-11-04 (1d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AADX | NYSE | 9.37 | -15.28 | -2.88 | — | 0.7x | 11.06 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-08-12 (85d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SNOW | NYSE | 290.6 | -1.50 | -2.88 | — | 0.9x | 295.04 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-09-02 (64d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| DASH | NASDAQ | 198.59 | 8.33 | -2.85 | — | 0.9x | 183.32 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-10-29 (7d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CDE | NYSE | 14.58 | 8.72 | -2.84 | — | 0.9x | 13.41 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-11-04 (1d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ATEC | NASDAQ | 8.28 | 10.84 | -2.78 | — | 0.5x | 7.47 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-10-29 (7d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BTG | AMEX | 5.11 | 8.72 | 2.74 | — | 0.9x | 4.70 | yahoo_chart_daily | 2026-11-03 | US-listed (ADR) | 2026-11-04 (1d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CAMT | NASDAQ | 101.46 | -9.71 | -2.73 | — | 0.7x | 112.37 | yahoo_chart_daily | 2026-11-03 | US-listed (ADR) | 2026-11-04 (1d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NEWP | AMEX | 5.54 | 14.46 | 2.71 | — | 0.6x | 4.84 | yahoo_chart_daily | 2026-11-03 | US-listed (ADR) | 2026-11-03 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| IESC | NASDAQ | 169.07 | -16.87 | -2.70 | — | 0.7x | 203.38 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-07-31 (97d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PLTR | NASDAQ | 171.7 | -2.11 | -2.70 | — | 1.1x | 175.40 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-11-02 (3d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| INTC | NASDAQ | 58.27 | -3.77 | -2.68 | — | 0.6x | 60.55 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-10-29 (7d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MTRN | NYSE | 187.26 | -17.66 | 2.66 | — | 0.7x | 227.43 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-11-04 (1d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TXN | NASDAQ | 311.49 | -0.32 | -2.64 | — | 1.5x | 312.49 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-10-21 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AVGO | NASDAQ | 325.48 | -2.00 | -2.56 | — | 1.2x | 332.13 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-09-02 (64d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FTAI | NASDAQ | 179.58 | -10.54 | -2.55 | — | 0.7x | 200.74 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-10-29 (7d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| APH | NYSE | 79.01 | -6.15 | -2.54 | — | 1.0x | 84.19 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-10-28 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RVLV | NYSE | 19.98 | -7.20 | 2.54 | — | 1.0x | 21.53 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-11-03 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TREX | NYSE | 57.15 | 14.30 | 2.54 | — | 1.1x | 50.00 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-11-04 (1d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SPCX | NASDAQ | 135.92 | -3.81 | -2.51 | — | 0.9x | 141.31 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-10-20 (16d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PPLI | NASDAQ | 41.99 | 9.06 | 2.50 | — | 1.2x | 38.50 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-11-02 (3d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TRUP | NASDAQ | 33.675 | 8.21 | 2.45 | — | 1.1x | 31.12 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-08-05 (92d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SVM | AMEX | 8.64 | 8.68 | 2.43 | — | 0.8x | 7.95 | yahoo_chart_daily | 2026-11-03 | US-listed (ADR) | 2026-08-10 (87d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BWLP | NYSE | 22.63 | -6.26 | 2.39 | — | 1.1x | 24.14 | yahoo_chart_daily | 2026-11-03 | US-listed (ADR) | 2026-10-19 (17d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| DOX | NASDAQ | 43.66 | -30.07 | 2.38 | — | 0.9x | 62.43 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-11-03 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| DG | NYSE | 141.64 | 8.52 | 2.37 | — | 0.9x | 130.52 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-08-27 (70d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CQP | NYSE | 56.68 | -10.07 | 2.33 | — | 1.3x | 63.03 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-10-29 (7d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CEG | NASDAQ | 245.72 | -6.71 | -2.31 | — | 0.9x | 263.40 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-08-06 (91d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TSLA | NASDAQ | 385.19 | -3.34 | -2.30 | — | 1.1x | 398.50 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-10-21 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ETN | NYSE | 353.08 | -9.86 | -2.29 | — | 0.8x | 391.70 | yahoo_chart_daily | 2026-11-03 | US-listed (ADR) | 2026-11-03 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| HL | NYSE | 14.95 | 13.17 | 2.27 | — | 0.7x | 13.21 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-11-03 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| EXK | NYSE | 7.83 | 11.38 | 2.27 | — | 0.7x | 7.03 | yahoo_chart_daily | 2026-11-03 | US-listed (ADR) | 2026-07-29 (99d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| COF | NYSE | 206.31 | -1.15 | 2.27 | — | 1.7x | 208.71 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-10-20 (16d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BAC | NYSE | 51.63 | 3.97 | 2.27 | — | 2.0x | 49.66 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-10-14 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMZN | NASDAQ | 266.03 | 6.12 | 2.26 | — | 1.1x | 250.69 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-10-29 (7d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| INNV | NASDAQ | 9.79 | 10.62 | 2.25 | — | 1.2x | 8.85 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-11-03 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SSMR | NYSE | 12.71 | 15.44 | 2.20 | — | 0.5x | 11.01 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-08-12 (85d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RIG | NYSE | 5.45 | -7.63 | 2.20 | — | 0.7x | 5.90 | yahoo_chart_daily | 2026-11-03 | US-listed (ADR) | 2026-11-02 (3d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| COST | NASDAQ | 1046.47 | 2.67 | 2.20 | — | 1.8x | 1019.26 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-09-24 (42d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AVAV | NASDAQ | 113.23 | -8.34 | -2.19 | — | 0.8x | 123.53 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-09-09 (57d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ENTG | NASDAQ | 142.87 | -6.47 | -2.18 | — | 0.5x | 152.76 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-10-29 (7d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FTNT | NASDAQ | 129.39 | 1.00 | -2.16 | — | 0.6x | 128.11 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-10-28 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| VET | NYSE | 10.75 | -13.17 | 2.14 | — | 0.8x | 12.38 | yahoo_chart_daily | 2026-11-03 | US-listed (ADR) | 2026-11-04 (1d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ASST | NASDAQ | 22.92 | 10.94 | -2.13 | — | 0.4x | 20.66 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-08-10 (87d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SNPS | NASDAQ | 462.95 | 0.02 | -2.12 | — | 0.9x | 462.88 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-08-26 (71d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| VST | NYSE | 120.29 | -13.83 | -2.11 | — | 0.6x | 139.59 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-08-07 (90d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ANDE | NASDAQ | 55.35 | -11.68 | 2.10 | — | 1.0x | 62.67 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-11-03 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SM | NYSE | 31.06 | -15.30 | 2.09 | — | 0.8x | 36.67 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-11-03 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NXT | NASDAQ | 106.7 | 11.12 | 2.09 | — | 0.5x | 96.02 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-10-28 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RIOT | NASDAQ | 15.37 | 9.63 | -2.08 | — | 0.4x | 14.02 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-11-04 (1d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| WMB | NYSE | 67.86 | -6.36 | 2.08 | — | 1.0x | 72.47 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-11-02 (3d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MMYT | NASDAQ | 50.75 | 11.54 | 2.07 | — | 0.6x | 45.50 | yahoo_chart_daily | 2026-11-03 | US-listed (ADR) | 2026-10-26 (10d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CNC | NYSE | 76.01 | 12.64 | 2.06 | — | 0.9x | 67.48 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-10-27 (9d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BWXT | NYSE | 121.5 | -7.83 | -2.06 | — | 1.0x | 131.82 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-11-02 (3d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PL | NYSE | 12.65 | -6.37 | -2.06 | — | 0.6x | 13.51 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-09-03 (63d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| EQX | AMEX | 11.28 | 12.80 | 2.04 | — | 0.6x | 10.00 | yahoo_chart_daily | 2026-11-03 | US-listed (ADR) | 2026-08-05 (92d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| DDOG | NASDAQ | 188.72 | -14.42 | -2.03 | — | 0.4x | 220.52 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-11-04 (1d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| HAWK | NYSE | 13.37 | -8.36 | 2.02 | — | 0.5x | 14.59 | yahoo_chart_daily | 2026-11-03 | US-listed | 2026-08-13 (84d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |

## US — QUIET one-liners

| Ticker | Venue | Chg % | Pre-mkt % | Post-mkt % | Move vs avg daily | Ref close | Ref source | Ref asof | US tradeable | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PWR | NYSE | -11.65 | -1.97 | — | 3.4x | 657.00 | yahoo_chart_daily | 2026-11-03 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| RYTM | NASDAQ | 28.04 | -1.97 | — | 8.6x | 86.44 | yahoo_chart_daily | 2026-11-03 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| SBET | NASDAQ | 8.50 | -1.96 | — | 2.1x | 6.59 | yahoo_chart_daily | 2026-11-03 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| IART | NASDAQ | 8.73 | -1.96 | — | 2.7x | 13.63 | yahoo_chart_daily | 2026-11-03 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| SITM | NASDAQ | -9.35 | 1.93 | — | 1.9x | 444.88 | yahoo_chart_daily | 2026-11-03 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| GOOGM | NASDAQ | 2.33 | 1.92 | — | 1.5x | 41.16 | yahoo_chart_daily | 2026-11-03 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| WFC | NYSE | 2.22 | 1.91 | — | 1.8x | 85.53 | yahoo_chart_daily | 2026-11-03 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| ECO | NYSE | -8.96 | 1.91 | — | 2.5x | 93.26 | yahoo_chart_daily | 2026-11-03 | US-listed (ADR) | — | no catalyst lookup (outside the per-run budget) |
| AGI | NYSE | 10.78 | 1.90 | — | 3.7x | 27.08 | yahoo_chart_daily | 2026-11-03 | US-listed (ADR) | — | no catalyst lookup (outside the per-run budget) |
| HYMC | NASDAQ | 8.58 | 1.89 | — | 2.3x | 16.09 | yahoo_chart_daily | 2026-11-03 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| PBF | NYSE | -6.67 | 1.89 | — | 1.8x | 77.81 | yahoo_chart_daily | 2026-11-03 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| CLSK | NASDAQ | -16.56 | -1.88 | — | 3.1x | 8.15 | yahoo_chart_daily | 2026-11-03 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| TNK | NYSE | -7.01 | -1.87 | — | 3.1x | 95.58 | yahoo_chart_daily | 2026-11-03 | US-listed (ADR) | — | no catalyst lookup (outside the per-run budget) |
| AEM | NYSE | 9.67 | 1.85 | — | 3.3x | 167.28 | yahoo_chart_daily | 2026-11-03 | US-listed (ADR) | — | no catalyst lookup (outside the per-run budget) |
| TLN | NASDAQ | -8.54 | -1.85 | — | 3.0x | 357.28 | yahoo_chart_daily | 2026-11-03 | US-listed | — | no catalyst lookup (outside the per-run budget) |

## EU/UK — Headline table

| Ticker | Market | Venue | Close | Chg % | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| YUBICO | sweden | OMXSTO | 173.2 | +31.21 | SEK | 8.7x | 132.00 | yahoo_chart_daily | 2026-11-04 | ADR (OTC:YUBCF) | 2026-08-06 | Y | Q3 2026 interim report, Nov 5 at 07:00 CET: net sales +29.3% to SEK 708.0M, EBIT SEK 179.3M with margin 25.3%, bookings +88.2% to SEK 949.0M, new 2027-2031 targets of 15-20% sales growth, CFO appointed Deputy CEO |
| LXS | germany | SWB | 14.49 | +18.67 | EUR | 9.7x | 12.23 | yahoo_chart_daily | 2026-11-04 | none | 2026-08-07 | Y | LANXESS Q3 2026 results day, earnings call Nov 5 at 13:00 CET; the +18.67% print is on the Stuttgart line (SWB), no verified beat or miss headline |
| RHM | germany | XETR | 838.4 | -16.44 | EUR | 8.3x | 1003.40 | yahoo_chart_daily | 2026-11-04 | none | 2026-08-06 | N | catalyst lookup not performed (the run's 10-call budget went to the other target names) |
| NCOD | norway | OSL | 19.4 | -15.65 | NOK | 3.1x | 23.00 | yahoo_chart_daily | 2026-11-04 | none | 2025-02-13 | Y | Norcod Q3 2026 report, Nov 5 at 07:00 CET: first profitable quarter, EBIT 23 MNOK and net profit 8.5 MNOK, record biomass 6,732 t valued at 475 MNOK, operating revenue 89 MNOK vs 37 MNOK a year earlier |
| AF | france | EURONEXT | 12.95 | +14.86 | EUR | 8.4x | 11.28 | yahoo_chart_daily | 2026-11-04 | none | 2026-07-30 | — | no catalyst lookup (outside the per-run budget) |
| TECN | switzerland | SIX | 276.2 | +12.92 | CHF | 7.5x | 244.60 | yahoo_chart_daily | 2026-11-04 | none | 2026-08-11 | — | no catalyst lookup (outside the per-run budget) |
| CBRAIN | denmark | OMXCOP | 115 | +12.30 | DKK | 4.1x | 102.40 | yahoo_chart_daily | 2026-11-04 | none | 2026-08-20 | — | no catalyst lookup (outside the per-run budget) |
| GN | denmark | OMXCOP | 124.4 | +11.97 | DKK | 8.4x | 111.10 | yahoo_chart_daily | 2026-11-04 | ADR (OTC:GNNDY) | 2026-08-19 | — | no catalyst lookup (outside the per-run budget) |
| NKR | norway | OSL | 18.55 | +11.75 | NOK | 4.7x | 16.60 | yahoo_chart_daily | 2026-11-04 | none | 2026-08-20 | — | no catalyst lookup (outside the per-run budget) |
| EGTX | sweden | OMXSTO | 11.14 | +11.51 | SEK | 5.5x | 9.99 | yahoo_chart_daily | 2026-11-04 | none | 2026-08-21 | — | no catalyst lookup (outside the per-run budget) |
| MATAS | denmark | OMXCOP | 86.2 | -11.32 | DKK | 8.7x | 97.20 | yahoo_chart_daily | 2026-11-04 | none | 2026-08-12 | — | no catalyst lookup (outside the per-run budget) |
| AKAST | norway | OSL | 11.56 | -10.25 | NOK | 7.3x | 12.88 | yahoo_chart_daily | 2026-11-04 | none | 2026-08-21 | — | no catalyst lookup (outside the per-run budget) |
| CAMX | sweden | OMXSTO | 730 | +9.77 | SEK | 11.7x | 665.00 | yahoo_chart_daily | 2026-11-04 | none | 2026-07-15 | — | no catalyst lookup (outside the per-run budget) |
| AKRBP | norway | OSL | 321 | -9.32 | NOK | 5.6x | 354.00 | yahoo_chart_daily | 2026-11-04 | none | 2026-10-29 | — | no catalyst lookup (outside the per-run budget) |
| CAT_B | sweden | OMXSTO | 14.7 | -9.15 | SEK | 7.9x | 16.18 | yahoo_chart_daily | 2026-11-04 | ADR (OTC:BLCAF) | 2026-08-20 | — | no catalyst lookup (outside the per-run budget) |
| ROVI | spain | BME | 69.45 | +8.94 | EUR | 7.4x | 63.75 | yahoo_chart_daily | 2026-11-04 | none | 2026-07-23 | — | no catalyst lookup (outside the per-run budget) |
| GOMX | sweden | OMXSTO | 11.12 | -8.85 | SEK | 2.2x | 12.20 | yahoo_chart_daily | 2026-11-04 | none | 2026-08-26 | — | no catalyst lookup (outside the per-run budget) |
| MTG_B | sweden | OMXSTO | 111.3 | -8.62 | SEK | 3.9x | 121.80 | yahoo_chart_daily | 2026-11-04 | none | 2026-07-21 | — | no catalyst lookup (outside the per-run budget) |
| MAERSK_B | denmark | OMXCOP | 20290 | -8.60 | DKK | 6.7x | 22200.00 | yahoo_chart_daily | 2026-11-04 | ADR (OTC:AMKAF) | 2026-08-13 | — | no catalyst lookup (outside the per-run budget) |
| SOI | france | EURONEXT | 101.65 | -7.63 | EUR | 1.6x | 110.05 | yahoo_chart_daily | 2026-11-04 | none | 2026-05-27 | — | no catalyst lookup (outside the per-run budget) |
| IQMX | finland | OMXHEX | 7.3 | -7.59 | EUR | 2.9x | 7.90 | yahoo_chart_daily | 2026-11-04 | none | 2026-11-05 | — | no catalyst lookup (outside the per-run budget) |
| R3NK | germany | XETR | 34.32 | -7.54 | EUR | 4.5x | 37.12 | yahoo_chart_daily | 2026-11-04 | none | 2026-11-05 | — | no catalyst lookup (outside the per-run budget) |
| NEM | germany | XETR | 70.05 | -7.46 | EUR | 3.3x | 75.70 | yahoo_chart_daily | 2026-11-04 | none | 2026-11-05 | — | no catalyst lookup (outside the per-run budget) |
| NRC | norway | OSL | 9.34 | -7.16 | NOK | 3.6x | 10.06 | yahoo_chart_daily | 2026-11-04 | none | 2026-08-13 | — | no catalyst lookup (outside the per-run budget) |
| AMBU_B | denmark | OMXCOP | 92.1 | +7.16 | DKK | 3.8x | 85.95 | yahoo_chart_daily | 2026-11-04 | ADR (OTC:AMBFF) | 2026-08-25 | — | no catalyst lookup (outside the per-run budget) |
| ASHM | uk | LSE | 213.4 | -6.89 | GBX | 6.9x | 229.20 | yahoo_chart_daily | 2026-11-04 | none | 2026-09-07 | — | no catalyst lookup (outside the per-run budget) |
| AMV0 | germany | XETR | 31.6 | -6.65 | EUR | 3.4x | 33.85 | yahoo_chart_daily | 2026-11-04 | none | 2026-08-05 | — | no catalyst lookup (outside the per-run budget) |
| ATT | poland | GPW | 16.96 | +6.60 | PLN | 4.4x | 15.91 | yahoo_chart_daily | 2026-11-04 | none | 2026-09-10 | — | no catalyst lookup (outside the per-run budget) |
| EDV | uk | LSE | 4019 | +6.38 | GBX | 3.0x | 3778.00 | yahoo_chart_daily | 2026-11-04 | none | 2026-07-30 | — | no catalyst lookup (outside the per-run budget) |
| MGNS | uk | LSE | 4403.204 | +6.36 | GBX | 5.0x | 4140.00 | yahoo_chart_daily | 2026-11-04 | none | 2026-07-23 | — | no catalyst lookup (outside the per-run budget) |

## AU (ASX) — Headline table

| Ticker | Venue | Close | Chg % | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CYL | ASX | 4.13 | +18.34 | AUD | 3.7x | 3.49 | yahoo_chart_daily | 2026-11-03 | none | 2026-08-31 | N | ASX announcement Nov 4 at 9:38 a.m. AWST: management team strengthened with the appointment of a CFO and a COO; the shares have risen about 17% since that release. No earnings release in the window |
| VUL | ASX | 1.235 | +18.18 | AUD | 3.4x | 1.04 | yahoo_chart_daily | 2026-11-03 | none | 2026-09-08 | N | no fresh catalyst found (the ASX and EQS items dated 2-5 Nov are WpHG distribution notices; the last headline-level filing was the 30 Sep quarterly activities report on 30 Oct) |
| NEU | ASX | 23.24 | +17.49 | AUD | 6.2x | 19.78 | yahoo_chart_daily | 2026-11-03 | none | 2026-08-24 | — | no catalyst lookup (outside the per-run budget) |
| CIA | ASX | 2.07 | +17.28 | AUD | 4.6x | 1.76 | yahoo_chart_daily | 2026-11-03 | none | 2026-10-28 | — | no catalyst lookup (outside the per-run budget) |
| CU6 | ASX | 1.6 | +15.94 | AUD | 3.5x | 1.38 | yahoo_chart_daily | 2026-11-03 | none | 2026-08-26 | — | no catalyst lookup (outside the per-run budget) |
| ZIP | ASX | 2.14 | +15.68 | AUD | 2.6x | 1.85 | yahoo_chart_daily | 2026-11-03 | ADR (OTC:ZIZTF) | 2026-08-19 | — | no catalyst lookup (outside the per-run budget) |
| EVN | ASX | 13.26 | +14.21 | AUD | 5.9x | 11.61 | yahoo_chart_daily | 2026-11-03 | none | 2026-08-18 | — | no catalyst lookup (outside the per-run budget) |
| KCN | ASX | 4.42 | +14.21 | AUD | 3.8x | 3.87 | yahoo_chart_daily | 2026-11-03 | none | 2026-08-30 | — | no catalyst lookup (outside the per-run budget) |
| CMM | ASX | 14.5 | +14.08 | AUD | 4.6x | 12.71 | yahoo_chart_daily | 2026-11-03 | none | 2026-08-26 | — | no catalyst lookup (outside the per-run budget) |
| VAU | ASX | 6.05 | +13.72 | AUD | 4.9x | 5.32 | yahoo_chart_daily | 2026-11-03 | none | 2026-08-20 | — | no catalyst lookup (outside the per-run budget) |
| PDI | ASX | 4.6 | +13.30 | AUD | 3.1x | 4.06 | yahoo_chart_daily | 2026-11-03 | ADR (OTC:PDIYF) | 2026-09-30 | — | no catalyst lookup (outside the per-run budget) |
| APE | ASX | 16.61 | -13.22 | AUD | 5.0x | 19.14 | yahoo_chart_daily | 2026-11-03 | none | 2026-08-26 | — | no catalyst lookup (outside the per-run budget) |
| RRL | ASX | 6.87 | +13.18 | AUD | 4.7x | 6.07 | yahoo_chart_daily | 2026-11-03 | none | 2026-08-20 | — | no catalyst lookup (outside the per-run budget) |
| RMS | ASX | 3.78 | +12.84 | AUD | 4.9x | 3.35 | yahoo_chart_daily | 2026-11-03 | none | 2026-08-20 | — | no catalyst lookup (outside the per-run budget) |
| EMR | ASX | 6.82 | +12.54 | AUD | 4.4x | 6.06 | yahoo_chart_daily | 2026-11-03 | none | 2026-08-26 | — | no catalyst lookup (outside the per-run budget) |

## Source health

- scanner_calls: 41 | scanner_errors: 0
- pipeline_version: 2026-11-05.2
- et_clock: zoneinfo America/New_York (DST-aware; a fixed UTC-4 mislabels every winter fire)
- premarket_window: 04:00-09:30 ET, resolved with zoneinfo (09:00-14:30 UTC in winter, 08:00-13:30 UTC in summer)
- session_selection: by DATE and order, never by a modal time-of-day. Yahoo stamps a daily bar at the session open, so the ET stamp of the SAME session shifts by one hour across a DST boundary; a modal filter kept the OLDER bars and discarded the NEWEST ones, which rolled the base back to the prior-prior session (66 US + 21 ASX rows lost on 2026-11-03, 24 of 25 ASX rows lost on 2026-11-04).
- yahoo_calls: 244 | yahoo_429: 9 | yahoo_errors: 0
- reference_close (screener vs Yahoo, resolved BEFORE the tables were built): agree=225 mismatch=0 unverified=9 stale_reference=0
  method: the screener's implied reference close (close / (1 + change/100)) is compared
  with Yahoo's own reference close. A match proves the move was measured against the
  TRUE prior close; a mismatch means the row sits on a STALE reference (phantom move).
  Coverage: every row of the US headline, US QUIET, EU/UK and ASX tables is checked.
  Yahoo bar mode: {"closed": 195, "live": 30} (closed = last completed session bar;
  live = in-progress EU/UK session bar, which is what a weekday 08:00 ET EU move needs)
  live drift between the screener snapshot and the later Yahoo print: median=0.00pp max=1.79pp (expected on a live market)
- rows_dropped_stale_ref: 0 (rows whose screener-implied reference close disagreed with Yahoo's by more than 0.5%; they are dropped, not published)
- cross_region_rows_dropped: ['NXT@AU'] (the same name on a US venue and a foreign venue - the US row is kept so the name appears exactly once)
- us_premarket_check (Yahoo 1-min pre/post feed vs the screener pre-market column, base = the IMMEDIATELY prior session's close): checked=9 within_1pp=5 within_3pp=8 unavailable=1
  us_premarket outliers (>3pp; thin pre-market books, not a screener error): [{"symbol": "ZG", "tv": -11.954, "yahoo": -8.621, "delta": 3.333, "yahoo_asof": "08:09"}]
- markets_with_lt5_rows: ['uk:less=4', 'france:less=4', 'netherlands:egreater=2', 'netherlands:less=2', 'belgium:egreater=1', 'belgium:less=2', 'portugal:egreater=1', 'portugal:less=0', 'ireland:egreater=1', 'ireland:less=0', 'italy:less=3', 'switzerland:egreater=4', 'switzerland:less=1', 'spain:egreater=3', 'spain:less=1', 'denmark:less=3', 'finland:egreater=0', 'finland:less=3', 'poland:less=2', 'austria:less=1', 'greece:egreater=0', 'greece:less=2']
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
- bod_no_extended_hours: 88 (deferred to the next scan; not in the headline table)
- earnings_source: screener `earnings_release_date` (last FULL report) + `earnings_release_next_date` (next scheduled)
- earnings_caveat: `earnings_release_date` does NOT capture preliminary, guidance or
  restructuring releases. On 2026-10-23 LKQ fell 22.47% on a preliminary Q3 miss while
  the field still read 2026-07-30. ALWAYS confirm the earnings-driven flag against the
  headline itself; the calendar field is a screen, not a verdict.
- us_line_index: ok (US-listed lines for the 18 foreign home countries, both scanner types; the `US tradeable` column is ADR / US-listed / none)
- catalyst_note: Catalyst lookups for 2026-11-05: 5 US + 3 EU + 2 AU = 10 web searches, the skill's per-run cap. Every headline below was confirmed against the issuer's own release or a market wire.
- catalyst_budget: 5 US + 3 EU + 2 AU = 10 lookups per run
- one_table_rule: each name appears exactly once, in exactly one table, with its
  catalyst in that row's last column. There is no separate catalysts section.
- data_date: US regular session close of the prior trading day; extended-hours columns
  carry the prior session's prints
- deprecations: mcp__tradingview-advanced__*, mcp__tradingview__*, mcp__financekit__*,
  mcp__stocktwits__* are ABSENT in Cloud sessions (tool_search 0 hits; connector catalog
  holds only media + credential tools). The public screener replaces them.

- degraded_sources: 2
  (the chat reply's `errors:` MUST equal this number - one entry per degraded
  source, not one per run)
  1. yahoo_chart_api.reference_close_unresolved — PNR.AX: the reference close could not be resolved (429 or a bad body)
  2. yahoo_premarket_check.unavailable — LMAT: Yahoo's 1-minute pre-market feed returned no usable print

## Audit line

`earnings-reaction target=earnings-reactions:2026-11-05 candidates=564 amc_reactions=0 pre_gaps=164 eu_reactions=30 asx_reactions=15 catalyst_lookups=11 bod=88 rows_dropped_stale_ref=0 degraded_sources=2`
