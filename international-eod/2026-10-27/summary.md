# Cron #05 — eod-international-daily — 2026-10-27

Daily EOD snapshot for the 16 international markets the skill covers (AU, JP, TW, CA and the 12 EU venues), written after each market's cash close settled. **4,467 instrument rows across 16 per-region CSVs**, one row per listed instrument, sorted by market cap (USD) descending.

> **Read this first:** `market_cap` is normalised to **USD**, while `close`/`open`/`high`/`low` stay in the **local listing currency** — the `currency` column states which. `change_pct` is TradingView's daily change in percent. Two structural caveats change how the file should be read: (1) TradingView stamps **company-level** market cap on every share class, so a preferred line inherits its parent's cap; (2) rows whose market cap the source does not report cannot be screened against a cap floor, so they are **excluded** rather than written with a blank cap.

> **This file was restated on 2026-11-03.** The original 2026-10-27 artifact wrote `market_cap` in listing currency and carried the full universe; this version matches the house convention used by every session from 2026-10-28 onward (USD market cap, per-region USD floor applied after conversion, no-cap rows excluded). The original is preserved in git history. The rates used are the 2026-10-27 table, so the numbers below are the 2026-10-27 market, re-expressed — not a re-pull.

## Coverage

| Region | Venues in file | Universe (country filter) | Unique instruments | Written | Floor (USD) | No cap | Off-official rows |
|---|---|---|---|---|---|---|---|
| `au` | ASX | 1,558 | 1,557 | **297** | $300M + vol ≥100,000 | 4 | 0 |
| `jp` | TSE, NAG, FSE, SAPSE | 3,892 | 3,865 | **1,392** | $300M | 2 | 6 |
| `tw` | TWSE, TPEx | 2,331 | 2,330 | **940** | $200M | 57 | 0 |
| `ca` | TSX, TSXV, NEO, CSE | 4,261 | 2,677 | **656** | $200M | 140 | 65 |
| `eu-de` | XETR | 4,281 | 497 | **111** | $300M + vol ≥50,000 | 3 | 0 |
| `eu-fr` | EURONEXT | 545 | 544 | **257** | $100M | 1 | 0 |
| `eu-it` | MIL | 393 | 393 | **181** | $100M | 2 | 0 |
| `eu-es` | BME | 276 | 276 | **144** | $100M | 36 | 0 |
| `eu-nl` | EURONEXT | 77 | 77 | **56** | $100M | 0 | 0 |
| `eu-be` | EURONEXT | 102 | 102 | **76** | $100M | 1 | 0 |
| `eu-at` | VIE | 66 | 66 | **51** | $100M | 2 | 0 |
| `eu-pt` | EURONEXT | 30 | 30 | **27** | $50M | 0 | 0 |
| `eu-ie` | EURONEXT | 19 | 19 | **17** | $200M | 0 | 0 |
| `eu-fi` | OMXHEX | 186 | 186 | **101** | $100M | 3 | 0 |
| `eu-dk` | OMXCOP | 134 | 134 | **75** | $100M | 1 | 0 |
| `eu-gr` | ATHEX | 128 | 128 | **86** | $50M | 0 | 0 |
| **total** | | **18,279** | **12,881** | **4,467** | | **252** | **71** |

`Universe` is every instrument the source returns for that country's own listings; `Unique instruments` collapses instruments quoted on several venues of the same market down to one row; `Written` applies the per-region USD market-cap floor and volume gate. `Off-official rows` counts written rows on a secondary venue of the same market (Nagoya/Sapporo for Japan, NEO/CSE for Canada).

## Market context

Settled closes, verified against the close and not an intraday print:

| Region | Index | Close | Change | Day | Source |
|---|---|---:|---:|---|---|
| au | `^AXJO` | 8,850.1 | +0.46% | up | Yahoo Finance (chart) |
| jp | `^N225` | 63,268.37 | +1.74% | up | Yahoo Finance (chart) |
| tw | `^TWII` | 46,096.23 | +0.12% | up | Yahoo Finance (chart) |
| ca | `^GSPTSE` | 36,171.49 | +0.63% | up | Yahoo Finance (chart) |
| eu-de | `^GDAXI` | 25,590.77 | +0.71% | up | Yahoo Finance (chart) |
| eu-fr | `^FCHI` | 7,887.14 | +0.51% | up | Yahoo Finance (chart) |
| eu-it | `FTSEMIB.MI` | 49,627.95 | +0.90% | up | Yahoo Finance (chart) |
| eu-es | `^IBEX` | 19,160.6 | +0.67% | up | Yahoo Finance (chart) |
| eu-nl | `^AEX` | 1,139.83 | +0.59% | up | Yahoo Finance (chart) |
| eu-be | `^BFX` | 5,801.95 | +0.32% | up | Yahoo Finance (chart) |
| eu-at | `^ATX` | 6,429.63 | +2.54% | up | Yahoo Finance (chart) |
| eu-pt | `PSI20.LS` | 9,253.58 | +0.85% | up | Yahoo Finance (chart) |
| eu-ie | `^ISEQ` | 14,296.54 | +0.95% | up | Yahoo Finance (chart) |
| eu-fi | `^OMXH25` | 6,281.579 | -0.14% | down | Yahoo Finance (chart) |
| eu-dk | `^OMXC20` | 1,585.329 | +0.35% | up | Yahoo Finance (chart) |
| eu-gr | ATHEX (no Yahoo index symbol) | — | +1.24% | up | median of the region's liquid names |

Regional breadth from the snapshot itself (median `change_pct` per file):

| Region | Rows | Median | Up / down / flat | Min | Max |
|---|---:|---:|---|---:|---:|
| au | 297 | +0.52% | 168 / 115 / 14 | -10.46% | +13.56% |
| jp | 1,392 | +0.00% | 686 / 666 / 40 | -8.16% | +20.73% |
| tw | 940 | -0.20% | 393 / 489 / 57 | -9.93% | +9.99% |
| ca | 656 | +0.10% | 346 / 258 / 52 | -13.24% | +15.36% |
| eu-de | 111 | +0.11% | 57 / 51 / 3 | -5.96% | +6.65% |
| eu-fr | 257 | +0.30% | 140 / 82 / 35 | -21.60% | +20.78% |
| eu-it | 181 | +0.59% | 117 / 46 / 18 | -4.59% | +7.29% |
| eu-es | 144 | +0.00% | 62 / 35 / 47 | -5.32% | +13.15% |
| eu-nl | 56 | +0.64% | 38 / 16 / 2 | -13.62% | +11.41% |
| eu-be | 76 | +0.00% | 34 / 30 / 12 | -5.93% | +5.38% |
| eu-at | 51 | +1.29% | 33 / 14 / 4 | -5.45% | +11.51% |
| eu-pt | 27 | +0.31% | 14 / 10 / 3 | -7.91% | +3.68% |
| eu-ie | 17 | +0.26% | 10 / 5 / 2 | -4.19% | +3.75% |
| eu-fi | 101 | +0.00% | 46 / 49 / 6 | -18.60% | +7.24% |
| eu-dk | 75 | +0.52% | 44 / 26 / 5 | -2.29% | +8.36% |
| eu-gr | 86 | +0.43% | 50 / 22 / 14 | -4.18% | +4.98% |

Sector rotation over the liquid subset (market cap ≥ $1bn and volume ≥ 100k, carry-over rows removed):

| Sector | Names | Mean | Median |
|---|---:|---:|---:|
| Non-Energy Minerals | 130 | +2.89% | +2.78% |
| Producer Manufacturing | 195 | +1.12% | +1.22% |
| Process Industries | 106 | +1.02% | +0.62% |
| Industrial Services | 82 | +0.83% | +0.91% |
| Electronic Technology | 203 | +0.79% | +0.80% |
| Utilities | 55 | +0.76% | +0.51% |
| Health Technology | 73 | +0.74% | +0.00% |
| Finance | 279 | +0.70% | +0.57% |
| Miscellaneous | 6 | +0.33% | +0.30% |
| Distribution Services | 58 | +0.20% | +0.35% |
| Commercial Services | 42 | +0.17% | +0.08% |
| Communications | 30 | +0.14% | -0.22% |
| Transportation | 74 | -0.10% | +0.00% |
| Technology Services | 79 | -0.12% | -0.23% |
| Health Services | 12 | -0.16% | -0.37% |
| Consumer Durables | 76 | -0.19% | -0.56% |
| Consumer Services | 50 | -0.56% | -0.88% |
| Consumer Non-Durables | 80 | -0.61% | -0.96% |
| Retail Trade | 73 | -0.91% | -1.13% |
| Energy Minerals | 53 | -0.94% | -0.63% |

## Top movers

Largest absolute daily moves among liquid names, 1,756 of 4,467 rows qualify:

| Region | Ticker | Name | Change | Close | Volume | Mkt cap (USD) | Catalyst |
|---|---|---|---:|---|---:|---:|---|
| eu-fi | `OMXHEX:GRK` | GRK Infra Plc | -18.36% | 20.9 EUR | 263162 | $1.22B | no catalyst research in this run |
| jp | `TSE:7970` | Shin-Etsu Polymer Co., Ltd. | +12.03% | 2505 JPY | 1777600 | $1.15B | no catalyst research in this run |
| ca | `TSX:CLS` | Celestica Inc. | +11.92% | 388.33 CAD | 746223 | $31.15B | no catalyst research in this run |
| eu-at | `VIE:ATS` | AT & S Austria Technologie & Systemtechnik Aktiengesellschaft | +11.51% | 155 EUR | 163009 | $6.01B | no catalyst research in this run |
| eu-nl | `EURONEXT:BESI` | BE Semiconductor Industries N.V. | +11.41% | 163.05 EUR | 1060961 | $13.15B | no catalyst research in this run |
| jp | `TSE:4588` | Oncolys BioPharma, Inc. | +10.79% | 6980 JPY | 1799700 | $1.18B | no catalyst research in this run |
| tw | `TWSE:2466` | Cosmo Electronics Corporation | +9.96% | 287 TWD | 1002983 | $1.40B | no catalyst research in this run |
| tw | `TWSE:7750` | Syntec Technology Co. Ltd. | +9.94% | 1990 TWD | 428288 | $4.01B | no catalyst research in this run |
| tw | `TWSE:2464` | Mirle Automation Corp. | +9.94% | 177 TWD | 13587723 | $1.13B | no catalyst research in this run |
| tw | `TWSE:2049` | HIWIN Technologies Corp. | +9.87% | 328.5 TWD | 6005497 | $3.26B | no catalyst research in this run |
| tw | `TPEX:6274` | Taiwan Union Technology Corporation | -9.86% | 1280 TWD | 16390096 | $13.12B | no catalyst research in this run |
| eu-es | `BME:SLR` | Solaria Energia y Medio Ambiente, S.A. | +9.61% | 15.565 EUR | 2147571 | $2.10B | no catalyst research in this run |
| tw | `TWSE:8021` | Topoint Technology Co., Ltd. | -9.60% | 433 TWD | 9900060 | $2.17B | no catalyst research in this run |
| au | `ASX:MP1` | Megaport Ltd. | +9.60% | 17.58 AUD | 1665758 | $2.67B | no catalyst research in this run |
| au | `ASX:PYC` | PYC Therapeutics Limited | +9.40% | 1.92 AUD | 4365632 | $1.21B | no catalyst research in this run |

Largest mover per region among liquid names:

| Region | Ticker | Name | Change |
|---|---|---|---:|
| au | `ASX:MP1` | Megaport Ltd. | +9.60% |
| jp | `TSE:7970` | Shin-Etsu Polymer Co., Ltd. | +12.03% |
| tw | `TWSE:2466` | Cosmo Electronics Corporation | +9.96% |
| ca | `TSX:CLS` | Celestica Inc. | +11.92% |
| eu-de | `XETR:VBK` | Verbio SE | +5.74% |
| eu-fr | `EURONEXT:NANO` | Nanobiotix SA | +7.37% |
| eu-it | `MIL:MAIRE` | MAIRE S.p.A. | +3.91% |
| eu-es | `BME:SLR` | Solaria Energia y Medio Ambiente, S.A. | +9.61% |
| eu-nl | `EURONEXT:BESI` | BE Semiconductor Industries N.V. | +11.41% |
| eu-be | `EURONEXT:UMI` | Umicore SA | +5.38% |
| eu-at | `VIE:ATS` | AT & S Austria Technologie & Systemtechnik Aktiengesellschaft | +11.51% |
| eu-pt | `EURONEXT:BCP` | Banco Comercial Portugues S.A. | +1.63% |
| eu-ie | `EURONEXT:KRX` | Kingspan Group PLC | +3.75% |
| eu-fi | `OMXHEX:GRK` | GRK Infra Plc | -18.36% |
| eu-dk | `OMXCOP:GN` | GN Store Nord A/S | +2.77% |
| eu-gr | `ATHEX:TPEIR` | Piraeus Bank S.A. | +4.06% |

## Method

- **Universe** — one POST per country to `scanner.tradingview.com/{country}/scan`, filtered on `type=stock` and the issuer country, sorted by `market_cap_basic` desc, paged at 3,000 rows.
- **Venue collapse** — exact-symbol dedupe, then primary-venue dedupe, then venue-duplicate collapse on the normalised company name with the region's primary venue preferred. One canonical row per company per region.
- **`market_cap`** — TradingView's `market_cap_basic` is denominated in the **listing currency**, not USD. Verified by share-count reconciliation (`market_cap_basic / close` returns the issuer's real share count for SAP 1.1626bn, Toyota 11.900bn, TSMC 25.770bn, Genmab 59.11m) and by a server-side filter of `market_cap_basic > 300000000` on the Japan endpoint that still returns names with a market cap of ¥385m. The floors are therefore applied **after** converting to USD.
- **FX** — the 2026-10-27 rate table measured at 16:33 ET from Yahoo Finance: EUR 1.1130, JPY 0.0063312, AUD 0.7026913, CAD 0.7117944, DKK 0.1488804, TWD 0.0308604 (USD per one unit of local currency). Cross-checked against `frankfurter.dev` for the same date: the five currencies it carries agree within 0.2%.
- **Floor** — per-region USD market-cap floor, plus a volume gate for Australia (≥ 100,000) and Germany (≥ 50,000). Rows the source reports no market cap for are excluded, not written blank.
- **Liquid subset** (movers and sector rotation) — market cap ≥ $1bn and volume ≥ 100k, carry-over rows removed.

## Caveats

- **1,486 rows did not trade on 2026-10-27.** The screener returns the last session's close and change for a row that did not trade, which is true of the instrument but false as a statement about the day. The rows are kept exactly as the source returned them (the schema is fixed at 14 columns) and the affected tickers are listed in `_carryover.json` with each instrument's last trade date. Every movers table above excludes them.
- **Venue-duplicate collapse inflates the apparent size of preferred and share-class lines.** 65 written Canadian rows sit on a secondary venue (NEO/CSE) and 6 Japanese rows on Nagoya/Sapporo, where thin-book prints can diverge from the primary close.
- **This session did no catalyst research.** The `Catalyst` column reads *no catalyst research in this run* for every row. This is a data snapshot; no reason for any move is asserted.
- **Cross-listings are not deduplicated against the US snapshot.** A name listed in two markets appears in both files with different closes.
- **The FX source differs from the 2026-10-30 session's.** That session used `open.er-api`; the free tier of that API serves only the current day's table, so the 2026-10-27 restatement uses Yahoo's 2026-10-27 table. The two sources agree within 0.2% on the same date, and market cap is not a price field, but the mcap column of 10-27 and 10-30 are not produced by an identical process.

## Source health

| Source | Query / URL | Status | Result |
|---|---|---|---|
| TradingView scanner (per-country) | `POST https://scanner.tradingview.com/{australia,japan,taiwan,canada,germany,france,italy,spain,netherlands,belgium,austria,portugal,ireland,finland,denmark,greece}/scan` | `ok` | 16/16 regions HTTP 200, 18,268 stock rows pulled, 0 errors |
| Yahoo Finance (cross-check) | `v7/finance/spark` (batches of 12) + `v8/finance/chart` | `ok` | 12,340 of 12,881 rows mapped and checked on close and change; 10,627 full agreement, 73 partial, 1,486 not traded today, 154 unresolved |
| Yahoo Finance (index levels) | `v8/finance/chart` | `ok` | 15 of 16 region indices; no Yahoo symbol exists for the ATHEX index, so the Greek figure is the median of the region's liquid names |
| Yahoo Finance (FX) | `v8/finance/chart` on `EURUSD=X`, `JPY=X`, `AUD=X`, `CAD=X`, `DKK=X`, `TWD=X` | `ok` | 2026-10-27 table, 6 currencies |
| Frankfurter (FX cross-check) | `api.frankfurter.dev/v1/2026-10-27?base=USD` | `ok` (partial) | 5 of 6 currencies agree with Yahoo within 0.2%; TWD is not carried |
| `mcp__tradingview_advanced__*`, `mcp__yahoo_finance__*` | — | `unavailable` | not registered in this runtime (as documented in the cron prompt); the public scanner API replaced them |

## Files

`international-eod/2026-10-27/` — `au.csv`, `ca.csv`, `eu-at.csv`, `eu-be.csv`, `eu-de.csv`, `eu-dk.csv`, `eu-es.csv`, `eu-fi.csv`, `eu-fr.csv`, `eu-gr.csv`, `eu-ie.csv`, `eu-it.csv`, `eu-nl.csv`, `eu-pt.csv`, `jp.csv`, `tw.csv`, `summary.md`, `_carryover.json`, `_calendar_correction.json`

Schema: `date,ticker,name,open,high,low,close,volume,change_pct,market_cap,pe_ratio,sector,currency,exchange`. `ticker` is `EXCHANGE:symbol` (e.g. `XETR:SAP`, `TSE:7203`, `TSX:RY`). Empty cells mean the source had no value — nothing is imputed.

---

Generated by cron #05 at 2026-10-27 16:31-16:36 ET (window check passed: weekday, 16:30 ET slot). Restated 2026-11-03 into the house convention; market data is unchanged, only the `market_cap` unit, the floor and the report layout differ from the original.