# Earnings reaction scanner — 2026-11-27

- Cron: `0 8 * * 1-5` America/New_York (weekdays, 08:00 ET)
- Fire time (ET): 2026-11-27 08:10:47 Fri
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

- 0 AMC reactions, 231 pre-market gaps, 109 without extended-hours data; 29 EU/UK and 4 ASX movers, 20 APAC/Gulf movers.
- Pass B2 (the US pre-market gap scan) met the filter on 116 names (114 up, 2 down); 28 were already a Pass A/B row and are recorded as dedupes, and 88 reached a table.
- Biggest US extended-hours move: XP PRE_GAP (17.80%).
- Biggest EU/UK move: ELON (-11.80%, sweden).
- Biggest ASX move: WTC (+15.08%).
- Biggest APAC/Gulf move: NETV (+34.62%, indonesia).
- 1 of the 29 EU/UK rows are SETTLED and 28 are LIVE (mid-session). The 12:15 ET settlement pass publishes where those
  live moves actually closed.
- EU/AU/APAC earnings-driven tagging is keyword-based on headlines (best-effort). A row
  whose lookup was not performed carries NO verdict — only a researched row does.

## Actionable read

- **Move vs this name's own history.** The `Move vs avg daily` column divides the
  reaction by the name's own mean absolute daily move over its last
  20 completed sessions. A -27% move in a name that averages +-3% is a
  different event from a -8% move in a name that averages +-7%.
- **US-listed and tradeable vs foreign-only.** 246 published US rows are on a
  US venue; 1 more foreign reactions have a US ADR line
  (the `US tradeable` column carries the ticker); 29 are foreign-only and
  cannot be bought directly by a US reader.
- **Not yet fully priced — US (hypothesis, not a recommendation).**
  STNE — +14.12%, 2.37% mean absolute daily move over the last 20 completed sessions, 6.0x that average, reference close 7.48 dated 2026-11-24, US access: US-listed, the move now (+14.12%) is larger than the move it follows (+3.21%); the reaction is still being repriced. Hypothesis only: this artifact states no
  direction and no trade.
- **Not yet fully priced — EU/UK (hypothesis, not a recommendation).**
  DESN — +10.69%, 1.37% mean absolute daily move over the last 20 completed sessions, 7.8x that average, reference close 276.00 dated 2026-11-26, US access: none, the move now (+10.69%) is larger than the move it follows (-0.54%); the reaction is still being repriced. Hypothesis only: this artifact states no
  direction and no trade.
- **Not yet fully priced — AU (ASX) (hypothesis, not a recommendation).**
  WTC — +15.08%, 2.87% mean absolute daily move over the last 20 completed sessions, 5.3x that average, reference close 46.81 dated 2026-11-25, US access: none, the move now (+15.08%) is larger than the move it follows (+3.31%); the reaction is still being repriced. Hypothesis only: this artifact states no
  direction and no trade.

## US — Headline table

| Ticker | Venue | Close | Chg % | Pre-mkt % | Post-mkt % | Move vs avg daily | Ref close | Ref source | Ref asof | US tradeable | Last earnings | Tag | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| XP | NASDAQ | 14.39 | 5.19 | 17.80 | — | 5.5x | 13.68 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-16 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| INTR | NASDAQ | 4.01 | 5.25 | 14.21 | — | 5.1x | 3.81 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-12 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| STNE | NASDAQ | 7.72 | 3.21 | 14.12 | — | 6.0x | 7.48 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-12 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| VERA | NASDAQ | 29.5 | 1.76 | 14.00 | — | 4.1x | 28.99 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-05 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PICS | NASDAQ | 5.26 | 7.35 | 12.55 | — | 2.0x | 4.90 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-16 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PAGS | NYSE | 7.7 | 2.39 | 11.04 | — | 4.6x | 7.52 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-16 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AGLT | NASDAQ | 6.49 | 20.41 | 10.02 | — | 1.2x | 5.39 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-16 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AXTI | NASDAQ | 31.98 | 1.27 | 9.47 | — | 1.0x | 31.58 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-29 (29d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NU | NYSE | 12.36 | 4.22 | 9.47 | — | 3.0x | 11.86 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-12 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AAOI | NASDAQ | 37.02 | -3.59 | 9.24 | — | 1.1x | 38.40 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-05 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ALVO | NASDAQ | 4.21 | -0.71 | -9.03 | — | 2.5x | 4.24 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-11 (16d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AYA | NASDAQ | 19.86 | 5.69 | 8.76 | — | 1.8x | 18.79 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-12 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ASM | AMEX | 3.69 | 6.34 | 8.71 | — | 1.9x | 3.47 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-04 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| HYMC | NASDAQ | 13.72 | 6.60 | 8.60 | — | 1.5x | 12.87 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-27 (31d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SCZM | NASDAQ | 7.51 | 9.64 | 8.52 | — | 1.4x | 6.85 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-17 (10d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SERV | NASDAQ | 2.29 | 0.44 | 8.49 | — | 1.2x | 2.28 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-05 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GLXY | NASDAQ | 11.56 | 0.09 | 8.29 | — | 1.1x | 11.55 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-27 (31d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| UUUU | AMEX | 5.21 | 1.56 | 8.25 | — | 1.9x | 5.13 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-04 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NG | AMEX | 5.24 | 1.35 | 8.21 | — | 2.0x | 5.17 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-08 (50d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| COHR | NYSE | 196.19 | -0.03 | 8.06 | — | 1.1x | 196.24 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-04 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LITE | NASDAQ | 476.58 | -2.16 | 8.05 | — | 1.0x | 487.12 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-02 (25d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| EXK | NYSE | 6.14 | 6.23 | 7.98 | — | 1.6x | 5.78 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-09 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| IREN | NASDAQ | 12.85 | -0.77 | 7.94 | — | 0.8x | 12.95 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-05 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BTDR | NASDAQ | 3.05 | 9.71 | 7.87 | — | 0.7x | 2.78 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-10 (17d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| DC | AMEX | 3.61 | 0.84 | 7.76 | — | 1.4x | 3.58 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-10 (17d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CRML | NASDAQ | 2.84 | -11.80 | 7.75 | — | 1.1x | 3.22 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-09-25 (63d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LPTH | NASDAQ | 5.57 | 4.90 | 7.72 | — | 1.1x | 5.31 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-10 (17d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PURR | NASDAQ | 7.41 | -4.26 | 7.69 | — | 1.5x | 7.74 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-05 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MUX | NYSE | 9.39 | 5.03 | 7.67 | — | 1.5x | 8.94 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-09 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| VRTX | NASDAQ | 564.12 | 0.04 | -7.64 | — | 4.6x | 563.92 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-02 (25d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NBIS | NASDAQ | 84.99 | -2.66 | 7.54 | — | 0.8x | 87.31 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-12 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AUGO | NASDAQ | 62.94 | 3.74 | 7.53 | — | 1.3x | 60.67 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-05 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ACMR | NASDAQ | 40.28 | -0.15 | 7.50 | — | 1.2x | 40.34 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-05 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TTMI | NASDAQ | 58.17 | -2.10 | 7.44 | — | 1.0x | 59.42 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-22 (36d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SATL | NASDAQ | 2.525 | 1.00 | 7.33 | — | 1.1x | 2.50 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-10 (17d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AG | NYSE | 11.23 | 4.37 | 7.30 | — | 1.8x | 10.76 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-05 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| POET | NASDAQ | 3.58 | 0.00 | 7.26 | — | 0.9x | 3.58 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-16 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BE | NYSE | 152.89 | -2.25 | 7.26 | — | 1.0x | 156.41 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-22 (36d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AEHR | NASDAQ | 41.44 | -1.07 | 7.17 | — | 0.7x | 41.89 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-02 (25d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SHAZ | NASDAQ | 16.71 | -0.30 | 7.14 | — | 0.7x | 16.76 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-16 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| UAMY | NYSE | 2.21 | 1.38 | 7.08 | — | 1.0x | 2.18 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-12 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MXL | NASDAQ | 42.05 | 0.38 | 7.06 | — | 0.8x | 41.89 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-22 (36d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LUNR | NASDAQ | 9.14 | 2.35 | 7.05 | — | 0.9x | 8.93 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-12 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ALAB | NASDAQ | 190.34 | -0.50 | 7.03 | — | 0.9x | 191.30 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-03 (24d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SVM | AMEX | 6.85 | 3.63 | 7.01 | — | 1.6x | 6.61 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-05 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| DNA | NYSE | 7.17 | -4.65 | 6.95 | — | 0.9x | 7.52 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-05 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SA | NYSE | 18.99 | 4.05 | 6.90 | — | 1.2x | 18.25 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-13 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TGB | AMEX | 5.66 | 4.04 | 6.89 | — | 1.7x | 5.44 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-04 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PAX | NASDAQ | 9.35 | 2.75 | 6.84 | — | 3.0x | 9.10 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-03 (24d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMPX | NYSE | 5.69 | -0.52 | 6.82 | — | 1.1x | 5.72 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-10 (17d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MELI | NASDAQ | 1467.3 | 1.17 | 6.73 | — | 2.5x | 1450.31 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-04 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| APLD | NASDAQ | 12.29 | 0.57 | 6.66 | — | 0.8x | 12.22 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-07 (51d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ALM | NASDAQ | 6.78 | 0.15 | 6.64 | — | 1.4x | 6.77 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-12 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NVTS | NASDAQ | 6.8 | 4.45 | 6.62 | — | 0.8x | 6.51 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-03 (24d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MRVL | NASDAQ | 130.93 | -0.49 | 6.60 | — | 0.9x | 131.57 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-08-27 (92d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| WULF | NASDAQ | 10.03 | 0.20 | 6.56 | — | 0.9x | 10.01 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-06 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CIFR | NASDAQ | 5.51 | -0.18 | 6.53 | — | 0.8x | 5.52 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-02 (25d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ARIS | NYSE | 12.89 | 4.71 | 6.52 | — | 1.5x | 12.31 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-04 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| INFQ | NYSE | 6.49 | 2.37 | 6.47 | — | 1.0x | 6.34 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-16 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CDE | NYSE | 11.75 | 5.00 | 6.47 | — | 1.4x | 11.19 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-04 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SMR | NYSE | 3.25 | -1.52 | 6.46 | — | 1.1x | 3.30 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-05 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BW | NYSE | 3.74 | -2.09 | 6.42 | — | 0.8x | 3.82 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-09 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ONDS | NASDAQ | 3.9 | 0.26 | 6.41 | — | 0.9x | 3.89 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-12 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| OUST | NASDAQ | 25.77 | 3.12 | 6.40 | — | 0.9x | 24.99 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-03 (24d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| HL | NYSE | 11.28 | 3.49 | 6.39 | — | 1.4x | 10.90 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-03 (24d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PPTA | NASDAQ | 15.21 | 6.07 | 6.38 | — | 1.3x | 14.34 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-13 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| WDC | NASDAQ | 272.45 | -0.55 | 6.35 | — | 1.1x | 273.95 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-22 (36d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| STX | NASDAQ | 472.33 | -2.10 | 6.33 | — | 1.1x | 482.48 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-27 (31d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| VZLA | AMEX | 2.86 | 6.32 | 6.29 | — | 1.4x | 2.69 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-09-04 (84d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TSEM | NASDAQ | 121.74 | -1.40 | 6.27 | — | 0.9x | 123.47 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-02 (25d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| EGO | NYSE | 27.66 | 4.30 | 6.25 | — | 1.4x | 26.52 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-28 (30d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FLY | NASDAQ | 18.14 | -0.22 | 6.23 | — | 0.8x | 18.18 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-10 (17d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CRDO | NASDAQ | 106.795 | 0.31 | 6.21 | — | 0.8x | 106.46 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-09-01 (87d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| IAG | NYSE | 16 | 5.12 | 6.16 | — | 1.4x | 15.22 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-05 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| WOLF | NYSE | 17.94 | -1.43 | 6.13 | — | 0.9x | 18.20 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-04 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| EQX | AMEX | 9.07 | 3.42 | 6.12 | — | 1.5x | 8.77 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-09 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ASST | NASDAQ | 14.95 | 5.36 | 6.09 | — | 1.0x | 14.19 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-06 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TER | NASDAQ | 212.15 | -0.50 | 6.06 | — | 1.0x | 213.22 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-27 (31d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PAAS | NYSE | 32.56 | 4.80 | 6.05 | — | 1.6x | 31.07 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-04 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SSRM | NASDAQ | 23.39 | 3.68 | 6.03 | — | 1.6x | 22.56 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-03 (24d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| STLA | NYSE | 3.66 | 6.40 | 6.01 | — | 2.0x | 3.44 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-28 (30d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| QBTS | NASDAQ | 7 | 3.86 | 6.00 | — | 0.8x | 6.74 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-10 (17d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| HUT | NASDAQ | 48.83 | 1.22 | 5.98 | — | 0.7x | 48.24 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-04 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CLSK | NASDAQ | 5.18 | 1.27 | 5.97 | — | 0.8x | 5.12 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-24 (3d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-24 (Nasdaq earnings calendar; no headline lookup), consensus EPS ($0.36) |
| SMTC | NASDAQ | 92.93 | 7.48 | 5.88 | — | 0.7x | 86.46 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-23 (4d ago) | PRE_GAP | — | Q4 2026 results, report date 2026-11-23 (Nasdaq earnings calendar; no headline lookup), consensus EPS $0.92 |
| PL | NYSE | 10.61 | -0.28 | 5.86 | — | 1.1x | 10.64 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-09-03 (85d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| XE | NASDAQ | 8.22 | -4.75 | 5.84 | — | 0.9x | 8.63 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-12 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PENG | NASDAQ | 37.03 | -1.44 | 5.81 | — | 0.7x | 37.57 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-06 (52d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| UEC | AMEX | 5.69 | 2.15 | 5.80 | — | 1.2x | 5.57 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-09-29 (59d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SKE | NYSE | 25.93 | 3.84 | 5.78 | — | 1.5x | 24.97 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-16 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MU | NASDAQ | 601.25 | -4.53 | 5.78 | — | 0.9x | 629.79 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-09-30 (58d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| KGC | NYSE | 18.42 | 3.14 | 5.75 | — | 1.6x | 17.86 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-28 (30d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FPS | NYSE | 18.82 | 1.02 | 5.74 | — | 0.7x | 18.63 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-12 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FCEL | NASDAQ | 7.44 | 4.79 | 5.70 | — | 0.7x | 7.10 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-09-02 (86d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FSM | NYSE | 7.92 | 3.66 | 5.68 | — | 1.5x | 7.64 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-04 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LRCX | NASDAQ | 185.01 | -5.68 | 5.65 | — | 1.0x | 196.16 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-21 (37d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NNE | NASDAQ | 8.855 | 0.17 | 5.62 | — | 1.1x | 8.84 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-08-12 (107d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SEI | NYSE | 58.23 | 3.01 | 5.62 | — | 0.9x | 56.53 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-04 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CRWV | NASDAQ | 42.57 | -0.08 | 5.61 | — | 0.7x | 42.60 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-10 (17d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LWLG | NASDAQ | 2.69 | -2.89 | 5.58 | — | 0.7x | 2.77 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-10 (17d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| WYFI | NASDAQ | 6.5 | -3.49 | 5.54 | — | 0.6x | 6.74 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-10 (17d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BETA | NYSE | 16.4 | 4.73 | 5.54 | — | 0.9x | 15.66 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-03 (24d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMKR | NASDAQ | 32.02 | 0.66 | 5.53 | — | 0.9x | 31.81 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-26 (32d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CLS | NYSE | 191.95 | -2.39 | 5.50 | — | 1.0x | 196.64 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-26 (32d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AAUC | NYSE | 19.15 | 4.36 | 5.48 | — | 1.5x | 18.35 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-04 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| USAR | NASDAQ | 6.59 | -1.35 | 5.46 | — | 0.9x | 6.68 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-09 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AEM | NYSE | 161.2 | 3.03 | 5.46 | — | 1.5x | 156.46 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-28 (30d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CORZ | NASDAQ | 10.82 | -1.55 | 5.36 | — | 0.8x | 10.99 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-05 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| EROC | NYSE | 5.6 | -4.27 | 5.36 | — | 0.7x | 5.85 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-12 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FCX | NYSE | 48.55 | 1.72 | 5.36 | — | 1.4x | 47.73 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-27 (31d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMAT | NASDAQ | 311.18 | -3.89 | 5.31 | — | 1.0x | 323.76 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-12 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AGI | NYSE | 26.28 | 3.34 | 5.29 | — | 1.5x | 25.43 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-28 (30d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| VRT | NYSE | 173.37 | -0.26 | 5.25 | — | 0.9x | 173.82 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-28 (30d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RUM | NASDAQ | 3.525 | -6.37 | 5.25 | — | 1.0x | 3.77 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-11 (16d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CBRS | NASDAQ | 89.68 | 1.01 | 5.24 | — | 0.7x | 88.78 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-12 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MSTR | NASDAQ | 79.96 | 3.11 | 5.23 | — | 1.0x | 77.55 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-29 (29d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| WPM | NYSE | 122.6 | 5.15 | 5.18 | — | 1.4x | 116.60 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-05 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| OGC | NYSE | 24.72 | 4.83 | 5.18 | — | 1.4x | 23.58 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-04 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MARA | NASDAQ | 5.42 | 0.18 | 5.17 | — | 0.8x | 5.41 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-09 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| HOOD | NASDAQ | 65.78 | 0.20 | 5.16 | — | 1.3x | 65.65 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-27 (31d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BTG | AMEX | 4.48 | 3.94 | 5.13 | — | 1.2x | 4.31 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-04 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FLNC | NASDAQ | 4.72 | 15.12 | 5.12 | — | 0.7x | 4.10 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-23 (4d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-23 (Nasdaq earnings calendar; no headline lookup), consensus EPS ($0.54) |
| AU | NYSE | 77.94 | 2.20 | 5.11 | — | 1.3x | 76.26 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-05 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| OR | NYSE | 32.97 | 3.91 | 5.10 | — | 1.5x | 31.73 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-11 (16d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| OKLO | NYSE | 19.47 | 1.41 | 5.08 | — | 0.8x | 19.20 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-06 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BRUN | NASDAQ | 3.74 | -7.43 | 5.08 | — | 0.5x | 4.04 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-12 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SCCO | NYSE | 140.99 | 3.03 | 5.06 | — | 1.4x | 136.85 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-21 (37d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NXT | NASDAQ | 68.99 | 4.91 | 5.04 | — | 0.9x | 65.76 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-28 (30d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RKLB | NASDAQ | 47.02 | 2.26 | 5.04 | — | 0.8x | 45.98 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-09 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| DOCN | NYSE | 71.72 | -3.09 | 5.01 | — | 0.8x | 74.01 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-03 (24d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MKSI | NASDAQ | 183.82 | -3.92 | 4.99 | — | 0.9x | 191.32 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-04 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NEM | NYSE | 101.44 | 1.76 | 4.99 | — | 1.5x | 99.69 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-22 (36d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| OCUL | NASDAQ | 6.1 | -3.17 | 4.92 | — | 1.4x | 6.30 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-09 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| DIOD | NASDAQ | 75.7 | 4.40 | 4.89 | — | 0.8x | 72.51 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-05 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LBRT | NYSE | 11.92 | 6.14 | 4.87 | — | 0.9x | 11.23 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-21 (37d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| IONQ | NYSE | 23.54 | 5.09 | 4.84 | — | 0.7x | 22.40 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-05 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GLW | NYSE | 100.24 | -1.60 | 4.83 | — | 0.9x | 101.87 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-27 (31d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AADX | NYSE | 7.06 | 9.46 | 4.82 | — | 0.8x | 6.45 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-11 (16d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AVEX | NYSE | 12.41 | 8.01 | 4.75 | — | 0.6x | 11.49 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-11 (16d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SHLS | NASDAQ | 7.1 | 9.23 | 4.73 | — | 0.7x | 6.50 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-04 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FIGR | NASDAQ | 25.96 | 5.57 | 4.62 | — | 0.9x | 24.59 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-12 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NEXA | NYSE | 10.42 | 4.20 | 4.61 | — | 1.2x | 10.00 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-29 (29d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMD | NASDAQ | 406.03 | -1.75 | 4.59 | — | 0.6x | 413.27 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-03 (24d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| KLAC | NASDAQ | 134.2 | 0.41 | 4.58 | — | 0.9x | 133.65 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-28 (30d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LMND | NYSE | 37.99 | 5.73 | 4.53 | — | 1.0x | 35.93 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-05 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| QNT | NASDAQ | 32.49 | 7.12 | 4.46 | — | 0.6x | 30.33 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-05 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| INIO | NASDAQ | 12.985 | 8.21 | 4.43 | — | 0.7x | 12.00 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-27 (31d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ANET | NYSE | 163.99 | -2.71 | 4.40 | — | 0.8x | 168.56 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-03 (24d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PARR | NYSE | 59.62 | -5.30 | 4.33 | — | 1.7x | 62.96 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-03 (24d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SEDG | NASDAQ | 19.7 | 8.18 | 4.31 | — | 0.9x | 18.21 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-04 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MPC | NYSE | 346.27 | -2.50 | 4.26 | — | 1.7x | 355.16 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-03 (24d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| KEN | NYSE | 54.17 | -3.70 | 4.26 | — | 1.7x | 56.25 | yahoo_chart_daily | 2026-11-24 | US-listed | — | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SSMR | NYSE | 11.04 | 4.84 | 4.26 | — | 0.7x | 10.53 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-12 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| INTC | NASDAQ | 54.47 | -0.60 | 4.24 | — | 0.7x | 54.80 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-29 (29d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| APP | NASDAQ | 378.95 | -0.57 | 4.23 | — | 0.7x | 381.11 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-04 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LASR | NASDAQ | 34.26 | 4.90 | 4.20 | — | 0.6x | 32.66 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-05 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ABCL | NASDAQ | 10.59 | -3.29 | 4.06 | — | 0.9x | 10.95 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-09 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| DELL | NYSE | 297.06 | 0.60 | 4.02 | — | 0.6x | 295.28 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-24 (3d ago) | PRE_GAP | — | Q4 2026 results, report date 2026-11-24 (Nasdaq earnings calendar; no headline lookup), consensus EPS $6.55 |
| APH | NYSE | 73.08 | -0.53 | 4.00 | — | 1.1x | 73.47 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-28 (30d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ORCL | NYSE | 103.88 | -5.13 | 3.94 | — | 0.8x | 109.50 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-09-10 (78d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SHOP | NASDAQ | 133.4 | 0.82 | 3.86 | — | 1.0x | 132.31 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-03 (24d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMSC | NASDAQ | 21.23 | 5.41 | 3.82 | — | 0.8x | 20.14 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-04 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CLMT | NASDAQ | 27.1 | -4.38 | 3.80 | — | 0.9x | 28.34 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-06 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MOD | NYSE | 136.34 | 3.97 | 3.78 | — | 0.5x | 131.13 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-03 (24d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ADI | NASDAQ | 333.105 | 6.44 | 3.68 | — | 0.8x | 312.95 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-24 (3d ago) | PRE_GAP | — | Q4 2026 results, report date 2026-11-24 (Nasdaq earnings calendar; no headline lookup), consensus EPS $3.89 |
| ANT | NASDAQ | 82.79 | 1.08 | 3.67 | — | 0.8x | 81.91 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-02 (25d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ETN | NYSE | 317.81 | -0.46 | 3.57 | — | 0.9x | 319.27 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-03 (24d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| RIG | NYSE | 5.03 | 4.14 | 3.38 | — | 0.9x | 4.83 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-02 (25d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BTU | NYSE | 16.45 | 5.92 | 3.34 | — | 0.9x | 15.53 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-04 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SNPS | NASDAQ | 405.09 | -2.35 | 3.34 | — | 1.4x | 414.82 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-08-26 (93d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SPCX | NASDAQ | 127.44 | 1.30 | 3.29 | — | 0.9x | 125.81 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-20 (38d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| WFRD | NASDAQ | 77.45 | 3.90 | 3.28 | — | 1.5x | 74.54 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-20 (38d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PWR | NYSE | 565.47 | -4.10 | 3.28 | — | 0.7x | 589.64 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-29 (29d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AGRO | NYSE | 8.08 | 4.26 | 3.22 | — | 1.2x | 7.75 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-11 (16d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GEV | NYSE | 715 | -0.78 | 3.22 | — | 0.8x | 720.65 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-28 (30d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| META | NASDAQ | 609.89 | 3.40 | 3.18 | — | 1.3x | 589.82 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-21 (37d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| QCOM | NASDAQ | 168.66 | 2.24 | 3.17 | — | 0.8x | 164.96 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-04 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CAI | NASDAQ | 17.84 | -3.88 | 3.14 | — | 0.6x | 18.56 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-04 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AGX | NYSE | 283.18 | 4.46 | 3.11 | — | 0.6x | 271.10 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-09-02 (86d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CDNS | NASDAQ | 294.89 | -0.58 | 3.09 | — | 1.1x | 296.60 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-26 (32d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CDLR | NYSE | 5.52 | -4.17 | 3.08 | — | 0.4x | 5.76 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-23 (4d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| IBKR | NASDAQ | 74.74 | 0.04 | 3.08 | — | 1.0x | 74.71 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-15 (43d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CVI | NYSE | 30.43 | -3.34 | 3.06 | — | 0.7x | 31.48 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-03 (24d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AVGO | NASDAQ | 300.86 | -0.07 | 3.04 | — | 0.7x | 301.08 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-09-02 (86d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| DDOG | NASDAQ | 158.25 | -4.31 | 2.98 | — | 0.7x | 165.38 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-04 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GPGI | NYSE | 15.25 | 4.81 | 2.95 | — | 0.7x | 14.55 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-05 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NVDA | NASDAQ | 149.3 | -3.91 | 2.93 | — | 0.5x | 155.38 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-17 (10d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TPL | NYSE | 261.37 | 3.97 | 2.92 | — | 1.1x | 251.40 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-04 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| OSCR | NYSE | 27.12 | 4.07 | 2.84 | — | 0.7x | 26.06 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-05 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CEG | NASDAQ | 235.28 | -3.90 | 2.77 | — | 0.8x | 244.84 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-09 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CAT | NYSE | 543.69 | 0.57 | 2.76 | — | 0.9x | 540.63 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-29 (29d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| QXO | NYSE | 11.97 | 8.62 | 2.76 | — | 0.6x | 11.02 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-12 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ASTS | NASDAQ | 26.02 | 10.25 | 2.73 | — | 0.3x | 23.60 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-09 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NET | NYSE | 283.3 | -1.39 | 2.71 | — | 0.6x | 287.29 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-05 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SNOW | NYSE | 267.72 | -1.24 | 2.71 | — | 0.8x | 271.09 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-09-02 (86d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PLTR | NASDAQ | 163.59 | 1.50 | 2.70 | — | 0.8x | 161.18 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-02 (25d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ATI | NYSE | 175.33 | 3.72 | 2.66 | — | 0.7x | 169.04 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-29 (29d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MS | NYSE | 167.55 | -0.73 | 2.63 | — | 1.2x | 168.79 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-14 (44d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LQDA | NASDAQ | 56.28 | -4.06 | 2.61 | — | 0.7x | 58.66 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-10 (17d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AXON | NASDAQ | 343.05 | 7.43 | 2.61 | — | 0.6x | 319.32 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-05 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GOOGL | NASDAQ | 273.1 | -2.13 | 2.59 | — | 1.4x | 279.05 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-28 (30d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMBA | NASDAQ | 35.68 | -19.77 | 2.58 | — | 0.4x | 44.47 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-24 (3d ago) | PRE_GAP | — | Q4 2026 results, report date 2026-11-24 (Nasdaq earnings calendar; no headline lookup), consensus EPS ($0.17) |
| TXN | NASDAQ | 270.19 | 4.55 | 2.56 | — | 0.6x | 258.44 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-21 (37d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CSCO | NASDAQ | 94.2 | 0.22 | 2.55 | — | 0.9x | 93.99 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-12 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| DK | NYSE | 52.87 | -4.22 | 2.53 | — | 0.8x | 55.20 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-06 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| VLO | NYSE | 323 | -0.51 | 2.53 | — | 1.0x | 324.67 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-22 (36d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CNQ | NYSE | 45.56 | 1.74 | 2.52 | — | 1.3x | 44.78 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-05 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PSX | NYSE | 236.08 | -0.37 | 2.50 | — | 1.3x | 236.95 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-28 (30d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| OLED | NASDAQ | 84.71 | 4.17 | 2.48 | — | 1.1x | 81.32 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-28 (30d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TSLA | NASDAQ | 380.14 | -1.18 | 2.45 | — | 0.8x | 384.68 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-21 (37d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GS | NYSE | 801.03 | -0.62 | 2.44 | — | 1.0x | 806.02 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-13 (45d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| DFTX | NASDAQ | 31.09 | -3.54 | 2.43 | — | 0.5x | 32.23 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-09 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| VET | NYSE | 10.4 | 3.69 | 2.40 | — | 0.8x | 10.03 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-04 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMZN | NASDAQ | 244.43 | -3.12 | 2.38 | — | 1.0x | 252.29 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-29 (29d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PANW | NASDAQ | 356.14 | 0.89 | -2.37 | — | 0.7x | 352.99 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-18 (9d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GCT | NASDAQ | 61.71 | 4.66 | 2.33 | — | 0.5x | 58.96 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-05 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| WMB | NYSE | 66.45 | 0.68 | 2.33 | — | 1.2x | 66.00 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-02 (25d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SAIL | NASDAQ | 22.87 | 4.05 | 2.32 | — | 0.6x | 21.98 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-09-09 (79d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GENI | NYSE | 5.67 | 9.46 | 2.29 | — | 0.5x | 5.18 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-05 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NTNX | NASDAQ | 46.3 | -15.19 | 2.28 | — | 0.7x | 54.59 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-24 (3d ago) | PRE_GAP | — | Q4 2026 results, report date 2026-11-24 (Nasdaq earnings calendar; no headline lookup), consensus EPS $0.29 |
| GOOG | NASDAQ | 270.98 | -2.02 | 2.27 | — | 1.3x | 276.58 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-28 (30d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| JCI | NYSE | 136.5 | -0.39 | 2.26 | — | 0.8x | 137.04 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-27 (31d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LIF | NASDAQ | 38.93 | -3.65 | 2.23 | — | 0.7x | 40.41 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-09 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AROC | NYSE | 26.88 | 3.86 | 2.23 | — | 0.7x | 25.88 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-02 (25d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GOLD | NYSE | 38.85 | 5.11 | 2.19 | — | 0.7x | 36.96 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-04 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| C | NYSE | 113.33 | -0.46 | 2.15 | — | 1.3x | 113.85 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-13 (45d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MRNA | NASDAQ | 220.84 | -2.88 | 2.11 | — | 0.5x | 227.38 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-06 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MO | NYSE | 76.28 | 1.95 | -2.05 | — | 1.8x | 74.82 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-10-29 (29d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CRK | NYSE | 12.75 | 5.55 | 2.04 | — | 0.6x | 12.08 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-04 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| IBRX | NASDAQ | 5.645 | -5.92 | 2.04 | — | 0.4x | 6.00 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-09 (18d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LB | NYSE | 74.63 | 6.04 | 2.01 | — | 0.6x | 70.38 | yahoo_chart_daily | 2026-11-24 | US-listed | 2026-11-04 (23d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |

## US — QUIET one-liners

| Ticker | Venue | Chg % | Pre-mkt % | Post-mkt % | Move vs avg daily | Ref close | Ref source | Ref asof | US tradeable | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|
| RBLX | NYSE | 4.00 | 1.96 | — | 0.8x | 53.49 | yahoo_chart_daily | 2026-11-24 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| AMLX | NASDAQ | 4.29 | 1.94 | — | 1.2x | 29.58 | yahoo_chart_daily | 2026-11-24 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| PH | NYSE | -0.92 | 1.90 | — | 0.4x | 906.24 | yahoo_chart_daily | 2026-11-24 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| TT | NYSE | -0.25 | 1.86 | — | 0.1x | 404.49 | yahoo_chart_daily | 2026-11-24 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| COP | NYSE | 0.28 | 1.84 | — | 0.2x | 134.64 | yahoo_chart_daily | 2026-11-24 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| NOW | NYSE | 0.46 | 1.83 | — | 0.2x | 91.74 | yahoo_chart_daily | 2026-11-24 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| CRSP | NASDAQ | -3.49 | 1.83 | — | 1.0x | 44.10 | yahoo_chart_daily | 2026-11-24 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| MSFT | NASDAQ | -1.25 | 1.82 | — | 0.6x | 496.13 | yahoo_chart_daily | 2026-11-24 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| NEOG | NASDAQ | -3.76 | -1.81 | — | 1.6x | 10.90 | yahoo_chart_daily | 2026-11-24 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| WHR | NYSE | 5.73 | 1.81 | — | 1.6x | 25.67 | yahoo_chart_daily | 2026-11-24 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| SLS | NASDAQ | -3.62 | 1.80 | — | 0.3x | 13.25 | yahoo_chart_daily | 2026-11-24 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| PATH | NYSE | 3.67 | 1.77 | — | 1.4x | 11.98 | yahoo_chart_daily | 2026-11-24 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| NEO | NASDAQ | -3.09 | 1.76 | — | 1.3x | 15.21 | yahoo_chart_daily | 2026-11-24 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| DKNG | NASDAQ | 9.56 | 1.76 | — | 2.5x | 16.11 | yahoo_chart_daily | 2026-11-24 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| DASH | NASDAQ | 3.92 | 1.74 | — | 1.3x | 160.13 | yahoo_chart_daily | 2026-11-24 | US-listed | — | no catalyst lookup (outside the per-run budget) |

## EU/UK — Headline table

| Ticker | Market | Venue | Close | Chg % | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | Session asof | Settle | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ELON | sweden | OMXSTO | 65.8 | -11.80 | SEK | 2.9x | 74.60 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | live | none | 2026-11-18 (9d ago) | N | no fresh catalyst found; the last release was the Q3 interim report (reported 2026-11-18) |
| DESN | switzerland | SIX | 305.5 | +10.69 | CHF | 7.8x | 276.00 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | live | none | — | — | no catalyst lookup (outside the per-run budget) |
| MDV | poland | GPW | 133.9 | +10.66 | PLN | 4.2x | 121.00 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | live | none | 2026-11-27 (0d ago) | Y | Q3 2026/27 results: revenue PLN 3.207bn (+11% y/y), adjusted EBITDA +48%, plus Nov 1-25 sales +34% y/y (reported 2026-11-27) |
| LMGAB | sweden | OMXSTO | 53.1 | +10.63 | SEK | 7.2x | 48.00 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | live | none | 2026-10-30 (28d ago) | — | no catalyst lookup (outside the per-run budget) |
| VER | sweden | OMXSTO | 7.66 | +9.43 | SEK | 2.6x | 7.00 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | live | none | 2026-11-23 (4d ago) | — | no catalyst lookup (outside the per-run budget) |
| SILEX | sweden | OMXSTO | 157.5 | +9.00 | SEK | 2.4x | 144.50 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | live | US line (OTC:SILXF) | 2026-11-04 (23d ago) | — | pending catalyst lookup |
| ATS | austria | VIE | 105.2 | +8.12 | EUR | 1.3x | 97.30 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | live | none | 2026-11-05 (22d ago) | N | CEO Mertin says on Bloomberg TV (2026-11-25) the company is weighing a US or Asia listing, blaming thin Vienna liquidity |
| ELG | germany | XETR | 107 | +7.97 | EUR | 2.1x | 99.10 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | live | none | 2026-11-10 (17d ago) | N | no fresh catalyst found - European chip stocks are rebounding; no ELG release today |
| IQMX | finland | OMXHEX | 7.32 | +7.96 | EUR | 1.5x | 6.78 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | live | none | 2026-11-05 (22d ago) | — | no catalyst lookup (outside the per-run budget) |
| BITTI | finland | OMXHEX | 35.95 | +7.63 | EUR | 2.3x | 33.40 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | live | none | 2026-10-29 (29d ago) | N | Nasdaq adds Bittium to the OMX Helsinki Benchmark index effective 2026-12-01 (announced 2026-11-23) |
| BEKB | belgium | EURONEXT | 42.45 | +7.60 | EUR | 5.3x | 39.45 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | live | none | 2026-11-27 (0d ago) | Y | Q3 2026 trading update: sales EUR 987m (+12%, +8% like-for-like), FY26 sales outlook raised above FY2025, new EUR 100m buyback (reported 2026-11-27) |
| DFENS | norway | OSL | 12.8 | +7.56 | NOK | 5.8x | 11.90 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | live | none | 2026-11-26 (1d ago) | — | no catalyst lookup (outside the per-run budget) |
| AMBU_B | denmark | OMXCOP | 93.2 | +7.31 | DKK | 5.1x | 86.85 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | live | US line (OTC:AMBFF) | 2026-11-05 (22d ago) | N | Nordea raises to Buy (PT DKK 110) and J.P. Morgan raises to Overweight (PT DKK 131) on the morning of 2026-11-27 |
| KOMPL | norway | OSL | 6.96 | +7.08 | NOK | 2.5x | 6.50 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | live | none | 2026-10-22 (36d ago) | N | no fresh catalyst found |
| DIA | poland | GPW | 145.2 | -6.92 | PLN | 6.5x | 156.00 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | live | none | 2026-11-26 (1d ago) | — | no catalyst lookup (outside the per-run budget) |
| CRNA | norway | OSL | 9.16 | -6.82 | NOK | 3.6x | 9.83 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | live | none | — | — | no catalyst lookup (outside the per-run budget) |
| FCT | italy | MIL | 12.225 | +6.77 | EUR | 2.9x | 11.45 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | live | none | 2026-07-29 (121d ago) | — | no catalyst lookup (outside the per-run budget) |
| CRI | poland | GPW | 683 | +6.55 | PLN | 2.2x | 641.00 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | live | none | 2026-11-26 (1d ago) | — | no catalyst lookup (outside the per-run budget) |
| EXENS | france | EURONEXT | 54.35 | +6.46 | EUR | 3.0x | 51.05 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | live | none | 2026-07-28 (122d ago) | — | pending catalyst lookup |
| OHB | germany | XETR | 204 | +6.14 | EUR | 1.6x | 192.20 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | live | US line (OTC:OHBTF) | 2026-11-12 (15d ago) | — | no catalyst lookup (outside the per-run budget) |
| S92 | germany | XETR | 46.76 | +5.89 | EUR | 1.6x | 44.16 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | live | none | 2026-11-12 (15d ago) | — | no catalyst lookup (outside the per-run budget) |
| HAG | germany | XETR | 83.82 | +5.59 | EUR | 2.5x | 79.38 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | live | none | 2026-11-05 (22d ago) | — | no catalyst lookup (outside the per-run budget) |
| BMA | norway | OSL | 23 | +5.50 | NOK | 3.1x | 21.80 | yahoo_chart_daily | 2026-11-25 | 2026-11-26 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| SENSO | finland | OMXHEX | 19.5 | +5.29 | EUR | 1.7x | 18.52 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | live | none | 2026-09-03 (85d ago) | — | no catalyst lookup (outside the per-run budget) |
| SOI | france | EURONEXT | 95.72 | +5.23 | EUR | 0.8x | 90.96 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | live | none | 2026-11-18 (9d ago) | — | no catalyst lookup (outside the per-run budget) |
| ENT | uk | LSE | 477.8 | +5.15 | GBX | 2.8x | 454.40 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | live | none | 2026-08-13 (106d ago) | — | no catalyst lookup (outside the per-run budget) |
| METSO | finland | OMXHEX | 15.06 | +5.09 | EUR | 2.2x | 14.33 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | live | ADR (OTC:OUKPY) | 2026-10-22 (36d ago) | N | Metals Focus Minerals 260 advances a Western Australia gold project (2026-11-27); no Metso release today |
| HOC | uk | LSE | 419 | +4.70 | GBX | 1.2x | 400.20 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | live | none | 2026-08-26 (93d ago) | — | no catalyst lookup (outside the per-run budget) |
| MRL | spain | BME | 11.86 | +4.49 | EUR | 2.8x | 11.35 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | live | none | 2026-11-11 (16d ago) | — | no catalyst lookup (outside the per-run budget) |

## AU (ASX) — Headline table

| Ticker | Venue | Close | Chg % | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | Session asof | Settle | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| WTC | ASX | 53.87 | +15.08 | AUD | 5.3x | 46.81 | yahoo_chart_daily | 2026-11-25 | 2026-11-27 | settled | none | 2026-08-25 (94d ago) | N | 2026 AGM addresses and FY27 trading update: CargoWise revenue +11% y/y to October, and the low end of the FY27 revenue range is now in sight (2026-11-27) |
| NEU | ASX | 18.73 | -12.15 | AUD | 4.0x | 21.32 | yahoo_chart_daily | 2026-11-25 | 2026-11-27 | settled | none | 2026-08-24 (95d ago) | — | no catalyst lookup (outside the per-run budget) |
| 4DX | ASX | 2.32 | +11.00 | AUD | 2.3x | 2.09 | yahoo_chart_daily | 2026-11-25 | 2026-11-27 | settled | none | 2026-08-27 (92d ago) | — | no catalyst lookup (outside the per-run budget) |
| SKS | ASX | 5.41 | +10.41 | AUD | 2.5x | 4.90 | yahoo_chart_daily | 2026-11-25 | 2026-11-27 | settled | none | 2026-08-18 (101d ago) | N | no fresh catalyst found - no ASX release today; the last releases were the 2026 AGM presentation and CEO address (2026-11-26) |

## APAC/Gulf — Headline table

| Ticker | Market | Venue | Close | Chg % | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | Session asof | Settle | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NETV | indonesia | IDX | 35 | +34.62 | IDR | 7.5x | 26.00 | yahoo_chart_daily | 2026-11-25 | 2026-11-26 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| PSDN | indonesia | IDX | 141 | +34.29 | IDR | 8.0x | 105.00 | yahoo_chart_daily | 2026-11-25 | 2026-11-26 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| SOSS | indonesia | IDX | 730 | +24.79 | IDR | 5.9x | 585.00 | yahoo_chart_daily | 2026-11-25 | 2026-11-26 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| 300663 | china | SZSE | 6.64 | +20.07 | CNY | 5.7x | 5.53 | yahoo_chart_daily | 2026-11-25 | 2026-11-26 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| 300324 | china | SZSE | 6.05 | +20.04 | CNY | 2.7x | 5.04 | yahoo_chart_daily | 2026-11-25 | 2026-11-26 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| 688371 | china | SSE | 18.4 | +20.03 | CNY | 2.5x | 15.33 | yahoo_chart_daily | 2026-11-25 | 2026-11-26 | settled | none | 2023-08-23 (1192d ago) | — | no catalyst lookup (outside the per-run budget) |
| GOYALALUM | india | NSE | 6.9 | +20.00 | INR | 8.7x | 5.75 | yahoo_chart_daily | 2026-11-25 | 2026-11-26 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| SOLARWORLD | india | NSE | 121.56 | +20.00 | INR | 5.7x | 101.30 | yahoo_chart_daily | 2026-11-25 | 2026-11-26 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| WAAREERTL | india | NSE | 825.7 | +20.00 | INR | 7.9x | 688.10 | yahoo_chart_daily | 2026-11-25 | 2026-11-26 | settled | none | 2026-10-19 (39d ago) | N | Letter of Award for a 120 MWp turnkey solar project (module supply plus EPC), received after the 2026-11-26 close, value undisclosed |
| 9517 | ksa | TADAWUL | 12.52 | -10.57 | SAR | 3.9x | 14.00 | yahoo_chart_daily | 2026-11-25 | 2026-11-26 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| SKN | thailand | SET | 4.82 | -9.74 | THB | 4.6x | 5.34 | yahoo_chart_daily | 2026-11-25 | 2026-11-26 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| GTK | newzealand | NZX | 5.02 | +8.89 | NZD | 2.2x | 4.61 | yahoo_chart_daily | 2026-11-25 | 2026-11-26 | settled | none | 2026-11-22 (5d ago) | — | no catalyst lookup (outside the per-run budget) |
| SIMAT | thailand | SET | 1.43 | +8.33 | THB | 3.6x | 1.32 | yahoo_chart_daily | 2026-11-25 | 2026-11-26 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| MGC | thailand | SET | 5.54 | +8.20 | THB | 2.8x | 5.12 | yahoo_chart_daily | 2026-11-25 | 2026-11-26 | settled | none | 2026-11-10 (17d ago) | N | no fresh catalyst found - the last release was the Q3 2026 report, net profit THB 320m (+26.4% y/y) (reported 2026-11-10) |
| MIM | singapore | SGX | 1.27 | +5.83 | SGD | 0.7x | 1.20 | yahoo_chart_daily | 2026-11-25 | 2026-11-26 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| 2200 | ksa | TADAWUL | 4.57 | +5.30 | SAR | 3.3x | 4.34 | yahoo_chart_daily | 2026-11-25 | 2026-11-26 | settled | none | 2026-08-06 (113d ago) | — | no catalyst lookup (outside the per-run budget) |
| F9D | singapore | SGX | 1.66 | +5.06 | SGD | 2.3x | 1.58 | yahoo_chart_daily | 2026-11-25 | 2026-11-26 | settled | none | 2026-11-10 (17d ago) | — | no catalyst lookup (outside the per-run budget) |
| EB5 | singapore | SGX | 2.82 | +4.06 | SGD | 1.1x | 2.71 | yahoo_chart_daily | 2026-11-25 | 2026-11-26 | settled | none | 2026-08-13 (106d ago) | — | no catalyst lookup (outside the per-run budget) |
| FCG | newzealand | NZX | 5.31 | +3.91 | NZD | 2.5x | 5.11 | yahoo_chart_daily | 2026-11-25 | 2026-11-26 | settled | none | 2026-03-23 (249d ago) | — | no catalyst lookup (outside the per-run budget) |
| SKL | newzealand | NZX | 7.64 | -2.92 | NZD | 1.8x | 7.87 | yahoo_chart_daily | 2026-11-25 | 2026-11-26 | settled | none | 2026-08-20 (99d ago) | N | no fresh catalyst found - no NZ disclosure since the FY26 result |

## Source health

- scanner_calls: 57 | scanner_errors: 0
- markets_scanned: US + 17 EU/UK + ASX + 7 APAC/Gulf (india, thailand, indonesia, china, singapore, newzealand, ksa)
- pipeline_version: 2026-11-20.1
- et_clock: zoneinfo America/New_York (DST-aware; a fixed UTC-4 mislabels every winter fire)
- premarket_window: 04:00-09:30 ET, resolved with zoneinfo (09:00-14:30 UTC in winter, 08:00-13:30 UTC in summer)
- session_selection: by DATE and order, never by a modal time-of-day. Yahoo stamps a daily bar at the session open, so the ET stamp of the SAME session shifts by one hour across a DST boundary; a modal filter kept the OLDER bars and discarded the NEWEST ones, which rolled the base back to the prior-prior session (66 US + 21 ASX rows lost on 2026-11-03, 24 of 25 ASX rows lost on 2026-11-04).
- yahoo_calls: 312 | yahoo_429: 0 | yahoo_errors: 0 | yahoo_breaker: closed
- reference_close (screener vs Yahoo, resolved BEFORE the tables were built): agree=299 mismatch=3 unverified=0 stale_reference=3
  method: the screener's implied reference close (close / (1 + change/100)) is compared
  with Yahoo's own reference close. A match proves the move was measured against the
  TRUE prior close; a mismatch means the row sits on a STALE reference (phantom move).
  Coverage: every row of the US headline, US QUIET, EU/UK and ASX tables is checked.
  Yahoo bar mode: {"closed": 271, "live": 28} (closed = last completed session bar;
  live = in-progress EU/UK session bar, which is what a weekday 08:00 ET EU move needs)
  live drift between the screener snapshot and the later Yahoo print: median=0.00pp max=3.54pp (expected on a live market)
- cross_check mismatches: [{"region": "US", "symbol": "SNDK", "tv": -5.568, "yahoo": -22.019, "delta": 16.451, "ref_delta_pct": -17.421, "tv_implied_ref": 77.95, "yahoo_ref": 94.395, "yahoo_date": "2026-11-25", "yahoo_ref_date": "2026-11-19", "verdict": "stale_reference"}, {"region": "poland", "symbol": "KGH.WA", "tv": 7.336, "yahoo": 6.64, "delta": 0.696, "ref_delta_pct": -2.71, "tv_implied_ref": 235.15, "yahoo_ref": 241.7, "yahoo_date": "2026-11-23", "yahoo_ref_date": "2026-11-20", "verdict": "stale_reference"}, {"region": "ksa", "symbol": "6022.SR", "tv": 4.815, "yahoo": 4.14, "delta": 0.675, "ref_delta_pct": -0.644, "tv_implied_ref": 54.0, "yahoo_ref": 54.35, "yahoo_date": "2026-11-26", "yahoo_ref_date": "2026-11-19", "verdict": "stale_reference"}]
- rows_dropped_stale_ref: 3 (rows whose screener-implied reference close disagreed with Yahoo's by more than 0.5%; they are dropped, not published)
- rows_dropped_unresolved_ref: 0 (rows whose reference close could not be resolved from Yahoo at all - the base of the move is unverifiable, so the row is dropped rather than published with a '—' base)
- us_premarket_check (Yahoo 1-min pre/post feed vs the screener pre-market column, base = the IMMEDIATELY prior session's close): checked=0 within_1pp=0 within_3pp=0 unavailable=10
- markets_with_lt5_rows: ['uk:less=0', 'germany:less=2', 'france:less=3', 'netherlands:less=0', 'belgium:egreater=4', 'belgium:less=0', 'portugal:egreater=0', 'portugal:less=0', 'ireland:egreater=0', 'ireland:less=0', 'italy:less=0', 'switzerland:less=1', 'spain:egreater=4', 'spain:less=0', 'sweden:less=4', 'norway:less=1', 'denmark:less=0', 'finland:less=0', 'poland:less=2', 'austria:less=0', 'greece:egreater=2', 'greece:less=0', 'singapore:less=0', 'newzealand:egreater=2', 'newzealand:less=2']
  NOTE: this fires per market AND direction, so it is NOT a coverage-failure signal on
  its own. A 'less' count of 0-3 means almost nothing fell more than 2.5% that session
  (a broad up-day); a small 'egreater' count usually means a small market with few
  names above the $1B market-cap floor. Check the median change before calling it a gap.
- filters: volume>10000 (removes stale-reference rows), country=home for EU/UK/AU,
  exchange drop-list for US, US venue allow-list, US preferred (slash ticker) excluded
- pass_b2 (US pre-market gap scan - "gapped today, flat yesterday"): candidates=116 deduped_against_pass_a_b=28 published=88 (up=114 down=2)
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
- bod_no_extended_hours: 109 (deferred to the next scan; not in the headline table)
- earnings_source: screener `earnings_release_date` (last FULL report) + `earnings_release_next_date` (next scheduled)
- earnings_caveat: `earnings_release_date` does NOT capture preliminary, guidance or
  restructuring releases. On 2026-10-23 LKQ fell 22.47% on a preliminary Q3 miss while
  the field still read 2026-07-30. ALWAYS confirm the earnings-driven flag against the
  headline itself; the calendar field is a screen, not a verdict.
- us_line_index: ok (US-listed lines for the 25 foreign home countries, both scanner types; the `US tradeable` column is ADR / US-listed / none)
- catalyst_note: Catalyst lookups: 0 US + 11 EU + 2 AU + 3 APAC/Gulf = 16 per run - the skill's cap, allocated by the evidence gap.
- catalyst_merge: region-matched - a row may only use a catalog entry from its OWN region;
  the same ticker on another venue is a different company and is not used.
- catalyst_budget: 0 US + 11 EU + 2 AU + 3 APAC/Gulf = 16 lookups per run (cap 16), allocated by the evidence gap: the US slice covers the rows whose earnings event can still explain today's move, the EU/AU/APAC floors are never squeezed because no bulk calendar reaches those markets, and whatever the US slice does not need goes to the region with the most unexplained rows
- earnings_calendar: Nasdaq public earnings calendar (calls=8 errors=0 symbols=155) - the source of record for the US earnings date, and the ranking key for the search budget
- earnings_field_stale_rows: 0 (the screener's earnings_release_date disagreed with the calendar; the calendar's date is published)
- earnings_dates: the published `Last earnings` date by source - catalog (researched) 11, calendar 7, asx 0, screener 266. The chain is researched -> calendar (US) -> ASX feed (AU) -> the screener's field, which is the FALLBACK and the one that lags (2026-11-12: NBIS carried the previous quarter's date on the morning it reported, and MEKO, NORBT and FG carried July and August dates on the morning they all reported).
- asx_announcements: 6 results-classified announcement(s) for the last ASX session (calls=1 errors=0); the announcement date IS the report date, and the meeting/AGM/offer/assay headlines are excluded because they are not reports
- earnings_date_quality: 2 of 22 markets publish a FRESH earnings date (median age <= 14d); the table below gives each market's rows, the rows with NO date at all, the median age of the published date and the rows within 7 and 30 days - the reader sees the input quality instead of trusting it
| market | rows | no date | median age | <=7d | <=30d |
|---|---|---|---|---|---|
| au | 4 | 0 | 95d | 0 | 0 |
| austria | 1 | 0 | 22d | 0 | 1 |
| belgium | 1 | 0 | 0d | 1 | 1 |
| china | 3 | 2 | 1192d | 0 | 0 |
| denmark | 1 | 0 | 22d | 0 | 1 |
| finland | 4 | 0 | 36d | 0 | 2 |
| france | 2 | 0 | 122d | 0 | 1 |
| germany | 4 | 0 | 17d | 0 | 4 |
| india | 3 | 2 | 39d | 0 | 0 |
| indonesia | 3 | 3 | n/a | 0 | 0 |
| italy | 1 | 0 | 121d | 0 | 0 |
| ksa | 2 | 1 | 113d | 0 | 0 |
| newzealand | 3 | 0 | 99d | 1 | 1 |
| norway | 4 | 2 | 36d | 1 | 1 |
| poland | 3 | 0 | 1d | 3 | 3 |
| singapore | 3 | 1 | 106d | 0 | 1 |
| spain | 1 | 0 | 16d | 0 | 1 |
| sweden | 4 | 0 | 23d | 1 | 4 |
| switzerland | 1 | 1 | n/a | 0 | 0 |
| thailand | 3 | 2 | 17d | 0 | 1 |
| uk | 2 | 0 | 106d | 0 | 0 |
| us | 231 | 1 | 23d | 8 | 182 |
- earnings_tiers: fresh=0 near=0 (fresh = the report is dated on the scan date, near = the previous session)
- one_table_rule: each name appears exactly once, in exactly one table, with its
  catalyst in that row's last column. There is no separate catalysts section.
- data_date: US regular session close of the prior trading day; extended-hours columns
  carry the prior session's prints
- settlement_state: 25 settled, 28 live (a live row's move is a mid-session snapshot, not the session's result)
- rows_per_market (EU/UK, cap 4/market): {'sweden': 4, 'switzerland': 4, 'poland': 4, 'austria': 4, 'germany': 4, 'finland': 4, 'belgium': 4, 'norway': 4, 'denmark': 4, 'italy': 4, 'france': 4, 'uk': 4, 'spain': 3, 'netherlands': 4, 'greece': 2} — the cap stops one thin market taking the table; the EU/UK table was 28% Sweden over nine runs (73 of 264 rows) while Belgium and Greece never appeared once.
- rows_per_market (APAC/Gulf, cap 3/market): {'indonesia': 3, 'china': 3, 'india': 3, 'ksa': 3, 'thailand': 3, 'newzealand': 3, 'singapore': 3}
- deprecations: mcp__tradingview-advanced__*, mcp__tradingview__*, mcp__financekit__*,
  mcp__stocktwits__* are ABSENT in Cloud sessions (tool_search 0 hits; connector catalog
  holds only media + credential tools). The public screener replaces them.

- degraded_sources: 1
  (the chat reply's `errors:` MUST equal this number - one entry per degraded
  source, not one per run)
  1. yahoo_premarket_check.unavailable — XP: Yahoo's 1-minute pre-market feed returned no usable print

## Audit line

`earnings-reaction target=earnings-reactions:2026-11-27 candidates=541 amc_reactions=0 pre_gaps=231 eu_reactions=29 asx_reactions=4 apac_reactions=19 catalyst_lookups=16 bod=109 pass_b2_candidates=116 pass_b2_dedup=28 pass_b2_published=88 earnings_calendar_rows=155 earnings_tiers_fresh=0 earnings_tiers_near=0 earnings_field_stale_rows=0 earnings_dates_catalog=11 earnings_dates_asx=0 asx_ann_rows=6 rows_dropped_stale_ref=3 rows_dropped_unresolved_ref=0 degraded_sources=1`
