# Earnings reaction scanner — 2026-11-25

- Cron: `0 8 * * 1-5` America/New_York (weekdays, 08:00 ET)
- Fire time (ET): 2026-11-25 08:12:34 Wed
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

- 0 AMC reactions, 229 pre-market gaps, 128 without extended-hours data; 29 EU/UK and 3 ASX movers, 21 APAC/Gulf movers.
- Pass B2 (the US pre-market gap scan) met the filter on 57 names (1 up, 56 down); 43 were already a Pass A/B row and are recorded as dedupes, and 14 reached a table.
- Biggest US extended-hours move: AMBA PRE_GAP (34.09%).
- Biggest EU/UK move: AMS2 (+15.59%, austria).
- Biggest ASX move: WEB (-23.53%).
- Biggest APAC/Gulf move: CITY (+34.40%, indonesia).
- 0 of the 29 EU/UK rows are SETTLED and 29 are LIVE (mid-session). The 12:15 ET settlement pass publishes where those
  live moves actually closed.
- EU/AU/APAC earnings-driven tagging is keyword-based on headlines (best-effort). A row
  whose lookup was not performed carries NO verdict — only a researched row does.

## Actionable read

- **Move vs this name's own history.** The `Move vs avg daily` column divides the
  reaction by the name's own mean absolute daily move over its last
  20 completed sessions. A -27% move in a name that averages +-3% is a
  different event from a -8% move in a name that averages +-7%.
- **US-listed and tradeable vs foreign-only.** 244 published US rows are on a
  US venue; 1 more foreign reactions have a US ADR line
  (the `US tradeable` column carries the ticker); 29 are foreign-only and
  cannot be bought directly by a US reader.
- **Not yet fully priced — US (hypothesis, not a recommendation).**
  AMBA — -34.09%, 5.02% mean absolute daily move over the last 20 completed sessions, 6.8x that average, reference close 55.56 dated 2026-11-23, US access: US-listed, the move now (-34.09%) is larger than the move it follows (-19.96%); the reaction is still being repriced. Hypothesis only: this artifact states no
  direction and no trade.
- **Not yet fully priced — EU/UK (hypothesis, not a recommendation).**
  BVI — +6.77%, 0.76% mean absolute daily move over the last 20 completed sessions, 8.9x that average, reference close 29.83 dated 2026-11-24, US access: none, the move now (+6.77%) is larger than the move it follows (+0.88%); the reaction is still being repriced. Hypothesis only: this artifact states no
  direction and no trade.
- **Not yet fully priced — AU (ASX) (hypothesis, not a recommendation).**
  WEB — -23.53%, 3.78% mean absolute daily move over the last 20 completed sessions, 6.2x that average, reference close 3.40 dated 2026-11-23, US access: US line (OTC:TSWCF), the move now (-23.53%) is larger than the move it follows (+4.29%); the reaction is still being repriced. Hypothesis only: this artifact states no
  direction and no trade.

## US — Headline table

| Ticker | Venue | Close | Chg % | Pre-mkt % | Post-mkt % | Move vs avg daily | Ref close | Ref source | Ref asof | US tradeable | Last earnings | Tag | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AMBA | NASDAQ | 44.47 | -19.96 | -34.09 | — | 6.8x | 55.56 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-24 (1d ago) | PRE_GAP | Y | Q3 FY2027 results (reported 2026-11-24): revenue $115.2M missed the $119.4M consensus and non-GAAP EPS $0.28 missed $0.32; Q4 revenue guided to $70-75M against ~$112M consensus (rising memory prices and supply shortages); Morgan Stanley cut to Equalweight, PT $42 |
| URBN | NASDAQ | 85.58 | 0.34 | -12.36 | — | 5.1x | 85.29 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-24 (1d ago) | PRE_GAP | Y | Q3 FY2027 results (reported 2026-11-24): adj EPS $1.54 edged past the $1.52-1.53 consensus on record profit and sales, but Q4 sales growth guided down to mid-single digits and comps to low single digits as traffic turned negative |
| NTNX | NASDAQ | 54.59 | -5.16 | -10.24 | — | 3.7x | 57.56 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-24 (1d ago) | PRE_GAP | Y | Q1 FY2027 results (reported 2026-11-24): record revenue $772M and adj EPS $0.73 beat, but the FY27 revenue outlook of $3.18-3.23bn came in below the $3.22bn consensus and CEO Rajiv Ramaswami announced his exit |
| ICHR | NASDAQ | 26.39 | -16.49 | -7.96 | — | 1.1x | 31.60 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-02 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MXL | NASDAQ | 41.89 | -16.74 | -7.43 | — | 0.8x | 50.31 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-22 (34d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FORM | NASDAQ | 73.3 | -10.14 | -7.37 | — | 1.0x | 81.57 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-28 (28d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ROMA | NASDAQ | 3.87 | -10.10 | 7.24 | — | 1.6x | 4.30 | yahoo_chart_daily | 2026-11-23 | US-listed | — | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AEHR | NASDAQ | 41.89 | -13.65 | -7.16 | — | 0.7x | 48.51 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-02 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AAOI | NASDAQ | 38.4 | -0.78 | -6.77 | — | 0.8x | 38.70 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-05 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| VICR | NASDAQ | 125.55 | -11.61 | -6.59 | — | 1.0x | 142.04 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-20 (36d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ACMR | NASDAQ | 40.34 | -10.69 | -6.54 | — | 1.0x | 45.17 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-05 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AXTI | NASDAQ | 31.58 | -16.94 | -6.46 | — | 0.6x | 38.02 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-29 (27d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NBIS | NASDAQ | 87.31 | -10.73 | -6.45 | — | 0.7x | 97.80 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-12 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CRWV | NASDAQ | 42.605 | -11.85 | -6.42 | — | 0.7x | 48.33 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-10 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GENB | NASDAQ | 10.91 | 6.86 | -6.42 | — | 1.1x | 10.21 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-12 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PENG | NASDAQ | 37.57 | -11.06 | -6.41 | — | 0.7x | 42.24 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-06 (50d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| IPGP | NASDAQ | 59.89 | -6.84 | -6.37 | — | 1.4x | 64.29 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-03 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CRDO | NASDAQ | 106.46 | -13.07 | -6.35 | — | 0.8x | 122.46 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-09-01 (85d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MU | NASDAQ | 629.79 | -11.01 | -6.25 | — | 0.9x | 707.70 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-09-30 (56d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CSIQ | NASDAQ | 4.84 | -14.94 | -6.20 | — | 1.0x | 5.69 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-08-27 (90d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LITE | NASDAQ | 487.12 | -10.52 | -6.18 | — | 0.8x | 544.38 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-02 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AEVA | NASDAQ | 8.26 | -10.12 | -6.17 | — | 0.8x | 9.19 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-04 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ALAB | NASDAQ | 191.3 | -13.88 | -6.17 | — | 0.8x | 222.12 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-03 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CIFR | NASDAQ | 5.52 | -10.97 | -6.16 | — | 0.7x | 6.20 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-02 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMAT | NASDAQ | 323.76 | -6.66 | -6.09 | — | 1.1x | 346.87 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-12 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LRCX | NASDAQ | 196.16 | -6.48 | -6.03 | — | 1.1x | 209.76 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-21 (35d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BE | NYSE | 156.41 | -6.98 | -5.92 | — | 0.8x | 168.15 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-22 (34d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ONDS | NASDAQ | 3.89 | -3.47 | -5.91 | — | 0.8x | 4.03 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-12 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CIEN | NYSE | 239.27 | -9.62 | -5.87 | — | 0.9x | 264.73 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-09-03 (83d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MRVL | NASDAQ | 131.57 | -9.10 | -5.85 | — | 0.8x | 144.74 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-08-27 (90d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NUAI | NASDAQ | 4.11 | -5.30 | -5.84 | — | 0.4x | 4.34 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-12 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| IREN | NASDAQ | 12.95 | -11.54 | -5.83 | — | 0.6x | 14.64 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-05 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| INIO | NASDAQ | 12 | -8.05 | -5.83 | — | 0.9x | 13.05 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-27 (29d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TER | NASDAQ | 213.22 | -8.69 | -5.80 | — | 0.9x | 233.51 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-27 (29d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LWLG | NASDAQ | 2.77 | -4.97 | -5.78 | — | 0.8x | 2.92 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-10 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| STX | NASDAQ | 482.48 | -7.23 | -5.72 | — | 1.0x | 520.10 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-27 (29d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMKR | NASDAQ | 31.81 | -8.62 | -5.69 | — | 0.9x | 34.81 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-26 (30d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| VRT | NYSE | 173.82 | -6.72 | -5.65 | — | 0.9x | 186.35 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-28 (28d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MTSI | NASDAQ | 200.2 | -13.45 | -5.63 | — | 0.8x | 231.30 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-05 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PLPC | NASDAQ | 259.52 | -6.04 | -5.59 | — | 1.0x | 276.19 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-28 (28d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| WDC | NASDAQ | 273.95 | -7.84 | -5.57 | — | 0.9x | 297.25 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-22 (34d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FCEL | NASDAQ | 7.1 | -8.74 | -5.54 | — | 0.7x | 7.78 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-09-02 (84d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LGN | NASDAQ | 33.62 | -7.76 | -5.50 | — | 0.7x | 36.45 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-12 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMD | NASDAQ | 413.27 | -8.86 | -5.50 | — | 0.8x | 453.46 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-03 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BELFB | NASDAQ | 202.14 | -7.48 | -5.50 | — | 1.1x | 218.48 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-28 (28d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| HUT | NASDAQ | 48.24 | -6.09 | -5.47 | — | 0.7x | 51.37 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-04 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| EROC | NYSE | 5.85 | -6.55 | -5.47 | — | 0.7x | 6.26 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-12 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| UMAC | AMEX | 8.86 | -6.83 | -5.47 | — | 0.7x | 9.51 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-05 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ONTO | NYSE | 173.48 | -9.17 | -5.46 | — | 0.8x | 190.99 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-09 (16d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NVT | NYSE | 104.58 | -6.56 | -5.45 | — | 1.1x | 111.92 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-30 (26d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NVDA | NASDAQ | 155.38 | -5.86 | -5.44 | — | 1.0x | 165.05 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-17 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BELFA | NASDAQ | 159.635 | -6.54 | -5.42 | — | 1.1x | 170.81 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-28 (28d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ECG | NYSE | 78.55 | -6.61 | -5.41 | — | 0.9x | 84.11 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-03 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| KLAC | NASDAQ | 133.65 | -8.36 | -5.39 | — | 1.0x | 145.85 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-28 (28d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GLXY | NASDAQ | 11.55 | -7.97 | -5.37 | — | 0.7x | 12.55 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-27 (29d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NVTS | NASDAQ | 6.51 | -11.19 | -5.35 | — | 0.6x | 7.33 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-03 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GDRX | NASDAQ | 3 | -0.99 | -5.33 | — | 1.7x | 3.03 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-24 (1d ago) | PRE_GAP | Y | Q3 2026 results (reported 2026-11-24): revenue $218.4M, net income $16.4M, adj EBITDA $74.5M and FY26 guidance raised to $844-850M revenue - but the raise absorbs a restatement of the first two quarters over Pharma Direct revenue recognition, alongside a Nasdaq listing-compliance update |
| APLD | NASDAQ | 12.22 | -11.58 | -5.32 | — | 0.7x | 13.82 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-07 (49d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| POWL | NASDAQ | 153.88 | -5.00 | -5.28 | — | 1.0x | 161.98 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-16 (9d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CORZ | NASDAQ | 10.99 | -11.08 | -5.28 | — | 0.8x | 12.36 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-05 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SMTC | NASDAQ | 86.46 | -16.97 | -5.27 | — | 0.6x | 104.13 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-23 (2d ago) | PRE_GAP | — | Q4 2026 results, report date 2026-11-23 (Nasdaq earnings calendar; no headline lookup), consensus EPS $0.92 |
| SEI | NYSE | 56.53 | -7.68 | -5.27 | — | 0.9x | 61.23 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-04 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| VSH | NYSE | 22.29 | -10.16 | -5.25 | — | 0.8x | 24.81 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-04 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ABSI | NASDAQ | 9.17 | 8.14 | -5.23 | — | 0.8x | 8.48 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-12 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GLW | NYSE | 101.87 | -5.95 | -5.18 | — | 1.0x | 108.31 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-27 (29d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AEIS | NASDAQ | 199.23 | -6.93 | -5.18 | — | 0.9x | 214.07 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-02 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RMBS | NASDAQ | 68.76 | -9.14 | -5.18 | — | 0.9x | 75.68 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-26 (30d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FIX | NYSE | 1096.56 | -5.35 | -5.16 | — | 0.9x | 1158.53 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-22 (34d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CLS | NYSE | 196.64 | -7.81 | -5.16 | — | 0.9x | 213.31 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-26 (30d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| STRL | NASDAQ | 256.15 | -8.11 | -5.13 | — | 0.8x | 278.77 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-28 (28d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| OUST | NASDAQ | 24.99 | -10.43 | -5.12 | — | 0.7x | 27.90 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-03 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FLNC | NASDAQ | 4.1 | 7.89 | -5.12 | — | 0.8x | 3.80 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-23 (2d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-23 (Nasdaq earnings calendar; no headline lookup), consensus EPS ($0.54) |
| WOLF | NYSE | 18.2 | -11.95 | -5.11 | — | 0.7x | 20.67 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-04 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| P | NYSE | 92.2 | -8.72 | -5.10 | — | 0.9x | 101.01 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-18 (7d ago) | PRE_GAP | — | Q4 2026 results, report date 2026-11-18 (Nasdaq earnings calendar; no headline lookup), consensus EPS $0.28 |
| WULF | NASDAQ | 10.01 | -8.25 | -5.09 | — | 0.7x | 10.91 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-06 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| DELL | NYSE | 295.28 | -11.83 | -5.08 | — | 0.7x | 334.91 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-24 (1d ago) | PRE_GAP | Y | Q3 FY2027 results (reported 2026-11-24): record revenue $54.9bn, +103% y/y, and non-GAAP EPS $9.45 vs the $6.59 consensus; AI backlog $132.3bn; FY27 revenue guidance raised to $202bn from $192bn and non-GAAP EPS to $29.68 |
| ORCL | NYSE | 109.5 | -3.68 | -5.07 | — | 1.1x | 113.68 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-09-10 (76d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| COHR | NYSE | 196.24 | -9.07 | -5.07 | — | 0.7x | 215.81 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-04 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SITM | NASDAQ | 378.29 | -13.79 | -5.05 | — | 0.7x | 438.82 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-04 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TSEM | NASDAQ | 123.47 | -9.75 | -4.98 | — | 0.7x | 136.81 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-02 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| DOCN | NYSE | 74.01 | -6.29 | -4.96 | — | 0.8x | 78.98 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-03 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CBRS | NASDAQ | 88.78 | -9.88 | -4.91 | — | 0.7x | 98.51 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-12 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SANM | NASDAQ | 138.28 | -10.14 | -4.90 | — | 0.9x | 153.88 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-09 (16d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ALGM | NASDAQ | 26.81 | -8.50 | -4.89 | — | 0.8x | 29.30 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-29 (27d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FRVO | NASDAQ | 9.37 | -13.08 | -4.87 | — | 0.6x | 10.78 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-09 (16d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ANET | NYSE | 168.56 | -5.47 | -4.81 | — | 0.9x | 178.31 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-03 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| VIAV | NASDAQ | 26.83 | -9.54 | -4.77 | — | 0.8x | 29.66 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-04 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| QBTS | NASDAQ | 6.74 | -7.80 | -4.75 | — | 0.7x | 7.31 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-10 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| INTC | NASDAQ | 54.8 | -8.15 | -4.74 | — | 0.7x | 59.66 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-29 (27d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PURR | NASDAQ | 7.74 | -6.41 | -4.72 | — | 0.7x | 8.27 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-05 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CAMT | NASDAQ | 94.59 | -5.50 | -4.66 | — | 0.8x | 100.10 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-04 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FN | NYSE | 290.12 | -11.88 | -4.65 | — | 0.6x | 329.22 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-02 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FPS | NYSE | 18.63 | -8.23 | -4.62 | — | 0.5x | 20.30 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-12 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SMCI | NASDAQ | 22.62 | -7.79 | -4.55 | — | 0.8x | 24.53 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-03 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LSCC | NASDAQ | 100.37 | -11.14 | -4.54 | — | 0.7x | 112.95 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-02 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| KLIC | NASDAQ | 57.59 | -6.42 | -4.50 | — | 0.8x | 61.54 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-18 (7d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-18 (Nasdaq earnings calendar; no headline lookup), consensus EPS $1.31 |
| USAR | NASDAQ | 6.68 | -4.84 | -4.49 | — | 0.7x | 7.02 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-09 (16d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RGTI | NASDAQ | 7.59 | -6.24 | -4.48 | — | 0.6x | 8.10 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-10 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| INFQ | NYSE | 6.34 | -6.07 | -4.42 | — | 0.7x | 6.75 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-16 (9d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ANT | NASDAQ | 81.905 | -6.54 | -4.41 | — | 0.8x | 87.64 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-02 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RKLB | NASDAQ | 45.98 | -7.35 | -4.39 | — | 0.7x | 49.63 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-09 (16d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| UCTT | NASDAQ | 36.08 | -12.37 | -4.38 | — | 0.6x | 41.18 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-27 (29d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PLTR | NASDAQ | 161.18 | 1.14 | -4.37 | — | 1.3x | 159.36 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-02 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LFUS | NASDAQ | 360.22 | -7.46 | -4.36 | — | 1.1x | 389.27 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-28 (28d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MPWR | NASDAQ | 1190.16 | -10.77 | -4.34 | — | 0.7x | 1333.88 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-29 (27d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PANW | NASDAQ | 352.99 | -0.12 | -4.34 | — | 1.3x | 353.43 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-18 (7d ago) | PRE_GAP | — | Q4 2026 results, report date 2026-11-18 (Nasdaq earnings calendar; no headline lookup), consensus EPS $0.52 |
| TTMI | NASDAQ | 59.42 | -13.34 | -4.33 | — | 0.6x | 68.57 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-22 (34d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PL | NYSE | 10.64 | -5.08 | -4.32 | — | 0.8x | 11.21 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-09-03 (83d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| VOYG | NYSE | 17.88 | -9.24 | -4.31 | — | 0.6x | 19.70 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-02 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ASST | NASDAQ | 14.19 | -8.27 | -4.30 | — | 0.7x | 15.47 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-06 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| HPE | NYSE | 40.19 | -16.31 | -4.29 | — | 0.8x | 48.02 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-23 (2d ago) | PRE_GAP | — | Q4 2026 results, report date 2026-11-23 (Nasdaq earnings calendar; no headline lookup), consensus EPS $1.18 |
| SNX | NYSE | 217.3 | -6.15 | -4.28 | — | 1.4x | 231.55 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-09-24 (62d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LUNR | NASDAQ | 8.93 | -8.41 | -4.26 | — | 0.5x | 9.75 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-12 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RDW | NYSE | 5.9 | -8.10 | -4.24 | — | 0.6x | 6.42 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-04 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CLSK | NASDAQ | 5.115 | -7.50 | -4.20 | — | 0.5x | 5.53 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-24 (1d ago) | PRE_GAP | Y | Fiscal Q4 and full-year 2026 results (reported 2026-11-24): Q4 revenue $120.9M missed the $134.1M estimate and fell 46% y/y; full-year net loss $987.1M on bitcoin mark-to-market plus a $171.7M impairment; Sandersville $6.6B lease signed and funded |
| FLEX | NASDAQ | 66.44 | -10.14 | -4.12 | — | 0.7x | 73.94 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-28 (28d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ABCL | NASDAQ | 10.95 | 3.99 | -4.11 | — | 0.9x | 10.53 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-09 (16d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ENTG | NASDAQ | 127.82 | -10.02 | -4.10 | — | 0.8x | 142.06 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-29 (27d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SHOP | NASDAQ | 132.31 | -1.48 | -4.09 | — | 1.1x | 134.30 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-03 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| OKLO | NYSE | 19.2 | -7.56 | -4.06 | — | 0.7x | 20.77 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-06 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FIGR | NASDAQ | 24.59 | -6.04 | -4.03 | — | 0.8x | 26.17 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-12 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| VKTX | NASDAQ | 29.48 | 6.46 | -4.02 | — | 0.9x | 27.69 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-28 (28d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SNOW | NYSE | 271.09 | -0.07 | -4.02 | — | 1.2x | 271.27 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-09-02 (84d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AVGO | NASDAQ | 301.08 | -3.98 | -4.01 | — | 0.9x | 313.55 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-09-02 (84d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CRWD | NASDAQ | 210.86 | 0.90 | -4.01 | — | 1.2x | 208.97 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-23 (2d ago) | PRE_GAP | — | Q4 2026 results, report date 2026-11-23 (Nasdaq earnings calendar; no headline lookup), consensus EPS $0 |
| PLXS | NASDAQ | 187.51 | -7.38 | -4.01 | — | 1.0x | 202.45 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-28 (28d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RIOT | NASDAQ | 16.34 | -4.72 | -3.98 | — | 0.7x | 17.15 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-04 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CENX | NASDAQ | 29.06 | -5.28 | -3.96 | — | 1.0x | 30.68 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-05 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PPTA | NASDAQ | 14.34 | -4.97 | -3.95 | — | 0.8x | 15.09 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-13 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BEAM | NASDAQ | 24.26 | 6.12 | -3.93 | — | 1.0x | 22.86 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-03 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CDNS | NASDAQ | 296.6 | -2.48 | -3.91 | — | 1.4x | 304.13 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-26 (30d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ERO | NYSE | 21.75 | -6.89 | -3.91 | — | 0.8x | 23.36 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-02 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| IMNM | NASDAQ | 18.45 | 13.26 | -3.90 | — | 1.0x | 16.29 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-09 (16d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TGB | AMEX | 5.44 | -5.23 | -3.84 | — | 1.0x | 5.74 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-04 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GEV | NYSE | 720.65 | -4.77 | -3.84 | — | 1.0x | 756.71 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-28 (28d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| JBL | NYSE | 226.69 | -6.42 | -3.83 | — | 1.1x | 242.24 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-09-30 (56d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| APH | NYSE | 73.47 | -5.09 | -3.78 | — | 1.0x | 77.41 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-28 (28d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PLAB | NASDAQ | 24.52 | -7.37 | -3.75 | — | 0.9x | 26.47 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-08-26 (91d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| OMCL | NASDAQ | 34.7 | 5.54 | 3.75 | — | 1.4x | 32.88 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-29 (27d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FLY | NASDAQ | 18.18 | -5.02 | -3.74 | — | 0.5x | 19.14 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-10 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MTRN | NYSE | 186.99 | -8.29 | -3.74 | — | 0.7x | 203.89 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-04 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| KEYS | NYSE | 272.22 | -6.01 | -3.70 | — | 0.9x | 289.63 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-19 (6d ago) | PRE_GAP | — | Q4 2026 results, report date 2026-11-19 (Nasdaq earnings calendar; no headline lookup), consensus EPS $3.09 |
| GOOG | NASDAQ | 276.58 | -1.06 | -3.66 | — | 1.6x | 279.53 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-28 (28d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| STDN | NYSE | 7.68 | -10.07 | -3.65 | — | 0.8x | 8.54 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-12 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GOOGL | NASDAQ | 279.05 | -1.08 | -3.63 | — | 1.5x | 282.10 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-28 (28d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NET | NYSE | 287.29 | -1.32 | -3.58 | — | 0.7x | 291.13 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-05 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SNPS | NASDAQ | 414.82 | -2.85 | -3.57 | — | 1.5x | 426.99 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-08-26 (91d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LASR | NASDAQ | 32.66 | -9.55 | -3.55 | — | 0.5x | 36.11 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-05 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| POWI | NASDAQ | 39.73 | -8.92 | -3.55 | — | 0.7x | 43.62 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-04 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GFS | NASDAQ | 36.42 | -6.50 | -3.54 | — | 0.8x | 38.95 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-04 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AGX | NYSE | 271.1 | -8.20 | -3.50 | — | 0.6x | 295.31 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-09-02 (84d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PWR | NYSE | 589.64 | -3.18 | -3.50 | — | 0.8x | 609.00 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-29 (27d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ECVT | NYSE | 9.72 | 4.07 | -3.50 | — | 1.5x | 9.34 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-05 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FTNT | NASDAQ | 132.5 | 1.07 | -3.46 | — | 0.9x | 131.10 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-28 (28d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SPCX | NASDAQ | 125.81 | -5.65 | -3.45 | — | 0.9x | 133.35 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-20 (36d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| APP | NASDAQ | 381.11 | 1.92 | -3.43 | — | 0.6x | 373.92 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-04 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SYM | NASDAQ | 37.39 | 6.92 | -3.42 | — | 1.0x | 34.97 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-23 (2d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-23 (Nasdaq earnings calendar; no headline lookup), consensus EPS $0.08 |
| BXMT | NYSE | 10.82 | 5.05 | -3.42 | — | 1.8x | 10.30 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-29 (27d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MSTR | NASDAQ | 77.55 | -8.12 | -3.42 | — | 0.7x | 84.40 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-29 (27d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LQDA | NASDAQ | 58.66 | 5.64 | -3.41 | — | 0.9x | 55.53 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-10 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ETN | NYSE | 319.27 | -5.08 | -3.32 | — | 0.9x | 336.34 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-03 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NVMI | NASDAQ | 292.19 | -6.18 | -3.32 | — | 0.8x | 311.44 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-05 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| KN | NYSE | 30.71 | -8.71 | -3.29 | — | 0.9x | 33.64 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-22 (34d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BETA | NYSE | 15.66 | -5.61 | -3.29 | — | 0.6x | 16.59 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-03 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| EXK | NYSE | 5.78 | -5.71 | -3.29 | — | 0.7x | 6.13 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-09 (16d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MSFT | NASDAQ | 496.13 | 0.74 | -3.26 | — | 1.7x | 492.50 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-28 (28d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| METAM | NASDAQ | 48.34 | -0.88 | 3.25 | — | 1.8x | 48.77 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-21 (35d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| XE | NASDAQ | 8.63 | -12.78 | -3.25 | — | 0.5x | 9.90 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-12 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ON | NASDAQ | 61.49 | -7.91 | -3.24 | — | 0.8x | 66.77 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-02 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MYRG | NASDAQ | 259.09 | -5.00 | -3.23 | — | 0.8x | 272.74 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-28 (28d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MRNA | NASDAQ | 227.38 | 7.21 | -3.15 | — | 0.7x | 212.08 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-06 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SCCO | NYSE | 136.85 | -4.51 | -3.15 | — | 0.9x | 143.32 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-21 (35d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| HLIT | NASDAQ | 9.85 | -4.83 | -3.15 | — | 0.9x | 10.35 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-02 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| OCTV | NASDAQ | 22.29 | 4.84 | -3.10 | — | 1.5x | 21.26 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-12 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| HBM | NYSE | 16.82 | -5.93 | -3.09 | — | 0.7x | 17.88 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-12 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AVT | NASDAQ | 73.2 | -6.33 | -3.05 | — | 0.9x | 78.15 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-04 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MCHP | NASDAQ | 56.36 | -7.94 | -3.05 | — | 0.7x | 61.22 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-05 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CAT | NYSE | 540.63 | -1.17 | -3.05 | — | 0.9x | 547.04 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-29 (27d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ADI | NASDAQ | 312.95 | -17.37 | -3.04 | — | 0.7x | 378.75 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-24 (1d ago) | PRE_GAP | Y | Q4 FY2026 results (reported 2026-11-24): record revenue $4.373bn, +42% y/y, adj EPS $4.06, FY26 revenue $15.2bn +38%; Q1 FY27 guided to $4.4bn (+/-150M) with AI now ~20% of revenue |
| COHU | NASDAQ | 37.84 | -9.88 | -3.04 | — | 0.5x | 41.99 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-28 (28d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ASTS | NASDAQ | 23.6 | -8.06 | -3.03 | — | 0.4x | 25.67 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-09 (16d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| COGT | NASDAQ | 33.01 | 17.43 | -3.03 | — | 0.7x | 28.11 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-05 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NXT | NASDAQ | 65.76 | -6.82 | -3.03 | — | 0.5x | 70.58 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-28 (28d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NOW | NYSE | 91.74 | 0.02 | -3.01 | — | 0.8x | 91.72 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-28 (28d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| DY | NYSE | 179.01 | -18.02 | -3.00 | — | 0.6x | 218.37 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-24 (1d ago) | PRE_GAP | — | Q4 2026 results, report date 2026-11-24 (Nasdaq earnings calendar; no headline lookup), consensus EPS $4.33 |
| PRIM | NYSE | 55.35 | -7.93 | -2.98 | — | 0.5x | 60.12 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-03 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CRCL | NYSE | 47.72 | -7.05 | -2.98 | — | 0.7x | 51.34 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-04 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| IBKR | NASDAQ | 74.71 | -2.30 | -2.94 | — | 0.9x | 76.47 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-15 (41d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NPO | NYSE | 258.98 | -4.91 | -2.89 | — | 0.9x | 272.36 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-03 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| QCOM | NASDAQ | 164.96 | -0.25 | -2.85 | — | 0.7x | 165.38 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-04 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PTON | NASDAQ | 5.64 | 5.22 | -2.84 | — | 0.9x | 5.36 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-05 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| UEC | AMEX | 5.57 | -4.62 | -2.82 | — | 0.6x | 5.84 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-09-29 (57d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| IONS | NASDAQ | 29.8 | 5.23 | -2.82 | — | 0.7x | 28.32 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-09 (16d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CEG | NASDAQ | 244.84 | -2.73 | -2.79 | — | 0.8x | 251.72 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-09 (16d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CSCO | NASDAQ | 93.99 | -2.90 | -2.76 | — | 0.9x | 96.80 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-12 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TLN | NASDAQ | 347.68 | -4.70 | -2.75 | — | 0.7x | 364.83 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-03 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMZN | NASDAQ | 252.29 | -1.21 | -2.73 | — | 1.1x | 255.39 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-29 (27d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TSLA | NASDAQ | 384.68 | -0.20 | -2.73 | — | 0.9x | 385.46 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-21 (35d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ERAS | NASDAQ | 15.83 | 13.97 | -2.72 | — | 0.6x | 13.89 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-12 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NXPI | NASDAQ | 239.4 | -6.50 | -2.71 | — | 0.9x | 256.03 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-27 (29d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NRG | NYSE | 90.9 | -6.98 | -2.63 | — | 0.7x | 97.72 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-09 (16d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GOOGM | NASDAQ | 41.38 | -0.31 | -2.61 | — | 1.4x | 41.51 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-28 (28d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NEM | NYSE | 99.69 | -1.03 | -2.59 | — | 0.8x | 100.73 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-22 (34d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BMNR | NYSE | 13.18 | -8.60 | -2.58 | — | 0.5x | 14.42 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-10 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TXN | NASDAQ | 258.44 | -11.25 | -2.56 | — | 0.7x | 291.19 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-21 (35d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CPNG | NYSE | 16.01 | 8.62 | -2.53 | — | 0.8x | 14.74 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-03 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AVEX | NYSE | 11.49 | -5.20 | -2.52 | — | 0.3x | 12.12 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-11 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SWKS | NASDAQ | 80.95 | 4.97 | -2.48 | — | 0.9x | 77.12 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-03 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MDT | NYSE | 96.13 | -4.56 | 2.48 | — | 1.7x | 100.72 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-24 (1d ago) | PRE_GAP | — | Q4 2026 results, report date 2026-11-24 (Nasdaq earnings calendar; no headline lookup), consensus EPS $1.34 |
| IOVA | NASDAQ | 7.33 | 7.64 | -2.46 | — | 0.4x | 6.81 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-05 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AEM | NYSE | 156.46 | -2.03 | -2.44 | — | 0.6x | 159.70 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-28 (28d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMTM | NYSE | 24.8 | 20.10 | -2.42 | — | 0.8x | 20.65 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-23 (2d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-23 (Nasdaq earnings calendar; no headline lookup), consensus EPS $0.63 |
| AGLT | NASDAQ | 5.39 | -8.18 | -2.41 | — | 0.3x | 5.87 | yahoo_chart_daily | 2026-11-23 | US-listed | — | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GOOGN | NASDAQ | 41.24 | -0.34 | -2.40 | — | 1.4x | 41.38 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-28 (28d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| REPL | NASDAQ | 22.24 | 6.11 | -2.38 | — | 0.5x | 20.96 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-28 (28d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| OCUL | NASDAQ | 6.3 | 8.81 | 2.38 | — | 0.7x | 5.79 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-09 (16d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ALM | NASDAQ | 6.77 | -5.58 | -2.36 | — | 0.5x | 7.17 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-12 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RACE | NYSE | 397.82 | -0.36 | 2.33 | — | 1.3x | 399.25 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-03 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| COIN | NASDAQ | 102.345 | -5.92 | -2.24 | — | 0.5x | 108.78 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-29 (27d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| DE | NYSE | 613.76 | -3.04 | -2.24 | — | 1.2x | 633.03 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-25 (0d ago) | PRE_GAP | Y | Q4 FY2026 results (reported 2026-11-25): net income $1.051bn ($3.89/sh) vs $3.93 a year ago; worldwide sales and revenues -2% to $12.115bn; Production & Precision Ag sales -15%, operating profit -33%; FY27 net income outlook $4.50-5.25bn |
| BSP | NASDAQ | 42.86 | -9.33 | -2.19 | — | 0.7x | 47.27 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-19 (6d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-19 (Nasdaq earnings calendar; no headline lookup), consensus EPS $0.26 |
| PTCT | NASDAQ | 62.86 | 5.68 | -2.16 | — | 0.7x | 59.48 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-29 (27d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FRHC | NASDAQ | 171.29 | 4.29 | 2.16 | — | 0.8x | 164.25 | yahoo_chart_daily | 2026-11-23 | US-listed | 2023-08-04 (1209d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| JCI | NYSE | 137.04 | -0.71 | -2.14 | — | 0.8x | 138.02 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-27 (29d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BLSH | NYSE | 19.34 | -8.04 | -2.02 | — | 0.4x | 21.03 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-18 (7d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-18 (Nasdaq earnings calendar; no headline lookup), consensus EPS $0.08 |
| META | NASDAQ | 589.82 | -1.30 | -2.01 | — | 0.8x | 597.60 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-21 (35d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| COCO | NASDAQ | 59.29 | -6.35 | -2.01 | — | 0.7x | 63.31 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-22 (34d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BHVN | NYSE | 13.47 | 7.59 | -2.00 | — | 0.5x | 12.52 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-10-29 (27d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ARW | NYSE | 170.91 | -6.06 | -2.00 | — | 0.6x | 181.93 | yahoo_chart_daily | 2026-11-23 | US-listed | 2026-11-05 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |

## US — QUIET one-liners

| Ticker | Venue | Chg % | Pre-mkt % | Post-mkt % | Move vs avg daily | Ref close | Ref source | Ref asof | US tradeable | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|
| RLAY | NASDAQ | 5.23 | -1.99 | — | 1.2x | 17.22 | yahoo_chart_daily | 2026-11-23 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| ARQT | NASDAQ | 4.95 | -1.96 | — | 1.2x | 27.66 | yahoo_chart_daily | 2026-11-23 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| MS | NYSE | -2.21 | -1.96 | — | 1.0x | 172.60 | yahoo_chart_daily | 2026-11-23 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| GS | NYSE | -2.14 | -1.90 | — | 0.9x | 823.62 | yahoo_chart_daily | 2026-11-23 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| BRO | NYSE | 4.51 | 1.86 | — | 2.4x | 72.73 | yahoo_chart_daily | 2026-11-23 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| ROIV | NASDAQ | 6.84 | 1.82 | — | 2.7x | 39.63 | yahoo_chart_daily | 2026-11-23 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| CRM | NYSE | 4.21 | -1.80 | — | 1.8x | 185.46 | yahoo_chart_daily | 2026-11-23 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| ELV | NYSE | 3.06 | -1.79 | — | 1.4x | 379.55 | yahoo_chart_daily | 2026-11-23 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| PINS | NYSE | 9.47 | -1.78 | — | 3.0x | 16.90 | yahoo_chart_daily | 2026-11-23 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| BOOT | NYSE | 4.01 | -1.77 | — | 1.1x | 132.53 | yahoo_chart_daily | 2026-11-23 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| RVMD | NASDAQ | 7.72 | -1.75 | — | 2.2x | 168.19 | yahoo_chart_daily | 2026-11-23 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| MRCY | NASDAQ | -5.35 | -1.75 | — | 1.1x | 76.25 | yahoo_chart_daily | 2026-11-23 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| VERA | NASDAQ | 7.05 | -1.69 | — | 2.1x | 27.08 | yahoo_chart_daily | 2026-11-23 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| MLTX | NASDAQ | 11.61 | -1.68 | — | 2.5x | 11.71 | yahoo_chart_daily | 2026-11-23 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| ANF | NYSE | 19.69 | -1.68 | — | 5.3x | 140.45 | yahoo_chart_daily | 2026-11-23 | US-listed | — | Q4 2026 results, report date 2026-11-24 (Nasdaq earnings calendar; no headline lookup), consensus EPS $3.15 |

## EU/UK — Headline table

| Ticker | Market | Venue | Close | Chg % | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | Session asof | Settle | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AMS2 | austria | VIE | 15.2 | +15.59 | EUR | 2.8x | 13.15 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | live | none | 2026-11-13 (12d ago) | — | no catalyst lookup (outside the per-run budget) |
| OCDO | uk | LSE | 274.2 | -11.95 | GBX | 5.6x | 311.40 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | live | none | 2026-07-16 (132d ago) | — | no catalyst lookup (outside the per-run budget) |
| BIOA_B | sweden | OMXSTO | 357.6 | +10.78 | SEK | 8.2x | 322.80 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | live | none | 2026-11-25 (0d ago) | — | no catalyst lookup (outside the per-run budget) |
| RCO | france | EURONEXT | 56.5 | +9.92 | EUR | 7.7x | 51.40 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | live | none | 2026-11-25 (0d ago) | — | no catalyst lookup (outside the per-run budget) |
| SECT_B | sweden | OMXSTO | 362.4 | +9.82 | SEK | 5.7x | 330.00 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | live | none | 2026-11-25 (0d ago) | — | no catalyst lookup (outside the per-run budget) |
| SRAIL | switzerland | SIX | 27.76 | -9.16 | CHF | 8.2x | 30.56 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | live | none | 2026-08-26 (91d ago) | — | no catalyst lookup (outside the per-run budget) |
| PETS | uk | LSE | 284.78 | +9.03 | GBX | 8.3x | 261.20 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | live | none | 2026-11-25 (0d ago) | — | no catalyst lookup (outside the per-run budget) |
| ELON | sweden | OMXSTO | 73.2 | +7.02 | SEK | 1.8x | 68.40 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | live | none | 2026-02-20 (278d ago) | — | no catalyst lookup (outside the per-run budget) |
| BVI | france | EURONEXT | 31.85 | +6.77 | EUR | 8.9x | 29.83 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | live | none | 2026-07-29 (119d ago) | — | no catalyst lookup (outside the per-run budget) |
| SSIC | uk | LSE | 66.2342 | -6.32 | GBX | 4.0x | 70.70 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | live | none | — | — | no catalyst lookup (outside the per-run budget) |
| GRE | spain | BME | 53.6 | +6.14 | EUR | 1.6x | 50.50 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | live | none | 2026-11-25 (0d ago) | Y | 9M 2026 results (reported 2026-11-25): revenue EUR845M +23%, EBITDA EUR141M +28%, net profit EUR72M +58%; 2.1 GW / 8.5 GWh in operation and under construction, 1.1 GW / 6.8 GWh added to backlog |
| WAF | germany | XETR | 47.04 | -6.01 | EUR | 1.4x | 50.05 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | live | none | 2026-11-04 (21d ago) | N | no company news: the global semiconductor selloff continued (AIXTRON's UBS downgrade took the MDAX equipment names down 5-9% on 24 Nov; Nvidia -4.65% pre-market and the Philadelphia Semiconductor Index -7.9% on 24 Nov dragged Asian chip values lower), taking Siltronic to a six-month low at EUR47.00 |
| ASMDEE_B | sweden | OMXSTO | 151.9 | -6.00 | SEK | 3.8x | 161.60 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | live | none | 2026-11-13 (12d ago) | — | no catalyst lookup (outside the per-run budget) |
| VOW3 | germany | XETR | 65.94 | +5.74 | EUR | 3.4x | 62.36 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | live | none | 2026-10-29 (27d ago) | — | no catalyst lookup (outside the per-run budget) |
| IQMX | finland | OMXHEX | 6.15 | +5.58 | EUR | 1.1x | 5.83 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | live | none | 2026-11-05 (20d ago) | — | no catalyst lookup (outside the per-run budget) |
| EYDAP | greece | ATHEX | 12.3 | -5.38 | EUR | 4.4x | 13.00 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | live | none | 2026-09-24 (62d ago) | — | no catalyst lookup (outside the per-run budget) |
| SAN | france | EURONEXT | 98.54 | +5.30 | EUR | 2.8x | 93.58 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | live | none | — | — | no catalyst lookup (outside the per-run budget) |
| BMW | germany | GETTEX | 55.72 | +5.13 | EUR | 3.8x | 53.26 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | live | none | 2026-11-04 (21d ago) | — | no catalyst lookup (outside the per-run budget) |
| JSW | poland | GPW | 23.94 | +4.91 | PLN | 2.4x | 22.82 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | live | none | 2026-11-19 (6d ago) | — | no catalyst lookup (outside the per-run budget) |
| IDR | spain | BME | 54.56 | +4.88 | EUR | 1.8x | 52.02 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | live | none | 2026-10-29 (27d ago) | — | no catalyst lookup (outside the per-run budget) |
| VAR | norway | OSL | 42.49 | -4.84 | NOK | 2.3x | 44.65 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | live | ADR (OTC:VARRY) | 2026-10-21 (35d ago) | — | no catalyst lookup (outside the per-run budget) |
| SMOP | norway | OSL | 51.4 | -4.81 | NOK | 1.4x | 54.00 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | live | none | 2026-10-29 (27d ago) | — | no catalyst lookup (outside the per-run budget) |
| ALO | france | EURONEXT | 8.232 | -4.81 | EUR | 1.3x | 8.65 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | live | none | 2026-11-17 (8d ago) | — | no catalyst lookup (outside the per-run budget) |
| LINK | norway | OSL | 22.42 | -4.76 | NOK | 3.0x | 23.54 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | live | none | 2026-11-04 (21d ago) | — | no catalyst lookup (outside the per-run budget) |
| CCC | uk | LSE | 4348 | -4.73 | GBX | 1.9x | 4564.00 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | live | none | 2026-09-08 (78d ago) | — | no catalyst lookup (outside the per-run budget) |
| MDATA | norway | OSL | 12.54 | -4.71 | NOK | 2.2x | 13.16 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | live | none | 2026-10-30 (26d ago) | — | no catalyst lookup (outside the per-run budget) |
| RBI | austria | VIE | 55.35 | -4.65 | EUR | 2.4x | 58.05 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | live | none | 2026-11-03 (22d ago) | N | no fresh catalyst found: no RBI release since the 3 Nov Q3 results and the upgraded net-interest-income guidance; the drop came in a broad Austrian bank selloff (ATX -0.9% with the heavyweights lower) that has hit the Vienna banks on each of the last four sessions |
| OPTIMA | greece | ATHEX | 14.16 | -4.65 | EUR | 2.5x | 14.85 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | live | US line (OTC:OHLTF) | 2026-11-11 (14d ago) | — | no catalyst lookup (outside the per-run budget) |
| CBRAIN | denmark | OMXCOP | 96 | -4.57 | DKK | 1.3x | 100.60 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | live | none | 2026-08-20 (97d ago) | — | no catalyst lookup (outside the per-run budget) |

## AU (ASX) — Headline table

| Ticker | Venue | Close | Chg % | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | Session asof | Settle | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| WEB | ASX | 2.6 | -23.53 | AUD | 6.2x | 3.40 | yahoo_chart_daily | 2026-11-23 | 2026-11-25 | settled | US line (OTC:TSWCF) | 2026-11-24 (1d ago) | — | no catalyst lookup (outside the per-run budget) |
| DVP | ASX | 2.46 | -9.56 | AUD | 2.1x | 2.72 | yahoo_chart_daily | 2026-11-23 | 2026-11-25 | settled | none | 2026-03-08 (262d ago) | Y | Pioneer Dome Project Update (25 Nov): Develop Global will pause operations at its WA lithium mine in December 2026 because the fall in the lithium price makes direct shipping ore uneconomic once the Trafigura offtake floor price expires on 31 Dec; the site moves to care and maintenance with a low-cost restart option |
| TUA | ASX | 1.63 | -9.44 | AUD | 2.1x | 1.80 | yahoo_chart_daily | 2026-11-23 | 2026-11-25 | settled | none | 2026-03-24 (246d ago) | — | pending catalyst lookup |

## APAC/Gulf — Headline table

| Ticker | Market | Venue | Close | Chg % | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | Session asof | Settle | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CITY | indonesia | IDX | 168 | +34.40 | IDR | 6.4x | 125.00 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | settled | ADR (OTC:CDEVY) | — | — | no catalyst lookup (outside the per-run budget) |
| VOKS | indonesia | IDX | 450 | +25.00 | IDR | 3.0x | 360.00 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| YUPI | indonesia | IDX | 1360 | +24.77 | IDR | 2.9x | 1090.00 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| 300086 | china | SZSE | 4.85 | +20.05 | CNY | 7.1x | 4.04 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| 300703 | china | SZSE | 17.8 | +20.03 | CNY | 3.7x | 14.83 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | settled | none | 2026-04-17 (222d ago) | — | no catalyst lookup (outside the per-run budget) |
| 301089 | china | SZSE | 21.34 | +20.02 | CNY | 6.5x | 17.78 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| YAASHVI | india | BSE | 122.64 | +20.00 | INR | 4.1x | 102.20 | yahoo_chart_daily | 2026-11-22 | 2026-11-24 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| SGMART | india | NSE | 829.45 | -20.00 | INR | 5.2x | 1036.80 | yahoo_chart_daily | 2026-11-22 | 2026-11-24 | settled | none | 2026-10-27 (29d ago) | — | no catalyst lookup (outside the per-run budget) |
| RMC | india | NSE | 196.33 | +20.00 | INR | 7.1x | 163.61 | yahoo_chart_daily | 2026-11-22 | 2026-11-24 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| 9517 | ksa | TADAWUL | 14 | -12.83 | SAR | 5.6x | 16.06 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| CNT | thailand | SET | 1.95 | -12.16 | THB | 3.5x | 2.22 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| SMT | thailand | SET | 5.02 | -11.62 | THB | 2.5x | 5.68 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | settled | none | 2026-11-05 (20d ago) | — | no catalyst lookup (outside the per-run budget) |
| CFRESH | thailand | SET | 1.4 | -11.39 | THB | 4.0x | 1.58 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| 4083 | ksa | TADAWUL | 21.01 | +10.00 | SAR | 4.0x | 19.10 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | settled | none | 2026-11-02 (23d ago) | N | Tasheel unit signs a $588 million revolving securitization contract (MT Newswires, 25 Nov) - the best Tadawul performer of the session at +10.0%; HSBC cut its Tasheel price target on 23 Nov while keeping Buy |
| 4144 | ksa | TADAWUL | 85.8 | +10.00 | SAR | 2.1x | 78.00 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| AWX | singapore | SGX | 5.79 | -6.76 | SGD | 1.1x | 6.21 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | settled | none | 2026-08-12 (105d ago) | — | no catalyst lookup (outside the per-run budget) |
| CC3 | singapore | SGX | 1.09 | +4.81 | SGD | 5.3x | 1.04 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | settled | none | 2026-08-12 (105d ago) | N | StarHub and Keppel signed definitive agreements to combine StarHub with M1 in an all-share deal - 651,675,290 new shares (27.4% of the enlarged capital) for roughly S$660M, plus the exercised call option on Circles.Life's Singapore mobile business; S$110M annual cost savings identified |
| 5E2 | singapore | SGX | 1.36 | -4.23 | SGD | 1.7x | 1.42 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | settled | none | 2026-07-30 (118d ago) | — | no catalyst lookup (outside the per-run budget) |
| RYM | newzealand | NZX | 1.7 | -3.95 | NZD | 2.4x | 1.77 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | settled | none | 2026-10-15 (41d ago) | — | no catalyst lookup (outside the per-run budget) |
| SKL | newzealand | NZX | 8 | +2.96 | NZD | 2.1x | 7.77 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | settled | none | 2026-08-20 (97d ago) | N | no fresh catalyst found: no announcement since the 21 Oct AGM, where the chair guided FY27 NPAT to NZ$67-72M on a 15% Q1 profit rise; the shares have drifted rather than moved on news |
| MEL | newzealand | NZX | 5.62 | +2.74 | NZD | 1.6x | 5.47 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | settled | none | 2026-08-25 (92d ago) | — | no catalyst lookup (outside the per-run budget) |

## Source health

- scanner_calls: 57 | scanner_errors: 0
- markets_scanned: US + 17 EU/UK + ASX + 7 APAC/Gulf (india, thailand, indonesia, china, singapore, newzealand, ksa)
- pipeline_version: 2026-11-20.1
- et_clock: zoneinfo America/New_York (DST-aware; a fixed UTC-4 mislabels every winter fire)
- premarket_window: 04:00-09:30 ET, resolved with zoneinfo (09:00-14:30 UTC in winter, 08:00-13:30 UTC in summer)
- session_selection: by DATE and order, never by a modal time-of-day. Yahoo stamps a daily bar at the session open, so the ET stamp of the SAME session shifts by one hour across a DST boundary; a modal filter kept the OLDER bars and discarded the NEWEST ones, which rolled the base back to the prior-prior session (66 US + 21 ASX rows lost on 2026-11-03, 24 of 25 ASX rows lost on 2026-11-04).
- yahoo_calls: 310 | yahoo_429: 0 | yahoo_errors: 0 | yahoo_breaker: closed
- reference_close (screener vs Yahoo, resolved BEFORE the tables were built): agree=298 mismatch=2 unverified=0 stale_reference=2
  method: the screener's implied reference close (close / (1 + change/100)) is compared
  with Yahoo's own reference close. A match proves the move was measured against the
  TRUE prior close; a mismatch means the row sits on a STALE reference (phantom move).
  Coverage: every row of the US headline, US QUIET, EU/UK and ASX tables is checked.
  Yahoo bar mode: {"closed": 269, "live": 29} (closed = last completed session bar;
  live = in-progress EU/UK session bar, which is what a weekday 08:00 ET EU move needs)
  live drift between the screener snapshot and the later Yahoo print: median=0.00pp max=1.72pp (expected on a live market)
- cross_check mismatches: [{"region": "US", "symbol": "SNDK", "tv": -11.128, "yahoo": -17.421, "delta": 6.293, "ref_delta_pct": -7.082, "tv_implied_ref": 87.71, "yahoo_ref": 94.395, "yahoo_date": "2026-11-24", "yahoo_ref_date": "2026-11-19", "verdict": "stale_reference"}, {"region": "germany", "symbol": "IFX.DE", "tv": -7.469, "yahoo": -4.413, "delta": -3.056, "ref_delta_pct": 3.007, "tv_implied_ref": 45.05, "yahoo_ref": 43.735, "yahoo_date": "2026-11-25", "yahoo_ref_date": "2026-11-24", "verdict": "stale_reference"}]
- rows_dropped_stale_ref: 2 (rows whose screener-implied reference close disagreed with Yahoo's by more than 0.5%; they are dropped, not published)
- rows_dropped_unresolved_ref: 0 (rows whose reference close could not be resolved from Yahoo at all - the base of the move is unverifiable, so the row is dropped rather than published with a '—' base)
- cross_region_rows_dropped: ['ELV@AU'] (the same name on a US venue and a foreign venue - the US row is kept so the name appears exactly once)
- us_premarket_check (Yahoo 1-min pre/post feed vs the screener pre-market column, base = the IMMEDIATELY prior session's close): checked=10 within_1pp=9 within_3pp=10 unavailable=0
- markets_with_lt5_rows: ['uk:egreater=3', 'netherlands:egreater=0', 'netherlands:less=4', 'belgium:egreater=2', 'belgium:less=0', 'portugal:egreater=0', 'portugal:less=0', 'ireland:egreater=0', 'ireland:less=2', 'italy:egreater=2', 'switzerland:egreater=2', 'switzerland:less=4', 'spain:egreater=4', 'spain:less=2', 'norway:egreater=1', 'denmark:egreater=2', 'finland:egreater=1', 'finland:less=4', 'poland:egreater=2', 'poland:less=3', 'austria:egreater=2', 'austria:less=3', 'greece:egreater=0', 'singapore:egreater=3', 'singapore:less=4', 'newzealand:egreater=2', 'newzealand:less=1']
  NOTE: this fires per market AND direction, so it is NOT a coverage-failure signal on
  its own. A 'less' count of 0-3 means almost nothing fell more than 2.5% that session
  (a broad up-day); a small 'egreater' count usually means a small market with few
  names above the $1B market-cap floor. Check the median change before calling it a gap.
- filters: volume>10000 (removes stale-reference rows), country=home for EU/UK/AU,
  exchange drop-list for US, US venue allow-list, US preferred (slash ticker) excluded
- pass_b2 (US pre-market gap scan - "gapped today, flat yesterday"): candidates=57 deduped_against_pass_a_b=43 published=14 (up=1 down=56)
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
- bod_no_extended_hours: 128 (deferred to the next scan; not in the headline table)
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
- earnings_calendar: Nasdaq public earnings calendar (calls=8 errors=0 symbols=257) - the source of record for the US earnings date, and the ranking key for the search budget
- earnings_field_stale_rows: 0 (the screener's earnings_release_date disagreed with the calendar; the calendar's date is published)
- earnings_dates: the published `Last earnings` date by source - catalog (researched) 9, calendar 14, asx 0, screener 259. The chain is researched -> calendar (US) -> ASX feed (AU) -> the screener's field, which is the FALLBACK and the one that lags (2026-11-12: NBIS carried the previous quarter's date on the morning it reported, and MEKO, NORBT and FG carried July and August dates on the morning they all reported).
- asx_announcements: 6 results-classified announcement(s) for the last ASX session (calls=1 errors=0); the announcement date IS the report date, and the meeting/AGM/offer/assay headlines are excluded because they are not reports
- earnings_date_quality: 3 of 21 markets publish a FRESH earnings date (median age <= 14d); the table below gives each market's rows, the rows with NO date at all, the median age of the published date and the rows within 7 and 30 days - the reader sees the input quality instead of trusting it
| market | rows | no date | median age | <=7d | <=30d |
|---|---|---|---|---|---|
| au | 3 | 0 | 246d | 1 | 1 |
| austria | 2 | 0 | 22d | 0 | 2 |
| china | 3 | 2 | 222d | 0 | 0 |
| denmark | 1 | 0 | 97d | 0 | 0 |
| finland | 1 | 0 | 20d | 0 | 1 |
| france | 4 | 1 | 8d | 1 | 2 |
| germany | 3 | 0 | 21d | 0 | 3 |
| greece | 2 | 0 | 62d | 0 | 1 |
| india | 3 | 2 | 29d | 0 | 1 |
| indonesia | 3 | 3 | n/a | 0 | 0 |
| ksa | 3 | 2 | 23d | 0 | 1 |
| newzealand | 3 | 0 | 92d | 0 | 0 |
| norway | 4 | 0 | 27d | 0 | 3 |
| poland | 1 | 0 | 6d | 1 | 1 |
| singapore | 3 | 0 | 105d | 0 | 0 |
| spain | 2 | 0 | 27d | 1 | 2 |
| sweden | 4 | 0 | 12d | 2 | 3 |
| switzerland | 1 | 0 | 91d | 0 | 0 |
| thailand | 3 | 2 | 20d | 0 | 1 |
| uk | 4 | 1 | 78d | 1 | 1 |
| us | 229 | 2 | 22d | 22 | 191 |
- earnings_tiers: fresh=1 near=9 (fresh = the report is dated on the scan date, near = the previous session)
- one_table_rule: each name appears exactly once, in exactly one table, with its
  catalyst in that row's last column. There is no separate catalysts section.
- data_date: US regular session close of the prior trading day; extended-hours columns
  carry the prior session's prints
- settlement_state: 24 settled, 29 live (a live row's move is a mid-session snapshot, not the session's result)
- rows_per_market (EU/UK, cap 4/market): {'austria': 4, 'uk': 4, 'sweden': 4, 'france': 4, 'switzerland': 4, 'germany': 4, 'spain': 4, 'finland': 4, 'greece': 4, 'poland': 4, 'norway': 4, 'denmark': 4, 'netherlands': 4, 'italy': 4, 'ireland': 2, 'belgium': 2} — the cap stops one thin market taking the table; the EU/UK table was 28% Sweden over nine runs (73 of 264 rows) while Belgium and Greece never appeared once.
- rows_per_market (APAC/Gulf, cap 3/market): {'indonesia': 3, 'china': 3, 'india': 3, 'ksa': 3, 'thailand': 3, 'singapore': 3, 'newzealand': 3}
- deprecations: mcp__tradingview-advanced__*, mcp__tradingview__*, mcp__financekit__*,
  mcp__stocktwits__* are ABSENT in Cloud sessions (tool_search 0 hits; connector catalog
  holds only media + credential tools). The public screener replaces them.

- degraded_sources: 0
  (none - every source answered for every published row)

## Audit line

`earnings-reaction target=earnings-reactions:2026-11-25 candidates=571 amc_reactions=0 pre_gaps=229 eu_reactions=29 asx_reactions=3 apac_reactions=19 catalyst_lookups=16 bod=128 pass_b2_candidates=57 pass_b2_dedup=43 pass_b2_published=14 earnings_calendar_rows=257 earnings_tiers_fresh=1 earnings_tiers_near=9 earnings_field_stale_rows=0 earnings_dates_catalog=9 earnings_dates_asx=0 asx_ann_rows=6 rows_dropped_stale_ref=2 rows_dropped_unresolved_ref=0 degraded_sources=0`
