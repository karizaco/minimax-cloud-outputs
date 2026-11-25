# Earnings reaction scanner — 2026-11-25 (EU settlement pass)

- Cron: `15 12 * * 1-5` America/New_York (weekdays, 12:15 ET)
- Fire time (ET): 2026-11-25 12:16:31 Wed
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
- morning_artifact: earnings/2026-11-25-reactions.md
- Status: `ok`

## TL;DR

- 29 EU/UK rows republished with their SETTLED close and move.
- 16 of them also appear in the 08:00 ET scan: the settled move
  differs from the scan move by a median of 1.88pp and a maximum of
  7.61pp; 12 of 16 rows moved more than 1pp
  between the scan and the close.
- Biggest settled EU/UK move: ROCK_A (-16.05%, denmark).

## EU/UK — Settled table

| Ticker | Market | Venue | Close | Chg % | Move @08:00 | Δ vs scan | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | Session asof | Settle | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ROCK_A | denmark | OMXCOP | 187.2 | -16.05 | — | — | DKK | 7.6x | 223.00 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | settled | ADR (NASDAQ:BNR) | 2026-08-19 (98d ago) | — | pending catalyst lookup |
| ROCK_B | denmark | OMXCOP | 178 | -15.64 | — | — | DKK | 7.3x | 211.00 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | settled | ADR (NASDAQ:BNR) | 2026-08-19 (98d ago) | — | pending catalyst lookup |
| RCO | france | EURONEXT | 58.15 | +13.13 | +9.92 | +3.21 | EUR | 6.7x | 51.40 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | settled | none | 2026-11-25 (0d ago) | — | no catalyst lookup (outside the per-run budget) |
| SECT_B | sweden | OMXSTO | 368.6 | +11.70 | +9.82 | +1.88 | SEK | 5.1x | 330.00 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | settled | none | 2026-11-25 (0d ago) | — | no catalyst lookup (outside the per-run budget) |
| OCDO | uk | LSE | 280.4 | -9.96 | -11.95 | +1.99 | GBX | 3.8x | 311.40 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | settled | none | 2026-07-16 (132d ago) | — | no catalyst lookup (outside the per-run budget) |
| PETS | uk | LSE | 286.2 | +9.57 | +9.03 | +0.54 | GBX | 6.3x | 261.20 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | settled | US line (OTC:PAHGF) | 2026-11-25 (0d ago) | — | no catalyst lookup (outside the per-run budget) |
| BIOA_B | sweden | OMXSTO | 353 | +9.36 | +10.78 | -1.42 | SEK | 5.2x | 322.80 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | settled | none | 2026-11-25 (0d ago) | — | pending catalyst lookup |
| SSIC | uk | LSE | 64.1 | -9.34 | -6.32 | -3.02 | GBX | 4.5x | 70.70 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| SRAIL | switzerland | SIX | 27.94 | -8.57 | -9.16 | +0.59 | CHF | 5.7x | 30.56 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | settled | none | 2026-08-26 (91d ago) | — | no catalyst lookup (outside the per-run budget) |
| CCC | uk | LSE | 4190 | -8.19 | -4.73 | -3.46 | GBX | 2.8x | 4564.00 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | settled | none | 2026-09-08 (78d ago) | — | no catalyst lookup (outside the per-run budget) |
| KOMPL | norway | OSL | 6.52 | -8.17 | — | — | NOK | 2.8x | 7.10 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | settled | none | 2026-10-22 (34d ago) | — | pending catalyst lookup |
| AMS2 | austria | VIE | 14.2 | +7.98 | +15.59 | -7.61 | EUR | 1.3x | 13.15 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | settled | none | 2026-11-13 (12d ago) | — | pending catalyst lookup |
| ASM | netherlands | EURONEXT | 587.6 | -7.81 | — | — | EUR | 1.8x | 637.40 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | settled | US line (OTC:ASMXF) | 2026-10-27 (29d ago) | — | no catalyst lookup (outside the per-run budget) |
| ATS | austria | VIE | 89.2 | -7.66 | — | — | EUR | 1.2x | 96.60 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | settled | none | 2026-11-05 (20d ago) | — | pending catalyst lookup |
| ASMDEE_B | sweden | OMXSTO | 149.3 | -7.61 | -6.00 | -1.61 | SEK | 3.9x | 161.60 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | settled | none | 2026-11-13 (12d ago) | — | pending catalyst lookup |
| JSW | poland | GPW | 24.51 | +7.41 | +4.91 | +2.50 | PLN | 3.3x | 22.82 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | settled | none | 2026-11-19 (6d ago) | — | no catalyst lookup (outside the per-run budget) |
| SMOP | norway | OSL | 50.2 | -7.04 | -4.81 | -2.23 | NOK | 2.1x | 54.00 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | settled | none | 2026-10-29 (27d ago) | — | no catalyst lookup (outside the per-run budget) |
| IQMX | finland | OMXHEX | 6.23 | +6.95 | +5.58 | +1.37 | EUR | 1.3x | 5.83 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | settled | none | 2026-11-05 (20d ago) | — | no catalyst lookup (outside the per-run budget) |
| SOI | france | EURONEXT | 85.06 | -6.92 | — | — | EUR | 1.0x | 91.38 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | settled | none | 2026-11-18 (7d ago) | — | no catalyst lookup (outside the per-run budget) |
| ELG | germany | XETR | 93.2 | -6.80 | — | — | EUR | 1.7x | 100.00 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | settled | none | 2026-11-10 (15d ago) | — | no catalyst lookup (outside the per-run budget) |
| WAF | germany | XETR | 46.74 | -6.61 | -6.01 | -0.60 | EUR | 1.5x | 50.05 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | settled | none | 2026-11-04 (21d ago) | N | no company news: the global semiconductor selloff continued (AIXTRON's UBS downgrade took the MDAX equipment names down 5-9% on 24 Nov; Nvidia -4.65% pre-market and the Philadelphia Semiconductor Index -7.9% on 24 Nov dragged Asian chip values lower), taking Siltronic to a six-month low at EUR47.00 |
| BVI | france | EURONEXT | 31.8 | +6.60 | +6.77 | -0.17 | EUR | 6.0x | 29.83 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | settled | none | 2026-07-29 (119d ago) | — | no catalyst lookup (outside the per-run budget) |
| NDX1 | germany | XETR | 33.7 | -6.49 | — | — | EUR | 2.6x | 36.04 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | settled | none | 2026-11-05 (20d ago) | — | no catalyst lookup (outside the per-run budget) |
| SIVE | sweden | OMXSTO | 11.02 | -6.45 | — | — | SEK | 0.8x | 11.78 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | settled | none | 2026-08-27 (90d ago) | — | pending catalyst lookup |
| SKJE | denmark | OMXCOP | 354.5 | -6.34 | — | — | DKK | 3.2x | 378.50 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| RBI | austria | VIE | 54.4 | -6.29 | -4.65 | -1.64 | EUR | 2.8x | 58.05 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | settled | none | 2026-11-03 (22d ago) | N | no fresh catalyst found: no RBI release since the 3 Nov Q3 results and the upgraded net-interest-income guidance; the drop came in a broad Austrian bank selloff (ATX -0.9% with the heavyweights lower) that has hit the Vienna banks on each of the last four sessions |
| GEKTERNA | greece | ATHEX | 41.28 | -6.18 | — | — | EUR | 3.0x | 44.00 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | settled | none | 2026-09-15 (71d ago) | — | no catalyst lookup (outside the per-run budget) |
| LAND | switzerland | SIX | 57.4 | +6.10 | — | — | CHF | 3.0x | 54.10 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | settled | US line (OTC:BRLAF) | 2026-10-29 (27d ago) | — | no catalyst lookup (outside the per-run budget) |
| ABVX | france | EURONEXT | 72.3 | +6.01 | — | — | EUR | 1.8x | 68.20 | yahoo_chart_daily | 2026-11-24 | 2026-11-25 | settled | none | 2026-09-21 (65d ago) | — | pending catalyst lookup |

## Source health

- scanner_calls: 36 | scanner_errors: 0
- pipeline_version: 2026-11-20.1
- settlement: the EU/UK session is CLOSED at this fire, so every row's `Settle`
  cell reads `settled` and its move is the session's own move.
- morning_artifact: found locally
- catalyst_catalog: found locally
- catalyst_merge: region-matched - a row may only use a catalog entry from its OWN
  region; the same ticker on another venue is a different company and is not used.
- scan_to_settle: 16 rows compared with the 08:00 ET scan, median drift 1.88pp, max 7.61pp, 12 rows more than 1pp apart
- reference_close (screener vs Yahoo, resolved BEFORE the table was built): agree=29 mismatch=1 unverified=0 stale_reference=1
- rows_dropped_stale_ref: 1 | rows_dropped_unresolved_ref: 0
- earnings_field_stale_rows: 0 (the bulk earnings calendar reaches the US only, and this artifact publishes no US row, so the screener's own field is the only source for its dates - a stale date here is POSSIBLE and is not detected)
- earnings_dates: the published `Last earnings` date by source - catalog (researched) 0, calendar 0, asx 0, screener 29. The chain is researched -> calendar (US) -> ASX feed (AU) -> the screener's field, which is the FALLBACK and the one that lags. This pass publishes the EU/UK rows only, so its dates come from the researched catalog and the screener's field; no bulk calendar or ASX feed reaches a European venue - each bulk feed is consulted only for its own market.
- catalyst_budget: 0 US + 0 EU + 0 AU + 0 APAC/Gulf = 0 lookups - the settlement pass performs NO new catalyst lookups (no research happens in this slot); every catalyst cell is merged from the 08:00 ET run's catalog, and a row may only use a catalog entry from its OWN region.
- earnings_tiers: fresh=4 near=0 (fresh = the row's earnings event is dated on the session that just settled, near = the previous session; measured over THIS table's rows - the 08:00 scan ranks the US rows by the same key)
- earnings_date_quality: 2 of 12 markets that publish rows here publish a FRESH earnings date (median age <= 14d); `us` and `au` publish 0 rows BY DESIGN (the US session is open at 12:15 ET and the AU rows belong to the 08:00 scan), not by a failed scan. The table below gives each market's rows, the rows with NO date at all, the median age of the published date and the rows within 7 and 30 days - the reader sees the input quality instead of trusting it
| market | rows | no date | median age | <=7d | <=30d |
|---|---|---|---|---|---|
| au | 0 | 0 | n/a | 0 | 0 |
| austria | 3 | 0 | 20d | 0 | 3 |
| denmark | 3 | 1 | 98d | 0 | 0 |
| finland | 1 | 0 | 20d | 0 | 1 |
| france | 4 | 0 | 65d | 2 | 2 |
| germany | 3 | 0 | 20d | 0 | 3 |
| greece | 1 | 0 | 71d | 0 | 0 |
| netherlands | 1 | 0 | 29d | 0 | 1 |
| norway | 2 | 0 | 34d | 0 | 1 |
| poland | 1 | 0 | 6d | 1 | 1 |
| sweden | 4 | 0 | 12d | 2 | 3 |
| switzerland | 2 | 0 | 91d | 0 | 1 |
| uk | 4 | 1 | 78d | 1 | 1 |
| us | 0 | 0 | n/a | 0 | 0 |
- yahoo_calls: 30 | yahoo_429: 0 | yahoo_errors: 0 | yahoo_breaker: closed
- degraded_sources: 0
  (none - every source answered for every published row)

## Audit line

`earnings-reaction mode=settle target=earnings-reactions:2026-11-25 eu_rows=29 scan_matched=16 scan_to_settle_median_pp=1.876969696969704 catalyst_lookups=16 rows_dropped_stale_ref=1 degraded_sources=0`
