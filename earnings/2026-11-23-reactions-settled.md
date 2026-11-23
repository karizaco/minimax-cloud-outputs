# Earnings reaction scanner — 2026-11-23 (EU settlement pass)

- Cron: `15 12 * * 1-5` America/New_York (weekdays, 12:15 ET)
- Fire time (ET): 2026-11-23 12:16:14 Mon
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
- morning_artifact: earnings/2026-11-23-reactions.md
- Status: `ok`

## TL;DR

- 27 EU/UK rows republished with their SETTLED close and move.
- 11 of them also appear in the 08:00 ET scan: the settled move
  differs from the scan move by a median of 4.11pp and a maximum of
  6.66pp; 10 of 11 rows moved more than 1pp
  between the scan and the close.
- Biggest settled EU/UK move: SIVE (+18.58%, sweden).

## EU/UK — Settled table

| Ticker | Market | Venue | Close | Chg % | Move @08:00 | Δ vs scan | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | Session asof | Settle | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SIVE | sweden | OMXSTO | 13.53 | +18.58 | +11.92 | +6.66 | SEK | 2.7x | 11.41 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | settled | none | 2026-08-27 (88d ago) | N | Q3 2026 interim report postponed from 26 Nov to 30 Nov (announced 23 Nov, US Thanksgiving clash); a new public short seller was disclosed on 20 Nov |
| HUNT | norway | OSL | 19.1 | +17.47 | +14.51 | +2.96 | NOK | 4.0x | 16.26 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | settled | none | 2026-11-20 (3d ago) | — | no catalyst lookup (outside the per-run budget) |
| JEN | germany | XETR | 36.06 | +13.32 | +8.55 | +4.77 | EUR | 3.9x | 31.82 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | settled | none | 2026-11-10 (13d ago) | — | no catalyst lookup (outside the per-run budget) |
| ATS | austria | VIE | 110.2 | +13.03 | — | — | EUR | 2.3x | 97.50 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | settled | none | 2026-11-05 (18d ago) | — | pending catalyst lookup |
| FRVIA | france | EURONEXT | 8.282 | +10.52 | +5.79 | +4.73 | EUR | 4.3x | 7.49 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | settled | none | 2026-07-31 (115d ago) | — | no catalyst lookup (outside the per-run budget) |
| SILEX | sweden | OMXSTO | 141 | +10.29 | — | — | SEK | 2.8x | 127.85 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | settled | US line (OTC:SILXF) | 2026-11-04 (19d ago) | — | pending catalyst lookup |
| HTRO | sweden | OMXSTO | 40.36 | +9.44 | — | — | SEK | 2.4x | 36.88 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | settled | none | 2026-10-22 (32d ago) | — | pending catalyst lookup |
| BESI | netherlands | EURONEXT | 155.9 | +9.25 | +4.48 | +4.77 | EUR | 3.0x | 142.70 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | settled | none | 2026-10-21 (33d ago) | — | no catalyst lookup (outside the per-run budget) |
| AG1 | germany | XETR | 14.91 | +9.23 | — | — | EUR | 2.9x | 13.65 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | settled | none | 2026-11-04 (19d ago) | — | pending catalyst lookup |
| ASML | netherlands | EURONEXT | 1272.2 | +8.92 | +4.81 | +4.11 | EUR | 2.5x | 1168.00 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | settled | ADR (NASDAQ:ASML) | 2026-10-14 (40d ago) | N | chip-equipment sector rebound after Nvidia's stronger-than-expected Q3 (ASML +3-5% with ASM Intl and BE Semiconductor); no ASML release today |
| NOKIA | finland | OMXHEX | 7.018 | +8.91 | — | — | EUR | 2.5x | 6.44 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | settled | ADR (NYSE:NOK) | 2026-10-22 (32d ago) | — | pending catalyst lookup |
| TPRO | italy | MIL | 20.02 | +8.75 | +4.18 | +4.57 | EUR | 2.0x | 18.41 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | settled | none | 2026-08-05 (110d ago) | — | no catalyst lookup (outside the per-run budget) |
| ASM | netherlands | EURONEXT | 692.6 | +8.29 | — | — | EUR | 2.2x | 639.60 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | settled | US line (OTC:ASMXF) | 2026-10-27 (27d ago) | — | pending catalyst lookup |
| NOD | norway | OSL | 180 | +7.46 | — | — | NOK | 3.0x | 167.50 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | settled | none | 2026-10-22 (32d ago) | — | pending catalyst lookup |
| BETCO_DKK | denmark | OMXCOP | 40.05 | +7.23 | +5.62 | +1.61 | DKK | 3.6x | 37.35 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | settled | none | 2026-11-18 (5d ago) | — | no catalyst lookup (outside the per-run budget) |
| CRNA | norway | OSL | 10.1 | +7.22 | +4.25 | +2.97 | NOK | 3.0x | 9.42 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| SENS | switzerland | SIX | 78.8 | +7.21 | — | — | CHF | 2.9x | 73.50 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | settled | none | 2026-08-19 (96d ago) | — | no catalyst lookup (outside the per-run budget) |
| GL9 | ireland | EURONEXT | 17.92 | -6.91 | -6.55 | -0.36 | EUR | 2.7x | 19.25 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | settled | none | 2026-08-06 (109d ago) | — | no catalyst lookup (outside the per-run budget) |
| COTN | switzerland | SIX | 297.4 | +6.90 | — | — | CHF | 2.3x | 278.20 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | settled | none | 2026-07-31 (115d ago) | — | no catalyst lookup (outside the per-run budget) |
| PAX | sweden | OMXSTO | 68.6 | +6.85 | — | — | SEK | 3.1x | 64.20 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | settled | none | 2026-11-20 (3d ago) | — | pending catalyst lookup |
| MDATA | norway | OSL | 13 | +6.73 | +3.94 | +2.79 | NOK | 2.9x | 12.18 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | settled | none | 2026-10-30 (24d ago) | — | no catalyst lookup (outside the per-run budget) |
| OXIG | uk | LSE | 2542 | +6.72 | — | — | GBX | 2.6x | 2382.00 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | settled | none | 2026-11-10 (13d ago) | — | no catalyst lookup (outside the per-run budget) |
| KGH | poland | GPW | 257.75 | +6.64 | — | — | PLN | 2.1x | 241.70 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | settled | none | 2026-11-17 (6d ago) | — | no catalyst lookup (outside the per-run budget) |
| UMI | belgium | EURONEXT | 16.88 | +6.57 | — | — | EUR | 2.4x | 15.84 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | settled | none | 2026-07-31 (115d ago) | — | pending catalyst lookup |
| PRY | italy | MIL | 107.05 | +6.52 | — | — | EUR | 2.2x | 100.50 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | settled | none | 2026-10-29 (25d ago) | — | no catalyst lookup (outside the per-run budget) |
| SPG | denmark | OMXCOP | 425 | +6.25 | — | — | DKK | 3.8x | 400.00 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | settled | none | 2026-11-17 (6d ago) | — | no catalyst lookup (outside the per-run budget) |
| IFCN | switzerland | SIX | 157 | +6.08 | — | — | CHF | 2.3x | 148.00 | yahoo_chart_daily | 2026-11-20 | 2026-11-23 | settled | none | 2026-07-30 (116d ago) | — | no catalyst lookup (outside the per-run budget) |

## Source health

- scanner_calls: 36 | scanner_errors: 0
- pipeline_version: 2026-11-20.1
- settlement: the EU/UK session is CLOSED at this fire, so every row's `Settle`
  cell reads `settled` and its move is the session's own move.
- morning_artifact: found locally
- catalyst_catalog: found locally
- catalyst_merge: region-matched - a row may only use a catalog entry from its OWN
  region; the same ticker on another venue is a different company and is not used.
- scan_to_settle: 11 rows compared with the 08:00 ET scan, median drift 4.11pp, max 6.66pp, 10 rows more than 1pp apart
- reference_close (screener vs Yahoo, resolved BEFORE the table was built): agree=27 mismatch=3 unverified=0 stale_reference=3
- rows_dropped_stale_ref: 3 | rows_dropped_unresolved_ref: 0
- earnings_field_stale_rows: 0 (the bulk earnings calendar reaches the US only, and this artifact publishes no US row, so the screener's own field is the only source for its dates - a stale date here is POSSIBLE and is not detected)
- earnings_dates: the published `Last earnings` date by source - catalog (researched) 0, calendar 0, asx 0, screener 27. The chain is researched -> calendar (US) -> ASX feed (AU) -> the screener's field, which is the FALLBACK and the one that lags. This pass publishes the EU/UK rows only, so its dates come from the researched catalog and the screener's field; no bulk calendar or ASX feed reaches a European venue - each bulk feed is consulted only for its own market.
- catalyst_budget: 0 US + 0 EU + 0 AU + 0 APAC/Gulf = 0 lookups - the settlement pass performs NO new catalyst lookups (no research happens in this slot); every catalyst cell is merged from the 08:00 ET run's catalog, and a row may only use a catalog entry from its OWN region.
- earnings_tiers: fresh=0 near=2 (fresh = the row's earnings event is dated on the session that just settled, near = the previous session; measured over THIS table's rows - the 08:00 scan ranks the US rows by the same key)
- earnings_date_quality: 3 of 14 markets that publish rows here publish a FRESH earnings date (median age <= 14d); `us` and `au` publish 0 rows BY DESIGN (the US session is open at 12:15 ET and the AU rows belong to the 08:00 scan), not by a failed scan. The table below gives each market's rows, the rows with NO date at all, the median age of the published date and the rows within 7 and 30 days - the reader sees the input quality instead of trusting it
| market | rows | no date | median age | <=7d | <=30d |
|---|---|---|---|---|---|
| au | 0 | 0 | n/a | 0 | 0 |
| austria | 1 | 0 | 18d | 0 | 1 |
| belgium | 1 | 0 | 115d | 0 | 0 |
| denmark | 2 | 0 | 6d | 2 | 2 |
| finland | 1 | 0 | 32d | 0 | 0 |
| france | 1 | 0 | 115d | 0 | 0 |
| germany | 2 | 0 | 19d | 0 | 2 |
| ireland | 1 | 0 | 109d | 0 | 0 |
| italy | 2 | 0 | 110d | 0 | 1 |
| netherlands | 3 | 0 | 33d | 0 | 1 |
| norway | 4 | 1 | 24d | 1 | 2 |
| poland | 1 | 0 | 6d | 1 | 1 |
| sweden | 4 | 0 | 32d | 1 | 2 |
| switzerland | 3 | 0 | 115d | 0 | 0 |
| uk | 1 | 0 | 13d | 0 | 1 |
| us | 0 | 0 | n/a | 0 | 0 |
- yahoo_calls: 30 | yahoo_429: 0 | yahoo_errors: 0 | yahoo_breaker: closed
- degraded_sources: 0
  (none - every source answered for every published row)

## Audit line

`earnings-reaction mode=settle target=earnings-reactions:2026-11-23 eu_rows=27 scan_matched=11 scan_to_settle_median_pp=4.111232876712333 catalyst_lookups=19 rows_dropped_stale_ref=3 degraded_sources=0`
