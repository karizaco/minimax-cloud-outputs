# Earnings reaction scanner — 2026-11-04

- Cron: `0 8 * * 1-5` America/New_York (weekdays, 08:00 ET)
- Fire time (ET): 2026-11-04 08:05:26 Wed
- Run type: `scheduled_scan`
- Source: TradingView public screener (`scanner.tradingview.com/<market>/scan`);
  Yahoo chart API as an independent cross-check on the reported movers.
- Method: 4 passes (US top-200 mcap, US prior-session movers, EU/UK movers,
  ASX movers). Volume floor 10,000 on every pass; `country` filter for
  primary listings; exchange drop-list applied.
- Status: `ok`

## TL;DR

- 0 AMC reactions, 171 pre-market gaps, 89 without extended-hours data; 29 EU/UK and 1 ASX movers.
- Biggest US extended-hours move: DUOL PRE_GAP (19.51%).
- Biggest EU/UK move: NOBI (-32.09%, sweden).
- Biggest ASX move: BJY (-4.01%).
- EU/AU earnings-driven tagging is keyword-based on headlines (best-effort).

## US — Headline table

| Ticker | Venue | Close | Chg % | Pre-mkt % | Post-mkt % | Last earnings | Tag |
|---|---|---|---|---|---|---|---|
| DUOL | NASDAQ | 128 | -5.37 | 19.51 | — | 2026-11-03 (1d ago) | PRE_GAP |
| CBLL | NASDAQ | 28.27 | 4.86 | -15.53 | — | 2026-11-03 (1d ago) | PRE_GAP |
| CIFR | NASDAQ | 8.12 | 18.37 | -15.52 | — | 2026-11-02 (2d ago) | PRE_GAP |
| SEDG | NASDAQ | 32.88 | 8.86 | -14.39 | — | 2026-08-05 (91d ago) | PRE_GAP |
| NVTS | NASDAQ | 8.56 | 7.94 | 12.73 | — | 2026-11-03 (1d ago) | PRE_GAP |
| KD | NYSE | 12.94 | -4.64 | 11.67 | — | 2026-08-05 (91d ago) | PRE_GAP |
| DJT | NASDAQ | 5.95 | 5.12 | -11.03 | — | — | PRE_GAP |
| FIX | NYSE | 1285.13 | 7.08 | -11.01 | — | 2026-10-22 (13d ago) | PRE_GAP |
| HUT | NASDAQ | 63.75 | 15.90 | -10.90 | — | 2026-08-04 (92d ago) | PRE_GAP |
| LIME | NASDAQ | 25.48 | 12.84 | -9.54 | — | 2026-11-03 (1d ago) | PRE_GAP |
| OSCR | NYSE | 32.41 | 4.55 | 9.53 | — | 2026-08-06 (90d ago) | PRE_GAP |
| CLSK | NASDAQ | 8.15 | 13.99 | -9.13 | — | 2026-08-06 (90d ago) | PRE_GAP |
| VSH | NYSE | 27.22 | 6.66 | 8.30 | — | 2026-08-05 (91d ago) | PRE_GAP |
| AUGO | NASDAQ | 64.11 | -3.22 | 8.25 | — | 2026-08-05 (91d ago) | PRE_GAP |
| GLXY | NASDAQ | 16.83 | 15.35 | -7.84 | — | 2026-10-27 (8d ago) | PRE_GAP |
| SPCX | NASDAQ | 141.31 | 3.62 | -7.39 | — | 2026-10-20 (15d ago) | PRE_GAP |
| ECG | NYSE | 112.73 | 9.46 | -7.30 | — | 2026-11-03 (1d ago) | PRE_GAP |
| VRT | NYSE | 235.97 | 5.23 | -7.09 | — | 2026-10-28 (7d ago) | PRE_GAP |
| STRL | NASDAQ | 361.145 | 7.66 | -6.96 | — | 2026-10-28 (7d ago) | PRE_GAP |
| CRWV | NASDAQ | 53.74 | 7.16 | -6.96 | — | 2026-08-11 (85d ago) | PRE_GAP |
| BTDR | NASDAQ | 6.92 | 12.16 | -6.94 | — | 2026-08-10 (86d ago) | PRE_GAP |
| CGAU | NYSE | 19.61 | -4.67 | 6.86 | — | 2026-10-29 (6d ago) | PRE_GAP |
| RAL | NYSE | 71.31 | 7.54 | 6.72 | — | 2026-07-30 (97d ago) | PRE_GAP |
| CORZ | NASDAQ | 14.24 | 13.87 | -6.60 | — | 2026-07-28 (99d ago) | PRE_GAP |
| IREN | NASDAQ | 24.46 | 11.08 | -6.46 | — | 2026-08-27 (69d ago) | PRE_GAP |
| GEV | NYSE | 918.2 | 6.49 | -6.45 | — | 2026-10-28 (7d ago) | PRE_GAP |
| CGEM | NASDAQ | 15.75 | 5.49 | -6.35 | — | 2026-08-06 (90d ago) | PRE_GAP |
| SEI | NYSE | 69.37 | 6.07 | -6.30 | — | 2026-08-05 (91d ago) | PRE_GAP |
| SHLS | NASDAQ | 8.47 | 11.45 | 6.26 | — | 2026-08-04 (92d ago) | PRE_GAP |
| AEM | NYSE | 167.28 | -1.84 | 6.24 | — | 2026-10-28 (7d ago) | PRE_GAP |
| NXT | NASDAQ | 96.02 | 5.37 | 6.23 | — | 2026-10-28 (7d ago) | PRE_GAP |
| APLD | NASDAQ | 17.81 | 9.80 | -6.18 | — | 2026-10-07 (28d ago) | PRE_GAP |
| ELE | NASDAQ | 14.12 | -3.16 | 6.16 | — | 2026-08-11 (85d ago) | PRE_GAP |
| KGC | NYSE | 19.93 | -3.06 | 6.13 | — | 2026-10-28 (7d ago) | PRE_GAP |
| FLNC | NASDAQ | 5.5 | 5.57 | 5.87 | — | 2026-08-05 (91d ago) | PRE_GAP |
| HCA | NYSE | 462.86 | -1.04 | 5.86 | — | 2026-10-27 (8d ago) | PRE_GAP |
| TSLA | NASDAQ | 398.5 | -1.32 | -5.77 | — | 2026-10-21 (14d ago) | PRE_GAP |
| FPS | NYSE | 27.14 | 10.50 | -5.75 | — | 2026-09-15 (50d ago) | PRE_GAP |
| LDOS | NYSE | 134.72 | -6.55 | -5.73 | — | 2026-11-03 (1d ago) | PRE_GAP |
| SMG | NYSE | 61.8 | -5.11 | 5.66 | — | 2026-07-29 (98d ago) | PRE_GAP |
| NEM | NYSE | 107.47 | -1.49 | 5.64 | — | 2026-10-22 (13d ago) | PRE_GAP |
| MARA | NASDAQ | 7.16 | 11.35 | -5.59 | — | 2026-08-06 (90d ago) | PRE_GAP |
| ANET | NYSE | 169.91 | 3.52 | 5.35 | — | 2026-11-03 (1d ago) | PRE_GAP |
| PWR | NYSE | 657 | 5.77 | -5.18 | — | 2026-10-29 (6d ago) | PRE_GAP |
| INIO | NASDAQ | 18.31 | 11.58 | -4.97 | — | 2026-10-27 (8d ago) | PRE_GAP |
| RUN | NASDAQ | 8.68 | 5.21 | 4.94 | — | 2026-08-05 (91d ago) | PRE_GAP |
| WULF | NASDAQ | 12.53 | 14.53 | -4.87 | — | 2026-08-05 (91d ago) | PRE_GAP |
| TLN | NASDAQ | 357.28 | 7.29 | -4.84 | — | 2026-11-03 (1d ago) | PRE_GAP |
| CRDO | NASDAQ | 150.91 | 7.78 | -4.83 | — | 2026-09-01 (64d ago) | PRE_GAP |
| PLTR | NASDAQ | 175.4 | -1.65 | -4.79 | — | 2026-11-02 (2d ago) | PRE_GAP |
| LZ | NASDAQ | 6.69 | -3.46 | 4.78 | — | 2026-08-05 (91d ago) | PRE_GAP |
| ETN | NYSE | 391.7 | 7.00 | -4.77 | — | 2026-11-03 (1d ago) | PRE_GAP |
| SEZL | NASDAQ | 122.43 | -4.59 | 4.72 | — | 2026-08-06 (90d ago) | PRE_GAP |
| POWL | NASDAQ | 163.34 | 6.06 | -4.71 | — | 2026-08-03 (93d ago) | PRE_GAP |
| ZG | NASDAQ | 31.35 | -4.71 | 4.66 | — | 2026-08-05 (91d ago) | PRE_GAP |
| UBS | NYSE | 48 | -0.99 | 4.65 | — | 2026-10-28 (7d ago) | PRE_GAP |
| NVT | NYSE | 129.26 | 4.49 | -4.53 | — | 2026-10-30 (5d ago) | PRE_GAP |
| DELL | NYSE | 408.4 | 3.98 | -4.51 | — | 2026-09-01 (64d ago) | PRE_GAP |
| SNOW | NYSE | 295.04 | 1.50 | -4.50 | — | 2026-09-02 (63d ago) | PRE_GAP |
| ORCL | NYSE | 126.19 | 5.85 | -4.46 | — | 2026-09-10 (55d ago) | PRE_GAP |
| CEG | NASDAQ | 263.4 | 2.39 | -4.39 | — | 2026-08-06 (90d ago) | PRE_GAP |
| NBIS | NASDAQ | 151.64 | 7.25 | -4.37 | — | 2026-08-12 (84d ago) | PRE_GAP |
| SNDX | NASDAQ | 14.29 | 9.08 | 4.32 | — | 2026-11-02 (2d ago) | PRE_GAP |
| NYT | NYSE | 67.12 | -4.06 | 4.29 | — | 2026-08-05 (91d ago) | PRE_GAP |
| NET | NYSE | 273.62 | 3.19 | -4.25 | — | 2026-08-06 (90d ago) | PRE_GAP |
| XPEL | NASDAQ | 42.49 | -5.25 | -4.07 | — | 2026-08-05 (91d ago) | PRE_GAP |
| DHI | NYSE | 145.23 | -5.03 | 3.97 | — | 2026-10-29 (6d ago) | PRE_GAP |
| ERO | NYSE | 30.44 | 4.39 | 3.94 | — | 2026-11-02 (2d ago) | PRE_GAP |
| LEN | NYSE | 86.09 | -5.42 | 3.86 | — | 2026-09-16 (49d ago) | PRE_GAP |
| LKQ | NASDAQ | 19.26 | -3.36 | 3.84 | — | 2026-10-29 (6d ago) | PRE_GAP |
| AGX | NYSE | 348.24 | 4.23 | -3.80 | — | 2026-09-02 (63d ago) | PRE_GAP |
| INBX | NASDAQ | 81.08 | 12.36 | -3.76 | — | 2026-08-13 (83d ago) | PRE_GAP |
| PHM | NYSE | 126.88 | -3.36 | 3.64 | — | 2026-10-22 (13d ago) | PRE_GAP |
| OC | NYSE | 117.76 | -6.23 | -3.62 | — | 2026-11-04 (0d ago) | PRE_GAP |
| FCX | NYSE | 61.77 | -1.91 | 3.61 | — | 2026-10-27 (8d ago) | PRE_GAP |
| SCCO | NYSE | 173.49 | -2.25 | 3.60 | — | 2026-10-21 (14d ago) | PRE_GAP |
| AMZN | NASDAQ | 250.69 | 2.06 | 3.56 | — | 2026-10-29 (6d ago) | PRE_GAP |
| ULCC | NASDAQ | 6.47 | -12.92 | 3.55 | — | 2026-10-28 (7d ago) | PRE_GAP |
| VERX | NASDAQ | 15.26 | -3.60 | -3.47 | — | 2026-08-03 (93d ago) | PRE_GAP |
| CLS | NYSE | 259.94 | 4.30 | -3.44 | — | 2026-10-26 (9d ago) | PRE_GAP |
| BMRN | NASDAQ | 55.66 | -3.10 | 3.41 | — | 2026-11-02 (2d ago) | PRE_GAP |
| AMGN | NASDAQ | 461.26 | -0.90 | 3.41 | — | 2026-11-03 (1d ago) | PRE_GAP |
| MMM | NYSE | 177.05 | -0.73 | 3.36 | — | 2026-10-20 (15d ago) | PRE_GAP |
| LMT | NYSE | 639 | -0.65 | -3.34 | — | 2026-10-22 (13d ago) | PRE_GAP |
| FLEX | NASDAQ | 88.1 | 4.63 | -3.33 | — | 2026-10-28 (7d ago) | PRE_GAP |
| AMRZ | NYSE | 41.97 | -3.09 | 3.31 | — | 2026-10-28 (7d ago) | PRE_GAP |
| LBTYA | NASDAQ | 8.52 | 4.93 | 3.29 | — | 2026-11-03 (1d ago) | PRE_GAP |
| SRAD | NASDAQ | 14.2 | 10.33 | 3.27 | — | 2026-11-03 (1d ago) | PRE_GAP |
| ISRG | NASDAQ | 440.75 | 0.89 | 3.23 | — | 2026-10-20 (15d ago) | PRE_GAP |
| CCEP | NASDAQ | 111.56 | -3.48 | 3.23 | — | 2026-08-04 (92d ago) | PRE_GAP |
| SHW | NYSE | 340.87 | -3.26 | 3.19 | — | 2026-10-27 (8d ago) | PRE_GAP |
| RTX | NYSE | 203.82 | 0.51 | -3.10 | — | 2026-10-20 (15d ago) | PRE_GAP |
| PFGC | NYSE | 96.51 | -4.29 | 3.00 | — | 2026-08-12 (84d ago) | PRE_GAP |
| WDC | NASDAQ | 347.35 | 2.59 | -2.97 | — | 2026-10-22 (13d ago) | PRE_GAP |
| CVS | NYSE | 91.41 | 3.28 | -2.91 | — | 2026-11-04 (0d ago) | PRE_GAP |
| TH | NASDAQ | 14.49 | 6.47 | -2.90 | — | 2026-08-10 (86d ago) | PRE_GAP |
| RH | NYSE | 134.13 | -8.46 | 2.89 | — | 2026-09-10 (55d ago) | PRE_GAP |
| WCC | NYSE | 351.61 | 4.78 | -2.88 | — | 2026-10-29 (6d ago) | PRE_GAP |
| RCUS | NYSE | 18.91 | 5.94 | 2.86 | — | 2026-08-05 (91d ago) | PRE_GAP |
| T | NYSE | 21.39 | -0.23 | 2.85 | — | 2026-10-21 (14d ago) | PRE_GAP |
| SOLS | NASDAQ | 61.74 | 4.77 | 2.85 | — | 2026-11-04 (0d ago) | PRE_GAP |
| AEHR | NASDAQ | 65.11 | 26.50 | -2.83 | — | 2026-07-14 (113d ago) | PRE_GAP |
| LEN.B | NYSE | 85.11 | -5.35 | 2.81 | — | 2026-09-16 (49d ago) | PRE_GAP |
| HD | NYSE | 333.66 | -2.20 | 2.80 | — | 2026-08-18 (78d ago) | PRE_GAP |
| EROC | NYSE | 8.96 | 13.42 | -2.79 | — | 2026-08-11 (85d ago) | PRE_GAP |
| BE | NYSE | 214.01 | 9.05 | -2.76 | — | 2026-10-22 (13d ago) | PRE_GAP |
| MRNA | NASDAQ | 228.44 | 3.45 | 2.75 | — | 2026-07-31 (96d ago) | PRE_GAP |
| RRX | NYSE | 179.93 | 11.81 | -2.74 | — | 2026-11-03 (1d ago) | PRE_GAP |
| INTC | NASDAQ | 60.55 | 0.97 | -2.73 | — | 2026-10-29 (6d ago) | PRE_GAP |
| ALK | NYSE | 36.78 | -3.94 | 2.73 | — | 2026-10-20 (15d ago) | PRE_GAP |
| Z | NASDAQ | 30.98 | -4.21 | 2.68 | — | 2026-08-05 (91d ago) | PRE_GAP |
| TMUS | NASDAQ | 154.41 | -3.58 | 2.65 | — | 2026-10-28 (7d ago) | PRE_GAP |
| GILD | NASDAQ | 167.47 | -1.68 | 2.63 | — | 2026-10-29 (6d ago) | PRE_GAP |
| MRVL | NASDAQ | 171.97 | 0.33 | -2.62 | — | 2026-08-27 (69d ago) | PRE_GAP |
| FRVO | NASDAQ | 9.32 | 12.97 | 2.58 | — | 2026-08-12 (84d ago) | PRE_GAP |
| ALHC | NASDAQ | 7.39 | 5.57 | 2.58 | — | 2026-10-29 (6d ago) | PRE_GAP |
| AXTI | NASDAQ | 51.33 | 6.49 | -2.57 | — | 2026-10-29 (6d ago) | PRE_GAP |
| VZ | NYSE | 45.24 | 0.42 | 2.56 | — | 2026-10-26 (9d ago) | PRE_GAP |
| BFLY | NYSE | 6.4 | 4.23 | 2.53 | — | 2026-10-29 (6d ago) | PRE_GAP |
| IP | NYSE | 35.12 | -4.15 | 2.51 | — | 2026-10-28 (7d ago) | PRE_GAP |
| NEE | NYSE | 84.33 | -0.82 | 2.44 | — | 2026-10-21 (14d ago) | PRE_GAP |
| BUUU | NASDAQ | 7.38 | 28.35 | -2.44 | — | — | PRE_GAP |
| TRV | NYSE | 395.41 | -0.85 | 2.42 | — | 2026-10-16 (19d ago) | PRE_GAP |
| STDN | NYSE | 12.41 | 4.81 | 2.42 | — | 2026-08-26 (70d ago) | PRE_GAP |
| ABNB | NASDAQ | 166.96 | -2.43 | 2.42 | — | 2026-08-06 (90d ago) | PRE_GAP |
| WGS | NASDAQ | 68.64 | 7.10 | 2.42 | — | 2026-08-03 (93d ago) | PRE_GAP |
| CAT | NYSE | 623.94 | 1.68 | -2.41 | — | 2026-10-29 (6d ago) | PRE_GAP |
| SMMT | NASDAQ | 15.8 | 6.76 | 2.41 | — | 2026-07-23 (104d ago) | PRE_GAP |
| SYK | NYSE | 310.55 | 1.22 | 2.40 | — | 2026-10-29 (6d ago) | PRE_GAP |
| STX | NASDAQ | 606.38 | 2.13 | -2.40 | — | 2026-10-27 (8d ago) | PRE_GAP |
| DRTS | NASDAQ | 13.54 | 5.53 | 2.36 | — | 2026-08-10 (86d ago) | PRE_GAP |
| UNH | NYSE | 404.44 | 1.00 | -2.33 | — | 2026-10-13 (22d ago) | PRE_GAP |
| AMRC | NYSE | 22.28 | 6.30 | 2.33 | — | 2026-08-03 (93d ago) | PRE_GAP |
| GD | NYSE | 374.5 | 0.28 | -2.33 | — | 2026-10-30 (5d ago) | PRE_GAP |
| FN | NYSE | 363.33 | 15.45 | -2.29 | — | 2026-11-02 (2d ago) | PRE_GAP |
| FTRE | NASDAQ | 20.95 | 4.65 | 2.29 | — | 2026-10-29 (6d ago) | PRE_GAP |
| MSFT | NASDAQ | 520.99 | 2.74 | 2.28 | — | 2026-10-28 (7d ago) | PRE_GAP |
| TWST | NASDAQ | 140.3 | 8.73 | 2.28 | — | 2026-08-03 (93d ago) | PRE_GAP |
| ADP | NASDAQ | 296.01 | -0.93 | 2.28 | — | 2026-10-28 (7d ago) | PRE_GAP |
| MCD | NYSE | 263.04 | -0.98 | 2.27 | — | 2026-08-04 (92d ago) | PRE_GAP |
| INTU | NASDAQ | 344.72 | -2.10 | 2.26 | — | 2026-08-25 (71d ago) | PRE_GAP |
| MYRG | NASDAQ | 291.59 | 4.80 | -2.26 | — | 2026-10-28 (7d ago) | PRE_GAP |
| WLK | NYSE | 68.47 | -3.79 | 2.23 | — | 2026-11-04 (0d ago) | PRE_GAP |
| PAGS | NYSE | 7.65 | -3.04 | 2.22 | — | 2026-08-11 (85d ago) | PRE_GAP |
| MPC | NYSE | 427.34 | -0.71 | -2.22 | — | 2026-11-03 (1d ago) | PRE_GAP |
| ENPH | NASDAQ | 30.42 | 8.92 | 2.20 | — | 2026-10-27 (8d ago) | PRE_GAP |
| WMT | NASDAQ | 124.86 | -2.22 | 2.19 | — | 2026-08-20 (76d ago) | PRE_GAP |
| IT | NYSE | 204.22 | -13.19 | 2.19 | — | 2026-11-03 (1d ago) | PRE_GAP |
| JNJ | NYSE | 266.17 | -1.62 | 2.19 | — | 2026-10-13 (22d ago) | PRE_GAP |
| MAR | NASDAQ | 416.38 | 0.02 | 2.19 | — | 2026-11-02 (2d ago) | PRE_GAP |
| MOS | NYSE | 18.42 | -3.21 | -2.17 | — | 2026-11-03 (1d ago) | PRE_GAP |
| EMR | NYSE | 166.39 | 0.26 | -2.16 | — | 2026-11-04 (0d ago) | PRE_GAP |
| LOW | NYSE | 213.38 | -2.19 | 2.16 | — | 2026-08-19 (77d ago) | PRE_GAP |
| CRM | NYSE | 222.2 | -1.76 | 2.16 | — | 2026-08-26 (70d ago) | PRE_GAP |
| BX | NYSE | 118.19 | -1.62 | 2.16 | — | 2026-10-22 (13d ago) | PRE_GAP |
| RVTY | NYSE | 163.48 | 7.84 | 2.15 | — | 2026-11-03 (1d ago) | PRE_GAP |
| CRCL | NYSE | 75.22 | 4.36 | -2.14 | — | 2026-11-04 (0d ago) | PRE_GAP |
| REGN | NASDAQ | 973.36 | 1.26 | 2.12 | — | 2026-10-30 (5d ago) | PRE_GAP |
| TJX | NYSE | 137.63 | -2.39 | 2.11 | — | 2026-08-19 (77d ago) | PRE_GAP |
| ABT | NYSE | 109.4 | -0.69 | 2.10 | — | 2026-10-21 (14d ago) | PRE_GAP |
| LLY | NYSE | 1409.38 | -0.11 | 2.10 | — | 2026-10-29 (6d ago) | PRE_GAP |
| GLW | NYSE | 126.14 | 2.39 | -2.10 | — | 2026-10-27 (8d ago) | PRE_GAP |
| WRBY | NYSE | 21.94 | -8.05 | 2.10 | — | 2026-08-06 (90d ago) | PRE_GAP |
| AXP | NYSE | 325.5 | -0.76 | 2.09 | — | 2026-10-23 (12d ago) | PRE_GAP |
| IBTA | NYSE | 60.35 | 20.53 | 2.07 | — | 2026-11-02 (2d ago) | PRE_GAP |
| CNQ | NYSE | 53.6 | -0.07 | -2.04 | — | 2026-08-06 (90d ago) | PRE_GAP |
| DIS | NYSE | 114.18 | 0.95 | 2.03 | — | 2026-08-05 (91d ago) | PRE_GAP |
| AZN | NYSE | 183.88 | -1.45 | 2.02 | — | 2026-10-30 (5d ago) | PRE_GAP |
| PLPC | NASDAQ | 311.51 | 11.78 | -2.02 | — | 2026-10-28 (7d ago) | PRE_GAP |
| MGA | NYSE | 62.97 | -3.89 | 2.00 | — | 2026-10-30 (5d ago) | PRE_GAP |
| BAX | NYSE | 25.49 | 5.24 | 2.00 | — | 2026-10-29 (6d ago) | PRE_GAP |

## US — QUIET one-liners

| Ticker | Venue | Chg % | Pre-mkt % | Post-mkt % |
|---|---|---|---|---|
| WY | NYSE | -3.29 | 1.99 | — |
| POWI | NASDAQ | 4.77 | 1.98 | — |
| PEP | NASDAQ | -2.24 | 1.97 | — |
| INSM | NASDAQ | -4.46 | 1.97 | — |
| MU | NASDAQ | 2.58 | -1.96 | — |
| DXC | NYSE | -6.64 | 1.96 | — |
| PNC | NYSE | -0.97 | 1.96 | — |
| DT | NYSE | -14.69 | -1.96 | — |
| BAM | NYSE | -1.01 | 1.94 | — |
| VRTX | NASDAQ | -4.05 | 1.93 | — |
| IOVA | NASDAQ | 10.10 | 1.93 | — |
| ACN | NYSE | -2.45 | 1.91 | — |
| SMTC | NASDAQ | 4.12 | -1.90 | — |
| SNDK | NASDAQ | 4.78 | -1.88 | — |
| NFLX | NASDAQ | 1.73 | 1.86 | — |

## EU/UK — Headline table

| Ticker | Market | Venue | Close | Chg % | Currency | Last earnings |
|---|---|---|---|---|---|---|
| NOBI | sweden | OMXSTO | 9.446 | -32.09 | SEK | 2026-07-17 |
| MTRO | uk | LSE | 178 | +16.64 | GBX | 2026-08-03 |
| ZZ_B | sweden | OMXSTO | 116.5 | -13.96 | SEK | 2026-08-25 |
| PNDORA | denmark | OMXCOP | 928.6 | +11.96 | DKK | 2026-08-11 |
| MMT | france | EURONEXT | 11.32 | +11.86 | EUR | 2024-07-23 |
| RUG | sweden | OMXSTO | 79.2 | +11.71 | SEK | 2026-07-17 |
| CHEF | sweden | OMXSTO | 81.5 | -11.32 | SEK | 2026-08-20 |
| ASKER | sweden | OMXSTO | 76 | +10.95 | SEK | 2026-07-21 |
| BEWI | norway | OSL | 19.4 | +10.86 | NOK | 2026-08-19 |
| TRUE_B | sweden | OMXSTO | 22.26 | +10.47 | SEK | 2026-11-03 |
| BOUV | norway | OSL | 48.75 | -9.55 | NOK | 2026-08-19 |
| HEI | germany | XETR | 170.45 | +8.88 | EUR | 2026-07-29 |
| ORRON | sweden | OMXSTO | 8.71 | +8.74 | SEK | 2026-08-05 |
| WEIR | uk | LSE | 2418 | -8.06 | GBX | 2026-07-29 |
| GL9 | ireland | EURONEXT | 21.28 | +7.97 | EUR | 2026-08-06 |
| BINT | norway | OSL | 21.8 | +7.39 | NOK | 2025-05-29 |
| OHB | germany | XETR | 227 | +7.33 | EUR | 2026-08-06 |
| LINK | norway | OSL | 26.8 | +6.77 | NOK | 2026-08-19 |
| NDX1 | germany | XETR | 41.54 | +6.62 | EUR | 2026-07-29 |
| SOI | france | EURONEXT | 116.5 | -6.61 | EUR | 2026-05-27 |
| HOC | uk | LSE | 459.4 | +6.59 | GBX | 2026-08-26 |
| AIXA | germany | GETTEX | 32.04 | -6.56 | EUR | 2026-10-29 |
| RBI | austria | VIE | 60.3 | +6.54 | EUR | 2026-11-03 |
| S92 | germany | XETR | 54.25 | +6.37 | EUR | 2026-08-13 |
| EBS | austria | VIE | 114 | +6.34 | EUR | 2026-10-30 |
| DBK | germany | FWB | 32.275 | +6.31 | EUR | 2026-10-28 |
| ZAP | norway | OSL | 58 | -6.30 | NOK | 2026-08-19 |
| KEOC | sweden | OMXSTO | 6.48 | -6.09 | SEK | 2026-08-31 |
| CBK | germany | SWB | 40.15 | +6.05 | EUR | 2026-08-06 |

## AU (ASX) — Headline table

| Ticker | Venue | Close | Chg % | Currency | Last earnings |
|---|---|---|---|---|---|
| BJY | ASX | 8.13 | -4.01 | AUD | 2026-08-26 |

## Catalysts

| Ticker | Region | Catalyst | Earnings-driven |
|---|---|---|---|
| DUOL | US | Q3 revenue $309.0M (+14% y/y) beat $303M est; DAU +29% to 64.9M; EPS $0.54 vs $0.56 est; guidance raised across the board (FY26 bookings $1.296B, adj EBITDA $323M) | Y |
| CBLL | US | Q3 revenue $29.3M (+30% y/y) but net loss $0.55/sh vs -$0.51 est and adj EBITDA loss widened to $12.1M from $9.2M on opex +36%; FY26 revenue guidance raised to $115-117M | Y |
| CIFR | US | Q3 (Nov 2) revenue $26.7M missed $39.3M est, -62.8% y/y; target cuts (JPM $22->$18, Cantor $19->$15, KB $28->$11, then KB downgrade to Market Perform, $9.50, Nov 4) | Y |
| SEDG | US | Q3 reported pre-market Nov 4: revenue $326.1M missed $329.1M est (-4.1% y/y), adj EPS $0.29 vs $0.02 est; Q4 guidance cut to $245-275M with non-GAAP GM 17-21% | Y |
| NVTS | US | Q3 revenue $14.0M at the high end of guidance (+33% q/q, +38% y/y - first y/y growth since 2024); non-GAAP GM 40%; Q4 guide $16.0M +/-0.5M (+119% y/y) | Y |
| NOBI | EU | Q3 adj EBIT SEK 47M vs SEK 69M a year ago, operating cash flow -SEK 157M, Nobia Park ramp-up still unresolved; Nordic restructuring targets SEK 150M annual savings from Q4 2027 | Y |
| MTRO | EU | Q3 trading update: target lending +37% y/y to GBP 6.62B, exit NIM 3.45% (+42bp); RoTE guidance reaffirmed (>13% Q4 2026, >18% by 2028) | Y |
| ZZ_B | EU | Preliminary October sales report: group revenue +1% y/y to SEK 328.7M (sales markets SEK 325.1M, +1%); Faun Pharma external sales +33% to SEK 3.6M | Y |
| BJY | AU | no fresh catalyst found - only the Magellan (MFG) to Barrenjoey (BJY) name/ticker change effective Nov 2; no company announcement found for the Nov 4 session | N |


## Source health

- scanner_calls: 39 | scanner_errors: 0
- pipeline_version: 2026-11-04.1
- et_clock: zoneinfo America/New_York (DST-aware; a fixed UTC-4 mislabels every winter fire)
- yahoo_calls: 238 | yahoo_429: 0 | yahoo_errors: 3
- cross_check (screener vs Yahoo, reference-close validation): agree=199 mismatch=25 unverified=2 stale_reference=25
  method: the screener's implied reference close (close / (1 + change/100)) is compared
  with Yahoo's own reference close. A match proves the move was measured against the
  TRUE prior close; a mismatch means the row sits on a STALE reference (phantom move).
  Coverage: every row of the US headline, EU/UK and ASX tables is checked. The US QUIET
  one-liner table is NOT cross-checked.
  Yahoo bar mode: {"closed": 170, "live": 29} (closed = last completed session bar;
  live = in-progress EU/UK session bar, which is what a weekday 08:00 ET EU move needs)
  live drift between the screener snapshot and the later Yahoo print: median=0.00pp max=1.38pp (expected on a live market)
- cross_check mismatches: [{"region": "germany", "symbol": "G24.DE", "tv": 6.785, "yahoo": 5.669, "delta": 1.116, "ref_delta_pct": -0.935, "tv_implied_ref": 84.75, "yahoo_ref": 85.55, "yahoo_date": "2026-11-04", "verdict": "stale_reference"}, {"region": "AU", "symbol": "4DX.AX", "tv": -10.788, "yahoo": -25.61, "delta": 14.822, "ref_delta_pct": -26.524, "tv_implied_ref": 2.41, "yahoo_ref": 3.28, "yahoo_date": "2026-10-29", "verdict": "stale_reference"}, {"region": "AU", "symbol": "SLX.AX", "tv": -9.581, "yahoo": -4.31, "delta": -5.271, "ref_delta_pct": -4.023, "tv_implied_ref": 3.34, "yahoo_ref": 3.48, "yahoo_date": "2026-10-29", "verdict": "stale_reference"}, {"region": "AU", "symbol": "AYA.AX", "tv": 8.091, "yahoo": 1.465, "delta": 6.626, "ref_delta_pct": 13.187, "tv_implied_ref": 3.09, "yahoo_ref": 2.73, "yahoo_date": "2026-10-29", "verdict": "stale_reference"}, {"region": "AU", "symbol": "EOS.AX", "tv": -7.771, "yahoo": -5.228, "delta": -2.543, "ref_delta_pct": -12.681, "tv_implied_ref": 7.85, "yahoo_ref": 8.99, "yahoo_date": "2026-10-29", "verdict": "stale_reference"}, {"region": "AU", "symbol": "DRO.AX", "tv": -7.634, "yahoo": -5.517, "delta": -2.117, "ref_delta_pct": -9.655, "tv_implied_ref": 1.31, "yahoo_ref": 1.45, "yahoo_date": "2026-10-29", "verdict": "stale_reference"}, {"region": "AU", "symbol": "CU6.AX", "tv": -6.122, "yahoo": -5.988, "delta": -0.134, "ref_delta_pct": -11.976, "tv_implied_ref": 1.47, "yahoo_ref": 1.67, "yahoo_date": "2026-10-29", "verdict": "stale_reference"}, {"region": "AU", "symbol": "PNI.AX", "tv": -5.93, "yahoo": 3.756, "delta": -9.686, "ref_delta_pct": 8.585, "tv_implied_ref": 16.19, "yahoo_ref": 14.91, "yahoo_date": "2026-10-29", "verdict": "stale_reference"}, {"region": "AU", "symbol": "NWL.AX", "tv": -5.849, "yahoo": 0.278, "delta": -6.127, "ref_delta_pct": 8.278, "tv_implied_ref": 19.49, "yahoo_ref": 18.0, "yahoo_date": "2026-10-29", "verdict": "stale_reference"}, {"region": "AU", "symbol": "QAN.AX", "tv": -4.915, "yahoo": 1.267, "delta": -6.182, "ref_delta_pct": 7.834, "tv_implied_ref": 9.36, "yahoo_ref": 8.68, "yahoo_date": "2026-10-29", "verdict": "stale_reference"}, {"region": "AU", "symbol": "EOL.AX", "tv": -4.859, "yahoo": 0.35, "delta": -5.209, "ref_delta_pct": -0.699, "tv_implied_ref": 14.2, "yahoo_ref": 14.3, "yahoo_date": "2026-10-29", "verdict": "stale_reference"}, {"region": "AU", "symbol": "CIA.AX", "tv": -4.852, "yahoo": 2.406, "delta": -7.258, "ref_delta_pct": -0.802, "tv_implied_ref": 1.855, "yahoo_ref": 1.87, "yahoo_date": "2026-10-29", "verdict": "stale_reference"}, {"region": "AU", "symbol": "ASB.AX", "tv": -4.535, "yahoo": -0.221, "delta": -4.314, "ref_delta_pct": -2.434, "tv_implied_ref": 4.41, "yahoo_ref": 4.52, "yahoo_date": "2026-10-29", "verdict": "stale_reference"}, {"region": "AU", "symbol": "QAL.AX", "tv": 4.331, "yahoo": -0.847, "delta": 5.178, "ref_delta_pct": 7.627, "tv_implied_ref": 2.54, "yahoo_ref": 2.36, "yahoo_date": "2026-10-29", "verdict": "stale_reference"}, {"region": "AU", "symbol": "NEU.AX", "tv": -4.259, "yahoo": 1.092, "delta": -5.351, "ref_delta_pct": 2.582, "tv_implied_ref": 20.66, "yahoo_ref": 20.14, "yahoo_date": "2026-10-29", "verdict": "stale_reference"}, {"region": "AU", "symbol": "WA1.AX", "tv": -4.234, "yahoo": -9.032, "delta": 4.798, "ref_delta_pct": -12.622, "tv_implied_ref": 8.03, "yahoo_ref": 9.19, "yahoo_date": "2026-10-29", "verdict": "stale_reference"}, {"region": "AU", "symbol": "NXT.AX", "tv": 4.147, "yahoo": -4.862, "delta": 9.009, "ref_delta_pct": 1.621, "tv_implied_ref": 6.27, "yahoo_ref": 6.17, "yahoo_date": "2026-10-29", "verdict": "stale_reference"}, {"region": "AU", "symbol": "HUB.AX", "tv": -4.144, "yahoo": 0.541, "delta": -4.685, "ref_delta_pct": 6.088, "tv_implied_ref": 76.5, "yahoo_ref": 72.11, "yahoo_date": "2026-10-29", "verdict": "stale_reference"}, {"region": "AU", "symbol": "VGN.AX", "tv": -4.074, "yahoo": 1.688, "delta": -5.762, "ref_delta_pct": 13.924, "tv_implied_ref": 2.7, "yahoo_ref": 2.37, "yahoo_date": "2026-10-29", "verdict": "stale_reference"}, {"region": "AU", "symbol": "VEA.AX", "tv": 4.074, "yahoo": 1.064, "delta": 3.01, "ref_delta_pct": -4.255, "tv_implied_ref": 2.7, "yahoo_ref": 2.82, "yahoo_date": "2026-10-29", "verdict": "stale_reference"}, {"region": "AU", "symbol": "EHL.AX", "tv": -4.015, "yahoo": 2.692, "delta": -6.707, "ref_delta_pct": 5.385, "tv_implied_ref": 1.37, "yahoo_ref": 1.3, "yahoo_date": "2026-10-29", "verdict": "stale_reference"}, {"region": "AU", "symbol": "ELV.AX", "tv": -3.797, "yahoo": -5.621, "delta": 1.824, "ref_delta_pct": -6.509, "tv_implied_ref": 3.16, "yahoo_ref": 3.38, "yahoo_date": "2026-10-29", "verdict": "stale_reference"}, {"region": "AU", "symbol": "SGM.AX", "tv": -3.765, "yahoo": 2.665, "delta": -6.43, "ref_delta_pct": 7.502, "tv_implied_ref": 21.78, "yahoo_ref": 20.26, "yahoo_date": "2026-10-29", "verdict": "stale_reference"}, {"region": "AU", "symbol": "INA.AX", "tv": -3.759, "yahoo": -0.933, "delta": -2.826, "ref_delta_pct": -0.746, "tv_implied_ref": 5.32, "yahoo_ref": 5.36, "yahoo_date": "2026-10-29", "verdict": "stale_reference"}, {"region": "AU", "symbol": "GDG.AX", "tv": -3.681, "yahoo": -1.587, "delta": -2.094, "ref_delta_pct": 3.492, "tv_implied_ref": 3.26, "yahoo_ref": 3.15, "yahoo_date": "2026-10-29", "verdict": "stale_reference"}]
- stale_rows_dropped: US=none EU=['G24'] AU=['4DX', 'SLX', 'AYA', 'EOS', 'DRO', 'CU6', 'PNI', 'NWL', 'QAN', 'EOL', 'CIA', 'ASB', 'QAL', 'NEU', 'WA1', 'NXT', 'HUB', 'VGN', 'VEA', 'EHL', 'ELV', 'SGM', 'INA', 'GDG']
- us_premarket_check (Yahoo 1-min pre/post feed vs the screener pre-market column): checked=9 within_1pp=3 within_3pp=8 unavailable=1
  us_premarket outliers (>3pp; thin pre-market books, not a screener error): [{"symbol": "SEDG", "tv": -14.394, "yahoo": -9.824, "delta": 4.57, "yahoo_asof": "08:05"}]
- markets_with_lt5_rows: ['france:less=3', 'netherlands:less=1', 'belgium:less=0', 'portugal:egreater=3', 'portugal:less=0', 'ireland:egreater=4', 'ireland:less=0', 'italy:less=3', 'switzerland:less=2', 'spain:less=2', 'denmark:less=1', 'finland:egreater=4', 'finland:less=2', 'poland:less=0', 'austria:less=0', 'greece:egreater=3', 'greece:less=0']
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
- bod_no_extended_hours: 89 (deferred to the next scan; not in the headline table)
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

`earnings-reaction target=earnings-reactions:2026-11-04 candidates=550 amc_reactions=0 pre_gaps=171 eu_reactions=29 asx_reactions=1 catalyst_lookups=9 bod=89`
