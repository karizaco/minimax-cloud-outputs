# Earnings reaction scanner — 2026-11-20

- Cron: `0 8 * * 1-5` America/New_York (weekdays, 08:00 ET)
- Fire time (ET): 2026-11-20 08:15:45 Fri
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

- 0 AMC reactions, 121 pre-market gaps, 77 without extended-hours data; 30 EU/UK and 4 ASX movers, 21 APAC/Gulf movers.
- Pass B2 (the US pre-market gap scan) met the filter on 36 names (4 up, 32 down); 12 were already a Pass A/B row and are recorded as dedupes, and 23 reached a table.
- Biggest US extended-hours move: CAPR PRE_GAP (15.01%).
- Biggest EU/UK move: VK (-11.32%, france).
- Biggest ASX move: MP1 (-12.89%).
- Biggest APAC/Gulf move: NTBK (+30.61%, indonesia).
- 0 of the 30 EU/UK rows are SETTLED and 30 are LIVE (mid-session). The 12:15 ET settlement pass publishes where those
  live moves actually closed.
- EU/AU/APAC earnings-driven tagging is keyword-based on headlines (best-effort). A row
  whose lookup was not performed carries NO verdict — only a researched row does.

## Actionable read

- **Move vs this name's own history.** The `Move vs avg daily` column divides the
  reaction by the name's own mean absolute daily move over its last
  20 completed sessions. A -27% move in a name that averages +-3% is a
  different event from a -8% move in a name that averages +-7%.
- **US-listed and tradeable vs foreign-only.** 136 published US rows are on a
  US venue; 2 more foreign reactions have a US ADR line
  (the `US tradeable` column carries the ticker); 31 are foreign-only and
  cannot be bought directly by a US reader.
- **Not yet fully priced — US (hypothesis, not a recommendation).**
  BJ — -7.00%, 0.99% mean absolute daily move over the last 20 completed sessions, 7.1x that average, reference close 110.88 dated 2026-11-18, US access: US-listed, the move now (-7.00%) is larger than the move it follows (-0.12%); the reaction is still being repriced. Hypothesis only: this artifact states no
  direction and no trade.
- **Not yet fully priced — EU/UK (hypothesis, not a recommendation).**
  VK — -11.32%, 1.36% mean absolute daily move over the last 20 completed sessions, 8.3x that average, reference close 18.11 dated 2026-11-19, US access: none, the move now (-11.32%) is larger than the move it follows (+0.08%); the reaction is still being repriced. Hypothesis only: this artifact states no
  direction and no trade.
- **Not yet fully priced — AU (ASX) (hypothesis, not a recommendation).**
  PRN — -11.23%, 2.97% mean absolute daily move over the last 20 completed sessions, 3.8x that average, reference close 1.87 dated 2026-11-18, US access: none, the move now (-11.23%) is larger than the move it follows (-4.59%); the reaction is still being repriced. Hypothesis only: this artifact states no
  direction and no trade.

## US — Headline table

| Ticker | Venue | Close | Chg % | Pre-mkt % | Post-mkt % | Move vs avg daily | Ref close | Ref source | Ref asof | US tradeable | Last earnings | Tag | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CAPR | NASDAQ | 7.53 | -6.23 | 15.01 | — | 1.9x | 8.03 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-10 (10d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AXTI | NASDAQ | 34.84 | -2.16 | -9.21 | — | 1.1x | 35.61 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-10-29 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| INTU | NASDAQ | 310.02 | -1.03 | -8.07 | — | 4.2x | 313.24 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-19 (1d ago) | PRE_GAP | Y | Q1 FY27 beat and the Mailchimp sale (reported 2026-11-19): revenue $4.4B +12%, non-GAAP EPS $2.91 +56%; FY27 revenue guide cut on Credit Karma (Consumer segment growth to 2-4%) with Q2 TurboTax revenue guided down mid-single-digits; Mailchimp sold to Bending Spoons for ~$3.68B |
| AAOI | NASDAQ | 39.46 | -3.26 | -8.01 | — | 1.1x | 40.79 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-05 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NUAI | NASDAQ | 4.28 | 7.27 | -7.46 | — | 0.6x | 3.99 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-12 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BE | NYSE | 168.11 | -1.68 | -7.14 | — | 1.2x | 170.98 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-10-22 (29d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BJ | NYSE | 110.75 | -0.12 | -7.00 | — | 7.1x | 110.88 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-20 (0d ago) | PRE_GAP | Y | Q3 FY26 beat, but earnings quality (reported 2026-11-20): adj EPS $1.73, revenue $6.28B +17.5%, comps +13.5% (+4.1% ex-gas); FY26 adj EPS guide raised to $5.10-$5.30, yet ~$240m of the quarter came from an interchange-fee settlement and merchandise margin fell 170bps, implying Q4 adj EPS of only $0.91-$1.11 |
| PURR | NASDAQ | 8.4 | 5.66 | -6.90 | — | 1.2x | 7.95 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-05 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MXL | NASDAQ | 48.13 | -2.83 | -6.86 | — | 1.0x | 49.53 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-10-22 (29d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ACMR | NASDAQ | 45.5 | 3.64 | -6.53 | — | 1.3x | 43.90 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-05 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMD | NASDAQ | 489.19 | -7.72 | -6.49 | — | 1.0x | 530.14 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-03 (17d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PENG | NASDAQ | 42.51 | -1.62 | -6.37 | — | 0.9x | 43.21 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-10-06 (45d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NVTS | NASDAQ | 7.17 | -1.78 | -6.14 | — | 0.9x | 7.30 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-03 (17d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AEHR | NASDAQ | 47.94 | -3.11 | -6.13 | — | 0.8x | 49.48 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-02 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SPCX | NASDAQ | 138.43 | -3.53 | -6.07 | — | 2.1x | 143.50 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-10-20 (31d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NBIS | NASDAQ | 96.92 | -9.39 | -5.90 | — | 0.7x | 106.96 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-12 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SKYA | NASDAQ | 4 | -3.15 | 5.88 | — | 0.8x | 4.13 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-06 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LITE | NASDAQ | 535.15 | -2.89 | -5.87 | — | 0.9x | 551.07 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-02 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| COHR | NYSE | 214.94 | 0.99 | -5.85 | — | 0.9x | 212.84 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-04 (16d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CLS | NYSE | 240.23 | -1.27 | -5.84 | — | 1.1x | 243.32 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-10-26 (25d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SEZL | NASDAQ | 146.33 | -7.72 | -5.69 | — | 1.5x | 158.58 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-04 (16d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| DELL | NYSE | 312.54 | -0.18 | -5.67 | — | 1.0x | 313.11 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-09-01 (80d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CRWV | NASDAQ | 44.91 | -6.10 | -5.54 | — | 0.8x | 47.83 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-10 (10d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ICHR | NASDAQ | 32.15 | -5.33 | -5.53 | — | 1.0x | 33.96 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-02 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CEVA | NASDAQ | 25.6 | 1.63 | -5.47 | — | 1.2x | 25.19 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-09 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ROST | NASDAQ | 219.88 | -3.41 | -5.40 | — | 2.5x | 227.64 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-19 (1d ago) | PRE_GAP | — | Q4 2026 results, report date 2026-11-19 (Nasdaq earnings calendar; no headline lookup), consensus EPS $1.85 |
| MRVL | NASDAQ | 138.47 | -4.86 | -5.36 | — | 0.9x | 145.54 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-08-27 (85d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AGLT | NASDAQ | 6.49 | -5.26 | -5.36 | — | 0.8x | 6.85 | yahoo_chart_daily | 2026-11-18 | US-listed | — | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| WULF | NASDAQ | 11.58 | -3.50 | -5.34 | — | 0.8x | 12.00 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-06 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| STX | NASDAQ | 521.39 | 1.06 | -5.29 | — | 1.1x | 515.90 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-10-27 (24d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CIFR | NASDAQ | 6.48 | -1.37 | -5.25 | — | 0.7x | 6.57 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-02 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| OUST | NASDAQ | 28.16 | -3.89 | -5.18 | — | 0.9x | 29.30 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-03 (17d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ALOY | NASDAQ | 4.35 | -3.55 | -5.06 | — | 0.8x | 4.51 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-13 (7d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RVMD | NASDAQ | 159.43 | -0.24 | 5.06 | — | 1.6x | 159.82 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-04 (16d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CRDO | NASDAQ | 117.76 | -4.21 | -5.01 | — | 0.8x | 122.94 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-09-01 (80d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LPTH | NASDAQ | 6.01 | -3.99 | -5.01 | — | 0.9x | 6.26 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-10 (10d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CHRN | NASDAQ | 8.51 | -11.08 | -4.94 | — | 0.6x | 9.57 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-10-15 (36d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| REAL | NASDAQ | 11.83 | -6.26 | 4.90 | — | 1.2x | 12.62 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-10-29 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| WDC | NASDAQ | 296.78 | 2.98 | -4.85 | — | 1.0x | 288.19 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-10-22 (29d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| VRT | NYSE | 184.99 | -4.88 | -4.80 | — | 0.8x | 194.48 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-10-28 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MU | NASDAQ | 690.44 | -2.10 | -4.78 | — | 1.0x | 705.27 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-09-30 (51d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GLW | NYSE | 105.97 | -2.02 | -4.69 | — | 1.2x | 108.15 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-10-27 (24d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| INTC | NASDAQ | 55.72 | 1.92 | -4.46 | — | 0.8x | 54.67 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-10-29 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ESTC | NYSE | 76.33 | -8.05 | -4.38 | — | 1.3x | 83.01 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-19 (1d ago) | PRE_GAP | Y | Q2 FY27 beat, revenue guide below consensus (reported 2026-11-19): revenue $495.9M +17%, non-GAAP EPS $0.94 vs $0.81 est, cRPO +19%; Q3 revenue guided $507.5-508.5M and FY27 $2.000-2.008B vs ~$2.01B consensus on a $9.5m FX headwind; shares fell about 8% after the print |
| IREN | NASDAQ | 14.41 | -5.45 | -4.37 | — | 0.6x | 15.24 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-05 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| P | NYSE | 105.5 | 4.73 | -4.27 | — | 0.9x | 100.74 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-18 (2d ago) | PRE_GAP | — | Q4 2026 results, report date 2026-11-18 (Nasdaq earnings calendar; no headline lookup), consensus EPS $0.28 |
| OKTA | NASDAQ | 206.85 | 5.75 | -4.25 | — | 1.1x | 195.61 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-08-26 (86d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| KLIC | NASDAQ | 61.58 | -8.08 | -4.19 | — | 1.0x | 66.99 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-18 (2d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-18 (Nasdaq earnings calendar; no headline lookup), consensus EPS $1.31 |
| GEV | NYSE | 756.28 | -2.06 | -4.14 | — | 1.2x | 772.22 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-10-28 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ANET | NYSE | 189.59 | -2.24 | -4.00 | — | 0.9x | 193.94 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-03 (17d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GAP | NYSE | 18.79 | -5.29 | 3.95 | — | 1.4x | 19.84 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-19 (1d ago) | PRE_GAP | Y | Q3 FY26 beat, full-year guide cut (reported 2026-11-19): adj EPS $0.82 vs $0.78 est, revenue $4.01B, comps flat vs +1.3% expected; Athleta comps -15%, Banana Republic -3%; FY26 EPS guide cut to $2.29-$2.34 and sales to roughly flat; new Athleta CEO named |
| USAR | NASDAQ | 6.87 | 4.73 | -3.93 | — | 0.6x | 6.56 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-09 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PLTR | NASDAQ | 153.68 | -1.91 | -3.86 | — | 1.5x | 156.67 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-02 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NET | NYSE | 303.68 | 0.92 | -3.85 | — | 0.9x | 300.91 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-05 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| QBTS | NASDAQ | 7.31 | -4.94 | -3.83 | — | 0.7x | 7.69 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-10 (10d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CBRS | NASDAQ | 86.96 | -7.64 | -3.69 | — | 0.6x | 94.15 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-12 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PWR | NYSE | 587.43 | -2.52 | -3.65 | — | 0.9x | 602.60 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-10-29 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RBRK | NYSE | 114.56 | 4.15 | -3.63 | — | 1.0x | 110.00 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-08-27 (85d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| STGW | NASDAQ | 10.33 | -5.66 | 3.58 | — | 1.2x | 10.95 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-10-29 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FIVN | NASDAQ | 23.18 | -4.96 | -3.58 | — | 1.1x | 24.39 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-05 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| INIO | NASDAQ | 12.81 | -5.74 | -3.51 | — | 0.6x | 13.59 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-10-27 (24d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GLXY | NASDAQ | 12.32 | -7.51 | -3.49 | — | 0.4x | 13.32 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-10-27 (24d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ZS | NASDAQ | 205.71 | 3.98 | -3.49 | — | 1.4x | 197.83 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-09-03 (78d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CLSK | NASDAQ | 5.84 | -5.96 | -3.42 | — | 0.5x | 6.21 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-08-06 (106d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ORCL | NYSE | 110.57 | -2.92 | -3.36 | — | 0.8x | 113.89 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-09-10 (71d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| META | NASDAQ | 596.22 | -3.27 | -3.35 | — | 1.8x | 616.38 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-10-21 (30d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FSLY | NASDAQ | 16.86 | -5.81 | -3.32 | — | 0.6x | 17.90 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-04 (16d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMAT | NASDAQ | 338.93 | -3.80 | -3.31 | — | 0.8x | 352.30 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-12 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MARA | NASDAQ | 6.245 | -4.80 | -3.28 | — | 0.6x | 6.56 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-09 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LRCX | NASDAQ | 203.68 | -3.77 | -3.28 | — | 0.7x | 211.67 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-10-21 (30d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ETN | NYSE | 330.57 | -2.30 | -3.26 | — | 1.0x | 338.34 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-03 (17d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NVDA | NASDAQ | 145.98 | -3.30 | -3.08 | — | 1.0x | 150.96 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-17 (3d ago) | PRE_GAP | — | Q4 2026 results, report date 2026-11-17 (Nasdaq earnings calendar; no headline lookup), consensus EPS $2.47 |
| QNT | NASDAQ | 27.96 | -12.60 | -3.08 | — | 0.4x | 31.99 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-05 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ZETA | NYSE | 32.22 | -5.12 | -3.07 | — | 0.9x | 33.96 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-09 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AVGO | NASDAQ | 346.65 | -2.09 | -3.07 | — | 0.8x | 354.05 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-09-02 (79d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CORZ | NASDAQ | 13.36 | -4.91 | -3.05 | — | 0.5x | 14.05 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-05 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PPTA | NASDAQ | 15.47 | -8.05 | -3.04 | — | 0.7x | 16.82 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-13 (7d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-13 (Nasdaq earnings calendar; no headline lookup), consensus EPS ($0.49) |
| ECHO | NASDAQ | 92.31 | -4.76 | -3.02 | — | 1.0x | 96.92 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-03 (17d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PGY | NASDAQ | 14.62 | -6.10 | -3.01 | — | 0.8x | 15.57 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-10-29 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TWLO | NYSE | 178.78 | -8.75 | -3.01 | — | 0.9x | 195.93 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-10-29 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CAT | NYSE | 537.37 | -3.83 | -2.99 | — | 1.0x | 558.77 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-10-29 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TH | NASDAQ | 11.33 | -7.13 | -2.91 | — | 0.6x | 12.20 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-09 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NTSK | NASDAQ | 24.8 | 5.51 | -2.91 | — | 0.7x | 23.50 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-09-02 (79d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| UPST | NASDAQ | 17 | -5.71 | -2.88 | — | 0.7x | 18.03 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-03 (17d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| HIMS | NYSE | 16.02 | -6.04 | -2.84 | — | 0.5x | 17.05 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-09 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CRWD | NASDAQ | 243.46 | 2.71 | -2.84 | — | 1.1x | 237.03 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-08-26 (86d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMBA | NASDAQ | 58.93 | 7.85 | -2.83 | — | 0.9x | 54.64 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-09-03 (78d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TEM | NASDAQ | 59.61 | -6.30 | -2.78 | — | 0.6x | 63.62 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-02 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| APH | NYSE | 75.61 | -0.94 | -2.74 | — | 0.9x | 76.33 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-10-28 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| APP | NASDAQ | 379.02 | -3.04 | -2.70 | — | 0.5x | 390.91 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-04 (16d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| EEFT | NASDAQ | 64.71 | -4.84 | -2.63 | — | 1.2x | 68.00 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-10-27 (24d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FOUR | NYSE | 37.97 | -6.91 | -2.53 | — | 0.7x | 40.79 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-05 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PRIM | NYSE | 60.08 | -6.45 | -2.50 | — | 0.5x | 64.22 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-03 (17d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ABCL | NASDAQ | 10.47 | -4.99 | -2.48 | — | 0.6x | 11.02 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-09 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| KLAC | NASDAQ | 141.48 | -2.35 | -2.46 | — | 0.6x | 144.88 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-10-28 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SNOW | NYSE | 268.59 | -3.94 | -2.45 | — | 0.8x | 279.62 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-09-02 (79d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SA | NYSE | 18.06 | -29.32 | -2.44 | — | 0.5x | 25.55 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-13 (7d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| HYMC | NASDAQ | 13.78 | -9.64 | -2.43 | — | 0.5x | 15.25 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-10-27 (24d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PTRN | NASDAQ | 18.86 | -7.09 | -2.39 | — | 0.9x | 20.30 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-04 (16d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SNAP | NYSE | 5.12 | -5.88 | -2.38 | — | 0.6x | 5.44 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-04 (16d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SNPS | NASDAQ | 430.91 | -0.71 | -2.35 | — | 1.1x | 434.01 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-08-26 (86d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMZN | NASDAQ | 257.37 | -3.87 | -2.34 | — | 1.1x | 267.74 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-10-29 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AYA | NASDAQ | 18.9 | -6.80 | -2.31 | — | 0.5x | 20.28 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-12 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| EXK | NYSE | 6.08 | -7.32 | -2.30 | — | 0.6x | 6.56 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-09 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CEG | NASDAQ | 252.03 | -4.08 | -2.27 | — | 0.8x | 262.74 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-09 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| JCI | NYSE | 136 | -1.75 | -2.26 | — | 0.8x | 138.42 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-10-27 (24d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| VVV | NYSE | 36.84 | 10.40 | -2.25 | — | 0.9x | 33.37 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-19 (1d ago) | PRE_GAP | Y | Q4 FY26 in line, margins down (reported 2026-11-19): adj EPS $0.42 -7% y/y on gross margin -300bps from elevated lubricant costs, sales $554M +22%, system-wide SSS +9.4%; FY27 adj EPS guided $1.85-$2.05, buyback raised to $500m; shares jumped 10% on the print |
| FTNT | NASDAQ | 131.46 | -0.27 | -2.25 | — | 0.6x | 131.81 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-10-28 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MSFT | NASDAQ | 498.3 | -1.97 | -2.25 | — | 1.3x | 508.29 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-10-28 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| IBKR | NASDAQ | 75.65 | -1.05 | -2.18 | — | 0.9x | 76.45 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-10-15 (36d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CDE | NYSE | 11.54 | -5.72 | -2.18 | — | 0.6x | 12.24 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-04 (16d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MAAS | NASDAQ | 9.2 | -5.06 | -2.17 | — | 0.9x | 9.69 | yahoo_chart_daily | 2026-11-18 | US-listed | — | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PANW | NASDAQ | 361.73 | 6.42 | -2.14 | — | 0.6x | 339.92 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-18 (2d ago) | PRE_GAP | — | Q4 2026 results, report date 2026-11-18 (Nasdaq earnings calendar; no headline lookup), consensus EPS $0.52 |
| VOYG | NYSE | 22.02 | -6.77 | -2.13 | — | 0.3x | 23.62 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-02 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BETA | NYSE | 18.83 | -6.08 | -2.12 | — | 0.4x | 20.05 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-03 (17d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AG | NYSE | 11.32 | -5.03 | -2.12 | — | 0.6x | 11.92 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-05 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TSLA | NASDAQ | 374.41 | -2.43 | -2.10 | — | 0.8x | 383.72 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-10-21 (30d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SCCO | NYSE | 141.46 | -3.25 | -2.09 | — | 0.7x | 146.21 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-10-21 (30d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GCT | NASDAQ | 60.44 | -7.44 | -2.04 | — | 0.6x | 65.30 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-05 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AADX | NYSE | 6.43 | -5.30 | -2.02 | — | 0.3x | 6.79 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-11-11 (9d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| EGO | NYSE | 26.84 | -5.43 | -2.01 | — | 0.5x | 28.38 | yahoo_chart_daily | 2026-11-18 | US-listed | 2026-10-28 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |

## US — QUIET one-liners

| Ticker | Venue | Chg % | Pre-mkt % | Post-mkt % | Move vs avg daily | Ref close | Ref source | Ref asof | US tradeable | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|
| NOW | NYSE | -1.90 | -1.94 | — | 0.5x | 90.59 | yahoo_chart_daily | 2026-11-18 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| ZM | NASDAQ | -9.56 | -1.93 | — | 3.5x | 92.68 | yahoo_chart_daily | 2026-11-18 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| HCA | NYSE | -3.36 | 1.91 | — | 1.5x | 476.35 | yahoo_chart_daily | 2026-11-18 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| SHOP | NASDAQ | -5.34 | -1.91 | — | 1.8x | 139.42 | yahoo_chart_daily | 2026-11-18 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| SXI | NYSE | -5.75 | -1.91 | — | 2.4x | 232.69 | yahoo_chart_daily | 2026-11-18 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| LQDT | NASDAQ | -24.88 | -1.89 | — | 8.1x | 43.97 | yahoo_chart_daily | 2026-11-18 | US-listed | — | Q3 2026 results, report date 2026-11-19 (Nasdaq earnings calendar; no headline lookup), consensus EPS $0.34 |
| FIG | NYSE | -6.17 | -1.85 | — | 1.5x | 17.33 | yahoo_chart_daily | 2026-11-18 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| TXN | NASDAQ | -2.28 | -1.83 | — | 0.9x | 292.43 | yahoo_chart_daily | 2026-11-18 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| CAKE | NASDAQ | -6.50 | -1.78 | — | 2.2x | 120.05 | yahoo_chart_daily | 2026-11-18 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| AVAV | NASDAQ | -5.14 | -1.74 | — | 1.1x | 101.11 | yahoo_chart_daily | 2026-11-18 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| VOR | NASDAQ | 3.87 | -1.73 | — | 1.2x | 17.83 | yahoo_chart_daily | 2026-11-18 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| WMT | NASDAQ | -1.04 | 1.71 | — | 0.9x | 127.36 | yahoo_chart_daily | 2026-11-18 | US-listed | — | Q4 2026 results, report date 2026-11-19 (Nasdaq earnings calendar; no headline lookup), consensus EPS $0.64 |
| NEM | NYSE | -4.29 | -1.71 | — | 1.5x | 104.53 | yahoo_chart_daily | 2026-11-18 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| ERAS | NASDAQ | 3.34 | 1.69 | — | 0.8x | 13.76 | yahoo_chart_daily | 2026-11-18 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| UNH | NYSE | -5.55 | 1.68 | — | 2.7x | 349.91 | yahoo_chart_daily | 2026-11-18 | US-listed | — | no catalyst lookup (outside the per-run budget) |

## EU/UK — Headline table

| Ticker | Market | Venue | Close | Chg % | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | Session asof | Settle | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| VK | france | EURONEXT | 16.065 | -11.32 | EUR | 8.3x | 18.11 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | live | none | — | — | no catalyst lookup (outside the per-run budget) |
| SIVE | sweden | OMXSTO | 12.18 | -11.03 | SEK | 2.0x | 13.69 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | live | none | 2026-08-27 (85d ago) | N | No issuer release (the Q3 interim is not due until 26 Nov): the stock fell with the global AI and semiconductor selloff, and Millennium International disclosed a new public short position of more than 0.5% of capital |
| ATS | austria | VIE | 102 | -10.53 | EUR | 2.2x | 114.00 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | live | none | 2026-11-05 (15d ago) | — | no catalyst lookup (outside the per-run budget) |
| HUNT | norway | OSL | 16.14 | -10.33 | NOK | 2.9x | 18.00 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | live | none | 2026-11-20 (0d ago) | N | The Jacktel bid is the driver: a NOK 1.63bn cash-funded purchase order at NOK 6.30 per Jacktel share; the Q3 print (reported 2026-11-20) showed a record net profit of USD 111.4m |
| SOI | france | EURONEXT | 98.32 | -10.00 | EUR | 1.7x | 109.25 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | live | none | 2026-11-18 (2d ago) | — | no catalyst lookup (outside the per-run budget) |
| PFS0 | germany | XETR | 55.1 | -8.01 | EUR | 4.3x | 59.90 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | live | none | 2026-11-18 (2d ago) | — | no catalyst lookup (outside the per-run budget) |
| G24 | germany | XETR | 80.8 | -7.97 | EUR | 6.1x | 87.80 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | live | none | 2025-08-07 (470d ago) | — | no catalyst lookup (outside the per-run budget) |
| AIXA | germany | XETR | 29.99 | -7.75 | EUR | 1.9x | 32.51 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | live | none | 2026-10-29 (22d ago) | — | no catalyst lookup (outside the per-run budget) |
| JACK | norway | OSL | 6.18 | +7.67 | NOK | 7.7x | 5.74 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | live | none | 2026-08-25 (87d ago) | N | Hunter Group unit HG Projectco 1 placed a conditional cash purchase order for all Jacktel shares at NOK 6.30, an 8.6% premium to the 18 Nov close, extended to 22:00 CET on 20 Nov; the release also carried preliminary Q3 revenue of USD 19.0m |
| SMG | switzerland | SIX | 27.85 | -7.63 | CHF | 4.8x | 30.15 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | live | none | 2026-08-25 (87d ago) | — | no catalyst lookup (outside the per-run budget) |
| HEM | sweden | OMXSTO | 46.6 | -7.54 | SEK | 2.1x | 50.40 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | live | none | 2026-10-22 (29d ago) | N | JPMorgan downgraded Hemnet to Neutral from Overweight and cut its target to SEK 49, an eighth straight daily fall; October net sales were down 24.5% |
| AMS2 | austria | VIE | 13.75 | -7.09 | EUR | 1.6x | 14.80 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | live | none | 2026-11-13 (7d ago) | — | no catalyst lookup (outside the per-run budget) |
| GOMX | sweden | OMXSTO | 13.15 | -6.94 | SEK | 1.6x | 14.13 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | live | none | 2026-08-26 (86d ago) | — | no catalyst lookup (outside the per-run budget) |
| CTEK | sweden | OMXSTO | 15.82 | +6.89 | SEK | 2.5x | 14.80 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | live | none | 2026-10-29 (22d ago) | — | no catalyst lookup (outside the per-run budget) |
| NOKIA | finland | OMXHEX | 6.634 | -6.19 | EUR | 2.0x | 7.07 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | live | ADR (NYSE:NOK) | 2026-10-22 (29d ago) | — | no catalyst lookup (outside the per-run budget) |
| ASML | netherlands | EURONEXT | 1209 | -6.15 | EUR | 2.2x | 1288.20 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | live | ADR (NASDAQ:ASML) | 2026-10-14 (37d ago) | N | No issuer news: the shares fell 6.3% with the European AI and semiconductor complex after the 19 Nov US session's AI selloff (AMD -7.7%), with the US export-control overhang still in the price |
| KGX | germany | GETTEX | 29.5 | -6.14 | EUR | 3.3x | 31.38 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | live | none | 2026-10-27 (24d ago) | — | no catalyst lookup (outside the per-run budget) |
| ZAP | norway | OSL | 55.3 | -6.11 | NOK | 2.5x | 58.90 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | live | none | 2026-11-04 (16d ago) | — | no catalyst lookup (outside the per-run budget) |
| PKO | poland | GPW | 110.54 | -5.96 | PLN | 4.0x | 117.54 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | live | none | 2026-11-05 (15d ago) | — | no catalyst lookup (outside the per-run budget) |
| SEL | poland | GPW | 54.2 | -5.90 | PLN | 5.7x | 57.60 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | live | none | 2026-11-20 (0d ago) | Y | Q3 profit fell y/y on cost pressure (reported 2026-11-20): net profit PLN 44.0m vs PLN 59.6m and EPS PLN 2.03, even as revenue rose 25.7% to PLN 629.9m |
| TPRO | italy | MIL | 19.11 | -5.86 | EUR | 1.5x | 20.30 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | live | none | 2026-08-05 (107d ago) | — | no catalyst lookup (outside the per-run budget) |
| HUBN | switzerland | SIX | 157.8 | -5.85 | CHF | 2.8x | 167.60 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | live | none | 2026-08-18 (94d ago) | — | no catalyst lookup (outside the per-run budget) |
| PRY | italy | MIL | 101.05 | -5.78 | EUR | 2.2x | 107.25 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | live | none | 2026-10-29 (22d ago) | — | no catalyst lookup (outside the per-run budget) |
| HEX | norway | OSL | 11.49 | -5.59 | NOK | 2.5x | 12.17 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | live | none | 2026-11-06 (14d ago) | — | no catalyst lookup (outside the per-run budget) |
| CRI | poland | GPW | 659 | -5.59 | PLN | 2.8x | 698.00 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | live | none | 2026-09-28 (53d ago) | — | no catalyst lookup (outside the per-run budget) |
| CGEO | uk | LSE | 4270 | -5.53 | GBX | 2.6x | 4520.00 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | live | none | — | — | no catalyst lookup (outside the per-run budget) |
| WRT1V | finland | OMXHEX | 23.71 | -5.50 | EUR | 2.5x | 25.09 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | live | none | 2026-10-27 (24d ago) | — | no catalyst lookup (outside the per-run budget) |
| ASM | netherlands | EURONEXT | 651.6 | -5.46 | EUR | 1.6x | 689.20 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | live | US line (OTC:ASMXF) | 2026-10-27 (24d ago) | — | no catalyst lookup (outside the per-run budget) |
| IFCN | switzerland | SIX | 149.6 | -5.44 | CHF | 2.1x | 158.20 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | live | none | 2026-07-30 (113d ago) | — | no catalyst lookup (outside the per-run budget) |
| DIG | poland | GPW | 268.6 | -5.42 | PLN | 2.3x | 284.00 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | live | none | 2026-09-07 (74d ago) | — | pending catalyst lookup |

## AU (ASX) — Headline table

| Ticker | Venue | Close | Chg % | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | Session asof | Settle | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MP1 | ASX | 14.94 | -12.89 | AUD | 3.0x | 17.15 | yahoo_chart_daily | 2026-11-18 | 2026-11-20 | settled | none | 2026-08-19 (93d ago) | N | AGM on 20 Nov 2026: the remuneration report drew a first strike with 57.96% of votes against, and the market read the governance outcome against the reiterated FY27 outlook |
| PRN | ASX | 1.66 | -11.23 | AUD | 3.8x | 1.87 | yahoo_chart_daily | 2026-11-18 | 2026-11-20 | settled | none | 2026-08-20 (92d ago) | N | ASX release 20 Nov 2026: CFO Michael Ellis to leave for MinRes with Simon Franich named successor; shares hit a 52-week low A$1.66 after the A$1b Geita contract award on 17 Nov |
| TEA | ASX | 7.61 | -9.62 | AUD | 3.1x | 8.42 | yahoo_chart_daily | 2026-11-18 | 2026-11-20 | settled | none | 2026-08-26 (86d ago) | — | no catalyst lookup (outside the per-run budget) |
| ZIP | ASX | 1.685 | -9.41 | AUD | 2.2x | 1.86 | yahoo_chart_daily | 2026-11-18 | 2026-11-20 | settled | none | 2026-08-19 (93d ago) | — | no catalyst lookup (outside the per-run budget) |

## APAC/Gulf — Headline table

| Ticker | Market | Venue | Close | Chg % | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | Session asof | Settle | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NTBK | indonesia | IDX | 64 | +30.61 | IDR | 5.2x | 49.00 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| MASB | indonesia | IDX | 2670 | +24.77 | IDR | 5.9x | 2140.00 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| YUPI | indonesia | IDX | 1240 | +24.62 | IDR | 3.4x | 995.00 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| ASCENSIVE | india | BSE | 17.1 | +20.00 | INR | 12.7x | 14.25 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| 301313 | china | SZSE | 59.16 | +20.00 | CNY | 3.0x | 49.30 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| 300812 | china | SZSE | 18 | +20.00 | CNY | 5.3x | 15.00 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| YAASHVI | india | BSE | 93.85 | +20.00 | INR | 5.7x | 78.21 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| OAL | india | NSE | 516.7 | +20.00 | INR | 5.1x | 430.60 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| 301132 | china | SZSE | 51.07 | +20.00 | CNY | 2.9x | 42.56 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| MGI | thailand | SET | 2.6 | -10.96 | THB | 3.6x | 2.92 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| KCE | thailand | SET | 50.5 | -10.62 | THB | 2.4x | 56.50 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | settled | none | 2026-11-05 (15d ago) | N | No issuer news in the 20 Nov session: Thai electronics were hit by the global tech risk-off (SET -1.3%), and the 5 Nov Q3 filing had shown net profit of THB 484.6m, +63% |
| AWX | singapore | SGX | 5.69 | -9.68 | SGD | 1.7x | 6.30 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | settled | none | 2026-08-12 (100d ago) | — | no catalyst lookup (outside the per-run budget) |
| ALT | thailand | SET | 1.35 | -9.40 | THB | 3.5x | 1.49 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | settled | none | 2026-11-06 (14d ago) | N | No issuer news in the 20 Nov session: -9.4% to THB 1.35 in the global tech sell-off (SET -1.3%) after a +20% run, on thin small-cap liquidity; the 6 Nov Q3 filing showed net profit of THB 95.0m |
| MIM | singapore | SGX | 1 | -9.09 | SGD | 1.2x | 1.10 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| 5E2 | singapore | SGX | 1.56 | -8.77 | SGD | 4.6x | 1.71 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | settled | none | 2026-07-30 (113d ago) | — | no catalyst lookup (outside the per-run budget) |
| 4144 | ksa | TADAWUL | 73 | -5.13 | SAR | 1.1x | 76.95 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| 8200 | ksa | TADAWUL | 28 | -5.08 | SAR | 1.5x | 29.50 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | settled | none | 2026-11-01 (19d ago) | — | no catalyst lookup (outside the per-run budget) |
| 4004 | ksa | TADAWUL | 56.1 | -4.35 | SAR | 2.0x | 58.65 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | settled | none | 2026-11-03 (17d ago) | — | no catalyst lookup (outside the per-run budget) |
| SPK | newzealand | NZX | 2.14 | -3.60 | NZD | 2.8x | 2.22 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | settled | none | 2026-08-20 (92d ago) | N | No issuer news in the 20 Nov session: -3.6% in the global sell-off (NZX50 -1.0%), with the last company news the 12 Nov reply to an open letter on classifying the data-centre gain in the FY26 accounts |
| FCG | newzealand | NZX | 5.14 | -3.20 | NZD | 3.0x | 5.31 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | settled | none | 2026-03-23 (242d ago) | — | no catalyst lookup (outside the per-run budget) |
| GNE | newzealand | NZX | 2.41 | -2.82 | NZD | 2.7x | 2.48 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | settled | none | 2026-08-26 (86d ago) | — | no catalyst lookup (outside the per-run budget) |

## Source health

- scanner_calls: 57 | scanner_errors: 0
- markets_scanned: US + 17 EU/UK + ASX + 7 APAC/Gulf (india, thailand, indonesia, china, singapore, newzealand, ksa)
- pipeline_version: 2026-11-20.1
- et_clock: zoneinfo America/New_York (DST-aware; a fixed UTC-4 mislabels every winter fire)
- premarket_window: 04:00-09:30 ET, resolved with zoneinfo (09:00-14:30 UTC in winter, 08:00-13:30 UTC in summer)
- session_selection: by DATE and order, never by a modal time-of-day. Yahoo stamps a daily bar at the session open, so the ET stamp of the SAME session shifts by one hour across a DST boundary; a modal filter kept the OLDER bars and discarded the NEWEST ones, which rolled the base back to the prior-prior session (66 US + 21 ASX rows lost on 2026-11-03, 24 of 25 ASX rows lost on 2026-11-04).
- yahoo_calls: 204 | yahoo_429: 0 | yahoo_errors: 1 | yahoo_breaker: closed
- reference_close (screener vs Yahoo, resolved BEFORE the tables were built): agree=191 mismatch=1 unverified=2 stale_reference=1
  method: the screener's implied reference close (close / (1 + change/100)) is compared
  with Yahoo's own reference close. A match proves the move was measured against the
  TRUE prior close; a mismatch means the row sits on a STALE reference (phantom move).
  Coverage: every row of the US headline, US QUIET, EU/UK and ASX tables is checked.
  Yahoo bar mode: {"closed": 161, "live": 30} (closed = last completed session bar;
  live = in-progress EU/UK session bar, which is what a weekday 08:00 ET EU move needs)
  live drift between the screener snapshot and the later Yahoo print: median=0.00pp max=1.62pp (expected on a live market)
- cross_check mismatches: [{"region": "US", "symbol": "SNDK", "tv": 0, "yahoo": -2.713, "delta": 2.713, "ref_delta_pct": -2.713, "tv_implied_ref": 94.395, "yahoo_ref": 97.0275, "yahoo_date": "2026-11-19", "yahoo_ref_date": "2026-11-18", "verdict": "stale_reference"}]
- rows_dropped_stale_ref: 1 (rows whose screener-implied reference close disagreed with Yahoo's by more than 0.5%; they are dropped, not published)
- rows_dropped_unresolved_ref: 2 (rows whose reference close could not be resolved from Yahoo at all - the base of the move is unverifiable, so the row is dropped rather than published with a '—' base)
- us_premarket_check (Yahoo 1-min pre/post feed vs the screener pre-market column, base = the IMMEDIATELY prior session's close): checked=10 within_1pp=8 within_3pp=9 unavailable=0
  us_premarket outliers (>3pp; thin pre-market books, not a screener error): [{"symbol": "CAPR", "tv": 15.007, "yahoo": 10.853, "delta": 4.154, "yahoo_asof": "08:14"}]
- markets_with_lt5_rows: ['uk:egreater=0', 'germany:egreater=3', 'france:egreater=0', 'netherlands:egreater=0', 'belgium:egreater=0', 'belgium:less=4', 'portugal:egreater=0', 'portugal:less=0', 'ireland:egreater=0', 'ireland:less=1', 'italy:egreater=0', 'switzerland:egreater=0', 'spain:egreater=0', 'sweden:egreater=1', 'norway:egreater=1', 'denmark:egreater=1', 'finland:egreater=0', 'poland:egreater=2', 'austria:egreater=0', 'greece:egreater=0', 'thailand:egreater=4', 'singapore:egreater=0', 'newzealand:egreater=0', 'ksa:egreater=1']
  NOTE: this fires per market AND direction, so it is NOT a coverage-failure signal on
  its own. A 'less' count of 0-3 means almost nothing fell more than 2.5% that session
  (a broad up-day); a small 'egreater' count usually means a small market with few
  names above the $1B market-cap floor. Check the median change before calling it a gap.
- filters: volume>10000 (removes stale-reference rows), country=home for EU/UK/AU,
  exchange drop-list for US, US venue allow-list, US preferred (slash ticker) excluded
- pass_b2 (US pre-market gap scan - "gapped today, flat yesterday"): candidates=36 deduped_against_pass_a_b=12 published=23 (up=4 down=32)
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
- bod_no_extended_hours: 77 (deferred to the next scan; not in the headline table)
- earnings_source: screener `earnings_release_date` (last FULL report) + `earnings_release_next_date` (next scheduled)
- earnings_caveat: `earnings_release_date` does NOT capture preliminary, guidance or
  restructuring releases. On 2026-10-23 LKQ fell 22.47% on a preliminary Q3 miss while
  the field still read 2026-07-30. ALWAYS confirm the earnings-driven flag against the
  headline itself; the calendar field is a screen, not a verdict.
- us_line_index: ok (US-listed lines for the 25 foreign home countries, both scanner types; the `US tradeable` column is ADR / US-listed / none)
- catalyst_note: Catalyst lookups: 5 US + 6 EU + 2 AU + 3 APAC/Gulf = 16 per run - the skill's cap, allocated by the evidence gap.
- catalyst_merge: region-matched - a row may only use a catalog entry from its OWN region;
  the same ticker on another venue is a different company and is not used.
- catalyst_budget: 6 US + 5 EU + 2 AU + 3 APAC/Gulf = 16 lookups per run (cap 16), allocated by the evidence gap: the US slice covers the rows whose earnings event can still explain today's move, the EU/AU/APAC floors are never squeezed because no bulk calendar reaches those markets, and whatever the US slice does not need goes to the region with the most unexplained rows
- earnings_calendar: Nasdaq public earnings calendar (calls=8 errors=0 symbols=613) - the source of record for the US earnings date, and the ranking key for the search budget
- earnings_field_stale_rows: 0 (the screener's earnings_release_date disagreed with the calendar; the calendar's date is published)
- earnings_dates: the published `Last earnings` date by source - catalog (researched) 10, calendar 6, asx 0, screener 160. The chain is researched -> calendar (US) -> ASX feed (AU) -> the screener's field, which is the FALLBACK and the one that lags (2026-11-12: NBIS carried the previous quarter's date on the morning it reported, and MEKO, NORBT and FG carried July and August dates on the morning they all reported).
- asx_announcements: 2 results-classified announcement(s) for the last ASX session (calls=1 errors=0); the announcement date IS the report date, and the meeting/AGM/offer/assay headlines are excluded because they are not reports
- earnings_date_quality: 1 of 20 markets publish a FRESH earnings date (median age <= 14d); the table below gives each market's rows, the rows with NO date at all, the median age of the published date and the rows within 7 and 30 days - the reader sees the input quality instead of trusting it
| market | rows | no date | median age | <=7d | <=30d |
|---|---|---|---|---|---|
| au | 4 | 0 | 93d | 0 | 0 |
| austria | 2 | 0 | 15d | 1 | 2 |
| china | 3 | 3 | n/a | 0 | 0 |
| finland | 2 | 0 | 29d | 0 | 2 |
| france | 2 | 1 | 2d | 1 | 1 |
| germany | 4 | 0 | 24d | 1 | 3 |
| india | 3 | 3 | n/a | 0 | 0 |
| indonesia | 3 | 3 | n/a | 0 | 0 |
| italy | 2 | 0 | 107d | 0 | 1 |
| ksa | 3 | 1 | 19d | 0 | 2 |
| netherlands | 2 | 0 | 37d | 0 | 1 |
| newzealand | 3 | 0 | 92d | 0 | 0 |
| norway | 4 | 0 | 16d | 1 | 3 |
| poland | 4 | 0 | 53d | 1 | 2 |
| singapore | 3 | 1 | 113d | 0 | 0 |
| sweden | 4 | 0 | 85d | 0 | 2 |
| switzerland | 3 | 0 | 94d | 0 | 0 |
| thailand | 3 | 1 | 15d | 0 | 2 |
| uk | 1 | 1 | n/a | 0 | 0 |
| us | 121 | 2 | 17d | 13 | 100 |
- earnings_tiers: fresh=1 near=5 (fresh = the report is dated on the scan date, near = the previous session)
- one_table_rule: each name appears exactly once, in exactly one table, with its
  catalyst in that row's last column. There is no separate catalysts section.
- data_date: US regular session close of the prior trading day; extended-hours columns
  carry the prior session's prints
- settlement_state: 25 settled, 30 live (a live row's move is a mid-session snapshot, not the session's result)
- rows_per_market (EU/UK, cap 4/market): {'france': 4, 'sweden': 4, 'austria': 4, 'norway': 4, 'germany': 4, 'switzerland': 4, 'finland': 4, 'netherlands': 4, 'poland': 4, 'italy': 4, 'uk': 4, 'denmark': 4, 'greece': 4, 'spain': 4, 'belgium': 4, 'ireland': 1} — the cap stops one thin market taking the table; the EU/UK table was 28% Sweden over nine runs (73 of 264 rows) while Belgium and Greece never appeared once.
- rows_per_market (APAC/Gulf, cap 3/market): {'indonesia': 3, 'india': 3, 'china': 3, 'thailand': 3, 'singapore': 3, 'ksa': 3, 'newzealand': 3}
- deprecations: mcp__tradingview-advanced__*, mcp__tradingview__*, mcp__financekit__*,
  mcp__stocktwits__* are ABSENT in Cloud sessions (tool_search 0 hits; connector catalog
  holds only media + credential tools). The public screener replaces them.

- degraded_sources: 1
  (the chat reply's `errors:` MUST equal this number - one entry per degraded
  source, not one per run)
  1. yahoo_chart_api.reference_close_unresolved — ANT: the reference close could not be resolved (429 or a bad body)

## Audit line

`earnings-reaction target=earnings-reactions:2026-11-20 candidates=452 amc_reactions=0 pre_gaps=121 eu_reactions=30 asx_reactions=4 apac_reactions=20 catalyst_lookups=16 bod=77 pass_b2_candidates=36 pass_b2_dedup=12 pass_b2_published=23 earnings_calendar_rows=613 earnings_tiers_fresh=1 earnings_tiers_near=5 earnings_field_stale_rows=0 earnings_dates_catalog=10 earnings_dates_asx=0 asx_ann_rows=2 rows_dropped_stale_ref=1 rows_dropped_unresolved_ref=2 degraded_sources=1`
