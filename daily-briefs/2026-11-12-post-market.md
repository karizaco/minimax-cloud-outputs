---
date: 2026-11-12
cron: 23-agentic-post-market-brief
contract: postmkt-artifact-v2
fire_time_et: 22:30
snapshot_et: 22:34-22:45
session: 462797923590223
scheduled_at_ms: 1794540620032
status: ok
source: MCP bridge market-recap (get_quotes, price_history) | TradingView public scanner | cron #20 us-eod/2026-11-12.csv | CBOE daily statistics + dated index history | refs/watchlist.yaml | web_search / web_fetch
primary_source: MCP bridge market-recap (Yahoo-sourced, keyless)
universe: cron #20 us-eod/2026-11-12.csv - 4,893 rows, 4,841 with a price, 4,275 cap-weighted
degraded_sources: 3
---

# Post-market brief — Thursday, 12 November 2026

## TL;DR

The headline index barely moved and the average stock was crushed: the S&P 500 closed **-0.35%** at 7,592.40 while the median name fell **1.15%** (`median_name_move_pct`), with **1,036 advancers** against **3,661 decliners** in the 4,841 priced names of the cron #20 universe and a `liquid_adv_dec_ratio` of **0.25** (364 up, 1,431 down above the $2B market-cap floor). The cap-weight penalty was **+51 bp** (`cap_weight_penalty_bp`, SPY -0.354% vs RSP -0.867%) — the fourth positive reading in five sessions, so this is a persistent narrow tape, not one bad day. The cause is identifiable: Nvidia fell 4.32% on Jensen Huang's resignation as chief executive (it was down 14% at the open), the 10-year yield rose 8bp to 5.09% on December rate-hike talk, and WTI settled +2.55% at $88.74 after the president said no Iran deal was needed — which left **Energy the only sector up on the day (+1.50% via its ETF)**. The claim is that the market absorbed a CEO exit, a bond-market repricing and an oil shock in one session and still finished a third of a percent lower; the caveat is that the calm headline hides a violent internal rotation, and the after-hours tape is where the risk is live: **Modine +27.43%** on Samsung acquisition talks, **Cerebras +18.34%** on a raised guide, **Vir Biotechnology -12.86%** on a dilutive offering, while the small caps that actually led the session are below the screen's market-cap floor.

## Tomorrow's setup — Friday, 13 November 2026

### Futures and the overnight setup

Every futures row carries `as_of` **2026-11-13T03:24Z (22:24 ET)** with `market_state: open` — six minutes before the fire — so this is the live Globex overnight, not the prior session's settlement. The percentages below are against the prior settlement, which is the correct basis for a futures quote; the cash index levels are in the row beside them.

| Contract | Level | vs prior settlement | Prior settlement | Session range |
|---|---|---|---|---|
| ES=F | 7631.50 | +0.21% | 7615.25 | 7619.25 - 7649.75 |
| NQ=F | 28428.00 | +0.15% | 28384.50 | 28393.50 - 28607.75 |
| YM=F | 52516 | +0.24% | 52390 | 52412 - 52564 |
| RTY=F | 2812.30 | +0.18% | 2807.30 | 2807.40 - 2816.90 |
| ZN=F | 105.328 | -0.12% | 105.453 | 105.219 - 105.359 |

Read it as a flat-to-slightly-higher open with **no** small-cap bid: RTY +0.18% and IWM -1.64% on the day means the Russell gap is a fraction of the S&P's. Note the basis — ES at 7631.50 sits **39.10 points above** the cash S&P 500 close of 7,592.40, which is normal for a fair-value-carrying overnight quote and is not an overnight rally.

Cross-asset, same timestamp: crude **88.11 (-0.71%)** after the day's +2.55% settle, gold **3918.50 (+0.85%)**, the dollar index **103.149 (-0.02%)**, bitcoin **69,164.87 (-3.09%)** after a -4.4% session. Oil giving back a fifth of the day's gain and bitcoin down another 3% overnight is a risk-off tell inside a green equity overnight.

### Economic calendar

- **08:30 ET — US Producer Price Index, October.** Consensus +0.4% m/m (prior +1.3%), core +0.3% m/m (prior +0.7%), headline +6.3% y/y (prior +6.3%). Source: TradingEconomics, FinanceCalendar, MarketWatch calendars. This is the day's only tier-1 US release and it lands on a tape that just repriced bonds: the 10-year yield rose 8bp to 5.09% and TLT fell 1.48%.
- **05:00 ET — Eurozone GDP, flash.** FinanceCalendar rates it high-impact.
- **Fed speaker — Cleveland Fed president Beth Hammack, 08:50 ET** (MarketWatch calendar). Rate-path chatter matters more than usual into a PPI print with a live December-hike debate.
- **No US jobless-claims release on Friday.** Claims are Thursday-timed; the 12 November print came in at **200,000** (consensus 195,000, prior 189,000). Next release 19 November.
- **University of Michigan preliminary November sentiment** is dated 10:00 ET Friday by the standard calendar, but the university's own page already publishes the preliminary reading (51.0, +6.3% m/m; year-ahead inflation expectations 4.3% from 4.7%). Treat the number as known and the release slot as nominal — the final is 20 November.

### Earnings calendar

Friday is a thin tape for US large caps — 105 companies report, 101 of them before the open and only 4 after the close (Earnings Whisper calendar). The names worth a level:

- **Before the open:** MUFG (EPS est 0.34), SMFG (0.40), MFG (0.17) — the Japanese banks, into a Financials tape that fell 0.82% cap-weighted; CG Oncology (CGON, close 70.15, -3.39% Thursday) with EPS est -$0.83; Twenty One Capital (XXI); Americas Gold and Silver (USAS, EPS est 0.04); Lithium Americas (LAC, est -$0.03) into the worst sector on the board; Sigma Lithium (SGML); Inhibrx (INBX); Owlet (OWLT); Noodles & Company (NDLS); Milestone Pharmaceuticals (MIST); Cocrystal Pharma (COCP).
- **After the close (4 names):** Almonty Industries (ALM, est 0.04), Immix Biopharma (IMMX), Eledon (ELDN), and FSI. The 4th-quarter Friday corporate calendar is thin enough that the after-hours tape will be driven by the AI complex and oil, not by earnings.

No watchlist name reports tomorrow; the nearest watchlist catalysts are Nvidia's Q3 print on Tuesday 17 November and the Modine shareholder meeting on Friday 13 November.

### News to watch for the top movers

- **Nvidia (NVDA) — closed 166.20, -4.32%, on 5.07x relative volume, after being 14% lower at the open and printing a 52-week low of 148.80.** Huang resigned as chief executive; chief financial officer Colette Kress is interim chief executive while the board searches for a permanent successor. Eight brokers downgraded; Baird cut to Neutral with a $200 target (from $500) and Bernstein cut to Market Perform with a $200 target (from $400) after removing Nvidia from its top semiconductor pick. Q3 guidance of $108.0bn is the number the tape is now trading against, and the report lands **Tuesday 17 November**. [Reuters, CNBC, Yahoo Finance, Benzinga]
- **Corteva (CTVA) — closed 9.19, -24.11%, low 9.14 (a 52-week low), the worst large-cap move on the board.** Q3 adjusted operating earnings of $0.06 vs $0.10 consensus and revenue of $1.59bn vs $1.76bn; FY2026 adjusted operating EBITDA guidance cut to $1.10-1.125bn (from about $1.3bn) and EPS to $0.76-0.80 on Brazil: Latin America organic sales -31%. MSCI also deleted the name from the MSCI USA Index, forcing passive selling. [MT Newswires, Investing.com, Proactive, Morningstar]
- **Global Payments (GPN) — closed 88.16, -12.02% on 3.15x relative volume.** Reuters reported that CD&R and GTCR have dropped early-stage take-private talks over financing complexity; the fall roughly hands back the 11% buyout pop from 30 October. Earnings were not the cause — Q3 adjusted EPS was $3.58, in line. [Reuters via Business Insider, Yahoo Finance]
- **Super Micro Computer (SMCI) — closed 26.99, -11.30%** on the de-rating of the AI complex around Nvidia's leadership vacuum. No single company-specific catalyst was captured in this run.
- **Mobility Global (MBGL) — closed 23.12, +16.01%, the best $2B+ name on the board** on 1.76x relative volume. No catalyst was captured in this run; treat the move as unexplained.
- **Veradermics (MANE) — closed 135.30, -13.55%** on 2.95x relative volume. No catalyst was captured in this run.

### Tomorrow's three things to watch

- **CBRS — 97.75 gap-fill level, 115.68 after-hours last — Q3 core revenue $230.9M beat the $214.7M consensus and FY2026 core revenue guidance was raised to $940-960M against $887.5M expected, with new Microsoft and Oracle wins; if the 97.75 close is not reclaimed the gap is not holding.**
- **MOD — 106.10 gap-fill level, 135.20 after-hours last — Samsung is in talks to acquire Modine (Bloomberg, unconfirmed; Reuters could not verify), and shareholders vote Friday on the Modexus Solutions name change; the talks can break, and a 106.10 close would mean the market never paid for the deal.**
- **NVDA — 166.19 gap-fill level, 167.84 after-hours last — Q3 results on Tuesday 17 November must hold the $108.0bn guide while the permanent chief executive search runs; Thursday's $148.80 low is the line that would say the leadership discount is not finished.**

## Day's tape

### Market read

One population throughout: cron #20's `us-eod/2026-11-12.csv` — 4,893 rows, of which 4,841 carry a price and a `change_pct`. The liquid set is the 1,809 names with a market cap above **$2B**.

| metric | value | where it comes from |
|---|---|---|
| advancers | 1,036 | us-eod CSV, priced names |
| decliners | 3,661 | us-eod CSV, priced names |
| unchanged | 144 | us-eod CSV, priced names |
| median_name_move_pct | -1.15% | us-eod CSV, `change_pct` |
| cap_weight_penalty_bp | +51 | bridge `price_history`, SPY vs RSP |
| liquid_adv_dec_ratio | 0.25 | us-eod CSV, names above the $2B cap floor (364 up / 1,431 down) |

The index-level story and the stock-level story disagree by 80 basis points: SPY -0.354% against a -1.15% median name, and 3,661 names down against 1,036 up. That is the participation read, and it is what the cap-weight penalty measures.

### Cap-weight penalty — 5-day history

Both ETFs are fetched in one bridge `price_history` call; `cap_weight_penalty_bp` = (SPY daily return - RSP daily return) x 100, rounded to the nearest basis point. Positive = the cap-weighted index outperformed the equal-weight index.

| Session | SPY % | RSP % | cap_weight_penalty_bp |
|---|---|---|---|
| 2026-11-06 | +0.31 | -0.38 | +69 |
| 2026-11-09 | +2.37 | +2.27 | +10 |
| 2026-11-10 | -0.37 | -0.03 | -34 |
| 2026-11-11 | +1.32 | +0.80 | +52 |
| 2026-11-12 | -0.35 | -0.87 | +51 |

Three positive readings in the last four sessions. The 51 bp is not a Thursday quirk — it is the fourth time in five days that the mega-cap half of the market carried the index while the average name did not. On 11-10 the sign flipped (-34 bp) for exactly one session; today's +51 bp is the same gap in the same direction.

### Index, ETF and volatility levels

Every index row was date-checked: all twelve symbols carry `as_of` on 2026-11-12, so no row here is a prior session's reading.

| Symbol | Close | Change | Day high | Day low | Source |
|---|---|---|---|---|---|
| S&P 500 (^GSPC) | 7592.40 | -0.35% | 7652.76 | 7550.84 | bridge, as_of 2026-11-12T21:58Z |
| Nasdaq Composite (^IXIC) | 25366.094 | -0.39% | 25597.225 | 25068.283 | bridge, as_of 2026-11-12T22:15Z |
| Dow Jones (^DJI) | 52297.09 | -0.36% | 52751.22 | 52271.16 | bridge, as_of 2026-11-12T21:58Z |
| Russell 2000 (^RUT) | 2799.06 | -1.66% | 2832.79 | 2796.83 | bridge, as_of 2026-11-12T21:30Z |
| Nasdaq 100 (^NDX) | 28289.188 | -0.30% | 28548.55 | 27940.584 | bridge, as_of 2026-11-12T22:15Z |
| Philadelphia Semi (^SOX) | 10506.674 | -0.54% | 10688.241 | 10174.117 | bridge, as_of 2026-11-12T22:15Z |
| SPY | 757.12 | -0.35% | 763.03 | 753.70 | bridge, as_of 2026-11-12T21:00Z |
| QQQ | 688.17 | -0.32% | 694.56 | 679.84 | bridge, as_of 2026-11-12T21:00Z |
| IWM | 278.44 | -1.64% | 282.20 | 278.04 | bridge, as_of 2026-11-12T21:00Z |
| DIA | 522.47 | -0.38% | 527.05 | 522.235 | bridge, as_of 2026-11-12T21:00Z |
| RSP | 220.72 | -0.87% | 222.925 | 220.58 | bridge, as_of 2026-11-12T21:00Z |
| SMH | 501.73 | -1.03% | 509.795 | 484.50 | bridge, as_of 2026-11-12T21:00Z |
| GLD | 354.89 | -2.82% | 357.76 | 352.92 | bridge, as_of 2026-11-12T21:00Z |
| TLT | 79.72 | -1.48% | 80.81 | 79.72 | bridge, as_of 2026-11-12T21:00Z |

Volatility is read from the dated history, not from the quote row, and cross-checked against Cboe's own dated close file — the two agree to the cent.

| Index | Close | Change | Intraday high | Bridge `price_history` | CBOE dated file |
|---|---|---|---|---|---|
| VIX | 18.70 | +6.92% | 19.34 | 2026-11-12 close 18.70 | 11/12/2026 close 18.70 |
| VXN | 28.55 | +6.77% | 28.93 | 2026-11-12 close 28.55 | 11/12/2026 close 28.55 |

The volatility indices rose but closed well off their highs (VIX 19.34 to 18.70, VXN 28.93 to 28.55) — the same "sell the shock, buy the bounce" pattern that ran through the equity session.

**Put/call ratio.** The CBOE daily statistics page carries `selectedDate: 2026-11-12` and `prevTradingDay: 2026-11-12` — the session that just closed, asserted against the fire date. Total put/call **0.89**, index 0.97, equity 0.72, exchange-traded products 1.06, SPX+SPXW+SPXO 1.10, XSP 1.05, VIX 0.42. These splits come from one payload and reconcile with the total. Total put volume 7,057,000 against 7,902,622 calls for 14,959,622 contracts in total.

### Cross-asset

| Asset | Level | Change | Note |
|---|---|---|---|
| WTI crude (CL=F) | 88.11 | -0.71% vs prior settlement | Day settle was 88.74, +2.55% on the session; Brent settled 95.82, +3.3% |
| Gold (GC=F) | 3918.50 | +0.85% | Reverses GLD's -2.82% cash-session loss |
| US dollar (DX-Y.NYB) | 103.149 | -0.02% | Flat |
| Bitcoin (BTC-USD) | 69164.87 | -3.09% | Second leg down; IBIT fell 4.44% on the day |
| 10-year Treasury yield | 5.09% | +8bp | Reported by Quantisnow; AP put it at 5.12% from 4.98% Tuesday |

### Day's movers

Top movers among names above the $2B market-cap floor (the universe's microcap tail is much larger — see `## Source health`).

| Ticker | Move | Close | Volume vs avg | Sector | Catalyst |
|---|---|---|---|---|---|
| CTVA | -24.11% | 9.19 | 1.80x | Materials | Q3 miss and FY2026 guidance cut on Brazil; MSCI USA Index deletion |
| MBGL | +16.01% | 23.12 | 1.76x | Information Technology | none captured in this run |
| MANE | -13.55% | 135.30 | 2.95x | Health Care | none captured in this run |
| DGII | -12.72% | 58.44 | — | Information Technology | none captured in this run |
| GPN | -12.02% | 88.16 | 3.15x | Financials | CD&R and GTCR abandon take-private talks |
| WRBY | -11.34% | 26.74 | — | Consumer Discretionary | none captured in this run |
| SMCI | -11.30% | 26.99 | 2.72x | Information Technology | AI-complex de-rating |
| ACHR | -11.10% | 4.325 | — | Industrials | none captured in this run |
| BLTE | +9.04% | 170.00 | 2.98x | Health Care | none captured in this run |
| LUNR | +6.98% | 13.03 | 3.35x | Industrials | none captured in this run |

The universe's extreme tail is far larger than this table: the three biggest absolute moves in the 4,893-row universe were PLCE +123.70%, AIMD +122.70% and XLAB +118.30%, all sub-$100M-cap names, and the worst was CDNL -62.37%.

### Watchlist EOD review

Eight names, from `refs/watchlist.yaml` (fetched at run time; published 2026-11-06). The five equities carry the cron #20 universe's day detail; the three ETFs are not in the equity universe, so their day range and volume come from the bridge quote row and their volume-vs-average is n/a.

| Ticker | Close | Day change | Day low | Day high | Volume | Volume vs avg | After-hours |
|---|---|---|---|---|---|---|---|
| AAPL | 354.90 | -0.20% | 354.40 | 359.40 | 28,750,328 | 0.65x | 354.76 (-0.03%) |
| MSFT | 523.00 | +0.36% | 520.00 | 529.60 | 16,424,925 | 0.67x | 521.09 (-0.37%) |
| NVDA | 166.20 | -4.32% | 148.80 | 167.10 | 732,056,534 | 5.07x | 167.84 (+0.99%) |
| GOOGL | 298.70 | +1.77% | 293.80 | 302.60 | 34,137,125 | 0.99x | 300.84 (+0.72%) |
| AMZN | 267.40 | +0.45% | 267.20 | 273.60 | 32,207,012 | 0.72x | 268.28 (+0.31%) |
| IWM | 278.44 | -1.64% | 278.04 | 282.20 | 22,572,446 | n/a | 278.80 (+0.13%) |
| GLD | 354.89 | -2.82% | 352.92 | 357.76 | 13,075,387 | n/a | 355.86 (+0.27%) |
| TLT | 79.72 | -1.48% | 79.72 | 80.81 | 46,920,625 | n/a | 79.57 (-0.19%) |

Two watchlist readings carry the session. Nvidia traded 732 million shares on 5.07x its average, with a 148.80 low against a 166.20 close — the close is 11.7% off the low, which is the whole "bought the blood" story in one line, and the after-hours mark of 167.84 (+0.99%) says the market has not finished arguing. Alphabet's +1.77% on the day (and +0.72% after hours) is the other: it is the name that made Communication Services look like a winning sector, and it is 53% of that sector's market cap.

## Sector rotation

Cap-weighted returns are computed on cron #20's universe: share classes de-duplicated on `cap_source_symbol` (the row whose `data_quality` does **not** contain `CAP_CARRIED` is kept), `EX_DISTRIBUTION` rows dropped, `NO_CAP` rows (149) excluded from every cap-weighted column and from the denominator, and the 370 rows carrying no sector excluded from the ranking. That leaves 4,244 rows in the cap-weighted denominator. Every cap-weighted return below sits inside ±20%.

| Sector | Cap-weighted % | Median name % | Sector ETF | ETF % | Gap (pp) | Cap sum |
|---|---|---|---|---|---|---|
| Energy | +1.43 | +0.68 | XLE | +1.51 | -0.08 | $3,001bn |
| Communication Services | +0.35 | -2.01 | XLC | -0.96 | **+1.31** | $6,951bn |
| Utilities | -0.07 | -0.36 | XLU | -0.02 | -0.05 | $1,548bn |
| Consumer Staples | -0.15 | -1.05 | XLP | -0.43 | +0.28 | $4,162bn |
| Consumer Discretionary | -0.20 | -1.97 | XLY | -0.44 | +0.24 | $8,057bn |
| Information Technology | -0.39 | -1.18 | XLK | -0.34 | -0.05 | $25,780bn |
| Real Estate | -0.59 | -0.99 | XLRE | -0.52 | -0.07 | $1,657bn |
| Financials | -0.82 | -0.52 | XLF | -0.72 | -0.10 | $10,372bn |
| Industrials | -0.84 | -1.35 | XLI | -0.89 | +0.05 | $8,936bn |
| Health Care | -0.92 | -3.12 | XLV | -0.59 | -0.33 | $8,572bn |
| Materials | -1.73 | -1.74 | XLB | -1.28 | -0.45 | $1,630bn |

**Top 3:** Energy +1.43%, Communication Services +0.35%, Utilities -0.07%. **Bottom 3:** Materials -1.73%, Health Care -0.92%, Industrials -0.84%.

Two of those rows need the constituent named.

**Communication Services is one company.** The cap-weighted +0.35% against a sector ETF at -0.96% is a 1.31pp gap, far past the ~0.5pp threshold where the gap is a constituent effect rather than a rotation. Alphabet is 53% of the sector's $6,951bn cap and rose 1.77%; **ex-Alphabet the sector is -1.61%**, i.e. below Materials' non-constituent reading and the true shape of the sector. The rotation here is "Alphabet bought the leadership vacuum", not "communication services rallied".

**Health Care is worse than it looks.** Cap-weighted -0.92% but a **median name of -3.12%**, the worst median on the board: Johnson & Johnson (+1.18%) and Eli Lilly (-0.56%) are carrying a sector whose median stock fell more than 3%. MRNA -6.96%, TMO -2.55% and ABT -1.92% did the damage. Health Care's own ETF (-0.59%) is also the second-widest gap on the board.

**Energy's move is oil, not rotation.** Cap-weighted +1.43% against XLE +1.51% is a clean 0.08pp — the sector moved with crude. The constituents are ExxonMobil +1.86% ($698bn), Chevron +1.55% ($428bn), Valero +3.14%, Marathon Petroleum +2.58%, ConocoPhillips +1.67%, with WTI settling +2.55% at $88.74 on the Iran headline. Materials at the other end (-1.73%) is the mirror: Newmont -4.89%, Freeport -2.67%, Southern Copper -2.61%, and Corteva -24.11% on its Brazil guidance cut.

## After-hours movers

One screen: TradingView's extended-hours columns, market cap above $1B, after-hours volume above 50,000 shares, ranked by absolute `postmarket_change`. Every row was verified against its own arithmetic — `postmarket_change` = (postmarket close - 16:00 close) / close x 100 — and no row failed. `gap_fill_level` is the prior close where the after-hours range brackets it, otherwise the after-hours midpoint. Prints are the scanner's snapshot as of ~22:35 ET.

| ticker | prior_close | ah_last | ah_high | ah_low | ah_volume | gap_pct | ah_range_pct | gap_fill_level |
|---|---|---|---|---|---|---|---|---|
| MOD | 106.10 | 135.20 | 139.00 | 106.10 | 242,071 | +27.43 | 31.01 | 106.10 |
| SLS | 8.03 | 9.65 | 9.94 | 8.00 | 970,288 | +20.13 | 24.16 | 8.03 |
| CBRS | 97.75 | 115.68 | 117.11 | 93.19 | 4,905,824 | +18.34 | 24.47 | 97.75 |
| LFTO | 18.71 | 21.94 | 22.10 | 18.71 | 211,594 | +17.26 | 18.12 | 18.71 |
| ACCV | 12.21 | 12.90 | 12.90 | 12.21 | 456,285 | +5.65 | 5.65 | 12.21 |
| VIR | 12.12 | 10.56 | 12.12 | 10.15 | 539,362 | -12.86 | 16.25 | 12.12 |
| ANDG | 65.42 | 60.00 | 65.42 | 60.00 | 74,005 | -8.28 | 8.28 | 65.42 |
| FLO | 6.01 | 5.54 | 6.08 | 5.11 | 1,751,654 | -7.82 | 16.14 | 6.01 |
| KEP | 11.13 | 10.50 | 11.14 | 10.45 | 133,999 | -5.66 | 6.20 | 11.13 |
| NKTR | 37.25 | 35.57 | 37.25 | 35.50 | 125,542 | -4.52 | 4.70 | 37.25 |

Two patterns a trader should notice. Every one of these ten names traded **back through its 16:00 close** in the after-hours session — all ten gap-fill levels are the prior close, so all ten have an unambiguous "the deal died" line if they give it back. And three of the five gainers (MOD, SLS, CBRS) have after-hours ranges between 24% and 31% of the close, which is what a contested price looks like: 139.00 high against a 135.20 last on Modine means the buyer is still being paid down.

**The screen's floor hides the real leaders.** The $1B market-cap filter is the contract's screen, not the tape: the biggest after-hours gainers of the night were BKHA +66.84% (a $22M-cap blank-check company), RAIN +54.93% ($5.5M), MRLN +54.50% ($98M), SHFS +43.996% ($3M), SLSN +39.71%, SNAL +37.72% and VTSI +34.74%; the worst were CADL -39.09% ($642M), NPCE -33.61%, RIME -28.48%, OGEN -27.76% and SST -23.95%. The table above is not the whole after-hours tape.

## After-hours earnings reactions

- **Cerebras Systems (CBRS) — 115.68 after hours, +18.34%, from a 97.75 close.** Q3 core revenue $230.9M vs $214.7M consensus (+70% y/y) and GAAP revenue $210.8M (+55%); GAAP EPS -$0.67 vs -$0.66 expected, core EPS +$0.13 vs -$0.13; first positive core net income ($29.8M). Q4 core revenue guided to $310-330M vs $274.9M consensus with a 47-49% core gross margin, and FY2026 core revenue raised to $940-960M vs $887.5M consensus. New commercial wins with Microsoft and Oracle; 700MW of data-center capacity contracted for delivery by end-2027. [CNBC, Investing.com, Earnings Whispers, Nasdaq.com]
- **Modine (MOD) — 135.20 after hours, +27.43% from 106.10 — this is not earnings.** Bloomberg reported Samsung Electronics is in talks to acquire Modine, at a reported value near $5.6bn; Reuters could not verify it and noted the talks could fall apart or another buyer could emerge. Modine shares traded at $137.45 at 19:23 ET. Separately, shareholders vote Friday 13 November on changing the company name to Modexus Solutions (ticker unchanged). [Bloomberg via Reuters/Investing.com/Yahoo Finance, AIStockWire]
- **Flowers Foods (FLO) — 5.54 after hours, -7.82% from 6.01.** Q3 adjusted EPS $0.10 vs $0.15 consensus on net sales of $1.169bn vs $1.18bn; FY2026 adjusted EPS guidance cut to $0.63-0.68 (from $0.75-0.85) and revenue guidance trimmed to $5.016-5.063bn on weak retail volume, promotional discounting and input costs. [StreetInsider, Seeking Alpha, MyAllies]
- **Vir Biotechnology (VIR) — 10.56 after hours, -12.86% from 12.12.** The company announced a proposed public offering priced below the last close; shares had already fallen 7.69% in the regular session. [Seeking Alpha, StockTitan, StockAnalysis]
- **Liftoff Mobile (LFTO) — 21.94 after hours, +17.26% from 18.71.** Q3 results released at 16:03 ET: a beat with the year raised, though decelerating growth kept the debate alive. [Nasdaq.com, Earnings Whispers, MarketWatch]
- **SELLAS Life Sciences (SLS) — 9.65 after hours, +20.13% from 8.03.** The Phase 3 REGAL trial hit its prespecified 80th event, triggering final-analysis procedures with topline results expected in November. [StockTitan, Stocktwits via Finviz]
- **Cisco (CSCO) — 101.50 after hours, -0.50% from 102.01 — the fade is the story.** A beat-and-raise: adjusted Q1 EPS $1.40 vs $1.33-1.40 consensus on revenue of $18.5bn vs $18.11bn, Q2 guided to $1.34-1.36 on $18.0-18.2bn, FY2027 raised to $5.47-5.53 on ~$75.3bn, hyperscaler AI infrastructure revenue guided to $9bn. The stock was at 110.63 in the after-hours high — up 8.4% — and was back to -0.50% by the fire. [CNBC, Barron's via NarrativeFlow, StreetInsider]
- **Applied Materials (AMAT) — beat-and-raise held flat.** Adjusted Q4 EPS $4.16 vs $4.06 consensus, revenue $10.41bn vs $10.30bn, Q1 FY2027 guided to $11.1bn ±$500M; the print was contained after a strong multi-quarter run. [CNBC, StreetInsider]
- **Newsmax (NMAX) — swung to a profit.** Q3 EPS $0.12 vs a -$0.02 loss expected on revenue of $96.0M, nearly double the $49.8M of a year earlier; the stock closed at $7.30 (-5.75%) and traded higher after hours. It sits below the screen's $1B cap floor at $940M. [StreetInsider, StockTitan]
- **Nkarta (NKTR) — 35.57 after hours, -4.52%.** The per-share beat is attributed to dilution as the Rezpeg Phase 3 programme moves into execution; the shares are down 48% since the last report. [Earnings Whispers via Finviz]
- **Two names in the table have no sourced catalyst:** ACCV +5.65% and KEP -5.66%. Nothing was captured in this run and nothing is invented here. ANDG -8.28% (a -8.28% move on only 74,005 after-hours shares) is likewise unexplained.

## Open research queue

1. **Is the cap-weight penalty a leadership rotation, or is the market simply short the average name?** Why it matters: four of the last five sessions printed a positive `cap_weight_penalty_bp` (+51 today) while 3,661 names fell — if the median name cannot hold its own for a week, the index level stops describing anything most holders own, and a mean-reversion day in the average name is a much bigger move than anything the megacaps can deliver. What would resolve it: Friday's advancer/decliner ratio and whether Alphabet's +1.77% and the AMD/AVGO/ANET rally persist without Nvidia's leadership — a rally that needs the old leader is a different rally than one that does not.
2. **Did Nvidia's CEO exit redistribute AI exposure or hollow it out?** Why it matters: AMD +5.95%, Broadcom +5.42% and Arista +5.18% on the day against XLK -0.34% means the "AI complex" is rotating rather than breaking — but Nvidia is roughly 6% of the S&P 500 and the successors' move may be borrow, not a durable reallocation. What would resolve it: whether the successors hold their relative strength on a flat-to-lower tape, and whether Nvidia's Q3 print on 17 November (guidance $108.0bn) confirms demand rather than leadership.
3. **Is the oil bid a headline spike or a supply repricing?** Why it matters: WTI +2.55% to $88.74 and Brent +3.3% to $95.82 on a political comment is why Energy was the only sector up, why GLD fell 2.82% and TLT 1.48%, and why the 10-year yield rose 8bp to 5.09% — the oil trade is currently the reason the discount rate is moving, and it is the most reversible of the three. What would resolve it: whether WTI holds above $88 into Friday's PPI print, and whether XLE holds its gain when crude is already giving back a fifth of the day's move overnight.

## Source health

- **The after-hours table is a screen, not the tape.** The $1B market-cap floor excludes the night's real extremes: BKHA +66.84%, RAIN +54.93%, MRLN +54.50%, SHFS +43.996% on the upside; CADL -39.09%, NPCE -33.61%, RIME -28.48%, OGEN -27.76% on the downside (a separate pull with no market-cap floor, 3,373 names qualifying on after-hours volume above 20,000 shares).
- **The extended-hours print is a moving target and vendors disagree materially.** The TradingView scanner print is the source of record here. For the same names, other vendors read: CBRS +18.41% at 18:00 ET (Nasdaq.com), +17.77% at 18:16 ET (Investing.com), +16.56% (ChartMill) and +12% (StreetInsider) against +18.34% on the scanner; VIR -13.78% (ChartMill) and -15.02% at 19:41 ET (StockAnalysis) against -12.86% here; MOD +29-30% in the 19:23 ET prints against +27.43% here. These are not blended — each number above is one vendor, one minute, and the scanner's is the one published.
- **Universe coverage (degraded source 1).** 370 of the 4,893 rows carry no sector and are excluded from the sector ranking — they are a bucket, not a sector, and including them would displace Utilities from the bottom three. 52 rows carry no price and are excluded from the participation read. 149 rows carry `NO_CAP` and are excluded from every cap-weighted column and from the denominator; 226 rows flagged `EX_DISTRIBUTION` are dropped per cron #20's rule; share classes are de-duplicated on `cap_source_symbol` (4,275 eligible rows become 4,244).
- **Watchlist ETF coverage (degraded source 2).** IWM, GLD and TLT are not in cron #20's equity universe, so their volume-versus-average is n/a — their day range and volume come from the bridge quote row, which carries no average volume.
- **Cross-vendor differences in the day's own numbers.** The 10-year yield is quoted at 5.09% by Quantisnow and 5.12% by AP; Nvidia's daily change reads -4.32% in cron #20's universe and -4.48% on Quantisnow; RSP's session reads -0.867% on the bridge's daily history and -0.84% in press coverage. This brief publishes the bridge and cron #20 figures as the source of record and does not average them.
- **Index and futures rows are dated, not assumed.** All twelve index rows carry `as_of` on 2026-11-12 and all five futures rows carry `as_of` 2026-11-13T03:24Z with `market_state: open` — the live overnight, six minutes before the fire. The CBOE put/call page carries `selectedDate: 2026-11-12`, asserted against the fire date. The VIX and VXN closes were read from the bridge's dated history and agreed to the cent with Cboe's own dated close file.
- **Three after-hours names have no sourced catalyst** (ACCV, KEP, ANDG), and five of the ten largest $2B+ daily movers have none either (MBGL, MANE, DGII, WRBY, ACHR). Those gaps are stated in place rather than filled.
- **degraded_sources: 3** — the universe CSV's sector/price coverage gaps; the watchlist ETF rows' missing volume-versus-average; and the extended-hours print's vendor disagreement, which bounds the precision of every after-hours percentage in this brief.

## Method notes

- **Population.** Every participation metric (advancers, decliners, unchanged, `median_name_move_pct`, `liquid_adv_dec_ratio`) comes from one population: cron #20's `us-eod/2026-11-12.csv`, 4,841 priced names. The liquid set is the 1,809 names above a $2B market cap.
- **`cap_weight_penalty_bp` is self-verifying.** Both ETFs are fetched in a single bridge `price_history` call; the metric is (SPY daily return - RSP daily return) x 100, and the five-session history is the same call's daily rows.
- **Sector returns are cap-weighted on de-duplicated, flagged rows only**, with the median name published beside each sector so a cap-weighted row cannot hide a sector where the average stock went the other way. Where the cap-weighted return and the sector ETF disagree by more than 0.5pp, the constituent is named and the sector is published with and without it.
- **Futures percentages are against the prior settlement**, which is the correct basis for a futures quote; the cash close and the overnight level are published side by side so no reader mistakes the basis for a move.
- **After-hours identity check.** Every published row satisfies `postmarket_change` = (after-hours close - 16:00 close) / 16:00 close x 100 within 0.06pp; no row was dropped for failing it, and no cell is blank — `n/a` is published where a field was genuinely unavailable.
- **Sources.** Bridge `market-recap` `get_quotes` and `price_history`; the TradingView public scanner through the shared validated client; cron #20's published CSV; CBOE's daily statistics page and its dated VIX/VXN history files; `refs/watchlist.yaml`; and issuer/press reporting via web search for catalysts, calendars and put/call context.
- **This brief places trades nowhere.** It is a read-only summary of what happened and what is scheduled.
