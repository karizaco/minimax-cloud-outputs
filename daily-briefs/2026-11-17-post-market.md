---
date: 2026-11-17
cron: 23-agentic-post-market-brief
contract: postmkt-artifact-v2
fire_time_et: 22:30
snapshot_et: 22:33-23:05
session: 464566780129451
scheduled_at_ms: 1794972615715
status: ok
source: MCP bridge market-recap (get_quotes, price_history); TradingView scanner (america/scan); cron #20 us-eod/2026-11-17.csv; CBOE daily statistics page; CBOE dated VIX/VXN history files; issuer IR pages and market press via web
primary_source: MCP bridge market-recap (keyless, Yahoo-sourced) for every regular-session close, the futures prints and the daily history
universe: cron #20 us-eod/2026-11-17.csv - 4,887 names (participation read and cap-weighted sectors)
degraded_sources: 3
---

# Post-market brief — Tuesday, 17 November 2026

## TL;DR

Third straight down day, and the worst S&P 500 close since late July: the S&P 500 fell **1.03% to 7,340.53**, the Dow 1.64% to 50,759.42, the Nasdaq 0.74% to 24,328.38 and the Russell 2000 1.50% to 2,701.87, with the VIX up 11.13% to 25.46. The tape was worse than the headline — advancers **1,045** against decliners **3,654**, `median_name_move_pct` **-1.25%** and `liquid_adv_dec_ratio` **0.22** — yet `cap_weight_penalty_bp` was **+43bp**, so the mega-caps actually *outperformed* the equal-weight index on the way down. Two catalysts drove the day: software was liquidated ahead of Anthropic's IPO pricing (Salesforce -9.45% on no company news), and the National Security Agency's classified-network outage report pushed the tape to its lows before the agency called it "temporary degradation during scheduled routine maintenance." The setup for tomorrow is Nvidia: it reported **after the close** — revenue $115.8bn (+103% y/y), adjusted EPS $2.68 against $2.47 expected, Q4 guided to $130bn, FY2028 growth raised to 75% — and the neocloud complex re-rated 9-11% after hours.

## Tomorrow's setup — Wednesday, 18 November 2026

### Futures and the overnight setup

Fresh Globex prints, not a stale settlement: every row carries `as_of` 2026-11-18T03:23Z — **22:23 ET**, seven minutes before the fire. The prior close is Tuesday's 16:00 settlement.

| Contract | Last | Prior settle | Change % | Session as_of (ET) |
|---|---|---|---|---|
| ES=F | 7370.75 | 7359.00 | **+0.16%** | 2026-11-17 22:23 |
| NQ=F | 27171.50 | 27075.50 | **+0.35%** | 2026-11-17 22:23 |
| YM=F | 50820 | 50815 | +0.01% | 2026-11-17 22:23 |
| RTY=F | 2709.40 | 2711.20 | -0.07% | 2026-11-17 22:23 |
| ZN=F | 105.671875 | 105.609375 | +0.06% | 2026-11-17 22:23 |

The overnight is modestly higher, not a collapse: the equity complex is pricing Nvidia's beat, and the bond complex is barely moving (10-year cash 5.10%, -1.8bp). The read is a relief bounce off a 1% down day, not a trend reversal — the cash session's breadth was the story and breadth has to come back on its own.

### Economic calendar

| Time (ET) | Release | Consensus / prior |
|---|---|---|
| 07:00 | UK CPI, October | — (overnight input) |
| 08:30 | US housing starts & building permits, October | starts 1.23m SAAR vs 1.221m prior; permits 1.380m vs 1.398m |
| 10:00 | BEA Outdoor Recreation Economic Statistics 2025; workplace injuries and illnesses | — |
| 10:30 | EIA crude oil inventories, week ending 13 Nov | — |
| 13:00 | 20-year Treasury auction | — |
| 13:35 | Fed Vice Chair for Supervision Barr speaks | — |
| 14:00 | **FOMC minutes, 27-28 October meeting** | — |
| 15:00 | Pending home sales, October; Atlanta Fed GDPNow (Q4) | -2.1% vs -7.3% prior |
| 16:00 | TIC net long-term flows, September | — |
| 19:30 | Australia labour force | 4.7% |

The 08:30 housing print lands on top of yesterday's NAHB index at 25 (lowest since April 2012, against 29 in October) and a homebuilders' read — the two together set the tone for the retail names that report before the open.

### Earnings calendar

60 companies are scheduled on Wednesday 18 November — 33 before the open, 27 after the close (Earnings Whispers). The names that matter to this tape:

| Ticker | Timing | EPS estimate | Revenue estimate |
|---|---|---|---|
| TGT | before the open | 2.08 | $26.5bn |
| TJX | before the open | 1.34 | $15.8bn |
| LOW | before the open | 2.88 | $22.4bn |
| PANW | after the close | 0.97 | $3.3bn |
| WWD | after the close | 2.54 | $1.1bn |
| SNEX | after the close | 0.88 | $1.4bn |
| KLIC | after the close | 1.43 | $376.8m |

Also before the open: GLBE, TCEHY, ZIM, BRBR, GLNG, HAFN, KRNT, PONY. After the close: HP, UGI, CPA, NJR, SBLK, BORR, CRNC, UT. Retail reports against a 25 housing index is the cleanest single test of whether the consumer is where the selloff started.

### News to watch for the top movers

- **SLS** — the $150m offering launched at 4:01pm ET is priced overnight; the follow-through is a read on how a Phase 3 win gets financed (the offering is the company's own answer to the $3.9bn it just created).
- **BILL** — the Financial Times report that TPG is nearing a take-private deal; the stock traded halted for a volatility pause before resuming, and the deal terms are the story, not the tape.
- **ACM** — FY2027 guidance of $6.15-6.35 adjusted EPS against a $5.99 consensus; the market has re-rated a 43%-drawdown name on one quarter, and the guide is now the support.
- **NXT** — the November 16 capital markets day reset fiscal 2028 margins; BMO cut fiscal 2028 EBITDA and EPS estimates by ~15% and ~16% and trimmed its target to $108.
- **CRM** — nothing company-specific; the Anthropic listing is the flow, and December 2's report is the first real test of seat-based software.

### Tomorrow's three things to watch

- NVDA — 162.95 after-hours print, 155.46 gap-fill — Q3 revenue of $115.8bn (+103% y/y) and adjusted EPS of 2.68 against 2.47 expected, with Q4 guided to $130bn and FY2028 growth lifted to 75%; the tell is whether the neocloud bid holds into the open.
- PANW — 309.29 close — reports after the close tomorrow, EPS estimate 0.97 on $3.3bn of revenue; the read is whether the software tape can hold its ground after the Anthropic listing.
- TJX — 129.85 close — reports before the open tomorrow, EPS estimate 1.34; with housing starts at 8:30 and the homebuilders index at 25, the consumer read is the tell.

## Day's tape

### Market read

One population (the cron #20 EOD universe, 4,887 names) for every row except the cap-weight penalty, which comes from the bridge's dated history.

| Metric | Value | Source |
|---|---|---|
| `advancers` | 1,045 | cron #20 `us-eod/2026-11-17.csv` |
| `decliners` | 3,654 | same |
| `unchanged` | 144 | same |
| `median_name_move_pct` | -1.25% | same (`change_pct`) |
| `cap_weight_penalty_bp` | **+43 bp** | bridge `price_history` (SPY -1.015% less RSP -1.448%) |
| `liquid_adv_dec_ratio` | 0.22 (323 : 1,439) | same CSV, names with market cap above $2bn |

The index fell 1.03% while the median name fell 1.25% and the liquid advance-decline ratio was 0.22 — three decliners for every advancer among names above $2bn. Yet the equal-weight index fell harder than the cap-weighted one (RSP -1.45% against SPY -1.01%), so the +43bp cap-weight penalty means the *megacaps held up better than the median stock* even on a down day. That is the opposite of the narrow, mega-cap-led tape: leadership sat in the largest names, and the damage was spread across everything below them.

### Cap-weight penalty — 5-day history

| Session | SPY % | RSP % | cap_weight_penalty_bp |
|---|---|---|---|
| 2026-11-11 | +1.32 | +0.80 | +52 |
| 2026-11-12 | -0.35 | -0.87 | +51 |
| 2026-11-13 | -0.36 | +0.20 | -56 |
| 2026-11-16 | -1.91 | -1.01 | -90 |
| 2026-11-17 | -1.02 | -1.45 | **+43** |

Three of the last five sessions carried a positive penalty, and the sign flipped twice inside the window. The penalty is not a regime — it is noise around a tape that has been falling in breadth for a week (the S&P is down 2.9% on the week and the Nasdaq 3.2%).

### Index, ETF and volatility levels

Every row below carries `as_of` 2026-11-17 from the bridge; no row is a prior session's reading.

| Index / ETF | Close | Change % | Day range | as_of (ET) |
|---|---|---|---|---|
| S&P 500 | 7340.53 | -1.03% | 7288.34 - 7415.37 | 16:42 |
| Nasdaq Composite | 24328.38 | -0.74% | 23989.09 - 24547.66 | 17:16 |
| Dow Jones Industrial Average | 50759.42 | -1.64% | 50566.98 - 51463.53 | 16:42 |
| Russell 2000 | 2701.87 | -1.50% | 2696.26 - 2741.11 | 16:30 |
| Nasdaq-100 | 27001.79 | -0.72% | 26580.86 - 27258.84 | 17:16 |
| PHLX Semiconductor | 9642.88 | +0.34% | 9295.02 - 9745.95 | 17:16 |
| VIX | 25.46 | +11.13% | 22.36 - 27.73 | 16:15 |
| VXN | 34.44 | +4.68% | 31.80 - 36.98 | 16:15 |
| SPY | 732.44 | -1.01% | 727.00 - 739.76 | 16:00 |
| QQQ | 656.95 | -0.73% | 646.65 - 663.36 | 16:00 |
| IWM | 269.05 | -1.43% | 267.87 - 273.04 | 16:00 |
| DIA | 507.31 | -1.62% | 505.32 - 514.27 | 16:00 |
| RSP | 215.76 | -1.45% | 215.33 - 219.13 | 16:00 |
| SMH | 460.10 | -0.39% | 445.32 - 466.43 | 16:00 |
| GLD | 352.48 | -0.13% | 352.01 - 356.53 | 16:00 |
| TLT | 79.55 | +0.21% | 79.24 - 79.77 | 16:00 |

The two volatility indices are read from the bridge's **dated history**, not from the quote row, and are cross-checked against Cboe's own dated close files: VXN 11/17/2026 close 34.44 (high 36.98, low 31.80) and VIX close 25.46 (high 27.73, low 22.36) — the two sources agree to the cent.

**Put/call.** Cboe's daily statistics page, session `selectedDate` 2026-11-17 (`prevTradingDay` 2026-11-17): total **0.98**, index 0.98, equity 0.71, ETP 1.26, SPX 1.28; total volume 17,423,391 (8,818,350 calls / 8,605,041 puts). All four splits come from the same payload and reconcile with the total; no component is estimated.

### Cross-asset

- 10-year Treasury 5.10%, down 1.8bp; 2-year 4.81%, down 1.7bp. Yields eased on the flight to safety and then recovered.
- Brent crude $93.14, +0.8%, on the Iran conflict.
- Gold ETF GLD -0.13%, 20-year bond ETF TLT +0.21% — no flight into either.
- Europe and Asia fell with Wall Street; the Kospi closed -2.6%, its lowest since February.

### Day's movers

Names with market cap above $2bn, priced from the bridge (the source of record for closes).

| Ticker | Close | Change % | Catalyst |
|---|---|---|---|
| SLS | 19.15 | **+156.36%** | Phase 3 REGAL met its primary endpoint — hazard ratio 0.59, p=0.035, median survival 24.0 vs 14.7 months; a $150m offering was launched at 4:01pm ET |
| BILL | 64.88 | +12.58% | the Financial Times reported TPG nearing a take-private deal; trading was halted for a volatility pause before resuming |
| ACM | 80.53 | +11.08% | record Q4 adjusted margin of 18.2%, adjusted EPS $1.63, FY2027 EPS guided to $6.15-6.35 against a $5.99 consensus, dividend +10% |
| RYTM | 116.61 | +8.49% | — |
| SNAP | 5.50 | +8.06% | — |
| UNFI | 51.99 | +7.44% | — |
| LUMN | 4.30 | +6.70% | — |
| TME | 9.47 | +6.64% | — |
| NXT | 78.48 | **-12.13%** | November 16 capital markets day guided fiscal 2028 margins lower; BMO cut fiscal 2028 EBITDA and EPS estimates ~15% and ~16% and cut its target to $108 |
| IEP | 3.19 | -11.39% | — |
| IDYA | 27.40 | -9.75% | — |
| SMMT | 10.67 | -9.73% | — |
| CRM | 194.52 | -9.45% | no company news; seat-based software sold ahead of Anthropic's IPO pricing, with HubSpot -7% and Workday -5% alongside |
| FRHC | 145.82 | -8.60% | — |
| TNGX | 22.11 | -8.52% | — |
| RH | 115.60 | -8.37% | — |

Also down on the day and worth naming: NKE -6.30% to 35.85, UNH -5.42% to 389.68, HD -2.45% to 339.01 (a profit beat that the housing market swamped), DIS -1.48% to 116.94, JPM -2.48%, V -2.27%, MA -2.48%, WMT +0.12%, XOM +0.12%.

### Watchlist EOD review

| Ticker | Close | Day % | Day range | Volume | Rel. vol | After-hours print |
|---|---|---|---|---|---|---|
| AAPL | 351.91 | -0.25% | 349.67 - 355.36 | 34,138,497 | 0.76x | 350.22 (-0.48%), 8,020,969 shares |
| MSFT | 506.24 | -2.27% | 496.51 - 515.64 | 24,219,063 | 0.98x | 510.53 (+0.85%), 4,459,389 shares |
| NVDA | 155.46 | -0.44% | 150.33 - 158.19 | 329,686,568 | 1.83x | **162.95 (+4.82%)**, 69,723,879 shares |
| GOOGL | 280.20 | -1.24% | 278.46 - 284.09 | 29,240,950 | 0.83x | 283.67 (+1.24%), 6,212,635 shares |
| AMZN | 257.89 | +0.05% | 254.00 - 259.90 | 34,704,890 | 0.77x | 260.20 (+0.90%), 6,309,794 shares |
| IWM | 269.05 | -1.43% | 267.87 - 273.04 | 28,399,284 | n/a | 270.15 (+0.41%), 1,201,775 shares |
| GLD | 352.48 | -0.13% | 352.01 - 356.53 | 7,817,964 | n/a | 349.64 (-0.81%), 266,358 shares |
| TLT | 79.55 | +0.21% | 79.24 - 79.77 | 34,650,277 | n/a | 79.53 (-0.02%), 2,709,150 shares |

Volume and relative volume come from cron #20's settled EOD file; the three ETFs are not in that file, so their volume comes from the bridge and their relative volume is published as n/a rather than estimated. Microsoft was the watchlist's worst day at -2.27% and is the one to note — it fell with the software complex and then recovered 0.85% after hours. Nvidia's regular-session volume ran 1.83x its normal and the after-hours tape did 69.7m shares.

## Sector rotation

Cap-weighted and median sector returns from the cron #20 universe, cross-checked against the sector ETF. Cap-weighted returns are computed on one row per `cap_source_symbol` (the primary listing is kept and the `CAP_CARRIED` carrier row is dropped).

| Sector | Cap-weighted % | Median % | ETF | ETF % | Gap (pp) | Names priced |
|---|---|---|---|---|---|---|
| Industrials | **+0.09** | -1.42 | XLI | -0.55 | **+0.64** | 545 |
| Consumer Discretionary | -0.60 | -1.48 | XLY | -0.89 | +0.29 | 386 |
| Energy | -0.64 | -1.34 | XLE | -0.52 | -0.12 | 176 |
| Real Estate | -1.39 | -1.28 | XLRE | -1.49 | +0.10 | 180 |
| Utilities | -1.56 | -1.54 | XLU | -1.59 | +0.03 | 82 |
| Financials | -1.84 | -1.09 | XLF | -1.91 | +0.07 | 1,192 |

Every sector fell, and the only positive cap-weighted reading — Industrials at +0.09% — is a constituent effect, not a rotation: **SpaceX (SPCX, $1.87tn cap, +3.16%) contributed +0.669pp of it.** Ex-SPCX, Industrials is **-0.74%**, which puts the sector fourth from the bottom rather than at the top. The reader should treat Industrials as a -0.74% sector with a $1.87tn satellite, and the cap-weighted column inherits that concentration.

Financials led the decliners (XLF -1.91%) on bank and card concerns around a broad pullback in AI spending — JPMorgan -2.48%, Visa -2.27%, Mastercard -2.48%. Health Care was the weakest by median (-1.42%) with UnitedHealth -5.42% and Humana -3.88% leading a managed-care de-rating.

**Coverage note.** Excluded from the cap-weighted columns and their denominator: 172 `EX_DISTRIBUTION` rows, 59 `NO_CAP` rows, 27 `CAP_CARRIED` carrier rows, and 335 `NO_SECTOR` rows (a bucket, not a sector — including it would displace Utilities from the bottom three). All six published cap-weighted returns are inside ±20%; that range check is what catches a doubled parent cap (with Berkshire counted twice, Financials printed +28.2% instead of -1.84% on a comparable day).

## After-hours movers

TradingView scanner, `postmarket_*` columns, pulled twice — descending and ascending on `postmarket_change` — and ranked by absolute change. Every row below passed the identity check `postmarket_change == (postmarket_close - close) / close x 100`, and every row is a major-US-exchange venue (no over-the-counter lines).

| ticker | prior_close | ah_last | ah_high | ah_low | ah_volume | gap_pct | ah_range_pct | gap_fill_level |
|---|---|---|---|---|---|---|---|---|
| NBIS | 106.035 | 117.99 | 119.50 | 106.00 | 5,408,939 | +11.27 | 12.73 | 106.04 |
| WULF | 11.67 | 12.88 | 12.93 | 11.6512 | 2,968,501 | +10.37 | 10.96 | 11.67 |
| IREN | 15.805 | 17.4082 | 17.8093 | 15.74 | 13,767,464 | +10.14 | 13.09 | 15.81 |
| VSH | 25.35 | 27.9111 | 27.9111 | 25.35 | 371,240 | +10.10 | 10.10 | 25.35 |
| APLD | 14.22 | 15.65 | 15.98 | 14.1384 | 2,358,059 | +10.06 | 12.95 | 14.22 |
| ARDT | 17.75 | 15.157 | 17.75 | 14.86 | 122,109 | -14.61 | 16.28 | 17.75 |
| SLS | 19.15 | 17.14 | 19.2097 | 15.31 | 5,776,993 | -10.50 | 20.36 | 19.15 |
| AAOI | 45.22 | 41.30 | 45.80 | 39.25 | 4,090,387 | -8.67 | 14.48 | 45.22 |
| ALHC | 7.62 | 7.2353 | 7.62 | 7.2353 | 893,554 | -5.05 | 5.05 | 7.62 |
| AVAH | 11.65 | 11.1703 | 11.65 | 11.1703 | 667,638 | -4.12 | 4.12 | 11.65 |

`gap_fill_level` is the prior close for every row: each of these names traded back through its 16:00 close during the extended session, so the gap fills at the prior close. The two biggest after-hours ranges belong to the two financing stories — SLS at 20.36% (a $150m offering priced into a 156% day) and NBIS at 12.73%.

**Why the neocloud complex moved.** Nvidia's post-close commentary on backstopping neocloud data centres, plus the FY2028 growth upgrade, re-rated the borrowed-capital AI names in one move: NBIS +11.27%, WULF +10.37%, IREN +10.14%, APLD +10.06%. These are the same names CNBC flagged during the session as the ones with the most to lose if Nvidia pulled back its financing of the AI ecosystem; the same report, read the other way, is what they rallied on.

**What this table is not.** The screen keeps names above $1bn of market cap, so the session's actual after-hours leaders sit below it: **AZI +68.48%** (0.7301 to 1.2301), **ABTS +45.79%** (0.3186 to 0.4645) and **CRIS +31.37%** (0.5418 to 0.7117) in a no-floor pull of the same screen. The table above is the contract's screen, not the whole after-hours tape. One row on each side of the ranking was dropped as a single print (identical high and low).

## After-hours earnings reactions

**NVDA — reported after the close, and it is the setup.** Fiscal Q3 2027 (quarter ended 25 October 2026): revenue **$115.8bn**, up 103% y/y and 20% q/q; adjusted EPS **$2.68** against $2.47 expected; adjusted gross margin 74.9%; Data Center revenue $107.6bn (+110% y/y) against $101.9bn expected; hyperscale revenue $60.1bn against $54.1bn expected. Q4 guidance is $130bn plus or minus 3% (consensus about $125bn), with no China Data Center compute revenue assumed and adjusted gross margin of 71-72%; FY2028 revenue growth was raised to about 75% from 70%, and a $150bn buyback was announced. It is the first report since Jensen Huang's exit on 12 November, led by interim CEO Colette Kress — and board chair Harvey Jones said on the call that the company does not plan to reinstate Huang. The after-hours print is **162.95, +4.82%** on 69.7m shares.

**No other watchlist name reported after the close.** Of AAPL, MSFT, NVDA, GOOGL and AMZN, only Nvidia reported.

**The other two after-hours headlines are financings, not earnings**, and both hit at 16:01 ET:

- **ARDT** — a proposed secondary offering of 7,000,000 shares (6,244,629 by an Equity Group Investments affiliate and 755,371 by a Ventas affiliate) with a 1,050,000-share underwriter option, alongside a concurrent repurchase of up to 1,500,000 shares from the underwriters funded from cash on hand. The company sells nothing and receives no proceeds. Print: **15.157, -14.61%**.
- **SLS** — a $150m stock offering launched at 4:01pm ET into the +156% session. Print: **17.14, -10.50%**, on a 20.36% after-hours range.

**Vendor divergence on the two prints that matter.** The scanner print is the source of record for this brief. Nvidia was +4.82% here, +3.66% (Yahoo, 20:30 ET), +2.7% (Investing.com) and +1.86% (CNBC, 16:41 ET); SLS was -10.50% here, -13.3% (Rallies.ai at $16.61) and -10% (Investing.com). The numbers are not blended.

**The sector-level catalyst** was Anthropic: its IPO was expected to price Wednesday, with a concurrent private placement filed on Tuesday, and the read-through was taken out of seat-priced software.

## Open research queue

1. **Is the neocloud bid a re-rating or relief?** NBIS, IREN, WULF, APLD and CRWV jumped 9-11% after hours on Nvidia's comments about backstopping neocloud data centres. Why it matters: the neocloud thesis depends on continued Nvidia financing of an AI ecosystem whose largest customer just lost its CEO, and a relief bounce on one earnings print is not the same as a durable funding regime. What would resolve it: Nvidia's own disclosure of the size and terms of the backstop, and each neocloud's next financing spread and covenant disclosure.
2. **Does Anthropic's listing permanently derate seat-based software?** Salesforce's -9.45% had no company news attached and was attributed to funds making room for an IPO that may raise up to about $64bn. Why it matters: if it is flow, the derating reverses when the deal settles; if it is a repricing of seat-based models against AI agents, it is a multi-year earnings reset that started on 18 November. What would resolve it: software's behaviour in the sessions after the pricing, and Salesforce's 2 December report — organic growth above the second quarter's 6% would be the push-back.
3. **What does a $150m raise into a +156% print tell us about biotech repricing?** SELLAS launched an offering hours after a 126-patient Phase 3 met its primary endpoint (hazard ratio 0.59, p=0.035, median survival 24.0 against 14.7 months, and no confidence interval published). Why it matters: the raise is the market's first live pricing of the data, and an estimated confidence interval reaching close to 0.96 would make the $3.9bn close hard to defend. What would resolve it: the offering's final pricing, the full REGAL data at a medical meeting, and the outcome of the planned FDA meeting.

## Source health

| Source | Query / URL | Status |
|---|---|---|
| Bridge `market-recap get_quotes` (16 index and ETF symbols) | MCP-over-HTTP bridge, `market-recap` pack | ok — retrieved 2026-11-18T03:33Z, all rows `as_of` 2026-11-17 |
| Bridge `market-recap get_quotes` (futures) | same | ok — `as_of` 2026-11-18T03:23Z (22:23 ET), live Globex, not a stale settlement |
| Bridge `market-recap get_quotes` (watchlist and movers) | same | ok |
| Bridge `market-recap price_history` (SPY, RSP, ^VIX, ^VXN) | 2026-11-03 to 2026-11-17 | ok — dated rows for the fire date |
| TradingView scanner (after-hours, two directions) | `POST https://scanner.tradingview.com/america/scan`, 200-row page each way | ok — 2,108 names match the screen; the page is deliberate, one single-print row dropped each side |
| TradingView scanner (no market-cap floor) | same, 150-row page | ok — 3,412 names; used only to publish the leaders below the floor |
| TradingView scanner (`pull --names`, 8 watchlist names) | one targeted call | ok — totalCount 8, all 8 returned |
| cron #20 EOD universe | `karizaco/minimax-cloud-outputs` `us-eod/2026-11-17.csv` | ok — 4,887 rows, all `settle_status=CONFIRMED` on the priced rows |
| Watchlist | `refs/watchlist.yaml` (contents API) | ok — 8 names |
| CBOE daily statistics | `cboe.com/us/options/market_statistics/daily/` | ok — `selectedDate` 2026-11-17; the summary extraction returned a null date and the raw page supplied it |
| CBOE dated index history | `cdn.cboe.com/.../VXN_History.csv`, `VIX_History.csv` | ok — agree with the bridge to the cent |
| MCP availability probe | `probe_mcp.py` | ok — `catalog_ok total=135 finance_tools=0`, `bridge_ok packs=tradier,fmp,market-recap` |
| Catalysts, calendars, issuer IR | issuer IR pages, exchange filings, market press | ok |

**degraded_sources: 3**

1. **After-hours screen coverage.** The published table is a 200-row page at each end of a 2,108-name screen, and the screen itself keeps names above $1bn of market cap. The session's real after-hours leaders are below that floor (AZI +68.48%, ABTS +45.79%, CRIS +31.37%), so the table must not be read as the whole tape.
2. **The after-hours print is one snapshot.** It was taken at about 22:40 ET, and vendors materially disagree on the two prints that carry the night: NVDA +4.82% here against +3.66% (Yahoo), +2.7% (Investing.com) and +1.86% (CNBC, 16:41 ET); SLS -10.50% here against -13.3% (Rallies.ai) and -10% (Investing.com). The scanner print is published as the record and the others are named rather than blended.
3. **Two published rows have no sourced company-specific catalyst.** AAOI (-8.67%) and ALHC (-5.05%, Alignment Healthcare) are published as tape — levels, volume and range — with no company news I could source for the move.

## Method notes

- **One number per field, one source per field.** Regular-session closes, futures and daily history come from the bridge `market-recap` (keyless, Yahoo-sourced, the quote source of record). The participation read and the cap-weighted sector columns come from cron #20's EOD CSV, because they need the whole universe. The two disagree slightly on `change_pct` for a few names because the CSV's prior close differs — SNAP 8.06% (bridge) vs 7.85% (CSV), TME 6.64% vs 6.99%, WSO 0.08% vs 0.14% — and the bridge's number is published for every named mover. The two are never blended.
- **Sector method.** Cap-weighted returns are computed on one row per `cap_source_symbol`, with `EX_DISTRIBUTION`, `NO_CAP`, `CAP_CARRIED` and `NO_SECTOR` rows excluded from both the numerator and the denominator; a duplicate check found no `cap_source_symbol` carrying two weighted rows. Every published cap-weighted return was asserted inside ±20%. The unweighted median column uses the same prices.
- **Volatility.** ^VIX and ^VXN were read from the bridge's dated history, not from the quote row, and cross-checked against Cboe's dated close files.
- **Futures.** Every futures row carries a live `as_of` at 22:23 ET, so the overnight move is in the data — this is not a settlement reprint. The prior close is Tuesday's 16:00 settlement.
- **Put/call.** Published as sourced, with its session date, and the splits are from the same Cboe payload. No component is estimated.
- **After-hours rows.** Every published row passed the identity check on its own numbers, and venue was checked separately: the identity test cannot detect a stale prior close, so over-the-counter venues were excluded and the surviving prints are all NASDAQ or NYSE listings.
- **Windows-safe paths, no `mcp__*` calls, read-only.** The finance MCP servers were reached over the HTTP bridge; no `mcp__*` tool is registered in this runtime and none was called. No browser automation. Nothing here is a trade recommendation.
