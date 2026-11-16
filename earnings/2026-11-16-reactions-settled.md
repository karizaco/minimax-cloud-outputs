# Earnings reaction scanner — 2026-11-16 (EU settlement pass)

- Cron: `15 12 * * 1-5` America/New_York (weekdays, 12:15 ET)
- Fire time (ET): 2026-11-16 12:30:05 Mon
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
- morning_artifact: earnings/2026-11-16-reactions.md
- Status: `ok`

## TL;DR

- 29 EU/UK rows republished with their SETTLED close and move.
- 16 of them also appear in the 08:00 ET scan: the settled move
  differs from the scan move by a median of 1.29pp and a maximum of
  3.95pp; 10 of 16 rows moved more than 1pp
  between the scan and the close.
- Biggest settled EU/UK move: N91 (-12.76%, uk).

## EU/UK — Settled table

| Ticker | Market | Venue | Close | Chg % | Move @08:00 | Δ vs scan | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | Session asof | Settle | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| N91 | uk | LSE | 177.8 | -12.76 | -8.81 | -3.95 | GBX | 8.2x | 203.80 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | settled | none | 2026-11-16 (0d ago) | — | no catalyst lookup (outside the per-run budget) |
| PLT | norway | OSL | 12.36 | +12.16 | +15.25 | -3.09 | NOK | 3.3x | 11.02 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | settled | none | 2026-08-06 (102d ago) | — | no catalyst lookup (outside the per-run budget) |
| FLS | denmark | OMXCOP | 517.5 | -8.89 | — | — | DKK | 3.7x | 568.00 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | settled | none | 2026-11-11 (5d ago) | — | pending catalyst lookup |
| ACT0 | germany | XETR | 150 | +7.76 | +4.60 | +3.16 | EUR | 2.3x | 139.20 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | settled | none | 2026-10-28 (19d ago) | — | no catalyst lookup (outside the per-run budget) |
| CTEK | sweden | OMXSTO | 15.8 | +7.48 | +8.71 | -1.23 | SEK | 2.7x | 14.70 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | settled | none | 2026-10-29 (18d ago) | — | pending catalyst lookup |
| BICO | sweden | OMXSTO | 15.58 | -6.71 | — | — | SEK | 2.1x | 16.70 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | settled | ADR (OTC:BCCOY) | 2026-11-11 (5d ago) | — | pending catalyst lookup |
| TRUE_B | sweden | OMXSTO | 24.74 | +6.32 | — | — | SEK | 2.1x | 23.27 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | settled | none | 2026-11-03 (13d ago) | — | no catalyst lookup (outside the per-run budget) |
| HNSA | sweden | OMXSTO | 49.56 | +5.81 | +8.77 | -2.96 | SEK | 1.9x | 46.84 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | settled | none | 2026-11-11 (5d ago) | — | pending catalyst lookup |
| NANO | france | EURONEXT | 26.32 | -5.66 | — | — | EUR | 1.3x | 27.90 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | settled | US line (NASDAQ:NA) | 2026-09-24 (53d ago) | — | no catalyst lookup (outside the per-run budget) |
| CMB | italy | MIL | 75.8 | -5.60 | -4.23 | -1.37 | EUR | 2.5x | 80.30 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | settled | US line (NYSE:CMBT) | 2026-11-12 (4d ago) | — | no catalyst lookup (outside the per-run budget) |
| ATT | poland | GPW | 15.39 | -5.47 | -4.18 | -1.29 | PLN | 2.8x | 16.28 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | settled | none | 2026-09-10 (67d ago) | N | DM BOS cut the recommendation to sell and the target price from PLN 24 to PLN 13 (gas-cost squeeze; 2026-27 EBITDA forecasts cut by ~PLN 1.4bn); Q3 consolidated report due 19 Nov 2026 |
| GPW | poland | GPW | 104.4 | +5.45 | +4.75 | +0.70 | PLN | 2.8x | 99.00 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | settled | none | 2026-11-16 (0d ago) | Y | Q3 2026 results (reported 2026-11-16): net profit PLN 70.3M, +44% y/y and 11% above consensus; revenue PLN 158.5M +17%, EBITDA PLN 71.1M +32% |
| VU | france | EURONEXT | 158.1 | +5.40 | +5.93 | -0.53 | EUR | 2.2x | 150.00 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | settled | none | 2026-09-21 (56d ago) | — | no catalyst lookup (outside the per-run budget) |
| SLR | spain | BME | 14.9 | -5.40 | -4.83 | -0.57 | EUR | 1.7x | 15.75 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | settled | none | 2026-09-24 (53d ago) | — | Q3/9M 2026 results due 2026-11-16 (vendor calendars; some list 17 Nov; consensus revenue EUR 129.9M) - no release confirmed at scan time; Spanish renewables sold off Friday (Acciona -7.98%, Acciona ER -7.17%, Solaria -3.52%); Capital Markets Day 17-18 Nov |
| S92 | germany | XETR | 47.66 | +5.30 | +6.45 | -1.15 | EUR | 1.3x | 45.26 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | settled | none | 2026-11-12 (4d ago) | — | no catalyst lookup (outside the per-run budget) |
| ATS | austria | VIE | 117.2 | -5.02 | -3.40 | -1.62 | EUR | 0.8x | 123.40 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | settled | none | 2026-11-05 (11d ago) | — | pending catalyst lookup |
| ADEN | switzerland | SIX | 24.9 | -4.74 | -3.75 | -0.99 | CHF | 1.9x | 26.14 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | settled | none | 2026-11-12 (4d ago) | — | no catalyst lookup (outside the per-run budget) |
| BC8 | germany | GETTEX | 32.38 | -4.71 | -4.84 | +0.13 | EUR | 2.4x | 33.86 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | settled | none | 2026-11-13 (3d ago) | — | no catalyst lookup (outside the per-run budget) |
| ACE | italy | MIL | 20.32 | -4.60 | -3.29 | -1.31 | EUR | 4.7x | 21.30 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | settled | none | 2026-11-13 (3d ago) | — | no catalyst lookup (outside the per-run budget) |
| AAL | uk | LSE | 3605 | -4.25 | — | — | GBX | 1.7x | 3765.00 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | settled | none | 2026-07-30 (109d ago) | — | no catalyst lookup (outside the per-run budget) |
| AKAST | norway | OSL | 9.69 | +4.19 | — | — | NOK | 1.2x | 9.30 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | settled | none | 2026-11-11 (5d ago) | — | no catalyst lookup (outside the per-run budget) |
| NORAM | norway | OSL | 43.45 | -4.19 | — | — | NOK | 2.3x | 45.35 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | settled | none | 2026-08-25 (83d ago) | — | pending catalyst lookup |
| TPRO | italy | MIL | 21.06 | -4.19 | — | — | EUR | 1.0x | 21.98 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | settled | none | 2026-08-05 (103d ago) | — | no catalyst lookup (outside the per-run budget) |
| BMAG | austria | VIE | 30 | -4.15 | — | — | EUR | 1.4x | 31.30 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| OTEC | norway | OSL | 17.52 | -3.84 | — | — | NOK | 1.6x | 18.22 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | settled | none | 2022-02-15 (1735d ago) | — | no catalyst lookup (outside the per-run budget) |
| NWL | italy | MIL | 25.3 | +3.60 | — | — | EUR | 1.5x | 24.42 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | settled | none | 2026-11-09 (7d ago) | — | no catalyst lookup (outside the per-run budget) |
| ASM | netherlands | EURONEXT | 669.8 | -3.57 | — | — | EUR | 1.0x | 694.60 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | settled | US line (OTC:ASMXF) | 2026-10-27 (20d ago) | — | no catalyst lookup (outside the per-run budget) |
| HLUN_B | denmark | OMXCOP | 61.4 | +3.45 | — | — | DKK | 1.8x | 59.35 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | settled | none | 2026-11-10 (6d ago) | — | pending catalyst lookup |
| CBF | poland | GPW | 199 | +3.43 | +3.17 | +0.26 | PLN | 3.8x | 192.40 | yahoo_chart_daily | 2026-11-13 | 2026-11-16 | settled | none | 2026-09-02 (75d ago) | — | pending catalyst lookup |

## Source health

- scanner_calls: 36 | scanner_errors: 0
- pipeline_version: 2026-11-16.2
- settlement: the EU/UK session is CLOSED at this fire, so every row's `Settle`
  cell reads `settled` and its move is the session's own move.
- morning_artifact: found locally
- catalyst_catalog: found locally
- catalyst_merge: region-matched - a row may only use a catalog entry from its OWN
  region; the same ticker on another venue is a different company and is not used.
- scan_to_settle: 16 rows compared with the 08:00 ET scan, median drift 1.29pp, max 3.95pp, 10 rows more than 1pp apart
- reference_close (screener vs Yahoo, resolved BEFORE the table was built): agree=29 mismatch=1 unverified=0 stale_reference=1
- rows_dropped_stale_ref: 1 | rows_dropped_unresolved_ref: 0
- earnings_field_stale_rows: 0 (the bulk earnings calendar reaches the US only, and this artifact publishes no US row, so the screener's own field is the only source for its dates - a stale date here is POSSIBLE and is not detected)
- earnings_dates: the published `Last earnings` date by source - catalog (researched) 1, calendar 0, asx 0, screener 28. The chain is researched -> calendar (US) -> ASX feed (AU) -> the screener's field, which is the FALLBACK and the one that lags. This pass publishes the EU/UK rows only, so its dates come from the researched catalog and the screener's field; no bulk calendar or ASX feed reaches a European venue - each bulk feed is consulted only for its own market.
- catalyst_budget: 0 US + 0 EU + 0 AU + 0 APAC/Gulf = 0 lookups - the settlement pass performs NO new catalyst lookups (no research happens in this slot); every catalyst cell is merged from the 08:00 ET run's catalog, and a row may only use a catalog entry from its OWN region.
- earnings_tiers: fresh=2 near=2 (fresh = the row's earnings event is dated on the session that just settled, near = the previous session; measured over THIS table's rows - the 08:00 scan ranks the US rows by the same key)
- earnings_date_quality: 6 of 12 markets that publish rows here publish a FRESH earnings date (median age <= 14d); `us` and `au` publish 0 rows BY DESIGN (the US session is open at 12:15 ET and the AU rows belong to the 08:00 scan), not by a failed scan. The table below gives each market's rows, the rows with NO date at all, the median age of the published date and the rows within 7 and 30 days - the reader sees the input quality instead of trusting it
| market | rows | no date | median age | <=7d | <=30d |
|---|---|---|---|---|---|
| au | 0 | 0 | n/a | 0 | 0 |
| austria | 2 | 1 | 11d | 0 | 1 |
| denmark | 2 | 0 | 6d | 2 | 2 |
| france | 2 | 0 | 56d | 0 | 0 |
| germany | 3 | 0 | 4d | 2 | 3 |
| italy | 4 | 0 | 7d | 3 | 3 |
| netherlands | 1 | 0 | 20d | 0 | 1 |
| norway | 4 | 0 | 102d | 1 | 1 |
| poland | 3 | 0 | 67d | 1 | 1 |
| spain | 1 | 0 | 53d | 0 | 0 |
| sweden | 4 | 0 | 13d | 2 | 4 |
| switzerland | 1 | 0 | 4d | 1 | 1 |
| uk | 2 | 0 | 109d | 1 | 1 |
| us | 0 | 0 | n/a | 0 | 0 |
- yahoo_calls: 30 | yahoo_429: 0 | yahoo_errors: 0 | yahoo_breaker: closed
- degraded_sources: 0
  (none - every source answered for every published row)

## Audit line

`earnings-reaction mode=settle target=earnings-reactions:2026-11-16 eu_rows=29 scan_matched=16 scan_to_settle_median_pp=1.2868304668304704 catalyst_lookups=16 rows_dropped_stale_ref=1 degraded_sources=0`
