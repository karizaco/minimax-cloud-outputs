# Cron #5 — eod-international-daily — 2026-11-02

Daily EOD snapshot for the 16 international markets the skill covers (AU, JP, TW, CA and the 12 EU venues), written after each market's cash close settled. **4,475 instrument rows across 16 per-region CSVs**, one row per listed instrument, sorted by market cap (USD) descending.

> **Read this first:** `market_cap` is normalised to **USD**, while `close`/`open`/`high`/`low` stay in the **local listing currency** — the `currency` column states which. `change_pct` is TradingView's daily change in percent. Two structural caveats change how the file should be read: (1) TradingView stamps **company-level** market cap on every share class, so a preferred line inherits its parent's cap (`TSX:RY.PR.S` carries Royal Bank's ~$282bn); (2) rows whose market cap the source does not report cannot be screened against a cap floor, so they are **excluded** rather than written with a blank cap — 245 such rows across the set.

## Coverage

| Region | Venues in file | Universe (country filter) | Unique instruments | Written | Floor (USD) | No cap | Off-official rows |
|---|---|---|---|---|---|---|---|
| `au` | ASX | 1,552 | 1,552 | **302** | $300M + vol ≥100k | 4 | 0 |
| `jp` | TSE, NAG, SAPSE | 3,895 | 3,868 | **1,390** | $300M | 3 | 6 |
| `tw` | TWSE, TPEX | 2,333 | 2,333 | **923** | $200M | 56 | 0 |
| `ca` | TSX, TSXV, CSE, NEO | 4,258 | 2,689 | **665** | $200M | 133 | 5 |
| `eu-de` | XETR | 4,301 | 499 | **117** | $300M + vol ≥50k | 3 | 0 |
| `eu-fr` | EURONEXT | 546 | 546 | **260** | $100M | 1 | 0 |
| `eu-it` | MIL | 393 | 393 | **181** | $100M | 2 | 0 |
| `eu-es` | BME | 272 | 272 | **146** | $100M | 35 | 0 |
| `eu-nl` | EURONEXT | 77 | 77 | **56** | $100M | 0 | 0 |
| `eu-be` | EURONEXT | 99 | 99 | **76** | $100M | 1 | 0 |
| `eu-at` | VIE | 66 | 66 | **51** | $100M | 3 | 0 |
| `eu-pt` | EURONEXT | 31 | 31 | **27** | $50M | 0 | 0 |
| `eu-ie` | EURONEXT | 19 | 19 | **17** | $200M | 0 | 0 |
| `eu-fi` | OMXHEX | 187 | 187 | **101** | $100M | 3 | 0 |
| `eu-dk` | OMXCOP | 134 | 134 | **76** | $100M | 1 | 0 |
| `eu-gr` | ATHEX | 128 | 128 | **87** | $50M | 0 | 0 |
| **total** | | **18,291** | | **4,475** | | **245** | **11** |

`Universe` is every instrument the source returns for that country's own listings; `Unique instruments` collapses instruments quoted on several venues of the same market down to one row; `Written` applies the skill's per-region USD market-cap floor (`screener_filters.filters_for_region`).

## Market context

Settled closes, verified against the close and not an intraday print:

| Index | Close | Change | Day | Source |
|---|---|---|---|---|
| STOXX 600 | 649.44 | +2.69 / +0.42% | up | Anadolu (close), Sharecast 649.65 +0.45% |
| DAX | 25,981.09 | +0.63% | up | Anadolu, Valor |
| CAC 40 | 8,047.69 | +0.98% | up | Anadolu, Valor |
| FTSE 100 | 10,761.33 | +0.29% | up | Anadolu, Valor |
| FTSE MIB | 49,947.94 | +0.90% | up | Anadolu |
| Nikkei 225 | 63,081.86 | −208.25 / −0.33% | down | News On Japan, AP, DPA |
| TOPIX | 3,930.28 | −34.79 / −0.88% | down | News On Japan |
| TAIEX | level not verified | −0.7% | down | AP |
| ASX 200 | 8,856.50 | −51.6 / −0.58% | down | DPA, AP, Samso |
| All Ordinaries | 8,977.20 | −0.53% | down | DPA, The Age |
| Kospi | 5,859.08 | +2.24% | up | DPA, AP (context only — not a covered region) |

Two sessions, two opposite drivers. **Europe closed higher on collapsing oil**: renewed US–Iran diplomacy pushed Brent down ~7% to $104.74 and WTI ~7.3% to $96.52, which lifted the STOXX 600 to a two-month high (its best close since 7 September) via airlines and travel names while the energy sector gave up 1%. **Japan went the other way** as Kioxia's cautious outlook reopened the AI-capex question: the Nikkei fell 0.33% but the broader TOPIX fell 0.88%, with Kioxia −15.8% and SCREEN Holdings −19% dragging the capital-goods complex while Tokyo Electron (+5.16% to ¥10,005 on upbeat earnings and a ¥150bn buyback) and Advantest offset part of it. **Australia fell ahead of the RBA decision** on Tuesday 3 November, which the market has priced as a fifth 25bp hike of the year, with gold miners hit by bullion slipping below $4,000/oz.

**Internal cross-check:** this snapshot's own cap-weighted averages land on the published index moves — JP −0.91% vs TOPIX −0.88%, AU −0.52% vs ASX 200 −0.58%, EU +0.73% vs STOXX 600 +0.42%, TW −0.62% vs TAIEX −0.7%. The snapshot is consistent with the settled closes, not with an intraday read.

Regional breadth from the snapshot itself (median `change_pct` per file):

| Region | Rows | Median | Up / down / flat | Min | Max | Cap-weighted |
|---|---|---|---|---|---|---|
| `au` | 302 | −0.22% | 120 / 157 / 25 | −13.94% | +10.34% | −0.52% |
| `jp` | 1,390 | −0.38% | 510 / 847 / 33 | −18.96% | +21.23% | −0.91% |
| `tw` | 923 | +0.00% | 392 / 449 / 82 | −10.83% | +16.02% | −0.62% |
| `ca` | 665 | +0.00% | 317 / 282 / 66 | −13.39% | +17.16% | −0.05% |
| `eu-de` | 117 | +1.18% | 87 / 28 / 2 | −20.72% | +7.38% | +0.59% |
| `eu-fr` | 260 | +0.36% | 140 / 95 / 25 | −38.09% | +8.06% | +0.78% |
| `eu-it` | 181 | +0.52% | 114 / 50 / 17 | −3.73% | +7.92% | +0.77% |
| `eu-es` | 146 | +0.00% | 72 / 26 / 48 | −5.23% | +10.16% | +1.52% |
| `eu-nl` | 56 | +0.98% | 40 / 14 / 2 | −2.20% | +11.98% | +0.28% |
| `eu-be` | 76 | +0.48% | 51 / 15 / 10 | −4.51% | +5.81% | +1.24% |
| `eu-at` | 51 | +0.46% | 30 / 15 / 6 | −10.61% | +11.35% | +0.32% |
| `eu-pt` | 27 | +0.00% | 9 / 9 / 9 | −2.21% | +2.04% | −0.43% |
| `eu-ie` | 17 | +0.56% | 12 / 2 / 3 | −3.12% | +5.24% | +1.49% |
| `eu-fi` | 101 | +0.23% | 56 / 37 / 8 | −6.36% | +12.60% | +0.32% |
| `eu-dk` | 76 | +0.55% | 42 / 29 / 5 | −5.47% | +8.42% | +0.76% |
| `eu-gr` | 87 | −0.14% | 23 / 46 / 18 | −6.25% | +4.33% | −1.05% |

Europe's median name is up in 9 of 12 EU venues while Japan's median name fell — the day's single cleanest structural split.

## Top movers

Largest absolute daily moves among liquid names (volume ≥ 100k and market cap ≥ $1B), 1,773 of 4,475 rows qualify:

| Region | Ticker | Name | Change | Close | Volume | Mkt cap (USD) | Catalyst |
|---|---|---|---|---|---|---|---|
| eu-fr | `EURONEXT:ALO` | Alstom SA | −26.09% | 11.685 EUR | 13,956,568 | $8.16B | Second guidance cut of the year: FY margin outlook slashed, H1 operating profit missed, **negative free cash flow** now expected for the year (was positive); Coradia Max execution and production problems in Germany; sales-growth guidance cut to 2–4% from ~5%. Opened as low as −31% intraday |
| jp | `TSE:7735` | SCREEN Holdings Co., Ltd. | −18.96% | 9,218 JPY | 8,753,800 | $13.47B | April–September operating profit missed expectations; full-year guidance **kept unchanged** despite record order intake — a credibility problem for a wet-clean equipment leader in the AI capex chain |
| jp | `TSE:6370` | Kurita Water Industries Ltd. | −17.71% | 4,647 JPY | 790,200 | $3.82B | No company-specific release found; second consecutive deep fall (−20.99% on Friday), so this is a continuation rather than a fresh event |
| jp | `TSE:285A` | Kioxia Holdings Corporation | −15.78% | 11,345 JPY | 97,833,400 | $140.76B | Cautious outlook from the memory maker raised the concern that AI-driven demand growth is beginning to moderate; the single biggest drag on the Nikkei |
| jp | `TSE:6960` | Fukuda Denshi Co., Ltd. | −14.64% | 9,740 JPY | 162,000 | $2.09B | No company-specific release found; Japan capital-goods de-rating |
| jp | `TSE:9301` | Mitsubishi Logistics Corporation | −14.00% | 1,293.5 JPY | 4,878,000 | $3.39B | No company-specific release found; press reports the same move at −14.10% |
| au | `ASX:SBM` | St Barbara Ltd. | −13.94% | 0.71 AUD | 33,315,877 | $0.71B | Canada's Impact Assessment Agency will require a "duplicative" federal assessment for the 15-Mile Processing Hub in Nova Scotia; Nova Scotia approved the Touquoy mill restart (first ore 3 Nov); maiden underground resource of 0.5moz Au at Old Austen and an on-market buy-back of up to 100m shares |
| jp | `TSE:4768` | OTSUKA CORPORATION | −12.04% | 3,828 JPY | 5,424,400 | $10.49B | No company-specific release found |

Largest mover per region among liquid names:

| Region | Ticker | Name | Change |
|---|---|---|---|
| au | `ASX:SBM` | St Barbara Limited | −13.94% |
| jp | `TSE:7735` | SCREEN Holdings Co., Ltd. | −18.96% |
| tw | `TPEX:3644` | Linco Technology Co., Ltd. | +13.87% |
| ca | `TSX:BTE` | Baytex Energy Corp. | −11.04% |
| eu-de | `XETR:IXX` | init innovation in traffic systems SE | −20.72% |
| eu-fr | `EURONEXT:ALO` | Alstom SA | −26.09% |
| eu-it | `MIL:WIIT` | WIIT SpA | −3.73% |
| eu-es | `BME:ART` | Arteche Lantegi Elkartea SA | −5.23% |
| eu-nl | `EURONEXT:AD` | Koninklijke Ahold Delhaize N.V. | −2.20% |
| eu-be | `EURONEXT:CMBT` | CMB.TECH NV | −4.51% |
| eu-at | `VIE:PYT` | POLYTEC HOLDING AG | −10.61% |
| eu-pt | `EURONEXT:GALP` | Galp Energia, SGPS S.A. Class B | −2.21% |
| eu-ie | `EURONEXT:MIO` | Mincon Group PLC | −3.12% |
| eu-fi | `OMXHEX:YIT` | YIT Oyj | −6.36% |
| eu-dk | `OMXCOP:GMAB` | Genmab A/S | −5.47% |
| eu-gr | `ATHEX:DAIOS` | Daios Plastics S.A. | −6.25% |

## Method

1. **Universe** — the skill's `mcp__tradingview-advanced__stock_screener(country=…)` is not registered in the Cloud runtime. The same underlying source is reachable over its public per-country scanner API, so each region was pulled with a `country` filter matching the instrument's own country of primary listing. Without that filter the per-country endpoint also returns *foreign* stocks quoted on that market's venues (NVIDIA, Apple and even SpaceX on Lang & Schwarz with WKN-style symbols), which would have inflated Germany from ~500 companies to 36,185 rows.
2. **Venue selection** — one row per instrument, preferring the official listing venue (XETR, TSE, TSX/TSXV, TWSE/TPEX, MIL, BME, VIE, OMXHEX, OMXCOP, ATHEX, EURONEXT, ASX), then the highest-volume print. Germany needs its own company key: Lang & Schwarz carries the same share under a WKN symbol (`LSX:750000` = thyssenkrupp's `TKA`), so German rows are deduped by company description — 4,301 raw rows collapse to 499 companies. Elsewhere the key is (description, ticker root), which keeps genuine share classes apart: `MFC` vs `MFC.PR.K`, `FFH` vs `FFH.U`, `SGR.U` vs `SGR.UN`, `DHT.U` vs `DHT.UN`, `HOT.U` vs `HOT.UN`, `CACR` vs `CACR.A`, and Japan's two unrelated companies both called "JTEC Corporation" (2479 / 3446) all survive as separate rows.
3. **Enrichment** — `volume`, `pe_ratio` and `sector` come straight from the same scanner response, so the skill's Yahoo `compare_stocks` enrichment stage was **not needed and was skipped** (Yahoo's JSON endpoints also return HTTP 429 from this egress).
4. **Market cap** — `market_cap_basic` is in the row's **local** currency, so every value is converted to USD with the 2 Nov open.er-api rate table (EUR 0.896073, AUD 1.422744, CAD 1.396839, JPY 157.532149, DKK 6.693558, TWD 32.636828 per USD; updated 2 Nov 00:02 UTC). Frankfurter agrees within 0.5% on every currency it carries (EUR 0.89158, AUD 1.4269, CAD 1.3974, JPY 157.9, DKK 6.6634; it has no TWD). Sanity-checked against implied share counts (local cap ÷ local close): SAP 1.17bn, Toyota 11.92bn, TSMC 26.38bn, Royal Bank 1.38bn, Alstom 0.63bn, TFI 0.080bn, Amplifon 0.265bn — all plausible.
5. **Change column** — the scanner's `change` field is already in **percent units** (0.0695 means +0.0695%), not a fraction. This was proven, not assumed: across all 4,475 written rows, `close − close/(1 + change/100)` reproduces `change_abs` exactly (total error 0.000000, mean 2.7e-14), and 4,442 of the 4,448 tickers present in both today's and Friday's file satisfy `30 Oct close × (1 + change/100) = 2 Nov close`. Multiplying by 100 would have inflated every move in this file by 100×.
6. **Movers mode** — the skill's Tue–Thu forward-fill optimisation was **not applied** (it runs Mon–Thu only, and forward-filling would stamp yesterday's closes with today's date and a `change_pct` of 0, which is wrong for a file whose whole purpose is the daily move). Every row here is a real 2026-11-02 print.

## Caveats

- **Share-class market caps are company-level.** TradingView replicates one cap across every line of a company, so preferred and unit lines carry their parent's cap and all clear the same floor. `TSX:RY.PR.S` shows Royal Bank's ~$282bn, not the preferred line's own value. This inflates the apparent size of Canadian and German preferreds.
- **245 rows have no market cap and were excluded** (133 Canada, 56 Taiwan, 35 Spain, 4 Australia, 4 Germany, 3 Japan, 3 Austria, 3 Finland, 2 Italy, 1 France, 1 Belgium, 1 Denmark). A row with no cap cannot be tested against a cap floor, so writing it would have put an unscreenable row in a screened file. The composition differs by region: the Canadian ones are preferred and share-class lines where the source publishes no company cap; the Taiwanese ones are small TPEx names; the Spanish ones are zero-volume SICAV and fund lines quoted on BME.
- **13 rows carry a stale `change_pct`.** Their close is identical to 30 Oct but the source's change column is non-zero, i.e. the instrument did not trade today and the change value is left over from an earlier session (`EURONEXT:CROS`, `EURONEXT:HYDRA`, `EURONEXT:CBSM`, `TPEX:8917`, `VIE:BTS` and 8 others, on volumes of 3–20,000 shares). A further 359 rows show a change of exactly 0.00% — genuine no-trade prints, not missing data.
- **One market cap is materially overstated.** `ASX:BHP` implies 5.16bn shares against a real count near 2.13bn, so BHP's market cap reads ~$206bn instead of ~$86bn. Every other checked name lands on a plausible share count. The field is written as the source reports it, but a cap-based screen will treat BHP as a mega-cap when it is not.
- **Regional Japanese venues carry stale prints.** 6 written rows come from Nagoya (NAG) and Sapporo (SAPSE) rather than TSE. Those venues routinely show a wrong prior close on a thin book — e.g. `NAG:6623` printed −0.95% on 15,800 shares. Every one of those names was resolved to its TSE row; the 6 that remain are NAG/SAPSE-only listings with no TSE twin. Five Canadian rows likewise come from off-official venues (4 CSE, 1 NEO), where prints can diverge from the official close.
- **Two TPEx moves exceed the nominal ±10% band, and both are genuine prints.** `TPEX:3595` Alliance Material closed +16.02% (NT$804 from NT$693) and `TPEX:7911` Apollo Power closed −10.83% (NT$107 from NT$120); Yahoo independently confirms both settled closes to the cent. A move past ±10% means the exchange's limit reference price was adjusted for a capital action rather than the prior close, so the band did not bind — these are not data errors. The TSE has had no daily limit for large caps since Oct 2024, so Japan's −18.96% print is a genuine repricing.
- **Cross-listings are not deduplicated against the US snapshot.** As the skill already notes, a name listed in two markets appears in both files with different closes.
- **Yesterday's row count was 4,486; today's is 4,475.** The gap is market movement, not missing data: every region's count is within a handful of rows of 30 Oct (AU −1, JP −3, TW −9, CA −3, DE +2, FR and FI identical, DK +1), and 4,442 of the 4,448 overlapping tickers chain exactly from Friday's close to today's.
- **Alstom's close carries a half-cent.** The scanner prints 11.685 EUR where Yahoo rounds the settled close to 11.69; the file keeps the source's precision.

## Source health

| Source | Query / URL | Status | Result |
|---|---|---|---|
| TradingView scanner (per-country) | `POST https://scanner.tradingview.com/{australia,japan,taiwan,canada,germany,france,italy,spain,netherlands,belgium,austria,portugal,ireland,finland,denmark,greece}/scan` | `ok` | 16/16 regions HTTP 200, 18,291 stock rows pulled (0.07–0.24 s per call, no rate limit) |
| TradingView scanner (columns) | `name,description,close,open,high,low,change,volume,market_cap_basic,exchange,currency,sector,price_earnings_ttm,change_abs,pricescale,minmov,type,country` | `ok` | 18 columns returned for every row; response carries no `columns` array, so rows are zipped positionally against the request list |
| Yahoo Finance HTML (verification) | `finance.yahoo.com/quote/{7203.T,SAP.DE,2330.TW,RY.TO,BHP.AX,RYA.IR,3595.TWO,7911.TWO}/` | `ok` | 8/8 settled closes matched the CSV, each dated 2 Nov: Toyota ¥3,051 (prev ¥3,070), SAP €210.50 (prev €211.25), TSMC NT$2,330 (prev NT$2,370), RY C$286.21 (prev C$283.93), BHP A$56.74 (prev A$57.56), Ryanair €24.10 (prev €22.90), Alliance Material NT$804 (prev NT$693), Apollo Power NT$107 (prev NT$120) |
| Press cross-check | Reuters, Anadolu, Sharecast, Valor, News On Japan, AP, DPA, Adalytica, Samso, The Age, Newsquawk | `ok` | 14/14 quoted moves matched the snapshot: STOXX 600 649.44 +0.42%, DAX 25,981.09 +0.63%, CAC 40 8,047.69 +0.98%, FTSE 100 10,761.33 +0.29%, Nikkei 63,081.86 −0.33%, TOPIX 3,930.28 −0.88%, ASX 200 8,856.50 −0.58%, Kioxia −15.8%, SCREEN −19%, SoftBank −1.6%, Alps Alpine −10.96%, Takara +11.06%, St Barbara −13.94% to A$0.71, BHP −1.42% |
| open.er-api | `https://open.er-api.com/v6/latest/USD` | `ok` | 2 Nov rate table (updated 2 Nov 00:02 UTC), 6 currencies |
| Frankfurter (FX cross-check) | `https://api.frankfurter.app/latest?from=USD` | `ok` | Agrees within 0.5% on EUR/AUD/CAD/JPY/DKK; no TWD rate |
| MCP-over-HTTP bridge | `market-recap get_quotes` via `mcp_bridge.py` | `429 rate-limited` | The pack returned "Today's 50 free anonymous calls are used up" — a rate limit, not an absent source. The scanner supplies every schema field, so no bridge call was needed for the artifact |
| Yahoo Finance JSON API | chart / spark / screener | `429 rate-limited` | not used — the scanner supplies every schema field, so no Yahoo enrichment call was made |
| `mcp__tradingview__*`, `mcp__yahoo_finance__*` | — | `unavailable` | not registered in this runtime (as documented in the cron prompt); the public scanner API replaced them |
| Connector catalog probe | `probe_mcp.py` | `ok` | `catalog_ok total=133 finance_tools=0` — healthy catalog, no financial MCP registered |

## Files

`international-eod/2026-11-02/` — `au.csv`, `ca.csv`, `eu-at.csv`, `eu-be.csv`, `eu-de.csv`, `eu-dk.csv`, `eu-es.csv`, `eu-fi.csv`, `eu-fr.csv`, `eu-gr.csv`, `eu-ie.csv`, `eu-it.csv`, `eu-nl.csv`, `eu-pt.csv`, `jp.csv`, `tw.csv`, `summary.md`

Schema: `date,ticker,name,open,high,low,close,volume,change_pct,market_cap,pe_ratio,sector,currency,exchange`. `ticker` is `EXCHANGE:symbol` (e.g. `XETR:SAP`, `TSE:7203`, `TSX:RY`). Empty cells mean the source had no value — nothing is imputed.

Integrity checks passed on all 16 files: no non-positive closes, no `high < max(open, close)` or `low > min(open, close)` violations, no `N/A` literals, every row dated 2026-11-02, every row carrying a positive USD market cap. Price formatting (4 decimals, trailing zeros stripped) reproduces all 17,944 price strings in the published 30 Oct file byte-for-byte.

---

Generated by cron #5 at 2026-11-02 16:32 EST (window check passed: weekday, 16:30 ET slot; not a delayed replay — `scheduled_at_ms` resolves to the same date). No region was skipped for a holiday — 2026-11-02 is a trading day in all 16 markets.
