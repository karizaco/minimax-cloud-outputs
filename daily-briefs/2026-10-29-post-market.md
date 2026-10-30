# Post-Market Brief — Thursday, 2026-10-29 (US/Eastern)

**Cash close 16:00:00 ET · After-hours snapshot ~20:05 ET (extended close) · Futures snapshot 22:30 ET · Written 22:45 ET**
`_source=tradingview_scanner (america/scan) + cboe_delayed_quotes + nasdaq_quote_api (/info, /historical) + cnbc_quote_service + us_treasury_daily_yield_csv + shibui_mcp_bridge (HTTP JSON-RPC) + cboe_options_daily_statistics + us-eod/2026-10-29.csv (cron #20) + web_search/web_fetch`
`_mcp_available=none` (see Source health)

---

## TL;DR

- **Alphabet's report broke the index, not the market.** The S&P 500 closed **7,720.39 −0.31%** and the Nasdaq Composite **26,184.73 −1.38%**, but the Dow held **52,343.00 −0.25%** and the Russell 2000 actually **gained 1.00% to 2,859.22**. The damage was concentrated: **GOOGL −12.64% to $283.82** — "steeper than any session since it went public in 2004" (Yahoo Finance) — with **GOOG −12.29%** and the listed Alphabet classes **GOOGM −8.97% / GOOGN −8.77%**, erasing roughly **$500B of market value**.
- **Underneath the index the tape was broad, green and defensive.** **RSP +1.20% against SPY −0.38% is a 158bp gap** — the equal-weight index beat the cap-weight by more than four points of percentage, the exact mirror image of yesterday's −38bp. In the liquid universe (cap > $200M, vol > 100k) **2,140 names advanced against 1,068 decliners — a 2.00:1 breadth ratio** — and **XLV +2.35%, XLRE +2.21%, XLP +1.52%, XLU +1.51%, XLF +1.44%** all led, while the two losers were **XLC −1.87%** and **XLK −1.20%**.
- **The three earnings bombs of the night landed after the bell.** **Intel −23.03% to $70.87** on a Q4 guide of $15–16B against a ~$17.1B consensus; **Amazon −7.30% to $225.99** on a top-and-bottom-line miss and **trailing-twelve-month free cash flow of −$42.4B**; and **Reddit −18.21%**, **Twilio −16.91%**, **Roblox −16.60%** on guidance. **Nasdaq-100 futures −2.27% at 22:30 ET** versus **S&P 500 futures −1.05%** and **Dow futures −0.24%**.
- **Macro was hot but not hot enough.** Q3 GDP came in at **3.4% annualized** (above expectations), September **headline PCE at 3.6% y/y** (0.1pt below the 3.7% consensus, up from 3.4%) and **core PCE at 3.1%** (in line, up from 3.0%) — a 67th consecutive month above the Fed's 2% goal, with energy up 9.2% m/m on the Iran war. The 2-year **fell 6bp to 4.61%** and the 10-year **7bp to 4.98%**, so the market took the slightly-soft headline as a reason to fade a December hike.
- **Software did not stay contained.** ServiceNow **−26.95%** (on top of −18.10% after hours Wednesday) and Fortinet **−20.09%** (after −25.71%) put Alphabet's two-day damage on the hyperscalers' peers; Marvell **−13.24%**, Oracle **−3.45%**, Salesforce **−4.61%**, Palo Alto **−3.53%**, Zscaler **−3.12%**, Atlassian **−7.28%**. CrowdStrike fell only **2.07%** — the contagion narrowed in the cash session and then widened again after the bell.

---

## 1. Day's tape

| Asset | Close | Chg | Chg % | Day range | Volume (vs 10-session avg) |
|---|---|---|---|---|---|
| S&P 500 (^SPX) | 7,720.39 | −23.59 | **−0.31%** | 7,690.94 – 7,732.21 | — |
| Nasdaq Composite (^IXIC) | 26,184.73 | −365.12 | **−1.38%** | n/a (index level only) | — |
| Nasdaq 100 (^NDX) | 29,402.51 | −410.65 | **−1.38%** | 29,257.05 – 29,517.80 | — |
| Dow Jones (^DJI) | 52,343.00 | −132.00 | **−0.25%** | 52,086 – 52,406 | — |
| Russell 2000 (^RUT) | 2,859.22 | +28.71 | **+1.00%** | 2,841.43 – 2,868.37 | — |
| VIX | 17.20 | +0.29 | **+1.69%** | 16.21 – 17.34 | — |
| VXN | 25.18 | +1.40 | **+5.89%** | 23.66 – 25.39 | — |
| US 2Y | 4.61% | −0.06 | **−6bp** | — | — |
| US 10Y | 4.98% | −0.07 | **−7bp** | — | — |
| US 30Y | 5.32% | −0.05 | **−5bp** | — | — |
| SPY | 769.36 | −2.95 | **−0.38%** | 766.62 – 770.76 | 40.09M (103%) |
| QQQ | 715.34 | −10.27 | **−1.44%** | 711.62 – 718.07 | 38.25M (94%) |
| IWM | 284.01 | +2.72 | **+0.96%** | 282.15 – 285.26 | 21.63M (95%) |
| DIA | 522.73 | −1.95 | **−0.37%** | 520.80 – 523.46 | 2.96M (94%) |
| **RSP (equal-weight S&P)** | 220.04 | +2.61 | **+1.20%** | 218.18 – 220.04 | 8.71M (98%) |
| SMH (semis) | 561.67 | −6.00 | **−1.06%** | 555.50 – 565.87 | 6.02M (n/a) |
| GLD | 368.57 | −4.94 | −1.32% | 366.97 – 369.94 | 9.12M (108%) |
| TLT | 81.73 | +0.50 | +0.62% | 81.16 – 81.86 | 26.02M (74%) |
| USO (crude) | 168.19 | +1.62 | +0.97% | 163.35 – 168.40 | 4.45M (83%) |

*Volume ratios are today's consolidated volume against the trailing 10-session average (today excluded) — TradingView's `relative_volume_10d_calc` where the ETF is in that feed, and shibui's trailing average through 2026-10-28 where it is not (TLT, over the nine available sessions). Index levels carry no volume. The Cboe quote service's `prev_day_close` field echoes the current price for every index and ETF it serves — the prior-session closes in this table are taken from shibui's 2026-10-28 bars and the close-to-close change from the quote service's own `price_change`, which cross-check exactly on all 18 ETFs.*

**Ten-session context (closes):**

| | 10-16 | 10-19 | 10-20 | 10-21 | 10-22 | 10-23 | 10-26 | 10-27 | 10-28 | **10-29** |
|---|---|---|---|---|---|---|---|---|---|---|
| SPY | 763.25 | 766.48 | 769.05 | 773.09 | 763.96 | 759.97 | 765.37 | 769.66 | 772.31 | **769.36** |
| QQQ | 709.80 | 718.36 | 717.63 | 725.20 | 704.47 | 704.40 | 712.20 | 721.25 | 725.61 | **715.34** |
| IWM | 270.44 | 271.28 | 275.78 | 276.48 | 276.67 | 275.75 | 276.99 | 280.18 | 281.29 | **284.01** |
| RSP | 214.09 | 213.40 | 215.86 | 216.64 | 218.22 | 216.54 | 217.29 | 217.52 | 217.43 | **220.04** |
| GLD | 382.01 | 379.69 | 377.65 | 378.95 | 369.00 | 366.61 | 367.82 | 372.28 | 373.51 | **368.57** |
| TLT | 80.05 | 79.46 | 80.13 | 80.24 | 81.74 | 81.34 | 81.68 | 81.63 | 80.99 | **81.73** |

**The week in one line:** the Nasdaq Composite is **+0.88% on the week (+229.39 points)** and the Nasdaq-100 **+1.54%**, but the equal-weight S&P is **+1.62%** and the small-cap proxy **+3.00%** — the week's gains are in the parts of the market Alphabet does not own. Year-to-date from the 2025-12-31 close, **SPY +12.84%, QQQ +16.45%, RSP +14.88%, IWM +15.36%, DIA +8.77%**, against **GLD −7.00%** and **TLT −6.24%**.

**The narrative:**
- *MT Newswires:* "The Nasdaq Composite and the S&P 500 fell Thursday, snapping a three-day advance, following a disappointing earnings report from Alphabet and hot inflation data." The Nasdaq shed 1.4% to 26,184.72; the S&P 500 and Dow dropped 0.3% each to 7,720.39 and 52,342.56. "Among sectors, communication services saw the steepest decline, while healthcare paced the gainers."
- *Investopedia:* "Tech stocks fell as shares of Alphabet sold off and investors digested financial results from big companies and fresh inflation data that was cooler than expected." Alphabet's EPS was **$2.12 vs a Visible Alpha consensus of $2.94** on revenue of **$127.58B vs $127.89B**; cloud revenue roughly doubled to $30.7B but search and advertising fell short. "Alphabet Stock Turns Negative for 2026" — the shares were trading at levels not seen since April, and back in the red for the year after a 13% S&P gain YTD.
- *Hargreaves Lansdown:* "Alphabet shares slumped nearly 13% after the Google parent missed third-quarter expectations on both earnings and revenue and reported over $9bn of negative free cash flow, while keeping full-year capex guidance unchanged at $195bn to $205bn."
- *Yahoo Finance:* "Alphabet stock fell 12% Thursday, steeper than any session since it went public in 2004," and the Nasdaq futures plunge was a "chip rally falters" story — Samsung Electronics also disappointed overnight, and the pre-market chip complex (SNDK, MU, ORCL, MSFT capex restraint) was hit before the open.
- *StockTitan:* Alphabet's market cap loss was "about $500 billion," from the $324.89 close of October 28 to the $283.82 close. BofA Securities attributed the search-revenue miss to "more people us[ing] AI-powered summaries that appear at the top of search results."
- *Schwab (midday):* "Caterpillar (CAT) toppled 9% despite topping consensus on earnings per share and hitting analysts' revenue estimates." Alphabet's 11% pre-market plunge "reverberated through the AI sector"; Zscaler fell 7%, CrowdStrike and Palo Alto more than 6%, and the neoclouds CoreWeave and Nebius both slipped more than 6% on "tight financial conditions for companies spending heavily on the data center buildout."

---

## 2. Sector rotation (top 3 / bottom 3)

Ranked by SPDR sector ETF regular-session change (official closes). The cross-check column is **breadth inside the 4,899-name US universe** from cron #20's EOD snapshot (GICS sector labels, advance/decline counts) — deliberately *not* a market-cap-weighted aggregate; see Source health for why.

| Rank | Sector | ETF | Close | Chg % | Broad universe: adv / dec (n) | Read |
|---|---|---|---|---|---|---|
| 1 | **Health Care** | XLV | 184.04 | **+2.35%** | 442 / 393 (852) | LLY +6.63%, TDOC +26.89%, GKOS +33.65%, BHC +28.76% — but IOVA −35.45%, ALNY −25.13% |
| 2 | **Real Estate** | XLRE | 43.06 | **+2.21%** | 162 / 31 (193) | Rates fell 5–7bp across the curve; 84% of the sector advanced |
| 3 | **Consumer Staples** | XLP | 88.18 | **+1.52%** | 93 / 61 (155) | Defensive bid; SFM −22.58% was the one big drag |
| … | Utilities | XLU | 43.14 | +1.51% | 68 / 16 (85) | Rate-sensitive, and rates fell |
| … | Financials | XLF | 56.94 | +1.44% | 871 / 301 (1,201) | MA +4.18%, JPM +1.25%, BAC +0.57%; the safest place to park the money |
| … | Industrials | XLI | 170.13 | +0.96% | 398 / 156 (564) | CAT −9.25% was the outlier |
| … | Consumer Discretionary | XLY | 116.20 | +0.75% | 289 / 101 (393) | CVNA +15.68%, HD +3.59%, LOW +4.46% vs AMZN −4.25% |
| … | Energy | XLE | 68.71 | +0.38% | 82 / 102 (186) | USO +0.97% but crude is the only thing that worked |
| 9 | **Information Technology** | XLK | 188.74 | **−1.20%** | 204 / 302 (512) | NOW −26.95%, FTNT −20.09%, MRVL −13.24% vs AAPL +1.48%, MSFT −0.16% |
| 10 | **Communication Services** | XLC | 101.21 | **−1.87%** | 110 / 57 (171) | Alphabet is the sector; GOOGL alone is ~12.5% of XLC |

*Reference: SMH (semiconductors) 561.67, −1.06%.*

**Read:** this was a **rotation, not a risk-off session**. The two worst sectors are exactly the two that own the AI-capex trade, and the eight that rose are the eight that own cash flows and duration. But note what the breadth column says about Health Care: 442 advancers against 393 decliners is a coin flip across the 852-name universe even though XLV closed +2.35% — the health-care bid was a **large-cap** bid (Lilly +6.63%), and the same sector's biotech was being sold (Iovance −35.45%, Alnylam −25.13%). Real Estate and Utilities, by contrast, advanced on breadth (162/31 and 68/16), which is what a genuine rate move looks like.

---

## 3. Large-cap leaders & laggards (watchlist substitute)

> **`watchlist.yaml` is unavailable.** It is absent from this Cloud workspace, from the migration repo (`cloud-prompts/skills/agentic-post-market-brief/` carries only `SKILL.md`) and from the outputs repo tree — the same gap the 2026-10-28 brief documented. This section therefore uses the same **defined Pass-B basket** for continuity: US-listed names with market cap > $40B in the TradingView scanner universe (643 names), plus the **liquid movers screen** (cap > $2B, volume > 1M; 1,212 names).

**Large-cap leaders (cap > $40B):**

| Ticker | Close | Chg % | AH print | AH % | rvol (10d) | Catalyst |
|---|---|---|---|---|---|---|
| CVNA | 68.31 | **+15.68%** | 67.65 | −0.97% | 2.63 | No catalyst confirmed in this run |
| LNG | 318.94 | **+7.11%** | 319.85 | +0.29% | 2.48 | No catalyst confirmed in this run |
| LHX | 278.43 | **+6.84%** | 278.30 | −0.05% | 1.79 | No catalyst confirmed in this run |
| LLY | 1,373.70 | **+6.63%** | 1,383.29 | +0.70% | 1.83 | Q3 adj. EPS **$7.48 vs $6.26 est**; revenue **$24.4B vs $22.61B est** (+39%); FY26 revenue guide raised to **$91–92B** |
| NXPI | 266.00 | +5.69% | 261.00 | −1.88% | 1.24 | No catalyst confirmed in this run |
| DASH | 179.00 | +5.61% | 181.33 | +1.30% | 2.44 | No catalyst confirmed in this run |
| HWM | 205.94 | +5.51% | 206.50 | +0.27% | 1.26 | No catalyst confirmed in this run |
| KLAC | 167.43 | +5.45% | 164.82 | −1.56% | 1.21 | Semicap bid inside the AI complex |
| GD | 370.82 | +4.65% | 377.95 | +1.92% | 1.70 | No catalyst confirmed in this run |

**Large-cap laggards (cap > $40B):**

| Ticker | Close | Chg % | AH print | AH % | rvol (10d) | Catalyst |
|---|---|---|---|---|---|---|
| NOW | 109.67 | **−26.95%** | 107.94 | −1.58% | 5.02 | Third day of the software de-rating (Wed AH −18.10%); no new company news |
| FTNT | 139.10 | **−20.09%** | 137.65 | −1.04% | 3.70 | Continues Wednesday's −25.71% after-hours break (two-day ≈ −40%) |
| MRVL | 218.34 | **−13.24%** | 208.75 | −4.39% | 2.35 | AI-capex complex; the Marvell–Lumentum M&A talk reversed |
| GOOGL | 283.82 | **−12.64%** | 280.66 | −1.11% | 5.02 | Q3 miss: EPS **$2.12 vs $2.94**, search revenue miss, **FCF −$9.07B**, capex held at $195–205B |
| GOOG | 282.32 | **−12.29%** | 279.17 | −1.12% | 5.11 | Same report, Class C |
| HONA | 160.04 | −9.60% | 159.92 | −0.07% | 2.34 | No catalyst confirmed in this run |
| CAT | 647.39 | −9.25% | 643.52 | −0.60% | 2.80 | Beat on EPS and revenue and still fell 9% (CNBC) |
| GOOGM | 42.53 | −8.97% | 42.40 | −0.31% | 15.15 | Same report, listed Class M |
| GOOGN | 42.53 | −8.77% | 42.35 | −0.42% | 10.96 | Same report, listed Class N |
| TEAM | 204.10 | −7.28% | 198.50 | −2.74% | 1.77 | Software de-rating; no own news |
| NBIS | 171.99 | −5.68% | 161.15 | −6.30% | 0.66 | Neocloud funding conditions |
| TER | 296.23 | −5.43% | 285.41 | −3.65% | 1.16 | No catalyst confirmed in this run |

**Liquid movers screen (cap > $2B, volume > 1M) — top gainers:** GKOS **+33.65%**, ADT **+33.20%**, BHC **+28.76%**, PRCH **+28.16%**, CROX **+25.54%**, PURR **+23.27%**, FTAI **+17.27%**, GEN **+15.81%**, CVNA **+15.68%**, BOOT **+15.16%**, INSM **+15.06%**, FCN **+14.28%**, NCLH **+13.45%**, HII **+13.23%**.

**Liquid movers screen — top decliners:** IOVA **−35.45%**, NOW **−26.95%**, ALNY **−25.13%**, SFM **−22.58%**, FTNT **−20.09%**, AUR **−13.46%**, MRVL **−13.24%**, GOOGL **−12.64%**, GOOG **−12.29%**, FORM **−11.65%**, FTRE **−10.61%**, RSI **−9.98%**, HONA **−9.60%**, ASST **−9.52%**.

**Confirmed catalysts for the top of the move list:**
- **ADT +33.20%** — agreed to be acquired by **Thrive Holdings for $10.00 a share in cash, 45.6% above its October 27 close**, a deal valued at **$15.3B including debt**, expected to close in Q1 2027. Volume 163.8M shares (rvol 22.3).
- **GKOS +33.65%** — record Q3 net sales of **$211.03M, +58% y/y**, swung to **$2M net income** from a −$16.2M loss; FY26 sales guidance raised to **$775–785M** and preliminary FY27 sales of **$1B**.
- **BHC +28.76%** — Q3 revenue **$2.941B, +9.7%**, net income **$436M ($1.15/sh)** vs $179M ($0.48), adj. earnings **$673M ($1.77/sh)**; raised guidance and announced a **$50M buyback**.
- **TDOC +26.89%** — Q3 revenue **$605.1M, −3%**, near the top of its own range; net loss narrowed to **−$26.9M** from −$49.5M; adj. EBITDA **+14% to $79.4M**; Integrated Care revenue +2% to $398.5M, BetterHelp −13%.
- **PRCH +28.16%** — Q3 results beat its own expectations and raised the full-year outlook.
- **CROX +25.54%** — raised its FY2026 sales and profit outlook, its third raise this year.
- **CLMB +26.29%** — record Q3 net sales of **$220.3M, +37%**.
- **IOVA −35.45%** — updated Phase 2 IOV-LUN-202 lifileucel data: **17 of 69 patients responded (24.6%)**, called consistent with the 25.6% reported earlier; plans a new biomarker-selected study.
- **ALNY −25.13%** — Q3 product revenue **$1.29B, +52%**, net income **$2.167B ($15.72/sh)**, adj. EPS **$16.26** on revenue **$1.46B** — results *beat*, and the release gives no reason for the drop. A Phase 3 nucresiran (TRITON-CM) update was filed the same morning.
- **XRX −40.32%** — cut its full-year forecasts for operating profit and free cash flow "as headwinds had intensified"; Q3 revenue −4.7% to $1.87B.
- **CAT −9.25%** — beat on EPS and revenue and fell anyway (Schwab).
- **KPLT +37.58%** — the only release since Wednesday's close set **November 12** as its Q3 results date and gives no reason for the gain; a 13G/A filed the same day. Treat as unconfirmed.
- **PURR +23.27%** — no company news found on the closing movers board at 16:00 ET. Treat as unconfirmed.

---

## 4. After-hours movers

Measured in the 16:00–20:00 ET extended session **against the 2026-10-29 regular close**, not the prior close. 91 names moved ≥5% on >10k shares in the liquid universe. Prices are the ~20:05 ET extended close from the TradingView scanner; the Cboe quote service's own 20:05–21:36 ET prints match the TradingView extended close exactly on INTC, AMZN, MDLZ and GOOGL, and differ by 8–70 cents (0.2–1.3 percentage points) on RDDT, TWLO, RBLX and ATEC, which were on a different tick.

**Decliners**

| Ticker | Close | AH price | AH % | AH volume | Note |
|---|---|---|---|---|---|
| ATEC | 11.37 | 8.18 | **−28.06%** | 1.94M | Q3 results — figures not confirmed in this run |
| INTC | 92.07 | 70.87 | **−23.03%** | 51.22M | Q4 guidance miss; CNBC had it at −23.43% ($70.50) at 19:13 ET |
| NPKI | 11.20 | 8.79 | **−21.52%** | 281k | No catalyst confirmed in this run |
| RDDT | 129.60 | 106.00 | **−18.21%** | 5.27M | Q4 revenue guide below consensus |
| AXG | 3.70 | 3.07 | −17.03% | 71k | Q3 results (also −34.86% in the regular session) |
| TWLO | 241.90 | 201.00 | **−16.91%** | 925k | Q4 guide: low end below consensus |
| RBLX | 52.46 | 43.75 | **−16.60%** | 4.64M | Q4 bookings and EBITDA guide |
| DXC | 15.23 | 13.37 | −12.24% | 805k | Q2 results |
| SYK | 311.75 | 275.00 | −11.79% | 492k | Q3 results |
| ALHC | 8.06 | 7.11 | −11.79% | 2.12M | Q3 results |
| CYPH | 3.31 | 2.93 | −11.55% | 2.12M | No catalyst confirmed in this run |
| ILMN | 290.06 | 257.90 | −11.09% | 287k | Q3 results |
| BNC | 5.41 | 4.88 | −9.80% | 347k | No catalyst confirmed in this run |
| PURR | 12.29 | 11.15 | −9.28% | 4.43M | Gave back most of a +23.27% regular-session move |
| COHU | 53.40 | 48.48 | −9.22% | 293k | Q3 results |
| ONTO | 221.89 | 202.15 | −8.89% | 54k | No catalyst confirmed in this run |
| PINS | 19.92 | 18.41 | −7.58% | 8.78M | Q3 miss on both lines |
| HPQ | 31.83 | 29.45 | −7.48% | 2.51M | No catalyst confirmed in this run |
| **AMZN** | **243.79** | **225.99** | **−7.30%** | **26.48M** | **Q3 miss + −$42.4B TTM FCF; Q4 guide below** |
| ASST | 24.91 | 23.15 | −7.07% | 861k | Q3 results |

**Gainers**

| Ticker | Close | AH price | AH % | AH volume | Note |
|---|---|---|---|---|---|
| OSPN | 20.15 | 24.81 | **+23.13%** | 131k | Q3 results |
| CVEO | 30.55 | 36.62 | **+19.87%** | 25k | No catalyst confirmed in this run |
| CDNA | 71.52 | 82.40 | **+15.21%** | 240k | Q3 beat; FY26 revenue guidance raised to $520–530M |
| ASUR | 7.23 | 8.25 | **+14.11%** | 114k | Q3 results |
| RMNI | 3.99 | 4.41 | +10.53% | 87k | Q3 results |
| CTMX | 2.29 | 2.51 | +9.61% | 557k | Q3 earnings date |
| ACCO | 4.36 | 4.74 | +8.73% | 137k | Q3 results |
| **MDLZ** | **62.53** | **67.30** | **+7.63%** | **1.44M** | **Q3 results** |
| INGM | 28.61 | 30.60 | +6.96% | 441k | Q3 results |
| BXBL | 1.90 | 2.01 | +5.79% | 18k | Recovered from −26.64% in the regular session |
| RIVN | 11.45 | 12.09 | +5.59% | 7.43M | Q3 beat; R2 ramp, 19,248 Q3 deliveries, FY26 guidance revised |
| GDYN | 9.49 | 10.00 | +5.37% | 426k | No catalyst confirmed in this run |
| OR | 33.31 | 35.04 | +5.20% | 40k | No catalyst confirmed in this run |

**Index ETFs after the bell (20:05 ET extended close vs the cash close):** SPY **−0.60%** (764.73), **QQQ −1.54%** (704.30), **XLK −2.20%** (184.59), XLC **−0.21%** (101.00), XLV **+0.77%** (185.45), RSP **+0.03%** (220.10), IWM **−0.06%** (283.83), DIA **+0.04%** (522.92), USO **+0.05%** (168.27), GLD **−0.38%** (367.16). *The Cboe quote service's later 21:14–21:36 ET prints on QQQ (704.30) and SMH (542.10) match these exactly and show the selling did not stop at the 20:00 ET extended close.*

---

## 5. After-hours earnings reactions

### Intel (INTC) — **−23.03% to $70.87** — a good quarter and a bad guide
- Q3 **adjusted EPS $0.52 vs $0.40–0.41 expected** (FactSet $0.41; Earnings Whisper $0.47); revenue **$16.51B vs $16.50B expected**, **+21% y/y**.
- **Data center and AI revenue $7.3B, +78%** — the strongest data-center growth in 15 years, and above the $6.6B projected.
- **Q4 guide $15.0–16.0B of revenue vs a ~$17.1B consensus**; adj. EPS guide **$0.25 vs $0.42–0.45**; GAAP gross margin guided to **37.1%** from 43%.
- CFO David Zinsner: "**We see the PC slowdown continuing at least the first half of next year.**" PC chip sales **$8.1B vs an $8.8B target**.
- An **explosion at an Israeli fab** is expected to account for roughly **$300M** of the Q4 miss.
- GAAP EPS fell to $0.60 from $0.90 (last year included a $5.45B Altera gain); diluted share count jumped after a **$23B public offering** this quarter.
- The stock had been up ~150% YTD before the print. **CNBC: −23.43% at $70.50 (19:13 ET); Yahoo: −20.64% at $73.07 (17:39 ET); the 20:05 ET extended close was $70.87.**

### Amazon (AMZN) — **−7.30% to $225.99** — Alphabet's question, answered with a miss
- **EPS $1.89 vs $1.96–1.97 expected**; revenue **$201.94B vs $202.2–202.3B expected** (+12% y/y).
- **AWS $45.98B, +39%** — a beat against $45.29–45.68B, and the fastest in nearly five years; Jassy guided AWS growth **above 40% in both 2027 and 2028** off a **$184B annualized run rate**.
- The misses were elsewhere: **advertising $19.64B vs $20.82B expected**; online store sales **$68.47B vs $69.68B** (North America +6% to $113B versus +16% the prior quarter on a Prime Day calendar shift).
- **Free cash flow on a trailing-twelve-month basis: −$42.4B**, versus +$14.8B a year ago and −$7.6B last quarter. Quarterly **capex $77.3B** versus a $58.7B consensus. FY2026 capex **held at $220B**.
- **Q4 revenue guide $240–247B** (midpoint $243.5B vs $244.5B expected); **Q4 operating income $28.5–33.5B**, midpoint $31B vs $32.99B expected — the operating-income guide is likely the bigger part of the reaction.
- Dan Ives (Yorkville Ives): "AWS exited the quarter at a $184 billion annualized revenue run rate… the debate is how long AWS can run as capacity and Trainium come online." RBC's Brad Erickson noted buy-side "whisper" expectations for AWS had climbed to 42% before the print.
- Print progression: **−6% to ~$227 at 17:40 ET**, **−5.25% to $231.00 at 16:37 ET**, **−7.30% to $225.99 at the 20:05 ET extended close**.

### Reddit (RDDT) — **−18.21% to $106.00** — a beat and a user problem
- Q3 revenue **$895M, +53%**, above the $874.9–878M consensus; EPS **$1.40 vs $1.33**; net income $283M (32% margin); adj. EBITDA $402M; FCF +98% to $363M.
- **US daily active uniques fell 2% y/y** to leave the global figure at **130.3M, +12%** (international +24%) — below expectations.
- **Q4 revenue guide $1.00–1.03B vs a $1.05B consensus** (implies 38–42% growth), attributed to **reduced Google search referrals as AI Overviews take traffic**. The company is shifting to a logged-in-focused experience and set a **$5B annual revenue target**.

### Twilio (TWLO) — **−16.91% to $201.00** — the guide, not the quarter
- Q3 revenue **$1.56B, +20%**, above the $1.52B consensus; non-GAAP EPS **$1.65 vs $1.47**; net income $161M.
- **Q4 revenue guide $1.595–1.605B**, implying **11–12% organic growth, a step down from 16%**; Q4 adj. EPS guide **$1.48–1.53 vs $1.49** expected — the low end missed.

### Roblox (RBLX) — **−16.60% to $43.75** — bookings and users
- **Q3 bookings $1.7B, −12% y/y**, versus $1.63B expected; **DAUs −9% to 138M versus 145.8M expected**; Q3 revenue $1.572B (vs $1.36B).
- **Q4 bookings guide $1.89–2.00B vs $2.00B expected**, and **adjusted EBITDA guide of a $70M to $10M loss**.

### The rest of the after-hours board
- **Pinterest (PINS) −7.58% to $18.41** — Q3 EPS **$0.46 vs $0.48** expected, revenue **$1.17B vs $1.21B** expected.
- **Illumina (ILMN) −11.09% to $257.90** — Q3 results.
- **Stryker (SYK) −11.79% to $275.00** — Q3 results; the stock had risen 2.55% in the regular session.
- **DXC Technology −12.24% to $13.37** — Q2 results.
- **Mondelez (MDLZ) +7.63% to $67.30** — Q3 results; the largest gainer in the S&P 500 after hours.
- **Rivian (RIVN) +5.59% to $12.09** — beat Q3 expectations as it ramped the R2; **19,248 Q3 deliveries**; FY26 guidance revised higher on deliveries, adj. pretax earnings and capex.
- **CareDx (CDNA) +15.21% to $82.40** — Q3 revenue $139M and EPS $0.70, both beating; FY26 revenue guidance raised to **$520–530M** (+39%).
- **Gilead (GILD) +2.65%** on the after-hours board (CappNotes).

---

## 6. Tomorrow's setup — Friday 2026-10-30

**Futures (22:30 ET, Globex, vs prior settlement):**

| Contract | Last | Chg | Chg % | Prior settle |
|---|---|---|---|---|
| S&P 500 (Dec'26, @SP.1) | 7,672.75 | −81.50 | **−1.05%** | 7,754.25 |
| Nasdaq 100 (Dec'26, @ND.1) | 28,891.50 | −670.50 | **−2.27%** | 29,562.00 |
| Dow (Dec'26, @DJ.1) | 52,384.00 | −128.00 | **−0.24%** | 52,512.00 |
| 10-Yr Treasury (Dec'26, @TY.1) | 106.7344 | +0.5469 | +0.52% | 106.1875 |
| US 10Y (cash) | 4.912% | −0.077 | −1.54% | 4.989% |
| US 30Y (cash) | 5.279% | −0.05 | −5bp | 5.329% |
| Russell 2000 | n/a | n/a | n/a | n/a |

*The Russell 2000 future was again unavailable from every symbol variant reachable in this run. Use IWM (284.01, +0.97%) and the cash Russell close (2,859.22, +1.00%) as the proxy. The shape of the curve is the tell: **Dow futures −0.24% and Nasdaq-100 futures −2.27%** — the overnight session is repricing the AI-capex complex, not the market.*

**The macro day — everything lands at 08:30 and 09:45 ET:**

| Time (ET) | Event | Consensus / note |
|---|---|---|
| 08:30 | **Employment Cost Index (Q3)** | **+0.8% q/q** (prior +0.9%); annual rate 3.4% |
| 08:30 | **Weekly jobless claims** (Oct 24) | Prior 194k (a three-month low); continuing claims 1.728M |
| 09:45 | **Chicago PMI (October)** | 54.8 expected, prior 58.8 |
| 10:00 | Multivariate Core Trend Inflation | NY Fed |
| 12:45 | NY Fed Staff Nowcast | — |
| Overnight | **BoJ decision** (Asian session) | Hold at 1.25% expected; ~80% priced for a December hike |
| Overnight | Eurozone Q3 GDP (advance) + unemployment; Canada GDP; UK house prices | — |

**Earnings — Friday's calendar is light on the mega-cap side. The calendars disagree on the totals (Digrin lists 405 reports with 46 before the open and 12 after the close; MetaCap lists 77 with 50 before the open), but both put the big names in the same place — before the open:**

| Session | Names |
|---|---|
| **Before the open** | **ExxonMobil (XOM — release 06:30 ET, call 09:30 ET)**, **Chevron (CVX)**, **AbbVie (ABBV — call 09:00 ET)**, AstraZeneca, BP, Sanofi, General Dynamics (GD), Regeneron (REGN), Canadian National, Colgate, Imperial Oil, Dominion Energy, Exelon, Kenvue, Ubiquiti, Cameco, Cboe Global Markets, Church & Dwight, nVent, LyondellBasell, Magna, RBC Bearings |
| **After the close** | A dozen or fewer reports by the calendars that split them. The TradingView next-print set also carries Globalstar (GSAT), AES, Federal Realty (FRT) and BrightSpring (BTSG), but the scanner does not separate before-open from after-close times — treat their timing as unconfirmed |
| Also Friday | **No FOMC, no CPI, no PPI.** Month-end positioning and the ECI print are the macro events of the week |

- **Exxon and Chevron are the event risk**, not the megacaps. XOM consensus EPS **$3.40–4.12** on revenue **$94.9–104.5B**; CVX **$4.32–4.93** on **$54.9–61.7B**. With crude up 0.97% on USO and the market pricing a December Fed hike against a 3.6% headline PCE, the oil read matters for the inflation path as much as for the stocks.
- **The AI-capex question has a third respondent.** Alphabet's negative free cash flow reset the market's expectations for hyperscaler cash generation; Amazon answered with −$42.4B of trailing FCF and a below-consensus Q4; **Intel answered with a PC slowdown**. All three reports landed within 24 hours, and the Nasdaq-100 future is −2.27% into the open.

**The three things that set the tone tomorrow:**
1. **Does the software damage spread from the mega-caps to the mid-cap software complex?** In the cash session the contagion *narrowed* (CrowdStrike −2.07%, Zscaler −3.12%, Atlassian −7.28%) versus Wednesday's after-hours carnage; after the bell it *widened* again (Twilio −16.91%, Roblox −16.60%, DXC −12.24%, Alignment Healthcare −11.79%). The QQQ after-hours print was only −1.54% while individual software names were down double digits — that gap is the question for the open.
2. **Does the ECI print break the December-hike pricing?** PCE came in 0.1pt below consensus at 3.6% headline and the 2-year still rallied 6bp to 4.61%; a hot ECI (+0.8% q/q or worse) removes the last soft-pushback and pushes the 2-year back toward 4.70%.
3. **Can the equal-weight bid survive an Alphabet-shaped headwind?** RSP +1.20% against SPY −0.38% is the cleanest breadth signal of the run — and it depends on the rotation into health care, real estate, staples and utilities holding, not on the mega-caps stabilising.

---

## 7. Breadth & volatility

| Metric | Value | Change | Note |
|---|---|---|---|
| VIX | **17.20** | +0.29 (+1.69%) | Range 16.21–17.34, opened 17.20 — a session that never had a bid |
| VXN | **25.18** | +1.40 (**+5.89%**) | Prior 23.78; range 23.66–25.39, opened 24.66. The Nasdaq vol premium widened sharply |
| Equity breadth (cap > $200M, vol > 100k) | **2,140 adv / 1,068 dec / 36 unch** | **2.00 : 1** | 3,244 names; **215 up ≥5%, 127 down ≥5%**; 940 up ≥2% vs 480 down ≥2% |
| Full US universe breadth (4,899 names) | 3,030 adv / 1,736 dec | 1.75 : 1 | Includes micro-caps; directionally confirms |
| Equal-weight vs cap-weight (RSP vs SPY) | **+1.20% vs −0.38%** | **+158bp** | The exact mirror of yesterday's −38bp gap |
| Put/call — total | **0.90** | −0.03 | Prior 0.93 (10/28); Cboe daily statistics, 10/29 table |
| Put/call — equity | **0.54** | −0.05 | Prior 0.59; volume 3,270,994 (2,119,311 calls / 1,151,683 puts) |
| Put/call — index | **1.06** | flat | Volume 4,947,283 (2,405,043 calls / 2,542,240 puts) |
| Put/call — ETP | **1.27** | — | Total option volume 10,620,515 (5,582,664 calls / 5,037,851 puts) |
| Put/call — VIX | **0.43** | — | 436,745 contracts (305,524 calls / 131,221 puts) |

**What the breadth actually says:** this was **not** a risk-off session, and that is the most important thing about it. Nearly two-thirds of the liquid universe advanced, 215 names moved more than 5% higher against 127 lower, and the equal-weight S&P outperformed the cap-weight by 158bp. What happened is that **one company took 12.6% off the cap-weighted index** while the equal-weight index rose 1.20% — the damage was Alphabet's, not the market's. The sectors that rose are the ones with no AI-capex exposure or with cash-flow durability: health care, real estate, staples, utilities, financials. The two that fell are the ones that carry the capex question.

**What the vol market says:** VXN **+5.89%** against VIX **+1.69%** is the cleanest read of the session. The options market paid up for Nasdaq-specific risk, not market risk — the Nasdaq vol premium to VIX widened from **23.78 vs 16.91 (6.87 points)** to **25.18 vs 17.20 (7.98 points)**. That is the market pricing Alphabet's read-through to the rest of the Nasdaq, which is exactly what the Intel and Amazon prints delivered three hours later. Total put/call at 0.90 and equity put/call at 0.54 show no broad hedging rush — this was a concentrated repricing, not a de-risking.

---

## 8. Open research queue

1. **Quantify the Alphabet contribution.** GOOGL is ~12.5% of XLC and the largest S&P weight in the scenario; a 12.64% single-name drop plus the listed Alphabet classes (GOOGM, GOOGN) needs to be subtracted from the index move before any conclusion about "the market." Rebuild the ex-Alphabet S&P 500 return properly — the RSP +1.20% is an approximation, not a substitute.
2. **Resolve the market-cap anomaly in the EOD universe file.** `us-eod/2026-10-29.csv` implies Alphabet at ~52% of Communication Services' market cap, while XLC's published holdings (as of 10/28) put GOOGL at 12.49% and GOOG at 10.02%. Until the shibui valuation column is reconciled, no cap-weighted sector aggregate from that file should be published — this is why §2 reports breadth instead.
3. **Verify the unconfirmed after-hours movers.** ATEC (−28.06%), NPKI (−21.52%), AXG (−17.03%), CYPH (−11.55%), BNC (−9.80%) and OSPN (+23.13%), CVEO (+19.87%), GDYN (+5.37%), OR (+5.20%) all moved double digits with no catalyst confirmed in this run. Check each issuer's IR page and 8-K directly.
4. **Explain Alnylam.** ALNY fell 25.13% on a beat-and-raise-quarter ($1.46B revenue, $16.26 adj. EPS, product revenue +52%) with an accompanying nucresiran Phase 3 update. Something in the release or the call is not being reported.
5. **Separate the software contagion from the AI-capex repricing.** NOW −26.95%, FTNT −20.09%, TEAM −7.28%, CRM −4.61%, PANW −3.53%, ZS −3.12%, CRWD −2.07% in the cash session, versus TWLO −16.91%, RBLX −16.60%, DXC −12.24% after the bell. The cash session narrowed, the after-hours session widened. Check the AH timestamps against each release to see which names moved on the Alphabet read-through and which on their own guidance.
6. **Map the December-hike pricing.** PCE at 3.6% headline and core at 3.1% with both FOMC dissents wanting a hike, but the 2-year rallied 6bp on a 0.1pt headline miss. Put the SOFR and Fed-funds futures path against tomorrow's ECI and the Nov 6 jobs report.
7. **Watch the oil complex into the XOM/CVX prints.** USO +0.97% with the Iran war still in the headlines and energy prices +9.2% m/m in September PCE. If crude extends, the December-hike odds rise regardless of what ECI prints.
8. **Confirm the breadth durability.** RSP +1.20% vs SPY −0.38% with no volume thrust (SPY rvol 1.03) is the strongest breadth print of the run. The open question is whether it survives an Alphabet-shaped gap-down in the mega-caps.

---

## 9. Source health

| Source | Endpoint / query | HTTP | Status | Used for |
|---|---|---|---|---|
| TradingView scanner | `POST scanner.tradingview.com/america/scan` — 20 calls: 7 breadth counts, 4 mover screens (120/120, 60/60, 40/40, 40/40), 4 large-cap/liquid screens, 1 full 3,244-row liquid universe, 1 earnings-date screen, 12 single-ETF quote pulls | 200 | **ok** | Per-stock close/change/after-hours/rvol; breadth counts; sector aggregates; ETF closes |
| Cboe delayed quotes | `cdn.cboe.com/api/global/delayed_quotes/quotes/{SYM}.json` — 24 index/ETF symbols + 11 single stocks (INTC, AMZN, RDDT, TWLO, RBLX, ATEC, MDLZ, GOOGL, NOW, FTNT, QQQ) | 200 | **ok** | Official closes, day ranges, volumes, sector rotation, VIX/VXN, and an independent after-hours print on 11 names |
| Cboe delayed quotes — validation | `close` vs TradingView `close` for all 24 index/ETF symbols; `price_change` vs shibui's 10/28 closes | 200 | **ok — 24/24 closes identical, 18/18 close-to-close changes exact** | Proof the quotes carry the *settled 10/29* close and a correct prior-session reference |
| Nasdaq quote API | `api.nasdaq.com/api/quote/{SYM}/info?assetclass=index` — COMP, NDX | 200 | **ok** | Nasdaq Composite 26,184.73 (−1.38%), Nasdaq-100 29,402.51 (−1.38%) |
| Nasdaq quote API | `/info` for INDU, SPX, RUT, VIX | 400 | **failed — "Symbol not exists"** | Dow, S&P and Russell levels came from Cboe instead |
| Nasdaq historical | `api.nasdaq.com/api/quote/COMP\|NDX/historical` (2026-01-02 → 2026-10-29) | 200 | **ok** | 10-session index closes; week-to-date for COMP and NDX |
| Nasdaq extended-trading | `api.nasdaq.com/api/quote/{SYM}/extended-trading?markettype=post` (+ `assetclass=stocks`) — 16 names | 400/200 | **failed — `tradesTable` empty and `previousInfo` serves the 10/28 close** | Endpoint no longer returns today's extended tape; the Cboe and TradingView after-hours prints were used instead |
| Nasdaq bulk screener | `api.nasdaq.com/api/screener/stocks?download=true` | — | **not used** | Sector labels came from cron #20's EOD file, which is GICS-tagged and same-day |
| CNBC quote service | `quote.cnbc.com/quote-html-webservice/restQuote/symbolType/symbol?symbols={SYM}` — @SP.1, @ND.1, @DJ.1, @TY.1, @RTY.1, US10Y, US30Y | 200 | **ok for 6 of 7** | Futures at 22:30 ET; cash 10Y/30Y overnight |
| CNBC quote service | Same, `@RTY.1` | 200 | **failed — no data for the Russell future** | Russell futures unavailable; flagged in §6 |
| US Treasury | `home.treasury.gov/.../daily_treasury_yield_curve.csv/2026/all` | 200 | **ok** | Official 2y/10y/30y closes for 10/29 and 10/28 (2s10s +37bp, from +38bp) |
| shibui MCP bridge (HTTP JSON-RPC) | `mcp.shibui.finance/mcp` → `stock_data_query` — 4 calls | 200 | **ok — but the EOD ingest lags ~30 min, so the latest bar is 10/28** | 10-session close/volume history; 2025-12-31 and 2026-01-02 closes for the YTD calculation; independent OHLCV on GOOGL/META/NFLX/SPY/QQQ/RSP/XLC/XLK |
| StockTwits MCP bridge (HTTP JSON-RPC) | `gateway.pipeworx.io/stocktwits/mcp` → `chart_data` (SPY, 1M) | 200 | **ok (1 of a 50/day anonymous quota)** | Independent OHLCV check on SPY: 23 daily bars, last close **769.36** — matches Cboe and TradingView exactly |
| Cboe options daily statistics | `cboe.com/markets/us/options/market-statistics/daily/` (via web_search) | — | **ok — 10/29 table** | Put/call ratios and option volumes (total 0.90, equity 0.54, index 1.06, ETP 1.27, VIX 0.43) |
| Cboe options statistics API | `cdn.cboe.com/api/global/us_indices/market_statistics/daily` | 403 | **failed — 403** | Fell back to the published daily-statistics page |
| Cboe US equities market share | `cboe.com/us/equities/market_share/` | 200 | **ok for the page, unusable for the day figure** | The page exposes only 30-day and month-to-date totals (`day_total` not present in the served payload), so **consolidated share volume for 10/29 was not retrieved** |
| US EOD universe (cron #20 artifact) | `karizaco/minimax-cloud-outputs@main:us-eod/2026-10-29.csv` — 4,899 rows | 200 | **ok for prices/breadth/sector labels; market-cap column NOT used** | Per-sector advance/decline counts; close and change cross-checks against Cboe and TradingView |
| Yahoo Finance JSON (chart/screener/spark) | — | 429 | **failed — persistent 429 (known from the runtime contract)** | Not used; Yahoo HTML and the JSON endpoints are both unusable for bulk data from this egress |
| Yahoo Finance HTML | `finance.yahoo.com/quote/XLC/history/` (via web_search) | — | **ok** | Independent confirmation of XLC's 10/29 OHLCV (101.18 / 101.76 / 100.13 / 101.21, 6.62M) |
| `mcp__yahoo_finance__*` / `mcp__tradingview_advanced__*` / `mcp__shibui_finance__*` | — | — | **do not exist in this runtime** | Replaced by the HTTP JSON-RPC bridge and the HTTP endpoints above |
| `watchlist.yaml` | workspace, migration repo tree, outputs repo tree | 404 | **failed — absent everywhere** | §3 uses the documented Pass-B basket instead |

**Degraded data paths — what this brief does *not* have:**
- **No consolidated share volume for 10/29.** The Cboe market-share page served only 30-day and month-to-date aggregates; the per-day figure was not in the payload, so no volume-thrust comparison against a 20-day average is offered. The ETF relative-volume column (rvol) is the substitute.
- **No cap-weighted sector aggregate.** `us-eod/2026-10-29.csv` implies Alphabet at ~52% of Communication Services' market cap, which is irreconcilable with XLC's own published holdings (GOOGL 12.49% + GOOG 10.02% as of 10/28) and with XLC's −1.87% close. §2 therefore ranks sectors on the official ETF closes and cross-checks with advance/decline breadth, which do not depend on the market-cap column.
- **No Russell 2000 future.** Every symbol variant returned no data.
- **No index day-range for the Nasdaq Composite**, and no day-range for the Dow (Cboe publishes a Dow sector index, not the DJIA).
- **No Nasdaq extended-trading tape.** The endpoint now returns an empty table and a prior-session close; the after-hours numbers here come from the TradingView `postmarket_*` columns, cross-checked against Cboe's own 20:05–21:36 ET prints on 11 names (INTC, AMZN, MDLZ and GOOGL agree to the cent; RDDT, TWLO, RBLX and ATEC differ by 0.1–0.8 points on a different tick).
- **No confirmed catalyst** for nine after-hours movers (ATEC, NPKI, AXG, CYPH, BNC, COHU, ONTO, OSPN, CVEO) and for the largest unconfirmed regular-session gainers (KPLT, PURR, LNG, LHX, NXPI, DASH, HWM, CRH, PWR). These are marked unconfirmed rather than explained.
- **No post-close VIX print.** The only after-hours VIX quote available from a web page is **17.07**, and its change reference shows it was captured Thursday *morning* (pre-session, versus the 16.91 prior close) — not tonight. The volatility numbers in §7 are the official cash close (VIX 17.20, VXN 25.18) and nothing more.
- **The after-hours snapshot is the ~20:05 ET extended close**, not an intraday snapshot. Prints taken at other times differ materially (INTC was −20.64% at 17:39 ET, −21.05% on MarketWatch's board, −23.43% at 19:13 ET on CNBC, −23.03% at the 20:05 close). The ETF after-hours prints are the 20:05 ET extended close; the Cboe 21:14–21:36 ET prints on QQQ and SMH match them exactly.

### Data lineage

```
Cash close (16:00 ET, 2026-10-29)
 ├─ Indices          Cboe _SPX/_NDX/_RUT/_DJX  +  Nasdaq /info COMP & NDX
 ├─ ETFs & sectors   Cboe delayed_quotes  →  validated vs TradingView (24/24) and shibui prior close (18/18)
 ├─ Per-stock        TradingView america/scan  →  validated vs Cboe (24/24 identical closes)
 ├─ After-hours      TradingView postmarket_* (vs the 10/29 close)
 │                    ↳ cross-checked vs Cboe current_price on 11 names (agree to ~1c)
 ├─ Futures          CNBC quote service (22:30 ET)
 ├─ Yields           US Treasury daily yield-curve CSV (official)
 ├─ Volume ratios    TradingView relative_volume_10d_calc + shibui 10-session bars
 ├─ Breadth          TradingView universe (cap > $200M, vol > 100k, n=3,244) + cron #20 EOD file (n=4,899)
 ├─ Put/call         Cboe daily options statistics (10/29 table)
 └─ Context/catalysts  MT Newswires, Investopedia, CNBC, Yahoo Finance, Hargreaves Lansdown,
                       StockTitan, CappNotes, RTTNews, Schwab, Earnings Whispers, MarketWatch,
                       TheStreet, WSJ, Reuters, AP, via web_search / web_fetch
```

**Audit log:** skipped per the Cloud rule (no Windows audit file in this runtime).
