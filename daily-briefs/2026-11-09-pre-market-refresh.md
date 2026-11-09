---
date: 2026-11-09
cron: 26-agentic-pre-market-brief-refresh
fire_time_et: 2026-11-09 09:20
snapshot_et: 09:22
source: TradingView america scanner
status: ok
changes_since_morning: 270
---

# Pre-market refresh — 2026-11-09

**09:20 ET refresh of the 08:30 ET pre-market brief.** Snapshot **09:22 ET**. Reference: `daily-briefs/2026-11-09-pre-market.csv` (the morning brief's own screen, snapshot 08:44 ET).

This is a refresh, not a second brief: it re-pulls the same screen and reports what moved. It carries no catalysts and no news — a name that needs explaining belongs in the next brief.

**One pull.** Every price, percentage and volume below comes from a single screen pull at 09:22 ET (the TradingView `america` scanner, gainers + losers, 462 + 231 = 693 rows; both screens asserted `len(rows) == totalCount`). Nothing in this file was re-fetched after the pull.

## Bottom line

1. **The one setup** — **DCTH** — break above the pre-market high **18.99** is the trigger (last print 18.8643, +26.35%, still at the top of its 15.95–18.99 pre-market range); invalidated by a trade back to/below prior close **14.93**. Driver `EARNINGS-RECONFIRM+ANCHORED` — the 08:30 brief's earnings table: Q3 beat, no debt, $95.9M cash.
2. **The one risk** — **NWGL** — the tape's biggest gainer has no sourced catalyst and is already handing its gap back (last 3.6191 against a 6.51 pre-market high, hold 6%, 881.94% of the 30-day average volume); below the pre-market low **3.43** the pre-market bid is a liquidity unwind, not sponsorship.
3. **The one thing to watch at the open** — **NVDA** — an open below the last pre-market print **175.50** (and below the **174.45** pre-market low) means the governance gap is still being sold; the AI complex trades with it.

## What to watch at the open

| Name | Prior close | PM last | PM low | PM high | Trigger | Invalidation |
|---|---|---|---|---|---|---|
| DCTH | 14.93 | 18.8643 | 15.95 | 18.99 | break above 18.99 | back to/below prior close 14.93 |
| NWGL | 2.53 | 3.6191 | 3.43 | 6.51 | break above 6.51 | back to/below prior close 2.53 |
| NVDA | 186.64 | 175.50 | 174.45 | 181.00 | reclaim above 181.00 | below PM low 174.45 |

- **Rule 1 — the open is the verdict on the gap.** An open BELOW the last pre-market print means the gap is being sold, not bought. Measured 2026-11-04: every name that gave back its gap opened below its last pre-market print (FTCI −0.48%, BRKR −1.67%, FTK −1.57%), and every name that ran opened at or above it. **This refresh fires at 09:20, so it cannot apply Rule 1 — it publishes the last pre-market print and the PM low so the reader can apply it at 09:31.**
- **Rule 2 — the 30-minute candle is the breakout test.** If, thirty minutes after the open, the session high is STILL the opening-range high, the gap is a fade, not a breakout; the levels in this file are then exit levels, not entry levels. A name that breaks its opening range and holds above it is a breakout. This is a 10:00 check, not a 09:45 one.

## Gap quality — can this gap hold?

| Ticker | Name | Gap % | PM range | Hold % | pm %ADV | Print | Driver | Key level | Invalidation |
|---|---|---|---|---|---|---|---|---|---|
| NWGL | CL Workshop Group Limited | +43.05% | 3.43–6.51 | 6 | 881.94% | CHURN+half-filled | NONE | prior close 2.53 | back to/below prior close 2.53 |
| CECO | CECO Environmental Corp. | +41.84% | 46.00–63.5804 | 91 | 5.96% | AUCTION+holding | NONE | prior close 43.71 | back to/below prior close 43.71 |
| GFR | Greenfire Resources Ltd. | +38.58% | 6.72–7.86 | 91 | 112.46% | CHURN+holding | NONE | prior close 5.60 | back to/below prior close 5.60 |
| DCTH | Delcath Systems, Inc. | +26.35% | 15.95–18.99 | 96 | 25.21% | AUCTION+holding | EARNINGS-RECONFIRM+ANCHORED | prior close 14.93 | back to/below prior close 14.93 |
| AIOT | PowerFleet, Inc. | +19.70% | 2.74–3.30 | 86 | 3.41% | AUCTION+holding | NONE | prior close 2.69 | back to/below prior close 2.69 |
| TLS | Telos Corporation | +17.22% | 4.8211–5.79 | 86 | 2.97% | AUCTION+holding | NONE | prior close 4.82 | back to/below prior close 4.82 |
| DDI | DoubleDown Interactive Co., Ltd. - American Depository Shares | +14.37% | 13.50–16.07 | 79 | 204.71% | CHURN+mid | NONE | prior close 13.58 | back to/below prior close 13.58 |
| IMVT | Immunovant, Inc. | +11.37% | 32.18–35.86 | 49 | 4.90% | AUCTION+half-filled | EARNINGS-RECONFIRM+ANCHORED | prior close 30.53 | back to/below prior close 30.53 |
| SGRY | Surgery Partners, Inc. | +11.34% | 23.30–26.10 | 90 | 10.07% | AUCTION+holding | NONE | prior close 23.20 | back to/below prior close 23.20 |
| INO | Inovio Pharmaceuticals, Inc. | +9.47% | 1.28–1.40 | 42 | 11.94% | AUCTION+half-filled | NONE | prior close 1.215 | back to/below prior close 1.215 |
| QXO | QXO, Inc. | +9.43% | 11.74–12.69 | 96 | 1.26% | QUOTE+holding | NONE | prior close 11.56 | back to/below prior close 11.56 |
| TTD | The Trade Desk, Inc. | +8.66% | 12.94–14.09 | 97 | 7.60% | AUCTION+holding | NONE | prior close 12.93 | back to/below prior close 12.93 |
| TMCI | Treace Medical Concepts, Inc. | +7.44% | 4.04–4.33 | 100 | 4.90% | AUCTION+holding | NONE | prior close 4.03 | back to/below prior close 4.03 |
| VFF | Village Farms International, Inc. | +7.29% | 2.95–3.10 | 93 | 27.12% | AUCTION+holding | NONE | prior close 2.88 | back to/below prior close 2.88 |
| THM | International Tower Hill Mines, Ltd. | +7.14% | 1.53–1.65 | 100 | 0.86% | QUOTE+holding | NONE | prior close 1.54 | back to/below prior close 1.54 |
| SOC | Sable Offshore Corp. | -74.41% | 0.3756–2.03 | 7 | 269.72% | CHURN+half-filled | NONE | prior close 1.93 | below PM low 0.3756 |
| ZURA | Zura Bio Limited | -68.92% | 0.89–4.20 | 12 | 172.44% | CHURN+half-filled | EARNINGS-CUT+ANCHORED | prior close 4.09 | below PM low 0.89 |
| VISN | Vistance Networks, Inc. | -25.39% | 4.10–4.4292 | 0 | 1.17% | QUOTE+half-filled | NONE | prior close 5.50 | below PM low 4.10 |
| IONS | Ionis Pharmaceuticals, Inc. | -19.33% | 29.84–40.50 | 18 | 11.78% | AUCTION+half-filled | EARNINGS-CUT | prior close 39.42 | below PM low 29.84 |
| FTH | Faeth Therapeutics, Inc. | -19.32% | 12.00–24.00 | 48 | 24.63% | AUCTION+half-filled | NONE | prior close 22.05 | below PM low 12.00 |
| NKTX | Nkarta, Inc. | -15.61% | 1.3503–1.84 | 22 | 26.36% | AUCTION+half-filled | NONE | prior close 1.73 | below PM low 1.3503 |
| CEVA | CEVA, Inc. | -15.09% | 21.65–26.20 | 30 | 5.13% | AUCTION+half-filled | SECTOR-BETA | prior close 27.10 | below PM low 21.65 |
| IBRX | ImmunityBio, Inc. | -12.67% | 7.20–9.09 | 18 | 17.38% | AUCTION+half-filled | EARNINGS-CUT+ANCHORED | prior close 8.635 | below PM low 7.20 |
| ABEO | Abeona Therapeutics Inc. | -11.99% | 3.50–4.34 | 20 | 16.23% | AUCTION+half-filled | NONE | prior close 4.17 | below PM low 3.50 |
| MNDY | monday.com Ltd. | -11.86% | 75.99–87.50 | 13 | 17.36% | AUCTION+half-filled | EARNINGS-CUT | prior close 87.93 | below PM low 75.99 |

**How the Driver column was set.** Read from the 08:30 brief — its §2 theme clusters, its §9 earnings table and the earnings-reaction cross-check it cites. **No news was searched for this file.**

- **Print is a descriptor, not a filter.** `AUCTION` = 2 ≤ pm %ADV ≤ 30, `QUOTE` = pm %ADV < 2, `CHURN` = pm %ADV > 30; `holding` = Hold % ≥ 80, `half-filled` = < 50, `mid` otherwise. Read them to see HOW the gap was made; rank on the Driver. On 2026-11-06 zero of the 25 headline names cleared `AUCTION+holding`, so gating on it would publish an empty bottom line on a fine tape.
- **The Driver vocabulary has no class for a clinical readout.** IMVT's beat is a met primary endpoint (ACR20 92.5% vs 75.6% placebo, p=0.0139) inside a fiscal-Q2 results release, so it is classified by the release — `EARNINGS-RECONFIRM` — and it carries the anchor. It is not an EPS beat and the vocabulary does not describe readouts directly.
- **Four of the 25 headline names carry an anchored catalyst**: DCTH, IMVT, ZURA, IBRX. **No headline name carries an anchored catalyst in the five classes this procedure's setup slot names** (`CASH-OUT` / `CASH-IN` / `LIABILITY-RESOLVED` / `ASSET-VALUE` / `EARNINGS-RAISE`) — the anchored names are two `EARNINGS-RECONFIRM` and two `EARNINGS-CUT`. DCTH fills the slot because it is the only anchored name whose gap is still holding (Hold 96%); no unanchored name was promoted to fill it.
- **Three names have no sourced catalyst at all**: NWGL and GFR (the 08:30 brief calls them shells with no sourced single-name catalyst) and CECO (not in any cluster, `has_news = no`; the earnings cross-check the brief cites records a Q3 2026 release pre-market but carries no reported figures). A gap with no sourced catalyst is a finding, not a blank.
- **IONS and MNDY are pre-open prints the tape sold** (`EARNINGS-CUT`), but the 08:30 brief carries no reported figure for either, so neither takes the `+ANCHORED` suffix.
- **CEVA** printed before the open, but the brief attributes its move to the AI/auto-IP complex — `SECTOR-BETA`. **TTD** prints after the close and has no result yet, so it takes no class.

## Refreshed top-of-book

### Top 15 gainers — 09:22 ET

| Ticker | Name | Pre-market | % | PM range | Pm vol | %ADV | Mkt cap | Sector | Snapshot |
|---|---|---|---|---|---|---|---|---|---|
| NWGL | CL Workshop Group Limited | 3.6191 | +43.05% | 3.43–6.51 | 4,968,604 | 881.94% | $143.0M | Non-Energy Minerals | 09:22 ET |
| CECO | CECO Environmental Corp. | 62.00 | +41.84% | 46.00–63.5804 | 69,941 | 5.96% | $2.56B | Producer Manufacturing | 09:22 ET |
| GFR | Greenfire Resources Ltd. | 7.7605 | +38.58% | 6.72–7.86 | 1,279,673 | 112.46% | $1.35B | Energy Minerals | 09:22 ET |
| DCTH | Delcath Systems, Inc. | 18.8643 | +26.35% | 15.95–18.99 | 84,569 | 25.21% | $518.1M | Health Technology | 09:22 ET |
| AIOT | PowerFleet, Inc. | 3.22 | +19.70% | 2.74–3.30 | 55,201 | 3.41% | $361.1M | Technology Services | 09:22 ET |
| TLS | Telos Corporation | 5.65 | +17.22% | 4.8211–5.79 | 22,448 | 2.97% | $360.2M | Technology Services | 09:22 ET |
| DDI | DoubleDown Interactive Co., Ltd. - American Depository Shares | 15.5315 | +14.37% | 13.50–16.07 | 283,430 | 204.71% | $672.9M | Technology Services | 09:22 ET |
| IMVT | Immunovant, Inc. | 34.00 | +11.37% | 32.18–35.86 | 68,252 | 4.90% | $6.31B | Health Technology | 09:22 ET |
| SGRY | Surgery Partners, Inc. | 25.83 | +11.34% | 23.30–26.10 | 474,491 | 10.07% | $2.99B | Health Services | 09:22 ET |
| INO | Inovio Pharmaceuticals, Inc. | 1.33 | +9.47% | 1.28–1.40 | 2,080,728 | 11.94% | $125.6M | Health Technology | 09:22 ET |
| QXO | QXO, Inc. | 12.65 | +9.43% | 11.74–12.69 | 270,997 | 1.26% | $11.99B | Distribution Services | 09:22 ET |
| TTD | The Trade Desk, Inc. | 14.05 | +8.66% | 12.94–14.09 | 1,191,422 | 7.60% | $6.11B | Technology Services | 09:22 ET |
| TMCI | Treace Medical Concepts, Inc. | 4.33 | +7.44% | 4.04–4.33 | 11,282 | 4.90% | $262.1M | Health Technology | 09:22 ET |
| VFF | Village Farms International, Inc. | 3.0899 | +7.29% | 2.95–3.10 | 209,472 | 27.12% | $352.2M | Process Industries | 09:22 ET |
| THM | International Tower Hill Mines, Ltd. | 1.65 | +7.14% | 1.53–1.65 | 10,457 | 0.86% | $402.9M | Non-Energy Minerals | 09:22 ET |

### Top 10 decliners — 09:22 ET

| Ticker | Name | Pre-market | % | PM range | Pm vol | %ADV | Mkt cap | Sector | Snapshot |
|---|---|---|---|---|---|---|---|---|---|
| SOC | Sable Offshore Corp. | 0.4939 | -74.41% | 0.3756–2.03 | 21,544,510 | 269.72% | $370.3M | Energy Minerals | 09:22 ET |
| ZURA | Zura Bio Limited | 1.2711 | -68.92% | 0.89–4.20 | 7,250,942 | 172.44% | $394.0M | Health Technology | 09:22 ET |
| VISN | Vistance Networks, Inc. | 4.10 | -25.39% | 4.10–4.4292 | 69,070 | 1.17% | $813.3M | Electronic Technology | 09:22 ET |
| IONS | Ionis Pharmaceuticals, Inc. | 31.80 | -19.33% | 29.84–40.50 | 333,912 | 11.78% | $6.55B | Health Technology | 09:22 ET |
| FTH | Faeth Therapeutics, Inc. | 17.79 | -19.32% | 12.00–24.00 | 85,841 | 24.63% | $569.9M | Health Technology | 09:22 ET |
| NKTX | Nkarta, Inc. | 1.46 | -15.61% | 1.3503–1.84 | 276,684 | 26.36% | $124.0M | Health Technology | 09:22 ET |
| CEVA | CEVA, Inc. | 23.01 | -15.09% | 21.65–26.20 | 27,365 | 5.13% | $763.0M | Electronic Technology | 09:22 ET |
| IBRX | ImmunityBio, Inc. | 7.5407 | -12.67% | 7.20–9.09 | 2,400,523 | 17.38% | $9.15B | Health Technology | 09:22 ET |
| ABEO | Abeona Therapeutics Inc. | 3.67 | -11.99% | 3.50–4.34 | 176,690 | 16.23% | $238.5M | Health Technology | 09:22 ET |
| MNDY | monday.com Ltd. | 77.50 | -11.86% | 75.99–87.50 | 195,581 | 17.36% | $3.72B | Technology Services | 09:22 ET |

**Thin tape** — passed the liquidity gate (pre-market volume ≥ 100,000 shares, or market cap ≥ $200M with ≥ 10,000 pre-market shares) but below the $100M quality floor, so they never top a headline table. 23 gainers and 25 decliners qualify; the largest are below.

| Ticker | Name | Pre-market | % | Mkt cap | Pm vol | Snapshot |
|---|---|---|---|---|---|---|
| OMH | Ohmyhome Limited | 21.80 | +196.20% | $15.5M | 4,295,813 | 09:22 ET |
| CKX | CKX Lands, Inc. | 17.21 | +65.96% | $21.3M | 1,447,237 | 09:22 ET |
| JDZG | JIADE LIMITED | 0.3291 | +56.57% | $1.1M | 80,178,911 | 09:22 ET |
| EDSA | Edesa Biotech, Inc. | 2.98 | +39.25% | $28.9M | 17,753,435 | 09:22 ET |
| NTCL | NETCLASS TECHNOLOGY INC | 0.3031 | +33.23% | $482K | 46,507,560 | 09:22 ET |
| INLF | INLIF LIMITED | 0.298 | +29.40% | $351K | 62,733,602 | 09:22 ET |
| SMX | SMX (Security Matters) Public Limited Company | 6.20 | +25.81% | $1.9M | 138,007 | 09:22 ET |
| NCPL | Netcapital Inc. | 1.5385 | +22.10% | $9.9M | 1,398,630 | 09:22 ET |
| HRTX | Heron Therapeutics, Inc. | 0.357 | +21.84% | $55.6M | 80,972,754 | 09:22 ET |
| TGE | The Generation Essentials Group | 0.438 | +20.50% | $17.6M | 15,168,678 | 09:22 ET |
| LICN | Lichen International Limited | 0.2999 | -41.24% | $8.3M | 188,235 | 09:22 ET |
| PLCE | Children's Place, Inc. (The) | 0.219 | -31.99% | $7.2M | 1,933,605 | 09:22 ET |
| DBGI | Digital Brands Group, Inc. | 0.201 | -28.90% | $264K | 19,341,595 | 09:22 ET |
| PARA | Parabolic Technologies, Inc. | 0.0818 | -28.56% | $75K | 25,197,598 | 09:22 ET |
| RCT | RedCloud Holdings plc | 0.0322 | -24.06% | $3.2M | 10,679,873 | 09:22 ET |
| KPTI | Karyopharm Therapeutics Inc. | 0.0446 | -18.76% | $1.2M | 2,632,860 | 09:22 ET |
| SDA | SunCar Technology Group Inc. | 0.3061 | -18.70% | $38.4M | 4,610,299 | 09:22 ET |
| RAYA | Erayak Power Solution Group Inc. | 0.688 | -18.50% | $908K | 234,876 | 09:22 ET |
| CDT | CDT Equity Inc. | 1.0797 | -17.58% | $1.3M | 1,806,212 | 09:22 ET |
| YFOR | YYForce Inc. | 0.098 | -16.81% | $1.5M | 1,720,389 | 09:22 ET |

## What changed since the morning brief

The morning brief's CSV is the reference: same rows, same screen, one pull earlier. **537 names** appear in both the live screen and the morning CSV; **270 of them disagree by more than 0.2 percentage points**, which is the definition of "the market moved". The other 267 moved by 0.2pp or less — 163 strengthened, 107 weakened.

> **Comparison base.** The morning brief's CSV carries 931 rows, of which 600 are in its ±3% band; the 08:44 brief published that band as 598 names (392 gainers + 206 decliners). This pull read the band in full — 693 names (462 + 231), both screens asserted complete — so the *level* counts are not comparable across the two pulls; the *delta* tables are, because every row in them is present in both.

### Biggest gap changes — 09:22 ET vs 08:44 ET

| Ticker | Name | 08:44 gap | 09:22 gap | Change (pp) | Pre-market | Mkt cap | Snapshot |
|---|---|---|---|---|---|---|---|
| OMH | Ohmyhome Limited | +158.29% | +196.20% | +37.91 | 21.80 | $15.5M | 09:22 ET |
| HRTX | Heron Therapeutics, Inc. | +43.24% | +21.84% | -21.40 | 0.357 | $55.6M | 09:22 ET |
| SOC | Sable Offshore Corp. | -55.24% | -74.41% | -19.17 | 0.4939 | $370.3M | 09:22 ET |
| NCPL | Netcapital Inc. | +3.97% | +22.10% | +18.13 | 1.5385 | $9.9M | 09:22 ET |
| AUID | authID Inc. | +2.51% | +20.54% | +18.03 | 0.2261 | $3.1M | 09:22 ET |
| JDZG | JIADE LIMITED | +73.26% | +56.57% | -16.69 | 0.3291 | $1.1M | 09:22 ET |
| CVRX | CVRx, Inc. | +0.00% | +15.38% | +15.38 | 1.0023 | $24.7M | 09:22 ET |
| XELB | Xcel Brands, Inc | +4.59% | -10.12% | -14.71 | 0.39 | $3.0M | 09:22 ET |
| EDSA | Edesa Biotech, Inc. | +24.68% | +39.25% | +14.57 | 2.98 | $28.9M | 09:22 ET |
| LICN | Lichen International Limited | -26.78% | -41.24% | -14.46 | 0.2999 | $8.3M | 09:22 ET |
| SPRB | Spruce Biosciences, Inc. | -3.18% | -15.15% | -11.97 | 39.50 | $133.8M | 09:22 ET |
| IPDN | Professional Diversity Network, Inc. | +5.19% | -6.66% | -11.85 | 1.2601 | $899K | 09:22 ET |
| DOGZ | Dogness (International) Corporation | +16.52% | +4.92% | -11.60 | 0.484 | $8.1M | 09:22 ET |
| RVSN | Rail Vision Ltd. | -3.24% | +7.91% | +11.15 | 3.00 | $6.1M | 09:22 ET |
| CABR | Caring Brands, Inc. | -3.82% | +6.86% | +10.68 | 1.09 | $10.7M | 09:22 ET |

### Did the morning brief's own leaders hold?

| Morning headline group | Still in the ±3% screen | Strengthened | Weakened | Flat (≤0.2pp) |
|---|---|---|---|---|
| Its top 15 gainers | 15 / 15 | 3 | 8 | 4 |
| Its top 10 decliners | 10 / 10 | 4 | 6 | 0 |

Morning's top 15 gainers, now:

| Ticker | 08:44 gap | 09:22 gap | Change (pp) | Pre-market |
|---|---|---|---|---|
| NWGL | +50.99% | +43.05% | -7.94 | 3.6191 |
| GFR | +38.39% | +38.58% | +0.19 | 7.7605 |
| CECO | +36.58% | +41.84% | +5.26 | 62.00 |
| DCTH | +19.83% | +26.35% | +6.52 | 18.8643 |
| AIOT | +17.32% | +19.70% | +2.38 | 3.22 |
| DDI | +17.16% | +14.37% | -2.79 | 15.5315 |
| IMVT | +11.37% | +11.37% | -0.00 | 34.00 |
| INO | +9.47% | +9.47% | -0.00 | 1.33 |
| ADCT | +8.23% | +3.80% | -4.43 | 1.64 |
| VIR | +8.11% | +6.55% | -1.56 | 13.01 |
| AUTL | +7.73% | +7.03% | -0.70 | 1.37 |
| TMCI | +7.44% | +7.44% | +0.00 | 4.33 |
| ALLO | +7.18% | +3.40% | -3.78 | 1.0754 |
| STLN | +6.91% | +6.35% | -0.56 | 3.85 |
| PCT | +6.31% | +4.16% | -2.15 | 1.7343 |

Morning's top 10 decliners, now:

| Ticker | 08:44 gap | 09:22 gap | Change (pp) | Pre-market |
|---|---|---|---|---|
| ZURA | -68.71% | -68.92% | -0.21 | 1.2711 |
| SOC | -55.24% | -74.41% | -19.17 | 0.4939 |
| VISN | -24.66% | -25.39% | -0.73 | 4.10 |
| IONS | -21.39% | -19.33% | +2.06 | 31.80 |
| NKTX | -19.08% | -15.61% | +3.47 | 1.46 |
| CEVA | -13.99% | -15.09% | -1.10 | 23.01 |
| IBRX | -13.84% | -12.67% | +1.17 | 7.5407 |
| FTH | -13.83% | -19.32% | -5.49 | 17.79 |
| ABEO | -9.83% | -11.99% | -2.16 | 3.67 |
| OCUL | -9.48% | -4.47% | +5.01 | 6.30 |

### Faded out of the band

**90 names** were in the 08:44 band and are **not** in the 09:22 band — their gap is no longer large enough to clear the ±3% line. They are not ranked below: the screen returns two disjoint lists, so a name outside both has no current gap to publish. The largest fades:

| Ticker | 08:44 gap | Now |
|---|---|---|
| NXTT | +10.21% | outside the ±3% screen |
| RCON | +8.55% | outside the ±3% screen |
| GELS | -8.05% | outside the ±3% screen |
| QXL | -7.86% | outside the ±3% screen |
| AVTX | +6.93% | outside the ±3% screen |
| GIXI | +6.59% | outside the ±3% screen |
| LIMN | +6.28% | outside the ±3% screen |
| DXF | +6.23% | outside the ±3% screen |
| IQ | -6.00% | outside the ±3% screen |
| CTNT | +5.73% | outside the ±3% screen |
| RC | +5.67% | outside the ±3% screen |
| MKDW | +5.55% | outside the ±3% screen |

### New entrants

**183 names** were not in the 08:44 band and **are** in the 09:22 band — their pre-market volume grew past the filter or the gap opened after the brief was published. The largest:

| Ticker | 09:22 gap | Pre-market | Mkt cap | Pm vol |
|---|---|---|---|---|
| ALPS | +400.45% (unreconciled) | 1.65 | $54.9M | 500 |
| NXTS | -37.38% | 1.61 | $1.5M | 2,000 |
| SMX | +25.81% | 6.20 | $1.9M | 138,007 |
| AUID | +20.54% | 0.2261 | $3.1M | 3,316 |
| TLS | +17.22% | 5.65 | $360.2M | 22,448 |
| CVRX | +15.38% | 1.0023 | $24.7M | 1,062 |
| SGRY | +11.34% | 25.83 | $2.99B | 474,491 |
| BRAG | +11.01% | 0.852 | $23.8M | 530 |
| ACFN | +11.00% | 16.24 | $37.1M | 500 |
| SCNI | +11.00% | 0.4895 | $597K | 3,051 |
| NSPR | +10.92% | 0.772 | $32.4M | 100 |
| WLDS | +10.00% | 1.43 | $3.2M | 1,409 |

### Direction on the comparable set (537 names)

| Measure | 08:44 ET | 09:22 ET |
|---|---|---|
| Names in the ±3% band | 598 | 693 |
| Gap-up names in the comparable set | 325 | 346 |
| Gap-down names in the comparable set | 180 | 191 |
| Average gap on the comparable set | +1.70% | +1.85% |
| Names that strengthened / weakened | — | 163 / 107 |

## Verdict

**Broader and shallower, not more directional.** The ±3% band widened 598 → 693 names and the comparable set's average gap rose +1.70% → +1.85%, but the leadership deteriorated at both ends: the biggest gainer is unwinding (NWGL hold 6%) with no sourced catalyst, and the tape's anchor weakened (NVDA −5.45% → −5.97%, hold 16%), while 90 morning names faded out of the band against 183 new entrants. The trade at 09:30 is in the anchored, holding names — DCTH at hold 96% is the only one — not in the leaderboard.

## Source health

- **One pull.** 09:22 ET, TradingView `america` scanner, gainers + losers. Both screens asserted `len(rows) == totalCount` (462/462 and 231/231) — the ±3% band counts in this file are exact, not floors. The CSV beside this file is the same merged table: 693 rows.
- **Close reconciliation sweep.** The identity `premarket_change == (premarket_close − close) / close` was checked on every published row; 2 of the 693 rows failed it.
  - **VISN — corrected, and published.** The scanner's `close` field reads 3.995 and does not reconcile with its own pre-market print (4.10, range 4.10–4.4292) or its own gap (−25.39%). An independent quote from the bridge (`market-recap get_quotes`) puts Friday's close at **5.495**, and with 5.495 the scanner's print and gap reconcile exactly (the derived reference from the scanner's own fields is 5.4949). This file publishes the bridge-confirmed prior close **5.50**, the same figure the 08:30 brief published. The defect is in the scanner's `close`, not in the gap.
  - **ALPS — excluded, not published.** The scanner carries `close` 1.6485 against a `premarket_change` of +400.45%, which references 0.3297 — the two are mutually inconsistent, and the bridge's own Friday bar shows a 0.31–0.3306 range against a 1.6485 close (the signature of a 1-for-5 reverse split between Friday's close and this pre-market). ALPS fails the liquidity gate outright — 500 pre-market shares, $54.9M cap — so it is in no headline or thin-tape table in this file. It appears in the new-entrant list above with its gap marked unreconciled, and no key level, invalidation or driver is published for it.
- **The companion CSV's `live_*` columns are empty by construction.** The regular session had not opened at the 09:22 ET pull (09:30 open), so there is no live regular-session price, change or volume to publish. They are blank, not zero. `prior_close` is derived as `premarket_close / (1 + premarket_change / 100)`, and `prior_session_change_pct` is the scanner's last completed session's `change`.
- **No catalysts were searched.** Every Driver is read from the 08:30 brief's §2 clusters, its §9 earnings table and the earnings-reaction cross-check that brief cites. Where that material carries no catalyst for a name, the Driver is `NONE` — that is a finding, not a blank.
- **The upstream fire was healthy.** The 08:30 brief published at 08:44 ET with `screen_complete: true`, 598 names in the band and 931 CSV rows; it was neither quota-killed nor missed. This file is not provisional.
- **Reconciliation against the 08:30 brief.** The 537-name comparable set is the only base used for the delta tables; the level counts differ because this pull read the band in full while the morning pull's screen was capped.
