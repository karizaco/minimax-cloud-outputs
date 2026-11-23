# Earnings reaction scanner — 2026-11-23

- Cron: `0 8 * * 1-5` America/New_York (weekdays, 08:00 ET)
- Fire time (ET): 2026-11-23 08:21:40 Mon
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

- 0 AMC reactions, 339 pre-market gaps, 36 without extended-hours data; 28 EU/UK and 3 ASX movers, 20 APAC/Gulf movers.
- Pass B2 (the US pre-market gap scan) met the filter on 169 names (163 up, 6 down); 82 were already a Pass A/B row and are recorded as dedupes, and 86 reached a table.
- Biggest US extended-hours move: CAPR PRE_GAP (74.57%).
- Biggest EU/UK move: VER (-16.83%, sweden).
- Biggest ASX move: ALQ (-12.23%).
- Biggest APAC/Gulf move: TRIN (+34.69%, indonesia).
- 0 of the 28 EU/UK rows are SETTLED and 28 are LIVE (mid-session). The 12:15 ET settlement pass publishes where those
  live moves actually closed.
- EU/AU/APAC earnings-driven tagging is keyword-based on headlines (best-effort). A row
  whose lookup was not performed carries NO verdict — only a researched row does.

## Actionable read

- **Move vs this name's own history.** The `Move vs avg daily` column divides the
  reaction by the name's own mean absolute daily move over its last
  20 completed sessions. A -27% move in a name that averages +-3% is a
  different event from a -8% move in a name that averages +-7%.
- **US-listed and tradeable vs foreign-only.** 354 published US rows are on a
  US venue; 3 more foreign reactions have a US ADR line
  (the `US tradeable` column carries the ticker); 25 are foreign-only and
  cannot be bought directly by a US reader.
- **Not yet fully priced — US (hypothesis, not a recommendation).**
  KYMR — +33.30%, 2.70% mean absolute daily move over the last 20 completed sessions, 12.3x that average, reference close 119.39 dated 2026-11-19, US access: US-listed, the move now (+33.30%) is larger than the move it follows (-3.42%); the reaction is still being repriced. Hypothesis only: this artifact states no
  direction and no trade.
- **Not yet fully priced — EU/UK (hypothesis, not a recommendation).**
  NWG — -11.14%, 1.53% mean absolute daily move over the last 20 completed sessions, 7.3x that average, reference close 88.00 dated 2026-11-20, US access: none, the move now (-11.14%) is larger than the move it follows (-4.35%); the reaction is still being repriced. Hypothesis only: this artifact states no
  direction and no trade.
- **Not yet fully priced — AU (ASX) (hypothesis, not a recommendation).**
  ALQ — -12.23%, 2.18% mean absolute daily move over the last 20 completed sessions, 5.6x that average, reference close 19.30 dated 2026-11-19, US access: none, the move now (-12.23%) is larger than the move it follows (-4.36%); the reaction is still being repriced. Hypothesis only: this artifact states no
  direction and no trade.

## US — Headline table

| Ticker | Venue | Close | Chg % | Pre-mkt % | Post-mkt % | Move vs avg daily | Ref close | Ref source | Ref asof | US tradeable | Last earnings | Tag | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CAPR | NASDAQ | 7.59 | 0.80 | -74.57 | — | 9.5x | 7.53 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-10 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| KYMR | NASDAQ | 115.31 | -3.42 | 33.30 | — | 12.3x | 119.39 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-29 (25d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| KNOP | NYSE | 7.32 | -8.39 | 23.22 | — | 8.7x | 7.99 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-09-03 (81d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ZS | NASDAQ | 194.82 | -5.29 | 19.98 | — | 7.3x | 205.71 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-12-02 | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| APLD | NASDAQ | 11.49 | -17.81 | 14.07 | — | 2.0x | 13.98 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-07 (47d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PLBL | NASDAQ | 9.74 | 3.62 | -12.36 | — | 2.7x | 9.40 | yahoo_chart_daily | 2026-11-19 | US-listed | — | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ASST | NASDAQ | 14.51 | -12.64 | 11.32 | — | 2.0x | 16.61 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-06 (17d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ABTC | NASDAQ | 3.5 | -8.85 | 10.00 | — | 1.7x | 3.84 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-04 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FWDI | NASDAQ | 3.28 | -16.75 | 9.76 | — | 1.8x | 3.94 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-08-12 (103d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| COHU | NASDAQ | 37.31 | -8.53 | 9.51 | — | 1.6x | 40.79 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-28 (26d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BMNR | NYSE | 12.98 | -13.87 | 9.40 | — | 2.0x | 15.07 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-10 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SBET | NASDAQ | 4.48 | -9.13 | 9.37 | — | 2.2x | 4.93 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-09 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GLXY | NASDAQ | 11.22 | -8.93 | 9.27 | — | 1.2x | 12.32 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-27 (27d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SMTC | NASDAQ | 87.63 | -13.93 | 9.04 | — | 1.3x | 101.81 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-23 (0d ago) | PRE_GAP | Y | Q3 FY2027 results due after today's close (2026-11-23); consensus adj EPS $1.13 on ~$417m revenue, data-centre revenue and 800G demand the focus |
| ICHR | NASDAQ | 27.28 | -15.15 | 8.72 | — | 1.4x | 32.15 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-02 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AYA | NASDAQ | 17.38 | -8.04 | 8.63 | — | 1.8x | 18.90 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-12 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BTDR | NASDAQ | 2.955 | -13.34 | 8.63 | — | 0.9x | 3.41 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-10 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NBIS | NASDAQ | 81.31 | -16.11 | 8.46 | — | 0.9x | 96.92 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-12 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FLY | NASDAQ | 17.69 | -9.37 | 8.20 | — | 1.0x | 19.52 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-10 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FORM | NASDAQ | 73.02 | -10.83 | 8.19 | — | 1.2x | 81.89 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-28 (26d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NUAI | NASDAQ | 3.78 | -11.68 | 8.18 | — | 0.6x | 4.28 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-12 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SHAZ | NASDAQ | 16.83 | -18.06 | 8.14 | — | 0.8x | 20.54 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-16 (7d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-16 (Nasdaq earnings calendar; no headline lookup), consensus EPS ($1.47) |
| AXTI | NASDAQ | 30.57 | -12.26 | 8.08 | — | 0.9x | 34.84 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-29 (25d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| UAMY | NYSE | 2.23 | -6.30 | 8.07 | — | 1.1x | 2.38 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-12 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NVTS | NASDAQ | 6.08 | -15.20 | 8.06 | — | 1.1x | 7.17 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-03 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NVDA | NASDAQ | 125.53 | -14.01 | 8.03 | — | 2.2x | 145.98 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-17 (6d ago) | PRE_GAP | — | Q4 2026 results, report date 2026-11-17 (Nasdaq earnings calendar; no headline lookup), consensus EPS $2.47 |
| PURR | NASDAQ | 7.48 | -10.95 | 8.02 | — | 1.4x | 8.40 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-05 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BORR | NYSE | 3.41 | 4.28 | 7.92 | — | 2.1x | 3.27 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-18 (5d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-18 (Nasdaq earnings calendar; no headline lookup), consensus EPS ($0.11) |
| ACMR | NASDAQ | 39.8 | -12.53 | 7.91 | — | 1.4x | 45.50 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-05 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AEHR | NASDAQ | 39.84 | -16.90 | 7.91 | — | 0.9x | 47.94 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-02 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MSTR | NASDAQ | 77.8 | -9.67 | 7.90 | — | 1.8x | 86.13 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-29 (25d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PENG | NASDAQ | 36.05 | -15.20 | 7.88 | — | 1.0x | 42.51 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-06 (48d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| IREN | NASDAQ | 11.82 | -17.97 | 7.87 | — | 0.9x | 14.41 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-05 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AVR | NASDAQ | 4.99 | -1.96 | 7.82 | — | 1.7x | 5.09 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-10 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FLNC | NASDAQ | 3.46 | -9.66 | 7.80 | — | 1.3x | 3.83 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-23 (0d ago) | PRE_GAP | Y | FY2026 Q4 results due after today's close (2026-11-23); consensus EPS -$0.26 on ~$903m revenue after August's guidance cut |
| RKLB | NASDAQ | 45.42 | -10.92 | 7.79 | — | 1.3x | 50.99 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-09 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SITM | NASDAQ | 361.24 | -10.83 | 7.76 | — | 1.3x | 405.10 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-04 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| VSH | NYSE | 22.36 | -10.74 | 7.74 | — | 1.4x | 25.05 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-04 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| EROC | NYSE | 6.12 | -15.59 | 7.68 | — | 1.0x | 7.25 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-12 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AAOI | NASDAQ | 32.93 | -16.55 | 7.65 | — | 0.9x | 39.46 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-05 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CIFR | NASDAQ | 5.435 | -16.13 | 7.64 | — | 0.9x | 6.48 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-02 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CRDO | NASDAQ | 99.86 | -15.20 | 7.62 | — | 1.1x | 117.76 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-09-01 (83d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| POET | NASDAQ | 3.42 | -15.97 | 7.60 | — | 1.1x | 4.07 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-16 (7d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-16 (Nasdaq earnings calendar; no headline lookup), consensus EPS ($0.07) |
| RDW | NYSE | 5.65 | -13.21 | 7.60 | — | 1.1x | 6.51 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-04 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ABSI | NASDAQ | 7.51 | -7.97 | 7.59 | — | 1.1x | 8.16 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-12 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| UMAC | AMEX | 8.64 | -14.88 | 7.58 | — | 1.0x | 10.15 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-05 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| DELL | NYSE | 278.02 | -11.04 | 7.55 | — | 1.3x | 312.54 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-09-01 (83d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| UEC | AMEX | 5.3 | -7.99 | 7.52 | — | 1.6x | 5.76 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-09-29 (55d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SANM | NASDAQ | 139.76 | -9.69 | 7.48 | — | 1.6x | 154.75 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-09 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LUNR | NASDAQ | 8.775 | -10.28 | 7.46 | — | 1.0x | 9.78 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-12 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| UUUU | AMEX | 4.96 | -9.49 | 7.46 | — | 1.6x | 5.48 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-04 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MRAM | NASDAQ | 9 | -16.36 | 7.44 | — | 1.2x | 10.76 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-28 (26d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ASTS | NASDAQ | 23.27 | -8.92 | 7.43 | — | 1.1x | 25.55 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-09 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MXL | NASDAQ | 41.45 | -13.88 | 7.43 | — | 1.0x | 48.13 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-22 (32d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| VOYG | NYSE | 18.74 | -14.90 | 7.42 | — | 1.1x | 22.02 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-02 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| WYFI | NASDAQ | 6.35 | -16.99 | 7.40 | — | 0.8x | 7.65 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-10 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RUM | NASDAQ | 4.19 | -8.71 | 7.40 | — | 1.5x | 4.59 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-11 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ALAB | NASDAQ | 180.35 | -14.77 | 7.39 | — | 1.1x | 211.60 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-03 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MARA | NASDAQ | 5.085 | -18.57 | 7.37 | — | 1.2x | 6.25 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-09 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AVEX | NYSE | 11.04 | -14.15 | 7.34 | — | 1.0x | 12.86 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-11 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BRUN | NASDAQ | 3.56 | -14.73 | 7.30 | — | 0.7x | 4.17 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-12 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CRWV | NASDAQ | 39.51 | -12.02 | 7.25 | — | 1.0x | 44.91 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-10 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| STDN | NYSE | 8.14 | -9.66 | 7.25 | — | 1.7x | 9.01 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-12 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| UCTT | NASDAQ | 37 | -12.96 | 7.19 | — | 1.1x | 42.51 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-27 (27d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| WOLF | NYSE | 19.22 | -14.50 | 7.18 | — | 1.1x | 22.48 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-04 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CRWD | NASDAQ | 229.44 | -5.76 | -7.15 | — | 2.5x | 243.46 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-12-01 | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ARIS | NYSE | 12.04 | -5.49 | 7.14 | — | 1.8x | 12.74 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-04 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| OUST | NASDAQ | 23.8 | -15.48 | 7.14 | — | 1.1x | 28.16 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-03 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ASM | AMEX | 3.44 | -5.75 | 7.11 | — | 1.7x | 3.65 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-04 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PLAB | NASDAQ | 24.03 | -8.80 | 7.11 | — | 2.0x | 26.35 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-08-26 (89d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ONDS | NASDAQ | 3.76 | -11.11 | 7.10 | — | 1.0x | 4.23 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-12 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| EGO | NYSE | 24.75 | -7.79 | 7.07 | — | 1.6x | 26.84 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-28 (26d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| HYMC | NASDAQ | 12.61 | -8.49 | 7.06 | — | 1.2x | 13.78 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-27 (27d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| HPE | NYSE | 40.91 | -10.07 | 7.02 | — | 1.8x | 45.49 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-23 (0d ago) | PRE_GAP | Y | Q4 FY2026 results due after today's close (2026-11-23); guidance was $13.9-14.8bn revenue and non-GAAP EPS $1.20-1.30, first group-wide FY27 guide expected |
| AU | NYSE | 72.43 | -5.92 | 7.00 | — | 2.0x | 76.99 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-05 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ONTO | NYSE | 170.16 | -13.15 | 6.96 | — | 1.2x | 195.93 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-09 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CLSK | NASDAQ | 4.89 | -16.27 | 6.95 | — | 0.9x | 5.84 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-08-06 (109d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RXRX | NASDAQ | 2.45 | -9.93 | 6.95 | — | 1.2x | 2.72 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-02 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ECG | NYSE | 76.59 | -8.66 | 6.93 | — | 1.2x | 83.85 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-03 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CRCL | NYSE | 47.545 | -8.36 | 6.93 | — | 1.8x | 51.88 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-04 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ENTG | NASDAQ | 124.53 | -9.85 | 6.92 | — | 1.5x | 138.14 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-29 (25d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BELFA | NASDAQ | 154.64 | -10.63 | 6.89 | — | 1.5x | 173.03 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-28 (26d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FCEL | NASDAQ | 6.69 | -11.86 | 6.88 | — | 1.0x | 7.59 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-09-02 (82d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ECO | NYSE | 84.83 | 2.18 | -6.87 | — | 2.1x | 83.02 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-11 (12d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FLEX | NASDAQ | 66.24 | -10.75 | 6.87 | — | 1.2x | 74.22 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-28 (26d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ALOY | NASDAQ | 3.79 | -12.87 | 6.86 | — | 1.0x | 4.35 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-13 (10d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LPTH | NASDAQ | 5.175 | -13.89 | 6.86 | — | 1.1x | 6.01 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-10 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TSEM | NASDAQ | 115.56 | -9.56 | 6.84 | — | 1.1x | 127.77 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-02 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PL | NYSE | 10.53 | -9.46 | 6.84 | — | 1.4x | 11.63 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-09-03 (81d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| QUBT | NASDAQ | 4.4 | -9.84 | 6.82 | — | 1.4x | 4.88 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-09 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BETA | NYSE | 17.13 | -9.03 | 6.80 | — | 1.2x | 18.83 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-03 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| DOCN | NYSE | 66.76 | -13.40 | 6.79 | — | 1.2x | 77.09 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-03 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MKSI | NASDAQ | 184.52 | -10.03 | 6.76 | — | 1.5x | 205.08 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-04 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| KLAC | NASDAQ | 126.87 | -10.33 | 6.74 | — | 1.5x | 141.48 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-28 (26d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| QMCO | NASDAQ | 11.48 | -17.23 | 6.71 | — | 1.0x | 13.87 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-09 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| DNA | NYSE | 7.46 | -9.02 | 6.70 | — | 0.8x | 8.20 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-05 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PLPC | NASDAQ | 246.78 | -8.86 | 6.69 | — | 1.3x | 270.78 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-28 (26d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| INOD | NASDAQ | 28.12 | -8.91 | 6.69 | — | 1.2x | 30.87 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-05 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| VSAT | NASDAQ | 56.26 | -8.49 | 6.68 | — | 1.2x | 61.48 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-05 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RGTI | NASDAQ | 7.16 | -11.17 | 6.67 | — | 1.0x | 8.06 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-10 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RMIX | NASDAQ | 5.85 | -7.14 | 6.67 | — | 0.7x | 6.30 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-13 (10d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PGY | NASDAQ | 13.5 | -7.66 | 6.67 | — | 1.6x | 14.62 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-29 (25d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| USAR | NASDAQ | 6.27 | -8.73 | 6.66 | — | 1.1x | 6.87 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-09 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| HUT | NASDAQ | 45.95 | -17.65 | 6.66 | — | 0.8x | 55.80 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-04 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AEVA | NASDAQ | 7.88 | -17.66 | 6.66 | — | 1.0x | 9.57 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-04 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CRML | NASDAQ | 3.02 | -13.22 | 6.62 | — | 0.9x | 3.48 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-09-25 (59d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| IONQ | NYSE | 20.72 | -8.76 | 6.59 | — | 1.0x | 22.71 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-05 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RIOT | NASDAQ | 16.23 | -8.46 | 6.59 | — | 1.1x | 17.73 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-04 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| UNH | NYSE | 339.885 | 2.85 | -6.59 | — | 3.1x | 330.48 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-13 (41d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LRCX | NASDAQ | 183.27 | -10.02 | 6.56 | — | 1.4x | 203.68 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-21 (33d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SMCI | NASDAQ | 21.65 | -9.19 | 6.56 | — | 1.3x | 23.84 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-03 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BKSY | NYSE | 16.37 | -12.88 | 6.54 | — | 1.1x | 18.79 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-05 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| KOPN | NASDAQ | 2.575 | -9.33 | 6.50 | — | 0.9x | 2.84 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-10 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MUX | NYSE | 9.165 | -4.63 | 6.49 | — | 1.3x | 9.61 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-09 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| INFQ | NYSE | 6.32 | -13.42 | 6.49 | — | 1.0x | 7.30 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-16 (7d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-16 (Nasdaq earnings calendar; no headline lookup), consensus EPS ($0.05) |
| HL | NYSE | 10.51 | -5.74 | 6.47 | — | 1.5x | 11.15 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-03 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ACHR | NYSE | 2.91 | -9.06 | 6.44 | — | 1.2x | 3.20 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-09 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AG | NYSE | 10.91 | -3.62 | 6.42 | — | 1.6x | 11.32 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-05 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MTSI | NASDAQ | 194.91 | -10.82 | 6.39 | — | 1.1x | 218.55 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-05 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| VICR | NASDAQ | 125.09 | -11.61 | 6.32 | — | 1.0x | 141.52 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-20 (34d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| QBTS | NASDAQ | 6.52 | -10.81 | 6.29 | — | 1.0x | 7.31 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-10 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RMBS | NASDAQ | 66.35 | -12.92 | 6.25 | — | 1.4x | 76.19 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-26 (28d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| WULF | NASDAQ | 9.85 | -14.94 | 6.21 | — | 0.9x | 11.58 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-06 (17d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ERO | NYSE | 21.47 | -8.05 | 6.19 | — | 1.5x | 23.35 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-02 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CDE | NYSE | 10.68 | -7.45 | 6.18 | — | 1.4x | 11.54 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-04 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FPS | NYSE | 18 | -14.12 | 6.17 | — | 0.7x | 20.96 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-12 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMKR | NASDAQ | 30.24 | -11.40 | 6.15 | — | 1.1x | 34.13 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-26 (28d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CAMT | NASDAQ | 89.2 | -8.77 | 6.14 | — | 1.2x | 97.78 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-04 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BE | NYSE | 142.45 | -15.26 | 6.14 | — | 0.9x | 168.11 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-22 (32d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CLS | NYSE | 201.63 | -16.07 | 6.13 | — | 1.0x | 240.23 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-26 (28d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NXE | NYSE | 6.41 | -7.50 | 6.08 | — | 1.9x | 6.93 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-09 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SATL | NASDAQ | 2.465 | -10.04 | 6.07 | — | 0.9x | 2.74 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-10 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| DIOD | NASDAQ | 72.95 | -9.90 | 6.07 | — | 1.2x | 80.97 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-05 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SEI | NYSE | 54.635 | -11.06 | 6.05 | — | 1.1x | 61.43 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-04 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SVM | AMEX | 6.8 | -6.34 | 6.04 | — | 1.4x | 7.26 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-05 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ALGM | NASDAQ | 25.56 | -10.06 | 6.03 | — | 1.1x | 28.42 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-29 (25d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NXT | NASDAQ | 67.13 | -11.61 | 6.02 | — | 1.1x | 75.95 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-28 (26d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NESR | NASDAQ | 17.78 | -10.97 | 6.02 | — | 1.7x | 19.97 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-09 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FTAI | NASDAQ | 150.02 | -10.80 | 5.98 | — | 1.0x | 168.18 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-29 (25d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SGML | NASDAQ | 3.69 | -9.34 | 5.96 | — | 0.9x | 4.07 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-13 (10d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| EQX | AMEX | 8.39 | -5.52 | 5.96 | — | 1.6x | 8.88 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-09 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| P | NYSE | 92.05 | -12.75 | 5.94 | — | 1.2x | 105.50 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-18 (5d ago) | PRE_GAP | — | Q4 2026 results, report date 2026-11-18 (Nasdaq earnings calendar; no headline lookup), consensus EPS $0.28 |
| UPST | NASDAQ | 15.66 | -7.88 | 5.94 | — | 1.4x | 17.00 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-03 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMAT | NASDAQ | 302.63 | -10.71 | 5.94 | — | 1.3x | 338.93 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-12 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BW | NYSE | 3.54 | -15.51 | 5.93 | — | 0.8x | 4.19 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-09 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| STX | NASDAQ | 457.01 | -12.35 | 5.91 | — | 1.1x | 521.39 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-27 (27d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SHOP | NASDAQ | 123.72 | -6.25 | 5.88 | — | 1.8x | 131.97 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-03 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| STRL | NASDAQ | 247.92 | -9.27 | 5.88 | — | 1.0x | 273.25 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-28 (26d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TTMI | NASDAQ | 58.85 | -13.46 | 5.88 | — | 0.9x | 68.00 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-22 (32d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RBLX | NYSE | 46.72 | 0.80 | 5.84 | — | 1.4x | 46.35 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-29 (25d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CIEN | NYSE | 234.37 | -10.76 | 5.82 | — | 0.9x | 262.63 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-09-03 (81d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LEU | NYSE | 81.43 | -9.22 | 5.81 | — | 1.0x | 89.70 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-04 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| QNT | NASDAQ | 27.74 | -0.79 | 5.80 | — | 0.8x | 27.96 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-05 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| XE | NASDAQ | 8.79 | -9.38 | 5.80 | — | 1.1x | 9.70 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-12 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CBRS | NASDAQ | 82.67 | -4.93 | 5.80 | — | 0.9x | 86.96 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-12 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ALM | NASDAQ | 6.39 | -15.48 | 5.79 | — | 1.4x | 7.56 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-12 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PDFS | NASDAQ | 30.44 | -13.03 | 5.78 | — | 1.0x | 35.00 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-05 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| HOOD | NASDAQ | 62.17 | -9.44 | 5.77 | — | 1.5x | 68.65 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-27 (27d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| INTC | NASDAQ | 51.28 | -7.97 | 5.77 | — | 1.0x | 55.72 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-29 (25d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BLSH | NYSE | 19.07 | -4.46 | 5.77 | — | 1.2x | 19.96 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-18 (5d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-18 (Nasdaq earnings calendar; no headline lookup), consensus EPS $0.08 |
| SOUN | NASDAQ | 2.61 | -10.31 | 5.75 | — | 1.6x | 2.91 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-05 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| QS | NASDAQ | 2.79 | -8.52 | 5.73 | — | 1.2x | 3.05 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-21 (33d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| Q | NYSE | 103.47 | -8.94 | 5.71 | — | 1.7x | 113.63 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-04 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LITE | NASDAQ | 460.54 | -13.94 | 5.65 | — | 0.8x | 535.15 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-02 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MRVL | NASDAQ | 122.28 | -11.69 | 5.64 | — | 0.8x | 138.47 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-08-27 (88d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| WDC | NASDAQ | 261.11 | -12.02 | 5.63 | — | 1.1x | 296.78 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-22 (32d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LSCC | NASDAQ | 98.31 | -11.37 | 5.60 | — | 1.1x | 110.92 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-02 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CDNL | NASDAQ | 4.745 | -8.40 | 5.58 | — | 0.6x | 5.18 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-12 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BTG | AMEX | 4.12 | -5.29 | 5.58 | — | 1.4x | 4.35 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-04 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| VIAV | NASDAQ | 26.71 | -9.06 | 5.58 | — | 1.0x | 29.37 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-04 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AUR | NASDAQ | 3.505 | -8.72 | 5.56 | — | 1.4x | 3.84 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-28 (26d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MPWR | NASDAQ | 1142.05 | -11.87 | 5.53 | — | 1.2x | 1295.86 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-29 (25d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FSM | NYSE | 7.33 | -7.80 | 5.53 | — | 1.6x | 7.95 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-04 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TEM | NASDAQ | 54.04 | -9.34 | 5.48 | — | 1.0x | 59.61 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-02 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CORZ | NASDAQ | 11.33 | -15.19 | 5.47 | — | 0.8x | 13.36 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-05 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| XXI | NYSE | 4.03 | -6.50 | 5.46 | — | 1.6x | 4.31 | yahoo_chart_daily | 2026-11-19 | US-listed | — | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SDGR | NASDAQ | 22.93 | -12.95 | 5.45 | — | 0.9x | 26.34 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-04 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| URGN | NASDAQ | 27.65 | -12.86 | 5.42 | — | 1.2x | 31.73 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-04 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SNDK | NASDAQ | 79.24 | -16.05 | 5.38 | — | 0.7x | 94.39 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-29 (25d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| APP | NASDAQ | 348.29 | -8.11 | 5.37 | — | 0.9x | 379.02 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-04 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SMR | NYSE | 3.36 | -11.81 | 5.37 | — | 0.9x | 3.81 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-05 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| DJT | NASDAQ | 3.73 | -8.80 | 5.36 | — | 0.8x | 4.09 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-09 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MTRN | NYSE | 182.47 | -10.02 | 5.35 | — | 1.2x | 202.80 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-04 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GOOGL | NASDAQ | 265.29 | -2.70 | 5.34 | — | 2.4x | 272.66 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-28 (26d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| IAG | NYSE | 14.44 | -5.19 | 5.33 | — | 1.3x | 15.23 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-05 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PAAS | NYSE | 30.61 | -5.50 | 5.33 | — | 1.6x | 32.39 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-04 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| QXO | NYSE | 10.34 | -6.17 | 5.32 | — | 1.2x | 11.02 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-12 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NNE | NASDAQ | 9.1 | -8.73 | 5.27 | — | 1.0x | 9.97 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-08-12 (103d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AEM | NYSE | 151.3 | -4.39 | 5.27 | — | 1.5x | 158.24 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-28 (26d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| WPM | NYSE | 109.91 | -5.36 | 5.27 | — | 1.6x | 116.13 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-05 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MNRO | NASDAQ | 9.5 | -2.66 | -5.26 | — | 1.3x | 9.76 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-29 (25d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PI | NASDAQ | 143.93 | -9.40 | 5.26 | — | 1.8x | 158.86 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-28 (26d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NG | AMEX | 4.67 | -2.91 | 5.26 | — | 1.3x | 4.81 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-08 (46d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ACLS | NASDAQ | 90.26 | -9.69 | 5.25 | — | 1.2x | 99.94 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-05 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CCJ | NYSE | 57.995 | -5.58 | 5.25 | — | 1.5x | 61.42 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-30 (24d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FN | NYSE | 285.04 | -8.56 | 5.25 | — | 0.8x | 311.71 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-02 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MU | NASDAQ | 594.51 | -13.89 | 5.24 | — | 0.9x | 690.44 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-09-30 (54d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| DHT | NYSE | 21.58 | 0.33 | -5.24 | — | 2.2x | 21.51 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-09 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SSRM | NASDAQ | 21.59 | -7.30 | 5.23 | — | 1.5x | 23.29 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-03 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GLW | NYSE | 94.38 | -10.94 | 5.21 | — | 1.2x | 105.97 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-27 (27d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LCID | NASDAQ | 2.5 | -10.39 | 5.20 | — | 0.9x | 2.79 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-09 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GFS | NASDAQ | 35.56 | -8.68 | 5.17 | — | 1.4x | 38.94 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-04 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| UROY | NASDAQ | 2.32 | -8.66 | 5.17 | — | 1.3x | 2.54 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-09-14 (70d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GNL | NYSE | 6 | -0.17 | 5.17 | — | 3.3x | 6.01 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-04 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AGI | NYSE | 24.87 | -4.24 | 5.15 | — | 1.4x | 25.97 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-28 (26d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AGLT | NASDAQ | 5.85 | -9.86 | 5.13 | — | 0.7x | 6.49 | yahoo_chart_daily | 2026-11-19 | US-listed | — | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ZETA | NYSE | 29.51 | -8.41 | 5.11 | — | 1.3x | 32.22 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-09 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MWH | NASDAQ | 24.69 | -9.16 | 5.10 | — | 1.3x | 27.18 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-12 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| KRMN | NYSE | 29.25 | -11.34 | 5.09 | — | 0.7x | 32.99 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-05 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GOOG | NASDAQ | 264 | -2.59 | 5.08 | — | 2.5x | 271.02 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-28 (26d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| KGC | NYSE | 17.32 | -5.10 | 5.08 | — | 1.5x | 18.25 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-28 (26d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FIGR | NASDAQ | 23.84 | -7.74 | 5.08 | — | 1.2x | 25.84 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-12 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMC | NYSE | 2.57 | -7.89 | 5.06 | — | 1.3x | 2.79 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-04 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TGB | AMEX | 5.34 | -4.81 | 5.06 | — | 1.4x | 5.61 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-04 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MTZ | NYSE | 144.71 | -12.17 | 5.03 | — | 1.0x | 164.76 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-29 (25d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMPX | NYSE | 5.77 | -9.84 | 5.03 | — | 0.9x | 6.40 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-10 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LWLG | NASDAQ | 2.59 | -13.67 | 5.02 | — | 0.7x | 3.00 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-10 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| JBL | NYSE | 225.76 | -8.39 | 5.01 | — | 1.6x | 246.44 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-09-30 (54d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CVS | NYSE | 80.84 | 1.00 | -5.00 | — | 2.1x | 80.04 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-04 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| COHR | NYSE | 187.22 | -12.90 | 4.96 | — | 0.8x | 214.94 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-04 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FRVO | NASDAQ | 9.99 | -10.32 | 4.95 | — | 0.6x | 11.14 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-09 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SNOW | NYSE | 254.82 | -5.13 | 4.94 | — | 1.6x | 268.59 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-09-02 (82d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NEM | NYSE | 94.68 | -5.37 | 4.91 | — | 1.6x | 100.05 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-22 (32d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| VRT | NYSE | 166.24 | -10.14 | 4.88 | — | 0.8x | 184.99 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-28 (26d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| IPGP | NASDAQ | 58.64 | -8.29 | 4.86 | — | 1.3x | 63.94 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-03 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FSLY | NASDAQ | 14.91 | -11.57 | 4.83 | — | 0.8x | 16.86 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-04 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AVGO | NASDAQ | 304.41 | -12.19 | 4.81 | — | 1.1x | 346.65 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-09-02 (82d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GOOGN | NASDAQ | 39.73 | -2.12 | 4.81 | — | 2.9x | 40.59 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-28 (26d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TSLA | NASDAQ | 345.82 | -7.64 | 4.80 | — | 1.7x | 374.41 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-21 (33d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PLTR | NASDAQ | 143.49 | -6.63 | 4.56 | — | 1.6x | 153.68 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-02 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RIVN | NASDAQ | 10.33 | -8.50 | 4.55 | — | 1.3x | 11.29 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-29 (25d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SEDG | NASDAQ | 18.27 | -10.13 | 4.54 | — | 0.9x | 20.33 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-04 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| KTOS | NASDAQ | 26.89 | -9.31 | 4.50 | — | 1.0x | 29.65 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-05 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ROG | NYSE | 109.57 | -9.03 | 4.50 | — | 1.3x | 120.44 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-27 (27d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PLXS | NASDAQ | 189.89 | -9.03 | 4.48 | — | 1.3x | 208.73 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-28 (26d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PRIM | NYSE | 53.6 | -10.79 | 4.48 | — | 0.8x | 60.08 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-03 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LASR | NASDAQ | 32.28 | -14.33 | 4.46 | — | 0.7x | 37.68 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-05 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| UI | NYSE | 590.66 | -10.94 | 4.46 | — | 1.1x | 663.22 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-06 (17d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ORCL | NYSE | 101.19 | -8.48 | 4.40 | — | 1.0x | 110.57 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-09-10 (74d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| APH | NYSE | 69.745 | -7.76 | 4.39 | — | 1.3x | 75.61 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-28 (26d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ACCV | NASDAQ | 9.58 | -13.62 | 4.38 | — | 0.6x | 11.09 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-12 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NET | NYSE | 274.96 | -9.46 | 4.38 | — | 0.9x | 303.68 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-05 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SCCO | NYSE | 134.02 | -5.26 | 4.37 | — | 1.3x | 141.46 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-21 (33d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TXG | NASDAQ | 51.8 | -9.72 | 4.36 | — | 0.8x | 57.38 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-05 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| HLIT | NASDAQ | 9.41 | -10.55 | 4.36 | — | 1.4x | 10.52 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-02 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMD | NASDAQ | 424.39 | -13.25 | 4.35 | — | 0.6x | 489.19 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-03 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| EXTR | NASDAQ | 24.2 | -9.19 | 4.34 | — | 1.2x | 26.65 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-28 (26d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LGN | NASDAQ | 32.31 | -7.92 | 4.33 | — | 0.6x | 35.09 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-12 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SSMR | NYSE | 10.45 | -13.21 | 4.30 | — | 0.7x | 12.04 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-12 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| HIMS | NYSE | 14.6 | -8.86 | 4.28 | — | 0.7x | 16.02 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-09 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMRC | NYSE | 20.7 | -9.05 | 4.25 | — | 0.7x | 22.76 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-09 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| QCOM | NASDAQ | 149.94 | -7.45 | 4.23 | — | 1.2x | 162.01 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-04 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ENPH | NASDAQ | 19.63 | -10.69 | 4.23 | — | 0.8x | 21.98 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-27 (27d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ADI | NASDAQ | 345.92 | -8.35 | 4.21 | — | 1.4x | 377.44 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-08-19 (96d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ETN | NYSE | 311.33 | -5.82 | 4.21 | — | 1.2x | 330.57 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-03 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CDNS | NASDAQ | 281.58 | -7.64 | 4.21 | — | 1.7x | 304.88 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-26 (28d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TXN | NASDAQ | 263.75 | -7.70 | 4.20 | — | 1.5x | 285.75 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-21 (33d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| KLIC | NASDAQ | 54.71 | -11.16 | 4.19 | — | 0.9x | 61.58 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-18 (5d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-18 (Nasdaq earnings calendar; no headline lookup), consensus EPS $1.31 |
| AGX | NYSE | 268.94 | -9.10 | 4.16 | — | 0.8x | 295.85 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-09-02 (82d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PWR | NYSE | 559.03 | -4.83 | 4.11 | — | 1.0x | 587.43 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-29 (25d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SHLS | NASDAQ | 6.48 | -9.87 | 4.10 | — | 0.7x | 7.19 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-04 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ANET | NYSE | 167.66 | -11.57 | 4.07 | — | 0.8x | 189.59 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-03 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AVAV | NASDAQ | 86.79 | -9.51 | 4.06 | — | 0.8x | 95.91 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-09-09 (75d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BELFB | NASDAQ | 196.38 | -10.93 | 3.91 | — | 0.9x | 220.48 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-28 (26d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| WCC | NYSE | 282.04 | -8.18 | 3.89 | — | 1.0x | 307.17 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-29 (25d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NTLA | NASDAQ | 10 | 5.04 | 3.86 | — | 0.8x | 9.52 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-05 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PS | NYSE | 33.61 | -8.77 | 3.84 | — | 0.8x | 36.84 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-02 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LBRT | NYSE | 10.755 | -11.84 | 3.77 | — | 0.8x | 12.20 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-21 (33d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| IBKR | NASDAQ | 71.19 | -5.90 | 3.75 | — | 1.3x | 75.65 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-15 (39d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SNPS | NASDAQ | 396.17 | -8.06 | 3.74 | — | 1.7x | 430.91 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-08-26 (89d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMBA | NASDAQ | 53.07 | -9.94 | 3.73 | — | 1.0x | 58.93 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-09-03 (81d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GEV | NYSE | 699.33 | -7.53 | 3.67 | — | 1.0x | 756.28 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-28 (26d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| META | NASDAQ | 560.84 | -5.93 | 3.59 | — | 1.7x | 596.22 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-21 (33d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FTNT | NASDAQ | 124.56 | -5.25 | 3.56 | — | 0.9x | 131.46 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-28 (26d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| REAL | NASDAQ | 10.78 | -8.88 | 3.53 | — | 0.8x | 11.83 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-29 (25d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BHE | NYSE | 55.63 | -9.35 | 3.52 | — | 1.0x | 61.37 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-28 (26d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AI | NYSE | 9.13 | -9.06 | 3.50 | — | 1.1x | 10.04 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-09-02 (82d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CSCO | NASDAQ | 90.64 | -4.29 | 3.49 | — | 1.4x | 94.70 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-12 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CLF | NYSE | 10.67 | -8.96 | 3.37 | — | 1.0x | 11.72 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-19 (35d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| WBTN | NASDAQ | 8.25 | -9.54 | 3.31 | — | 1.0x | 9.12 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-09 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MS | NYSE | 165.67 | -5.32 | 3.27 | — | 1.6x | 174.98 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-14 (40d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BN | NYSE | 37.75 | -3.06 | 3.26 | — | 1.6x | 38.94 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-12 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| URI | NYSE | 973.43 | -8.13 | 3.24 | — | 1.2x | 1059.56 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-21 (33d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| JCI | NYSE | 130.18 | -4.28 | 3.23 | — | 1.1x | 136.00 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-27 (27d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SLS | NASDAQ | 13.66 | -8.08 | 3.22 | — | 0.2x | 14.86 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-12 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CEG | NASDAQ | 237.41 | -5.80 | 3.21 | — | 1.0x | 252.03 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-09 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FSLR | NASDAQ | 137.59 | -9.45 | 3.21 | — | 1.0x | 151.95 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-29 (25d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BAM | NYSE | 48.94 | -2.53 | 3.17 | — | 1.7x | 50.21 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-06 (17d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| KALU | NASDAQ | 90.16 | -8.36 | 3.15 | — | 0.9x | 98.38 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-21 (33d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BX | NYSE | 110.8 | -4.47 | 3.15 | — | 1.5x | 115.99 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-22 (32d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CAT | NYSE | 510.45 | -5.01 | 3.14 | — | 1.0x | 537.37 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-29 (25d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BNY | NYSE | 141.24 | -2.48 | 3.13 | — | 2.6x | 144.83 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-15 (39d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BLK | NYSE | 1101.72 | -3.00 | 3.09 | — | 1.7x | 1135.81 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-14 (40d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TTD | NASDAQ | 13.38 | -8.10 | 3.06 | — | 0.8x | 14.56 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-09 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NOVT | NASDAQ | 101.99 | -11.22 | -3.04 | — | 0.8x | 114.88 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-09 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMZN | NASDAQ | 246.82 | -4.10 | 3.02 | — | 1.3x | 257.37 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-29 (25d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| EQIX | NASDAQ | 968.22 | -4.89 | 2.99 | — | 1.4x | 1018.05 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-28 (26d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PRLB | NYSE | 57.52 | -8.54 | 2.99 | — | 0.7x | 62.89 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-29 (25d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SOJE | NYSE | 15.05 | 0.80 | 2.99 | — | 3.2x | 14.93 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-05 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MSFT | NASDAQ | 484.52 | -2.77 | 2.99 | — | 1.6x | 498.30 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-28 (26d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MRNA | NASDAQ | 195 | -2.17 | 2.92 | — | 0.7x | 199.33 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-06 (17d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SPCX | NASDAQ | 127.79 | -7.69 | 2.86 | — | 0.9x | 138.43 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-20 (34d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| HWM | NYSE | 209.16 | -4.13 | 2.84 | — | 0.9x | 218.17 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-29 (25d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GENB | NASDAQ | 9.54 | -8.00 | 2.83 | — | 0.4x | 10.37 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-12 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PH | NYSE | 872.345 | -3.73 | 2.83 | — | 1.5x | 906.13 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-05 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| HTFL | NASDAQ | 46.69 | 4.62 | 2.83 | — | 0.7x | 44.63 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-12 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GS | NYSE | 790.69 | -6.71 | 2.82 | — | 1.3x | 847.53 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-13 (41d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NOW | NYSE | 87.66 | -1.36 | 2.81 | — | 0.7x | 88.87 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-28 (26d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ELV | NYSE | 394.48 | 1.11 | -2.80 | — | 1.4x | 390.16 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-21 (33d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| HAWK | NYSE | 16.14 | -10.73 | 2.79 | — | 0.5x | 18.08 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-12 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| KKR | NYSE | 88.54 | -3.90 | 2.78 | — | 1.3x | 92.13 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-09 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ECL | NYSE | 294.7 | -0.88 | 2.65 | — | 1.9x | 297.32 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-27 (27d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RKT | NYSE | 13.75 | 4.25 | 2.59 | — | 0.8x | 13.19 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-29 (25d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| UBER | NYSE | 63.475 | -3.24 | 2.54 | — | 1.5x | 65.60 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-04 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RCL | NYSE | 296.48 | -2.20 | 2.54 | — | 0.9x | 303.15 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-27 (27d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TMDX | NASDAQ | 85.25 | -9.33 | 2.53 | — | 0.6x | 94.02 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-05 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PNC | NYSE | 213.17 | -2.22 | 2.52 | — | 1.9x | 218.00 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-15 (39d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| KVYO | NYSE | 22.24 | 4.41 | 2.52 | — | 1.1x | 21.30 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-04 (19d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ECHO | NASDAQ | 84.26 | -8.72 | 2.50 | — | 0.7x | 92.31 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-03 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ITW | NYSE | 273.57 | -1.20 | 2.46 | — | 1.9x | 276.89 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-27 (27d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| C | NYSE | 110.62 | -4.04 | 2.42 | — | 1.5x | 115.28 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-13 (41d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ISRG | NASDAQ | 399.05 | -2.01 | 2.34 | — | 1.1x | 407.24 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-20 (34d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GENI | NYSE | 5.18 | -11.00 | 2.32 | — | 0.6x | 5.82 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-05 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| IBM | NYSE | 224.44 | 0.25 | 2.29 | — | 1.5x | 223.88 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-21 (33d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| WFC | NYSE | 78.62 | -2.47 | 2.26 | — | 1.7x | 80.61 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-13 (41d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| INTU | NASDAQ | 270.44 | -12.77 | 2.24 | — | 0.9x | 310.02 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-19 (4d ago) | PRE_GAP | — | Q4 2026 results, report date 2026-11-19 (Nasdaq earnings calendar; no headline lookup), consensus EPS $2.47 |
| JPM | NYSE | 310.68 | -2.98 | 2.23 | — | 1.4x | 320.22 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-13 (41d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| WMB | NYSE | 64.31 | -2.75 | 2.19 | — | 1.1x | 66.13 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-02 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CRM | NYSE | 180.675 | -1.44 | 2.19 | — | 1.0x | 183.31 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-08-26 (89d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| EFOR | NYSE | 31.32 | 7.89 | 2.17 | — | 0.6x | 29.03 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-28 (26d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| IBRX | NASDAQ | 6.02 | -8.37 | 2.16 | — | 0.4x | 6.57 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-09 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SHW | NYSE | 339.74 | -0.03 | 2.14 | — | 1.0x | 339.83 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-27 (27d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GAP | NYSE | 20.94 | 11.44 | 2.14 | — | 0.6x | 18.79 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-19 (4d ago) | PRE_GAP | — | Q4 2026 results, report date 2026-11-19 (Nasdaq earnings calendar; no headline lookup), consensus EPS $0.76 |
| GE | NYSE | 309.72 | -2.87 | 2.11 | — | 0.9x | 318.88 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-20 (34d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| DRTS | NASDAQ | 11.755 | 3.93 | 2.08 | — | 0.6x | 11.31 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-19 (4d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-19 (Nasdaq earnings calendar; no headline lookup), consensus EPS ($0.15) |
| BNS | NYSE | 83.66 | -2.68 | 2.08 | — | 1.5x | 85.96 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-08-25 (90d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BA | NYSE | 155.89 | -2.88 | 2.06 | — | 1.1x | 160.51 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-27 (27d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BKNG | NASDAQ | 144.91 | -1.64 | 2.03 | — | 0.9x | 147.32 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-11-03 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| UBS | NYSE | 43.32 | -3.78 | 2.03 | — | 1.1x | 45.02 | yahoo_chart_daily | 2026-11-19 | US-listed | 2026-10-28 (26d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |

## US — QUIET one-liners

| Ticker | Venue | Chg % | Pre-mkt % | Post-mkt % | Move vs avg daily | Ref close | Ref source | Ref asof | US tradeable | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|
| NFLX | NASDAQ | -2.96 | 1.97 | — | 1.8x | 58.46 | yahoo_chart_daily | 2026-11-19 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| GPN | NYSE | 9.95 | 1.94 | — | 2.7x | 83.52 | yahoo_chart_daily | 2026-11-19 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| SYK | NYSE | -0.98 | 1.94 | — | 0.5x | 313.08 | yahoo_chart_daily | 2026-11-19 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| TMO | NYSE | -2.79 | 1.92 | — | 1.7x | 688.75 | yahoo_chart_daily | 2026-11-19 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| ABNB | NASDAQ | -1.41 | 1.90 | — | 0.5x | 172.79 | yahoo_chart_daily | 2026-11-19 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| SPGI | NYSE | -0.66 | 1.90 | — | 0.5x | 442.66 | yahoo_chart_daily | 2026-11-19 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| MKC | NYSE | 3.43 | 1.85 | — | 1.6x | 45.83 | yahoo_chart_daily | 2026-11-19 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| ACN | NYSE | 1.21 | 1.84 | — | 0.5x | 218.58 | yahoo_chart_daily | 2026-11-19 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| SBUX | NASDAQ | -1.28 | 1.82 | — | 0.8x | 104.47 | yahoo_chart_daily | 2026-11-19 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| MMM | NYSE | -0.27 | 1.81 | — | 0.2x | 178.47 | yahoo_chart_daily | 2026-11-19 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| CTSH | NASDAQ | 3.11 | 1.79 | — | 1.3x | 56.31 | yahoo_chart_daily | 2026-11-19 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| DE | NYSE | -2.50 | 1.77 | — | 1.7x | 624.89 | yahoo_chart_daily | 2026-11-19 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| UNP | NYSE | -1.15 | 1.77 | — | 0.8x | 290.63 | yahoo_chart_daily | 2026-11-19 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| AXP | NYSE | -3.02 | 1.77 | — | 2.3x | 311.11 | yahoo_chart_daily | 2026-11-19 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| MCO | NYSE | -1.06 | 1.75 | — | 0.7x | 471.84 | yahoo_chart_daily | 2026-11-19 | US-listed | — | no catalyst lookup (outside the per-run budget) |

## EU/UK — Headline table

| Ticker | Market | Venue | Close | Chg % | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | Session asof | Settle | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| VER | sweden | OMXSTO | 6.72 | -16.83 | SEK | 5.8x | 8.08 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | live | none | 2026-11-23 (0d ago) | Y | Q3 2026 interim report (reported 2026-11-23): adjusted EBITDA ~12% below consensus, revenue in line; FY26 guidance reiterated but now expected at the lower end of EUR 680-730m revenue and EUR 145-175m EBITDA |
| HUNT | norway | OSL | 18.62 | +14.51 | NOK | 3.7x | 16.26 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | live | none | 2026-11-20 (3d ago) | — | no catalyst lookup (outside the per-run budget) |
| SIVE | sweden | OMXSTO | 12.77 | +11.92 | SEK | 1.9x | 11.41 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | live | none | 2026-08-27 (88d ago) | N | Q3 2026 interim report postponed from 26 Nov to 30 Nov (announced 23 Nov, US Thanksgiving clash); a new public short seller was disclosed on 20 Nov |
| NWG | poland | GPW | 78.2 | -11.14 | PLN | 7.3x | 88.00 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | live | none | 2026-11-20 (3d ago) | — | no catalyst lookup (outside the per-run budget) |
| ABVX | france | EURONEXT | 68.55 | +8.81 | EUR | 3.1x | 63.00 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | live | none | 2026-09-21 (63d ago) | N | rebound after the Scorpion Capital short report (20 Nov) and Abivax's rebuttal the same evening; presenting at the German Equity Forum 23-25 Nov |
| JEN | germany | XETR | 34.54 | +8.55 | EUR | 3.0x | 31.82 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | live | none | 2026-11-10 (13d ago) | — | no catalyst lookup (outside the per-run budget) |
| OHB | germany | XETR | 185 | +7.56 | EUR | 1.6x | 172.00 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | live | US line (OTC:OHBTF) | 2026-11-12 (11d ago) | — | no catalyst lookup (outside the per-run budget) |
| DRX | uk | LSE | 877.72972 | +6.84 | GBX | 6.5x | 821.50 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | live | none | 2026-07-30 (116d ago) | — | no catalyst lookup (outside the per-run budget) |
| GL9 | ireland | EURONEXT | 17.99 | -6.55 | EUR | 2.9x | 19.25 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | live | none | 2026-08-06 (109d ago) | — | no catalyst lookup (outside the per-run budget) |
| NOHAL | norway | OSL | 26 | -6.47 | NOK | 3.9x | 27.80 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | live | none | 2026-11-19 (4d ago) | — | no catalyst lookup (outside the per-run budget) |
| FRVIA | france | EURONEXT | 7.928 | +5.79 | EUR | 3.0x | 7.49 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | live | none | 2026-07-31 (115d ago) | — | no catalyst lookup (outside the per-run budget) |
| BETCO_DKK | denmark | OMXCOP | 39.45 | +5.62 | DKK | 3.3x | 37.35 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | live | none | 2026-11-18 (5d ago) | — | no catalyst lookup (outside the per-run budget) |
| POS | austria | VIE | 35.35 | +5.37 | EUR | 3.7x | 33.55 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | live | none | 2026-11-19 (4d ago) | — | no catalyst lookup (outside the per-run budget) |
| YUBICO | sweden | OMXSTO | 188.1 | +4.97 | SEK | 1.0x | 179.20 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | live | US line (OTC:YUBCF) | 2026-11-05 (18d ago) | N | no fresh catalyst found - the Q3 report was 5 Nov and the capital markets day 19 Nov; the stock is still up 77% over 12 months |
| DVL | poland | GPW | 8.26 | -4.95 | PLN | 2.9x | 8.69 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | live | none | 2026-11-19 (4d ago) | — | no catalyst lookup (outside the per-run budget) |
| ERA | france | EURONEXT | 16.67 | -4.85 | EUR | 0.9x | 17.52 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | live | none | 2026-07-29 (117d ago) | N | no fresh catalyst found - still trading ex-rights after the EUR 500m capital increase and at a ten-year low; no release today |
| ASML | netherlands | EURONEXT | 1224.2 | +4.81 | EUR | 1.5x | 1168.00 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | live | ADR (NASDAQ:ASML) | 2026-10-14 (40d ago) | N | chip-equipment sector rebound after Nvidia's stronger-than-expected Q3 (ASML +3-5% with ASM Intl and BE Semiconductor); no ASML release today |
| COFFEE_B | sweden | OMXSTO | 21.13 | +4.79 | SEK | 3.5x | 20.16 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | live | ADR (OTC:LKNCY) | 2026-11-05 (18d ago) | N | Kepler Cheuvreux raised its target price to SEK 27 (hold) today; the Chronicles: Medieval IP acquisition (inside information 14 Nov) still awaits an EGM |
| ENT | uk | LSE | 454.871 | +4.78 | GBX | 2.9x | 434.10 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | live | none | 2026-08-13 (102d ago) | — | no catalyst lookup (outside the per-run budget) |
| UQA | austria | VIE | 19.3 | +4.66 | EUR | 3.2x | 18.44 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | live | none | 2025-08-22 (458d ago) | — | no catalyst lookup (outside the per-run budget) |
| FCT | italy | MIL | 11.27 | +4.55 | EUR | 2.3x | 10.78 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | live | none | 2026-07-29 (117d ago) | — | no catalyst lookup (outside the per-run budget) |
| BESI | netherlands | EURONEXT | 149.1 | +4.48 | EUR | 1.4x | 142.70 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | live | none | 2026-10-21 (33d ago) | — | no catalyst lookup (outside the per-run budget) |
| CRNA | norway | OSL | 9.82 | +4.25 | NOK | 2.0x | 9.42 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | live | none | — | — | no catalyst lookup (outside the per-run budget) |
| TPRO | italy | MIL | 19.18 | +4.18 | EUR | 1.0x | 18.41 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | live | none | 2026-08-05 (110d ago) | — | no catalyst lookup (outside the per-run budget) |
| TYRES | finland | OMXHEX | 12.46 | -4.15 | EUR | 2.2x | 13.00 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | live | ADR (OTC:NKRKY) | 2026-10-27 (27d ago) | N | Kepler Cheuvreux cut the rating to Reduce (Hold) with a EUR 12.50 target, published 23 Nov; no company release |
| MDATA | norway | OSL | 12.66 | +3.94 | NOK | 1.9x | 12.18 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | live | none | 2026-10-30 (24d ago) | — | no catalyst lookup (outside the per-run budget) |
| CMBT | belgium | EURONEXT | 15.34 | +3.79 | EUR | 2.6x | 14.78 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | live | none | 2026-08-27 (88d ago) | N | Q3 2026 results pulled forward to 24 Nov (announced 17 Nov); DNB Carnegie upgraded CMB.Tech to Buy from Hold on 17 Nov |
| VOD | uk | LSE | 104.25 | -3.78 | GBX | 2.7x | 108.35 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | live | none | 2026-11-10 (13d ago) | — | no catalyst lookup (outside the per-run budget) |

## AU (ASX) — Headline table

| Ticker | Venue | Close | Chg % | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | Session asof | Settle | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ALQ | ASX | 16.94 | -12.23 | AUD | 5.6x | 19.30 | yahoo_chart_daily | 2026-11-19 | 2026-11-23 | settled | none | 2026-11-23 (0d ago) | Y | H1 FY27 results released before the open (reported 2026-11-23): revenue +3.4% to A$1,715m (organic +10.2%), underlying EBIT +18.6% to A$332.7m, underlying NPAT +23.6% to A$214.6m, EPS 42.3c, interim DPS 23.3c; Life Sciences "below expectations" and FY27 organic growth guidance cut to about 3% |
| WEB | ASX | 3.26 | -10.44 | AUD | 4.1x | 3.64 | yahoo_chart_daily | 2026-11-19 | 2026-11-23 | settled | US line (OTC:TSWCF) | 2026-05-26 (181d ago) | N | no fresh catalyst found - only a substantial-holder notice since Friday; the 1H27 interim report is due 24 Nov |
| SGM | ASX | 21.28 | +9.69 | AUD | 3.7x | 19.40 | yahoo_chart_daily | 2026-11-19 | 2026-11-23 | settled | none | 2026-08-17 (98d ago) | Y | AGM Chair's Address (20 Nov): FY2026 underlying EBIT up ~170% to A$468m and 1H FY27 group underlying EBIT guidance lifted to A$270-285m; Macquarie downgraded while Jefferies raised its target |

## APAC/Gulf — Headline table

| Ticker | Market | Venue | Close | Chg % | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | Session asof | Settle | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TRIN | indonesia | IDX | 198 | +34.69 | IDR | 3.1x | 147.00 | yahoo_chart_daily | 2026-11-19 | 2026-11-22 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| TRUE | indonesia | IDX | 43 | +30.30 | IDR | 2.9x | 33.00 | yahoo_chart_daily | 2026-11-19 | 2026-11-22 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| CUAN | indonesia | IDX | 400 | +25.00 | IDR | 4.2x | 320.00 | yahoo_chart_daily | 2026-11-19 | 2026-11-22 | settled | none | 2026-07-31 (115d ago) | — | no catalyst lookup (outside the per-run budget) |
| APLAPOLLO | india | BSE | 1668.15 | -21.39 | INR | 8.8x | 2122.15 | yahoo_chart_daily | 2026-11-19 | 2026-11-22 | settled | none | 2026-10-26 (28d ago) | N | Tata Steel to buy 26.38% from promoter S Gupta at Rs 2,100/share in three tranches (Rs 16,756 Cr) and to trigger an open offer, below Friday's Rs 2,122.15 close |
| JTS | thailand | SET | 14.3 | +20.17 | THB | 3.5x | 11.90 | yahoo_chart_daily | 2026-11-19 | 2026-11-22 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| 301030 | china | SZSE | 3.95 | +20.06 | CNY | 2.8x | 3.29 | yahoo_chart_daily | 2026-11-19 | 2026-11-22 | settled | none | 2024-04-25 (942d ago) | — | no catalyst lookup (outside the per-run budget) |
| 300006 | china | SZSE | 8.74 | +20.05 | CNY | 2.5x | 7.28 | yahoo_chart_daily | 2026-11-19 | 2026-11-22 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| 300007 | china | SZSE | 36.1 | +20.01 | CNY | 3.3x | 30.08 | yahoo_chart_daily | 2026-11-19 | 2026-11-22 | settled | none | 2026-08-29 (86d ago) | — | no catalyst lookup (outside the per-run budget) |
| SKYLMILAR | india | BSE | 15.98 | +19.97 | INR | 3.6x | 13.32 | yahoo_chart_daily | 2026-11-19 | 2026-11-22 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| CNT | thailand | SET | 2.44 | -18.67 | THB | 7.5x | 3.00 | yahoo_chart_daily | 2026-11-19 | 2026-11-22 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| GTK | newzealand | NZX | 3.87 | -14.00 | NZD | 4.9x | 4.50 | yahoo_chart_daily | 2026-11-19 | 2026-11-22 | settled | none | 2026-11-22 (1d ago) | — | no catalyst lookup (outside the per-run budget) |
| 9557 | ksa | TADAWUL | 210 | -13.47 | SAR | 4.1x | 242.70 | yahoo_chart_daily | 2026-11-22 | 2026-11-23 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| MGI | thailand | SET | 2.94 | +13.08 | THB | 3.6x | 2.60 | yahoo_chart_daily | 2026-11-19 | 2026-11-22 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| 9637 | ksa | TADAWUL | 9.85 | +9.93 | SAR | 2.7x | 8.96 | yahoo_chart_daily | 2026-11-22 | 2026-11-23 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| 4190 | ksa | TADAWUL | 15.68 | -8.04 | SAR | 4.2x | 17.05 | yahoo_chart_daily | 2026-11-22 | 2026-11-23 | settled | none | 2026-11-08 (15d ago) | N | Jarir disclosed the impact of Saudi Arabia's new 15% local minimum tax: about SAR 130m, ~11% of projected net profit, from January 2027 |
| H22 | singapore | SGX | 1.73 | -5.98 | SGD | 2.2x | 1.84 | yahoo_chart_daily | 2026-11-19 | 2026-11-22 | settled | none | 2026-08-12 (103d ago) | — | no catalyst lookup (outside the per-run budget) |
| AWX | singapore | SGX | 6 | +5.45 | SGD | 0.9x | 5.69 | yahoo_chart_daily | 2026-11-19 | 2026-11-22 | settled | none | 2026-08-12 (103d ago) | — | no catalyst lookup (outside the per-run budget) |
| SAN | newzealand | NZX | 6.56 | -5.07 | NZD | 3.5x | 6.91 | yahoo_chart_daily | 2026-11-19 | 2026-11-22 | settled | none | 2026-11-16 (7d ago) | — | no catalyst lookup (outside the per-run budget) |
| RYM | newzealand | NZX | 1.75 | -4.37 | NZD | 2.8x | 1.83 | yahoo_chart_daily | 2026-11-19 | 2026-11-22 | settled | none | 2026-05-26 (181d ago) | N | no fresh catalyst found - broad NZX selloff (S&P/NZX 50 -2.67%); 1H27 results due 25 Nov, not yet published |
| F17 | singapore | SGX | 1.77 | -3.28 | SGD | 2.6x | 1.83 | yahoo_chart_daily | 2026-11-19 | 2026-11-22 | settled | none | 2026-08-26 (89d ago) | — | no catalyst lookup (outside the per-run budget) |

## Source health

- scanner_calls: 57 | scanner_errors: 0
- markets_scanned: US + 17 EU/UK + ASX + 7 APAC/Gulf (india, thailand, indonesia, china, singapore, newzealand, ksa)
- pipeline_version: 2026-11-20.1
- et_clock: zoneinfo America/New_York (DST-aware; a fixed UTC-4 mislabels every winter fire)
- premarket_window: 04:00-09:30 ET, resolved with zoneinfo (09:00-14:30 UTC in winter, 08:00-13:30 UTC in summer)
- session_selection: by DATE and order, never by a modal time-of-day. Yahoo stamps a daily bar at the session open, so the ET stamp of the SAME session shifts by one hour across a DST boundary; a modal filter kept the OLDER bars and discarded the NEWEST ones, which rolled the base back to the prior-prior session (66 US + 21 ASX rows lost on 2026-11-03, 24 of 25 ASX rows lost on 2026-11-04).
- yahoo_calls: 420 | yahoo_429: 0 | yahoo_errors: 0 | yahoo_breaker: closed
- reference_close (screener vs Yahoo, resolved BEFORE the tables were built): agree=406 mismatch=3 unverified=1 stale_reference=3
  method: the screener's implied reference close (close / (1 + change/100)) is compared
  with Yahoo's own reference close. A match proves the move was measured against the
  TRUE prior close; a mismatch means the row sits on a STALE reference (phantom move).
  Coverage: every row of the US headline, US QUIET, EU/UK and ASX tables is checked.
  Yahoo bar mode: {"closed": 377, "live": 29} (closed = last completed session bar;
  live = in-progress EU/UK session bar, which is what a weekday 08:00 ET EU move needs)
  live drift between the screener snapshot and the later Yahoo print: median=0.00pp max=1.49pp (expected on a live market)
- cross_check mismatches: [{"region": "US", "symbol": "TER", "tv": -0.063, "yahoo": -9.959, "delta": 9.896, "ref_delta_pct": -9.961, "tv_implied_ref": 204.775, "yahoo_ref": 227.43, "yahoo_date": "2026-11-20", "yahoo_ref_date": "2026-11-19", "verdict": "stale_reference"}, {"region": "germany", "symbol": "IFX.DE", "tv": 5.668, "yahoo": 3.059, "delta": 2.609, "ref_delta_pct": -2.157, "tv_implied_ref": 44.46, "yahoo_ref": 45.44, "yahoo_date": "2026-11-23", "yahoo_ref_date": "2026-11-20", "verdict": "stale_reference"}, {"region": "AU", "symbol": "ZIP.AX", "tv": 363.501, "yahoo": -9.409, "delta": 372.91, "ref_delta_pct": -81.882, "tv_implied_ref": 1.685, "yahoo_ref": 9.3, "yahoo_date": "2026-11-19", "yahoo_ref_date": "2026-11-18", "verdict": "stale_reference"}]
- rows_dropped_stale_ref: 3 (rows whose screener-implied reference close disagreed with Yahoo's by more than 0.5%; they are dropped, not published)
- rows_dropped_unresolved_ref: 1 (rows whose reference close could not be resolved from Yahoo at all - the base of the move is unverifiable, so the row is dropped rather than published with a '—' base)
- cross_region_rows_dropped: ['NEM@germany'] (the same name on a US venue and a foreign venue - the US row is kept so the name appears exactly once)
- us_premarket_check (Yahoo 1-min pre/post feed vs the screener pre-market column, base = the IMMEDIATELY prior session's close): checked=9 within_1pp=7 within_3pp=8 unavailable=1
  us_premarket outliers (>3pp; thin pre-market books, not a screener error): [{"symbol": "KYMR", "tv": 33.302, "yahoo": 23.259, "delta": 10.043, "yahoo_asof": "08:21"}]
- markets_with_lt5_rows: ['uk:less=3', 'france:less=2', 'netherlands:egreater=4', 'netherlands:less=0', 'belgium:egreater=4', 'belgium:less=0', 'portugal:egreater=0', 'portugal:less=0', 'ireland:egreater=0', 'ireland:less=1', 'italy:less=2', 'switzerland:egreater=2', 'switzerland:less=2', 'spain:egreater=2', 'spain:less=0', 'norway:less=4', 'denmark:less=0', 'finland:egreater=2', 'finland:less=3', 'poland:less=2', 'austria:egreater=3', 'austria:less=0', 'greece:egreater=0', 'greece:less=1', 'singapore:egreater=3', 'singapore:less=3', 'newzealand:egreater=0', 'ksa:egreater=3']
  NOTE: this fires per market AND direction, so it is NOT a coverage-failure signal on
  its own. A 'less' count of 0-3 means almost nothing fell more than 2.5% that session
  (a broad up-day); a small 'egreater' count usually means a small market with few
  names above the $1B market-cap floor. Check the median change before calling it a gap.
- filters: volume>10000 (removes stale-reference rows), country=home for EU/UK/AU,
  exchange drop-list for US, US venue allow-list, US preferred (slash ticker) excluded
- pass_b2 (US pre-market gap scan - "gapped today, flat yesterday"): candidates=169 deduped_against_pass_a_b=82 published=86 (up=163 down=6)
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
- bod_no_extended_hours: 36 (deferred to the next scan; not in the headline table)
- earnings_source: screener `earnings_release_date` (last FULL report) + `earnings_release_next_date` (next scheduled)
- earnings_caveat: `earnings_release_date` does NOT capture preliminary, guidance or
  restructuring releases. On 2026-10-23 LKQ fell 22.47% on a preliminary Q3 miss while
  the field still read 2026-07-30. ALWAYS confirm the earnings-driven flag against the
  headline itself; the calendar field is a screen, not a verdict.
- us_line_index: ok (US-listed lines for the 25 foreign home countries, both scanner types; the `US tradeable` column is ADR / US-listed / none)
- catalyst_note: Catalyst lookups: 3 US + 8 EU + 2 AU + 3 APAC/Gulf = 16 per run - the skill's cap, allocated by the evidence gap.
- catalyst_merge: region-matched - a row may only use a catalog entry from its OWN region;
  the same ticker on another venue is a different company and is not used.
- catalyst_budget: 3 US + 8 EU + 2 AU + 3 APAC/Gulf = 16 lookups per run (cap 16), allocated by the evidence gap: the US slice covers the rows whose earnings event can still explain today's move, the EU/AU/APAC floors are never squeezed because no bulk calendar reaches those markets, and whatever the US slice does not need goes to the region with the most unexplained rows
- earnings_calendar: Nasdaq public earnings calendar (calls=8 errors=0 symbols=463) - the source of record for the US earnings date, and the ranking key for the search budget
- earnings_field_stale_rows: 3 (the screener's earnings_release_date disagreed with the calendar; the calendar's date is published)
- earnings_field_stale_detail: [{"ticker": "SMTC", "screener": "2026-08-25", "calendar": "2026-11-23"}, {"ticker": "FLNC", "screener": "2026-08-05", "calendar": "2026-11-23"}, {"ticker": "HPE", "screener": "2026-09-02", "calendar": "2026-11-23"}]
- earnings_dates: the published `Last earnings` date by source - catalog (researched) 5, calendar 11, asx 0, screener 374. The chain is researched -> calendar (US) -> ASX feed (AU) -> the screener's field, which is the FALLBACK and the one that lags (2026-11-12: NBIS carried the previous quarter's date on the morning it reported, and MEKO, NORBT and FG carried July and August dates on the morning they all reported).
- asx_announcements: 3 results-classified announcement(s) for the last ASX session (calls=1 errors=0); the announcement date IS the report date, and the meeting/AGM/offer/assay headlines are excluded because they are not reports
- earnings_date_quality: 5 of 22 markets publish a FRESH earnings date (median age <= 14d); the table below gives each market's rows, the rows with NO date at all, the median age of the published date and the rows within 7 and 30 days - the reader sees the input quality instead of trusting it
| market | rows | no date | median age | <=7d | <=30d |
|---|---|---|---|---|---|
| au | 3 | 0 | 98d | 1 | 1 |
| austria | 2 | 0 | 458d | 1 | 1 |
| belgium | 1 | 0 | 88d | 0 | 0 |
| china | 3 | 1 | 942d | 0 | 0 |
| denmark | 1 | 0 | 5d | 1 | 1 |
| finland | 1 | 0 | 27d | 0 | 1 |
| france | 3 | 0 | 115d | 0 | 0 |
| germany | 2 | 0 | 13d | 0 | 2 |
| india | 2 | 1 | 28d | 0 | 1 |
| indonesia | 3 | 2 | 115d | 0 | 0 |
| ireland | 1 | 0 | 109d | 0 | 0 |
| italy | 2 | 0 | 117d | 0 | 0 |
| ksa | 3 | 2 | 15d | 0 | 1 |
| netherlands | 2 | 0 | 40d | 0 | 0 |
| newzealand | 3 | 0 | 7d | 2 | 2 |
| norway | 4 | 1 | 4d | 2 | 3 |
| poland | 2 | 0 | 4d | 2 | 2 |
| singapore | 3 | 0 | 103d | 0 | 0 |
| sweden | 4 | 0 | 18d | 1 | 3 |
| thailand | 3 | 3 | n/a | 0 | 0 |
| uk | 3 | 0 | 102d | 0 | 1 |
| us | 339 | 3 | 20d | 16 | 274 |
- earnings_tiers: fresh=3 near=0 (fresh = the report is dated on the scan date, near = the previous session)
- one_table_rule: each name appears exactly once, in exactly one table, with its
  catalyst in that row's last column. There is no separate catalysts section.
- data_date: US regular session close of the prior trading day; extended-hours columns
  carry the prior session's prints
- settlement_state: 23 settled, 28 live (a live row's move is a mid-session snapshot, not the session's result)
- rows_per_market (EU/UK, cap 4/market): {'sweden': 4, 'norway': 4, 'poland': 4, 'france': 4, 'germany': 4, 'uk': 4, 'ireland': 1, 'denmark': 4, 'austria': 3, 'netherlands': 4, 'italy': 4, 'finland': 4, 'belgium': 4, 'switzerland': 4, 'spain': 2, 'greece': 1} — the cap stops one thin market taking the table; the EU/UK table was 28% Sweden over nine runs (73 of 264 rows) while Belgium and Greece never appeared once.
- rows_per_market (APAC/Gulf, cap 3/market): {'indonesia': 3, 'india': 3, 'thailand': 3, 'china': 3, 'newzealand': 3, 'ksa': 3, 'singapore': 3}
- deprecations: mcp__tradingview-advanced__*, mcp__tradingview__*, mcp__financekit__*,
  mcp__stocktwits__* are ABSENT in Cloud sessions (tool_search 0 hits; connector catalog
  holds only media + credential tools). The public screener replaces them.

- degraded_sources: 2
  (the chat reply's `errors:` MUST equal this number - one entry per degraded
  source, not one per run)
  1. yahoo_chart_api.reference_close_unresolved — HCL-INSYS.BO: the reference close could not be resolved (429 or a bad body)
  2. yahoo_premarket_check.unavailable — COHU: Yahoo's 1-minute pre-market feed returned no usable print

## Audit line

`earnings-reaction target=earnings-reactions:2026-11-23 candidates=496 amc_reactions=0 pre_gaps=339 eu_reactions=28 asx_reactions=3 apac_reactions=20 catalyst_lookups=19 bod=36 pass_b2_candidates=169 pass_b2_dedup=82 pass_b2_published=86 earnings_calendar_rows=463 earnings_tiers_fresh=3 earnings_tiers_near=0 earnings_field_stale_rows=3 earnings_dates_catalog=5 earnings_dates_asx=0 asx_ann_rows=3 rows_dropped_stale_ref=3 rows_dropped_unresolved_ref=1 degraded_sources=2`
