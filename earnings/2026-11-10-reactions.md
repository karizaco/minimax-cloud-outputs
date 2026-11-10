# Earnings reaction scanner — 2026-11-10

- Cron: `0 8 * * 1-5` America/New_York (weekdays, 08:00 ET)
- Fire time (ET): 2026-11-10 08:08:47 Tue
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

- 0 AMC reactions, 69 pre-market gaps, 82 without extended-hours data; 30 EU/UK and 24 ASX movers.
- Biggest US extended-hours move: APPS PRE_GAP (23.89%).
- Biggest EU/UK move: MMK (+12.54%, austria).
- Biggest ASX move: MND (+15.30%).
- EU/AU earnings-driven tagging is keyword-based on headlines (best-effort).

## Actionable read

- **Move vs this name's own history.** The `Move vs avg daily` column divides the
  reaction by the name's own mean absolute daily move over its last
  20 completed sessions. A -27% move in a name that averages +-3% is a
  different event from a -8% move in a name that averages +-7%.
- **US-listed and tradeable vs foreign-only.** 84 published US rows are on a
  US venue; 2 more foreign reactions have a US ADR line
  (the `US tradeable` column carries the ticker); 52 are foreign-only and
  cannot be bought directly by a US reader.
- **Not yet fully priced — US (hypothesis, not a recommendation).**
  APPS — -23.89%, 5.80% mean absolute daily move over the last 20 completed sessions, 4.1x that average, reference close 10.38 dated 2026-11-06, US access: US-listed, the move now (-23.89%) is larger than the move it follows (+8.86%); the reaction is still being repriced. Hypothesis only: this artifact states no
  direction and no trade.
- **Not yet fully priced — EU/UK (hypothesis, not a recommendation).**
  AUSS — +9.05%, 0.69% mean absolute daily move over the last 20 completed sessions, 13.2x that average, reference close 82.90 dated 2026-11-09, US access: none, the move now (+9.05%) is larger than the move it follows (+0.73%); the reaction is still being repriced. Hypothesis only: this artifact states no
  direction and no trade.
- **Not yet fully priced — AU (ASX) (hypothesis, not a recommendation).**
  MND — +15.30%, 2.29% mean absolute daily move over the last 20 completed sessions, 6.7x that average, reference close 28.30 dated 2026-11-08, US access: none, the move now (+15.30%) is larger than the move it follows (-0.53%); the reaction is still being repriced. Hypothesis only: this artifact states no
  direction and no trade.

## US — Headline table

| Ticker | Venue | Close | Chg % | Pre-mkt % | Post-mkt % | Move vs avg daily | Ref close | Ref source | Ref asof | US tradeable | Last earnings | Tag | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| APPS | NASDAQ | 11.3 | 8.86 | -23.89 | — | 4.1x | 10.38 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-11-09 (1d ago) | PRE_GAP | Y | Q2 FY27 results released after the Nov 9 close (consensus rev $166.75M, EPS -$0.003); shares fell ~26% the day after the print |
| AAON | NASDAQ | 62.87 | 9.93 | 15.52 | — | 3.3x | 57.19 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-11-09 (1d ago) | PRE_GAP | Y | Record Q3 FY26: revenue $707.4M (+84% y/y vs $602.2M cons), adj EPS $0.83 vs $0.58 cons; FY26 sales-growth guidance raised to 72-75%; also disclosed a restatement and a material weakness |
| SANM | NASDAQ | 149.64 | 11.11 | 13.95 | — | 2.7x | 134.68 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-11-09 (1d ago) | PRE_GAP | Y | Q4 FY26 (ended Oct 3): revenue $3.86B, non-GAAP EPS $4.43; FY26 revenue $14.53B (+79% y/y); FY27 outlook about +27% revenue and about +24% non-GAAP EPS |
| RKLB | NASDAQ | 58.86 | 10.91 | -7.78 | — | 1.4x | 53.07 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-11-09 (1d ago) | PRE_GAP | Y | Q3 FY26: record revenue $268M (+73% y/y, above $257M cons) but EPS -$0.12 vs -$0.07 cons; backlog $3.57B (+52% q/q); Q4 guide $270-290M; Neutron first launch pushed to 2027 |
| SRRK | NASDAQ | 51.55 | 9.82 | -6.83 | — | 2.7x | 46.94 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-11-10 (0d ago) | PRE_GAP | Y | Q3 2026 results pre-market Nov 10: net loss $107.2M (-$0.81/sh), ISEMBYLD launch revenue $0.6M; agreed to sell a priority review voucher for $205M; cash and securities $413.6M |
| LIF | NASDAQ | 45.02 | -4.96 | -6.66 | — | 2.5x | 47.37 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-11-10 (0d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CLMT | NASDAQ | 36.06 | -9.03 | -6.54 | — | 1.8x | 39.64 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-11-06 (4d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GEV | NYSE | 829.34 | 7.13 | -6.19 | — | 1.6x | 774.11 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-10-28 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TTD | NASDAQ | 14.93 | 15.47 | -5.44 | — | 1.7x | 12.93 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-11-09 (1d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| QUBT | NASDAQ | 6.86 | 8.37 | -4.81 | — | 1.0x | 6.33 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-11-09 (1d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ATEN | NYSE | 27.06 | 9.29 | -4.14 | — | 1.1x | 24.76 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-11-05 (5d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| OUST | NASDAQ | 38.57 | 10.85 | -3.98 | — | 0.6x | 34.80 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-11-03 (7d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CAT | NYSE | 598.88 | 7.21 | -3.79 | — | 1.3x | 558.63 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-10-29 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AXTI | NASDAQ | 42.91 | 10.37 | -3.78 | — | 0.5x | 38.88 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-10-29 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SEI | NYSE | 62.61 | 8.38 | -3.69 | — | 0.5x | 57.77 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-11-04 (6d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| IONQ | NYSE | 35.34 | 8.34 | -3.62 | — | 0.6x | 32.62 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-11-05 (5d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| HYMC | NASDAQ | 21.27 | 13.32 | -3.62 | — | 0.8x | 18.77 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-10-27 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FLY | NASDAQ | 24.31 | 17.10 | -3.62 | — | 0.5x | 20.76 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-08-11 (91d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TTWO | NASDAQ | 207.4 | -3.48 | 3.47 | — | 2.0x | 214.87 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-11-09 (1d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LEU | NYSE | 117.34 | 12.18 | -3.45 | — | 0.6x | 104.60 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-11-04 (6d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| COHR | NYSE | 225.19 | 16.79 | -3.43 | — | 0.5x | 192.81 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-11-04 (6d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| VRT | NYSE | 200.47 | 9.63 | -3.41 | — | 0.6x | 182.86 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-10-28 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| WIX | NASDAQ | 69.75 | -8.33 | -3.23 | — | 1.0x | 76.09 | yahoo_chart_daily | 2026-11-06 | US-listed (ADR) | 2026-08-04 (98d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RDW | NYSE | 8.15 | 13.04 | -3.07 | — | 0.5x | 7.21 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-11-04 (6d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LITE | NASDAQ | 596.16 | 10.69 | -3.06 | — | 0.5x | 538.59 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-11-02 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BE | NYSE | 193.88 | 11.91 | -3.00 | — | 0.5x | 173.24 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-10-22 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CIEN | NYSE | 269.33 | 10.66 | -2.99 | — | 0.5x | 243.39 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-09-03 (68d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RGTI | NASDAQ | 12.98 | 10.47 | -2.93 | — | 0.5x | 11.75 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-08-06 (96d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| VICR | NASDAQ | 163.51 | 11.32 | -2.89 | — | 0.4x | 146.88 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-10-20 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PPTA | NASDAQ | 21.16 | 8.35 | -2.88 | — | 0.6x | 19.53 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-08-15 (87d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SMTC | NASDAQ | 116.45 | 12.83 | -2.88 | — | 0.4x | 103.21 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-08-25 (77d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AEHR | NASDAQ | 59.81 | 11.65 | -2.86 | — | 0.3x | 53.57 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-07-14 (119d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ASTS | NASDAQ | 36.89 | 14.10 | -2.82 | — | 0.5x | 32.33 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-11-09 (1d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LUNR | NASDAQ | 12.04 | 15.00 | -2.74 | — | 0.4x | 10.47 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-08-13 (89d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BTDR | NASDAQ | 6.61 | 9.89 | -2.72 | — | 0.4x | 6.01 | yahoo_chart_daily | 2026-11-06 | US-listed (ADR) | 2026-08-10 (92d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MXL | NASDAQ | 55.91 | 13.68 | -2.72 | — | 0.3x | 49.18 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-10-22 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FPS | NYSE | 22.6 | 16.02 | -2.70 | — | 0.3x | 19.48 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-09-15 (56d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AEM | NYSE | 200.8 | 4.82 | -2.69 | — | 0.8x | 191.57 | yahoo_chart_daily | 2026-11-06 | US-listed (ADR) | 2026-10-28 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SG | NYSE | 13.36 | 11.24 | -2.62 | — | 0.7x | 12.01 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-11-05 (5d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| OKLO | NYSE | 26.84 | 13.97 | -2.57 | — | 0.5x | 23.55 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-11-06 (4d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ONTO | NYSE | 194.04 | 11.98 | 2.56 | — | 0.4x | 173.28 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-11-09 (1d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| EROC | NYSE | 8.25 | 15.87 | -2.55 | — | 0.3x | 7.12 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-08-11 (91d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ONDS | NASDAQ | 5.97 | 11.90 | -2.51 | — | 0.4x | 5.33 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-08-13 (89d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| INTC | NASDAQ | 59.37 | 5.49 | -2.48 | — | 0.4x | 56.28 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-10-29 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ECG | NYSE | 84.43 | 10.22 | -2.40 | — | 0.4x | 76.60 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-11-03 (7d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MOD | NYSE | 106.15 | 9.87 | -2.39 | — | 0.4x | 96.61 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-11-03 (7d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| INFQ | NYSE | 9.66 | 8.66 | -2.38 | — | 0.4x | 8.89 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-08-12 (90d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| WOLF | NYSE | 26.12 | 9.79 | -2.37 | — | 0.3x | 23.79 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-11-04 (6d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FN | NYSE | 365.94 | 11.86 | -2.36 | — | 0.4x | 327.13 | yahoo_chart_daily | 2026-11-06 | US-listed (ADR) | 2026-11-02 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FLR | NYSE | 50.33 | 8.28 | -2.33 | — | 0.9x | 46.48 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-11-06 (4d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AVAV | NASDAQ | 126.96 | 12.59 | -2.33 | — | 0.6x | 112.76 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-09-09 (62d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ETN | NYSE | 359.3 | 5.14 | -2.31 | — | 0.6x | 341.72 | yahoo_chart_daily | 2026-11-06 | US-listed (ADR) | 2026-11-03 (7d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MRVL | NASDAQ | 154.6 | 9.49 | -2.31 | — | 0.4x | 141.20 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-08-27 (75d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AUGO | NASDAQ | 86.99 | 11.78 | -2.30 | — | 0.5x | 77.82 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-11-05 (5d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GLW | NYSE | 115.95 | 9.25 | -2.26 | — | 0.6x | 106.13 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-10-27 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PENG | NASDAQ | 45.7 | 9.25 | -2.21 | — | 0.3x | 41.83 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-10-06 (35d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NEM | NYSE | 125.16 | 3.52 | -2.19 | — | 0.8x | 120.91 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-10-22 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PWR | NYSE | 591.48 | 9.35 | -2.17 | — | 0.5x | 540.90 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-10-29 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CLSK | NASDAQ | 6.91 | 12.18 | -2.17 | — | 0.3x | 6.16 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-08-06 (96d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TEM | NASDAQ | 84.44 | 11.03 | -2.17 | — | 0.4x | 76.05 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-11-02 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MKSI | NASDAQ | 211.59 | 10.05 | -2.16 | — | 0.5x | 192.27 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-11-04 (6d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SVM | AMEX | 9.73 | 9.33 | -2.16 | — | 0.5x | 8.90 | yahoo_chart_daily | 2026-11-06 | US-listed (ADR) | 2026-11-05 (5d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TTMI | NASDAQ | 75.33 | 13.26 | -2.11 | — | 0.3x | 66.51 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-10-22 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SKYD | NYSE | 8.7 | 8.61 | -2.11 | — | 0.5x | 8.01 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-11-09 (1d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TER | NASDAQ | 246 | 12.73 | -2.08 | — | 0.4x | 218.22 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-10-27 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NVTS | NASDAQ | 9.58 | 11.27 | -2.07 | — | 0.3x | 8.61 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-11-03 (7d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PL | NYSE | 14.37 | 14.50 | -2.06 | — | 0.4x | 12.55 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-09-03 (68d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CEG | NASDAQ | 276.09 | 10.46 | -2.02 | — | 0.7x | 249.95 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-11-09 (1d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MPWR | NASDAQ | 1388.05 | 16.60 | -2.01 | — | 0.5x | 1190.44 | yahoo_chart_daily | 2026-11-06 | US-listed | 2026-10-29 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |

## US — QUIET one-liners

| Ticker | Venue | Chg % | Pre-mkt % | Post-mkt % | Move vs avg daily | Ref close | Ref source | Ref asof | US tradeable | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|
| LRCX | NASDAQ | 10.41 | -2.00 | — | 2.1x | 200.44 | yahoo_chart_daily | 2026-11-06 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| UBS | NYSE | 2.47 | 1.97 | — | 1.5x | 47.78 | yahoo_chart_daily | 2026-11-06 | US-listed (ADR) | — | no catalyst lookup (outside the per-run budget) |
| SPCX | NASDAQ | 5.81 | -1.96 | — | 1.6x | 134.27 | yahoo_chart_daily | 2026-11-06 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| APP | NASDAQ | 4.80 | -1.95 | — | 0.9x | 391.22 | yahoo_chart_daily | 2026-11-06 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| SOLS | NASDAQ | 9.74 | -1.95 | — | 2.8x | 58.00 | yahoo_chart_daily | 2026-11-06 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| STX | NASDAQ | 9.79 | -1.91 | — | 1.9x | 460.99 | yahoo_chart_daily | 2026-11-06 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| NBIS | NASDAQ | 9.24 | -1.91 | — | 1.4x | 129.49 | yahoo_chart_daily | 2026-11-06 | US-listed (ADR) | — | no catalyst lookup (outside the per-run budget) |
| SNDK | NASDAQ | 6.16 | -1.86 | — | 1.0x | 835.06 | yahoo_chart_daily | 2026-11-06 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| SRPT | NASDAQ | -3.25 | 1.86 | — | 1.0x | 17.82 | yahoo_chart_daily | 2026-11-06 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| VIAV | NASDAQ | 12.33 | -1.81 | — | 2.0x | 28.47 | yahoo_chart_daily | 2026-11-06 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| VOYG | NYSE | 16.35 | -1.79 | — | 2.9x | 23.98 | yahoo_chart_daily | 2026-11-06 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| ENTG | NASDAQ | 9.44 | -1.76 | — | 1.9x | 127.98 | yahoo_chart_daily | 2026-11-06 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| MTSI | NASDAQ | 9.02 | -1.74 | — | 1.5x | 210.98 | yahoo_chart_daily | 2026-11-06 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| TRLV | NYSE | -4.76 | 1.73 | — | 1.5x | 11.56 | yahoo_chart_daily | 2026-11-06 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| MPC | NYSE | 4.60 | -1.72 | — | 1.9x | 372.74 | yahoo_chart_daily | 2026-11-06 | US-listed | — | no catalyst lookup (outside the per-run budget) |

## EU/UK — Headline table

| Ticker | Market | Venue | Close | Chg % | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MMK | austria | VIE | 75.4 | +12.54 | EUR | 12.1x | 67.00 | yahoo_chart_daily | 2026-11-09 | none | 2026-08-20 | N | KPS Capital Partners to acquire MM Packaging for a EUR 2.4bn enterprise value; MM Group retains a 30% stake (announced Nov 10) |
| EG7 | sweden | OMXSTO | 15.66 | +12.18 | SEK | 10.1x | 13.96 | yahoo_chart_daily | 2026-11-09 | none | 2026-08-19 | Y | Q3 2026 interim report (Nov 10): net revenue SEK 495.6M (+39.5%), adj EBITDA SEK 125.8M, adj EPS SEK 0.47, EPS -SEK 2.83 after a SEK 367.5M impairment |
| GENO | sweden | OMXSTO | 23.15 | +10.24 | SEK | 8.9x | 21.00 | yahoo_chart_daily | 2026-11-09 | none | 2026-07-23 | Y | Interim report January-September 2026 published Nov 10 07:09 CET: Q3 revenue +34% y/y, nine-month net sales SEK 104.7M |
| AUSS | norway | OSL | 90.4 | +9.05 | NOK | 13.2x | 82.90 | yahoo_chart_daily | 2026-11-09 | none | 2026-08-19 | — | no catalyst lookup (outside the per-run budget) |
| GOMX | sweden | OMXSTO | 13.55 | +7.54 | SEK | 1.6x | 12.60 | yahoo_chart_daily | 2026-11-09 | none | 2026-08-26 | — | no catalyst lookup (outside the per-run budget) |
| HUNT | norway | OSL | 15.52 | -6.51 | NOK | 1.7x | 16.60 | yahoo_chart_daily | 2026-11-09 | none | 2024-05-30 | — | no catalyst lookup (outside the per-run budget) |
| GNS | poland | GPW | 14.8 | +6.47 | PLN | 3.9x | 13.90 | yahoo_chart_daily | 2026-11-09 | none | 2026-09-30 | — | no catalyst lookup (outside the per-run budget) |
| FLAT_B | sweden | OMXSTO | 8.645 | +6.47 | SEK | 4.0x | 8.12 | yahoo_chart_daily | 2026-11-09 | none | — | — | no catalyst lookup (outside the per-run budget) |
| FOUR | uk | LSE | 4038 | -5.87 | GBX | 5.3x | 4290.00 | yahoo_chart_daily | 2026-11-09 | none | 2026-08-05 | — | no catalyst lookup (outside the per-run budget) |
| AZT | norway | OSL | 22.9 | +5.53 | NOK | 3.0x | 21.70 | yahoo_chart_daily | 2026-11-09 | none | 2026-11-05 | — | no catalyst lookup (outside the per-run budget) |
| KOMPL | norway | OSL | 6.88 | +5.52 | NOK | 1.9x | 6.52 | yahoo_chart_daily | 2026-11-09 | none | 2026-10-22 | — | no catalyst lookup (outside the per-run budget) |
| SMCRT | sweden | OMXSTO | 17.9 | +5.29 | SEK | 2.5x | 17.00 | yahoo_chart_daily | 2026-11-09 | none | 2026-11-05 | — | no catalyst lookup (outside the per-run budget) |
| HLUN_A | denmark | OMXCOP | 55.7 | +5.29 | DKK | 4.5x | 52.90 | yahoo_chart_daily | 2026-11-09 | none | — | — | no catalyst lookup (outside the per-run budget) |
| PLT | norway | OSL | 11.5 | -5.27 | NOK | 1.9x | 12.14 | yahoo_chart_daily | 2026-11-09 | none | 2026-08-06 | — | no catalyst lookup (outside the per-run budget) |
| ELPE | greece | ATHEX | 17.09 | +5.17 | EUR | 2.3x | 16.25 | yahoo_chart_daily | 2026-11-09 | none | 2026-08-05 | — | no catalyst lookup (outside the per-run budget) |
| TRUE_B | sweden | OMXSTO | 22.87 | -4.79 | SEK | 1.5x | 24.02 | yahoo_chart_daily | 2026-11-09 | none | 2026-11-03 | — | no catalyst lookup (outside the per-run budget) |
| FIA1S | finland | OMXHEX | 5.64 | +4.74 | EUR | 1.8x | 5.38 | yahoo_chart_daily | 2026-11-09 | none | 2026-10-27 | — | no catalyst lookup (outside the per-run budget) |
| COA | uk | LSE | 79.9 | -4.71 | GBX | 5.5x | 83.85 | yahoo_chart_daily | 2026-11-09 | none | 2026-07-28 | — | no catalyst lookup (outside the per-run budget) |
| ELG | germany | XETR | 115 | -4.64 | EUR | 1.5x | 120.60 | yahoo_chart_daily | 2026-11-09 | none | 2026-08-04 | — | no catalyst lookup (outside the per-run budget) |
| KEOC | sweden | OMXSTO | 6.21 | -4.61 | SEK | 1.6x | 6.51 | yahoo_chart_daily | 2026-11-09 | none | 2026-08-31 | — | no catalyst lookup (outside the per-run budget) |
| HEX | norway | OSL | 12.86 | +4.55 | NOK | 2.0x | 12.30 | yahoo_chart_daily | 2026-11-09 | none | 2026-11-06 | — | no catalyst lookup (outside the per-run budget) |
| ROSE | uk | LSE | 332.478 | +4.55 | GBX | 4.0x | 318.00 | yahoo_chart_daily | 2026-11-09 | none | 2026-09-03 | — | no catalyst lookup (outside the per-run budget) |
| OPTIMA | greece | ATHEX | 14.77 | +4.53 | EUR | 2.0x | 14.13 | yahoo_chart_daily | 2026-11-09 | none | 2026-07-30 | — | no catalyst lookup (outside the per-run budget) |
| EDEN | france | EURONEXT | 25.41 | +4.40 | EUR | 2.2x | 24.34 | yahoo_chart_daily | 2026-11-09 | ADR (OTC:EDNSF) | 2026-07-22 | — | no catalyst lookup (outside the per-run budget) |
| FG | sweden | OMXSTO | 16.18 | +4.39 | SEK | 1.4x | 15.50 | yahoo_chart_daily | 2026-11-09 | none | 2026-08-20 | — | no catalyst lookup (outside the per-run budget) |
| HEN3 | germany | XETR | 87.28 | +4.28 | EUR | 4.3x | 83.70 | yahoo_chart_daily | 2026-11-09 | none | 2026-08-06 | — | no catalyst lookup (outside the per-run budget) |
| HLUN_B | denmark | OMXCOP | 58.6 | +4.27 | DKK | 3.4x | 56.20 | yahoo_chart_daily | 2026-11-09 | none | 2026-08-19 | — | no catalyst lookup (outside the per-run budget) |
| NTG | denmark | OMXCOP | 314.5 | -4.26 | DKK | 2.2x | 328.50 | yahoo_chart_daily | 2026-11-09 | none | 2026-09-22 | — | no catalyst lookup (outside the per-run budget) |
| OVZON | sweden | OMXSTO | 39.5 | +4.22 | SEK | 1.5x | 37.90 | yahoo_chart_daily | 2026-11-09 | none | 2026-10-21 | — | no catalyst lookup (outside the per-run budget) |
| BICO | sweden | OMXSTO | 24.75 | +4.21 | SEK | 3.6x | 23.75 | yahoo_chart_daily | 2026-11-09 | ADR (OTC:CLLKF) | 2026-08-19 | — | no catalyst lookup (outside the per-run budget) |

## AU (ASX) — Headline table

| Ticker | Venue | Close | Chg % | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MND | ASX | 32.63 | +15.30 | AUD | 6.7x | 28.30 | yahoo_chart_daily | 2026-11-08 | none | 2026-08-24 | Y | Business update Nov 10: H1 FY27 guidance of about A$1.7bn revenue and A$80-85M net profit after tax; A$830M of new contracts secured since 1 July |
| NXL | ASX | 1.7 | -10.29 | AUD | 3.5x | 1.90 | yahoo_chart_daily | 2026-11-08 | none | 2026-08-23 | N | no fresh catalyst found |
| SLC | ASX | 2.47 | -10.18 | AUD | 6.4x | 2.75 | yahoo_chart_daily | 2026-11-08 | none | 2026-08-18 | — | no catalyst lookup (outside the per-run budget) |
| WBT | ASX | 2.48 | +9.25 | AUD | 1.7x | 2.27 | yahoo_chart_daily | 2026-11-08 | none | 2026-08-28 | — | no catalyst lookup (outside the per-run budget) |
| TPW | ASX | 6.42 | +8.08 | AUD | 1.5x | 5.94 | yahoo_chart_daily | 2026-11-08 | none | 2026-08-18 | — | no catalyst lookup (outside the per-run budget) |
| SKS | ASX | 5.88 | +7.69 | AUD | 1.7x | 5.46 | yahoo_chart_daily | 2026-11-08 | none | 2026-08-17 | — | no catalyst lookup (outside the per-run budget) |
| OBM | ASX | 1.64 | +7.19 | AUD | 1.7x | 1.53 | yahoo_chart_daily | 2026-11-08 | none | 2026-08-25 | — | no catalyst lookup (outside the per-run budget) |
| CGS | ASX | 3.6 | +7.14 | AUD | 3.6x | 3.36 | yahoo_chart_daily | 2026-11-08 | none | 2026-08-17 | — | no catalyst lookup (outside the per-run budget) |
| MLX | ASX | 1.725 | +7.14 | AUD | 1.4x | 1.61 | yahoo_chart_daily | 2026-11-08 | none | 2026-08-27 | — | no catalyst lookup (outside the per-run budget) |
| VUL | ASX | 1.22 | +6.55 | AUD | 1.2x | 1.15 | yahoo_chart_daily | 2026-11-08 | none | 2026-09-08 | — | no catalyst lookup (outside the per-run budget) |
| MP1 | ASX | 18.45 | +6.40 | AUD | 1.4x | 17.34 | yahoo_chart_daily | 2026-11-08 | none | 2026-08-19 | — | no catalyst lookup (outside the per-run budget) |
| SXE | ASX | 3.84 | +6.37 | AUD | 1.7x | 3.61 | yahoo_chart_daily | 2026-11-08 | none | 2026-08-17 | — | no catalyst lookup (outside the per-run budget) |
| SHA | ASX | 7.02 | +6.36 | AUD | 2.0x | 6.60 | yahoo_chart_daily | 2026-11-08 | none | 2026-08-18 | — | no catalyst lookup (outside the per-run budget) |
| SRG | ASX | 3.51 | +6.36 | AUD | 3.7x | 3.30 | yahoo_chart_daily | 2026-11-08 | none | 2026-08-17 | — | no catalyst lookup (outside the per-run budget) |
| QAN | ASX | 9.9 | +6.34 | AUD | 3.3x | 9.31 | yahoo_chart_daily | 2026-11-08 | none | 2026-08-26 | — | no catalyst lookup (outside the per-run budget) |
| IMD | ASX | 3.48 | +6.10 | AUD | 2.2x | 3.28 | yahoo_chart_daily | 2026-11-08 | none | 2026-08-16 | — | no catalyst lookup (outside the per-run budget) |
| NWH | ASX | 6.49 | +6.05 | AUD | 2.5x | 6.12 | yahoo_chart_daily | 2026-11-08 | none | 2026-08-19 | — | no catalyst lookup (outside the per-run budget) |
| MAD | ASX | 5.79 | +6.04 | AUD | 2.6x | 5.46 | yahoo_chart_daily | 2026-11-08 | none | 2026-08-23 | — | no catalyst lookup (outside the per-run budget) |
| CU6 | ASX | 1.66 | +5.73 | AUD | 1.2x | 1.57 | yahoo_chart_daily | 2026-11-08 | none | 2026-08-26 | — | no catalyst lookup (outside the per-run budget) |
| FDC | ASX | 3.53 | +5.37 | AUD | 3.0x | 3.35 | yahoo_chart_daily | 2026-11-08 | none | 2026-08-27 | — | no catalyst lookup (outside the per-run budget) |
| CIA | ASX | 2.21 | +5.24 | AUD | 1.3x | 2.10 | yahoo_chart_daily | 2026-11-08 | none | 2026-10-28 | — | no catalyst lookup (outside the per-run budget) |
| DOW | ASX | 7.3 | +5.19 | AUD | 3.5x | 6.94 | yahoo_chart_daily | 2026-11-08 | none | 2026-08-19 | — | no catalyst lookup (outside the per-run budget) |
| AYA | ASX | 3.66 | +5.17 | AUD | 1.3x | 3.48 | yahoo_chart_daily | 2026-11-08 | none | 2026-08-18 | — | no catalyst lookup (outside the per-run budget) |
| PDN | ASX | 8.68 | +4.96 | AUD | 1.3x | 8.27 | yahoo_chart_daily | 2026-11-08 | none | 2026-11-04 | — | no catalyst lookup (outside the per-run budget) |

## Source health

- scanner_calls: 41 | scanner_errors: 0
- pipeline_version: 2026-11-06.2
- et_clock: zoneinfo America/New_York (DST-aware; a fixed UTC-4 mislabels every winter fire)
- premarket_window: 04:00-09:30 ET, resolved with zoneinfo (09:00-14:30 UTC in winter, 08:00-13:30 UTC in summer)
- session_selection: by DATE and order, never by a modal time-of-day. Yahoo stamps a daily bar at the session open, so the ET stamp of the SAME session shifts by one hour across a DST boundary; a modal filter kept the OLDER bars and discarded the NEWEST ones, which rolled the base back to the prior-prior session (66 US + 21 ASX rows lost on 2026-11-03, 24 of 25 ASX rows lost on 2026-11-04).
- yahoo_calls: 149 | yahoo_429: 0 | yahoo_errors: 0
- reference_close (screener vs Yahoo, resolved BEFORE the tables were built): agree=138 mismatch=1 unverified=0 stale_reference=1
  method: the screener's implied reference close (close / (1 + change/100)) is compared
  with Yahoo's own reference close. A match proves the move was measured against the
  TRUE prior close; a mismatch means the row sits on a STALE reference (phantom move).
  Coverage: every row of the US headline, US QUIET, EU/UK and ASX tables is checked.
  Yahoo bar mode: {"closed": 108, "live": 30} (closed = last completed session bar;
  live = in-progress EU/UK session bar, which is what a weekday 08:00 ET EU move needs)
  live drift between the screener snapshot and the later Yahoo print: median=0.00pp max=2.10pp (expected on a live market)
- cross_check mismatches: [{"region": "AU", "symbol": "SSM.AX", "tv": -5.909, "yahoo": -4.66, "delta": -1.249, "ref_delta_pct": 1.326, "tv_implied_ref": 2.2, "yahoo_ref": 2.1712, "yahoo_date": "2026-11-10", "yahoo_ref_date": "2026-11-08", "verdict": "stale_reference"}]
- rows_dropped_stale_ref: 1 (rows whose screener-implied reference close disagreed with Yahoo's by more than 0.5%; they are dropped, not published)
- rows_dropped_unresolved_ref: 0 (rows whose reference close could not be resolved from Yahoo at all - the base of the move is unverifiable, so the row is dropped rather than published with a '—' base)
- us_premarket_check (Yahoo 1-min pre/post feed vs the screener pre-market column, base = the IMMEDIATELY prior session's close): checked=10 within_1pp=8 within_3pp=9 unavailable=0
  us_premarket outliers (>3pp; thin pre-market books, not a screener error): [{"symbol": "SRRK", "tv": -6.828, "yahoo": -3.589, "delta": 3.239, "yahoo_asof": "07:52"}]
- markets_with_lt5_rows: ['uk:less=4', 'france:less=1', 'netherlands:egreater=1', 'netherlands:less=0', 'belgium:egreater=0', 'belgium:less=1', 'portugal:egreater=0', 'portugal:less=0', 'ireland:egreater=0', 'ireland:less=0', 'italy:less=0', 'switzerland:egreater=1', 'switzerland:less=1', 'spain:less=1', 'finland:egreater=3', 'finland:less=2', 'poland:egreater=3', 'poland:less=1', 'austria:egreater=2', 'austria:less=0', 'greece:egreater=3', 'greece:less=0']
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
- bod_no_extended_hours: 82 (deferred to the next scan; not in the headline table)
- earnings_source: screener `earnings_release_date` (last FULL report) + `earnings_release_next_date` (next scheduled)
- earnings_caveat: `earnings_release_date` does NOT capture preliminary, guidance or
  restructuring releases. On 2026-10-23 LKQ fell 22.47% on a preliminary Q3 miss while
  the field still read 2026-07-30. ALWAYS confirm the earnings-driven flag against the
  headline itself; the calendar field is a screen, not a verdict.
- us_line_index: ok (US-listed lines for the 18 foreign home countries, both scanner types; the `US tradeable` column is ADR / US-listed / none)
- catalyst_note: none
- catalyst_budget: 5 US + 3 EU + 2 AU = 10 lookups per run
- one_table_rule: each name appears exactly once, in exactly one table, with its
  catalyst in that row's last column. There is no separate catalysts section.
- data_date: US regular session close of the prior trading day; extended-hours columns
  carry the prior session's prints
- deprecations: mcp__tradingview-advanced__*, mcp__tradingview__*, mcp__financekit__*,
  mcp__stocktwits__* are ABSENT in Cloud sessions (tool_search 0 hits; connector catalog
  holds only media + credential tools). The public screener replaces them.

- degraded_sources: 0
  (none - every source answered for every published row)

## Audit line

`earnings-reaction target=earnings-reactions:2026-11-10 candidates=419 amc_reactions=0 pre_gaps=69 eu_reactions=30 asx_reactions=24 catalyst_lookups=10 bod=82 rows_dropped_stale_ref=1 rows_dropped_unresolved_ref=0 degraded_sources=0`
