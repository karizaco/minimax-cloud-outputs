# Cron #5 — eod-international-daily — 2026-10-30

Daily EOD snapshot for the 16 international markets the skill covers (AU, JP, TW, CA and the 12 EU venues), written after each market's cash close settled. **4,486 instrument rows across 16 per-region CSVs**, one row per listed instrument, sorted by market cap (USD) descending.

> **Read this first:** `market_cap` is normalised to **USD**, while `close`/`open`/`high`/`low` stay in the **local listing currency** — the `currency` column states which. `change_pct` is TradingView's daily change in percent. Two structural caveats change how the file should be read: (1) TradingView stamps **company-level** market cap on every share class, so a preferred line inherits its parent's cap (`TSX:RY.PR.S` carries Royal Bank's ~$286bn); (2) rows whose market cap the source does not report cannot be screened against a cap floor, so they are **excluded** rather than written with a blank cap — 244 such rows across the set.

## Coverage

| Region | Venues in file | Universe (country filter) | Unique instruments | Written | Floor (USD) | No cap | Off-official rows |
|---|---|---|---|---|---|---|---|
| `au` | ASX | 1,557 | 1,557 | **303** | $300M + vol ≥100k | 4 | 0 |
| `jp` | TSE, NAG, SAPSE | 3,894 | 3,868 | **1,393** | $300M | 3 | 6 |
| `tw` | TWSE, TPEX | 2,335 | 2,335 | **932** | $200M | 56 | 0 |
| `ca` | TSX, TSXV, CSE, NEO | 4,260 | 2,687 | **668** | $200M | 130 | 5 |
| `eu-de` | XETR | 4,286 | 500 | **115** | $300M + vol ≥50k | 4 | 0 |
| `eu-fr` | EURONEXT | 546 | 546 | **260** | $100M | 1 | 0 |
| `eu-it` | MIL | 393 | 393 | **180** | $100M | 2 | 0 |
| `eu-es` | BME | 278 | 278 | **146** | $100M | 36 | 0 |
| `eu-nl` | EURONEXT | 77 | 77 | **56** | $100M | 0 | 0 |
| `eu-be` | EURONEXT | 100 | 100 | **76** | $100M | 1 | 0 |
| `eu-at` | VIE | 66 | 66 | **51** | $100M | 3 | 0 |
| `eu-pt` | EURONEXT | 31 | 31 | **27** | $50M | 0 | 0 |
| `eu-ie` | EURONEXT | 19 | 19 | **17** | $200M | 0 | 0 |
| `eu-fi` | OMXHEX | 187 | 187 | **101** | $100M | 3 | 0 |
| `eu-dk` | OMXCOP | 134 | 134 | **75** | $100M | 1 | 0 |
| `eu-gr` | ATHEX | 127 | 127 | **86** | $50M | 0 | 0 |
| **total** | | **18,290** | | **4,486** | | **244** | **11** |

`Universe` is every instrument the source returns for that country's own listings; `Unique instruments` collapses instruments quoted on several venues of the same market down to one row; `Written` applies the skill's per-region USD market-cap floor (`screener_filters.filters_for_region`).

## Market context

Settled closes, verified against the close and not an intraday print:

| Index | Close | Change | Day | Source |
|---|---|---|---|---|
| STOXX 600 | 646.75 | −0.36% | down | Reuters (close) |
| Nikkei 225 | 63,290.11 | −1,369.36 / −2.12% | down | CNA, Jiji Press, AP |
| TOPIX | 3,965.07 | −38.21 / −0.95% | down | CNA, Jiji Press |
| TAIEX | 45,211.83 | −1,156.50 / −2.49% | down | CNA, Focus Taiwan, Taiwan News |
| Kospi | 5,730.74 | −3.5% | down | AP (context only — not a covered region) |
| ASX 200 | 8,908.10 | +0.2% | up | AP |
| DAX, CAC 40, FTSE 100 | not verified | — | — | Yahoo history pages served stale Oct-2025 rows (see Source health) |

The driver was a global AI-capex de-rating: Alphabet fell ~14%, and Amazon and Intel were sold in the after-hours session on negative cash flow, which set Asia's tone on Friday. The Nikkei fell more than 1,900 points intraday before recovering over 500 of them into the close, and 92% of the index decline came from five stocks (Advantest, SoftBank, Tokyo Electron, IBIDEN and peers) — 16 of 33 sectors finished higher. The BoJ held at 1.25% and accelerated its ETF sales on the same day; the ECB had held rates on Thursday. Taiwan was the session's clear laggard: the TAIEX fell 2.49% to 45,211.83 (low 44,726.26) on turnover of NT$877.73bn with foreigners net-selling NT$112.47bn, ending **October down 5.69% (−2,728.3 points), its worst month on record**.

Regional breadth from the snapshot itself (median `change_pct` per file):

| Region | Rows | Median | Up / down / flat | Min | Max |
|---|---|---|---|---|---|
| `au` | 303 | +0.18% | 159 / 130 / 14 | −25.61% | +10.71% |
| `jp` | 1,393 | 0.00% | 679 / 687 / 27 | −20.99% | +23.33% |
| `tw` | 932 | −2.66% | 82 / 814 / 36 | −10.00% | +20.52% |
| `ca` | 668 | −0.58% | 188 / 421 / 59 | −17.24% | +13.76% |
| `eu-de` | 115 | −0.59% | 37 / 74 / 4 | −8.48% | +5.59% |
| `eu-fr` | 260 | −0.26% | 99 / 140 / 21 | −18.21% | +13.84% |
| `eu-it` | 180 | −0.73% | 50 / 115 / 15 | −14.50% | +3.88% |
| `eu-es` | 146 | 0.00% | 34 / 68 / 44 | −5.47% | +6.40% |
| `eu-nl` | 56 | −0.20% | 24 / 31 / 1 | −7.57% | +7.89% |
| `eu-be` | 76 | −0.26% | 25 / 41 / 10 | −5.12% | +11.79% |
| `eu-at` | 51 | 0.00% | 17 / 24 / 10 | −13.29% | +3.31% |
| `eu-pt` | 27 | 0.00% | 9 / 13 / 5 | −3.05% | +2.36% |
| `eu-ie` | 17 | −0.20% | 6 / 9 / 2 | −2.63% | +2.86% |
| `eu-fi` | 101 | −0.97% | 26 / 68 / 7 | −9.43% | +9.29% |
| `eu-dk` | 75 | −0.49% | 27 / 41 / 7 | −4.59% | +3.94% |
| `eu-gr` | 86 | 0.00% | 29 / 41 / 16 | −5.71% | +4.23% |

Japan's headline index fell 2.12% but the median name did not move at all; Taiwan is the only market where the median name fell more than 1%. Europe closed slightly red — STOXX 600 −0.36% — after a strong month.

## Top movers

Largest absolute daily moves among liquid names (volume ≥ 100k and market cap ≥ $1B), 1,814 of 4,486 rows qualify:

| Region | Ticker | Name | Change | Close | Volume | Mkt cap (USD) | Catalyst |
|---|---|---|---|---|---|---|---|
| au | `ASX:4DX` | 4DMedical Ltd. | −25.61% | 2.44 AUD | 18,974,184 | $1.39B | A$3 support broke on 6.7× ADV; funding/dilution worry after the facility was fully drawn (A$242.8m cash left); −42.6% in October |
| jp | `TSE:6370` | Kurita Water Industries | −20.99% | 5,647 JPY | 288,100 | $4.82B | Printed a single price all session (O=H=L=C); treasury-buyback completion disclosed the same morning (4,125,080 shares cumulative) |
| jp | `TSE:1946` | Toenec Corporation | −18.00% | 1,795 JPY | 1,570,300 | $1.33B | AI/tech complex de-rating; no company-specific release found |
| ca | `TSX:TFII` | TFI International Inc. | −17.24% | 130.05 CAD | 927,830 | $9.23B | Q3 EPS $1.67 vs $1.75 est; LTL operating ratio deteriorated and Q4 outlook disappointed; diesel costs; Scotiabank cut estimates |
| jp | `TSE:6702` | Fujitsu Limited | −16.20% | 3,622 JPY | 23,990,700 | $47.49B | H1 adj. operating profit −6.1% to ¥113.9bn on component costs and R&D; Hardware Solutions profit −64%; missed consensus despite FY guidance kept |
| jp | `TSE:4062` | IBIDEN CO., LTD. | −15.21% | 8,359 JPY | 10,712,200 | $35.35B | AI-infrastructure supplier hit by Intel's post-market slump |
| jp | `TSE:9766` | KONAMI Group Corporation | +15.02% | 26,385 JPY | 2,106,100 | $19.70B | Raised FY27 operating-profit forecast to ¥193.0bn from ¥143.0bn; top Nikkei gainer as money rotated out of chips |
| eu-it | `MIL:AMP` | Amplifon SpA | −14.50% | 11.17 EUR | 12,553,791 | $3.94B | Q3 in line (rev €575m, adj. net profit +38.7%) but FY guidance confirmed, not raised → profit-taking after +34% in six months |
| jp | `TSE:2160` | GNI Group Ltd. | −14.68% | 2,325 JPY | 8,393,200 | $1.14B | Data-centre infrastructure de-rating; no company-specific release found |
| eu-fr | `EURONEXT:NK` | Imerys SA | +13.84% | 25.34 EUR | 385,149 | $2.11B | No company-specific release found |
| eu-at | `VIE:ATS` | AT&S Austria Technologie | −13.29% | 134.40 EUR | 265,241 | $6.72B | PCB/AI-infrastructure de-rating; no company-specific release found |
| tw | `TWSE:2409` | AUO Corporation | −9.99% | 30.65 TWD | 296,771,840 | $7.84B | Limit-down close at the session low; AI/semiconductor unwind |

Largest mover per region among liquid names:

| Region | Ticker | Name | Change |
|---|---|---|---|
| au | `ASX:4DX` | 4DMedical Limited | −25.61% |
| jp | `TSE:6370` | Kurita Water Industries | −20.99% |
| tw | `TWSE:2409` | AUO Corporation | −9.99% |
| ca | `TSX:TFII` | TFI International Inc. | −17.24% |
| eu-de | `XETR:WAF` | Siltronic AG | −7.54% |
| eu-fr | `EURONEXT:NK` | Imerys SA | +13.84% |
| eu-it | `MIL:AMP` | Amplifon SpA | −14.50% |
| eu-es | `BME:ACX` | Acerinox SA | −5.47% |
| eu-nl | `EURONEXT:UMG` | Universal Music Group N.V. | +7.89% |
| eu-be | `EURONEXT:PROX` | Proximus SA | +11.79% |
| eu-at | `VIE:ATS` | AT&S Austria Technologie | −13.29% |
| eu-pt | `EURONEXT:BCP` | Banco Comercial Portugues | −2.49% |
| eu-ie | `EURONEXT:GL9` | Glanbia PLC | +2.86% |
| eu-fi | `OMXHEX:AKTIA` | Aktia Bank Plc Class A | −9.43% |
| eu-dk | `OMXCOP:NKT` | NKT A/S | −4.00% |
| eu-gr | `ATHEX:AIA` | Athens International Airport | −4.61% |

## Method

1. **Universe** — the skill's `mcp__tradingview-advanced__stock_screener(country=…)` is not registered in the Cloud runtime. The same underlying source is reachable over its public per-country scanner API, so each region was pulled with a `country` filter matching the instrument's own country of primary listing. Without that filter the per-country endpoint also returns *foreign* stocks quoted on that market's venues (NVIDIA, Apple and even SpaceX on Lang & Schwarz with WKN-style symbols), which would have inflated Germany from ~500 companies to 36,185 rows.
2. **Venue selection** — one row per instrument, preferring the official listing venue (XETR, TSE, TSX/TSXV, TWSE/TPEX, MIL, BME, VIE, OMXHEX, OMXCOP, ATHEX, EURONEXT, ASX), then the highest-volume print. Germany needs its own company key: Lang & Schwarz carries the same share under a WKN symbol (`LSX:750000` = thyssenkrupp's `TKA`), so German rows are deduped by company description — 4,286 raw rows collapse to 500 companies. Elsewhere the key is (description, ticker root), which keeps genuine share classes apart: `MFC` vs `MFC.PR.K`, `FFH` vs `FFH.U`, `SGR.U` vs `SGR.UN`, `DHT.U` vs `DHT.UN`, `HOT.U` vs `HOT.UN`, `CACR` vs `CACR.A`, and Japan's two unrelated companies both called "JTEC Corporation" (2479 / 3446) all survive as separate rows.
3. **Enrichment** — `volume`, `pe_ratio` and `sector` come straight from the same scanner response, so the skill's Yahoo `compare_stocks` enrichment stage was **not needed and was skipped** (Yahoo's JSON endpoints also return HTTP 429 from this egress).
4. **Market cap** — `market_cap_basic` is in the row's **local** currency, so every value is converted to USD with the 30 Oct open.er-api rate table (EUR 0.895934, AUD 1.422859, CAD 1.398868, JPY 157.881601, DKK 6.71395, TWD 32.55178 per USD). Sanity-checked against implied share counts (local cap ÷ local close): SAP 1.16bn, TSMC 26.4bn, Toyota 11.87bn, Fujitsu 2.07bn, Konami 0.12bn, Amplifon 0.32bn, TFI 0.099bn, AT&S 0.045bn, 4DMedical 0.81bn — all plausible.
5. **Change column** — the scanner's `change` field is already in **percent units** (0.0695 means +0.0695%), not a fraction. This was proven, not assumed: across all 18,274 priced rows, `close − close/(1 + change/100)` reproduces `change_abs` exactly (total error 0.0000), while the fraction reading misses by a mean of 671 price units per row. The 29 Oct file confirms the same convention — `TSE:4365`'s scanner value 1.483679525222552 was written as `1.4837` there. Multiplying by 100 would have inflated every move in this file by 100×.
6. **Movers mode** — the skill's Tue–Thu forward-fill optimisation was **not applied** (it runs Mon–Thu only, and forward-filling would stamp yesterday's closes with today's date and a `change_pct` of 0, which is wrong for a file whose whole purpose is the daily move). Every row here is a real 2026-10-30 print.

## Caveats

- **Share-class market caps are company-level.** TradingView replicates one cap across every line of a company, so preferred and unit lines carry their parent's cap and all clear the same floor. `TSX:RY.PR.S` shows Royal Bank's ~$286bn, not the preferred line's own value. This inflates the apparent size of Canadian and German preferreds.
- **244 rows have no market cap and were excluded** (130 Canada, 56 Taiwan, 36 Spain, 4 Australia, 4 Germany, 3 Japan, 3 Austria, 3 Finland, 2 Italy, 1 France, 1 Belgium, 1 Denmark). A row with no cap cannot be tested against a cap floor, so writing it would have put an unscreenable row in a screened file. The composition differs by region: the Spanish ones are zero-volume SICAV and fund lines quoted on BME (`Inbest GPF`, `Ursus-3C Valor SIL`, `Diale Inversiones`); the Canadian ones are preferred and share-class lines where the source publishes no company cap (Power Financial 4.2% notes, Brookfield Office Properties, M Split preferreds); the Taiwanese ones are small TPEx names; the Australian ones are micro uranium/resource names; and the four German ones are the TKCC (Accelis Group) line across ten venues plus AVERDION SE.
- **14 rows carry a stale `change_pct`.** Their close is identical to 29 Oct but the source's change column is non-zero, i.e. the instrument did not trade today and the change value is left over from an earlier session (`TSE:4365`, `TPEX:7728`, `EURONEXT:CROS` and 11 others, all on volumes of 11–9,943 shares). A further 278 rows show a change of exactly 0.00% — genuine no-trade prints, not missing data.
- **One market cap is materially overstated.** `ASX:BHP` implies 5.08bn shares against a real count near 2.13bn, so BHP's market cap reads ~$205bn instead of ~$86bn. Every other checked name lands on a plausible share count. The field is written as the source reports it, but a cap-based screen will treat BHP as a mega-cap when it is not.
- **Regional Japanese venues carry stale prints.** 6 written rows come from Nagoya (NAG) and Sapporo (SAPSE) rather than TSE. Those venues routinely show a wrong prior close on a thin book — e.g. `NAG:8306` printed −5.13% on 400 shares against TSE:8306's −0.49% on 31.1M. Every one of those names was resolved to its TSE row; the 6 that remain are NAG/SAPSE-only listings with no TSE twin. Five Canadian rows likewise come from off-official venues (4 CSE, 1 NEO), where prints can diverge from the official close.
- **TPEx's ±10% daily limit is live.** `TWSE:2409` AUO closed −9.99% at NT$30.65, exactly the session low — a limit move, not a data error. The TSE has had no daily limit for large caps since Oct 2024, so Japan's −9.99% prints are genuine repricings.
- **One row's move is a single-price print, not a gap.** `TSE:6370` Kurita Water printed open 5,647 / high 5,647 / low 5,647 / close 5,647 on 288,100 shares. The close is corroborated by the FT tearsheet and stockanalysis.com, but the intraday range is unverifiable from a row where all four prices are identical.
- **Cross-listings are not deduplicated against the US snapshot.** As the skill already notes, a name listed in two markets appears in both files with different closes.
- **Yesterday's row count was 4,500; today's is 4,486.** The gap is market movement, not missing data: every region's count is within a handful of rows of 29 Oct (AU identical at 303, JP −2, TW −10, CA +1, DE −4, FR identical, FI/DK identical), and 4,485 of 4,498 tickers present in both files carry a close that chains exactly from yesterday's close to today's.

## Source health

| Source | Query / URL | Status | Result |
|---|---|---|---|
| TradingView scanner (per-country) | `POST https://scanner.tradingview.com/{australia,japan,taiwan,canada,germany,france,italy,spain,netherlands,belgium,austria,portugal,ireland,finland,denmark,greece}/scan` | `ok` | 16/16 regions HTTP 200, 18,290 stock rows pulled (0.0–0.5 s per call, no rate limit) |
| TradingView scanner (columns) | `name,description,close,open,high,low,change,volume,market_cap_basic,exchange,currency,sector,price_earnings_ttm,change_abs,pricescale,minmov,type,country` | `ok` | 18 columns returned for every row; response carries no `columns` array, so rows are zipped positionally against the request list |
| Yahoo Finance HTML (verification) | `finance.yahoo.com/quote/{7203.T,2330.TW,SAP.DE,RY.TO,BHP.AX}/` | `ok` | 5/5 settled closes matched the CSV to the cent, each dated 30 Oct: Toyota ¥3,070 (prev ¥3,077), TSMC NT$2,370 (prev NT$2,415), SAP €211.25 (prev €208.90), RY C$283.93 (prev C$288.21), BHP A$57.56 (prev A$57.52) |
| Yahoo Finance HTML (index history) | `finance.yahoo.com/quote/{^N225,^TWII,^GDAXI,^GSPTSE,^AXJO}/history/` | `failed:stale` | 5/5 served stale tables — ^N225 and ^TWII stopped at the 29 Oct row, ^GDAXI/^GSPTSE/^AXJO served Oct-2025 rows. **No index level in this file comes from Yahoo**; index levels were replaced by press sources and the DAX/CAC/FTSE closes are reported as unverified |
| Press cross-check | CNA / Focus Taiwan / Taiwan News, Jiji Press, Reuters, AP via UNB, Investing.com, Borsa Italiana (Radiocor), MarketBeat, Winnipeg Free Press, TheBull, Wiener Börse, stockanalysis.com, FT Markets | `ok` | Every quoted figure matched the snapshot: TAIEX 45,211.83 (−2.49%), Nikkei 63,290.11 (−2.12%), TOPIX 3,965.07, ASX 200 8,908.10 (+0.2%), STOXX 600 646.75 (−0.36%), Fujitsu ¥3,622 (−16.2%), Amplifon €11.17 (−14.5%), TFI C$130.05, 4DMedical A$2.44 (−25.61%), Konami ¥26,385 (+15.02%), Kurita ¥5,647 (−20.99%) |
| open.er-api | `https://open.er-api.com/v6/latest/USD` | `ok` | 2026-10-30 rate table (updated 30 Oct 00:02 UTC), 6 currencies |
| Yahoo Finance JSON API | chart / spark / screener | `429 rate-limited` | not used — the scanner supplies every schema field, so no Yahoo enrichment call was made |
| `mcp__tradingview__*`, `mcp__yahoo_finance__*` | — | `unavailable` | not registered in this runtime (as documented in the cron prompt); the public scanner API replaced them |
| Yahoo Finance quote page via curl | `finance.yahoo.com/quote/{SYM}/` | `failed:bot-blocked` | not used — curl on Yahoo quote pages returns a generic shell whose price is the same default for every symbol; `web_fetch` is the only safe path and was used instead |

## Files

`international-eod/2026-10-30/` — `au.csv`, `ca.csv`, `eu-at.csv`, `eu-be.csv`, `eu-de.csv`, `eu-dk.csv`, `eu-es.csv`, `eu-fi.csv`, `eu-fr.csv`, `eu-gr.csv`, `eu-ie.csv`, `eu-it.csv`, `eu-nl.csv`, `eu-pt.csv`, `jp.csv`, `tw.csv`, `summary.md`

Schema: `date,ticker,name,open,high,low,close,volume,change_pct,market_cap,pe_ratio,sector,currency,exchange`. `ticker` is `EXCHANGE:symbol` (e.g. `XETR:SAP`, `TSE:7203`, `TSX:RY`). Empty cells mean the source had no value — nothing is imputed.

Integrity checks passed on all 16 files: no non-positive closes, no `high < max(open, close)` or `low > min(open, close)` violations, no `N/A` literals, every row dated 2026-10-30, every row carrying a positive USD market cap.

---

Generated by cron #5 at 2026-10-30 16:32 EDT (window check passed: weekday, 16:30 ET slot). No region was skipped for a holiday — 2026-10-30 is a trading day in all 16 markets.
