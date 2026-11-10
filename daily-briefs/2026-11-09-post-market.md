---
date: 2026-11-09
cron: 23-agentic-post-market-brief
contract: postmkt-artifact-v2
fire_time_et: 22:30
snapshot_et: 22:22-22:36
session: 461736165777543
scheduled_at_ms: 1794281421526
status: ok
source: MCP-over-HTTP bridge (market-recap: get_quotes, price_history); TradingView public scanner; cron #20 us-eod/2026-11-09.csv; watchlist.yaml; BLS; Cboe; issuer IR and press
primary_source: MCP-over-HTTP bridge, pack market-recap (keyless, Yahoo-sourced)
universe: cron #20 us-eod/2026-11-09.csv - 4,895 rows, 4,563 after share-class de-duplication and EX_DISTRIBUTION drops
degraded_sources: 3
---

# Post-market brief — Monday, 9 November 2026

## TL;DR

The S&P 500 closed **+2.35% at 7,549.94** — its best day since 8 April — recovering most of last week's AI-data-centre washout, with semis leading (SOX +6.85%) and crude down about 5.75% in the regular session doing most of the work. The rally was genuinely broad, not a mega-cap squeeze: **3,483 advancers against 865 decliners and 215 unchanged** across 4,563 names, **median_name_move_pct +1.76%**, and **liquid_adv_dec_ratio 6.69** in the $2B-and-up set. The cap-weight spread was a rounding error by comparison — SPY +2.37% against RSP +2.27% is only a **+10bp cap_weight_penalty_bp**, the narrowest reading in five sessions. The one crack in the tape was Nvidia at **-4.23%** on an investigation into its chief executive, and the tape still paid for it: VIX collapsed 22.31% to 19.92.

## Tomorrow's setup — Tuesday, 10 November 2026

### Futures and the overnight setup

The bridge's futures rows carry `as_of` 2026-11-10 03:22Z (22:22 ET) — eight minutes before this fire, so **this is the live Globex move, not a stale settlement**. The overnight is flat, and that is the point: nothing has priced the 08:30 ET CPI print yet.

| Contract | Last | Change | Prior settle | as_of (ET) |
|---|---|---|---|---|
| ES=F | 7,581.25 | +0.09% | 7,574.25 | 22:22 |
| NQ=F | 27,976.25 | -0.14% | 28,014.50 | 22:22 |
| YM=F | 52,656.00 | +0.30% | 52,498.00 | 22:22 |
| RTY=F | 2,851.20 | +0.09% | 2,848.70 | 22:22 |
| ZN=F | 107.0313 | -0.03% | 107.0625 | 22:22 |

Read-through: S&P futures sit **7.2 points above** the cash close and Nasdaq futures **10.2 points below** it. The overnight is a pause, not a continuation — with CPI at 08:30 ET, the index open is a binary on the print, not on the futures.

### Economic calendar

| Time (ET) | Release | Consensus | Previous |
|---|---|---|---|
| 04:00 | Fed Governor Waller speaks | — | — |
| 06:00 | NFIB small business optimism, October | — | — |
| **08:30** | **CPI, October** | **0.3% m/m; 3.9% y/y** | 0.6% m/m; 3.7% y/y |
| **08:30** | **Core CPI, October** | **0.2% m/m; 2.8% y/y** | 0.3% m/m; 2.6% y/y |
| 08:30 | CPI index, n.s.a. | 337.02 | 336.94 |
| 08:30 | Real earnings, October | — | -0.5% |
| 09:35 | Fed President Logan speaks | — | — |
| 12:00 | WASDE crop report | — | — |
| 13:00 | 10-year note auction | — | — |
| 13:30 | Fed President Schmid speaks | — | — |
| 15:30 | Fed Vice Chair Bowman speaks | — | — |

Sources: BLS release schedule (bls.gov/schedule/2026/11_sched_list.htm), Macro Bullseye and Investing.com calendars. PPI follows on Friday 13 November.

### Earnings calendar

- **CoreWeave (CRWV) — after the close Tuesday, call at 17:00 ET.** Consensus is a loss of **$1.45** per share against a $0.31 loss a year ago, on revenue of roughly **$3.54B** (Moomoo/Nasdaq). This is the single name the whole chip complex is trading against tomorrow: today's SOX +6.85% is a bet on AI-compute demand that CoreWeave's capex line confirms or breaks.
- 147 companies report Tuesday (58 before the open, 89 after the close, per Earnings Whispers). Named before the open: TransDigm, Sea Limited, Vodafone. Named after the close: CoreWeave, Petrobras, Alcon, Embraer.
- **None of the eight watchlist names has a confirmed 10 November report date** in the sources read tonight. AAPL, MSFT, NVDA, GOOGL and AMZN all carry `earnings_flag: true` on the published watchlist, but no confirmed date lands tomorrow.
- Forward: Cisco and Applied Materials report Thursday 12 November; Praxis hosts its Investor Day the same morning at 08:00 ET.

### News to watch for the top movers

- **FRVO +26.09% to 11.38** — Fervo Energy's Q3 landed before the open: a loss of $0.07 per share against a $0.10 consensus, plus a **15-year, 396MW power purchase agreement with Google** and a 600MW expansion option taking the partnership toward a gigawatt. Binding contracted revenue jumped to about **$11.9B** from $7.2B at June-end, and Cape Station GeoBlock 1 was declared commercial operation on 30 September, a month ahead of its contractual date. Second-half capex guidance was trimmed to $700–750M from $850–900M as spend shifted later. An investor open house at the site is set for 19 November.
- **PRAX +19.96% to 332.97** — Praxis Precision Medicines narrowed its Q3 loss to **$3.23** per share against a $3.52 FactSet consensus, and both of its FDA files survived the day: relutrigine's PDUFA action date of 27 December 2026 and ulixacaltamide's of 29 January 2027. Cash of about **$1.3B** funds the company into 2028. The company presented at the Guggenheim Healthcare Innovation Conference today and hosts its Investor Day on 12 November.
- **WRBY +18.56% to 30.21** — Warby Parker printed a new 52-week high. No company-specific release turned up in tonight's sources; treat the move as a momentum print rather than a catalyst-driven one.

### Tomorrow's three things to watch

- SANM — 149.64 gap-fill level, 186.96 after-hours high — Q4 adjusted EPS of $4.43 against a $3.27 estimate; the fiscal 2027 guide of $15.50–17.50 is what the open has to digest.
- CRWV — 48.98 close, 45.15 session low — reports after Tuesday's close; consensus is a $1.45 loss on about $3.54B of revenue, and the capex guide is the real tell.
- TLT — 81.96 close — CPI at 08:30 ET is the catalyst, with consensus at 0.3% m/m and 3.9% y/y against a 4.864% 10-year yield.

## Day's tape

### Market read

| metric | value | source |
|---|---|---|
| advancers | 3,483 | cron #20 us-eod/2026-11-09.csv (4,563 names after de-duplication) |
| decliners | 865 | same |
| unchanged | 215 | same |
| median_name_move_pct | +1.76% | same, `change_pct` |
| cap_weight_penalty_bp | +10 | bridge `price_history`, SPY +2.37% vs RSP +2.27% |
| liquid_adv_dec_ratio | 6.69 (1,399 : 209) | same CSV, market_cap >= $2B (n=1,624) |

The participation read is the headline, not the index: 80% of the universe closed higher, the median name gained 1.76%, and the liquid set advanced 6.7 names for every decliner. The +10bp cap-weight penalty is the smallest of the last five sessions and says the rally was not a mega-cap squeeze — the median name did the work.

### Cap-weight penalty — 5-day history

| Session | SPY % | RSP % | cap_weight_penalty_bp |
|---|---|---|---|
| 2026-11-03 | +0.30 | -0.33 | +63 |
| 2026-11-04 | +1.65 | +1.86 | -20 |
| 2026-11-05 | -4.41 | -2.89 | -152 |
| 2026-11-06 | +0.31 | -0.38 | +69 |
| 2026-11-09 | +2.37 | +2.27 | +10 |

The three-session sequence that ended on 6 November was violent in both directions; today's +10bp is the first sign of the equal-weight index catching up.

### Index, ETF and volatility levels

| Instrument | Close | Change | Previous close | Day range | Volume |
|---|---|---|---|---|---|
| S&P 500 | 7,549.94 | +2.35% | 7,376.86 | 7,422.24 – 7,577.39 | 3,554,608,000 |
| Nasdaq Composite | 25,253.14 | +2.74% | 24,579.40 | 24,762.57 – 25,354.30 | 8,069,510,000 |
| Dow Jones | 52,389.75 | +2.15% | 51,285.73 | 51,643.01 – 52,574.34 | 811,284,523 |
| Russell 2000 | 2,840.81 | +3.15% | 2,754.11 | 2,784.04 – 2,852.68 | n/a (index) |
| Nasdaq 100 | 27,907.63 | +3.40% | 26,990.00 | 27,227.53 – 28,025.77 | 1,813,321,000 |
| PHLX Semiconductors | 10,033.93 | +6.85% | 9,390.25 | 9,467.26 – 10,116.64 | n/a (index) |
| VIX | 19.92 | -22.31% | 25.64 | 19.64 – 25.08 | n/a (index) |
| VXN | 29.11 | -14.43% | 34.02 | 29.11 – 32.34 | n/a (index) |
| SPY | 752.69 | +2.37% | 735.29 | 741.09 – 755.42 | 48,888,639 |
| QQQ | 679.35 | +3.54% | 656.10 | 662.02 – 681.70 | 54,176,627 |
| IWM | 282.51 | +3.23% | 273.67 | 276.81 – 283.79 | 28,487,908 |
| DIA | 523.33 | +2.17% | 512.22 | 517.24 – 525.17 | 3,414,019 |
| RSP | 220.95 | +2.27% | 216.05 | 217.67 – 221.90 | 11,692,171 |
| SMH | 487.41 | +5.05% | 463.96 | 462.88 – 490.47 | 14,596,565 |
| GLD | 379.53 | +1.88% | 372.52 | 375.68 – 380.18 | 7,330,193 |
| TLT | 81.96 | +0.05% | 81.92 | 81.82 – 82.28 | 28,888,963 |

Three of the three major averages rose more than 2% on the same day for the first time since 5 April. VXN is stamped 12:54 ET, not the 16:00 ET close — see `## Source health`.

### Cross-asset

| Asset | Last | Change | as_of (ET) |
|---|---|---|---|
| 10-year yield (^TNX) | 4.864% | +0.1% | 15:59 |
| 5-year yield (^FVX) | 4.659% | +0.24% | 15:59 |
| 3-month bill (^IRX) | 4.035% | +0.88% | 15:59 |
| WTI crude (CL=F) | 85.79 | -1.22% | 22:22 (overnight, vs 87.01 settle) |
| Gold (GC=F) | 4,123.70 | +0.22% | 22:22 |
| Dollar index | 101.691 | +0.04% | 22:22 |
| EUR/USD | 1.1225 | +0.06% | 22:32 |
| USD/JPY | 157.993 | +0.06% | 22:32 |
| Bitcoin | 74,539.58 | -0.95% | 22:32 |

The oil move is the spine of the session: Brent fell about 5.8% and WTI settled near 87.01, down roughly 4.2%, which is what lifted the industrials and small caps, and it kept going lower overnight to 85.79. The long end barely moved — the 10-year at 4.864% is effectively unchanged despite a 2.35% equity day, and TLT was flat at +0.05%, so this was a risk-on move built on cheaper energy, not on a dovish rates repricing. That matters tomorrow: with CPI due at 08:30, rates are the untouched variable.

### Day's movers

| Ticker | Close | Change | Rel. volume | Sector |
|---|---|---|---|---|
| FRVO | 11.38 | +26.09% | 2.63 | Utilities |
| PRAX | 332.97 | +19.96% | 2.22 | Health Care |
| WRBY | 30.21 | +18.56% | 3.25 | Consumer Discretionary |
| FLY | 24.31 | +17.10% | 2.40 | Industrials |
| COHR | 225.20 | +16.74% | 1.77 | Information Technology |
| ACAD | 16.50 | -22.28% | 5.76 | Health Care |
| IONS | 31.00 | -21.36% | 6.88 | Health Care |
| IBRX | 7.11 | -17.66% | 3.24 | Health Care |
| ARWR | 49.24 | -15.34% | 4.67 | Health Care |
| HIMS | 22.94 | -11.77% | 4.44 | Health Care |

The top of the tape is idiosyncratic and mostly company-specific: Fervo's Google geothermal contract, Praxis's narrower loss, Warby Parker's new 52-week high. The bottom is a single-sector event — five of the five worst liquid names were health care, and four of them traded on multiples of normal volume. Ionis cut full-year revenue guidance for a flagship drug by about half, overshadowing otherwise solid results, and Acadia made a new 52-week low with no company-specific cause disclosed. Hims missed on the bottom line ($0.17 against a $0.29 estimate). Notably, the whole health-care complex fell while the median name rose 1.76% — dispersion, not a broad risk-off.

### Watchlist EOD review

| Ticker | Close | Change | Day range | Volume | Rel. vol | After-hours |
|---|---|---|---|---|---|---|
| AAPL | 350.70 | +2.42% | 344.80 – 352.30 | 46,934,095 | 1.05 | 350.40 (-0.08%) |
| MSFT | 545.20 | +2.75% | 538.70 – 548.30 | 25,210,709 | 1.05 | 543.79 (-0.26%) |
| NVDA | 178.70 | **-4.23%** | 170.20 – 179.90 | 455,146,828 | 3.94 | 180.50 (+1.02%) |
| GOOGL | 288.10 | +1.16% | 288.10 – 296.30 | 36,009,408 | 1.06 | 290.13 (+0.69%) |
| AMZN | 266.90 | +2.93% | 266.90 – 275.30 | 50,438,489 | 1.14 | 267.05 (+0.05%) |
| IWM | 282.51 | +3.23% | 276.81 – 283.79 | 28,487,908 | — | 282.08 (-0.15%) |
| GLD | 379.53 | +1.88% | 375.68 – 380.18 | 7,330,193 | — | 377.85 (-0.44%) |
| TLT | 81.96 | +0.05% | 81.82 – 82.28 | 28,888,963 | — | 81.84 (-0.15%) |

Source: cron #20's us-eod CSV for the five equity names and the bridge for the three ETFs (ETFs are outside the EOD universe); after-hours prints from the TradingView scanner. Nvidia is the one that matters: it opened at 173.00, washed to 170.20, and closed at 178.70 on 3.9x normal volume — a full recovery from the session low but still 4.23% down, on reports that the company's chief executive is under investigation over his relationship with a woman suspected of being a Chinese spy. It is now the largest single drag on the tape and, judging by the semis' behaviour, the reason SOX needed to print 6.85%.

## Sector rotation

| Sector | Cap-weighted % | Median % | Sector ETF | ETF % | Gap (pp) | Largest contributor |
|---|---|---|---|---|---|---|
| Industrials | +4.48 | +3.99 | XLI | +3.82 | +0.66 | SPCX +5.81% (contributes +1.27pp) |
| Information Technology | +3.26 | +3.69 | XLK | +3.73 | -0.47 | AVGO +8.78% (contributes +0.53pp) |
| Consumer Discretionary | +3.15 | +2.89 | XLY | +2.92 | +0.23 | — |
| Energy | +0.60 | +1.13 | XLE | +0.52 | +0.08 | MPC +4.62% |
| Consumer Staples | +0.72 | +2.08 | XLP | +0.90 | -0.19 | — |
| Financials | +0.99 | +0.95 | XLF | +1.45 | -0.47 | BX +3.85% |

The Industrials gap of +0.66pp is a constituent effect, not a rotation: Space Exploration Technologies (SPCX, $1.93T cap) alone contributed +1.27pp, and the sector ex-SPCX prints +4.11% against XLI's +3.82% — a gap of +0.29pp, inside tolerance. Below the leaders, Energy at +0.60% cap-weighted is the day's laggard even though its median name did better (+1.13%); the sector is being dragged by the largest refiner names, and the whole group sat on the wrong side of the oil move. Financials at +0.99% is a laggard for the opposite reason — the equity move was a rotation out of value, not into it.

## After-hours movers

The screen is the TradingView extended-hours screen with a $1B market-cap floor and a 50,000-share after-hours volume floor (2,144 names matched). Every row carries the full level set; `gap_fill_level` is the prior close where the after-hours range brackets it, otherwise the after-hours midpoint.

| ticker | prior_close | ah_last | ah_high | ah_low | ah_volume | gap_pct | ah_range_pct | gap_fill_level | catalyst |
|---|---|---|---|---|---|---|---|---|---|
| SANM | 149.64 | 179.8776 | 186.96 | 149.64 | 286,405 | +20.21% | 24.94% | 149.64 | Q4 adjusted EPS $4.43 vs $3.27 estimate; FY27 guide $15.50–17.50 |
| HROW | 27.47 | 31.81 | 32.23 | 26.4801 | 205,285 | +15.80% | 20.93% | 27.47 | Q3 EPS $0.25 vs $0.22; FY26 EBITDA guidance cut to >$40M from $80–100M |
| AAON | 62.87 | 72.57 | 73.38 | 62.87 | 284,253 | +15.43% | 16.72% | 62.87 | Record Q3 and higher FY26 outlook, but Q1/Q2 restated and a material weakness disclosed |
| SECZ | 6.97 | 7.88 | 8.17 | 6.97 | 550,349 | +13.06% | 17.22% | 6.97 | Q2 loss of $0.03 per share against a $0.41 estimate; revenue $17.4M vs $18.6M |
| KLRA | 13.70 | 14.90 | 14.98 | 13.70 | 190,823 | +8.76% | 9.34% | 13.70 | No company-specific release found in tonight's sources |
| APPS | 11.30 | 8.37 | 11.52 | 7.75 | 2,205,391 | -25.93% | 33.36% | 11.30 | Revenue $166.6M vs a $178.7M estimate and EPS $0.17 vs $0.18, despite a return to GAAP profit |
| BMO | 174.08 | 142.385 | 174.08 | 142.385 | 282,578 | -18.21% | 18.21% | 174.08 | Single print at the session low, no catalyst found; BMO's own Q4 is not due until 2 December |
| WGS | 65.72 | 58.70 | 65.81 | 54.80 | 350,783 | -10.68% | 16.75% | 65.72 | Beat: EPS $0.28 vs $0.07 and revenue $123.1M above consensus, FY26 revenue guidance reaffirmed |
| TNDM | 18.17 | 16.60 | 18.17 | 16.60 | 323,472 | -8.64% | 8.64% | 18.17 | Single print at the session low; the company reported on 5 November, not tonight |
| QLYS | 202.46 | 188.00 | 202.95 | 183.00 | 158,777 | -7.14% | 9.85% | 202.46 | No company-specific release found in tonight's sources |

Two of these rows are not the same kind of fact as the others. BMO and TNDM each printed once, at the session low, and nothing corroborates either move from a second source — BMO does not report until 2 December, so this is not an earnings reaction, and I could not find a news item behind it. Treat both as unverified prints, not as decisions. WGS is the inverse problem: a clean beat on both lines and the stock is still down 10.68% after hours, which suggests something in the call that the headline release did not carry.

## After-hours earnings reactions

- **SANM +20.21%** — the session's biggest liquid after-hours gain. Fiscal Q4 revenue of $3.86B was up 84% year on year and beat the $3.48B consensus; adjusted EPS of $4.43 beat the $3.27 estimate by 35.5%. Q1 fiscal 2027 guidance is $3.8–4.1B of revenue and $3.50–3.85 of adjusted EPS; the full-year guide is $17.5–19.5B of revenue and $15.50–17.50 of adjusted EPS. Cloud & AI Systems revenue rose 179% to $2.37B, the ZT Systems integration is complete, and the company is about to ship AMD's Helios accelerated-compute systems. One caveat management volunteered: a $30M tariff recovery, mostly legacy ZT Systems, added about 75bp to adjusted operating margin and is not in the outlook.
- **TTD** — not in the table, and the reason matters. The Trade Desk beat hard (Q3 revenue $736M against a $650.7M consensus, adjusted EPS $0.33 against $0.26, Q4 revenue guided to at least $755M against roughly $685M expected) and the shares hit **$19.20 after hours, +28.6%** above the close. The last print was **$15.29, only +2.41%**. The gap gave back more than 25 points. A 15% workforce cut and more than $100M of 2027 savings are in the release, and political advertising is guided to a slightly larger share of Q4. This is the single most useful after-hours datapoint tonight and it is a warning about the whole post-earnings complex.
- **AAON +15.43%** — record third quarter and a raised full-year sales-growth outlook, but the same 8-K restates the first and second quarter of 2026 and discloses a material weakness in internal controls. The tape rewarded the print and ignored the restatement; that is a tradeable gap if the restatement grows.
- **HROW +15.80%** — Q3 EPS of $0.25 against $0.22 and revenue of $99.3M against $98.5M, with a $5.0M litigation-settlement gain inside GAAP net income. The catch is in the guidance: full-year adjusted EBITDA was cut from $80–100M to more than $40M. The stock is trading the revenue beat, not the guidance cut.
- **APPS -25.93%** — Digital Turbine returned to GAAP profitability and guided fiscal 2027 revenue to $670–690M, but revenue came in at $166.6M against a $178.7M estimate and EPS at $0.17 against $0.18. A revenue miss of that size, on a name that had been rebuilding, is what a -25.93% after-hours tape is pricing.
- **TTWO +4.32%** — Take-Two missed on the bottom line, $0.96 against $1.21, while revenue of $1.65B beat the $1.60B estimate, and the shares are still up after hours.
- **QMCO +15.95%** and **RKLB -6.66%** — Quantum missed badly ($0.13 against $0.25) and is up 16%; Rocket Lab, the heaviest after-hours volume name in the screen at 7.2M shares, is down 6.7% on no catalyst I could source. Neither move reads cleanly tonight.

## Open research queue

1. **Is the cap-weight penalty genuinely gone, or was today just oil beta?** The +10bp reading is the narrowest in five sessions and the median name gained 1.76% — but a 5.75% crude collapse lifts everything with an energy input, so breadth may be a factor effect rather than a change in who is buying. What would resolve it: two more sessions with median_name_move_pct above +1.0% *and* liquid_adv_dec_ratio above 4 with WTI flat, which would separate stock-picking from the commodity.
2. **What was BMO's -18.21% after-hours print?** One print, at the session low, on 282,578 shares, with no news item found and no earnings due until 2 December. Either a news headline the scanner saw and the web search did not, or a bad tick in a thin tape. What would resolve it: a second source for the 142.385 print, or a second print in the same neighbourhood before tomorrow's open.
3. **Does the semiconductor rally survive CoreWeave?** Today's SOX +6.85%, AVGO +8.78%, AMD +13.27% and AMAT +11.36% is a bet that AI-compute demand is intact against the post-midterm data-centre slowdown narrative that drove last week's selloff. CoreWeave reports tomorrow after the close with revenue of about $3.54B expected and a consensus loss of $1.45. What would resolve it: CoreWeave's revenue against that estimate and, more importantly, its capital-expenditure guide — that number is what the chip names are really trading.

## Source health

| Source | Endpoint / query | Status | Note |
|---|---|---|---|
| MCP bridge, market-recap `get_quotes` | gateway.pipeworx.io/market-recap/mcp, 4 batched calls | ok | Quote source of record for index, ETF, futures, cross-asset levels. Keyless, Yahoo-sourced, not rate-limited. |
| MCP bridge, market-recap `price_history` | SPY + RSP, 2026-10-28 to 2026-11-09 | ok | Reproduces the published +63bp reading for 2026-11-03 exactly. |
| TradingView public scanner | POST scanner.tradingview.com/america/scan, 4 screens | ok (degraded) | 2,144 names with the $1B floor; 2,808 without. Two published rows (BMO, TNDM) are single prints at the session low with no corroboration — see `## Method notes`. |
| cron #20 EOD universe | api.github.com/repos/karizaco/minimax-cloud-outputs/contents/us-eod/2026-11-09.csv | ok | 4,895 rows; 4,563 after de-duplication and EX_DISTRIBUTION drops. `AMZN` carries `data_quality=RANGE_ADJUSTED`. |
| Published watchlist | api.github.com/.../contents/refs/watchlist.yaml | ok | 8 names; ETFs (IWM, GLD, TLT) are not in the EOD universe and are priced from the bridge instead. |
| BLS release schedule | bls.gov/schedule/2026/11_sched_list.htm | ok | CPI for October confirmed at 08:30 ET on 10 November 2026. |
| Cboe daily market statistics | cboe.com/markets/us/options/market-statistics/daily/ | degraded | Total put/call **0.95** as read. The page's embedded data carries no session date stamp, so the session it describes cannot be dated with certainty — it may be the 6 November reading, which carries the same 0.95. The same page shows index 1.26 and equity 0.59; both are from the one page and no independent source disagrees. |
| VXN | bridge `get_quotes` | degraded | `as_of` 2026-11-09 17:54Z (12:54 ET), not the 16:00 ET close. Published at 29.11 as read, but the stamp means it may not be the closing value. |
| Web / issuer IR | fervoenergy.com, praxis IR, sanmina IR, sec.gov, tradesdesk IR, coreweave IR, bls.gov, cboe.com, marketchameleon, stocktitan | ok | Catalysts, calendars and put/call. Where no catalyst was found, the brief says so rather than inferring one. |

**The screen's floor hides the session.** The table above holds $1B-and-up names only. The same screen without the market-cap floor shows much larger moves, and those names are deliberately not in the movers table:

| ticker | after-hours change | note |
|---|---|---|
| CISS | +62.86% | micro-cap, no catalyst found |
| TANH | +55.74% | micro-cap, no catalyst found |
| CODX | +40.44% | micro-cap, no catalyst found |
| AMIX | +24.71% | micro-cap |
| WFF | +24.07% | micro-cap |
| RUBI | +22.28% | micro-cap |
| MVST | -52.63% | sub-$250M cap |
| IHRT | -36.16% | sub-$350M cap |
| THRY | -27.30% | Q3 results |
| TGE | -22.54% | micro-cap |
| FF | -22.09% | micro-cap |

One further row was discarded rather than published: CBMDF showed a -90.00% after-hours change from a close of $0.00001, which is a data artifact rather than a move. Separately, StockTitan's unfiltered leaderboard shows the largest single regular-session mover of the night was OMH at roughly +499%, which the extended-hours screen does not surface because its after-hours change is negative (-12.34% from a 25.84 close).

**Materials is the one sector where the cap-weighted column and the ETF disagree materially.** Cap-weighted Materials prints +3.07% against XLB's +1.91%, a +1.16pp gap. Stripping the precious-metals and copper complex — SCCO +5.26% ($150B), NEM +3.56% ($130B), RGLD +6.36% ($24B) — still leaves +2.73% against the ETF, a +0.82pp gap. The cap-weighted Materials column therefore inherits a composition difference: the universe's materials set carries mid-cap names (RGLD, AMRZ, AMIX) that sit outside XLB, and a gold bid (GLD +1.88%) that lifted miners more than the ETF. The gap is published rather than reconciled.

## Method notes

- **Participation population.** The four universe metrics and the liquid ratio use one population: cron #20's `us-eod/2026-11-09.csv`, de-duplicated to one row per `cap_source_symbol` (Alphabet A+C, Berkshire A+B, the JPMorgan preferred lines each carry a full parent cap) with `EX_DISTRIBUTION` rows dropped — 4,895 raw rows to 4,563 names. The liquid set is `market_cap >= $2B` (n=1,624).
- **`cap_weight_penalty_bp`** = (SPY `daily_return_pct` − RSP `daily_return_pct`) × 100, from one bridge `price_history` call, signed positive when the cap-weighted index outperformed.
- **`gap_fill_level`** = the prior close when the after-hours range brackets it (the 16:00 close traded through), otherwise the after-hours midpoint. Applied uniformly.
- **After-hours row verification.** Every published row was checked against the identity `postmarket_change == (postmarket_close − close) / close × 100`; no row was dropped on identity. The scanner's `close` is the settled 16:00 ET close and matches cron #20's CSV close for every row it overlaps.
- **Two published rows are single prints.** BMO (-18.21%) and TNDM (-8.64%) each have an after-hours high equal to the regular close and a low equal to the last print — one print each, at the session low. I could not corroborate either from a second source or find a catalyst. They are published with that caveat rather than silently dropped, because the screen is the screen, but they should not be traded off this table alone.
- **No put/call split is invented.** The total (0.95) is published as read from Cboe; the session it describes cannot be dated with certainty.
- **VXN is published with its 12:54 ET stamp**, not presented as a close.
- Read-only. Nothing here places a trade, sizes a position, or forecasts an index. Levels are references for a trader who has already decided what to watch.
