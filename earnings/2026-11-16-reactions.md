# Earnings reaction scanner — 2026-11-16

- Cron: `0 8 * * 1-5` America/New_York (weekdays, 08:00 ET)
- Fire time (ET): 2026-11-16 08:13:46 Mon
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

- 0 AMC reactions, 165 pre-market gaps, 81 without extended-hours data; 29 EU/UK and 4 ASX movers, 16 APAC/Gulf movers.
- Pass B2 (the US pre-market gap scan) met the filter on 73 names (5 up, 68 down); 39 were already a Pass A/B row and are recorded as dedupes, and 33 reached a table.
- Biggest US extended-hours move: LXEO PRE_GAP (37.28%).
- Biggest EU/UK move: PLT (+15.25%, norway).
- Biggest ASX move: ELD (+7.49%).
- Biggest APAC/Gulf move: AREA (+34.46%, indonesia).
- 0 of the 29 EU/UK rows are SETTLED and 29 are LIVE (mid-session). The 12:15 ET settlement pass publishes where those
  live moves actually closed.
- EU/AU/APAC earnings-driven tagging is keyword-based on headlines (best-effort). A row
  whose lookup was not performed carries NO verdict — only a researched row does.

## Actionable read

- **Move vs this name's own history.** The `Move vs avg daily` column divides the
  reaction by the name's own mean absolute daily move over its last
  20 completed sessions. A -27% move in a name that averages +-3% is a
  different event from a -8% move in a name that averages +-7%.
- **US-listed and tradeable vs foreign-only.** 180 published US rows are on a
  US venue; 1 more foreign reactions have a US ADR line
  (the `US tradeable` column carries the ticker); 29 are foreign-only and
  cannot be bought directly by a US reader.
- **Not yet fully priced — US (hypothesis, not a recommendation).**
  TU — +26.96%, 1.87% mean absolute daily move over the last 20 completed sessions, 14.4x that average, reference close 8.52 dated 2026-11-12, US access: US-listed, the move now (+26.96%) is larger than the move it follows (+0.12%); the reaction is still being repriced. Hypothesis only: this artifact states no
  direction and no trade.
- **Not yet fully priced — EU/UK (hypothesis, not a recommendation).**
  N91 — -8.81%, 0.95% mean absolute daily move over the last 20 completed sessions, 9.3x that average, reference close 203.80 dated 2026-11-13, US access: none, the move now (-8.81%) is larger than the move it follows (-1.64%); the reaction is still being repriced. Hypothesis only: this artifact states no
  direction and no trade.
- **Not yet fully priced — AU (ASX) (hypothesis, not a recommendation).**
  ELD — +7.49%, 1.35% mean absolute daily move over the last 20 completed sessions, 5.6x that average, reference close 6.54 dated 2026-11-12, US access: none, the move now (+7.49%) is larger than the move it follows (-0.46%); the reaction is still being repriced. Hypothesis only: this artifact states no
  direction and no trade.

## US — Headline table

| Ticker | Venue | Close | Chg % | Pre-mkt % | Post-mkt % | Move vs avg daily | Ref close | Ref source | Ref asof | US tradeable | Last earnings | Tag | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LXEO | NASDAQ | 2.87 | -1.37 | 37.28 | — | 9.2x | 2.91 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-12-14 | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TU | NYSE | 8.53 | 0.12 | 26.96 | — | 14.4x | 8.52 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-06 (10d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SMMT | NASDAQ | 14.15 | -6.14 | -13.00 | — | 2.4x | 15.07 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-04 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| DRTS | NASDAQ | 13.38 | 0.15 | 11.14 | — | 3.8x | 13.36 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-08-10 (98d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BNC | NASDAQ | 4.14 | -3.72 | -11.11 | — | 2.1x | 4.30 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-09-11 (66d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| POET | NASDAQ | 5.13 | -1.54 | -9.75 | — | 1.7x | 5.21 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-16 (0d ago) | PRE_GAP | Y | Q3 2026 results due pre-market 2026-11-16 07:00 ET (issuer release 2026-10-16); release figures not confirmed at scan time 08:30 ET; consensus revenue CAD 0.97M, net loss CAD 16.8M |
| PURR | NASDAQ | 8.7 | -1.19 | -9.54 | — | 1.7x | 8.80 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-05 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ASST | NASDAQ | 21.36 | -4.00 | -9.41 | — | 1.7x | 22.25 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-06 (10d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FWDI | NASDAQ | 4.94 | -2.76 | -9.31 | — | 2.0x | 5.08 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-08-12 (96d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BRUN | NASDAQ | 5.53 | -6.59 | -8.68 | — | 0.9x | 5.92 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-12 (4d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-12 (Nasdaq earnings calendar; no headline lookup), consensus EPS ($0.17) |
| MSTR | NASDAQ | 111.62 | -2.44 | -8.39 | — | 2.3x | 114.41 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-10-29 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GLXY | NASDAQ | 14.38 | -5.27 | -8.21 | — | 1.0x | 15.18 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-10-27 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CRCL | NYSE | 62.2 | -2.54 | -8.17 | — | 2.3x | 63.82 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-04 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ACRS | NASDAQ | 3.92 | -2.00 | -7.92 | — | 2.4x | 4.00 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-05 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BMNR | NYSE | 17.58 | -4.72 | -7.74 | — | 1.7x | 18.45 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-10 (6d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-10 (Nasdaq earnings calendar; no headline lookup), consensus EPS $0.01 |
| VICR | NASDAQ | 159.05 | -3.42 | -7.51 | — | 1.1x | 164.69 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-10-20 (27d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SBET | NASDAQ | 5.61 | -2.77 | -7.49 | — | 1.7x | 5.77 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-09 (7d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| COIN | NASDAQ | 127.645 | -2.31 | -7.48 | — | 2.1x | 130.67 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-10-29 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AXTI | NASDAQ | 41.84 | -3.90 | -7.31 | — | 0.9x | 43.54 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-10-29 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MXL | NASDAQ | 55.78 | -5.39 | -7.23 | — | 0.9x | 58.96 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-10-22 (25d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SITM | NASDAQ | 444.54 | -5.53 | -7.09 | — | 1.2x | 470.55 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-04 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MARA | NASDAQ | 6.99 | -2.92 | -7.01 | — | 1.3x | 7.20 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-09 (7d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-09 (Nasdaq earnings calendar; no headline lookup), consensus EPS ($0.58) |
| WOLF | NYSE | 24.83 | -6.34 | -6.97 | — | 1.1x | 26.51 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-04 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ABTC | NASDAQ | 5.07 | 0.40 | -6.90 | — | 1.2x | 5.05 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-04 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PENG | NASDAQ | 47.36 | -5.47 | -6.88 | — | 0.9x | 50.10 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-10-06 (41d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| OPTX | NASDAQ | 7.08 | 4.12 | -6.78 | — | 0.8x | 6.80 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-13 (3d ago) | PRE_GAP | Y | Q3 2026 results (reported 2026-11-13): record revenue $8.5M +23% y/y, gross profit +127%, net income swung to +$0.2M from -$1.4M, adj. EBITDA 10% of revenue |
| NBIS | NASDAQ | 115.88 | -9.92 | -6.76 | — | 0.9x | 128.64 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-12 (4d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-12 (Nasdaq earnings calendar; no headline lookup), consensus EPS ($0.61) |
| BTDR | NASDAQ | 5.6 | -8.65 | -6.70 | — | 0.8x | 6.13 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-10 (6d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-10 (Nasdaq earnings calendar; no headline lookup), consensus EPS ($0.33) |
| AAOI | NASDAQ | 49.89 | -5.60 | -6.67 | — | 0.9x | 52.85 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-05 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| COHU | NASDAQ | 43.59 | -3.13 | -6.65 | — | 1.1x | 45.00 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-10-28 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CIFR | NASDAQ | 6.86 | -4.06 | -6.63 | — | 0.8x | 7.15 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-02 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| UCTT | NASDAQ | 46.35 | -3.64 | -6.58 | — | 1.0x | 48.10 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-10-27 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| WULF | NASDAQ | 12.62 | -3.22 | -6.50 | — | 1.0x | 13.04 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-06 (10d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LITE | NASDAQ | 596.62 | -4.49 | -6.47 | — | 1.0x | 624.65 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-02 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| COHR | NYSE | 218.15 | -6.00 | -6.41 | — | 1.0x | 232.08 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-04 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MTSI | NASDAQ | 232.06 | -5.57 | -6.40 | — | 1.1x | 245.76 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-05 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MAZE | NASDAQ | 34.33 | -4.88 | 6.32 | — | 2.2x | 36.09 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-09 (7d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-09 (Nasdaq earnings calendar; no headline lookup), consensus EPS ($0.78) |
| XXI | NYSE | 4.95 | -1.00 | -6.26 | — | 2.1x | 5.00 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-13 (3d ago) | PRE_GAP | Y | Q3 2026 results (reported 2026-11-13): net income $1.087B on a $1.093B Bitcoin fair-value gain; 43,514 BTC held, $102.8M cash, $486.5M convertible principal |
| FORM | NASDAQ | 87.53 | -5.19 | -6.26 | — | 0.9x | 92.32 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-10-28 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| HUT | NASDAQ | 57.57 | -7.11 | -6.26 | — | 0.8x | 61.98 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-04 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NUAI | NASDAQ | 3.2 | 17.65 | -6.25 | — | 0.5x | 2.72 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-12 (4d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-12 (Nasdaq earnings calendar; no headline lookup), consensus EPS ($0.13) |
| AEHR | NASDAQ | 56.98 | -6.65 | -6.23 | — | 0.8x | 61.04 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-02 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RIOT | NASDAQ | 17.52 | -1.74 | -6.22 | — | 1.1x | 17.83 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-04 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ICHR | NASDAQ | 35.72 | -3.64 | -6.22 | — | 1.1x | 37.07 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-02 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ONTO | NYSE | 203.62 | -2.89 | -6.19 | — | 1.1x | 209.67 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-09 (7d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-09 (Nasdaq earnings calendar; no headline lookup), consensus EPS $2.27 |
| ACMR | NASDAQ | 47.95 | -3.87 | -6.15 | — | 1.2x | 49.88 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-05 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SNDK | NASDAQ | 885.01 | -5.59 | -6.07 | — | 1.0x | 937.46 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-10-29 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| IREN | NASDAQ | 18.17 | -6.72 | -6.05 | — | 0.8x | 19.48 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-05 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CLSK | NASDAQ | 6.65 | -2.78 | -6.02 | — | 0.9x | 6.84 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-08-06 (102d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| USAR | NASDAQ | 8.16 | 1.12 | -6.00 | — | 1.1x | 8.07 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-09 (7d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-09 (Nasdaq earnings calendar; no headline lookup), consensus EPS ($0.19) |
| CRWV | NASDAQ | 53.13 | -6.13 | -6.00 | — | 0.9x | 56.60 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-10 (6d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-10 (Nasdaq earnings calendar; no headline lookup), consensus EPS ($1.45) |
| MRVL | NASDAQ | 156.76 | -4.68 | -5.94 | — | 1.0x | 164.45 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-08-27 (81d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| HOOD | NASDAQ | 77.86 | -4.29 | -5.94 | — | 1.8x | 81.35 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-10-27 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| APLD | NASDAQ | 15.97 | -5.78 | -5.93 | — | 0.9x | 16.95 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-10-07 (40d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| KLIC | NASDAQ | 69.07 | -4.63 | -5.89 | — | 1.4x | 72.42 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-08-05 (103d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ALAB | NASDAQ | 221.83 | -2.62 | -5.86 | — | 1.0x | 227.79 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-03 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| STX | NASDAQ | 528.29 | -3.09 | -5.83 | — | 1.2x | 545.14 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-10-27 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CRDO | NASDAQ | 131.51 | -5.94 | -5.82 | — | 0.8x | 139.81 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-09-01 (76d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SMTC | NASDAQ | 114.59 | -4.06 | -5.75 | — | 0.8x | 119.44 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-08-25 (83d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BXDC | NYSE | 16.69 | 0.85 | 5.69 | — | 4.5x | 16.55 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-16 (0d ago) | PRE_GAP | Y | Q3 2026 results due before the 9:00 a.m. ET call on 2026-11-16 (issuer announcement 2026-10-22); not confirmed at scan time; consensus EPS $0.13, revenue $15.9M |
| AUGO | NASDAQ | 75.02 | -3.75 | -5.68 | — | 1.2x | 77.94 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-05 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CORZ | NASDAQ | 14.52 | 0.97 | -5.65 | — | 1.0x | 14.38 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-05 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SGML | NASDAQ | 5.15 | 2.79 | -5.63 | — | 1.0x | 5.01 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-13 (3d ago) | PRE_GAP | Y | Q3 2026 results (reported 2026-11-13): net sales $13.5M -52.6% y/y and net loss $25.9M after operations were stopped ~65% of the quarter; $125M convertible bond to cut short-term debt 85% |
| MU | NASDAQ | 778.31 | -2.52 | -5.56 | — | 1.1x | 798.44 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-09-30 (47d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| WYFI | NASDAQ | 9.43 | -8.76 | -5.51 | — | 0.6x | 10.34 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-10 (6d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-10 (Nasdaq earnings calendar; no headline lookup), consensus EPS ($0.36) |
| FPS | NYSE | 22.12 | -0.14 | -5.47 | — | 0.6x | 22.15 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-12 (4d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-12 (Nasdaq earnings calendar; no headline lookup), consensus EPS $0.18 |
| FN | NYSE | 327.98 | -7.31 | -5.42 | — | 0.8x | 353.83 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-02 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| VIAV | NASDAQ | 30.72 | -5.59 | -5.40 | — | 0.9x | 32.54 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-04 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BE | NYSE | 191.99 | -4.92 | -5.38 | — | 0.8x | 201.93 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-10-22 (25d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NVTS | NASDAQ | 8.95 | -6.38 | -5.36 | — | 0.9x | 9.56 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-03 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| WDC | NASDAQ | 295.65 | -5.00 | -5.30 | — | 1.0x | 311.21 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-10-22 (25d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMKR | NASDAQ | 36.11 | -2.72 | -5.29 | — | 1.0x | 37.12 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-10-26 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BW | NYSE | 4.56 | -6.17 | -5.28 | — | 0.8x | 4.86 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-09 (7d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-09 (Nasdaq earnings calendar; no headline lookup), consensus EPS $0.03 |
| SANM | NASDAQ | 158.31 | -3.75 | -5.25 | — | 1.1x | 164.48 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-09 (7d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-09 (Nasdaq earnings calendar; no headline lookup), consensus EPS $2.89 |
| VRT | NYSE | 202.07 | -3.61 | -5.23 | — | 0.9x | 209.64 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-10-28 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CRMD | NASDAQ | 4.66 | -3.72 | 5.23 | — | 1.1x | 4.84 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-12 (4d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-12 (Nasdaq earnings calendar; no headline lookup), consensus EPS ($0.09) |
| AMD | NASDAQ | 534.06 | -8.75 | -5.21 | — | 0.9x | 585.30 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-03 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LGN | NASDAQ | 35 | -3.50 | -5.18 | — | 0.7x | 36.27 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-12 (4d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-12 (Nasdaq earnings calendar; no headline lookup), consensus EPS $0.50 |
| VSH | NYSE | 26.62 | -4.21 | -5.15 | — | 0.9x | 27.79 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-04 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| INTC | NASDAQ | 59.66 | -2.52 | -5.15 | — | 0.9x | 61.20 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-10-29 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FLNC | NASDAQ | 4.68 | -1.16 | -5.13 | — | 1.0x | 4.74 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-08-05 (103d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FIGR | NASDAQ | 25.22 | -1.75 | -5.11 | — | 1.2x | 25.67 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-12 (4d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-12 (Nasdaq earnings calendar; no headline lookup), consensus EPS $0.31 |
| PDFS | NASDAQ | 36.98 | -9.01 | -5.08 | — | 0.8x | 40.64 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-05 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| HPE | NYSE | 48.29 | -3.73 | -5.05 | — | 1.3x | 50.16 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-09-02 (75d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CLS | NYSE | 240.34 | -5.39 | -5.05 | — | 0.8x | 254.03 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-10-26 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ONDS | NASDAQ | 5.16 | -3.01 | -5.04 | — | 0.8x | 5.32 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-12 (4d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-12 (Nasdaq earnings calendar; no headline lookup), consensus EPS ($0.13) |
| ENTG | NASDAQ | 147.41 | -3.79 | -5.01 | — | 1.0x | 153.21 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-10-29 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TER | NASDAQ | 249.55 | -5.38 | -4.84 | — | 1.0x | 263.75 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-10-27 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMAT | NASDAQ | 370.5 | -2.74 | -4.83 | — | 1.1x | 380.95 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-12 (4d ago) | PRE_GAP | — | Q4 2026 results, report date 2026-11-12 (Nasdaq earnings calendar; no headline lookup), consensus EPS $4.06 |
| CIEN | NYSE | 280.54 | -4.57 | -4.83 | — | 0.8x | 293.99 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-09-03 (74d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LRCX | NASDAQ | 225.92 | -3.36 | -4.82 | — | 1.0x | 233.78 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-10-21 (26d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BELFA | NASDAQ | 176.88 | -3.98 | -4.75 | — | 1.2x | 184.22 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-10-28 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SECZ | NYSE | 8.08 | -3.69 | -4.70 | — | 0.8x | 8.39 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-09 (7d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-09 (Nasdaq earnings calendar; no headline lookup) |
| RMBS | NASDAQ | 82.23 | -3.22 | -4.66 | — | 1.1x | 84.97 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-10-26 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BELFB | NASDAQ | 225.49 | -3.43 | -4.65 | — | 1.2x | 233.49 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-10-28 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| DIOD | NASDAQ | 87.25 | -4.75 | -4.64 | — | 0.9x | 91.60 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-05 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AEIS | NASDAQ | 219.68 | -3.98 | -4.63 | — | 0.9x | 228.78 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-02 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ALM | NASDAQ | 8.22 | 7.73 | -4.62 | — | 1.2x | 7.63 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-12 (4d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-12 (Nasdaq earnings calendar; no headline lookup), consensus EPS $0.07 |
| CAMT | NASDAQ | 101.73 | -3.50 | -4.53 | — | 1.0x | 105.42 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-04 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| DELL | NYSE | 344.53 | -7.18 | -4.51 | — | 0.8x | 371.17 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-09-01 (76d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ALGM | NASDAQ | 30.13 | -4.98 | -4.50 | — | 0.9x | 31.71 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-10-29 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GLW | NYSE | 114.08 | -4.54 | -4.45 | — | 1.1x | 119.50 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-10-27 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| EPC | NYSE | 27.28 | -5.08 | 4.44 | — | 1.7x | 28.74 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-12 (4d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-12 (Nasdaq earnings calendar; no headline lookup), consensus EPS $0.78 |
| TEM | NASDAQ | 71.6 | -5.65 | -4.37 | — | 0.9x | 75.89 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-02 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PWR | NYSE | 602.01 | -0.68 | -4.32 | — | 1.0x | 606.16 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-10-29 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FLYW | NASDAQ | 22.26 | 3.68 | -4.31 | — | 1.8x | 21.47 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-03 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CBRS | NASDAQ | 108.72 | 11.22 | -4.25 | — | 0.7x | 97.75 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-12 (4d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-12 (Nasdaq earnings calendar; no headline lookup), consensus EPS ($0.13) |
| LASR | NASDAQ | 41.25 | -4.20 | -4.24 | — | 0.8x | 43.06 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-05 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| STRL | NASDAQ | 292.39 | -3.05 | -4.24 | — | 0.7x | 301.60 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-10-28 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMSC | NASDAQ | 24.13 | -3.63 | -4.23 | — | 1.2x | 25.04 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-04 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| KKR | NYSE | 98.05 | 0.87 | -4.13 | — | 1.9x | 97.20 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-09 (7d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-09 (Nasdaq earnings calendar; no headline lookup), consensus EPS $1.41 |
| ACAD | NASDAQ | 18.75 | 3.36 | -4.01 | — | 1.3x | 18.14 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-04 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FLEX | NASDAQ | 74.98 | -4.02 | -4.00 | — | 0.7x | 78.12 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-10-28 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| VECO | NASDAQ | 39.06 | -3.15 | -3.99 | — | 1.0x | 40.33 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-04 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| OUST | NASDAQ | 33.48 | -8.52 | -3.97 | — | 0.7x | 36.60 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-03 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ANET | NYSE | 197.29 | -4.52 | -3.90 | — | 0.9x | 206.63 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-03 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ASTS | NASDAQ | 32.6 | -5.51 | -3.90 | — | 0.7x | 34.50 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-09 (7d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-09 (Nasdaq earnings calendar; no headline lookup), consensus EPS ($0.41) |
| LSCC | NASDAQ | 112.35 | -5.47 | -3.85 | — | 0.8x | 118.85 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-02 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GEV | NYSE | 803.13 | -1.88 | -3.74 | — | 1.0x | 818.49 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-10-28 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| INIO | NASDAQ | 14.57 | -3.89 | -3.71 | — | 0.6x | 15.16 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-10-27 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| Q | NYSE | 118.36 | -3.53 | -3.68 | — | 1.1x | 122.69 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-04 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TSEM | NASDAQ | 146.89 | -6.95 | -3.54 | — | 0.6x | 157.86 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-02 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RDW | NYSE | 7.73 | -3.74 | -3.49 | — | 0.6x | 8.03 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-04 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AVGO | NASDAQ | 347.01 | -4.76 | -3.49 | — | 1.0x | 364.36 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-09-02 (75d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MP | NYSE | 38.76 | 3.50 | -3.48 | — | 1.1x | 37.45 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-05 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CRSR | NASDAQ | 11.78 | -4.07 | -3.48 | — | 1.1x | 12.28 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-05 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ORCL | NYSE | 125.35 | -1.38 | -3.45 | — | 0.9x | 127.11 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-09-10 (67d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| VSAT | NASDAQ | 67.72 | -4.94 | -3.43 | — | 0.6x | 71.24 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-05 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CDLR | NYSE | 6.65 | -4.04 | -3.31 | — | 0.4x | 6.93 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-08-25 (83d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MPWR | NASDAQ | 1390.54 | -3.93 | -3.27 | — | 0.7x | 1447.40 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-10-29 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| DOCN | NYSE | 86.32 | -4.16 | -3.27 | — | 0.6x | 90.07 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-03 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ETN | NYSE | 352.97 | -1.69 | -3.25 | — | 0.9x | 359.04 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-03 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RGTI | NASDAQ | 9.62 | -6.87 | -3.22 | — | 0.6x | 10.33 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-10 (6d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-10 (Nasdaq earnings calendar; no headline lookup), consensus EPS ($0.08) |
| ALNT | NASDAQ | 77.68 | -7.96 | -3.19 | — | 0.7x | 84.40 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-04 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| IONQ | NYSE | 28.88 | -6.42 | -3.15 | — | 0.6x | 30.86 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-05 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| APH | NYSE | 78.23 | -1.75 | -3.14 | — | 1.0x | 79.62 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-10-28 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FSLY | NASDAQ | 16.62 | -3.32 | -3.13 | — | 0.6x | 17.19 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-04 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| QNT | NASDAQ | 35.4 | -5.50 | -3.08 | — | 0.5x | 37.46 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-05 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PI | NASDAQ | 168.54 | -3.87 | -2.98 | — | 1.0x | 175.32 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-10-28 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RKLB | NASDAQ | 61.53 | -3.96 | -2.94 | — | 0.5x | 64.07 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-09 (7d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-09 (Nasdaq earnings calendar; no headline lookup), consensus EPS ($0.06) |
| AMPX | NYSE | 7.93 | -5.03 | -2.90 | — | 0.5x | 8.35 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-10 (6d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-10 (Nasdaq earnings calendar; no headline lookup), consensus EPS ($0.01) |
| NVDA | NASDAQ | 162.85 | -2.01 | -2.87 | — | 1.0x | 166.19 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-08-26 (82d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| QUBT | NASDAQ | 5.56 | -4.47 | -2.85 | — | 0.6x | 5.82 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-09 (7d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-09 (Nasdaq earnings calendar; no headline lookup), consensus EPS ($0.08) |
| VERA | NASDAQ | 28.1 | -3.24 | -2.81 | — | 0.9x | 29.04 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-05 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FCX | NYSE | 59.24 | -2.00 | -2.80 | — | 1.1x | 60.45 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-10-27 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ACCV | NASDAQ | 12.92 | 5.81 | -2.79 | — | 0.4x | 12.21 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-12 (4d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-12 (Nasdaq earnings calendar; no headline lookup), consensus EPS $0.09 |
| POWI | NASDAQ | 44.18 | -4.08 | -2.78 | — | 0.7x | 46.06 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-04 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AADX | NYSE | 8.38 | -3.34 | -2.74 | — | 0.5x | 8.67 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-11 (5d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-11 (Nasdaq earnings calendar; no headline lookup), consensus EPS $0.09 |
| NET | NYSE | 305.81 | -3.98 | -2.72 | — | 0.6x | 318.50 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-05 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BFLY | NYSE | 6.08 | -8.85 | -2.63 | — | 0.5x | 6.67 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-10-29 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| IBKR | NASDAQ | 81.79 | 0.57 | -2.56 | — | 0.9x | 81.33 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-10-15 (32d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NMAX | NYSE | 9.58 | 31.41 | -2.51 | — | 0.6x | 7.29 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-12 (4d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-12 (Nasdaq earnings calendar; no headline lookup), consensus EPS ($0.02) |
| ABSI | NASDAQ | 8.45 | -7.50 | -2.49 | — | 0.3x | 9.13 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-12 (4d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-12 (Nasdaq earnings calendar; no headline lookup), consensus EPS ($0.14) |
| CAT | NYSE | 600.2 | -0.84 | -2.45 | — | 0.8x | 605.28 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-10-29 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| JOBY | NYSE | 5.08 | -4.87 | -2.36 | — | 0.7x | 5.34 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-04 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CECO | AMEX | 54.25 | -3.12 | -2.30 | — | 0.4x | 56.00 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-09 (7d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| IOND | NASDAQ | 59.84 | -7.40 | -2.22 | — | 0.4x | 64.62 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-04 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| HYMC | NASDAQ | 15.9 | -6.47 | -2.20 | — | 0.4x | 17.00 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-10-27 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CB | NYSE | 375.74 | 1.07 | 2.20 | — | 2.1x | 371.76 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-10-20 (27d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SNOW | NYSE | 291 | -2.58 | -2.18 | — | 0.8x | 298.70 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-09-02 (75d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ADI | NASDAQ | 397.97 | -2.77 | -2.16 | — | 0.7x | 409.29 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-08-19 (89d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BULL | NASDAQ | 5.18 | 4.44 | -2.12 | — | 0.8x | 4.96 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-08-19 (89d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MOD | NYSE | 135.66 | 27.86 | -2.11 | — | 0.3x | 106.10 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-03 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| DAVE | NASDAQ | 277.04 | 3.62 | -2.09 | — | 0.5x | 267.37 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-11-04 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CLF | NYSE | 12.65 | -3.21 | -2.06 | — | 0.5x | 13.07 | yahoo_chart_daily | 2026-11-12 | US-listed | 2026-10-19 (28d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |

## US — QUIET one-liners

| Ticker | Venue | Chg % | Pre-mkt % | Post-mkt % | Move vs avg daily | Ref close | Ref source | Ref asof | US tradeable | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|
| CENX | NASDAQ | -4.17 | -1.91 | — | 1.1x | 35.51 | yahoo_chart_daily | 2026-11-12 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| SCCO | NYSE | -2.46 | -1.87 | — | 0.9x | 168.21 | yahoo_chart_daily | 2026-11-12 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| CDNS | NASDAQ | -3.09 | -1.86 | — | 1.2x | 333.32 | yahoo_chart_daily | 2026-11-12 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| SVM | AMEX | -3.24 | -1.85 | — | 0.8x | 8.95 | yahoo_chart_daily | 2026-11-12 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| GENB | NASDAQ | -3.98 | 1.82 | — | 0.8x | 12.57 | yahoo_chart_daily | 2026-11-12 | US-listed | — | Q3 2026 results, report date 2026-11-12 (Nasdaq earnings calendar; no headline lookup), consensus EPS ($0.50) |
| QCOM | NASDAQ | -2.64 | -1.80 | — | 0.9x | 177.14 | yahoo_chart_daily | 2026-11-12 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| LFTO | NASDAQ | 30.63 | -1.80 | — | 6.3x | 18.71 | yahoo_chart_daily | 2026-11-12 | US-listed | — | Q3 2026 results, report date 2026-11-12 (Nasdaq earnings calendar; no headline lookup), consensus EPS $0.17 |
| SDGR | NASDAQ | -4.28 | -1.79 | — | 0.9x | 30.85 | yahoo_chart_daily | 2026-11-12 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| ENS | NYSE | -3.25 | -1.79 | — | 1.1x | 147.80 | yahoo_chart_daily | 2026-11-12 | US-listed | — | Q3 2026 results, report date 2026-11-11 (Nasdaq earnings calendar; no headline lookup), consensus EPS $3.19 |
| TXN | NASDAQ | -2.84 | -1.79 | — | 1.1x | 312.48 | yahoo_chart_daily | 2026-11-12 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| CRWD | NASDAQ | -1.42 | -1.73 | — | 0.5x | 229.87 | yahoo_chart_daily | 2026-11-12 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| ATI | NYSE | -3.72 | -1.69 | — | 1.0x | 190.16 | yahoo_chart_daily | 2026-11-12 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| APP | NASDAQ | 3.92 | 1.69 | — | 0.8x | 393.68 | yahoo_chart_daily | 2026-11-12 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| STDN | NYSE | -4.35 | -1.61 | — | 1.3x | 11.03 | yahoo_chart_daily | 2026-11-12 | US-listed | — | Q3 2026 results, report date 2026-11-12 (Nasdaq earnings calendar; no headline lookup), consensus EPS ($0.13) |
| HLF | NYSE | 4.93 | 1.59 | — | 2.1x | 15.21 | yahoo_chart_daily | 2026-11-12 | US-listed | — | no catalyst lookup (outside the per-run budget) |

## EU/UK — Headline table

| Ticker | Market | Venue | Close | Chg % | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | Session asof | Settle | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PLT | norway | OSL | 12.7 | +15.25 | NOK | 4.9x | 11.02 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | live | none | 2026-11-16 (0d ago) | — | no catalyst lookup (outside the per-run budget) |
| N91 | uk | LSE | 185.8552 | -8.81 | GBX | 9.3x | 203.80 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | live | none | 2026-11-16 (0d ago) | — | no catalyst lookup (outside the per-run budget) |
| HNSA | sweden | OMXSTO | 50.95 | +8.77 | SEK | 2.8x | 46.84 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | live | none | 2026-11-11 (5d ago) | — | no catalyst lookup (outside the per-run budget) |
| CTEK | sweden | OMXSTO | 15.98 | +8.71 | SEK | 3.5x | 14.70 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | live | none | 2026-10-29 (18d ago) | — | no catalyst lookup (outside the per-run budget) |
| SMCRT | sweden | OMXSTO | 19.36 | +6.61 | SEK | 2.6x | 18.16 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | live | none | 2026-11-06 (10d ago) | — | no catalyst lookup (outside the per-run budget) |
| S92 | germany | XETR | 48.18 | +6.45 | EUR | 1.6x | 45.26 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | live | none | 2026-11-12 (4d ago) | — | no catalyst lookup (outside the per-run budget) |
| GOMX | sweden | OMXSTO | 14.92 | +6.12 | SEK | 1.6x | 14.06 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | live | none | 2026-08-26 (82d ago) | — | no catalyst lookup (outside the per-run budget) |
| VU | france | EURONEXT | 158.9 | +5.93 | EUR | 2.6x | 150.00 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | live | none | 2026-09-21 (56d ago) | — | no catalyst lookup (outside the per-run budget) |
| GENO | norway | OSL | 16.7 | +5.43 | NOK | 1.4x | 15.84 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | live | none | 2026-11-12 (4d ago) | — | no catalyst lookup (outside the per-run budget) |
| BC8 | germany | XETR | 32.22 | -4.84 | EUR | 2.8x | 33.86 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | live | none | 2026-11-13 (3d ago) | — | no catalyst lookup (outside the per-run budget) |
| SLR | spain | BME | 14.99 | -4.83 | EUR | 1.6x | 15.75 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | live | none | 2026-09-24 (53d ago) | — | Q3/9M 2026 results due 2026-11-16 (vendor calendars; some list 17 Nov; consensus revenue EUR 129.9M) - no release confirmed at scan time; Spanish renewables sold off Friday (Acciona -7.98%, Acciona ER -7.17%, Solaria -3.52%); Capital Markets Day 17-18 Nov |
| GPW | poland | GPW | 103.7 | +4.75 | PLN | 2.8x | 99.00 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | live | none | 2026-11-16 (0d ago) | Y | Q3 2026 results (reported 2026-11-16): net profit PLN 70.3M, +44% y/y and 11% above consensus; revenue PLN 158.5M +17%, EBITDA PLN 71.1M +32% |
| MOL | italy | MIL | 34.775 | -4.73 | EUR | 2.4x | 36.50 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | live | none | 2026-11-12 (4d ago) | — | no catalyst lookup (outside the per-run budget) |
| ACT0 | germany | XETR | 145.6 | +4.60 | EUR | 1.5x | 139.20 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | live | none | 2026-10-28 (19d ago) | — | no catalyst lookup (outside the per-run budget) |
| EXENS | france | EURONEXT | 53.2 | +4.52 | EUR | 2.2x | 50.90 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | live | none | 2026-07-28 (111d ago) | — | no catalyst lookup (outside the per-run budget) |
| CMB | italy | MIL | 76.9 | -4.23 | EUR | 2.1x | 80.30 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | live | US line (NYSE:CMBT) | 2026-11-12 (4d ago) | — | no catalyst lookup (outside the per-run budget) |
| ATT | poland | GPW | 15.6 | -4.18 | PLN | 2.2x | 16.28 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | live | none | 2026-09-10 (67d ago) | N | DM BOS cut the recommendation to sell and the target price from PLN 24 to PLN 13 (gas-cost squeeze; 2026-27 EBITDA forecasts cut by ~PLN 1.4bn); Q3 consolidated report due 19 Nov 2026 |
| BEWI | norway | OSL | 19.96 | +3.96 | NOK | 1.8x | 19.20 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | live | none | 2026-11-04 (12d ago) | — | no catalyst lookup (outside the per-run budget) |
| GRE | spain | BME | 65.2 | -3.83 | EUR | 1.2x | 67.80 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | live | none | 2026-09-16 (61d ago) | — | pending catalyst lookup |
| ADEN | switzerland | SIX | 25.16 | -3.75 | CHF | 1.6x | 26.14 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | live | none | 2026-11-12 (4d ago) | — | no catalyst lookup (outside the per-run budget) |
| MAIRE | italy | MIL | 14.02 | +3.55 | EUR | 2.3x | 13.54 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | live | none | 2026-10-27 (20d ago) | — | no catalyst lookup (outside the per-run budget) |
| ATS | austria | VIE | 119.2 | -3.40 | EUR | 0.6x | 123.40 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | live | none | 2026-11-05 (11d ago) | — | pending catalyst lookup |
| CFR | switzerland | SIX | 175.2 | +3.39 | CHF | 2.5x | 169.45 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | live | none | 2026-11-13 (3d ago) | — | no catalyst lookup (outside the per-run budget) |
| ACE | italy | MIL | 20.6 | -3.29 | EUR | 3.8x | 21.30 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | live | none | 2026-11-13 (3d ago) | — | no catalyst lookup (outside the per-run budget) |
| POST | austria | VIE | 33.15 | +3.27 | EUR | 6.0x | 32.10 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | live | US line (OTC:SPSTF) | 2026-11-12 (4d ago) | — | no catalyst lookup (outside the per-run budget) |
| GMAB | denmark | OMXCOP | 3560 | +3.25 | DKK | 0.8x | 3448.00 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | live | none | 2026-11-05 (11d ago) | — | no catalyst lookup (outside the per-run budget) |
| NOVO_B | denmark | OMXCOP | 287.4 | +3.21 | DKK | 2.2x | 278.45 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | live | ADR (NYSE:NVO) | 2026-11-04 (12d ago) | — | no catalyst lookup (outside the per-run budget) |
| WISE | uk | LSE | 866 | -3.18 | GBX | 2.3x | 894.40 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | live | US line (NASDAQ:WSE) | 2026-11-12 (4d ago) | — | no catalyst lookup (outside the per-run budget) |
| CBF | poland | GPW | 198.5 | +3.17 | PLN | 3.9x | 192.40 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | live | none | 2026-09-02 (75d ago) | — | pending catalyst lookup |

## AU (ASX) — Headline table

| Ticker | Venue | Close | Chg % | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | Session asof | Settle | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ELD | ASX | 7.03 | +7.49 | AUD | 5.6x | 6.54 | yahoo_chart_daily | 2026-11-12 | 2026-11-16 | settled | none | 2026-11-16 (0d ago) | Y | FY26 results (reported 2026-11-16): underlying EBIT $187.7M +43% y/y, statutory NPAT $144.2M +187%, underlying EPS 47.3c, final dividend 18.0c 100% franked |
| CNI | ASX | 1.235 | +6.47 | AUD | 4.4x | 1.16 | yahoo_chart_daily | 2026-11-12 | 2026-11-16 | settled | none | 2026-08-26 (82d ago) | N | no fresh catalyst found - no earnings event in the window (FY26 results were 2026-08-27); the latest ASX filing is a MUFG change in substantial holding (16 Nov 06:45 AEDT) |
| NHC | ASX | 4.92 | -5.93 | AUD | 3.0x | 5.23 | yahoo_chart_daily | 2026-11-12 | 2026-11-16 | settled | none | 2026-09-14 (63d ago) | — | no catalyst lookup (outside the per-run budget) |
| DVP | ASX | 3.33 | -5.40 | AUD | 1.3x | 3.52 | yahoo_chart_daily | 2026-11-12 | 2026-11-16 | settled | none | 2026-03-08 (253d ago) | — | no catalyst lookup (outside the per-run budget) |

## APAC/Gulf — Headline table

| Ticker | Market | Venue | Close | Chg % | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | Session asof | Settle | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AREA | indonesia | IDX | 199 | +34.46 | IDR | 6.0x | 148.00 | yahoo_chart_daily | 2026-11-12 | 2026-11-15 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| TRIN | indonesia | IDX | 133 | +34.34 | IDR | 4.2x | 99.00 | yahoo_chart_daily | 2026-11-12 | 2026-11-15 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| NAT | thailand | SET | 2.24 | -25.33 | THB | 7.0x | 3.00 | yahoo_chart_daily | 2026-11-12 | 2026-11-15 | settled | none | 2024-11-12 (734d ago) | N | no fresh catalyst found - no SET filing for NAT between 13 and 16 Nov 2026; the -25% session came with a Thai tech sell-off and a below-expectation 3Q26 GDP print |
| STARDELTA | india | BSE | 427 | -20.04 | INR | 4.7x | 532.15 | yahoo_chart_daily | 2026-11-12 | 2026-11-15 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| 300530 | china | SZSE | 27.83 | +20.01 | CNY | 4.3x | 23.19 | yahoo_chart_daily | 2026-11-12 | 2026-11-15 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| KPGEL | india | BSE | 224.4 | -20.00 | INR | 4.4x | 280.50 | yahoo_chart_daily | 2026-11-12 | 2026-11-15 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| 300779 | china | SZSE | 31.32 | -20.00 | CNY | 4.1x | 39.15 | yahoo_chart_daily | 2026-11-12 | 2026-11-15 | settled | none | 2025-10-28 (384d ago) | — | no catalyst lookup (outside the per-run budget) |
| 300824 | china | SZSE | 8.6 | +19.94 | CNY | 6.7x | 7.17 | yahoo_chart_daily | 2026-11-12 | 2026-11-15 | settled | none | 2026-10-23 (24d ago) | — | no catalyst lookup (outside the per-run budget) |
| NOBLE | thailand | SET | 1.1 | -18.52 | THB | 10.3x | 1.35 | yahoo_chart_daily | 2026-11-12 | 2026-11-15 | settled | US line (OTC:NBHEF) | 2023-02-22 (1363d ago) | N | Board approved a THB 800-900M rights offering (1 new share per 2.29 held at an indicative THB 1.35-1.65; EGM in December); Q3 2026 real-estate revenue THB 2,331M +45% y/y with a THB 483M net loss and presales THB 3,906M +391% |
| PLAT | thailand | SET | 1.54 | +15.79 | THB | 9.2x | 1.33 | yahoo_chart_daily | 2026-11-12 | 2026-11-15 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| S63 | singapore | SGX | 9.03 | -6.62 | SGD | 4.8x | 9.67 | yahoo_chart_daily | 2026-11-12 | 2026-11-15 | settled | none | 2026-08-12 (96d ago) | — | no catalyst lookup (outside the per-run budget) |
| AWX | singapore | SGX | 6.67 | -6.06 | SGD | 1.1x | 7.10 | yahoo_chart_daily | 2026-11-12 | 2026-11-15 | settled | none | 2026-08-12 (96d ago) | — | no catalyst lookup (outside the per-run budget) |
| MIM | singapore | SGX | 1.24 | -4.62 | SGD | 0.6x | 1.30 | yahoo_chart_daily | 2026-11-12 | 2026-11-15 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| THL | newzealand | NZX | 2.82 | -3.75 | NZD | 4.2x | 2.93 | yahoo_chart_daily | 2026-11-12 | 2026-11-15 | settled | none | 2026-08-24 (84d ago) | — | no catalyst lookup (outside the per-run budget) |
| SPK | newzealand | NZX | 2.2 | +2.80 | NZD | 2.3x | 2.14 | yahoo_chart_daily | 2026-11-12 | 2026-11-15 | settled | none | 2026-08-19 (89d ago) | N | November shareholder update (9 Nov) and UBS Australasia conference presentation (10 Nov) - FY27 guidance unchanged, no earnings event until the Feb 2027 half-year |
| HGH | newzealand | NZX | 1.295 | +2.78 | NZD | 3.7x | 1.26 | yahoo_chart_daily | 2026-11-12 | 2026-11-15 | settled | none | 2026-02-25 (264d ago) | — | no catalyst lookup (outside the per-run budget) |

## Source health

- scanner_calls: 57 | scanner_errors: 0
- markets_scanned: US + 17 EU/UK + ASX + 7 APAC/Gulf (india, thailand, indonesia, china, singapore, newzealand, ksa)
- pipeline_version: 2026-11-15.4
- et_clock: zoneinfo America/New_York (DST-aware; a fixed UTC-4 mislabels every winter fire)
- premarket_window: 04:00-09:30 ET, resolved with zoneinfo (09:00-14:30 UTC in winter, 08:00-13:30 UTC in summer)
- session_selection: by DATE and order, never by a modal time-of-day. Yahoo stamps a daily bar at the session open, so the ET stamp of the SAME session shifts by one hour across a DST boundary; a modal filter kept the OLDER bars and discarded the NEWEST ones, which rolled the base back to the prior-prior session (66 US + 21 ASX rows lost on 2026-11-03, 24 of 25 ASX rows lost on 2026-11-04).
- yahoo_calls: 248 | yahoo_429: 0 | yahoo_errors: 0 | yahoo_breaker: closed
- reference_close (screener vs Yahoo, resolved BEFORE the tables were built): agree=229 mismatch=9 unverified=0 stale_reference=9
  method: the screener's implied reference close (close / (1 + change/100)) is compared
  with Yahoo's own reference close. A match proves the move was measured against the
  TRUE prior close; a mismatch means the row sits on a STALE reference (phantom move).
  Coverage: every row of the US headline, US QUIET, EU/UK and ASX tables is checked.
  Yahoo bar mode: {"closed": 200, "live": 29} (closed = last completed session bar;
  live = in-progress EU/UK session bar, which is what a weekday 08:00 ET EU move needs)
  live drift between the screener snapshot and the later Yahoo print: median=0.00pp max=1.98pp (expected on a live market)
- cross_check mismatches: [{"region": "US", "symbol": "IEP", "tv": -10.549, "yahoo": -2.469, "delta": -8.08, "ref_delta_pct": -2.469, "tv_implied_ref": 4.74, "yahoo_ref": 4.86, "yahoo_date": "2026-11-13", "yahoo_ref_date": "2026-11-12", "verdict": "stale_reference"}, {"region": "US", "symbol": "KLAC", "tv": -0.151, "yahoo": -3.166, "delta": 3.015, "ref_delta_pct": -3.166, "tv_implied_ref": 152.32, "yahoo_ref": 157.3, "yahoo_date": "2026-11-13", "yahoo_ref_date": "2026-11-12", "verdict": "stale_reference"}, {"region": "US", "symbol": "CEG", "tv": -0.152, "yahoo": -0.779, "delta": 0.627, "ref_delta_pct": -0.779, "tv_implied_ref": 280.2, "yahoo_ref": 282.4, "yahoo_date": "2026-11-13", "yahoo_ref_date": "2026-11-12", "verdict": "stale_reference"}, {"region": "germany", "symbol": "AIXA.DE", "tv": -3.716, "yahoo": -1.991, "delta": -1.725, "ref_delta_pct": 1.307, "tv_implied_ref": 32.56, "yahoo_ref": 32.14, "yahoo_date": "2026-11-16", "yahoo_ref_date": "2026-11-13", "verdict": "stale_reference"}, {"region": "indonesia", "symbol": "MKNT.JK", "tv": 33.333, "yahoo": 0.0, "delta": 33.333, "ref_delta_pct": -25.0, "tv_implied_ref": 24.0, "yahoo_ref": 32.0, "yahoo_date": "2026-11-12", "yahoo_ref_date": "2026-11-11", "verdict": "stale_reference"}, {"region": "india", "symbol": "YATRA.BO", "tv": 20.801, "yahoo": 19.997, "delta": 0.804, "ref_delta_pct": -0.665, "tv_implied_ref": 77.64, "yahoo_ref": 78.16, "yahoo_date": "2026-11-15", "yahoo_ref_date": "2026-11-12", "verdict": "stale_reference"}, {"region": "ksa", "symbol": "1301.SR", "tv": -9.616, "yahoo": -6.21, "delta": -3.406, "ref_delta_pct": 3.769, "tv_implied_ref": 19.55, "yahoo_ref": 18.84, "yahoo_date": "2026-11-16", "yahoo_ref_date": "2026-11-12", "verdict": "stale_reference"}, {"region": "ksa", "symbol": "8200.SR", "tv": 8.627, "yahoo": 7.711, "delta": 0.916, "ref_delta_pct": -0.843, "tv_implied_ref": 24.69, "yahoo_ref": 24.9, "yahoo_date": "2026-11-16", "yahoo_ref_date": "2026-11-12", "verdict": "stale_reference"}, {"region": "ksa", "symbol": "4144.SR", "tv": 5.6, "yahoo": 16.103, "delta": -10.503, "ref_delta_pct": 9.946, "tv_implied_ref": 81.25, "yahoo_ref": 73.9, "yahoo_date": "2026-11-16", "yahoo_ref_date": "2026-11-12", "verdict": "stale_reference"}]
- rows_dropped_stale_ref: 9 (rows whose screener-implied reference close disagreed with Yahoo's by more than 0.5%; they are dropped, not published)
- rows_dropped_unresolved_ref: 0 (rows whose reference close could not be resolved from Yahoo at all - the base of the move is unverifiable, so the row is dropped rather than published with a '—' base)
- us_premarket_check (Yahoo 1-min pre/post feed vs the screener pre-market column, base = the IMMEDIATELY prior session's close): checked=10 within_1pp=7 within_3pp=8 unavailable=0
  us_premarket outliers (>3pp; thin pre-market books, not a screener error): [{"symbol": "LXEO", "tv": 37.282, "yahoo": 22.997, "delta": 14.285, "yahoo_asof": "08:13"}, {"symbol": "TU", "tv": 26.964, "yahoo": 19.695, "delta": 7.269, "yahoo_asof": "08:13"}]
- markets_with_lt5_rows: ['uk:egreater=4', 'uk:less=3', 'france:egreater=2', 'france:less=2', 'netherlands:egreater=0', 'netherlands:less=1', 'belgium:egreater=0', 'belgium:less=0', 'portugal:egreater=0', 'portugal:less=0', 'ireland:egreater=0', 'ireland:less=0', 'italy:egreater=3', 'italy:less=4', 'switzerland:egreater=1', 'switzerland:less=1', 'spain:egreater=0', 'spain:less=2', 'norway:egreater=4', 'norway:less=2', 'denmark:egreater=3', 'denmark:less=0', 'finland:egreater=0', 'finland:less=0', 'poland:egreater=2', 'poland:less=2', 'austria:egreater=1', 'austria:less=1', 'greece:egreater=0', 'greece:less=1', 'singapore:egreater=0', 'newzealand:egreater=4', 'newzealand:less=1']
  NOTE: this fires per market AND direction, so it is NOT a coverage-failure signal on
  its own. A 'less' count of 0-3 means almost nothing fell more than 2.5% that session
  (a broad up-day); a small 'egreater' count usually means a small market with few
  names above the $1B market-cap floor. Check the median change before calling it a gap.
- filters: volume>10000 (removes stale-reference rows), country=home for EU/UK/AU,
  exchange drop-list for US, US venue allow-list, US preferred (slash ticker) excluded
- pass_b2 (US pre-market gap scan - "gapped today, flat yesterday"): candidates=73 deduped_against_pass_a_b=39 published=33 (up=5 down=68)
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
- bod_no_extended_hours: 81 (deferred to the next scan; not in the headline table)
- earnings_source: screener `earnings_release_date` (last FULL report) + `earnings_release_next_date` (next scheduled)
- earnings_caveat: `earnings_release_date` does NOT capture preliminary, guidance or
  restructuring releases. On 2026-10-23 LKQ fell 22.47% on a preliminary Q3 miss while
  the field still read 2026-07-30. ALWAYS confirm the earnings-driven flag against the
  headline itself; the calendar field is a screen, not a verdict.
- us_line_index: ok (US-listed lines for the 25 foreign home countries, both scanner types; the `US tradeable` column is ADR / US-listed / none)
- catalyst_note: Catalyst lookups: 7 US + 4 EU + 2 AU + 3 APAC/Gulf = 16 per run - the skill's cap, allocated by the evidence gap.
- catalyst_merge: region-matched - a row may only use a catalog entry from its OWN region;
  the same ticker on another venue is a different company and is not used.
- catalyst_budget: 5 US + 6 EU + 2 AU + 3 APAC/Gulf = 16 lookups per run (cap 16), allocated by the evidence gap: the US slice covers the rows whose earnings event can still explain today's move, the EU/AU/APAC floors are never squeezed because no bulk calendar reaches those markets, and whatever the US slice does not need goes to the region with the most unexplained rows
- earnings_calendar: Nasdaq public earnings calendar (calls=8 errors=0 symbols=1292) - the source of record for the US earnings date, and the ranking key for the search budget
- earnings_field_stale_rows: 1 (the screener's earnings_release_date disagreed with the calendar; the calendar's date is published)
- earnings_field_stale_detail: [{"ticker": "POET", "screener": "2026-08-13", "calendar": "2026-11-16"}]
- earnings_dates: the published `Last earnings` date by source - catalog (researched) 7, calendar 33, asx 1, screener 173. The chain is researched -> calendar (US) -> ASX feed (AU) -> the screener's field, which is the FALLBACK and the one that lags (2026-11-12: NBIS carried the previous quarter's date on the morning it reported, and MEKO, NORBT and FG carried July and August dates on the morning they all reported).
- asx_announcements: 6 results-classified announcement(s) for the last ASX session (calls=1 errors=0); the announcement date IS the report date, and the meeting/AGM/offer/assay headlines are excluded because they are not reports
- earnings_tiers: fresh=2 near=3 (fresh = the report is dated on the scan date, near = the previous session)
- one_table_rule: each name appears exactly once, in exactly one table, with its
  catalyst in that row's last column. There is no separate catalysts section.
- data_date: US regular session close of the prior trading day; extended-hours columns
  carry the prior session's prints
- settlement_state: 20 settled, 29 live (a live row's move is a mid-session snapshot, not the session's result)
- rows_per_market (EU/UK, cap 4/market): {'norway': 4, 'uk': 4, 'sweden': 4, 'germany': 4, 'france': 4, 'spain': 2, 'poland': 4, 'italy': 4, 'switzerland': 2, 'austria': 2, 'denmark': 3, 'greece': 1, 'netherlands': 1} — the cap stops one thin market taking the table; the EU/UK table was 28% Sweden over nine runs (73 of 264 rows) while Belgium and Greece never appeared once.
- rows_per_market (APAC/Gulf, cap 3/market): {'indonesia': 3, 'thailand': 3, 'india': 3, 'china': 3, 'ksa': 3, 'singapore': 3, 'newzealand': 3}
- deprecations: mcp__tradingview-advanced__*, mcp__tradingview__*, mcp__financekit__*,
  mcp__stocktwits__* are ABSENT in Cloud sessions (tool_search 0 hits; connector catalog
  holds only media + credential tools). The public screener replaces them.

- degraded_sources: 0
  (none - every source answered for every published row)

## Audit line

`earnings-reaction target=earnings-reactions:2026-11-16 candidates=492 amc_reactions=0 pre_gaps=165 eu_reactions=29 asx_reactions=4 apac_reactions=14 catalyst_lookups=16 bod=81 pass_b2_candidates=73 pass_b2_dedup=39 pass_b2_published=33 earnings_calendar_rows=1292 earnings_tiers_fresh=2 earnings_tiers_near=3 earnings_field_stale_rows=1 earnings_dates_catalog=7 earnings_dates_asx=1 asx_ann_rows=6 rows_dropped_stale_ref=9 rows_dropped_unresolved_ref=0 degraded_sources=0`
