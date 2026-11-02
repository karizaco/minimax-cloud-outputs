# peoplewish 1000%-in-10-years — Pattern-Study Backlog

_Long-lived log of US equities that have compounded 1000%+ from their 10-year low
to the most recent close. Maintained by cron #6 stock-screener-pattern-study-backlog
(Saturday weekly). Newly-discovered names are appended each Saturday._

## Methodology

- **Universe:** all symbols in shibui.stock_quotes with at least 1,260 trading days in the
  trailing 10-year window (≥ 5y of data — filters out recent IPOs / SPAC mergers that would
  not have a real 10-yr baseline).
- **Trigger:** `(current_close / 10y_min_close) - 1 >= 10.0` (i.e., 1000%+ from trough).
- **Min close filter:** `min_close_10y >= $0.50` (avoids micro-cap noise that hit 1000% off a sub-penny base).
- **Sort:** current gain from 10y low, descending. Scan cap 200 rows per run; top 100 get shape tags.
- **Security type:** newly-tagged names are restricted to `type = 'Common Stock'`. Leveraged ETNs and
  ETFs inflate a 10-year return mechanically and have no chart shape worth studying, so they are
  excluded from the tag list (the raw scan still records them in the run JSON).
- **Chart-shape tags** (computed on the most recent 60d / 10d window of stock_quotes):
  - `coil` — close within 15% of 60d high AND contraction_ratio (10d range / 60d range) < 0.85
  - `VCP` — Volatility Contraction Pattern: contraction_ratio < 0.65 (10d range < 65% of 60d range)
  - `breakout` — close within 5% of 60d high (close / high_60d ≥ 0.95)
  - `EP` — Extended Play: current close > 50% above YTD low (already in a strong uptrend)
  - `big_day` — most recent trading day moved > 5% (catalyst signal)

## Run manifest

- **Run date (ET):** 2026-10-31 (Saturday weekly cron)
- **Latest shibui data:** 2026-10-30 (T+1 lag vs cron date)
- **Source:** shibui MCP (streamable-http `https://mcp.shibui.finance/mcp`), `stock_data_query`
- **Scan:** 200 rows returned by the 10y scan; 100 shape-tagged
- **Newly tagged this run:** 3 common stocks (already-known names carried forward: 97; new non-equity rows excluded: 0)
- **Cumulative backlog size:** 100
- **Prior backlog source:** pattern-study/peoplewish-1000pct-backlog.md (2026-10-24 run)
- **Source tag:** `_source=mcp`

## Newly tagged entries (2026-10-31 run)

| # | Ticker | Name | Type | Exchange | Sector | Current | 10y Low | Peak Gain | Gain | 60d High | Contraction | YTD Low | Last Day | Tags |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | BBW | Build-A-Bear Workshop Inc. | Common Stock | NYSE | Consumer Discretionary | $27.61 | $1.02 | 7,336% | 2,607% | $40.18 | 0.31 | $23.19 | +0.47% | VCP |
| 2 | PWR | Quanta Services Inc | Common Stock | NYSE | Industrials | $620.73 | $23.80 | 3,199% | 2,508% | $724.80 | 0.63 | $408.36 | -2.27% | VCP, coil, EP |
| 3 | CROX | Crocs Inc | Common Stock | NASDAQ | Consumer Discretionary | $150.52 | $5.94 | 2,940% | 2,434% | $154.05 | 0.81 | $75.13 | +0.17% | breakout, coil, EP |

### Excluded from tagging (non-Common-Stock, 0)

No newly-discovered non-Common-Stock names in this week's top-100. All 11 non-equity rows in the tagged
window (ZCSH, USD, GBTC, ARGX, TECL, LTM, VIST, IVT, SOXL, TQQQ, FNGO) were already known from previous
runs, so nothing new was added to the exclusion ledger.

## Carried forward (first tagged on or before 2026-10-31)

| Ticker | Name | Type | Exchange | Sector | Current | 10y Low | Peak Gain | Gain | 60d High | Contraction | YTD Low | Last Day | Tags | First Tagged |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NVDA | NVIDIA Corp | Common Stock | NASDAQ | Information Technology | $233.95 | $1.63 | 14,330% | 14,220% | $233.95 | 0.86 | $164.27 | +1.34% | breakout | 2026-10-03 |
| CLS | Celestica Inc | Common Stock | NYSE | Information Technology | $387.32 | $2.83 | 16,593% | 13,586% | $387.32 | 1.01 | $244.51 | +3.81% | breakout, EP | 2026-10-03 |
| BE | Bloom Energy Corp - Class A | Common Stock | NYSE | Industrials | $289.15 | $2.67 | 12,853% | 10,730% | $291.25 | 1.08 | $88.86 | +4.17% | breakout, EP | 2026-10-03 |
| AEHR | Aehr Test Systems | Common Stock | NASDAQ | Information Technology | $107.21 | $1.06 | 13,637% | 10,014% | $145.61 | 0.85 | $20.99 | +5.52% | EP, big_day | 2026-10-03 |
| AMD | Advanced Micro Devices Inc | Common Stock | NASDAQ | Information Technology | $633.91 | $6.29 | 9,970% | 9,970% | $633.91 | 0.91 | $188.22 | +2.95% | breakout, EP | 2026-10-03 |
| LEU | Centrus Energy Corp - Class A | Common Stock | NYSE | Energy | $139.27 | $1.44 | 30,178% | 9,572% | $194.78 | 0.66 | $135.75 | +0.12% | — | 2026-10-03 |
| FRHC | Freedom Holding Corp | Common Stock | NASDAQ | Financials | $173.00 | $1.85 | 10,178% | 9,251% | $176.37 | 1.03 | $107.98 | -0.24% | breakout, EP | 2026-10-03 |
| INOD | Innodata Inc | Common Stock | NASDAQ | Industrials | $70.07 | $0.78 | 15,477% | 8,883% | $71.99 | 1.17 | $34.23 | -2.48% | breakout, EP | 2026-10-03 |
| AXSM | Axsome Therapeutics Inc | Common Stock | NASDAQ | Health Care | $179.25 | $2.00 | 12,658% | 8,862% | $220.89 | 1.16 | $152.28 | -1.55% | — | 2026-10-03 |
| USD ⚠ | PROSHARES ULTRA SEMICONDUCTORS | ETF | NYSE | — | $100.98 | $1.16 | 9,683% | 8,601% | $100.98 | 0.88 | $42.56 | +3.29% | breakout, EP | 2026-10-03 |
| CVNA | Carvana Co. - Class A | Common Stock | NYSE | Consumer Discretionary | $63.77 | $0.74 | 12,762% | 8,471% | $75.77 | 1.06 | $54.46 | +1.16% | — | 2026-10-03 |
| CDNA | Caredx Inc | Common Stock | NASDAQ | Health Care | $67.15 | $0.79 | 12,063% | 8,443% | $67.15 | 1.35 | $15.56 | +1.39% | breakout, EP | 2026-10-03 |
| STRL | Sterling Infrastructure Inc | Common Stock | NASDAQ | Industrials | $533.42 | $6.42 | 15,379% | 8,209% | $603.89 | 0.88 | $293.30 | +5.60% | EP, big_day | 2026-10-03 |
| AMR | Alpha Metallurgical Resources Inc | Common Stock | NYSE | Materials | $171.54 | $2.10 | 20,958% | 8,069% | $235.70 | 0.83 | $133.64 | +0.73% | — | 2026-10-03 |
| AAOI | Applied Optoelectronics Inc | Common Stock | NASDAQ | Information Technology | $115.59 | $1.50 | 14,773% | 7,606% | $154.89 | 0.96 | $31.67 | +7.71% | EP, big_day | 2026-10-03 |
| DAVE | Dave Inc - Class A | Common Stock | NASDAQ | Information Technology | $346.57 | $4.54 | 9,968% | 7,525% | $430.16 | 0.89 | $152.21 | +2.06% | EP | 2026-10-03 |
| AXTI | AXT Inc | Common Stock | NASDAQ | Information Technology | $85.87 | $1.16 | 12,040% | 7,303% | $95.97 | 0.90 | $14.62 | +4.96% | EP | 2026-10-03 |
| GBTC ⚠ | Grayscale Investments LLC | ETF | NYSE | — | $65.11 | $0.95 | 10,315% | 6,789% | $66.88 | 1.05 | $44.98 | -0.50% | breakout | 2026-10-03 |
| KOD | Kodiak Sciences Inc | Common Stock | NASDAQ | Health Care | $94.45 | $1.40 | 11,648% | 6,646% | $98.46 | 1.98 | $20.88 | -4.07% | breakout, EP | 2026-10-03 |
| MU | Micron Technology Inc | Common Stock | NASDAQ | Information Technology | $1,074.89 | $16.62 | 7,202% | 6,367% | $1,097.39 | 0.88 | $294.86 | -2.05% | breakout, EP | 2026-10-03 |
| FIX | Comfort Systems USA Inc | Common Stock | NYSE | Industrials | $1,728.01 | $27.21 | 7,495% | 6,251% | $1,881.18 | 0.84 | $938.40 | +2.53% | coil, EP | 2026-10-03 |
| MOD | Modine Manufacturing Company | Common Stock | NYSE | Consumer Discretionary | $178.20 | $2.98 | 10,198% | 5,880% | $216.75 | 1.11 | $111.18 | -5.82% | EP, big_day | 2026-10-03 |
| TRGP | Targa Resources Corp | Common Stock | NYSE | Energy | $281.74 | $4.73 | 6,290% | 5,856% | $302.25 | 1.00 | $173.57 | +0.87% | EP | 2026-10-03 |
| DAC | Danaos Corporation | Common Stock | NYSE | Industrials | $165.15 | $2.78 | 5,841% | 5,841% | $165.15 | 1.08 | $93.34 | +2.11% | breakout, EP | 2026-10-03 |
| WGS | GeneDx Holdings Corp - Class A | Common Stock | NASDAQ | Health Care | $73.09 | $1.24 | 68,588% | 5,794% | $104.95 | 1.32 | $32.21 | +3.00% | EP | 2026-10-03 |
| CAMT | Camtek Ltd | Common Stock | NASDAQ | Information Technology | $165.19 | $2.83 | 7,231% | 5,737% | $174.20 | 0.88 | $110.55 | +7.41% | big_day | 2026-10-03 |
| SOXL ⚠ | DIREXION DAILY SEMICONDUCTOR BULL 3X SHARES | ETF | NYSE | — | $163.71 | $2.84 | 10,505% | 5,673% | $163.71 | 0.89 | $39.52 | +6.52% | breakout, EP, big_day | 2026-10-03 |
| TECL ⚠ | DIREXION DAILY TECHNOLOGY BULL 3X SHARES | ETF | NYSE | — | $246.31 | $4.30 | 6,254% | 5,627% | $246.31 | 0.89 | $75.16 | +2.92% | breakout, EP | 2026-10-03 |
| ATLC | Atlanticus Holdings Corp | Common Stock | NASDAQ | Financials | $91.89 | $1.63 | 6,758% | 5,537% | $111.79 | 0.75 | $47.50 | +2.91% | EP | 2026-10-03 |
| NTRA | Natera Inc | Common Stock | NASDAQ | Health Care | $410.35 | $7.50 | 5,427% | 5,371% | $414.52 | 0.97 | $181.00 | +0.46% | breakout, EP | 2026-10-03 |
| SITM | SiTime Corp | Common Stock | NASDAQ | Information Technology | $709.44 | $13.00 | 6,834% | 5,357% | $749.44 | 0.96 | $305.21 | +4.50% | EP | 2026-10-03 |
| MNPR | Monopar Therapeutics Inc | Common Stock | NASDAQ | Health Care | $77.97 | $1.45 | 9,233% | 5,290% | $123.84 | 0.97 | $50.07 | +0.00% | EP | 2026-10-03 |
| DRUG | Bright Minds Biosciences Inc | Common Stock | NASDAQ | Health Care | $50.69 | $0.96 | 9,897% | 5,180% | $84.74 | 1.31 | $48.53 | +3.01% | — | 2026-10-03 |
| ACMR | ACM Research Inc - Class A | Common Stock | NASDAQ | Information Technology | $83.38 | $1.58 | 7,914% | 5,166% | $85.64 | 1.02 | $37.16 | -0.24% | breakout, EP | 2026-10-03 |
| ARWR | Arrowhead Pharmaceuticals Inc | Common Stock | NASDAQ | Health Care | $64.19 | $1.24 | 7,196% | 5,077% | $89.59 | 0.91 | $54.02 | -0.93% | — | 2026-10-03 |
| ESEA | Euroseas Ltd | Common Stock | NASDAQ | Industrials | $72.42 | $1.41 | 5,540% | 5,045% | $77.59 | 0.89 | $51.65 | +2.71% | — | 2026-10-03 |
| AR | Antero Resources Corp | Common Stock | NYSE | Energy | $34.08 | $0.67 | 7,120% | 4,993% | $39.81 | 1.03 | $31.15 | +0.15% | — | 2026-10-03 |
| NUTX | Nutex Health Inc | Common Stock | NASDAQ | Health Care | $216.50 | $4.34 | 570,176% | 4,888% | $220.11 | 0.78 | $83.99 | +1.97% | breakout, coil, EP | 2026-10-03 |
| IESC | IES Holdings Inc | Common Stock | NASDAQ | Industrials | $339.34 | $7.00 | 5,567% | 4,744% | $396.98 | 0.73 | $184.09 | +2.78% | coil, EP | 2026-10-03 |
| ENPH | Enphase Energy Inc | Common Stock | NASDAQ | Information Technology | $33.47 | $0.70 | 47,900% | 4,681% | $42.30 | 0.94 | $29.90 | +1.98% | — | 2026-10-03 |
| ARGX ⚠ | argenx SE | ADR | NASDAQ | Health Care | $919.21 | $19.77 | 5,258% | 4,551% | $1,058.90 | 1.00 | $661.85 | -1.79% | — | 2026-10-03 |
| VRT | Vertiv Holdings Co - Class A | Common Stock | NYSE | Industrials | $252.18 | $5.57 | 6,655% | 4,428% | $293.84 | 0.80 | $158.77 | +2.46% | coil, EP | 2026-10-03 |
| MTDR | Matador Resources Company | Common Stock | NYSE | Energy | $53.50 | $1.20 | 6,014% | 4,358% | $63.17 | 0.94 | $39.72 | +1.02% | — | 2026-10-03 |
| HUT | Hut 8 Corp | Common Stock | NASDAQ | Financials | $89.63 | $2.03 | 6,461% | 4,321% | $106.61 | 0.79 | $42.06 | +3.79% | EP | 2026-10-03 |
| LTM ⚠ | LATAM Airlines Group SA | ADR | NYSE | Industrials | $47.92 | $1.10 | 6,124% | 4,256% | $57.70 | 1.04 | $45.09 | +0.38% | — | 2026-10-03 |
| PMTS | CPI Card Group Inc | Common Stock | NASDAQ | Information Technology | $24.86 | $0.58 | 7,660% | 4,186% | $30.50 | 0.54 | $10.81 | +0.89% | VCP, EP | 2026-10-03 |
| XPEL | XPEL Inc - Reg S | Common Stock | NASDAQ | Consumer Discretionary | $44.97 | $1.05 | 9,557% | 4,183% | $51.45 | 0.88 | $36.99 | +0.92% | — | 2026-10-03 |
| ANET | Arista Networks Inc | Common Stock | NYSE | Information Technology | $207.35 | $5.03 | 4,086% | 4,024% | $210.50 | 0.76 | $115.42 | +1.40% | breakout, coil, EP | 2026-10-03 |
| CELH | Celsius Holdings Inc | Common Stock | NASDAQ | Consumer Staples | $26.75 | $0.67 | 14,316% | 3,912% | $35.34 | 0.87 | $23.56 | -2.41% | — | 2026-10-03 |
| BELFB | Bel Fuse Inc - Class B | Common Stock | NASDAQ | Information Technology | $257.94 | $6.44 | 5,071% | 3,905% | $300.64 | 0.95 | $166.41 | +2.32% | EP | 2026-10-03 |
| SHOP | Shopify Inc - Class A | Common Stock | NASDAQ | Information Technology | $151.39 | $3.79 | 4,623% | 3,894% | $158.53 | 1.10 | $94.00 | +1.54% | breakout, EP | 2026-10-03 |
| KRYS | Krystal Biotech Inc | Common Stock | NASDAQ | Health Care | $322.28 | $8.19 | 4,517% | 3,835% | $371.47 | 0.94 | $235.61 | -0.93% | — | 2026-10-03 |
| MDGL | Madrigal Pharmaceuticals Inc | Common Stock | NASDAQ | Health Care | $499.40 | $12.81 | 4,606% | 3,798% | $546.93 | 0.91 | $416.21 | -0.06% | — | 2026-10-03 |
| PLSE | Pulse Biosciences Inc | Common Stock | NASDAQ | Health Care | $47.90 | $1.23 | 4,388% | 3,794% | $55.20 | 0.83 | $13.17 | -3.87% | coil, EP | 2026-10-03 |
| DELL | Dell Technologies Inc - Class C | Common Stock | NYSE | Information Technology | $562.52 | $14.63 | 3,921% | 3,744% | $588.40 | 0.76 | $110.22 | +3.84% | breakout, coil, EP | 2026-10-03 |
| POWL | Powell Industries Inc | Common Stock | NASDAQ | Industrials | $196.10 | $5.21 | 6,081% | 3,664% | $218.73 | 0.83 | $107.33 | +2.89% | coil, EP | 2026-10-03 |
| RCMT | RCM Technologies Inc | Common Stock | NASDAQ | Industrials | $42.01 | $1.12 | 3,652% | 3,651% | $42.02 | 0.70 | $17.26 | -0.02% | breakout, coil, EP | 2026-10-03 |
| SMCI | Super Micro Computer Inc | Common Stock | NASDAQ | Information Technology | $43.69 | $1.17 | 10,098% | 3,650% | $43.69 | 0.88 | $19.48 | +4.22% | breakout, EP | 2026-10-03 |
| ATI | ATI Inc | Common Stock | NYSE | Industrials | $192.42 | $5.23 | 4,332% | 3,579% | $231.78 | 0.91 | $114.75 | +0.67% | EP | 2026-10-03 |
| LRCX | Lam Research Corp | Common Stock | NASDAQ | Information Technology | $347.49 | $9.46 | 4,481% | 3,574% | $347.49 | 0.75 | $177.50 | +2.17% | breakout, coil, EP | 2026-10-03 |
| PSIX | Power Solutions International Inc | Common Stock | NASDAQ | Industrials | $44.85 | $1.25 | 9,162% | 3,488% | $47.10 | 0.80 | $25.28 | -1.21% | breakout, coil, EP | 2026-10-03 |
| GME | Gamestop Corporation - Class A | Common Stock | NYSE | Consumer Discretionary | $24.70 | $0.70 | 12,311% | 3,429% | $25.02 | 1.39 | $17.79 | +2.45% | breakout | 2026-10-03 |
| SYRE | Spyre Therapeutics Inc | Common Stock | NASDAQ | Health Care | $93.19 | $2.66 | 10,271% | 3,403% | $108.92 | 1.13 | $28.00 | +3.63% | EP | 2026-10-03 |
| TQQQ ⚠ | PROSHARES ULTRAPRO QQQ | ETF | NASDAQ | — | $81.01 | $2.34 | 3,626% | 3,361% | $81.01 | 0.97 | $37.32 | +2.90% | breakout, EP | 2026-10-03 |
| SM | SM Energy Company | Common Stock | NYSE | Energy | $35.24 | $1.03 | 5,178% | 3,321% | $41.29 | 1.01 | $17.45 | +0.51% | EP | 2026-10-03 |
| BELFA | Bel Fuse Inc - Class A | Common Stock | NASDAQ | Information Technology | $209.31 | $6.15 | 4,635% | 3,303% | $248.02 | 0.91 | $147.12 | +2.73% | — | 2026-10-03 |
| VIST ⚠ | Vista Energy S.A.B. de C.V | ADR | NYSE | Energy | $64.25 | $1.90 | 4,071% | 3,282% | $78.95 | 0.90 | $43.71 | -0.59% | — | 2026-10-03 |
| NVMI | Nova Ltd | Common Stock | NASDAQ | Information Technology | $396.12 | $11.72 | 5,068% | 3,280% | $420.79 | 0.74 | $329.57 | +2.46% | coil | 2026-10-03 |
| PRCH | Porch Group Inc - Class A | Common Stock | NASDAQ | Information Technology | $17.31 | $0.53 | 4,788% | 3,197% | $18.06 | 1.29 | $6.36 | +3.34% | breakout, EP | 2026-10-03 |
| PLTR | Palantir Technologies Inc - Class A | Common Stock | NASDAQ | Information Technology | $196.75 | $6.00 | 3,384% | 3,179% | $209.05 | 1.37 | $106.37 | +0.29% | EP | 2026-10-24 |
| CRWD | Crowdstrike Holdings Inc - Class A | Common Stock | NASDAQ | Information Technology | $270.04 | $8.25 | 3,172% | 3,172% | $270.04 | 0.77 | $85.68 | +1.48% | breakout, coil, EP | 2026-10-03 |
| OVV | Ovintiv Inc | Common Stock | NYSE | Energy | $72.27 | $2.22 | 3,155% | 3,155% | $72.27 | 1.12 | $36.81 | +4.29% | breakout, EP | 2026-10-24 |
| CHEF | Chefs` Warehouse Inc | Common Stock | NASDAQ | Consumer Staples | $116.42 | $3.60 | 3,134% | 3,134% | $116.42 | 0.86 | $56.56 | +3.43% | breakout, EP | 2026-10-03 |
| LITE | Lumentum Holdings Inc | Common Stock | NASDAQ | Information Technology | $1,085.42 | $33.60 | 3,130% | 3,130% | $1,085.42 | 0.91 | $317.44 | +3.79% | breakout, EP | 2026-10-03 |
| VKTX | Viking Therapeutics Inc | Common Stock | NASDAQ | Health Care | $29.94 | $0.93 | 10,061% | 3,119% | $41.65 | 1.52 | $25.77 | -1.87% | — | 2026-10-03 |
| IVT ⚠ | InvenTrust Properties Corp | REIT | NYSE | Real Estate | $30.40 | $0.95 | 3,766% | 3,100% | $34.08 | 1.04 | $27.75 | +0.10% | — | 2026-10-03 |
| FTNT | Fortinet Inc | Common Stock | NASDAQ | Information Technology | $180.95 | $5.72 | 3,062% | 3,062% | $180.95 | 0.76 | $73.55 | +1.25% | breakout, coil, EP | 2026-10-03 |
| TSLA | Tesla Inc | Common Stock | NASDAQ | Consumer Discretionary | $372.22 | $11.93 | 4,006% | 3,020% | $386.47 | 1.16 | $297.38 | -0.63% | breakout | 2026-10-24 |
| MEDP | Medpace Holdings Inc | Common Stock | NASDAQ | Health Care | $669.20 | $22.18 | 2,917% | 2,917% | $669.20 | 1.43 | $373.00 | +2.33% | breakout, EP | 2026-10-24 |
| PTGX | Protagonist Therapeutics Inc | Common Stock | NASDAQ | Health Care | $138.43 | $4.69 | 3,282% | 2,852% | $151.50 | 1.11 | $77.00 | -0.79% | EP | 2026-10-24 |
| RYTM | Rhythm Pharmaceuticals Inc | Common Stock | NASDAQ | Health Care | $89.27 | $3.12 | 3,670% | 2,761% | $113.35 | 0.89 | $74.50 | -1.79% | — | 2026-10-24 |
| APP | Applovin Corp - Class A | Common Stock | NASDAQ | Information Technology | $260.25 | $9.30 | 7,788% | 2,698% | $334.24 | 0.96 | $258.32 | -1.52% | — | 2026-10-24 |
| HRTG | Heritage Insurance Holdings Inc | Common Stock | NYSE | Financials | $36.82 | $1.32 | 2,756% | 2,689% | $37.70 | 1.10 | $20.48 | -2.33% | breakout, EP | 2026-10-24 |
| KINS | Kingstone Cos. Inc | Common Stock | NASDAQ | Financials | $20.04 | $0.72 | 2,914% | 2,683% | $20.22 | 0.96 | $13.83 | -0.74% | breakout | 2026-10-24 |
| BTU | Peabody Energy Corp New | Common Stock | NYSE | Energy | $22.89 | $0.83 | 5,610% | 2,654% | $29.69 | 1.07 | $20.06 | +2.05% | — | 2026-10-24 |
| MPC | Marathon Petroleum Corp | Common Stock | NYSE | Energy | $457.22 | $16.62 | 2,818% | 2,651% | $484.92 | 0.98 | $162.33 | -0.45% | EP | 2026-10-24 |
| FET | Forum Energy Technologies Inc | Common Stock | NYSE | Energy | $87.17 | $3.20 | 15,088% | 2,624% | $87.37 | 1.39 | $35.70 | +6.88% | breakout, EP, big_day | 2026-10-24 |
| FTAI | FTAI Aviation Ltd - Class A | Common Stock | NASDAQ | Industrials | $154.37 | $5.67 | 5,368% | 2,623% | $201.27 | 1.42 | $146.48 | -1.99% | — | 2026-10-24 |
| TPC | Tutor Perini Corp | Common Stock | NYSE | Industrials | $76.86 | $2.91 | 3,306% | 2,541% | $91.95 | 1.10 | $66.77 | -0.03% | — | 2026-10-24 |
| ASTH | Astrana Health Inc. | Common Stock | NASDAQ | Health Care | $37.45 | $1.50 | 7,873% | 2,400% | $39.60 | 0.86 | $18.08 | -1.47% | EP | 2026-10-24 |
| CNR | Core Natural Resources Inc | Common Stock | NYSE | Industrials | $92.10 | $3.69 | 3,513% | 2,396% | $102.66 | 1.04 | $77.50 | +4.24% | — | 2026-10-24 |
| AAMI | Acadian Asset Management Inc. | Common Stock | NYSE | Financials | $92.35 | $3.73 | 2,509% | 2,376% | $97.31 | 0.87 | $45.85 | -0.47% | EP | 2026-10-24 |
| ETON | Eton Pharmaceuticals Inc | Common Stock | NASDAQ | Health Care | $50.00 | $2.02 | 3,090% | 2,375% | $63.05 | 0.98 | $14.27 | -0.04% | EP | 2026-10-24 |
| COGT | Cogent Biosciences Inc | Common Stock | NASDAQ | Health Care | $31.21 | $1.28 | 5,141% | 2,338% | $37.09 | 0.95 | $27.74 | -0.32% | — | 2026-10-24 |
| THC | Tenet Healthcare Corp | Common Stock | NYSE | Health Care | $268.45 | $11.01 | 2,450% | 2,338% | $275.13 | 0.93 | $157.58 | -0.81% | breakout, EP | 2026-10-24 |
| EAT | Brinker International Inc | Common Stock | NYSE | Consumer Discretionary | $182.70 | $7.62 | 3,232% | 2,298% | $248.70 | 1.01 | $124.96 | -3.90% | — | 2026-10-24 |
| RRC | Range Resources Corp | Common Stock | NYSE | Energy | $45.52 | $1.94 | 2,356% | 2,246% | $45.52 | 1.15 | $32.68 | +3.78% | breakout | 2026-10-24 |

## Notes
- Rows in **Carried forward** are frozen at the values they carried when first tagged — they are a discovery ledger, not a live quote sheet. Re-scan for live values via the daily sweep.
- 3 of the 89 shape-tagged common stocks were new this week; 86 were already in the backlog and are not duplicated; 0 new non-equity names were excluded.
- Full 200-row scan (including untagged ranks 101-200) is preserved in `peoplewish-backlog-run-full.json` in this directory.
- Cross-reference: the peoplewish screener (filter G) uses 14d velocity as primary sort; this backlog is the multi-year analogue.
- Market note: the 10y-trough basis means the 1000% set is sensitive to drawdown. A name dropping 50% off its high can fall out of the top ranks without ever leaving the backlog.
- Backlog maturity note: the discovery rate has fallen from 22 new names (2026-10-24) to 3 (2026-10-31) as the 10-year universe saturates — 86 of the 100 tagged slots are now names already known.
- ⚠ = tagged before the Common-Stock filter was applied. The 9 legacy rows are ETFs / ADRs / a REIT and are retained for ledger continuity but should be ignored for stock-pattern research: USD, GBTC, SOXL, TECL, ARGX, LTM, TQQQ, VIST, IVT.

## Source health

| Source | Query / URL | Status | Result |
|---|---|---|---|
| shibui MCP (`stock_data_query` via mcp_bridge.py) | 10y scan over `shibui.stock_quotes` + `shibui.general_info` + `shibui.valuation` | ok | 200 rows scanned, 100 shape-tagged, `_source=mcp` |
| shibui MCP (date resolve) | `SELECT MAX(date) FROM shibui.stock_quotes` | ok | 2026-10-30 (T+1 lag vs cron date 2026-10-31) |
| Finviz fallback | not invoked | n/a | primary path succeeded — no fallback chain entered |
| web_search / web_fetch | not invoked | n/a | not needed; no MCP errors to recover from |
