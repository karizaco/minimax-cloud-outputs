---
date: 2026-11-19
cron: 23-agentic-post-market-brief
contract: postmkt-artifact-v2
fire_time_et: 22:30
snapshot_et: 22:20-22:40
session: 465275316924740
scheduled_at_ms: 1795145411569
status: ok
source: MCP-over-HTTP bridge market-recap (get_quotes, price_history, market_snapshot); TradingView US scanner (america/scan); cron #20 us-eod/2026-11-19.csv; CBOE daily statistics page and CBOE dated VIX/VXN close files; refs/watchlist.yaml; issuer releases and press via web
primary_source: bridge market-recap get_quotes / price_history (the quote source of record)
universe: cron #20 us-eod/2026-11-19.csv - 4,884 rows, 4,845 priced, 4,736 carrying a market cap; liquid set (cap >= $2B) 1,769 names
degraded_sources: 0
---

# Post-market brief — Thursday, 19 November 2026

## TL;DR

The AI trade broke, and it broke globally. The S&P 500 fell **2.02% to 7,175.83** — a sixth straight
loss, the longest run since April 2024 — with the Dow down 1,101 points to 49,097.06 and the Nasdaq
Composite through 24,000. The catalyst was Anthropic's Nasdaq debut (ticker ANT) at midday: the stock
opened +34% and the whole complex sold off on the print. Hunterbrook Capital's short report on AMD
took the chip trade down separately, and the Fed's October minutes plus Governor Waller's argument
for a half-point December hike repriced the policy path. The VIX closed **28.44, +15.80%**, its
highest close since 30 March, after touching 29.13 intraday.

The tape was broad, not narrow. In cron #20's 4,884-name universe, **816 advancers** against **3,861
decliners** (168 unchanged) and a **median_name_move_pct** of **-1.54**. Among names above $2B the
**liquid_adv_dec_ratio** is **0.13** — 197 up against 1,552 down. The **cap_weight_penalty_bp** is
**-20**: SPY -1.962% against RSP -1.764%, so the equal-weight index *outperformed* by two tenths of a
point and the selling was not a mega-cap story. Every one of the eleven S&P sectors closed lower,
Energy least at -0.74% and Consumer Discretionary worst at -3.07%.

Overnight is the interesting part, and it cuts both ways. The US equity futures are **flat to the
cash close** (ES 7,178.75 against the cash close of 7,175.83) while the cash markets in Asia are
being sold hard: the Nikkei 225 is down 4.49% after Japan's core inflation printed 2.2%, the highest
this year, and South Korea's Kospi is down about 4.3%. Gold is down another 4.34% against its
Thursday settlement. The US futures market has not extended the selloff; Asia has not stopped it.

## Tomorrow's setup — Friday, 20 November 2026

### Futures and the overnight setup

CME equity-index futures are trading (Globex, reopened 18:00 ET Thursday), so this is a live
overnight print, not a stale settlement. Every row carries a bridge `as_of` of 22:21 ET, nine minutes
before the fire.

| Instrument | Last | Quoted prior settle | Change vs settle | vs cash close | as_of |
|---|---|---|---|---|---|
| ES=F (S&P 500) | 7,178.75 | 7,197.25 | -0.26% | **+0.04%** | 22:21 ET |
| NQ=F (Nasdaq 100) | 26,460.25 | 26,600.25 | -0.53% | -0.21% vs NDX 26,517.05 | 22:21 ET |
| YM=F (Dow) | 49,152 | 49,180 | -0.06% | +0.11% vs DJI 49,097.06 | 22:21 ET |
| RTY=F (Russell 2000) | 2,656.20 | 2,663.30 | -0.27% | +0.04% vs RUT 2,655.11 | 22:21 ET |
| ZN=F (10-year) | 106.109 | 105.875 | +0.22% | n/a (bond future) | 22:20 ET |

The sign flip is the story: against the futures' own prior settlement the move looks like another
small down-day, but measured against the cash close the futures are essentially **flat**, and the
Globex range (7,160.75 low to 7,199.25 high) shows the overnight session faded 0.5% and then
recovered most of it. The US futures market has not repriced the selloff. Asia has.

Live Asia cash (bridge, stamped 22:21-22:35 ET):

| Market | Level | Change | Note |
|---|---|---|---|
| Nikkei 225 | 56,775.04 | **-4.49%** | live; core CPI 2.2%, highest this year, raises December hike odds |
| Kospi | n/a (level not read) | about -4.3% | CNBC live blog, early Asia |
| Hang Seng | 22,432.28 | -1.79% | live |
| Shanghai Composite | 3,522.38 | -1.54% | live |

Also live overnight: WTI crude 82.72 (+0.34%), the dollar index 103.855 (-0.04%), bitcoin 62,003.68
(+0.16%), and December gold futures 3,525.70 (-4.34% against the 3,685.50 settlement Reuters
confirms). The 10-year Treasury yield settled at 5.052%, down 1.4bp, and the 10-year future is
+0.22% — a modest flight to quality that did not stop equities from falling.

The setup question for Friday: US futures are pricing this as contained while Asia is pricing it as
systemic. The 10:00 ET Michigan sentiment release, with its inflation-expectations sub-readings, is
the first hard datapoint that can settle that disagreement.

### Economic calendar

Friday 20 November 2026 is a light release day.

| Time (ET) | Release | Forecast | Previous |
|---|---|---|---|
| 10:00 | University of Michigan final consumer sentiment | 51.5 | 51.0 |
| 10:00 | University of Michigan final 1-year inflation expectations | 4.2% | 4.3% |
| 10:00 | University of Michigan final 5-10 year inflation expectations | 3.4% | 3.4% |
| 12:45 | New York Fed staff nowcast | n/a | n/a |
| 13:25 | Federal Reserve — Governor Waller speaks | n/a | n/a |
| 17:15 | Federal Reserve — Governor Cook speaks | n/a | n/a |

Housing starts (October, 1,309K) and the FOMC minutes both printed earlier in the week; initial
jobless claims were due Thursday. The market's policy pricing is now a **December hike**, not merely
no more cuts: CME FedWatch was quoted at a 97.3% chance of a 25bp increase with 2.7% on 50bp in
overnight Reuters copy, against roughly 94%/6% earlier in the US session. Wall Street's own
consensus is a quarter-point; Waller has argued publicly for fifty.

### Earnings calendar

Friday's roster is thin — 8 to 14 names depending on the calendar vendor, all but two before the
open. Sources: Yahoo Finance earnings calendar for 2026-11-20, EarningsWhispers, Market Chameleon
and Nexqual (these disagree on the count and on some names; the list below is the intersection
plus names two sources carry).

| Ticker | Company | When | EPS estimate | Prior close |
|---|---|---|---|---|
| BJ | BJ's Wholesale Club | before the open | 1.09 | n/a (not read) |
| MOG-A | Moog | before the open | 2.68 | 328.07 |
| FRO | Frontline | before the open | 2.44 | 44.75 |
| IESC | IES Holdings | before the open | 2.81 | 166.90 |
| BKE | The Buckle | before the open | 0.95 | 41.78 |
| RLX | RLX Technology | before the open | 0.23 | 1.46 |
| WRD | WeRide | before the open | -0.99 | 3.265 |
| BSP | Bending Spoons | before the open | 0.30 | 41.70 |
| DLNG | Dynagas LNG Partners | after the close | 0.34 | 3.00 |
| KPTI | Karyopharm Therapeutics | after the close | -1.05 | n/a (not read) |

Two entries carry extra weight. **Bending Spoons** reports Friday morning as the buyer of Intuit's
Mailchimp — its own print lands in the same session that opens on Intuit's guidance cut. **WeRide**
fell 11.04% on Thursday and reports before the open, so the name arrives pre-sold; no sourced
catalyst for the Thursday decline was found, so the move is disclosed without an explanation.

### News to watch for the top movers

- **SNEX -26.71%** — fiscal Q4 diluted EPS of $0.66 against a $0.81-0.88 consensus, a miss of at
  least $0.15 and 23% below the street. Institutional segment income fell 25% and Self-Directed/
  Retail 56%; securities revenue per million fell 23% on narrower spreads. The revenue beat ($1.46bn
  operating revenue against a $1.38bn consensus) and the record fiscal year did not save it. Shares
  traded 39.28 after hours, a further -0.43%.
- **INSM +20.58%** — Bloomberg reported Sanofi is working with advisers on a possible acquisition;
  no formal proposal has been made and the talks may not produce a deal. Shares hit 149.07 intraday
  and closed 144.46, and traded 144.60 after hours. The stock had been down about 40% over the prior
  twelve months.
- **WSM -15.16%** — fiscal Q3 net revenue of $1.99bn against a $2.00bn expectation, comparable brand
  revenue +5.1% against +5.6% expected, adjusted EPS $2.19 in line. Full-year guidance was only
  reiterated, and gross margin ex the $29.3m tariff refund fell about 50bp as oil-driven supply-chain
  costs bit. It traded at roughly 26x forward earnings against a five-year average near 16x.

AMD is the fourth name that matters and is not in the day's top three by move: it closed **-7.72%**
on Hunterbrook Capital's short report alleging continued firmware shipments to blacklisted Chinese
server makers, with the company calling the report a misrepresentation, and it fell a further
-3.41% after hours to 472.51.

### Tomorrow's three things to watch

- INTU — 279.74 after-hours last, gap fill at the 310.02 close — fiscal-2027 revenue was cut to
  $23.08-23.37bn on weaker credit-scoring revenue and Mailchimp is being sold for $3.68bn; the
  full-year guide is the tell.
- AMD — 472.51 after-hours last, 489.19 prior close — Hunterbrook's export-control short report and
  the company's rebuttal; whether the artificial-intelligence trade keeps unwinding is the tell.
- INSM — 144.46 close, 144.60 after hours — Sanofi is reported weighing a takeover; whether a
  formal proposal arrives or the rumor premium unwinds is the tell.

## Day's tape

### Market read

One population throughout: cron #20's published universe for 2026-11-19. The liquid set is names
above a $2B market cap.

| Metric | Value |
|---|---|
| advancers | 816 |
| decliners | 3,861 |
| unchanged | 168 |
| median_name_move_pct | -1.54 |
| cap_weight_penalty_bp | -20 |
| liquid_adv_dec_ratio | 0.13 |

The liquid set holds 1,769 names: 197 advancers, 1,552 decliners, 20 unchanged, and a median move
of -1.657%. The cap-weight penalty is negative, which means the equal-weight index outperformed —
the opposite of the narrow, mega-cap-led selloff this tape was not.

### Cap-weight penalty — 5-day history

| Session | SPY % | RSP % | cap_weight_penalty_bp |
|---|---|---|---|
| 2026-11-13 | -0.363 | +0.199 | -56 |
| 2026-11-16 | -1.912 | -1.008 | -90 |
| 2026-11-17 | -1.015 | -1.448 | +43 |
| 2026-11-18 | -0.306 | -0.153 | -15 |
| 2026-11-19 | -1.962 | -1.764 | -20 |

The penalty has been flipping sign session by session all month — five sessions, three negative —
so the cap-weighted and equal-weight tapes have been trading within a band rather than diverging.
Today is the second-worst equal-weight day of the stretch in percentage terms, and the cap-weighted
index did slightly better, not worse.

### Index, ETF and volatility levels

| Instrument | Close | Change | Day range | as_of |
|---|---|---|---|---|
| S&P 500 | 7,175.83 | -2.02% | 7,173.63 - 7,415.64 | 16:59 ET |
| Nasdaq Composite | 23,879.20 | -2.25% | 23,870.70 - 24,939.62 | 17:15 ET |
| Dow Jones Industrial Average | 49,097.06 | -2.19% | 49,091.92 - 50,454.81 | 16:59 ET |
| Nasdaq 100 | 26,517.05 | -2.21% | 26,481.82 - 27,749.35 | 17:15 ET |
| Russell 2000 | 2,655.11 | -2.18% | 2,653.92 - 2,730.01 | 16:30 ET |
| PHX Semiconductor | 9,419.72 | -2.41% | 9,412.19 - 10,109.88 | 17:15 ET |
| VIX | 28.44 | +15.80% | 21.84 - 29.13 | 16:15 ET |
| VXN | 36.48 | +10.14% | 30.34 - 37.02 | 16:15 ET |
| SPY | 715.87 | -1.96% | 715.65 - 739.90 | 16:00 ET |
| QQQ | 645.04 | -2.19% | 644.34 - 676.46 | 16:00 ET |
| IWM | 264.22 | -2.18% | 263.74 - 271.80 | 16:00 ET |
| DIA | 490.79 | -2.18% | 490.73 - 504.41 | 16:00 ET |
| RSP | 211.63 | -1.76% | 211.34 - 216.25 | 16:00 ET |
| SMH | 447.48 | -2.62% | 447.20 - 479.96 | 16:00 ET |
| GLD | 335.18 | -1.76% | 335.05 - 340.52 | 16:00 ET |
| TLT | 80.35 | +0.16% | 79.81 - 80.45 | 16:00 ET |

Every index row carries a 19 November `as_of`; no row is a prior session's reading. The two
volatility indices were read from the bridge's dated `price_history` and cross-checked to the cent
against CBOE's own dated close files (VIX 28.44, VXN 36.48 for 11/19/2026). The Russell 2000 row
carries no traded volume — index quotes do not have one — so that cell is n/a rather than zero.

The intraday shape matters more than the close. The S&P traded as high as 7,415.64 before the
Anthropic listing at midday, then sold off to close near its low of 7,173.63. The VIX's 21.84 low
came before that, and its 29.13 high came after.

### Cross-asset

| Instrument | Level | Change | Note |
|---|---|---|---|
| 10-year Treasury yield (^TNX) | 5.052% | -0.28% | settled 15:00 ET |
| 10-year Treasury future (ZN=F) | 106.109 | +0.22% | live 22:20 ET |
| Dollar index (DX-Y.NYB) | 103.855 | -0.04% | live 22:26 ET |
| WTI crude (CL=F) | 82.72 | +0.34% | live 22:26 ET |
| Gold — December future (GC=F) | 3,525.70 | -4.34% | vs the 3,685.50 settlement Reuters confirms |
| Gold — GLD ETF | 335.18 | -1.76% | session; after hours 329.48, -1.70% |
| Bitcoin | 62,003.68 | +0.16% | live 22:36 ET |

Yields eased and the dollar held near a 19-month high, but the 10-year future barely moved — this
was not a flight-to-quality session in size. Gold is the leg that broke: a 14-month low, on the
strongest December-hike pricing of the cycle. The gold ETF's after-hours print (-1.70%) does not
mark the futures' -4.34% overnight move; the ETF's extended-hours book repriced lazily while the
futures moved continuously. Treat the futures as the overnight gold signal and the ETF as the
session leg.

### Day's movers

Liquid names (market cap above $2B) from cron #20's universe. Drivers are sourced or explicitly
marked as not sourced.

| Ticker | Company | Day change | Market cap | Driver |
|---|---|---|---|---|
| INSM | Insmed | +20.62% | $31.5B | Bloomberg: Sanofi reported weighing a takeover |
| VVV | Valvoline | +10.31% | $4.7B | no sourced driver found |
| AMBA | Ambarella | +7.85% | $2.6B | no sourced driver found |
| IEP | Icahn Enterprises | +6.74% | $2.1B | no sourced driver found |
| PANW | Palo Alto Networks | +6.42% | $294.9B | fiscal Q1 EPS $1.05 on $3.44bn revenue, full-year guidance raised, and a $4.5bn all-stock agreement to acquire Applied Compute |
| SNEX | StoneX Group | -26.71% | $4.7B | fiscal Q4 diluted EPS $0.66 vs a $0.81-0.88 consensus |
| SLS | SELLAS Life Sciences | -17.21% | $3.0B | $150m offering priced at $13.00, a 28% discount to the prior close; closes 20 November |
| WSM | Williams-Sonoma | -15.08% | $26.0B | fiscal Q3 revenue $1.99bn vs $2.00bn expected; comps +5.1% vs +5.6% expected |
| WRBY | Warby Parker | -14.29% | $3.0B | no sourced driver found |
| QNT | Quantinuum | -12.60% | $7.4B | no sourced driver found |

The universe file's percentages and the bridge's differ by a few basis points on the names both
carry — INSM +20.62% against +20.58%, WSM -15.08% against -15.16% — a settlement convention
difference, not a disagreement about the tape. The table carries the universe file's numbers
because its cap and sector fields come from the same file.

### Watchlist EOD review

Prices, ranges and volume from the TradingView scanner and the bridge; relative volume is the
scanner's 10-day relative volume.

| Ticker | Close | Day change | Day range | Volume | Volume vs 10-day avg | After hours | AH change |
|---|---|---|---|---|---|---|---|
| AAPL | 349.21 | -0.94% | 346.47 - 355.28 | 40,906,700 | 0.96x | 351.56 | +0.67% |
| MSFT | 498.30 | -1.78% | 498.16 - 526.49 | 29,350,379 | 1.06x | 494.89 | -0.68% |
| NVDA | 145.98 | -3.30% | 145.71 - 158.13 | 322,939,561 | 0.82x | 144.67 | -0.90% |
| GOOGL | 272.66 | -3.46% | 272.36 - 295.43 | 49,718,485 | 1.46x | 273.31 | +0.24% |
| AMZN | 257.37 | -3.87% | 256.75 - 274.00 | 53,117,120 | 1.18x | 256.37 | -0.39% |
| IWM | 264.22 | -2.18% | 263.74 - 271.80 | 31,433,136 | 1.20x | 263.67 | -0.21% |
| GLD | 335.18 | -1.76% | 335.05 - 340.52 | 11,230,607 | 1.14x | 329.48 | -1.70% |
| TLT | 80.35 | +0.16% | 79.81 - 80.45 | 38,752,266 | 1.04x | 80.40 | +0.06% |

The three big-cap tech legs all printed a session high in the morning and a close near their low.
NVDA and GOOGL closed on their lows of the day (145.71 and 272.36) after touching 158.13 and
295.43. The watchlist's two non-equity legs held their own: bonds up, gold down with the metal.

## Sector rotation

Cap-weighted and median moves from cron #20's universe, de-duplicated on `cap_source_symbol` with
`CAP_CARRIED` carrier rows, `EX_DISTRIBUTION` rows, `NO_CAP` rows and the 18 `NO_SECTOR` rows
excluded, as cron #20's rules require. Each sector is cross-checked against its ETF.

| Sector | cap_weighted % | median % | Names | ETF | ETF % | Gap (pp) |
|---|---|---|---|---|---|---|
| Energy | -0.74 | -1.31 | 177 | XLE | -0.65 | 0.09 |
| Utilities | -1.24 | -1.19 | 80 | XLU | -1.24 | 0.00 |
| Consumer Staples | -1.45 | -1.77 | 142 | XLP | -1.45 | 0.00 |
| Financials | -1.56 | -0.93 | 1,143 | XLF | -1.49 | 0.07 |
| Real Estate | -1.79 | -1.83 | 179 | XLRE | -1.70 | 0.09 |
| Health Care | -1.86 | -1.88 | 820 | XLV | -2.05 | 0.19 |
| Information Technology | -1.95 | -2.53 | 492 | XLK | -1.90 | 0.05 |
| Materials | -1.97 | -2.29 | 153 | XLB | -2.06 | 0.09 |
| Industrials | -2.37 | -2.02 | 535 | XLI | -2.00 | 0.37 |
| Communication Services | -3.01 | -2.41 | 155 | XLC | -2.67 | 0.34 |
| Consumer Discretionary | -3.07 | -3.50 | 382 | XLY | -2.79 | 0.28 |

Top three by cap-weighted return: Energy, Utilities, Consumer Staples. Bottom three: Consumer
Discretionary, Communication Services, Industrials. Every cap-weighted figure sits inside ±20%, and
every sector's gap to its own ETF is under 0.5pp — so no sector row is carrying a single-name
concentration effect and none of these is a rotation rather than a decline.

The dispersion is narrow (0.33pp between the best and worst sector) compared with the 2.02% index
move, and the defensive sectors led by only a little. That is the signature of a de-risking tape
rather than a rotation: nothing worked, and the things that usually hold up held up least.

## After-hours movers

TradingView extended-hours screen, type stock and dr, market cap above $1B, after-hours volume
above 50,000 shares, run twice (descending and ascending) and ranked by absolute change. Levels and
the 22:35 ET scanner print are the source of record.

| ticker | prior_close | ah_last | ah_high | ah_low | ah_volume | gap_pct | ah_range_pct | gap_fill_level |
|---|---|---|---|---|---|---|---|---|
| OPEN | 1.46 | 1.56 | 1.58 | 1.45 | 6,995,753 | +6.85 | 8.90 | 1.46 |
| BBVA | 24.43 | 25.90 | 25.90 | 23.01 | 65,868 | +6.01 | 11.82 | 24.43 |
| ESE | 223.02 | 235.00 | 235.01 | 223.02 | 55,141 | +5.37 | 5.38 | 223.02 |
| BSP | 41.70 | 43.80 | 47.68 | 39.50 | 290,252 | +5.04 | 19.62 | 41.70 |
| KEP | 9.07 | 9.48 | 9.48 | 9.07 | 146,192 | +4.52 | 4.52 | 9.07 |
| INTU | 310.02 | 279.74 | 310.02 | 263.00 | 1,197,117 | -9.77 | 15.17 | 310.02 |
| MIR | 17.18 | 16.23 | 17.22 | 16.23 | 836,203 | -5.52 | 5.75 | 17.18 |
| ROST | 219.88 | 208.53 | 220.09 | 193.00 | 789,312 | -5.16 | 12.32 | 219.88 |
| UMC | 13.40 | 12.79 | 13.40 | 12.50 | 2,257,919 | -4.55 | 6.72 | 13.40 |
| SOLV | 85.80 | 82.09 | 85.80 | 82.09 | 231,031 | -4.32 | 4.32 | 85.80 |

Every row was verified before publication: `postmarket_change` equals
`(postmarket_close - close) / close × 100` for all ten, and every `prior_close` was confirmed
against the primary listing through the bridge. No row is over-the-counter and no prior close is a
suspiciously round number, so the table is not carrying a stale-base print. The `gap_fill_level`
rule was applied deterministically — where the after-hours range contains the 16:00 close the gap
fills at that close, otherwise the reference is the after-hours midpoint.

The screen's $1B floor hides the session's actual leaderboard. The same screen run without the
market-cap floor returns MEDS at +55.28%, WAST at +34.37% (over-the-counter, excluded), VIVS at
+21.10%, CIGL at +20.49% and CALC at +17.95% on the upside, and ONFO at -16.80%, CODX at -16.20%,
INLF at -14.45% and GRSD at -13.52% on the downside. The table is the liquid tape, not the whole
after-hours tape.

## After-hours earnings reactions

Three S&P 500 names reported after Thursday's close, and all three beat — the tape sold the
guidance anyway.

| Ticker | EPS | EPS estimate | Revenue | Revenue estimate | After-hours change | Level |
|---|---|---|---|---|---|---|
| INTU | $2.91 | $2.46-2.70 | $4.35bn | $4.30-4.31bn | -9.77% | 279.74 after hours, 310.02 close |
| ROST | $1.91 | $1.86 | $6.26bn | $6.23-6.25bn | -5.16% | 208.53 after hours, 219.88 close |
| KEYS | $3.61 | $3.37 | $1.99bn | $1.95bn | +0.31% | 282.30 after hours, 281.42 close |

- **Intuit** beat on revenue and earnings and still fell 9.77% after hours: fiscal-2027 revenue was
  cut to $23.08-23.37bn from $23.28-23.51bn, entirely on weaker credit-scoring revenue, and the
  adjusted earnings range was left at $22.88-23.12, below the $23.62 the street wanted. Intuit also
  agreed to sell Mailchimp to Bending Spoons for about $3.68bn — the same company reporting Friday
  morning.
- **Ross Stores** beat on everything — EPS $1.91, revenue $6.26bn, comparable sales +8% — and raised
  full-year EPS to $8.75-8.84, but guided fourth-quarter EPS to $2.16-2.25 against a $2.26-2.28
  consensus. The holiday guide is the whole story. Its after-hours range was wide, touching 193.00.
- **Keysight** also beat and is the only one of the three that rose, at +0.31%.
- **Gap** cut its full-year profit outlook to $2.29-2.34 and rose 3.61% after hours to 19.47, and
  **C.H. Robinson** fell 6.32% in early extended trading.

Vendor dispersion on the extended-hours tape is wide and the numbers keep moving. Intuit was
-9.77% on the TradingView scanner at about 22:35 ET, -9.79% at 18:30 ET on another feed, -11% and
-13% on two evening snapshots; Ross was -5.16% on the scanner and -8.6% to -9% on others earlier in
the session. The scanner's print is published above as the source of record and the others are
named here rather than blended into a single figure.

## Open research queue

1. **Is the futures' flat overnight print a genuine stabilisation, or has the US session simply not
   caught up to Asia?** The US equity futures sit at parity with the cash close while the Nikkei is
   down 4.49% and the Kospi about 4.3%. Either Friday is a second leg down or Asia is about to
   catch up to a stabilised US tape, and the two readings imply opposite trades. It matters because
   it decides whether the VIX's 28.44 close is a ceiling or a floor. The pre-open cash index
   indications and the 10:00 ET Michigan inflation-expectations readings would settle it.
2. **Who is actually carrying the artificial-intelligence trade's risk now?** Anthropic's debut did
   not resuscitate the trade and the Hunterbrook report on AMD attacks China exposure rather than
   demand. If this is a positioning unwind it ends quickly; if it is a demand revision it does not,
   and the answer decides whether semis keep bleeding. The 13F and short-interest data, and the
   order-book commentary in the next round of results, would resolve it.
3. **Can the median stock stabilise while the liquid adv/dec ratio is 0.13?** Equal-weight has
   outperformed the cap-weighted index for two sessions, which on a 3,861-to-816 decliner tape is
   more a sign of the mega-caps having already fallen than of the broad market holding up. The
   question is whether the median name's -1.54% is the start of a floor. Tomorrow's breadth, and
   whether the cap-weight penalty flips positive again, would resolve it.

## Source health

| Source | Query / URL | Status | Result |
|---|---|---|---|
| Bridge `market-recap` get_quotes | 21 symbols (indices, ETFs, futures, watchlist) | ok | all 21 found |
| Bridge `market-recap` price_history | SPY, RSP, ^VIX, ^VXN, 2026-11-05 to 2026-11-19 | ok | 11 sessions each |
| Bridge `market-recap` market_snapshot | full | ok | overnight cross-asset |
| Bridge `market-recap` get_quotes | 40 symbols (sector ETFs, after-hours cross-check, tomorrow's earnings names) | ok | all found |
| TradingView scanner `america/scan` | extended-hours screen, twice, with and without the $1B cap floor | ok | 2,120 names on the contract screen; 200 rows per deliberate page |
| TradingView scanner `america/scan` | watchlist and named-mover pulls | ok | 8 and 14 rows, totalCount matched |
| cron #20 `us-eod/2026-11-19.csv` | `minimax-cloud-outputs`, contents API | ok | 4,884 rows |
| `refs/watchlist.yaml` | `minimax-cloud-outputs`, contents API | ok | 8 tickers |
| CBOE daily statistics | `https://www.cboe.com/us/options/market_statistics/daily/` | ok | selectedDate 2026-11-19, prevTradingDay 2026-11-19 |
| CBOE dated VIX close file | `https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv` | ok | 11/19/2026 close 28.44 |
| CBOE dated VXN close file | `https://cdn.cboe.com/api/global/us_indices/daily_prices/VXN_History.csv` | ok | 11/19/2026 close 36.48 |
| MCP availability probe | `probe_mcp.py` | ok | catalog_ok total=135 finance_tools=0 |
| Web (issuer releases, press, calendars) | catalyst, earnings and economic calendar research | ok | 9 searches, all returned |

**Put/call, session 2026-11-19** (CBOE, from one payload): total **1.01**, index 1.20, equity 0.62,
ETP 1.09. The page's `selectedDate` and `prevTradingDay` both read 2026-11-19, equal to the fire
date, so the ratio belongs to the session that just closed. No component split is published beyond
the four the page itself carries.

**Disclosures.**

- The **$1B market-cap floor** on the extended-hours screen hides the session's real leaderboard;
  the sub-$1B names are listed above under `## After-hours movers` so the table is not mistaken for
  the whole tape.
- **Vendor dispersion on extended hours**: Intuit was quoted at -9.77% (TradingView, ~22:35 ET),
  -9.79% (18:30 ET), -11% and -13% (evening snapshots) on different feeds. Ross was -5.16%
  (TradingView) against -5.6% and -8.6% to -9% earlier. The scanner is the source of record; the
  others are named, not blended.
- **Gold**: the ETF's after-hours print (-1.70%) does not mark the December futures' -4.34% move
  against the 3,685.50 settlement that Reuters independently confirms. The ETF's extended-hours book
  repriced lazily. Both numbers are published, each with its own source and timestamp; the futures
  are treated as the overnight signal.
- **Earnings-calendar counts differ** across vendors for 20 November (Yahoo 14, EarningsWhispers 12,
  Market Chameleon 8, Nexqual 9). The roster above is the intersection of two or more sources and
  the disagreement is disclosed rather than resolved by preference.
- **After-hours tape keeps moving.** The scanner's print is a snapshot as of the fire; by Friday's
  open these levels will have moved.
- **Kospi level not read** — the bridge does not carry the Korean index, so its change is taken from
  CNBC's live blog and its level is n/a.

## Method notes

- **Participation** is one population: cron #20's published universe for 2026-11-19, 4,884 rows,
  4,845 priced. The liquid set is names above a $2B market cap (1,769 names). The cap-weight penalty
  comes from the bridge's `price_history` for SPY and RSP and is signed: negative means the
  equal-weight index outperformed.
- **Sector rotation** is computed on one row per `cap_source_symbol`, keeping the row whose
  `data_quality` does not contain `CAP_CARRIED`. Rows flagged `EX_DISTRIBUTION` and `NO_CAP` are
  dropped from the cap-weighted columns and the denominator; the 18 rows flagged `NO_SECTOR` are
  excluded from the ranking entirely because that bucket is not a sector. Every cap-weighted sector
  return was asserted inside ±20% before publication.
- **After-hours movers** were ranked by absolute change from two runs of the same screen, capped at
  five gainers and five losers. Each row passed the internal identity check and its prior close was
  confirmed against the primary listing.
- **Volatility indices** were read from the dated `price_history` rather than the quote row and
  cross-checked against CBOE's dated close files; the two agree to the cent.
- **Futures** were checked for freshness: every row carries a 22:21 ET `as_of`, nine minutes before
  the fire, so this is a live Globex print on a Thursday night, not a stale settlement.
- **Prices** are the bridge's, which is Yahoo-sourced and the source of record. Where cron #20's
  universe file carries the same field, the difference is a settlement convention of a few basis
  points and the file's number is used in the tables that come from that file.
- This brief is read-only. It places no trades and recommends none.
