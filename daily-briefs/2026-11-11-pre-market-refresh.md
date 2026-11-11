---
date: 2026-11-11
cron: 26-agentic-pre-market-brief-refresh
routine: 26b
fire_time_et: 2026-11-11 09:20
snapshot_et: 09:21
source: TradingView america scanner
status: ok
changes_since_morning: 381
up_3pct: 638
down_3pct: 169
screen_complete: true
---

# Pre-market refresh - Wednesday 2026-11-11

## Bottom line

1. **The one setup** - **FOSL** (Fossil Group, Inc.) - a long on a break of its pre-market high **10.09**; invalidated by a trade back to/below prior close **7.87**. Driver **EARNINGS-RAISE+ANCHORED** - its own Q3: adjusted EPS $0.23 against a $0.04 loss expected, sales $271.2m against $248.7m expected, FY2026 sales guidance raised to $980-990m from $953.8-973.9m, Diesel licensing extended to 2032.
2. **The one risk** - **NVDA** - the anchor of the whole AI bid is fading: **174.03** against a 178.36 pre-market high is a **24% Hold** (the range is being given back) after **+3.86%** at the 08:37 brief - a trade back to/below prior close **168.90** unwinds the complex that six of the fifteen gainers sit in, with the 10-year at **4.998%** (1.5bp above the brief's 4.983%) against it.
3. **The one thing to watch at the open** - **GEVO** - the largest anchored gap whose range is still intact (**+21.47%**, Hold **89%** on AUCTION volume): an open at or above the **1.6884** pre-market print says the earnings gap is still being bought, an open below the **1.5962** pre-market low says it is gone.

## What to watch at the open

| Name | Prior close | PM last | PM low | PM high | Trigger | Invalidation |
|---|---|---|---|---|---|---|
| FOSL | 7.87 | 9.83 | 9.31 | 10.09 | above 10.09 (PM high) | back to/below prior close 7.87 |
| NVDA | 168.90 | 174.03 | 172.66 | 178.36 | above 178.36 (PM high) | back to/below prior close 168.90 |
| GEVO | 1.39 | 1.6884 | 1.5962 | 1.7 | above 1.7 (PM high) | back to/below prior close 1.39 |

- **Rule 1 - the open is the verdict on the gap.** An open BELOW the last pre-market print means
  the gap is being sold, not bought. Measured 2026-11-04: every name that gave back its gap
  opened below its last pre-market print (FTCI -0.48%, BRKR -1.67%, FTK -1.57%), and every name
  that ran opened at or above it. **This refresh fires at 09:20, so it cannot apply Rule 1 - it
  publishes the last pre-market print and the PM low so the reader can apply it at 09:31.**
- **Rule 2 - the 30-minute candle is the breakout test.** If, thirty minutes after the open, the
  session high is STILL the opening-range high, the gap is a fade, not a breakout; the levels in
  this file are then exit levels, not entry levels. A name that breaks its opening range and
  holds above it is a breakout. This is a 10:00 check, not a 09:45 one.

## 1. Refreshed top-of-book

One pull of the TradingView `america` scanner at **09:21 ET** - **638** names in the +3% band and **169** in the -3% band, `len(rows) == totalCount` asserted on BOTH screens. Gate A (pre-market volume >= 100,000 shares, or cap >= $200M with >= 10,000 pre-market shares) and Gate B (cap >= $100M on the reconciled cap) applied: 226 names clear both gates on the gainer side, 16 on the decliner side.

### Top 15 gainers

| Ticker | Name | Pre-market | % | Pm vol | %ADV | Mkt cap | Sector | Snapshot |
|---|---|---|---|---|---|---|---|---|
| FOSL | Fossil Group, Inc. | 9.83 | +24.90% | 148,981 | 16.8% | $465.4M | Consumer Durables | 09:21 ET |
| RSKD | Riskified Ltd. | 10.44 | +23.11% | 382,881 | 19.8% | $1.22B | Technology Services | 09:21 ET |
| GEVO | Gevo, Inc. | 1.6884 | +21.47% | 512,232 | 17.2% | $343.7M | Process Industries | 09:21 ET |
| SATL | Satellogic Inc. | 4.6 | +17.95% | 723,583 | 15.8% | $599.6M | Electronic Technology | 09:21 ET |
| CRWV | CoreWeave, Inc. | 55.33 | +13.54% | 9,482,107 | 16.7% | $26.88B | Technology Services | 09:21 ET |
| SHAZ | SharonAI Holdings, Inc. | 26.38 | +13.12% | 31,984 | 1.6% | $834.9M | Technology Services | 09:21 ET |
| BRUN | Boost Run Inc. | 7.22 | +12.99% | 31,889 | 0.9% | $535.8M | Technology Services | 09:21 ET |
| CECO | CECO Environmental Corp. | 58.09 | +12.08% | 38,454 | 2.8% | $3.04B | Producer Manufacturing | 09:21 ET |
| HYLN | Hyliion Holdings Corp. | 3.35 | +12.04% | 75,517 | 4.7% | $556.3M | Producer Manufacturing | 09:21 ET |
| BRAI | Braiin Limited | 1.99 | +11.80% | 117,996 | 2.6% | $366.8M | Technology Services | 09:21 ET |
| NBIS | Nebius Group N.V. | 148.9411 | +11.15% | 2,351,452 | 10.5% | $36.43B | Technology Services | 09:21 ET |
| FORM | FormFactor, Inc. | 94.5729 | +10.44% | 10,528 | 0.5% | $6.71B | Electronic Technology | 09:21 ET |
| BGS | B&G Foods, Inc. | 2.93 | +10.15% | 53,960 | 2.5% | $216.2M | Consumer Non-Durables | 09:21 ET |
| AXTI | AXT Inc | 43.2206 | +9.95% | 375,973 | 3.6% | $2.58B | Electronic Technology | 09:21 ET |
| NUAI | New Era Energy & Digital, Inc. | 2.27 | +9.66% | 281,558 | 2.6% | $242.8M | Industrial Services | 09:21 ET |

### Top 10 decliners

| Ticker | Name | Pre-market | % | Pm vol | %ADV | Mkt cap | Sector | Snapshot |
|---|---|---|---|---|---|---|---|---|
| SUJA | Suja Life, Inc. | 7.9 | -20.76% | 29,964 | 15.2% | $332.6M | Consumer Non-Durables | 09:21 ET |
| STIM | Neuronetics, Inc. | 1.68 | -16.42% | 231,137 | 20.4% | $153.2M | Health Technology | 09:21 ET |
| BV | BrightView Holdings, Inc. | 9.96 | -12.86% | 32,917 | 3.3% | $1.06B | Commercial Services | 09:21 ET |
| LWLG | Lightwave Logic, Inc. | 3.8373 | -12.59% | 465,018 | 12.8% | $676.4M | Process Industries | 09:21 ET |
| VELO | Velo3D, Inc. | 5.36 | -11.26% | 136,232 | 7.9% | $180.0M | Producer Manufacturing | 09:21 ET |
| GPRO | GoPro, Inc. | 0.7499 | -11.02% | 467,486 | 6.7% | $161.8M | Consumer Durables | 09:21 ET |
| HGTY | Hagerty, Inc. | 15.5 | -8.50% | 630,786 | 147.8% | $5.82B | Finance | 09:21 ET |
| SPIR | Spire Global, Inc. | 8.59 | -8.13% | 18,924 | 3.5% | $379.8M | Technology Services | 09:21 ET |
| GO | Grocery Outlet Holding Corp. | 12.92 | -7.85% | 12,133 | 0.5% | $1.39B | Retail Trade | 09:21 ET |
| CYPH | Cypherpunk Technologies Inc. | 1.9914 | -6.51% | 652,078 | 4.7% | $226.8M | Finance | 09:21 ET |

### Thin tape - passes Gate A, fails the $100m quality floor

**21 gainers and 22 decliners qualify**, published in full - a truncated block with an unstated truncation reads as a complete one. Real prints on thin books: these never top a headline table, and every one of them fails Gate B on the reconciled cap.

| Ticker | Name | % | Pre-market | Mkt cap | Pm vol | Sector |
|---|---|---|---|---|---|---|
| SHFS | SHF Holdings, Inc. | +145.28% | 0.039 | $2.1M | 1,382,398,536 | Finance |
| OMH | Ohmyhome Limited | +59.09% | 26.4324 | $35.1M | 1,532,505 | Finance |
| INLF | INLIF LIMITED | +50.37% | 0.8195 | $831,287 | 107,305,123 | Producer Manufacturing |
| YMAT | J-Star Holding Co., Ltd. | +31.00% | 1.31 | $4.5M | 12,757,760 | Producer Manufacturing |
| HUHU | HUHUTECH International Group Inc. | +29.37% | 0.5149 | $10.7M | 49,994,351 | Technology Services |
| AUUD | Auddia Inc. | +28.98% | 0.3098 | $1.4M | 95,793,882 | Technology Services |
| BURU | Nuburu, Inc. | +21.90% | 0.2457 | $2.8M | 14,284,965 | Electronic Technology |
| RCT | RedCloud Holdings plc | +18.89% | 0.0365 | $2.3M | 335,621,277 | Technology Services |
| UCL | uCloudlink Group Inc. | +16.64% | 0.2205 | $7.2M | 17,780,704 | Technology Services |
| CANG | Cango Inc. | +15.79% | 1.32 | $46.8M | 188,791 | Technology Services |
| BDAI | Biddance AI Systems, Inc. | +14.29% | 2 | $15.7M | 612,143 | Technology Services |
| BDMD | Baird Medical Investment Holdings Ltd | +11.24% | 0.1079 | $3.1M | 61,430,152 | Health Technology |
| MI | NFT Limited | +9.91% | 0.4468 | $36.5M | 25,530,407 | Technology Services |
| TPST | Tempest Therapeutics, Inc. | +7.91% | 0.4038 | $7.5M | 178,464 | Health Technology |
| WETO | Wetour Robotics Limited | +7.30% | 0.6438 | $646,681 | 115,990 | Transportation |
| MVST | Microvast Holdings, Inc. | +6.72% | 0.235 | $84.8M | 949,160 | Producer Manufacturing |
| BKYI | BIO-key International, Inc. | +5.51% | 2.49 | $4.8M | 234,174 | Technology Services |
| OBAI | Our Bond, Inc. | +5.00% | 1.68 | $2.6M | 163,320 | Technology Services |
| NNOX | NANO-X IMAGING LTD | +4.93% | 0.3917 | $29.4M | 1,307,806 | Health Technology |
| DVLT | Datavault AI Inc. | +3.92% | 0.0609 | $60.3M | 3,983,427 | Electronic Technology |
| GPUS | Hyperscale Data, Inc. | +3.52% | 0.1939 | $43.4M | 2,450,578 | Producer Manufacturing |
| STAK | STAK Inc. | -49.75% | 2.47 | $51.9M | 2,167,943 | Industrial Services |
| BMGL | Basel Medical Group Ltd | -43.02% | 1.0998 | $10.7M | 594,769 | Health Services |
| NXXT | NextNRG, Inc. | -28.04% | 0.1342 | $314,066 | 1,035,187 | Technology Services |
| INVZ | Innoviz Technologies Ltd. | -19.14% | 0.1783 | $48.4M | 2,419,303 | Producer Manufacturing |
| PARA | Parabolic Technologies, Inc. | -16.03% | 0.0655 | $51,163 | 8,989,437 | Technology Services |
| VIVK | Vivakor, Inc. | -14.88% | 0.2494 | $470,849 | 1,273,397 | Process Industries |
| RUBI | Rubico Inc. | -13.95% | 1.11 | $697,495 | 252,639 | Transportation |
| CHSN | Chanson International Holding | -12.77% | 2.05 | $5.5M | 16,713,226 | Consumer Non-Durables |
| DBGI | Digital Brands Group, Inc. | -11.55% | 0.1371 | $144,694 | 845,781 | Consumer Non-Durables |
| CDT | CDT Equity Inc. | -10.76% | 0.5009 | $571,327 | 157,500 | Health Technology |
| HUBC | Hub Cyber Security Ltd. | -10.66% | 0.0679 | $136,482 | 21,829,371 | Commercial Services |
| YFOR | YYForce Inc. | -10.35% | 0.0511 | $731,694 | 21,975,178 | Commercial Services |
| WKSP | Worksport, Ltd. | -10.34% | 0.2609 | $5.8M | 247,878 | Producer Manufacturing |
| ARAI | Arrive AI Inc. | -10.34% | 0.0477 | $2.9M | 39,309,255 | Technology Services |
| SMX | SMX (Security Matters) Public Limited Company | -9.87% | 17.35 | $17.3M | 251,421 | Technology Services |
| AMIX | Autonomix Medical, Inc. | -8.07% | 1.7007 | $3.6M | 254,564 | Health Technology |
| JDZG | JIADE LIMITED | -5.96% | 0.1987 | $1.1M | 416,725 | Commercial Services |
| RBNE | Robin Energy Ltd. | -5.36% | 0.1218 | $6.2M | 3,403,576 | Transportation |
| NCT | Intercont (Cayman) Limited | -4.23% | 0.3916 | $7.4M | 298,034 | Transportation |
| NTCL | NETCLASS TECHNOLOGY INC | -3.82% | 0.2241 | $493,963 | 147,738 | Technology Services |
| IHRT | iHeartMedia, Inc. | -3.65% | 0.5964 | $95.5M | 205,686 | Consumer Services |
| FTCI | FTC Solar, Inc. | -3.23% | 1.5 | $28.3M | 112,197 | Technology Services |

## 2. Gap quality - can this gap hold?

One row per headline name, all from the SAME pull. **PM range** = premarket_low - premarket_high. **Hold %** = (premarket_close - premarket_low) / (premarket_high - premarket_low) x 100; 100 = the last print is AT the top of its range (the gap is holding), 0 = it is at the bottom (the gap is gone). **pm %ADV** = premarket_volume / average_volume_30d_calc x 100. **Print** = the auction flag (`AUCTION` 2-30, `QUOTE` under 2, `CHURN` over 30) joined with the holding flag (`holding` 80 or more, `half-filled` under 50) - two descriptors of how the gap was made, NOT filters and NOT a ranking. **Driver** is the fixed vocabulary applied to the catalyst the 08:30 brief already sourced; `+ANCHORED` means the catalyst carries a hard number (a price, a per-share amount, a settlement figure, a balance-sheet total).

| Ticker | Name | Gap % | PM range | Hold % | pm %ADV | Print | Driver | Key level | Invalidation |
|---|---|---|---|---|---|---|---|---|---|
| FOSL | Fossil Group, Inc. | +24.90% | 9.31-10.09 | 67% | 16.8% | AUCTION+mid | EARNINGS-RAISE+ANCHORED | 7.87 | back to/below prior close 7.87 |
| RSKD | Riskified Ltd. | +23.11% | 8.65-10.77 | 84% | 19.8% | AUCTION+holding | NONE | 8.48 | back to/below prior close 8.48 |
| GEVO | Gevo, Inc. | +21.47% | 1.5962-1.7 | 89% | 17.2% | AUCTION+holding | EARNINGS-RECONFIRM+ANCHORED | 1.39 | back to/below prior close 1.39 |
| SATL | Satellogic Inc. | +17.95% | 4.46-4.77 | 45% | 15.8% | AUCTION+half-filled | EARNINGS-RECONFIRM+ANCHORED | 3.90 | back to/below prior close 3.90 |
| CRWV | CoreWeave, Inc. | +13.54% | 53.5-57.82 | 42% | 16.7% | AUCTION+half-filled | EARNINGS-RAISE+ANCHORED | 48.73 | back to/below prior close 48.73 |
| SHAZ | SharonAI Holdings, Inc. | +13.12% | 24.3-27.1 | 74% | 1.6% | QUOTE+mid | NONE | 23.32 | back to/below prior close 23.32 |
| BRUN | Boost Run Inc. | +12.99% | 6.81-7.29 | 85% | 0.9% | QUOTE+holding | NONE | 6.39 | back to/below prior close 6.39 |
| CECO | CECO Environmental Corp. | +12.08% | 52.06-58.09 | 100% | 2.8% | AUCTION+holding | NONE | 51.83 | back to/below prior close 51.83 |
| HYLN | Hyliion Holdings Corp. | +12.04% | 3.16-3.4 | 79% | 4.7% | AUCTION+mid | NONE | 2.99 | back to/below prior close 2.99 |
| BRAI | Braiin Limited | +11.80% | 1.82-2 | 94% | 2.6% | AUCTION+holding | NONE | 1.78 | back to/below prior close 1.78 |
| NBIS | Nebius Group N.V. | +11.15% | 146.88-154.44 | 27% | 10.5% | AUCTION+half-filled | EARNINGS-RAISE+ANCHORED | 134.00 | back to/below prior close 134.00 |
| FORM | FormFactor, Inc. | +10.44% | 91-95 | 89% | 0.5% | QUOTE+holding | SECTOR-BETA | 85.63 | back to/below prior close 85.63 |
| BGS | B&G Foods, Inc. | +10.15% | 2.82-2.96 | 79% | 2.5% | AUCTION+mid | NONE | 2.66 | back to/below prior close 2.66 |
| AXTI | AXT Inc | +9.95% | 42.1-43.36 | 89% | 3.6% | AUCTION+holding | SECTOR-BETA | 39.31 | back to/below prior close 39.31 |
| NUAI | New Era Energy & Digital, Inc. | +9.66% | 2.18-2.27 | 100% | 2.6% | AUCTION+holding | NONE | 2.07 | back to/below prior close 2.07 |
| SUJA | Suja Life, Inc. | -20.76% | 7.9-9.13 | 0% | 15.2% | AUCTION+half-filled | NONE | 9.97 | below PM low 7.9 |
| STIM | Neuronetics, Inc. | -16.42% | 1.65-1.99 | 9% | 20.4% | AUCTION+half-filled | NONE | 2.01 | below PM low 1.65 |
| BV | BrightView Holdings, Inc. | -12.86% | 9.35-10.24 | 69% | 3.3% | AUCTION+mid | NONE | 11.43 | below PM low 9.35 |
| LWLG | Lightwave Logic, Inc. | -12.59% | 3.17-3.86 | 97% | 12.8% | AUCTION+holding | EARNINGS-CUT+ANCHORED | 4.39 | below PM low 3.17 |
| VELO | Velo3D, Inc. | -11.26% | 5.21-5.8 | 25% | 7.9% | AUCTION+half-filled | NONE | 6.04 | below PM low 5.21 |
| GPRO | GoPro, Inc. | -11.02% | 0.7449-0.78 | 14% | 6.7% | AUCTION+half-filled | CORPORATE-EVENT | 0.8428 | below PM low 0.7449 |
| HGTY | Hagerty, Inc. | -8.50% | 15.14-16.4 | 29% | 147.8% | CHURN+half-filled | NONE | 16.94 | below PM low 15.14 |
| SPIR | Spire Global, Inc. | -8.13% | 8.08-8.95 | 59% | 3.5% | AUCTION+mid | unclassified | 9.35 | below PM low 8.08 |
| GO | Grocery Outlet Holding Corp. | -7.85% | 12.857-13.68 | 8% | 0.5% | QUOTE+half-filled | NONE | 14.02 | below PM low 12.857 |
| CYPH | Cypherpunk Technologies Inc. | -6.51% | 1.93-2.03 | 61% | 4.7% | AUCTION+mid | NONE | 2.13 | below PM low 1.93 |

## 3. What changed since the morning brief

Read against the 08:30 brief's own CSV (`daily-briefs/2026-11-11-pre-market.csv`): **381** of **684** compared names moved their gap by more than 0.2pp since the 08:37:40 ET pull. Sorted by the size of the CHANGE, not by the size of the gap. 194 faded and 187 extended.

| Ticker | Name | Gap at 09:21 | Gap at 08:37 | Change | In tables |
|---|---|---|---|---|---|
| CHSN | Chanson International Holding | -12.77% | +47.87% | -60.64pp | thin tape |
| DPU | Nexpu Ltd. | +14.50% | -3.05% | +17.55pp | not published |
| OMH | Ohmyhome Limited | +59.09% | +75.65% | -16.56pp | thin tape |
| SHFS | SHF Holdings, Inc. | +145.28% | +128.93% | +16.35pp | thin tape |
| TLSI | TriSalus Life Sciences, Inc. | -3.86% | -19.30% | +15.44pp | not published |
| HUHU | HUHUTECH International Group Inc. | +29.37% | +43.28% | -13.91pp | thin tape |
| IMNN | Imunon, Inc. | +3.00% | +14.55% | -11.55pp | not published |
| AUUD | Auddia Inc. | +28.98% | +40.09% | -11.11pp | thin tape |
| UPC | Universe Pharmaceuticals Inc | +6.45% | -4.52% | +10.97pp | not published |
| ALGS | Aligos Therapeutics, Inc. | +4.28% | +14.79% | -10.51pp | not published |
| SPAI | Safe Pro Group Inc. | +3.07% | +10.92% | -7.85pp | not published |
| DOMH | Dominari Holdings Inc. | +12.49% | +5.74% | +6.75pp | not published |
| RCT | RedCloud Holdings plc | +18.89% | +25.41% | -6.52pp | thin tape |
| MSS | Maison Solutions Inc. | +6.45% | +12.90% | -6.45pp | not published |
| PLUR | Pluri Inc. | +9.82% | +3.57% | +6.25pp | not published |

Biggest movers among the *published* names: **BRAI** +6.18pp, **STIM** -5.82pp, **VELO** -4.97pp, **LWLG** +3.36pp, **RSKD** +3.30pp.

## 4. Verdict

**More directional than at 08:30 ET, and skewed to the upside** - but the conviction behind it did not improve. The band grew from 610 gainers and 165 decliners to **638** and **169**, with **123** names new to the band and **91** morning names out of it, and NQ futures at 28,362 (+1.89%) and ES at 7,615.25 (+0.94%) at 09:14 ET. What did not improve is gap quality: on the 581 common names with a computable pre-market range in both pulls, mean Hold went 64.3% -> 62.6%, median 75% -> 68%, the number holding their range (80% or more) fell 249 -> 216 and the number half-filled (under 50%) rose 169 -> 185. The moves themselves are near-symmetric - 194 fades against 187 extends - and only ONE name moved 20pp or more in either direction: **CHSN**, a $5.5M thin-tape shell that went from +47.87% to -12.77% (-60.64pp) in forty-five minutes, with zero names extending 20pp. That is churn, not a narrowing into a trend. **FOSL** is the setup because it is the only headline name that is both anchored and in one of the five eligible classes and still extending (+23.89% at 08:37 -> +24.90% at 09:21); **NVDA**, the $4.07T anchor of the bid, went the other way (+3.86% -> +3.04%, Hold 24%).

## 5. Source health

| Source | Query | Status | Notes |
|---|---|---|---|
| TradingView america scanner | POST https://scanner.tradingview.com/america/scan (gainers, losers; range [0,1000]) | ok | 638 gainers + 169 decliners; `len(rows) == totalCount` asserted on BOTH; the close-vs-gap reconciliation sweep flagged 0 of 807 rows |
| Scanner pre-market columns | premarket_high / premarket_low | ok | non-null on all 807 rows - the PM range, the Hold % and the `half-filled` flag are computed, not omitted |
| Market-cap reconciliation | Nasdaq `/summary` + shibui `valuation` (latest row on or before 2026-11-10) | ok | 63 candidate names swept against three sources; 30 disagreed by more than 15% and are published as the median of the available sources; **no name changed Gate B** on the reconciled cap |
| Market-cap source gaps | scanner `market_cap_basic` | fixed | two screen rows carry no scanner cap. **TREO** is reconciled to $37.0M from Nasdaq ($39.3M) and shibui ($35.3M). **ECC/PD** - a $17.50 preferred with 100 pre-market shares - has a cap in NO source, so it is published with an EMPTY cap and never a 0; it fails Gate A, so it appears in no table |
| MCP-over-HTTP bridge - market-recap | `get_quotes` (15 headline screen names plus NVDA, plus ^TNX / NQ=F / ES=F / GC=F) | ok | every quote carries its own `as_of`; the screen quotes are the 2026-11-10 regular-session closes and reconcile with the scanner's own prior close on every one of them |
| Morning brief 08:30 ET | `daily-briefs/2026-11-11-pre-market.md` + `.csv` | ok | 794 rows, `screen_complete: true` - its published band counts (610 gainers / 165 decliners) match its own front matter; read for the Driver column and for the 08:37 baseline |

**`live_*` in the companion CSV are deliberately BLANK, not zero.** The pull landed at 09:21 ET, before the 09:30 open, so there is no live regular-session price, change or volume to publish - and a settled prior-session close wearing a `live_` label is a stale value presented as a live one. The last completed session's numbers are already carried under `prior_session_change_pct`, and `prior_close` is derived.

**`prior_close` is derived, never the scanner's `close` column.** Every row's prior close is `premarket_close / (1 + premarket_change / 100)`, computed from the values THAT ROW PUBLISHES, so every row reproduces its own prior close and a reader can check it.

**The derived prior close carries a rounding step, and it is disclosed rather than hidden.** The published gap is rounded to 2 dp, so a row whose price and gap do not divide exactly back to the close lands a fraction of a cent away: 19 of the 807 rows differ from the scanner's own close by more than a cent (the largest is 4.1c, on FIX), and the largest effect among the 25 headline names is **NVDA** - published at 168.8952 against the 168.89 prior close that the bridge, Nasdaq and the scanner's own close column all agree on; the 08:30 brief published the same close as 168.89. The CSV's `prior_close` is the derived value on every row, so every row reproduces its own close.

**The Driver vocabulary, applied to the catalyst the 08:30 brief already sourced.** 6 of the 25 headline names carry an anchored catalyst and 3 of those sit in the five classes the setup ladder accepts: FOSL (EARNINGS-RAISE+ANCHORED), CRWV (EARNINGS-RAISE+ANCHORED), NBIS (EARNINGS-RAISE+ANCHORED). The rest are classified from the morning CSV's own `has_news` and `setup_theme` columns: `has_news = no` is `NONE` whatever the cluster, and the two cluster-level reads are **NBIS** - whose gap is CoreWeave's print, not its own, and which reports on Nov 12 - and **FORM**/**AXTI**, whose C2 catalyst is Bernstein's co-packaged-optics call, a sector theme with price targets on other names, so `SECTOR-BETA` without an anchor. **GPRO** is `CORPORATE-EVENT`: its Q3 release was delayed over accounting and valuation work, so there is no reported result to classify. **SPIR** is `unclassified`: the brief says only that it fell on its results, gives no direction and no figure, and the name is not in the brief's earnings table - a miss is not inferred from a price move. **LWLG** is `EARNINGS-CUT+ANCHORED` on its own $38,000 of Q3 revenue and a $7.2m net loss. Anchors are the catalyst's own hard numbers, not a growth rate: GEVO's $83m revenue and $23m net income, of which about $29.4m came from Canadian clean-fuel credits.

Companion file: `daily-briefs/2026-11-11-pre-market-refresh.csv` (807 rows, one per name seen in the pre-market screens; the pinned 16-column date-independent header).
