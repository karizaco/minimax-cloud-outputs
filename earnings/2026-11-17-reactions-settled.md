# Earnings reaction scanner — 2026-11-17 (EU settlement pass)

- Cron: `15 12 * * 1-5` America/New_York (weekdays, 12:15 ET)
- Fire time (ET): 2026-11-17 12:16:29 Tue
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
- morning_artifact: earnings/2026-11-17-reactions.md
- Status: `ok`

## TL;DR

- 29 EU/UK rows republished with their SETTLED close and move.
- 18 of them also appear in the 08:00 ET scan: the settled move
  differs from the scan move by a median of 0.81pp and a maximum of
  2.74pp; 8 of 18 rows moved more than 1pp
  between the scan and the close.
- Biggest settled EU/UK move: XTB (-17.52%, poland).

## EU/UK — Settled table

| Ticker | Market | Venue | Close | Chg % | Move @08:00 | Δ vs scan | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | Session asof | Settle | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| XTB | poland | GPW | 115.24 | -17.52 | -16.30 | -1.22 | PLN | 6.3x | 139.72 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | settled | none | 2026-10-28 (20d ago) | — | no catalyst lookup (outside the per-run budget) |
| AVIO | italy | MIL | 39.18 | +14.90 | +15.32 | -0.42 | EUR | 4.6x | 34.10 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | settled | US line (OTC:AVVOF) | 2026-03-12 (250d ago) | — | no catalyst lookup (outside the per-run budget) |
| GOMX | sweden | OMXSTO | 13.73 | -7.23 | -5.47 | -1.76 | SEK | 1.7x | 14.80 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | settled | none | 2026-08-26 (83d ago) | — | no catalyst lookup (outside the per-run budget) |
| CBF | poland | GPW | 213.2 | +7.14 | +6.33 | +0.81 | PLN | 5.7x | 199.00 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | settled | none | 2026-11-16 (1d ago) | — | no catalyst lookup (outside the per-run budget) |
| HEM | sweden | OMXSTO | 53.95 | -6.98 | -5.00 | -1.98 | SEK | 1.7x | 58.00 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | settled | none | 2026-10-22 (26d ago) | — | pending catalyst lookup |
| TRUE_B | sweden | OMXSTO | 23.04 | -6.87 | — | — | SEK | 2.1x | 24.74 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | settled | none | 2026-11-03 (14d ago) | N | no fresh catalyst found - no company news on 17 Nov; the Viceroy Research short-seller report of 12 Nov on data protection of minors is still the live overhang, and the Q3 net loss of 3 Nov is already priced after the 16 Nov +6.3% rally |
| OVH | france | EURONEXT | 13.85 | -6.73 | -5.52 | -1.21 | EUR | 1.5x | 14.85 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | settled | none | 2026-10-20 (28d ago) | — | no catalyst lookup (outside the per-run budget) |
| IDR | spain | BME | 54 | -6.41 | -3.67 | -2.74 | EUR | 2.5x | 57.70 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | settled | none | 2026-10-29 (19d ago) | — | no catalyst lookup (outside the per-run budget) |
| TECN | switzerland | SIX | 233 | -6.35 | -6.43 | +0.08 | CHF | 3.3x | 248.80 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | settled | none | 2026-08-11 (98d ago) | — | no catalyst lookup (outside the per-run budget) |
| NANO | france | EURONEXT | 24.7 | -6.16 | -4.64 | -1.52 | EUR | 1.6x | 26.32 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | settled | US line (NASDAQ:NA) | 2026-09-24 (54d ago) | — | no catalyst lookup (outside the per-run budget) |
| VRC | poland | GPW | 130.6 | +5.83 | — | — | PLN | 4.4x | 123.40 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | settled | none | 2026-11-17 (0d ago) | Y | Q3 2026 results (reported 2026-11-17): revenue PLN 139.8m vs PLN 135.6m consensus, EBITDA PLN 42.7m vs PLN 41.3m, net profit PLN 31.2m vs PLN 29.3m (+56% y/y); 9M revenue PLN 395.6m and a 28.7% operating EBITDA margin |
| WWI | norway | OSL | 949 | +5.80 | +5.57 | +0.23 | NOK | 3.3x | 897.00 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | settled | none | 2026-11-04 (13d ago) | N | no fresh catalyst found - no company release today; the Q3 2026 report (4 Nov) showed EPS US$3.70 and revenue US$327m, +5.1%, and the shares trade ex a NOK 8.50 dividend (ex 11 Nov, paid 19 Nov) after the buyback tender priced the A-shares at NOK 885 |
| CDR | poland | GPW | 264.8 | -5.70 | -5.16 | -0.54 | PLN | 3.7x | 280.80 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | settled | none | 2026-09-02 (76d ago) | N | no fresh catalyst found - Q3 2026 results are due on 24 Nov 2026; the shares fell with a -1.04% WIG20 session in which CD Projekt RED, KGHM, Orlen and the energy names led the decline |
| IOS | germany | XETR | 35.06 | -5.60 | -3.26 | -2.34 | EUR | 3.5x | 37.14 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | settled | none | 2026-11-12 (5d ago) | — | no catalyst lookup (outside the per-run budget) |
| SAP | germany | XETR | 201.5 | -5.58 | — | — | EUR | 4.1x | 213.40 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | settled | ADR (NYSE:SAP) | 2026-10-21 (27d ago) | — | pending catalyst lookup |
| NORBT | norway | OSL | 166.7 | -5.55 | -4.36 | -1.19 | NOK | 2.1x | 176.50 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | settled | none | 2026-11-12 (5d ago) | Y | Q3 2026 results (reported 2026-11-12): revenue NOK 676.7m beat the NOK 638m consensus, statutory EPS NOK 1.12 missed by 14%, extra dividend of NOK 2.00 declared - the shares traded ex-dividend today, which accounts for part of the 4.25% fall |
| AOF | germany | XETR | 82.9 | -5.37 | — | — | EUR | 2.2x | 87.60 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | settled | none | 2026-07-27 (113d ago) | — | pending catalyst lookup |
| ASML | netherlands | EURONEXT | 1236.8 | -5.34 | — | — | EUR | 1.8x | 1306.60 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | settled | ADR (NASDAQ:ASML) | 2026-10-14 (34d ago) | — | pending catalyst lookup |
| RMV | uk | LSE | 549 | -5.28 | — | — | GBX | 2.6x | 579.60 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | settled | none | 2026-07-31 (109d ago) | — | no catalyst lookup (outside the per-run budget) |
| KOMPL | norway | OSL | 6.52 | -5.23 | — | — | NOK | 1.7x | 6.88 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | settled | none | 2026-10-22 (26d ago) | — | pending catalyst lookup |
| SINCH | sweden | OMXSTO | 41.58 | -5.20 | — | — | SEK | 2.5x | 43.86 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | settled | none | 2026-11-05 (12d ago) | — | pending catalyst lookup |
| RMS | france | EURONEXT | 1280.5 | -5.11 | -4.59 | -0.52 | EUR | 2.8x | 1349.50 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | settled | none | 2026-07-29 (111d ago) | N | no fresh catalyst found - no company news on 17 Nov; the luxury de-rating continues after the 22 Oct Q3 revenue slowdown (+4.3% in Q3 against +6.1% in H1, the shares hitting a 4-year low then), with the stock down about 38% YTD and roughly -4.5% today in a barely positive CAC 40 |
| DSY | france | EURONEXT | 24.4 | -4.91 | — | — | EUR | 2.5x | 25.66 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | settled | none | 2026-10-28 (20d ago) | — | pending catalyst lookup |
| MONC | italy | MIL | 41.56 | -4.48 | -4.02 | -0.46 | EUR | 2.4x | 43.51 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | settled | none | 2026-07-22 (118d ago) | — | no catalyst lookup (outside the per-run budget) |
| ENDUR | norway | OSL | 145.8 | +4.44 | — | — | NOK | 2.5x | 139.60 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | settled | none | 2026-11-12 (5d ago) | — | no catalyst lookup (outside the per-run budget) |
| SFER | italy | MIL | 6.115 | -4.38 | -3.99 | -0.39 | EUR | 3.0x | 6.39 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | settled | none | 2026-08-03 (106d ago) | — | no catalyst lookup (outside the per-run budget) |
| TPRO | italy | MIL | 20.14 | -4.37 | — | — | EUR | 1.0x | 21.06 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | settled | none | 2026-08-05 (104d ago) | — | no catalyst lookup (outside the per-run budget) |
| ZEAL | denmark | OMXCOP | 229.6 | -4.25 | -3.54 | -0.71 | DKK | 2.7x | 239.80 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | settled | none | 2026-11-12 (5d ago) | — | no catalyst lookup (outside the per-run budget) |
| GUBRA | denmark | OMXCOP | 289 | -4.18 | -3.78 | -0.40 | DKK | 1.6x | 301.60 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | settled | none | 2026-08-20 (89d ago) | — | no catalyst lookup (outside the per-run budget) |

## Source health

- scanner_calls: 36 | scanner_errors: 0
- pipeline_version: 2026-11-16.2
- settlement: the EU/UK session is CLOSED at this fire, so every row's `Settle`
  cell reads `settled` and its move is the session's own move.
- morning_artifact: found locally
- catalyst_catalog: found locally
- catalyst_merge: region-matched - a row may only use a catalog entry from its OWN
  region; the same ticker on another venue is a different company and is not used.
- scan_to_settle: 18 rows compared with the 08:00 ET scan, median drift 0.81pp, max 2.74pp, 8 rows more than 1pp apart
- reference_close (screener vs Yahoo, resolved BEFORE the table was built): agree=29 mismatch=1 unverified=0 stale_reference=1
- rows_dropped_stale_ref: 1 | rows_dropped_unresolved_ref: 0
- earnings_field_stale_rows: 0 (the bulk earnings calendar reaches the US only, and this artifact publishes no US row, so the screener's own field is the only source for its dates - a stale date here is POSSIBLE and is not detected)
- earnings_dates: the published `Last earnings` date by source - catalog (researched) 2, calendar 0, asx 0, screener 27. The chain is researched -> calendar (US) -> ASX feed (AU) -> the screener's field, which is the FALLBACK and the one that lags. This pass publishes the EU/UK rows only, so its dates come from the researched catalog and the screener's field; no bulk calendar or ASX feed reaches a European venue - each bulk feed is consulted only for its own market.
- catalyst_budget: 0 US + 0 EU + 0 AU + 0 APAC/Gulf = 0 lookups - the settlement pass performs NO new catalyst lookups (no research happens in this slot); every catalyst cell is merged from the 08:00 ET run's catalog, and a row may only use a catalog entry from its OWN region.
- earnings_tiers: fresh=1 near=1 (fresh = the row's earnings event is dated on the session that just settled, near = the previous session; measured over THIS table's rows - the 08:00 scan ranks the US rows by the same key)
- earnings_date_quality: 1 of 11 markets that publish rows here publish a FRESH earnings date (median age <= 14d); `us` and `au` publish 0 rows BY DESIGN (the US session is open at 12:15 ET and the AU rows belong to the 08:00 scan), not by a failed scan. The table below gives each market's rows, the rows with NO date at all, the median age of the published date and the rows within 7 and 30 days - the reader sees the input quality instead of trusting it
| market | rows | no date | median age | <=7d | <=30d |
|---|---|---|---|---|---|
| au | 0 | 0 | n/a | 0 | 0 |
| denmark | 2 | 0 | 89d | 1 | 1 |
| france | 4 | 0 | 54d | 0 | 2 |
| germany | 3 | 0 | 27d | 1 | 2 |
| italy | 4 | 0 | 118d | 0 | 0 |
| netherlands | 1 | 0 | 34d | 0 | 0 |
| norway | 4 | 0 | 13d | 2 | 4 |
| poland | 4 | 0 | 20d | 2 | 3 |
| spain | 1 | 0 | 19d | 0 | 1 |
| sweden | 4 | 0 | 26d | 0 | 3 |
| switzerland | 1 | 0 | 98d | 0 | 0 |
| uk | 1 | 0 | 109d | 0 | 0 |
| us | 0 | 0 | n/a | 0 | 0 |
- yahoo_calls: 30 | yahoo_429: 0 | yahoo_errors: 0 | yahoo_breaker: closed
- degraded_sources: 0
  (none - every source answered for every published row)

## Audit line

`earnings-reaction mode=settle target=earnings-reactions:2026-11-17 eu_rows=29 scan_matched=18 scan_to_settle_median_pp=0.805678391959793 catalyst_lookups=23 rows_dropped_stale_ref=1 degraded_sources=0`
