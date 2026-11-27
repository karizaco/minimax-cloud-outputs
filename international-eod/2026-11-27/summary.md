# Cron #05 eod-international-daily — Friday, 27 November 2026

## TL;DR

- **Global equities ended the bruised month with a broad relief rally across all 16 boards.** Every regional index closed higher — the **Nikkei 225 +2.11% to 58,711.11** led the European and Asian sessions, the **S&P/ASX 200 +0.80% to 8,833.60** (its best week since August), the **STOXX Europe 600 +1.08% to 643.85** and the **S&P/TSX Composite +1.20% to 34,839.87** — with **4,221 names published** across the 16 per-region CSVs, up 0.5% on Wednesday's 4,243 and in line with the archive's normal range. The trigger was the return of risk appetite to the beaten-down AI and semiconductor complex after the Thanksgiving holiday lull, with China's Shanghai Composite +3.73% on Beijing's pledge of stronger market support (Reuters; AP; ABC News live blog, 27 Nov).
- **The one consequential move was Japan's semiconductor-equipment complex, and a US trader can reach most of it.** The Nikkei added 1,211.95 points with **Advantest +7.07%** (ADR) the largest single contributor, followed by **Kioxia +8.86%** (OTC), **Tokyo Electron +4.43%**, **SCREEN +8.70%** (OTC), **IBIDEN +9.68%** (OTC), **Taiyo Yuden +8.63%** (ADR), **SUMCO +9.81%** (OTC) and **Furukawa Electric +9.79%** (ADR) — buybacks and short covering in AI names after Wednesday's rout (Kabutan, 27 Nov). The second-largest wave was **Canada's gold and silver miners, all 29 US-reachable**: **Skeena +9.51%** (NYSE), **Aya Gold & Silver +9.48%** (NASDAQ), **AbraSilver +9.31%** (OTC), **Endeavour Silver +9.02%** (NYSE), **Eldorado +7.73%** (NYSE), **B2Gold +7.57%** (NYSE), **First Majestic +6.39%** (NYSE), **Pan American +6.19%** (NYSE), **IAMGOLD +6.07%** (NYSE) and **Agnico Eagle +5.15%** (NYSE), on **gold +4.1% to $3,681.90/oz and silver +10.4% to $44.22/oz** (Dow Jones, 27 Nov).
- **The caveat that changes how to read it: `market_cap` is in USD while `open`/`high`/`low`/`close` are in the listing currency** (the `currency` column says which), and two further facts sit on top of the numbers. First, **the archive has no 2026-11-26 international session** — the routine's US-holiday gate declined that fire for Thanksgiving — so the prior-session anchor was reconstructed from that session's own daily bars; without it, 460 ordinary 26 Nov moves read as stale venue prints and the Taiwan file lost 299 rows. Second, **the Taiwan session was directionless under a flat index** — the TAIEX added only 0.40% while 639 names fell against 451 risers, and Taiwan's +/-10% prints are limit prices, not calculated moves (CNA, 27 Nov).

## Market context

### Coverage

| Region | Venues | Universe | Unique instruments | Written | Floor (USD) | Excluded: no cap | Excluded: below floor | Excluded: below volume | Excluded: issuer unresolved | Excluded: cap mismatch | Carry-over rows | Off-official rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| au | 1 | 1541 | 1541 | 293 | $300M + vol >= 100,000 | 4 | 1221 | 22 | 1 | 0 | 2 | 0 |
| jp | 3 | 3889 | 3869 | 1349 | $300M | 3 | 2516 | 0 | 1 | 0 | 0 | 0 |
| tw | 2 | 2347 | 2347 | 808 | $200M | 57 | 1482 | 0 | 0 | 0 | 2 | 0 |
| ca | 3 | 4274 | 2721 | 608 | $200M | 66 | 1921 | 0 | 126 | 0 | 26 | 0 |
| eu-de | 1 | 4282 | 711 | 113 | $300M + vol >= 50,000 | 4 | 401 | 193 | 0 | 0 | 0 | 0 |
| eu-fr | 1 | 544 | 544 | 260 | $100M | 1 | 283 | 0 | 0 | 0 | 6 | 0 |
| eu-it | 1 | 377 | 377 | 177 | $100M | 2 | 198 | 0 | 0 | 0 | 4 | 0 |
| eu-es | 1 | 230 | 229 | 133 | $100M | 24 | 72 | 0 | 0 | 0 | 18 | 1 |
| eu-nl | 1 | 77 | 77 | 55 | $100M | 0 | 22 | 0 | 0 | 0 | 0 | 0 |
| eu-be | 1 | 101 | 101 | 75 | $100M | 1 | 25 | 0 | 0 | 0 | 0 | 0 |
| eu-at | 1 | 66 | 66 | 50 | $100M | 2 | 14 | 0 | 0 | 0 | 6 | 0 |
| eu-pt | 1 | 30 | 30 | 26 | $50M | 0 | 4 | 0 | 0 | 0 | 1 | 0 |
| eu-ie | 1 | 19 | 19 | 16 | $200M | 0 | 3 | 0 | 0 | 0 | 0 | 0 |
| eu-fi | 1 | 189 | 189 | 101 | $100M | 4 | 84 | 0 | 0 | 0 | 0 | 0 |
| eu-dk | 1 | 133 | 133 | 75 | $100M | 1 | 57 | 0 | 0 | 0 | 1 | 0 |
| eu-gr | 1 | 128 | 128 | 82 | $50M | 1 | 45 | 0 | 0 | 0 | 1 | 0 |
| **total** | | 18227 | 13082 | **4221** | | 170 | 8348 | 215 | 128 | 0 | 67 | 1 |

The exclusion counts are the per-reason counts in `_excluded.json`, not estimates, and the reconciliation identity `unique_instruments == written + sum(excluded)` holds for every region. Written rows are 4,221 against 4,243 on 25 November (-0.5%), inside the archive's normal band, and the 67 carry-over rows match the prior session's 66.

### Index levels

| Region | Index | Close | Change | Session date | Source |
|---|---|---|---|---|---|
| au | S&P/ASX 200 | 8,833.60 | +69.80 / +0.80% | 2026-11-27 | SP:XJO; Yahoo ^AXJO 8,833.5996 (26 Nov 8,763.7998) — MarketIndex, ShareTrader, Ticker & Price and the ABC News live blog all report 8,833.6, up 69.8 points or 0.80%, the best week since August |
| jp | Nikkei 225 | 58,711.11 | +1,211.95 / +2.11% | 2026-11-27 | TVC:NI225 — Kabutan and Ticker & Price report the close at 58,711.11, up 1,211.95 points or 2.11%, with Advantest the largest contributor |
| jp | TOPIX | 3,815.20 | +64.80 / +1.73% | 2026-11-27 | TSE:TOPIX — note.com and TradingView report 3,815.20, up 64.80 points or 1.73% |
| tw | TAIEX | 39,308.08 | +156.27 / +0.40% | 2026-11-27 | TWSE:IX0001; Yahoo ^TWII 39,151.81 on 26 Nov — CNA / Focus Taiwan reports the close at 39,308.08, up 156.27 points or 0.40%, on a range of 38,890.53-39,495.41, with 20 limit-ups and 5 limit-downs |
| ca | S&P/TSX Composite | 34,839.87 | +412.99 / +1.20% | 2026-11-27 | TSX:TSX; Yahoo ^GSPTSE 34,839.8711 — Reuters reports the index 0.71% higher at 34,671.34 by 10:03 ET on miners and tech; MarketScreener's delayed print reads 34,845.93 (+1.22%) |
| eu-de | DAX | 25,441.24 | +225.72 / +0.90% | 2026-11-27 | XETR:DAX; Yahoo ^GDAXI 25,441.2402 — the DAX added 225.72 points with chipmakers leading the AI rebound |
| eu-fr | CAC 40 | 8,156.09 | +47.35 / +0.58% | 2026-11-27 | EURONEXT:PX1; Yahoo ^FCHI 8,156.0898 |
| eu-it | FTSE MIB | 49,275.60 | +913.25 / +1.89% | 2026-11-27 | FTSE:FTSEMIB |
| eu-es | IBEX 35 | 19,386.60 | +328.70 / +1.72% | 2026-11-27 | BME:IBC; Yahoo ^IBEX 19,386.5996 |
| eu-nl | AEX | 1,096.67 | +13.41 / +1.24% | 2026-11-27 | EURONEXT:AEX; Yahoo ^AEX 1,096.67 |
| eu-be | BEL 20 | 5,992.96 | +63.52 / +1.07% | 2026-11-27 | EURONEXT:BEL20; Yahoo ^BFX 5,992.96 |
| eu-at | ATX | 6,225.96 | +120.40 / +1.97% | 2026-11-27 | VIE:ATX; Yahoo ^ATX 6,225.96 |
| eu-pt | PSI 20 | 9,489.66 | +112.62 / +1.20% | 2026-11-27 | EURONEXT:PSI20 |
| eu-ie | ISEQ | 14,492.50 | +108.39 / +0.75% | 2026-11-27 | EURONEXT:ISEQ; Yahoo ^ISEQ 14,492.50 |
| eu-fi | OMX Helsinki 25 | 6,059.73 | +65.00 / +1.08% | 2026-11-27 | OMXHEX:OMXH25 |
| eu-dk | OMX Copenhagen 20 | 1,651.29 | +16.54 / +1.01% | 2026-11-27 | OMXCOP:OMXC20; Yahoo ^OMXC20 1,651.2852 |
| eu-gr | ATHEX General | 2,512.83 | +32.89 / +1.33% | 2026-11-27 | Euronext Athens' own print, via euro2day (27 Nov, 17:41) and ekathimerini: close 2,512.83, up 32.89 points or 1.33% on Thursday's 2,479.94, on a high of 2,517.99 (+1.53%) |
| * | STOXX Europe 600 | 643.85 | +6.87 / +1.08% | 2026-11-27 | STOXX:SXXP; Yahoo ^STOXX 643.85 — Reuters had it 1% higher at 643.52 by 09:33 GMT, its best level in a week and its sharpest gain since mid-May |

### Regional breadth

| Region | Rows | Median | Up / down / flat | Min | Max |
|---|---|---|---|---|---|
| au | 293 | +0.99% | 202 / 72 / 19 | -50.00% | +4250.00% |
| jp | 1349 | +0.77% | 826 / 493 / 30 | -7.31% | +15.87% |
| tw | 808 | -0.71% | 224 / 524 / 60 | -10.00% | +16.60% |
| ca | 608 | +0.56% | 418 / 119 / 71 | -5.05% | +15.22% |
| eu-de | 113 | +0.80% | 86 / 23 / 4 | -3.24% | +9.18% |
| eu-fr | 260 | +0.25% | 139 / 85 / 36 | -6.25% | +18.13% |
| eu-it | 177 | +0.69% | 114 / 46 / 17 | -7.97% | +6.00% |
| eu-es | 133 | +0.57% | 83 / 20 / 30 | -3.70% | +6.67% |
| eu-nl | 55 | +1.10% | 45 / 8 / 2 | -9.65% | +8.10% |
| eu-be | 75 | +0.76% | 49 / 22 / 4 | -2.97% | +8.68% |
| eu-at | 50 | +0.34% | 27 / 20 / 3 | -4.90% | +7.91% |
| eu-pt | 26 | +0.38% | 17 / 4 / 5 | -6.63% | +2.45% |
| eu-ie | 16 | +0.67% | 10 / 5 / 1 | -3.89% | +1.70% |
| eu-fi | 101 | +0.85% | 66 / 29 / 6 | -2.24% | +8.79% |
| eu-dk | 75 | +0.28% | 44 / 26 / 5 | -2.07% | +7.60% |
| eu-gr | 82 | +0.84% | 57 / 13 / 12 | -10.62% | +5.71% |

The index move and the typical name disagree in several places: **Canada's index rose 1.20% on a median name of +0.56%**, because the move was a metals bid concentrated in a few dozen large miners; **Japan's index rose 2.11% on a median name of +0.77%**, because the AI complex carried the index weights; and **Taiwan's median name fell 0.71% while its index rose 0.40%**, a directionless session with 639 decliners against 451 risers. The Australian min and max are two artefact rows, not market moves: `ASX:EDO` (a stale change field) and `ASX:EDOO` (an option line) — both are disclosed in the caveats and neither is in any published table.

## Top movers

### au

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `ASX:WTC` | Wisetech Global Ltd. | **+15.08%** | 53.87 AUD | 5,159,418 | $10.41B | OTC | FY27 trading update at the AGM: confident of A$1.48-1.50bn revenue before growth initiatives, CargoWise +11% through October, A$64m e2open cost savings; closed A$53.87 (+15.1%) (ShareTrader, Ticker & Price, 27 Nov) |
| `ASX:NEU` | Neuren Pharmaceuticals Limited | **-12.15%** | 18.73 AUD | 908,264 | $1.80B | none | FDA Type B End-of-Phase-2 feedback on NNZ-2591 in Pitt Hopkins syndrome — the regulator wants a placebo-controlled Phase 3 the company says is not feasible; resumed from a halt, closed A$18.73 (-12.1%) (Capital Brief; ABC News live blog; MarketIndex, 27 Nov) |
| `ASX:BVS` | Bravura Solutions Limited | **+7.72%** | 3.63 AUD | 1,980,095 | $1.01B | none | no company-specific release found — ASX materials bid on a mid-session 6% spike in copper futures, with gold miners and resources joining the advance (MarketIndex Evening Wrap, 27 Nov) |
| `ASX:MI6` | Minerals 260 Limited | **+7.52%** | 0.715 AUD | 7,205,439 | $1.14B | OTC | no company-specific release found — ASX materials bid on a mid-session 6% spike in copper futures, with gold miners and resources joining the advance (MarketIndex Evening Wrap, 27 Nov) |
| `ASX:LTR` | Liontown Limited | **+7.48%** | 0.575 AUD | 26,754,787 | $1.14B | OTC | no company-specific release found — ASX materials bid on a mid-session 6% spike in copper futures, with gold miners and resources joining the advance (MarketIndex Evening Wrap, 27 Nov) |
| `ASX:SRL` | Sunrise Energy Metals Limited | **+7.35%** | 10.66 AUD | 744,926 | $1.14B | OTC | no company-specific release found — ASX materials bid on a mid-session 6% spike in copper futures, with gold miners and resources joining the advance (MarketIndex Evening Wrap, 27 Nov) |
| `ASX:OBM` | Ora Banda Mining Ltd. | **+6.77%** | 1.34 AUD | 6,513,022 | $1.62B | OTC | no company-specific release found — ASX materials bid on a mid-session 6% spike in copper futures, with gold miners and resources joining the advance (MarketIndex Evening Wrap, 27 Nov) |
| `ASX:PDN` | Paladin Energy Ltd | **+6.67%** | 6.72 AUD | 4,915,346 | $2.17B | OTC | no company-specific release found — ASX materials bid on a mid-session 6% spike in copper futures, with gold miners and resources joining the advance (MarketIndex Evening Wrap, 27 Nov) |
| `ASX:GMD` | Genesis Minerals Limited | **+6.56%** | 6.82 AUD | 9,019,074 | $5.02B | OTC | no company-specific release found — ASX materials bid on a mid-session 6% spike in copper futures, with gold miners and resources joining the advance (MarketIndex Evening Wrap, 27 Nov) |

### jp

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `TSE:7826` | Furuya Metal Co., Ltd. | **+13.35%** | 8320 JPY | 433,700 | $1.15B | none | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:6777` | santec Holdings Corporation | **+12.86%** | 16940 JPY | 200,200 | $1.11B | none | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:6526` | Socionext Inc. | **+12.56%** | 1662 JPY | 8,662,500 | $1.67B | none | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:6871` | Micronics Japan Co., Ltd. | **+12.34%** | 9659 JPY | 1,786,600 | $2.07B | none | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:6787` | Meiko Electronics Co., Ltd. | **+12.24%** | 9900 JPY | 3,015,500 | $2.90B | none | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:6508` | Meidensha Corporation | **+12.23%** | 6881 JPY | 753,000 | $1.74B | none | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:5706` | Mitsui Kinzoku Co., Ltd. | **+11.53%** | 1238.5 JPY | 16,068,500 | $4.00B | ADR | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:6622` | Daihen Corporation | **+10.54%** | 1983 JPY | 1,569,700 | $1.37B | none | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:5805` | SWCC Corporation | **+10.46%** | 1842.5 JPY | 2,638,400 | $1.60B | OTC | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:6920` | Lasertec Corp. | **+9.98%** | 33600 JPY | 5,686,100 | $17.16B | ADR | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:3436` | SUMCO Corporation | **+9.81%** | 2054 JPY | 10,890,700 | $4.11B | OTC | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:5801` | Furukawa Electric Co., Ltd. | **+9.79%** | 1822 JPY | 35,209,900 | $7.32B | ADR | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:4062` | IBIDEN CO., LTD. | **+9.68%** | 5120 JPY | 25,996,300 | $16.56B | OTC | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:4107` | ISE Chemicals Corporation | **+9.33%** | 3925 JPY | 257,100 | $1.15B | none | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:6278` | Union Tool Co. | **+9.30%** | 10110 JPY | 244,100 | $1.13B | none | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:4004` | Resonac Holdings Corporation | **+9.04%** | 12670 JPY | 3,464,200 | $13.69B | OTC | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:5344` | MARUWA CO., LTD. | **+8.99%** | 41450 JPY | 201,700 | $2.94B | none | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:285A` | Kioxia Holdings Corporation | **+8.86%** | 8450 JPY | 218,138,600 | $80.11B | OTC | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:7735` | SCREEN Holdings Co., Ltd | **+8.70%** | 7687 JPY | 2,300,600 | $8.27B | OTC | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:6976` | Taiyo Yuden Co., Ltd. | **+8.63%** | 6659 JPY | 19,375,300 | $5.11B | ADR | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:6324` | Harmonic Drive Systems Inc. | **+8.46%** | 3973 JPY | 1,687,200 | $2.21B | OTC | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:5631` | Japan Steel Works, Ltd. | **+8.45%** | 4854 JPY | 1,495,800 | $2.07B | ADR | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:4186` | Tokyo Ohka Kogyo Co., Ltd. | **+8.37%** | 6966 JPY | 901,400 | $4.99B | OTC | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:5384` | Fujimi Incorporated | **+8.19%** | 2840 JPY | 1,065,000 | $1.25B | none | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:6490` | PILLAR Corporation | **+8.11%** | 10260 JPY | 203,300 | $1.41B | OTC | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:6890` | Ferrotec Corporation | **+8.02%** | 6751 JPY | 2,095,200 | $2.11B | OTC | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:5016` | JX Advanced Metals Corporation | **+7.82%** | 1979.5 JPY | 21,406,100 | $10.91B | ADR | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:6525` | Kokusai Electric Corporation | **+7.64%** | 5143 JPY | 15,330,100 | $7.11B | none | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:6407` | CKD Corporation | **+7.48%** | 3952 JPY | 690,300 | $1.54B | none | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:7013` | IHI Corporation | **+7.46%** | 2391 JPY | 11,365,800 | $14.79B | none | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:6507` | Sinfonia Technology Co., Ltd. | **+7.38%** | 8000 JPY | 246,100 | $1.32B | none | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:6814` | Furuno Electric Co., Ltd. | **+7.23%** | 7120 JPY | 256,800 | $1.31B | none | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:429A` | Tekscend Photomask Corp. | **+7.19%** | 2593 JPY | 791,200 | $1.51B | none | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:7003` | Mitsui ES Holdings Co., Ltd. | **+7.19%** | 3249 JPY | 2,101,300 | $1.92B | ADR | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:268A` | Rigaku Holdings Corporation | **+7.18%** | 1389 JPY | 1,641,300 | $1.84B | ADR | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:6134` | FUJI CORPORATION | **+7.09%** | 4759 JPY | 645,100 | $2.69B | none | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:6857` | Advantest Corp. | **+7.07%** | 26585 JPY | 23,955,900 | $108.57B | ADR | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:6723` | Renesas Electronics Corporation | **+6.88%** | 2600.5 JPY | 9,719,000 | $27.10B | ADR | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:5713` | Sumitomo Metal Mining Co., Ltd. | **+6.84%** | 6140 JPY | 2,810,800 | $9.82B | ADR | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:4368` | Fuso Chemical Co., Ltd. | **+6.81%** | 2777 JPY | 604,100 | $1.73B | none | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:3110` | Nitto Boseki Co., Ltd. | **+6.75%** | 2332.5 JPY | 4,002,700 | $2.57B | OTC | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:1515` | Nittetsu Mining Co., Ltd. | **+6.73%** | 2412 JPY | 469,400 | $1.13B | none | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:1980` | DAI-DAN Co., Ltd. | **+6.69%** | 3350 JPY | 710,700 | $2.68B | none | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:6925` | Ushio Inc. | **+6.68%** | 2793 JPY | 662,800 | $1.32B | OTC | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:5802` | Sumitomo Electric Industries, Ltd. | **+6.58%** | 1368 JPY | 23,418,400 | $25.44B | ADR | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:6590` | Shibaura Mechatronics Corp. | **+6.52%** | 2467 JPY | 1,810,300 | $1.00B | none | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:7012` | Kawasaki Heavy Industries Ltd. | **+6.47%** | 1588 JPY | 15,904,800 | $8.19B | ADR | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:6856` | Horiba, Ltd. | **+6.35%** | 18435 JPY | 193,600 | $4.55B | OTC | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:7729` | Tokyo Seimitsu Co., Ltd | **+6.25%** | 11820 JPY | 368,600 | $2.86B | OTC | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:5714` | DOWA HOLDINGS CO., LTD. | **+6.24%** | 7801 JPY | 670,800 | $2.74B | OTC | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:5711` | Mitsubishi Materials Corp. | **+6.19%** | 3841 JPY | 1,326,700 | $2.96B | OTC | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:4203` | Sumitomo Bakelite Co., Ltd. | **+6.17%** | 6811 JPY | 652,900 | $3.30B | ADR | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:6963` | ROHM Company Limited | **+6.08%** | 2845 JPY | 3,717,400 | $6.49B | OTC | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:6703` | OKI Electric Industry Company, Limited | **+5.91%** | 2313 JPY | 673,600 | $1.19B | ADR | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:5803` | Fujikura Ltd | **+5.90%** | 2199.5 JPY | 59,778,100 | $22.85B | ADR | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:6323` | Rorze Corporation | **+5.84%** | 2889.5 JPY | 3,832,800 | $3.01B | none | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:3132` | MACNICA HOLDINGS INC. | **+5.78%** | 2990 JPY | 1,118,200 | $3.16B | none | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:5333` | NGK Corp. | **+5.77%** | 4365 JPY | 670,300 | $7.04B | OTC | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:6965` | Hamamatsu Photonics K.K. | **+5.66%** | 2007.5 JPY | 1,683,700 | $3.68B | ADR | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:6981` | Murata Manufacturing Co., Ltd. | **+5.47%** | 5087 JPY | 17,958,900 | $55.76B | ADR | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:8050` | SEIKO GROUP CORPORATION | **+5.47%** | 8755 JPY | 605,000 | $4.30B | none | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:6504` | Fuji Electric Co., Ltd. | **+5.37%** | 10455 JPY | 869,000 | $8.88B | ADR | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:6361` | Ebara Corporation | **+5.37%** | 3335 JPY | 6,493,400 | $9.07B | OTC | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:6268` | Nabtesco Corporation | **+5.20%** | 3438 JPY | 1,105,000 | $2.40B | ADR | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:4980` | Dexerials Corp. | **+5.09%** | 1983 JPY | 2,542,000 | $2.03B | none | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:6302` | Sumitomo Heavy Industries, Ltd. | **+5.01%** | 4866 JPY | 555,800 | $3.56B | ADR | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:6506` | Yaskawa Electric Corporation | **+5.00%** | 3380 JPY | 3,391,700 | $5.27B | ADR | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |
| `TSE:6368` | Organo Corp. | **+5.00%** | 1648.5 JPY | 2,023,300 | $2.28B | none | no company-specific release found — renewed buying in AI and semiconductor names, with buybacks and short covering after the 25 Nov AI rout; nonferrous metals, electrical equipment and machinery led the sectors (Kabutan, 27 Nov; Reuters, 27 Nov) |

### tw

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `TWSE:2466` | Cosmo Electronics Corporation | **+9.88%** | 361.5 TWD | 4,567,475 | $1.73B | none | AI-hardware complex bid on the session's 20 limit-ups (CNA / Focus Taiwan, 27 Nov) |
| `TWSE:2313` | Compeq Manufacturing Co., Ltd. | **+9.82%** | 184.5 TWD | 48,385,873 | $6.29B | none | low-orbit satellite complex — the FCC cleared SpaceX to deploy 1m AI computing satellites and Compeq hit the 10% limit-up for a second session (Commercial Times, 27 Nov; Commercial Times / udn, 27 Nov) |
| `TWSE:2385` | Chicony Electronics Co. Ltd. | **+9.78%** | 101 TWD | 7,237,038 | $2.03B | none | AI-hardware complex bid on the session's 20 limit-ups (CNA / Focus Taiwan, 27 Nov) |
| `TPEX:3081` | LandMark Optoelectronics Corp. | **-9.71%** | 1395 TWD | 984,424 | $4.77B | none | no company-specific release found — AI-hardware and low-orbit-satellite complex bid in a directionless session with foreign investors net sellers of NT$29.6bn (CNA / Focus Taiwan, 27 Nov; Commercial Times, 27 Nov) |
| `TWSE:3406` | GeniuS Electronic Optical Co., Ltd. | **-7.69%** | 708 TWD | 5,643,673 | $2.75B | none | no company-specific release found — AI-hardware and low-orbit-satellite complex bid in a directionless session with foreign investors net sellers of NT$29.6bn (CNA / Focus Taiwan, 27 Nov; Commercial Times, 27 Nov) |
| `TPEX:3491` | Universal Microwave Technology, Inc. | **+7.25%** | 1480 TWD | 1,220,989 | $2.88B | none | low-orbit satellite complex — FCC clearance for SpaceX's 1m AI satellites (Commercial Times, 27 Nov) |
| `TPEX:3324` | AURAS Technology Co., Ltd. | **-6.64%** | 801 TWD | 3,925,823 | $2.36B | none | no company-specific release found — AI-hardware and low-orbit-satellite complex bid in a directionless session with foreign investors net sellers of NT$29.6bn (CNA / Focus Taiwan, 27 Nov; Commercial Times, 27 Nov) |
| `TWSE:2368` | Gold Circuit Electronics Ltd | **-6.63%** | 929 TWD | 10,403,492 | $15.85B | none | no company-specific release found — AI-hardware and low-orbit-satellite complex bid in a directionless session with foreign investors net sellers of NT$29.6bn (CNA / Focus Taiwan, 27 Nov; Commercial Times, 27 Nov) |
| `TWSE:3653` | Jentech Precision Industrial Co., Ltd | **+6.54%** | 4885 TWD | 1,602,531 | $20.32B | none | AI-hardware complex bid on the session's 20 limit-ups (CNA / Focus Taiwan, 27 Nov) |
| `TWSE:6669` | Wiwynn Corporation | **+6.37%** | 1670 TWD | 7,323,979 | $26.69B | none | AWS ASIC liquid-cooled rack volumes seen continuing to ramp, with AI server demand intact into 2027 (Economic Daily News, 27 Nov) |
| `TWSE:3665` | BizLink Holding Inc. | **-6.15%** | 1680 TWD | 3,777,836 | $10.84B | none | no company-specific release found — AI-hardware and low-orbit-satellite complex bid in a directionless session with foreign investors net sellers of NT$29.6bn (CNA / Focus Taiwan, 27 Nov; Commercial Times, 27 Nov) |
| `TWSE:3443` | Global Unichip Corp. | **-5.57%** | 5090 TWD | 1,059,338 | $21.92B | none | no company-specific release found — AI-hardware and low-orbit-satellite complex bid in a directionless session with foreign investors net sellers of NT$29.6bn (CNA / Focus Taiwan, 27 Nov; Commercial Times, 27 Nov) |
| `TWSE:1802` | Taiwan Glass Industry Corp. | **-5.53%** | 56.4 TWD | 142,215,793 | $5.27B | none | no company-specific release found — AI-hardware and low-orbit-satellite complex bid in a directionless session with foreign investors net sellers of NT$29.6bn (CNA / Focus Taiwan, 27 Nov; Commercial Times, 27 Nov) |
| `TPEX:3529` | eMemory Technology, Inc. | **-5.33%** | 1865 TWD | 559,941 | $4.37B | none | no company-specific release found — AI-hardware and low-orbit-satellite complex bid in a directionless session with foreign investors net sellers of NT$29.6bn (CNA / Focus Taiwan, 27 Nov; Commercial Times, 27 Nov) |
| `TPEX:7828` | Innostar Service Inc | **-5.06%** | 1220 TWD | 104,092 | $1.58B | none | no company-specific release found — AI-hardware and low-orbit-satellite complex bid in a directionless session with foreign investors net sellers of NT$29.6bn (CNA / Focus Taiwan, 27 Nov; Commercial Times, 27 Nov) |

### ca

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `TSX:SKE` | Skeena Resources Limited | **+9.51%** | 41.58 CAD | 290,458 | $3.35B | NYSE | precious-metals bid — gold +4.1% to $3,681.90/oz, silver +10.4% to $44.22/oz (Dow Jones, 27 Nov) |
| `TSX:AYA` | Aya Gold & Silver Inc. | **+9.48%** | 32.23 CAD | 1,239,033 | $2.98B | NASDAQ | no company-specific release found — precious-metals bid: gold +4.1% to $3,681.90 and silver +10.4% to $44.22/oz, with copper the most in four months (Dow Jones, 27 Nov; Reuters, 27 Nov) |
| `TSX:ABRA` | AbraSilver Resource Corp. | **+9.31%** | 10.1 CAD | 449,708 | $1.04B | OTC | no company-specific release found — precious-metals bid: gold +4.1% to $3,681.90 and silver +10.4% to $44.22/oz, with copper the most in four months (Dow Jones, 27 Nov; Reuters, 27 Nov) |
| `TSX:EDR` | Endeavour Silver Corp. | **+9.02%** | 9.79 CAD | 1,126,534 | $1.87B | NYSE | no company-specific release found — precious-metals bid: gold +4.1% to $3,681.90 and silver +10.4% to $44.22/oz, with copper the most in four months (Dow Jones, 27 Nov; Reuters, 27 Nov) |
| `TSX:DSV` | Discovery Mining Ltd. | **+7.86%** | 9.88 CAD | 1,890,643 | $5.24B | ADR | no company-specific release found — precious-metals bid: gold +4.1% to $3,681.90 and silver +10.4% to $44.22/oz, with copper the most in four months (Dow Jones, 27 Nov; Reuters, 27 Nov) |
| `TSX:GMIN` | G Mining Ventures Corp | **+7.84%** | 46.88 CAD | 624,150 | $9.04B | OTC | no company-specific release found — precious-metals bid: gold +4.1% to $3,681.90 and silver +10.4% to $44.22/oz, with copper the most in four months (Dow Jones, 27 Nov; Reuters, 27 Nov) |
| `TSX:ELD` | Eldorado Gold Corporation | **+7.73%** | 43.21 CAD | 447,350 | $7.36B | NYSE | no company-specific release found — precious-metals bid: gold +4.1% to $3,681.90 and silver +10.4% to $44.22/oz, with copper the most in four months (Dow Jones, 27 Nov; Reuters, 27 Nov) |
| `TSX:BTO` | B2Gold Corp. | **+7.57%** | 6.96 CAD | 3,985,372 | $5.98B | NYSE | no company-specific release found — precious-metals bid: gold +4.1% to $3,681.90 and silver +10.4% to $44.22/oz, with copper the most in four months (Dow Jones, 27 Nov; Reuters, 27 Nov) |
| `TSX:MAU` | Montage Gold Corp. | **+7.52%** | 14.73 CAD | 886,062 | $3.92B | OTC | no company-specific release found — precious-metals bid: gold +4.1% to $3,681.90 and silver +10.4% to $44.22/oz, with copper the most in four months (Dow Jones, 27 Nov; Reuters, 27 Nov) |
| `TSX:SVM` | Silvercorp Metals Inc. | **+7.39%** | 10.75 CAD | 597,426 | $1.56B | NYSE | no company-specific release found — precious-metals bid: gold +4.1% to $3,681.90 and silver +10.4% to $44.22/oz, with copper the most in four months (Dow Jones, 27 Nov; Reuters, 27 Nov) |
| `TSX:SGD` | Snowline Gold Corp. | **+7.04%** | 12.47 CAD | 280,109 | $1.54B | OTC | no company-specific release found — precious-metals bid: gold +4.1% to $3,681.90 and silver +10.4% to $44.22/oz, with copper the most in four months (Dow Jones, 27 Nov; Reuters, 27 Nov) |
| `TSX:TXR` | Torex Resources Inc. | **+7.03%** | 70.53 CAD | 230,726 | $4.18B | NYSE | no company-specific release found — precious-metals bid: gold +4.1% to $3,681.90 and silver +10.4% to $44.22/oz, with copper the most in four months (Dow Jones, 27 Nov; Reuters, 27 Nov) |
| `TSX:VZLA` | Vizsla Silver Corp. | **+6.97%** | 4.45 CAD | 873,913 | $1.04B | NYSE | no company-specific release found — precious-metals bid: gold +4.1% to $3,681.90 and silver +10.4% to $44.22/oz, with copper the most in four months (Dow Jones, 27 Nov; Reuters, 27 Nov) |
| `TSX:KNT` | K92 Mining, Inc. | **+6.70%** | 24.86 CAD | 497,228 | $4.02B | OTC | no company-specific release found — precious-metals bid: gold +4.1% to $3,681.90 and silver +10.4% to $44.22/oz, with copper the most in four months (Dow Jones, 27 Nov; Reuters, 27 Nov) |
| `TSX:SXGC` | Southern Cross Gold Consolidated Ltd. | **+6.45%** | 7.26 CAD | 614,215 | $1.29B | OTC | no company-specific release found — precious-metals bid: gold +4.1% to $3,681.90 and silver +10.4% to $44.22/oz, with copper the most in four months (Dow Jones, 27 Nov; Reuters, 27 Nov) |
| `TSX:AG` | First Majestic Silver Corp. | **+6.39%** | 17.48 CAD | 1,284,936 | $5.69B | NYSE | no company-specific release found — precious-metals bid: gold +4.1% to $3,681.90 and silver +10.4% to $44.22/oz, with copper the most in four months (Dow Jones, 27 Nov; Reuters, 27 Nov) |
| `TSX:PAAS` | Pan American Silver Corp. | **+6.19%** | 49.92 CAD | 759,680 | $13.61B | NYSE | no company-specific release found — precious-metals bid: gold +4.1% to $3,681.90 and silver +10.4% to $44.22/oz, with copper the most in four months (Dow Jones, 27 Nov; Reuters, 27 Nov) |
| `TSX:IMG` | IAMGOLD Corporation | **+6.07%** | 24.64 CAD | 821,126 | $9.24B | NYSE | no company-specific release found — precious-metals bid: gold +4.1% to $3,681.90 and silver +10.4% to $44.22/oz, with copper the most in four months (Dow Jones, 27 Nov; Reuters, 27 Nov) |
| `TSX:EQX` | Equinox Gold Corp. | **+6.06%** | 14.01 CAD | 2,573,929 | $11.09B | NYSE | no company-specific release found — precious-metals bid: gold +4.1% to $3,681.90 and silver +10.4% to $44.22/oz, with copper the most in four months (Dow Jones, 27 Nov; Reuters, 27 Nov) |
| `TSX:ORE` | Orezone Gold Corporation | **+5.86%** | 2.35 CAD | 953,429 | $1.12B | OTC | no company-specific release found — precious-metals bid: gold +4.1% to $3,681.90 and silver +10.4% to $44.22/oz, with copper the most in four months (Dow Jones, 27 Nov; Reuters, 27 Nov) |
| `TSX:HBM` | Hudbay Minerals Inc | **+5.84%** | 26.46 CAD | 2,423,534 | $7.79B | NYSE | no company-specific release found — precious-metals bid: gold +4.1% to $3,681.90 and silver +10.4% to $44.22/oz, with copper the most in four months (Dow Jones, 27 Nov; Reuters, 27 Nov) |
| `TSX:FVI` | Fortuna Mining Corp. | **+5.76%** | 12.12 CAD | 542,182 | $2.38B | NYSE | no company-specific release found — precious-metals bid: gold +4.1% to $3,681.90 and silver +10.4% to $44.22/oz, with copper the most in four months (Dow Jones, 27 Nov; Reuters, 27 Nov) |
| `TSX:TKO` | Trekor Metals Limited | **+5.75%** | 8.65 CAD | 651,329 | $2.11B | NYSE | no company-specific release found — precious-metals bid: gold +4.1% to $3,681.90 and silver +10.4% to $44.22/oz, with copper the most in four months (Dow Jones, 27 Nov; Reuters, 27 Nov) |
| `TSX:AAUC` | Allied Gold Corporation | **+5.71%** | 29.46 CAD | 301,047 | $2.75B | NYSE | no company-specific release found — precious-metals bid: gold +4.1% to $3,681.90 and silver +10.4% to $44.22/oz, with copper the most in four months (Dow Jones, 27 Nov; Reuters, 27 Nov) |
| `TSX:K` | Kinross Gold Corporation | **+5.58%** | 28.39 CAD | 2,537,093 | $22.24B | NYSE | no company-specific release found — precious-metals bid: gold +4.1% to $3,681.90 and silver +10.4% to $44.22/oz, with copper the most in four months (Dow Jones, 27 Nov; Reuters, 27 Nov) |
| `TSX:WDO` | Wesdome Gold Mines Ltd. | **+5.52%** | 26.55 CAD | 263,439 | $2.54B | OTC | no company-specific release found — precious-metals bid: gold +4.1% to $3,681.90 and silver +10.4% to $44.22/oz, with copper the most in four months (Dow Jones, 27 Nov; Reuters, 27 Nov) |
| `TSX:CG` | Centerra Gold Inc. | **+5.46%** | 27.83 CAD | 341,500 | $3.59B | NYSE | no company-specific release found — precious-metals bid: gold +4.1% to $3,681.90 and silver +10.4% to $44.22/oz, with copper the most in four months (Dow Jones, 27 Nov; Reuters, 27 Nov) |
| `TSX:ARIS` | Aris Mining Corp | **+5.25%** | 19.64 CAD | 461,620 | $2.71B | NYSE | no company-specific release found — precious-metals bid: gold +4.1% to $3,681.90 and silver +10.4% to $44.22/oz, with copper the most in four months (Dow Jones, 27 Nov; Reuters, 27 Nov) |
| `TSX:AEM` | Agnico Eagle Mines Limited | **+5.15%** | 245.85 CAD | 674,940 | $83.03B | NYSE | no company-specific release found — precious-metals bid: gold +4.1% to $3,681.90 and silver +10.4% to $44.22/oz, with copper the most in four months (Dow Jones, 27 Nov; Reuters, 27 Nov) |

### eu-de

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `XETR:S92` | SMA Solar Technology AG | **+7.61%** | 47.52 EUR | 104,395 | $1.68B | ADR | Berenberg upgrade with backlog driving earnings upside (Everhint market wrap, 27 Nov) |

### eu-fr

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `EURONEXT:EXENS` | Exosens SA | **+6.37%** | 54.3 EUR | 234,682 | $2.85B | none | German army order for 6,000 night-vision units (Everhint market wrap, 27 Nov) |
| `EURONEXT:SOI` | Soitec SA | **+5.01%** | 95.52 EUR | 304,342 | $3.57B | OTC | European semiconductor bid — ASML, ASM International and Infineon up 5-6% in a session where STOXX 600 technology added 2.6% (Reuters, 27 Nov) |

### eu-it

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `MIL:FCT` | Fincantieri S.p.A. | **+5.72%** | 12.105 EUR | 4,237,993 | $4.76B | OTC | EUR 500m Italian navy contract win (Everhint market wrap, 27 Nov) |

### eu-es

No name in this region cleared the mover gate (volume >= 100,000, market cap >= $1bn, |change| >= 5%).

### eu-nl

No name in this region cleared the mover gate (volume >= 100,000, market cap >= $1bn, |change| >= 5%).

### eu-be

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `EURONEXT:BEKB` | Bekaert SA | **+7.86%** | 42.55 EUR | 126,584 | $2.06B | none | strong Q3 nine-month trading update (Everhint market wrap, 27 Nov) |

### eu-at

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `VIE:ATS` | AT & S Austria Technologie & Systemtechnik Aktiengesellschaft | **+7.91%** | 105 EUR | 146,822 | $4.14B | OTC | Dörflinger Management & Beteiligungs GmbH buy disclosure published as ad-hoc EQS news five times between 14:00 and 14:20 on 27 Nov, on top of the AI-substrate PCB bid; the Vienna exchange's own print is EUR 105.00, +7.91% (Wiener Boerse price page, 27 Nov) |

### eu-pt

No name in this region cleared the mover gate (volume >= 100,000, market cap >= $1bn, |change| >= 5%).

### eu-ie

No name in this region cleared the mover gate (volume >= 100,000, market cap >= $1bn, |change| >= 5%).

### eu-fi

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `OMXHEX:METSO` | Metso Corporation | **+5.02%** | 15.05 EUR | 1,808,613 | $13.00B | OTC | no company-specific release found — European technology and semiconductor shares led the STOXX 600 higher (Reuters, 27 Nov) |

### eu-dk

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing | Catalyst |
|---|---|---|---|---|---|---|---|
| `OMXCOP:AMBU_B` | Ambu A/S Class B | **+7.60%** | 93.45 DKK | 1,387,630 | $3.38B | OTC | Nordea raised Ambu to Buy (Hold) with a DKK 110 target (MarketScreener / MarketScreener, 27 Nov) |

### eu-gr

No name in this region cleared the mover gate (volume >= 100,000, market cap >= $1bn, |change| >= 5%).

## Below the gate

Names that moved hard but fell **below the cap floor**, so they are not in the CSVs (`_excluded.json`, reason `below_cap_floor`) — published, because a -39% or a +200% move is not noise. Their tickers are printed **without** the backtick format used for CSV rows precisely because they are not CSV rows. The three largest per region are shown; the full list is in `_excluded.json`. **Most of them are sub-$0.05 micro-caps whose percentage carries little information** — their prices, not their percentages, are the signal.

### au

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | Why it is here |
|---|---|---|---|---|---|---|
| ASX:FIN | Fin Resources Limited | **+100.00%** | 0.002 | 29,125,000 | $1M | below the $300.0M Australia cap floor |
| ASX:HYD | Hydrix Limited | **+100.00%** | 0.002 | 200,000 | $2M | below the $300.0M Australia cap floor |
| ASX:BIT | Biotron Limited | **+100.00%** | 0.002 | 352,007 | $2M | below the $300.0M Australia cap floor |

### jp

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | Why it is here |
|---|---|---|---|---|---|---|
| TSE:6085 | Architects Studio Japan, Inc. | **+45.24%** | 61 | 15,928,500 | $32M | below the $300.0M Japan cap floor |
| TSE:281A | Informetis Co.,Ltd. | **+33.33%** | 320 | 1,715,500 | $9M | below the $300.0M Japan cap floor |
| TSE:4586 | Medrx Co., Ltd. | **-23.70%** | 103 | 26,061,100 | $63M | below the $300.0M Japan cap floor |

### tw

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | Why it is here |
|---|---|---|---|---|---|---|
| TPEX:6812 | SAULTECH Technology Co., Ltd. | **+16.64%** | 66.6 | 237,793 | $63M | below the $200.0M Taiwan cap floor |
| TPEX:6980 | Rapidtek Technologies Inc. | **+13.24%** | 124 | 334,979 | $107M | below the $200.0M Taiwan cap floor |
| TPEX:6973 | U-Neuron Biomedical Inc | **+11.29%** | 55.2 | 151,846 | $75M | below the $200.0M Taiwan cap floor |

### ca

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | Why it is here |
|---|---|---|---|---|---|---|
| CSE:ATHR | Aether Catalyst Solutions, Inc. | **+100.00%** | 0.01 | 155,000 | $264,762 | below the $200.0M Canada cap floor |
| TSXV:MTLO | Martello Technologies Group, Inc. | **+100.00%** | 0.01 | 182,200 | $2M | below the $200.0M Canada cap floor |
| TSXV:CRD | Copper Road Resources Inc | **+60.00%** | 0.04 | 131,000 | $2M | below the $200.0M Canada cap floor |

### eu-de

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | Why it is here |
|---|---|---|---|---|---|---|
| XETR:TPG0 | Platform Group SE & Co. KGaA | **-14.76%** | 0.231 | 785,405 | $6M | below the $300.0M Germany cap floor |
| XETR:BRNK | BRANICKS Group AG | **+5.07%** | 0.29 | 211,774 | $25M | below the $300.0M Germany cap floor |

### eu-fr

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | Why it is here |
|---|---|---|---|---|---|---|
| EURONEXT:ALIBR | Calibre | **+50.00%** | 0.0003 | 12,259,398 | $7M | below the $100.0M France cap floor |
| EURONEXT:MAAT | MaaT Pharma | **+25.65%** | 0.779 | 171,152 | $13M | below the $100.0M France cap floor |
| EURONEXT:ALCRB | Carbios SA | **-12.66%** | 3.07 | 108,532 | $65M | below the $100.0M France cap floor |

### eu-it

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | Why it is here |
|---|---|---|---|---|---|---|
| MIL:FDA | Fidia S.p.A. | **-13.58%** | 0.014 | 90,639,724 | $22M | below the $100.0M Italy cap floor |
| MIL:AGP | Altea Green Power S.p.A. | **+11.92%** | 4.6 | 246,522 | $82M | below the $100.0M Italy cap floor |
| MIL:ENY | Energy SpA | **-6.08%** | 0.34 | 145,000 | $23M | below the $100.0M Italy cap floor |

### eu-es

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | Why it is here |
|---|---|---|---|---|---|---|
| BME:NYE | Nyesa Valores Corporacion, S.A. | **+8.70%** | 0.0025 | 202,662,420 | $13M | below the $100.0M Spain cap floor |
| BME:EZE | Grupo Ezentis SA | **+8.04%** | 0.0524 | 3,318,756 | $43M | below the $100.0M Spain cap floor |
| BME:VANA | Vanadi Coffee SA | **+5.00%** | 0.0105 | 2,478,640 | $3M | below the $100.0M Spain cap floor |

### eu-be

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | Why it is here |
|---|---|---|---|---|---|---|
| EURONEXT:OXUR | Oxurion NV | **-14.29%** | 0.0012 | 4,681,579 | $355,890 | below the $100.0M Belgium cap floor |

### eu-fi

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | Why it is here |
|---|---|---|---|---|---|---|
| OMXHEX:MODU | Modulight Oyj | **+6.29%** | 1.69 | 168,799 | $74M | below the $100.0M Finland cap floor |
| OMXHEX:PNA1V | Panostaja Oyj | **+6.19%** | 0.326 | 105,331 | $18M | below the $100.0M Finland cap floor |

### eu-dk

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | Why it is here |
|---|---|---|---|---|---|---|
| OMXCOP:UNLGRP | Unlimit Group A/S | **-12.00%** | 0.0044 | 4,066,605 | $3M | below the $100.0M Denmark cap floor |

## No catalyst

Names that moved with no sourced driver — no company release, no filing, no analyst action, and no sourced sector or macro move behind them — kept separate so they do not dilute the mover table.

### jp

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing |
|---|---|---|---|---|---|---|
| `TSE:485A` | PowerX, Inc. | **+12.73%** | 1798 JPY | 6,205,400 | $1.17B | none |
| `TSE:1942` | Kandenko Co., Ltd. | **+10.37%** | 4777 JPY | 2,027,200 | $5.54B | none |
| `TSE:4588` | Oncolys BioPharma, Inc. | **+10.00%** | 8580 JPY | 2,072,400 | $1.45B | none |
| `TSE:5838` | Rakuten Bank, Ltd. | **+8.63%** | 4080 JPY | 7,731,100 | $5.27B | none |
| `TSE:7806` | MTG Co., Ltd. | **+8.28%** | 7190 JPY | 354,400 | $1.65B | none |
| `TSE:7014` | Namura Shipbuilding Co., Ltd. | **+8.11%** | 3400 JPY | 855,400 | $1.37B | OTC |
| `TSE:3774` | Internet Initiative Japan Inc. | **-7.31%** | 3730 JPY | 2,171,200 | $4.55B | ADR |
| `TSE:1944` | Kinden Corporation | **+6.78%** | 5937 JPY | 769,500 | $5.73B | none |
| `TSE:1961` | Sanki Engineering Co., Ltd. | **+6.14%** | 2540 JPY | 579,200 | $2.22B | none |
| `TSE:4565` | Nxera Pharma Co., Ltd. | **+5.72%** | 2051 JPY | 3,466,200 | $1.13B | OTC |
| `TSE:9412` | SKY Perfect JSAT Corporation | **+5.27%** | 1679 JPY | 1,861,000 | $2.83B | ADR |
| `TSE:1893` | Penta-Ocean Construction Co., Ltd. | **+5.22%** | 1310.5 JPY | 1,737,400 | $2.23B | OTC |
| `TSE:8020` | Kanematsu Corporation | **+5.08%** | 2387 JPY | 884,300 | $2.39B | none |

### tw

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing |
|---|---|---|---|---|---|---|
| `TWSE:6949` | PELL Bio-Med Technology Co Ltd | **-10.00%** | 32.4 TWD | 12,203,707 | $1.43B | none |
| `TWSE:7610` | LIANYOU METALS CO.,LTD. | **-9.88%** | 775 TWD | 916,379 | $1.52B | none |

### ca

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing |
|---|---|---|---|---|---|---|
| `TSX:GRGD` | Groupe Dynamite Inc. | **+6.30%** | 55.84 CAD | 175,195 | $4.02B | OTC |

### eu-de

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing |
|---|---|---|---|---|---|---|
| `XETR:AG1` | AUTO1 Group SE | **+5.44%** | 15.71 EUR | 488,732 | $3.62B | OTC |
| `XETR:VBK` | Verbio SE | **+5.07%** | 21.14 EUR | 102,585 | $1.41B | none |

### eu-fi

| Ticker | Name | Change | Close | Volume | Mkt cap (USD) | US listing |
|---|---|---|---|---|---|---|
| `OMXHEX:BITTI` | Bittium Corporation | **+5.99%** | 35.4 EUR | 122,520 | $1.30B | none |

## Method, source health & caveats

### Method

- **Universe** — the TradingView per-country scanner, one complete pull per region, filtered on the ISSUER's `country` column (`filter`, not `filters`) and on `type == stock`. The pull's completeness test is a set test on the venue-qualified symbol, not a row count: every pull returned exactly `totalCount` rows with no duplicate symbol. The 16 universe counts (au 1,541; jp 3,889; tw 2,347; ca 4,274; eu-de 4,282; eu-fr 544; eu-it 377; eu-es 230; eu-nl 77; eu-be 101; eu-at 66; eu-pt 30; eu-ie 19; eu-fi 189; eu-dk 133; eu-gr 128) reproduce the 25 November archive's counts to within the listing changes of two sessions.
- **Floors** — applied in USD **after** the FX conversion, on the issuer's company-level cap: au and jp $300M, eu-de $300M, tw, ca and eu-ie $200M, most eurozone boards $100M, eu-pt and eu-gr $50M; the extra volume gate is `>= 100,000` for au and `>= 50,000` for eu-de, applied to the company's liquidity across its venue rows, not to the selected print.
- **FX** — Frankfurter (`api.frankfurter.dev/v1/latest?base=USD`, rate date 2026-11-27) with TWD from open.er-api (`open.er-api.com/v6/latest/USD`, updated Fri, 27 Nov 2026 00:02:31 +0000). The table is **local currency per 1 USD**, so the conversion is a division: `usd_cap = market_cap_basic / FX_per_USD[currency]`. EUR 0.91266, AUD 1.4996, CAD 1.4245, JPY 159.54, TWD 32.948403, DKK 6.8209.
- **Cap carrier rule** — the cap is resolved to the issuer's **primary common line**, converted once with the primary's currency, and every line of that issuer carries that one USD figure; `cap_source_symbol` records the line it came from and a preferred line never outranks the common line. A group with no common line is dropped as `issuer_unresolved` (128 Canadian rows). The cross-venue check compares each carried cap with the issuer's US line from the America scanner (13,406 rows, 1,628 depositary receipts): **61** pairs disagree by more than 10% and are flagged.
- **Venue collapse and the venue-official price rule** — the primary venue's line wins (au ASX; jp TSE, NAG, FSE, SAPSE; tw TWSE, TPEX; ca TSX, TSXV, CSE, NEO; eu-de XETR, FWB, LSX, LS, GETTEX, DUS, MUN, SWB, TRADEGATE, HAM, HAN), and a line whose implied prior close does not reconcile with the prior session's published close is a `stale_venue_print`. Where an exchange's own print exists it is the price: **AT&S is published at the Vienna Stock Exchange's own close of EUR 105.00 (+7.91%)**, and the **ATHEX General at Euronext Athens' own print of 2,512.83 (+1.33%)**. No row carries a `price_conflict` cell, because no venue-official print was obtained that disagreed with the published close.
- **CSV schema** — 18 columns, unchanged from the previous session: `date,ticker,name,open,high,low,close,volume,change_pct,market_cap,pe_ratio,sector,currency,exchange,cap_source_symbol,share_class,us_listing,price_conflict`. Prices are written to 4 decimals with trailing zeros stripped, `change_pct` and `pe_ratio` to 4 decimals, `market_cap` and `volume` as integers.
- **Files written** — `international-eod/2026-11-27/`: 16 per-region CSVs (`au.csv`, `jp.csv`, `tw.csv`, `ca.csv`, `eu-de.csv`, `eu-fr.csv`, `eu-it.csv`, `eu-es.csv`, `eu-nl.csv`, `eu-be.csv`, `eu-at.csv`, `eu-pt.csv`, `eu-ie.csv`, `eu-fi.csv`, `eu-dk.csv`, `eu-gr.csv`), plus `summary.md`, `_manifest.json`, `_excluded.json` and `_carryover.json`.

### Source health

| Source | Query / URL | Status | Result |
|---|---|---|---|
| TradingView per-country scanners | `POST scanner.tradingview.com/{country}/scan`, 16 pulls, `filter: country == <issuer country>`, `type == stock` | ok | 18,228 stock rows, 16/16 pulls complete (`rows == totalCount`, no duplicate symbol); universe counts reproduce the 25 Nov archive |
| TradingView America scanner | `POST scanner.tradingview.com/america/scan`, `type in [stock, dr]` | ok | 13,406 rows (11,778 stock, 1,628 dr) — the `us_listing` map and the cross-venue cap check |
| TradingView index scanner | `POST scanner.tradingview.com/global/scan`, 17 index symbols | ok | 16 regional benchmarks plus the STOXX 600, all closed levels |
| MCP bridge `market-recap price_history` | Yahoo-sourced daily bars, 40 symbols per call, 1,713 symbols requested | ok | **1,620 of 1,713 returned a 2026-11-26 close** — the session the archive is missing; the 93 without one are named gaps, and 1,620 closes plus 1,551 27 Nov closes were used to reconstruct the prior-session anchor and to cross-check the scanner |
| MCP bridge `market-recap price_history` (indices) | `^AXJO, ^N225, ^TWII, ^GSPTSE, ^GDAXI, ^FCHI, ^MIB, ^IBEX, ^AEX, ^BFX, ^ATX, ^PSI20, ^ISEQ, ^HEX, ^OMXC20, ^STOXX` | partial | 13 of 16 indices priced; `^MIB`, `^PSI20` and `^HEX` are not recognised by Yahoo, so those three benchmarks rest on the TradingView index pull alone |
| Yahoo chart API | `query1.finance.yahoo.com/v8/finance/chart/{SYM}` | failed | HTTP 429 ("Too Many Requests") on every request from this egress, with a browser User-Agent and without one — a rate limit, not an absence; the bridge's Yahoo-sourced history was used instead |
| Frankfurter FX | `api.frankfurter.dev/v1/latest?base=USD` | ok | rate date 2026-11-27, 29 currencies |
| open.er-api FX | `open.er-api.com/v6/latest/USD` | ok | TWD 32.948403, updated 2026-11-27 00:02:31 UTC |
| MCP availability probe | `_shared/probe_mcp.py` | ok | `catalog_ok total=138 finance_tools=0` — no financial MCP registered; the bridge is the quote source of record |
| Press cross-checks | Reuters, AP, CNA / Focus Taiwan, Kabutan, MarketIndex, Dow Jones, euro2day, Wiener Boerse, Commercial Times, ABC News live blog | ok | index levels and the named catalysts; AT&S's close and the ATHEX close are taken from the venue's own print |

### Caveats

- **The prior-session anchor was reconstructed, and that is the single most important caveat.** The archive has no 2026-11-26 international session: the routine's US-holiday gate declined that fire for Thanksgiving, so the newest published file for every region is 2026-11-25. Anchored on a two-session-old file, the stale-print test read 460 ordinary 26 November moves as stale venue prints and the Taiwan file lost 299 rows. The 26 November closes were therefore pulled from the bridge (1,620 of 1,713 requested symbols) and used as the per-symbol prior close. **The reconstruction is independently corroborated three ways**: the scanner's implied prior close reproduces the bridge's 26 November close to a median relative error of 0 on 1,514 checked rows; the Nikkei's 26 November close (57,499.16), the TAIEX's (39,151.81) and the TSX's (34,426.90) match the published press tables; and AT&S's Vienna exchange history shows a 26 November close of EUR 97.30, the archive's implied prior.
- **93 of the 1,713 symbols requested for the reconstruction returned no 26 November bar** (Yahoo does not carry them, or they did not print). Those rows keep the 25 November close as their anchor, so a name that moved more than 5% on 26 November and again on 27 November can still be misread as a stale print. Only 1 off-official row survived the rebuilt test, in eu-es.
- **Seven published Taiwan rows carry a close that the bridge's Yahoo-sourced history disagrees with by 1.4-3.5%** (`TPEX:6586`, `TPEX:6696`, `TPEX:7686`, `TPEX:7729`, `TPEX:7815`, `TPEX:7934`, `TPEX:7965`). Yahoo's TPEX volume differs materially from the scanner's on the same rows, so the scanner close is published and the disagreement is disclosed here. No conflict row appears in the movers table.
- **Carry-over rows are disclosed, not hidden.** 67 rows across the 16 boards did not trade in this session; their close is a carry-over from an earlier session and their `change_pct` describes that earlier session. They are listed in `_carryover.json` with each instrument's last trade date and are excluded from every movers table.
- **Taiwan's +/-10% prints are limit prices, not calculated moves.** On this session 20 Taiwanese names hit limit-up and 5 hit limit-down, and the index itself moved only 0.40% on 639 decliners against 451 advancers — a directionless session in which the movers table is a leadership list, not a measure of the market.
- **`market_cap` is company-level and in USD; the prices are in the listing currency.** A preferred line carries its issuer's company-level cap, and the cap is converted once, on the issuer's primary line. `share_class` and `cap_source_symbol` make that auditable.
- **The sector attribution is a sector attribution.** Where no company-specific release was found the catalyst cell says so and names the sourced sector or macro move behind the name; a company event is never asserted without a source. 18 names across five regions moved with no sourced driver at all and are published in `## No catalyst` instead.
- **Two Australian rows are artefacts, not moves, and both stay out of every published table.** `ASX:EDO` (El Dorado Goldfields, close A$0.087) carries the scanner's **+4,250.00%** change field, which is measured against an old A$0.002 print; the bridge's own daily bars put the 26 November close at A$0.06 and the 27 November close at A$0.087, a **+45%** move, and the row's A$0.06 open is consistent with that. `ASX:EDOO` is an **option line** (a DFD on the same issuer) at -50.00%. Both rows stay in the CSV with the source's own field, as the contract-adjustment rule requires, and both are excluded from the movers and below-gate tables; they are the reason Australia's breadth min and max read -50.00% and +4,250.00%.
- **61 published rows have a US line whose company-level cap differs from the local cap by more than 10%**, and are flagged in the build's cross-venue check: `ASX:APA` (+54.5%), `ASX:EDV` (-48.8%), `ASX:VAU` (-27.8%), `ASX:OBM` (-13.2%), `ASX:EMR` (-11.5%), `ASX:PDI` (-10.3%) and `ASX:WAF` (-10.1%) are the largest. The local primary-line cap is published in every case; the flag records that the US line disagrees, which is what a re-check of those issuers should start from.
- **Sector rotation (mean and median `change_pct` over the written rows)** — the gold and silver complex carried Canada (Non-Energy Minerals median +4.97% over 141 rows), electronic technology and producer manufacturing carried Japan, and the materials sector carried Australia (S&P/ASX 200 Materials +2.3% on the copper-futures spike). These are the same rows as the tables above, not a separate screen.

