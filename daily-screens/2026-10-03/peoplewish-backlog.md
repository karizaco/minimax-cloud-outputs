# peoplewish 1000%-in-10-years — Pattern-Study Backlog

_Long-lived log of US equities that have compounded 1000%+ from their 10-year low
to the most recent close. Maintained by cron #6 stock-screener-pattern-study-backlog
(Saturday weekly). New rows are appended each Saturday._

## Methodology

- **Universe:** all symbols in shibui.stock_quotes with at least 1,260 trading days
  in the trailing 10-year window (≥ 5y of data, to filter out recent IPOs / SPAC
  mergers that wouldn't have a real 10-yr baseline).
- **Trigger:** `(current_close / 10y_min_close) - 1 >= 10.0` (i.e., 1000%+ from trough).
- **Min close filter:** `min_close_10y >= $0.50` (avoids micro-cap noise that hit
  1000% off a sub-penny base).
- **Sort:** current gain from 10y low, descending. Cap 200 rows per run.
- **Chart-shape tags** (computed on the most recent 60d / 10d window of stock_quotes):
  - `coil` — close within 15% of 60d high AND contraction_ratio (10d range / 60d range) < 0.85
  - `VCP` — Volatility Contraction Pattern: contraction_ratio < 0.65 (10d range < 65% of 60d range)
  - `breakout` — close within 5% of 60d high (close / high_60d ≥ 0.95)
  - `EP` — Extended Play: current close > 50% above YTD low (already in a strong uptrend)
  - `big_day` — most recent trading day moved > 5% (catalyst signal)

## Run manifest

- **Run date (ET):** 2026-10-03 (Saturday 10:00 ET cron)
- **Latest shibui data:** 2026-10-02 (T+1 lag)
- **Source:** shibui MCP, `stock_data_query` over shibui.stock_quotes + shibui.general_info
- **Rows in this run:** 75 newly-tagged (top of 200-row scan)
- **Scan depth:** full 10-year window per symbol; window function + `MIN(close)` aggregate
- **Source tag:** `_source=mcp` (shibui primary path)

## New entries (2026-10-03 run)

| # | Ticker | Name | Exchange | Sector | Current | 10y Low | Peak Gain | Gain | 60d High | Contraction | YTD Low | Last Day | Tags |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | NVDA | NVIDIA Corp | NASDAQ | Information Technology | $233.95 | $1.63 | 14330% | 14220% | $233.95 | 0.86 | $164.27 | +1.34% | breakout |
| 2 | CLS | Celestica Inc | NYSE | Information Technology | $387.32 | $2.83 | 16593% | 13586% | $387.32 | 1.01 | $244.51 | +3.81% | breakout, EP |
| 3 | BE | Bloom Energy Corp - Class A | NYSE | Industrials | $289.15 | $2.67 | 12853% | 10730% | $291.25 | 1.08 | $88.86 | +4.17% | breakout, EP |
| 4 | AEHR | Aehr Test Systems | NASDAQ | Information Technology | $107.21 | $1.06 | 13637% | 10014% | $145.61 | 0.85 | $20.99 | +5.52% | EP, big_day |
| 5 | AMD | Advanced Micro Devices Inc | NASDAQ | Information Technology | $633.91 | $6.29 | 9970% | 9970% | $633.91 | 0.91 | $188.22 | +2.95% | breakout, EP |
| 6 | LEU | Centrus Energy Corp - Class A | NYSE | Energy | $139.27 | $1.44 | 30178% | 9572% | $194.78 | 0.66 | $135.75 | +0.12% | — |
| 7 | FRHC | Freedom Holding Corp | NASDAQ | Financials | $173.00 | $1.85 | 10178% | 9251% | $176.37 | 1.03 | $107.98 | -0.24% | breakout, EP |
| 8 | INOD | Innodata Inc | NASDAQ | Industrials | $70.07 | $0.78 | 15477% | 8883% | $71.99 | 1.17 | $34.23 | -2.48% | breakout, EP |
| 9 | AXSM | Axsome Therapeutics Inc | NASDAQ | Health Care | $179.25 | $2.00 | 12658% | 8862% | $220.89 | 1.16 | $152.28 | -1.55% | — |
| 10 | USD | PROSHARES ULTRA SEMICONDUCTORS | NYSE | — | $100.98 | $1.16 | 9683% | 8601% | $100.98 | 0.88 | $42.56 | +3.29% | breakout, EP |
| 11 | CVNA | Carvana Co. - Class A | NYSE | Consumer Discretionary | $63.77 | $0.74 | 12762% | 8471% | $75.77 | 1.06 | $54.46 | +1.16% | — |
| 12 | CDNA | Caredx Inc | NASDAQ | Health Care | $67.15 | $0.79 | 12063% | 8443% | $67.15 | 1.35 | $15.56 | +1.39% | breakout, EP |
| 13 | STRL | Sterling Infrastructure Inc | NASDAQ | Industrials | $533.42 | $6.42 | 15379% | 8209% | $603.89 | 0.88 | $293.30 | +5.60% | EP, big_day |
| 14 | AMR | Alpha Metallurgical Resources Inc | NYSE | Materials | $171.54 | $2.10 | 20958% | 8069% | $235.70 | 0.83 | $133.64 | +0.73% | — |
| 15 | AAOI | Applied Optoelectronics Inc | NASDAQ | Information Technology | $115.59 | $1.50 | 14773% | 7606% | $154.89 | 0.96 | $31.67 | +7.71% | EP, big_day |
| 16 | DAVE | Dave Inc - Class A | NASDAQ | Information Technology | $346.57 | $4.54 | 9968% | 7525% | $430.16 | 0.89 | $152.21 | +2.06% | EP |
| 17 | AXTI | AXT Inc | NASDAQ | Information Technology | $85.87 | $1.16 | 12040% | 7303% | $95.97 | 0.90 | $14.62 | +4.96% | EP |
| 18 | GBTC | Grayscale Investments LLC | NYSE | — | $65.11 | $0.95 | 10315% | 6789% | $66.88 | 1.05 | $44.98 | -0.50% | breakout |
| 19 | KOD | Kodiak Sciences Inc | NASDAQ | Health Care | $94.45 | $1.40 | 11648% | 6646% | $98.46 | 1.98 | $20.88 | -4.07% | breakout, EP |
| 20 | MU | Micron Technology Inc | NASDAQ | Information Technology | $1074.89 | $16.62 | 7202% | 6367% | $1097.39 | 0.88 | $294.86 | -2.05% | breakout, EP |
| 21 | FIX | Comfort Systems USA Inc | NYSE | Industrials | $1728.01 | $27.21 | 7495% | 6251% | $1881.18 | 0.84 | $938.40 | +2.53% | coil, EP |
| 22 | MOD | Modine Manufacturing Company | NYSE | Consumer Discretionary | $178.20 | $2.98 | 10198% | 5880% | $216.75 | 1.11 | $111.18 | -5.82% | EP, big_day |
| 23 | TRGP | Targa Resources Corp | NYSE | Energy | $281.74 | $4.73 | 6290% | 5856% | $302.25 | 1.00 | $173.57 | +0.87% | EP |
| 24 | DAC | Danaos Corporation | NYSE | Industrials | $165.15 | $2.78 | 5841% | 5841% | $165.15 | 1.08 | $93.34 | +2.11% | breakout, EP |
| 25 | WGS | GeneDx Holdings Corp - Class A | NASDAQ | Health Care | $73.09 | $1.24 | 68588% | 5794% | $104.95 | 1.32 | $32.21 | +3.00% | EP |
| 26 | CAMT | Camtek Ltd | NASDAQ | Information Technology | $165.19 | $2.83 | 7231% | 5737% | $174.20 | 0.88 | $110.55 | +7.41% | big_day |
| 27 | SOXL | DIREXION DAILY SEMICONDUCTOR BULL 3X SHARES | NYSE | — | $163.71 | $2.84 | 10505% | 5673% | $163.71 | 0.89 | $39.52 | +6.52% | breakout, EP, big_day |
| 28 | TECL | DIREXION DAILY TECHNOLOGY BULL 3X SHARES | NYSE | — | $246.31 | $4.30 | 6254% | 5627% | $246.31 | 0.89 | $75.16 | +2.92% | breakout, EP |
| 29 | ATLC | Atlanticus Holdings Corp | NASDAQ | Financials | $91.89 | $1.63 | 6758% | 5537% | $111.79 | 0.75 | $47.50 | +2.91% | EP |
| 30 | NTRA | Natera Inc | NASDAQ | Health Care | $410.35 | $7.50 | 5427% | 5371% | $414.52 | 0.97 | $181.00 | +0.46% | breakout, EP |
| 31 | SITM | SiTime Corp | NASDAQ | Information Technology | $709.44 | $13.00 | 6834% | 5357% | $749.44 | 0.96 | $305.21 | +4.50% | EP |
| 32 | MNPR | Monopar Therapeutics Inc | NASDAQ | Health Care | $77.97 | $1.45 | 9233% | 5290% | $123.84 | 0.97 | $50.07 | +0.00% | EP |
| 33 | DRUG | Bright Minds Biosciences Inc | NASDAQ | Health Care | $50.69 | $0.96 | 9897% | 5180% | $84.74 | 1.31 | $48.53 | +3.01% | — |
| 34 | ACMR | ACM Research Inc - Class A | NASDAQ | Information Technology | $83.38 | $1.58 | 7914% | 5166% | $85.64 | 1.02 | $37.16 | -0.24% | breakout, EP |
| 35 | ARWR | Arrowhead Pharmaceuticals Inc | NASDAQ | Health Care | $64.19 | $1.24 | 7196% | 5077% | $89.59 | 0.91 | $54.02 | -0.93% | — |
| 36 | ESEA | Euroseas Ltd | NASDAQ | Industrials | $72.42 | $1.41 | 5540% | 5045% | $77.59 | 0.89 | $51.65 | +2.71% | — |
| 37 | AR | Antero Resources Corp | NYSE | Energy | $34.08 | $0.67 | 7120% | 4993% | $39.81 | 1.03 | $31.15 | +0.15% | — |
| 38 | NUTX | Nutex Health Inc | NASDAQ | Health Care | $216.50 | $4.34 | 570176% | 4888% | $220.11 | 0.78 | $83.99 | +1.97% | breakout, coil, EP |
| 39 | IESC | IES Holdings Inc | NASDAQ | Industrials | $339.34 | $7.00 | 5567% | 4744% | $396.98 | 0.73 | $184.09 | +2.78% | coil, EP |
| 40 | ENPH | Enphase Energy Inc | NASDAQ | Information Technology | $33.47 | $0.70 | 47900% | 4681% | $42.30 | 0.94 | $29.90 | +1.98% | — |
| 41 | ARGX | argenx SE | NASDAQ | Health Care | $919.21 | $19.77 | 5258% | 4551% | $1058.90 | 1.00 | $661.85 | -1.79% | — |
| 42 | VRT | Vertiv Holdings Co - Class A | NYSE | Industrials | $252.18 | $5.57 | 6655% | 4428% | $293.84 | 0.80 | $158.77 | +2.46% | coil, EP |
| 43 | MTDR | Matador Resources Company | NYSE | Energy | $53.50 | $1.20 | 6014% | 4358% | $63.17 | 0.94 | $39.72 | +1.02% | — |
| 44 | HUT | Hut 8 Corp | NASDAQ | Financials | $89.63 | $2.03 | 6461% | 4321% | $106.61 | 0.79 | $42.06 | +3.79% | EP |
| 45 | LTM | LATAM Airlines Group SA | NYSE | Industrials | $47.92 | $1.10 | 6124% | 4256% | $57.70 | 1.04 | $45.09 | +0.38% | — |
| 46 | PMTS | CPI Card Group Inc | NASDAQ | Information Technology | $24.86 | $0.58 | 7660% | 4186% | $30.50 | 0.54 | $10.81 | +0.89% | VCP, EP |
| 47 | XPEL | XPEL Inc - Reg S | NASDAQ | Consumer Discretionary | $44.97 | $1.05 | 9557% | 4183% | $51.45 | 0.88 | $36.99 | +0.92% | — |
| 48 | ANET | Arista Networks Inc | NYSE | Information Technology | $207.35 | $5.03 | 4086% | 4024% | $210.50 | 0.76 | $115.42 | +1.40% | breakout, coil, EP |
| 49 | CELH | Celsius Holdings Inc | NASDAQ | Consumer Staples | $26.75 | $0.67 | 14316% | 3912% | $35.34 | 0.87 | $23.56 | -2.41% | — |
| 50 | BELFB | Bel Fuse Inc - Class B | NASDAQ | Information Technology | $257.94 | $6.44 | 5071% | 3905% | $300.64 | 0.95 | $166.41 | +2.32% | EP |
| 51 | SHOP | Shopify Inc - Class A | NASDAQ | Information Technology | $151.39 | $3.79 | 4623% | 3894% | $158.53 | 1.10 | $94.00 | +1.54% | breakout, EP |
| 52 | KRYS | Krystal Biotech Inc | NASDAQ | Health Care | $322.28 | $8.19 | 4517% | 3835% | $371.47 | 0.94 | $235.61 | -0.93% | — |
| 53 | MDGL | Madrigal Pharmaceuticals Inc | NASDAQ | Health Care | $499.40 | $12.81 | 4606% | 3798% | $546.93 | 0.91 | $416.21 | -0.06% | — |
| 54 | PLSE | Pulse Biosciences Inc | NASDAQ | Health Care | $47.90 | $1.23 | 4388% | 3794% | $55.20 | 0.83 | $13.17 | -3.87% | coil, EP |
| 55 | DELL | Dell Technologies Inc - Class C | NYSE | Information Technology | $562.52 | $14.63 | 3921% | 3744% | $588.40 | 0.76 | $110.22 | +3.84% | breakout, coil, EP |
| 56 | POWL | Powell Industries Inc | NASDAQ | Industrials | $196.10 | $5.21 | 6081% | 3664% | $218.73 | 0.83 | $107.33 | +2.89% | coil, EP |
| 57 | RCMT | RCM Technologies Inc | NASDAQ | Industrials | $42.01 | $1.12 | 3652% | 3651% | $42.02 | 0.70 | $17.26 | -0.02% | breakout, coil, EP |
| 58 | SMCI | Super Micro Computer Inc | NASDAQ | Information Technology | $43.69 | $1.17 | 10098% | 3650% | $43.69 | 0.88 | $19.48 | +4.22% | breakout, EP |
| 59 | ATI | ATI Inc | NYSE | Industrials | $192.42 | $5.23 | 4332% | 3579% | $231.78 | 0.91 | $114.75 | +0.67% | EP |
| 60 | LRCX | Lam Research Corp | NASDAQ | Information Technology | $347.49 | $9.46 | 4481% | 3574% | $347.49 | 0.75 | $177.50 | +2.17% | breakout, coil, EP |
| 61 | PSIX | Power Solutions International Inc | NASDAQ | Industrials | $44.85 | $1.25 | 9162% | 3488% | $47.10 | 0.80 | $25.28 | -1.21% | breakout, coil, EP |
| 62 | GME | Gamestop Corporation - Class A | NYSE | Consumer Discretionary | $24.70 | $0.70 | 12311% | 3429% | $25.02 | 1.39 | $17.79 | +2.45% | breakout |
| 63 | SYRE | Spyre Therapeutics Inc | NASDAQ | Health Care | $93.19 | $2.66 | 10271% | 3403% | $108.92 | 1.13 | $28.00 | +3.63% | EP |
| 64 | TQQQ | PROSHARES ULTRAPRO QQQ | NASDAQ | — | $81.01 | $2.34 | 3626% | 3361% | $81.01 | 0.97 | $37.32 | +2.90% | breakout, EP |
| 65 | SM | SM Energy Company | NYSE | Energy | $35.24 | $1.03 | 5178% | 3321% | $41.29 | 1.01 | $17.45 | +0.51% | EP |
| 66 | BELFA | Bel Fuse Inc - Class A | NASDAQ | Information Technology | $209.31 | $6.15 | 4635% | 3303% | $248.02 | 0.91 | $147.12 | +2.73% | — |
| 67 | VIST | Vista Energy S.A.B. de C.V | NYSE | Energy | $64.25 | $1.90 | 4071% | 3282% | $78.95 | 0.90 | $43.71 | -0.59% | — |
| 68 | NVMI | Nova Ltd | NASDAQ | Information Technology | $396.12 | $11.72 | 5068% | 3280% | $420.79 | 0.74 | $329.57 | +2.46% | coil |
| 69 | PRCH | Porch Group Inc - Class A | NASDAQ | Information Technology | $17.31 | $0.53 | 4788% | 3197% | $18.06 | 1.29 | $6.36 | +3.34% | breakout, EP |
| 70 | CRWD | Crowdstrike Holdings Inc - Class A | NASDAQ | Information Technology | $270.04 | $8.25 | 3172% | 3172% | $270.04 | 0.77 | $85.68 | +1.48% | breakout, coil, EP |
| 71 | CHEF | Chefs` Warehouse Inc | NASDAQ | Consumer Staples | $116.42 | $3.60 | 3134% | 3134% | $116.42 | 0.86 | $56.56 | +3.43% | breakout, EP |
| 72 | LITE | Lumentum Holdings Inc | NASDAQ | Information Technology | $1085.42 | $33.60 | 3130% | 3130% | $1085.42 | 0.91 | $317.44 | +3.79% | breakout, EP |
| 73 | VKTX | Viking Therapeutics Inc | NASDAQ | Health Care | $29.94 | $0.93 | 10061% | 3119% | $41.65 | 1.52 | $25.77 | -1.87% | — |
| 74 | IVT | InvenTrust Properties Corp | NYSE | Real Estate | $30.40 | $0.95 | 3766% | 3100% | $34.08 | 1.04 | $27.75 | +0.10% | — |
| 75 | FTNT | Fortinet Inc | NASDAQ | Information Technology | $180.95 | $5.72 | 3062% | 3062% | $180.95 | 0.76 | $73.55 | +1.25% | breakout, coil, EP |

## Notes
- **First cloud run for this backlog** — the file was created fresh in `/workspace/daily-screens/2026-10-03/`. On subsequent Saturday runs, only newly-discovered tickers (gain ≥ 1000% not seen in prior runs) are appended; this run lays down the full 75-row sample.
- The full 200-row scan (rows beyond 75) is preserved in this run's `pattern_study_full.json` (see run log).
- Cross-reference: the peoplewish screener (filter G) uses 14d velocity as primary sort; this backlog is the multi-year analogue.
