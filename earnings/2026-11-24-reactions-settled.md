# Earnings reaction scanner — 2026-11-24 (EU settlement pass)

- Cron: `15 12 * * 1-5` America/New_York (weekdays, 12:15 ET)
- Fire time (ET): 2026-11-24 12:16:27 Tue
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
- morning_artifact: earnings/2026-11-24-reactions.md
- Status: `ok`

## TL;DR

- 29 EU/UK rows republished with their SETTLED close and move.
- 19 of them also appear in the 08:00 ET scan: the settled move
  differs from the scan move by a median of 3.05pp and a maximum of
  6.17pp; 14 of 19 rows moved more than 1pp
  between the scan and the close.
- Biggest settled EU/UK move: NDA (-14.97%, germany).

## EU/UK — Settled table

| Ticker | Market | Venue | Close | Chg % | Move @08:00 | Δ vs scan | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | Session asof | Settle | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NDA | germany | XETR | 107.9 | -14.97 | -11.66 | -3.31 | EUR | 5.5x | 126.90 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | settled | none | 2026-08-06 (110d ago) | N | Aurubis cut its FY2026/27 earnings outlook on extended delays at its Richmond, Georgia copper smelter, knocking about 10% off the shares on 2026-11-23 and leaving them down further today |
| SZG | germany | XETR | 40.4 | -13.38 | -8.53 | -4.85 | EUR | 3.4x | 46.64 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | settled | none | 2026-11-12 (12d ago) | — | no catalyst lookup (outside the per-run budget) |
| VER | sweden | OMXSTO | 6.7 | -12.99 | -7.01 | -5.98 | SEK | 3.6x | 7.70 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | settled | none | 2026-11-23 (1d ago) | — | no catalyst lookup (outside the per-run budget) |
| SIVE | sweden | OMXSTO | 11.78 | -12.93 | — | — | SEK | 1.7x | 13.53 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | settled | none | 2026-08-27 (89d ago) | — | pending catalyst lookup |
| AMS2 | austria | VIE | 13.15 | -12.91 | — | — | EUR | 2.3x | 15.10 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | settled | none | 2026-11-13 (11d ago) | — | pending catalyst lookup |
| ATS | austria | VIE | 96.6 | -12.34 | -6.17 | -6.17 | EUR | 2.0x | 110.20 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | settled | none | 2026-11-05 (19d ago) | — | pending catalyst lookup |
| TPRO | italy | MIL | 18 | -10.09 | -4.65 | -5.44 | EUR | 2.1x | 20.02 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | settled | none | 2026-08-05 (111d ago) | — | no catalyst lookup (outside the per-run budget) |
| SOI | france | EURONEXT | 91.38 | -9.97 | -6.92 | -3.05 | EUR | 1.5x | 101.50 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | settled | none | 2026-11-18 (6d ago) | — | no catalyst lookup (outside the per-run budget) |
| SAN | france | EURONEXT | 93.58 | +9.76 | +6.59 | +3.17 | EUR | 5.2x | 85.26 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| JEN | germany | XETR | 32.56 | -9.71 | — | — | EUR | 2.6x | 36.06 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | settled | none | 2026-11-10 (14d ago) | — | no catalyst lookup (outside the per-run budget) |
| PCELL | sweden | OMXSTO | 17.05 | -9.60 | — | — | SEK | 2.0x | 18.86 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | settled | none | 2026-10-22 (33d ago) | — | pending catalyst lookup |
| MUR | poland | GPW | 34.9 | -9.35 | -9.35 | -0.00 | PLN | 7.8x | 38.50 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | settled | none | 2026-09-15 (70d ago) | N | Ex-dividend date 2026-11-24 with a PLN 2.94 dividend, roughly 7.6% of the 38.50 PLN reference close; next results are scheduled for 2026-11-25 |
| KGH | poland | GPW | 234.25 | -9.12 | -5.49 | -3.63 | PLN | 2.6x | 257.75 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | settled | none | 2026-11-17 (7d ago) | — | no catalyst lookup (outside the per-run budget) |
| BESI | netherlands | EURONEXT | 142.2 | -8.79 | -4.71 | -4.08 | EUR | 2.5x | 155.90 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | settled | none | 2026-10-21 (34d ago) | — | no catalyst lookup (outside the per-run budget) |
| TOM | norway | OSL | 79.55 | -8.77 | -7.80 | -0.97 | NOK | 4.7x | 87.20 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | settled | none | 2026-10-23 (32d ago) | — | pending catalyst lookup |
| EMEIS | france | EURONEXT | 10.97 | +8.08 | +8.08 | -0.00 | EUR | 3.6x | 10.15 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | settled | none | 2026-07-29 (118d ago) | — | no catalyst lookup (outside the per-run budget) |
| ANTO | uk | LSE | 2546 | -8.05 | -6.12 | -1.93 | GBX | 2.4x | 2769.00 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | settled | none | 2026-08-13 (103d ago) | — | no catalyst lookup (outside the per-run budget) |
| PRY | italy | MIL | 98.44 | -8.04 | -4.76 | -3.28 | EUR | 2.5x | 107.05 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | settled | none | 2026-10-29 (26d ago) | — | no catalyst lookup (outside the per-run budget) |
| ASM | netherlands | EURONEXT | 637.4 | -7.97 | — | — | EUR | 2.0x | 692.60 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | settled | US line (OTC:ASMXF) | 2026-10-27 (28d ago) | — | no catalyst lookup (outside the per-run budget) |
| GENO | norway | OSL | 14.5 | -7.88 | -5.97 | -1.91 | NOK | 2.0x | 15.74 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | settled | none | 2026-11-12 (12d ago) | — | no catalyst lookup (outside the per-run budget) |
| COTN | switzerland | SIX | 274.2 | -7.80 | — | — | CHF | 2.4x | 297.40 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | settled | none | 2026-07-31 (116d ago) | — | no catalyst lookup (outside the per-run budget) |
| FNM | sweden | OMXSTO | 114.5 | +7.51 | +7.51 | +0.00 | SEK | 1.9x | 106.50 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | settled | none | 2026-11-11 (13d ago) | — | pending catalyst lookup |
| HUNT | norway | OSL | 20.45 | +7.07 | +8.64 | -1.57 | NOK | 1.6x | 19.10 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | settled | none | 2026-11-20 (4d ago) | — | no catalyst lookup (outside the per-run budget) |
| IQMX | finland | OMXHEX | 5.825 | -6.73 | — | — | EUR | 1.3x | 6.25 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | settled | none | 2026-11-05 (19d ago) | — | no catalyst lookup (outside the per-run budget) |
| GMAB | denmark | OMXCOP | 3809 | +6.72 | — | — | DKK | 3.0x | 3569.00 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | settled | none | 2026-11-05 (19d ago) | — | no catalyst lookup (outside the per-run budget) |
| MAERSK_B | denmark | OMXCOP | 18855 | -6.70 | — | — | DKK | 3.5x | 20210.00 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | settled | US line (OTC:AMKAF) | 2026-11-05 (19d ago) | — | pending catalyst lookup |
| METSO | finland | OMXHEX | 14.22 | -6.69 | — | — | EUR | 2.9x | 15.24 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | settled | ADR (OTC:OUKPY) | 2026-10-22 (33d ago) | — | pending catalyst lookup |
| NOD | norway | OSL | 168 | -6.67 | -4.72 | -1.95 | NOK | 2.4x | 180.00 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | settled | none | 2026-10-22 (33d ago) | — | pending catalyst lookup |
| TOR | poland | GPW | 49.95 | -6.64 | -6.17 | -0.47 | PLN | 3.3x | 53.50 | yahoo_chart_daily | 2026-11-23 | 2026-11-24 | settled | none | 2026-08-20 (96d ago) | — | no catalyst lookup (outside the per-run budget) |

## Source health

- scanner_calls: 36 | scanner_errors: 0
- pipeline_version: 2026-11-20.1
- settlement: the EU/UK session is CLOSED at this fire, so every row's `Settle`
  cell reads `settled` and its move is the session's own move.
- morning_artifact: found locally
- catalyst_catalog: found locally
- catalyst_merge: region-matched - a row may only use a catalog entry from its OWN
  region; the same ticker on another venue is a different company and is not used.
- scan_to_settle: 19 rows compared with the 08:00 ET scan, median drift 3.05pp, max 6.17pp, 14 rows more than 1pp apart
- reference_close (screener vs Yahoo, resolved BEFORE the table was built): agree=29 mismatch=1 unverified=0 stale_reference=1
- rows_dropped_stale_ref: 1 | rows_dropped_unresolved_ref: 0
- earnings_field_stale_rows: 0 (the bulk earnings calendar reaches the US only, and this artifact publishes no US row, so the screener's own field is the only source for its dates - a stale date here is POSSIBLE and is not detected)
- earnings_dates: the published `Last earnings` date by source - catalog (researched) 0, calendar 0, asx 0, screener 29. The chain is researched -> calendar (US) -> ASX feed (AU) -> the screener's field, which is the FALLBACK and the one that lags. This pass publishes the EU/UK rows only, so its dates come from the researched catalog and the screener's field; no bulk calendar or ASX feed reaches a European venue - each bulk feed is consulted only for its own market.
- catalyst_budget: 0 US + 0 EU + 0 AU + 0 APAC/Gulf = 0 lookups - the settlement pass performs NO new catalyst lookups (no research happens in this slot); every catalyst cell is merged from the 08:00 ET run's catalog, and a row may only use a catalog entry from its OWN region.
- earnings_tiers: fresh=0 near=1 (fresh = the row's earnings event is dated on the session that just settled, near = the previous session; measured over THIS table's rows - the 08:00 scan ranks the US rows by the same key)
- earnings_date_quality: 1 of 12 markets that publish rows here publish a FRESH earnings date (median age <= 14d); `us` and `au` publish 0 rows BY DESIGN (the US session is open at 12:15 ET and the AU rows belong to the 08:00 scan), not by a failed scan. The table below gives each market's rows, the rows with NO date at all, the median age of the published date and the rows within 7 and 30 days - the reader sees the input quality instead of trusting it
| market | rows | no date | median age | <=7d | <=30d |
|---|---|---|---|---|---|
| au | 0 | 0 | n/a | 0 | 0 |
| austria | 2 | 0 | 19d | 0 | 2 |
| denmark | 2 | 0 | 19d | 0 | 2 |
| finland | 2 | 0 | 33d | 0 | 1 |
| france | 3 | 1 | 118d | 1 | 1 |
| germany | 3 | 0 | 14d | 0 | 2 |
| italy | 2 | 0 | 111d | 0 | 1 |
| netherlands | 2 | 0 | 34d | 0 | 1 |
| norway | 4 | 0 | 32d | 1 | 2 |
| poland | 3 | 0 | 70d | 1 | 1 |
| sweden | 4 | 0 | 33d | 1 | 2 |
| switzerland | 1 | 0 | 116d | 0 | 0 |
| uk | 1 | 0 | 103d | 0 | 0 |
| us | 0 | 0 | n/a | 0 | 0 |
- yahoo_calls: 30 | yahoo_429: 0 | yahoo_errors: 0 | yahoo_breaker: closed
- degraded_sources: 0
  (none - every source answered for every published row)

## Audit line

`earnings-reaction mode=settle target=earnings-reactions:2026-11-24 eu_rows=29 scan_matched=19 scan_to_settle_median_pp=3.0504433497536994 catalyst_lookups=16 rows_dropped_stale_ref=1 degraded_sources=0`
