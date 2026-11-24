# Earnings reaction scanner — 2026-11-24

- Cron: `0 8 * * 1-5` America/New_York (weekdays, 08:00 ET)
- Fire time (ET): 2026-11-24 08:09:24 Tue
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

- 0 AMC reactions, 159 pre-market gaps, 71 without extended-hours data; 28 EU/UK and 4 ASX movers, 17 APAC/Gulf movers.
- Pass B2 (the US pre-market gap scan) met the filter on 30 names (10 up, 20 down); 17 were already a Pass A/B row and are recorded as dedupes, and 13 reached a table.
- Biggest US extended-hours move: SHOE PRE_GAP (23.47%).
- Biggest EU/UK move: NDA (-11.66%, germany).
- Biggest ASX move: TUA (+32.35%).
- Biggest APAC/Gulf move: AREA (+24.51%, indonesia).
- 0 of the 28 EU/UK rows are SETTLED and 28 are LIVE (mid-session). The 12:15 ET settlement pass publishes where those
  live moves actually closed.
- EU/AU/APAC earnings-driven tagging is keyword-based on headlines (best-effort). A row
  whose lookup was not performed carries NO verdict — only a researched row does.

## Actionable read

- **Move vs this name's own history.** The `Move vs avg daily` column divides the
  reaction by the name's own mean absolute daily move over its last
  20 completed sessions. A -27% move in a name that averages +-3% is a
  different event from a -8% move in a name that averages +-7%.
- **US-listed and tradeable vs foreign-only.** 174 published US rows are on a
  US venue; 1 more foreign reactions have a US ADR line
  (the `US tradeable` column carries the ticker); 31 are foreign-only and
  cannot be bought directly by a US reader.
- **Not yet fully priced — US (hypothesis, not a recommendation).**
  SHOE — -23.47%, 3.52% mean absolute daily move over the last 20 completed sessions, 6.7x that average, reference close 14.26 dated 2026-11-20, US access: US-listed, the move now (-23.47%) is larger than the move it follows (-0.49%); the reaction is still being repriced. Hypothesis only: this artifact states no
  direction and no trade.
- **Not yet fully priced — EU/UK (hypothesis, not a recommendation).**
  MUR — -9.35%, 1.05% mean absolute daily move over the last 20 completed sessions, 8.9x that average, reference close 38.50 dated 2026-11-23, US access: none, the move now (-9.35%) is larger than the move it follows (+1.45%); the reaction is still being repriced. Hypothesis only: this artifact states no
  direction and no trade.
- **Not yet fully priced — AU (ASX) (hypothesis, not a recommendation).**
  TUA — +32.35%, 4.26% mean absolute daily move over the last 20 completed sessions, 7.6x that average, reference close 1.36 dated 2026-11-22, US access: none, the move now (+32.35%) is larger than the move it follows (-2.16%); the reaction is still being repriced. Hypothesis only: this artifact states no
  direction and no trade.

## US — Headline table

| Ticker | Venue | Close | Chg % | Pre-mkt % | Post-mkt % | Move vs avg daily | Ref close | Ref source | Ref asof | US tradeable | Last earnings | Tag | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SHOE | NASDAQ | 14.19 | -0.49 | -23.47 | — | 6.7x | 14.26 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-24 (0d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| DKS | NYSE | 133.67 | 1.07 | 17.50 | — | 5.8x | 132.25 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-24 (0d ago) | PRE_GAP | Y | Q3 FY2026 (quarter ended 2026-10-31) reported 2026-11-24: net sales $5.13B +23.2% as Foot Locker contributed, GAAP EPS $1.87 and non-GAAP EPS $1.94 (vs $2.07 a year earlier); FY26 GAAP EPS guidance raised to $11.40-$12.25 (reported 2026-11-24) |
| FLNC | NASDAQ | 3.8 | 9.83 | 16.84 | — | 2.7x | 3.46 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-23 (1d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-23 (Nasdaq earnings calendar; no headline lookup), consensus EPS ($0.54) |
| INSM | NASDAQ | 149.09 | 5.49 | 14.59 | — | 3.5x | 141.33 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-10-29 (26d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MWH | NASDAQ | 27.12 | 9.84 | -13.35 | — | 3.1x | 24.69 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-12 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| EMBC | NASDAQ | 5.745 | -4.57 | 13.14 | — | 5.6x | 6.02 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-24 (0d ago) | PRE_GAP | Y | Q4 FY2026 (quarter ended 2026-09-30) reported 2026-11-24: revenue $298.7M +13.1% (organic +3.1%), GAAP EPS $1.17, adjusted EPS $0.72 vs $0.31 consensus; initial FY2027 guidance issued (reported 2026-11-24) |
| ANF | NYSE | 140.45 | 1.83 | 11.93 | — | 4.2x | 137.92 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-24 (0d ago) | PRE_GAP | Y | Q3 FY2026 (quarter ended 2026-10-31) reported 2026-11-24: record net sales $1.4B +11% (comps +6%), operating margin 15.5%, EPS $3.82 vs $3.09 consensus; FY26 EPS guidance raised to $13.70-$13.90 (reported 2026-11-24) |
| SMTC | NASDAQ | 104.13 | 18.83 | -11.84 | — | 1.5x | 87.63 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-23 (1d ago) | PRE_GAP | — | Q4 2026 results, report date 2026-11-23 (Nasdaq earnings calendar; no headline lookup), consensus EPS $0.92 |
| HPE | NYSE | 48.02 | 17.38 | -11.22 | — | 2.4x | 40.91 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-23 (1d ago) | PRE_GAP | — | Q4 2026 results, report date 2026-11-23 (Nasdaq earnings calendar; no headline lookup), consensus EPS $1.18 |
| ADI | NASDAQ | 378.75 | 9.49 | -9.44 | — | 2.9x | 345.92 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-24 (0d ago) | PRE_GAP | Y | Q4 FY2026 (quarter ended 2026-10-31) reported 2026-11-24: revenue $4.37B +42%, adjusted EPS $4.06 vs $3.89 consensus and above the top of its own range, but Q1 FY27 guided to $4.4B revenue and $3.82 adjusted EPS, below the Q4 level (reported 2026-11-24) |
| KSS | NYSE | 21.2 | -4.72 | 8.73 | — | 2.6x | 22.25 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-24 (0d ago) | PRE_GAP | Y | Q3 FY2026 (quarter ended 2026-10-31) reported 2026-11-24: net sales $3.45B +1.3% with comps +1.2%, GAAP EPS $2.15 including a $1.16 tax benefit and $0.28 of tariff refunds; FY26 EPS guidance raised to $4.30-$4.50 (reported 2026-11-24) |
| CHRN | NASDAQ | 8.99 | 13.08 | 8.34 | — | 1.1x | 7.95 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-10-15 (40d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| DLTR | NASDAQ | 139.1 | 0.83 | 7.48 | — | 2.6x | 137.96 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-24 (0d ago) | PRE_GAP | Y | Q3 FY2026 (quarter ended 2026-10-31) reported 2026-11-24: net sales $5.1B +6.9% with comps +4.6% (traffic +3.8%), adjusted EPS $1.16 including a $0.42 tariff-reinvestment cost, operating margin down 110bp; FY26 adjusted EPS outlook raised to $8.05-$8.25 (reported 2026-11-24) |
| NEXA | NYSE | 10.4 | 9.70 | -7.34 | — | 2.2x | 9.48 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-10-29 (26d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FORM | NASDAQ | 81.57 | 11.71 | -6.77 | — | 0.9x | 73.02 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-10-28 (27d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ACMR | NASDAQ | 45.17 | 13.49 | -6.63 | — | 1.1x | 39.80 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-05 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMTM | NYSE | 20.65 | 1.52 | 6.54 | — | 3.6x | 20.34 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-23 (1d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-23 (Nasdaq earnings calendar; no headline lookup), consensus EPS $0.63 |
| VICR | NASDAQ | 142.04 | 13.55 | -6.36 | — | 1.0x | 125.09 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-10-20 (35d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BURL | NYSE | 235.16 | -4.15 | 6.31 | — | 2.7x | 245.34 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-24 (0d ago) | PRE_GAP | Y | Q3 FY2026 (quarter ended 2026-10-31) reported 2026-11-24: total sales +8% but comps only +1% at the low end of guidance, adjusted EPS $1.73 above the high end of guidance; Q4 adjusted EPS guidance cut $0.20 for fuel and freight, FY26 adjusted EPS $11.70-$11.80 (reported 2026-11-24) |
| MXL | NASDAQ | 50.31 | 21.38 | -6.24 | — | 0.8x | 41.45 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-10-22 (33d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BBY | NYSE | 97 | -0.97 | 6.19 | — | 2.6x | 97.95 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-24 (0d ago) | PRE_GAP | Y | Q3 FY27 (quarter ended 2026-10-31) reported 2026-11-24: revenue $10.24B +5.8%, comps +6.1% vs +2.3% expected, adjusted EPS $1.62; FY27 comp guidance raised to 3.4%-4.0% and adjusted EPS to $6.90-$7.05 (reported 2026-11-24) |
| ALGM | NASDAQ | 29.3 | 14.63 | -6.14 | — | 1.1x | 25.56 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-10-29 (26d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MU | NASDAQ | 707.7 | 19.04 | -5.92 | — | 0.9x | 594.51 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-09-30 (55d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| INTC | NASDAQ | 59.66 | 16.34 | -5.90 | — | 0.9x | 51.28 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-10-29 (26d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BTDR | NASDAQ | 3.39 | 14.72 | -5.90 | — | 0.6x | 2.96 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-10 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| DELL | NYSE | 334.91 | 20.46 | -5.89 | — | 0.9x | 278.02 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-24 (0d ago) | PRE_GAP | — | Q4 2026 results, report date today (Nasdaq earnings calendar; no headline lookup), consensus EPS $6.55 |
| AXTI | NASDAQ | 38.02 | 24.37 | -5.60 | — | 0.6x | 30.57 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-10-29 (26d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GRRR | NASDAQ | 7.59 | 44.43 | -5.53 | — | 0.5x | 5.25 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-19 (5d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-19 (Nasdaq earnings calendar; no headline lookup), consensus EPS ($0.24) |
| AMKR | NASDAQ | 34.81 | 15.11 | -5.49 | — | 0.9x | 30.24 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-10-26 (29d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RMBS | NASDAQ | 75.68 | 14.06 | -5.46 | — | 1.1x | 66.35 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-10-26 (29d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AEHR | NASDAQ | 48.51 | 21.76 | -5.44 | — | 0.6x | 39.84 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-02 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| KYMR | NASDAQ | 150.37 | 30.40 | 5.41 | — | 1.3x | 115.31 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-10-29 (26d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TER | NASDAQ | 233.51 | 14.03 | -5.36 | — | 0.9x | 204.78 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-10-27 (28d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ONTO | NYSE | 190.99 | 12.24 | -5.23 | — | 0.8x | 170.16 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-09 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NVTS | NASDAQ | 7.33 | 20.56 | -5.18 | — | 0.7x | 6.08 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-03 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ICHR | NASDAQ | 31.6 | 15.84 | -5.09 | — | 0.8x | 27.28 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-02 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TECK | NYSE | 52.3 | 7.85 | -5.05 | — | 1.4x | 48.48 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-10-29 (26d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| WOLF | NYSE | 20.67 | 7.54 | -5.03 | — | 0.7x | 19.22 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-04 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| OUST | NASDAQ | 27.9 | 17.23 | -5.02 | — | 0.7x | 23.80 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-03 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SITM | NASDAQ | 438.82 | 21.48 | -4.98 | — | 0.7x | 361.24 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-04 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MKSI | NASDAQ | 205.33 | 11.28 | -4.98 | — | 1.0x | 184.52 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-04 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| P | NYSE | 101.01 | 9.73 | -4.96 | — | 1.0x | 92.05 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-18 (6d ago) | PRE_GAP | — | Q4 2026 results, report date 2026-11-18 (Nasdaq earnings calendar; no headline lookup), consensus EPS $0.28 |
| VSH | NYSE | 24.81 | 10.96 | -4.96 | — | 0.9x | 22.36 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-04 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BE | NYSE | 168.15 | 18.04 | -4.94 | — | 0.7x | 142.39 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-10-22 (33d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FN | NYSE | 329.22 | 15.50 | -4.93 | — | 0.7x | 285.04 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-02 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| DIOD | NASDAQ | 82.56 | 13.17 | -4.92 | — | 0.9x | 72.95 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-05 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LITE | NASDAQ | 544.38 | 18.20 | -4.83 | — | 0.6x | 460.54 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-02 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| WDC | NASDAQ | 297.25 | 13.84 | -4.81 | — | 0.8x | 261.11 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-10-22 (33d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| UCTT | NASDAQ | 41.175 | 11.28 | -4.80 | — | 0.7x | 37.00 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-10-27 (28d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SANM | NASDAQ | 153.88 | 10.10 | -4.80 | — | 1.0x | 139.76 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-09 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CRDO | NASDAQ | 122.46 | 22.63 | -4.79 | — | 0.6x | 99.86 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-09-01 (84d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| VIAV | NASDAQ | 29.66 | 11.04 | -4.79 | — | 0.8x | 26.71 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-04 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PENG | NASDAQ | 42.24 | 17.17 | -4.73 | — | 0.6x | 36.05 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-10-06 (49d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ENTG | NASDAQ | 142.06 | 14.08 | -4.65 | — | 0.9x | 124.53 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-10-29 (26d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| COHU | NASDAQ | 41.99 | 12.54 | -4.64 | — | 0.7x | 37.31 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-10-28 (27d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| VRT | NYSE | 186.35 | 12.10 | -4.64 | — | 0.7x | 166.24 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-10-28 (27d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ALAB | NASDAQ | 222.12 | 23.16 | -4.61 | — | 0.6x | 180.35 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-03 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CRWV | NASDAQ | 48.33 | 22.32 | -4.57 | — | 0.5x | 39.51 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-10 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NVDA | NASDAQ | 165.05 | 31.48 | -4.57 | — | 0.9x | 125.53 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-17 (7d ago) | PRE_GAP | — | Q4 2026 results, report date 2026-11-17 (Nasdaq earnings calendar; no headline lookup), consensus EPS $2.47 |
| MRVL | NASDAQ | 144.74 | 18.37 | -4.57 | — | 0.6x | 122.28 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-08-27 (89d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LRCX | NASDAQ | 209.76 | 14.45 | -4.45 | — | 0.8x | 183.27 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-10-21 (34d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ANT | NASDAQ | 87.64 | -1.43 | -4.44 | — | 0.9x | 88.91 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-02 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SCCO | NYSE | 143.32 | 6.94 | -4.41 | — | 1.3x | 134.02 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-10-21 (34d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TTMI | NASDAQ | 68.57 | 16.52 | -4.39 | — | 0.6x | 58.85 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-10-22 (33d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AVEX | NYSE | 12.12 | 9.78 | -4.35 | — | 0.6x | 11.04 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-11 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| APLD | NASDAQ | 13.82 | 20.28 | -4.34 | — | 0.6x | 11.49 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-10-07 (48d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MTSI | NASDAQ | 231.3 | 18.67 | -4.31 | — | 0.7x | 194.91 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-05 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| KLIC | NASDAQ | 61.54 | 12.48 | -4.26 | — | 0.8x | 54.71 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-18 (6d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-18 (Nasdaq earnings calendar; no headline lookup), consensus EPS $1.31 |
| IREN | NASDAQ | 14.64 | 23.86 | -4.23 | — | 0.4x | 11.82 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-05 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| WULF | NASDAQ | 10.91 | 10.76 | -4.22 | — | 0.6x | 9.85 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-06 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LSCC | NASDAQ | 112.95 | 14.89 | -4.21 | — | 0.8x | 98.31 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-02 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SYM | NASDAQ | 34.97 | 12.44 | -4.20 | — | 1.4x | 31.10 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-23 (1d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-23 (Nasdaq earnings calendar; no headline lookup), consensus EPS $0.08 |
| TXN | NASDAQ | 291.19 | 10.40 | -4.18 | — | 1.3x | 263.75 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-10-21 (34d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CLSK | NASDAQ | 5.53 | 13.09 | -4.16 | — | 0.5x | 4.89 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-24 (0d ago) | PRE_GAP | — | Q3 2026 results, report date today (Nasdaq earnings calendar; no headline lookup), consensus EPS ($0.36) |
| VECO | NASDAQ | 37.24 | 9.82 | -4.14 | — | 1.0x | 33.91 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-04 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| DOCN | NYSE | 78.98 | 18.30 | -4.09 | — | 0.7x | 66.76 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-03 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| KLAC | NASDAQ | 145.85 | 14.96 | -4.08 | — | 0.8x | 126.87 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-10-28 (27d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CAMT | NASDAQ | 100.1 | 12.22 | -4.03 | — | 0.8x | 89.20 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-04 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AEIS | NASDAQ | 214.07 | 12.56 | -4.00 | — | 0.7x | 190.18 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-02 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| HBM | NYSE | 17.88 | 10.40 | -4.00 | — | 1.0x | 16.19 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-12 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMAT | NASDAQ | 346.87 | 14.62 | -4.00 | — | 0.8x | 302.63 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-12 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BELFA | NASDAQ | 170.81 | 10.46 | -3.98 | — | 0.8x | 154.64 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-10-28 (27d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TSEM | NASDAQ | 136.81 | 18.39 | -3.97 | — | 0.6x | 115.56 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-02 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CORZ | NASDAQ | 12.36 | 9.09 | -3.96 | — | 0.6x | 11.33 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-05 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MCHP | NASDAQ | 61.22 | 10.43 | -3.95 | — | 1.0x | 55.44 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-05 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| HUT | NASDAQ | 51.37 | 11.80 | -3.95 | — | 0.5x | 45.95 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-04 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MARA | NASDAQ | 5.58 | 9.73 | -3.92 | — | 0.6x | 5.09 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-09 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SMCI | NASDAQ | 24.53 | 13.30 | -3.91 | — | 0.7x | 21.65 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-03 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NVMI | NASDAQ | 311.44 | 10.89 | -3.87 | — | 1.0x | 280.86 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-05 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| STX | NASDAQ | 520.1 | 13.80 | -3.85 | — | 0.7x | 457.01 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-10-27 (28d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GLW | NYSE | 108.31 | 14.76 | -3.84 | — | 0.8x | 94.38 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-10-27 (28d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ON | NASDAQ | 66.77 | 9.75 | -3.77 | — | 1.0x | 60.84 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-02 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ACLS | NASDAQ | 100.5 | 11.35 | -3.77 | — | 0.8x | 90.26 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-05 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| COHR | NYSE | 215.81 | 15.27 | -3.77 | — | 0.5x | 187.22 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-04 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BSP | NASDAQ | 47.27 | 15.15 | -3.74 | — | 1.3x | 41.05 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-19 (5d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-19 (Nasdaq earnings calendar; no headline lookup), consensus EPS $0.26 |
| AMD | NASDAQ | 453.46 | 6.85 | -3.70 | — | 0.5x | 424.39 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-03 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PLPC | NASDAQ | 276.19 | 11.92 | -3.69 | — | 0.7x | 246.78 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-10-28 (27d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CIEN | NYSE | 264.73 | 12.95 | -3.68 | — | 0.6x | 234.37 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-09-03 (82d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GFS | NASDAQ | 38.95 | 9.53 | -3.67 | — | 0.9x | 35.56 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-04 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMSC | NASDAQ | 21.29 | 10.43 | -3.66 | — | 0.9x | 19.28 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-04 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FPS | NYSE | 20.3 | 12.78 | -3.65 | — | 0.4x | 18.00 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-12 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| STRL | NASDAQ | 278.77 | 12.44 | -3.62 | — | 0.6x | 247.92 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-10-28 (27d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| QBTS | NASDAQ | 7.31 | 12.12 | -3.57 | — | 0.5x | 6.52 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-10 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ANET | NYSE | 178.31 | 6.35 | -3.54 | — | 0.7x | 167.62 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-03 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CGNX | NASDAQ | 48.47 | 9.27 | -3.51 | — | 1.0x | 44.36 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-04 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NVT | NYSE | 111.92 | 9.90 | -3.49 | — | 0.7x | 101.84 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-10-30 (25d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| INOD | NASDAQ | 32.21 | 14.54 | -3.45 | — | 0.7x | 28.12 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-05 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ADEA | NASDAQ | 14.08 | 9.57 | -3.41 | — | 0.7x | 12.85 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-02 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RGTI | NASDAQ | 8.095 | 13.06 | -3.40 | — | 0.5x | 7.16 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-10 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CIFR | NASDAQ | 6.2 | 14.08 | -3.39 | — | 0.4x | 5.43 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-02 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NBIS | NASDAQ | 97.8 | 20.28 | -3.38 | — | 0.4x | 81.31 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-12 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MTRN | NYSE | 203.89 | 11.74 | -3.35 | — | 0.7x | 182.47 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-04 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FLEX | NASDAQ | 73.94 | 11.62 | -3.30 | — | 0.6x | 66.24 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-10-28 (27d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PURR | NASDAQ | 8.27 | 10.56 | -3.26 | — | 0.5x | 7.48 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-05 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| Q | NYSE | 114.68 | 10.83 | -3.24 | — | 0.9x | 103.47 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-04 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CBRS | NASDAQ | 98.51 | 19.16 | -3.21 | — | 0.4x | 82.67 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-12 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BELFB | NASDAQ | 218.48 | 11.25 | -3.19 | — | 0.7x | 196.38 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-10-28 (27d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AGX | NYSE | 295.31 | 9.81 | -3.15 | — | 0.6x | 268.94 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-09-02 (83d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AVGO | NASDAQ | 313.55 | 3.00 | -3.14 | — | 0.7x | 304.41 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-09-02 (83d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| POWL | NASDAQ | 161.98 | 9.31 | -3.07 | — | 0.6x | 148.18 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-16 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ECG | NYSE | 84.11 | 9.82 | -2.98 | — | 0.5x | 76.59 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-03 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PI | NASDAQ | 158.72 | 10.28 | -2.96 | — | 0.9x | 143.93 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-10-28 (27d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MPWR | NASDAQ | 1333.88 | 16.80 | -2.94 | — | 0.5x | 1142.05 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-10-29 (26d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ALM | NASDAQ | 7.17 | 12.21 | -2.93 | — | 0.6x | 6.39 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-12 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PLAB | NASDAQ | 26.47 | 10.15 | -2.91 | — | 0.8x | 24.03 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-08-26 (90d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CRS | NYSE | 277.03 | 9.07 | -2.90 | — | 0.8x | 254.00 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-10-22 (33d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SEI | NYSE | 61.23 | 12.07 | -2.89 | — | 0.5x | 54.67 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-04 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ORCL | NYSE | 113.68 | 12.34 | -2.89 | — | 0.6x | 101.19 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-09-10 (75d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LGN | NASDAQ | 36.45 | 12.81 | -2.88 | — | 0.4x | 32.31 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-12 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| IESC | NASDAQ | 170.92 | 9.52 | -2.88 | — | 0.6x | 156.06 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-20 (4d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-20 (Nasdaq earnings calendar; no headline lookup) |
| IONQ | NYSE | 23.34 | 12.64 | -2.87 | — | 0.4x | 20.72 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-05 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FIX | NYSE | 1158.53 | 11.13 | -2.81 | — | 0.5x | 1042.47 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-10-22 (33d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PDFS | NASDAQ | 35.34 | 16.10 | -2.80 | — | 0.4x | 30.44 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-05 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GLXY | NASDAQ | 12.55 | 11.85 | -2.79 | — | 0.3x | 11.22 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-10-27 (28d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| USAR | NASDAQ | 7.02 | 11.96 | -2.79 | — | 0.5x | 6.27 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-09 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| APH | NYSE | 77.41 | 10.99 | -2.78 | — | 0.7x | 69.72 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-10-28 (27d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ABSI | NASDAQ | 8.48 | 12.92 | -2.71 | — | 0.4x | 7.51 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-12 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MDT | NYSE | 100.72 | 0.78 | -2.70 | — | 2.1x | 99.94 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-24 (0d ago) | PRE_GAP | — | Q4 2026 results, report date today (Nasdaq earnings calendar; no headline lookup), consensus EPS $1.34 |
| KEYS | NYSE | 289.63 | 10.75 | -2.58 | — | 0.7x | 261.51 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-19 (5d ago) | PRE_GAP | — | Q4 2026 results, report date 2026-11-19 (Nasdaq earnings calendar; no headline lookup), consensus EPS $3.09 |
| NOW | NYSE | 91.72 | 4.63 | -2.53 | — | 0.6x | 87.61 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-10-28 (27d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMBQ | NYSE | 44.98 | 13.36 | -2.47 | — | 0.4x | 39.68 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-10 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| QCOM | NASDAQ | 165.38 | 10.30 | -2.35 | — | 0.6x | 149.94 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-04 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FIGR | NASDAQ | 26.17 | 9.77 | -2.33 | — | 0.5x | 23.84 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-12 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| XE | NASDAQ | 9.895 | 12.57 | -2.32 | — | 0.4x | 8.79 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-12 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MOD | NYSE | 137.39 | 10.20 | -2.31 | — | 0.3x | 124.67 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-03 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SHOP | NASDAQ | 134.3 | 8.55 | -2.30 | — | 0.6x | 123.72 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-03 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RKLB | NASDAQ | 49.63 | 9.27 | -2.28 | — | 0.4x | 45.42 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-09 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GEV | NYSE | 756.71 | 8.20 | -2.27 | — | 0.6x | 699.33 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-10-28 (27d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MYRG | NASDAQ | 272.74 | 10.10 | -2.21 | — | 0.6x | 247.71 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-10-28 (27d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ETN | NYSE | 336.34 | 8.03 | -2.18 | — | 0.6x | 311.33 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-03 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FTAI | NASDAQ | 163.56 | 9.03 | -2.18 | — | 0.4x | 150.02 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-10-29 (26d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NRG | NYSE | 97.72 | 11.30 | -2.17 | — | 0.6x | 87.80 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-09 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BMNR | NYSE | 14.42 | 11.09 | -2.15 | — | 0.4x | 12.98 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-10 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MNR | NYSE | 7.5 | -5.66 | 2.13 | — | 1.0x | 7.95 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-05 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PWR | NYSE | 609 | 8.94 | -2.13 | — | 0.5x | 559.03 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-10-29 (26d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| HWM | NYSE | 217.28 | 3.88 | -2.13 | — | 0.7x | 209.16 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-10-29 (26d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PLTR | NASDAQ | 159.36 | 11.06 | -2.11 | — | 0.6x | 143.49 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-02 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CRM | NYSE | 185.46 | 2.65 | -2.04 | — | 0.9x | 180.62 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-08-26 (90d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FSLY | NASDAQ | 16.28 | 9.19 | -2.03 | — | 0.3x | 14.91 | yahoo_chart_daily | 2026-11-20 | US-listed | 2026-11-04 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |

## US — QUIET one-liners

| Ticker | Venue | Chg % | Pre-mkt % | Post-mkt % | Move vs avg daily | Ref close | Ref source | Ref asof | US tradeable | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|
| BLSH | NYSE | 10.28 | -1.95 | — | 2.0x | 19.07 | yahoo_chart_daily | 2026-11-20 | US-listed | — | Q3 2026 results, report date 2026-11-18 (Nasdaq earnings calendar; no headline lookup), consensus EPS $0.08 |
| ZETA | NYSE | 9.89 | -1.94 | — | 2.3x | 29.51 | yahoo_chart_daily | 2026-11-20 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| COST | NASDAQ | -2.73 | -1.94 | — | 2.3x | 1102.15 | yahoo_chart_daily | 2026-11-20 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| TXG | NASDAQ | 11.29 | -1.93 | — | 1.9x | 51.80 | yahoo_chart_daily | 2026-11-20 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| CRSR | NASDAQ | 13.37 | -1.88 | — | 3.1x | 10.77 | yahoo_chart_daily | 2026-11-20 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| UEC | AMEX | 10.19 | -1.88 | — | 2.1x | 5.30 | yahoo_chart_daily | 2026-11-20 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| RDW | NYSE | 13.63 | -1.87 | — | 2.0x | 5.65 | yahoo_chart_daily | 2026-11-20 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| MDB | NASDAQ | 9.37 | -1.82 | — | 2.5x | 285.90 | yahoo_chart_daily | 2026-11-20 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| ECO | NYSE | -7.24 | 1.78 | — | 2.1x | 84.83 | yahoo_chart_daily | 2026-11-20 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| NET | NYSE | 5.88 | -1.77 | — | 1.2x | 274.96 | yahoo_chart_daily | 2026-11-20 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| MTZ | NYSE | 10.18 | -1.76 | — | 2.0x | 144.71 | yahoo_chart_daily | 2026-11-20 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| TENB | NASDAQ | 9.10 | -1.72 | — | 2.2x | 41.99 | yahoo_chart_daily | 2026-11-20 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| ASTS | NASDAQ | 10.31 | -1.71 | — | 1.5x | 23.27 | yahoo_chart_daily | 2026-11-20 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| CAT | NYSE | 7.17 | -1.71 | — | 2.1x | 510.45 | yahoo_chart_daily | 2026-11-20 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| PANW | NASDAQ | 2.94 | -1.62 | — | 0.9x | 343.32 | yahoo_chart_daily | 2026-11-20 | US-listed | — | Q4 2026 results, report date 2026-11-18 (Nasdaq earnings calendar; no headline lookup), consensus EPS $0.52 |

## EU/UK — Headline table

| Ticker | Market | Venue | Close | Chg % | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | Session asof | Settle | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NDA | germany | XETR | 112.1 | -11.66 | EUR | 6.0x | 126.90 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | live | none | 2026-08-06 (110d ago) | N | Aurubis cut its FY2026/27 earnings outlook on extended delays at its Richmond, Georgia copper smelter, knocking about 10% off the shares on 2026-11-23 and leaving them down further today |
| MUR | poland | GPW | 34.9 | -9.35 | PLN | 8.9x | 38.50 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | live | none | 2026-09-15 (70d ago) | N | Ex-dividend date 2026-11-24 with a PLN 2.94 dividend, roughly 7.6% of the 38.50 PLN reference close; next results are scheduled for 2026-11-25 |
| HUNT | norway | OSL | 20.75 | +8.64 | NOK | 2.0x | 19.10 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | live | none | 2026-11-20 (4d ago) | — | no catalyst lookup (outside the per-run budget) |
| SZG | germany | XETR | 42.66 | -8.53 | EUR | 2.4x | 46.64 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | live | none | 2026-11-12 (12d ago) | — | no catalyst lookup (outside the per-run budget) |
| EMEIS | france | EURONEXT | 10.97 | +8.08 | EUR | 4.2x | 10.15 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | live | none | 2026-07-29 (118d ago) | — | no catalyst lookup (outside the per-run budget) |
| TOM | norway | OSL | 80.4 | -7.80 | NOK | 5.4x | 87.20 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | live | none | 2026-10-23 (32d ago) | — | no catalyst lookup (outside the per-run budget) |
| FNM | sweden | OMXSTO | 114.5 | +7.51 | SEK | 2.0x | 106.50 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | live | none | 2026-11-11 (13d ago) | — | no catalyst lookup (outside the per-run budget) |
| SCST | sweden | OMXSTO | 177.2 | -7.32 | SEK | 5.4x | 191.20 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | live | none | 2026-10-20 (35d ago) | — | no catalyst lookup (outside the per-run budget) |
| VER | sweden | OMXSTO | 7.16 | -7.01 | SEK | 2.3x | 7.70 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | live | none | 2026-11-23 (1d ago) | — | no catalyst lookup (outside the per-run budget) |
| SOI | france | EURONEXT | 94.48 | -6.92 | EUR | 1.1x | 101.50 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | live | none | 2026-11-18 (6d ago) | — | no catalyst lookup (outside the per-run budget) |
| SAN | france | EURONEXT | 90.88 | +6.59 | EUR | 4.8x | 85.26 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | live | none | — | — | no catalyst lookup (outside the per-run budget) |
| COA | uk | LSE | 70.15 | -6.47 | GBX | 4.7x | 75.00 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | live | none | 2026-07-28 (119d ago) | — | no catalyst lookup (outside the per-run budget) |
| CLAS_B | sweden | OMXSTO | 517.5 | -6.33 | SEK | 4.7x | 552.50 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | live | none | 2026-09-03 (82d ago) | — | no catalyst lookup (outside the per-run budget) |
| ATS | austria | VIE | 103.4 | -6.17 | EUR | 1.1x | 110.20 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | live | none | 2026-11-05 (19d ago) | — | no catalyst lookup (outside the per-run budget) |
| TOR | poland | GPW | 50.2 | -6.17 | PLN | 3.6x | 53.50 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | live | none | 2026-08-20 (96d ago) | — | no catalyst lookup (outside the per-run budget) |
| ANTO | uk | LSE | 2599.5 | -6.12 | GBX | 2.0x | 2769.00 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | live | none | 2026-08-13 (103d ago) | — | no catalyst lookup (outside the per-run budget) |
| GENO | norway | OSL | 14.8 | -5.97 | NOK | 1.7x | 15.74 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | live | none | 2026-11-12 (12d ago) | — | no catalyst lookup (outside the per-run budget) |
| 1SXP | germany | XETR | 21 | -5.62 | EUR | 3.5x | 22.25 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | live | none | 2026-08-12 (104d ago) | — | no catalyst lookup (outside the per-run budget) |
| KGH | poland | GPW | 243.6 | -5.49 | PLN | 1.8x | 257.75 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | live | none | 2026-11-17 (7d ago) | — | no catalyst lookup (outside the per-run budget) |
| CRI | poland | GPW | 637 | -5.49 | PLN | 2.4x | 674.00 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | live | none | 2026-09-28 (57d ago) | N | no fresh company catalyst found on 2026-11-24; the last event was the 2026-11-23 approval of the Mikroglob D3 documentation, which entitles the company to PLN 41.37m, and the shares are falling with WIG20 down about 1.7% |
| DEMANT | denmark | OMXCOP | 332.4 | -5.14 | DKK | 4.1x | 350.40 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | live | ADR (OTC:WILYY) | 2026-08-11 (105d ago) | — | no catalyst lookup (outside the per-run budget) |
| AAL | uk | LSE | 3164 | -5.04 | GBX | 1.8x | 3332.00 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | live | none | 2026-07-30 (117d ago) | — | no catalyst lookup (outside the per-run budget) |
| PRY | italy | MIL | 101.95 | -4.76 | EUR | 1.6x | 107.05 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | live | none | 2026-10-29 (26d ago) | — | no catalyst lookup (outside the per-run budget) |
| NOD | norway | OSL | 171.5 | -4.72 | NOK | 1.9x | 180.00 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | live | none | 2026-10-22 (33d ago) | — | no catalyst lookup (outside the per-run budget) |
| BESI | netherlands | EURONEXT | 148.55 | -4.71 | EUR | 1.5x | 155.90 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | live | none | 2026-10-21 (34d ago) | — | no catalyst lookup (outside the per-run budget) |
| TPRO | italy | MIL | 19.09 | -4.65 | EUR | 1.1x | 20.02 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | live | none | 2026-08-05 (111d ago) | — | no catalyst lookup (outside the per-run budget) |
| SLR | spain | BME | 13.39 | -4.60 | EUR | 1.7x | 14.04 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | live | none | 2026-11-19 (5d ago) | — | no catalyst lookup (outside the per-run budget) |
| CLN | switzerland | SIX | 9.83 | -4.10 | CHF | 2.6x | 10.25 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | live | none | 2026-07-31 (116d ago) | — | no catalyst lookup (outside the per-run budget) |

## AU (ASX) — Headline table

| Ticker | Venue | Close | Chg % | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | Session asof | Settle | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TUA | ASX | 1.8 | +32.35 | AUD | 7.6x | 1.36 | yahoo_chart_daily | 2026-11-22 | 2026-11-24 | settled | none | 2026-03-24 (245d ago) | — | no catalyst lookup (outside the per-run budget) |
| SHV | ASX | 4.8 | +17.07 | AUD | 6.4x | 4.10 | yahoo_chart_daily | 2026-11-22 | 2026-11-24 | settled | none | 2026-11-24 (0d ago) | Y | FY2026 full-year results (year ended 30 September 2026) released 2026-11-24: NPAT $39.3M +29%, EBIT $67.0M +38%, EPS 27.8c, crop 29,061MT +17%, final dividend 4.5c fully franked (reported 2026-11-24) |
| LOV | ASX | 26.54 | +10.58 | AUD | 4.5x | 24.00 | yahoo_chart_daily | 2026-11-22 | 2026-11-24 | settled | none | 2026-08-25 (91d ago) | N | AGM trading update released 2026-11-24: global sales +15.5% in the first 21 weeks of FY27 on constant currency, comparable store sales +3.4%, driven by store network expansion |
| TEA | ASX | 8.4 | +10.38 | AUD | 3.4x | 7.61 | yahoo_chart_daily | 2026-11-22 | 2026-11-24 | settled | none | 2026-08-26 (90d ago) | — | no catalyst lookup (outside the per-run budget) |

## APAC/Gulf — Headline table

| Ticker | Market | Venue | Close | Chg % | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | Session asof | Settle | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AREA | indonesia | IDX | 254 | +24.51 | IDR | 2.6x | 204.00 | yahoo_chart_daily | 2026-11-22 | 2026-11-23 | settled | US line (OTC:GBAIF) | — | — | no catalyst lookup (outside the per-run budget) |
| WMUU | indonesia | IDX | 50 | +21.95 | IDR | 2.5x | 41.00 | yahoo_chart_daily | 2026-11-22 | 2026-11-23 | settled | none | 2022-08-24 (1553d ago) | — | no catalyst lookup (outside the per-run budget) |
| APLAPOLLO | india | BSE | 1668.15 | -21.39 | INR | 8.8x | 2122.15 | yahoo_chart_daily | 2026-11-19 | 2026-11-22 | settled | none | 2026-10-26 (29d ago) | N | Tata Steel agreed to acquire a 26.38% stake in APL Apollo for Rs 15,510 crore in a three-stage deal; the shares hit a series of lower circuits and fell about 22% on 2026-11-23 |
| 300338 | china | SZSE | 1.96 | +20.25 | CNY | 4.2x | 1.63 | yahoo_chart_daily | 2026-11-22 | 2026-11-23 | settled | none | 2021-04-24 (2040d ago) | — | no catalyst lookup (outside the per-run budget) |
| 301575 | china | SZSE | 34.42 | +20.01 | CNY | 5.1x | 28.68 | yahoo_chart_daily | 2026-11-22 | 2026-11-23 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| 301189 | china | SZSE | 43.72 | +20.01 | CNY | 3.2x | 36.43 | yahoo_chart_daily | 2026-11-22 | 2026-11-23 | settled | none | 2026-10-29 (26d ago) | — | no catalyst lookup (outside the per-run budget) |
| SKYLMILAR | india | BSE | 15.98 | +19.97 | INR | 3.6x | 13.32 | yahoo_chart_daily | 2026-11-19 | 2026-11-22 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| JTS | thailand | SET | 11.65 | -18.53 | THB | 2.8x | 14.30 | yahoo_chart_daily | 2026-11-22 | 2026-11-23 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| BROCK | thailand | SET | 1.28 | +9.40 | THB | 3.1x | 1.17 | yahoo_chart_daily | 2026-11-22 | 2026-11-23 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| CNT | thailand | SET | 2.22 | -9.02 | THB | 3.1x | 2.44 | yahoo_chart_daily | 2026-11-22 | 2026-11-23 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| SUM | newzealand | NZX | 6 | +7.14 | NZD | 3.5x | 5.60 | yahoo_chart_daily | 2026-11-22 | 2026-11-23 | settled | none | 2026-08-26 (90d ago) | — | no catalyst lookup (outside the per-run budget) |
| 9637 | ksa | TADAWUL | 10.49 | +6.50 | SAR | 1.6x | 9.85 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| FBU | newzealand | NZX | 3.63 | +4.91 | NZD | 2.7x | 3.46 | yahoo_chart_daily | 2026-11-22 | 2026-11-23 | settled | none | 2026-08-18 (98d ago) | N | no fresh company catalyst found; the move tracks the NZX 50, which closed up 1.75% on 2026-11-24 |
| 4144 | ksa | TADAWUL | 78 | +4.84 | SAR | 1.1x | 74.40 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| BN4 | singapore | SGX | 8.42 | -4.64 | SGD | 2.7x | 8.85 | yahoo_chart_daily | 2026-11-19 | 2026-11-23 | settled | none | 2026-07-29 (118d ago) | N | Keppel completed the sale of its 40% stake in the Ho Chi Minh City Empire City project for S$343M and discontinued the land-fee arbitration, leaving the shares at a 52-week closing low |
| MFT | newzealand | NZX | 72.2 | +4.26 | NZD | 3.0x | 69.25 | yahoo_chart_daily | 2026-11-22 | 2026-11-23 | settled | none | 2026-11-11 (13d ago) | — | no catalyst lookup (outside the per-run budget) |
| 8120 | ksa | TADAWUL | 12.61 | +4.21 | SAR | 2.2x | 12.10 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |

## Source health

- scanner_calls: 57 | scanner_errors: 0
- markets_scanned: US + 17 EU/UK + ASX + 7 APAC/Gulf (india, thailand, indonesia, china, singapore, newzealand, ksa)
- pipeline_version: 2026-11-20.1
- et_clock: zoneinfo America/New_York (DST-aware; a fixed UTC-4 mislabels every winter fire)
- premarket_window: 04:00-09:30 ET, resolved with zoneinfo (09:00-14:30 UTC in winter, 08:00-13:30 UTC in summer)
- session_selection: by DATE and order, never by a modal time-of-day. Yahoo stamps a daily bar at the session open, so the ET stamp of the SAME session shifts by one hour across a DST boundary; a modal filter kept the OLDER bars and discarded the NEWEST ones, which rolled the base back to the prior-prior session (66 US + 21 ASX rows lost on 2026-11-03, 24 of 25 ASX rows lost on 2026-11-04).
- yahoo_calls: 240 | yahoo_429: 0 | yahoo_errors: 0 | yahoo_breaker: closed
- reference_close (screener vs Yahoo, resolved BEFORE the tables were built): agree=223 mismatch=6 unverified=1 stale_reference=6
  method: the screener's implied reference close (close / (1 + change/100)) is compared
  with Yahoo's own reference close. A match proves the move was measured against the
  TRUE prior close; a mismatch means the row sits on a STALE reference (phantom move).
  Coverage: every row of the US headline, US QUIET, EU/UK and ASX tables is checked.
  Yahoo bar mode: {"closed": 195, "live": 28} (closed = last completed session bar;
  live = in-progress EU/UK session bar, which is what a weekday 08:00 ET EU move needs)
  live drift between the screener snapshot and the later Yahoo print: median=0.00pp max=2.35pp (expected on a live market)
- cross_check mismatches: [{"region": "US", "symbol": "SNDK", "tv": 10.689, "yahoo": -7.082, "delta": 17.771, "ref_delta_pct": -16.055, "tv_implied_ref": 79.24, "yahoo_ref": 94.395, "yahoo_date": "2026-11-23", "yahoo_ref_date": "2026-11-19", "verdict": "stale_reference"}, {"region": "germany", "symbol": "AIXA.DE", "tv": -12.184, "yahoo": -10.861, "delta": -1.323, "ref_delta_pct": 1.186, "tv_implied_ref": 32.42, "yahoo_ref": 32.04, "yahoo_date": "2026-11-24", "yahoo_ref_date": "2026-11-23", "verdict": "stale_reference"}, {"region": "uk", "symbol": "0A9M.L", "tv": 6.621, "yahoo": 6.621, "delta": 0.0, "ref_delta_pct": null, "tv_implied_ref": 48.63, "yahoo_ref": 48.63, "yahoo_date": "2026-11-23", "yahoo_ref_date": "2026-11-09", "verdict": "stale_reference_date", "why": "the feed skipped a session (base 2026-11-09 -> session 2026-11-23, 14 days)"}, {"region": "indonesia", "symbol": "RDTX.JK", "tv": -95.195, "yahoo": -3.906, "delta": -91.289, "ref_delta_pct": 1900.0, "tv_implied_ref": 12800.0, "yahoo_ref": 640.0, "yahoo_date": "2026-11-23", "yahoo_ref_date": "2026-11-22", "verdict": "stale_reference"}, {"region": "singapore", "symbol": "MIM.SI", "tv": 23.077, "yahoo": 28.0, "delta": -4.923, "ref_delta_pct": 4.0, "tv_implied_ref": 1.04, "yahoo_ref": 1.0, "yahoo_date": "2026-11-23", "yahoo_ref_date": "2026-11-19", "verdict": "stale_reference"}, {"region": "singapore", "symbol": "5E2.SI", "tv": -7.19, "yahoo": -8.974, "delta": 1.784, "ref_delta_pct": -1.923, "tv_implied_ref": 1.53, "yahoo_ref": 1.56, "yahoo_date": "2026-11-23", "yahoo_ref_date": "2026-11-19", "verdict": "stale_reference"}]
- rows_dropped_stale_ref: 6 (rows whose screener-implied reference close disagreed with Yahoo's by more than 0.5%; they are dropped, not published)
- rows_dropped_unresolved_ref: 1 (rows whose reference close could not be resolved from Yahoo at all - the base of the move is unverifiable, so the row is dropped rather than published with a '—' base)
- us_premarket_check (Yahoo 1-min pre/post feed vs the screener pre-market column, base = the IMMEDIATELY prior session's close): checked=10 within_1pp=6 within_3pp=10 unavailable=0
- markets_with_lt5_rows: ['france:egreater=3', 'france:less=2', 'netherlands:egreater=0', 'netherlands:less=3', 'belgium:egreater=1', 'belgium:less=1', 'portugal:egreater=0', 'portugal:less=0', 'ireland:egreater=0', 'ireland:less=1', 'italy:egreater=0', 'italy:less=3', 'switzerland:egreater=0', 'switzerland:less=3', 'spain:egreater=0', 'spain:less=4', 'norway:egreater=3', 'denmark:egreater=1', 'denmark:less=3', 'finland:egreater=0', 'finland:less=2', 'poland:egreater=1', 'austria:egreater=0', 'austria:less=1', 'greece:egreater=0', 'greece:less=1', 'singapore:less=4', 'newzealand:less=0']
  NOTE: this fires per market AND direction, so it is NOT a coverage-failure signal on
  its own. A 'less' count of 0-3 means almost nothing fell more than 2.5% that session
  (a broad up-day); a small 'egreater' count usually means a small market with few
  names above the $1B market-cap floor. Check the median change before calling it a gap.
- filters: volume>10000 (removes stale-reference rows), country=home for EU/UK/AU,
  exchange drop-list for US, US venue allow-list, US preferred (slash ticker) excluded
- pass_b2 (US pre-market gap scan - "gapped today, flat yesterday"): candidates=30 deduped_against_pass_a_b=17 published=13 (up=10 down=20)
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
- bod_no_extended_hours: 71 (deferred to the next scan; not in the headline table)
- earnings_source: screener `earnings_release_date` (last FULL report) + `earnings_release_next_date` (next scheduled)
- earnings_caveat: `earnings_release_date` does NOT capture preliminary, guidance or
  restructuring releases. On 2026-10-23 LKQ fell 22.47% on a preliminary Q3 miss while
  the field still read 2026-07-30. ALWAYS confirm the earnings-driven flag against the
  headline itself; the calendar field is a screen, not a verdict.
- us_line_index: ok (US-listed lines for the 25 foreign home countries, both scanner types; the `US tradeable` column is ADR / US-listed / none)
- catalyst_note: Catalyst lookups: 8 US + 3 EU + 2 AU + 3 APAC/Gulf = 16 per run - the skill's cap, allocated by the evidence gap.
- catalyst_merge: region-matched - a row may only use a catalog entry from its OWN region;
  the same ticker on another venue is a different company and is not used.
- catalyst_budget: 8 US + 3 EU + 2 AU + 3 APAC/Gulf = 16 lookups per run (cap 16), allocated by the evidence gap: the US slice covers the rows whose earnings event can still explain today's move, the EU/AU/APAC floors are never squeezed because no bulk calendar reaches those markets, and whatever the US slice does not need goes to the region with the most unexplained rows
- earnings_calendar: Nasdaq public earnings calendar (calls=8 errors=0 symbols=262) - the source of record for the US earnings date, and the ranking key for the search budget
- earnings_field_stale_rows: 2 (the screener's earnings_release_date disagreed with the calendar; the calendar's date is published)
- earnings_field_stale_detail: [{"ticker": "DELL", "screener": "2026-09-01", "calendar": "2026-11-24"}, {"ticker": "CLSK", "screener": "2026-08-06", "calendar": "2026-11-24"}]
- earnings_dates: the published `Last earnings` date by source - catalog (researched) 9, calendar 15, asx 0, screener 184. The chain is researched -> calendar (US) -> ASX feed (AU) -> the screener's field, which is the FALLBACK and the one that lags (2026-11-12: NBIS carried the previous quarter's date on the morning it reported, and MEKO, NORBT and FG carried July and August dates on the morning they all reported).
- asx_announcements: 6 results-classified announcement(s) for the last ASX session (calls=1 errors=0); the announcement date IS the report date, and the meeting/AGM/offer/assay headlines are excluded because they are not reports
- earnings_date_quality: 1 of 21 markets publish a FRESH earnings date (median age <= 14d); the table below gives each market's rows, the rows with NO date at all, the median age of the published date and the rows within 7 and 30 days - the reader sees the input quality instead of trusting it
| market | rows | no date | median age | <=7d | <=30d |
|---|---|---|---|---|---|
| au | 4 | 0 | 91d | 1 | 1 |
| austria | 1 | 0 | 19d | 0 | 1 |
| china | 3 | 1 | 2040d | 0 | 1 |
| denmark | 1 | 0 | 105d | 0 | 0 |
| france | 3 | 1 | 118d | 1 | 1 |
| germany | 3 | 0 | 104d | 0 | 1 |
| india | 2 | 1 | 29d | 0 | 1 |
| indonesia | 2 | 1 | 1553d | 0 | 0 |
| italy | 2 | 0 | 111d | 0 | 1 |
| ksa | 3 | 3 | n/a | 0 | 0 |
| netherlands | 1 | 0 | 34d | 0 | 0 |
| newzealand | 3 | 0 | 90d | 0 | 1 |
| norway | 4 | 0 | 32d | 1 | 2 |
| poland | 4 | 0 | 70d | 1 | 1 |
| singapore | 1 | 0 | 118d | 0 | 0 |
| spain | 1 | 0 | 5d | 1 | 1 |
| sweden | 4 | 0 | 35d | 1 | 2 |
| switzerland | 1 | 0 | 116d | 0 | 0 |
| thailand | 3 | 3 | n/a | 0 | 0 |
| uk | 3 | 0 | 117d | 0 | 0 |
| us | 159 | 0 | 20d | 24 | 137 |
- earnings_tiers: fresh=11 near=5 (fresh = the report is dated on the scan date, near = the previous session)
- one_table_rule: each name appears exactly once, in exactly one table, with its
  catalyst in that row's last column. There is no separate catalysts section.
- data_date: US regular session close of the prior trading day; extended-hours columns
  carry the prior session's prints
- settlement_state: 21 settled, 28 live (a live row's move is a mid-session snapshot, not the session's result)
- rows_per_market (EU/UK, cap 4/market): {'germany': 4, 'poland': 4, 'norway': 4, 'france': 4, 'sweden': 4, 'uk': 4, 'austria': 1, 'denmark': 4, 'italy': 3, 'netherlands': 3, 'spain': 4, 'switzerland': 3, 'finland': 2, 'belgium': 2, 'ireland': 1, 'greece': 1} — the cap stops one thin market taking the table; the EU/UK table was 28% Sweden over nine runs (73 of 264 rows) while Belgium and Greece never appeared once.
- rows_per_market (APAC/Gulf, cap 3/market): {'indonesia': 3, 'singapore': 3, 'india': 3, 'china': 3, 'thailand': 3, 'newzealand': 3, 'ksa': 3}
- deprecations: mcp__tradingview-advanced__*, mcp__tradingview__*, mcp__financekit__*,
  mcp__stocktwits__* are ABSENT in Cloud sessions (tool_search 0 hits; connector catalog
  holds only media + credential tools). The public screener replaces them.

- degraded_sources: 1
  (the chat reply's `errors:` MUST equal this number - one entry per degraded
  source, not one per run)
  1. yahoo_chart_api.reference_close_unresolved — HCL-INSYS.BO: the reference close could not be resolved (429 or a bad body)

## Audit line

`earnings-reaction target=earnings-reactions:2026-11-24 candidates=413 amc_reactions=0 pre_gaps=159 eu_reactions=28 asx_reactions=4 apac_reactions=17 catalyst_lookups=16 bod=71 pass_b2_candidates=30 pass_b2_dedup=17 pass_b2_published=13 earnings_calendar_rows=262 earnings_tiers_fresh=11 earnings_tiers_near=5 earnings_field_stale_rows=2 earnings_dates_catalog=9 earnings_dates_asx=0 asx_ann_rows=6 rows_dropped_stale_ref=6 rows_dropped_unresolved_ref=1 degraded_sources=1`
