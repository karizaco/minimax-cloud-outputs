---
date: 2026-11-16
cron: 23-agentic-post-market-brief
contract: postmkt-artifact-v2
fire_time_et: 22:30
snapshot_et: 22:33-22:41
session: 464213617524945
scheduled_at_ms: 1794886221045
status: ok
source: MCP bridge market-recap (get_quotes, price_history) + TradingView scanner + CBOE daily statistics and dated index files + cron #20 us-eod CSV + web_search
primary_source: MCP bridge market-recap (get_quotes / price_history)
universe: cron #20 us-eod/2026-11-16.csv — 4,890 rows, 4,844 priced
degraded_sources: 0
---

# Post-market brief — Monday, 16 November 2026

## TL;DR

A third straight down day, and this one was about AI leadership rather than the shape of the
market: the S&P 500 fell 1.92% to 7,416.59, the Nasdaq Composite 2.49% to 24,509.76 and the
Philadelphia Semiconductor Index 5.28%, after the 12 November resignation of the chief executive
of the largest chipmaker and a new Commerce Department rule requiring licences for advanced AI
chips bound for Singapore, Malaysia, Thailand, Indonesia and Brazil. The damage was broad rather
than narrow: 1,086 advancers against 3,594 decliners in the 4,844-name priced universe,
median_name_move_pct -1.17%, liquid_adv_dec_ratio 0.37 in the $2B-plus set, and
cap_weight_penalty_bp **-90** (SPY -1.91% against RSP -1.01%) — the first negative reading in
the five-session window, so the equal-weight index beat the cap-weighted one. The after-hours
tape is a narrow bounce, not a risk-on turn: at 22:23 ET the Nasdaq future was +0.57% while the
Dow and small-cap futures were both -0.30%. Volatility says fear (VIX 22.91, +18.7%) but the CBOE
total put/call was 0.95 and the equity ratio 0.73 — the tape is hedged in vol, not in puts, which
is the single most useful number into a chip earnings print.

## Tomorrow's setup — Tuesday, 17 November 2026

### Futures and the overnight setup

Live Globex prints read at 22:22-22:23 ET — inside the post-18:00 ET overnight window, so these
are genuine overnight moves, not a stale 16:00 settlement. Each change is measured against the
contract's 2026-11-16 close, which the bridge's own dated history confirms (ES 7439.00,
NQ 27284.25, YM 51670, RTY 2751.40, ZN 105.4375).

| Contract | Overnight last | 2026-11-16 close | Change | as_of (ET) |
|---|---|---|---|---|
| ES=F | 7,443.50 | 7,439.00 | +0.06% | 22:23 |
| NQ=F | 27,439.25 | 27,284.25 | +0.57% | 22:23 |
| YM=F | 51,515 | 51,670 | -0.30% | 22:23 |
| RTY=F | 2,743.10 | 2,751.40 | -0.30% | 22:23 |
| ZN=F | 105.4063 | 105.4375 | -0.03% | 22:22 |

Read it as a chip-specific bid, not a market bid: the Nasdaq future is green while the Dow and
the Russell are both red, and the 10-year future is flat. The overnight is a narrow AI-complex
relief, not a broad risk-on turn, and it arrives into a session where the chip complex has to
print.

### Economic calendar

| Time (ET) | Release | Forecast | Previous |
|---|---|---|---|
| 08:15 | ADP weekly employment change | — | 19.75K |
| 08:30 | Retail sales (Oct, m/m) | +0.2% | +0.8% |
| 08:30 | Core retail sales (Oct, m/m) | +0.4% | +0.9% |
| 08:30 | Retail control group (Oct, m/m) | +0.4% | +0.1% |
| 08:30 | Import price index (Oct, m/m) | +0.7% | +1.1% |
| 08:30 | Export price index (Oct, m/m) | +0.3% | +2.2% |
| 09:15 | Industrial production (Oct, m/m) | +0.1% | +0.7% |
| 09:15 | Capacity utilisation (Oct) | 76.8% | 76.9% |
| 10:00 | NAHB housing market index (Nov) | 29 | 29 |
| 10:00 | Business inventories (Sep, m/m) | +0.5% | +0.4% |
| 11:30 | Atlanta Fed GDPNow (Q4) | 3.5% | 3.5% |
| 14:25 | New York Fed president speaks | — | — |
| 16:30 | API weekly crude stocks | — | 9.0M barrels |

Fed speakers sit on both sides of the session: two governors in the morning (Waller and
Cleveland's Hammack, an October dissenter) and the New York Fed president at 14:25. Sources
disagree on Waller's exact start minute (9:10 ET on MarketWatch, 9:20 ET on Finviz), so treat
the morning as a two-speaker window rather than a single timestamp.

### Earnings calendar

Tomorrow carries 42 reporting names — 29 before the open, 13 after the close — and one of them
carries the whole AI complex.

**Before the open:** Home Depot (EPS estimate $3.83-3.84), Walt Disney ($1.68), Viking Holdings
($1.16-1.27), JD.com ($5.88-6.06), Elbit Systems ($3.94), Amer Sports ($0.35), Tencent Music
($1.50), Klarna, Spire, Energizer, FuboTV, Weibo, Griffon, MINISO, Opera, Huya.

**After the close:** NVIDIA (EPS estimate $2.47, revenue estimate $108.85B) — the first results
call without the chief executive who resigned on 12 November — plus Dolby Laboratories, ZTO
Express, Sociedad Quimica y Minera de Chile, La-Z-Boy, Corporacion America Airports, Golub
Capital BDC and Auna.

Also on the week's radar: Anthropic prices its IPO on Wednesday night and trades Thursday, and
Palo Alto Networks reports Wednesday after the close.

### News to watch for the top movers

- **CGON** (+13.95%): the pivotal PIVOT-006 trial of cretostimogene met its primary endpoint in
  intermediate-risk, high-grade Ta non-muscle invasive bladder cancer — a 68% reduction in
  recurrence risk against control (hazard ratio 0.32, p<0.0001). The full data are scheduled for
  the Society of Urologic Oncology meeting on 2 December and the company plans a broadened licence
  application in the second quarter of 2027.
- **MOH** (+11.41%): a managed-care sector rally with no company release — Centene rose 4.93% and
  Elevance about 4%. The standing supports are the late-October Q3 beat ($0.89 against $0.79) and
  a non-binding framework of at least $9.50 of 2027 EPS outlined on 10 November.
- **IEP** (-24.05%): the ex-dividend date for the $0.50 quarterly distribution, on top of a third
  quarter that swung to a $225M net loss from $287M of net income. See the note in Method notes
  on the published change.
- **INTC** (-7.02%): a shareholder class action filed on 13 November alleging the company
  understated the effect of the PC slowdown, landing alongside the semiconductor de-rating.
- **SMMT** (-16.47%): the FDA issued a complete response letter on the ivonescimab application
  in lung cancer — substantial evidence of effectiveness was not established without a
  statistically significant overall-survival gain.

### Tomorrow's three things to watch

- NVDA — 156.14 prior close, 155.5984 after hours — reports after the close, EPS estimate $2.47; the data-centre guide is the tell, not the print.
- DIS — 118.70 prior close — reports before the open, EPS estimate $1.68; streaming margin and park outlook are what decide the reaction.
- VIK — 90.28 prior close — reports before the open, EPS estimate $1.27; bookings and capacity guidance are the consumer tell into a defensive tape.

## Day's tape

### Market read

The participation read is the story of this session: the index fell less than the typical stock,
and the typical stock fell less than the chips.

| Metric | Value | Source |
|---|---|---|
| advancers | 1,086 | cron #20 us-eod CSV, 4,844 priced names |
| decliners | 3,594 | cron #20 us-eod CSV |
| unchanged | 164 | cron #20 us-eod CSV |
| median_name_move_pct | -1.17% | cron #20 us-eod CSV, `change_pct` |
| cap_weight_penalty_bp | -90 bp | bridge `price_history` (SPY -1.912% − RSP -1.008%) |
| liquid_adv_dec_ratio | 0.37 (476 : 1,279) | same CSV, `market_cap` > $2B (1,786 names) |

cap_weight_penalty_bp is negative: the equal-weight index outperformed the cap-weighted one by
90bp. This is the opposite of the narrow, mega-cap-led tape the contract was written against, and
it happened because the two mega-caps that carried the index (NVDA and the chip complex) are
exactly what fell. The median name fell 1.17% against the index's 1.92%, so the average stock
held up better than the average dollar of market cap — but 3,594 decliners against 1,086
advancers is still a broadly negative session, not a rotation inside a healthy tape.

### Cap-weight penalty — 5-day history

| Session | SPY % | RSP % | cap_weight_penalty_bp |
|---|---|---|---|
| 2026-11-10 | -0.368 | -0.032 | -34 |
| 2026-11-11 | +1.319 | +0.801 | +52 |
| 2026-11-12 | -0.354 | -0.867 | +51 |
| 2026-11-13 | -0.363 | +0.199 | -56 |
| 2026-11-16 | -1.912 | -1.008 | -90 |

The sign flipped twice in five sessions and the magnitude is now the largest of the window. The
-90bp is a function of the chip complex's weight, not of a broad flight to the equal-weighted
sid: RSP still fell 1.01% on the day.

### Index, ETF and volatility levels

| Instrument | Close | Day % | Prior close | Day low | Day high |
|---|---|---|---|---|---|
| S&P 500 | 7,416.59 | -1.92% | 7,561.67 | 7,400.15 | 7,515.60 |
| Nasdaq Composite | 24,509.76 | -2.49% | 25,136.27 | 24,460.28 | 24,882.04 |
| Dow Jones Industrial | 51,608.17 | -1.41% | 52,347.55 | 51,511.56 | 52,324.00 |
| Nasdaq 100 | 27,197.15 | -2.67% | 27,943.74 | 27,149.15 | 27,621.64 |
| Russell 2000 | 2,742.94 | -1.70% | 2,790.49 | 2,736.47 | 2,777.41 |
| Philadelphia Semiconductor | 9,610.65 | -5.28% | 10,146.32 | 9,587.11 | 9,818.76 |
| VIX | 22.91 | +18.71% | 19.30 | 19.84 | 24.52 |
| VXN | 32.90 | +11.98% | 29.38 | 31.01 | 34.14 |
| SPY | 739.95 | -1.91% | 754.37 | 738.07 | 749.82 |
| QQQ | 661.75 | -2.67% | 679.89 | 660.48 | 672.14 |
| IWM | 272.94 | -1.66% | 277.54 | 271.97 | 276.54 |
| DIA | 515.68 | -1.43% | 523.15 | 514.70 | 523.09 |
| RSP | 218.93 | -1.01% | 221.16 | 218.42 | 221.25 |
| SMH | 461.90 | -5.11% | 486.75 | 460.66 | 473.32 |
| GLD | 352.93 | -0.71% | 355.45 | 351.96 | 356.29 |
| TLT | 79.38 | 0.00% | 79.38 | 79.28 | 79.76 |

The two volatility indices were read from the bridge's dated history and cross-checked against
CBOE's own dated close file: VIX 22.91 and VXN 32.90, both agreeing to the cent. VXN's intraday
high was 34.14 and VIX's 24.52, so the close was off the highs — the panic cooled into the bell.

### Cross-asset

- Gold (GLD) -0.71%; the 10-year Treasury ETF (TLT) was flat at 79.38 and the 10-year future
  105.4063, -0.03%. Duration did not bid on an equity down day.
- Crude fell: Brent was down about 2.6% near $93.35 in Monday trade after the International
  Energy Agency said the global oil market returns to a 1.7M barrel-per-day surplus in the fourth
  quarter as Middle Eastern exports recover.
- The dollar index was not fetched this run; no level is published for it.

### Day's movers

Liquid names (market cap above $2B) from the cron #20 universe. The extreme movers of the day
were all micro-caps and are listed under Source health.

| Ticker | Close | Day % | Sector | Cap | Note |
|---|---|---|---|---|---|
| CGON | 84.78 | +13.95% | Health Care | $7.5B | PIVOT-006 met its primary endpoint |
| MOH | 233.30 | +11.41% | Health Care | $12.2B | managed-care sector rally |
| TSN | 63.96 | +8.63% | Consumer Staples | $22.5B | Q4 beat, positive beef outlook |
| HUBS | 232.00 | +6.67% | Information Technology | $11.6B | no sourced catalyst |
| POWL | 151.20 | +5.96% | Industrials | $5.5B | no sourced catalyst |
| IEP | 3.60 | -24.05% | Industrials | $2.6B | ex-dividend date; see Method notes |
| SMMT | 11.82 | -16.47% | Health Care | $9.4B | complete response letter |
| USAR | 7.13 | -12.62% | Materials | $2.7B | no sourced catalyst |
| ASTS | 28.58 | -12.33% | Communication Services | $11.1B | no sourced catalyst |
| NVTS | 7.88 | -11.96% | Information Technology | $2.1B | no sourced catalyst |

### Watchlist EOD review

Published watchlist (refs/watchlist.yaml, eight names). Prices and day ranges from the bridge;
after-hours prints from the TradingView scanner at ~22:30 ET. The ETF legs are not in the cron #20
equity universe, so their volume-versus-average is published as n/a rather than estimated.

| Ticker | Close | Day % | Day low | Day high | Volume | Vol vs avg | After-hours print |
|---|---|---|---|---|---|---|---|
| AAPL | 352.78 | -0.98% | 351.31 | 357.10 | 45,013,034 | 0.86x | 353.611 (+0.24%) |
| MSFT | 517.99 | -1.12% | 516.83 | 527.95 | 29,564,193 | 1.02x | 519.1412 (+0.22%) |
| NVDA | 156.14 | -4.12% | 155.01 | 163.00 | 329,959,344 | 1.78x | 155.5984 (-0.35%) |
| GOOGL | 283.72 | -4.07% | 282.96 | 294.13 | 34,077,805 | 0.89x | 283.90 (+0.06%) |
| AMZN | 257.75 | -3.34% | 256.68 | 262.92 | 47,704,999 | 1.02x | 258.3018 (+0.21%) |
| IWM | 272.94 | -1.66% | 271.97 | 276.54 | 25,670,035 | n/a | 272.38 (-0.21%) |
| GLD | 352.93 | -0.71% | 351.96 | 356.29 | 9,629,924 | n/a | 353.00 (+0.02%) |
| TLT | 79.38 | 0.00% | 79.28 | 79.76 | 30,912,568 | n/a | 79.3662 (-0.02%) |

Every watchlist equity closed lower and the Treasury ETF was flat on the day. The two
software mega-caps were the most resilient (AAPL -0.98%, MSFT -1.12%) and the two AI-adjacent
mega-caps the weakest (NVDA -4.12%, GOOGL -4.07%), with AMZN -3.34% alongside them.

## Sector rotation

Cap-weighted sector returns from the cron #20 universe, de-duplicated on `cap_source_symbol`
(the primary listing is kept and the `CAP_CARRIED` carrier row dropped), with `EX_DISTRIBUTION`,
`NO_CAP` and `NO_SECTOR` rows excluded from the cap-weighted column and from the denominator.
4,197 rows survive. Each sector is cross-checked against its ETF and the gap is published.

| Sector | Cap-weighted % | Median % | Sector ETF | ETF % | Gap (pp) |
|---|---|---|---|---|---|
| Consumer Staples | +0.295 | -0.441 | XLP | +0.271 | +0.02 |
| Utilities | -0.034 | -0.143 | XLU | +0.182 | -0.22 |
| Real Estate | -0.247 | -0.320 | XLRE | -0.270 | +0.02 |
| Health Care | -0.771 | -2.696 | XLV | -0.514 | -0.26 |
| Financials | -0.938 | -0.543 | XLF | -0.852 | -0.09 |
| Industrials | -1.725 | -2.009 | XLI | -1.849 | +0.12 |
| Consumer Discretionary | -1.996 | -1.159 | XLY | -1.525 | -0.47 |
| Materials | -2.152 | -2.441 | XLB | -1.455 | -0.70 |
| Energy | -2.202 | -2.806 | XLE | -1.955 | -0.25 |
| Communication Services | -2.891 | -0.939 | XLC | -1.720 | **-1.17** |
| Information Technology | -2.956 | -3.276 | XLK | -3.242 | +0.29 |

Top three: Consumer Staples, Utilities, Real Estate. Bottom three: Information Technology,
Communication Services, Energy. Every cap-weighted sector return is inside ±20%, so no
doubled-parent-cap inflation is present in the column.

Two gaps are worth naming. **Communication Services** is the outlier at -1.17pp: GOOGL
($3,469B cap, -4.07%) alone contributes -1.27pp of the sector's -2.891%, and the sector ex-GOOGL
is -1.625% — the cap-weighted column inherits that single-name concentration and should not be
read as a read on the other communication names. **Materials** shows a -0.70pp gap between the
cap-weighted -2.152% and the ETF's -1.455%, so part of the sector's decline is in larger names
than the ETF's mid-cap weighting reflects.

The defensive read is real but narrow: staples, utilities and real estate were the only three
sectors with cap-weighted returns above -0.25%, and the median name inside staples was still
-0.441%. Nobody was buying this tape; the buyers were buying the parts of it that had fallen
least.

## After-hours movers

The TradingView extended-hours screen with a $1B market-cap floor and after-hours volume above
50,000 shares, read at ~22:30 ET. Every row below passed the identity check
`postmarket_change == (ah_last − prior_close) / prior_close`, every venue is a major US exchange
(no OTC lines), and every prior close was independently confirmed against the bridge's
`get_quotes` before publication.

| ticker | prior_close | ah_last | ah_high | ah_low | ah_volume | gap_pct | ah_range_pct | gap_fill_level |
|---|---|---|---|---|---|---|---|---|
| SLS | 7.47 | 7.99 | 8.7924 | 7.3229 | 1,587,625 | +6.96 | 19.67 | 7.47 |
| ACM | 72.50 | 77.45 | 77.9628 | 71.92 | 587,569 | +6.83 | 8.33 | 72.50 |
| SITE | 110.90 | 116.75 | 118.16 | 110.81 | 133,880 | +5.28 | 6.63 | 110.90 |
| TEM | 64.76 | 66.9768 | 69.68 | 64.21 | 607,534 | +3.42 | 8.45 | 64.76 |
| LBRT | 12.25 | 12.66 | 12.66 | 12.25 | 464,895 | +3.35 | 3.35 | 12.25 |
| OMER | 16.68 | 15.40 | 17.532 | 14.45 | 470,492 | -7.67 | 18.48 | 16.68 |
| ARQT | 27.15 | 25.7875 | 27.15 | 25.7875 | 269,910 | -5.02 | 5.02 | 27.15 |
| SPG | 232.78 | 222.3305 | 232.78 | 222.3305 | 580,680 | -4.49 | 4.49 | 232.78 |
| CPRI | 20.55 | 19.65 | 20.60 | 19.23 | 553,096 | -4.38 | 6.67 | 20.55 |
| ASND | 271.73 | 260.02 | 271.73 | 260.02 | 114,995 | -4.31 | 4.31 | 271.73 |

Every row's after-hours range traded back through the 16:00 close, so on the contract's
deterministic rule the gap fills at the prior close in all ten cases — the levels are marks, not
targets.

## After-hours earnings reactions

- **ACM** +6.83% after hours: fiscal Q4 adjusted EPS $1.63 against $1.59 consensus, revenue
  $3.88B (-7% y/y, below the $4.01B estimate), net service revenue +3% with design +6%, segment
  adjusted operating margin a record 18.2%, total backlog a record $28.0B (+13%) on record wins of
  $13.4B, and a first fiscal-2027 adjusted EPS guide of $6.15-6.35 (midpoint $6.25 against $6.24
  consensus). The quarterly dividend was raised 10% to $0.34. The call is 08:00 ET on Tuesday.
- **RCAT** -26.19% after hours (scanner, ~22:30 ET; -24.65% at 18:01 ET per StockTitan): third
  quarter results plus the withdrawal of the full-year 2026 revenue target, with funding and
  contract awards coming in more slowly than expected. Market cap $539M, so it is below this
  screen's floor — see Source health.
- **SPG** -4.49% after hours: third quarter real estate FFO of $3.37 per diluted share, +4.7%
  y/y, and a raised full-year 2026 FFO guidance to $13.30-13.40, with domestic property NOI +6.6%.
  The numbers were fine; the print is what the tape did with them.
- **ARQT** -5.02% after hours: the mid-stage trial of bosakitug in atopic dermatitis missed both
  its main goal and its secondary goals.
- **OMER** -7.67%, **CPRI** -4.38% and **ASND** -4.31%: no company release or catalyst was found
  in the sources searched for these three names; the prints are published as observed.
- **SLS** +6.96%, **SITE** +5.28%, **TEM** +3.42% and **LBRT** +3.35% after hours: no catalyst was
  sourced for these four names in the searches run.
- **TSN** +8.63% in regular hours: fourth quarter adjusted EPS $0.61, down 47% y/y, with a
  positive beef-segment outlook against FY2027 sales guided down 3.5% to 5.5%.

## Open research queue

1. **How much of the -90bp cap-weight penalty is a genuine rotation into defensives and how much
   is mechanical AI de-grossing?** It matters because the two readings imply opposite positions:
   a durable rotation says staples, utilities and real estate have money in them, while
   mechanical de-grossing says the penalty will reverse the moment the chip complex stops
   falling. It would be resolved by running the cap-weighted sector column for the next five
   sessions against the same SPY/RSP spread — if the defensive sectors hold their relative
   bid while the penalty normalises, it is de-grossing; if it fades with the penalty, it is
   rotation.
2. **With VIX +18.7% and the CBOE total put/call at only 0.95 (equity 0.73), who is hedging?** It
   matters because a volatility market bid without a put bid is an options-market positioning
   signal rather than a directional one — it can resolve into sharp selling on a chip earnings
   print without a slow unwind. It would be resolved by tracking the total and equity put/call
   ratios and the VIX term structure into Wednesday's results, and by checking whether the
   volatility bid came from VIX call spreads rather than outright put buying.
3. **Is the participation read distorted by ex-distribution rows?** It matters because the median
   name and the advancer/decliner counts are the metrics that say whether this was a rotation or
   a de-grossing, and cron #20's `change_pct` is not adjusted for distributions for the 255 rows
   flagged `EX_DISTRIBUTION` — Icahn Enterprises alone published -24.05% against a price-only move
   of -15.09%. It would be resolved by recomputing the participation read on a
   distribution-adjusted universe and publishing both numbers side by side.

## Source health

| Source | Query / URL | Status | Result |
|---|---|---|---|
| MCP bridge `market-recap` `get_quotes` | 26 symbols for the tape (indices, ETFs, watchlist, futures) plus 16 after-hours names cross-checked | ok | 42 of 42 found; every row's `as_of` carries the 2026-11-16 session date |
| MCP bridge `market-recap` `price_history` | SPY, RSP, 11 sector ETFs, SMH, GDX, ^VIX, ^VXN, 5 futures, 2026-11-03 to 2026-11-16 | ok | 22 of 22 served with dated rows |
| CBOE dated index history | `https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv` and `VXN_History.csv` | ok (200) | VIX 22.91 and VXN 32.90 on 11/16/2026 — agree to the cent with the bridge history |
| CBOE daily statistics | `https://www.cboe.com/us/options/market_statistics/daily/` | ok (200) | payload `selectedDate` 2026-11-16 = fire date; `prevTradingDay` 2026-11-16 |
| TradingView scanner (americas) | 6 pulls: after-hours gainers/losers with a $1B floor, the same screen without the floor, watchlist names, universe movers | ok | every pull returned HTTP 200; the two $1B-floor pulls returned 200 rows of 2,081 names each, which is the deliberate first page of a sorted pull, not truncation |
| cron #20 EOD universe | `us-eod/2026-11-16.csv` in `karizaco/minimax-cloud-outputs` (main) | ok | 4,890 rows, 4,844 priced |
| Published watchlist | `refs/watchlist.yaml` in `karizaco/minimax-cloud-outputs` (main) | ok | 8 names |
| MCP availability probe | `probe_mcp.py` | ok | `catalog_ok total=135 finance_tools=0` — no finance MCP registered, as expected; not an error |
| Web (catalysts, calendars) | web_search across market wrap, movers, earnings and economic calendars | ok | see Method notes for the source-disagreement note on one release time |

**Leaders outside the published table.** The after-hours screen's $1B floor hides the session's
real leaders, so the same screen was pulled once without the floor. Above the table: CSAI +51.54%
(market cap $1.1M), AYTU +43.96% ($19.8M), GLAS +31.78% ($99.9M), AKAN +22.62% ($5.8M).
Below the table: BAER -33.03% ($14.1M), STEM -29.95% ($19.0M), RCAT -26.19% ($539M),
VIVK -26.13% ($0.6M). The table is the contract's screen, not the whole after-hours tape.

**Micro-cap extremes of the regular session**, for the same reason: VIVK +80.19%, CLRO +41.84%,
ETS +34.93%, CVM +30.20%, POLA +28.56% on the way up; DVLT -53.33%, MTEX -40.32%, XXII -35.96%,
CNTY -35.19%, MBOT -34.16% on the way down. The day's movers table is restricted to the $2B-plus
set for the same reason.

**Cross-source differences carried, not blended.** The regular-session close of TSN is published
as the cron #20 value (+8.63%); a market wrap put the same move at +8.72%, a different prior-close
convention. The scanner's after-hours prints are the source of record for the extended session;
StockTitan's earlier RCAT print (-24.65% at 18:01 ET) is named rather than averaged into the
scanner's -26.19%.

## Method notes

- **Fire resolution.** `window_check.sh` resolved the fire against the session's scheduled instant
  (2026-11-16, `stall_min` 2 — inside the 5-minute threshold, so no stall is counted as an error)
  and confirmed the 2026-11-16 session was a trading day. Every number in this brief is for the
  16 November session.
- **Universe and de-duplication.** The participation read and the sector column both come from
  cron #20's `us-eod/2026-11-16.csv`: 4,890 rows, 4,844 of them priced, 46 without a usable
  `change_pct`. The liquid set for `liquid_adv_dec_ratio` is `market_cap` above $2B (1,786 names).
  The cap-weighted sector column keeps one row per `cap_source_symbol` — where two share classes
  exist, the primary listing (the row without the `CAP_CARRIED` flag) is kept and the carrier row
  dropped — and excludes `EX_DISTRIBUTION`, `NO_CAP` and `NO_SECTOR` rows from both the column
  and its denominator. The `NO_SECTOR` bucket (369 rows) is excluded, not ranked as a sector.
- **One source per field.** Prices, index levels, futures and the cap-weight history come from
  the bridge's `market-recap` pack; extended-hours prints and the sector/mover screens come from
  the TradingView scanner; the participation read and the sector column come from cron #20's CSV;
  volatility closes are read from the dated history and cross-checked against CBOE's dated files;
  the put/call comes from the CBOE daily statistics payload. The SPY/RSP session returns in the
  penalty table are printed to three decimals from `price_history`; the levels table prints the
  settled quote row at two decimals, so the same session reads -1.912% there and -1.91% here.
- **Volatility indices were not taken from the quote row.** Both were read from the dated history
  and confirmed against CBOE's dated close files; the quote row's `as_of` for a volatility index
  was checked rather than assumed.
- **The put/call split is published because one payload carries it.** The CBOE page's embedded
  object gave total 0.95, index 1.01, ETP 1.16, equity 0.73, VIX 0.42, SPX 1.23 and XSP 1.01
  for the session stamped 2026-11-16, and the underlying volumes reconcile: 7,655,860 puts over
  8,018,994 calls is 0.95, and the equity split reproduces 0.73. No component was taken from a
  second source.
- **The ex-dividend caveat on Icahn Enterprises.** Cron #20 published IEP's change as -24.05%,
  measured against the $4.74 pre-distribution close; the price-only move on the 16 November
  ex-dividend date was -15.09% ($4.24 to $3.60). The published figure is cron #20's field, and
  the row is flagged `EX_DISTRIBUTION` in the CSV, so the participation read may carry a small
  dividend-adjustment bias across its 255 flagged rows. This is the subject of the third research
  question.
- **After-hours prints are a snapshot.** The extended-hours tape keeps moving: RCAT read -24.65%
  at 18:01 ET and -26.19% at the ~22:30 ET pull. All extended-hours numbers here are the
  scanner's print at the fire, and they should be treated as a snapshot of a live tape.
- **Futures are live, not a stale settlement.** Every futures row carried an `as_of` between
  22:22 and 22:23 ET — after the 18:00 ET Globex reopen — and the bridge's dated history
  confirms the reference close for each contract on 2026-11-16. This is a Monday, so the
  overnight move genuinely exists.
- **No level was published that was not read.** Where a field was unavailable it is printed as
  `n/a` and named: the watchlist ETFs' volume-versus-average (the cron #20 universe is equities
  only), and the Russell 2000's volume (the bridge did not supply it).
- **Read-only.** No trades are placed or implied; this brief is a summary of a closed session and
  the setup it leaves behind.
