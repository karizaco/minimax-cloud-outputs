# Earnings reaction scanner — 2026-10-24

- Cron: `0 8 * * 1-5` America/New_York (weekdays, 08:00 ET)
- Fire time (ET): 2026-10-24 17:53:51 Sat
- Source: TradingView public screener (`scanner.tradingview.com/<market>/scan`);
  Yahoo chart API as an independent cross-check on the reported movers.
- Method: 4 passes (US top-200 mcap, US prior-session movers, EU/UK movers,
  ASX movers). Volume floor 10,000 on every pass; `country` filter for
  primary listings; exchange drop-list applied.
- Status: `ok`

## TL;DR

- 2 AMC reactions, 52 pre-market gaps, 1 without extended-hours data; 30 EU/UK and 25 ASX movers.
- Biggest US extended-hours move: LKQ PRE_GAP (19.94%).
- Biggest EU/UK move: VOLCAR_B (-24.23%, sweden).
- Biggest ASX move: TPW (+33.42%).
- EU/AU earnings-driven tagging is keyword-based on headlines (best-effort).

## US — Headline table

| Ticker | Venue | Close | Chg % | Pre-mkt % | Post-mkt % | Last earnings | Tag |
|---|---|---|---|---|---|---|---|
| LKQ | NASDAQ | 17.42 | -22.47 | -19.94 | 0.46 | 2026-07-30 (86d ago) | PRE_GAP |
| CCI | NYSE | 85.97 | 9.06 | 17.20 | 0.95 | 2026-10-21 (3d ago) | PRE_GAP |
| RNG | NYSE | 83.39 | 5.00 | 14.58 | -0.55 | 2026-10-22 (2d ago) | PRE_GAP |
| RHI | NYSE | 45.87 | 21.74 | 12.74 | -0.01 | 2026-10-22 (2d ago) | PRE_GAP |
| AMT | NYSE | 188.97 | 4.08 | 11.25 | 0.16 | 2026-07-28 (88d ago) | PRE_GAP |
| SBAC | NASDAQ | 184.75 | 3.57 | 10.76 | -0.03 | 2026-08-03 (82d ago) | PRE_GAP |
| WGS | NASDAQ | 56.15 | -16.37 | — | 9.08 | 2026-08-03 (82d ago) | AMC_REACTION |
| GNTX | NASDAQ | 20.66 | -4.97 | -8.46 | 0.15 | 2026-10-23 (1d ago) | PRE_GAP |
| TNGX | NASDAQ | 23.34 | -16.43 | -8.20 | 2.06 | 2026-08-11 (74d ago) | PRE_GAP |
| CRDO | NASDAQ | 147.29 | -9.51 | -7.23 | 1.06 | 2026-09-01 (53d ago) | PRE_GAP |
| KNSL | NYSE | 364.49 | -6.69 | -7.07 | 0.00 | 2026-10-22 (2d ago) | PRE_GAP |
| BE | NYSE | 193.3 | -11.24 | -6.78 | -0.34 | 2026-10-22 (2d ago) | PRE_GAP |
| FLG | NYSE | 10.38 | -9.27 | -6.64 | 0.20 | 2026-10-23 (1d ago) | PRE_GAP |
| SIGI | NASDAQ | 96.61 | 5.31 | 5.73 | 0.19 | 2026-10-22 (2d ago) | PRE_GAP |
| TMUS | NASDAQ | 146.54 | -7.71 | -5.55 | 0.29 | 2026-07-23 (93d ago) | PRE_GAP |
| DECK | NYSE | 81.09 | -4.91 | -5.55 | -0.30 | 2026-10-22 (2d ago) | PRE_GAP |
| FIX | NYSE | 1160.86 | -9.26 | -5.42 | 0.22 | 2026-10-22 (2d ago) | PRE_GAP |
| SLM | NASDAQ | 19.415 | -10.78 | -5.24 | 1.42 | 2026-10-22 (2d ago) | PRE_GAP |
| CHRD | NASDAQ | 158.13 | 5.08 | -5.02 | 0.00 | 2026-08-05 (80d ago) | PRE_GAP |
| RITM | NYSE | 9.39 | 8.18 | 4.78 | -0.32 | 2026-10-23 (1d ago) | PRE_GAP |
| KN | NYSE | 32.17 | -3.62 | 4.52 | 0.00 | 2026-10-22 (2d ago) | PRE_GAP |
| BHVN | NYSE | 13.88 | -5.51 | 4.49 | -0.34 | 2026-08-10 (75d ago) | PRE_GAP |
| ORIC | NASDAQ | 13.17 | -3.37 | -4.48 | 2.05 | 2026-08-03 (82d ago) | PRE_GAP |
| T | NYSE | 20.93 | -7.96 | -4.44 | 0.18 | 2026-10-21 (3d ago) | PRE_GAP |
| RDN | NYSE | 35.75 | 3.03 | 4.03 | 0.00 | 2026-08-05 (80d ago) | PRE_GAP |
| FCNCA | NASDAQ | 2375.84 | 8.15 | 3.83 | 0.00 | 2026-10-23 (1d ago) | PRE_GAP |
| VZ | NYSE | 44.66 | -1.19 | -3.76 | -0.13 | 2026-07-24 (92d ago) | PRE_GAP |
| ALV | NYSE | 114.67 | -3.54 | -3.57 | 0.00 | 2026-10-23 (1d ago) | PRE_GAP |
| GE | NYSE | 285.64 | -2.69 | -3.24 | 0.13 | 2026-10-20 (4d ago) | PRE_GAP |
| SEZL | NASDAQ | 132.12 | -5.15 | -3.24 | 0.33 | 2026-08-06 (79d ago) | PRE_GAP |
| MRNA | NASDAQ | 200.1 | -1.25 | -3.18 | 0.62 | 2026-07-31 (85d ago) | PRE_GAP |
| AXP | NYSE | 313.22 | -3.68 | -3.12 | 0.00 | 2026-10-23 (1d ago) | PRE_GAP |
| RACE | NYSE | 393.28 | -1.10 | -1.18 | -3.12 | 2026-07-30 (86d ago) | AMC_REACTION |
| PCVX | NASDAQ | 60.43 | -3.85 | -3.04 | 0.00 | 2026-08-05 (80d ago) | PRE_GAP |
| NEM | NYSE | 108.87 | -4.59 | -3.02 | 0.29 | 2026-10-22 (2d ago) | PRE_GAP |
| ACN | NYSE | 249.37 | -3.62 | -2.93 | -0.21 | 2026-10-01 (23d ago) | PRE_GAP |
| SAM | NYSE | 202.28 | 3.35 | -2.92 | 0.00 | 2026-10-22 (2d ago) | PRE_GAP |
| CECO | AMEX | 49.08 | -4.72 | -2.81 | 0.65 | 2026-08-10 (75d ago) | PRE_GAP |
| ONON | NYSE | 32.51 | -4.38 | -2.79 | -0.15 | 2026-08-11 (74d ago) | PRE_GAP |
| MTG | NYSE | 28.8 | 3.82 | 2.74 | 0.00 | 2026-07-29 (87d ago) | PRE_GAP |
| HWM | NYSE | 185.91 | -3.82 | -2.67 | 0.80 | 2026-08-06 (79d ago) | PRE_GAP |
| INTR | NASDAQ | 7.19 | 6.68 | 2.52 | 0.70 | 2026-08-05 (80d ago) | PRE_GAP |
| CCL | NYSE | 26.11 | -3.58 | -2.51 | -0.02 | 2026-09-29 (25d ago) | PRE_GAP |
| AAL | NASDAQ | 12.11 | -3.89 | -2.46 | -0.08 | 2026-10-22 (2d ago) | PRE_GAP |
| NN | NASDAQ | 10.08 | 9.45 | 2.39 | 0.20 | 2026-08-11 (74d ago) | PRE_GAP |
| WDC | NASDAQ | 343.67 | -2.97 | -2.30 | -0.49 | 2026-10-22 (2d ago) | PRE_GAP |
| CNXC | NASDAQ | 33 | -3.65 | -2.28 | 0.00 | 2026-09-29 (25d ago) | PRE_GAP |
| BIRK | NYSE | 32.57 | -3.30 | -2.23 | -0.98 | 2026-08-13 (72d ago) | PRE_GAP |
| MLTX | NASDAQ | 11.85 | -3.97 | -2.19 | 1.18 | 2026-08-10 (75d ago) | PRE_GAP |
| SPCX | NASDAQ | 147.49 | 1.89 | 2.18 | 0.06 | 2026-10-20 (4d ago) | PRE_GAP |
| FLO | NYSE | 6.15 | -4.21 | -2.10 | 0.49 | 2026-02-12 (254d ago) | PRE_GAP |
| VC | NASDAQ | 76.37 | -6.52 | -2.06 | 0.00 | 2026-10-22 (2d ago) | PRE_GAP |
| STX | NASDAQ | 630.49 | -1.81 | -2.05 | -0.08 | 2026-07-28 (88d ago) | PRE_GAP |
| RCL | NYSE | 276.48 | -3.37 | -2.04 | 0.26 | 2026-07-28 (88d ago) | PRE_GAP |
| SOJD | NYSE | 17.42 | 0.11 | — | — | 2026-07-30 (86d ago) | BOD |

## US — QUIET one-liners

| Ticker | Venue | Chg % | Pre-mkt % | Post-mkt % |
|---|---|---|---|---|
| KNSA | NASDAQ | -5.03 | 0.26 | -2.65 |
| KALU | NASDAQ | -6.70 | 0.05 | 2.54 |
| CI | NYSE | -2.83 | -0.28 | -2.26 |
| MGM | NYSE | -4.88 | -2.00 | 0.29 |
| LULU | NASDAQ | -4.85 | -2.00 | 0.24 |
| MLYS | NASDAQ | -4.29 | 0.33 | 2.00 |
| UAL | NASDAQ | -3.99 | -1.95 | 0.17 |
| ESTC | NYSE | 4.30 | -0.05 | -1.94 |
| FLY | NASDAQ | 4.05 | -1.88 | -0.11 |
| CMCSA | NASDAQ | -0.66 | -1.88 | 0.48 |
| AVAV | NASDAQ | 4.72 | -1.87 | -0.32 |
| VSAT | NASDAQ | 4.19 | 0.34 | -1.87 |
| BUUU | NASDAQ | 12.53 | — | -1.86 |
| TEN | NYSE | 3.54 | 1.84 | 0.02 |
| RCUS | NYSE | -4.24 | -0.36 | -1.83 |

## EU/UK — Headline table

| Ticker | Market | Venue | Close | Chg % | Currency | Last earnings |
|---|---|---|---|---|---|---|
| VOLCAR_B | sweden | OMXSTO | 10.695 | -24.23 | SEK | 2026-10-23 |
| OVH | france | EURONEXT | 12.39 | -21.08 | EUR | 2026-04-09 |
| KNOW | sweden | OMXSTO | 120 | +20.00 | SEK | 2026-07-17 |
| KER | france | EURONEXT | 178.12 | -16.57 | EUR | 2026-07-28 |
| BHG | sweden | OMXSTO | 25 | +15.10 | SEK | 2026-10-23 |
| ANOD_B | sweden | OMXSTO | 64.2 | +13.43 | SEK | 2026-07-15 |
| ROKO_B | sweden | OMXSTO | 2145 | +12.66 | SEK | 2026-10-23 |
| LIFCO_B | sweden | OMXSTO | 280.4 | -12.05 | SEK | 2026-10-23 |
| HIAB | finland | OMXHEX | 46.4 | -11.70 | EUR | 2026-10-23 |
| FR | france | EURONEXT | 11.38 | -11.54 | EUR | 2026-07-22 |
| CBRAIN | denmark | OMXCOP | 93.4 | +11.46 | DKK | 2026-08-20 |
| NOTE | sweden | OMXSTO | 154.1 | -11.03 | SEK | 2026-07-15 |
| ALLIGO_B | sweden | OMXSTO | 111.8 | -10.42 | SEK | 2026-10-23 |
| SAF | france | EURONEXT | 271.8 | -10.00 | EUR | 2026-07-28 |
| MCAP | sweden | OMXSTO | 600.5 | +9.98 | SEK | 2026-07-21 |
| 50GP | uk | LSE | 77 | -9.14 | GBX | 2026-07-28 |
| NCOD | norway | OSL | 17.95 | +9.12 | NOK | 2025-02-13 |
| LOGI_B | sweden | OMXSTO | 14.08 | +8.98 | SEK | 2026-10-22 |
| AOF | germany | XETR | 87.3 | -8.97 | EUR | 2026-07-27 |
| SBB_D | sweden | OMXSTO | 6.15 | -8.75 | SEK | — |
| RATO_B | sweden | OMXSTO | 39.5 | +8.16 | SEK | 2026-10-23 |
| XVIVO | sweden | OMXSTO | 206 | -7.79 | SEK | 2026-10-22 |
| KCR | finland | OMXHEX | 26.44 | -7.75 | EUR | 2026-10-23 |
| BESI | netherlands | EURONEXT | 145.1 | -7.73 | EUR | 2026-10-21 |
| HOFI | sweden | OMXSTO | 178.7 | -7.70 | SEK | 2026-10-23 |
| RR. | uk | LSE | 1164.2 | -7.57 | GBX | 2026-07-30 |
| LIGHT | netherlands | EURONEXT | 15.19 | +7.43 | EUR | 2026-10-23 |
| S92 | germany | GETTEX | 47.24 | -7.37 | EUR | 2026-08-13 |
| BOUV | norway | OSL | 51.9 | +7.23 | NOK | 2026-08-19 |
| VICO | sweden | OMXSTO | 9.52 | +7.21 | SEK | 2026-08-21 |

## AU (ASX) — Headline table

| Ticker | Venue | Close | Chg % | Currency | Last earnings |
|---|---|---|---|---|---|
| TPW | ASX | 5.43 | +33.42 | AUD | 2026-08-18 |
| ZIP | ASX | 1.46 | -29.47 | AUD | 2026-08-19 |
| OBM | ASX | 1.11 | -16.54 | AUD | 2026-08-25 |
| SRL | ASX | 12.68 | -13.68 | AUD | 2026-09-07 |
| ALK | ASX | 1.475 | -10.88 | AUD | 2026-10-23 |
| ELV | ASX | 3.4 | -9.33 | AUD | 2026-08-27 |
| FFM | ASX | 1.225 | -9.26 | AUD | 2026-09-17 |
| CYL | ASX | 4.75 | -9.18 | AUD | 2026-08-31 |
| MLX | ASX | 1.475 | -8.95 | AUD | 2026-08-27 |
| WA1 | ASX | 7.63 | -8.18 | AUD | 2026-09-18 |
| PLS | ASX | 2.62 | -8.07 | AUD | 2026-08-23 |
| KCN | ASX | 3.94 | -7.94 | AUD | 2026-08-30 |
| CMM | ASX | 12.39 | -7.88 | AUD | 2026-08-26 |
| PDI | ASX | 3.54 | -7.81 | AUD | 2026-09-30 |
| GMD | ASX | 6.16 | -7.78 | AUD | 2026-08-20 |
| GNG | ASX | 6.25 | -7.41 | AUD | 2026-08-23 |
| IGO | ASX | 4.77 | -7.38 | AUD | 2026-08-25 |
| PNR | ASX | 2.58 | -7.19 | AUD | 2026-09-28 |
| RSG | ASX | 1.035 | -7.17 | AUD | 2026-08-19 |
| WGX | ASX | 4.79 | -7.17 | AUD | 2026-08-27 |
| LYL | ASX | 19.3 | -7.17 | AUD | 2026-08-19 |
| EOS | ASX | 8.46 | -7.03 | AUD | 2026-08-24 |
| DVP | ASX | 3.71 | -7.02 | AUD | 2026-03-08 |
| VAU | ASX | 5.18 | -7.00 | AUD | 2026-08-20 |
| GGP | ASX | 8.68 | -6.97 | AUD | 2026-08-26 |

## Catalysts

<!-- AGENT: fill catalyst text for the tickers in <date>-catalyst-targets.json, then
     delete this comment. Cap: 5 US + 3 EU + 2 AU. Never fabricate a headline. -->

| Ticker | Region | Catalyst | Earnings-driven |
|---|---|---|---|

## Source health

- scanner_calls: 39 | scanner_errors: 0
- yahoo_calls: 39 | yahoo_429: 0 | yahoo_errors: 12
- cross_check (screener vs Yahoo): agree=27 mismatch=0 unverified=4
- markets_with_lt5_rows: ['netherlands:egreater=3', 'netherlands:less=1', 'belgium:less=2', 'portugal:egreater=1', 'portugal:less=0', 'ireland:egreater=0', 'ireland:less=0', 'italy:egreater=2', 'switzerland:egreater=3', 'spain:egreater=1', 'spain:less=1', 'denmark:egreater=3', 'denmark:less=1', 'finland:egreater=2', 'poland:egreater=3', 'austria:egreater=1', 'austria:less=2', 'greece:egreater=1', 'greece:less=4']
- filters: volume>10000 (removes stale-reference rows), country=home for EU/UK/AU,
  exchange drop-list for US, US venue allow-list, US preferred (slash ticker) excluded
- us_preferred_dropped: 59
- earnings_source: screener `earnings_release_date` (last report) + `earnings_release_next_date` (next scheduled)
- data_date: US regular session close of the prior trading day; extended-hours columns
  carry the prior session's prints
- deprecations: mcp__tradingview-advanced__*, mcp__tradingview__*, mcp__financekit__*,
  mcp__stocktwits__* are ABSENT in Cloud sessions (tool_search 0 hits; connector catalog
  holds only media + credential tools). The public screener replaces them.

## Audit line

`earnings-reaction target=earnings-reactions:2026-10-24 candidates=540 amc_reactions=2 pre_gaps=52 eu_reactions=30 asx_reactions=25 catalyst_lookups=0`
