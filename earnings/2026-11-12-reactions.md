# Earnings reaction scanner — 2026-11-12

- Cron: `0 8 * * 1-5` America/New_York (weekdays, 08:00 ET)
- Fire time (ET): 2026-11-12 08:07:49 Thu
- Run type: `scheduled_scan`
- Source: TradingView public screener (`scanner.tradingview.com/<market>/scan`);
  Yahoo chart API as the independent reference-close source.
- Method: 5 passes (US top-200 mcap, US prior-session movers, EU/UK movers,
  ASX movers, APAC/Gulf movers). Volume floor 10,000 on every pass; `country` filter for
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

- 0 AMC reactions, 115 pre-market gaps, 90 without extended-hours data; 30 EU/UK and 4 ASX movers, 20 APAC/Gulf movers.
- Biggest US extended-hours move: EYE PRE_GAP (16.09%).
- Biggest EU/UK move: BME (+20.84%, uk).
- Biggest ASX move: CU6 (+23.49%).
- Biggest APAC/Gulf move: TRON (+34.48%, indonesia).
- 0 of the 30 EU/UK rows are SETTLED and 30 are LIVE (mid-session). The 12:15 ET settlement pass publishes where those
  live moves actually closed.
- EU/AU/APAC earnings-driven tagging is keyword-based on headlines (best-effort). A row
  whose lookup was not performed carries NO verdict — only a researched row does.

## Actionable read

- **Move vs this name's own history.** The `Move vs avg daily` column divides the
  reaction by the name's own mean absolute daily move over its last
  20 completed sessions. A -27% move in a name that averages +-3% is a
  different event from a -8% move in a name that averages +-7%.
- **US-listed and tradeable vs foreign-only.** 130 published US rows are on a
  US venue; 2 more foreign reactions have a US ADR line
  (the `US tradeable` column carries the ticker); 32 are foreign-only and
  cannot be bought directly by a US reader.
- **Not yet fully priced — US (hypothesis, not a recommendation).**
  TTEK — +10.77%, 1.70% mean absolute daily move over the last 20 completed sessions, 6.3x that average, reference close 40.65 dated 2026-11-10, US access: US-listed, the move now (+10.77%) is larger than the move it follows (-7.48%); the reaction is still being repriced. Hypothesis only: this artifact states no
  direction and no trade.
- **Not yet fully priced — EU/UK (hypothesis, not a recommendation).**
  MEKO — -16.38%, 0.61% mean absolute daily move over the last 20 completed sessions, 26.8x that average, reference close 72.05 dated 2026-11-11, US access: none, the move now (-16.38%) is larger than the move it follows (+1.34%); the reaction is still being repriced. Hypothesis only: this artifact states no
  direction and no trade.
- **Not yet fully priced — AU (ASX) (hypothesis, not a recommendation).**
  DMP — +12.93%, 1.67% mean absolute daily move over the last 20 completed sessions, 7.7x that average, reference close 22.19 dated 2026-11-10, US access: none, the move now (+12.93%) is larger than the move it follows (-0.31%); the reaction is still being repriced. Hypothesis only: this artifact states no
  direction and no trade.

## US — Headline table

| Ticker | Venue | Close | Chg % | Pre-mkt % | Post-mkt % | Move vs avg daily | Ref close | Ref source | Ref asof | US tradeable | Last earnings | Tag | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| EYE | NASDAQ | 18.09 | -4.84 | -16.09 | — | 4.8x | 19.01 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-12 (0d ago) | PRE_GAP | Y | Q3 FY2026 results (Nov 12): revenue $510.53M vs $512.53M consensus; FY2026 guidance EPS $0.95-1.03 and revenue $2.0B vs $2.1B consensus |
| DPC | NYSE | 31.68 | 5.99 | 13.64 | — | 2.3x | 29.89 | yahoo_chart_daily | 2026-11-10 | US-listed (ADR) | 2026-11-12 (0d ago) | PRE_GAP | Y | Q3 2026 results (Nov 12, pre-open): record revenue $308.1M, +39.2% YoY, net income $31.8M vs a $42.2M loss a year earlier, adjusted EBITDA +56% QoQ; FY2026 outlook raised to $1.12-1.13B with new FY2027 guidance |
| AVEX | NYSE | 12.13 | 4.57 | 11.29 | — | 1.4x | 11.60 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-11 (1d ago) | PRE_GAP | Y | Q3 2026 results (Nov 11): revenue $189.7M, +56.5% YoY and above the $150.8M consensus, but a $16.8M net loss ($0.40/sh vs +$0.09 est); FY2026 revenue guidance raised to $820-840M from $700-720M |
| TTEK | NASDAQ | 37.61 | -7.48 | 10.77 | — | 6.3x | 40.65 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-11 (1d ago) | PRE_GAP | Y | Q4 and FY2026 results (Nov 11): adjusted EPS $0.49 vs $0.47 est, net revenue $1.15B in line, backlog $4.67B +13% YoY; Q1 FY2027 EPS guidance $0.36-0.38 came in below the $0.38 consensus midpoint |
| EROC | NYSE | 8.83 | 12.20 | -9.98 | — | 1.3x | 7.87 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-12 (0d ago) | PRE_GAP | Y | Q3 2026 results (Nov 12, pre-open): revenue $152.8M, nearly 4x QoQ, and a first profitable quarter as a public company with net income $8.9M and adjusted EBITDA $12.6M; over $300M of bookings after quarter end push backlog to a record ~$1.6B; FY2026 guidance reaffirmed |
| CRWV | NASDAQ | 60.77 | 24.71 | -9.45 | — | 1.4x | 48.73 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-10 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NBIS | NASDAQ | 154.69 | 15.44 | -9.11 | — | 1.3x | 134.00 | yahoo_chart_daily | 2026-11-10 | US-listed (ADR) | 2026-08-12 (92d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| YETI | NYSE | 42.79 | -4.42 | -8.62 | — | 3.2x | 44.77 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-12 (0d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TWST | NASDAQ | 122.59 | -7.22 | -8.23 | — | 1.2x | 132.13 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-12 (0d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NVDA | NASDAQ | 173.73 | 2.87 | -7.56 | — | 2.8x | 168.89 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-08-26 (78d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SNDK | NASDAQ | 977.69 | 13.69 | -6.00 | — | 0.9x | 859.99 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-10-29 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FPS | NYSE | 24.57 | 14.39 | -5.98 | — | 0.7x | 21.48 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-12 (0d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AXTI | NASDAQ | 46.97 | 19.49 | -5.98 | — | 0.7x | 39.31 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-10-29 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AAOI | NASDAQ | 55.86 | 15.60 | -5.96 | — | 0.8x | 48.32 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-05 (7d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SMCI | NASDAQ | 30.43 | 9.50 | -5.75 | — | 1.2x | 27.79 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-03 (9d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| EQPT | NASDAQ | 15.99 | 18.14 | -5.62 | — | 0.8x | 13.54 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-09 (3d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ASST | NASDAQ | 23.2 | 7.66 | -5.60 | — | 1.0x | 21.55 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-06 (6d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CIFR | NASDAQ | 7.11 | 8.88 | -5.54 | — | 0.7x | 6.53 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-02 (10d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| IREN | NASDAQ | 20.84 | 5.63 | -5.52 | — | 0.7x | 19.73 | yahoo_chart_daily | 2026-11-10 | US-listed (ADR) | 2026-11-05 (7d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PURR | NASDAQ | 9.15 | 4.57 | -5.42 | — | 0.9x | 8.75 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-05 (7d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BMNR | NYSE | 19.24 | 6.42 | -5.15 | — | 1.2x | 18.08 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-10 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| APLD | NASDAQ | 17.91 | 7.37 | -5.08 | — | 0.7x | 16.68 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-10-07 (36d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| HUT | NASDAQ | 61.06 | 7.56 | -5.03 | — | 0.7x | 56.77 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-04 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| COHR | NYSE | 234.51 | 9.25 | -4.92 | — | 0.8x | 214.66 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-04 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GLXY | NASDAQ | 15.97 | 13.18 | -4.82 | — | 0.6x | 14.11 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-10-27 (16d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MXL | NASDAQ | 59.95 | 11.37 | -4.81 | — | 0.6x | 53.83 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-10-22 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CORZ | NASDAQ | 14.57 | 10.97 | -4.80 | — | 0.8x | 13.13 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-05 (7d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PENG | NASDAQ | 49.25 | 10.33 | -4.77 | — | 0.6x | 44.64 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-10-06 (37d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CLSK | NASDAQ | 6.91 | 5.18 | -4.63 | — | 0.7x | 6.57 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-08-06 (98d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LGN | NASDAQ | 37.09 | 15.73 | 4.48 | — | 0.6x | 32.05 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-12 (0d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CRDO | NASDAQ | 141.41 | 8.94 | -4.46 | — | 0.6x | 129.80 | yahoo_chart_daily | 2026-11-10 | US-listed (ADR) | 2026-09-01 (72d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| WULF | NASDAQ | 13.36 | 6.37 | -4.42 | — | 0.6x | 12.56 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-06 (6d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MU | NASDAQ | 811.3 | 11.89 | -4.31 | — | 0.8x | 725.11 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-09-30 (43d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LITE | NASDAQ | 648.06 | 10.67 | -4.24 | — | 0.6x | 585.57 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-02 (10d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MANE | NYSE | 156.56 | 5.47 | -4.20 | — | 1.0x | 148.44 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-10 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| WOLF | NYSE | 27.68 | 5.53 | -4.19 | — | 0.6x | 26.23 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-04 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ALAB | NASDAQ | 230.91 | 6.81 | -4.17 | — | 0.7x | 216.18 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-03 (9d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BTDR | NASDAQ | 7.03 | 9.67 | -4.13 | — | 0.6x | 6.41 | yahoo_chart_daily | 2026-11-10 | US-listed (ADR) | 2026-11-10 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| STX | NASDAQ | 551.72 | 9.99 | -4.06 | — | 0.8x | 501.62 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-10-27 (16d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| WDC | NASDAQ | 313.31 | 8.34 | -4.04 | — | 0.7x | 289.20 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-10-22 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AEHR | NASDAQ | 65.78 | 10.42 | -4.03 | — | 0.5x | 59.57 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-02 (10d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SECZ | NYSE | 9.06 | 6.21 | -3.97 | — | 0.6x | 8.53 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-09 (3d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| DELL | NYSE | 373.68 | 11.75 | -3.93 | — | 0.7x | 334.38 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-09-01 (72d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| HIMS | NYSE | 20.81 | 8.78 | -3.89 | — | 0.8x | 19.13 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-09 (3d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ACMR | NASDAQ | 52.43 | 7.73 | -3.84 | — | 0.7x | 48.67 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-05 (7d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMBQ | NYSE | 50.33 | 11.25 | -3.83 | — | 0.6x | 45.24 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-10 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CIEN | NYSE | 296.04 | 8.80 | -3.83 | — | 0.6x | 272.10 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-09-03 (70d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TTMI | NASDAQ | 78.7 | 8.96 | -3.81 | — | 0.5x | 72.23 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-10-22 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BE | NYSE | 209.47 | 12.97 | -3.78 | — | 0.5x | 185.42 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-10-22 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NVTS | NASDAQ | 10.07 | 7.36 | -3.67 | — | 0.6x | 9.38 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-03 (9d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MRVL | NASDAQ | 168.8 | 9.33 | -3.64 | — | 0.6x | 154.39 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-08-27 (77d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TH | NASDAQ | 11.8 | 14.56 | 3.56 | — | 0.7x | 10.30 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-09 (3d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| VIAV | NASDAQ | 33 | 6.42 | -3.54 | — | 0.6x | 31.01 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-04 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SMCIP | NASDAQ | 52.71 | 8.21 | -3.41 | — | 0.8x | 48.71 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-03 (9d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SEI | NYSE | 64.8 | 4.74 | -3.33 | — | 0.5x | 61.87 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-04 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| COHU | NASDAQ | 45.975 | 5.52 | -3.32 | — | 0.5x | 43.57 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-10-28 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SITM | NASDAQ | 472.56 | 6.32 | -3.21 | — | 0.5x | 444.45 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-04 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ECO | NYSE | 85.75 | 5.00 | -3.19 | — | 1.0x | 81.67 | yahoo_chart_daily | 2026-11-10 | US-listed (ADR) | 2026-11-11 (1d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ENTG | NASDAQ | 154.22 | 11.29 | -3.19 | — | 0.6x | 138.57 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-10-29 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ORCL | NYSE | 128.38 | 8.82 | -3.18 | — | 0.8x | 117.98 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-09-10 (63d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FUN | NYSE | 11.1 | 9.25 | 3.15 | — | 0.5x | 10.16 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-05 (7d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RMBS | NASDAQ | 85.36 | 5.70 | -3.09 | — | 0.7x | 80.76 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-10-26 (17d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| INOD | NASDAQ | 38.17 | 8.90 | -3.07 | — | 0.6x | 35.05 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-05 (7d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| HPE | NYSE | 50.25 | 4.84 | -3.04 | — | 0.8x | 47.93 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-09-02 (71d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| DOCN | NYSE | 87.15 | 9.60 | -3.04 | — | 0.6x | 79.52 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-03 (9d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MKSI | NASDAQ | 226 | 5.87 | -3.01 | — | 0.7x | 213.47 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-04 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GLW | NYSE | 120.46 | 7.43 | -3.01 | — | 0.8x | 112.13 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-10-27 (16d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ONTO | NYSE | 215.06 | 8.89 | -2.98 | — | 0.5x | 197.51 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-09 (3d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| QNT | NASDAQ | 40.57 | -5.65 | -2.97 | — | 0.5x | 43.00 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-05 (7d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| INTC | NASDAQ | 62.5 | 7.52 | -2.96 | — | 0.5x | 58.13 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-10-29 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TER | NASDAQ | 265.78 | 8.30 | -2.93 | — | 0.6x | 245.40 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-10-27 (16d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ASTS | NASDAQ | 36.62 | 8.70 | -2.91 | — | 0.5x | 33.69 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-09 (3d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| VSH | NYSE | 29.14 | 8.77 | -2.88 | — | 0.5x | 26.79 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-04 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| P | NYSE | 106.5 | 4.43 | -2.85 | — | 0.6x | 101.98 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-08-26 (78d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CLS | NYSE | 242.92 | 8.50 | -2.85 | — | 0.5x | 223.89 | yahoo_chart_daily | 2026-11-10 | US-listed (ADR) | 2026-10-26 (17d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ALGM | NASDAQ | 32.11 | 4.59 | -2.83 | — | 0.6x | 30.70 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-10-29 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMKR | NASDAQ | 38.1 | 10.53 | -2.81 | — | 0.5x | 34.47 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-10-26 (17d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BLSH | NYSE | 23.53 | 6.04 | -2.80 | — | 0.6x | 22.19 | yahoo_chart_daily | 2026-11-10 | US-listed (ADR) | 2026-08-13 (91d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| KLAC | NASDAQ | 161.01 | 5.24 | -2.80 | — | 0.6x | 152.99 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-10-28 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ZETA | NYSE | 37.74 | 7.61 | -2.78 | — | 0.8x | 35.07 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-09 (3d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LRCX | NASDAQ | 235.88 | 6.07 | -2.77 | — | 0.6x | 222.39 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-10-21 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FRVO | NASDAQ | 12.94 | 13.71 | -2.70 | — | 0.4x | 11.38 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-09 (3d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| UCTT | NASDAQ | 49.63 | 6.25 | -2.70 | — | 0.4x | 46.71 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-10-27 (16d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NET | NYSE | 315 | 3.01 | -2.70 | — | 0.6x | 305.80 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-05 (7d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FORM | NASDAQ | 95.78 | 11.85 | -2.69 | — | 0.4x | 85.63 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-10-28 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MPWR | NASDAQ | 1478.69 | 8.92 | -2.68 | — | 0.6x | 1357.60 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-10-29 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FLY | NASDAQ | 26.61 | 12.28 | -2.67 | — | 0.4x | 23.70 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-10 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| VRT | NYSE | 206.51 | 6.33 | -2.67 | — | 0.5x | 194.22 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-10-28 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| INIO | NASDAQ | 15.1 | 9.66 | -2.65 | — | 0.4x | 13.77 | yahoo_chart_daily | 2026-11-10 | US-listed (ADR) | 2026-10-27 (16d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FIX | NYSE | 1161.63 | 5.04 | -2.64 | — | 0.5x | 1105.93 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-10-22 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PARR | NYSE | 71.18 | 6.18 | 2.56 | — | 0.8x | 67.04 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-03 (9d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PBF | NYSE | 69.73 | 5.80 | 2.54 | — | 0.6x | 65.91 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-10-29 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RKLB | NASDAQ | 66.15 | 5.49 | -2.53 | — | 0.5x | 62.71 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-09 (3d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FN | NYSE | 369.01 | 5.88 | -2.51 | — | 0.4x | 348.52 | yahoo_chart_daily | 2026-11-10 | US-listed (ADR) | 2026-11-02 (10d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AEM | NYSE | 185.96 | -2.36 | -2.49 | — | 0.8x | 190.46 | yahoo_chart_daily | 2026-11-10 | US-listed (ADR) | 2026-10-28 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMAT | NASDAQ | 395.08 | 6.05 | -2.48 | — | 0.6x | 372.53 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-08-13 (91d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| EGO | NYSE | 33.47 | -5.74 | -2.45 | — | 0.7x | 35.51 | yahoo_chart_daily | 2026-11-10 | US-listed (ADR) | 2026-10-28 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ICHR | NASDAQ | 37.45 | 6.18 | -2.43 | — | 0.4x | 35.27 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-02 (10d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LLY | NYSE | 1437.29 | 0.35 | 2.42 | — | 1.3x | 1432.29 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-10-29 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| STRL | NASDAQ | 303.85 | 4.94 | -2.33 | — | 0.4x | 289.56 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-10-28 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PLPC | NASDAQ | 301 | 5.51 | -2.32 | — | 0.5x | 285.27 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-10-28 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PDFS | NASDAQ | 41.79 | 6.72 | -2.32 | — | 0.4x | 39.16 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-05 (7d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FSLY | NASDAQ | 17.26 | 6.28 | -2.32 | — | 0.4x | 16.24 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-04 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GFS | NASDAQ | 42.85 | 5.49 | -2.31 | — | 0.6x | 40.62 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-04 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TSEM | NASDAQ | 158.87 | 7.64 | -2.28 | — | 0.4x | 147.60 | yahoo_chart_daily | 2026-11-10 | US-listed (ADR) | 2026-11-02 (10d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NEWP | AMEX | 5.41 | -3.39 | -2.22 | — | 0.5x | 5.60 | yahoo_chart_daily | 2026-11-10 | US-listed (ADR) | 2026-11-03 (9d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TRAX | NASDAQ | 50.53 | -3.44 | -2.22 | — | 0.6x | 52.33 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-03 (9d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GNRC | NYSE | 194 | 6.72 | -2.22 | — | 0.6x | 181.78 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-10-28 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ON | NASDAQ | 73.62 | 5.76 | -2.21 | — | 0.6x | 69.61 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-02 (10d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CBRS | NASDAQ | 101.08 | 7.92 | -2.21 | — | 0.4x | 93.66 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-08-12 (92d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| POWI | NASDAQ | 46.49 | 5.80 | -2.13 | — | 0.6x | 43.94 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-04 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FROG | NASDAQ | 109.51 | 5.76 | -2.11 | — | 0.3x | 103.55 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-11-05 (7d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NEM | NYSE | 118.47 | -1.24 | -2.08 | — | 0.8x | 119.96 | yahoo_chart_daily | 2026-11-10 | US-listed | 2026-10-22 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NVMI | NASDAQ | 340.62 | 4.58 | -2.08 | — | 0.6x | 325.70 | yahoo_chart_daily | 2026-11-10 | US-listed (ADR) | 2026-11-05 (7d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| EQX | AMEX | 10.8 | -3.83 | -2.04 | — | 0.7x | 11.23 | yahoo_chart_daily | 2026-11-10 | US-listed (ADR) | 2026-11-09 (3d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |

## US — QUIET one-liners

| Ticker | Venue | Chg % | Pre-mkt % | Post-mkt % | Move vs avg daily | Ref close | Ref source | Ref asof | US tradeable | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|
| RDDT | NYSE | 7.08 | -1.99 | — | 1.5x | 98.67 | yahoo_chart_daily | 2026-11-10 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| NG | AMEX | -3.04 | -1.98 | — | 0.9x | 6.24 | yahoo_chart_daily | 2026-11-10 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| KLIC | NASDAQ | 5.02 | -1.98 | — | 1.2x | 69.70 | yahoo_chart_daily | 2026-11-10 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| AZTA | NASDAQ | 20.80 | -1.84 | — | 4.4x | 40.48 | yahoo_chart_daily | 2026-11-10 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| AMD | NASDAQ | 7.32 | 1.83 | — | 1.3x | 515.21 | yahoo_chart_daily | 2026-11-10 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| EXTR | NASDAQ | 4.67 | -1.79 | — | 1.4x | 25.48 | yahoo_chart_daily | 2026-11-10 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| MTSI | NASDAQ | 10.32 | -1.74 | — | 1.8x | 226.48 | yahoo_chart_daily | 2026-11-10 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| QCOM | NASDAQ | 1.75 | -1.74 | — | 0.6x | 173.53 | yahoo_chart_daily | 2026-11-10 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| DJT | NASDAQ | 21.26 | -1.73 | — | 3.6x | 4.28 | yahoo_chart_daily | 2026-11-10 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| MRNA | NASDAQ | -0.85 | -1.70 | — | 0.2x | 250.83 | yahoo_chart_daily | 2026-11-10 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| ALNY | NASDAQ | 5.41 | 1.65 | — | 1.7x | 151.64 | yahoo_chart_daily | 2026-11-10 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| PLTR | NASDAQ | 2.12 | -1.62 | — | 0.7x | 168.82 | yahoo_chart_daily | 2026-11-10 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| RSKD | NYSE | 22.29 | 1.62 | — | 6.9x | 8.48 | yahoo_chart_daily | 2026-11-10 | US-listed (ADR) | — | no catalyst lookup (outside the per-run budget) |
| RES | NYSE | 7.28 | 1.61 | — | 2.4x | 5.22 | yahoo_chart_daily | 2026-11-10 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| APH | NYSE | -0.80 | -1.60 | — | 0.2x | 79.95 | yahoo_chart_daily | 2026-11-10 | US-listed | — | no catalyst lookup (outside the per-run budget) |

## EU/UK — Headline table

| Ticker | Market | Venue | Close | Chg % | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | Session asof | Settle | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BME | uk | LSE | 337.15117 | +20.84 | GBX | 14.2x | 279.00 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | live | none | 2026-11-12 | — | no catalyst lookup (outside the per-run budget) |
| MEKO | sweden | OMXSTO | 60.25 | -16.38 | SEK | 26.8x | 72.05 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | live | none | 2026-07-23 | Y | Q3 2026 report (Nov 12): net sales SEK 4,341M, -2% reported and -3% organic, adjusted EBIT SEK 214M (4.8% margin) flat y/y, leverage down to 3.0x; no near-term growth guidance |
| YSN | germany | XETR | 198 | -15.20 | EUR | 7.1x | 233.50 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | live | none | 2026-08-13 | — | no catalyst lookup (outside the per-run budget) |
| ADEN | switzerland | SIX | 26.22 | +15.00 | CHF | 9.9x | 22.80 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | live | none | 2026-11-12 | — | no catalyst lookup (outside the per-run budget) |
| FG | sweden | OMXSTO | 18.76 | +13.42 | SEK | 4.3x | 16.54 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | live | none | 2026-08-20 | Y | Q3 2026 report (Nov 12): net sales SEK 1,414.5M, +2.4%, EBITA SEK 139.6M (9.9% margin), EPS SEK 0.84, order book SEK 4,254.3M, +4.4% |
| NORBT | norway | OSL | 184.9 | +12.95 | NOK | 8.3x | 163.70 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | live | none | 2026-08-13 | Y | Q3 2026 results (Nov 12): revenue NOK 677M, +34% YoY and +28% organic, EBIT NOK 116M (+53%), EBIT margin 17% from 14%, contract wins totalling over NOK 500M, additional dividend of NOK 2.00 per share |
| MTHH | denmark | OMXCOP | 338 | +12.11 | DKK | 6.4x | 301.50 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | live | none | 2026-08-27 | — | no catalyst lookup (outside the per-run budget) |
| OBCK | germany | XETR | 42.4 | -9.79 | EUR | 9.0x | 47.00 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | live | none | 2026-08-13 | — | no catalyst lookup (outside the per-run budget) |
| WAC | germany | XETR | 20.7 | -9.61 | EUR | 8.3x | 22.90 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | live | none | 2026-08-13 | — | no catalyst lookup (outside the per-run budget) |
| STG | denmark | OMXCOP | 84.4 | +9.33 | DKK | 14.3x | 77.20 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | live | none | 2026-11-11 | — | no catalyst lookup (outside the per-run budget) |
| BRBY | uk | LSE | 1185 | +8.42 | GBX | 5.9x | 1093.00 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | live | none | 2026-11-12 | — | no catalyst lookup (outside the per-run budget) |
| SIVE | sweden | OMXSTO | 15.95 | -8.33 | SEK | 1.7x | 17.40 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | live | none | 2026-08-27 | — | no catalyst lookup (outside the per-run budget) |
| SUS | sweden | OMXSTO | 57.25 | -8.18 | SEK | 6.4x | 62.35 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | live | none | 2026-08-19 | — | no catalyst lookup (outside the per-run budget) |
| ALCE | switzerland | SIX | 61.24 | +7.21 | CHF | n/a | 57.12 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | live | none | 2026-11-10 | — | no catalyst lookup (outside the per-run budget) |
| EDV | uk | LSE | 3841 | -6.93 | GBX | 2.7x | 4127.00 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | live | none | 2026-11-12 | — | no catalyst lookup (outside the per-run budget) |
| VLX | uk | LSE | 528 | -6.88 | GBX | 2.5x | 567.00 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | live | none | 2026-11-12 | — | no catalyst lookup (outside the per-run budget) |
| OHB | germany | XETR | 197 | -6.86 | EUR | 1.4x | 211.50 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | live | ADR (OTC:OHBTF) | 2026-08-06 | — | no catalyst lookup (outside the per-run budget) |
| NCOD | norway | OSL | 18.75 | -6.02 | NOK | 1.0x | 19.95 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | live | none | 2025-02-13 | — | no catalyst lookup (outside the per-run budget) |
| ENDUR | norway | OSL | 137.4 | +5.69 | NOK | 3.9x | 130.00 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | live | none | 2026-08-20 | — | no catalyst lookup (outside the per-run budget) |
| ANDF | norway | OSL | 26.3 | +5.62 | NOK | 4.2x | 24.90 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | live | none | 2026-08-27 | — | no catalyst lookup (outside the per-run budget) |
| TPRO | italy | MIL | 22.5 | -5.06 | EUR | 1.2x | 23.70 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | live | none | 2026-08-05 | — | no catalyst lookup (outside the per-run budget) |
| FLS | denmark | OMXCOP | 573.5 | -5.05 | DKK | 2.9x | 604.00 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | live | none | 2026-11-11 | — | no catalyst lookup (outside the per-run budget) |
| LBW | poland | GPW | 10.53 | +4.88 | PLN | 2.9x | 10.04 | yahoo_chart_daily | 2026-11-10 | 2026-11-12 | live | none | 2026-09-01 | — | no catalyst lookup (outside the per-run budget) |
| ERA | france | EURONEXT | 36.64 | -4.78 | EUR | 1.8x | 38.48 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | live | none | 2026-07-29 | — | no catalyst lookup (outside the per-run budget) |
| RAND | netherlands | EURONEXT | 43.01 | +4.55 | EUR | 1.9x | 41.14 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | live | none | 2026-10-21 | — | no catalyst lookup (outside the per-run budget) |
| RBREW | denmark | OMXCOP | 468.8 | +4.41 | DKK | 4.0x | 449.00 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | live | none | 2026-11-11 | — | no catalyst lookup (outside the per-run budget) |
| YPSN | switzerland | SIX | 432 | +4.35 | CHF | 4.1x | 414.00 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | live | none | 2026-11-11 | — | no catalyst lookup (outside the per-run budget) |
| BELA | greece | ATHEX | 27.08 | -4.31 | EUR | 5.9x | 28.30 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | live | none | 2026-09-24 | — | no catalyst lookup (outside the per-run budget) |
| BITTI | finland | OMXHEX | 33.05 | -4.20 | EUR | 1.3x | 34.50 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | live | none | 2022-02-10 | — | no catalyst lookup (outside the per-run budget) |
| CMB | italy | MIL | 75.3 | -3.83 | EUR | 2.4x | 78.30 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | live | ADR (NYSE:CMBT) | 2026-09-11 | — | no catalyst lookup (outside the per-run budget) |

## AU (ASX) — Headline table

| Ticker | Venue | Close | Chg % | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | Session asof | Settle | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CU6 | ASX | 2.05 | +23.49 | AUD | 4.3x | 1.66 | yahoo_chart_daily | 2026-11-10 | 2026-11-12 | settled | none | 2026-08-26 | — | no catalyst lookup (outside the per-run budget) |
| DMP | ASX | 25.06 | +12.93 | AUD | 7.7x | 22.19 | yahoo_chart_daily | 2026-11-10 | 2026-11-12 | settled | none | 2026-08-25 | Y | 2026 AGM address and presentation (Nov 11): FY26 underlying EBIT $200.1M, record free cash flow $164.1M, and a trading update showing group same-store sales improving to -4.6% FYTD from -5.8% at the August result |
| G6M | ASX | 2.74 | +10.93 | AUD | 2.6x | 2.47 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | settled | none | 2025-07-06 | — | no catalyst lookup (outside the per-run budget) |
| BOE | ASX | 1.495 | -9.39 | AUD | 1.9x | 1.65 | yahoo_chart_daily | 2026-11-10 | 2026-11-12 | settled | none | 2026-08-26 | N | Substantial-holding notices only (Nov 11: ceasing to be a substantial holder, plus a change in substantial holding) as uranium names sold off; no company results or other news |

## APAC/Gulf — Headline table

| Ticker | Market | Venue | Close | Chg % | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | Session asof | Settle | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TRON | indonesia | IDX | 78 | +34.48 | IDR | 6.0x | 58.00 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| VKTR | indonesia | IDX | 320 | +25.00 | IDR | 3.6x | 256.00 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| HANA | thailand | SET | 48 | +20.75 | THB | 4.5x | 39.75 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | settled | none | 2026-11-11 | — | no catalyst lookup (outside the per-run budget) |
| TKN | thailand | SET | 5.65 | +20.21 | THB | 8.8x | 4.70 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | settled | none | 2026-11-11 | — | no catalyst lookup (outside the per-run budget) |
| BHARATROHAN | india | BSE | 108.6 | +20.00 | INR | 4.1x | 90.50 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| PROZONER | india | BSE | 63.88 | +19.98 | INR | 7.0x | 53.24 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| FLEXFO | india | BSE | 43.84 | -18.78 | INR | 5.8x | 53.98 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| 688787 | china | SSE | 124.9 | -14.21 | CNY | 1.7x | 145.59 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | settled | none | 2026-04-24 | — | no catalyst lookup (outside the per-run budget) |
| 301618 | china | SZSE | 31.7 | +14.07 | CNY | 5.7x | 27.79 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| 300133 | china | SZSE | 10.28 | -13.97 | CNY | 2.5x | 11.95 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | settled | none | 2026-10-23 | — | no catalyst lookup (outside the per-run budget) |
| MIM | singapore | SGX | 1.32 | -9.59 | SGD | 1.1x | 1.46 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| 4144 | ksa | TADAWUL | 73.9 | -8.43 | SAR | 2.4x | 80.70 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| UNIX | thailand | SET | 2.06 | -7.21 | THB | 3.3x | 2.22 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | settled | none | 2026-08-13 | N | no fresh catalyst found |
| C09 | singapore | SGX | 6.64 | -6.74 | SGD | 5.5x | 7.12 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | settled | none | 2026-08-12 | Y | Q3 FY2026 business update (after the Nov 11 close): CDL warns 2HFY2026 results will be "significantly weaker" y/y as capital-recycling transactions slip to FY2027, with KRW FX losses on the Korean subsidiary's intercompany loan and possible property impairments |
| 4280 | ksa | TADAWUL | 12.65 | -6.43 | SAR | 2.4x | 13.52 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | settled | none | 2026-08-06 | — | no catalyst lookup (outside the per-run budget) |
| FCG | newzealand | NZX | 5.45 | -6.03 | NZD | 4.6x | 5.80 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | settled | none | 2026-03-23 | — | no catalyst lookup (outside the per-run budget) |
| 9618 | ksa | TADAWUL | 29 | +5.92 | SAR | 1.0x | 27.38 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| MFT | newzealand | NZX | 70.45 | +5.86 | NZD | 4.0x | 66.55 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | settled | none | 2026-11-11 | — | no catalyst lookup (outside the per-run budget) |
| TRA | newzealand | NZX | 7.54 | +5.45 | NZD | 4.9x | 7.15 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | settled | none | 2026-05-20 | N | no fresh catalyst found |
| 558 | singapore | SGX | 1.8 | -4.76 | SGD | 1.1x | 1.89 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | settled | none | 2026-11-11 | — | no catalyst lookup (outside the per-run budget) |

## Source health

- scanner_calls: 55 | scanner_errors: 0
- markets_scanned: US + 17 EU/UK + ASX + 7 APAC/Gulf (india, thailand, indonesia, china, singapore, newzealand, ksa)
- pipeline_version: 2026-11-11.2
- et_clock: zoneinfo America/New_York (DST-aware; a fixed UTC-4 mislabels every winter fire)
- premarket_window: 04:00-09:30 ET, resolved with zoneinfo (09:00-14:30 UTC in winter, 08:00-13:30 UTC in summer)
- session_selection: by DATE and order, never by a modal time-of-day. Yahoo stamps a daily bar at the session open, so the ET stamp of the SAME session shifts by one hour across a DST boundary; a modal filter kept the OLDER bars and discarded the NEWEST ones, which rolled the base back to the prior-prior session (66 US + 21 ASX rows lost on 2026-11-03, 24 of 25 ASX rows lost on 2026-11-04).
- yahoo_calls: 195 | yahoo_429: 0 | yahoo_errors: 0
- reference_close (screener vs Yahoo, resolved BEFORE the tables were built): agree=184 mismatch=1 unverified=0 stale_reference=1
  method: the screener's implied reference close (close / (1 + change/100)) is compared
  with Yahoo's own reference close. A match proves the move was measured against the
  TRUE prior close; a mismatch means the row sits on a STALE reference (phantom move).
  Coverage: every row of the US headline, US QUIET, EU/UK and ASX tables is checked.
  Yahoo bar mode: {"closed": 154, "live": 30} (closed = last completed session bar;
  live = in-progress EU/UK session bar, which is what a weekday 08:00 ET EU move needs)
  live drift between the screener snapshot and the later Yahoo print: median=0.00pp max=2.18pp (expected on a live market)
- cross_check mismatches: [{"region": "indonesia", "symbol": "MKNT.JK", "tv": 33.333, "yahoo": 0.0, "delta": 33.333, "ref_delta_pct": -25.0, "tv_implied_ref": 24.0, "yahoo_ref": 32.0, "yahoo_date": "2026-11-10", "yahoo_ref_date": "2026-11-09", "verdict": "stale_reference"}]
- rows_dropped_stale_ref: 1 (rows whose screener-implied reference close disagreed with Yahoo's by more than 0.5%; they are dropped, not published)
- rows_dropped_unresolved_ref: 0 (rows whose reference close could not be resolved from Yahoo at all - the base of the move is unverifiable, so the row is dropped rather than published with a '—' base)
- us_premarket_check (Yahoo 1-min pre/post feed vs the screener pre-market column, base = the IMMEDIATELY prior session's close): checked=10 within_1pp=5 within_3pp=9 unavailable=0
  us_premarket outliers (>3pp; thin pre-market books, not a screener error): [{"symbol": "EYE", "tv": -16.086, "yahoo": -11.001, "delta": 5.085, "yahoo_asof": "08:05"}]
- markets_with_lt5_rows: ['france:egreater=0', 'france:less=3', 'netherlands:egreater=1', 'netherlands:less=1', 'belgium:egreater=0', 'belgium:less=1', 'portugal:egreater=0', 'portugal:less=0', 'ireland:egreater=0', 'ireland:less=0', 'italy:less=4', 'switzerland:less=0', 'spain:egreater=1', 'spain:less=1', 'denmark:less=4', 'finland:egreater=0', 'finland:less=3', 'poland:egreater=4', 'poland:less=1', 'austria:egreater=3', 'austria:less=0', 'greece:egreater=1', 'greece:less=1', 'singapore:egreater=2', 'newzealand:egreater=3', 'newzealand:less=1']
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
- bod_no_extended_hours: 90 (deferred to the next scan; not in the headline table)
- earnings_source: screener `earnings_release_date` (last FULL report) + `earnings_release_next_date` (next scheduled)
- earnings_caveat: `earnings_release_date` does NOT capture preliminary, guidance or
  restructuring releases. On 2026-10-23 LKQ fell 22.47% on a preliminary Q3 miss while
  the field still read 2026-07-30. ALWAYS confirm the earnings-driven flag against the
  headline itself; the calendar field is a screen, not a verdict.
- us_line_index: ok (US-listed lines for the 25 foreign home countries, both scanner types; the `US tradeable` column is ADR / US-listed / none)
- catalyst_note: none
- catalyst_budget: 5 US + 3 EU + 2 AU = 10 lookups per run
- one_table_rule: each name appears exactly once, in exactly one table, with its
  catalyst in that row's last column. There is no separate catalysts section.
- data_date: US regular session close of the prior trading day; extended-hours columns
  carry the prior session's prints
- settlement_state: 24 settled, 30 live (a live row's move is a mid-session snapshot, not the session's result)
- rows_per_market (EU/UK, cap 4/market): {'uk': 4, 'sweden': 4, 'germany': 4, 'switzerland': 4, 'norway': 4, 'denmark': 4, 'italy': 4, 'poland': 4, 'france': 3, 'netherlands': 2, 'greece': 2, 'finland': 3, 'spain': 2, 'belgium': 1, 'austria': 3} — the cap stops one thin market taking the table; the EU/UK table was 28% Sweden over nine runs (73 of 264 rows) while Belgium and Greece never appeared once.
- rows_per_market (APAC/Gulf, cap 3/market): {'indonesia': 3, 'thailand': 3, 'india': 3, 'china': 3, 'singapore': 3, 'ksa': 3, 'newzealand': 3}
- deprecations: mcp__tradingview-advanced__*, mcp__tradingview__*, mcp__financekit__*,
  mcp__stocktwits__* are ABSENT in Cloud sessions (tool_search 0 hits; connector catalog
  holds only media + credential tools). The public screener replaces them.

- degraded_sources: 0
  (none - every source answered for every published row)

## Audit line

`earnings-reaction target=earnings-reactions:2026-11-12 candidates=428 amc_reactions=0 pre_gaps=115 eu_reactions=30 asx_reactions=4 apac_reactions=20 catalyst_lookups=13 bod=90 rows_dropped_stale_ref=1 rows_dropped_unresolved_ref=0 degraded_sources=0`
