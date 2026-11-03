# Cron #05 — eod-international-daily — 2026-10-26

Daily EOD snapshot for the international markets the skill covers (AU, JP, CA and the EU venues), written after each market's cash close settled. **3,469 instrument rows across 13 per-region CSVs**, one row per listed instrument, sorted by market cap (USD) descending.

> **Read this first:** `market_cap` is normalised to **USD**, while `close`/`open`/`high`/`low` stay in the **local listing currency** — the `currency` column states which. `change_pct` is TradingView's daily change in percent. Two structural caveats change how the file should be read: (1) TradingView stamps **company-level** market cap on every share class, so a preferred line inherits its parent's cap; (2) rows whose market cap the source does not report cannot be screened against a cap floor, so they are **excluded** rather than written with a blank cap.

> **This file was restated on 2026-11-03.** The original 2026-10-26 artifact wrote `market_cap` in listing currency and carried the full universe (15,862 rows); this version matches the house convention used by every session from 2026-10-27 onward (USD market cap, per-region USD floor applied after conversion, no-cap rows excluded). The original is preserved in git history at commit `9291938`. The rates used are the 2026-10-26 table, so the numbers below are the 2026-10-26 market, re-expressed — not a re-pull.

## Coverage

| Region | Venues in file | Universe (country filter) | Unique instruments | Written | Floor (USD) | No cap | Off-official rows |
|---|---|---|---|---|---|---|---|
| `au` | ASX | 1,558 | 1,558 | **302** | $300M + vol ≥100,000 | 4 | 0 |
| `ca` | NEO, TSX | 4,261 | 2,667 | **658** | $200M | 134 | 67 |
| `eu-be` | EURONEXT | 103 | 103 | **75** | $100M | 1 | 0 |
| `eu-de` | XETR | 4,279 | 498 | **115** | $300M + vol ≥50,000 | 3 | 0 |
| `eu-dk` | OMXCOP | 134 | 134 | **75** | $100M | 1 | 0 |
| `eu-es` | BME | 276 | 276 | **144** | $100M | 36 | 0 |
| `eu-fi` | OMXHEX | 186 | 186 | **100** | $100M | 3 | 0 |
| `eu-fr` | EURONEXT | 544 | 542 | **255** | $100M | 1 | 0 |
| `eu-gr` | ATHEX | 128 | 128 | **86** | $50M | 0 | 0 |
| `eu-it` | MIL | 393 | 393 | **181** | $100M | 2 | 0 |
| `eu-nl` | EURONEXT | 77 | 77 | **56** | $100M | 0 | 0 |
| `eu-pt` | EURONEXT | 30 | 30 | **27** | $50M | 0 | 0 |
| `jp` | NAG, SAPSE, TSE | 3,893 | 3,865 | **1,395** | $300M | 2 | 6 |
| **total** | | **15,862** | **10,457** | **3,469** | | **187** | **73** |

`Universe` is every instrument the source returns for that country's own listings; `Unique instruments` collapses instruments quoted on several venues of the same market down to one row; `Written` applies the per-region USD market-cap floor and volume gate. `Off-official rows` counts written rows on a secondary venue of the same market (Nagoya/Fujisawa/Sapporo for Japan, NEO/CSE for Canada).

Three of the skill's sixteen regions were closed on 2026-10-26 and have no file: **tw** (光復節 substitute public holiday; last session 2026-10-23, reopens 2026-10-27), **eu-at** (National Day), **eu-ie** (October bank holiday, the last Monday in October).

## Market context

| Index | Close | Change | Source |
|---|---:|---:|---|
| ASX 200 (`^AXJO`) | 8,809.9 | +0.17% | Yahoo Finance |
| S&P/TSX Composite (`^GSPTSE`) | 35,944.16 | +0.44% | Yahoo Finance |
| BEL 20 (`^BFX`) | 5,783.75 | +0.03% | Yahoo Finance |
| DAX (`^GDAXI`) | 25,410.84 | +0.91% | Yahoo Finance |
| OMX Copenhagen 20 (`^OMXC20`) | 1,579.8345 | +1.05% | Yahoo Finance |
| IBEX 35 (`^IBEX`) | 19,033.3 | +0.23% | Yahoo Finance |
| OMX Helsinki 25 (`^OMXH25`) | 6,290.255 | +1.83% | Yahoo Finance |
| CAC 40 (`^FCHI`) | 7,847.32 | +0.83% | Yahoo Finance |
| ATHEX | — | +1.09% | median of the region's liquid names (no Yahoo index symbol) |
| FTSE MIB (`FTSEMIB.MI`) | 49,186.81 | +1.29% | Yahoo Finance |
| AEX (`^AEX`) | 1,133.19 | +0.14% | Yahoo Finance |
| PSI 20 (`PSI20.LS`) | 9,175.73 | -0.74% | Yahoo Finance |
| Nikkei 225 (`^N225`) | 62,189.65 | -0.80% | Yahoo Finance |

| Region | Rows | Median | Up / down / flat | Min | Max |
|---|---:|---:|---|---:|---:|
| au | 302 | +0.52% | 171 / 106 / 25 | -30.49% | +10.96% |
| ca | 658 | +0.00% | 322 / 248 / 88 | -7.53% | +77.45% |
| eu-be | 75 | +0.10% | 38 / 29 / 8 | -4.46% | +3.22% |
| eu-de | 115 | +1.24% | 83 / 32 / 0 | -4.66% | +8.71% |
| eu-dk | 75 | +0.60% | 47 / 26 / 2 | -14.23% | +12.10% |
| eu-es | 144 | +0.00% | 70 / 34 / 40 | -6.41% | +6.64% |
| eu-fi | 100 | +0.74% | 67 / 29 / 4 | -4.38% | +7.30% |
| eu-fr | 255 | +0.47% | 160 / 67 / 27 | -12.46% | +10.29% |
| eu-gr | 86 | +0.50% | 56 / 18 / 12 | -3.04% | +4.55% |
| eu-it | 181 | +0.69% | 125 / 37 / 19 | -6.27% | +12.97% |
| eu-nl | 56 | +0.35% | 32 / 24 / 0 | -6.54% | +4.72% |
| eu-pt | 27 | +0.22% | 14 / 8 / 5 | -10.84% | +2.81% |
| jp | 1,395 | +0.37% | 842 / 513 / 40 | -15.65% | +26.14% |

## Top movers

Liquid subset: market cap ≥ $1bn, volume ≥ 100,000, carry-over rows removed.

| Region | Ticker | Name | Change | Close | Volume | Mkt cap (USD) | Catalyst |
|---|---|---|---:|---:|---:|---:|---|
| jp | `TSE:9449` | GMO Internet Group, Inc. | -15.65% | 3179.0 | 3,861,000 | $2.47bn | no catalyst research in this run |
| eu-dk | `OMXCOP:GMAB` | Genmab A/S | +12.10% | 2964.0 | 470,264 | $23.63bn | no catalyst research in this run |
| eu-fr | `EURONEXT:GTT` | Gaztransport & Technigaz SA | -11.66% | 181.1 | 728,557 | $8.45bn | no catalyst research in this run |
| au | `ASX:ZIP` | Zip Co Ltd. | +10.96% | 1.62 | 59,427,965 | $1.28bn | no catalyst research in this run |
| eu-pt | `EURONEXT:GALP` | Galp Energia, SGPS S.A. Class B | -10.84% | 20.47 | 4,465,065 | $18.92bn | no catalyst research in this run |
| eu-fr | `EURONEXT:NANO` | Nanobiotix SA | +9.46% | 28.22 | 355,429 | $1.46bn | no catalyst research in this run |
| eu-fr | `EURONEXT:ETL` | Eutelsat Communications SA | +8.59% | 1.9205 | 2,704,718 | $2.33bn | no catalyst research in this run |
| au | `ASX:PLS` | PLS Group Limited | +8.40% | 2.84 | 34,792,072 | $5.93bn | no catalyst research in this run |
| eu-dk | `OMXCOP:NTG` | NTG Nordic Transport Group A/S | +8.00% | 337.5 | 163,948 | $1.04bn | no catalyst research in this run |
| au | `ASX:APE` | Eagers Automotive Limited | +7.75% | 20.03 | 904,316 | $3.68bn | no catalyst research in this run |
| au | `ASX:MI6` | Minerals 260 Limited | +7.58% | 0.71 | 12,116,304 | $1.15bn | no catalyst research in this run |
| au | `ASX:PDI` | PDI Gold Limited | +7.34% | 3.8 | 3,034,141 | $2.46bn | no catalyst research in this run |
| jp | `TSE:6923` | Stanley Electric Co., Ltd. | -7.18% | 3360.0 | 2,436,400 | $2.82bn | no catalyst research in this run |
| au | `ASX:GGP` | Greatland Resources Limited | +7.03% | 9.29 | 2,108,956 | $4.08bn | no catalyst research in this run |
| au | `ASX:OBM` | Ora Banda Mining Ltd. | +6.76% | 1.185 | 10,338,727 | $1.51bn | no catalyst research in this run |
| eu-de | `XETR:DEZ` | DEUTZ AG | +6.63% | 10.29 | 942,570 | $1.81bn | no catalyst research in this run |
| eu-es | `BME:TEF` | Telefonica SA | -6.41% | 3.198 | 37,667,694 | $21.56bn | no catalyst research in this run |
| jp | `TSE:3769` | GMO Payment Gateway, Inc. | -6.29% | 8176.0 | 830,900 | $4.20bn | no catalyst research in this run |
| au | `ASX:LTR` | Liontown Limited | +6.25% | 0.68 | 38,285,626 | $1.43bn | no catalyst research in this run |
| jp | `TSE:4588` | Oncolys BioPharma, Inc. | +6.24% | 6300.0 | 1,575,600 | $1.11bn | no catalyst research in this run |
| jp | `TSE:4385` | Mercari, Inc. | -6.21% | 3474.0 | 2,752,700 | $3.89bn | no catalyst research in this run |
| eu-it | `MIL:GVS` | GVS S.p.A | +6.08% | 5.58 | 388,103 | $1.11bn | no catalyst research in this run |
| eu-es | `BME:TRE` | Tecnicas Reunidas SA | +5.99% | 27.6 | 114,310 | $2.27bn | no catalyst research in this run |
| jp | `TSE:6323` | Rorze Corporation | -5.93% | 3440.0 | 4,870,900 | $4.09bn | no catalyst research in this run |
| jp | `TSE:7459` | MEDIPAL HOLDINGS Corporation | +5.93% | 3396.0 | 771,900 | $3.69bn | no catalyst research in this run |

| Region | Largest mover | Change |
|---|---|---:|
| au | `ASX:ZIP` Zip Co Ltd. | +10.96% |
| ca | `TSX:SEA` Seabridge Gold Inc | +5.36% |
| eu-be | `EURONEXT:UMI` Umicore SA | +2.56% |
| eu-de | `XETR:DEZ` DEUTZ AG | +6.63% |
| eu-dk | `OMXCOP:GMAB` Genmab A/S | +12.10% |
| eu-es | `BME:TEF` Telefonica SA | -6.41% |
| eu-fi | `OMXHEX:WRT1V` Wartsila Oyj Abp | +5.62% |
| eu-fr | `EURONEXT:GTT` Gaztransport & Technigaz SA | -11.66% |
| eu-gr | `ATHEX:ALPHA` Alpha Bank S.A. | +4.27% |
| eu-it | `MIL:GVS` GVS S.p.A | +6.08% |
| eu-nl | `EURONEXT:BFIT` Basic-Fit NV | +3.34% |
| eu-pt | `EURONEXT:GALP` Galp Energia, SGPS S.A. Class B | -10.84% |
| jp | `TSE:9449` GMO Internet Group, Inc. | -15.65% |

## Method

- **Universe** — one POST per country to `scanner.tradingview.com/{country}/scan`, filtered on `type=stock` and the issuer country, sorted by `market_cap_basic` desc, paged at 3,000 rows.
- **Venue collapse** — exact-symbol dedupe, then primary-venue dedupe, then venue-duplicate collapse on the normalised company name with the region's primary venue preferred. One canonical row per company per region.
- **`market_cap`** — TradingView's `market_cap_basic` is denominated in the **listing currency**, not USD. Verified by share-count reconciliation (`market_cap_basic / close` returns the issuer's real share count: Royal Bank 1,374m, Toronto-Dominion 1,677m, BMO 689m, Shopify 1,288m) and by a server-side filter of `market_cap_basic > 300000000` on the Japan endpoint that still returns names with a market cap of ¥385m. The floors are therefore applied **after** converting to USD.
- **FX** — the 2026-10-26 rate table measured at 16:33 ET from Yahoo Finance: EUR 1.117818, JPY 0.0063480, AUD 0.701902, CAD 0.713222, DKK 0.149520 (USD per one unit of local currency). `USDCAD=X` and `USDDKK=X` quote local-per-USD and are inverted.
- **Floor** — per-region USD market-cap floor, plus a volume gate for Australia (≥ 100,000) and Germany (≥ 50,000). Rows the source reports no market cap for are excluded, not written blank; they are indexed in `_excluded.json`.
- **Liquid subset** (movers) — market cap ≥ $1bn and volume ≥ 100,000, carry-over rows removed.

## Caveats

- **1,457 rows did not trade on 2026-10-26.** The screener returns the last session's close and change for a row that did not trade, which is true of the instrument but false as a statement about the day. The rows are kept exactly as the source returned them (the schema is fixed at 14 columns) and the affected tickers are listed in `_carryover.json` with each instrument's last trade date. Every movers table above excludes them.
- **187 rows were excluded for having no reported market cap.** They cannot be screened against the floor; they are listed in `_excluded.json` so the exclusion is recoverable.
- **The FX table was corrected during this restatement.** The original run stored CAD as 1.402160 (CAD per USD) without inverting it, which overstated every Canadian market cap by ~1.97x and made the run's Canadian liquidity filter too loose. The published CSVs are unaffected — they carry listing-currency `market_cap` and no conversion — but the restatement uses the corrected rate.
- **Venue-duplicate collapse inflates the apparent size of preferred and share-class lines.** Where a company is quoted on several venues, the canonical row is the primary one.
- **This session did no catalyst research.** The `Catalyst` column reads *no catalyst research in this run* for every row. This is a data snapshot; no reason for any move is asserted.
- **Cross-listings are not deduplicated against the US snapshot.** A name listed in two markets appears in both files with different closes.

## Source health

| Source | Query / URL | Status | Result |
|---|---|---|---|
| TradingView scanner (per-country) | `POST https://scanner.tradingview.com/{australia,japan,canada,germany,france,italy,spain,netherlands,belgium,portugal,finland,denmark,greece}/scan` | `ok` | 13/13 regions HTTP 200, 15,862 stock rows pulled, 0 errors |
| Yahoo Finance (cross-check) | `v7/finance/spark` (batches of 12) + `v8/finance/chart` | `ok` | 9,921 of 10,457 rows mapped and checked on close and change; 8,241 full agreement, 44 change-only, 17 mismatches, 1,457 not traded today |
| Yahoo Finance (index levels) | `v8/finance/chart` | `ok` (partial) | 12 of 13 region indices; no Yahoo symbol exists for the ATHEX index, so the Greek figure is the median of the region's liquid names |
| Yahoo Finance (FX) | `v8/finance/chart` on `EURUSD=X`, `USDJPY=X`, `AUDUSD=X`, `USDCAD=X`, `USDDKK=X` | `ok` | 2026-10-26 table, 5 currencies |
| `mcp__tradingview_advanced__*`, `mcp__yahoo_finance__*` | — | `unavailable` | not registered in this runtime (as documented in the cron prompt); the public scanner API replaced them |

## Files

`international-eod/2026-10-26/` — `au.csv`, `ca.csv`, `eu-be.csv`, `eu-de.csv`, `eu-dk.csv`, `eu-es.csv`, `eu-fi.csv`, `eu-fr.csv`, `eu-gr.csv`, `eu-it.csv`, `eu-nl.csv`, `eu-pt.csv`, `jp.csv`, `summary.md`, `_manifest.json`, `_excluded.json`, `_carryover.json`

Schema: `date,ticker,name,open,high,low,close,volume,change_pct,market_cap,pe_ratio,sector,currency,exchange`. Missing values are empty cells, never `N/A`. `market_cap` is USD; all other numeric fields are in the listing currency named by the `currency` column.
