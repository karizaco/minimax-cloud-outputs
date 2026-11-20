# Earnings reaction scanner — 2026-11-19 (EU settlement pass)

- Cron: `15 12 * * 1-5` America/New_York (weekdays, 12:15 ET)
- Fire time (ET): 2026-11-19 12:15:00 Thu (REPLAY - the scheduled fire was blocked by the platform's Token Plan window; this run executed 2026-11-20 01:29:14 Fri, 794 min after the fire)
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
- morning_artifact: earnings/2026-11-19-reactions.md
- Status: `ok`

## TL;DR

- 26 EU/UK rows republished with their SETTLED close and move.
- 18 of them also appear in the 08:00 ET scan: the settled move
  differs from the scan move by a median of 0.97pp and a maximum of
  5.27pp; 8 of 18 rows moved more than 1pp
  between the scan and the close.
- Biggest settled EU/UK move: OROX (-15.01%, italy).

## EU/UK — Settled table

| Ticker | Market | Venue | Close | Chg % | Move @08:00 | Δ vs scan | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | Session asof | Settle | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| OROX | italy | MIL | 9.4 | -15.01 | -14.47 | -0.54 | EUR | 8.9x | 11.06 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| TRUE_B | sweden | OMXSTO | 26.09 | +12.41 | +7.45 | +4.96 | SEK | 3.2x | 23.21 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | settled | none | 2026-11-03 (16d ago) | — | pending catalyst lookup |
| SOI | france | EURONEXT | 109.25 | +12.01 | +17.18 | -5.17 | EUR | 2.1x | 97.54 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | settled | none | 2026-11-18 (1d ago) | — | no catalyst lookup (outside the per-run budget) |
| GRE | spain | BME | 55 | -9.39 | -4.12 | -5.27 | EUR | 2.7x | 60.70 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | settled | none | 2026-09-16 (64d ago) | — | pending catalyst lookup |
| BAB | uk | LSE | 1066.5 | +9.38 | +4.91 | +4.47 | GBX | 4.1x | 975.00 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | settled | none | 2026-11-19 (0d ago) | — | no catalyst lookup (outside the per-run budget) |
| BETCO_DKK | denmark | OMXCOP | 38.8 | -8.38 | -8.62 | +0.24 | DKK | 3.7x | 42.35 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | settled | none | 2026-11-18 (1d ago) | — | pending catalyst lookup |
| FMM_B | sweden | OMXSTO | 116.5 | +8.37 | +7.91 | +0.46 | SEK | 3.9x | 107.50 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | settled | none | 2026-11-05 (14d ago) | — | pending catalyst lookup |
| INVP | uk | LSE | 549.5 | -8.34 | -6.42 | -1.92 | GBX | 5.5x | 599.50 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | settled | none | 2026-11-19 (0d ago) | — | no catalyst lookup (outside the per-run budget) |
| NANO | france | EURONEXT | 25.94 | +7.72 | +4.73 | +2.99 | EUR | 1.9x | 24.08 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | settled | US line (NASDAQ:NA) | 2026-09-24 (56d ago) | — | no catalyst lookup (outside the per-run budget) |
| FG | sweden | OMXSTO | 15.26 | -6.84 | -7.81 | +0.97 | SEK | 2.0x | 16.38 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | settled | none | 2026-11-12 (7d ago) | — | pending catalyst lookup |
| IQMX | finland | OMXHEX | 6.56 | +6.75 | +4.96 | +1.79 | EUR | 1.5x | 6.14 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | settled | none | 2026-11-05 (14d ago) | — | no catalyst lookup (outside the per-run budget) |
| ELTEL | sweden | OMXSTO | 14.85 | -6.60 | — | — | SEK | 2.9x | 15.90 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | settled | none | 2026-10-29 (21d ago) | — | pending catalyst lookup |
| ACT0 | germany | XETR | 140.8 | -6.26 | -3.99 | -2.27 | EUR | 1.7x | 150.20 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | settled | none | 2026-10-28 (22d ago) | — | no catalyst lookup (outside the per-run budget) |
| SSPG | uk | LSE | 178.8 | -5.65 | -5.07 | -0.58 | GBX | 2.6x | 189.50 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | settled | none | 2026-05-19 (184d ago) | N | no fresh catalyst found - no dated company release found for 19 November; the move follows the prior session 8.6% rebound and FY26 results are due 8 December |
| SLR | spain | BME | 14.16 | -5.41 | -5.04 | -0.37 | EUR | 1.7x | 14.97 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | settled | none | 2026-11-19 (0d ago) | Y | 9M 2026 results (reported 2026-11-19): 9M revenue doubled to EUR260m, EBITDA EUR298.8m, up 30% and equal to 90% of the FY target, and net profit EUR177.9m, up 26%, on record output of +56%; EUR336m was invested in plants and batteries, part-funded by a EUR299.9m private placement, with capacity at 3.25GW heading to 3.52GW by year-end |
| LXS | germany | GETTEX | 11.92 | -5.40 | — | — | EUR | 3.1x | 12.55 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | settled | none | 2026-11-05 (14d ago) | — | no catalyst lookup (outside the per-run budget) |
| POS | austria | VIE | 33.9 | +4.95 | +4.64 | +0.31 | EUR | 3.5x | 32.30 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | settled | none | 2026-08-27 (84d ago) | — | no catalyst lookup (outside the per-run budget) |
| PLT | norway | OSL | 12.9 | +4.88 | — | — | NOK | 1.3x | 12.30 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | settled | none | 2026-08-06 (105d ago) | — | no catalyst lookup (outside the per-run budget) |
| PHM | spain | BME | 59.2 | -4.59 | -4.27 | -0.32 | EUR | 2.2x | 62.05 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | settled | none | 2026-10-29 (21d ago) | — | no catalyst lookup (outside the per-run budget) |
| EDEN | france | EURONEXT | 24.19 | -4.43 | — | — | EUR | 2.4x | 25.31 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | settled | none | 2026-07-22 (120d ago) | — | no catalyst lookup (outside the per-run budget) |
| ALO | france | EURONEXT | 8.9 | -4.34 | -4.62 | +0.28 | EUR | 1.3x | 9.30 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | settled | none | 2026-11-17 (2d ago) | — | no catalyst lookup (outside the per-run budget) |
| APR | norway | OSL | 34.7 | +4.20 | — | — | NOK | 1.1x | 33.30 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | settled | none | 2026-10-29 (21d ago) | — | pending catalyst lookup |
| SCHP | switzerland | SIX | 288.4 | -4.12 | — | — | CHF | 4.7x | 300.80 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | settled | none | 2026-07-21 (121d ago) | — | pending catalyst lookup |
| ZEAL | denmark | OMXCOP | 212.7 | -4.06 | — | — | DKK | 2.2x | 221.70 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | settled | none | 2026-11-12 (7d ago) | — | no catalyst lookup (outside the per-run budget) |
| BEAN | switzerland | SIX | 767 | +4.00 | +4.61 | -0.61 | CHF | 2.3x | 737.50 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | settled | none | 2026-07-20 (122d ago) | — | no catalyst lookup (outside the per-run budget) |
| HAUTO | norway | OSL | 173.7 | -3.98 | — | — | NOK | 2.6x | 180.90 | yahoo_chart_daily | 2026-11-18 | 2026-11-19 | settled | none | 2026-11-19 (0d ago) | — | pending catalyst lookup |

## Source health

- scanner_calls: 36 | scanner_errors: 0
- pipeline_version: 2026-11-20.1
- settlement: the EU/UK session is CLOSED at this fire, so every row's `Settle`
  cell reads `settled` and its move is the session's own move.
- morning_artifact: found locally
- catalyst_catalog: found locally
- catalyst_merge: region-matched - a row may only use a catalog entry from its OWN
  region; the same ticker on another venue is a different company and is not used.
- scan_to_settle: 18 rows compared with the 08:00 ET scan, median drift 0.97pp, max 5.27pp, 8 rows more than 1pp apart
- reference_close (screener vs Yahoo, resolved BEFORE the table was built): agree=26 mismatch=3 unverified=1 stale_reference=3
- rows_dropped_stale_ref: 3 | rows_dropped_unresolved_ref: 1
- earnings_field_stale_rows: 0 (the bulk earnings calendar reaches the US only, and this artifact publishes no US row, so the screener's own field is the only source for its dates - a stale date here is POSSIBLE and is not detected)
- earnings_dates: the published `Last earnings` date by source - catalog (researched) 1, calendar 0, asx 0, screener 25. The chain is researched -> calendar (US) -> ASX feed (AU) -> the screener's field, which is the FALLBACK and the one that lags. This pass publishes the EU/UK rows only, so its dates come from the researched catalog and the screener's field; no bulk calendar or ASX feed reaches a European venue - each bulk feed is consulted only for its own market.
- catalyst_budget: 0 US + 0 EU + 0 AU + 0 APAC/Gulf = 0 lookups - the settlement pass performs NO new catalyst lookups (no research happens in this slot); every catalyst cell is merged from the 08:00 ET run's catalog, and a row may only use a catalog entry from its OWN region.
- earnings_tiers: fresh=4 near=2 (fresh = the row's earnings event is dated on the session that just settled, near = the previous session; measured over THIS table's rows - the 08:00 scan ranks the US rows by the same key)
- earnings_date_quality: 3 of 11 markets that publish rows here publish a FRESH earnings date (median age <= 14d); `us` and `au` publish 0 rows BY DESIGN (the US session is open at 12:15 ET and the AU rows belong to the 08:00 scan), not by a failed scan. The table below gives each market's rows, the rows with NO date at all, the median age of the published date and the rows within 7 and 30 days - the reader sees the input quality instead of trusting it
| market | rows | no date | median age | <=7d | <=30d |
|---|---|---|---|---|---|
| au | 0 | 0 | n/a | 0 | 0 |
| austria | 1 | 0 | 84d | 0 | 0 |
| denmark | 2 | 0 | 7d | 2 | 2 |
| finland | 1 | 0 | 14d | 0 | 1 |
| france | 4 | 0 | 56d | 2 | 2 |
| germany | 2 | 0 | 22d | 0 | 2 |
| italy | 1 | 1 | n/a | 0 | 0 |
| norway | 3 | 0 | 21d | 1 | 2 |
| spain | 3 | 0 | 21d | 1 | 2 |
| sweden | 4 | 0 | 16d | 1 | 4 |
| switzerland | 2 | 0 | 122d | 0 | 0 |
| uk | 3 | 0 | 0d | 2 | 2 |
| us | 0 | 0 | n/a | 0 | 0 |
- yahoo_calls: 30 | yahoo_429: 0 | yahoo_errors: 1 | yahoo_breaker: closed
- degraded_sources: 2
  (the chat reply's `errors:` MUST equal this number - one entry per degraded
  source, not one per run)
  1. yahoo_chart_api.reference_close_unresolved — JD..L: the reference close could not be resolved (429 or a bad body)
  2. platform.fire_blocked — the scheduled 12:15 ET settlement fire was blocked by the platform and this run executed 794 min after it

## Audit line

`earnings-reaction mode=settle target=earnings-reactions:2026-11-19 eu_rows=26 scan_matched=18 scan_to_settle_median_pp=0.9723931623931668 catalyst_lookups=16 rows_dropped_stale_ref=3 degraded_sources=2`
