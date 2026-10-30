# Earnings reaction scanner — 2026-10-29

- Cron: `0 8 * * 1-5` America/New_York (weekdays, 08:00 ET)
- Fire time (ET): 2026-10-29 08:07:36 Thu
- Run type: `scheduled_scan`
- Source: TradingView public screener (`scanner.tradingview.com/<market>/scan`);
  Yahoo chart API as an independent cross-check on the reported movers.
- Method: 4 passes (US top-200 mcap, US prior-session movers, EU/UK movers,
  ASX movers). Volume floor 10,000 on every pass; `country` filter for
  primary listings; exchange drop-list applied.
- Status: `ok`

## TL;DR

- 0 AMC reactions, 124 pre-market gaps, 119 without extended-hours data; 29 EU/UK and 25 ASX movers.
- Biggest US extended-hours move: FTNT PRE_GAP (26.04%).
- Biggest EU/UK move: BINV (-61.55%, sweden).
- Biggest ASX move: MSB (+23.40%).
- EU/AU earnings-driven tagging is keyword-based on headlines (best-effort).

## US — Headline table

| Ticker | Venue | Close | Chg % | Pre-mkt % | Post-mkt % | Last earnings | Tag |
|---|---|---|---|---|---|---|---|
| FTNT | NASDAQ | 174.08 | -5.90 | -26.04 | — | 2026-10-28 (1d ago) | PRE_GAP |
| SFM | NASDAQ | 62 | -3.74 | -23.06 | — | 2026-10-28 (1d ago) | PRE_GAP |
| PRCH | NASDAQ | 16.3 | -7.70 | 20.61 | — | 2026-10-29 (0d ago) | PRE_GAP |
| NOW | NYSE | 150.13 | -3.00 | -19.81 | — | 2026-10-28 (1d ago) | PRE_GAP |
| TDOC | NYSE | 6.88 | 6.67 | 14.10 | — | 2026-10-28 (1d ago) | PRE_GAP |
| MRVL | NASDAQ | 251.65 | 3.32 | -11.38 | — | 2026-08-27 (63d ago) | PRE_GAP |
| GOOGL | NASDAQ | 324.89 | 1.34 | -11.30 | — | 2026-10-28 (1d ago) | PRE_GAP |
| GOOG | NASDAQ | 321.89 | 1.60 | -11.06 | — | 2026-10-28 (1d ago) | PRE_GAP |
| COHU | NASDAQ | 53.14 | 4.24 | 9.69 | — | 2026-10-28 (1d ago) | PRE_GAP |
| CAT | NYSE | 713.38 | 0.01 | -9.34 | — | 2026-10-29 (0d ago) | PRE_GAP |
| BHC | NYSE | 6.92 | 9.67 | 8.09 | — | 2026-10-28 (1d ago) | PRE_GAP |
| NVCR | NASDAQ | 14.17 | -3.08 | 7.54 | — | 2026-10-29 (0d ago) | PRE_GAP |
| INIO | NASDAQ | 18.35 | 8.07 | -7.36 | — | 2026-10-27 (2d ago) | PRE_GAP |
| FTRE | NASDAQ | 25.88 | 5.94 | -7.34 | — | 2026-07-29 (92d ago) | PRE_GAP |
| GOOGN | NASDAQ | 46.62 | 1.00 | -7.23 | — | 2026-10-28 (1d ago) | PRE_GAP |
| GOOGM | NASDAQ | 46.72 | 1.02 | -7.21 | — | 2026-10-28 (1d ago) | PRE_GAP |
| AXTI | NASDAQ | 64.38 | 10.56 | -7.19 | — | 2026-07-30 (91d ago) | PRE_GAP |
| CRWD | NASDAQ | 266.66 | -0.51 | -6.94 | — | 2026-08-26 (64d ago) | PRE_GAP |
| PANW | NASDAQ | 394.49 | -1.79 | -6.84 | — | 2026-09-01 (58d ago) | PRE_GAP |
| NBIS | NASDAQ | 182.34 | 6.96 | -6.70 | — | 2026-08-12 (78d ago) | PRE_GAP |
| CRWV | NASDAQ | 63.93 | 7.32 | -6.54 | — | 2026-08-11 (79d ago) | PRE_GAP |
| TYL | NYSE | 360.9 | -4.68 | -6.27 | — | 2026-10-28 (1d ago) | PRE_GAP |
| CRM | NYSE | 242.11 | 0.51 | -6.24 | — | 2026-08-26 (64d ago) | PRE_GAP |
| FTAI | NASDAQ | 167.14 | 5.34 | 6.05 | — | 2026-07-29 (92d ago) | PRE_GAP |
| LITE | NASDAQ | 913.95 | 5.52 | 5.80 | — | 2026-08-11 (79d ago) | PRE_GAP |
| TT | NYSE | 448.47 | -2.73 | -5.68 | — | 2026-10-29 (0d ago) | PRE_GAP |
| PWR | NYSE | 606.89 | 4.85 | 5.62 | — | 2026-10-29 (0d ago) | PRE_GAP |
| ENTG | NASDAQ | 159.32 | 6.14 | 5.45 | — | 2026-10-29 (0d ago) | PRE_GAP |
| MYRG | NASDAQ | 279.92 | 4.98 | 5.39 | — | 2026-10-28 (1d ago) | PRE_GAP |
| STRL | NASDAQ | 388.87 | 5.81 | -5.35 | — | 2026-10-28 (1d ago) | PRE_GAP |
| IREN | NASDAQ | 28.84 | 5.10 | -4.93 | — | 2026-08-27 (63d ago) | PRE_GAP |
| CIFR | NASDAQ | 8.87 | 4.60 | -4.74 | — | 2026-08-04 (86d ago) | PRE_GAP |
| NET | NYSE | 318.72 | -2.77 | -4.62 | — | 2026-08-06 (84d ago) | PRE_GAP |
| GLXY | NASDAQ | 19.09 | 11.12 | -4.61 | — | 2026-10-27 (2d ago) | PRE_GAP |
| LLY | NYSE | 1288.3 | 0.50 | 4.46 | — | 2026-10-29 (0d ago) | PRE_GAP |
| SDGR | NASDAQ | 30.87 | 15.53 | -4.44 | — | 2026-08-05 (85d ago) | PRE_GAP |
| MOD | NYSE | 143.54 | 5.15 | -4.42 | — | 2026-07-29 (92d ago) | PRE_GAP |
| RIOT | NASDAQ | 14.45 | 6.56 | -4.36 | — | 2026-08-10 (80d ago) | PRE_GAP |
| WOLF | NYSE | 26.64 | 5.67 | -4.28 | — | 2026-08-19 (71d ago) | PRE_GAP |
| HONA | NASDAQ | 177.03 | 5.44 | -4.25 | — | 2026-10-28 (1d ago) | PRE_GAP |
| WULF | NASDAQ | 13.42 | 6.00 | -4.25 | — | 2026-08-05 (85d ago) | PRE_GAP |
| APLD | NASDAQ | 20.39 | 4.51 | -4.22 | — | 2026-10-07 (22d ago) | PRE_GAP |
| BE | NYSE | 228.08 | 4.38 | -4.20 | — | 2026-10-22 (7d ago) | PRE_GAP |
| OWL | NYSE | 9.67 | 3.87 | 4.03 | — | 2026-07-30 (91d ago) | PRE_GAP |
| INTU | NASDAQ | 328.19 | -0.08 | -4.02 | — | 2026-08-25 (65d ago) | PRE_GAP |
| CRDO | NASDAQ | 173.69 | 3.74 | -3.93 | — | 2026-09-01 (58d ago) | PRE_GAP |
| RCL | NYSE | 298.3 | 0.80 | 3.90 | — | 2026-10-27 (2d ago) | PRE_GAP |
| SNOW | NYSE | 339.91 | 0.74 | -3.84 | — | 2026-09-02 (57d ago) | PRE_GAP |
| MARA | NASDAQ | 7.35 | 3.67 | -3.83 | — | 2026-08-06 (84d ago) | PRE_GAP |
| ICHR | NASDAQ | 43.08 | 5.72 | -3.78 | — | 2026-08-03 (87d ago) | PRE_GAP |
| CORZ | NASDAQ | 15 | 5.15 | -3.67 | — | 2026-07-28 (93d ago) | PRE_GAP |
| SEI | NYSE | 68.97 | 5.57 | -3.58 | — | 2026-08-05 (85d ago) | PRE_GAP |
| AMGN | NASDAQ | 451.83 | 0.87 | 3.58 | — | 2026-08-04 (86d ago) | PRE_GAP |
| ADBE | NASDAQ | 249.76 | 0.56 | -3.50 | — | 2026-09-10 (49d ago) | PRE_GAP |
| ACN | NYSE | 243.4 | 3.50 | -3.46 | — | 2026-10-01 (28d ago) | PRE_GAP |
| CSTL | NASDAQ | 36.68 | 6.29 | 3.46 | — | 2026-07-30 (91d ago) | PRE_GAP |
| INOD | NASDAQ | 47.65 | 6.50 | -3.42 | — | 2026-08-06 (84d ago) | PRE_GAP |
| AESI | NYSE | 9.44 | 3.96 | 3.39 | — | 2026-08-03 (87d ago) | PRE_GAP |
| KLAC | NASDAQ | 158.77 | 3.33 | 3.34 | — | 2026-10-28 (1d ago) | PRE_GAP |
| VRTX | NASDAQ | 529.69 | 1.66 | 3.34 | — | 2026-08-03 (87d ago) | PRE_GAP |
| BTU | NYSE | 22.51 | -3.47 | 3.29 | — | 2026-07-29 (92d ago) | PRE_GAP |
| CLSK | NASDAQ | 8.58 | 4.76 | -3.27 | — | 2026-08-06 (84d ago) | PRE_GAP |
| CLS | NYSE | 299.8 | 8.41 | -3.27 | — | 2026-10-26 (3d ago) | PRE_GAP |
| FLEX | NASDAQ | 93.03 | 11.61 | -3.25 | — | 2026-10-28 (1d ago) | PRE_GAP |
| ALAB | NASDAQ | 297.2 | 3.67 | -3.23 | — | 2026-08-04 (86d ago) | PRE_GAP |
| GEV | NYSE | 878.03 | -1.90 | -3.18 | — | 2026-10-28 (1d ago) | PRE_GAP |
| FPS | NYSE | 29.27 | 8.45 | -3.14 | — | 2026-09-15 (44d ago) | PRE_GAP |
| INTC | NASDAQ | 95.53 | 1.91 | -3.12 | — | 2026-07-23 (98d ago) | PRE_GAP |
| DDOG | NASDAQ | 278.41 | -0.86 | -3.09 | — | 2026-08-06 (84d ago) | PRE_GAP |
| TTMI | NASDAQ | 90.79 | 4.62 | -3.07 | — | 2026-10-22 (7d ago) | PRE_GAP |
| CMPR | NASDAQ | 74.79 | -7.40 | -3.06 | — | 2026-10-28 (1d ago) | PRE_GAP |
| VRT | NYSE | 242.94 | 16.48 | -3.04 | — | 2026-10-28 (1d ago) | PRE_GAP |
| PGY | NASDAQ | 20.47 | 3.54 | -3.03 | — | 2026-10-29 (0d ago) | PRE_GAP |
| VIAV | NASDAQ | 34.46 | 3.48 | -2.99 | — | 2026-08-05 (85d ago) | PRE_GAP |
| TMUS | NASDAQ | 148.08 | 0.85 | 2.98 | — | 2026-10-28 (1d ago) | PRE_GAP |
| GILD | NASDAQ | 159.2 | 0.08 | 2.94 | — | 2026-08-04 (86d ago) | PRE_GAP |
| STX | NASDAQ | 697.97 | 4.51 | -2.93 | — | 2026-10-27 (2d ago) | PRE_GAP |
| BTDR | NASDAQ | 7.92 | 5.04 | -2.90 | — | 2026-08-10 (80d ago) | PRE_GAP |
| DB | NYSE | 33.51 | 4.33 | 2.89 | — | 2026-10-28 (1d ago) | PRE_GAP |
| WDC | NASDAQ | 396.42 | 4.08 | -2.89 | — | 2026-10-22 (7d ago) | PRE_GAP |
| KYMR | NASDAQ | 122.51 | 4.20 | -2.87 | — | 2026-10-29 (0d ago) | PRE_GAP |
| UCTT | NASDAQ | 55.88 | 8.55 | -2.85 | — | 2026-10-27 (2d ago) | PRE_GAP |
| GLW | NYSE | 131.2 | 3.88 | -2.82 | — | 2026-10-27 (2d ago) | PRE_GAP |
| POWL | NASDAQ | 168.01 | 4.12 | -2.80 | — | 2026-08-03 (87d ago) | PRE_GAP |
| TER | NASDAQ | 313.24 | -3.23 | -2.80 | — | 2026-10-27 (2d ago) | PRE_GAP |
| TEX | NYSE | 53.37 | 7.43 | -2.75 | — | 2026-10-28 (1d ago) | PRE_GAP |
| TEM | NASDAQ | 76.61 | 6.18 | -2.74 | — | 2026-07-30 (91d ago) | PRE_GAP |
| BEAM | NASDAQ | 28.78 | 15.58 | -2.71 | — | 2026-08-04 (86d ago) | PRE_GAP |
| FN | NYSE | 367.3 | 7.02 | -2.67 | — | 2026-08-17 (73d ago) | PRE_GAP |
| FRVO | NASDAQ | 8.33 | -4.03 | 2.64 | — | 2026-08-12 (78d ago) | PRE_GAP |
| SAIA | NASDAQ | 324.62 | -4.76 | 2.58 | — | 2026-10-29 (0d ago) | PRE_GAP |
| MU | NASDAQ | 983.23 | 5.86 | -2.58 | — | 2026-09-30 (29d ago) | PRE_GAP |
| ADP | NASDAQ | 285.37 | -2.64 | 2.57 | — | 2026-10-28 (1d ago) | PRE_GAP |
| IBM | NYSE | 253.22 | 1.19 | -2.54 | — | 2026-10-21 (8d ago) | PRE_GAP |
| AAOI | NASDAQ | 82.22 | 6.85 | -2.53 | — | 2026-08-06 (84d ago) | PRE_GAP |
| ON | NASDAQ | 75.63 | -3.86 | -2.53 | — | 2026-08-03 (87d ago) | PRE_GAP |
| SNDK | NASDAQ | 1404.77 | 7.66 | -2.49 | — | 2026-08-05 (85d ago) | PRE_GAP |
| AVGO | NASDAQ | 351.81 | 2.77 | -2.49 | — | 2026-09-02 (57d ago) | PRE_GAP |
| SHAZ | NASDAQ | 28.47 | 10.56 | -2.44 | — | 2026-08-06 (84d ago) | PRE_GAP |
| BFLY | NYSE | 7.81 | 5.83 | 2.43 | — | 2026-10-29 (0d ago) | PRE_GAP |
| AMKR | NASDAQ | 42.21 | 5.68 | -2.42 | — | 2026-10-26 (3d ago) | PRE_GAP |
| GFL | NYSE | 43.59 | -3.13 | 2.41 | — | 2026-10-28 (1d ago) | PRE_GAP |
| MRK | NYSE | 140.93 | -0.63 | 2.40 | — | 2026-10-29 (0d ago) | PRE_GAP |
| AER | NYSE | 155.48 | 3.62 | 2.36 | — | 2026-10-28 (1d ago) | PRE_GAP |
| DELL | NYSE | 493.79 | -1.63 | -2.31 | — | 2026-09-01 (58d ago) | PRE_GAP |
| NTLA | NASDAQ | 13.32 | 8.47 | -2.26 | — | 2026-08-06 (84d ago) | PRE_GAP |
| BKNG | NASDAQ | 147.94 | -1.47 | 2.25 | — | 2026-08-04 (86d ago) | PRE_GAP |
| AZN | NYSE | 169.51 | -0.34 | 2.25 | — | 2026-07-27 (94d ago) | PRE_GAP |
| MO | NYSE | 72.99 | -0.68 | 2.25 | — | 2026-10-29 (0d ago) | PRE_GAP |
| APPN | NASDAQ | 51.96 | 4.04 | -2.23 | — | 2026-08-06 (84d ago) | PRE_GAP |
| TTE | NYSE | 92.88 | 0.57 | 2.22 | — | 2026-10-29 (0d ago) | PRE_GAP |
| SBUX | NASDAQ | 103.2 | 0.16 | 2.21 | — | 2026-07-29 (92d ago) | PRE_GAP |
| HPE | NYSE | 60.33 | -0.84 | -2.20 | — | 2026-09-02 (57d ago) | PRE_GAP |
| BMY | NYSE | 60.57 | -1.59 | 2.18 | — | 2026-10-29 (0d ago) | PRE_GAP |
| ONTO | NYSE | 223.68 | 4.44 | -2.18 | — | 2026-08-06 (84d ago) | PRE_GAP |
| NN | NASDAQ | 12.53 | 5.21 | -2.14 | — | 2026-08-11 (79d ago) | PRE_GAP |
| AMD | NASDAQ | 578.44 | 3.24 | -2.13 | — | 2026-08-04 (86d ago) | PRE_GAP |
| UBS | NYSE | 46.69 | -0.21 | 2.12 | — | 2026-10-28 (1d ago) | PRE_GAP |
| NEO | NASDAQ | 17.99 | 4.17 | -2.11 | — | 2026-10-28 (1d ago) | PRE_GAP |
| SNPS | NASDAQ | 481.89 | 1.57 | -2.11 | — | 2026-08-26 (64d ago) | PRE_GAP |
| CBRS | NASDAQ | 112.56 | -5.66 | -2.11 | — | 2026-08-12 (78d ago) | PRE_GAP |
| CRML | NASDAQ | 7.79 | -4.18 | -2.05 | — | 2026-09-25 (34d ago) | PRE_GAP |
| MS | NYSE | 190.13 | 1.72 | 2.04 | — | 2026-10-14 (15d ago) | PRE_GAP |
| UEC | AMEX | 8.34 | 3.73 | -2.03 | — | 2026-09-29 (30d ago) | PRE_GAP |

## US — QUIET one-liners

| Ticker | Venue | Chg % | Pre-mkt % | Post-mkt % |
|---|---|---|---|---|
| QNT | NASDAQ | -4.68 | -1.98 | — |
| AEM | NYSE | 1.33 | -1.97 | — |
| PEP | NASDAQ | -0.65 | 1.96 | — |
| ALMR | NASDAQ | 7.42 | -1.95 | — |
| ULCC | NASDAQ | 11.57 | -1.94 | — |
| JNJ | NYSE | 0.86 | 1.92 | — |
| MAR | NASDAQ | 1.07 | 1.91 | — |
| ABCL | NASDAQ | 6.31 | -1.91 | — |
| WMT | NASDAQ | -0.46 | 1.89 | — |
| AMZN | NASDAQ | 0.59 | -1.86 | — |
| NVT | NYSE | 4.16 | -1.86 | — |
| GRAL | NASDAQ | 4.83 | -1.82 | — |
| REGN | NASDAQ | -0.35 | 1.81 | — |
| HP | NYSE | 5.31 | -1.79 | — |
| WFC | NYSE | 1.22 | 1.78 | — |

## EU/UK — Headline table

| Ticker | Market | Venue | Close | Chg % | Currency | Last earnings |
|---|---|---|---|---|---|---|
| BINV | sweden | OMXSTO | 7.96 | -61.55 | SEK | 2026-08-27 |
| PLX | france | EURONEXT | 11.63 | -18.04 | EUR | 2026-04-16 |
| ENGCON_B | sweden | OMXSTO | 61.2 | -17.74 | SEK | 2026-07-17 |
| CPS | poland | GPW | 15.285 | -14.94 | PLN | 2026-08-19 |
| HLN | uk | LSE | 319.6 | -14.55 | GBX | 2026-07-30 |
| APR | norway | OSL | 31.4 | -12.78 | NOK | 2026-08-14 |
| SMOP | norway | OSL | 57.4 | +12.55 | NOK | 2026-07-13 |
| KOG | norway | OSL | 344.2 | +10.29 | NOK | 2026-07-13 |
| TE | france | EURONEXT | 35.66 | +9.39 | EUR | 2026-07-30 |
| OHB | germany | XETR | 238 | -8.46 | EUR | 2026-08-06 |
| NETC | denmark | OMXCOP | 362 | -8.40 | DKK | 2026-08-13 |
| FLOW | netherlands | EURONEXT | 22.62 | -8.35 | EUR | — |
| SZG | germany | XETR | 47.36 | +8.23 | EUR | 2026-08-11 |
| STJ | uk | LSE | 1027.5 | -7.72 | GBX | 2026-07-29 |
| SJF | denmark | OMXCOP | 530 | +7.29 | DKK | 2026-08-13 |
| RNO | france | EURONEXT | 28.14 | +6.79 | EUR | 2026-07-28 |
| CPR | italy | MIL | 6.136 | -6.49 | EUR | 2026-07-29 |
| PDX | sweden | OMXSTO | 143.3 | +6.38 | SEK | 2026-08-06 |
| PLT | norway | OSL | 14.8 | -6.33 | NOK | 2026-08-06 |
| HUH1V | finland | OMXHEX | 25.5 | -6.04 | EUR | 2026-07-23 |
| ELAN_B | sweden | OMXSTO | 56.5 | +6.00 | SEK | 2026-10-23 |
| AVOL | switzerland | SIX | 47.8 | +5.94 | CHF | 2026-07-30 |
| SDZ | switzerland | SIX | 84.6 | +5.91 | CHF | 2026-08-05 |
| AOJ_B | denmark | OMXCOP | 113 | +5.81 | DKK | 2026-10-28 |
| GUBRA | denmark | OMXCOP | 308.6 | -5.68 | DKK | 2026-08-20 |
| NOLA_B | sweden | OMXSTO | 53.8 | -5.45 | SEK | 2026-07-17 |
| BEAMMW_B | sweden | OMXSTO | 18.72 | -5.26 | SEK | 2026-08-12 |
| KBX | germany | XETR | 91.45 | -5.04 | EUR | 2026-07-29 |
| PRY | italy | MIL | 113.15 | +5.01 | EUR | 2026-07-29 |

## AU (ASX) — Headline table

| Ticker | Venue | Close | Chg % | Currency | Last earnings |
|---|---|---|---|---|---|
| MSB | ASX | 2.32 | +23.40 | AUD | 2026-08-26 |
| ELS | ASX | 2.3 | -18.44 | AUD | 2026-08-25 |
| CIA | ASX | 1.87 | -17.26 | AUD | 2026-10-28 |
| IDX | ASX | 1.775 | -14.66 | AUD | 2026-08-24 |
| MAD | ASX | 5.5 | -10.71 | AUD | 2026-08-23 |
| ELV | ASX | 3.38 | -9.38 | AUD | 2026-08-27 |
| PLS | ASX | 2.75 | -8.03 | AUD | 2026-08-23 |
| CBO | ASX | 2.74 | +7.87 | AUD | 2026-08-27 |
| CU6 | ASX | 1.67 | +6.71 | AUD | 2026-08-26 |
| ZIP | ASX | 1.86 | +6.59 | AUD | 2026-08-19 |
| NEU | ASX | 20.14 | +6.28 | AUD | 2026-08-24 |
| DVP | ASX | 3.95 | -6.18 | AUD | 2026-03-08 |
| DUR | ASX | 2.07 | -5.48 | AUD | 2026-08-25 |
| WA1 | ASX | 9.19 | +4.91 | AUD | 2026-09-18 |
| GNP | ASX | 8.41 | +4.73 | AUD | 2026-08-24 |
| TUA | ASX | 1.255 | -4.56 | AUD | 2026-03-24 |
| 4DX | ASX | 3.28 | -4.37 | AUD | 2026-08-27 |
| LYC | ASX | 13.03 | +4.16 | AUD | 2026-08-25 |
| FFM | ASX | 1.395 | -4.12 | AUD | 2026-09-17 |
| BOQCD | ASX | 7.05 | -4.08 | AUD | 2026-10-13 |
| WES | ASX | 74.02 | -4.04 | AUD | 2026-08-26 |
| ILU | ASX | 5.9 | +3.69 | AUD | 2026-08-18 |
| SKS | ASX | 6.15 | -3.45 | AUD | 2026-08-17 |
| SHA | ASX | 6.89 | -3.37 | AUD | 2026-08-18 |
| MP1 | ASX | 17.87 | -3.30 | AUD | 2026-08-19 |

## Catalysts

| Ticker | Region | Catalyst | Earnings-driven |
|---|---|---|---|
| FTNT | US | Fortinet Q3 2026 beat (non-GAAP EPS $0.91 vs $0.86 consensus; revenue $2.08B, +20% YoY, vs $2.06B expected) with FY26 revenue guidance raised to $8.125-8.215B, but FY26 service-revenue guidance was cut to $5.15-5.17B from $5.18-5.22B, revenue growth slowed to 20% from 26%, price increases drove about 10pp of the 29% billings growth and non-GAAP gross margin slipped to 79.6% from 81.6%; shares fell about 25% after hours to near $130. | Y |
| SFM | US | Sprouts Farmers Market Q3 2026 miss: EPS $1.21 vs $1.22-1.23 consensus and revenue $2.30B vs $2.33B expected; comparable sales fell 0.9% with transactions down 3.3% (a cyclospora disruption cut comps about 60bp); FY26 guidance lowered to about 4.3% sales growth, about -1.7% comps and roughly $4.80 EPS; RBC downgraded to Sector Perform; shares -21.6% after hours. | Y |
| NOW | US | ServiceNow Q3 2026 revenue $4.106B (+20.5% YoY) beat but EPS $1.00 missed $1.02, the first adjusted EPS miss in six quarters, and GAAP operating margin fell to 9.5% from 17% on acquisition costs; FY26 subscription revenue and free-cash-flow margin were raised (FCF margin to 36%) and the AI ACV target lifted to $1.7B, but Q4 cRPO growth was guided to 18.5% against 21% in Q3; shares initially -14%. | Y |
| PRCH | US | Porch Group Q3 2026 beat-and-raise: EPS $0.10 vs about $0.01 consensus, revenue $143.9M vs $133.4M, Insurance Services revenue +39%, reciprocal policies written +42% and adjusted EBITDA excluding the Reciprocal $44.5M (+116% YoY); FY26 guidance raised to $518-523M revenue and $135-140M adjusted EBITDA; shares +21% pre-market to about $19.80. | Y |
| TDOC | US | Teladoc Health Q3 2026 revenue $605.1M (-3% YoY) near the top of guidance, adjusted EBITDA $79.4M (+14%) above the high end and net loss narrowed to $0.15 per share from $0.28; BetterHelp revenue fell 13% but BetterHelp insurance revenue of $32.1M beat; FY26 revenue guidance raised to $2.395-2.441B and adjusted EBITDA to $277-303M. | Y |
| BINV | EU | BioInvent International AB published its interim report for January-September 2026 today: net sales SEK 37.0M, loss after tax SEK 361.0M, liquid funds down to SEK 224.6M from SEK 690.5M a year earlier, alongside a rights issue of about SEK 430M resolved; shares -57% to SEK 8.93 on 1.2M shares. | Y |
| PLX | EU | PLUXEE N.V. FY2026 results published today met or beat all financial objectives: total revenues EUR 1,302M (+0.7% organic), recurring EBITDA EUR 488M (+3.8% organic) at a 37.5% margin (+101bp) and adjusted net profit EUR 223M, but FY27 is framed as a Brazil PAT1 reform transition year with the impact continuing into H1 FY27; shares -18%. | Y |
| ENGCON_B | EU | engcon AB Q3 2026 interim report (29 October, 08:00 CET): order intake fell 9% to SEK 424M (organic -10%) with Europe still weak, although net sales rose 5% to SEK 435M, EBIT rose 23% to SEK 86M (margin 19.9%) and profit rose 32% to SEK 69M (EPS SEK 0.45). | Y |
| MSB | AU | Mesoblast Q1 FY27 quarterly activities report: Ryoncil net revenue of US$28M, +44% YoY, with a record September for new patient starts; net operating cash spend improved 86% to US$2.1M with about US$99M cash; all 350 patients treated in the pivotal Phase 3 rexlemestrocel-L chronic-back-pain trial and a positive FDA meeting on the LVAD filing path; shares +23.4%. | Y |
| ELS | AU | Elsight Ltd Q3 FY26 update (28 October): unaudited revenue of about US$2.4M against Bell Potter's US$6M expectation, a substantial miss, with a non-GAAP loss of about US$700K, though nine-month revenue rose 91% to US$25.8M and the pipeline reached US$196M; cash US$59.4M with no debt; Bell Potter cut its target to A$5.30 from A$8.20. | Y |

## Source health

- scanner_calls: 39 | scanner_errors: 0
- pipeline_version: 2026-10-26.2
- yahoo_calls: 189 | yahoo_429: 0 | yahoo_errors: 0
- cross_check (screener vs Yahoo, reference-close validation): agree=177 mismatch=1 unverified=1 stale_reference=1
  method: the screener's implied reference close (close / (1 + change/100)) is compared
  with Yahoo's own reference close. A match proves the move was measured against the
  TRUE prior close; a mismatch means the row sits on a STALE reference (phantom move).
  Coverage: every row of the US headline, EU/UK and ASX tables is checked. The US QUIET
  one-liner table is NOT cross-checked.
  Yahoo bar mode: {"closed": 148, "live": 29} (closed = last completed session bar;
  live = in-progress EU/UK session bar, which is what a weekday 08:00 ET EU move needs)
  live drift between the screener snapshot and the later Yahoo print: median=0.00pp max=0.94pp (expected on a live market)
- cross_check mismatches: [{"region": "germany", "symbol": "AIXA.DE", "tv": 8.541, "yahoo": 6.451, "delta": 2.09, "ref_delta_pct": -1.779, "tv_implied_ref": 30.91, "yahoo_ref": 31.47, "yahoo_date": "2026-10-29", "verdict": "stale_reference"}]
- stale_rows_dropped: US=none EU=['AIXA'] AU=none
- us_premarket_check (Yahoo 1-min pre/post feed vs the screener pre-market column): checked=10 within_1pp=7 within_3pp=9 unavailable=0
  us_premarket outliers (>3pp; thin pre-market books, not a screener error): [{"symbol": "COHU", "tv": 9.691, "yahoo": 6.511, "delta": 3.18, "yahoo_asof": "06:16"}]
- markets_with_lt5_rows: ['germany:less=4', 'france:less=2', 'netherlands:egreater=0', 'netherlands:less=2', 'belgium:egreater=1', 'belgium:less=0', 'portugal:egreater=0', 'portugal:less=0', 'ireland:egreater=0', 'ireland:less=0', 'italy:egreater=3', 'italy:less=1', 'switzerland:egreater=3', 'switzerland:less=0', 'spain:egreater=4', 'spain:less=3', 'denmark:egreater=4', 'denmark:less=2', 'finland:egreater=0', 'finland:less=3', 'poland:egreater=1', 'poland:less=1', 'austria:egreater=0', 'austria:less=0', 'greece:egreater=0', 'greece:less=3']
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
- us_preferred_dropped: 60
- bod_no_extended_hours: 119 (deferred to the next scan; not in the headline table)
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

`earnings-reaction target=earnings-reactions:2026-10-29 candidates=484 amc_reactions=0 pre_gaps=124 eu_reactions=29 asx_reactions=25 catalyst_lookups=10 bod=119`
