# Earnings reaction scanner — 2026-11-09

- Cron: `0 8 * * 1-5` America/New_York (weekdays, 08:00 ET)
- Fire time (ET): 2026-11-09 08:07:35 Mon
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

- 0 AMC reactions, 83 pre-market gaps, 131 without extended-hours data; 30 EU/UK and 25 ASX movers.
- Biggest US extended-hours move: CECO PRE_GAP (35.19%).
- Biggest EU/UK move: KNOS (-11.83%, uk).
- Biggest ASX move: VNT (-16.23%).
- EU/AU earnings-driven tagging is keyword-based on headlines (best-effort).

## Actionable read

- **Move vs this name's own history.** The `Move vs avg daily` column divides the
  reaction by the name's own mean absolute daily move over its last
  20 completed sessions. A -27% move in a name that averages +-3% is a
  different event from a -8% move in a name that averages +-7%.
- **US-listed and tradeable vs foreign-only.** 98 published US rows are on a
  US venue; 4 more foreign reactions have a US ADR line
  (the `US tradeable` column carries the ticker); 51 are foreign-only and
  cannot be bought directly by a US reader.
- **Not yet fully priced — US (hypothesis, not a recommendation).**
  CECO — +35.19%, 6.10% mean absolute daily move over the last 20 completed sessions, 5.8x that average, reference close 37.66 dated 2026-11-05, US access: US-listed, the move now (+35.19%) is larger than the move it follows (+16.06%); the reaction is still being repriced. Hypothesis only: this artifact states no
  direction and no trade.
- **Not yet fully priced — EU/UK (hypothesis, not a recommendation).**
  KNOS — -11.83%, 1.29% mean absolute daily move over the last 20 completed sessions, 9.2x that average, reference close 1230.00 dated 2026-11-06, US access: none, the move now (-11.83%) is larger than the move it follows (-1.91%); the reaction is still being repriced. Hypothesis only: this artifact states no
  direction and no trade.
- **Not yet fully priced — AU (ASX) (hypothesis, not a recommendation).**
  VNT — -16.23%, 1.82% mean absolute daily move over the last 20 completed sessions, 8.9x that average, reference close 5.73 dated 2026-11-05, US access: none, the move now (-16.23%) is larger than the move it follows (-2.22%); the reaction is still being repriced. Hypothesis only: this artifact states no
  direction and no trade.

## US — Headline table

| Ticker | Venue | Close | Chg % | Pre-mkt % | Post-mkt % | Move vs avg daily | Ref close | Ref source | Ref asof | US tradeable | Last earnings | Tag | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CECO | AMEX | 43.71 | 16.06 | 35.19 | — | 5.8x | 37.66 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-08-10 (91d ago) | PRE_GAP | Y | Q3 2026 results released pre-market Mon Nov 9 (8:30 ET call), first print as the first primary listing on TXSE after the voluntary Nasdaq transfer; the retrieved sources carry the release date but not the reported figures |
| VIR | NASDAQ | 12.21 | 10.80 | 15.09 | — | 4.1x | 11.02 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-11-04 (5d ago) | PRE_GAP | Y | Q3 2026 (Nov 4): EPS -$0.81 vs -$1.02 est, revenue $25.7M, Lumvoa net product revenue $24.7M with 100+ patients on therapy; today's pre-market move driven by positive VRDN-008 Phase 1 data (Nov 9) - 74% peak IgG reduction, 15-18 day half-life, potential every-8-week dosing, MG registrational start planned mid-2027 |
| IBRX | NASDAQ | 8.635 | 7.80 | -13.72 | — | 2.9x | 8.01 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-08-04 (97d ago) | PRE_GAP | N | QUILT-2.005 Cohort A topline (Nov 9): ANKTIVA plus BCG met the primary endpoint in BCG-naive high-grade non-muscle invasive bladder cancer (n=370), statistically significant vs BCG alone in CIS, no treatment-related deaths; Q3 earnings due Nov 10 |
| REF | NYSE | 18.05 | 7.12 | 10.08 | — | 2.5x | 16.85 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-09-10 (60d ago) | PRE_GAP | Y | Reformation Q3 FY2026 (Nov 5): revenue $173.6M +19.1% vs $169.7M consensus, adjusted EBITDA +64.2% to a 13.3% margin, EPS -$0.02 vs +$0.11 consensus on a 165.9% effective tax rate, FY26 revenue guidance raised to $610-612M; BTIG target raised to $21, Baird to $20 |
| IMVT | NASDAQ | 30.53 | 7.54 | 9.66 | — | 3.7x | 28.39 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-08-06 (95d ago) | PRE_GAP | Y | Fiscal Q2 2026 results (Nov 9, 8:00 ET): IMVT-1402 600mg met the primary endpoint - ACR20 at Week 28 of 92.5% vs 75.6% placebo (p=0.0139) in difficult-to-treat rheumatoid arthritis, ACR50 80.0% vs 56.1%; the 300mg arm was not differentiated, IMVT-1402 is not being advanced in Sjogren's disease, cash $722.3M |
| KGS | NYSE | 41.67 | 7.04 | 8.16 | — | 2.2x | 38.93 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-08-06 (95d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MNDY | NASDAQ | 87.93 | -6.30 | -6.91 | — | 2.1x | 93.84 | yahoo_chart_daily | 2026-11-05 | US-listed (ADR) | 2026-08-10 (91d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AKAM | NASDAQ | 83.09 | 6.74 | -6.25 | — | 1.9x | 77.84 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-11-05 (4d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ASTS | NASDAQ | 32.33 | 7.05 | 5.94 | — | 1.1x | 30.20 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-08-10 (91d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CNL | NASDAQ | 13.39 | 7.38 | 4.85 | — | 1.2x | 12.47 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-08-12 (89d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NVDA | NASDAQ | 186.64 | 2.78 | -4.81 | — | 2.0x | 181.60 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-08-26 (75d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| DB | NYSE | 34.84 | -4.34 | 4.45 | — | 2.1x | 36.42 | yahoo_chart_daily | 2026-11-05 | US-listed (ADR) | 2026-10-28 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMD | NASDAQ | 449.04 | 11.04 | 4.32 | — | 0.9x | 404.40 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-11-03 (6d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NRG | NYSE | 88.29 | 9.61 | 4.20 | — | 1.3x | 80.55 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-11-09 (0d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| HYMC | NASDAQ | 18.77 | 10.28 | 4.16 | — | 1.1x | 17.02 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-10-27 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MANE | NYSE | 138.78 | 7.92 | 4.05 | — | 1.0x | 128.60 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-08-11 (90d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PLAB | NASDAQ | 27.36 | 7.29 | -3.98 | — | 1.6x | 25.50 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-08-26 (75d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TH | NASDAQ | 11.36 | 9.02 | -3.96 | — | 0.8x | 10.42 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-08-10 (91d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SCCO | NYSE | 167.27 | 1.14 | 3.84 | — | 1.7x | 165.38 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-10-21 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FCX | NYSE | 59.42 | 2.63 | 3.82 | — | 1.9x | 57.90 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-10-27 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| YELP | NYSE | 19.46 | -5.17 | 3.80 | — | 1.1x | 20.52 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-08-06 (95d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SGI | NYSE | 64.17 | -5.45 | -3.77 | — | 1.4x | 67.87 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-08-06 (95d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| KOD | NASDAQ | 99.3 | 9.10 | 3.73 | — | 0.8x | 91.02 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-08-13 (88d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| USAR | NASDAQ | 8.225 | 10.85 | 3.71 | — | 0.7x | 7.42 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-08-10 (91d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GCT | NASDAQ | 58.37 | -7.36 | 3.68 | — | 1.3x | 63.01 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-08-06 (95d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| UEC | AMEX | 6.92 | 6.79 | 3.47 | — | 0.9x | 6.48 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-09-29 (41d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AVGO | NASDAQ | 293.69 | 0.74 | 3.45 | — | 1.3x | 291.53 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-09-02 (68d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FLO | NYSE | 6.71 | -5.49 | 3.43 | — | 1.4x | 7.10 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-02-12 (270d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PPTA | NASDAQ | 19.53 | 16.60 | 3.33 | — | 0.7x | 16.75 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-08-15 (86d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| IREN | NASDAQ | 21.64 | 20.02 | -3.33 | — | 0.4x | 18.03 | yahoo_chart_daily | 2026-11-05 | US-listed (ADR) | 2026-08-27 (74d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMZN | NASDAQ | 259.3 | -0.35 | 3.28 | — | 1.7x | 260.21 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-10-29 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ONDS | NASDAQ | 5.335 | 18.03 | 3.28 | — | 0.6x | 4.52 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-08-13 (88d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BSP | NASDAQ | 42.41 | -5.94 | 3.18 | — | 0.6x | 45.09 | yahoo_chart_daily | 2026-11-05 | US-listed (ADR) | 2026-08-13 (88d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CIFR | NASDAQ | 6.545 | 17.93 | -3.14 | — | 0.4x | 5.55 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-11-02 (7d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BETA | NYSE | 27.12 | 12.77 | -3.10 | — | 0.7x | 24.05 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-11-03 (6d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| EROC | NYSE | 7.12 | 7.23 | 3.09 | — | 0.4x | 6.64 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-08-11 (90d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AUGO | NASDAQ | 77.82 | 9.19 | 3.06 | — | 0.7x | 71.27 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-08-05 (96d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GOOGL | NASDAQ | 284.78 | 0.78 | 3.04 | — | 1.5x | 282.57 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-10-28 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RCL | NYSE | 327.16 | 1.37 | 3.01 | — | 1.3x | 322.73 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-10-27 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GOOG | NASDAQ | 283.93 | 0.78 | 3.00 | — | 1.6x | 281.74 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-10-28 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NVMI | NASDAQ | 313.18 | 11.73 | 2.95 | — | 1.0x | 280.30 | yahoo_chart_daily | 2026-11-05 | US-listed (ADR) | 2026-08-06 (95d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| VICR | NASDAQ | 146.88 | 8.72 | 2.94 | — | 0.4x | 135.10 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-10-20 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| IAG | NYSE | 18.76 | 7.20 | 2.93 | — | 0.9x | 17.50 | yahoo_chart_daily | 2026-11-05 | US-listed (ADR) | 2026-08-06 (95d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AEM | NYSE | 191.57 | 1.33 | 2.87 | — | 1.0x | 189.06 | yahoo_chart_daily | 2026-11-05 | US-listed (ADR) | 2026-10-28 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FPS | NYSE | 19.48 | 6.97 | 2.82 | — | 0.4x | 18.21 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-09-15 (55d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AXON | NASDAQ | 313 | -18.18 | 2.81 | — | 0.9x | 382.56 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-11-05 (4d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SVM | AMEX | 8.9 | 6.71 | 2.81 | — | 0.8x | 8.34 | yahoo_chart_daily | 2026-11-05 | US-listed (ADR) | 2026-08-10 (91d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| HUT | NASDAQ | 52.65 | 14.58 | -2.79 | — | 0.4x | 45.95 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-11-04 (5d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| META | NASDAQ | 610.15 | 0.84 | 2.78 | — | 1.4x | 605.08 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-10-21 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SPCX | NASDAQ | 134.27 | 8.62 | 2.76 | — | 0.8x | 123.62 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-10-20 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NEM | NYSE | 120.91 | 1.00 | 2.76 | — | 1.1x | 119.71 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-10-22 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CENX | NASDAQ | 33.47 | 11.31 | 2.75 | — | 0.8x | 30.07 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-08-06 (95d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ETON | NASDAQ | 56.46 | 19.75 | 2.73 | — | 0.9x | 47.15 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-08-13 (88d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MSFT | NASDAQ | 530.61 | -0.99 | 2.71 | — | 1.7x | 535.93 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-10-28 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RH | NYSE | 130.96 | -4.71 | 2.70 | — | 0.6x | 137.43 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-09-10 (60d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MSDL | NYSE | 13.62 | -3.47 | 2.64 | — | 1.6x | 14.11 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-08-06 (95d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LRCX | NASDAQ | 200.44 | 8.23 | 2.62 | — | 0.6x | 185.20 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-10-21 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BTDR | NASDAQ | 6.015 | 13.28 | -2.58 | — | 0.4x | 5.31 | yahoo_chart_daily | 2026-11-05 | US-listed (ADR) | 2026-08-10 (91d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMAT | NASDAQ | 332.715 | 4.22 | 2.55 | — | 0.6x | 319.25 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-08-13 (88d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ARDT | NYSE | 17.3 | 8.81 | 2.54 | — | 0.7x | 15.90 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-11-04 (5d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CRDO | NASDAQ | 120.51 | 7.28 | 2.53 | — | 0.4x | 112.33 | yahoo_chart_daily | 2026-11-05 | US-listed (ADR) | 2026-09-01 (69d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ATEC | NASDAQ | 7.44 | -4.62 | 2.49 | — | 0.5x | 7.80 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-10-29 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GLP | NYSE | 45.01 | 8.02 | -2.47 | — | 1.2x | 41.67 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-08-07 (94d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ANET | NYSE | 170.8 | 7.31 | 2.45 | — | 0.6x | 159.16 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-11-03 (6d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CYTK | NASDAQ | 53.69 | -3.35 | 2.42 | — | 1.1x | 55.55 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-11-04 (5d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FUN | NYSE | 10 | 8.23 | 2.40 | — | 0.4x | 9.24 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-08-06 (95d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LUNR | NASDAQ | 10.47 | 21.46 | 2.39 | — | 0.4x | 8.62 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-08-13 (88d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RDW | NYSE | 7.21 | 16.48 | 2.36 | — | 0.4x | 6.19 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-11-04 (5d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RKLB | NASDAQ | 53.07 | 15.39 | 2.34 | — | 0.4x | 45.99 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-08-10 (91d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ITW | NYSE | 280.95 | -1.56 | 2.33 | — | 1.9x | 285.41 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-10-27 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| VECO | NASDAQ | 37.19 | 11.85 | 2.31 | — | 0.5x | 33.25 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-11-04 (5d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SEI | NYSE | 57.77 | 14.28 | 2.30 | — | 0.3x | 50.55 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-11-04 (5d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| HWM | NYSE | 205.81 | 2.44 | 2.27 | — | 0.7x | 200.90 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-10-29 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PENG | NASDAQ | 41.83 | 12.39 | 2.22 | — | 0.3x | 37.22 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-10-06 (34d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GE | NYSE | 323.24 | 2.70 | 2.17 | — | 1.0x | 314.73 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-10-20 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NVT | NYSE | 106.22 | 7.97 | 2.15 | — | 0.4x | 98.38 | yahoo_chart_daily | 2026-11-05 | US-listed (ADR) | 2026-10-30 (10d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ETN | NYSE | 341.72 | 4.50 | 2.13 | — | 0.6x | 327.02 | yahoo_chart_daily | 2026-11-05 | US-listed (ADR) | 2026-11-03 (6d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| APPS | NASDAQ | 10.38 | 7.34 | 2.12 | — | 0.4x | 9.67 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-08-04 (97d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| HIMS | NYSE | 26 | 8.06 | -2.12 | — | 0.5x | 24.06 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-08-10 (91d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| DKNG | NASDAQ | 18.51 | -21.30 | -2.11 | — | 0.7x | 23.52 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-08-06 (95d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GEV | NYSE | 774.11 | 0.47 | 2.06 | — | 0.6x | 770.51 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-10-28 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| URGN | NASDAQ | 24.75 | -3.81 | 2.02 | — | 0.6x | 25.73 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-11-04 (5d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BX | NYSE | 119.5 | -0.27 | 2.01 | — | 0.8x | 119.82 | yahoo_chart_daily | 2026-11-05 | US-listed | 2026-10-22 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |

## US — QUIET one-liners

| Ticker | Venue | Chg % | Pre-mkt % | Post-mkt % | Move vs avg daily | Ref close | Ref source | Ref asof | US tradeable | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|
| JMKE | NYSE | -4.04 | 2.00 | — | 1.3x | 19.81 | yahoo_chart_daily | 2026-11-05 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| KSS | NYSE | -3.60 | 2.00 | — | 1.2x | 23.90 | yahoo_chart_daily | 2026-11-05 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| NVTS | NASDAQ | 9.54 | 1.97 | — | 1.6x | 7.86 | yahoo_chart_daily | 2026-11-05 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| LIND | NASDAQ | 7.63 | 1.97 | — | 2.6x | 31.57 | yahoo_chart_daily | 2026-11-05 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| GS | NYSE | -0.36 | 1.95 | — | 0.2x | 868.95 | yahoo_chart_daily | 2026-11-05 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| CLMT | NASDAQ | -8.56 | -1.95 | — | 2.6x | 43.35 | yahoo_chart_daily | 2026-11-05 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| AEHR | NASDAQ | 8.97 | 1.92 | — | 1.2x | 49.16 | yahoo_chart_daily | 2026-11-05 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| COHR | NYSE | 13.58 | 1.91 | — | 2.4x | 169.76 | yahoo_chart_daily | 2026-11-05 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| GLW | NYSE | 2.61 | 1.91 | — | 0.8x | 103.43 | yahoo_chart_daily | 2026-11-05 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| LEU | NYSE | 17.49 | 1.91 | — | 3.4x | 89.03 | yahoo_chart_daily | 2026-11-05 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| AZN | NYSE | -0.22 | 1.89 | — | 0.1x | 186.85 | yahoo_chart_daily | 2026-11-05 | US-listed (ADR) | — | no catalyst lookup (outside the per-run budget) |
| CAT | NYSE | 0.90 | 1.89 | — | 0.3x | 553.64 | yahoo_chart_daily | 2026-11-05 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| ICHR | NASDAQ | 10.47 | 1.89 | — | 1.8x | 28.03 | yahoo_chart_daily | 2026-11-05 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| MRNA | NASDAQ | 5.27 | 1.89 | — | 1.1x | 241.46 | yahoo_chart_daily | 2026-11-05 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| ARHS | NASDAQ | 9.66 | 1.86 | — | 2.6x | 12.94 | yahoo_chart_daily | 2026-11-05 | US-listed | — | no catalyst lookup (outside the per-run budget) |

## EU/UK — Headline table

| Ticker | Market | Venue | Close | Chg % | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| KNOS | uk | LSE | 1084.489 | -11.83 | GBX | 9.2x | 1230.00 | yahoo_chart_daily | 2026-11-06 | none | 2026-11-09 | Y | H1 FY26 interim results (Nov 9): revenue +37% to GBP 268.8M but group gross margin down to 43.1% from 48.0% as revenue through contractors and partners rose to GBP 49.2M, adjusted pre-tax profit +30% to GBP 41.7M, and second-half guidance held only in line with expectations rather than upgraded |
| AUTO | norway | OSL | 15.63 | +10.46 | NOK | 8.0x | 14.15 | yahoo_chart_daily | 2026-11-06 | none | 2026-11-05 | Y | AutoStore Holdings Q3 2026 (Nov 5): revenue +38% YoY to $192M, record Q3 order intake of $178M (+17%), FY26 revenue guidance raised to about $750M alongside the Logiqs acquisition |
| BAMI | italy | MIL | 14.84 | +10.38 | EUR | 5.5x | 13.45 | yahoo_chart_daily | 2026-11-06 | none | 2026-08-05 | N | Credit Agricole proposed combining its Italian subsidiary with Banco BPM at a 20% valuation premium plus a EUR 1bn extraordinary dividend; the proposal has been submitted for evaluation by Banco BPM's board - a merger proposal, not an earnings event |
| KOMPL | norway | OSL | 6.54 | +7.21 | NOK | 2.9x | 6.10 | yahoo_chart_daily | 2026-11-06 | none | 2026-10-22 | — | no catalyst lookup (outside the per-run budget) |
| 1SXP | germany | XETR | 20.2 | -7.13 | EUR | 4.8x | 21.75 | yahoo_chart_daily | 2026-11-06 | none | 2026-08-12 | — | no catalyst lookup (outside the per-run budget) |
| ATS | austria | VIE | 113.2 | +6.99 | EUR | 1.2x | 105.80 | yahoo_chart_daily | 2026-11-06 | none | 2026-08-04 | — | no catalyst lookup (outside the per-run budget) |
| TBCG | uk | LSE | 5160 | +6.26 | GBX | 3.1x | 4856.00 | yahoo_chart_daily | 2026-11-06 | none | 2026-08-06 | — | no catalyst lookup (outside the per-run budget) |
| OHB | germany | XETR | 203 | +6.17 | EUR | 1.2x | 191.20 | yahoo_chart_daily | 2026-11-06 | ADR (OTC:OHBTF) | 2026-08-06 | — | no catalyst lookup (outside the per-run budget) |
| VICO | sweden | OMXSTO | 10.84 | +6.07 | SEK | 2.4x | 10.22 | yahoo_chart_daily | 2026-11-06 | none | 2026-08-21 | — | no catalyst lookup (outside the per-run budget) |
| RPI | uk | LSE | 522.5 | +6.03 | GBX | 2.0x | 492.80 | yahoo_chart_daily | 2026-11-06 | none | 2026-09-24 | — | no catalyst lookup (outside the per-run budget) |
| SF | sweden | OMXSTO | 6.41 | +5.95 | SEK | 2.3x | 6.05 | yahoo_chart_daily | 2026-11-06 | none | 2026-10-23 | — | no catalyst lookup (outside the per-run budget) |
| HUNT | norway | OSL | 16.7 | +5.83 | NOK | 1.6x | 15.78 | yahoo_chart_daily | 2026-11-06 | none | 2024-05-30 | — | no catalyst lookup (outside the per-run budget) |
| PHO | norway | OSL | 42.1 | -5.61 | NOK | 4.8x | 44.60 | yahoo_chart_daily | 2026-11-06 | none | 2026-10-28 | — | no catalyst lookup (outside the per-run budget) |
| UCG | italy | MIL | 81.06 | +5.55 | EUR | 3.6x | 76.80 | yahoo_chart_daily | 2026-11-06 | none | 2026-11-08 | — | no catalyst lookup (outside the per-run budget) |
| VISC | sweden | OMXSTO | 17.98 | +5.52 | SEK | 2.0x | 17.04 | yahoo_chart_daily | 2026-11-06 | none | 2026-08-13 | — | no catalyst lookup (outside the per-run budget) |
| CBRAIN | denmark | OMXCOP | 107 | -5.48 | DKK | 1.4x | 113.20 | yahoo_chart_daily | 2026-11-06 | none | 2026-08-20 | — | no catalyst lookup (outside the per-run budget) |
| HAYPP | sweden | OMXSTO | 154.8 | +5.45 | SEK | 2.6x | 146.80 | yahoo_chart_daily | 2026-11-06 | none | 2026-08-12 | — | no catalyst lookup (outside the per-run budget) |
| VH2 | germany | XETR | 70.6 | +5.29 | EUR | 1.9x | 67.05 | yahoo_chart_daily | 2026-11-06 | none | 2026-08-13 | — | no catalyst lookup (outside the per-run budget) |
| ANTO | uk | LSE | 3274 | +5.17 | GBX | 1.9x | 3113.00 | yahoo_chart_daily | 2026-11-06 | none | 2026-08-13 | — | no catalyst lookup (outside the per-run budget) |
| WIZZ | uk | LSE | 1116.5 | +5.13 | GBX | 2.6x | 1062.00 | yahoo_chart_daily | 2026-11-06 | ADR (OTC:WZZZY) | 2025-11-13 | — | no catalyst lookup (outside the per-run budget) |
| HOC | uk | LSE | 512 | +5.05 | GBX | 1.7x | 487.40 | yahoo_chart_daily | 2026-11-06 | none | 2026-08-26 | — | no catalyst lookup (outside the per-run budget) |
| ALM | spain | BME | 10.66 | -4.99 | EUR | 4.6x | 11.22 | yahoo_chart_daily | 2026-11-06 | none | 2026-07-24 | — | no catalyst lookup (outside the per-run budget) |
| DEZ | germany | XETR | 9.705 | +4.92 | EUR | 2.2x | 9.25 | yahoo_chart_daily | 2026-11-06 | none | 2026-08-06 | — | no catalyst lookup (outside the per-run budget) |
| EDV | uk | LSE | 4293 | +4.86 | GBX | 2.0x | 4094.00 | yahoo_chart_daily | 2026-11-06 | none | 2026-07-30 | — | no catalyst lookup (outside the per-run budget) |
| HEX | norway | OSL | 12.35 | +4.84 | NOK | 2.3x | 11.78 | yahoo_chart_daily | 2026-11-06 | none | 2026-08-06 | — | no catalyst lookup (outside the per-run budget) |
| ENO | spain | BME | 30.45 | +4.82 | EUR | 2.5x | 29.05 | yahoo_chart_daily | 2026-11-06 | none | 2026-07-27 | — | no catalyst lookup (outside the per-run budget) |
| ANIM | italy | MIL | 7.19 | +4.81 | EUR | 5.2x | 6.86 | yahoo_chart_daily | 2026-11-06 | none | 2026-11-04 | — | no catalyst lookup (outside the per-run budget) |
| IFX | germany | XETR | 47.915 | +4.72 | EUR | 1.7x | 45.76 | yahoo_chart_daily | 2026-11-06 | none | 2026-08-05 | — | no catalyst lookup (outside the per-run budget) |
| SCATC | norway | OSL | 90.95 | +4.72 | NOK | 1.6x | 86.85 | yahoo_chart_daily | 2026-11-06 | none | 2026-10-30 | — | no catalyst lookup (outside the per-run budget) |
| AAL | uk | LSE | 3872 | +4.62 | GBX | 2.3x | 3701.00 | yahoo_chart_daily | 2026-11-06 | none | 2026-07-30 | — | no catalyst lookup (outside the per-run budget) |

## AU (ASX) — Headline table

| Ticker | Venue | Close | Chg % | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| VNT | ASX | 4.8 | -16.23 | AUD | 8.9x | 5.73 | yahoo_chart_daily | 2026-11-05 | none | 2026-08-23 | Y | FY26 outlook and strategy announcement (Nov 9, 8:13am AEDT): H2 FY26 group revenue expected below the prior year on challenging Telecommunications and Energy markets, NPATA growth guidance held at 7-10% excluding about A$30M of one-offs, A$60M annualised cost savings targeted by Dec 2027, fewer operating sectors and a new CEO from Dec 1 |
| SLX | ASX | 3.33 | +12.12 | AUD | 2.4x | 2.97 | yahoo_chart_daily | 2026-11-05 | none | 2026-08-27 | N | no fresh catalyst found - uranium mid-cap sector rally (SLX +12.12%, BOE +10.71%, DYL +10.60%, PDN +10.86%); no ASX announcement was lodged and no published reason was identified |
| DNL | ASX | 3.4 | -10.99 | AUD | 5.8x | 3.82 | yahoo_chart_daily | 2026-11-05 | none | 2026-05-10 | — | no catalyst lookup (outside the per-run budget) |
| PDN | ASX | 8.27 | +10.86 | AUD | 2.7x | 7.46 | yahoo_chart_daily | 2026-11-05 | none | 2026-11-04 | — | no catalyst lookup (outside the per-run budget) |
| BOE | ASX | 1.55 | +10.71 | AUD | 2.3x | 1.40 | yahoo_chart_daily | 2026-11-05 | none | 2026-08-26 | — | no catalyst lookup (outside the per-run budget) |
| CYL | ASX | 4.44 | +8.82 | AUD | 1.6x | 4.08 | yahoo_chart_daily | 2026-11-05 | none | 2026-08-31 | — | no catalyst lookup (outside the per-run budget) |
| SRL | ASX | 12.59 | +8.72 | AUD | 1.5x | 11.58 | yahoo_chart_daily | 2026-11-05 | none | 2026-09-07 | — | no catalyst lookup (outside the per-run budget) |
| FFM | ASX | 1.425 | +7.95 | AUD | 1.8x | 1.32 | yahoo_chart_daily | 2026-11-05 | none | 2026-09-17 | — | no catalyst lookup (outside the per-run budget) |
| WA1 | ASX | 8.59 | +7.91 | AUD | 1.5x | 7.96 | yahoo_chart_daily | 2026-11-05 | none | 2026-09-18 | — | no catalyst lookup (outside the per-run budget) |
| ALK | ASX | 1.85 | +7.25 | AUD | 1.9x | 1.73 | yahoo_chart_daily | 2026-11-05 | none | 2026-10-23 | — | no catalyst lookup (outside the per-run budget) |
| PNR | ASX | 3.28 | +7.19 | AUD | 1.7x | 3.06 | yahoo_chart_daily | 2026-11-05 | none | 2026-09-28 | — | no catalyst lookup (outside the per-run budget) |
| ELV | ASX | 3.58 | +7.19 | AUD | 1.5x | 3.34 | yahoo_chart_daily | 2026-11-05 | none | 2026-08-27 | — | no catalyst lookup (outside the per-run budget) |
| LYC | ASX | 13.15 | +6.82 | AUD | 1.8x | 12.31 | yahoo_chart_daily | 2026-11-05 | none | 2026-08-25 | — | no catalyst lookup (outside the per-run budget) |
| EOS | ASX | 7.48 | +6.55 | AUD | 1.6x | 7.02 | yahoo_chart_daily | 2026-11-05 | none | 2026-08-24 | — | no catalyst lookup (outside the per-run budget) |
| GMD | ASX | 7.49 | +6.39 | AUD | 1.8x | 7.04 | yahoo_chart_daily | 2026-11-05 | none | 2026-08-20 | — | no catalyst lookup (outside the per-run budget) |
| OBM | ASX | 1.53 | +6.25 | AUD | 1.5x | 1.44 | yahoo_chart_daily | 2026-11-05 | none | 2026-08-25 | — | no catalyst lookup (outside the per-run budget) |
| WBT | ASX | 2.27 | +6.07 | AUD | 1.2x | 2.14 | yahoo_chart_daily | 2026-11-05 | none | 2026-08-28 | — | no catalyst lookup (outside the per-run budget) |
| PDI | ASX | 4.77 | +6.00 | AUD | 1.3x | 4.50 | yahoo_chart_daily | 2026-11-05 | ADR (OTC:PDIYF) | 2026-09-30 | — | no catalyst lookup (outside the per-run budget) |
| RMS | ASX | 3.89 | +5.99 | AUD | 2.0x | 3.67 | yahoo_chart_daily | 2026-11-05 | none | 2026-08-20 | — | no catalyst lookup (outside the per-run budget) |
| VAU | ASX | 6.19 | +5.99 | AUD | 1.9x | 5.84 | yahoo_chart_daily | 2026-11-05 | none | 2026-08-20 | — | no catalyst lookup (outside the per-run budget) |
| MLX | ASX | 1.61 | +5.92 | AUD | 1.2x | 1.52 | yahoo_chart_daily | 2026-11-05 | none | 2026-08-27 | — | no catalyst lookup (outside the per-run budget) |
| DVP | ASX | 3.76 | +5.92 | AUD | 1.5x | 3.55 | yahoo_chart_daily | 2026-11-05 | none | 2026-03-08 | — | no catalyst lookup (outside the per-run budget) |
| PYC | ASX | 1.99 | +5.85 | AUD | 1.6x | 1.88 | yahoo_chart_daily | 2026-11-05 | ADR (OTC:PYCXF) | 2026-08-28 | — | no catalyst lookup (outside the per-run budget) |
| BMN | ASX | 3.69 | +5.73 | AUD | 1.5x | 3.49 | yahoo_chart_daily | 2026-11-05 | none | 2026-09-23 | — | no catalyst lookup (outside the per-run budget) |
| SFR | ASX | 20.19 | +5.65 | AUD | 1.8x | 19.11 | yahoo_chart_daily | 2026-11-05 | none | 2026-08-25 | — | no catalyst lookup (outside the per-run budget) |

## Source health

- scanner_calls: 41 | scanner_errors: 0
- pipeline_version: 2026-11-06.2
- et_clock: zoneinfo America/New_York (DST-aware; a fixed UTC-4 mislabels every winter fire)
- premarket_window: 04:00-09:30 ET, resolved with zoneinfo (09:00-14:30 UTC in winter, 08:00-13:30 UTC in summer)
- session_selection: by DATE and order, never by a modal time-of-day. Yahoo stamps a daily bar at the session open, so the ET stamp of the SAME session shifts by one hour across a DST boundary; a modal filter kept the OLDER bars and discarded the NEWEST ones, which rolled the base back to the prior-prior session (66 US + 21 ASX rows lost on 2026-11-03, 24 of 25 ASX rows lost on 2026-11-04).
- yahoo_calls: 163 | yahoo_429: 0 | yahoo_errors: 0
- reference_close (screener vs Yahoo, resolved BEFORE the tables were built): agree=153 mismatch=0 unverified=0 stale_reference=0
  method: the screener's implied reference close (close / (1 + change/100)) is compared
  with Yahoo's own reference close. A match proves the move was measured against the
  TRUE prior close; a mismatch means the row sits on a STALE reference (phantom move).
  Coverage: every row of the US headline, US QUIET, EU/UK and ASX tables is checked.
  Yahoo bar mode: {"closed": 123, "live": 30} (closed = last completed session bar;
  live = in-progress EU/UK session bar, which is what a weekday 08:00 ET EU move needs)
  live drift between the screener snapshot and the later Yahoo print: median=0.00pp max=0.71pp (expected on a live market)
- rows_dropped_stale_ref: 0 (rows whose screener-implied reference close disagreed with Yahoo's by more than 0.5%; they are dropped, not published)
- rows_dropped_unresolved_ref: 0 (rows whose reference close could not be resolved from Yahoo at all - the base of the move is unverifiable, so the row is dropped rather than published with a '—' base)
- us_premarket_check (Yahoo 1-min pre/post feed vs the screener pre-market column, base = the IMMEDIATELY prior session's close): checked=9 within_1pp=2 within_3pp=7 unavailable=1
  us_premarket outliers (>3pp; thin pre-market books, not a screener error): [{"symbol": "VIR", "tv": 15.093, "yahoo": 10.512, "delta": 4.581, "yahoo_asof": "08:06"}, {"symbol": "REF", "tv": 10.083, "yahoo": 0.831, "delta": 9.252, "yahoo_asof": "07:51"}]
- markets_with_lt5_rows: ['uk:less=2', 'france:egreater=4', 'france:less=0', 'netherlands:egreater=3', 'netherlands:less=0', 'belgium:egreater=1', 'belgium:less=0', 'portugal:egreater=0', 'portugal:less=0', 'ireland:egreater=1', 'ireland:less=0', 'italy:less=0', 'switzerland:egreater=4', 'switzerland:less=0', 'spain:less=1', 'sweden:less=2', 'norway:less=4', 'denmark:less=1', 'finland:egreater=1', 'finland:less=0', 'poland:egreater=4', 'poland:less=2', 'austria:less=0', 'greece:egreater=0', 'greece:less=0']
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
- bod_no_extended_hours: 131 (deferred to the next scan; not in the headline table)
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
  1. yahoo_premarket_check.unavailable — CECO: Yahoo's 1-minute pre-market feed returned no usable print

## Audit line

`earnings-reaction target=earnings-reactions:2026-11-09 candidates=577 amc_reactions=0 pre_gaps=83 eu_reactions=30 asx_reactions=25 catalyst_lookups=10 bod=131 rows_dropped_stale_ref=0 rows_dropped_unresolved_ref=0 degraded_sources=1`
