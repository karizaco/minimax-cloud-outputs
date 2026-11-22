# Earnings reaction scanner — 2026-11-20 (EU settlement pass)

- Cron: `15 12 * * 1-5` America/New_York (weekdays, 12:15 ET)
- Fire time (ET): 2026-11-20 12:15:00 Fri (REPLAY - the scheduled fire was blocked by the platform's Token Plan window; this run executed 2026-11-22 00:50:13 Sun, 2195 min after the fire)
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
- morning_artifact: earnings/2026-11-20-reactions.md
- Status: `ok`

## TL;DR

- 29 EU/UK rows republished with their SETTLED close and move.
- 17 of them also appear in the 08:00 ET scan: the settled move
  differs from the scan move by a median of 1.85pp and a maximum of
  5.62pp; 12 of 17 rows moved more than 1pp
  between the scan and the close.
- Biggest settled EU/UK move: PCELL (+31.79%, sweden).

## EU/UK — Settled table

| Ticker | Market | Venue | Close | Chg % | Move @08:00 | Δ vs scan | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | Session asof | Settle | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PCELL | sweden | OMXSTO | 19.4 | +31.79 | — | — | SEK | 7.4x | 14.72 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | settled | none | 2026-10-22 (29d ago) | — | pending catalyst lookup |
| ABVX | france | EURONEXT | 63 | -17.21 | — | — | EUR | 6.0x | 76.10 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | settled | none | 2026-09-21 (60d ago) | — | pending catalyst lookup |
| SIVE | sweden | OMXSTO | 11.41 | -16.65 | -11.03 | -5.62 | SEK | 2.7x | 13.69 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | settled | none | 2026-08-27 (85d ago) | N | No issuer release (the Q3 interim is not due until 26 Nov): the stock fell with the global AI and semiconductor selloff, and Millennium International disclosed a new public short position of more than 0.5% of capital |
| VK | france | EURONEXT | 15.475 | -14.57 | -11.32 | -3.25 | EUR | 7.4x | 18.11 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| ATS | austria | VIE | 97.5 | -14.47 | -10.53 | -3.94 | EUR | 2.6x | 114.00 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | settled | none | 2026-11-05 (15d ago) | — | pending catalyst lookup |
| KEOC | sweden | OMXSTO | 5.14 | -12.29 | — | — | SEK | 2.9x | 5.86 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | settled | none | 2026-08-31 (81d ago) | — | pending catalyst lookup |
| SOI | france | EURONEXT | 96.3 | -11.85 | -10.00 | -1.85 | EUR | 1.9x | 109.25 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | settled | none | 2026-11-18 (2d ago) | — | no catalyst lookup (outside the per-run budget) |
| JEN | germany | XETR | 31.82 | -11.76 | — | — | EUR | 4.2x | 36.06 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | settled | none | 2026-11-10 (10d ago) | — | no catalyst lookup (outside the per-run budget) |
| HUNT | norway | OSL | 16.26 | -9.67 | -10.33 | +0.66 | NOK | 2.4x | 18.00 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | settled | none | 2026-11-20 (0d ago) | N | The Jacktel bid is the driver: a NOK 1.63bn cash-funded purchase order at NOK 6.30 per Jacktel share; the Q3 print (reported 2026-11-20) showed a record net profit of USD 111.4m |
| AIXA | germany | XETR | 29.42 | -9.50 | -7.75 | -1.75 | EUR | 2.2x | 32.51 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | settled | none | 2026-10-29 (22d ago) | — | no catalyst lookup (outside the per-run budget) |
| ASML | netherlands | EURONEXT | 1168 | -9.33 | -6.15 | -3.18 | EUR | 2.9x | 1288.20 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | settled | ADR (NASDAQ:ASML) | 2026-10-14 (37d ago) | N | No issuer news: the shares fell 6.3% with the European AI and semiconductor complex after the 19 Nov US session's AI selloff (AMD -7.7%), with the US export-control overhang still in the price |
| TPRO | italy | MIL | 18.41 | -9.31 | -5.86 | -3.45 | EUR | 2.3x | 20.30 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | settled | none | 2026-08-05 (107d ago) | — | no catalyst lookup (outside the per-run budget) |
| NOKIA | finland | OMXHEX | 6.444 | -8.88 | -6.19 | -2.69 | EUR | 2.8x | 7.07 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | settled | ADR (NYSE:NOK) | 2026-10-22 (29d ago) | — | pending catalyst lookup |
| VER | sweden | OMXSTO | 8.08 | -8.60 | — | — | SEK | 2.9x | 8.84 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | settled | none | 2026-08-27 (85d ago) | — | pending catalyst lookup |
| IQMX | finland | OMXHEX | 6 | -8.54 | — | — | EUR | 1.7x | 6.56 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | settled | none | 2026-11-05 (15d ago) | — | no catalyst lookup (outside the per-run budget) |
| CGEO | uk | LSE | 4150 | -8.19 | -5.53 | -2.66 | GBX | 3.4x | 4520.00 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| AMS2 | austria | VIE | 13.6 | -8.11 | -7.09 | -1.02 | EUR | 1.7x | 14.80 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | settled | none | 2026-11-13 (7d ago) | — | no catalyst lookup (outside the per-run budget) |
| G24 | germany | XETR | 80.75 | -8.03 | -7.97 | -0.06 | EUR | 4.8x | 87.80 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | settled | none | 2025-08-07 (470d ago) | — | no catalyst lookup (outside the per-run budget) |
| SEL | poland | GPW | 53 | -7.99 | -5.90 | -2.09 | PLN | 5.5x | 57.60 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | settled | none | 2026-11-20 (0d ago) | Y | Q3 profit fell y/y on cost pressure (reported 2026-11-20): net profit PLN 44.0m vs PLN 59.6m and EPS PLN 2.03, even as revenue rose 25.7% to PLN 629.9m |
| COTN | switzerland | SIX | 278.2 | -7.88 | — | — | CHF | 2.7x | 302.00 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | settled | none | 2026-07-31 (112d ago) | — | no catalyst lookup (outside the per-run budget) |
| SMG | switzerland | SIX | 27.8 | -7.79 | -7.63 | -0.16 | CHF | 3.9x | 30.15 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | settled | ADR (OTC:SMGSY) | 2026-08-25 (87d ago) | — | no catalyst lookup (outside the per-run budget) |
| JACK | norway | OSL | 6.18 | +7.67 | +7.67 | -0.00 | NOK | 5.7x | 5.74 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | settled | none | 2026-08-25 (87d ago) | N | Hunter Group unit HG Projectco 1 placed a conditional cash purchase order for all Jacktel shares at NOK 6.30, an 8.6% premium to the 18 Nov close, extended to 22:00 CET on 20 Nov; the release also carried preliminary Q3 revenue of USD 19.0m |
| SENS | switzerland | SIX | 73.5 | -7.66 | — | — | CHF | 3.3x | 79.60 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | settled | none | 2026-08-19 (93d ago) | — | no catalyst lookup (outside the per-run budget) |
| GRE | spain | BME | 50.9 | -7.45 | — | — | EUR | 2.0x | 55.00 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | settled | none | 2026-09-16 (65d ago) | — | pending catalyst lookup |
| ASM | netherlands | EURONEXT | 639.6 | -7.20 | -5.46 | -1.74 | EUR | 2.0x | 689.20 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | settled | US line (OTC:ASMXF) | 2026-10-27 (24d ago) | — | no catalyst lookup (outside the per-run budget) |
| FRVIA | france | EURONEXT | 7.494 | -7.11 | — | — | EUR | 3.7x | 8.07 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | settled | none | 2026-07-31 (112d ago) | — | no catalyst lookup (outside the per-run budget) |
| BGEO | uk | LSE | 12020 | -7.04 | — | — | GBX | 3.8x | 12930.00 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | settled | none | 2026-11-04 (16d ago) | — | no catalyst lookup (outside the per-run budget) |
| ASHM | uk | LSE | 179.9 | -6.88 | — | — | GBX | 3.6x | 193.20 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | settled | none | 2026-09-07 (74d ago) | — | pending catalyst lookup |
| PKO | poland | GPW | 109.48 | -6.86 | -5.96 | -0.90 | PLN | 4.0x | 117.54 | yahoo_chart_daily | 2026-11-19 | 2026-11-20 | settled | none | 2026-11-05 (15d ago) | — | no catalyst lookup (outside the per-run budget) |

## Source health

- scanner_calls: 36 | scanner_errors: 0
- pipeline_version: 2026-11-20.1
- settlement: the EU/UK session is CLOSED at this fire, so every row's `Settle`
  cell reads `settled` and its move is the session's own move.
- morning_artifact: found locally
- catalyst_catalog: found locally
- catalyst_merge: region-matched - a row may only use a catalog entry from its OWN
  region; the same ticker on another venue is a different company and is not used.
- scan_to_settle: 17 rows compared with the 08:00 ET scan, median drift 1.85pp, max 5.62pp, 12 rows more than 1pp apart
- reference_close (screener vs Yahoo, resolved BEFORE the table was built): agree=29 mismatch=1 unverified=0 stale_reference=1
- rows_dropped_stale_ref: 1 | rows_dropped_unresolved_ref: 0
- earnings_field_stale_rows: 0 (the bulk earnings calendar reaches the US only, and this artifact publishes no US row, so the screener's own field is the only source for its dates - a stale date here is POSSIBLE and is not detected)
- earnings_dates: the published `Last earnings` date by source - catalog (researched) 2, calendar 0, asx 0, screener 27. The chain is researched -> calendar (US) -> ASX feed (AU) -> the screener's field, which is the FALLBACK and the one that lags. This pass publishes the EU/UK rows only, so its dates come from the researched catalog and the screener's field; no bulk calendar or ASX feed reaches a European venue - each bulk feed is consulted only for its own market.
- catalyst_budget: 0 US + 0 EU + 0 AU + 0 APAC/Gulf = 0 lookups - the settlement pass performs NO new catalyst lookups (no research happens in this slot); every catalyst cell is merged from the 08:00 ET run's catalog, and a row may only use a catalog entry from its OWN region.
- earnings_tiers: fresh=2 near=0 (fresh = the row's earnings event is dated on the session that just settled, near = the previous session; measured over THIS table's rows - the 08:00 scan ranks the US rows by the same key)
- earnings_date_quality: 0 of 12 markets that publish rows here publish a FRESH earnings date (median age <= 14d); `us` and `au` publish 0 rows BY DESIGN (the US session is open at 12:15 ET and the AU rows belong to the 08:00 scan), not by a failed scan. The table below gives each market's rows, the rows with NO date at all, the median age of the published date and the rows within 7 and 30 days - the reader sees the input quality instead of trusting it
| market | rows | no date | median age | <=7d | <=30d |
|---|---|---|---|---|---|
| au | 0 | 0 | n/a | 0 | 0 |
| austria | 2 | 0 | 15d | 1 | 2 |
| finland | 2 | 0 | 29d | 0 | 2 |
| france | 4 | 1 | 60d | 1 | 1 |
| germany | 3 | 0 | 22d | 0 | 2 |
| italy | 1 | 0 | 107d | 0 | 0 |
| netherlands | 2 | 0 | 37d | 0 | 1 |
| norway | 2 | 0 | 87d | 1 | 1 |
| poland | 2 | 0 | 15d | 1 | 2 |
| spain | 1 | 0 | 65d | 0 | 0 |
| sweden | 4 | 0 | 85d | 0 | 1 |
| switzerland | 3 | 0 | 93d | 0 | 0 |
| uk | 3 | 1 | 74d | 0 | 1 |
| us | 0 | 0 | n/a | 0 | 0 |
- yahoo_calls: 30 | yahoo_429: 0 | yahoo_errors: 0 | yahoo_breaker: closed
- degraded_sources: 1
  (the chat reply's `errors:` MUST equal this number - one entry per degraded
  source, not one per run)
  1. platform.fire_blocked — the scheduled 12:15 ET settlement fire was blocked by the platform and this run executed 2195 min after it

## Audit line

`earnings-reaction mode=settle target=earnings-reactions:2026-11-20 eu_rows=29 scan_matched=17 scan_to_settle_median_pp=1.853546910755151 catalyst_lookups=16 rows_dropped_stale_ref=1 degraded_sources=1`
