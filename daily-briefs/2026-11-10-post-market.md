---
date: 2026-11-10
cron: 23-agentic-post-market-brief
contract: postmkt-artifact-v2
fire_time_et: 22:30
snapshot_et: 22:30-22:52
session: 462089783816555
scheduled_at_ms: 1794367817882
status: ok
source: MCP-over-HTTP bridge (market-recap get_quotes + price_history); TradingView public scanner (america/scan); cron #20 us-eod/2026-11-10.csv; CBOE daily statistics; web (CNBC, Bloomberg, Investopedia, StockTitan, Reuters via Yahoo)
primary_source: MCP-over-HTTP bridge market-recap (keyless Yahoo-sourced) for every regular-session close, the futures set and the SPY/RSP history
universe: cron #20 us-eod/2026-11-10.csv — 4,893 rows; 4,521 names after dropping EX_DISTRIBUTION rows and de-duplicating share classes on cap_source_symbol; 4,432 of those carry a change_pct
degraded_sources: 2
---

# Post-market brief — Tuesday, 10 November 2026

## TL;DR

The tape was red, and it was red in the rate-sensitive corner. A hotter-than-expected October CPI print — headline **+0.4% m/m** against +0.3% expected and core **+0.3%** against +0.2% — pushed the 10-year Treasury through 5.00% and left the S&P 500 **-0.38%**, the Nasdaq Composite **-0.74%** and the Russell 2000 **-0.68%**. The participation read confirms it was broad, not cosmetic: **advancers 1,608** against **decliners 2,818** in the 4,432-name priced universe, **median_name_move_pct -0.53%**, **liquid_adv_dec_ratio 0.77**, and **cap_weight_penalty_bp -34** (SPY -0.37% against RSP -0.03%) — a *negative* penalty, so the equal-weight index beat the cap-weighted one and the damage was worse outside the mega-caps.

Two things broke the session, and only one of them was macro. Nvidia closed **-5.47% at $168.89** on 429m shares (2.5x its 10-day average) as *The Information* reported that the relationship at the centre of the board's independent review may have moved at least $7.5bn of chips to Chinese firms; AMD +1.30% and Broadcom +3.91% rose, so this was a key-person and governance repricing, not a demand repricing. The Fed was the other: December 8-9 is now priced for a 25bp hike with a 13.6% chance of 50bp, after Governor Waller said a half-point should be "on the table" if core printed 0.3%.

The after-hours tape found its own leadership, and it is AI infrastructure rather than the megacaps: **CRWV +7.90%** on a Q3 revenue beat and a raised 2026 guide, **NBIS +8.40%**, **AZTA +9.19%** on an EPS beat. The damage prints ran the other way — BV -15.75%, ATRO -10.97%, HGTY -10.39%. And the futures are the setup, not the cash close: at 22:21 ET **ES +0.55% and NQ +1.21%**, the Nasdaq leading the rebound, with the 10-year bond future slightly lower (yields marginally higher) even as equities bid.

## Tomorrow's setup — Wednesday, 11 November 2026

### Futures and the overnight setup

| Contract | Last | Change | Session high | Session low | as_of (ET) | State |
|---|---|---|---|---|---|---|
| ES=F (E-Mini S&P, Dec 26) | 7,585.50 | +0.55% | 7,587.50 | 7,547.50 | 22:21 | open (Globex) |
| NQ=F (Nasdaq 100, Dec 26) | 28,173.25 | +1.21% | 28,184.25 | 27,847.75 | 22:21 | open (Globex) |
| YM=F (Mini Dow, Dec 26) | 52,458 | +0.27% | 52,475 | 52,343 | 22:21 | open (Globex) |
| RTY=F (E-mini Russell 2000) | 2,838.30 | +0.33% | 2,839.00 | 2,829.40 | 22:21 | open (Globex) |
| ZN=F (10-Year T-Note, Dec 26) | 106-094 | -0.15% | 106-188 | 106-031 | 22:21 | open (Globex) |

**The overnight move is in the data.** Every futures row carries `as_of` at 22:21 ET — nine minutes before the fire — so this is a live Globex print, not the prior session's 16:00 settlement, and it is not the stale-settlement trap the skill warns about. The shape: **NQ +1.21% versus ES +0.55%** is a tech-led bounce after a session in which tech was the thing that broke, and the small-cap future (RTY +0.33%) lags both. The bond future is the tell that has not turned — ZN -0.15% means yields are still marginally higher, so this is a risk bounce, not a rates relief rally. The equity after-hours tape agrees with the futures: SPY +0.35% and QQQ +0.66% after the close.

One caveat on the after-hours numbers below: the TradingView `postmarket_*` columns carry the 16:00-20:00 ET extended-hours session. The overnight ATS that follows trades separately — Nebius, for example, printed $145.25 at the 20:00 ET extended-hours close and $147.95 (+10.41%) on Blue Ocean at 21:58 ET. The table is the 20:00 ET book, not the overnight book.

### Economic calendar

- **Fed speakers from the overnight.** Governor Schmid and Governor Bowman are both on the calendar. After Waller's "more robust action" remarks and a 0.3% core print, this is the day's dominant macro risk — a hawkish push would reopen the bond sell-off that drove today's tape.
- **13:45 ET — ADP weekly employment change.** A single-week labour read against a Fed that has just been repriced for a hike.
- **08:00 ET — MBA mortgage applications** (prior: 192.6 index; 30-year mortgage rate 7.3%).
- **The US bond market is CLOSED tomorrow for Veterans Day.** No Treasury supply, no rate discovery in Treasuries on Wednesday. That is a genuine setup constraint: the rates channel that drove today cannot be expressed in the bond market tomorrow, so it will express in equities instead. The next bond events are Thursday's 30-year auction and Friday's PPI.
- **Overseas:** German final CPI (07:00 ET), Italian industrial production (09:00 ET), Chinese vehicle sales (07:30 ET), and Japanese PPI lands 18:50 ET tomorrow — after the US close.
- **Stocks trade normal hours tomorrow.** Veterans Day is a federal holiday but not an equity-market holiday.

### Earnings calendar

52 US companies above $300m of market cap report on Wednesday — 13 before the open, 36 after the close.

| Name | Market cap | Timing | EPS est. | Why it matters |
|---|---|---|---|---|
| FNV (Franco-Nevada) | $49.4B | after close | $1.73 | The gold royalty complex's first read after GLD -2.68% |
| VYLR (Vylor) | $48.6B | after close | -$0.52 | Largest scheduled print by market cap |
| GIB (CGI Inc.) | $17.0B | before open | $2.30 | Pre-open macro-adjacent IT spend |
| TTEK (Tetra Tech) | $10.4B | after close | $0.47 | Infrastructure services; rate-sensitive read |
| CAE (CAE Inc.) | $8.9B | after close | $0.26 | Defence/aerospace |
| CTVA (Corteva) | $8.1B | after close | $0.10 | Farm-input economics against a 4% headline inflation print |
| ENS (EnerSys) | $5.4B | after close | $3.18 | Also reported an estimate for 10 November |
| ERAS (Erasca) | $5.4B | after close | -$0.13 | Biotech, high implied move |

**No watchlist name reports tomorrow.** The nearest watchlist catalyst is Nvidia on **17 November** (Q3 FY2027).

### News to watch for the top movers

- **NVDA -5.47% to $168.89** (the day's heaviest name, 429m shares). The board's independent review of the chief executive's relationship with a Chinese national escalated when *The Information* reported that at least $7.5bn of hardware may have shipped to Chinese firms through a network linked to her — Reuters says it could not independently verify. Citi cut its target to $285 from $315 while keeping Buy, citing gross-margin pressure from HBM pricing. Two dated catalysts: **the chief executive has until Wednesday to answer three House committees' briefing request**, and **Q3 FY2027 results land 17 November**. The after-hours print of $170.48 (+0.94%) is the market's first reaction to the escalation.
- **MSFT -2.20% to $533.16** on 26.9m shares, below average. The driver was competitive rather than operational: Anthropic launched Claude Sheets, Whiteboards and Data, reopening the productivity-suite fight. Microsoft separately pressed the administration to drop a planned ban on Chinese optical transceivers. This is an AI-app de-rating, not a demand event.
- **AAON +19.31% to $75.01** — record Q3 revenue $707.4m and non-GAAP EPS $0.83, both well ahead of consensus, with the FY2026 sales-growth outlook raised to 72-75%. The asterisk: the same filing discloses a $10.7m revenue restatement and a material weakness in financial reporting, and the stock is giving some of it back after hours.
- **CHTR +10.61% to $134.06** — a $1.5bn tender offer for eight series of long-dated notes below face value, on top of a new operating model targeting $2bn of annualised savings. Q3 carried a $6.33bn franchise impairment and an adjusted loss of $20.50 per share against a +$8.50 estimate, so the rally is a balance-sheet and cost-structure trade, not an earnings trade.
- **HIMS -16.61% to $19.13** — the largest liquid decliner. Q3 revenue $890.4m (+49% y/y) narrowly missed $892.77m, the company swung to a $33.0m net loss (-$0.14 per share) against a +$0.06 expectation, gross margin compressed to 57% from about 64%, and FY2026 adjusted EBITDA guidance was cut to $257-277m from $275-325m. Subscribers fell about 100,000 sequentially to 2.8m. Jefferies cut its target to $24 and warned of "heightened gyrations" from the GLP-1 demand environment.

### Tomorrow's three things to watch

- **CRWV — 52.58 after-hours print, 48.73 gap-fill level** — Q3 revenue $3.66B beat against $3.56B estimated, +168% y/y, and a raised 2026 revenue guide of $13-13.3B; management appears on television at 9:00 am ET. The gap already traded through the prior close, so 48.73 is the level that fills it.
- **NVDA — 168.89 prior close, 170.48 after-hours print** — the board's independent review has to answer three House committees by Wednesday, and Q3 FY2027 results land on 17 November. If the overnight bid holds the 168.89 close into the open, the key-person premium is being treated as a contained risk; if it does not, the 10% two-day slide continues.
- **CTVA — 12.17 close** — reports after the close on Wednesday with EPS estimated at $0.10; the corn and fertiliser read-through from a 0.4% headline inflation print is the tell.

## Day's tape

### Market read

| metric | value | how it is measured |
|---|---|---|
| `advancers` | 1,608 | names closing higher in the 4,432-name priced universe |
| `decliners` | 2,818 | names closing lower |
| `unchanged` | 6 | names closing flat |
| `median_name_move_pct` | -0.53% | median of `change_pct` across the universe |
| `cap_weight_penalty_bp` | -34 | SPY -0.37% minus RSP -0.03%, in basis points (signed: negative = cap-weighted lagged equal-weight) |
| `liquid_adv_dec_ratio` | 0.77 | advancers 702 : decliners 909 in the $2bn+ liquid set (1,611 names) |

The read in words: the median name fell more than the S&P 500's equal-weight proxy did (RSP -0.03% against a universe median of -0.53%), so the softness was worst in the small and mid-cap tail even though the headline index loss was only 0.38%. The negative `cap_weight_penalty_bp` is the day's signature — mega-cap leadership was the liability, not the support.

### Cap-weight penalty — 5-day history

| Session | SPY % | RSP % | cap_weight_penalty_bp |
|---|---|---|---|
| 2026-11-04 | +1.65 | +1.86 | -20 |
| 2026-11-05 | -4.41 | -2.89 | -152 |
| 2026-11-06 | +0.31 | -0.38 | +69 |
| 2026-11-09 | +2.37 | +2.27 | +10 |
| 2026-11-10 | -0.37 | -0.03 | -34 |

Today's -34bp is the second-most-negative reading of the five, behind only the 2026-11-05 capitulation. The five-session pattern is a two-way swing: two days of mega-cap leadership (+69, +10) bracketed by three days of mega-cap drag (-20, -152, -34).

### Index, ETF and volatility levels

| Instrument | Close | Change | Day high | Day low | as_of (ET) |
|---|---|---|---|---|---|
| S&P 500 | 7,520.93 | -0.38% | 7,543.92 | 7,470.43 | 17:00 |
| Nasdaq Composite | 25,065.88 | -0.74% | 25,286.83 | 24,816.10 | 17:16 |
| Dow Jones Industrial Average | 52,231.89 | -0.30% | 52,316.89 | 51,977.08 | 17:00 |
| Russell 2000 | 2,821.38 | -0.68% | 2,826.54 | 2,799.25 | 16:30 |
| Nasdaq 100 | 27,740.80 | -0.60% | 27,990.34 | 27,421.18 | 17:16 |
| PHLX Semiconductor | 9,998.33 | -0.35% | 10,197.21 | 9,777.17 | 17:16 |
| SPY | 749.92 | -0.37% | 752.14 | 744.87 | 16:00 |
| QQQ | 674.76 | -0.68% | 680.95 | 667.05 | 16:00 |
| IWM | 280.58 | -0.68% | 281.33 | 277.91 | 16:00 |
| DIA | 521.73 | -0.31% | 522.59 | 519.19 | 16:00 |
| RSP | 220.88 | -0.03% | 221.15 | 218.90 | 16:00 |
| SMH | 483.63 | -0.78% | 492.74 | 474.03 | 16:00 |
| VIX | 19.46 | -2.31% | 21.61 | 19.29 | 16:15 |
| VXN | 28.97 | -14.84% | 32.34 | 29.11 | **16:00 on 2026-11-09 (stale)** |

The volatility line is the surprise: **VIX closed at 19.46, down 2.31%, having traded as high as 21.61** — the index went up 11% intraday and then round-tripped to *lower* on the day while the market fell 0.38%. That is a positioning signature, not a fear signature: the sellers were not paying up for protection, and the day's largest single-name losses (HIMS -16.61%, HGTY, BV) were idiosyncratic, not macro-driven. **The VXN reading is from the 9 November session** (its `as_of` is 16:00 ET on 2026-11-09) and is published for completeness only; the 10 November VXN close was not available from the source. Do not read the -14.84% as today's Nasdaq-vol move.

### Cross-asset

- **10-year Treasury ~4.99%** (up 13bp on the day, trading above 5.00% intraday), 2-year ~4.736% (up more than 18bp), 30-year ~5.352% (up more than 9bp). The 10-year last traded above 5% earlier in the month; in October 10-year and 30-year yields hit 24-year highs. A mediocre $42bn Treasury note auction compounded the bond decline.
- **Gold fell -2.68% (GLD to 369.36) on a hot inflation print.** That is the counterintuitive one — a hawkish inflation surprise usually supports the metal, and it did not. The rate channel dominated the haven bid, which is a genuine read on positioning: nobody treated this as a flight-to-safety session.
- **Bonds sold off too (TLT -1.32% to 80.88).** Stocks and Treasuries fell together, which is a policy-tightening signature rather than a growth-scare signature — the market repriced the Fed, not the economy.
- WTI crude was down about 0.5% near $86.50, extending the prior day's decline to levels last seen in late August.

### Day's movers

Liquid set (market cap above $2bn), top three each way:

| Ticker | Move | Close | Cap | Sector | Driver |
|---|---|---|---|---|---|
| AAON | +19.31% | 75.01 | $6.1B | Industrials | record Q3 revenue $707.4m, EPS $0.83, FY2026 outlook raised |
| CHTR | +10.61% | 134.06 | $24.0B | Communication Services | $1.5bn tender offer for long-dated notes; $2bn cost programme |
| ACAD | +10.79% | 18.28 | $3.1B | Health Care | Q3 beat |
| HIMS | -16.61% | 19.13 | $4.4B | Health Care | Q3 loss, gross margin to 57%, EBITDA guidance cut |
| EQPT | -16.50% | 13.53 | $3.4B | Industrials | no catalyst sourced in this run |
| LEGN | -15.97% | 20.41 | $3.8B | Health Care | no catalyst sourced in this run |

Beyond the liquid set the session's extremes were microcaps: PEPG +92.89%, TTEC +72.04%, ZIP +53.61% on a Q3 beat and a capital-return plan (with a law-firm investigation announced on 10 November), against NXXT -92.85%, IHRT -65.03% and MVST -64.34%. The day's heaviest names by turnover were NVDA ($26.6bn average daily dollar volume), MU ($26.9bn), SPCX ($15.5bn), AAPL ($15.4bn) and META ($14.8bn).

### Watchlist EOD review

| Ticker | Close | Day change | Day range | Volume | Rel. volume (10d) | After-hours print |
|---|---|---|---|---|---|---|
| AAPL | 348.51 | -0.62% | 346.46 - 353.87 | 29.73m | 0.52 | 348.80 (+0.08%) |
| MSFT | 533.16 | -2.20% | 526.37 - 544.15 | 26.91m | 0.83 | 534.81 (+0.31%) |
| NVDA | 168.89 | -5.47% | 165.89 - 174.65 | 429.27m | 2.48 | 170.48 (+0.94%) |
| GOOGL | 287.38 | -0.27% | 285.68 - 292.02 | 28.40m | 0.51 | 289.18 (+0.63%) |
| AMZN | 270.87 | +1.48% | 266.14 - 272.88 | 38.97m | 0.62 | 271.95 (+0.40%) |
| IWM | 280.58 | -0.68% | 277.91 - 281.33 | 21.53m | 0.81 | 281.30 (+0.26%) |
| GLD | 369.36 | -2.68% | 367.80 - 371.88 | 7.84m | 0.83 | 369.45 (+0.02%) |
| TLT | 80.88 | -1.32% | 80.55 - 81.17 | 40.46m | 1.16 | 80.86 (-0.02%) |

The watchlist tells one story: **three of the five mega-caps fell on light volume** (AAPL 0.52x, GOOGL 0.51x, MSFT 0.83x) while the one that broke, NVDA, traded 2.48x its average. That is the difference between a market being repriced by rates and a single name being repriced by its own news. The one watchlist name that worked was AMZN (+1.48%), and it is the largest single constituent in its sector — 36.4% of the consumer-discretionary cap-weighted return, +0.54pp of a +0.34% sector return.

## Sector rotation

Cap-weighted on the de-duplicated universe, ranked, with the sector ETF cross-check and the gap published.

| Rank | Sector | Cap-weighted % | Median % | Sector ETF | ETF % | Gap (pp) | Dominant constituent |
|---|---|---|---|---|---|---|---|
| 1 | Energy | **+0.46%** | +0.04% | XLE | +0.44% | +0.02 | LNG +2.98% (2.0% wt, +0.06pp) |
| 2 | Consumer Discretionary | **+0.34%** | -0.95% | XLY | +0.03% | +0.31 | AMZN +1.49% (36.4% wt, +0.54pp) |
| 3 | Financials | **+0.28%** | -0.28% | XLF | +0.52% | -0.24 | BRK-B +1.40% (12.1% wt, +0.17pp) |
| ... | | | | | | | |
| 9 | Utilities | **-0.24%** | -0.09% | XLU | -0.14% | -0.10 | CEG -3.02% (6.4% wt, -0.19pp) |
| 10 | Materials | **-1.06%** | -1.12% | XLB | -0.17% | **-0.89** | NEM -4.19% (7.8% wt, -0.33pp) |
| 11 | Information Technology | **-1.31%** | -0.73% | XLK | -1.15% | -0.16 | NVDA -5.49% (16.4% wt, -0.90pp) |

**Materials is a constituent effect, not a rotation.** The cap-weighted read of -1.06% against XLB's -0.17% is a 0.89pp gap, well past the 0.5pp threshold, so both numbers are published: **Materials is -1.06% with the miners and -0.35% without NEM, SCCO and FCX**, whose individual moves (-4.19%, -3.21%, -3.24%) account for -0.78pp of the sector's cap-weighted return between them. The sector ETF, not the cap-weighted column, is the honest description of the sector's day: a broad, quiet materials tape with three large miners sold off on commodity news.

**Information Technology is the day's real story, and it is narrower than -1.31% suggests.** Ex-NVDA the sector is -0.49%, so Nvidia alone contributed -0.90pp of the -1.31%. The ETF cross-check (XLK -1.15%) sits inside the gap threshold, so the tech weakness was real rather than an artefact of Nvidia's weight — but the size of it was a function of one name's governance crisis.

**Consumer Discretionary passes the gap test (+0.31pp) but inherits a concentration**: AMZN is 36.4% of the sector's cap, and ex-AMZN the sector is **-0.32%**, not +0.34%. Consumer discretionary was not up today; Amazon was up today.

**Financials** at +0.28% cap-weighted against XLF +0.52% is a Berkshire effect: ex-BRK the sector is +0.13%, so Berkshire's +1.40% contributed +0.17pp.

**Energy** is the only sector with a positive median (+0.04%) and it reconciles cleanly with XLE (+0.44%) — the one sector that worked for reasons other than one constituent.

Coverage note: 105 universe rows carry no sector assignment and 241 rows carry no market cap. The former are excluded from this ranking (and are not a sector); the latter cannot be cap-weighted and are excluded from every cap-weighted column here.

## After-hours movers

TradingView public scanner, US equities with market cap above $1bn and after-hours volume above 50,000 shares, run once sorted by gain and once by loss, then ranked by absolute move. Every row was checked against the scanner's own identity (`postmarket_change` equals `(postmarket_close - close) / close x 100`); all 500 rows returned passed and no row was dropped. After-hours prints are the 16:00-20:00 ET session.

**Gainers**

| ticker | prior_close | ah_last | ah_high | ah_low | ah_volume | gap_pct | ah_range_pct | gap_fill_level |
|---|---|---|---|---|---|---|---|---|
| AZTA | 40.48 | 44.20 | 44.20 | 39.99 | 111,365 | +9.19% | 10.40% | 40.48 |
| NBIS | 134.00 | 145.25 | 145.30 | 133.55 | 2,648,443 | +8.40% | 8.77% | 134.00 |
| CRWV | 48.73 | 52.58 | 54.00 | 46.50 | 27,367,822 | +7.90% | 15.39% | 48.73 |
| NN | 8.40 | 8.98 | 9.40 | 8.40 | 577,538 | +6.85% | 11.90% | 8.40 |
| ESAB | 87.13 | 92.99 | 92.99 | 87.13 | 200,154 | +6.73% | 6.73% | 87.13 |

**Losers**

| ticker | prior_close | ah_last | ah_high | ah_low | ah_volume | gap_pct | ah_range_pct | gap_fill_level |
|---|---|---|---|---|---|---|---|---|
| BV | 11.43 | 9.63 | 11.43 | 8.95 | 345,902 | -15.75% | 21.70% | 11.43 |
| ATRO | 62.00 | 55.20 | 64.00 | 51.40 | 187,903 | -10.97% | 20.32% | 62.00 |
| HGTY | 16.94 | 15.18 | 16.94 | 15.18 | 203,706 | -10.39% | 10.39% | 16.94 |
| GO | 14.02 | 12.96 | 14.02 | 12.34 | 652,626 | -7.56% | 11.98% | 14.02 |
| RGTI | 12.15 | 11.32 | 12.17 | 10.94 | 4,313,217 | -6.83% | 10.12% | 12.15 |

`gap_fill_level` follows the deterministic rule: where the after-hours range straddles the prior close (AZTA, NBIS, CRWV, NN, ESAB, BV, ATRO, HGTY, GO, RGTI — all ten), the gap fills at the prior close, so the prior close is the level to mark. Every one of these names traded back through its 16:00 close, which is itself the signal: the after-hours session was a two-way auction, not a clean drift in either direction.

**The screen has a $1bn floor, and the floor hides the session.** On the same screen with the market-cap filter removed, the actual after-hours leaders were **OMH +48.24%** ($35m cap), **HUHU +45.28%** ($11m cap), **FOSL +23.00%** and **GEVO +15.11%** on the gain side, and **STAK -56.05%** ($49m cap), **LWLG -28.26%**, **BYAH -27.69%** and **NXXT -24.93%** on the loss side. The table above is not the whole after-hours tape and must not be read as such.

Two names in the table need a note rather than a story: **AZTA** traded only 111,365 shares after hours on a 9.19% move, so the print is thin; **ESAB**'s 6.73% has no sourced catalyst in this run — it follows a 4 November Q3 EPS miss and two price-target trims on 10 November (Evercore ISI to $99, In Line; Roth to $130, Buy). The move is published without an explanation because none was found.

## After-hours earnings reactions

- **AZTA +9.19% to 44.20.** Q4 FY2026 EPS $0.28 against $0.11 estimated; revenue $167.1m against $160.3m estimated. A beat on both lines, but on 111k shares of after-hours volume.
- **CRWV +7.90% to 52.58.** Q3 EPS -$0.95 against -$1.21 estimated; revenue $3.66b against $3.56b estimated, +168% y/y; the 2026 revenue guide was raised to $13-13.3b and the 2026 adjusted operating-income forecast also beat. The print has ranged $46.50-$54.00 — a 15.39% range on a $26.9b market cap. StockTitan read it at +2.59% at 18:07 ET, so the stock made its highs well after the first reaction.
- **RGTI -6.83% to 11.32.** Q3 EPS -$0.06, in line; **revenue $1.4m against a $3.5m estimate** — a 60% miss on the line that matters for a quantum-hardware pre-revenue name. The stock was -8.40% at 18:07 ET and improved into the close of the extended session. The Cepheus system reached its accuracy goal, and it was not enough.
- **ATRO -10.97% to 55.20.** EPS $0.81 against $0.71 estimated and revenue $271.7m against $268.2m estimated — a beat on both lines that sold hard. The guidance or cost detail behind it is not in the sources read here, so no reason is asserted.
- **GO -7.56% to 12.96.** EPS $0.16 against $0.15 estimated and revenue $1.18b against $1.17b estimated, after a +1.08% regular session.
- **NN +6.85% to 8.98.** EPS -$0.04 against -$0.11 estimated; revenue $1.6m against $1.0m estimated.
- **FRNM +6.04% to 11.42.** EPS $1.10 against $0.40 estimated; revenue $183.5m against $105.8m estimated.
- **ALC -5.48% to 70.00.** Alcon reported after the close; no estimate comparison was sourced in this run.
- **FOSL +23.00%.** Not an earnings print — the watchmaker extended its global licensing agreement with Diesel by five years, through 2032.
- **GEVO +15.11%.** Record Q3 revenue of $83m against $43m a year earlier, and net income of $23m, including about $29.4m from Canadian clean-fuel credits.
- **COST +1.58% after hours** on a declared special dividend of $30 a share.
- **STAK -56.05% to 2.16** after a +20.17% regular session. No catalyst was sourced in this run and none is asserted.

The 10 November after-close roster was large — 89 to 147 companies depending on the calendar — with CoreWeave, Rigetti, Grocery Outlet, Alcon, Petrobras and Ecopetrol the liquid names.

## Open research queue

1. **Is the after-hours neocloud bid a leadership change or a short-covering bounce?** CoreWeave +7.90% and Nebius +8.40% after hours, with Iren up about 2% — but both are 55-72% below their June highs, and the entire bid sits against a hot-CPI rate shock that the bond market cannot even price tomorrow because it is closed for Veterans Day. *Why it matters:* it is the only leadership candidate the tape has left once Nvidia has de-rated, so if it is real the market has a new sponsor; if it is a bounce, tomorrow's open hands back a -5.47% gap and the tape has no leadership at all. *What would resolve it:* whether the bid survives the cash open, the Nebius Q3 print on 12 November, and the CoreWeave management appearance on the morning of 11 November.
2. **Is December a 25bp hike or a 50bp hike?** The market prices a 25bp move with a 13.6-17% chance of 50bp, and Governor Waller put 50bp "on the table" explicitly. *Why it matters:* the entire 2027 tightening path is being repriced off one data point and two speakers' remarks, and the 10-year at 4.99% with the 30-year at 5.352% leaves no cushion for a second hot print. *What would resolve it:* the Fed speakers on 11 November, Friday's PPI, and the PCE report later in November — Logan has already said she sees two more quarter-point increases.
3. **Why did the median name (-0.53%) fall further than the large-cap equal-weight index (-0.03%)?** The participation read says the damage was concentrated in the small and mid-cap tail, where the median lives, even as the equal-weight mega-cap proxy was almost flat. *Why it matters:* it decides whether "the index was down 0.38%" is an honest summary of the day or a flattering one, and it determines whether the -34bp cap-weight penalty is a mega-cap story or a tail story. *What would resolve it:* whether IWM and RSP hold their after-hours gains (+0.26% and +0.35%) into Wednesday, and a breakdown of the 2,818 decliners by market cap band, which this run does not carry.

## Source health

| Source | Endpoint / query | Status |
|---|---|---|
| MCP bridge, market-recap `get_quotes` | `^GSPC,^IXIC,^DJI,^RUT,^VIX,^VXN,^NDX,^SOX,SPY,QQQ,IWM,DIA,RSP,SMH,GLD,TLT` plus a futures batch and single-name batches | ok — 16/16 and 5/5 found; **VXN is stale (2026-11-09)**, all other rows carry 2026-11-10 as_of |
| MCP bridge, market-recap `price_history` | `SPY,RSP` 2026-10-29 to 2026-11-10 | ok — 9 sessions for both symbols |
| MCP bridge, market-recap `get_quotes` (watchlist and movers) | 8 watchlist names + 16 single names | ok — 8/8 and 16/16 found |
| TradingView public scanner | `POST https://scanner.tradingview.com/america/scan`, `postmarket_*` columns, cap floor $1bn and no floor | ok — 2,110 names matched the floored screen (250 gain + 250 loss pulled), 2,785 on the unfloored screen; 500/500 rows passed the change identity |
| cron #20 EOD universe | `minimax-cloud-outputs` `us-eod/2026-11-10.csv` | ok — 4,893 rows; 4,521 after EX_DISTRIBUTION removal and share-class de-duplication; 241 rows carry no market cap, 105 carry no sector |
| CBOE daily statistics | `https://www.cboe.com/us/options/market_statistics/daily/` | **degraded — the embedded data carries no session date stamp.** Total put/call 0.95 (put volume 6,319,117 vs call volume 6,632,948), equity 0.77, index 1.02, as read. The session it describes cannot be dated with certainty |
| Web — macro and catalysts | CNBC, Bloomberg, Investopedia, StockTitan, Reuters/Yahoo, Hilltop Securities, StoneX, Schwab | ok — every catalyst in this brief is sourced; no catalyst was inferred |
| MCP availability probe | `probe_mcp.py` | ok — `catalog_ok total=135 finance_tools=0`, bridge packs tradier/fmp/market-recap |

**degraded_sources: 2** — the undated CBOE put/call session, and the stale VXN row.

Concentration inherited by the cap-weighted column: consumer discretionary is 36.4% Amazon, information technology 16.4% Nvidia, financials 12.1% Berkshire, industrials 21.1% SpaceX. Every one of those is a single-name outcome, and the sector table publishes each sector both with and without its dominant constituent for that reason.

## Method notes

- **This brief is post-market, so its product is tomorrow.** `## Tomorrow's setup` is section 2 of 10 and carries the futures, the economic calendar, the earnings roster, the news to watch and the three things to watch; the day's tape follows it.
- **Regular-session prices, the futures set and the SPY/RSP history all come from one source**: the MCP-over-HTTP bridge (`market-recap`, keyless Yahoo-sourced). Where the TradingView scanner carries the same field, the scanner's value was not published alongside it — one number per field, one source per field.
- **Participation metrics use one population**: the cron #20 universe after dropping `EX_DISTRIBUTION` rows and de-duplicating on `cap_source_symbol` (preferring the primary listing over a `CAP_CARRIED` row, so Berkshire B and Alphabet A carry the parent cap once). That is 4,521 names, of which 4,432 carry a `change_pct`. The liquid set is the same universe filtered to market cap above $2bn.
- **`cap_weight_penalty_bp` is signed and self-verifying**: SPY's `daily_return_pct` minus RSP's, times 100, rounded to the nearest basis point. Today: (-0.368 - (-0.032)) x 100 = -34.
- **`gap_fill_level` is deterministic**: where the after-hours range straddles the 16:00 close, the gap fills at the prior close; otherwise the reference is the after-hours midpoint. All ten published rows fall in the first case.
- **The after-hours movers table was verified row by row** against the scanner's own identity before publication. No row was dropped; the 500 rows checked all passed.
- **The $1bn market-cap floor is a screen, not the tape.** The unfloored leaders are published in `## After-hours movers` and in `## Source health` so the table is never mistaken for the whole session.
- **A catalyst is only stated where it was sourced.** ESAB's +6.73%, EQPT's -16.50%, LEGN's -15.97% and STAK's -56.05% carry no asserted reason because none was found in the sources read.
- The put/call ratio's equity and index components are published because the same page sourced both and they reconcile with the total; no split from a second, disagreeing source was invented.
