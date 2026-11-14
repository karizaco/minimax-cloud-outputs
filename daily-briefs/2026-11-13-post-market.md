---
date: 2026-11-13
cron: 23-agentic-post-market-brief
contract: postmkt-artifact-v2
fire_time_et: 22:30
snapshot_et: 22:33-22:48
session: 463151857426572
scheduled_at_ms: 1794627016073
status: ok
source: MCP bridge market-recap (get_quotes, price_history) for all closes and futures; TradingView scanner (america/scan, futures/scan) for the after-hours tape and the futures indicative; cron #20 us-eod/2026-11-13.csv for the EOD universe; CBOE daily statistics and dated VIX/VXN close files; refs/watchlist.yaml; web_search for catalysts and calendars
primary_source: MCP bridge market-recap (keyless, Yahoo-sourced) for every index, ETF and futures close
universe: cron #20 us-eod/2026-11-13.csv — 4,890 rows, 4,840 of them priced (a 50-name market_cap floor applies only to the liquid set, which is 1,805 names)
degraded_sources: 3
---

# Post-market brief — Friday, 13 November 2026

## TL;DR

Friday was a chip-led de-rating, not a broad risk-off session: the S&P 500 fell 0.40% while the equal-weight index rose 0.20%, a **cap_weight_penalty_bp of -56** — the cap-weighted names did all the damage. Across the 4,840 priced names in the EOD universe, **advancers 2,065** against **decliners 2,596** and a **median_name_move_pct of -0.14%**, with a **liquid_adv_dec_ratio of 1.09** in the $2B-plus set (927 up, 848 down). Semiconductors did the selling — AMD -8.75%, Cisco -6.24%, Broadcom -4.76%, Nvidia -2.01% — after the rotation out of Nvidia unwound on the leadership vacuum, and the 10-year Treasury yield cleared 5%. Staples, energy, healthcare and financials all bid, and the equal-weight index was green. Read it as a narrow mega-cap de-rating, not a broad sell-off: the average S&P 500 name finished higher while the index finished lower.

## Tomorrow's setup — Monday, 16 November 2026

Tomorrow, Saturday 14 November, is not a session. The next trading session is **Monday 16 November**, and this section is written for that session.

### Futures and the overnight setup

**There is no overnight print yet, and there cannot be one tonight.** The CME equity-index session closed for the week at 17:00 ET Friday; Globex does not reopen until **Sunday 18:00 ET**, which is the first chance for an overnight move into Monday's cash open. Every futures figure available at this fire is therefore Friday's settlement, not an overnight setup.

| Contract | Friday settlement (16:59:59 ET) | Session range | Post-close indicative print | Reference |
|---|---|---|---|---|
| ES (S&P 500 future) | 7561.00 (-0.71%) | 7519.25 - 7669.25 | 7583.00 (stamped 20:56 ET) | bridge / Yahoo |
| NQ (Nasdaq-100 future) | 27927.25 (-1.61%) | 27695.25 - 28607.75 | 28034.75 (stamped 20:56 ET) | bridge / Yahoo |
| YM (Dow future) | 52347.00 (-0.08%) | 52081 - 52722 | 52418.00 (stamped 20:56 ET) | bridge / Yahoo |
| RTY (Russell 2000 future) | 2791.20 (-0.57%) | n/a | n/a | bridge |
| ZN (10-year Treasury future) | 105.28125 (-0.16%) | 105.078125 - 105.453125 | 105.1875 (stamped 20:24 ET) | bridge / Yahoo |

The post-close indicative column is the TradingView futures scanner (a 10-minute delayed feed) and sits about 0.3% above the Friday settlement. It is published as an observation, not as a tradeable overnight level: the CME equity-index week was closed when it stamped. **The setup for Monday is therefore the Sunday 18:00 ET Globex open, not this number.**

### Economic calendar — Monday, 16 November

| Time (ET) | Release | Note |
|---|---|---|
| 08:30 | Empire State Manufacturing Index (Nov) | The week's first US read; the October print was the first soft one in a while |
| 12:00 | Fed Chair Kevin Warsh — opening remarks, Productivity and Jobs Task Force Conference | A first-tier speech on the day after a 5%-plus 10-year |
| 08:30 | Canada CPI (Oct) | Consensus +0.3% m/m, +3.2% y/y |
| overnight | China industrial production, retail sales, fixed-asset investment (Oct); Japan Q3 GDP; eurozone industrial production (Sep) | Asia opens before the cash session |

The heavier US data sits later in the week: October retail sales and Nvidia's print are both Tuesday 17 November, the FOMC minutes are Wednesday 18 November, and jobless claims and the Philadelphia Fed are Thursday 19 November.

### Earnings calendar — Monday, 16 November

Roughly 80 to 99 companies are scheduled, the smaller names mostly.

- **Before the open:** Baidu, Tyson Foods, KE Holdings, H World, Aramark, XPeng, POET Technologies.
- **After the close:** Powell Industries, AECOM, XP Inc, Infleqtion, Driven Brands, Omeros, PagSeguro, Blackstone Digital Infrastructure Trust.

No watchlist name reports Monday. **Nvidia reports Tuesday 17 November after the close**, Walmart Thursday morning, Home Depot and Disney Tuesday morning, Palo Alto Networks Wednesday after the close.

### News to watch for the top movers

- **LFTO** (Liftoff Mobile) +30.63% — third-quarter revenue of $238m, up 32%, net income of $87m, above the top of its own guidance, with a raised full-year outlook and several bullish upgrades. It traded 13.6x its average volume, the highest relative volume in the universe.
- **MOD** (Modine Manufacturing) +27.87% — Bloomberg reported Samsung Electronics is in talks to acquire the data-centre cooling maker, roughly $5.6bn of market value before the talks.
- **CBRS** (Cerebras) +11.22% — raised its 2026 adjusted revenue outlook to $940m-$960m from $880m-$890m, above a consensus of $887m, posted a surprise profit, and named Microsoft as a cloud customer.

### Tomorrow's three things to watch

- POWL — 134.68 after-hours print, 142.72 prior close — reports after the close on Monday 16 November (Q4 FY2026, consensus $1.52-$1.56); the guide is the tell after a -5.64% after-hours slide.
- NVDA — 161.01 after-hours print, 162.85 close — reports after the close on Tuesday 17 November (consensus $2.49) with no permanent chief executive; Monday is the setup into that print, and the chip complex will not settle without it.
- AMD — 521.20 after-hours print, 534.06 close — no company news of its own; the rotation unwind has to stop here, and the Sunday 18:00 ET Globex open into Tuesday's chip print is the test.

## Day's tape

### Market read

One population — cron #20's EOD universe, 4,890 rows of which 4,840 carry a priced change.

| metric | value | source |
|---|---|---|
| advancers | 2,065 | cron #20 universe, 4,840 priced names |
| decliners | 2,596 | same |
| unchanged | 179 | same |
| median_name_move_pct | -0.14% | same (median of `change_pct`) |
| cap_weight_penalty_bp | -56 | bridge `price_history`, SPY -0.363% vs RSP +0.199% |
| liquid_adv_dec_ratio | 1.09 | 927 advancers / 848 decliners above a $2B market-cap floor (1,805 names, 30 unchanged) |

The two readings disagree in an informative way: the median name across the whole universe was down 0.14%, while the S&P 500 equal-weight index was up 0.20%. The large-cap end is where the loss sat.

### Cap-weight penalty — 5-day history

| Session | SPY % | RSP % | cap_weight_penalty_bp |
|---|---|---|---|
| 2026-11-09 | +2.37 | +2.27 | +10 |
| 2026-11-10 | -0.37 | -0.03 | -34 |
| 2026-11-11 | +1.32 | +0.80 | +52 |
| 2026-11-12 | -0.35 | -0.87 | +51 |
| 2026-11-13 | -0.36 | +0.20 | -56 |

The sign flipped hard: the index gave up its cap-weight premium in a single session, and it is the largest negative reading in the five-session window.

### Index, ETF and volatility levels

Every row's `as_of` was checked against the fire date; all carried 2026-11-13. Volatility indices are read from the dated `price_history` series, not from the quote row, and cross-checked against CBOE's own dated close files — both agree to the cent.

| Instrument | Close | Change % | Day range |
|---|---|---|---|
| S&P 500 | 7561.67 | -0.40 | 7499.40 - 7621.78 |
| Nasdaq Composite | 25136.27 | -0.91 | 24872.41 - 25423.09 |
| Dow Jones Industrial Average | 52347.55 | +0.10 | 52017.86 - 52521.48 |
| Nasdaq-100 | 27943.74 | -1.22 | 27609.71 - 28295.80 |
| Russell 2000 | 2790.49 | -0.31 | 2763.72 - 2805.90 |
| PHLX Semiconductor | 10146.32 | -3.43 | 9828.98 - 10461.98 |
| VIX | 19.30 | +3.21 | 17.64 - 20.92 |
| VXN | 29.38 | +2.91 | 28.39 - 31.23 |
| SPY | 754.37 | -0.36 | 747.89 - 760.12 |
| QQQ | 679.89 | -1.20 | 671.71 - 688.75 |
| RSP | 221.16 | +0.20 | 219.43 - 221.82 |
| IWM | 277.54 | -0.32 | 274.67 - 279.16 |
| DIA | 523.15 | +0.13 | 519.70 - 524.99 |
| SMH | 486.75 | -2.99 | 473.26 - 500.27 |

VIX at 19.30 came from a 17.64 low and a 20.92 high — the volatility bid was intraday and partly faded. VXN at 29.38 is the higher of the two and the one that matters for the chip complex, with a 31.23 intraday high.

### Cross-asset

| Instrument | Level | Change |
|---|---|---|
| 10-year Treasury yield (^TNX) | 5.154% | above 5% for the first time in this move; cited as a weight on technology shares |
| 10-year Treasury future (ZN) | 105.28125 | -0.16% (Friday settlement) |
| Gold future (GC) | 3887.60 | +0.06% (Friday settlement) |
| Gold ETF (GLD) | 355.45 | +0.16% |
| 20+ year Treasury ETF (TLT) | 79.38 | -0.43% |
| Dollar index (DX-Y.NYB) | 103.411 | flat on the session |
| Crude future (CL) | 88.92 | +0.20% (Friday settlement) |

Long bonds fell while the yield rose above 5%, and gold was flat: the defensive bid went into staples, energy and healthcare equities rather than into bullion.

### Day's movers

From cron #20's universe file, names above a $2B market cap. Two names larger than anything on this list sat below the floor: Newsmax (+31.23%, third-quarter beat and an upgrade to buy) and Hawk (+24.06%, a revenue beat of $59m against a $56m consensus and raised 2026 guidance).

| Ticker | Change % | Close | Volume | Rel. volume | Sector |
|---|---|---|---|---|---|
| LFTO | +30.63 | 24.44 | 9,449,378 | 13.58 | Communication Services |
| MOD | +27.87 | 135.80 | 8,094,325 | 4.12 | Consumer Discretionary |
| CBRS | +11.20 | 108.70 | 36,077,723 | 3.27 | Information Technology |
| WWW | +8.82 | 24.91 | 2,571,150 | 2.61 | Consumer Discretionary |
| FOUR | +7.80 | 44.79 | 2,816,967 | 1.23 | Industrials |
| ACCV | +5.82 | 12.92 | 1,527,880 | n/a | Industrials |
| HTFL | -19.13 | 48.46 | 3,503,021 | 2.00 | Health Care |
| AMD | -8.75 | 534.10 | 47,795,898 | 1.66 | Information Technology |
| OUST | -8.53 | 33.48 | 2,420,285 | 0.84 | Information Technology |
| CVLT | -8.48 | 152.10 | 976,908 | 1.45 | Information Technology |
| IOND | -7.40 | 59.84 | 303,517 | 0.75 | Financials |
| DELL | -7.27 | 344.30 | 9,574,653 | 1.35 | Information Technology |
| HUT | -7.12 | 57.57 | 4,369,787 | 0.63 | Financials |
| RGTI | -6.87 | 9.62 | 15,431,027 | 0.97 | Information Technology |

Closes in this table are cron #20's settled close column, and two of them differ marginally from the bridge's print for the same session: Modine (135.80 here, 135.66 on the bridge) and Dell (344.30 here, 344.53 on the bridge). The bridge is the quote source of record everywhere else in this brief, and the after-hours table's prior closes come from it.

The losers are overwhelmingly the AI-hardware complex, and the reasons are specific: AMD published no news of its own and simply gave back 37% of a five-session run; Cisco beat and raised (Q1 revenue $18.5bn, up 24%, EPS $1.40) but fell 6.24% as order growth excluding hyperscalers decelerated to 14% and gross margin came under pressure; Applied Materials fell after a downgrade; Heartflow dropped 19.13% on a Q3 revenue beat of $72.9m that still raised questions about fourth-quarter growth.

### Watchlist EOD review

| Ticker | Close | Day % | Day range | Volume | Vol vs avg | After-hours print |
|---|---|---|---|---|---|---|
| AAPL | 356.27 | +0.39 | 355.80 - 360.80 | 33,922,177 | 0.77x | 355.40 (-0.24%) |
| MSFT | 523.88 | +0.17 | 513.80 - 526.40 | 21,622,043 | 0.88x | 522.46 (-0.27%) |
| NVDA | 162.85 | -2.01 | 158.40 - 170.00 | 356,991,780 | 2.15x | 161.01 (-1.13%) |
| GOOGL | 295.77 | -0.97 | 293.40 - 305.00 | 29,134,410 | 0.84x | 294.05 (-0.58%) |
| AMZN | 266.66 | -0.29 | 263.90 - 269.90 | 28,454,460 | 0.63x | 264.33 (-0.87%) |
| IWM | 277.54 | -0.32 | 274.67 - 279.16 | 17,588,703 | n/a | 275.56 (-0.71%) |
| GLD | 355.45 | +0.16 | 354.41 - 357.32 | 11,703,859 | n/a | 355.70 (+0.07%) |
| TLT | 79.38 | -0.43 | 79.11 - 79.64 | 31,831,810 | n/a | 79.42 (+0.05%) |

The watchlist is a mega-cap book and the mega-caps were what got hit: Nvidia -2.01% on 2.15x its average volume, and the whole list closed below its intraday highs. Apple was the only watchlist name above its 50-day average by more than 5%. Volume-versus-average is not available for the three ETF legs — the universe file carries stocks only — and is published as `n/a` rather than estimated.

## Sector rotation

Cap-weighted on one row per `cap_source_symbol`, with `EX_DISTRIBUTION`, `CAP_CARRIED`, `NO_CAP` and `NO_SECTOR` rows excluded (4,120 names carried into the weights; 369 rows with no sector and 148 with no market cap are excluded from every cap-weighted column and the denominator). Every cap-weighted return was checked to sit inside plus or minus 20% before publication.

| Sector | Cap-weighted % | Median name % | Sector ETF % | ETF gap (pp) | Names |
|---|---|---|---|---|---|
| Consumer Staples | +1.39 | +0.88 | XLP +1.42 | -0.03 | 141 |
| Energy | +0.93 | +0.70 | XLE +0.98 | -0.05 | 174 |
| Financials | +0.68 | +0.09 | XLF +0.81 | -0.13 | 1,026 |
| Information Technology | -1.63 | -1.75 | XLK -2.01 | +0.38 | 493 |
| Industrials | -0.46 | -0.67 | XLI -0.39 | -0.07 | 537 |
| Materials | -0.42 | -0.80 | XLB -0.21 | -0.21 | 153 |

No sector's cap-weighted return diverges from its ETF by more than 0.5pp, so no row needs a constituent-effect explanation. Two things the table does show: technology's -1.63% is a semiconductor effect (semis are 39.4% of the sector's cap; excluding them the sector is -0.51%), and healthcare is a cap-weighted positive with a negative median (+0.40% against -0.71%) — the megacaps carried it while the median healthcare name fell.

## After-hours movers

The screen keeps names above $1B of market cap with more than 50,000 after-hours shares traded (2,032 names qualify). Every row passed the scanner's own identity check — the published change equals (after-hours last minus prior close) divided by the prior close — and every row's `gap_fill_level` follows the fixed rule: the prior close when the after-hours range brackets it, otherwise the after-hours midpoint.

| ticker | prior_close | ah_last | ah_high | ah_low | ah_volume | gap_pct | ah_range_pct | gap_fill_level |
|---|---|---|---|---|---|---|---|---|
| ACCV | 12.92 | 13.51 | 13.51 | 12.92 | 557,719 | +4.57 | 4.57 | 12.92 |
| PRIM | 69.30 | 71.6742 | 71.6742 | 69.30 | 124,703 | +3.43 | 3.43 | 69.30 |
| CHYM | 33.55 | 34.6918 | 34.80 | 33.37 | 848,629 | +3.40 | 4.26 | 33.55 |
| STE | 264.32 | 272.2042 | 272.2042 | 264.30 | 182,313 | +2.98 | 2.99 | 264.32 |
| ELV | 429.69 | 442.00 | 443.20 | 429.69 | 196,540 | +2.86 | 3.14 | 429.69 |
| NN | 8.73 | 8.219 | 8.73 | 8.132 | 250,411 | -5.85 | 6.85 | 8.73 |
| POWL | 142.72 | 134.6757 | 142.72 | 134.6757 | 60,487 | -5.64 | 5.64 | 142.72 |
| MMED | 17.99 | 16.9946 | 17.99 | 16.9946 | 427,821 | -5.53 | 5.53 | 17.99 |
| LBTYK | 10.52 | 10.00 | 10.52 | 10.00 | 217,669 | -4.94 | 4.94 | 10.52 |
| KRMN | 40.66 | 39.00 | 40.66 | 39.00 | 348,280 | -4.08 | 4.08 | 40.66 |

All ten after-hours rows traded through the 16:00 close inside their own range, so every gap fills at the prior close.

Two things this table is not. First, the $1B floor hides the session: the same screen without the market-cap floor surfaced Generation Income Properties at +84.12%, Polar Power at +42.22%, Akanda at +37.40%, ClearOne at +27.14% and, on the downside, Datavault AI at -34.50% and Forcendra at -33.82%. Second, the tape is a snapshot as of the fire and the extended hours keep moving — for Elevance, other vendors printed materially different numbers the same evening (see `## Source health`).

Four over-the-counter lines were excluded from this table: their prior closes are stale rounded values on a venue that does not trade the session, so their changes are artefacts rather than moves. Banco Santander's line showed +14.80% against a $12.00 stale close while the primary New York listing closed flat at $12.21; HSBC's line showed +3.32% while the primary listing was +0.61%.

## After-hours earnings reactions

No S&P 500 company reported after Friday's close, so the after-hours tape is continuation rather than reaction. What is on it:

- **CHYM** +3.40% — S&P Dow Jones Indices announced at 20:18 ET that Chime joins the S&P MidCap 400 effective before the open on Wednesday 18 November, replacing NorthWestern Energy. It follows a Q3 print of $0.11 EPS against a $0.02 loss expected.
- **ELV** +2.86% — no company news was sourced for the move; it is published as an unsourced print and flagged in `## Source health`.
- **STE** +2.98% — Jefferies upgraded Steris to buy during the session, after which it rose 4.29% on the day.
- **PRIM** +3.43% — a reversal of a 3.14% decline on the day; no fresh news was sourced, and the company last reported on 3 November and has investor conferences scheduled from 17 November.
- **POWL** -5.64% — de-rating into Monday's after-close report.

Friday's late reporters were Cisco and Applied Materials, both of whom beat and were both marked below the bar: Cisco's EPS of $1.40 beat the $1.33 consensus and revenue of $18.52bn beat the $18.13bn estimate, and the stock still fell 6.24% on the day and is -1.19% after hours; Applied Materials' EPS of $4.16 beat a $4.05 consensus on revenue of $10.41bn and fell 2.74% after a downgrade to hold.

## Open research queue

1. **Is the chip move a de-rating or a rotation?** AMD fell 8.75% with no company news, and the group's move was blamed on the unwind of the post-Nvidia-leadership rotation rather than on any issuer. It matters because the equal-weight index rose on the same day: if the unwind continues, the damage gets broader rather than worse, and the median name follows. What would resolve it: Monday's open with semis and small caps both higher, and then Nvidia's Tuesday guide.
2. **Why did the equal-weight index rise while 2,596 of 4,840 names fell?** The median name was -0.14% while the S&P 500 equal-weight index was +0.20%. Either the index's membership hides a genuinely weak broad market, or the universe file and the index do not cover the same names. What would resolve it: the same participation metric computed on a Russell 3000 equal-weight basis, and a check of the 179 names the universe file prices at exactly zero.
3. **What is a real after-hours print on an over-the-counter venue?** Banco Santander's line printed +14.80% against a stale $12.00 close while the primary listing was flat, and three other over-the-counter lines failed the same way. It matters because the scanner is a discovery screen the fleet trusts. What would resolve it: a consolidated tape for those venues, or a rule that drops any row whose after-hours range has a single print and whose venue is not a major US exchange.

## Source health

| Source | Query / URL | Status | Result |
|---|---|---|---|
| MCP bridge `market-recap` `get_quotes` | 16 index/ETF symbols, then 36 sector and mover symbols | ok | every row's `as_of` dated 2026-11-13 |
| MCP bridge `market-recap` `price_history` | SPY, RSP, ^VIX, ^VXN, ^GSPC, 2026-10-28 to 2026-11-13 | ok | 5 sessions of SPY/RSP returns, dated volatility closes |
| MCP bridge `market-recap` `get_quotes` (futures) | ES=F, NQ=F, YM=F, RTY=F, ZN=F | **degraded** | every row stamped 2026-11-13 16:59:59 ET — 5.5 hours before the fire and the last print of the CME week |
| TradingView scanner `america/scan` via `_shared/tv_scan.py` | after-hours screen, $1B floor, 2,032 names; no-floor screen, 2,690 names | ok | 200 rows each side, sorted by `postmarket_change`; all 400 rows passed the change identity check |
| TradingView scanner `futures/scan` | ES1!, NQ1!, YM1!, ZN1! | ok (delayed) | post-close indicative print stamped 20:56 ET, `delayed_streaming_600` |
| CBOE daily market statistics | `https://www.cboe.com/us/options/market_statistics/daily/` | **degraded** | payload carries `selectedDate` 2026-11-12 — the 13 November session was not published at the fire |
| CBOE dated index closes | `https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv`, `VXN_History.csv` | ok | VIX 19.30 and VXN 29.38 for 11/13, agreeing to the cent with the bridge's dated history |
| cron #20 EOD universe | `karizaco/minimax-cloud-outputs` → `us-eod/2026-11-13.csv` | ok | 4,890 rows, 4,840 priced |
| Watchlist | `karizaco/minimax-cloud-outputs` → `refs/watchlist.yaml` | ok | 8 names |
| Yahoo chart API | `ES=F`, `NQ=F` daily bars | ok | confirmed the 17:00 ET Friday close and the absence of a weekend session |
| MCP availability probe | `probe_mcp.py` | ok | `catalog_ok total=135 finance_tools=0` — no finance MCP registered; the bridge was used instead |
| Catalysts and calendars | web_search | ok | StockTitan, Market Wrap, Reuters, Yahoo Finance, EarningsWhispers, macrobullseye |

Three degraded sources:

1. **Futures** — the bridge and Yahoo both carry only the 16:59:59 ET Friday settlement, so no overnight figure exists anywhere at this fire. The TradingView indicative print is dated 20:56 ET but the CME equity-index week was closed. Published as a Friday settlement, not as an overnight setup.
2. **Put/call ratio** — CBOE's page carries `selectedDate` 2026-11-12, so the total put/call of **0.89** belongs to the 12 November session (index 0.97, equity 0.72, ETP 1.06, SPX+SPXW+SPXO 1.10, XSP 1.05 — all from that one payload). The 13 November session was not published at the 22:30 fire, and the page's date parameter does not change the payload.
3. **Elevance's after-hours print** — the scanner published $442.00 (+2.86%) at 16:33 ET, Barron's showed $440.49 (+2.51%) at 19:56 ET, and another vendor showed $416.01 at 20:00 ET. The scanner's number is published as the source of record; the others are named here rather than blended into one figure.

## Method notes

- **Universe.** Every participation metric uses one population: cron #20's `us-eod/2026-11-13.csv`, 4,890 rows of which 4,840 carry a priced change. The liquid set is the 1,805 names with a market cap above $2B.
- **Cap-weighting.** Sectors are weighted on one row per `cap_source_symbol`. Rows flagged `EX_DISTRIBUTION` are dropped, the primary listing is kept in preference to a `CAP_CARRIED` row, and `NO_CAP` and `NO_SECTOR` rows are excluded from both the numerator and the denominator. Every published cap-weighted sector return was asserted inside plus or minus 20%; a value outside that band would be a computation bug, not a market event.
- **The cap-weight penalty** is (SPY daily return minus RSP daily return) times 100, rounded to the nearest basis point, taken from one `price_history` call covering both ETFs. It is signed: positive means the cap-weighted index outperformed the equal-weight index.
- **Volatility indices** were read from the dated `price_history` series and cross-checked against CBOE's own dated close files, because a quote row can carry the prior session's value for a volatility index while every other symbol in the same call is current. Both checks agreed to the cent.
- **After-hours levels** come from the TradingView scanner as a snapshot at the fire. `gap_fill_level` is the prior close when the after-hours range brackets it, and the after-hours midpoint otherwise. A field that could not be read is published as `n/a` and never as a guess or a zero.
- **Over-the-counter rows were excluded** from the movers table: their venues do not trade the session and their prior closes are stale rounded values, so the computed change is an artefact. The primary listings were used to confirm each case.
- **Liquidity caveat.** The after-hours screen requires more than 50,000 shares traded, so thin names are absent from the table by construction, and the $1B market-cap floor is why the largest moves of the night are below it.
- **Futures convention.** Every futures row's `as_of` was checked. A row stamped more than 30 minutes before the fire is the prior session's settlement, and the CME equity-index session was closed for the weekend at the time of this fire.
- The brief is read-only research. No positions, no trade recommendations, and no sizing.
