---
date: 2026-11-18
cron: 23-agentic-post-market-brief
contract: postmkt-artifact-v2
fire_time_et: 22:30
snapshot_et: 22:35-22:50
session: 464920675135849
scheduled_at_ms: 1795059017211
status: ok
source: MCP-over-HTTP bridge (market-recap: get_quotes, price_history) | TradingView public scanner | Cboe dated close files + daily statistics | cron #20 us-eod/2026-11-17.csv (sector taxonomy and de-duplication flags only) | issuer press and financial media via web
primary_source: bridge market-recap (get_quotes / price_history, keyless Yahoo-sourced)
universe: TradingView US scanner, NYSE/NASDAQ/AMEX type stock+dr - 6,086 names, 6,084 priced (cron #20's us-eod/2026-11-18.csv was not published at the fire time - see Source health)
degraded_sources: 1
---

# Post-market brief — Wednesday, 18 November 2026

## TL;DR

The Dow fell **561.25 points (-1.11%)** while the Nasdaq rose **0.42%** — this was not one tape, it was three: health insurers were sold on a proposed Medicare Advantage audit rule, cybersecurity was bought wholesale, and gold broke to a 14-month low. The index-level spread is the story, not the headline: **2657 advancers** against **3227 decliners** across 6,084 priced names, **median_name_move_pct -0.13%**, and **cap_weight_penalty_bp -15** (SPY -0.31% vs RSP -0.15%) — the equal-weight index *beat* the cap-weighted one, the mirror image of a narrow mega-cap tape. **liquid_adv_dec_ratio 0.95** (1,081 advancers vs 1,143 decliners above $2bn). Palo Alto Networks closed +9.90% and is +9.08% more after hours on a beat-and-raise plus a $4.5bn acquisition; UnitedHealth closed -10.21% and Humana -12.98% on the audit rule. The caveat that matters most: the after-hours numbers are a 22:35 ET snapshot of a tape that is still moving, and Anthropic's $83.00 IPO — the largest ever at $1.5tn — starts trading tomorrow, so tomorrow's index gap is set in a market that has not yet had its first print of the week.

## Tomorrow's setup — Thursday, 19 November 2026

### Futures and the overnight setup

The Globex session is **live and current** — every futures row carries a 22:25 ET stamp, ~5 minutes before the fire, so this is a genuine overnight print and not a stale settlement.

| Contract | Last | vs prior settle | as_of (ET) |
|---|---|---|---|
| ES=F (S&P 500) | 7,364.25 | +0.32% | 2026-11-18 22:25 |
| NQ=F (Nasdaq 100) | 27,352.25 | +0.61% | 2026-11-18 22:25 |
| YM=F (Dow) | 50,355.00 | +0.16% | 2026-11-18 22:25 |
| RTY=F (Russell 2000) | 2,721.60 | -0.01% | 2026-11-18 22:25 |
| ZN=F (10-year note) | 105.86 | +0.07% | 2026-11-18 22:25 |
| CL=F (WTI crude) | 81.84 | -0.57% | 2026-11-18 22:25 |
| GC=F (gold) | 3,712.10 | -0.80% | 2026-11-18 22:25 |
| DX-Y.NYB (dollar index) | 103.938 | +0.07% | 2026-11-18 22:25 |

The read: **Nasdaq futures +0.61% against Dow futures +0.16%** — the overnight is leaning back into the growth/AI complex and away from the insurers that dragged the Dow, and the small caps (RTY -0.01%) are not joining. Duration is bid (ZN +0.07%, TLT +0.84% in the cash session) and the dollar is firm (DX +0.07%), which is exactly the combination that keeps pressuring gold (GC -0.80%). The overnight is leaning against the insurers' damage rather than into it — the Dow futures bid is a 0.16% bounce on a -1.11% session.

### Economic calendar

| Time (ET) | Event | Prior | Forecast |
|---|---|---|---|
| 08:30 | Initial jobless claims (w/e 14 Nov) | 200K | 197K |
| 08:30 | Continuing claims (w/e 7 Nov) | 1,697K | — |
| 08:30 | Philadelphia Fed Business Outlook (Nov) | 20.9 | 20.0-23.2 |
| 08:50 | Fed: Hammack (Cleveland) opening remarks | — | — |
| 10:00 | Pending home sales (Oct) | -7.2% MoM | — |
| 12:30 | Fed: Goolsbee speaks | — | — |
| 13:00 | 10-year TIPS auction | 2.65% | — |
| 14:15 | Fed: Barr speaks | — | — |
| 18:30 | Fed: Paulson (Philadelphia) | — | — |
| 19:00 | Fed: Barkin (Richmond) | — | — |

The macro stance has flipped hawkish: after the 27-28 October minutes released at 14:00 ET yesterday, the market prices a **95.7% chance of a 25bp December hike** (and 4.3% for 50bp), with officials Williams and Musalem arguing for several increases before spring 2027 and Waller floating a 50bp December. That is the mechanism behind the gold low, the firm dollar and the long-duration bid — and it is why tomorrow's Philly Fed and claims print matters more than a normal Thursday. The proposed Medicare Advantage rule is also **scheduled to publish in the Federal Register tomorrow**, which starts the formal comment record the insurers are fighting.

### Earnings calendar

**Before the open (38 names):** WMT (EPS est 0.64), PDD (18.84), BABA (11.03), NTES (16.07), WSM (1.87), BBWI (0.40), FUTU (26.15), LQDT (0.45), VVV (0.42), ROAD (1.03), WMG (0.43), SPWR, MMS, YMM (1.32), ATKR, CATO, DAO, DOYU, MANU, TEN, MAGN, plus the Australian and Canadian calendar.

**After the close (21 names):** INTU (EPS est 2.64), KEYS (3.09), ROST (1.87), GAP (0.78), ESTC (0.14), BULL (0.05), ESE (2.59), GLOB (1.48), POST (1.66), NGVC (0.56), MATW, CLIR, GEOS, NTAR, DRTS (-0.15), TCOM.

Two clusters matter for tomorrow's tape. **Retail before the open** (WMT, plus WSM and BBWI) is the direct read-through on the consumer-discretionary rally that carried Amazon and the two retailers who reported today. **Software after the close** (INTU, ESTC, plus KEYS in the hardware complex) is a live test of whether today's software bid — the same bid that lifted Palo Alto and the security group — holds.

### News to watch for the top movers

- **PLBL +16.84% to 8.88** — no company-specific catalyst identified in the day's coverage; a Singapore-based holding company with a 366m share count and a wide $6.54/$9.75 intraday bid-ask. Volume of 301,731 shares was above the 208,424 average. Treat it as a flow name, not an event.
- **TENB +15.75% to 44.68** — the day's leader among liquid names, and the move has no Tenable-specific cause: it is a security-software rotation after Tuesday's sell-off, reinforced by a more constructive Morgan Stanley sector stance (security software at ~9.3x forward sales back near its one-year average). The only company release was a conference-appearance logistics note.
- **MFP +13.95% to 48.28** — the day after its first standalone quarter: EPS 0.54 vs 0.51 expected, revenue 228.9M vs 219.6M, orders +13% to 229M with a record 446M backlog, and full-year guidance raised to 953-973M of revenue. Baird lifted its target to 43 from 40, still Neutral.

### Tomorrow's three things to watch

- ANT — 83.00 IPO price — Anthropic begins trading on Nasdaq tomorrow after pricing at $83.00 above its $70-78 range, a $1.5tn valuation and an $81bn raise; the first print is the whole AI-trade anchor for the week.
- WMT — 127.36 prior close — reports before the open with EPS estimated at 0.64; guidance is the tell after two retail prints lifted the consumer-discretionary sector today.
- UNH — 349.91 close — a third session of the Medicare Advantage audit rule, and the rule is due to publish in the Federal Register tomorrow; positioning rather than a ruling sets the tape while no company has sized its share of the roughly $9bn-per-payment-year estimate.

## Day's tape

### Market read

One population throughout: the TradingView US scanner's NYSE/NASDAQ/AMEX stocks and ADRs, 6,086 names of which 6,084 printed a change. The liquid set is the same population filtered to a **$2bn market-cap floor** (2,247 names).

| Metric | Value | What it is |
|---|---|---|
| advancers | 2,657 | names closing higher |
| decliners | 3,227 | names closing lower |
| unchanged | 200 | names closing flat |
| median_name_move_pct | -0.13% | median % move of the universe |
| cap_weight_penalty_bp | -15 | SPY -0.306% minus RSP -0.153% = -15.3bp |
| liquid_adv_dec_ratio | 0.95 | 1,081 advancers : 1,143 decliners above $2bn |

The **cap_weight_penalty_bp is negative**, and that is the read of the day. The last five sessions have oscillated around zero (+51, -56, -90, +43, -15bp), so today's -15bp is noise-adjacent rather than a regime call — but the direction matters for the narrative: the Dow's -1.11% was concentrated in two insurers (UnitedHealth at a 4.32% Dow weight, Humana), not in the broad market, and the median name was only -0.13% worse than flat.

### Cap-weight penalty — 5-day history

| Session | SPY % | RSP % | cap_weight_penalty_bp |
|---|---|---|---|
| 2026-11-12 | -0.354 | -0.867 | +51 |
| 2026-11-13 | -0.363 | +0.199 | -56 |
| 2026-11-16 | -1.912 | -1.008 | -90 |
| 2026-11-17 | -1.015 | -1.448 | +43 |
| 2026-11-18 | -0.306 | -0.153 | -15 |

Both series come from one bridge `price_history` call; the 2026-11-18 pair reproduces the settled closes exactly (SPY 730.20, RSP 215.43).

### Index, ETF and volatility levels

Every index row carries an `as_of` of 2026-11-18 between 16:15 and 17:16 ET — the session just closed, no stale rows.

| Instrument | Close | Change | as_of (ET) |
|---|---|---|---|
| S&P 500 | 7,323.63 | -0.23% | 16:57 |
| Nasdaq Composite | 24,429.89 | +0.42% | 17:16 |
| Dow Jones Industrial Average | 50,198.17 | -1.11% | 16:57 |
| Russell 2000 | 2,714.31 | +0.46% | 16:30 |
| Nasdaq 100 | 27,116.26 | +0.42% | 17:16 |
| PHLX Semiconductor | 9,652.80 | +0.10% | 17:16 |
| VIX | 24.56 | -3.53% | 16:15 |
| VXN | 33.12 | -3.83% | 16:15 |
| SPY | 730.20 | -0.31% | 16:00 |
| QQQ | 659.51 | +0.39% | 16:00 |
| IWM | 270.12 | +0.40% | 16:00 |
| DIA | 501.73 | -1.10% | 16:00 |
| RSP | 215.43 | -0.15% | 16:00 |
| SMH | 459.54 | -0.12% | 16:00 |
| GLD | 341.19 | -3.20% | 16:00 |
| TLT | 80.22 | +0.84% | 16:00 |

**The volatility indices were read from the dated history and cross-checked against Cboe's own dated close file**, not from the quote row: the bridge's `price_history` gives VIX 24.56 (-3.535%) and VXN 33.12 (-3.833%) for 2026-11-18, and `cdn.cboe.com/.../VIX_History.csv` and `VXN_History.csv` agree to the cent (VIX open 24.22, high 26.26, low 23.45, close 24.56; VXN close 33.12). Note the intraday shape: the VIX made its high of 26.26 before the close and was sold off into it — volatility spiked and then deflated in the same session.

**Put/call ratio, session 2026-11-18** (Cboe daily statistics, payload `selectedDate` = 2026-11-18): total **1.05**, index 1.14, equity 0.72, exchange-traded products 1.42, VIX 0.88, SPX+SPXW+SPXO 1.19, XSP 1.07. The total at 1.05 with equity at 0.72 is a call-heavy tape, and the equity figure is the more informative one.

### Cross-asset

| Asset | Level | Change |
|---|---|---|
| WTI crude (CL=F) | 81.84 | -0.57% |
| Gold (GC=F) | 3,712.10 | -0.80% |
| Gold ETF (GLD) | 341.19 | -3.20% |
| Dollar index (DX-Y.NYB) | 103.938 | +0.07% |
| 10-year note future (ZN=F) | 105.86 | +0.07% |
| 20+ year Treasury ETF (TLT) | 80.22 | +0.84% |

Gold fell to a **14-month low** (spot below $3,800 for the first time since September 2025, about 31% below its January record) on a firm dollar at a 19-month high and a market priced for further Fed tightening — with the 10-year yield holding above 5%. The dollar index at 103.938 is its highest since April 2025. TLT's +0.84% on 1.13x its 10-day average volume is the duration bid in one line. Energy's sector close (-2.99% cap-weighted, XLE -3.27%) is consistent with crude -0.57% and a hawkish Fed taking the growth premium out of cyclicals.

### Day's movers

Liquid set: market cap >= $2bn, from the same 6,086-name universe. The full table is in the artifact's universe pull; the leaders are:

| name | Close | Change | Market cap |
|---|---|---|---|
| PLBL | 8.88 | +16.84% | $3.3bn |
| TENB | 44.68 | +15.75% | $4.7bn |
| MFP | 48.28 | +13.95% | $2.2bn |
| QLYS | 197.24 | +12.92% | $6.9bn |
| NTSK | 23.51 | +12.73% | $9.6bn |
| FSLY | 17.90 | +12.58% | $2.9bn |
| OKTA | 195.61 | +12.07% | $34.2bn |
| PANW | 339.92 | +9.90% | $278.3bn |
| UNH | 349.91 | -10.21% | $313.5bn |
| HUM | 385.78 | -12.98% | $46.3bn |
| ARDT | 14.40 | -18.87% | $2.0bn |
| CLOV | 4.17 | -11.84% | $2.2bn |
| ACIW | 52.89 | -10.25% | $5.3bn |
| AAOI | 40.79 | -9.80% | $3.7bn |
| CBRS | 94.15 | -9.63% | $18.0bn |

The top of the gainers list is a **security-software complex** — PANW, CRWD, OKTA, TENB, QLYS, NTSK, FSLY, S, SAIL, ATEN — and the top of the losers list is **managed care** — UNH, HUM, ELV, CNC, CVS. Two single-name stories sit outside the sector pattern. **ARDT -18.87% to 14.40** is a shareholder event, not a fundamental one: on Tuesday night two shareholders priced a sale of 8,000,000 existing shares at 14.50 each and the company said it would buy back 1,500,000 of them. The largest move of the session outside the $2bn screen was **HY -41.07%**, the lift-truck maker, on a proposal to sell 125m of convertible notes due 2031 — debt that can turn into shares, partly funding a 100.0m term-loan repayment and a 15m buyback.

### Watchlist EOD review

Published watchlist (`refs/watchlist.yaml`, updated 2026-11-06) — 8 names, all quoted from the scanner at the close. Volume is against the 10-day average.

| name | Close | Day | Day range | Volume vs 10d avg | After hours | AH % |
|---|---|---|---|---|---|---|
| AAPL | 352.45 | +0.15% | 351.47 - 356.42 | 34.2M / 42.7M (0.80x) | 354.70 | +0.64% |
| MSFT | 508.29 | +0.40% | 501.08 - 510.44 | 22.0M / 27.6M (0.80x) | 514.00 | +1.12% |
| NVDA | 150.96 | -2.89% | 150.40 - 159.70 | 349.8M / 392.2M (0.89x) | 151.94 | +0.65% |
| GOOGL | 282.44 | +0.80% | 279.69 - 284.97 | 27.4M / 34.1M (0.80x) | 286.72 | +1.51% |
| AMZN | 267.74 | +3.82% | 259.51 - 268.29 | 41.3M / 45.0M (0.92x) | 271.32 | +1.34% |
| IWM | 270.12 | +0.40% | 267.89 - 272.36 | 22.5M / 26.2M (0.86x) | 271.48 | +0.50% |
| GLD | 341.19 | -3.20% | 340.76 - 346.31 | 13.5M / 9.9M (1.37x) | 343.79 | +0.76% |
| TLT | 80.22 | +0.84% | 79.82 - 80.28 | 42.0M / 37.1M (1.13x) | 80.22 | 0.00% |

Two things stand out. **NVDA is the only watchlist name down on the day** (-2.89%) despite reporting revenue of 115.8bn, up 103%, with a roughly 130bn fourth-quarter guide that assumes no China data-centre sales — it opened higher and gave the gain back, and it has now closed below its prior close for two sessions while the after-hours print sits at 151.94. **AMZN's +3.82%** came on volume *below* its 10-day average (0.92x) with no single company news; the AWS growth story (39% to 46.0bn in Q3, guided "north of 40%" in 2027-28) and the pre-holiday retail set-up are the published reasons. GLD and TLT both traded above their 10-day average volume — gold on the way down (1.37x) and duration on the way up (1.13x), the same trade expressed twice.

## Sector rotation

Cap-weighted return is computed on one row per share-class family over 4,021 names: the universe's own market caps and moves, de-duplicated on cron #20's `cap_source_symbol` (so Alphabet A+C and Berkshire A+B count once each), with EX_DISTRIBUTION, NO_CAP and NO_SECTOR rows excluded. Every cap-weighted return below is inside the ±20% sanity band.

| Sector | Cap-weighted % | Median % | Sector ETF | ETF % | Gap (pp) |
|---|---|---|---|---|---|
| Consumer Discretionary | +2.22 | +1.64 | XLY | +1.79 | +0.43 |
| Communication Services | +0.44 | -0.19 | XLC | +0.30 | +0.14 |
| Industrials | +0.35 | +0.30 | XLI | -0.05 | +0.40 |
| Utilities | +0.33 | +0.45 | XLU | +0.30 | +0.03 |
| Real Estate | +0.31 | +0.38 | XLRE | +0.07 | +0.24 |
| Information Technology | +0.28 | +0.14 | XLK | +0.34 | -0.06 |
| Consumer Staples | -0.35 | +0.37 | XLP | -0.31 | -0.04 |
| Financials | -0.80 | -0.10 | XLF | -1.14 | +0.34 |
| Materials | -1.42 | -0.53 | XLB | -0.75 | -0.67 |
| Health Care | -1.75 | -0.60 | XLV | -2.20 | +0.45 |
| Energy | -2.99 | -1.10 | XLE | -3.27 | +0.28 |

**Top three:** Consumer Discretionary (+2.22%), Communication Services (+0.44%), Industrials (+0.35%). **Bottom three:** Energy (-2.99%), Health Care (-1.75%), Materials (-1.42%).

Two of these numbers are constituent effects rather than rotations, and the ETF cross-check is what exposes them:

- **Consumer Discretionary is Amazon.** AMZN's 2.895tn cap contributed **+1.39pp of the +2.22%** — 63% of the sector move. The sector ex-AMZN is **+0.82%** against XLY's +1.79%. Amazon also drove 82% of the volume-weighted turn in the sector. Read this as a mega-cap event, not a consumer rotation; the rest of consumer discretionary (TJX +8.05%, Target +4.01% on their own earnings) was genuinely good, but it is a smaller share of the cap-weighted number than the headline suggests.
- **Communication Services is Alphabet.** GOOGL's 3.438tn cap contributed **+0.41pp of the +0.44%** — 93% — and the sector's median name was **-0.19%**, i.e. negative. This is one stock, not a sector.
- **Health Care and Energy agree with their ETFs** (-1.75% vs XLV -2.20%; -2.99% vs XLE -3.27%), so those bottom-three readings are broad, not concentrated. Health Care's damage is the insurers: the managed-care complex carried it, and it is why the sector's median (-0.60%) sits well below its cap-weighted print.

## After-hours movers

TradingView scanner, extended-hours screen (type stock/dr, market cap >= $1bn, after-hours volume > 50,000), 2,094 names screened, published at the contract's 10-name cap. `gap_fill_level` is the prior close when the after-hours range traded through it, otherwise the after-hours midpoint. Every row passes the identity check `postmarket_change == (postmarket_close - close) / close x 100`, and every row is on a primary US listing (over-the-counter venues are excluded).

| ticker | prior_close | ah_last | ah_high | ah_low | ah_volume | gap_pct | ah_range_pct | gap_fill_level | venue |
|---|---|---|---|---|---|---|---|---|---|
| PANW | 339.92 | 370.78 | 381.68 | 324.00 | 4,155,550 | +9.08% | 16.97% | 339.92 | NASDAQ |
| CRWD | 237.03 | 251.27 | 251.68 | 233.96 | 1,544,465 | +6.01% | 7.48% | 237.03 | NASDAQ |
| CGON | 80.00 | 84.78 | 84.78 | 79.04 | 290,735 | +5.98% | 7.17% | 80.00 | NASDAQ |
| EFOR | 32.30 | 34.08 | 34.08 | 31.85 | 134,721 | +5.51% | 6.90% | 32.30 | NYSE |
| CRGY | 10.77 | 11.26 | 11.26 | 10.76 | 571,605 | +4.55% | 4.64% | 10.77 | NYSE |
| UTI | 22.04 | 20.15 | 22.09 | 18.70 | 342,917 | -8.59% | 15.38% | 22.04 | NYSE |
| CLVT | 2.16 | 2.03 | 2.16 | 2.03 | 609,383 | -6.02% | 6.02% | 2.16 | NYSE |
| MLCO | 4.17 | 4.02 | 4.17 | 4.02 | 83,854 | -3.58% | 3.58% | 4.17 | NASDAQ |
| ASAN | 9.20 | 8.91 | 9.21 | 8.91 | 379,604 | -3.15% | 3.26% | 9.20 | NYSE |
| BIIB | 251.41 | 244.01 | 251.41 | 244.01 | 216,836 | -2.94% | 2.94% | 251.41 | NASDAQ |

**The screen's floor hides the session's real leaderboard.** Pulling the same screen without the $1bn market-cap floor, the night's actual extremes are far outside the table above: INHD **+75.23%** (Inno Holdings, $5.8m cap), SPRC **+38.90%** ($0.6m), INLF **+16.85%** ($0.4m), MAGN **+15.03%** ($426m — and it reports tomorrow morning), FTH +13.93%, OPRT +13.44%; on the downside FCHL **-37.82%** ($0.8m), VWAV **-18.74%** ($2.5m), IMCC **-17.85%** ($0.9m), RRGB **-17.48%** ($150m), ZNB -16.72%, MRM -14.89%. All six of the smallest are sub-$3m shells where a single print moves the price; they are disclosed so the table is not mistaken for the whole tape, not because they are signals. The one name in that group worth carrying is RRGB, a $150m restaurant operator at -17.48% after hours.

**PANW's after-hours range is the widest on the board at 16.97% of the prior close** — it printed as high as 381.68 and as low as 324.00 around a 370.78 last. The close traded through in the after-hours session, so the gap fill level is the prior close of 339.92: that is the level a long waits for. **Every one of the ten rows traded through its 16:00 close inside the after-hours range**, so all ten gap fill levels are the prior close and the midpoint branch of the rule does not apply to any of them. UTI is the mirror image on the downside, a 15.38% range around a 20.15 last — but its fill level is still the 22.04 close, because the after-hours high of 22.09 traded through it.

## After-hours earnings reactions

**Palo Alto Networks — reported fiscal Q1 2027 after the bell, beat and raised, and the tape has not finished repricing it.**

- Revenue 3.45bn, +39% year over year, against a 3.31bn consensus; adjusted EPS 1.05 against 0.97; subscription and support revenue 2.85bn from 2.04bn.
- Next-generation security ARR +66% year over year to 9.73bn — an acceleration from 63% — against a 9.55bn estimate; RPO +35% to 21bn.
- Fiscal Q2 guide 3.53-3.55bn of revenue against 3.42bn expected, adjusted EPS 1.01-1.03 (midpoint 1.02 vs 1.01), NGS ARR 10.20-10.22bn against 9.91bn expected.
- Full-year fiscal 2027 lifted to 14.52-14.57bn of revenue (from 14.1-14.2bn) and 4.26-4.30 of adjusted EPS (from 4.16-4.19).
- Announced a **4.5bn all-stock acquisition of Applied Compute**, an open-weight AI post-training and inference platform, expected to close in fiscal Q3 2027.
- Non-GAAP operating margin 30.7%, a record and a second consecutive quarter above 30%; adjusted free cash flow 1.9bn in the quarter.
- The stock closed +9.90% at 339.92 and is +9.08% after hours at 370.78 — the after-hours move is larger in percentage terms than the session move.

The reaction to the *group* is the bigger trade: the cybersecurity complex rallied all day on a Morgan Stanley upgrade of the sector's valuation stance, and Palo Alto's print landed on top of it. CRWD +7.95% into the close and +6.01% after hours, OKTA +12.07%, TENB +15.75%, QLYS +12.92%, NTSK +12.73%, FSLY +12.58%, SentinelOne +10.35%, SAIL +10.26%. That is a sector re-rating with one very large confirmed earnings print under it — which is why tomorrow's software calendar (INTU, ESTC) matters more than usual.

**Other after-hours names, with the catalyst where one exists and none where it does not:**

- **CGON +5.98% to 84.78** (CG Oncology, $7.15bn) — no after-hours news located in the day's coverage; the print is one high-to-low (84.78 / 79.04), i.e. a single level, so treat it as a thin tape rather than a discovery.
- **EFOR +5.51% to 34.08** (Everforth, $1.33bn) — no catalyst located.
- **CRGY +4.55% to 11.26** (Crescent Energy, $4.55bn) — no catalyst located; also a single-print row (11.26 high, 10.76 low).
- **UTI -8.59% to 20.15** (Universal Technical Institute, $1.21bn) — no after-hours catalyst located; the 15.38% range (18.70-22.09) is the widest downside range on the board.
- **CLVT -6.02% to 2.03** (Clarivate, $1.38bn) — extends a weak fundamental position: Q3 revenue 481.6M (-9.2% year over year), a net loss of 80.8M including 62.2M of goodwill and intangible impairments, and full-year guidance of a 144-154M net loss. The company presented at an RBC conference today; no fresh after-hours release was located.
- **MLCO -3.58% to 4.02** (Melco Resorts, $1.51bn), **ASAN -3.15% to 8.91** (Asana, $2.11bn), **BIIB -2.94% to 244.01** (Biogen, $37.2bn) — no after-hours catalysts located in the day's coverage.

## Open research queue

1. **Is a $1.5tn Anthropic debut absorbable, or does it drain the AI complex?** Anthropic priced 980m shares at 83.00 for a 1.5tn valuation and an 81bn raise — ahead of SpaceX's 75bn — and trades tomorrow under ANT. Why it matters: it is either the largest liquidity event the AI complex has seen, which argues for a flush in the names it competes with, or a spectacular proof of demand that keeps buying the whole trade. What would resolve it: the first prints of ANT against the Nasdaq 100's overnight +0.61%, and whether the megacap AI names (NVDA -2.89% today, AMZN +3.82%, GOOGL +0.80%) move with it or against it.
2. **Is the Medicare Advantage audit rule a sized earnings event or a positioning unwind?** CMS's proposed CRUSH rule would extrapolate risk-adjustment audit findings back to payment year 2018; CMS estimates roughly 9bn per payment year recovered industry-wide, the rule is due to publish in the Federal Register tomorrow, and comments run to 19 January 2027. Why it matters: Humana is down 12.98% and UnitedHealth 10.21% with the exposure ranked by the analysts but never sized by any issuer, and Medicare Advantage was 99.4bn of Humana's 129.7bn of 2025 revenue. What would resolve it: any company 8-K quantifying the share, the Federal Register text itself, and whether the third session extends the selling or finds a bid.
3. **What does the negative cap-weight penalty actually mean for positioning?** cap_weight_penalty_bp has been negative on three of the last five sessions (-56, -90, -15) and the median name was -0.13% while the Dow fell 1.11% — the losses were concentrated in two index weights, not in the market. Why it matters: if the index's decline is a factor story (insurers) rather than a breadth story, the hedges that sold beta are wrong-footed into a session where NQ futures are +0.61%. What would resolve it: tomorrow's advancers/decliners and liquid_adv_dec_ratio against the Nasdaq's overnight bid, and whether the equal-weight/ cap-weight gap persists on a third consecutive down-Dow session.

## Source health

- **Quotes and history (clean):** bridge `market-recap` `get_quotes` for 16 indices/ETFs plus 8 futures and 14 single names, and `price_history` for SPY/RSP and VIX/VXN. Every index row carries an `as_of` of 2026-11-18; every futures row carries a 22:25 ET stamp, so the overnight print is live rather than a settlement.
- **Volatility indices (verified twice):** VIX 24.56 and VXN 33.12 read from `price_history` and cross-checked against Cboe's dated close files — agreement to the cent, on the dated row.
- **Put/call (clean):** Cboe daily statistics, payload `selectedDate` = 2026-11-18, i.e. the session that just closed. Total 1.05 with index 1.14, equity 0.72, ETP 1.42, SPX 1.19, XSP 1.07, VIX 0.88 — all splits are from the same payload and reconcile with the total.
- **DEGRADED SOURCE 1 of 1 — cron #20's `us-eod/2026-11-18.csv` was not published at the fire time.** The outputs repo's newest EOD universe file is 2026-11-17 (the routine is a known late publisher). Consequences, both disclosed: (a) the participation read's population is the TradingView scanner's 6,086 NYSE/NASDAQ/AMEX stocks and ADRs rather than cron #20's ~4,888-name universe, so the counts are not comparable with the prior session's published breadth; (b) the GICS sector labels and the de-duplication flags were carried from cron #20's 2026-11-17 file, which maps 4,167 of today's 6,086 names — so the sector table covers 4,021 names, not the full universe, and the 1,919 unmapped names (mostly newer listings and non-US listings) are outside every cap-weighted sector number. Excluded from the cap-weighted columns per cron #20's rules: 125 EX_DISTRIBUTION rows, 1 NO_CAP row and 1 NO_SECTOR row inside the mapped set. The NO_SECTOR bucket is excluded rather than ranked, because a bucket is not a sector.
- **After-hours vendor divergence — named, not blended.** The scanner's 22:35 ET prints differ materially from the earlier vendor prints for the same names: PANW +9.08% at 22:35 ET against Benzinga's +8.11% at 16:26, Investing.com's +7.43% at about 17:36 and CNBC's +9.00% at 17:02; CRWD +6.01% at 22:35 against Yahoo's +4.42% at 16:50. The scanner is the source of record for the table; the earlier prints are not averaged into it. The extended-hours tape is still moving after the fire.
- **After-hours screen floor:** the published table carries a $1bn market-cap floor, so it is not the session's leaderboard — the real extremes are sub-$3m shells (INHD +75.23%, FCHL -37.82%) listed in the After-hours movers section.
- **Day's mover leaders without a sourced catalyst:** PLBL (+16.84%) and ARDT (-18.87%) are covered by the day's filings/news cycle, but no single attributable catalyst was located for PLBL; its 366m share count and 1.71-wide bid-ask are the honest explanation offered.
- **Universe change column:** the participation read uses the TradingView scanner's own `change` field, not cron #20's `change_pct`, so small differences against the prior session's published numbers are expected even where the populations overlap.

## Method notes

- Fire date resolved from the run's `scheduled_at_ms` (1795059017211 = 2026-11-18 22:30:17 ET), not the wall clock; the window check returned `fire-date: 2026-11-18`, `replay: no`, `stall_min: 5`.
- The participation read, the liquid set and the sector rotation all use one population — the scanner's 6,086-name universe, one row per share-class family for the cap-weighted columns. The liquid set is the same population with a $2bn market-cap floor (2,247 names), and that floor is named in the metric table.
- `cap_weight_penalty_bp = (SPY daily_return_pct - RSP daily_return_pct) x 100`, rounded to the nearest basis point; the 2026-11-18 pair reproduces the published -15bp from a single `price_history` call.
- `gap_fill_level` follows the contract rule: the prior close when the after-hours range traded through it, otherwise the after-hours midpoint. Every after-hours row was checked against `postmarket_change == (postmarket_close - close) / close x 100` before publication, and rows on over-the-counter venues were excluded from the table.
- The futures table is the live 22:25 ET Globex print. This is a Wednesday fire, so there is no weekend-closure caveat; the futures source is not degraded.
- Catalyst sourcing: issuer releases and financial media for Palo Alto's print, the Medicare Advantage rule and the Anthropic pricing; calendars from EarningsWhispers, Yahoo Finance and Nexqual; the economic calendar from Benzinga, MarketWatch and Il Sole 24 Ore Radiocor. Where no catalyst could be sourced, the brief says so rather than inferring one.
- Read-only by design: no positions, no orders, nothing but the published tape.
