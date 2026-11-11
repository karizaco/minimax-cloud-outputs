# Earnings reaction scanner — 2026-11-11

- Cron: `0 8 * * 1-5` America/New_York (weekdays, 08:00 ET)
- Fire time (ET): 2026-11-11 08:29:18 Wed
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

- 0 AMC reactions, 120 pre-market gaps, 109 without extended-hours data; 29 EU/UK and 4 ASX movers, 17 APAC/Gulf movers.
- Biggest US extended-hours move: NBIS PRE_GAP (13.11%).
- Biggest EU/UK move: BICO (-30.12%, sweden).
- Biggest ASX move: IEL (+16.29%).
- Biggest APAC/Gulf move: HRME (+34.15%, indonesia).
- 2 of the 29 EU/UK rows are SETTLED and 27 are LIVE (mid-session). The 12:15 ET settlement pass publishes where those
  live moves actually closed.
- EU/AU/APAC earnings-driven tagging is keyword-based on headlines (best-effort). A row
  whose lookup was not performed carries NO verdict — only a researched row does.

## Actionable read

- **Move vs this name's own history.** The `Move vs avg daily` column divides the
  reaction by the name's own mean absolute daily move over its last
  20 completed sessions. A -27% move in a name that averages +-3% is a
  different event from a -8% move in a name that averages +-7%.
- **US-listed and tradeable vs foreign-only.** 135 published US rows are on a
  US venue; 2 more foreign reactions have a US ADR line
  (the `US tradeable` column carries the ticker); 31 are foreign-only and
  cannot be bought directly by a US reader.
- **Not yet fully priced — US (hypothesis, not a recommendation).**
  ATRO — -11.82%, 3.32% mean absolute daily move over the last 20 completed sessions, 3.6x that average, reference close 58.99 dated 2026-11-09, US access: US-listed, the move now (-11.82%) is larger than the move it follows (+5.10%); the reaction is still being repriced. Hypothesis only: this artifact states no
  direction and no trade.
- **Not yet fully priced — EU/UK (hypothesis, not a recommendation).**
  BICO — -30.12%, 1.38% mean absolute daily move over the last 20 completed sessions, 21.9x that average, reference close 24.70 dated 2026-11-10, US access: ADR (OTC:CLLKF), the move now (-30.12%) is larger than the move it follows (+4.00%); the reaction is still being repriced. Hypothesis only: this artifact states no
  direction and no trade.
- **Not yet fully priced — AU (ASX) (hypothesis, not a recommendation).**
  IEL — +16.29%, 1.69% mean absolute daily move over the last 20 completed sessions, 9.7x that average, reference close 2.21 dated 2026-11-09, US access: none, the move now (+16.29%) is larger than the move it follows (+0.46%); the reaction is still being repriced. Hypothesis only: this artifact states no
  direction and no trade.

## US — Headline table

| Ticker | Venue | Close | Chg % | Pre-mkt % | Post-mkt % | Move vs avg daily | Ref close | Ref source | Ref asof | US tradeable | Last earnings | Tag | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NBIS | NASDAQ | 134 | -5.27 | 13.11 | — | 2.1x | 141.45 | yahoo_chart_daily | 2026-11-09 | US-listed (ADR) | 2026-08-12 (91d ago) | PRE_GAP | N | CoreWeave's Q3 beat (sales +168% to $3.66bn, backlog $133bn) and raised FY26 outlook lifted the neocloud complex overnight, CRWV +15% and NBIS +11% pre-market; NBIS reports Q3 on 12 Nov |
| ATRO | NASDAQ | 62 | 5.10 | -11.82 | — | 3.6x | 58.99 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-11-10 (1d ago) | PRE_GAP | Y | Q3 FY2026 results released 10 Nov after the close: record sales $271.7m (+28.5% y/y), operating income doubled to $54m, adjusted EBITDA $59.3m, aerospace backlog a record $670m - but Q4 revenue guidance of $255-275m came in below the $273.7m consensus, so shares fell in pre-market |
| COHR | NYSE | 214.66 | -4.68 | 9.66 | — | 1.6x | 225.19 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-11-04 (7d ago) | PRE_GAP | N | no fresh catalyst found (no Coherent release; the pre-market bid tracked the AI and optical complex - Lumentum +9% pre-market - after CoreWeave's Q3 beat and the Microsoft transceiver-ban story) |
| NN | NASDAQ | 8.4 | -5.83 | 9.64 | — | 1.7x | 8.92 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-11-10 (1d ago) | PRE_GAP | Y | NextNav Q3 2026 results released 10 Nov after the close: revenue $1.582m against a $0.993m consensus, a net loss of $4.2m (EPS -$0.02 vs -$0.12 est) partly offset by a $13m non-cash warrant-liability gain, about $290m of cash and investments and debt-free, with the FCC's P&T Notice of Proposed Rulemaking still in interagency review and the proposed SpaceX purchase of low-band spectrum cited as a scarcity precedent |
| CIFR | NASDAQ | 6.53 | -4.11 | 9.49 | — | 1.2x | 6.81 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-11-02 (9d ago) | PRE_GAP | N | Jefferies cut the price target to $10 from $12 (Buy kept) in an AI data-centre re-rating, and the pre-market gain came from CoreWeave's beat lifting AI-infrastructure names; no company release |
| AXTI | NASDAQ | 39.31 | -8.39 | 9.47 | — | 1.1x | 42.91 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-10-29 (13d ago) | PRE_GAP | N | AI-optical complex bid after CoreWeave's Q3 beat, with the attached headline being Reuters' report that Microsoft is pressing the Trump administration to scrap the planned Chinese optical-transceiver import ban; no AXT-specific release |
| MRVL | NASDAQ | 154.39 | -0.14 | 8.93 | — | 1.5x | 154.60 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-08-27 (76d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| STX | NASDAQ | 501.62 | -0.89 | 8.83 | — | 1.8x | 506.14 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-10-27 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FPS | NYSE | 21.48 | -4.96 | 8.01 | — | 1.0x | 22.60 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-09-15 (57d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| EROC | NYSE | 7.87 | -4.61 | 8.01 | — | 1.1x | 8.25 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-08-11 (92d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| WDC | NASDAQ | 289.2 | -0.20 | 8.00 | — | 1.5x | 289.78 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-10-22 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SNDK | NASDAQ | 859.99 | -2.99 | 7.88 | — | 1.4x | 886.51 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-10-29 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FUN | NYSE | 10.16 | -5.58 | 7.78 | — | 1.4x | 10.76 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-11-05 (6d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BE | NYSE | 185.42 | -4.36 | 7.32 | — | 1.1x | 193.88 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-10-22 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CORZ | NASDAQ | 13.13 | 3.22 | 7.31 | — | 1.3x | 12.72 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-11-05 (6d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| DELL | NYSE | 334.38 | -3.44 | 7.30 | — | 1.4x | 346.31 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-09-01 (71d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TTMI | NASDAQ | 72.23 | -4.12 | 7.16 | — | 0.9x | 75.33 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-10-22 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| OKLO | NYSE | 25.09 | -6.52 | 6.98 | — | 1.3x | 26.84 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-11-06 (5d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| IREN | NASDAQ | 19.73 | -7.85 | 6.96 | — | 0.9x | 21.41 | yahoo_chart_daily | 2026-11-09 | US-listed (ADR) | 2026-11-05 (6d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AAOI | NASDAQ | 48.32 | -7.26 | 6.73 | — | 1.0x | 52.10 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-11-05 (6d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GLW | NYSE | 112.13 | -3.29 | 6.66 | — | 1.8x | 115.95 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-10-27 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MU | NASDAQ | 725.11 | -1.10 | 6.49 | — | 1.4x | 733.15 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-09-30 (42d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CLSK | NASDAQ | 6.57 | -4.92 | 6.24 | — | 0.9x | 6.91 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-08-06 (97d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FN | NYSE | 348.52 | -4.76 | 6.23 | — | 1.0x | 365.94 | yahoo_chart_daily | 2026-11-09 | US-listed (ADR) | 2026-11-02 (9d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| KLAC | NASDAQ | 152.99 | 1.06 | 6.15 | — | 1.4x | 151.38 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-10-28 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| INTC | NASDAQ | 58.13 | -2.09 | 5.98 | — | 1.1x | 59.37 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-10-29 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SMR | NYSE | 5.22 | -4.04 | 5.84 | — | 1.2x | 5.44 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-11-05 (6d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ABSI | NASDAQ | 9.97 | -7.69 | 5.82 | — | 0.9x | 10.80 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-08-11 (92d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SANM | NASDAQ | 155.43 | 3.87 | 5.78 | — | 1.2x | 149.64 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-11-09 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LRCX | NASDAQ | 222.39 | 0.49 | 5.76 | — | 1.2x | 221.31 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-10-21 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| INIO | NASDAQ | 13.77 | -7.65 | 5.74 | — | 1.0x | 14.91 | yahoo_chart_daily | 2026-11-09 | US-listed (ADR) | 2026-10-27 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ONDS | NASDAQ | 5.57 | -6.70 | 5.57 | — | 1.0x | 5.97 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-08-13 (90d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GEV | NYSE | 797.04 | -3.89 | 5.52 | — | 1.4x | 829.34 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-10-28 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMAT | NASDAQ | 372.53 | 0.53 | 5.49 | — | 1.3x | 370.55 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-08-13 (90d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMD | NASDAQ | 515.21 | 1.30 | 5.48 | — | 1.0x | 508.58 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-11-03 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ORCL | NYSE | 117.98 | -1.51 | 5.15 | — | 1.4x | 119.79 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-09-10 (62d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| INOD | NASDAQ | 35.05 | -5.17 | 5.04 | — | 1.0x | 36.96 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-11-05 (6d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TDW | NYSE | 73.98 | 4.11 | 4.93 | — | 1.7x | 71.06 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-11-09 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ANET | NYSE | 185.02 | -0.62 | 4.89 | — | 1.1x | 186.17 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-11-03 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MTZ | NYSE | 180.84 | -4.34 | 4.79 | — | 1.2x | 189.05 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-10-29 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RGC | NASDAQ | 5.23 | -7.02 | 4.78 | — | 0.7x | 5.62 | yahoo_chart_daily | 2026-11-09 | US-listed (ADR) | — | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| UEC | AMEX | 7.17 | -5.91 | 4.74 | — | 1.1x | 7.62 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-09-29 (43d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PWR | NYSE | 583.14 | -1.41 | 4.57 | — | 1.0x | 591.48 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-10-29 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ACCV | NASDAQ | 10.68 | -11.55 | 4.49 | — | 0.6x | 12.08 | yahoo_chart_daily | 2026-11-09 | US-listed | — | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LEU | NYSE | 109.87 | -6.37 | 4.47 | — | 0.8x | 117.34 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-11-04 (7d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| USAR | NASDAQ | 7.92 | -9.59 | 4.29 | — | 0.7x | 8.76 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-11-09 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AVGO | NASDAQ | 331.98 | 3.91 | 4.10 | — | 1.3x | 319.48 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-09-02 (70d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MARA | NASDAQ | 7.34 | 10.54 | 4.09 | — | 0.7x | 6.64 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-11-09 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMRC | NYSE | 27.62 | 23.03 | 3.98 | — | 0.7x | 22.45 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-11-09 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| UUUU | AMEX | 6.74 | -7.80 | 3.86 | — | 1.0x | 7.31 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-11-04 (7d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| IE | AMEX | 7.66 | -7.26 | 3.79 | — | 0.8x | 8.26 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-11-05 (6d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| APH | NYSE | 79.95 | -0.94 | 3.78 | — | 1.1x | 80.71 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-10-28 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CAI | NASDAQ | 24.43 | -4.46 | 3.76 | — | 0.9x | 25.57 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-11-04 (7d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ETN | NYSE | 354.22 | -1.41 | 3.75 | — | 1.1x | 359.30 | yahoo_chart_daily | 2026-11-09 | US-listed (ADR) | 2026-11-03 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ELE | NASDAQ | 16.09 | -4.34 | -3.67 | — | 1.3x | 16.82 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-11-10 (1d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NVDA | NASDAQ | 168.89 | -5.47 | 3.57 | — | 1.3x | 178.67 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-08-26 (77d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NTSK | NASDAQ | 21.44 | -4.67 | 3.54 | — | 0.8x | 22.49 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-09-02 (70d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| QLYS | NASDAQ | 175.11 | -13.51 | 3.36 | — | 0.8x | 202.46 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-11-09 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| QBTS | NASDAQ | 10.48 | -8.63 | 3.35 | — | 0.7x | 11.47 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-11-10 (1d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FIGR | NASDAQ | 23.34 | -4.81 | 3.34 | — | 0.7x | 24.52 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-08-13 (90d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BAND | NASDAQ | 43.57 | 4.09 | 3.33 | — | 0.5x | 41.86 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-10-29 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| QCOM | NASDAQ | 173.53 | 1.20 | 3.33 | — | 1.0x | 171.47 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-11-04 (7d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SNOW | NYSE | 295.76 | 1.59 | 3.22 | — | 1.0x | 291.14 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-09-02 (70d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SHLS | NASDAQ | 8.13 | -6.77 | 3.19 | — | 0.6x | 8.72 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-11-04 (7d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CAT | NYSE | 584.57 | -2.39 | 3.10 | — | 1.1x | 598.88 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-10-29 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TENB | NASDAQ | 41.96 | -3.92 | 3.10 | — | 0.8x | 43.67 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-10-28 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TXN | NASDAQ | 300.52 | 1.62 | 3.09 | — | 1.3x | 295.73 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-10-21 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| EQPT | NASDAQ | 13.535 | -16.50 | 3.07 | — | 0.5x | 16.21 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-11-09 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FTAI | NASDAQ | 188 | -5.45 | 3.06 | — | 0.6x | 198.83 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-10-29 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TEM | NASDAQ | 80.54 | -4.62 | 3.05 | — | 0.6x | 84.44 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-11-02 (9d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| QUBT | NASDAQ | 6.3 | -8.16 | 3.04 | — | 0.7x | 6.86 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-11-09 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CRWD | NASDAQ | 225.76 | -1.23 | 3.03 | — | 1.0x | 228.58 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-08-26 (77d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SECZ | NYSE | 8.53 | 22.38 | 3.01 | — | 0.5x | 6.97 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-11-09 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ASTS | NASDAQ | 33.69 | -8.67 | 3.00 | — | 0.5x | 36.89 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-11-09 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MRCY | NASDAQ | 83.58 | 4.97 | 2.97 | — | 0.7x | 79.62 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-11-10 (1d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RGTI | NASDAQ | 12.15 | -6.39 | 2.96 | — | 0.6x | 12.98 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-11-10 (1d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PS | NYSE | 44.2 | -14.92 | 2.94 | — | 0.8x | 51.95 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-11-02 (9d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LIME | NASDAQ | 17.51 | -3.90 | 2.91 | — | 0.5x | 18.22 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-11-03 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NTLA | NASDAQ | 11.17 | -7.76 | 2.86 | — | 0.7x | 12.11 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-11-05 (6d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NEWP | AMEX | 5.6 | -8.35 | 2.86 | — | 0.6x | 6.11 | yahoo_chart_daily | 2026-11-09 | US-listed (ADR) | 2026-11-03 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MBLY | NASDAQ | 5.63 | -3.92 | 2.84 | — | 0.7x | 5.86 | yahoo_chart_daily | 2026-11-09 | US-listed (ADR) | 2026-10-29 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CRSP | NASDAQ | 45.15 | -9.77 | 2.77 | — | 1.0x | 50.04 | yahoo_chart_daily | 2026-11-09 | US-listed (ADR) | 2026-11-02 (9d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ADI | NASDAQ | 393.3 | -0.34 | 2.72 | — | 1.0x | 394.66 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-08-19 (84d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ALM | NASDAQ | 8.14 | -7.24 | 2.70 | — | 0.7x | 8.78 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-08-11 (92d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NET | NYSE | 305.8 | 4.10 | 2.68 | — | 0.6x | 293.75 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-11-05 (6d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NXE | NYSE | 8.33 | -4.80 | 2.64 | — | 0.9x | 8.75 | yahoo_chart_daily | 2026-11-09 | US-listed (ADR) | 2026-11-09 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| VOYG | NYSE | 29.02 | 4.01 | 2.62 | — | 0.5x | 27.90 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-11-02 (9d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AYA | NASDAQ | 25.17 | -5.98 | 2.61 | — | 0.7x | 26.77 | yahoo_chart_daily | 2026-11-09 | US-listed (ADR) | 2026-08-13 (90d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ALB | NYSE | 94.93 | -4.23 | 2.60 | — | 1.3x | 99.12 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-11-04 (7d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ETOR | NASDAQ | 21.56 | -7.55 | 2.58 | — | 1.4x | 23.32 | yahoo_chart_daily | 2026-11-09 | US-listed (ADR) | 2026-11-10 (1d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| IEP | NASDAQ | 5.08 | 4.74 | 2.56 | — | 1.0x | 4.85 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-11-03 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| HYMC | NASDAQ | 18.87 | -11.28 | 2.54 | — | 0.5x | 21.27 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-10-27 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ROAD | NASDAQ | 81.64 | -4.29 | 2.49 | — | 0.7x | 85.30 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-08-07 (96d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SEDG | NASDAQ | 25.86 | -6.51 | 2.47 | — | 0.6x | 27.66 | yahoo_chart_daily | 2026-11-09 | US-listed (ADR) | 2026-11-04 (7d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ENPH | NASDAQ | 27.64 | -4.95 | 2.46 | — | 0.6x | 29.08 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-10-27 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| WPM | NYSE | 136.62 | -5.09 | 2.45 | — | 0.8x | 143.94 | yahoo_chart_daily | 2026-11-09 | US-listed (ADR) | 2026-11-05 (6d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| XP | NASDAQ | 14.8 | -4.33 | 2.40 | — | 0.4x | 15.47 | yahoo_chart_daily | 2026-11-09 | US-listed (ADR) | 2026-08-17 (86d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FROG | NASDAQ | 103.55 | -4.28 | 2.37 | — | 0.4x | 108.18 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-11-05 (6d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SVM | AMEX | 9.31 | -4.32 | 2.36 | — | 0.6x | 9.73 | yahoo_chart_daily | 2026-11-09 | US-listed (ADR) | 2026-11-05 (6d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PLTR | NASDAQ | 168.82 | -0.22 | 2.36 | — | 0.8x | 169.20 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-11-02 (9d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PANW | NASDAQ | 326.36 | -1.37 | 2.34 | — | 0.7x | 330.89 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-09-01 (71d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| QNT | NASDAQ | 43 | 7.39 | 2.33 | — | 0.4x | 40.04 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-11-05 (6d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NXT | NASDAQ | 99.82 | -4.83 | 2.32 | — | 0.6x | 104.89 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-10-28 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SA | NYSE | 26.04 | -6.77 | 2.30 | — | 0.8x | 27.93 | yahoo_chart_daily | 2026-11-09 | US-listed (ADR) | 2026-08-13 (90d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PGY | NASDAQ | 17.21 | -5.39 | 2.27 | — | 0.6x | 18.19 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-10-29 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PBF | NYSE | 65.91 | -5.23 | 2.26 | — | 0.6x | 69.55 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-10-29 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| JOBY | NYSE | 5.92 | -4.21 | 2.20 | — | 0.7x | 6.18 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-11-04 (7d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| IBKR | NASDAQ | 77.59 | 0.03 | 2.17 | — | 0.8x | 77.57 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-10-15 (27d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CRK | NYSE | 14.42 | 4.72 | 2.15 | — | 1.0x | 13.77 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-11-04 (7d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FCX | NYSE | 60.31 | -3.24 | 2.14 | — | 1.0x | 62.33 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-10-27 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AAON | NASDAQ | 75.01 | 19.31 | 2.12 | — | 0.4x | 62.87 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-11-09 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AUGO | NASDAQ | 81.31 | -6.53 | 2.08 | — | 0.4x | 86.99 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-11-05 (6d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| XXI | NYSE | 5.32 | -4.49 | 2.07 | — | 0.7x | 5.57 | yahoo_chart_daily | 2026-11-09 | US-listed | — | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| IAG | NYSE | 18.52 | -6.65 | 2.05 | — | 0.6x | 19.84 | yahoo_chart_daily | 2026-11-09 | US-listed (ADR) | 2026-11-05 (6d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| REPL | NASDAQ | 23.28 | 4.58 | 2.04 | — | 0.4x | 22.26 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-10-28 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| INGM | NYSE | 27.44 | 4.65 | 2.04 | — | 1.0x | 26.22 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-10-29 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| HL | NYSE | 14.29 | -7.27 | 2.03 | — | 0.6x | 15.41 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-11-03 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CDE | NYSE | 15.29 | -7.05 | 2.03 | — | 0.6x | 16.45 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-11-04 (7d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| REGN | NASDAQ | 916.06 | -0.42 | -2.03 | — | 0.9x | 919.96 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-10-30 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SRPT | NASDAQ | 16.42 | -4.76 | 2.01 | — | 0.6x | 17.24 | yahoo_chart_daily | 2026-11-09 | US-listed | 2026-11-05 (6d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |

## US — QUIET one-liners

| Ticker | Venue | Chg % | Pre-mkt % | Post-mkt % | Move vs avg daily | Ref close | Ref source | Ref asof | US tradeable | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATEC | NASDAQ | -5.15 | 2.00 | — | 1.0x | 7.38 | yahoo_chart_daily | 2026-11-09 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| ZETA | NYSE | 8.17 | 2.00 | — | 2.6x | 32.42 | yahoo_chart_daily | 2026-11-09 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| MANE | NYSE | 3.12 | 1.99 | — | 0.8x | 143.95 | yahoo_chart_daily | 2026-11-09 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| BEAM | NASDAQ | -6.92 | 1.99 | — | 1.7x | 27.02 | yahoo_chart_daily | 2026-11-09 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| ASAN | NYSE | -4.29 | 1.98 | — | 1.3x | 10.02 | yahoo_chart_daily | 2026-11-09 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| DPC | NYSE | -8.68 | 1.97 | — | 1.5x | 32.73 | yahoo_chart_daily | 2026-11-09 | US-listed (ADR) | — | no catalyst lookup (outside the per-run budget) |
| ARIS | NYSE | -4.33 | 1.95 | — | 1.2x | 16.64 | yahoo_chart_daily | 2026-11-09 | US-listed (ADR) | — | no catalyst lookup (outside the per-run budget) |
| SCCO | NYSE | -3.22 | 1.94 | — | 1.3x | 176.02 | yahoo_chart_daily | 2026-11-09 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| SRRK | NASDAQ | -6.89 | 1.92 | — | 2.5x | 51.55 | yahoo_chart_daily | 2026-11-09 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| NESR | NASDAQ | 4.25 | 1.91 | — | 1.1x | 19.55 | yahoo_chart_daily | 2026-11-09 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| NOVT | NASDAQ | -15.26 | 1.89 | — | 4.1x | 145.98 | yahoo_chart_daily | 2026-11-09 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| HWM | NYSE | 1.30 | 1.89 | — | 0.4x | 216.24 | yahoo_chart_daily | 2026-11-09 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| SSRM | NASDAQ | -4.94 | 1.88 | — | 1.7x | 29.67 | yahoo_chart_daily | 2026-11-09 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| EGO | NYSE | -5.10 | 1.83 | — | 1.4x | 37.42 | yahoo_chart_daily | 2026-11-09 | US-listed (ADR) | — | no catalyst lookup (outside the per-run budget) |
| VLO | NYSE | -1.69 | 1.83 | — | 0.7x | 356.75 | yahoo_chart_daily | 2026-11-09 | US-listed | — | no catalyst lookup (outside the per-run budget) |

## EU/UK — Headline table

| Ticker | Market | Venue | Close | Chg % | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | Session asof | Settle | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BICO | sweden | OMXSTO | 17.26 | -30.12 | SEK | 21.9x | 24.70 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | live | ADR (OTC:CLLKF) | 2026-08-19 | Y | Q3 2026 interim report published 11 Nov 07:00 CET: net sales SEK 465.2m (+20.2% y/y, including a one-off SEK 135m SCIENION supply and licence deal), adjusted EBITDA SEK 124.3m at a 26.7% margin - but a SEK 296m impairment of Biosero goodwill and technology, net loss SEK 220.4m and negative operating cash flow sent the shares down about 30% |
| HNSA | sweden | OMXSTO | 44.58 | +14.48 | SEK | 6.2x | 38.94 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | live | none | 2026-11-11 | — | no catalyst lookup (outside the per-run budget) |
| APR | norway | OSL | 33.4 | -12.79 | NOK | 3.6x | 38.30 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | live | none | 2026-10-29 | — | no catalyst lookup (outside the per-run budget) |
| GNS | poland | GPW | 15.6 | +12.23 | PLN | 5.5x | 13.90 | yahoo_chart_daily | 2026-11-09 | 2026-11-10 | settled | none | 2026-09-30 | — | no catalyst lookup (outside the per-run budget) |
| SIVE | sweden | OMXSTO | 17.48 | +11.27 | SEK | 2.3x | 15.71 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | live | none | 2026-08-27 | — | no catalyst lookup (outside the per-run budget) |
| ATS | austria | VIE | 125.4 | +11.17 | EUR | 1.9x | 112.80 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | live | none | 2026-11-05 | — | no catalyst lookup (outside the per-run budget) |
| FNM | sweden | OMXSTO | 104.5 | +10.70 | SEK | 3.8x | 94.40 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | live | none | 2026-08-12 | Y | Ferronordic Q3 2026 interim report published 11 Nov 07:30 CET: sales SEK 1,216m (+3% y/y) and EBIT SEK 69m, a beat versus the ABGSCe SEK 1,178m, on higher earnings and growing aftermarket |
| CAF | spain | BME | 69.6 | -10.19 | EUR | 7.7x | 77.50 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | live | none | 2026-07-30 | — | no catalyst lookup (outside the per-run budget) |
| SOI | france | EURONEXT | 106.4 | +9.92 | EUR | 1.9x | 96.80 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | live | none | 2026-05-27 | — | no catalyst lookup (outside the per-run budget) |
| ENR | germany | XETR | 130.64 | +9.01 | EUR | 2.4x | 119.84 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | live | none | 2026-08-04 | Y | Siemens Energy record fiscal 2026 reported 11 Nov: comparable revenue EUR 44.2bn (+15.5%), orders EUR 68.1bn (+18.8%), record year-end backlog EUR 164bn with a 1.54 book-to-bill, profit before special items more than doubled to EUR 5.486bn, dividend more than tripled to EUR 2.30 a share, and FY27 guidance of 14-16% comparable revenue growth |
| DRW3 | germany | XETR | 108 | +8.32 | EUR | 3.5x | 99.70 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | live | none | 2026-10-29 | — | no catalyst lookup (outside the per-run budget) |
| IFX | germany | XETR | 53.11 | +8.28 | EUR | 2.7x | 49.05 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | live | none | 2026-11-10 | — | no catalyst lookup (outside the per-run budget) |
| AIXA | germany | SWB | 33.97 | +7.13 | EUR | 1.5x | 31.75 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | live | none | 2026-10-29 | — | no catalyst lookup (outside the per-run budget) |
| TPRO | italy | MIL | 23.56 | +7.09 | EUR | 1.7x | 22.00 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | live | none | 2026-08-05 | — | no catalyst lookup (outside the per-run budget) |
| ERA | france | EURONEXT | 38.28 | +6.87 | EUR | 2.6x | 35.82 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | live | none | 2026-07-29 | — | no catalyst lookup (outside the per-run budget) |
| ASM | netherlands | EURONEXT | 725.8 | +6.70 | EUR | 2.0x | 680.20 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | live | ADR (OTC:ASMXF) | 2026-10-27 | — | no catalyst lookup (outside the per-run budget) |
| KOMPL | norway | OSL | 6.96 | +5.45 | NOK | 1.9x | 6.60 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | live | none | 2026-10-22 | — | no catalyst lookup (outside the per-run budget) |
| COTN | switzerland | SIX | 319.2 | +5.21 | CHF | 1.6x | 303.40 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | live | none | 2026-07-31 | — | no catalyst lookup (outside the per-run budget) |
| BESI | netherlands | EURONEXT | 158.5 | +5.11 | EUR | 1.3x | 150.80 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | live | none | 2026-10-21 | — | no catalyst lookup (outside the per-run budget) |
| DVL | poland | GPW | 8.4 | +5.00 | PLN | 3.1x | 8.00 | yahoo_chart_daily | 2026-11-09 | 2026-11-10 | settled | none | 2026-09-11 | — | no catalyst lookup (outside the per-run budget) |
| BWE | norway | OSL | 47.4 | +4.87 | NOK | 1.9x | 45.20 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | live | none | 2026-10-29 | — | no catalyst lookup (outside the per-run budget) |
| AKAST | norway | OSL | 11.88 | +4.76 | NOK | 2.2x | 11.34 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | live | none | 2026-08-21 | — | no catalyst lookup (outside the per-run budget) |
| IFCN | switzerland | SIX | 163.8 | +4.73 | CHF | 1.6x | 156.40 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | live | none | 2026-07-30 | — | no catalyst lookup (outside the per-run budget) |
| FLS | denmark | OMXCOP | 599 | +4.72 | DKK | 3.0x | 572.00 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | live | none | 2026-08-18 | — | no catalyst lookup (outside the per-run budget) |
| HUBN | switzerland | SIX | 172.4 | +4.48 | CHF | 1.6x | 165.00 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | live | none | 2026-08-18 | — | no catalyst lookup (outside the per-run budget) |
| SENSO | finland | OMXHEX | 19.77 | +4.33 | EUR | 1.6x | 18.95 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | live | none | — | — | no catalyst lookup (outside the per-run budget) |
| YPSN | switzerland | SIX | 411.4 | +4.26 | CHF | 4.4x | 394.60 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | live | none | 2026-11-11 | — | no catalyst lookup (outside the per-run budget) |
| VWS | denmark | OMXCOP | 190.15 | -4.25 | DKK | 2.5x | 198.60 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | live | none | 2026-11-11 | — | no catalyst lookup (outside the per-run budget) |
| ICOS | italy | MIL | 13.82 | +4.22 | EUR | 3.3x | 13.26 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | live | none | 2026-08-04 | — | no catalyst lookup (outside the per-run budget) |

## AU (ASX) — Headline table

| Ticker | Venue | Close | Chg % | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | Session asof | Settle | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IEL | ASX | 2.57 | +16.29 | AUD | 9.7x | 2.21 | yahoo_chart_daily | 2026-11-09 | 2026-11-11 | settled | none | 2026-08-19 | N | Blackstone Singapore revised its unsolicited takeover proposal to A$3.00 per share in cash (announced 11 Nov 09:38 AEDT) after the board had unanimously rejected earlier offers; the board is weighing the revised bid and no decision has been made |
| ELV | ASX | 4.07 | +9.70 | AUD | 1.9x | 3.71 | yahoo_chart_daily | 2026-11-09 | 2026-11-11 | settled | none | 2026-08-27 | — | no catalyst lookup (outside the per-run budget) |
| SRL | ASX | 14 | +7.69 | AUD | 1.4x | 13.00 | yahoo_chart_daily | 2026-11-09 | 2026-11-11 | settled | none | 2026-09-07 | — | no catalyst lookup (outside the per-run budget) |
| MND | ASX | 34.99 | +7.23 | AUD | 2.9x | 32.63 | yahoo_chart_daily | 2026-11-09 | 2026-11-11 | settled | none | 2026-08-24 | Y | Monadelphous business update 10 Nov: first-half FY27 revenue of about A$1.7bn (up from A$1.53bn) and net profit after tax of A$80-85m (up from A$64.8m), with A$830m of new contracts since 1 July; Bell Potter upgraded to buy with a A$36.50 target on 11 Nov |

## APAC/Gulf — Headline table

| Ticker | Market | Venue | Close | Chg % | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | Session asof | Settle | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| HRME | indonesia | IDX | 55 | +34.15 | IDR | 4.3x | 41.00 | yahoo_chart_daily | 2026-11-09 | 2026-11-10 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| WMUU | indonesia | IDX | 35 | +29.63 | IDR | 3.8x | 27.00 | yahoo_chart_daily | 2026-11-09 | 2026-11-10 | settled | none | 2022-08-24 | — | no catalyst lookup (outside the per-run budget) |
| 688135 | china | SSE | 35.02 | +20.01 | CNY | 4.5x | 29.18 | yahoo_chart_daily | 2026-11-09 | 2026-11-10 | settled | none | 2025-10-28 | — | no catalyst lookup (outside the per-run budget) |
| 301636 | china | SZSE | 47.2 | +20.01 | CNY | 4.9x | 39.33 | yahoo_chart_daily | 2026-11-09 | 2026-11-10 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| 300473 | china | SZSE | 58.79 | +20.00 | CNY | 3.1x | 48.99 | yahoo_chart_daily | 2026-11-09 | 2026-11-10 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| FLOMIC | india | BSE | 57.6 | +20.00 | INR | 4.5x | 48.00 | yahoo_chart_daily | 2026-11-08 | 2026-11-10 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| PIONRINV | india | NSE | 69.39 | +19.99 | INR | 5.2x | 57.83 | yahoo_chart_daily | 2026-11-08 | 2026-11-10 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| MIM | singapore | SGX | 1.46 | +16.80 | SGD | 2.0x | 1.25 | yahoo_chart_daily | 2026-11-09 | 2026-11-10 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| THG | thailand | SET | 7.75 | +13.97 | THB | 7.9x | 6.80 | yahoo_chart_daily | 2026-11-09 | 2026-11-10 | settled | none | 2026-08-11 | N | no fresh catalyst found (no THG announcement on the SET news page for 10 or 11 Nov; the 11 Nov session traded 8.79m shares against 108k the prior session - unusual volume with no public catalyst identified) |
| 4310 | ksa | TADAWUL | 20.99 | +9.95 | SAR | 3.1x | 19.09 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| 4144 | ksa | TADAWUL | 80.7 | +9.95 | SAR | 3.2x | 73.40 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| 2288 | ksa | TADAWUL | 6.65 | +9.38 | SAR | 3.9x | 6.08 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| NCAP | thailand | SET | 3.24 | -8.99 | THB | 4.2x | 3.56 | yahoo_chart_daily | 2026-11-09 | 2026-11-10 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| EB5 | singapore | SGX | 2.82 | +8.88 | SGD | 2.5x | 2.59 | yahoo_chart_daily | 2026-11-09 | 2026-11-10 | settled | none | 2026-08-13 | — | no catalyst lookup (outside the per-run budget) |
| S11 | thailand | SET | 4.86 | +8.00 | THB | 7.7x | 4.50 | yahoo_chart_daily | 2026-11-09 | 2026-11-10 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| 558 | singapore | SGX | 1.89 | +8.00 | SGD | 1.7x | 1.75 | yahoo_chart_daily | 2026-11-09 | 2026-11-10 | settled | none | 2026-11-10 | Y | UMS Integration Q3 FY2026 results released 10 Nov after the close: record quarterly revenue S$95.4m (+61% y/y) and net attributable profit more than doubled to S$21.1m, EPS 2.37 cents, on the AI chip super-cycle and aviation demand; third interim dividend of 1.0 cent a share declared |
| MEL | newzealand | NZX | 5.94 | +2.77 | NZD | 2.3x | 5.78 | yahoo_chart_daily | 2026-11-09 | 2026-11-10 | settled | none | 2026-08-25 | N | no fresh catalyst found (no company announcement identified; Meridian tracked the NZX 50 higher on 11 Nov, with Morningstar publishing two company reports the same day) |

## Source health

- scanner_calls: 55 | scanner_errors: 0
- markets_scanned: US + 17 EU/UK + ASX + 7 APAC/Gulf (india, thailand, indonesia, china, singapore, newzealand, ksa)
- pipeline_version: 2026-11-11.1
- et_clock: zoneinfo America/New_York (DST-aware; a fixed UTC-4 mislabels every winter fire)
- premarket_window: 04:00-09:30 ET, resolved with zoneinfo (09:00-14:30 UTC in winter, 08:00-13:30 UTC in summer)
- session_selection: by DATE and order, never by a modal time-of-day. Yahoo stamps a daily bar at the session open, so the ET stamp of the SAME session shifts by one hour across a DST boundary; a modal filter kept the OLDER bars and discarded the NEWEST ones, which rolled the base back to the prior-prior session (66 US + 21 ASX rows lost on 2026-11-03, 24 of 25 ASX rows lost on 2026-11-04).
- yahoo_calls: 198 | yahoo_429: 0 | yahoo_errors: 1
- reference_close (screener vs Yahoo, resolved BEFORE the tables were built): agree=185 mismatch=1 unverified=2 stale_reference=1
  method: the screener's implied reference close (close / (1 + change/100)) is compared
  with Yahoo's own reference close. A match proves the move was measured against the
  TRUE prior close; a mismatch means the row sits on a STALE reference (phantom move).
  Coverage: every row of the US headline, US QUIET, EU/UK and ASX tables is checked.
  Yahoo bar mode: {"closed": 158, "live": 27} (closed = last completed session bar;
  live = in-progress EU/UK session bar, which is what a weekday 08:00 ET EU move needs)
  live drift between the screener snapshot and the later Yahoo print: median=0.00pp max=1.49pp (expected on a live market)
- cross_check mismatches: [{"region": "indonesia", "symbol": "MKNT.JK", "tv": 33.333, "yahoo": 0.0, "delta": 33.333, "ref_delta_pct": -25.0, "tv_implied_ref": 24.0, "yahoo_ref": 32.0, "yahoo_date": "2026-11-09", "yahoo_ref_date": "2026-11-08", "verdict": "stale_reference"}]
- rows_dropped_stale_ref: 1 (rows whose screener-implied reference close disagreed with Yahoo's by more than 0.5%; they are dropped, not published)
- rows_dropped_unresolved_ref: 2 (rows whose reference close could not be resolved from Yahoo at all - the base of the move is unverifiable, so the row is dropped rather than published with a '—' base)
- us_premarket_check (Yahoo 1-min pre/post feed vs the screener pre-market column, base = the IMMEDIATELY prior session's close): checked=10 within_1pp=8 within_3pp=10 unavailable=0
- markets_with_lt5_rows: ['uk:less=2', 'france:less=2', 'netherlands:egreater=3', 'netherlands:less=0', 'belgium:egreater=2', 'belgium:less=0', 'portugal:egreater=0', 'portugal:less=0', 'ireland:egreater=0', 'ireland:less=0', 'italy:egreater=4', 'italy:less=2', 'switzerland:less=1', 'spain:egreater=1', 'spain:less=1', 'norway:less=2', 'denmark:less=2', 'finland:egreater=2', 'finland:less=0', 'poland:less=0', 'austria:egreater=3', 'austria:less=0', 'greece:egreater=1', 'greece:less=0', 'singapore:less=2', 'newzealand:egreater=1', 'newzealand:less=0', 'ksa:less=4']
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
- bod_no_extended_hours: 109 (deferred to the next scan; not in the headline table)
- earnings_source: screener `earnings_release_date` (last FULL report) + `earnings_release_next_date` (next scheduled)
- earnings_caveat: `earnings_release_date` does NOT capture preliminary, guidance or
  restructuring releases. On 2026-10-23 LKQ fell 22.47% on a preliminary Q3 miss while
  the field still read 2026-07-30. ALWAYS confirm the earnings-driven flag against the
  headline itself; the calendar field is a screen, not a verdict.
- us_line_index: ok (US-listed lines for the 25 foreign home countries, both scanner types; the `US tradeable` column is ADR / US-listed / none)
- catalyst_note: Catalyst lookups: 5 US + 3 EU + 2 AU + 3 APAC/Gulf = 13 per run, the skill's cap.
- catalyst_budget: 5 US + 3 EU + 2 AU = 10 lookups per run
- one_table_rule: each name appears exactly once, in exactly one table, with its
  catalyst in that row's last column. There is no separate catalysts section.
- data_date: US regular session close of the prior trading day; extended-hours columns
  carry the prior session's prints
- settlement_state: 23 settled, 27 live (a live row's move is a mid-session snapshot, not the session's result)
- rows_per_market (EU/UK, cap 4/market): {'sweden': 4, 'norway': 4, 'poland': 4, 'austria': 3, 'spain': 2, 'france': 4, 'germany': 4, 'italy': 4, 'netherlands': 3, 'switzerland': 4, 'denmark': 4, 'finland': 2, 'uk': 4, 'belgium': 2, 'greece': 1} — the cap stops one thin market taking the table; the EU/UK table was 28% Sweden over nine runs (73 of 264 rows) while Belgium and Greece never appeared once.
- rows_per_market (APAC/Gulf, cap 3/market): {'indonesia': 3, 'china': 3, 'india': 3, 'singapore': 3, 'thailand': 3, 'ksa': 3, 'newzealand': 1}
- deprecations: mcp__tradingview-advanced__*, mcp__tradingview__*, mcp__financekit__*,
  mcp__stocktwits__* are ABSENT in Cloud sessions (tool_search 0 hits; connector catalog
  holds only media + credential tools). The public screener replaces them.

- degraded_sources: 1
  (the chat reply's `errors:` MUST equal this number - one entry per degraded
  source, not one per run)
  1. yahoo_chart_api.reference_close_unresolved — TW..L: the reference close could not be resolved (429 or a bad body)

## Audit line

`earnings-reaction target=earnings-reactions:2026-11-11 candidates=498 amc_reactions=0 pre_gaps=120 eu_reactions=29 asx_reactions=4 apac_reactions=16 catalyst_lookups=14 bod=109 rows_dropped_stale_ref=1 rows_dropped_unresolved_ref=2 degraded_sources=1`
