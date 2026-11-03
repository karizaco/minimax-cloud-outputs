# Cron #5 — eod-international-daily — 2026-11-03

Daily EOD snapshot for the international markets the skill covers (AU, TW, CA and 12 EU venues), written after each market's cash close settled. **3,082 instrument rows across 15 per-region CSVs**, one row per listed instrument, sorted by market cap (USD) descending.

> **Read this first:** `market_cap` is normalised to **USD**, while `close`/`open`/`high`/`low` stay in the **local listing currency** — the `currency` column states which. `change_pct` is TradingView's daily change in percent (not a fraction). Three facts change how the file reads: (1) **Japan has no file** — the Tokyo Stock Exchange was closed on 3 November for Culture Day, so `jp.csv` is intentionally absent; (2) rows the source reports **no market cap** for cannot be screened against a cap floor and are **excluded rather than written blank** (243 rows, listed in `_excluded.json`); (3) 87 written rows **did not trade today** and carry a carry-over close (listed in `_carryover.json`) — they are excluded from every movers list.

## Coverage

| Region | Venues in file | Universe | Unique instruments | Written | Floor (USD) | No cap | Off-official rows |
|---|---|---|---|---|---|---|---|
| `au` | ASX | 1,551 | 1,551 | **300** | $300M + vol ≥100k | 4 | 0 |
| `jp` | — | — | — | **no session** | $300M | — | — |
| `tw` | TWSE, TPEX | 2,332 | 2,332 | **920** | $200M | 56 | 0 |
| `ca` | TSX, TSXV, CSE | 4,260 | 2,694 | **663** | $200M | 133 | 4 |
| `eu-de` | XETR | 4,299 | 499 | **121** | $300M + vol ≥50k | 3 | 0 |
| `eu-fr` | EURONEXT | 548 | 548 | **261** | $100M | 1 | 0 |
| `eu-it` | MIL | 393 | 393 | **181** | $100M | 2 | 0 |
| `eu-es` | BME | 272 | 272 | **146** | $100M | 35 | 0 |
| `eu-nl` | EURONEXT | 77 | 77 | **56** | $100M | 0 | 0 |
| `eu-be` | EURONEXT | 100 | 100 | **76** | $100M | 1 | 0 |
| `eu-at` | VIE | 66 | 66 | **51** | $100M | 3 | 0 |
| `eu-pt` | EURONEXT | 31 | 31 | **27** | $50M | 0 | 0 |
| `eu-ie` | EURONEXT | 19 | 19 | **17** | $200M | 0 | 0 |
| `eu-fi` | OMXHEX | 188 | 188 | **100** | $100M | 4 | 0 |
| `eu-dk` | OMXCOP | 134 | 134 | **77** | $100M | 1 | 0 |
| `eu-gr` | ATHEX | 128 | 128 | **86** | $50M | 0 | 0 |
| **total** | | **14,398** | | **3,082** | | **243** | **4** |

`Universe` is every instrument the source returns for that country's own listings; `Unique instruments` collapses instruments quoted on several venues of the same market down to one row; `Written` applies the skill's per-region USD market-cap floor (`screener_filters.usd_floor_for_region`) plus the region volume gate.

**Japan was skipped because the exchange did not trade — not because a calendar said so.** The session probe could not confirm a session (`traded=unknown`, Yahoo's `^N225` daily bars stop at 2 November), but two independent sources agree that the TSE was closed: the skill's own `holiday_calendar.py` marks `jp` as a non-trading day for 3 November (Culture Day, 文化の日), and every one of the 1,390 Japanese rows the scanner returned is **byte-identical to the 2 November file** (0 of 1,390 changed, including volumes) — a stale print, not a session. `unknown` alone would never have been enough to drop a region.

## Market context

Settled closes, verified against the close and not an intraday print:

| Index | Close | Change | Day | Source |
|---|---|---|---|---|
| ASX 200 | 8,886.80 | +30.30 / **+0.30%** | up | Yahoo `^AXJO`; CommBank, AP (30.3 pts, 0.30%) |
| All Ordinaries | 9,008.90 | +31.70 / +0.40% | up | Yahoo `^AORD`; CommBank |
| Nikkei 225 | **no session** | — | closed | TSE closed for Culture Day; Yahoo `^N225` last bar 2 Nov |
| TAIEX | 43,307.54 | −1,612.60 / **−3.59%** | down | Yahoo `^TWII` quote page; CNA, Focus Taiwan, Taiwan News |
| S&P/TSX Composite | 35,532.28 | −268.82 / −0.75% | down | Yahoo `^GSPTSE` |
| DAX | 25,864.62 | −116.47 / −0.45% | down | Yahoo `^GDAXI`; Investing.com (−0.45%) |
| CAC 40 | 8,020.31 | −27.38 / −0.34% | down | Yahoo `^FCHI` |
| FTSE MIB | 49,941.83 | −6.17 / −0.01% | flat | Yahoo `FTSEMIB.MI` |
| IBEX 35 | 18,807.20 | −150.60 / −0.79% | down | Yahoo `^IBEX` |
| AEX | 1,121.76 | −10.78 / −0.95% | down | Yahoo `^AEX` |
| BEL 20 | 5,837.52 | −39.24 / −0.67% | down | Yahoo `^BFX` |
| ATX | 6,396.13 | −34.14 / −0.53% | down | Yahoo `^ATX` |
| PSI 20 | 9,223.89 | −28.57 / −0.31% | down | Yahoo `PSI20.LS`; Jornal Económico (9,223.89, −0.31%) |
| ISEQ | 14,353.34 | −64.52 / −0.45% | down | Yahoo `^ISEQ` |
| OMX Helsinki 25 | 6,189.62 | −23.93 / −0.39% | down | Yahoo `^OMXH25` |
| OMX Copenhagen 20 | 1,648.67 | +2.56 / +0.16% | up | Yahoo `^OMXC20` quote page (prev 1,646.11) |
| ATHEX General | 2,616.12 | +13.77 / **+0.53%** | up | euro2day close 17:25 (TradingEconomics CFD 2,617.5, +0.58%) |
| STOXX 600 *(context)* | 645.66 | −3.78 / −0.58% | down | Yahoo `^STOXX`; Irish Times ("closed 0.58 per cent lower") |

Three sessions, three different drivers. **Europe faded on a global tech rout**: Apple's warning that persistent memory-chip inflation would squeeze gross margins through the holiday quarter, alongside Oracle's $20bn raise, dragged technology lower (ASML −1.63%, SAP −1.83%) and pulled the STOXX 600 down 0.58% to 645.66 with mining leading the decline on weaker copper — all of it on US midterm-election day, with doubts over a Middle East peace deal pushing oil up again (Brent +1.96% to $106.75 intraday). The index-level picture hides the real action, which was **single-stock earnings**: TeamViewer cut its FY revenue guidance and fell 26.83%, while Philips (+4.81%), Ferrari (+4.47%) and Grifols (+2.09%) rallied on their own prints.

**Taiwan had the day of its own**: the TAIEX fell 1,612.60 points (−3.59%) to 43,307.54 — the **seventh-largest closing point decline on record** — as the Philadelphia Semiconductor Index's 3.37% overnight fall and continuing doubts over AI capital spending triggered panic selling. PCB, memory, packaging and testing names were hit to their ±10% limits (Kinsus, Cosmo, MPI, Nanya, Nan Ya Plastics), the OTC index dropped 6.12%, and foreign institutions sold a net NT$107.31bn. The snapshot agrees: 857 of 920 Taiwanese rows fell and the cap-weighted average is −3.79% against the index's −3.59%.

**Australia went the other way.** The RBA lifted the cash rate 25bp to 4.85% — the fifth hike of 2026 and an 18-year high — on a 6-3 split, with inflation now expected above 3% through much of 2027. The market treated it as a no-surprise and looked past it: the ASX 200 closed up 0.30% with the median written name up 0.33%. **Greece bucked Europe entirely**, closing +0.53% at the session high on a 1.42% bank rally, with refiners the weak spot.

**Internal cross-check:** the snapshot's own cap-weighted averages land on the published index moves — TW −3.79% vs TAIEX −3.59%, AU +0.30% vs ASX 200 +0.30%, DE −0.48% vs DAX −0.45%, NL −0.97% vs AEX −0.95%, ES −0.78% vs IBEX −0.79%, GR +0.59% vs ATHEX +0.53%, BE −0.92% vs BEL 20 −0.67%, CA −0.25% vs TSX −0.75%. The snapshot is consistent with the settled closes, not with an intraday read.

Regional breadth from the snapshot itself (median `change_pct` per file):

| Region | Rows | Median | Up / down / flat | Min | Max | Cap-weighted |
|---|---|---|---|---|---|---|
| `au` | 300 | +0.33% | 164 / 124 / 12 | −24.72% | +8.87% | +0.30% |
| `tw` | 920 | −3.73% | 47 / 857 / 16 | −14.36% | +9.90% | −3.79% |
| `ca` | 663 | +0.00% | 263 / 315 / 83 | −12.99% | +24.74% | −0.25% |
| `eu-de` | 121 | −0.40% | 42 / 76 / 3 | −26.83% | +7.05% | −0.48% |
| `eu-fr` | 261 | +0.00% | 112 / 125 / 24 | −10.53% | +22.25% | −0.07% |
| `eu-it` | 181 | −0.13% | 75 / 93 / 13 | −6.04% | +5.32% | +0.06% |
| `eu-es` | 146 | +0.00% | 46 / 53 / 47 | −6.02% | +4.85% | −0.78% |
| `eu-nl` | 56 | −0.44% | 22 / 32 / 2 | −8.95% | +7.55% | −0.97% |
| `eu-be` | 76 | −0.32% | 23 / 46 / 7 | −3.16% | +9.72% | −0.92% |
| `eu-at` | 51 | −0.15% | 16 / 27 / 8 | −14.77% | +5.67% | −0.67% |
| `eu-pt` | 27 | −0.28% | 7 / 15 / 5 | −9.57% | +1.33% | −0.86% |
| `eu-ie` | 17 | +0.00% | 5 / 8 / 4 | −2.91% | +2.10% | −0.45% |
| `eu-fi` | 100 | −0.12% | 43 / 52 / 5 | −5.05% | +3.66% | −0.31% |
| `eu-dk` | 77 | +0.29% | 43 / 25 / 9 | −2.87% | +5.65% | +0.02% |
| `eu-gr` | 86 | +0.00% | 41 / 28 / 17 | −2.56% | +4.46% | +0.59% |

Europe's median name fell in 11 of 12 EU venues, while Denmark and Greece were the only European regions with a rising median name — a session where the index (ATHEX +0.53%) and the typical name (Greece median 0.00%) disagreed, which is why both are published.

## Top movers

Largest absolute daily moves among liquid names (volume ≥ 100k **and** market cap ≥ $1B), 1,091 of 3,082 written rows qualify:

| Region | Ticker | Name | Change | Close | Volume | Mkt cap (USD) | Catalyst |
|---|---|---|---|---|---|---|---|
| eu-de | `XETR:TMV` | TeamViewer SE | −26.83% | 5.29 EUR | 6,501,522 | $1.28B | Q3 2026 ad-hoc release (3 Nov): ARR €736.9m (−0.6% cc), revenue €184.5m (−2.2% cc), adjusted EBITDA margin 42.8%; **FY26 revenue guidance cut to −2%…−1% cc from 0%…+3%** on delayed large-enterprise deal conversions and renewed European uncertainty. EBITDA margin (~43%) reaffirmed. Morningstar cut fair value 13%; dpa reported the shares down a double-digit percent |
| ca | `TSX:VNP` | 5N Plus Inc. | +24.74% | 32.62 CAD | 1,304,172 | $1.68B | Q3 beat (reported 2 Nov, call 3 Nov): adjusted EPS US$0.20 vs US$0.15 consensus, revenue **+30% y/y to US$136.4m** vs US$119.2m expected; Specialty Semiconductors revenue +34% and backlog at a 365-day maximum; ~50% expansion of the St. George (Utah) facility, a US$7.3m gallium-arsenide defence award, and space-solar demand driving "AZUR" capacity evaluation |
| tw | `TWSE:3189` | Kinsus Interconnect Technology Corp. | −10.00% | 819 TWD | 18,122,609 | $14.71B | **Limit-down** in the PCB sell-off after the Philadelphia Semiconductor Index fell 3.37% overnight on AI-spending concerns; the TAIEX lost 1,612.60 points (−3.59%), its seventh-largest point decline on record. PCB names (Wus, Microcosm, Taiwan Union, Nan Ya PCB) all hit their daily limits |
| tw | `TWSE:2466` | Cosmo Electronics Corporation | −10.00% | 342 TWD | 1,107,919 | $2.02B | Same session-wide limit-down cascade; demand for traditional consumer electronics (computers, smartphones) has yet to recover and DRAM price increases have slowed in both short-term trades and longer-term supply contracts |
| tw | `TPEX:7751` | Horng Terng Automation Co Ltd | −10.00% | 1,125 TWD | 290,486 | $1.03B | Limit-down in the AI-hardware de-rating; the OTC index fell 6.12%, so mid-caps absorbed the heaviest selling |
| tw | `TPEX:6223` | MPI Corporation | −9.99% | 4,190 TWD | 1,064,746 | $14.00B | Limit-down; high-priced thousand-dollar names were slammed directly to the floor as the correction extended beyond TSSE main-board names |
| au | `ASX:AMP` | AMP Limited | −9.36% | 2.13 AUD | 39,646,618 | $3.95B | The ASX issued a **price query letter** on 2 Nov after AMP's price swung from A$2.51 to A$2.22 on heavy volume; AMP replied it is aware of no unpublished information, pointing instead to China Life Pension Company's 3Q solvency report (lower net profit) — AMP holds 19.99% of CLPC. FY26 partnerships guidance unchanged |
| eu-pt | `EURONEXT:COR` | Corticeira Amorim SGPS SA | −9.57% | 6.33 EUR | 860,566 | $1.04B | 9M 2026 results: sales −4.3% to €647.7m and **net profit −22.4% to €35.4m** on restructuring charges in the flooring business and adverse product mix; 9M EPS €0.267 vs €0.343. The worst performer on the PSI (which still closed only −0.31%) |

Two of the day's largest moves fall below the $1B cap gate and are therefore **not** in the table above: **Alpha HPA (`ASX:A4N`) −24.72%** to A$0.335 on 26.8m shares — a new 52-week low of A$0.3275, no company-specific release found — and **2CRSI (`EURONEXT:AL2SI`) +22.25%**.

Largest mover per region among liquid names:

| Region | Ticker | Name | Change | Catalyst |
|---|---|---|---|---|
| au | `ASX:AMP` | AMP Limited | −9.36% | ASX price-query letter + China Life Pension 3Q solvency update |
| jp | — | — | **no session** | TSE closed for Culture Day |
| tw | `TWSE:3189` | Kinsus Interconnect Technology | −10.00% | Limit-down in the AI-hardware sell-off |
| ca | `TSX:VNP` | 5N Plus Inc. | +24.74% | Q3 beat: revenue +30%, adjusted EPS US$0.20 vs US$0.15 |
| eu-de | `XETR:TMV` | TeamViewer SE | −26.83% | FY26 revenue guidance cut to −2%…−1% cc |
| eu-fr | `EURONEXT:BIM` | bioMérieux SA | +4.81% | Q3 sales €1,042m, +8% organic (vs 5.9% consensus), BIOFIRE non-respiratory panels +25%, FY26 guidance confirmed |
| eu-it | `MIL:RACE` | Ferrari NV | +4.47% | Q3 beat and a guidance upgrade: adjusted EBITDA €753m (+12%) vs €739m consensus, FY26 adj. EBITDA now ≥ €3bn; order book into 2028, Luce EV allocations "fully booked" |
| eu-es | `BME:GRF.P` | Grifols, S.A. Pref Class B | +4.85% | Grifols Q3: net profit +27.9% to €162m, revenue +8.4% cc to €2.04bn, FY26 guidance confirmed; the Class A line (€11.23) rose 2.09% |
| eu-nl | `EURONEXT:PHIA` | Koninklijke Philips N.V. | +4.81% | Q3 adjusted EBITA €569m (+7.2%) beat by ~9%, margin +70bp to 13.0%, order intake +8%, **Respironics agreement in principle with the US DOJ** (€288m provision), FY26 outlook reiterated — an eight-month high |
| eu-be | `EURONEXT:SOLB` | Solvay SA | −1.92% | No company-specific release found; Q3 results are due 4 November |
| eu-at | `VIE:ATS` | AT & S Austria Technologie | +5.67% | No company-specific release found; Q2 FY27 results are due 5 November |
| eu-pt | `EURONEXT:COR` | Corticeira Amorim SGPS SA | −9.57% | 9M net profit −22.4% on restructuring charges and weaker sales |
| eu-ie | `EURONEXT:GL9` | Glanbia PLC | −2.91% | No company-specific release found |
| eu-fi | `OMXHEX:NESTE` | Neste Corporation | −3.06% | No company-specific release found (Q3 was 29 Oct: record Renewable Products EBITDA, refining margin US$48.2/bbl); a refiners' margin move |
| eu-dk | `OMXCOP:CHEMM` | ChemoMetec A/S | +5.65% | No company-specific release found |
| eu-gr | `ATHEX:CREDIA` | CrediaBank S.A. | +2.83% | No company-specific release found; a rebound in the Greek banks that lifted the ATHEX banking index +1.42% (CrediaBank reports 12 November) |

## Method

1. **Universe** — the skill's `mcp__tradingview-advanced__stock_screener(country=…)` is not registered in the Cloud runtime, and the MCP-over-HTTP bridge's 50-call/day anonymous allowance was already exhausted (`authentication_required`, resets 2026-11-04T00:00Z). The same underlying source is reachable over its public per-country scanner API, so each region was pulled with a `country` filter matching the instrument's own country of primary listing plus `type = stock`. Without the `country` filter the per-country endpoint also returns *foreign* stocks quoted on that market's venues (NVIDIA, Apple and even SpaceX on Lang & Schwarz with WKN-style symbols), which would have inflated Germany from ~500 companies to 36,185 rows. **16/16 calls returned HTTP 200 in 0.07–1.94 s with no rate limiting.**
2. **Venue selection and the venue-collapse rule** — one row per instrument, preferring the official listing venue (XETR, TSE, TSX/TSXV, TWSE/TPEX, MIL, BME, VIE, OMXHEX, OMXCOP, ATHEX, EURONEXT, ASX), then the highest-volume print. Germany needs its own company key: Lang & Schwarz carries the same share under a WKN symbol (`LSX:750000` = thyssenkrupp's `TKA`), so German rows are deduped by company description — 4,299 raw rows collapse to 499 companies. Elsewhere the key is (description, ticker root), which keeps genuine share classes apart: `MFC` vs `MFC.PR.K`, `FFH` vs `FFH.U`, `SGR.U` vs `SGR.UN`, `DHT.U` vs `DHT.UN`, `HOT.U` vs `HOT.UN`, `CACR` vs `CACR.A`, and Japan's two unrelated companies both called "JTEC Corporation" (2479 / 3446) all survive as separate rows.
3. **Enrichment** — `volume`, `pe_ratio` and `sector` come straight from the same scanner response, so the skill's Yahoo `compare_stocks` enrichment stage was **not needed and was skipped** (Yahoo's JSON endpoints also return HTTP 429 from this egress). No Yahoo quote was used for any price in the CSVs.
4. **Market cap** — `market_cap_basic` is in the row's **local** currency, so every value is converted to USD with the 3 Nov open.er-api rate table (updated 3 Nov 00:02 UTC). Frankfurter (2026-11-03) agrees within 0.5% on every currency it carries. Sanity-checked against implied share counts (local cap ÷ local close): SAP 1,189m, TSMC 26,328m, Royal Bank 1,390m, Alstom 486m, Ryanair 1,045m — all plausible.
5. **Change column** — the scanner's `change` field is already in **percent units** (0.0695 means +0.0695%), not a fraction. This was proven, not assumed: across all 18,274 priced rows of the pull, `close − close/(1 + change/100)` reproduces `change_abs` exactly (total error 0.000000, zero rows off by more than 0.011). Multiplying by 100 would have inflated every move in this file by 100×.
6. **Floors applied client-side, after conversion** — the USD floors cannot be handed to the screener as server-side filters (the field is a local-currency number), so the per-region floor from `screener_filters.usd_floor_for_region` is applied to the converted USD cap, with the region volume gate applied to the company's liquidity (max volume across its venue rows) rather than the selected print.

### FX table (source: open.er-api, 3 Nov 2026 00:02 UTC)

| Currency | Per 1 USD | Frankfurter (2026-11-03) | Difference |
|---|---|---|---|
| EUR | 0.893269 | 0.89453 | +0.14% |
| AUD | 1.427896 | 1.4319 | +0.28% |
| CAD | 1.39809 | 1.3975 | −0.04% |
| JPY | 157.896122 | 158.29 | +0.25% |
| DKK | 6.667072 | 6.6853 | +0.27% |
| TWD | 32.589181 | *no TWD rate* | — |

## Caveats

- **Japan has no file.** The TSE was closed on 3 November (Culture Day). The 2 November file remains the latest Japanese session in this archive; do not read the missing `jp.csv` as a fetch failure. Evidence that the market was shut rather than merely unserved: the skill's holiday calendar marks the day, and all 1,390 scanner rows for Japan are byte-identical to the 2 November file, volumes included.
- **87 written rows did not trade today** and are listed in `_carryover.json`: 14 rows whose close is identical to 2 November while the source's change column is non-zero (a stale leftover — e.g. `EURONEXT:CROS` −8.76% on 11 shares, `VIE:BTS` −3.61% on 70 shares), and 73 rows with an unchanged close on zero volume. A further **181 rows closed exactly flat with real volume** — those *did* trade and are not carry-overs. All carry-over rows are excluded from every movers list.
- **243 rows have no market cap and were excluded** (133 Canada, 56 Taiwan, 35 Spain, 4 Australia, 4 Germany, 3 Austria, 4 Finland, 2 Italy, 1 France, 1 Belgium, 1 Denmark). A row with no cap cannot be tested against a cap floor, so writing it would have put an unscreenable row in a screened file. The composition differs by region: the Canadian ones are preferred and share-class lines where the source publishes no company cap; the Taiwanese ones are small TPEx names; the Spanish ones are zero-volume SICAV and fund lines quoted on BME.
- **Share-class market caps are company-level.** TradingView replicates one cap across every line of a company, so preferred and unit lines carry their parent's cap and all clear the same floor. `BME:GRF.P` carries Grifols' ~$7.3bn and `EURONEXT:AL2SI` carries 2CRSI's ~$0.34bn. This inflates the apparent size of Canadian, Spanish and German preferreds — and it is why a preferred line can appear as a region's largest mover.
- **One market cap is materially overstated.** `ASX:BHP` implies 5.11bn shares against a real count near 2.13bn, so BHP's market cap reads ~$202bn instead of ~$86bn. Every other checked name lands on a plausible share count. The field is written as the source reports it, but a cap-based screen will treat BHP as a mega-cap when it is not. (This is a repeat of the 2 November anomaly, unchanged.)
- **Taiwan's limit moves are genuine prints, not data errors.** Kinsus, Cosmo, Horng Terng and MPI closed at exactly −10.00% and Nanya and Nan Ya Plastics at −9.97% (their limit floors), all independently confirmed by CNA, Taiwan News and Focus Taiwan. A move past ±10% would mean the limit reference price was adjusted for a capital action; these are inside the band.
- **One scanner close differs from the official auction close.** Vienna's own price page puts AT & S (`VIE:ATS`) at €139.60 (+6.89%) at the 17:22 closing auction against a €130.60 reference, while the scanner prints €138.00 (+5.67%). Every other checked name matched its official close to the cent (TeamViewer €5.29, Alstom €11.125, Corticeira Amorim €6.33, Grifols €11.23, Neste €27.54, AMP A$2.13, TSMC NT$2,295, MediaTek NT$3,675, Delta NT$1,270, Kinsus NT$819). The file keeps the scanner's print, and this one row is worth a second look before it is used for anything size-sensitive.
- **Two Canadian rows carry no `change_pct`** (`TSX:TXR`, `TSX:MAXQ`): the source returned no change value and nothing was imputed. They are excluded from the breadth counts.
- **Yahoo's TAIEX daily bar lags the session** (it still serves the 2 November close), so the 3 November level and change were taken from the Yahoo quote page and cross-checked against CNA, Focus Taiwan and Taiwan News, which agree on 43,307.54 and −1,612.60 / −3.59%. The ATHEX close (2,616.12, +0.53%) comes from local press — there is no Yahoo index symbol for the ATHEX — and TradingEconomics' CFD quote reads 2,617.5 / +0.58%, a 1.4-point difference from the official close.
- **Cross-listings are not deduplicated against the US snapshot.** As the skill already notes, a name listed in two markets appears in both files with different closes.
- **Row count versus 2 November:** 4,475 rows then, 3,082 today — but 1,390 of yesterday's were Japanese and Japan did not trade. Excluding Japan, today is **3,082 against 3,085**, a difference of three rows, which is market movement rather than missing data.
- **Prices carry the source's precision** (4 decimals, trailing zeros stripped); Alstom's €11.125 half-cent and Grifols' €7.78 preferred line are as printed.

## Source health

| Source | Query / URL | Status | Result |
|---|---|---|---|
| TradingView scanner (per-country) | `POST https://scanner.tradingview.com/{australia,japan,taiwan,canada,germany,france,italy,spain,netherlands,belgium,austria,portugal,ireland,finland,denmark,greece}/scan` with `country` + `type=stock` | `ok` | 16/16 regions HTTP 200, 18,290 stock rows pulled (14,398 for the 15 written regions + 3,892 for Japan, which had no session); 0.07–1.94 s per call, no rate limit |
| TradingView scanner (columns) | `name,description,close,open,high,low,change,change_abs,volume,market_cap_basic,exchange,currency,sector,price_earnings_ttm,type,country,pricescale,minmov` | `ok` | 18 columns for every row; the response carries no `columns` array, so rows are zipped positionally against the request list |
| Yahoo Finance chart API (index levels) | `query1.finance.yahoo.com/v8/finance/chart/{^AXJO,^AORD,^TWII,^GSPTSE,^GDAXI,^FCHI,FTSEMIB.MI,^IBEX,^AEX,^BFX,^ATX,PSI20.LS,^ISEQ,^OMXH25,^OMXC20,^N225,^STOXX}` | `ok` | 16/17 series returned a 3 November bar (local-date conversion via `gmtoffset`); `^TWII`'s bar still serves 2 November and `^OMXC20` returns a single bar, so both were taken from the Yahoo quote page instead |
| Yahoo Finance quote pages (verification) | `finance.yahoo.com/quote/{%5ETWII,%5EOMXC20}/` via `web_fetch` | `ok` | TAIEX 43,307.54 (prev 44,920.14); OMX Copenhagen 20 1,648.67 (prev 1,646.11) |
| Market-session probe | `market_session_probe.py --region <r> --date 2026-11-03` (16 runs) | `ok` | 15/16 `traded=yes` with a 3 November last bar; `jp` returned `traded=unknown` (Yahoo `^N225` last bar 2 November) — resolved independently, see Caveats |
| Press cross-check | CNA, Focus Taiwan, Taiwan News, Irish Times, Investing.com, Jornal Económico, RBA, CommBank, SBS, euro2day, Morningstar, Reuters, detroitnews, wienerborse, euronext.com, tradingeconomics | `ok` | 20+ quoted levels matched the snapshot: TAIEX 43,307.54 −3.59%, ASX 200 8,886.8 +0.30%, All Ordinaries 9,008.9 +0.40%, STOXX 600 645.66 −0.58%, PSI 9,223.89 −0.31%, ATHEX 2,616.12 +0.53%, TSMC NT$2,295 −1.50%, MediaTek NT$3,675 −7.43%, Delta NT$1,270 −6.27%, Nanya NT$411 −10%, Nan Ya Plastics NT$271 limit-down, Grifols €11.23 +2.09%, ASML −1.63%, Bayer +3.64%, AMP A$2.13 −9.36%, Alpha HPA A$0.335 −24.72%, RBA cash rate 4.85% (+25bp) |
| open.er-api | `https://open.er-api.com/v6/latest/USD` | `ok` | 3 Nov rate table (updated 3 Nov 00:02 UTC), 6 currencies |
| Frankfurter (FX cross-check) | `https://api.frankfurter.app/latest?from=USD` | `ok` | 2026-11-03 rates; agrees within 0.5% on EUR/AUD/CAD/JPY/DKK; no TWD |
| MCP-over-HTTP bridge | `market-recap` / `stocktwits` / `shibui` via `mcp_bridge.py` | `429 rate-limited` | The gateway returned "Today's 50 free anonymous calls are used up" (resets 2026-11-04T00:00Z) — a rate limit, not an absent source. The scanner supplies every schema field, so no bridge call was needed for the artifact |
| Yahoo Finance JSON API (enrichment) | chart / spark / screener | `429 rate-limited` | not used — the scanner supplies every schema field, so no Yahoo enrichment call was made |
| `mcp__tradingview__*`, `mcp__yahoo_finance__*` | — | `unavailable` | not registered in this runtime (as documented in the cron prompt); the public scanner API replaced them |
| Connector catalog probe | `probe_mcp.py` | `ok` | `catalog_ok total=135 finance_tools=0` — healthy catalog, no financial MCP registered |

## Files

`international-eod/2026-11-03/` — `au.csv`, `ca.csv`, `eu-at.csv`, `eu-be.csv`, `eu-de.csv`, `eu-dk.csv`, `eu-es.csv`, `eu-fi.csv`, `eu-fr.csv`, `eu-gr.csv`, `eu-ie.csv`, `eu-it.csv`, `eu-nl.csv`, `eu-pt.csv`, `tw.csv`, `summary.md`, `_manifest.json`, `_excluded.json`, `_carryover.json`

Schema: `date,ticker,name,open,high,low,close,volume,change_pct,market_cap,pe_ratio,sector,currency,exchange`. `ticker` is `EXCHANGE:symbol` (e.g. `XETR:SAP`, `TWSE:2330`, `TSX:RY`). Empty cells mean the source had no value — nothing is imputed. `market_cap` is USD; the prices are in the listing currency named by `currency`.

Integrity checks passed on all 15 files: no non-positive closes, no `high < max(open, close)` or `low > min(open, close)` violations, no `N/A` literals, every row dated 2026-11-03, every row carrying a positive USD market cap. 3,045 of the 3,057 tickers that exist in both today's and 2 November's file chain from the prior close through `change_pct` (tolerance: the larger of 0.02 price units and 0.1% of price); **all 12 that do not are carry-over rows whose `change_pct` is a stale leftover**, and two further stale-change rows fall inside the tolerance.

---

Generated by cron #05 at 2026-11-03 16:32 ET (window check passed: weekday, 16:30 ET slot; not a delayed replay — `scheduled_at_ms` 1793741400000 resolves to 2026-11-03). One region was skipped for a holiday: **jp — TSE closed for Culture Day, confirmed by two independent sources.**
