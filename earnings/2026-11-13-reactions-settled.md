# Earnings reaction scanner — 2026-11-13 (EU settlement pass)

- Cron: `15 12 * * 1-5` America/New_York (weekdays, 12:15 ET)
- Fire time (ET): 2026-11-13 12:16:21 Fri
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
- morning_artifact: earnings/2026-11-13-reactions.md
- Status: `ok`

## TL;DR

- 28 EU/UK rows republished with their SETTLED close and move.
- 17 of them also appear in the 08:00 ET scan: the settled move
  differs from the scan move by a median of 0.78pp and a maximum of
  4.78pp; 7 of 17 rows moved more than 1pp
  between the scan and the close.
- Biggest settled EU/UK move: AKAST (-22.63%, norway).

## EU/UK — Settled table

| Ticker | Market | Venue | Close | Chg % | Move @08:00 | Δ vs scan | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | Session asof | Settle | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AKAST | norway | OSL | 9.3 | -22.63 | -22.71 | +0.08 | NOK | 6.6x | 12.02 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | settled | none | 2026-11-11 | — | no catalyst lookup (outside the per-run budget) |
| HEM | sweden | OMXSTO | 61.05 | -13.40 | -10.50 | -2.90 | SEK | 3.5x | 70.50 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | settled | none | 2026-10-22 | — | no catalyst lookup (outside the per-run budget) |
| ERA | france | EURONEXT | 32.92 | -10.64 | -5.86 | -4.78 | EUR | 3.5x | 36.84 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | settled | none | 2026-07-29 | — | no catalyst lookup (outside the per-run budget) |
| SIVE | sweden | OMXSTO | 14.3 | -10.29 | — | — | SEK | 1.7x | 15.94 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | settled | none | 2026-08-27 | — | no catalyst lookup (outside the per-run budget) |
| S92 | germany | XETR | 45.26 | -8.23 | -5.64 | -2.59 | EUR | 2.0x | 49.32 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | settled | none | 2026-11-12 | — | no catalyst lookup (outside the per-run budget) |
| OHB | germany | XETR | 177 | -8.10 | -5.50 | -2.60 | EUR | 1.6x | 192.60 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | settled | ADR (OTC:OHBTF) | 2026-11-12 | — | no catalyst lookup (outside the per-run budget) |
| PAX | sweden | OMXSTO | 67.5 | +8.00 | +7.52 | +0.48 | SEK | 4.8x | 62.50 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | settled | none | 2026-08-21 | N | FDA advanced the Paxman Neuropathy De Novo application to substantive review (press release 13 Nov 12:45 CET; 134 review days left from the Oct 26 filing); Q3 report due Nov 20 |
| ANA | spain | BME | 203 | -7.98 | -7.62 | -0.36 | EUR | 4.0x | 220.60 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | settled | none | 2026-07-30 | — | no catalyst lookup (outside the per-run budget) |
| WISE | uk | LSE | 894.4 | +7.68 | +6.41 | +1.27 | GBX | 5.4x | 830.60 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | settled | ADR (NASDAQ:WSE) | 2026-06-25 | — | no catalyst lookup (outside the per-run budget) |
| ANE | spain | BME | 20.26 | -6.89 | -7.17 | +0.28 | EUR | 3.5x | 21.76 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | settled | none | 2026-07-31 | — | no catalyst lookup (outside the per-run budget) |
| TOR | poland | GPW | 57 | -6.86 | -6.05 | -0.81 | PLN | 4.0x | 61.20 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | settled | none | 2026-08-20 | — | no catalyst lookup (outside the per-run budget) |
| GENO | norway | OSL | 15.84 | -6.82 | -5.41 | -1.41 | NOK | 1.7x | 17.00 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | settled | none | 2026-11-12 | — | no catalyst lookup (outside the per-run budget) |
| CMB | italy | MIL | 80.3 | +6.64 | +9.30 | -2.66 | EUR | 3.2x | 75.30 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | settled | ADR (NYSE:CMBT) | 2026-09-11 | Y | 9M 2026 results Nov 12: consolidated revenue EUR 207.6m +15.4%, net profit EUR 41.0m +27.4%; Q3 revenue +19.6% and EBITDA +23% |
| ORRON | sweden | OMXSTO | 8.37 | -5.96 | — | — | SEK | 1.9x | 8.90 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | settled | none | 2026-11-04 | — | no catalyst lookup (outside the per-run budget) |
| IQMX | finland | OMXHEX | 6.18 | -5.50 | — | — | EUR | 1.4x | 6.54 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | settled | none | 2026-11-05 | — | no catalyst lookup (outside the per-run budget) |
| BOUV | norway | OSL | 53.6 | +5.30 | +4.52 | +0.78 | NOK | 2.6x | 50.90 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | settled | none | 2026-11-04 | — | no catalyst lookup (outside the per-run budget) |
| CRI | poland | GPW | 719 | -5.15 | — | — | PLN | 2.2x | 758.00 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | settled | none | 2026-09-28 | — | no catalyst lookup (outside the per-run budget) |
| AMBU_B | denmark | OMXCOP | 91.65 | +5.04 | — | — | DKK | 2.8x | 87.25 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | settled | ADR (OTC:AMBFF) | 2026-11-05 | — | no catalyst lookup (outside the per-run budget) |
| BMAG | austria | VIE | 31.3 | -5.01 | -5.61 | +0.60 | EUR | 1.7x | 32.95 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| AZT | norway | OSL | 21.6 | -4.85 | — | — | NOK | 2.2x | 22.70 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | settled | none | 2026-11-05 | — | no catalyst lookup (outside the per-run budget) |
| GRE | spain | BME | 67.8 | -4.51 | -4.51 | +0.00 | EUR | 1.5x | 71.00 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | settled | none | 2026-09-16 | — | pending catalyst lookup |
| NOKIA | finland | OMXHEX | 7.294 | -4.50 | — | — | EUR | 1.3x | 7.64 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | settled | ADR (NYSE:NOK) | 2026-10-22 | — | no catalyst lookup (outside the per-run budget) |
| FCT | italy | MIL | 11.405 | -4.28 | -3.73 | -0.55 | EUR | 2.2x | 11.91 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | settled | none | 2026-07-29 | — | no catalyst lookup (outside the per-run budget) |
| ABVX | france | EURONEXT | 79.1 | -4.12 | — | — | EUR | 1.7x | 82.50 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | settled | none | 2026-09-21 | — | no catalyst lookup (outside the per-run budget) |
| ASM | netherlands | EURONEXT | 694.6 | -4.09 | — | — | EUR | 1.2x | 724.20 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | settled | ADR (OTC:ASMXF) | 2026-10-27 | — | no catalyst lookup (outside the per-run budget) |
| BME | uk | LSE | 351 | +4.03 | — | — | GBX | 1.6x | 337.40 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | settled | none | 2026-11-12 | — | no catalyst lookup (outside the per-run budget) |
| NANO | france | EURONEXT | 27.9 | -3.93 | — | — | EUR | 0.8x | 29.04 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | settled | ADR (NASDAQ:NA) | 2026-09-24 | — | no catalyst lookup (outside the per-run budget) |
| CNA | uk | LSE | 160.65 | +3.81 | +3.59 | +0.22 | GBX | 3.3x | 154.75 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | settled | none | 2026-07-23 | — | no catalyst lookup (outside the per-run budget) |

## Source health

- scanner_calls: 36 | scanner_errors: 0
- pipeline_version: 2026-11-12.2
- settlement: the EU/UK session is CLOSED at this fire, so every row's `Settle`
  cell reads `settled` and its move is the session's own move.
- morning_artifact: found locally
- catalyst_catalog: found locally
- catalyst_merge: region-matched - a row may only use a catalog entry from its OWN
  region; the same ticker on another venue is a different company and is not used.
- scan_to_settle: 17 rows compared with the 08:00 ET scan, median drift 0.78pp, max 4.78pp, 7 rows more than 1pp apart
- reference_close (screener vs Yahoo, resolved BEFORE the table was built): agree=28 mismatch=2 unverified=0 stale_reference=2
- rows_dropped_stale_ref: 2 | rows_dropped_unresolved_ref: 0
- degraded_sources: 0
  (none - every source answered for every published row)

## Audit line

`earnings-reaction mode=settle target=earnings-reactions:2026-11-13 eu_rows=28 scan_matched=17 scan_to_settle_median_pp=0.784518664047158 catalyst_lookups=13 rows_dropped_stale_ref=2 degraded_sources=0`
