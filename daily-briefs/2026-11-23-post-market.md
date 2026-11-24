---
date: 2026-11-23
cron: 23-agentic-post-market-brief
contract: postmkt-artifact-v2
fire_time_et: 22:30
snapshot_et: 22:30-22:52
session: 466687114649775
scheduled_at_ms: 1795491005706
status: ok
source: MCP-over-HTTP bridge (market-recap: get_quotes, price_history) | TradingView public scanner (tv_scan.py, TV_SCAN_V2) | cron #20 us-eod/2026-11-23.csv | CBOE daily market statistics | CBOE dated index files | web_search
primary_source: bridge market-recap (Yahoo-sourced, not rate-limited)
universe: cron #20 us-eod/2026-11-23.csv — 4,882 names, 4,860 priced (632 rows excluded from the cap-weighted columns)
degraded_sources: 3
---

# Post-market brief — Monday, 23 November 2026

## TL;DR

Jensen Huang came back and the whole market came with him. Nvidia's board reinstated its co-founder as chief executive before the open, and NVDA closed **+31.48% at 165.05** — its biggest single-day gain since May 2003 and roughly a trillion dollars of market value — dragging the S&P 500 up **4.73% to 7,237.17**, the Nasdaq Composite **6.51% to 24,089.56** and the PHLX Semiconductor index **14.03% to 9,588.05**, the best session for the major indices since April 2025. The tape was broad *and* concentrated at once: **advancers 3,939** against **decliners 802** on the 4,860-name cron #20 universe, a **median_name_move_pct of +2.01**, and a **liquid_adv_dec_ratio of 7.95** (1,559 advancers vs 196 decliners above a $2B market-cap floor) — yet the **cap_weight_penalty_bp was +212** (SPY +4.71% vs RSP +2.59%), the second-largest positive reading in the five-session history, because Nvidia alone contributed **+4.88pp** of the sector's **+9.41%** cap-weighted move. Volatility collapsed in the same hour (VIX 26.62, **-25.83%**; VXN 36.31, **-19.76%**), the 10-year yield barely moved (4.918%, +0.6bp), and the Asian leg confirmed it: the **Nikkei 225 +3.97%** (live, stamped 21:35 ET) and the **Kospi +6.12%** (live, stamped 22:12 ET). Two caveats travel with the story. First, the board's decision came with investigations into Nvidia's accounting still open, so a single person's governance is now the market's beta. Second, after a 31% day the after-hours tape is no longer a clean vote: **HPE fell 6.91%** even while raising its FY27 revenue guide to 27–35%, and **Fluence rose 17.37%** on a $6.2B order book in a quarter with a negative gross margin.

## Tomorrow's setup — Tuesday, 24 November 2026

### Futures and the overnight setup

**The overnight is real this time.** Unlike the Friday fire, CME equity-index futures are open: every row below carries `as_of` 22:21–22:23 ET, seven to nine minutes before the fire, and a live Globex session — not a stale settlement.

| Contract | Level | vs prior settle | vs the cash index close |
|---|---|---|---|
| ES=F (S&P 500) | 7,255.75 | +0.02% (settle 7,254.50) | **+0.26%** vs SPX 7,237.17 |
| NQ=F (Nasdaq-100) | 26,762.50 | -0.17% (settle 26,808) | **+0.06%** vs NDX 26,746.10 |
| YM=F (Dow) | 49,678 | 0.00% (settle 49,677) | **+0.17%** vs DJI 49,595.31 |
| RTY=F (Russell 2000) | 2,676.10 | +0.07% (settle 2,674.10) | **+0.24%** vs RUT 2,669.66 |
| ZN=F (10-year note) | 106.766 | +0.01% | 10-year yield 4.918%, +0.6bp |

Both denominators are published because they say different things. Measured against the prior settle the overnight reads as flat; measured against the cash index close — the only comparison that answers "did the overnight extend the session's move?" — the futures are **+0.06% to +0.26%** above the cash close, i.e. the rally was **not** extended overnight, it was **held**. The Globex range for ES was 7,239.50–7,297.75, so the overnight gave back most of its early strength and finished near the top of a modest band. Nothing in the futures says "second leg".

**The Asia cash leg is the bigger overnight signal, and it is the second leg.** These are live prints, each stamped:

| Index | Level | Change | as_of (ET) | Basis |
|---|---|---|---|---|
| Nikkei 225 | 58,675.79 | **+3.97%** | 21:35 | vs the prior close 56,436.65 |
| Kospi | 4,996.71 | **+6.12%** | 22:12 | vs the prior close 4,708.54 |
| Hang Seng | 22,316.26 | -0.30% | 22:17 | vs the prior close 22,383.74 |
| Shanghai Composite | 3,551.50 | +0.35% | 22:17 | vs the prior close 3,538.95 |

Tokyo was closed on Monday 23 November, so the Nikkei print is **Tuesday's session measured against Friday 20 November's close of 56,436.65** — the same close published in the 20 November brief, which is why the two sessions look like one continuous move. The Kospi's **+6.12%** is the strongest leg anywhere in the tape and is a semiconductor-complex move, not a market move: Korea is the most Nvidia-levered equity market in Asia. The Hang Seng is the one Asia index that did not confirm, and it is the one that trades the least AI hardware. **Read the Asia leg as a continuation of the AI trade, not as a broadening.**

### Economic calendar

Tuesday, 24 November (ET):

| Time (ET) | Release | Prior | Consensus |
|---|---|---|---|
| 7:30 PM (Mon) | Japan flash manufacturing / services PMIs (Nov) — published ahead of the Tokyo open | — | — |
| 8:15 | ADP Employment Change, weekly 4-week average | 23.75K | — |
| 8:55 | Redbook retail sales (YoY) | 9.5 | — |
| 9:00 | FHFA House Price Index + Case-Shiller (Sep) | +0.3% MoM / 2.7% YoY | +0.2% MoM |
| 10:00 | CB Consumer Confidence (Nov) | 91.7 | 92.1–92.5 |
| 10:00 | Richmond Fed manufacturing (Nov) | -2 | -2 to -3 |
| 11:30 | 52-week bill ($54B) and 6-week bill ($90B) auctions | 4.29% | — |
| 1:00 | **5-year note auction ($70B)** and 2-year FRN ($28B) | 4.845% | — |
| 4:30 | API weekly crude oil stocks | 5.30M | — |

The 5-year auction at 1:00 PM is the live read: the 10-year ended the session at 4.918%, up only 0.6bp, so the curve is pricing a stable rate into a 4.7% index day. A weak 5-year bid-to-cover would say the equity rally is a positioning event the bond market is not funding. Consumer Confidence at 10:00 is the first soft-data test of the November slowdown — the flash PMIs printed Monday at a four-month low on growth with price pressure cooling — and Richmond Fed is the industrial read that will say whether the +9.41% information-technology move has a manufacturing echo. Fed Richmond President Barkin speaks at a time to be confirmed. **Wednesday 25 November carries the week's heavy prints** — core PCE (Oct), the 3Q GDP second estimate, durable goods and initial claims, plus the 2:00 PM Beige Book; Thursday 26 November is Thanksgiving and the market is closed; Friday 27 November has the preliminary December consumer sentiment and existing home sales.

### Earnings calendar

Vendor calendars disagree on both the count and the names for Tuesday. EarningsWhispers: **37 companies (26 before the open, 11 after the close)**; the same vendor's after-the-close page says 38/12. Digrin: **89 (16 before the open, 9 after the close, 64 time unconfirmed)**. Atlas: **35**. Market Chameleon: **39** for Tuesday alone. Yahoo: **55**. Breakaway: **31**. The roster below is the **intersection of at least two sources**; where the vendors disagree on the EPS estimate, both numbers are shown rather than one being picked.

| Ticker | Company | When | EPS est. (vendor) | Sources |
|---|---|---|---|---|
| ADI | Analog Devices | before the open | 3.92 (Digrin) / 3.90 (OpenCapital) / 3.89 (Atlas) | 3 |
| MDT | Medtronic | before the open | 1.34 (Digrin) / 1.33 (OpenCapital) / 1.33 (Atlas) | 3 |
| DLTR | Dollar Tree | before the open | 0.92 (Digrin) / 0.91 (OpenCapital) / 0.92 (Atlas) | 3 |
| BBY | Best Buy | before the open | 1.50 (Digrin) / 1.49 (OpenCapital) / 1.49 (Atlas) | 3 |
| SJM | J.M. Smucker | before the open | 2.59 (Digrin) / 2.56 (OpenCapital) / 2.56 (Atlas) | 3 |
| KSS | Kohl's | before the open | 0.00 (Digrin) / -0.00 (OpenCapital) / 0.00 (Atlas) | 3 |
| BURL | Burlington Stores | before the open | 1.73 (OpenCapital) / 1.72 (Atlas) | 2 |
| ANF | Abercrombie & Fitch | before the open | 3.08 (OpenCapital) / 3.15 (Atlas) / 3.32 (Breakaway) | 3 |
| DKS | Dick's Sporting Goods | before the open | 1.41 (Digrin) / 1.41 (OpenCapital) | 2 |
| DY | Dycom Industries | before the open | 4.70 (Digrin) / 4.56 (OpenCapital) / 4.57 (Atlas) | 3 |
| DELL | Dell Technologies | **disputed** | 6.75 (Digrin) / 6.62 (OpenCapital) / 6.55 (Atlas) | 3 |
| ADSK | Autodesk | after the close | 3.13 (Digrin) / 3.07 (OpenCapital) / 3.07 (Atlas) | 3 |
| WDAY | Workday | after the close | 2.80 (Digrin) / 2.74 (OpenCapital) / **1.28 (Atlas)** | 3 |
| HPQ | HP Inc. | after the close | 0.76 (Digrin) / 0.75 (OpenCapital) / 0.74 (Atlas) | 3 |
| NTNX | Nutanix | after the close | 0.62 (Digrin) / 0.61 (OpenCapital) / **0.29 (Atlas)** | 3 |
| URBN | Urban Outfitters | after the close | 1.52 (OpenCapital) / 1.53 (Atlas) | 2 |
| AMBA | Ambarella | after the close | 0.32 (Digrin) / 0.31 (OpenCapital) / -0.17 (Atlas) | 3 |
| CLSK | CleanSpark | after the close | -0.23 (Digrin) / -0.35 (OpenCapital) / -0.36 (Atlas) | 3 |
| QFIN | Qfin Holdings | after the close | 3.19 (Digrin) | 2 |

Also appearing in two or more vendors below the sizes above: VIPS, BILI, ITRN, MOV, TITN, EMBC, SHOE, TIGR, BWLP, BZUN, CMBT, VALN, MMED (before the open), and ZS, VREX, GDRX, DRVN, PD, NOAH (after the close or time unconfirmed). **Two disagreements worth naming rather than smoothing over.** Dell's *timing* is not agreed — EarningsWhispers, Digrin and OpenCapital put it after the close, Market Chameleon says before the open — and two EPS estimates are far apart (Workday 2.80 vs 1.28, Nutanix 0.62 vs 0.29). Neither is reconciled here; what is published is the roster and the disagreement.

### News to watch for the top movers

The day's three largest liquid movers were driven by two separate things, and only one of them is a market event.

- **NVDA +31.48% to 165.05** — the board reinstated Jensen Huang as chief executive, president and board member before the open, with the approval of President Trump; the company said the review continues and that investigations into Nvidia's accounting practices are still open, and the US added a cloud company linked to the scandal to the trade blacklist alongside an Alibaba subsidiary. It is Nvidia's fourth-best day since its 1999 listing and its biggest since May 2003; roughly $1 trillion of market value was added in one session.
- **KYMR +30.40% to 150.37** — company news, and a clean one: the BROADEN2 Phase 2b trial of KT-621 in atopic dermatitis met its primary and secondary endpoints with statistically significant improvements versus placebo across all doses, delivering Dupixent-like results at 16 weeks.
- **AXTI +24.37% to 38.02** — no separate company release was sourced; the substrate maker moved with the AI hardware complex on the Huang repricing, and it is one of the names the market used to rebuild the semiconductor leg.

Carried into Tuesday: **DELL +20.46% to 334.91** (server read-across, and it reports tomorrow), **MU +19.04%**, **INTC +16.34%**, **TSM +14.08%**, **MRVL +18.37%**, **ARM +16.08%**, **VRT +12.10%**, **ORCL +12.34%**, **ONTO +12.24%**, **TER +14.10%**, **KLAC +14.96%**, **TSLA +11.46%** — the AI complex, priced as one thing. On the other side **CRWD -8.92% to 208.97**: CrowdStrike beat on Q3 FY27 (revenue $1.583B, +28.3%, non-GAAP EPS $0.34 against a $0.31 consensus) and raised the full-year guide, and in the same release announced the **$43.9B all-stock acquisition of Zscaler** at $260.41 a share, roughly a 34% premium; acquirer shares fell on the deal, and the stock recovered only +1.48% after hours. **KSS -4.72% to 21.20** ahead of its own Tuesday print, and **WLYB** was excluded from the published movers (see `## Source health`).

### Tomorrow's three things to watch

- **DELL — 334.91 close, 338.49 after-hours — reports tomorrow, with the timing itself disputed (after the close at most vendors, before the open at one) and consensus EPS 6.55 to 6.75; after a +20.46% day the guidance is the tell, because the server chain is where the Huang premium has to become a number.**
- **ADI — 378.75 close, 377.60 after-hours — reports before the open with consensus EPS 3.89 to 3.92; it is the first clean read on whether the AI repricing reached industrial analog, since the sector's +9.41% cap-weighted day was 4.88pp of one company.**
- **HPE — 48.02 close, 44.70 after-hours — record Q4 (revenue $14.5B, +50%; server revenue +94.7%) and a raised FY27 revenue guide of 27% to 35%, and the stock still gave it back: if 44.70 holds, the rally's leadership premium is narrower than the index suggests.**

## Day's tape

### Market read

Population: cron #20's `us-eod/2026-11-23.csv` — 4,882 names, 4,860 with a settled close. The liquid set is the 1,770 names with a market cap above $2B.

| metric | value |
|---|---|
| advancers | 3,939 |
| decliners | 802 |
| unchanged | 119 |
| median_name_move_pct | +2.01 |
| cap_weight_penalty_bp | +212 |
| liquid_adv_dec_ratio | 7.95 (1,559 advancers vs 196 decliners, $2B market-cap floor) |

The breadth was genuinely broad — 81% of the universe closed higher and the median name gained 2.01% — but the **magnitude** was not: the cap-weight penalty of **+212bp** says the biggest names outran the median by more than two percentage points, and the penalty flipped from **-166bp** on Friday to **+212bp** today in a single session. That is the same crowd that sold the AI trade hardest last week buying it back harder.

### Cap-weight penalty — 5-day history

| Session | SPY % | RSP % | cap_weight_penalty_bp |
|---|---|---|---|
| 2026-11-17 | -1.02 | -1.45 | +43 |
| 2026-11-18 | -0.31 | -0.15 | -15 |
| 2026-11-19 | -1.96 | -1.76 | -20 |
| 2026-11-20 | -3.64 | -1.98 | -166 |
| 2026-11-23 | +4.71 | +2.59 | +212 |

The penalty has been negative in three of the last five sessions and is now the second-largest positive reading in this window — the crowding is on the other side of the trade.

### Index, ETF and volatility levels

| Instrument | Close | Change | Day range | as_of (ET) |
|---|---|---|---|---|
| S&P 500 | 7,237.17 | +4.73% | 7,152.66–7,295.60 | 16:42 |
| Nasdaq Composite | 24,089.56 | +6.51% | 23,794.96–24,353.65 | 17:15 |
| Dow Jones | 49,595.31 | +3.01% | 49,033.31–49,810.26 | 16:42 |
| Nasdaq-100 | 26,746.10 | +6.86% | 26,386.42–27,018.88 | 17:15 |
| Russell 2000 | 2,669.66 | +3.40% | 2,631.59–2,671.76 | 16:30 |
| PHLX Semiconductor | 9,588.05 | +14.03% | 9,374.83–9,728.12 | 17:15 |
| VIX | 26.62 | **-25.83%** | 15.39–35.08 | 16:15 |
| VXN | 36.31 | **-19.76%** | 26.57–45.25 | 16:15 |
| SPY | 722.29 | +4.71% | 713.54–727.97 | 16:00 |
| QQQ | 651.03 | +7.00% | 641.95–657.50 | 16:00 |
| IWM | 265.74 | +3.56% | 263.00–266.08 | 16:00 |
| DIA | 495.80 | +3.06% | 489.80–497.50 | 16:00 |
| RSP | 212.82 | +2.59% | 210.74–213.27 | 16:00 |
| SMH | 460.18 | +15.03% | 449.64–469.35 | 16:00 |
| GLD | 333.02 | +3.14% | 332.52–338.00 | 16:00 |
| TLT | 81.69 | +0.29% | 81.08–81.71 | 16:00 |

Every index row's `as_of` was date-checked against the fire date. The volatility indices were read from the **dated history** (`price_history`), not from the quote rows, and cross-checked to the cent against CBOE's own dated close files: VIX 26.62 and VXN 36.31 for 2026-11-23 in both — the bridge's own `^VIX` quote row carried a stale prior close of 28.44 (the 19 November close) and a -6.40% change against the correct 35.89 prior close; the published -25.83% comes from the dated history. See `## Source health`.

Put/call (CBOE daily market statistics): **total 0.94**, index 1.21, equity 0.55, ETP 1.13, VIX 0.88, SPX+SPXW+SPXO 1.27, XSP 1.15, KPI binary 0.00, OEX 2.00, MRUT 1.65 — total volume 16,482,450 contracts, open interest 659,637,698, all from one payload. The payload's `selectedDate` reads **2026-11-23**, the fire date. The equity ratio of 0.55 against a total of 0.94 says the call side of the equity complex was the active one on the way up.

### Cross-asset

| Instrument | Level | Change |
|---|---|---|
| US 10-year yield (^TNX) | 4.918% | +0.6bp |
| Gold (Dec future, GC=F) | 3,629.10 | -0.61% vs prior settle 3,651.40 |
| GLD ETF (session close) | 333.02 | +3.14%; extended-hours print 336.03, +0.90% |
| WTI crude (CL=F) | 80.04 | -0.16% vs prior settle 80.17 |
| US dollar index (DXY) | 104.27 | -0.05% |
| Bitcoin | 60,207.01 | -1.64% |
| Nikkei 225 (live, 24 Nov session) | 58,675.79 | +3.97% (21:35 ET stamp) |
| Kospi (live, 24 Nov session) | 4,996.71 | +6.12% (22:12 ET stamp) |
| Hang Seng (live) | 22,316.26 | -0.30% (22:17 ET stamp) |
| Shanghai Composite (live) | 3,551.50 | +0.35% (22:17 ET stamp) |
| FTSE 100 (closed) | 10,480.82 | +1.30% |
| DAX (closed) | 25,337.27 | +2.15% |
| Euro Stoxx 50 (closed) | 6,074.47 | +2.23% |

Gold deserves two numbers, not one blended figure. The December future settled **-0.61%** against its own prior settle of 3,651.40 while the GLD ETF's thin extended-hours book printed **+0.90%** against its own 16:00 close — the ETF's after-hours book is repricing lazily and is not the overnight signal. Rates, the dollar and oil barely moved on a 4.7% index day: this was a re-rating of one sector's risk premium, not a change in the macro discount rate. Bitcoin fell 1.64% — the AI-euphoria tape did not extend to the other risk asset.

### Day's movers

Bridge `market-recap` `get_quotes` as the quote source of record (one source per field); the universe screen is the $2B market-cap floor.

| Ticker | Close | Change | Catalyst |
|---|---|---|---|
| NVDA | 165.05 | +31.48% | board reinstated the co-founder as chief executive before the open; biggest day since May 2003 |
| KYMR | 150.37 | +30.40% | BROADEN2 Phase 2b of KT-621 met primary and secondary endpoints in atopic dermatitis |
| AXTI | 38.02 | +24.37% | AI hardware complex read-across; no separate company release sourced |
| ALAB | 222.12 | +23.16% | connectivity complex read-across; no company news sourced |
| CRDO | 122.46 | +22.63% | connectivity complex read-across; no company news sourced |
| CRWV | 48.33 | +22.32% | neocloud complex read-across; no company news sourced |
| SITM | 438.82 | +21.48% | AI hardware complex read-across; no company news sourced |
| MXL | 50.31 | +21.38% | AI hardware complex read-across; no company news sourced |
| DELL | 334.91 | +20.46% | server read-across ahead of its own report; no company news sourced |
| APLD | 13.82 | +20.28% | neocloud/compute complex read-across; no company news sourced |
| CRWD | 208.97 | -8.92% | $43.9B all-stock acquisition of Zscaler announced with a Q3 beat; acquirer shares fell |
| CLMT | 28.98 | -5.08% | no company news sourced |
| VVX | 71.63 | -4.72% | no company news sourced |
| KSS | 21.20 | -4.72% | ahead of its own Tuesday print; no company news sourced |
| IP | 28.98 | -4.55% | no company news sourced |
| BURL | 235.16 | -4.15% | ahead of its own Tuesday print; no company news sourced |
| ELV | 379.55 | -3.78% | no company news sourced |
| WING | 146.00 | -3.65% | no company news sourced |
| BJ | 101.41 | -3.25% | no company news sourced |

### Watchlist EOD review

Close, day change and day range are the bridge's; the after-hours print is the TradingView scanner's; volume against average is cron #20's relative-volume multiple on its own volume series. Cron #20's universe does not carry the three ETFs, so those cells are `n/a` rather than a guess.

| Ticker | Close | Day change | Day range | Volume vs avg | After-hours print |
|---|---|---|---|---|---|
| AAPL | 349.08 | +1.90% | 345.44–352.60 | 0.83x | 349.70, +0.18% |
| MSFT | 492.50 | +1.65% | 492.02–509.15 | 0.84x | 492.60, +0.02% |
| NVDA | 165.05 | +31.48% | 156.93–171.50 | 3.36x | 166.79, +1.05% |
| GOOGL | 282.10 | +6.34% | 275.36–285.14 | 1.10x | 284.75, +0.94% |
| AMZN | 255.39 | +3.47% | 251.25–262.48 | 0.97x | 257.00, +0.63% |
| IWM | 265.74 | +3.56% | 263.00–266.08 | n/a | 266.12, +0.14% |
| GLD | 333.02 | +3.14% | 332.52–338.00 | n/a | 336.03, +0.90% |
| TLT | 81.69 | +0.29% | 81.08–81.71 | n/a | 81.61, -0.10% |

The watchlist confirms the shape of the day: the mega-cap core rose, but NVDA alone carried the volume (3.36x its average while AAPL and MSFT traded below theirs), and the after-hours prints are a fraction of a percent — the tape is not extended, it is held. IWM at +3.56% and the small-cap leg at +0.14% after hours say the rally was not a beta event.

## Sector rotation

Cap-weighted on one row per `cap_source_symbol`, keeping the non-`CAP_CARRIED` listing and dropping `EX_DISTRIBUTION`, `NO_CAP` and `NO_SECTOR` rows (632 of 4,882 rows excluded; 4,250 rows priced into the columns). Each sector is cross-checked against its own ETF, and where the gap exceeds ~0.5pp the constituent effect is named and the sector is published with and without it.

| Sector | Cap-weighted % | Median % | n | Sector ETF | ETF % | Gap | Largest constituent | Sector ex-constituent |
|---|---|---|---|---|---|---|---|---|
| Information Technology | **+9.41%** | +6.21 | 505 | XLK | +8.97 | +0.44 | NVDA +31.52% | **+5.36%** |
| Communication Services | **+5.21%** | +1.98 | 158 | XLC | +3.57 | +1.64 | GOOGL +6.33% | **+3.99%** |
| Consumer Discretionary | **+4.61%** | +2.29 | 387 | XLY | +3.97 | +0.64 | TSLA +11.48% | **+2.96%** |
| Industrials | +4.20% | +3.99 | 550 | XLI | +3.90 | +0.30 | SPCX +4.38% | +4.15% |
| Materials | +4.01% | +3.97 | 155 | XLB | +3.23 | +0.78 | SCCO +6.94% | +3.76% |
| Financials | +2.11% | +1.16 | 1,171 | XLF | +1.98 | +0.13 | JPM +2.00% | +2.12% |
| Health Care | +1.73% | +3.34 | 831 | XLV | +1.23 | +0.50 | LLY +1.41% | +1.79% |
| Utilities | +1.54% | +0.77 | 80 | XLU | +1.48 | +0.06 | CEG +6.02% | +1.25% |
| Real Estate | **+1.19%** | +1.35 | 189 | XLRE | +1.04 | +0.15 | EQIX +3.22% | +1.06% |
| Consumer Staples | **+0.10%** | +0.24 | 147 | XLP | -0.09 | +0.19 | WMT +1.25% | -0.29% |
| Energy | **-0.97%** | +0.34 | 184 | XLE | -1.06 | +0.09 | WMB +1.74% | -1.05% |

Top three: Information Technology, Communication Services, Consumer Discretionary. Bottom three: Energy, Consumer Staples, Real Estate.

**The rotation was one sector, not a rotation.** Information Technology's +9.41% is a Nvidia story: NVDA alone contributed **+4.88pp**, and without it the sector's cap-weighted move was **+5.36%** — a good day, but half the headline. Communication Services shows the same signature with a 1.64pp gap against XLC: Alphabet contributed **+3.30pp** and the sector ex-Alphabet was **+3.99%**, in line with its ETF. Consumer Discretionary's gap is Tesla: ex-Tesla the sector was **+2.96%** against XLY's +3.97%. Energy was the only sector to close lower on a day when the median stock rose 2.01% — its median name was still **+0.34%**, so the loss is concentrated in the majors, not in the sector's breadth.

## After-hours movers

The contract screen: `type in [stock, dr]`, market cap above $1B, after-hours volume above 50,000 shares, pulled twice (descending and ascending on `postmarket_change`) through the validated client. Every row passed the identity check `postmarket_change == (postmarket_close − close) / close × 100` and the venue check, and every print above +3% was confirmed against the primary listing on the bridge. `gap_fill_level` follows the fixed rule — the prior close when the after-hours range brackets it, otherwise the after-hours midpoint; here every row's range brackets its prior close, so the level is the prior close.

| ticker | prior_close | ah_last | ah_high | ah_low | ah_volume | gap_pct | ah_range_pct | gap_fill_level |
|---|---|---|---|---|---|---|---|---|
| LOAR | 63.50 | 68.46 | 68.46 | 63.50 | 192,861 | +7.82 | 7.82 | 63.50 |
| TDG | 1,140.33 | 1,225.00 | 1,225.00 | 1,126.86 | 94,047 | +7.43 | 8.61 | 1,140.33 |
| A | 176.04 | 188.00 | 193.50 | 176.04 | 624,560 | +6.79 | 9.92 | 176.04 |
| SVM | 6.96 | 7.37 | 7.37 | 6.96 | 117,367 | +5.95 | 5.95 | 6.96 |
| AMRC | 22.03 | 23.17 | 23.17 | 22.03 | 75,095 | +5.17 | 5.17 | 22.03 |
| HPE | 48.02 | 44.70 | 52.05 | 43.67 | 8,830,412 | -6.91 | 17.45 | 48.02 |
| USFD | 109.11 | 102.00 | 109.11 | 102.00 | 288,612 | -6.52 | 6.52 | 109.11 |
| ZLAB | 22.23 | 21.00 | 22.23 | 21.00 | 61,221 | -5.53 | 5.53 | 22.23 |
| CRCT | 8.74 | 8.26 | 8.74 | 8.26 | 146,106 | -5.49 | 5.49 | 8.74 |
| NWN | 51.08 | 48.60 | 51.08 | 48.60 | 73,193 | -4.85 | 4.85 | 51.08 |

**The screen's floor hides the session's leader.** The table keeps names above $1B of market cap; the same screen pulled without that floor shows the actual after-hours leaderboard: **FLNC +17.37%** (Fluence Energy, ~$701M market cap, 4.46 after hours on 2.54M shares, a 27.37% after-hours range — the earnings name, published below), **APUS +39.33%** and **AKAN +28.68%** (sub-$10M caps, not tradable in any meaningful size), and on the downside **SCAG -31.81%**, **GMEX -28.72%** and **ABTS -23.93%**. The reader should treat the table above as the liquid after-hours tape, not as the whole of it.

**Two vendor disagreements on the after-hours tape are named rather than blended.** The scanner's print is the source of record and is a snapshot as of the fire; the tape was still moving while this brief was written. **TDG** is the one to watch: the scanner carries a **single print** at 1,225.00 (its after-hours high and low are the same) against a 1,140.33 prior close, while Benzinga's 16:45 ET print was **1,126.86, -1.18%** — a materially different number for the same field. Treat the 1,225.00 as an observation, not as a confirmed level, until the book proves it. **LOAR** is corroborated: Yahoo and Benzinga independently carried 68.46, +7.82% at 16:29 ET.

## After-hours earnings reactions

- **HPE -6.91% to 44.70 after hours** — the most consequential reaction of the night. Q4 FY26 (quarter ended 31 October) revenue was **$14.5B, +50%**, Cloud & AI revenue **$11.3B, +68.6%**, server revenue **$8.8B, +94.7%**, AI orders of $5.7B booked in the quarter and $12.4B year to date, GAAP diluted EPS **$1.26**, and the board added **$5B** to the buyback authorisation. The company **raised** FY27 revenue growth to **27–35% ($59.4–63.1B)** and FY27 free cash flow to at least **$5.5B**. The stock had already closed **+17.38% at 48.02** on the AI rebound, and the after-hours book took it back to 44.70 with a 17.45% range. A raise was not enough for a name that had already run.
- **Agilent +6.79% to 188.00 after hours** — Q4 FY26 revenue **$2.04B, +9.6% reported and +8.3% core**, non-GAAP EPS **$1.86 (+17%)** against a $1.72 consensus, non-GAAP operating margin 30.0%, and an initiated FY27 guide of **$8.00–8.15B revenue and $6.73–6.86 non-GAAP EPS**. The beat was on core growth (210bp above the high end of guidance) but the FY27 core midpoint of 5–7% is below the exit rate, which is why the reaction was a strong one and not a limit-up.
- **FLNC +17.37% to 4.46 after hours** — Fluence Energy's FY26 results: order intake **above $6.2B** for the year including **$3.5B in Q4**, backlog **~$8.9B**, against Q4 revenue of **$744.1M** versus $1,041.9M a year earlier, GAAP gross margin of **-5.0%** and a Q4 net loss of **$137.8M** (adjusted EBITDA -$112.0M). The market bought the order book and ignored the margin. The call is at 08:30 ET on Tuesday.
- **CRWD +1.48% to 212.07 after hours** — the -8.92% regular-session fall (to 208.97) was the deal, not the quarter: the $43.9B all-stock Zscaler acquisition announced with a Q3 beat and a raised FY27 guide. Acquirer shares fell on the announcement and stabilised after hours.
- **SMTC -4.61% to 99.33** (after-hours range 91.23–112.78, 20.69% of the prior close — the widest range in the table) and **CENT -5.36% to 42.05** were the two notable post-earnings fades among the 23 November reporters; **AMTM +4.99% to 21.68**, **J -2.04% to 154.32**, **SYM -0.23% to 34.89** (after-hours low 31.10) and **ZM -0.56% to 85.55** were the rest of the after-close cohort's reaction. KSS, which reports Tuesday, rose **+4.25% to 22.10** after hours after closing -4.72%.

## Open research queue

1. **Is the Huang reinstatement durable, and what does it cost Nvidia?** Nvidia's board reinstated its co-founder as chief executive less than two weeks after removing him, with the review continuing and investigations into the company's accounting practices still open; the US has blacklisted a cloud company linked to the scandal. Why it matters: Nvidia contributed **+4.88pp of the +9.41%** cap-weighted information-technology move, so the market's beta for two consecutive sessions rests on one person's governance status, and the accounting question is unresolved rather than closed. What would resolve it: the outcome of the internal review and any charge the accounting investigation produces, and whether the October quarter's 103% revenue growth converts into cash.
2. **Is the breadth real or is this a squeeze?** The tape was broad — 3,939 advancers, a +2.01% median name, a 7.95 liquid advance/decline ratio — yet the equal-weight index lagged the cap-weighted one by **212bp**, and the technology sector ex-Nvidia was +5.36% rather than +9.41%. Why it matters: if the equal-weight index keeps lagging by more than two percentage points while the median name rises, the rally is a concentration trade wearing a breadth costume, and the next shock reverses in the same proportion. What would resolve it: Wednesday's core PCE and the GDP second estimate for the equal-weight index's follow-through, and the five-session penalty history's own path.
3. **Who is actually funding the AI capex?** HPE guided FY27 revenue up 27–35% with server revenue up 94.7% and still fell 6.91% after hours; Fluence booked $6.2B of orders and rose 17.37% on a quarter with a negative gross margin; Agilent beat and rose 6.79%. Why it matters: if the suppliers cannot hold a good print, the capex story is sentiment rather than a spending cycle, and the 5-year note auction at 13:00 ET will show whether anyone is financing it. What would resolve it: tomorrow's Dell and Analog Devices prints, and the 5-year auction's bid-to-cover against the 4.845% prior yield.

## Source health

| Source | URL / query | Status | What it changed |
|---|---|---|---|
| Bridge `market-recap` `get_quotes` | 5 batched calls of ≤40 symbols: indices/ETFs (16), futures (7), Asia & macro (9), movers (40 + 40 + 40) | ok, **one row degraded** | quote source of record; every index row's `as_of` date-checked against the fire date. The `^VIX` row carried a **stale prior close of 28.44** (the 19 November close) and a -6.40% change; the published -25.83% was read from the dated history instead and the row's own 15.39–35.08 range is what the index actually printed |
| Bridge `market-recap` `price_history` | SPY, RSP, ^VIX, ^VXN, 2026-11-09 to 2026-11-23 | ok | the cap-weight penalty 5-session history and the dated volatility closes |
| TradingView scanner (validated client `tv_scan.py`, marker TV_SCAN_V2) | 6 scans: after-hours up/down at a $1B floor, the same screen without the floor, a targeted watchlist pull, a targeted 65-name pull (earnings roster + watchlist + movers) | ok, **one row degraded** | the after-hours levels; the watchlist prints. The **TDG** row is a **single print** at 1,225.00 that conflicts with Benzinga's 16:45 ET print of 1,126.86 (-1.18%); the scanner's print is published as the source of record and the disagreement is named rather than blended |
| CBOE daily market statistics | `https://www.cboe.com/us/options/market_statistics/daily/` | ok | total put/call 0.94; the payload's `selectedDate` reads **2026-11-23**, the fire date — no degradation this run |
| CBOE dated index closes | `cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv`, `VXN_History.csv` | ok | cross-check of the VIX and VXN closes to the cent (26.62 and 36.31) |
| cron #20 EOD universe | `karizaco/minimax-cloud-outputs` `us-eod/2026-11-23.csv` (4,882 rows) | ok, **degraded** | the participation population, the sector taxonomy and the de-duplication keys. Two row-level defects: **WLYB** is flagged `CAP_CARRIED|RANGE_ADJUSTED|NO_HISTORY|SPLIT_ADJUSTED` with `settle_status=UNCONFIRMED`, and the bridge's own WLYB quote row carried a stale `as_of` of 2026-11-19 — **WLYB was therefore excluded from the published movers** rather than published on either source. **DELL** is flagged `settle_status=UNCONFIRMED` and its CSV close (335.90) differs from the bridge's 334.91, so DELL's published close and change are the bridge's. NVDA's row is flagged `PRIOR_CLOSE_SUPERSEDED`; its change (+31.52%) and close (165.10) agree with the bridge's 165.05 to within 0.03% |
| Watchlist | `refs/watchlist.yaml` on the outputs repo | ok | 8 names, published as the watchlist EOD review |
| `web_search` | the Huang reinstatement, the HPE/Agilent/Fluence/CrowdStrike results, tomorrow's earnings and economic calendars, the vendor counts | ok | catalysts and calendars; the vendor disagreements are disclosed in `### Earnings calendar` rather than resolved by preference |

**Degraded sources: 3** — (1) the bridge `get_quotes` call, whose `^VIX` row carried a stale prior close and whose `WLYB` row carried a 2026-11-19 `as_of` (both corrected or excluded, and named above); (2) the TradingView after-hours screen, whose `TDG` row is a single print that conflicts materially with another vendor's print for the same field; (3) cron #20's universe CSV, whose `WLYB` and `DELL` rows forced one published mover number to be taken from the bridge and another to be excluded. The absent `mcp__*` tool names are not a degraded source; the bridge reached its server over plain HTTPS JSON-RPC throughout (5 calls, all batched).

## Method notes

- **The fire is a Monday fire.** `scheduled_at_ms` 1795491005706 resolves to 2026-11-23 22:30 ET; the next session is Tuesday 24 November. Unlike the previous Friday fire, the CME equity-index week is open, so the futures numbers above are a live overnight setup rather than a settlement, and every futures row's `as_of` (22:21–22:23 ET) was checked against the fire before it was called an overnight.
- **The overnight has two legs and both are published.** The futures leg is judged on the cash-close comparison (the prior-settle comparison is published beside it), and the Asia leg is published as live, stamped prints rather than as a session close. Tokyo's exchange was closed on 23 November, so the Nikkei change is measured against Friday's close; the Hang Seng, which trades the least AI hardware, did not confirm the move.
- **One source per field.** Prices, changes and levels come from the bridge `market-recap`; the TradingView scanner supplies the extended-hours prints; cron #20's CSV supplies the participation population, the sector classification, the relative-volume multiples and the de-duplication keys (its taxonomy is carried forward, its moves and caps are not used for the published mover table); CBOE supplies the put/call ratio and the dated volatility closes. Where two sources disagree by more than 0.6% the bridge wins and the other is named above.
- **Cap-weighted columns** use one row per `cap_source_symbol`, keep the non-`CAP_CARRIED` listing, and drop `EX_DISTRIBUTION`, `NO_CAP` and `NO_SECTOR` rows (632 rows excluded, 4,250 priced into the columns). Every published cap-weighted return was asserted inside ±20% before publication, and each sector was cross-checked against its ETF with the gap published; the three sectors with a gap above ~0.5pp are published with and without their largest constituent.
- **After-hours rows** were accepted only after passing the identity check and a venue check; no row's venue was outside a major US exchange, and every print above +3% was confirmed against the primary listing on the bridge. `gap_fill_level` follows the fixed rule. The print is a snapshot as of the fire and the tape was still moving while the brief was written.
- The put/call components published above all come from the same CBOE payload and reconcile with the total; no component split was invented across sources.
- Read-only. No trades, no positions, no advice.
