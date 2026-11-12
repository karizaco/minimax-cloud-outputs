# Earnings reaction scanner — 2026-11-12 (EU settlement pass)

- Cron: `15 12 * * 1-5` America/New_York (weekdays, 12:15 ET)
- Fire time (ET): 2026-11-12 12:16:05 Thu
- Run type: `settlement_pass` — the EU/UK session has closed, so the same rows as
  the 08:00 ET scan are republished with their SETTLED close and move.
- Source: TradingView public screener; Yahoo chart API as the independent
  reference-close source.
- Method: the EU/UK cash session closed at 11:30 ET (16:30 CET in winter; 10:30
  ET in summer). The 08:00 ET scan's move is carried alongside each settled move
  so the reaction can be read as a measurement, not an impression. The US session
  is OPEN at 12:15 ET, so no US rows are published here - a live intraday price
  presented as a close would be a fabricated settle.
- artifact_contract: REACTION_ARTIFACT_V2
- morning_artifact: earnings/2026-11-12-reactions.md
- Status: `ok`

## TL;DR

- 30 EU/UK rows republished with their SETTLED close and move.
- 19 of them also appear in the 08:00 ET scan: the settled move
  differs from the scan move by a median of 1.26pp and a maximum of
  6.81pp; 12 of 19 rows moved more than 1pp
  between the scan and the close.
- Biggest settled EU/UK move: BME (+20.93%, uk).

## EU/UK — Settled table

| Ticker | Market | Venue | Close | Chg % | Move @08:00 | Δ vs scan | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | Session asof | Settle | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BME | uk | LSE | 337.4 | +20.93 | +20.84 | +0.09 | GBX | 8.6x | 279.00 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | settled | none | 2026-11-12 | — | no catalyst lookup (outside the per-run budget) |
| MEKO | sweden | OMXSTO | 58.5 | -18.81 | -16.38 | -2.43 | SEK | 11.8x | 72.05 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | settled | none | 2026-07-23 | Y | Q3 2026 report (Nov 12): net sales SEK 4,341M, -2% reported and -3% organic, adjusted EBIT SEK 214M (4.8% margin) flat y/y, leverage down to 3.0x; no near-term growth guidance |
| YSN | germany | XETR | 193.6 | -17.09 | -15.20 | -1.89 | EUR | 5.8x | 233.50 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | settled | none | 2026-08-13 | — | no catalyst lookup (outside the per-run budget) |
| OBCK | germany | XETR | 39.2 | -16.60 | -9.79 | -6.81 | EUR | 8.5x | 47.00 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | settled | none | 2026-08-13 | — | pending catalyst lookup |
| ADEN | switzerland | SIX | 26.16 | +14.74 | +15.00 | -0.26 | CHF | 6.5x | 22.80 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | settled | none | 2026-11-12 | — | no catalyst lookup (outside the per-run budget) |
| NORBT | norway | OSL | 186.8 | +14.11 | +12.95 | +1.16 | NOK | 6.5x | 163.70 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | settled | none | 2026-08-13 | Y | Q3 2026 results (Nov 12): revenue NOK 677M, +34% YoY and +28% organic, EBIT NOK 116M (+53%), EBIT margin 17% from 14%, contract wins totalling over NOK 500M, additional dividend of NOK 2.00 per share |
| STG | denmark | OMXCOP | 87.8 | +13.73 | +9.33 | +4.40 | DKK | 10.1x | 77.20 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | settled | none | 2026-11-11 | — | no catalyst lookup (outside the per-run budget) |
| FG | sweden | OMXSTO | 18.5 | +11.85 | +13.42 | -1.57 | SEK | 3.4x | 16.54 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | settled | none | 2026-08-20 | Y | Q3 2026 report (Nov 12): net sales SEK 1,414.5M, +2.4%, EBITA SEK 139.6M (9.9% margin), EPS SEK 0.84, order book SEK 4,254.3M, +4.4% |
| GENO | norway | OSL | 17 | -11.46 | — | — | NOK | 3.2x | 19.20 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | settled | none | 2026-08-13 | — | no catalyst lookup (outside the per-run budget) |
| SUS | sweden | OMXSTO | 55.6 | -10.83 | -8.18 | -2.65 | SEK | 5.9x | 62.35 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | settled | none | 2026-08-19 | — | no catalyst lookup (outside the per-run budget) |
| MTHH | denmark | OMXCOP | 333 | +10.45 | +12.11 | -1.66 | DKK | 4.6x | 301.50 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | settled | none | 2026-08-27 | — | no catalyst lookup (outside the per-run budget) |
| WAC | germany | XETR | 20.6 | -10.04 | -9.61 | -0.43 | EUR | 6.4x | 22.90 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | settled | none | 2026-08-13 | — | no catalyst lookup (outside the per-run budget) |
| MTRO | uk | LSE | 196 | +9.74 | — | — | GBX | 3.4x | 178.60 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | settled | none | 2026-08-03 | — | no catalyst lookup (outside the per-run budget) |
| DMP | germany | XETR | 34.95 | -9.46 | — | — | EUR | 7.1x | 38.60 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | settled | none | 2026-08-25 | Y | 2026 AGM address and presentation (Nov 11): FY26 underlying EBIT $200.1M, record free cash flow $164.1M, and a trading update showing group same-store sales improving to -4.6% FYTD from -5.8% at the August result |
| XPLRA | norway | OSL | 26.25 | +9.15 | — | — | NOK | 3.0x | 24.05 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | settled | none | 2026-08-19 | — | no catalyst lookup (outside the per-run budget) |
| EDV | uk | LSE | 3778 | -8.46 | -6.93 | -1.53 | GBX | 2.9x | 4127.00 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | settled | none | 2026-11-12 | — | no catalyst lookup (outside the per-run budget) |
| SIVE | sweden | OMXSTO | 15.94 | -8.39 | -8.33 | -0.06 | SEK | 1.5x | 17.40 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | settled | none | 2026-08-27 | — | no catalyst lookup (outside the per-run budget) |
| DEMANT | denmark | OMXCOP | 339.4 | -8.32 | — | — | DKK | 6.7x | 370.20 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | settled | ADR (OTC:WILYY) | 2026-08-11 | — | no catalyst lookup (outside the per-run budget) |
| ENDUR | norway | OSL | 140.8 | +8.31 | +5.69 | +2.62 | NOK | 4.5x | 130.00 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | settled | none | 2026-08-20 | — | no catalyst lookup (outside the per-run budget) |
| BRBY | uk | LSE | 1180.5 | +8.01 | +8.42 | -0.41 | GBX | 4.3x | 1093.00 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | settled | none | 2026-11-12 | — | no catalyst lookup (outside the per-run budget) |
| ENA | poland | GPW | 22.26 | +7.85 | — | — | PLN | 4.0x | 20.64 | yahoo_chart_daily | 2026-11-10 | 2026-11-12 | settled | none | 2026-08-11 | — | no catalyst lookup (outside the per-run budget) |
| ALCE | switzerland | SIX | 60.52 | +5.95 | +7.21 | -1.26 | CHF | 19.0x | 57.12 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | settled | none | 2026-11-10 | — | no catalyst lookup (outside the per-run budget) |
| MOL | italy | MIL | 37.55 | +5.63 | — | — | EUR | 3.0x | 35.55 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | settled | none | 2026-09-08 | — | no catalyst lookup (outside the per-run budget) |
| YPSN | switzerland | SIX | 437.2 | +5.60 | +4.35 | +1.25 | CHF | 4.2x | 414.00 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | settled | none | 2026-11-11 | — | no catalyst lookup (outside the per-run budget) |
| FLS | denmark | OMXCOP | 570.5 | -5.55 | -5.05 | -0.50 | DKK | 2.8x | 604.00 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | settled | none | 2026-11-11 | — | no catalyst lookup (outside the per-run budget) |
| REY | italy | MIL | 139.1 | +5.54 | — | — | EUR | 4.5x | 131.80 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | settled | none | 2026-07-30 | — | no catalyst lookup (outside the per-run budget) |
| ENAV | italy | MIL | 5.59 | +5.37 | — | — | EUR | 4.8x | 5.30 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | settled | none | 2026-08-03 | — | no catalyst lookup (outside the per-run budget) |
| AMP | italy | MIL | 11.54 | -5.29 | — | — | EUR | 2.5x | 12.19 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | settled | ADR (OTC:AMLTF) | 2026-10-29 | — | no catalyst lookup (outside the per-run budget) |
| BITTI | finland | OMXHEX | 32.8 | -4.93 | -4.20 | -0.73 | EUR | 1.5x | 34.50 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | settled | none | 2022-02-10 | — | no catalyst lookup (outside the per-run budget) |
| WIE | austria | VIE | 16.38 | -4.77 | — | — | EUR | 2.5x | 17.20 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | settled | none | 2026-08-12 | — | no catalyst lookup (outside the per-run budget) |

## Source health

- scanner_calls: 36 | scanner_errors: 0
- pipeline_version: 2026-11-11.2
- settlement: the EU/UK session is CLOSED at this fire, so every row's `Settle`
  cell reads `settled` and its move is the session's own move.
- morning_artifact: fetched from the outputs repo (api-token)
- catalyst_catalog: rebuilt from the morning artifact (13 researched catalysts recovered)
- scan_to_settle: 19 rows compared with the 08:00 ET scan, median drift 1.26pp, max 6.81pp, 12 rows more than 1pp apart
- reference_close (screener vs Yahoo, resolved BEFORE the table was built): agree=30 mismatch=0 unverified=0 stale_reference=0
- rows_dropped_stale_ref: 0 | rows_dropped_unresolved_ref: 0
- degraded_sources: 0
  (none - every source answered for every published row)

## Audit line

`earnings-reaction mode=settle target=earnings-reactions:2026-11-12 eu_rows=30 scan_matched=19 scan_to_settle_median_pp=1.2576190476190376 catalyst_lookups=13 rows_dropped_stale_ref=0 degraded_sources=0`
