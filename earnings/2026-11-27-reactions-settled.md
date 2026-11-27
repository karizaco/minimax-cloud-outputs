# Earnings reaction scanner — 2026-11-27 (EU settlement pass)

- Cron: `15 12 * * 1-5` America/New_York (weekdays, 12:15 ET)
- Fire time (ET): 2026-11-27 12:16:19 Fri
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
- morning_artifact: earnings/2026-11-27-reactions.md
- Status: `ok`

## TL;DR

- 30 EU/UK rows republished with their SETTLED close and move.
- 21 of them also appear in the 08:00 ET scan: the settled move
  differs from the scan move by a median of 1.45pp and a maximum of
  12.46pp; 13 of 21 rows moved more than 1pp
  between the scan and the close.
- Biggest settled EU/UK move: ELON (-14.75%, sweden).

## EU/UK — Settled table

| Ticker | Market | Venue | Close | Chg % | Move @08:00 | Δ vs scan | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | Session asof | Settle | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ELON | sweden | OMXSTO | 63.6 | -14.75 | -11.80 | -2.95 | SEK | 3.2x | 74.60 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | settled | none | 2026-11-18 (9d ago) | N | no fresh catalyst found; the last release was the Q3 interim report (reported 2026-11-18) |
| LMGAB | sweden | OMXSTO | 53.8 | +12.08 | +10.63 | +1.45 | SEK | 5.8x | 48.00 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | settled | none | 2026-10-30 (28d ago) | — | no catalyst lookup (outside the per-run budget) |
| MDV | poland | GPW | 134.5 | +11.16 | +10.66 | +0.50 | PLN | 3.9x | 121.00 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | settled | none | 2026-11-27 (0d ago) | Y | Q3 2026/27 results: revenue PLN 3.207bn (+11% y/y), adjusted EBITDA +48%, plus Nov 1-25 sales +34% y/y (reported 2026-11-27) |
| SILEX | sweden | OMXSTO | 160.3 | +10.93 | +9.00 | +1.93 | SEK | 2.6x | 144.50 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | settled | US line (OTC:SILXF) | 2026-11-04 (23d ago) | — | pending catalyst lookup |
| CRNA | norway | OSL | 8.78 | -10.68 | -6.82 | -3.86 | NOK | 4.6x | 9.83 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| CLAV | sweden | OMXSTO | 5.01 | +9.92 | — | — | SEK | 3.1x | 4.56 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | settled | none | 2026-11-12 (15d ago) | N | BAE Systems awards a 450 MSEK contract for Clavister CyberArmour on the CV90 Nordic Edition programme (2026-11-27) |
| ELG | germany | XETR | 108.2 | +9.18 | +7.97 | +1.21 | EUR | 2.2x | 99.10 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | settled | none | 2026-11-10 (17d ago) | N | no fresh catalyst found - European chip stocks are rebounding; no ELG release today |
| DIA | poland | GPW | 142.9 | -8.40 | -6.92 | -1.48 | PLN | 5.7x | 156.00 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | settled | none | 2026-11-26 (1d ago) | — | no catalyst lookup (outside the per-run budget) |
| ATS | austria | VIE | 105 | +7.91 | +8.12 | -0.21 | EUR | 1.2x | 97.30 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | settled | none | 2026-11-05 (22d ago) | N | CEO Mertin says on Bloomberg TV (2026-11-25) the company is weighing a US or Asia listing, blaming thin Vienna liquidity |
| SENSO | finland | OMXHEX | 19.98 | +7.88 | +5.29 | +2.59 | EUR | 2.3x | 18.52 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | settled | none | 2026-09-03 (85d ago) | — | no catalyst lookup (outside the per-run budget) |
| BEKB | belgium | EURONEXT | 42.55 | +7.86 | +7.60 | +0.26 | EUR | 4.4x | 39.45 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | settled | none | 2026-11-27 (0d ago) | Y | Q3 2026 trading update: sales EUR 987m (+12%, +8% like-for-like), FY26 sales outlook raised above FY2025, new EUR 100m buyback (reported 2026-11-27) |
| DESN | switzerland | SIX | 297.5 | +7.79 | +10.69 | -2.90 | CHF | 4.4x | 276.00 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| S92 | germany | GETTEX | 47.5 | +7.66 | +5.89 | +1.77 | EUR | 1.9x | 44.16 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | settled | none | 2026-11-12 (15d ago) | — | no catalyst lookup (outside the per-run budget) |
| MRB | poland | GPW | 12.41 | +7.63 | — | — | PLN | 3.7x | 11.53 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | settled | none | 2026-08-25 (94d ago) | — | no catalyst lookup (outside the per-run budget) |
| AMBU_B | denmark | OMXCOP | 93.45 | +7.60 | +7.31 | +0.29 | DKK | 4.2x | 86.85 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | settled | US line (OTC:AMBFF) | 2026-11-05 (22d ago) | N | Nordea raises to Buy (PT DKK 110) and J.P. Morgan raises to Overweight (PT DKK 131) on the morning of 2026-11-27 |
| KGH | poland | GPW | 252.5 | +7.38 | — | — | PLN | 1.9x | 235.15 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | settled | none | 2026-11-17 (10d ago) | — | no catalyst lookup (outside the per-run budget) |
| AMS2 | austria | VIE | 17 | +7.26 | — | — | EUR | 1.1x | 15.85 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | settled | none | 2026-11-13 (14d ago) | — | pending catalyst lookup |
| KOMPL | norway | OSL | 6.96 | +7.08 | +7.08 | -0.00 | NOK | 2.3x | 6.50 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | settled | none | 2026-10-22 (36d ago) | N | no fresh catalyst found |
| BMA | norway | OSL | 21.4 | -6.96 | +5.50 | -12.46 | NOK | 3.6x | 23.00 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| EXENS | france | EURONEXT | 54.3 | +6.37 | +6.46 | -0.09 | EUR | 2.7x | 51.05 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | settled | none | 2026-07-28 (122d ago) | — | no catalyst lookup (outside the per-run budget) |
| NTG | denmark | OMXCOP | 324 | +6.06 | — | — | DKK | 2.9x | 305.50 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | settled | none | 2026-11-09 (18d ago) | — | no catalyst lookup (outside the per-run budget) |
| BITTI | finland | OMXHEX | 35.4 | +5.99 | +7.63 | -1.64 | EUR | 1.8x | 33.40 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | settled | none | 2026-10-29 (29d ago) | N | Nasdaq adds Bittium to the OMX Helsinki Benchmark index effective 2026-12-01 (announced 2026-11-23) |
| PFS0 | germany | XETR | 60.7 | +5.93 | — | — | EUR | 2.2x | 57.30 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | settled | none | 2026-11-18 (9d ago) | — | no catalyst lookup (outside the per-run budget) |
| DFENS | norway | OSL | 12.6 | +5.88 | +7.56 | -1.68 | NOK | 3.8x | 11.90 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | settled | none | 2026-11-26 (1d ago) | — | no catalyst lookup (outside the per-run budget) |
| FCT | italy | MIL | 12.105 | +5.72 | +6.77 | -1.05 | EUR | 2.2x | 11.45 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | settled | none | 2026-07-29 (121d ago) | — | no catalyst lookup (outside the per-run budget) |
| AG1 | germany | GETTEX | 15.72 | +5.72 | — | — | EUR | 1.6x | 14.90 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | settled | none | 2026-11-04 (23d ago) | — | no catalyst lookup (outside the per-run budget) |
| SRAIL | switzerland | SIX | 30.36 | +5.05 | — | — | CHF | 2.6x | 28.90 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | settled | none | 2026-08-26 (93d ago) | — | no catalyst lookup (outside the per-run budget) |
| ENRGY | belgium | EURONEXT | 21.85 | +5.05 | — | — | EUR | 2.4x | 20.80 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | settled | none | 2026-09-03 (85d ago) | — | no catalyst lookup (outside the per-run budget) |
| METSO | finland | OMXHEX | 15.05 | +5.02 | +5.09 | -0.07 | EUR | 2.1x | 14.33 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | settled | US line (OTC:OUKPF) | 2026-10-22 (36d ago) | N | Metals Focus Minerals 260 advances a Western Australia gold project (2026-11-27); no Metso release today |
| ENT | uk | LSE | 477.2 | +5.02 | +5.15 | -0.13 | GBX | 2.6x | 454.40 | yahoo_chart_daily | 2026-11-26 | 2026-11-27 | settled | none | 2026-08-13 (106d ago) | — | no catalyst lookup (outside the per-run budget) |

## Source health

- scanner_calls: 36 | scanner_errors: 0
- pipeline_version: 2026-11-20.1
- settlement: the EU/UK session is CLOSED at this fire, so every row's `Settle`
  cell reads `settled` and its move is the session's own move.
- morning_artifact: found locally
- catalyst_catalog: found locally
- catalyst_merge: region-matched - a row may only use a catalog entry from its OWN
  region; the same ticker on another venue is a different company and is not used.
- scan_to_settle: 21 rows compared with the 08:00 ET scan, median drift 1.45pp, max 12.46pp, 13 rows more than 1pp apart
- reference_close (screener vs Yahoo, resolved BEFORE the table was built): agree=30 mismatch=0 unverified=0 stale_reference=0
- rows_dropped_stale_ref: 0 | rows_dropped_unresolved_ref: 0
- earnings_field_stale_rows: 0 (the bulk earnings calendar reaches the US only, and this artifact publishes no US row, so the screener's own field is the only source for its dates - a stale date here is POSSIBLE and is not detected)
- earnings_dates: the published `Last earnings` date by source - catalog (researched) 10, calendar 0, asx 0, screener 20. The chain is researched -> calendar (US) -> ASX feed (AU) -> the screener's field, which is the FALLBACK and the one that lags. This pass publishes the EU/UK rows only, so its dates come from the researched catalog and the screener's field; no bulk calendar or ASX feed reaches a European venue - each bulk feed is consulted only for its own market.
- catalyst_budget: 0 US + 0 EU + 0 AU + 0 APAC/Gulf = 0 lookups - the settlement pass performs NO new catalyst lookups (no research happens in this slot); every catalyst cell is merged from the 08:00 ET run's catalog, and a row may only use a catalog entry from its OWN region.
- earnings_tiers: fresh=2 near=2 (fresh = the row's earnings event is dated on the session that just settled, near = the previous session; measured over THIS table's rows - the 08:00 scan ranks the US rows by the same key)
- earnings_date_quality: 1 of 12 markets that publish rows here publish a FRESH earnings date (median age <= 14d); `us` and `au` publish 0 rows BY DESIGN (the US session is open at 12:15 ET and the AU rows belong to the 08:00 scan), not by a failed scan. The table below gives each market's rows, the rows with NO date at all, the median age of the published date and the rows within 7 and 30 days - the reader sees the input quality instead of trusting it
| market | rows | no date | median age | <=7d | <=30d |
|---|---|---|---|---|---|
| au | 0 | 0 | n/a | 0 | 0 |
| austria | 2 | 0 | 22d | 0 | 2 |
| belgium | 2 | 0 | 85d | 1 | 1 |
| denmark | 2 | 0 | 22d | 0 | 2 |
| finland | 3 | 0 | 36d | 0 | 1 |
| france | 1 | 0 | 122d | 0 | 0 |
| germany | 4 | 0 | 17d | 0 | 4 |
| italy | 1 | 0 | 121d | 0 | 0 |
| norway | 4 | 2 | 36d | 1 | 1 |
| poland | 4 | 0 | 10d | 2 | 3 |
| sweden | 4 | 0 | 23d | 0 | 4 |
| switzerland | 2 | 1 | 93d | 0 | 0 |
| uk | 1 | 0 | 106d | 0 | 0 |
| us | 0 | 0 | n/a | 0 | 0 |
- yahoo_calls: 30 | yahoo_429: 0 | yahoo_errors: 0 | yahoo_breaker: closed
- degraded_sources: 0
  (none - every source answered for every published row)

## Audit line

`earnings-reaction mode=settle target=earnings-reactions:2026-11-27 eu_rows=30 scan_matched=21 scan_to_settle_median_pp=1.4533333333333278 catalyst_lookups=16 rows_dropped_stale_ref=0 degraded_sources=0`
