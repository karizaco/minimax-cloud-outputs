---
date: 2026-11-27
cron: 23-agentic-post-market-brief
contract: postmkt-artifact-v2
fire_time_et: 22:30
snapshot_et: 22:31-22:52
session: 468104736227539
scheduled_at_ms: 1795836603385
status: ok
source: bridge market-recap (get_quotes, price_history), TradingView america scanner, cron #20 us-eod CSV, CBOE daily statistics + dated volatility CSVs, EarningsWhispers/StockTitan/ATLAS calendars, press sweep
primary_source: MCP-over-HTTP bridge market-recap (quote source of record); TradingView scanner for extended hours
universe: cron #20 us-eod/2026-11-27.csv - 4,902 rows, 4,826 priced (US equities and ADRs, GICS sectors)
degraded_sources: 2
---

# Post-market brief — Friday, 27 November 2026

## TL;DR

A shortened Black Friday session (the tape closed at **13:00 ET**, four hours not eight) still produced the strongest week on record for this tape: the S&P 500 gained **1.60% to 7,297.49**, the Nasdaq Composite **2.31% to 24,129.50**, the Dow **1.18% to 50,774.94** and the PHLX Semiconductor Index **4.69% to 9,186.71** — a chip-and-AI rebound after last week's ~12% technology selloff. Participation was genuinely broad, not a two-stock tape: **advancers 3,569** against **decliners 1,091** and 166 unchanged, with a **median_name_move_pct** of **+0.94** across the 4,826 priced names. But the cap-weighting is still visible: **cap_weight_penalty_bp** was **+40** (SPY +1.62% against RSP +1.22%) — narrow in the sense that the equal-weight index lagged, not that breadth failed — and the liquid set (names above $2B of market cap, 1,782 names) printed a **liquid_adv_dec_ratio** of **4.54** (1,434 up, 316 down). The overnight setup does not exist: CME equity-index futures closed with the equity market at 13:15 ET and the trading week ended, Globex reopens Sunday 18:00 ET, and Asian cash markets are shut for the weekend. Read the next session's setup off the futures-versus-cash-close comparison, not off a session that has not happened.

## Tomorrow's setup — Monday, 30 November 2026

Tomorrow is Saturday; **the next trading session is Monday, 30 November**, the first full-length session after a shortened Black Friday. The setup therefore has no overnight print to read: what matters is where the cash close left the tape and what Monday's calendar puts on it.

### Futures and the overnight setup

There is no overnight move to publish, and the reason is structural rather than a data failure: **CME equity-index futures shut at the 13:15 ET stamp** (every futures row in the bridge carries `as_of` 2026-11-27T18:14:59Z = 13:14:59 ET, matching the shortened equity session), the **trading week ended**, and Globex reopens **Sunday 18:00 ET**. The Asian cash leg is closed for the weekend as well — there is no Nikkei or Kospi print to stamp.

What the futures rows *do* carry is the session's own settlement, and the honest way to read it is against both denominators:

| Instrument | Last | vs prior settlement | vs cash index close | as_of (ET) |
|---|---|---|---|---|
| ES=F (S&P 500 Dec 26) | 7,308.25 | +1.56% (settle 7,195.75) | **+0.15%** vs SPX 7,297.49 | 13:14:59 |
| NQ=F (Nasdaq 100 Dec 26) | 26,765 | +2.55% (settle 26,100.25) | **+0.14%** vs NDX 26,726.39 | 13:14:59 |
| YM=F (Dow Dec 26) | 50,821 | +1.18% (settle 50,228) | **+0.09%** vs DJI 50,774.94 | 13:14:58 |
| RTY=F (Russell 2000 Dec 26) | 2,754.40 | +1.78% (settle 2,706.10) | **+0.15%** vs RUT 2,750.30 | 13:14:59 |
| ZN=F (10Y note Dec 26) | 106.53 | −0.51% (settle 107.08) | n/a | 13:14:59 |
| GC=F (gold Dec 26) | 3,668.50 | +2.91% (settle 3,564.60) | n/a | 14:44:58 |

**The overnight did not extend the session.** Measured against the cash index close the futures are flat (+0.09% to +0.15% across the four equity contracts) even though they show +1.18% to +2.55% against the prior settlement — the futures simply tracked the cash session to its early close. Judge Monday's open on the cash-close column, not the settlement column. GC=F is a different instrument with a different clock: it still traded after the equity close, stamped 14:44:58 ET at 3,668.50 (**+2.91%** on the session), and the gold ETF's own after-hours print barely moved (GLD closed +2.12% and printed 334.99, only +0.18% after hours) — treat the future as the signal and the ETF as the session leg, and do not call either one wrong.

### Economic calendar

Monday is the quietest day of a heavy week — the calendar's 13 releases are all first- or second-tier, and the week's real catalysts sit on Tuesday through Friday.

| Time (ET) | Release | Forecast | Previous | Impact |
|---|---|---|---|---|
| 9:45 AM | Chicago Business Barometer (ISM-Chicago PMI) | 54.6 | 55.3 | Medium |
| 10:30 AM | Dallas Fed Manufacturing Business Index | 10.2 | 13.4 | Medium |
| 11:30 AM | 13-week Treasury bill auction, $95B | 4.111% | 4.18% | Medium |
| 11:30 AM | 26-week Treasury bill auction, $82B | — | 4.34% | Medium |
| 3:30 PM | CFTC net positions (gold, oil, S&P 500) | — | — | Low |

Ahead of Monday, the week carries **ISM manufacturing PMI on Tuesday 10:00** (forecast 55.0 vs 55.5), **ADP employment Wednesday 8:15**, **ISM services and JOLTS Thursday 10:00**, and **nonfarm payrolls Friday 8:30** (forecast 90K against 165K prior) plus the University of Michigan sentiment survey. Monday itself has no high-impact release — and the Dow's rally Friday, alongside a flat futures tape, says the session was positioning for that Friday payrolls print rather than for Monday.

### Earnings calendar

The calendar vendors disagree sharply on **Monday 30 November**: EarningsWhispers shows 10-33 companies depending on which of its own pages is read, StockTitan shows 2 names worth $2B or more, ATLAS shows 15 confirmed dates, and EarningsMadness shows 1 S&P 500 constituent. **The roster below is the intersection of two or more sources**, and the disagreement is disclosed rather than resolved by preference:

| Company | Ticker | When | EPS est. | Close |
|---|---|---|---|---|
| Chagee Holdings | CHA | Before the open | — | 10.72 |
| Heidmar Maritime Holdings | HMR | Before the open | 0.04 | — |
| Nordic American Tankers | NAT | Before the open | — | — |
| B.O.S. Better Online Solutions | BOSC | Before the open | 0.06 | — |
| Powerlaw Corp | PWRL | Before the open | — | — |
| Rubrik | RBRK | **After the close** | −0.38 | 112.89 |
| Nano Nuclear Energy | NNE | After the close | −0.31 | 9.54 |

Monday is thin: ATLAS puts the one-day expected move on RBRK at ±4.2% and on NNE at ±5.7%. **Credo (CRDO) and FactSet (FDS) are contested** — EarningsMadness places both on Monday after the close, ATLAS places CRDO on Tuesday 1 December, so they are carried here as contested rather than published as confirmed. Tuesday is where the weight is: MRVL (consensus 0.79 against 0.62 year-ago), NTAP (2.14 against 1.63), OKTA, MDB and CRDO all report after Tuesday's close.

### News to watch for the top movers

- **COHR — 223.90 close, +14.12%.** The largest single-sector driver in Information Technology: roughly $51 million of insider purchases and a $2 billion buyback authorised the week before, with datacenter and communications revenue up 79% year over year and orders extending into calendar 2028. Still roughly 50% below its June record high.
- **VRTX — 534.60 close, −5.23%.** The drug regulator extended its review of povetacicept in IgA nephropathy by up to three months; **the original decision date was 30 November 2026 — Monday** — and is now no later than 28 February 2027. It is the session's one loser with a date on Monday's calendar.
- **NVDA — 150.49 close, +0.80%.** The stock traded lower early on a report that partners were told to suspend shipments of NVIDIA-based servers to Malaysia, Singapore, Thailand and Indonesia, then recovered most of the loss into a shortened close. The report, not the print, is the open question.

### Tomorrow's three things to watch

- **NVDA** — 150.49 close (after-hours 149.80) — the export-suspension report is unresolved going into Monday; watch whether the stock can hold the 149.36 after-hours low that the Friday tape set.
- **VRTX** — 534.60 close, −5.23% — the regulator pushed the review out by up to three months, and the decision date that fell due today has slipped to no later than 28 February 2027; the timeline is the story, not the review.
- **RBRK** — 112.89 close — reports after Monday's close with consensus EPS at −$0.38; the guide is the tell on a cyber-security name reporting into an AI-led tape.

## Day's tape

### Market read

One population throughout: cron #20's `us-eod/2026-11-27.csv` — 4,902 rows, 4,826 of them priced. The liquid set is the same universe with a **$2B market-cap floor**.

| Metric | Value | How it is computed |
|---|---|---|
| advancers | 3,569 | names closing higher in the EOD universe |
| decliners | 1,091 | names closing lower |
| unchanged | 166 | names closing flat |
| median_name_move_pct | +0.94 | median `change_pct` over the 4,826 priced names |
| cap_weight_penalty_bp | **+40** | SPY +1.62% minus RSP +1.22%, bridge `price_history` |
| liquid_adv_dec_ratio | 4.54 | 1,434 advancers : 316 decliners, names above $2B (n=1,782) |

The participation read and the cap-weighted read agree: four in five names rose (press consensus, AP), the median name was +0.94%, and yet the equal-weight index still lagged the cap-weighted one by 40bp. That is a *narrowing* penalty — the three prior sessions ran −102bp, −112bp and −166bp — so the breadth genuinely broadened rather than the tape merely looking green.

### Cap-weight penalty — 5-day history

| Session | SPY % | RSP % | cap_weight_penalty_bp |
|---|---|---|---|
| 2026-11-20 | -3.64 | -1.98 | -166 |
| 2026-11-23 | +4.71 | +2.59 | +211 |
| 2026-11-24 | -0.49 | +0.54 | -102 |
| 2026-11-25 | -0.29 | +0.83 | -112 |
| 2026-11-27 | +1.62 | +1.22 | **+40** |

26 November was Thanksgiving and there was no session; these are the five most recent trading days. The series reads as a violent week (a 4.71% up day and a 3.64% down day inside five sessions) in which the equal-weight index has been the more resilient leg — its penalty flipped positive only today, and at +40bp it is the smallest of the five.

### Index, ETF and volatility levels

| Instrument | Close | Change | Day range | as_of / source |
|---|---|---|---|---|
| S&P 500 | 7,297.49 | +1.60% | 7,211.46 – 7,304.10 | 2026-11-27, bridge `price_history` |
| Nasdaq Composite | 24,129.50 | +2.31% | 23,690.60 – 24,149.09 | 2026-11-27, bridge `price_history` |
| Dow Jones Industrial Average | 50,774.94 | +1.18% | 50,398.29 – 50,830.19 | 2026-11-27, bridge `price_history` |
| Nasdaq 100 | 26,726.39 | +2.61% | — | 2026-11-27, bridge `price_history` |
| Russell 2000 | 2,750.30 | +1.71% | 2,721.39 – 2,751.42 | 2026-11-27, bridge `price_history` |
| PHLX Semiconductor | 9,186.71 | +4.69% | — | 2026-11-27, bridge `price_history` |
| VIX | 23.81 | **-11.16%** | 23.81 – 27.52 | bridge `price_history`, cross-checked against CBOE `VIX_History.csv` |
| VXN | 33.34 | **-13.47%** | 33.15 – 37.74 | bridge `price_history`, cross-checked against CBOE `VXN_History.csv` |
| SPY | 728.32 | +1.62% | — | bridge `price_history` |
| RSP | 218.38 | +1.22% | — | bridge `price_history` |
| QQQ | — | +2.61% (Nasdaq 100) | — | press/ETF proxy |
| IWM | 273.79 | +1.83% | 270.69 – 273.92 | bridge `get_quotes` |
| DIA | — | +1.18% (Dow) | — | press/ETF proxy |
| SMH | — | +4.69% (PHLX) | — | press/ETF proxy |
| GLD | 334.40 | +2.12% | 331.26 – 334.41 | bridge `get_quotes` |
| TLT | 81.27 | **-1.18%** | 81.23 – 81.94 | bridge `get_quotes` |

Both volatility indices are read from the **dated history**, not from the quote row, and both are confirmed to the cent against CBOE's own dated close files. CBOE's VIX file carries a 26.80 row for 26 November (Thanksgiving) that its VXN file does not; the bridge agrees with CBOE on both 27 November closes, so the published moves are unaffected. **Total put/call 0.83** for session **2026-11-27** (the page's `selectedDate` and `prevTradingDay` both read 2026-11-27), with index 1.08, equity 0.58, ETP 0.81, VIX 0.90, SPX+SPXW+SPXO 1.09 and XSP 1.10 — all six read from the one payload, so they reconcile with the total.

### Cross-asset

Gold was the day's other story: the December future printed **3,668.50, +2.91%** on its own session (stamped 14:44:58 ET), and the gold miners led the materials complex — Newmont +5.52% and Southern Copper +4.33% are two of the three largest cap-weighted contributors in Materials. GLD closed +2.12% at 334.40 and its extended-hours book repriced only +0.18%, a thin after-hours market for the ETF against a continuously traded future. Rates backed up: TLT closed −1.18% at 81.27 and the 10-year note future settled −0.51% at 106.53.

### Day's movers

Liquid names (above $2B of market cap) on a shortened session:

| Movers | Close | Change | Sector |
|---|---|---|---|
| VERA — Vera Therapeutics | 34.26 | +16.14% | Health Care |
| SNDK — Sandisk | 85.36 | **+15.96%** | Information Technology |
| COHR — Coherent | 223.90 | +14.12% | Information Technology |
| AXTI — AXT | 36.37 | +13.73% | Information Technology |
| ANT — Anthropic | 91.88 | +10.98% | Information Technology |
| EQPT — EquipmentShare | 16.29 | +10.07% | Industrials |
| LFTO — Liftoff Mobile | 26.14 | +9.88% | Communication Services |
| VRTX — Vertex Pharmaceuticals | 534.60 | **-5.23%** | Health Care |
| RHI — Robert Half | 37.83 | -3.94% | Industrials |
| SFM — Sprouts Farmers Market | 51.37 | -3.66% | Consumer Staples |
| DLTR — Dollar Tree | 148.50 | -2.43% | Consumer Staples |
| GME — GameStop | 26.31 | -2.41% | Consumer Discretionary |

The day's leaderboard was the AI-and-memory complex: Sandisk +15.96%, Coherent +14.12%, Anthropic +10.98% (back above its $83 IPO price after two sessions below it), Micron +7.60% at 646.95 and Marvell +7.34% at 140.54. NVIDIA lagged the group at +0.80%. Micro-cap movers were far larger — the EOD universe's top regular-session gainer rose 58.8% — so the table above is the liquid set, not the whole tape.

### Watchlist EOD review

The published watchlist (`refs/watchlist.yaml`, fetched at run time) — price and day range from the bridge, after-hours from the TradingView scanner, volume against the average from cron #20's `avg_daily_dollar_volume`:

| Ticker | Close | Day change | Day range | Volume vs average | After-hours print |
|---|---|---|---|---|---|
| AAPL | 358.54 | +0.83% | 355.64 – 359.50 | 0.46x (22.7M sh) | 359.25 (+0.20%), range 358.00 – 359.37 |
| MSFT | 492.85 | +0.60% | 488.83 – 500.47 | 0.43x (12.5M sh) | 496.49 (+0.74%), range 492.00 – 496.49 |
| NVDA | 150.49 | +0.80% | 145.39 – 151.98 | 0.60x (185.8M sh) | 149.80 (-0.46%), range 149.36 – 150.80 |
| GOOGL | 274.96 | +0.68% | 270.03 – 279.52 | 0.53x (22.6M sh) | 275.95 (+0.36%), range 274.36 – 277.20 |
| AMZN | 254.12 | **+3.96%** | 248.45 – 255.28 | 0.55x (27.3M sh) | 255.05 (+0.37%), range 253.97 – 255.43 |
| IWM | 273.79 | +1.83% | 270.69 – 273.92 | n/a — ETF outside the EOD universe | 275.05 (+0.46%), range 272.50 – 275.08 |
| GLD | 334.40 | +2.12% | 331.26 – 334.41 | n/a — ETF outside the EOD universe | 334.99 (+0.18%), range 333.28 – 335.50 |
| TLT | 81.27 | **-1.18%** | 81.23 – 81.94 | n/a — ETF outside the EOD universe | 81.23 (-0.05%), range 81.11 – 81.39 |

Every watchlist name ran below its own dollar-volume average — the 0.43x–0.60x readings are a four-hour session's share of a full-day average, and should be read as such, not as an absence of volume. AMZN was the watchlist's best name on Black Friday (+3.96%); TLT was the only loser as rates backed up.

## Sector rotation

Eleven GICS sectors were ranked from the EOD universe on one row per `cap_source_symbol` (share-class duplicates collapsed onto the primary listing), with `EX_DISTRIBUTION` rows dropped and `NO_CAP`/`NO_SECTOR` rows excluded from the cap-weighted column: 4,359 usable rows, 4,336 of them cap-weighted and sector-tagged, covering **88% of the universe's priced names**. The six extremes are shown; the middle band ran +0.63% to +2.40%.

| Sector | Cap-weighted % | Median % | Sector ETF | ETF % | Gap |
|---|---|---|---|---|---|
| Information Technology | **+2.83** | +3.02 | XLK | +2.80 | +0.03pp |
| Consumer Discretionary | **+2.79** | +1.33 | XLY | +2.11 | **+0.68pp** |
| Materials | **+2.48** | +2.35 | XLB | +1.84 | **+0.63pp** |
| Consumer Staples | **+0.59** | +0.41 | XLP | +0.41 | +0.18pp |
| Health Care | **+0.46** | +1.04 | XLV | +0.28 | +0.18pp |
| Utilities | **+0.35** | +0.22 | XLU | +0.28 | +0.07pp |

**Two of the three leaders do not survive their own ETF cross-check, and the reason is a constituent, not a rotation.** Consumer Discretionary's cap-weighted +2.79% against XLY's +2.11% is a 0.68pp gap; strip Amazon (+3.97%, $2.74T cap) and Tesla (+5.24%, $1.58T) out and the sector prints **+0.83%** — 1.28pp *below* its ETF. The cap-weighted column for Consumer Discretionary is two mega-caps, not a sector move. Materials' +2.48% against XLB's +1.84% is the same story with a smaller cast: strip Newmont (+5.52%) and Southern Copper (+4.33%) and the sector prints **+2.05%**, only 0.21pp above the ETF — the gold and copper complex, not materials broadly. Information Technology is the clean one: **+2.83%** cap-weighted against XLK's **+2.80%**, a 0.03pp gap, and even excluding Anthropic (+10.98%, $1.21T cap) the sector holds **+2.42%**.

The laggards are a coherent, low-beta trio rather than a single weak sector: Staples +0.59%, Health Care +0.46%, Utilities +0.35% — three sectors that did not participate in the AI rebound, and all three inside 0.25pp of their own ETFs. Third-party sector leaderboards put Communication Services third on the day; this cap-weighted GICS ranking does not, at +1.56% against XLC's +1.99%. The difference is the weighting: Meta (+3.13%, $1.60T) and Alphabet (+0.70%, $3.36T) dominate the cap-weighted column.

## After-hours movers

The TradingView extended-hours screen, market cap above $1B and after-hours volume above 50,000 shares, run twice — descending and ascending — and ranked by absolute move. **`prior_close` is the 13:00 ET regular-session close**, because that is when Friday's shortened tape closed. Every row below passed the identity check `postmarket_change == (ah_last - prior_close) / prior_close` and carries a major-US-venue listing; no over-the-counter line appears in the table.

| ticker | prior_close | ah_last | ah_high | ah_low | ah_volume | gap_pct | ah_range_pct | gap_fill_level |
|---|---|---|---|---|---|---|---|---|
| TPL | 263.51 | 279.69 | 279.69 | 263.51 | 63039 | +6.14 | 6.14 | 263.51 |
| YPF | 31.85 | 32.99 | 33.59 | 31.85 | 308654 | +3.58 | 5.45 | 31.85 |
| VRDN | 38.82 | 40.00 | 40.00 | 38.48 | 225408 | +3.04 | 3.92 | 38.82 |
| SGI | 64.85 | 66.81 | 66.81 | 64.85 | 213202 | +3.02 | 3.02 | 64.85 |
| WSM | 212.86 | 219.02 | 219.02 | 212.02 | 92458 | +2.89 | 3.29 | 212.86 |
| EQPT | 16.29 | 15.41 | 16.32 | 15.34 | 126197 | -5.44 | 6.02 | 16.29 |
| QSR | 76.66 | 72.57 | 76.66 | 72.57 | 78453 | -5.34 | 5.34 | 76.66 |
| EC | 13.48 | 12.91 | 13.49 | 12.43 | 56098 | -4.23 | 7.86 | 13.48 |
| ARLO | 12.89 | 12.45 | 12.89 | 12.45 | 112406 | -3.41 | 3.41 | 12.89 |
| PPC | 29.47 | 28.50 | 29.47 | 28.50 | 66977 | -3.29 | 3.29 | 29.47 |

**Every one of these ten names closed its gap** — the after-hours low and high bracket the prior close in all ten rows, so `gap_fill_level` equals the prior close in each case and no row needs the midpoint fallback. That is itself the signal: the after-hours tape repriced and then came back to the cash close, which is what a quiet Friday after a four-hour session looks like.

The names: **TPL** Texas Pacific Land, **YPF** YPF SA sponsored ADR, **VRDN** Viridian Therapeutics, **SGI** Somnigroup International, **WSM** Williams-Sonoma, **EQPT** EquipmentShare.com, **QSR** Restaurant Brands International, **EC** Ecopetrol sponsored ADR, **ARLO** Arlo Technologies, **PPC** Pilgrim's Pride. TPL's move is the one with a sourced catalyst: it agreed to acquire EagleRock Land in an all-stock deal with an implied equity value of about $3 billion announced on 23 November, and it carries a $0.60 dividend with a 1 December ex-date. Yahoo's own quote confirms the scanner's TPL row to the cent — close 263.51 at 13:00:02 ET, after-hours 279.69 at 16:41:44 ET, +6.14%.

**EQPT is the session's sharpest reversal**: it closed the regular session up 10.07% at 16.29 and then gave back 5.44% after hours, printing a low of 15.34 before the close was recovered at 16.29. QSR is the widest loss on a thin book (78,453 shares) and ARLO and PPC are both single-print names.

**The screen's floor hides the session's real leaders.** Without the $1B market-cap floor the same screen returns moves the table above cannot show: **VESI +86.01%** (0.7634 → 1.420), **BGL +43.91%** (0.088 → 0.127), **PMVP +29.37%**, **EVRL +24.51%**, **LAES +24.09%** (1.370 → 1.700) on the way up, and **AMOD −37.35%** (1.020 → 0.639), **VWAV −30.59%**, **ZYN −21.81%**, **TRUG −15.81%**, **FIEE −13.36%** on the way down. The published table is the contract's screen, not the leaderboard.

## After-hours earnings reactions

**No S&P 500 company reported earnings after Friday's close**, and the broader after-hours earnings tape was thin: one S&P 500 constituent rose at least 2% after hours, three fell. Nothing on the watchlist reported after the close, so the watchlist's after-hours prints above are positioning, not reactions.

The names with sourced after-hours moves are **AMCR** (Amcor, 45.56 → 44.32, −2.72%) and **DGX** (Quest Diagnostics, 263.29 → 257.83, −2.07%) — and both agree to the cent with an independent after-hours feed, which is a useful validation of the scanner's extended-hours columns on this fire. **RVTY** (Revvity) and **EXE** (Expand Energy) do not: this scanner carries RVTY flat at its 151.27 close and EXE at +0.31% (87.72), while the independent feed shows RVTY +4.44% to 157.99 and EXE −3.83% to 84.10. The scanner's print is published as the source of record here and the other feed's numbers are named rather than blended.

Two after-hours reactions worth carrying: **MiniMed (MMED)** printed +2.87% after a session that saw it up 14.06% on an earnings beat, and **TPL**'s +6.14% is a deal, not an earnings reaction.

## Open research queue

1. **Is this an AI-led rebound or a short-covering bounce?** The S&P 500 gained 5.6% on the week — its best since April 2025 — after a week that lost roughly 12% in technology. Why it matters: a bounce built on short covering fades the moment the covering ends, and the equal-weight index still lags the cap-weighted one by 40bp, so the "breadth" is a narrowing penalty rather than a genuine broadening. What would resolve it: whether the penalty stays near +40bp on Monday and Tuesday or flips back toward the −100bp readings of the three prior sessions.
2. **Why did Texas Pacific Land reprice 6.14% after hours four days after the EagleRock deal was announced?** Why it matters: it is the only large-cap name in the after-hours tape with a large move, and on a Friday with no earnings season the after-hours print is the only fresh price signal available. What would resolve it: the Form 425 and the 8-K on the merger agreement, and whether the 1 December $0.60 dividend ex-date is entangled with the share-count mechanics of an all-stock deal.
3. **Does a four-hour session distort the volatility and volume reads?** Why it matters: the VIX fell 11.16% to 23.81 and the VXN 13.47% to 33.34 on a session that ran 09:30–13:00, with put/call at 0.83 and every watchlist name running at 0.43x–0.60x of its daily dollar-volume average. A short session produces fewer prints and thinner books, so both the volatility close and the volume comparisons are measured against a different day length than the rest of the archive. What would resolve it: Monday's full-length session — if the VIX holds below 23.81 on a full day, the compression is real; if it snaps back, Friday's close was a short-session artefact.

## Source health

| Source | Used for | Status |
|---|---|---|
| MCP bridge `market-recap` `get_quotes` / `price_history` | index, ETF, futures, watchlist, volatility levels, SPY/RSP history | ok — 16/16 and 6/6 symbols found; index closes confirmed dated 2026-11-27 |
| `probe_mcp.py` | MCP catalog | ok — `catalog_ok total=138 finance_tools=0`; no financial MCP registered, so the source ladder was used |
| TradingView america scanner (`tv_scan.py`, `TV_SCAN_V2`) | after-hours screen, watchlist after-hours | ok — 1,588-name screen pulled twice (gainers, losers), every row identity-checked, no over-the-counter rows in the published table |
| cron #20 `us-eod/2026-11-27.csv` (outputs repo, `main`) | participation read, sector rotation, universe movers, volume averages | ok — 4,902 rows, 4,826 priced |
| CBOE daily statistics page | total and component put/call ratios | ok — `selectedDate` and `prevTradingDay` both 2026-11-27; six ratios read from the one payload |
| CBOE `VIX_History.csv` / `VXN_History.csv` | volatility close cross-check | ok — agree with the bridge to the cent on 2026-11-27 |
| `refs/watchlist.yaml` (outputs repo, `main`) | watchlist EOD review | ok — 8 names fetched at run time |
| Web: EarningsWhispers, StockTitan, ATLAS, EarningsMadness | Monday earnings calendar | degraded — vendors disagree materially on the count (10 / 11 / 33 / 15 / 1); the intersection of two or more sources is published and the disagreement disclosed |
| Web: press sweep (AP, Investopedia, Barron's, StockAnalysis, CNBC, Nexqual, WiseView, MarketBeat) | session story, mover catalysts, after-hours context | ok — session figures corroborated across four independent outlets |
| CME equity-index futures (via bridge) | tomorrow's setup, futures leg | **degraded** — every futures row is stamped 13:14:59 ET, the shortened session's own close; CME's week ended Friday and Globex reopens Sunday 18:00 ET, so no overnight print exists to publish |
| Asian cash markets | tomorrow's setup, Asia leg | **degraded** — Asia is closed for the weekend (it reopens Sunday 18:00 ET); no Nikkei or Kospi leg is available, so it is published as absent rather than guessed |

**Coverage notes.** The after-hours table's screen keeps names above $1B of market cap, so the session's actual leaderboard is materially larger — VESI +86.01% and AMOD −37.35% sit outside it, and are listed above rather than published as the tape. The participation and sector columns come from cron #20's universe and are therefore comparable with that archive's published breadth; the ETF cross-checks are a different population (11 ETFs). Twenty-one rows carry `NO_SECTOR` and are excluded from the sector ranking as a bucket, not a sector — they would otherwise land at −0.32% and displace Utilities from the bottom three. Volume-versus-average for IWM, GLD and TLT is `n/a` because the three ETFs sit outside cron #20's equity universe; no average was inferred. The scanner's TPL close of 263.51 agrees with Yahoo's own quote page to the cent, while cron #20's CSV prints TPL at 264.20 — the scanner's value is published because it is the one the after-hours identity check reconciles against. Two after-hours prints (RVTY, EXE) disagree materially with an independent after-hours feed and are named rather than blended.

## Method notes

- **The session was four hours long.** The equity tape closed at 13:00 ET and the bond market at 14:00 ET. Every "close" in this brief is that 13:00 ET print, and every after-hours `prior_close` is the same print. Volatility and volume comparisons against a full-day archive are consequently weaker on this day than on a normal session.
- **The cap-weighted sector column inherits concentration.** Consumer Discretionary's cap-weighted return is Amazon plus Tesla; Materials' is Newmont plus Southern Copper. Both sectors are published with and without those names, and the sector-ETF gap is published next to the cap-weighted number rather than left implicit.
- **Volatility indices are read from the dated history, not from quote rows**, and are cross-checked against CBOE's own dated close files. A quote row for a volatility index can carry the prior session's reading while every other symbol in the same call is correct.
- **The after-hours print is a snapshot as of the fire**, not a settled close — the extended-hours tape keeps moving, and vendors disagree (RVTY and EXE). The scanner's print is the source of record; other vendors' numbers are named.
- **The futures change is published against two denominators**, the prior settlement and the cash index close, and judged on the cash close. A stale settlement presented as an overnight setup would be a fabricated setup, and on this Friday there is no overnight at all.
- **`gap_fill_level` follows the contract's deterministic rule**: the prior close where the after-hours range brackets it (all ten rows here), otherwise the after-hours midpoint.
- **The participation population is cron #20's EOD universe** for the four names-based metrics and the $2B-floor liquid subset for the ratio; the cap-weight penalty comes from the bridge's `price_history` for SPY and RSP, so it is not a universe-derived figure.
- Read-only throughout. No trades are placed and no positions are sized.
