# Cron #5 — eod-international-daily — 2026-10-28

Daily EOD snapshot for the 16 international markets the skill covers (AU, JP, TW, CA and the 12 EU venues), written after each market's cash close settled. **4,876 instrument rows across 16 per-region CSVs**, one row per listed instrument, sorted by market cap (USD) descending.

> **Read this first:** `market_cap` is normalised to **USD** (the skill's own filter spec is USD-based), while `close`/`open`/`high`/`low` stay in the **local listing currency** — the `currency` column states which. `change_pct` is TradingView's daily change, and on a corporate-action day (reverse split, subscription-receipt conversion, listing debut) that field can reflect the adjustment rather than a real session move. Both cases seen today are flagged in *Caveats*.

## Coverage

| Region | Venue | Universe (country filter) | After venue dedupe | Written (above floor) | Floor (USD) | Non-official venue rows |
|---|---|---|---|---|---|---|
| `au` | ASX | 1,558 | 1,558 | **327** | $300M | 0 |
| `ca` | TSX, TSXV | 2,692 | 2,692 | **799** | $200M | 18 |
| `eu-at` | VIE | 65 | 65 | **53** | $100M | 0 |
| `eu-be` | EURONEXT | 102 | 102 | **77** | $100M | 0 |
| `eu-de` | XETR, GETTEX | 924 | 502 | **239** | $300M | 29 |
| `eu-dk` | OMXCOP | 134 | 134 | **76** | $100M | 0 |
| `eu-es` | BME | 272 | 272 | **180** | $100M | 0 |
| `eu-fi` | OMXHEX | 186 | 186 | **104** | $100M | 0 |
| `eu-fr` | EURONEXT | 545 | 545 | **260** | $100M | 0 |
| `eu-gr` | ATHEX | 128 | 128 | **86** | $50M | 0 |
| `eu-ie` | EURONEXT | 19 | 19 | **17** | $200M | 0 |
| `eu-it` | MIL | 393 | 393 | **183** | $100M | 0 |
| `eu-nl` | EURONEXT | 77 | 77 | **55** | $100M | 0 |
| `eu-pt` | EURONEXT | 31 | 31 | **27** | $50M | 0 |
| `jp` | TSE, NAG | 3,868 | 3,868 | **1,399** | $300M | 5 |
| `tw` | TWSE, TPEX | 2,330 | 2,330 | **994** | $200M | 0 |
| **total** | | | | **4,876** | | |

`Universe` is the count of instruments the source returns for that country's own listings; `After venue dedupe` collapses instruments listed on several venues of the same market down to one row; `Written` applies the skill's per-region USD market-cap floor (`screener_filters.filters_for_region`).

## Top movers

Largest absolute daily moves among liquid names (volume ≥ 100k and market cap ≥ $1B), 1,773 of 4,876 rows qualify:

| Region | Ticker | Name | Change | Close | Volume | Mkt cap (USD) |
|---|---|---|---|---|---|---|
| au | `ASX:WCN` | White Cliff Minerals Limited | +1900.00% | 0.44 AUD | 315,996 | $1.22B |
| eu-dk | `OMXCOP:GMAB` | Genmab A/S | +29.06% | 3868 DKK | 800,296 | $26.71B |
| jp | `TSE:2737` | Tomen Devices Corp. | -21.57% | 25450 JPY | 1,235,000 | $1.40B |
| eu-de | `XETR:TKA` | thyssenkrupp AG | -16.93% | 12.19 EUR | 6,241,464 | $10.18B |
| jp | `TSE:5344` | MARUWA CO., LTD. | +14.89% | 54000 JPY | 482,900 | $3.67B |
| jp | `TSE:285A` | Kioxia Holdings Corporation | +13.76% | 14340 JPY | 107,607,100 | $131.42B |
| eu-nl | `EURONEXT:ADYEN` | Adyen NV | -13.35% | 818 EUR | 608,947 | $33.34B |
| jp | `TSE:4588` | Oncolys BioPharma, Inc. | +13.18% | 7900 JPY | 2,348,900 | $1.31B |
| jp | `TSE:9697` | Capcom Co., Ltd. | -12.44% | 3835 JPY | 9,195,700 | $11.60B |
| eu-fi | `OMXHEX:SANOMA` | Sanoma Oyj | -11.84% | 9.31 EUR | 315,583 | $1.92B |
| jp | `TSE:6834` | Seikoh Giken Co., Ltd. | +11.01% | 6150 JPY | 971,900 | $1.63B |
| eu-de | `XETR:SY1` | Symrise AG | -10.24% | 89.8 EUR | 988,593 | $15.58B |
| tw | `TWSE:3189` | Kinsus Interconnect Technology Cor | +9.99% | 1035 TWD | 18,392,492 | $15.28B |
| tw | `TPEX:3260` | ADATA Technology Co., Ltd. | +9.98% | 363.5 TWD | 10,933,607 | $3.56B |
| tw | `TWSE:3006` | Elite Semiconductor Microelectroni | +9.98% | 275.5 TWD | 19,329,933 | $2.20B |

Two rows dominate the raw mover list and are **not** real session moves:

- `ASX:WCN` (White Cliff Minerals) at +1,900% — the ASX shows A$0.029 (+7.4%); the company did a **1-for-20 reverse split effective 28 Oct 2026**, and the source compares the split-adjusted price against the unadjusted prior close.
- `CSE:FLY` (LUNR Aerospace) at +204% — a **new CSE listing that began trading 27 Oct 2026** after subscription-receipt conversion; the reference price is the 0.75 conversion price, while the actual session range was 5.00 → 2.28.

Largest mover per region among liquid names:

| Region | Ticker | Name | Change |
|---|---|---|---|
| au | `ASX:WCN` | White Cliff Minerals Limited | +1900.00% |
| eu-dk | `OMXCOP:GMAB` | Genmab A/S | +29.06% |
| jp | `TSE:2737` | Tomen Devices Corp. | -21.57% |
| eu-de | `XETR:TKA` | thyssenkrupp AG | -16.93% |
| eu-nl | `EURONEXT:ADYEN` | Adyen NV | -13.35% |
| eu-fi | `OMXHEX:SANOMA` | Sanoma Oyj | -11.84% |
| tw | `TWSE:3189` | Kinsus Interconnect Technology C | +9.99% |
| ca | `TSX:BHC` | Bausch Health Companies Inc. | +9.02% |
| eu-it | `MIL:TGYM` | Technogym S.p.A | +8.03% |
| eu-es | `BME:ANE` | Corporacion Acciona Energias Ren | -6.27% |
| eu-fr | `EURONEXT:DSY` | Dassault Systemes SE | -4.50% |
| eu-gr | `ATHEX:TPEIR` | Piraeus Bank S.A. | +4.06% |
| eu-ie | `EURONEXT:BIRG` | Bank of Ireland Group PLC | +3.85% |
| eu-be | `EURONEXT:MELE` | Melexis NV | -3.47% |
| eu-at | `VIE:VOE` | voestalpine AG | -2.31% |
| eu-pt | `EURONEXT:NVG` | Navigator Company SA | +1.86% |

## Method

1. **Universe** — the skill's `mcp__tradingview-advanced__stock_screener(country=…)` is not registered in the Cloud runtime. The same underlying source is reachable over its public per-country scanner API, so each region was pulled with a `country` filter matching the instrument's own country of primary listing. Without that filter the per-country endpoint also returns *foreign* stocks quoted on that market's venues (NVIDIA, Apple and even SpaceX on Lang & Schwarz with WKN-style symbols), which would have inflated Germany from ~500 companies to 36,006 rows. With the filter, every region lands on its real listed-company count (Athens 128, Madrid 272, Vienna 65, Dublin 19, Helsinki 186, Copenhagen 134, Euronext Paris 545, Borsa Italiana 393, TSE 3,758, TWSE 1,082, ASX 1,558).
2. **Venue dedupe** — one row per instrument, preferring the official listing venue (XETR/FWB, TSE, TSX/TSXV, TWSE/TPEX, MIL, BME, VIE, OMXHEX, OMXCOP, ATHEX, EURONEXT, ASX), then the highest-volume row. Germany needs one extra rule: Lang & Schwarz (LS/LSX) carries the *same* shares under WKN-style symbols (`LSX:716460` = SAP SE) with visibly worse prints, so a company already covered by an official venue drops its off-exchange row. Distinct German share classes keep their own description (`METRO AG` vs `METRO AG Pref Bearer Shs`) and survive, as do Canadian preferred lines (`MFC` vs `MFC.PR.K`).
3. **Enrichment** — `volume`, `pe_ratio` and `sector` come straight from the same scanner response, so the skill's Yahoo `compare_stocks` enrichment stage was **not needed and was skipped** (it is also unreachable here — Yahoo's JSON endpoints return HTTP 429 from this egress). Schema coverage: volume non-zero on 4,732/4,876 rows, `pe_ratio` on 3,865, `sector` on 4,875.
4. **Movers mode** — the skill's Tue–Thu forward-fill optimisation was **not applied**: it needs the previous day's CSV, and this is the first run to write the `international-eod/` path (the repo had no prior artifact). Forward-filling would also stamp stale closes with today's date and a `change_pct` of 0. A full fresh pull costs 16 HTTP calls here, so every row is a real 2026-10-28 print.
5. **Market cap** — `market_cap_basic` is in the row's **local** currency, so every value is converted to USD with the 28 Oct open.er-api rate table (EUR 0.897453, AUD 1.422618, CAD 1.404056, JPY 157.892678, DKK 6.706467, TWD 32.438942 per USD). Frankfurter agrees on all five currencies it covers to within 0.10% (TWD is not an ECB currency and is single-sourced).

## Caveats

- **Off-exchange venue rows.** 47 rows across the set (29 Germany, 18 Canada) come from secondary venues — Lang & Schwarz / GETTEX for German names that have no Xetra listing, and Cboe Canada / CSE for Canadian names with no TSX/TSXV listing. Those prints are thinner and can lag the official close; the `exchange` column identifies them.
- **Corporate actions distort `change_pct`** — reverse splits (ASX:WCN today), subscription-receipt conversions and listing debuts (CSE:FLY) produce changes that are not session moves. The `open` column is the cleanest tell: `CSE:FLY` shows open 5.00 against a 0.75 reference price.
- **Regional Japanese venues.** 5 rows come from Nagoya / Sapporo rather than TSE. Those venues carry thin volume and have previously shown stale prior closes, so treat their `change_pct` as indicative.
- **Two rows have an empty `change_pct` and `market_cap`** (`ASX:JRL`, `NEO:AIOS`) — the source returned no reference price for them. Every other row has a parseable change, and no row has a non-positive close, and no row violates high ≥ max(open, close) / low ≤ min(open, close).
- **Cross-listings are not deduplicated against the US snapshot.** As the skill already notes, a name listed in two markets appears in both files with different closes.

## Source health

| Source | Query / URL | Status | Result |
|---|---|---|---|
| TradingView scanner (per-country) | `POST https://scanner.tradingview.com/{australia,japan,taiwan,canada,germany,france,italy,spain,netherlands,belgium,austria,portugal,ireland,finland,denmark,greece}/scan` | `ok` | 16/16 regions HTTP 200, 48,423 rows pulled, `country` filter applied on the second pass |
| TradingView scanner (columns) | `name,description,close,open,high,low,volume,change,change_abs,market_cap_basic,exchange,currency,sector,price_earnings_ttm,dividends_yield,country,type` | `ok` | all 17 columns returned values for every row |
| Yahoo Finance HTML (verification only) | `finance.yahoo.com/quote/{7203.T,SAP.DE,RY.TO,2330.TW}/` | `ok` | 4/4 quotes matched the CSV to the cent (Toyota 3,051 / 3,102; SAP €211.20 / €213.15; RY C$286.41 / C$285.46; TSMC NT$2,425 / NT$2,400) |
| shibui MCP bridge (verification only) | `shibui.stock_data_query` on RY, BHP, SAP, SHOP | `ok` | prior-session closes matched the implied prior close of the source within ~1% (EUR/USD, AUD/USD, CAD/USD applied) |
| open.er-api | `https://open.er-api.com/v6/latest/USD` | `ok` | 2026-10-28 rate table, 6 currencies |
| Frankfurter | `https://api.frankfurter.app/latest?from=USD` | `ok` | cross-check, agrees with open.er-api within 0.10% on EUR/AUD/CAD/JPY/DKK; no TWD |
| Yahoo Finance JSON API | chart / spark / screener | `429 rate-limited` | not used — the scanner supplies every schema field, so no Yahoo enrichment call was made |
| `mcp__tradingview__*`, `mcp__yahoo_finance__*` | — | `unavailable` | not registered in this runtime (as documented in the cron prompt); the public scanner API replaced them |

## Files

`international-eod/2026-10-28/` — `au.csv`, `ca.csv`, `eu-at.csv`, `eu-be.csv`, `eu-de.csv`, `eu-dk.csv`, `eu-es.csv`, `eu-fi.csv`, `eu-fr.csv`, `eu-gr.csv`, `eu-ie.csv`, `eu-it.csv`, `eu-nl.csv`, `eu-pt.csv`, `jp.csv`, `tw.csv`, `summary.md`

Schema: `date,ticker,name,open,high,low,close,volume,change_pct,market_cap,pe_ratio,sector,currency,exchange`. `ticker` is `EXCHANGE:symbol` (e.g. `XETR:SAP`, `TSE:7203`, `TSX:RY`). Empty cells mean the source had no value — nothing is imputed.

---

Generated by cron #5 at 2026-10-28 16:39 EDT (window check passed: weekday, 16:30 ET slot). No region was skipped for a holiday — 2026-10-28 is a trading day in all 16 markets (Athens' Ochi Day was 27 Oct).
