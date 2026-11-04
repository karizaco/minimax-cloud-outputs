# Cron #5 — eod-international-daily — 2026-11-04

Daily EOD snapshot for the international markets the skill covers (AU, JP, TW, CA and 12 EU venues), written after each market's cash close settled. **4,440 instrument rows across 16 per-region CSVs**, one row per listed instrument, sorted by market cap (USD) descending.

> **Read this first:** `market_cap` is normalised to **USD**, while `close`/`open`/`high`/`low` stay in the **local listing currency** — the `currency` column states which. `change_pct` is TradingView's daily change in percent (not a fraction). Three facts change how the file reads: (1) **all 16 regions traded** — every per-country scanner pull returned a settled 4 November session, so unlike yesterday's run there is no missing `jp.csv`; (2) rows the source reports **no market cap** for cannot be screened against a cap floor and are **excluded rather than written blank** (244 rows, listed in `_excluded.json`); (3) **89 written rows did not trade today** and carry a carry-over close (listed in `_carryover.json`) — they are excluded from every movers list and from the breadth counts.

## Coverage

| Region | Venues | Universe | Unique instruments | Written | Floor (USD) | No cap | Off-official rows |
|---|---|---|---|---|---|---|---|
| `au` | ASX | 1,551 | 1,551 | **303** | $300M + vol ≥100,000 | 4 | 0 |
| `jp` | TSE | 3,896 | 3,868 | **1,380** | $300M | 2 | 110 |
| `tw` | TPEX, TWSE | 2,332 | 2,332 | **891** | $200M | 56 | 0 |
| `ca` | CSE, TSX, TSXV | 4,289 | 2,709 | **661** | $200M | 134 | 15 |
| `eu-de` | XETR | 4,303 | 498 | **126** | $300M + vol ≥50,000 | 2 | 173 |
| `eu-fr` | EURONEXT | 547 | 547 | **262** | $100M | 1 | 0 |
| `eu-it` | MIL | 392 | 392 | **179** | $100M | 2 | 0 |
| `eu-es` | BME | 273 | 273 | **147** | $100M | 34 | 0 |
| `eu-nl` | EURONEXT | 78 | 78 | **56** | $100M | 0 | 0 |
| `eu-be` | EURONEXT | 100 | 100 | **76** | $100M | 1 | 0 |
| `eu-at` | VIE | 65 | 65 | **51** | $100M | 3 | 0 |
| `eu-pt` | EURONEXT | 31 | 31 | **27** | $50M | 0 | 0 |
| `eu-ie` | EURONEXT | 19 | 19 | **17** | $200M | 0 | 0 |
| `eu-fi` | OMXHEX | 188 | 188 | **102** | $100M | 4 | 0 |
| `eu-dk` | OMXCOP | 134 | 134 | **76** | $100M | 1 | 0 |
| `eu-gr` | ATHEX | 128 | 128 | **86** | $50M | 0 | 0 |
| **total** | | **18,326** | **12,913** | **4,440** | | **244** | **298** |

`Universe` is every instrument the source returns for that country's own listings; `Unique instruments` collapses instruments quoted on several venues of the same market down to one row; `Written` applies the skill's per-region USD market-cap floor (`screener_filters.usd_floor_for_region`) plus the region volume gate. A further 7,922 instruments fell below the cap floor and 94 below the volume gate; 298 rows were dropped because their instrument has no listing on an official venue in its home market (Japan's NAG/FSE/SAPSE lines 110, Canada's NEO ATS lines 15, Germany's off-exchange lines 173).

## Market context

| Index | Close | Change | Day | Source |
|---|---|---|---|---|
| ASX 200 | **8,834.50** | -52.30 / **-0.59%** | down | Yahoo `^AXJO`; The Age & AFR ("down 52.30 points, or 0.6 per cent, at 8834.50"); Business Recorder (weakest close since 26 Oct) |
| All Ordinaries | **8,954.90** | -54.00 / **-0.60%** | down | Yahoo `^AORD`; Yahoo Finance AU ("All Ordinaries dragged 54 points or 0.60 per cent to 8954.90") |
| Nikkei 225 | **62,188.63** | -893.23 / **-1.42%** | down | Yahoo `^N225`; Jiji (62,188.63 / −893.23); AFP; Il Sole 24 Ore; edge consultancy Asia wrap |
| TOPIX | **3,895.38** | -34.90 / **-0.89%** | down | Jiji (3,895.38 / −34.90); Il Sole 24 Ore; edge consultancy Asia wrap |
| TAIEX | **42,948.91** | -358.63 / **-0.83%** | down | Yahoo `^TWII`; CNA / Focus Taiwan (42,948.91, −358.63 / −0.83%); Taiwan News |
| S&amp;P/TSX Composite | **36,341.40** | +809.12 / **+2.28%** | up | Yahoo `^GSPTSE`; Yahoo quote page ("At close 4:20:00 PM EST", 36,341.40 / 35,532.28) |
| DAX (Xetra) | **26,437.67** | +573.05 / **+2.22%** | up | Yahoo `^GDAXI` (Xetra close); edge consultancy Europe wrap (26,437.67 / +2.22%); SquawkNews |
| CAC 40 | **8,177.89** | +157.58 / **+1.96%** | up | Yahoo `^FCHI`; edge consultancy Europe wrap (8,177.89 / +1.96%); SquawkNews |
| FTSE MIB | **51,031.02** | +1089.02 / **+2.18%** | up | Yahoo `FTSEMIB.MI`; edge consultancy Europe wrap (51,031.02 / +2.18%) |
| IBEX 35 | **19,370.90** | +563.70 / **+3.00%** | up | Yahoo `^IBEX`; edge consultancy Europe wrap (19,370.90 / +3.00%, best of the nine) |
| AEX | **1,136.29** | +14.53 / **+1.30%** | up | Yahoo `^AEX`; edge consultancy Europe wrap (1,136.29 / +1.30%) |
| BEL 20 | **5,979.01** | +141.49 / **+2.42%** | up | Yahoo `^BFX` |
| ATX | **6,518.52** | +122.39 / **+1.91%** | up | Yahoo `^ATX` |
| PSI 20 | **9,391.57** | +167.68 / **+1.82%** | up | Yahoo `PSI20.LS` |
| ISEQ | **14,852.83** | +499.49 / **+3.48%** | up | Yahoo `^ISEQ`; Irish Times (14,852.83, +3.48%) |
| OMX Helsinki 25 | **6,289.73** | +100.11 / **+1.62%** | up | Yahoo `^OMXH25` |
| OMX Copenhagen 20 | **1,692.46** | +43.79 / **+2.66%** | up | Yahoo `^OMXC20` (single bar for 4 Nov; previous close 1,648.67) |
| ATHEX General | **2,662.45** | +46.33 / **+1.77%** | up | Euronext Athens historical data (2,662.45, +1.77%); pelop.gr (2,662.45, +46.33, best day since 21 Jul) |
| STOXX 600 *(context)* | **657.40** | +11.74 / **+1.82%** | up | Yahoo `^STOXX`; edge consultancy (657.40 / +1.82%); Sharecast/HL ("highest close since 14 August"). Anadolu Agency quotes 658.02 / +1.91% |
| Euro Stoxx 50 *(context)* | **6,265.71** | — / **+1.97%** | up | edge consultancy Europe wrap (6,265.71 / +1.97%); SquawkNews |
| FTSE 100 *(context)* | **10,829.21** | — / **+1.79%** | up | edge consultancy Europe wrap (10,829.21 / +1.79%); SquawkNews |

**One election, four different sessions.** Democrats took both chambers of the US Congress on Tuesday, and every market read it its own way. **Europe ripped higher** — the STOXX 600 closed +1.82% at 657.40, its best close since 14 August, with banks +4.32% and autos +3.26% leading and oil & gas the only clearly negative sector at −2.35% as crude slid. **Canada's TSX rose 2.28%** on a precious-metals melt-up (gold +2.9–3.4% to ~$4,050/oz, silver +4.8–5.3% to ~$52.13) that lifted the gold and silver miners 10–15%. **Tokyo fell 1.42% to a three-month low** despite a late rally from a nearly 5% intraday drop, as the same election raised fears of a congressional deadlock and a less favourable outlook for AI investment — semiconductor and AI-linked names were sold. **Taiwan fell 0.83%** after swinging 1,885.72 points, a fourth-largest intraday range on record, recovering from a 41,855.82 low as bargain hunters bought AI semis on AMD's and Supermicro's strong prints. **Australia fell 0.59%** to its weakest close since 26 October as investors digested the RBA's 25bp hike to 4.85% and the copper slide.

Regional breadth from the snapshot itself (median `change_pct` per file, carry-over rows excluded):

| Region | Rows | Median | Up / down / flat | Min | Max | Cap-weighted |
|---|---|---|---|---|---|---|
| `au` | 303 | -0.58% | 99 / 185 / 19 | -10.79% | +8.09% | -0.65% |
| `jp` | 1,380 | -0.62% | 419 / 926 / 35 | -15.60% | +15.06% | -0.88% |
| `tw` | 890 | -0.17% | 365 / 456 / 69 | -9.97% | +10.00% | -0.84% |
| `ca` | 622 | +0.88% | 420 / 167 / 35 | -14.75% | +15.46% | +1.77% |
| `eu-de` | 126 | +2.19% | 94 / 30 / 2 | -7.95% | +9.55% | +2.15% |
| `eu-fr` | 257 | +1.27% | 179 / 62 / 16 | -11.78% | +12.06% | +2.15% |
| `eu-it` | 174 | +0.82% | 110 / 56 / 8 | -8.63% | +5.82% | +2.22% |
| `eu-es` | 112 | +1.10% | 74 / 27 / 11 | -9.31% | +9.05% | +3.04% |
| `eu-nl` | 56 | +1.85% | 42 / 11 / 3 | -5.06% | +6.69% | -0.06% |
| `eu-be` | 74 | +1.35% | 54 / 12 / 8 | -2.65% | +10.00% | +2.37% |
| `eu-at` | 49 | +0.18% | 25 / 16 / 8 | -5.36% | +5.83% | +1.50% |
| `eu-pt` | 27 | 0.00% | 13 / 7 / 7 | -11.26% | +6.00% | +1.91% |
| `eu-ie` | 17 | +1.13% | 10 / 4 / 3 | -4.38% | +11.01% | +3.48% |
| `eu-fi` | 102 | +1.62% | 71 / 22 / 9 | -20.32% | +14.11% | +1.51% |
| `eu-dk` | 76 | +0.66% | 44 / 26 / 6 | -3.79% | +10.90% | +2.39% |
| `eu-gr` | 86 | +0.37% | 49 / 23 / 14 | -5.71% | +5.01% | +1.47% |

The cap-weighted column is the written rows' own market-cap-weighted average — **not** index methodology — computed on distinct company caps so a share class does not count its parent's size twice. It therefore will not equal the index, and most visibly it does not in the Netherlands: ASML alone carries roughly 60% of the snapshot's Dutch cap weight and fell 3.42% while the AEX rose 1.30%. **That disagreement is the point** — the index and the typical name, and the index and its largest constituent, did not tell the same story.

Sector rotation across the liquid subset (volume ≥ 100k, cap-weighted; the same rows as the movers list):

| Sector | Cap-weighted | Median | Names |
|---|---|---|---|
| Health Services | +3.42% | +0.81% | 17 |
| Commercial Services | +2.78% | +0.16% | 105 |
| Non-Energy Minerals | +2.73% | +1.32% | 279 |
| Consumer Non-Durables | +2.54% | +0.29% | 115 |
| Retail Trade | +2.43% | +0.69% | 121 |
| Finance | +2.05% | +0.41% | 420 |
| Utilities | +1.93% | +0.85% | 77 |
| Transportation | +1.61% | +0.11% | 101 |
| … | | | |
| Communications | -0.03% | +1.50% | 35 |
| Industrial Services | -0.30% | -0.52% | 147 |
| Miscellaneous | -1.14% | +0.25% | 11 |
| Producer Manufacturing | -1.61% | -0.86% | 355 |
| Electronic Technology | -1.65% | -0.67% | 456 |
| Energy Minerals | -3.07% | -3.90% | 68 |

## Top movers

Largest absolute daily moves among liquid names (volume ≥ 100k **and** market cap ≥ $1B), 1,802 of 4,440 written rows qualify. Carry-over rows are excluded from this table.

| Region | Ticker | Name | Change | Close | Volume | Mkt cap (USD) | Catalyst |
|---|---|---|---|---|---|---|---|
| ca | `TSX:DSV` | Discovery Mining Ltd. | **+15.28%** | 11.09 CAD | 3,692,441 | $5.60B | No company-specific release found; No company-specific release found — the precious-metals bid: gold rose 2.9–3.4% to ~$4,050/oz and silver 4.8–5.3% to ~$52.13 on a one-month-low dollar after the Democratic sweep (Reuters, Fair Value, 4 Nov) |
| jp | `TSE:6370` | Kurita Water Industries Ltd. | **+15.06%** | 5,347.00 JPY | 4,740,200 | $3.13B | Rebound after a three-session collapse — the 29 Oct guidance revision cut interim operating profit to ¥9,400m and booked a ¥36.2bn equity valuation loss, the stock then fell 21% on 30 Oct (¥7,147 → ¥5,647) and a further 18% on 2 Nov (to ¥4,647). No new release on 4 Nov; Q2 FY2027 results are due 5 Nov |
| ca | `TSX:GMIN` | G Mining Ventures Corp | **+13.97%** | 44.22 CAD | 1,417,257 | $8.21B | No company-specific release found; No company-specific release found — the precious-metals bid: gold rose 2.9–3.4% to ~$4,050/oz and silver 4.8–5.3% to ~$52.13 on a one-month-low dollar after the Democratic sweep (Reuters, Fair Value, 4 Nov) |
| ca | `TSX:VET` | Vermilion Energy Inc. | **-13.54%** | 15 CAD | 3,047,582 | $1.90B | Energy: crude slid (Brent ~−9% to $94.47, WTI −7.4%) as the election eased energy-cost fears, and the S&P/TSX Capped Energy Index fell 5.20%; no company-specific release found |
| ca | `TSX:EFX` | Enerflex Ltd. | **-12.90%** | 28.49 CAD | 1,512,843 | $2.85B | No new release on 4 Nov. The post-Q3 de-rating continued — 29 Oct results showed revenue −19.8% to US$623m — after RBC cut its target to C$33.00 (31 Oct) and a 4 Nov analyst downgrade took the shares below their 200-day average |
| ca | `TSX:EQX` | Equinox Gold Corp. | **+12.40%** | 15.77 CAD | 8,568,402 | $11.70B | No company-specific release found; No company-specific release found — the precious-metals bid: gold rose 2.9–3.4% to ~$4,050/oz and silver 4.8–5.3% to ~$52.13 on a one-month-low dollar after the Democratic sweep (Reuters, Fair Value, 4 Nov) |
| ca | `TSX:ABRA` | AbraSilver Resource Corp. | **+12.18%** | 11.42 CAD | 738,819 | $1.17B | No company-specific release found — the precious-metals bid: gold rose 2.9–3.4% to ~$4,050/oz and silver 4.8–5.3% to ~$52.13 on a one-month-low dollar after the Democratic sweep (Reuters, Fair Value, 4 Nov) (silver +5.3%) |
| eu-fr | `EURONEXT:MMT` | Metropole Television SA | **+12.06%** | 11.34 EUR | 586,128 | $1.43B | Reaction to the Q3 2026 release published after the close on 3 Nov: record audiences for the 25-49 demo and the best audience progression of the year versus 2025, on top of the Disney+ content agreement signed 25 September (M6/BusinessWire, 3 Nov) |
| ca | `TSX:SPB` | Superior Plus Corp | **-11.81%** | 6.05 CAD | 1,988,949 | $1.05B | No company-specific release found; a move with the Canadian energy-distribution complex as crude fell ~8% and the TSX energy sub-index lost 5.20% |
| eu-fr | `EURONEXT:SOI` | Soitec SA | **-11.78%** | 110.05 EUR | 525,909 | $5.00B | Morgan Stanley downgraded Soitec to Equal-Weight (from overweight) and cut its target from €200 to €140, citing volatility in a challenging macro environment; UBS went the other way (target €94 → €130, sell → neutral). The shares had already fallen 29.1% in a month after a +200% year, and the name finished last-but-one in the SBF 120 |
| ca | `TSX:GRGD` | Groupe Dynamite Inc. | **+11.70%** | 63.03 CAD | 366,329 | $4.37B | No company-specific release found; No company-specific release found — the precious-metals bid: gold rose 2.9–3.4% to ~$4,050/oz and silver 4.8–5.3% to ~$52.13 on a one-month-low dollar after the Democratic sweep (Reuters, Fair Value, 4 Nov) |
| ca | `TSX:WPM` | Wheaton Precious Metals Corp | **+11.66%** | 183.73 CAD | 1,626,825 | $53.40B | No company-specific release found; No company-specific release found — the precious-metals bid: gold rose 2.9–3.4% to ~$4,050/oz and silver 4.8–5.3% to ~$52.13 on a one-month-low dollar after the Democratic sweep (Reuters, Fair Value, 4 Nov) |
| jp | `TSE:9064` | Yamato Holdings Co., Ltd. | **+11.54%** | 2,194.50 JPY | 6,495,800 | $4.26B | Farallon Capital Management disclosed a 5.02% stake (~18.11m shares) in a large shareholding report filed with the Kanto Local Finance Bureau on 2 November; Farallon has urged the removal of Chairman and Representative Director Yutaka Nagao, and the shares were the top gainer among Nikkei constituents on reform expectations (Kabutan, Fisco Japan, 4 Nov) |
| ca | `TSXV:ARTG` | Artemis Gold Inc | **+11.19%** | 39.05 CAD | 400,408 | $5.85B | No company-specific release found; No company-specific release found — the precious-metals bid: gold rose 2.9–3.4% to ~$4,050/oz and silver 4.8–5.3% to ~$52.13 on a one-month-low dollar after the Democratic sweep (Reuters, Fair Value, 4 Nov) |

Largest mover per region among liquid names:

| Region | Ticker | Name | Change | Close | Catalyst |
|---|---|---|---|---|---|
| au | `ASX:4DX` | 4DMedical Ltd. | **-10.79%** | 2.15 AUD | No new release on 4 Nov. The stock is in an ASX-supervised slide: the exchange queried the 30 Oct move from A$3.28 to A$2.41 on a volume surge, the company replied on 2 Nov that it is aware of no unannounced information and that an increase in short interest drives the trading; the 28 Oct AGM result and Quarterly Activity Report took the price from A$3.61 to A$2.15 in seven sessions |
| jp | `TSE:6370` | Kurita Water Industries Ltd. | **+15.06%** | 5,347.00 JPY | Rebound after a three-session collapse — the 29 Oct guidance revision cut interim operating profit to ¥9,400m and booked a ¥36.2bn equity valuation loss, the stock then fell 21% on 30 Oct (¥7,147 → ¥5,647) and a further 18% on 2 Nov (to ¥4,647). No new release on 4 Nov; Q2 FY2027 results are due 5 Nov |
| tw | `TWSE:7750` | Syntec Technology Co. Ltd. | **-9.97%** | 1,490.00 TWD | −9.97% is the Taiwan ±10% limit-down; no company-specific release found. The worst performer on the exchange, in a session where losses were led by Information Services and Other Electronic (Investing.com) |
| ca | `TSX:DSV` | Discovery Mining Ltd. | **+15.28%** | 11.09 CAD | No company-specific release found; No company-specific release found — the precious-metals bid: gold rose 2.9–3.4% to ~$4,050/oz and silver 4.8–5.3% to ~$52.13 on a one-month-low dollar after the Democratic sweep (Reuters, Fair Value, 4 Nov) |
| eu-de | `XETR:HEI` | Heidelberg Materials AG | **+9.55%** | 171.5 EUR | Q3 2026 results before the open: revenue €6,413m (+10%), result from current operations €1,281m (+9%) and RCO before D&A €1.62bn (+8%) versus €1.57bn consensus, FY26 guidance confirmed (RCO €3.40–3.65bn) and a further €300m of savings targeted by end-2028 (company release, 4 Nov; Morningstar/Dow Jones, RTTNews) |
| eu-fr | `EURONEXT:MMT` | Metropole Television SA | **+12.06%** | 11.34 EUR | Reaction to the Q3 2026 release published after the close on 3 Nov: record audiences for the 25-49 demo and the best audience progression of the year versus 2025, on top of the Disney+ content agreement signed 25 September (M6/BusinessWire, 3 Nov) |
| eu-it | `MIL:TPRO` | Technoprobe SpA | **-7.07%** | 22.62 EUR | Chief technology officer departure — the worst performer on the Milan exchange, which still closed +2.18% with banks leading (ANSA, 4 Nov). Prysmian −6.9% and Avio −6.04% fell alongside it in the AI-related de-rating |
| eu-es | `BME:IDR` | Indra Sistemas, S.A. Class A | **-5.82%** | 59.88 EUR | No company-specific release found that explains the fall — the only 4 November release was a €40m+ SESAR air-traffic-management award; the move was with the European technology complex (Stoxx 600 technology −0.20%) |
| eu-nl | `EURONEXT:WKL` | Wolters Kluwer N.V. | **+6.69%** | 91.16 EUR | Nine-month 2026 trading update at 08:00 CET: 6% organic growth (up from 5% at the half year), recurring revenue (85% of the total) +7% organically, adjusted operating profit +10% at constant rates and 2026 guidance reaffirmed (company release, 4 Nov) |
| eu-be | `EURONEXT:UMI` | Umicore SA | **+6.25%** | 18.87 EUR | No company-specific release found; a move with the European materials complex on the election-driven bid for clean-energy names (Orsted +4.6%, Vestas and Nordex up), against a backdrop where energy itself was the weakest Stoxx sector |
| eu-at | `VIE:RBI` | Raiffeisen Bank International AG | **+5.83%** | 59.9 EUR | No company-specific release found; a move with the European banking rally — the Stoxx 600 banks index rose 4.32%, the strongest of the eight sectors, on the Democratic sweep's read-across for domestic lenders |
| eu-pt | `EURONEXT:JMT` | Jeronimo Martins, SGPS S.A. | **+3.88%** | 19.27 EUR | No company-specific release found; a move with the European consumer staples complex |
| eu-ie | `EURONEXT:GL9` | Glanbia PLC | **+11.01%** | 21.88 EUR | 9M revenue growth with raised full-year EPS guidance — the best performer on the Irish exchange, which closed +3.48% at 14,852.83 (Irish Times, 4 Nov) |
| eu-fi | `OMXHEX:BITTI` | Bittium Corporation | **-6.19%** | 34.85 EUR | No company-specific release found; a move with the European technology and defence-electronics complex |
| eu-dk | `OMXCOP:PNDORA` | Pandora A/S | **+10.90%** | 919.8 DKK | Q3 2026 results before the open: like-for-like sales +4% against a 2% consensus, organic growth 6% versus 4% expected, revenue DKK 6.69bn and operating profit DKK 1.06bn versus DKK 860m consensus (including a DKK 246m one-off US tariff refund); 2026 organic-growth guidance narrowed up to 2–3% from 0–3% and the EBIT margin outlook to 22.5–23% (company release, 4 Nov) |
| eu-gr | `ATHEX:ALPHA` | Alpha Bank S.A. | **+5.01%** | 4.736 EUR | Greek bank rally — the ATHEX banking index rose 2.81% to 3,121.33 and the General Index closed 2,662.45 (+1.77%), its best day since 21 July; Alpha Bank closed €4.736 (+5.01%) and National Bank of Greece €16.60 (+4.50%), with ETE results due after the close |

Six of the day's fourteen largest liquid moves are Canadian precious-metals names moving on the same macro bid, and the next three largest are the other side of the same trade — crude producers and a gas-processing name sold as oil fell. **The single biggest signal in the tape is not any one stock: it is that the TSX gained 2.28% while its energy sub-index lost 5.20% and its gold cohort gained 10–15%.**

Two large moves fall below the $1B / 100k-share liquid gate and are therefore not in the tables above: **Kempower (`OMXHEX:KEMPOWR`) −20.32%** to €6.45 on 535,571 shares (a €503M cap) and **NIHON DENGI (`TSE:1723`) −15.60%** to ¥1,672 on 1,239,800 shares (a ¥818M cap). No company-specific release was found for either; both are in the Electronic Technology complex that sold off across Asia and Europe.

## Method

1. **Universe** — the skill's `mcp__tradingview-advanced__stock_screener(country=…)` is not registered in this runtime, and the MCP-over-HTTP bridge's anonymous 50-call/day allowance was already spent. The same underlying source is reachable over its public per-country scanner API, so each region was pulled with a `country` filter matching the instrument's own country of primary listing plus `type = stock`. Without the `country` filter the per-country endpoint also returns *foreign* stocks quoted on that market's venues, which would have inflated Germany from ~500 companies to 36,000 rows. **16/16 calls returned HTTP 200 with no rate limiting.**
2. **Venue selection and the venue-collapse rule** — one row per instrument, preferring the official listing venue (XETR/FWB, TSE, TSX/TSXV/CSE, TWSE/TPEX, MIL, BME, VIE, OMXHEX, OMXCOP, ATHEX, EURONEXT, ASX), then the highest-volume print. Germany needs its own company key: Lang & Schwarz carries the same share under a WKN symbol (`LSX:750000` = thyssenkrupp's `TKA`), so German rows are deduped by company description — 4,303 raw rows collapse to 498 companies. Elsewhere the key is (description, ticker root), which keeps genuine share classes apart: `MFC` vs `MFC.PR.K`, `FFH` vs `FFH.U`, `SGR.U` vs `SGR.UN`, `DHT.U` vs `DHT.UN`, `HOT.U` vs `HOT.UN`, `CACR` vs `CACR.A`, and Japan's two unrelated companies both called "JTEC Corporation" (2479 / 3446) all survive as separate rows.
3. **Enrichment** — `volume`, `pe_ratio` and `sector` come straight from the same scanner response, so the skill's Yahoo `compare_stocks` enrichment stage was **not needed and was skipped**. No Yahoo quote was used for any price in the CSVs.
4. **Market cap** — `market_cap_basic` is in the row's **local** currency, so every value is converted to USD with the 4 Nov open.er-api rate table (updated 4 Nov 00:02 UTC). Frankfurter (2026-11-04) agrees within 0.71% on every currency it carries. Sanity-checked against implied share counts (local cap ÷ local close): Toyota 11,932m, TSMC 26,334m, SAP 1,126m, ASML 395m, Novo Nordisk 4,199m, Royal Bank 1,353m — all plausible.
5. **Change column** — the scanner's `change` field is already in **percent units** (0.0695 means +0.0695%), not a fraction. This was proven, not assumed: across all 18,319 priced rows of the pull, `close − close/(1 + change/100)` reproduces `change_abs` with a worst-case error of 6.8e-13. Multiplying by 100 would have inflated every move in this file by 100×.
6. **Floors applied client-side, after conversion** — the USD floors cannot be handed to the screener as server-side filters (the field is a local-currency number), so the per-region floor from `screener_filters.usd_floor_for_region` is applied to the converted USD cap, with the region volume gate applied to the company's liquidity (max volume across its venue rows) rather than the selected print.

### FX table (source: open.er-api, 4 Nov 2026 00:02 UTC)

| Currency | Per 1 USD | Frankfurter (2026-11-04) | Difference |
|---|---|---|---|
| EUR | 0.893426 | 0.88755 | +0.66% |
| AUD | 1.434205 | 1.4255 | +0.61% |
| CAD | 1.399422 | 1.3935 | +0.42% |
| JPY | 158.39919 | 158.25 | +0.09% |
| DKK | 6.680451 | 6.6334 | +0.71% |
| TWD | 32.770816 | *no rate* | — |

## Caveats

- **All 16 regions traded, but Japan's session came after a one-day holiday.** The TSE was closed on 3 November for Culture Day, so Japan's previous session in this archive is 2 November and the Nikkei and TOPIX changes below are measured against 2 November, not 3 November. Every other region is measured against 3 November.
- **89 written rows did not trade today** and are listed in `_carryover.json`: 79 rows with an unchanged close on zero volume (thin Canadian, Spanish, Italian and Austrian preferreds and small caps) and 10 rows whose close is unchanged but whose change column is a stale leftover (e.g. `EURONEXT:CROS` −8.76% on 11 shares, `EURONEXT:FGRMC` +2.92% on 1,202 shares, `VIE:BHD` +1.20% on 3 shares). Carry-over is detected by an exact string match on the close against the prior session's file, not a tolerance — a 0.5-cent move on a $1.31 stock is a move, not an unchanged close. All carry-over rows are excluded from every movers list and from the breadth counts.
- **244 rows have no market cap and were excluded** (134 Canada, 56 Taiwan, 34 Spain, 4 Australia, 4 Finland, 3 Austria, 2 Japan, 2 Germany, 2 Italy, 1 France, 1 Belgium, 1 Denmark). A row with no cap cannot be tested against a cap floor, so writing it would have put an unscreenable row in a screened file. The composition differs by region: the Canadian ones are preferred and share-class lines where the source publishes no company cap; the Taiwanese ones are small TPEx names; the Spanish ones are zero-volume SICAV and fund lines quoted on BME.
- **Share-class market caps are company-level.** TradingView replicates one cap across every line of a company, so preferred and unit lines carry their parent's cap and all clear the same floor. `BME:GRF.P` carries Grifols' cap and `TSX:RY.PR.S` carries Royal Bank's ~$283bn. This inflates the apparent size of Canadian, Spanish and German preferreds — and it is why a preferred line can appear as a region's largest mover.
- **One market cap is materially overstated.** `ASX:BHP` implies 5,162m shares against a real count near 2,130m, so BHP's market cap reads ~$200bn instead of ~$86bn. Every other checked name lands on a plausible share count. The field is written as the source reports it, but a cap-based screen will treat BHP as a mega-cap when it is not. (This is a repeat of the 2 and 3 November anomalies, unchanged.)
- **Two cross-venue prints differ for the same instrument.** On Xetra, Heidelberg Materials closed €171.50 while its Frankfurt line printed €170.95. The file keeps the official Xetra print, but for a handful of German names the off-exchange lines diverge by more than 0.3% and are not interchangeable with the file's price.
- **The Tokyo session was violent and partially recovered.** The Nikkei opened at 62,973.16, fell almost 5% intraday to 60,835.36 by the 11:30 close and then rallied back to finish 62,188.63, a three-month low and its third consecutive decline. Japan's own 14 movers list therefore mixes genuine repricing with a violent reversal, and the day's close understates the intraday stress.
- **Taiwan's limit moves are genuine prints.** Syntec Technology closed at exactly −9.97% and Systex at −9.90%, both limit-down, in a session where most AI-hardware names rebounded (ASRock +9.91%, Horng Terng limit-up at NT$1,235). A move past −10% would have meant an adjusted limit reference price; these are inside the band.
- **The Stoxx 600 level is quoted two ways.** The Stoxx administrator's 17:00 GMT final value is 657.40 (+1.82%) per the exchange-aggregated wrap and Yahoo; Anadolu Agency quotes 658.02 (+1.91%). The file uses 657.40 and does not publish both.
- **The ATHEX close is sourced from the exchange, not a feed.** There is no Yahoo index symbol for the ATHEX, so the General Index level comes from Euronext Athens' own historical data and cross-checked against Greek press (pelop.gr); yesterday's run noted a TradingEconomics CFD printing 1.4 points away from the official close, so the CFD is not used.
- **Yahoo's daily bars for Japan and Taiwan lag the session by up to two days** (`7203.T` still served the 2 November row). The Asian closes were therefore verified against Yahoo's 5-minute bars instead, which carry the 15:30 / 13:30 closing prints directly.
- **Cross-listings are not deduplicated against the US snapshot.** As the skill already notes, a name listed in two markets appears in both files with different closes.
- **Row count versus yesterday: 4,440 rows today against 3,082 yesterday** — but yesterday's file set had no Japan at all (Culture Day), and Japan contributes 1,380 rows today. Excluding Japan, today is 3,060 against 3,082, a difference of -22 rows, which is market movement rather than missing data.
- **Prices carry the source's precision** (4 decimals, trailing zeros stripped); Alstom's €11.125 half-cent and Grifols' €7.78 preferred line are as printed.

## Source health

| Source | Query / URL | Status | Result |
|---|---|---|---|
| TradingView scanner (per-country) | `POST https://scanner.tradingview.com/{australia,japan,taiwan,canada,germany,france,italy,spain,netherlands,belgium,austria,portugal,ireland,finland,denmark,greece}/scan` with `country` + `type=stock` | `ok` | 16/16 regions HTTP 200, 18,326 stock rows pulled; no rate limiting |
| TradingView scanner (columns) | `name,description,close,open,high,low,volume,change,change_abs,market_cap_basic,exchange,currency,sector,price_earnings_ttm,country` | `ok` | 15 columns for every row; the response carries no `columns` array, so rows are zipped positionally against the request list |
| Yahoo Finance chart API (index levels) | `query1.finance.yahoo.com/v8/finance/chart/{^AXJO,^AORD,^N225,^TWII,^GSPTSE,^GDAXI,^FCHI,FTSEMIB.MI,^IBEX,^AEX,^BFX,^ATX,PSI20.LS,^ISEQ,^OMXH25,^OMXC20,^STOXX}` | `ok` | 17/17 series returned a 4 November bar or a live settled print; `^N225` and `^TWII` had no 4 November *bar* (both had a holiday or a lagging bar) and their close was taken from `regularMarketPrice` at the settled session time (15:45 JST and 13:33 TST respectively) |
| Yahoo Finance chart API (close verification) | 28 symbols across all 16 regions, daily and 5-minute bars | `ok` | **28 of 28 spot-checked closes matched the file to the cent**, including the five Asian names verified on their 15:30 / 13:30 closing bars (Toyota ¥3,028, Mitsui Chemicals ¥1,856.5, Syntec NT$1,490, Systex NT$182, GlobalWafers NT$619, Yamato ¥2,194.5) |
| Yahoo Finance quote page | `finance.yahoo.com/quote/%5EGSPTSE/` | `ok` | TSX "At close 4:20:00 PM EST", 36,341.40 / 35,532.28 — confirms the chart-API close |
| Market-session probe | `market_session_probe.py --region <r> --date 2026-11-04` (16 runs) | `ok` | **16/16 `traded=yes`** with a 4 November last bar — no region skipped |
| Press cross-check | Jiji, AFP, Il Sole 24 Ore, CNA, Focus Taiwan, Taiwan News, Taipei Times, The Age, AFR, Business Recorder, edge consultancy, SquawkNews, Sharecast/HL, Irish Times, Euronext Athens, pelop.gr, ANSA, Euronext/Reuters, Morningstar/Dow Jones, RTTNews, Investing.com, Yahoo Finance, company IR releases | `ok` | 30+ quoted levels and moves matched the snapshot, including every Asian and Canadian close (TAIEX 42,948.91 −358.63; Nikkei 62,188.63 −893.23; TOPIX 3,895.38; TSX 36,341.40; ATHEX 2,662.45 +1.77%; Alpha Bank €4.736 +5.01%; TSMC NT$2,260 −1.53%; MediaTek NT$3,715 +1.09%; Hon Hai NT$240 −2.24%) |
| open.er-api | `https://open.er-api.com/v6/latest/USD` | `ok` | 4 Nov rate table (updated 4 Nov 00:02 UTC), 6 currencies |
| Frankfurter (FX cross-check) | `https://api.frankfurter.app/latest?from=USD` | `ok` | 2026-11-04 rates; agrees within 0.71% on EUR/AUD/CAD/JPY/DKK; no TWD |
| MCP-over-HTTP bridge | `market-recap` / `stocktwits` / `shibui` via `mcp_bridge.py` | `not used` | The scanner supplies every schema field, so no bridge call was needed for the artifact |
| `mcp__tradingview__*`, `mcp__yahoo_finance__*` | — | `unavailable` | Not registered in this runtime (as documented in the cron prompt); the public scanner API replaced them |
| Connector catalog probe | `probe_mcp.py` | `ok` | `catalog_ok total=135 finance_tools=0` — healthy catalog, no financial MCP registered |

## Files

`international-eod/2026-11-04/` — `au.csv`, `ca.csv`, `eu-at.csv`, `eu-be.csv`, `eu-de.csv`, `eu-dk.csv`, `eu-es.csv`, `eu-fi.csv`, `eu-fr.csv`, `eu-gr.csv`, `eu-ie.csv`, `eu-it.csv`, `eu-nl.csv`, `eu-pt.csv`, `jp.csv`, `tw.csv`, `summary.md`, `_manifest.json`, `_excluded.json`, `_carryover.json`

Schema: `date,ticker,name,open,high,low,close,volume,change_pct,market_cap,pe_ratio,sector,currency,exchange`. `ticker` is `EXCHANGE:symbol` (e.g. `XETR:SAP`, `TWSE:2330`, `TSX:RY`). Empty cells mean the source had no value — nothing is imputed. `market_cap` is USD; the prices are in the listing currency named by `currency`.

Integrity checks passed on all 16 files: no non-positive closes, no `high < max(open, close)` or `low > min(open, close)` violations, no `N/A` literals, every row dated 2026-11-04, every row carrying a positive USD market cap, and 28 of 28 independently spot-checked closes matching Yahoo to the cent.

---

Generated by cron #05 at 2026-11-04 16:30 ET (window check passed: weekday, 16:30 ET slot; not a delayed replay — `scheduled_at_ms` 1793827843993 resolves to 2026-11-04). All 16 regions traded; no region was skipped.
