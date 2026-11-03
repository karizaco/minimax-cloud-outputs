# Earnings reaction scanner — 2026-11-03

- Cron: `0 8 * * 1-5` America/New_York (weekdays, 08:00 ET)
- Fire time (ET): 2026-11-03 08:02 Tue — the canonical 08:00 ET weekday slot.
- Run type: `on_cycle`. The pre-market columns are LIVE (captured ~08:03 ET,
  before the 09:30 ET US open).
  Correction: the pipeline's own header printed "09:03:48" and labelled this run
  `validation_run_offcycle`. That came from a hardcoded UTC-4 Eastern offset
  inside the pipeline (US/Eastern is UTC-5 on this date — DST ended 2026-11-01),
  so the fire time was printed one hour late. The same offset shifted its Yahoo
  pre-market window one hour early (see `pre_market_recheck` in Source health).
- Source: TradingView public screener (`scanner.tradingview.com/<market>/scan`);
  Yahoo chart API as an independent cross-check on the reported movers.
- Method: 4 passes (US top-200 mcap, US prior-session movers, EU/UK movers,
  ASX movers). Volume floor 10,000 on every pass; `country` filter for
  primary listings; exchange drop-list applied.
- Status: `ok`

## TL;DR

- 0 AMC reactions, 6 pre-market gaps, 151 without extended-hours data; 29 EU/UK and 7 ASX movers.
- Biggest US extended-hours move: HLMN PRE_GAP (4.65%).
- Biggest EU/UK move: TMV (-27.18%, germany).
- Biggest ASX move: QAN (+6.36%).
- EU/AU earnings-driven tagging is keyword-based on headlines (best-effort).

## US — Headline table

| Ticker | Venue | Close | Chg % | Pre-mkt % | Post-mkt % | Last earnings | Tag |
|---|---|---|---|---|---|---|---|
| HLMN | NASDAQ | 8.39 | 7.56 | -4.65 | — | 2026-11-02 (1d ago) | PRE_GAP |
| UPWK | NASDAQ | 9.72 | 6.23 | 4.64 | — | 2026-11-02 (1d ago) | PRE_GAP |
| ECO | NYSE | 91.25 | -9.95 | 3.52 | — | 2026-08-04 (91d ago) | PRE_GAP |
| PGR | NYSE | 233.92 | 1.14 | -3.47 | — | 2026-10-14 (20d ago) | PRE_GAP |
| AESI | NYSE | 8.23 | -10.74 | -2.43 | — | 2026-11-02 (1d ago) | PRE_GAP |
| ULCC | NASDAQ | 7.43 | 15.19 | -2.42 | — | 2026-10-28 (6d ago) | PRE_GAP |

## US — QUIET one-liners

| Ticker | Venue | Chg % | Pre-mkt % | Post-mkt % |
|---|---|---|---|---|
| MPC | NYSE | -3.22 | 2.00 | — |
| KRYS | NASDAQ | -10.95 | -1.99 | — |
| CRM | NYSE | -1.30 | -1.99 | — |
| ICE | NYSE | 2.03 | -1.98 | — |
| AXTI | NASDAQ | -12.46 | 1.97 | — |
| FRO | NYSE | -8.47 | 1.96 | — |
| DHI | NYSE | 4.75 | -1.95 | — |
| GLW | NYSE | -0.09 | 1.95 | — |
| AVGO | NASDAQ | -1.18 | 1.95 | — |
| RACE | NYSE | 1.79 | 1.90 | — |
| WGS | NASDAQ | -7.20 | 1.89 | — |
| LITE | NASDAQ | -18.59 | 1.88 | — |
| PURR | NASDAQ | -11.81 | 1.85 | — |
| RIOT | NASDAQ | -7.57 | 1.85 | — |
| APLD | NASDAQ | -8.95 | 1.85 | — |

## EU/UK — Headline table

| Ticker | Market | Venue | Close | Chg % | Currency | Last earnings |
|---|---|---|---|---|---|---|
| TMV | germany | XETR | 5.265 | -27.18 | EUR | 2026-07-28 |
| TRUE_B | sweden | OMXSTO | 19.56 | -17.64 | SEK | 2026-11-03 |
| KABE_B | sweden | OMXSTO | 287 | +16.19 | SEK | — |
| RAY_B | sweden | OMXSTO | 167.3 | -15.08 | SEK | 2026-08-13 |
| BCHN | switzerland | SIX | 544 | +14.53 | CHF | 2026-06-04 |
| NCOD | norway | OSL | 26 | +11.59 | NOK | 2025-02-13 |
| REJL_B | sweden | OMXSTO | 137.4 | -9.01 | SEK | 2026-07-15 |
| DRX | uk | LSE | 878 | +8.53 | GBX | 2026-07-30 |
| BMAG | austria | VIE | 35 | -8.50 | EUR | — |
| MULTI | norway | OSL | 128.4 | -7.76 | NOK | 2026-11-03 |
| GENO | norway | OSL | 18.94 | -7.38 | NOK | 2026-08-13 |
| BERNER_B | sweden | OMXSTO | 69.2 | -7.24 | SEK | 2026-07-17 |
| PHIA | netherlands | EURONEXT | 26.12 | +6.53 | EUR | 2026-11-03 |
| ACAD | sweden | OMXSTO | 124 | +6.35 | SEK | 2026-11-03 |
| BAYN | germany | GETTEX | 52.88 | +6.16 | EUR | 2026-11-03 |
| DVYSR | sweden | OMXSTO | 65 | +5.69 | SEK | 2026-07-20 |
| PPGN | switzerland | SIX | 43.7 | +5.68 | CHF | 2026-08-13 |
| ACP | poland | GPW | 235.7 | -5.38 | PLN | 2026-08-27 |
| EVD | germany | XETR | 61.2 | -5.04 | EUR | 2026-08-20 |
| BIM | france | EURONEXT | 94.95 | +5.03 | EUR | 2026-07-28 |
| DAR | uk | LSE | 7.25 | -4.92 | USD | 2026-09-24 |
| NEM | germany | XETR | 72.45 | -4.80 | EUR | 2026-07-30 |
| SILEX | sweden | OMXSTO | 151.45 | +4.74 | SEK | 2026-07-17 |
| BPT | uk | LSE | 403.6 | -4.63 | GBX | 2026-07-17 |
| ALO | france | EURONEXT | 11.16 | -4.49 | EUR | 2026-05-13 |
| JDW | uk | LSE | 1030 | -4.45 | GBX | 2026-10-02 |
| NORCO | norway | OSL | 36.9 | -4.40 | NOK | 2026-08-20 |
| ZAL | germany | XETR | 25.83 | -4.30 | EUR | 2026-08-04 |
| VER | sweden | OMXSTO | 9.48 | -4.24 | SEK | 2026-08-27 |

## AU (ASX) — Headline table

| Ticker | Venue | Close | Chg % | Currency | Last earnings |
|---|---|---|---|---|---|
| QAN | ASX | 9.36 | +6.36 | AUD | 2026-08-26 |
| BJY | ASX | 8.47 | +6.14 | AUD | 2026-08-26 |
| HVN | ASX | 4.37 | +5.81 | AUD | 2026-08-27 |
| WBT | ASX | 2.23 | -5.51 | AUD | 2026-08-28 |
| NHC | ASX | 5.61 | -5.40 | AUD | 2026-09-14 |
| VMM | ASX | 3.37 | -5.34 | AUD | 2026-03-13 |
| HMC | ASX | 3.16 | +5.33 | AUD | 2026-08-25 |

## Catalysts

<!-- AGENT: fill catalyst text for the tickers in <date>-catalyst-targets.json, then
     write it to /workspace/catalog/catalysts/<date>.md (so a re-run does not wipe it)
     OR edit this table in place. Cap: 5 US + 3 EU + 2 AU. Never fabricate a headline. -->

| Ticker | Region | Catalyst | Earnings-driven |
|---|---|---|---|
| HLMN | US | Q3 2026 (Nov 2, after close): adj EPS $0.22 vs $0.21 est; revenue $457.5M vs $462.1M est (1% miss); net sales +7.7% to a record $457.5M; FY26 adj EBITDA guidance (~ $285M) reaffirmed, net sales guidance narrowed to $1.660-1.680B. Q3 call 08:30 ET on Nov 3 | Y |
| UPWK | US | Q3 2026 (Nov 2, after close): adj EPS $0.40 vs ~$0.31 est and adj EBITDA $63.8M beat, but Q4/FY26 revenue guided below consensus ($169-177M Q4); FY26 adj EPS guide raised to $1.45-1.47; acquires WorkMotion (Lifted) | Y |
| AESI | US | Q3 2026 (Nov 2, after close): net loss $45.1M, revenue $267.8M (vs $293.2M in Q2), adj EBITDA $30.3M vs $50.8M; closed a $424M senior secured bridge facility and signed cost-reimbursement agreements covering 283 MW for two frontier-AI-lab data-centre projects; Q4 adj EBITDA guided to $40-50M | Y |
| ULCC | US | Q3 2026 (Oct 28): record revenue of $1.4B, +53% y/y, adj EPS $0.18 vs -$0.06 est; the Nov 2 +15.2% leg came from the oil-price collapse plus UBS raising its target to $7.00 and the appointment of a new COO | Y |
| ECO | US | No fresh catalyst found — shares gapped down -9.94% to $91.25 on Nov 2 and Q3 results are due Nov 11; no company release located for the gap | N |
| PGR | US | No fresh catalyst found (outside the 5-name US catalyst budget for this run) | N |
| TMV | EU | TeamViewer Q3 2026 (published Nov 3): revenue EUR 184.5M, -3.9% y/y (-2.2% cc), ARR EUR 736.9M (-2.6%), adj EBITDA EUR 78.9M (-10%); FY26 revenue guidance cut to -1%/-2% cc from 0%/+3%; shares broke ~25% to a July low of EUR 5.35 | Y |
| TRUE_B | EU | Truecaller final Q3 2026 report released today (call 13:00 CET); the Oct 19 preliminary numbers had net sales SEK 464M, +3% cc, but adj EBITDA margin 31.8% vs 34.7% a year earlier — the margin slide drove the sell-off | Y |
| KABE_B | EU | Q3 2026 interim report published 08:00 CET today: net sales SEK 2,794M (+11%), net profit SEK 168M vs SEK 73M, EPS SEK 18.67 vs SEK 8.11, operating margin 7.0% vs 3.3% | Y |
| QAN | AU | Oil collapse, not earnings: Brent settled -7.63% at $104.77 and WTI -7.36% at $96.46 overnight on US-Iran peace progress; Qantas +6.36% to A$9.36 (highest since early September), with Virgin Australia +8.9% — an airline-sector move; the RBA hiked 25bp to 4.85% the same day | N |
| BJY | AU | No fresh catalyst found | N |


## Source health

- scanner_calls: 39 | scanner_errors: 0
- pipeline_version: 2026-10-26.2
- yahoo_calls: 142 | yahoo_429: 3 | yahoo_errors: 0
- cross_check (screener vs Yahoo, reference-close validation): agree=40 mismatch=88 unverified=2 stale_reference=88
  method: the screener's implied reference close (close / (1 + change/100)) is compared
  with Yahoo's own reference close. A match proves the move was measured against the
  TRUE prior close; a mismatch means the row sits on a STALE reference (phantom move).
  Coverage: every row of the US headline, EU/UK and ASX tables is checked. The US QUIET
  one-liner table is NOT cross-checked.
  Yahoo bar mode: {"closed": 11, "live": 29} (closed = last completed session bar;
  live = in-progress EU/UK session bar, which is what a weekday 08:00 ET EU move needs)
  live drift between the screener snapshot and the later Yahoo print: median=0.27pp max=15.66pp (expected on a live market)
- cross_check coverage: 42 rows are published (6 US headline + 29 EU/UK + 7 ASX); 40 agree
  with Yahoo's reference close and 2 could not be checked at all (Yahoo returned 429 on
  those fetches). ALL 88 mismatches are `stale_reference` rows that were DROPPED from
  the tables before publication, not published rows that disagree — no published row
  failed the reference-close test.
- independent corroboration for the two rate-limited rows: TMV's move is confirmed by
  same-day wire reports (MarketWatch -23.51% at 10:06 CEST, dpa-AFX -25.7%, Investing.com
  -23.79%); a re-check of the 37 EU/ASX symbols found only transient 429s.
- cross_check mismatches: [{"region": "US", "symbol": "SHOP", "tv": -0.806, "yahoo": -5.632, "delta": 4.826, "ref_delta_pct": -5.632, "tv_implied_ref": 157.49, "yahoo_ref": 166.89, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "AEHR", "tv": -6.231, "yahoo": -10.325, "delta": 4.094, "ref_delta_pct": -10.325, "tv_implied_ref": 54.89, "yahoo_ref": 61.21, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "PLTR", "tv": -3.134, "yahoo": -6.267, "delta": 3.133, "ref_delta_pct": -6.267, "tv_implied_ref": 184.11, "yahoo_ref": 196.42, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "SRAD", "tv": 6.983, "yahoo": -1.635, "delta": 8.618, "ref_delta_pct": -1.635, "tv_implied_ref": 12.03, "yahoo_ref": 12.23, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "AVEX", "tv": -5.646, "yahoo": -9.01, "delta": 3.364, "ref_delta_pct": -9.01, "tv_implied_ref": 12.22, "yahoo_ref": 13.43, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "UPST", "tv": -7.428, "yahoo": -7.327, "delta": -0.101, "ref_delta_pct": -7.327, "tv_implied_ref": 23.02, "yahoo_ref": 24.84, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "SNDK", "tv": -6.587, "yahoo": -13.47, "delta": 6.883, "ref_delta_pct": -13.47, "tv_implied_ref": 1150.89, "yahoo_ref": 1330.05, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "KLAC", "tv": -3.04, "yahoo": -5.686, "delta": 2.646, "ref_delta_pct": -5.686, "tv_implied_ref": 157.91, "yahoo_ref": 167.43, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "AAPL", "tv": -1.831, "yahoo": -1.227, "delta": -0.604, "ref_delta_pct": -1.227, "tv_implied_ref": 344.63, "yahoo_ref": 348.91, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "PENG", "tv": -8.531, "yahoo": -11.669, "delta": 3.138, "ref_delta_pct": -11.669, "tv_implied_ref": 51.93, "yahoo_ref": 58.79, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "MXL", "tv": -9.1, "yahoo": -5.781, "delta": -3.319, "ref_delta_pct": -5.781, "tv_implied_ref": 67.47, "yahoo_ref": 71.61, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "ALAB", "tv": -11.221, "yahoo": -10.925, "delta": -0.296, "ref_delta_pct": -10.925, "tv_implied_ref": 258.7, "yahoo_ref": 290.43, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "VICR", "tv": -8.436, "yahoo": -7.516, "delta": -0.92, "ref_delta_pct": -7.516, "tv_implied_ref": 191.09, "yahoo_ref": 206.62, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "MU", "tv": -5.781, "yahoo": -5.301, "delta": -0.48, "ref_delta_pct": -5.301, "tv_implied_ref": 884.74, "yahoo_ref": 934.27, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "BWLP", "tv": -6.158, "yahoo": -3.324, "delta": -2.834, "ref_delta_pct": -3.324, "tv_implied_ref": 25.01, "yahoo_ref": 25.87, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "AMAT", "tv": -3.989, "yahoo": -7.487, "delta": 3.498, "ref_delta_pct": -7.487, "tv_implied_ref": 390.09, "yahoo_ref": 421.66, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "TRMD", "tv": -6.723, "yahoo": -0.825, "delta": -5.898, "ref_delta_pct": -0.825, "tv_implied_ref": 42.69, "yahoo_ref": 43.045, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "INTC", "tv": -8.805, "yahoo": -28.576, "delta": 19.771, "ref_delta_pct": -28.576, "tv_implied_ref": 65.76, "yahoo_ref": 92.07, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "NET", "tv": -5.533, "yahoo": -9.539, "delta": 4.006, "ref_delta_pct": -9.539, "tv_implied_ref": 280.7, "yahoo_ref": 310.3, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "OVV", "tv": -6.665, "yahoo": 1.467, "delta": -8.132, "ref_delta_pct": 1.467, "tv_implied_ref": 72.62, "yahoo_ref": 71.57, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "LRCX", "tv": -4.83, "yahoo": -6.007, "delta": 1.177, "ref_delta_pct": -6.007, "tv_implied_ref": 239.11, "yahoo_ref": 254.39, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "TTMI", "tv": -7.668, "yahoo": -5.352, "delta": -2.316, "ref_delta_pct": -5.352, "tv_implied_ref": 82.94, "yahoo_ref": 87.63, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "ADI", "tv": -1.021, "yahoo": -3.732, "delta": 2.711, "ref_delta_pct": -3.732, "tv_implied_ref": 417.11, "yahoo_ref": 433.28, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "AAOI", "tv": -9.486, "yahoo": -12.805, "delta": 3.319, "ref_delta_pct": -12.805, "tv_implied_ref": 69.05, "yahoo_ref": 79.19, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "CRDO", "tv": -7.265, "yahoo": -8.651, "delta": 1.386, "ref_delta_pct": -8.651, "tv_implied_ref": 150.99, "yahoo_ref": 165.29, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "UCTT", "tv": -5.794, "yahoo": -9.122, "delta": 3.328, "ref_delta_pct": -9.122, "tv_implied_ref": 49.71, "yahoo_ref": 54.7, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "AMD", "tv": -7.52, "yahoo": -10.879, "delta": 3.359, "ref_delta_pct": -10.879, "tv_implied_ref": 504.8, "yahoo_ref": 566.42, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "MHK", "tv": 6.578, "yahoo": 7.247, "delta": -0.669, "ref_delta_pct": 7.247, "tv_implied_ref": 139.41, "yahoo_ref": 129.99, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "AMKR", "tv": -6.43, "yahoo": -4.149, "delta": -2.281, "ref_delta_pct": -4.149, "tv_implied_ref": 39.5, "yahoo_ref": 41.21, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "DDOG", "tv": -8.148, "yahoo": -11.499, "delta": 3.351, "ref_delta_pct": -11.499, "tv_implied_ref": 235.27, "yahoo_ref": 265.84, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "VYX", "tv": 5.189, "yahoo": 3.163, "delta": 2.026, "ref_delta_pct": 3.163, "tv_implied_ref": 8.48, "yahoo_ref": 8.22, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "WDC", "tv": -7.517, "yahoo": -7.41, "delta": -0.107, "ref_delta_pct": -7.41, "tv_implied_ref": 366.11, "yahoo_ref": 395.41, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "CIFR", "tv": -5.898, "yahoo": -10.0, "delta": 4.102, "ref_delta_pct": -10.0, "tv_implied_ref": 7.29, "yahoo_ref": 8.1, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "SM", "tv": -7.281, "yahoo": 2.021, "delta": -9.302, "ref_delta_pct": 2.021, "tv_implied_ref": 40.38, "yahoo_ref": 39.58, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "LUNR", "tv": -7.591, "yahoo": -8.647, "delta": 1.056, "ref_delta_pct": -8.647, "tv_implied_ref": 10.67, "yahoo_ref": 11.68, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "GLXY", "tv": -8.812, "yahoo": -11.748, "delta": 2.935, "ref_delta_pct": -11.748, "tv_implied_ref": 16.0, "yahoo_ref": 18.13, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "SSMR", "tv": -9.772, "yahoo": -7.251, "delta": -2.521, "ref_delta_pct": -7.251, "tv_implied_ref": 12.28, "yahoo_ref": 13.24, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "EROC", "tv": -5.389, "yahoo": -6.912, "delta": 1.523, "ref_delta_pct": -6.912, "tv_implied_ref": 8.35, "yahoo_ref": 8.97, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "FCX", "tv": 0.8, "yahoo": -5.549, "delta": 6.349, "ref_delta_pct": -5.549, "tv_implied_ref": 62.47, "yahoo_ref": 66.14, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "SITM", "tv": -6.523, "yahoo": -8.404, "delta": 1.881, "ref_delta_pct": -8.404, "tv_implied_ref": 447.06, "yahoo_ref": 488.08, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "STX", "tv": -7.884, "yahoo": -7.979, "delta": 0.095, "ref_delta_pct": -7.979, "tv_implied_ref": 644.58, "yahoo_ref": 700.47, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "NVTS", "tv": -6.486, "yahoo": -7.826, "delta": 1.34, "ref_delta_pct": -7.826, "tv_implied_ref": 8.48, "yahoo_ref": 9.2, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "ALGM", "tv": 5.306, "yahoo": -7.569, "delta": 12.875, "ref_delta_pct": -7.569, "tv_implied_ref": 30.53, "yahoo_ref": 33.03, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "TSEM", "tv": -6.704, "yahoo": -11.409, "delta": 4.705, "ref_delta_pct": -11.409, "tv_implied_ref": 166.48, "yahoo_ref": 187.92, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "HUT", "tv": -7.399, "yahoo": -10.596, "delta": 3.197, "ref_delta_pct": -10.596, "tv_implied_ref": 59.4, "yahoo_ref": 66.44, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "CIEN", "tv": -11.343, "yahoo": -8.221, "delta": -3.122, "ref_delta_pct": -8.221, "tv_implied_ref": 320.72, "yahoo_ref": 349.45, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "P", "tv": -10.395, "yahoo": -7.449, "delta": -2.946, "ref_delta_pct": -7.449, "tv_implied_ref": 126.98, "yahoo_ref": 137.2, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "QNT", "tv": -7.887, "yahoo": -10.4, "delta": 2.513, "ref_delta_pct": -10.4, "tv_implied_ref": 33.6, "yahoo_ref": 37.5, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "FLUT", "tv": 6.139, "yahoo": 4.293, "delta": 1.846, "ref_delta_pct": 4.293, "tv_implied_ref": 82.59, "yahoo_ref": 79.19, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "APPF", "tv": 5.444, "yahoo": 2.994, "delta": 2.45, "ref_delta_pct": 2.994, "tv_implied_ref": 213.25, "yahoo_ref": 207.05, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "CRWV", "tv": -8.602, "yahoo": -9.664, "delta": 1.062, "ref_delta_pct": -9.664, "tv_implied_ref": 54.87, "yahoo_ref": 60.74, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "IREN", "tv": -8.058, "yahoo": -8.762, "delta": 0.704, "ref_delta_pct": -8.762, "tv_implied_ref": 23.95, "yahoo_ref": 26.25, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "MRVL", "tv": -12.724, "yahoo": -10.049, "delta": -2.675, "ref_delta_pct": -10.049, "tv_implied_ref": 196.4, "yahoo_ref": 218.34, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "ABSI", "tv": -12.938, "yahoo": -8.017, "delta": -4.921, "ref_delta_pct": -8.017, "tv_implied_ref": 11.13, "yahoo_ref": 12.1, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "URGN", "tv": 5.012, "yahoo": -2.27, "delta": 7.282, "ref_delta_pct": -2.27, "tv_implied_ref": 32.72, "yahoo_ref": 33.48, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "SMCI", "tv": -7.618, "yahoo": -4.299, "delta": -3.319, "ref_delta_pct": -4.299, "tv_implied_ref": 32.95, "yahoo_ref": 34.43, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "TXN", "tv": 0.392, "yahoo": -3.867, "delta": 4.259, "ref_delta_pct": -3.867, "tv_implied_ref": 300.84, "yahoo_ref": 312.94, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "CLS", "tv": -6.142, "yahoo": -6.09, "delta": -0.052, "ref_delta_pct": -6.09, "tv_implied_ref": 265.53, "yahoo_ref": 282.75, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "LGIH", "tv": 6.874, "yahoo": 1.44, "delta": 5.434, "ref_delta_pct": 1.44, "tv_implied_ref": 44.37, "yahoo_ref": 43.74, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "NBIS", "tv": -8.272, "yahoo": -10.379, "delta": 2.107, "ref_delta_pct": -10.379, "tv_implied_ref": 154.14, "yahoo_ref": 171.99, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "SCCO", "tv": 1.031, "yahoo": -7.416, "delta": 8.447, "ref_delta_pct": -7.416, "tv_implied_ref": 175.6679, "yahoo_ref": 189.7388, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "DPC", "tv": 5.734, "yahoo": -6.521, "delta": 12.255, "ref_delta_pct": -6.521, "tv_implied_ref": 27.38, "yahoo_ref": 29.29, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "VRT", "tv": -3.553, "yahoo": -5.457, "delta": 1.904, "ref_delta_pct": -5.457, "tv_implied_ref": 232.5, "yahoo_ref": 245.92, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "LOW", "tv": 4.343, "yahoo": 0.864, "delta": 3.479, "ref_delta_pct": 0.864, "tv_implied_ref": 209.07, "yahoo_ref": 207.28, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "BTDR", "tv": -8.048, "yahoo": -11.478, "delta": 3.43, "ref_delta_pct": -11.478, "tv_implied_ref": 6.71, "yahoo_ref": 7.58, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "BUUU", "tv": -5.892, "yahoo": 4.623, "delta": -10.515, "ref_delta_pct": 4.623, "tv_implied_ref": 6.11, "yahoo_ref": 5.84, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "ASTS", "tv": -11.325, "yahoo": -4.876, "delta": -6.449, "ref_delta_pct": -4.876, "tv_implied_ref": 40.97, "yahoo_ref": 43.07, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "AEM", "tv": 3.041, "yahoo": -5.991, "delta": 9.032, "ref_delta_pct": -5.991, "tv_implied_ref": 165.38, "yahoo_ref": 175.92, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "US", "symbol": "VRTX", "tv": -1.025, "yahoo": 3.496, "delta": -4.521, "ref_delta_pct": 3.496, "tv_implied_ref": 558.88, "yahoo_ref": 540.0, "yahoo_date": "2026-10-30", "verdict": "stale_reference"}, {"region": "germany", "symbol": "LHA.DE", "tv": 4.725, "yahoo": 4.071, "delta": 0.654, "ref_delta_pct": -0.803, "tv_implied_ref": 7.408, "yahoo_ref": 7.468, "yahoo_date": "2026-11-03", "verdict": "stale_reference"}, {"region": "AU", "symbol": "AMP.AX", "tv": -9.362, "yahoo": -7.48, "delta": -1.882, "ref_delta_pct": -7.48, "tv_implied_ref": 2.35, "yahoo_ref": 2.54, "yahoo_date": "2026-11-01", "verdict": "stale_reference"}, {"region": "AU", "symbol": "VGN.AX", "tv": 8.871, "yahoo": 2.905, "delta": 5.966, "ref_delta_pct": 2.905, "tv_implied_ref": 2.48, "yahoo_ref": 2.41, "yahoo_date": "2026-11-01", "verdict": "stale_reference"}, {"region": "AU", "symbol": "SIQ.AX", "tv": -7.973, "yahoo": -1.149, "delta": -6.824, "ref_delta_pct": -1.149, "tv_implied_ref": 12.04, "yahoo_ref": 12.18, "yahoo_date": "2026-11-01", "verdict": "stale_reference"}, {"region": "AU", "symbol": "4DX.AX", "tv": -7.308, "yahoo": 6.557, "delta": -13.865, "ref_delta_pct": 6.557, "tv_implied_ref": 2.6, "yahoo_ref": 2.44, "yahoo_date": "2026-11-01", "verdict": "stale_reference"}, {"region": "AU", "symbol": "TPW.AX", "tv": 6.96, "yahoo": 3.409, "delta": 3.551, "ref_delta_pct": 3.409, "tv_implied_ref": 5.46, "yahoo_ref": 5.28, "yahoo_date": "2026-11-01", "verdict": "stale_reference"}, {"region": "AU", "symbol": "NWL.AX", "tv": 6.912, "yahoo": 0.997, "delta": 5.915, "ref_delta_pct": 0.997, "tv_implied_ref": 18.23, "yahoo_ref": 18.05, "yahoo_date": "2026-11-01", "verdict": "stale_reference"}, {"region": "AU", "symbol": "VEA.AX", "tv": -6.574, "yahoo": 1.404, "delta": -7.978, "ref_delta_pct": 1.404, "tv_implied_ref": 2.89, "yahoo_ref": 2.85, "yahoo_date": "2026-11-01", "verdict": "stale_reference"}, {"region": "AU", "symbol": "YAL.AX", "tv": -6.425, "yahoo": -0.817, "delta": -5.608, "ref_delta_pct": -0.817, "tv_implied_ref": 6.07, "yahoo_ref": 6.12, "yahoo_date": "2026-11-01", "verdict": "stale_reference"}, {"region": "AU", "symbol": "NCK.AX", "tv": 5.551, "yahoo": -1.661, "delta": 7.212, "ref_delta_pct": -1.661, "tv_implied_ref": 12.43, "yahoo_ref": 12.64, "yahoo_date": "2026-11-01", "verdict": "stale_reference"}, {"region": "AU", "symbol": "MMS.AX", "tv": -5.531, "yahoo": 0.989, "delta": -6.52, "ref_delta_pct": 0.989, "tv_implied_ref": 20.43, "yahoo_ref": 20.23, "yahoo_date": "2026-11-01", "verdict": "stale_reference"}, {"region": "AU", "symbol": "LLC.AX", "tv": 5.508, "yahoo": 3.057, "delta": 2.451, "ref_delta_pct": 3.057, "tv_implied_ref": 2.36, "yahoo_ref": 2.29, "yahoo_date": "2026-11-01", "verdict": "stale_reference"}, {"region": "AU", "symbol": "NXT.AX", "tv": 5.378, "yahoo": 1.363, "delta": 4.015, "ref_delta_pct": 1.363, "tv_implied_ref": 5.95, "yahoo_ref": 5.87, "yahoo_date": "2026-11-01", "verdict": "stale_reference"}, {"region": "AU", "symbol": "PYC.AX", "tv": -5.263, "yahoo": 1.064, "delta": -6.327, "ref_delta_pct": 1.064, "tv_implied_ref": 1.9, "yahoo_ref": 1.88, "yahoo_date": "2026-11-01", "verdict": "stale_reference"}, {"region": "AU", "symbol": "ZIP.AX", "tv": 5.234, "yahoo": 1.397, "delta": 3.837, "ref_delta_pct": 1.397, "tv_implied_ref": 1.815, "yahoo_ref": 1.79, "yahoo_date": "2026-11-01", "verdict": "stale_reference"}, {"region": "AU", "symbol": "SMR.AX", "tv": -5.2, "yahoo": -1.961, "delta": -3.239, "ref_delta_pct": -1.961, "tv_implied_ref": 2.5, "yahoo_ref": 2.55, "yahoo_date": "2026-11-01", "verdict": "stale_reference"}, {"region": "AU", "symbol": "WHC.AX", "tv": -5.052, "yahoo": -1.152, "delta": -3.9, "ref_delta_pct": -1.152, "tv_implied_ref": 7.72, "yahoo_ref": 7.81, "yahoo_date": "2026-11-01", "verdict": "stale_reference"}, {"region": "AU", "symbol": "SKS.AX", "tv": -5.051, "yahoo": -1.493, "delta": -3.558, "ref_delta_pct": -1.493, "tv_implied_ref": 5.94, "yahoo_ref": 6.03, "yahoo_date": "2026-11-01", "verdict": "stale_reference"}, {"region": "AU", "symbol": "HLI.AX", "tv": -5.01, "yahoo": -7.934, "delta": 2.924, "ref_delta_pct": -7.934, "tv_implied_ref": 4.99, "yahoo_ref": 5.42, "yahoo_date": "2026-11-01", "verdict": "stale_reference"}]
- stale_rows_dropped: US=['SHOP', 'AEHR', 'PLTR', 'SRAD', 'AVEX', 'UPST', 'SNDK', 'KLAC', 'AAPL', 'PENG', 'MXL', 'ALAB', 'VICR', 'MU', 'BWLP', 'AMAT', 'TRMD', 'INTC', 'NET', 'OVV', 'LRCX', 'TTMI', 'ADI', 'AAOI', 'CRDO', 'UCTT', 'AMD', 'MHK', 'AMKR', 'DDOG', 'VYX', 'WDC', 'CIFR', 'SM', 'LUNR', 'GLXY', 'SSMR', 'EROC', 'FCX', 'SITM', 'STX', 'NVTS', 'ALGM', 'TSEM', 'HUT', 'CIEN', 'P', 'QNT', 'FLUT', 'APPF', 'CRWV', 'IREN', 'MRVL', 'ABSI', 'URGN', 'SMCI', 'TXN', 'CLS', 'LGIH', 'NBIS', 'SCCO', 'DPC', 'VRT', 'LOW', 'BTDR', 'BUUU', 'ASTS', 'AEM', 'VRTX'] EU=['LHA'] AU=['AMP', 'VGN', 'SIQ', '4DX', 'TPW', 'NWL', 'VEA', 'YAL', 'NCK', 'MMS', 'LLC', 'NXT', 'PYC', 'ZIP', 'SMR', 'WHC', 'SKS', 'HLI']
- us_premarket_check (Yahoo 1-min pre/post feed vs the screener pre-market column): checked=10 within_1pp=1 within_3pp=1 unavailable=0
  NOTE: this check as written is NOT a valid verdict on the published pre-market column.
  Two defects: (1) it measures Yahoo's pre-market print against Yahoo's own
  `chartPreviousClose`, which on a 1-day range is the PRIOR PRIOR close (Oct 30),
  not the Nov 2 close the screener measures against; (2) the pipeline's hardcoded
  UTC-4 Eastern offset shifts its 04:00-09:30 ET pre-market filter back to
  ~03:00-07:00 ET, so it only ever sees the thin early-book prints. Both errors
  inflate the apparent gap. The outlier list below is a pipeline artefact.
- pre_market_recheck (independent, recomputed 2026-11-03 ~08:45 ET from Yahoo's
  own 1-minute pre-market prints against the CORRECT Nov 2 close as the base):
  HLMN 8.00 vs 8.39 = -4.65% (screener -4.65), UPWK 10.20 vs 9.72 = +4.94%
  (screener +4.64), ECO 94.72 vs 91.25 = +3.80% (screener +3.52), PGR 225.81 vs
  233.92 = -3.47% (screener -3.47), AESI 8.03 vs 8.23 = -2.43% (screener -2.43),
  ULCC 7.25 vs 7.43 = -2.42% (screener -2.42). 6 of 6 published US pre-market
  percentages reproduce within 0.3pp. Caveat: Yahoo's pre-market tape for these
  thin names is STALE — the last prints were 04:27-08:06 ET, so each figure is
  the last available pre-market print, not a live 08:45 quote.
- catalyst_lookups: 11 (US cap 5 = HLMN, UPWK, AESI, ULCC, ECO; EU cap 3 = TMV,
  TRUE_B, KABE_B; AU cap 2 = QAN, BJY; PGR included but outside the US budget)
  — 10 web_search calls, 1 per ticker. Every catalyst row is sourced from the
  issuer's own release, its IR page or a same-day wire report; none is inferred.
  us_premarket outliers (>3pp; thin pre-market books, not a screener error): [{"symbol": "AEHR", "tv": 15.562, "yahoo": 8.399, "delta": 7.163, "yahoo_asof": "08:59"}, {"symbol": "PLTR", "tv": -6.275, "yahoo": -9.57, "delta": 3.295, "yahoo_asof": "08:59"}, {"symbol": "SRAD", "tv": 5.672, "yahoo": 13.549, "delta": 7.877, "yahoo_asof": "08:12"}, {"symbol": "AVEX", "tv": 4.944, "yahoo": -0.982, "delta": 5.926, "yahoo_asof": "08:46"}, {"symbol": "UPST", "tv": 4.76, "yahoo": -5.43, "delta": 10.19, "yahoo_asof": "08:59"}, {"symbol": "SNDK", "tv": 4.689, "yahoo": -1.899, "delta": 6.588, "yahoo_asof": "08:59"}, {"symbol": "HLMN", "tv": -4.648, "yahoo": 2.564, "delta": 7.212, "yahoo_asof": "06:17"}, {"symbol": "UPWK", "tv": 4.64, "yahoo": 11.475, "delta": 6.835, "yahoo_asof": "08:48"}, {"symbol": "KLAC", "tv": 4.062, "yahoo": 0.861, "delta": 3.201, "yahoo_asof": "08:57"}]
- markets_with_lt5_rows: ['uk:egreater=2', 'france:egreater=3', 'netherlands:egreater=1', 'netherlands:less=3', 'belgium:egreater=0', 'belgium:less=0', 'portugal:egreater=0', 'portugal:less=0', 'ireland:egreater=0', 'ireland:less=0', 'italy:less=0', 'switzerland:egreater=2', 'switzerland:less=2', 'spain:egreater=3', 'spain:less=1', 'norway:egreater=4', 'denmark:egreater=3', 'denmark:less=2', 'finland:egreater=0', 'finland:less=1', 'poland:egreater=2', 'austria:egreater=1', 'austria:less=1', 'greece:egreater=0', 'greece:less=2']
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
- bod_no_extended_hours: 151 (deferred to the next scan; not in the headline table)
- earnings_source: screener `earnings_release_date` (last FULL report) + `earnings_release_next_date` (next scheduled)
- earnings_caveat: `earnings_release_date` does NOT capture preliminary, guidance or
  restructuring releases. On 2026-10-23 LKQ fell 22.47% on a preliminary Q3 miss while
  the field still read 2026-07-30. ALWAYS confirm the earnings-driven flag against the
  headline itself; the calendar field is a screen, not a verdict.
- data_date: US regular session close of the prior trading day; extended-hours columns
  carry the prior session's prints
- deprecations: mcp__tradingview-advanced__*, mcp__tradingview__*, mcp__financekit__*,
  mcp__stocktwits__* are ABSENT in Cloud sessions (tool_search 0 hits; connector catalog
  holds only media + credential tools). The public screener replaces them.

## Audit line

`earnings-reaction target=earnings-reactions:2026-11-03 candidates=570 amc_reactions=0 pre_gaps=6 eu_reactions=29 asx_reactions=7 catalyst_lookups=11 bod=151`
