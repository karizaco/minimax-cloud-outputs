# Earnings reaction scanner — 2026-11-18 (EU settlement pass)

- Cron: `15 12 * * 1-5` America/New_York (weekdays, 12:15 ET)
- Fire time (ET): 2026-11-18 12:18:52 Wed
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
- morning_artifact: earnings/2026-11-18-reactions.md
- Status: `ok`

## TL;DR

- 29 EU/UK rows republished with their SETTLED close and move.
- 15 of them also appear in the 08:00 ET scan: the settled move
  differs from the scan move by a median of 1.14pp and a maximum of
  2.95pp; 8 of 15 rows moved more than 1pp
  between the scan and the close.
- Biggest settled EU/UK move: CTEC (+9.40%, uk).

## EU/UK — Settled table

| Ticker | Market | Venue | Close | Chg % | Move @08:00 | Δ vs scan | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | Session asof | Settle | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CTEC | uk | LSE | 270 | +9.40 | +9.97 | -0.57 | GBX | 5.8x | 246.80 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | settled | none | 2026-08-04 (106d ago) | — | no catalyst lookup (outside the per-run budget) |
| SEYE | sweden | OMXSTO | 51.5 | +9.39 | +8.75 | +0.64 | SEK | 3.1x | 47.08 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | settled | none | 2026-11-17 (1d ago) | — | no catalyst lookup (outside the per-run budget) |
| SSPG | uk | LSE | 189.5 | +8.60 | — | — | GBX | 4.6x | 174.50 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | settled | none | 2026-05-19 (183d ago) | — | pending catalyst lookup |
| HOC | uk | LSE | 405.4 | -8.36 | -5.52 | -2.84 | GBX | 2.6x | 442.40 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | settled | none | 2026-08-26 (84d ago) | — | no catalyst lookup (outside the per-run budget) |
| ANTO | uk | LSE | 2782 | -7.85 | -5.20 | -2.65 | GBX | 2.6x | 3019.00 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | settled | none | 2026-08-13 (97d ago) | — | no catalyst lookup (outside the per-run budget) |
| DAD | poland | GPW | 84.7 | -7.53 | -10.48 | +2.95 | PLN | 4.6x | 91.60 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | settled | none | 2026-11-17 (1d ago) | — | no catalyst lookup (outside the per-run budget) |
| ALO | france | EURONEXT | 9.304 | -7.15 | -7.78 | +0.63 | EUR | 2.3x | 10.02 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | settled | none | 2026-11-17 (1d ago) | — | no catalyst lookup (outside the per-run budget) |
| GRE | spain | BME | 60.7 | -6.90 | — | — | EUR | 2.2x | 65.20 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | settled | none | 2026-09-16 (63d ago) | — | pending catalyst lookup |
| CDR | poland | GPW | 282.9 | +6.84 | — | — | PLN | 3.8x | 264.80 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | settled | none | 2026-09-02 (77d ago) | — | pending catalyst lookup |
| SVEAF_B | sweden | OMXSTO | 33.76 | +6.77 | — | — | SEK | 5.1x | 31.62 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | settled | none | 2026-07-16 (125d ago) | — | pending catalyst lookup |
| GUBRA | denmark | OMXCOP | 269.8 | -6.64 | — | — | DKK | 2.3x | 289.00 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | settled | none | 2026-08-20 (90d ago) | — | no catalyst lookup (outside the per-run budget) |
| DRW3 | germany | XETR | 119 | +6.63 | — | — | EUR | 3.1x | 111.60 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | settled | none | 2026-10-29 (20d ago) | — | no catalyst lookup (outside the per-run budget) |
| HEM | sweden | OMXSTO | 50.45 | -6.49 | -5.75 | -0.74 | SEK | 1.7x | 53.95 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | settled | none | 2026-10-22 (27d ago) | — | pending catalyst lookup |
| REP | spain | BME | 28.71 | -6.42 | — | — | EUR | 2.8x | 30.68 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | settled | none | 2026-10-29 (20d ago) | — | no catalyst lookup (outside the per-run budget) |
| XPLRA | norway | OSL | 22.4 | -6.28 | -3.97 | -2.31 | NOK | 1.8x | 23.90 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | settled | none | 2026-11-12 (6d ago) | — | no catalyst lookup (outside the per-run budget) |
| PEN | norway | OSL | 28.4 | -6.27 | -4.79 | -1.48 | NOK | 2.8x | 30.30 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | settled | none | 2026-11-18 (0d ago) | Y | Panoro Energy: Q3 2026 trading statement (reported 2026-11-18): revenue USD 114.3m, IFRS EBITDA USD 33.8m, record pro forma production of 20,049 boepd, the FY26 pro forma forecast raised to about 19,000 boepd and a NOK 50m cash distribution (NOK 0.356/sh) - but capex guidance was withdrawn after the 24 Oct Prospector 5 rig sinking at Dussafu (four fatalities) and the MaBoMo Phase 2 drilling delay; the shares fell 4.8% to NOK 28.85 |
| AFX | germany | XETR | 32.26 | -6.22 | — | — | EUR | 4.7x | 34.40 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | settled | none | 2026-05-12 (190d ago) | — | pending catalyst lookup |
| KGH | poland | GPW | 248.2 | -6.09 | -4.88 | -1.21 | PLN | 2.2x | 264.30 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | settled | none | 2026-08-18 (92d ago) | N | KGHM: the copper and silver sell-off hit the shares -4.9% to about PLN 252, a 2026 low and a sixth straight down session - with copper at its lowest since May (about -4% on the day to multi-month lows) and silver its weakest since October 2025; a broad metals de-rating, not an earnings reaction, and the Q3/9M 2026 report is due after today's close (consensus revenue PLN 12.4bn, adjusted EBITDA PLN 3.56bn) |
| FLAT_B | sweden | OMXSTO | 9.59 | +5.97 | — | — | SEK | 2.7x | 9.05 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| VU | france | EURONEXT | 142.9 | -5.86 | -4.22 | -1.64 | EUR | 2.1x | 151.80 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | settled | none | 2026-09-21 (58d ago) | — | no catalyst lookup (outside the per-run budget) |
| NEM | germany | XETR | 57.4 | -5.82 | — | — | EUR | 2.3x | 60.95 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | settled | none | 2026-11-05 (13d ago) | — | no catalyst lookup (outside the per-run budget) |
| MDV | poland | GPW | 114.45 | +5.39 | — | — | PLN | 1.9x | 108.60 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | settled | none | 2026-08-07 (103d ago) | — | pending catalyst lookup |
| GENO | norway | OSL | 15.5 | -5.26 | — | — | NOK | 1.3x | 16.36 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | settled | none | 2026-11-12 (6d ago) | — | no catalyst lookup (outside the per-run budget) |
| PRX | netherlands | EURONEXT | 32.525 | -5.05 | -5.37 | +0.32 | EUR | 3.3x | 34.26 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | settled | none | 2026-06-29 (142d ago) | — | pending catalyst lookup |
| IQMX | finland | OMXHEX | 6.145 | +4.86 | +4.52 | +0.34 | EUR | 1.1x | 5.86 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | settled | none | 2026-11-05 (13d ago) | — | no catalyst lookup (outside the per-run budget) |
| SMOP | norway | OSL | 55 | +4.56 | +5.70 | -1.14 | NOK | 1.4x | 52.60 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | settled | none | 2026-10-29 (20d ago) | — | no catalyst lookup (outside the per-run budget) |
| FLS | denmark | OMXCOP | 485 | -4.53 | — | — | DKK | 1.8x | 508.00 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | settled | none | 2026-11-11 (7d ago) | — | no catalyst lookup (outside the per-run budget) |
| HLUN_A | denmark | OMXCOP | 60.4 | +4.50 | +5.19 | -0.69 | DKK | 2.2x | 57.80 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| MOH | greece | ATHEX | 60.3 | -4.36 | — | — | EUR | 2.3x | 63.05 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | settled | none | 2026-08-25 (85d ago) | — | pending catalyst lookup |

## Source health

- scanner_calls: 36 | scanner_errors: 0
- pipeline_version: 2026-11-16.2
- settlement: the EU/UK session is CLOSED at this fire, so every row's `Settle`
  cell reads `settled` and its move is the session's own move.
- morning_artifact: found locally
- catalyst_catalog: found locally
- catalyst_merge: region-matched - a row may only use a catalog entry from its OWN
  region; the same ticker on another venue is a different company and is not used.
- scan_to_settle: 15 rows compared with the 08:00 ET scan, median drift 1.14pp, max 2.95pp, 8 rows more than 1pp apart
- reference_close (screener vs Yahoo, resolved BEFORE the table was built): agree=29 mismatch=1 unverified=0 stale_reference=1
- rows_dropped_stale_ref: 1 | rows_dropped_unresolved_ref: 0
- earnings_field_stale_rows: 0 (the bulk earnings calendar reaches the US only, and this artifact publishes no US row, so the screener's own field is the only source for its dates - a stale date here is POSSIBLE and is not detected)
- earnings_dates: the published `Last earnings` date by source - catalog (researched) 1, calendar 0, asx 0, screener 28. The chain is researched -> calendar (US) -> ASX feed (AU) -> the screener's field, which is the FALLBACK and the one that lags. This pass publishes the EU/UK rows only, so its dates come from the researched catalog and the screener's field; no bulk calendar or ASX feed reaches a European venue - each bulk feed is consulted only for its own market.
- catalyst_budget: 0 US + 0 EU + 0 AU + 0 APAC/Gulf = 0 lookups - the settlement pass performs NO new catalyst lookups (no research happens in this slot); every catalyst cell is merged from the 08:00 ET run's catalog, and a row may only use a catalog entry from its OWN region.
- earnings_tiers: fresh=1 near=3 (fresh = the row's earnings event is dated on the session that just settled, near = the previous session; measured over THIS table's rows - the 08:00 scan ranks the US rows by the same key)
- earnings_date_quality: 2 of 11 markets that publish rows here publish a FRESH earnings date (median age <= 14d); `us` and `au` publish 0 rows BY DESIGN (the US session is open at 12:15 ET and the AU rows belong to the 08:00 scan), not by a failed scan. The table below gives each market's rows, the rows with NO date at all, the median age of the published date and the rows within 7 and 30 days - the reader sees the input quality instead of trusting it
| market | rows | no date | median age | <=7d | <=30d |
|---|---|---|---|---|---|
| au | 0 | 0 | n/a | 0 | 0 |
| denmark | 3 | 1 | 90d | 1 | 1 |
| finland | 1 | 0 | 13d | 0 | 1 |
| france | 2 | 0 | 58d | 1 | 1 |
| germany | 3 | 0 | 20d | 0 | 2 |
| greece | 1 | 0 | 85d | 0 | 0 |
| netherlands | 1 | 0 | 142d | 0 | 0 |
| norway | 4 | 0 | 6d | 3 | 4 |
| poland | 4 | 0 | 92d | 1 | 1 |
| spain | 2 | 0 | 63d | 0 | 1 |
| sweden | 4 | 1 | 27d | 1 | 2 |
| uk | 4 | 0 | 106d | 0 | 0 |
| us | 0 | 0 | n/a | 0 | 0 |
- yahoo_calls: 30 | yahoo_429: 0 | yahoo_errors: 0 | yahoo_breaker: closed
- degraded_sources: 0
  (none - every source answered for every published row)

## Audit line

`earnings-reaction mode=settle target=earnings-reactions:2026-11-18 eu_rows=29 scan_matched=15 scan_to_settle_median_pp=1.1372623574144516 catalyst_lookups=16 rows_dropped_stale_ref=1 degraded_sources=0`
