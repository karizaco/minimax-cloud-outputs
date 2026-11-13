# Earnings reaction scanner — 2026-11-13

- Cron: `0 8 * * 1-5` America/New_York (weekdays, 08:00 ET)
- Fire time (ET): 2026-11-13 08:08:23 Fri
- Run type: `scheduled_scan`
- Source: TradingView public screener (`scanner.tradingview.com/<market>/scan`);
  Yahoo chart API as the independent reference-close source.
- Method: 5 passes (US top-200 mcap, US prior-session movers, EU/UK movers,
  ASX movers, APAC/Gulf movers). Volume floor 10,000 on every pass; `country` filter for
  primary listings; exchange drop-list applied.
- artifact_contract: REACTION_ARTIFACT_V2
- settlement_state: every foreign row carries a `Settle` cell - `live` when the row's
  session bar is an in-progress bar, `settled` when it is a completed session. The
  EU/UK session is still OPEN at the 08:00 ET fire (it closes 11:30 ET in winter), so
  its rows read `live`: the move is a mid-session snapshot, not the session's result.
- ref_close_source: yahoo_chart_daily (Yahoo Finance daily chart bars; the base
  every published row is measured against)
- Status: `ok`

## TL;DR

- 0 AMC reactions, 25 pre-market gaps, 122 without extended-hours data; 29 EU/UK and 4 ASX movers, 19 APAC/Gulf movers.
- Biggest US extended-hours move: VIR PRE_GAP (16.67%).
- Biggest EU/UK move: AKAST (-22.71%, norway).
- Biggest ASX move: PDN (-17.59%).
- Biggest APAC/Gulf move: ESIP (+34.72%, indonesia).
- 0 of the 29 EU/UK rows are SETTLED and 29 are LIVE (mid-session). The 12:15 ET settlement pass publishes where those
  live moves actually closed.
- EU/AU/APAC earnings-driven tagging is keyword-based on headlines (best-effort). A row
  whose lookup was not performed carries NO verdict — only a researched row does.

## Actionable read

- **Move vs this name's own history.** The `Move vs avg daily` column divides the
  reaction by the name's own mean absolute daily move over its last
  20 completed sessions. A -27% move in a name that averages +-3% is a
  different event from a -8% move in a name that averages +-7%.
- **US-listed and tradeable vs foreign-only.** 40 published US rows are on a
  US venue; 5 more foreign reactions have a US ADR line
  (the `US tradeable` column carries the ticker); 28 are foreign-only and
  cannot be bought directly by a US reader.
- **Not yet fully priced — US (hypothesis, not a recommendation).**
  VIR — -16.67%, 4.19% mean absolute daily move over the last 20 completed sessions, 4.0x that average, reference close 13.13 dated 2026-11-11, US access: US-listed, the move now (-16.67%) is larger than the move it follows (-7.69%); the reaction is still being repriced. Hypothesis only: this artifact states no
  direction and no trade.
- **Not yet fully priced — EU/UK (hypothesis, not a recommendation).**
  AKAST — -22.71%, 2.27% mean absolute daily move over the last 20 completed sessions, 10.0x that average, reference close 12.02 dated 2026-11-12, US access: none, the move now (-22.71%) is larger than the move it follows (+1.18%); the reaction is still being repriced. Hypothesis only: this artifact states no
  direction and no trade.
- **Not yet fully priced — AU (ASX) (hypothesis, not a recommendation).**
  RPL — -10.41%, 2.14% mean absolute daily move over the last 20 completed sessions, 4.9x that average, reference close 2.21 dated 2026-11-11, US access: none, the move now (-10.41%) is larger than the move it follows (-2.21%); the reaction is still being repriced. Hypothesis only: this artifact states no
  direction and no trade.

## US — Headline table

| Ticker | Venue | Close | Chg % | Pre-mkt % | Post-mkt % | Move vs avg daily | Ref close | Ref source | Ref asof | US tradeable | Last earnings | Tag | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| VIR | NASDAQ | 12.12 | -7.69 | -16.67 | — | 4.0x | 13.13 | yahoo_chart_daily | 2026-11-11 | US-listed | 2026-11-04 (9d ago) | PRE_GAP | N | Public offering priced at $10.00/sh (15.0m shares, ~$150M) announced after the close Nov 12, a discount to the $12.12 close; follows the Nov 8-9 ECLIPSE-1 Phase 3 win in hepatitis delta (44% response vs 0%) |
| SLS | NASDAQ | 8.03 | -4.63 | 8.66 | — | 1.5x | 8.42 | yahoo_chart_daily | 2026-11-11 | US-listed | 2026-11-12 (1d ago) | PRE_GAP | Y | Q3 2026 results after the close Nov 12: net loss $10.1M (vs $6.8M), cash $134.7M; topline primary endpoint of the Phase 3 REGAL trial of galinpepimut-S now expected this month |
| HOS | NYSE | 5.83 | 4.67 | 6.35 | — | 1.9x | 5.57 | yahoo_chart_daily | 2026-11-11 | US-listed | 2026-11-04 (9d ago) | PRE_GAP | N | CEO Todd Hornbeck bought 280,866 shares for ~$1.5M on Nov 10-11 (Form 4 filed Nov 12) after terminating a 10b5-1 sale plan for 1.17m shares on Nov 9 |
| GENB | NASDAQ | 12.57 | -6.82 | 4.53 | — | 0.9x | 13.49 | yahoo_chart_daily | 2026-11-11 | US-listed | 2026-11-12 (1d ago) | PRE_GAP | Y | Q3 2026 results Nov 12: net loss widened to $87.7M (vs $60.0M), revenue $4.2M (vs $9.6M), cash and marketable securities $404.2M |
| TRV | NYSE | 403.18 | 0.93 | 3.68 | — | 3.1x | 399.46 | yahoo_chart_daily | 2026-11-11 | US-listed | 2026-10-16 (28d ago) | PRE_GAP | N | no fresh catalyst found (most recent items: board expanded to 10 directors with Lesley Goldwasser effective Nov 4; Q3 reported Oct 16 - the +3.68% pre-market print could not be verified by Yahoo) |
| CSCO | NASDAQ | 102.01 | 1.24 | -3.62 | — | 1.7x | 100.76 | yahoo_chart_daily | 2026-11-11 | US-listed | 2026-11-12 (1d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ALM | NASDAQ | 7.63 | -6.50 | 3.33 | — | 0.8x | 8.16 | yahoo_chart_daily | 2026-11-11 | US-listed | 2026-11-12 (1d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PANW | NASDAQ | 322.66 | -3.53 | 3.13 | — | 1.0x | 334.47 | yahoo_chart_daily | 2026-11-11 | US-listed | 2026-09-01 (73d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CRML | NASDAQ | 5.31 | -5.35 | 3.01 | — | 0.5x | 5.61 | yahoo_chart_daily | 2026-11-11 | US-listed (ADR) | 2026-09-25 (49d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AGBK | NYSE | 6.32 | 17.25 | 3.01 | — | 0.6x | 5.39 | yahoo_chart_daily | 2026-11-11 | US-listed (ADR) | 2026-11-11 (2d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMD | NASDAQ | 585.3 | 5.86 | -2.78 | — | 0.5x | 552.90 | yahoo_chart_daily | 2026-11-11 | US-listed | 2026-11-03 (10d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| WGS | NASDAQ | 51.87 | -5.90 | -2.64 | — | 0.5x | 55.12 | yahoo_chart_daily | 2026-11-11 | US-listed | 2026-11-09 (4d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ABSI | NASDAQ | 9.135 | -9.73 | 2.57 | — | 0.4x | 10.12 | yahoo_chart_daily | 2026-11-11 | US-listed | 2026-11-12 (1d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AEHR | NASDAQ | 61.04 | -7.21 | -2.52 | — | 0.3x | 65.78 | yahoo_chart_daily | 2026-11-11 | US-listed | 2026-11-02 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NBIS | NASDAQ | 128.64 | -16.84 | -2.44 | — | 0.3x | 154.69 | yahoo_chart_daily | 2026-11-11 | US-listed (ADR) | 2026-11-12 (1d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CRWD | NASDAQ | 229.87 | 0.35 | 2.43 | — | 0.9x | 229.06 | yahoo_chart_daily | 2026-11-11 | US-listed | 2026-08-26 (79d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MSTR | NASDAQ | 114.41 | -6.49 | -2.41 | — | 0.7x | 122.35 | yahoo_chart_daily | 2026-11-11 | US-listed | 2026-10-29 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SECZ | NYSE | 8.39 | -7.40 | 2.38 | — | 0.4x | 9.06 | yahoo_chart_daily | 2026-11-11 | US-listed | 2026-11-09 (4d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PLBL | NASDAQ | 7.27 | 28.79 | -2.34 | — | 0.7x | 5.64 | yahoo_chart_daily | 2026-11-11 | US-listed (ADR) | — | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| VOYG | NYSE | 27.79 | -6.05 | -2.30 | — | 0.4x | 29.58 | yahoo_chart_daily | 2026-11-11 | US-listed | 2026-11-02 (11d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| S | NYSE | 22.29 | -6.27 | 2.29 | — | 0.7x | 23.78 | yahoo_chart_daily | 2026-11-11 | US-listed | 2026-08-27 (78d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AVGO | NASDAQ | 364.36 | 5.54 | -2.27 | — | 0.7x | 345.22 | yahoo_chart_daily | 2026-11-11 | US-listed | 2026-09-02 (72d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FIGR | NASDAQ | 25.67 | 6.12 | 2.26 | — | 0.5x | 24.19 | yahoo_chart_daily | 2026-11-11 | US-listed | 2026-11-12 (1d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| IREN | NASDAQ | 19.48 | -6.53 | -2.05 | — | 0.3x | 20.84 | yahoo_chart_daily | 2026-11-11 | US-listed (ADR) | 2026-11-05 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GLXY | NASDAQ | 15.18 | -4.95 | -2.04 | — | 0.3x | 15.97 | yahoo_chart_daily | 2026-11-11 | US-listed | 2026-10-27 (17d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |

## US — QUIET one-liners

| Ticker | Venue | Chg % | Pre-mkt % | Post-mkt % | Move vs avg daily | Ref close | Ref source | Ref asof | US tradeable | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|
| LOW | NYSE | -1.79 | -1.96 | — | 0.9x | 231.60 | yahoo_chart_daily | 2026-11-11 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| CRCL | NYSE | -4.92 | -1.96 | — | 1.4x | 67.12 | yahoo_chart_daily | 2026-11-11 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| SNDK | NASDAQ | -4.11 | -1.95 | — | 0.6x | 977.69 | yahoo_chart_daily | 2026-11-11 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| AYA | NASDAQ | -6.66 | 1.92 | — | 1.7x | 24.49 | yahoo_chart_daily | 2026-11-11 | US-listed (ADR) | — | no catalyst lookup (outside the per-run budget) |
| OCUL | NASDAQ | -5.71 | 1.91 | — | 1.5x | 6.66 | yahoo_chart_daily | 2026-11-11 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| MDLN | NASDAQ | -5.17 | -1.86 | — | 1.9x | 42.16 | yahoo_chart_daily | 2026-11-11 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| INFQ | NYSE | -7.32 | 1.83 | — | 1.3x | 9.42 | yahoo_chart_daily | 2026-11-11 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| DHT | NYSE | 3.29 | 1.81 | — | 1.4x | 21.57 | yahoo_chart_daily | 2026-11-11 | US-listed (ADR) | — | no catalyst lookup (outside the per-run budget) |
| TXG | NASDAQ | -4.75 | 1.80 | — | 0.8x | 62.05 | yahoo_chart_daily | 2026-11-11 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| NTLA | NASDAQ | -7.54 | 1.79 | — | 1.7x | 11.41 | yahoo_chart_daily | 2026-11-11 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| CDLR | NYSE | 5.32 | -1.73 | — | 0.7x | 6.58 | yahoo_chart_daily | 2026-11-11 | US-listed (ADR) | — | no catalyst lookup (outside the per-run budget) |
| NET | NYSE | 1.11 | 1.68 | — | 0.3x | 315.00 | yahoo_chart_daily | 2026-11-11 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| HPK | NASDAQ | 13.18 | 1.68 | — | 2.6x | 7.36 | yahoo_chart_daily | 2026-11-11 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| AAOI | NASDAQ | -5.39 | -1.61 | — | 0.8x | 55.86 | yahoo_chart_daily | 2026-11-11 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| FTNT | NASDAQ | 1.12 | 1.60 | — | 0.3x | 128.10 | yahoo_chart_daily | 2026-11-11 | US-listed | — | no catalyst lookup (outside the per-run budget) |

## EU/UK — Headline table

| Ticker | Market | Venue | Close | Chg % | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | Session asof | Settle | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AKAST | norway | OSL | 9.29 | -22.71 | NOK | 10.0x | 12.02 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | live | none | 2026-11-11 | — | no catalyst lookup (outside the per-run budget) |
| HEM | sweden | OMXSTO | 63.1 | -10.50 | SEK | 3.1x | 70.50 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | live | none | 2026-10-22 | — | no catalyst lookup (outside the per-run budget) |
| CMB | italy | MIL | 82.3 | +9.30 | EUR | 5.2x | 75.30 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | live | ADR (NYSE:CMBT) | 2026-09-11 | Y | 9M 2026 results Nov 12: consolidated revenue EUR 207.6m +15.4%, net profit EUR 41.0m +27.4%; Q3 revenue +19.6% and EBITDA +23% |
| ANA | spain | BME | 203.8 | -7.62 | EUR | 4.6x | 220.60 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | live | none | 2026-07-30 | — | no catalyst lookup (outside the per-run budget) |
| PAX | sweden | OMXSTO | 67.2 | +7.52 | SEK | 5.4x | 62.50 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | live | none | 2026-08-21 | N | FDA advanced the Paxman Neuropathy De Novo application to substantive review (press release 13 Nov 12:45 CET; 134 review days left from the Oct 26 filing); Q3 report due Nov 20 |
| ANE | spain | BME | 20.2 | -7.17 | EUR | 4.2x | 21.76 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | live | none | 2026-07-31 | — | no catalyst lookup (outside the per-run budget) |
| WISE | uk | LSE | 883.8 | +6.41 | GBX | 5.9x | 830.60 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | live | ADR (NASDAQ:WSE) | 2026-06-25 | — | no catalyst lookup (outside the per-run budget) |
| TOR | poland | GPW | 57.5 | -6.05 | PLN | 4.4x | 61.20 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | live | none | 2026-08-20 | — | no catalyst lookup (outside the per-run budget) |
| VBK | germany | XETR | 24.04 | -6.02 | EUR | 2.4x | 25.58 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | live | none | 2026-11-12 | — | no catalyst lookup (outside the per-run budget) |
| ERA | france | EURONEXT | 34.68 | -5.86 | EUR | 2.1x | 36.84 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | live | none | 2026-07-29 | — | no catalyst lookup (outside the per-run budget) |
| MOL | italy | MIL | 35.35 | -5.86 | EUR | 3.1x | 37.55 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | live | none | 2026-11-12 | — | no catalyst lookup (outside the per-run budget) |
| S92 | germany | XETR | 46.54 | -5.64 | EUR | 1.5x | 49.32 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | live | none | 2026-11-12 | — | no catalyst lookup (outside the per-run budget) |
| BMAG | austria | VIE | 31.1 | -5.61 | EUR | 2.1x | 32.95 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | live | none | — | — | no catalyst lookup (outside the per-run budget) |
| SMOP | norway | OSL | 56.6 | +5.60 | NOK | 1.7x | 53.60 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | live | none | 2026-10-29 | — | no catalyst lookup (outside the per-run budget) |
| OHB | germany | XETR | 182 | -5.50 | EUR | 1.1x | 192.60 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | live | ADR (OTC:OHBTF) | 2026-11-12 | — | no catalyst lookup (outside the per-run budget) |
| EOLU_B | sweden | OMXSTO | 48.5 | -5.46 | SEK | 4.1x | 51.30 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | live | none | 2026-08-27 | Y | Q3 2026 interim report published 13 Nov 07:45 CET: net revenue SEK 393m vs 200m, operating profit SEK 112m vs -87m, EPS SEK 2.89 vs -3.87 |
| GENO | norway | OSL | 16.08 | -5.41 | NOK | 1.5x | 17.00 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | live | none | 2026-11-12 | — | no catalyst lookup (outside the per-run budget) |
| CFR | switzerland | SIX | 168.05 | -4.60 | CHF | 4.0x | 176.15 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | live | none | 2026-11-13 | — | no catalyst lookup (outside the per-run budget) |
| OBCK | germany | XETR | 41 | +4.59 | EUR | 2.3x | 39.20 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | live | none | 2026-11-12 | — | no catalyst lookup (outside the per-run budget) |
| GOMX | sweden | OMXSTO | 14.81 | +4.59 | SEK | 1.2x | 14.16 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | live | none | 2026-08-26 | — | no catalyst lookup (outside the per-run budget) |
| BOUV | norway | OSL | 53.2 | +4.52 | NOK | 2.5x | 50.90 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | live | none | 2026-11-04 | — | no catalyst lookup (outside the per-run budget) |
| GRE | spain | BME | 67.8 | -4.51 | EUR | 1.4x | 71.00 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | live | none | 2026-09-16 | — | no catalyst lookup (outside the per-run budget) |
| ATS | austria | VIE | 126.8 | +4.11 | EUR | 0.7x | 121.80 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | live | none | 2026-11-05 | — | no catalyst lookup (outside the per-run budget) |
| MMK | austria | VIE | 77.5 | +4.03 | EUR | 2.7x | 74.50 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | live | none | 2026-08-20 | — | no catalyst lookup (outside the per-run budget) |
| FCT | italy | MIL | 11.47 | -3.73 | EUR | 2.0x | 11.91 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | live | none | 2026-07-29 | — | no catalyst lookup (outside the per-run budget) |
| CNA | uk | LSE | 160.3 | +3.59 | GBX | 3.5x | 154.75 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | live | none | 2026-07-23 | — | no catalyst lookup (outside the per-run budget) |
| III | uk | LSE | 2614 | -3.54 | GBX | 1.9x | 2710.00 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | live | ADR (NASDAQ:CHEC) | 2026-11-12 | — | no catalyst lookup (outside the per-run budget) |
| UHR | switzerland | SIX | 196.75 | +3.39 | CHF | 2.1x | 190.30 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | live | none | 2026-07-21 | — | no catalyst lookup (outside the per-run budget) |
| OVH | france | EURONEXT | 15.23 | +3.25 | EUR | 0.6x | 14.75 | yahoo_chart_daily | 2026-11-12 | 2026-11-13 | live | ADR (OTC:OVHFF) | 2026-10-20 | — | no catalyst lookup (outside the per-run budget) |

## AU (ASX) — Headline table

| Ticker | Venue | Close | Chg % | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | Session asof | Settle | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PDN | ASX | 7.17 | -17.59 | AUD | 4.3x | 8.70 | yahoo_chart_daily | 2026-11-11 | 2026-11-13 | settled | none | 2026-11-04 | N | Fully underwritten A$525m equity raise announced Nov 12 for Patterson Lake South: placement at A$7.80, ~10% discount to the A$8.70 close, plus a C$50m bought deal and a non-underwritten retail offer |
| G6M | ASX | 2.41 | -12.04 | AUD | 2.5x | 2.74 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | settled | none | 2025-07-06 | — | no catalyst lookup (outside the per-run budget) |
| CU6 | ASX | 1.815 | -11.46 | AUD | 2.0x | 2.05 | yahoo_chart_daily | 2026-11-11 | 2026-11-13 | settled | none | 2026-08-26 | — | no catalyst lookup (outside the per-run budget) |
| RPL | ASX | 1.98 | -10.41 | AUD | 4.9x | 2.21 | yahoo_chart_daily | 2026-11-11 | 2026-11-13 | settled | none | 2026-08-23 | N | CY26 fund performance fee revenue and other income update lodged Nov 12 9:28am; the only other release was a securities trading policy on Nov 12 4:23pm |

## APAC/Gulf — Headline table

| Ticker | Market | Venue | Close | Chg % | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | Session asof | Settle | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ESIP | indonesia | IDX | 97 | +34.72 | IDR | 6.5x | 72.00 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| WMUU | indonesia | IDX | 49 | +32.43 | IDR | 3.6x | 37.00 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | settled | none | 2022-08-24 | — | no catalyst lookup (outside the per-run budget) |
| 300528 | china | SZSE | 17.99 | +20.01 | CNY | 4.7x | 14.99 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| ANUP | india | NSE | 1725 | +20.00 | INR | 6.9x | 1437.50 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | settled | none | 2026-11-06 | Y | Q2 FY27 results approved Nov 6: revenue INR 182.4 cr (-21% YoY, +46% QoQ), net profit INR 6.6 cr (-79% YoY), pending order book INR 941 cr; no Nov 13 release found |
| MSTCLTD | india | BSE | 783.65 | +20.00 | INR | 5.3x | 653.05 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| CHEMTECH | india | BSE | 60.28 | +19.98 | INR | 4.8x | 50.24 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| 300237 | china | SZSE | 3.26 | +19.85 | CNY | 4.8x | 2.72 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| HTECH | thailand | SET | 4.62 | +17.86 | THB | 6.2x | 3.92 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | settled | none | 2022-05-17 | N | no fresh catalyst found (no SET release on 13 Nov; Q3 report due 16 Nov - the last print was Q2 revenue THB 363.4m +18% with net income THB 48.1m +99%) |
| 300324 | china | SZSE | 3.88 | +17.58 | CNY | 4.6x | 3.30 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| SVOA | thailand | SET | 1.73 | -12.63 | THB | 7.5x | 1.98 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| SGC | thailand | SET | 1.69 | -11.98 | THB | 4.1x | 1.92 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| 4144 | ksa | TADAWUL | 73.9 | -8.43 | SAR | 2.4x | 80.70 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| F03 | singapore | SGX | 1.66 | -7.26 | SGD | 3.0x | 1.79 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | settled | none | 2026-08-11 | — | no catalyst lookup (outside the per-run budget) |
| EB5 | singapore | SGX | 2.97 | +6.45 | SGD | 1.9x | 2.79 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | settled | none | 2026-08-13 | — | no catalyst lookup (outside the per-run budget) |
| 4280 | ksa | TADAWUL | 12.65 | -6.43 | SAR | 2.4x | 13.52 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | settled | none | 2026-08-06 | — | no catalyst lookup (outside the per-run budget) |
| 9618 | ksa | TADAWUL | 29 | +5.92 | SAR | 1.0x | 27.38 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| VGL | newzealand | NZX | 2.78 | +4.51 | NZD | 2.5x | 2.66 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | settled | none | 2026-08-02 | — | no catalyst lookup (outside the per-run budget) |
| AWX | singapore | SGX | 7.1 | +4.41 | SGD | 0.8x | 6.80 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | settled | none | 2026-08-12 | Y | Q3 2026 results released Nov 10; FY2026 revenue guidance raised to SGD 630-680m from SGD 550-600m, AMPS backlog above SGD 400m |
| FCG | newzealand | NZX | 5.29 | -2.94 | NZD | 2.1x | 5.45 | yahoo_chart_daily | 2026-11-11 | 2026-11-12 | settled | none | 2026-03-23 | — | no catalyst lookup (outside the per-run budget) |

## Source health

- scanner_calls: 55 | scanner_errors: 0
- markets_scanned: US + 17 EU/UK + ASX + 7 APAC/Gulf (india, thailand, indonesia, china, singapore, newzealand, ksa)
- pipeline_version: 2026-11-12.2
- et_clock: zoneinfo America/New_York (DST-aware; a fixed UTC-4 mislabels every winter fire)
- premarket_window: 04:00-09:30 ET, resolved with zoneinfo (09:00-14:30 UTC in winter, 08:00-13:30 UTC in summer)
- session_selection: by DATE and order, never by a modal time-of-day. Yahoo stamps a daily bar at the session open, so the ET stamp of the SAME session shifts by one hour across a DST boundary; a modal filter kept the OLDER bars and discarded the NEWEST ones, which rolled the base back to the prior-prior session (66 US + 21 ASX rows lost on 2026-11-03, 24 of 25 ASX rows lost on 2026-11-04).
- yahoo_calls: 104 | yahoo_429: 0 | yahoo_errors: 1
- reference_close (screener vs Yahoo, resolved BEFORE the tables were built): agree=92 mismatch=1 unverified=1 stale_reference=1
  method: the screener's implied reference close (close / (1 + change/100)) is compared
  with Yahoo's own reference close. A match proves the move was measured against the
  TRUE prior close; a mismatch means the row sits on a STALE reference (phantom move).
  Coverage: every row of the US headline, US QUIET, EU/UK and ASX tables is checked.
  Yahoo bar mode: {"closed": 63, "live": 29} (closed = last completed session bar;
  live = in-progress EU/UK session bar, which is what a weekday 08:00 ET EU move needs)
  live drift between the screener snapshot and the later Yahoo print: median=0.00pp max=1.35pp (expected on a live market)
- cross_check mismatches: [{"region": "indonesia", "symbol": "MKNT.JK", "tv": 33.333, "yahoo": 0.0, "delta": 33.333, "ref_delta_pct": -25.0, "tv_implied_ref": 24.0, "yahoo_ref": 32.0, "yahoo_date": "2026-11-11", "yahoo_ref_date": "2026-11-10", "verdict": "stale_reference"}]
- rows_dropped_stale_ref: 1 (rows whose screener-implied reference close disagreed with Yahoo's by more than 0.5%; they are dropped, not published)
- rows_dropped_unresolved_ref: 1 (rows whose reference close could not be resolved from Yahoo at all - the base of the move is unverifiable, so the row is dropped rather than published with a '—' base)
- us_premarket_check (Yahoo 1-min pre/post feed vs the screener pre-market column, base = the IMMEDIATELY prior session's close): checked=9 within_1pp=9 within_3pp=9 unavailable=1
- markets_with_lt5_rows: ['uk:egreater=2', 'france:egreater=1', 'france:less=3', 'netherlands:egreater=0', 'netherlands:less=0', 'belgium:egreater=0', 'belgium:less=0', 'portugal:egreater=0', 'portugal:less=0', 'ireland:egreater=0', 'ireland:less=0', 'italy:egreater=2', 'italy:less=4', 'switzerland:egreater=3', 'switzerland:less=2', 'spain:egreater=1', 'spain:less=3', 'denmark:egreater=1', 'denmark:less=1', 'finland:egreater=0', 'finland:less=0', 'poland:egreater=0', 'poland:less=1', 'austria:egreater=2', 'austria:less=1', 'greece:egreater=0', 'greece:less=0', 'singapore:egreater=3', 'singapore:less=1', 'newzealand:egreater=1', 'newzealand:less=1']
  NOTE: this fires per market AND direction, so it is NOT a coverage-failure signal on
  its own. A 'less' count of 0-3 means almost nothing fell more than 2.5% that session
  (a broad up-day); a small 'egreater' count usually means a small market with few
  names above the $1B market-cap floor. Check the median change before calling it a gap.
- filters: volume>10000 (removes stale-reference rows), country=home for EU/UK/AU,
  exchange drop-list for US, US venue allow-list, US preferred (slash ticker) excluded
- volume_floor_note: volume>10000 removes MOST stale-reference rows, but a row can
  still sit on a stale reference when its only volume came from one thin day (verified
  2026-10-26: LSE 50GP cleared the floor on 12,000 shares dated 2026-10-15 while Yahoo
  showed no bar for the scan date). The reference-close cross-check is what catches
  those; rows that fail it are dropped from the tables, not published.
- us_preferred_dropped: 59
- bod_no_extended_hours: 122 (deferred to the next scan; not in the headline table)
- earnings_source: screener `earnings_release_date` (last FULL report) + `earnings_release_next_date` (next scheduled)
- earnings_caveat: `earnings_release_date` does NOT capture preliminary, guidance or
  restructuring releases. On 2026-10-23 LKQ fell 22.47% on a preliminary Q3 miss while
  the field still read 2026-07-30. ALWAYS confirm the earnings-driven flag against the
  headline itself; the calendar field is a screen, not a verdict.
- us_line_index: ok (US-listed lines for the 25 foreign home countries, both scanner types; the `US tradeable` column is ADR / US-listed / none)
- catalyst_note: Catalyst lookups: 5 US + 3 EU + 2 AU + 3 APAC/Gulf = 13 per run, the skill's cap.
- catalyst_merge: region-matched - a row may only use a catalog entry from its OWN region;
  the same ticker on another venue is a different company and is not used.
- catalyst_budget: 5 US + 3 EU + 2 AU = 10 lookups per run
- one_table_rule: each name appears exactly once, in exactly one table, with its
  catalyst in that row's last column. There is no separate catalysts section.
- data_date: US regular session close of the prior trading day; extended-hours columns
  carry the prior session's prints
- settlement_state: 23 settled, 29 live (a live row's move is a mid-session snapshot, not the session's result)
- rows_per_market (EU/UK, cap 4/market): {'norway': 4, 'sweden': 4, 'italy': 4, 'spain': 4, 'uk': 4, 'poland': 1, 'germany': 4, 'france': 4, 'austria': 3, 'switzerland': 4, 'denmark': 2} — the cap stops one thin market taking the table; the EU/UK table was 28% Sweden over nine runs (73 of 264 rows) while Belgium and Greece never appeared once.
- rows_per_market (APAC/Gulf, cap 3/market): {'indonesia': 3, 'china': 3, 'india': 3, 'thailand': 3, 'ksa': 3, 'singapore': 3, 'newzealand': 2}
- deprecations: mcp__tradingview-advanced__*, mcp__tradingview__*, mcp__financekit__*,
  mcp__stocktwits__* are ABSENT in Cloud sessions (tool_search 0 hits; connector catalog
  holds only media + credential tools). The public screener replaces them.

- degraded_sources: 2
  (the chat reply's `errors:` MUST equal this number - one entry per degraded
  source, not one per run)
  1. yahoo_chart_api.reference_close_unresolved — QQ..L: the reference close could not be resolved (429 or a bad body)
  2. yahoo_premarket_check.unavailable — TRV: Yahoo's 1-minute pre-market feed returned no usable print

## Audit line

`earnings-reaction target=earnings-reactions:2026-11-13 candidates=432 amc_reactions=0 pre_gaps=25 eu_reactions=29 asx_reactions=4 apac_reactions=18 catalyst_lookups=13 bod=122 rows_dropped_stale_ref=1 rows_dropped_unresolved_ref=1 degraded_sources=2`
