# Earnings reaction scanner — 2026-11-11 (EU settlement pass)

- Cron: `15 12 * * 1-5` America/New_York (weekdays, 12:15 ET)
- Fire time (ET): 2026-11-11 12:22:17 Wed
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
- morning_artifact: earnings/2026-11-11-reactions.md
- Status: `ok`

## TL;DR

- 30 EU/UK rows republished with their SETTLED close and move.
- 22 of them also appear in the 08:00 ET scan: the settled move
  differs from the scan move by a median of 0.71pp and a maximum of
  6.86pp; 7 of 22 rows moved more than 1pp
  between the scan and the close.
- Biggest settled EU/UK move: BICO (-32.15%, sweden).

## EU/UK — Settled table

| Ticker | Market | Venue | Close | Chg % | Move @08:00 | Δ vs scan | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | Session asof | Settle | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BICO | sweden | OMXSTO | 16.76 | -32.15 | -30.12 | -2.03 | SEK | 10.7x | 24.70 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | settled | ADR (OTC:CLLKF) | 2026-08-19 | Y | Q3 2026 interim report published 11 Nov 07:00 CET: net sales SEK 465.2m (+20.2% y/y, including a one-off SEK 135m SCIENION supply and licence deal), adjusted EBITDA SEK 124.3m at a 26.7% margin - but a SEK 296m impairment of Biosero goodwill and technology, net loss SEK 220.4m and negative operating cash flow sent the shares down about 30% |
| HNSA | sweden | OMXSTO | 44.76 | +14.95 | +14.48 | +0.47 | SEK | 5.1x | 38.94 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | settled | none | 2026-11-11 | — | no catalyst lookup (outside the per-run budget) |
| APR | norway | OSL | 33.5 | -12.53 | -12.79 | +0.26 | NOK | 3.0x | 38.30 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | settled | none | 2026-10-29 | — | no catalyst lookup (outside the per-run budget) |
| GNS | poland | GPW | 15.6 | +12.23 | +12.23 | +0.00 | PLN | 5.5x | 13.90 | yahoo_chart_daily | 2026-11-09 | 2026-11-10 | settled | none | 2026-09-30 | — | no catalyst lookup (outside the per-run budget) |
| SOI | france | EURONEXT | 108.35 | +11.93 | +9.92 | +2.01 | EUR | 2.2x | 96.80 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | settled | none | 2026-05-27 | — | no catalyst lookup (outside the per-run budget) |
| ATS | austria | VIE | 126.2 | +11.88 | +11.17 | +0.71 | EUR | 1.8x | 112.80 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | settled | none | 2026-11-05 | — | no catalyst lookup (outside the per-run budget) |
| CAF | spain | BME | 68.3 | -11.87 | -10.19 | -1.68 | EUR | 6.6x | 77.50 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | settled | none | 2026-07-30 | — | no catalyst lookup (outside the per-run budget) |
| FNM | sweden | OMXSTO | 105 | +11.23 | +10.70 | +0.53 | SEK | 3.4x | 94.40 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | settled | none | 2026-08-12 | Y | Ferronordic Q3 2026 interim report published 11 Nov 07:30 CET: sales SEK 1,216m (+3% y/y) and EBIT SEK 69m, a beat versus the ABGSCe SEK 1,178m, on higher earnings and growing aftermarket |
| SENSO | finland | OMXHEX | 21.07 | +11.19 | +4.33 | +6.86 | EUR | 3.3x | 18.95 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| ENR | germany | XETR | 132.76 | +10.78 | +9.01 | +1.77 | EUR | 2.6x | 119.84 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | settled | none | 2026-08-04 | Y | Siemens Energy record fiscal 2026 reported 11 Nov: comparable revenue EUR 44.2bn (+15.5%), orders EUR 68.1bn (+18.8%), record year-end backlog EUR 164bn with a 1.54 book-to-bill, profit before special items more than doubled to EUR 5.486bn, dividend more than tripled to EUR 2.30 a share, and FY27 guidance of 14-16% comparable revenue growth |
| SIVE | sweden | OMXSTO | 17.4 | +10.76 | +11.27 | -0.51 | SEK | 2.1x | 15.71 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | settled | none | 2026-08-27 | — | no catalyst lookup (outside the per-run budget) |
| DRW3 | germany | XETR | 109.6 | +9.93 | +8.32 | +1.61 | EUR | 5.0x | 99.70 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | settled | none | 2026-10-29 | — | no catalyst lookup (outside the per-run budget) |
| AIXA | germany | SWB | 34.35 | +8.33 | +7.13 | +1.20 | EUR | 1.8x | 31.75 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | settled | none | 2026-10-29 | — | no catalyst lookup (outside the per-run budget) |
| TPRO | italy | MIL | 23.7 | +7.73 | +7.09 | +0.64 | EUR | 1.9x | 22.00 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | settled | none | 2026-08-05 | — | no catalyst lookup (outside the per-run budget) |
| VOE | austria | VIE | 38.38 | -7.65 | — | — | EUR | 4.0x | 41.56 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | settled | none | 2026-11-11 | — | no catalyst lookup (outside the per-run budget) |
| WAF | germany | XETR | 57.65 | +7.46 | — | — | EUR | 2.0x | 53.65 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | settled | none | 2026-11-04 | — | no catalyst lookup (outside the per-run budget) |
| ERA | france | EURONEXT | 38.48 | +7.43 | +6.87 | +0.56 | EUR | 2.8x | 35.82 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | settled | none | 2026-07-29 | — | no catalyst lookup (outside the per-run budget) |
| ASM | netherlands | EURONEXT | 727.6 | +6.97 | +6.70 | +0.27 | EUR | 2.1x | 680.20 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | settled | ADR (OTC:ASMXF) | 2026-10-27 | — | no catalyst lookup (outside the per-run budget) |
| BESI | netherlands | EURONEXT | 159.75 | +5.94 | +5.11 | +0.83 | EUR | 1.6x | 150.80 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | settled | none | 2026-10-21 | — | no catalyst lookup (outside the per-run budget) |
| WOSG | uk | LSE | 795 | +5.86 | — | — | GBX | 3.2x | 751.00 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | settled | none | 2026-07-14 | — | no catalyst lookup (outside the per-run budget) |
| BWE | norway | OSL | 47.8 | +5.75 | +4.87 | +0.88 | NOK | 2.1x | 45.20 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | settled | none | 2026-10-29 | — | no catalyst lookup (outside the per-run budget) |
| FLS | denmark | OMXCOP | 604 | +5.59 | +4.72 | +0.87 | DKK | 3.2x | 572.00 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | settled | none | 2026-08-18 | — | no catalyst lookup (outside the per-run budget) |
| MDATA | norway | OSL | 13.36 | +5.53 | — | — | NOK | 1.7x | 12.66 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | settled | none | 2026-10-30 | — | no catalyst lookup (outside the per-run budget) |
| CMB | italy | MIL | 78.3 | +5.38 | — | — | EUR | 3.3x | 74.30 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | settled | ADR (NYSE:CMBT) | 2026-09-11 | — | no catalyst lookup (outside the per-run budget) |
| KOMPL | norway | OSL | 6.94 | +5.15 | +5.45 | -0.30 | NOK | 1.7x | 6.60 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | settled | none | 2026-10-22 | — | no catalyst lookup (outside the per-run budget) |
| DVL | poland | GPW | 8.4 | +5.00 | +5.00 | +0.00 | PLN | 3.1x | 8.00 | yahoo_chart_daily | 2026-11-09 | 2026-11-10 | settled | none | 2026-09-11 | — | no catalyst lookup (outside the per-run budget) |
| YPSN | switzerland | SIX | 414 | +4.92 | +4.26 | +0.66 | CHF | 4.6x | 394.60 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | settled | none | 2026-11-11 | — | no catalyst lookup (outside the per-run budget) |
| HLUN_A | denmark | OMXCOP | 59.6 | +4.75 | — | — | DKK | 2.7x | 56.90 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| CCC | uk | LSE | 4928 | +4.67 | — | — | GBX | 1.5x | 4708.00 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | settled | none | 2026-09-08 | — | no catalyst lookup (outside the per-run budget) |
| LOGNE | switzerland | SIX | 83.46 | +4.59 | — | — | CHF | 1.9x | 79.80 | yahoo_chart_daily | 2026-11-10 | 2026-11-11 | settled | none | 2026-10-27 | — | no catalyst lookup (outside the per-run budget) |

## Source health

- scanner_calls: 36 | scanner_errors: 0
- pipeline_version: 2026-11-11.2
- settlement: the EU/UK session is CLOSED at this fire, so every row's `Settle`
  cell reads `settled` and its move is the session's own move.
- morning_artifact: fetched from the outputs repo (api-token)
- catalyst_catalog: rebuilt from the morning artifact (14 researched catalysts recovered)
- scan_to_settle: 22 rows compared with the 08:00 ET scan, median drift 0.71pp, max 6.86pp, 7 rows more than 1pp apart
- reference_close (screener vs Yahoo, resolved BEFORE the table was built): agree=30 mismatch=0 unverified=0 stale_reference=0
- rows_dropped_stale_ref: 0 | rows_dropped_unresolved_ref: 0
- degraded_sources: 0
  (none - every source answered for every published row)

## Audit line

`earnings-reaction mode=settle target=earnings-reactions:2026-11-11 eu_rows=30 scan_matched=22 scan_to_settle_median_pp=0.7094326241134805 catalyst_lookups=14 rows_dropped_stale_ref=0 degraded_sources=0`
