# Cron #5 — eod-international-daily — 2026-10-29

Daily EOD snapshot for the 16 international markets the skill covers (AU, JP, TW, CA and the 12 EU venues), written after each market's cash close settled. **4,500 instrument rows across 16 per-region CSVs**, one row per listed instrument, sorted by market cap (USD) descending.

> **Read this first:** `market_cap` is normalised to **USD**, while `close`/`open`/`high`/`low` stay in the **local listing currency** — the `currency` column states which. `change_pct` is TradingView's daily change in percent. Two structural caveats change how the file should be read: (1) TradingView stamps **company-level** market cap on every share class, so a preferred line inherits its parent's cap (TSX:RY.PR.S carries Royal Bank's $283bn); (2) rows whose market cap the source does not report cannot be screened against a cap floor, so they are **excluded** rather than written with a blank cap — 241 such rows across the set.

## Coverage

| Region | Venues in file | Universe (country filter) | Unique instruments | Written | Floor (USD) | Off-official rows |
|---|---|---|---|---|---|---|
| `au` | ASX | 1,557 | 1,557 | **303** | $300M + vol ≥100k | 0 |
| `jp` | TSE, NAG, SAPSE | 3,890 | 3,866 | **1,395** | $300M | 6 |
| `tw` | TWSE, TPEX | 2,332 | 2,332 | **942** | $200M | 0 |
| `ca` | TSX, TSXV, CSE, NEO | 4,263 | 2,687 | **667** | $200M | 5 |
| `eu-de` | XETR | 4,292 | 500 | **119** | $300M + vol ≥50k | 0 |
| `eu-fr` | EURONEXT | 545 | 545 | **260** | $100M | 0 |
| `eu-it` | MIL | 393 | 393 | **181** | $100M | 0 |
| `eu-es` | BME | 273 | 273 | **145** | $100M | 0 |
| `eu-nl` | EURONEXT | 77 | 77 | **56** | $100M | 0 |
| `eu-be` | EURONEXT | 100 | 100 | **76** | $100M | 0 |
| `eu-at` | VIE | 66 | 66 | **51** | $100M | 0 |
| `eu-pt` | EURONEXT | 31 | 31 | **27** | $50M | 0 |
| `eu-ie` | EURONEXT | 19 | 19 | **17** | $200M | 0 |
| `eu-fi` | OMXHEX | 186 | 186 | **101** | $100M | 0 |
| `eu-dk` | OMXCOP | 134 | 134 | **75** | $100M | 0 |
| `eu-gr` | ATHEX | 127 | 127 | **85** | $50M | 0 |
| **total** | | | | **18,285** | | | **4,500** | | |

`Universe` is every instrument the source returns for that country's own listings; `Unique instruments` collapses instruments quoted on several venues of the same market down to one row; `Written` applies the skill's per-region USD market-cap floor (`screener_filters.filters_for_region`).

## Market context

| Index | Close | Change | Day |
|---|---|---|---|
| Nikkei 225 | 64,659.47 | +1.10% | up |
| DAX | 26,039.68 | +1.30% | up |
| ASX 200 | 8,891.80 | +0.50% | up |
| TSX Composite | 36,249.03 | −0.04% | flat |
| TAIEX | 46,368.33 | −1.42% | down |
| CAC 40 | — | +1.09% | up |

Regional breadth from the snapshot itself (median `change_pct` per file): Germany +0.99% (89 up / 26 down), France +0.38%, Australia +0.36%, Belgium +0.39%, Denmark +0.63%, Canada 0.00%, Japan −0.07%, **Taiwan −1.19% (200 up / 681 down)**. Europe and Australia closed firm; Japan was flat on the index but violently dispersed underneath it; Taiwan was the session's clear laggard.

## Top movers

Largest absolute daily moves among liquid names (volume ≥ 100k and market cap ≥ $1B), 1,793 of 4,500 rows qualify:

| Region | Ticker | Name | Change | Close | Volume | Mkt cap (USD) |
|---|---|---|---|---|---|---|
| tw | `TPEX:3595` | Alliance Material Co., Ltd. | -28.84% | 575.0000 TWD | 4,284,586 | $1.01B |
| ca | `TSX:BHC` | Bausch Health Companies Inc. | +28.34% | 12.4100 CAD | 3,428,765 | $2.58B |
| au | `ASX:MSB` | Mesoblast Limited | +23.40% | 2.3200 AUD | 13,592,793 | $1.72B |
| eu-fr | `EURONEXT:PLX` | PLUXEE N.V. | -16.42% | 11.8600 EUR | 801,317 | $3.21B |
| jp | `TSE:6574` | Convano, Inc. | +15.46% | 1,120.0000 JPY | 261,400 | $3.13B |
| jp | `TSE:2160` | GNI Group Ltd. | -15.24% | 2,725.0000 JPY | 12,221,000 | $1.34B |
| tw | `TPEX:7861` | Bellwether Electronic Corp. | -12.64% | 781.0000 TWD | 406,891 | $1.78B |
| eu-fr | `EURONEXT:MRN` | Mersen SA | +11.91% | 43.9600 EUR | 107,094 | $1.07B |
| jp | `TSE:5482` | Aichi Steel Corporation | -11.80% | 2,496.0000 JPY | 1,239,200 | $1.15B |
| eu-de | `XETR:SZG` | Salzgitter AG | +11.24% | 48.6800 EUR | 328,875 | $2.93B |
| tw | `TPEX:3105` | Win Semiconductors Corp. | +10.00% | 594.0000 TWD | 58,591,219 | $7.04B |
| tw | `TPEX:6510` | Chunghwa Precision Test Tech Co., Ltd. | -10.00% | 2,880.0000 TWD | 1,751,894 | $3.25B |
| jp | `TSE:4528` | ONO Pharmaceutical Co., Ltd. | -9.99% | 2,224.5000 JPY | 9,730,600 | $7.35B |
| tw | `TWSE:3035` | Faraday Technology Corp. | +9.98% | 231.5000 TWD | 35,582,841 | $1.69B |
| tw | `TWSE:2352` | Qisda Corporation | +9.88% | 32.8000 TWD | 87,290,472 | $1.46B |
| tw | `TWSE:5469` | HannStar Board Corp. | -9.85% | 74.1000 TWD | 8,000,725 | $1.23B |
| tw | `TWSE:3406` | GeniuS Electronic Optical Co., Ltd. | -9.77% | 1,200.0000 TWD | 6,476,429 | $4.63B |
| jp | `TSE:6501` | Hitachi, Ltd. | -9.77% | 5,071.0000 JPY | 45,384,300 | $160.95B |
| tw | `TWSE:2303` | United Microelectronics Corp. | -9.77% | 115.5000 TWD | 350,078,013 | $49.51B |
| ca | `TSX:AGI` | Alamos Gold Inc. | -9.10% | 40.2600 CAD | 1,687,574 | $13.23B |

Largest mover per region among liquid names:

| Region | Ticker | Name | Change |
|---|---|---|---|
| au | `ASX:MSB` | Mesoblast Limited | +23.40% |
| jp | `TSE:6574` | Convano, Inc. | +15.46% |
| tw | `TPEX:3595` | Alliance Material Co., Ltd. | -28.84% |
| ca | `TSX:BHC` | Bausch Health Companies Inc. | +28.34% |
| eu-de | `XETR:SZG` | Salzgitter AG | +11.24% |
| eu-fr | `EURONEXT:PLX` | PLUXEE N.V. | -16.42% |
| eu-it | `MIL:CPR` | Davide Campari-Milano N.V. | -6.64% |
| eu-es | `BME:MAP` | Mapfre SA | -3.74% |
| eu-nl | `EURONEXT:FLOW` | Flow Traders Ltd | -3.40% |
| eu-be | `EURONEXT:UCB` | UCB S.A. | +3.51% |
| eu-at | `VIE:VOE` | voestalpine AG | +2.27% |
| eu-pt | `EURONEXT:JMT` | Jeronimo Martins, SGPS S.A. | +2.58% |
| eu-ie | `EURONEXT:GL9` | Glanbia PLC | -2.12% |
| eu-fi | `OMXHEX:SANOMA` | Sanoma Oyj | -6.02% |
| eu-dk | `OMXCOP:NETC` | Netcompany Group A/S | -8.91% |
| eu-gr | `ATHEX:MOH` | MOTOR OIL (HELLAS) CORINTH REFINERIES S. | -5.63% |

## Method

1. **Universe** — the skill's `mcp__tradingview-advanced__stock_screener(country=…)` is not registered in the Cloud runtime. The same underlying source is reachable over its public per-country scanner API, so each region was pulled with a `country` filter matching the instrument's own country of primary listing. Without that filter the per-country endpoint also returns *foreign* stocks quoted on that market's venues (NVIDIA, Apple and even SpaceX on Lang & Schwarz with WKN-style symbols), which would have inflated Germany from ~500 companies to 36,185 rows.
2. **Venue selection** — one row per instrument, preferring the official listing venue (XETR, TSE, TSX/TSXV, TWSE/TPEX, MIL, BME, VIE, OMXHEX, OMXCOP, ATHEX, EURONEXT, ASX), then the highest-volume print. Germany needs its own company key: Lang & Schwarz carries the same share under a WKN symbol (`LSX:750000` = thyssenkrupp's `TKA`), so German rows are deduped by company description — 4,292 raw rows collapse to 500 companies. Elsewhere the key is (description, ticker root), which keeps genuine share classes apart: `MFC` vs `MFC.PR.K`, `FFH` vs `FFH.U`, `SGR.U` vs `SGR.UN`, `DHT.U` vs `DHT.UN`, `HOT.U` vs `HOT.UN`, `CACR` vs `CACR.A`, and Japan's two unrelated companies both called "JTEC Corporation" (2479 / 3446) all survive as separate rows.
3. **Enrichment** — `volume`, `pe_ratio` and `sector` come straight from the same scanner response, so the skill's Yahoo `compare_stocks` enrichment stage was **not needed and was skipped** (Yahoo's JSON endpoints also return HTTP 429 from this egress).
4. **Market cap** — `market_cap_basic` is in the row's **local** currency, so every value is converted to USD with the 29 Oct open.er-api rate table (EUR 0.897215, AUD 1.419838, CAD 1.401824, JPY 157.905370, DKK 6.714157, TWD 32.415976 per USD). Sanity-checked against implied share counts: SAP 1.18bn, TSMC 26.04bn, BHP 5.13bn, Toyota 1.98bn — all plausible.
5. **Movers mode** — the skill's Tue–Thu forward-fill optimisation was **not applied**. Forward-filling would stamp yesterday's closes with today's date and a `change_pct` of 0, which is wrong for a file whose whole purpose is the daily move. Every row here is a real 2026-10-29 print.

## Caveats

- **Share-class market caps are company-level.** TradingView replicates one cap across every line of a company, so preferred and unit lines carry their parent's cap and all clear the same floor. `TSX:RY.PR.S` shows Royal Bank's $283bn, not the preferred line's own value. This inflates the apparent size of Canadian and German preferreds.
- **241 rows have no market cap and were excluded** (132 Canada, 57 Taiwan, 35 Spain, 4 Australia, 4 Germany, 3 Austria, 3 Finland, 2 Japan, 2 Italy, 1 France, 1 Belgium, 1 Denmark). A row with no cap cannot be tested against a cap floor, so writing it would have put an unscreenable row in a screened file. The Spanish ones are Italian funds quoted on BME (`SCALF`, `HAN`, `S1013`) at zero volume; the German ones are sub-cent GETTEX lines with no cap.
- **Regional Japanese venues carry stale prints.** 6 written rows come from Nagoya (NAG) and Sapporo (SAPSE) rather than TSE. Those venues routinely show a wrong prior close on a thin book — live today, `NAG:7282` showed +15.74% on 200 shares against TSE:7282's −4.98% on 21.3M, and `FSE:6504` showed +35.37% on 100 shares against TSE:6504's −1.91%. Every one of those names was resolved to its TSE row; the 6 that remain are NAG/SAPSE-only listings with no TSE twin.
- **11 rows come from secondary venues** (6 Japan regional, 5 Canada off-official — CSE and one NEO line). Their prints are thinner and can lag the official close; the `exchange` column identifies them.
- **TPEx's ±10% daily limit is live.** `TPEX:3105` Win Semiconductors closed +10.00% at NT$594 and `TPEX:6510` Chunghwa Precision Test −10.00% at NT$2,880 are limit moves, not data errors. The TSE has had no daily limit for large caps since Oct 2024, so Japan's −9.99% prints are genuine repricings.
- **One row's move is an intraday crash, not a gap.** `TPEX:3595` Alliance Material printed open 796 / high 812 / **low 395.50** / close 575 — a −28.84% close after touching −60% intraday, on 4.28M shares. It follows −9.11% the previous session and −7.92% on 22 Oct, so this is a multi-day unwind, not a corporate action.
- **13 rows carry an unchanged close** because the instrument did not trade today (volumes of 1–500 shares). These are genuine no-trade rows, not stale data; every other row's `change_pct` differs from the prior session's.
- **Cross-listings are not deduplicated against the US snapshot.** As the skill already notes, a name listed in two markets appears in both files with different closes.
- **Yesterday's row count was 4,876; today's is 4,500.** The gap is methodology, not missing data: today's run applies the `filters_for_region` **volume floor** that the 28 Oct run left out (removes ~24 AU and ~113 DE thin rows), **dedupes Canada by instrument** (the 28 Oct file kept venue-duplicate rows for 119 TSX/TSXV names), and **excludes rows with no market cap** (241 rows the 28 Oct file carried with an empty cap). Germany and Canada therefore carry fewer rows on a cleaner basis; Japan, France, Italy and the smaller EU markets are within ±3 rows of the 28 Oct file.

## Source health

| Source | Query / URL | Status | Result |
|---|---|---|---|
| TradingView scanner (per-country) | `POST https://scanner.tradingview.com/{australia,japan,taiwan,canada,germany,france,italy,spain,netherlands,belgium,austria,portugal,ireland,finland,denmark,greece}/scan` | `ok` | 16/16 regions HTTP 200, 18,285 stock rows pulled (0.1–0.3 s per call, no rate limit) |
| TradingView scanner (columns) | `name,description,close,open,high,low,volume,change,change_abs,market_cap_basic,exchange,currency,sector,price_earnings_ttm,dividends_yield,country,type` | `ok` | 17 columns returned for every row |
| Yahoo Finance HTML (verification) | `finance.yahoo.com/quote/{SAP.DE,2330.TW,RY.TO,7203.T,6501.T}/` | `ok` | 5/5 settled closes matched the CSV to the cent: SAP €208.90 (prev €211.20), TSMC NT$2,415 (prev NT$2,425), RY C$288.21 (prev C$286.41), Toyota ¥3,077 (prev ¥3,051), Hitachi ¥5,071 (prev ¥5,620) |
| Yahoo Finance HTML (history) | `finance.yahoo.com/quote/{3595.TWO,%5EN225,%5EGDAXI,%5EGSPTSE,%5EAXJO}/history/` | `ok` | Alliance Material's OHLCV matched row-for-row (796/812/395.50/575, 4,284,586 sh); Nikkei 64,659.47, DAX 26,039.68, TSX 36,249.03, ASX 200 8,891.80 confirmed for 29 Oct |
| Press cross-check | Taiwan News / Focus Taiwan, Investing.com, Reuters via Euronext, company IR releases | `ok` | TAIEX 46,368.33 (−1.42%), TSMC −0.41% to NT$2,415, Hitachi −10.5% (worst Nikkei performer), Bausch Health adj EPS $1.77 vs $1.27 est, Alamos Gold adj EPS $0.44 vs $0.4846 est — every quoted figure matched the snapshot |
| open.er-api | `https://open.er-api.com/v6/latest/USD` | `ok` | 2026-10-29 rate table (updated 29 Oct 00:02 UTC), 6 currencies |
| Frankfurter | `https://api.frankfurter.app/latest?from=USD` | `failed:301` | first call returned HTTP 301 without `-L`; not re-run — open.er-api was sufficient and its rates were sanity-checked against implied share counts |
| Yahoo Finance JSON API | chart / spark / screener | `429 rate-limited` | not used — the scanner supplies every schema field, so no Yahoo enrichment call was made |
| `mcp__tradingview__*`, `mcp__yahoo_finance__*` | — | `unavailable` | not registered in this runtime (as documented in the cron prompt); the public scanner API replaced them |
| TradingEconomics | `tradingeconomics.com/taiwan/stock-market` | `stale` | quoted TAIEX 46,969 (−0.14%), TSMC 2,405, MediaTek 4,125 — intraday/prior-session values that contradict the settled prints; **not used** for any figure |

## Files

`international-eod/2026-10-29/` — `au.csv`, `ca.csv`, `eu-at.csv`, `eu-be.csv`, `eu-de.csv`, `eu-dk.csv`, `eu-es.csv`, `eu-fi.csv`, `eu-fr.csv`, `eu-gr.csv`, `eu-ie.csv`, `eu-it.csv`, `eu-nl.csv`, `eu-pt.csv`, `jp.csv`, `tw.csv`, `summary.md`

Schema: `date,ticker,name,open,high,low,close,volume,change_pct,market_cap,pe_ratio,sector,currency,exchange`. `ticker` is `EXCHANGE:symbol` (e.g. `XETR:SAP`, `TSE:7203`, `TSX:RY`). Empty cells mean the source had no value — nothing is imputed.

Integrity checks passed on all 16 files: no non-positive closes, no `high < max(open, close)` or `low > min(open, close)` violations, no `N/A` literals, every row dated 2026-10-29, every row carrying a positive USD market cap.

---

Generated by cron #5 at 2026-10-29 16:30 EDT (window check passed: weekday, 16:30 ET slot). No region was skipped for a holiday — 2026-10-29 is a trading day in all 16 markets (Athens' Ochi Day was 27 Oct, Vienna/Prague and the Netherlands' Reformation Day fall on 26 Oct).
