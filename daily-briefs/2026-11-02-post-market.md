---
date: 2026-11-02
cron: 23-agentic-post-market-brief
fire_time_et: 22:30
snapshot_et: 22:35
session: 459259165593795
scheduled_at_ms: 1793676600000
status: ok
source: MCP bridge market-recap (quotes/movers) + TradingView public scanner (sector/breadth/extended hours) + web (catalysts, calendars, put/call)
primary_source: bridge market-recap for prices | TradingView scanner for breadth/sector/after-hours | Investing.com + Marvell 8-K + company IR for catalysts
universe: S&P 500 (500 of 503 Wikipedia symbols matched the scanner) + 2,121 US names >= $2B mcap + 3,563 names >= $300M mcap for after-hours
---

# Post-market brief — Monday, 2026-11-02 (ET)

## TL;DR

The index level was the least interesting thing about today. The S&P 500 closed down 0.51% and the
Nasdaq Composite down 1.07%, but **breadth was decisively positive: 344 of the 500 S&P 500 names we
matched closed higher**. What actually happened was a violent, company-specific unwinding of the AI
infrastructure complex — Lumentum -18.6%, Marvell -12.7%, Ciena -11.3%, Intel -8.8%, Oracle -8.8%,
Datadog -8.2% — against a broad rotation into consumer, transport, materials and housing. Two
things drove it: Marvell's all-stock $115B acquisition of Lumentum (which the market refused to
accept as a currency) and a fresh wave of AI-financing anxiety from Oracle's $20B raise and
Anthropic's disclosed compute commitments. Oil, not tech, was the day's other story: WTI fell ~7.6%
on renewed US-Iran diplomatic signals, dragging XLE -3.96% and XOP -5.01%.

**The caveat that changes how to read this:** a positive breadth print alongside a falling index is
not a healthy tape. It is a **narrow, high-weight de-risking** — the mega-cap AI names that carry
the index fell hard while the median stock rose. Volume confirms it: the Nasdaq Composite traded
8.00B shares. The equal-weight S&P 500 outperformed in October for the first time since March 2009,
and Monday was the first instalment of that rotation, not a broad risk-on session.

## Day's tape

Settled closes, 2026-11-02 (source: bridge `market-recap` → `get_quotes`, Yahoo-sourced).

| Index | Close | Change |
|---|---|---|
| S&P 500 (^GSPC) | 7,541.40 | **-0.51%** |
| Nasdaq Composite (^IXIC) | 25,164.36 | **-1.07%** |
| Dow Jones (^DJI) | 51,983.98 | **+0.41%** |
| Russell 2000 (^RUT) | 2,805.88 | -0.21% |
| VIX | 21.15 | **+8.91%** |
| VXN | 30.89 | **+8.39%** |
| US 10Y (^TNX) | 4.894% | -3.5 bp (from 4.929%) |
| DXY | 101.83 | +0.08% |
| Bitcoin | 76,679.30 | -0.01% |

Exchange volume: ^GSPC 3.56B shares, ^IXIC 8.00B, ^DJI 522M. A published market wrap puts total
US session volume at 18.8B shares vs a 20-day average of 17.3B — i.e. the down-move came on
elevated volume, not a thin drift.

### ETF proxies

| Proxy | Close | Change | Proxy | Close | Change |
|---|---|---|---|---|---|
| SPY | 752.10 | -0.48% | GLD | 361.65 | **+1.65%** |
| QQQ | 681.09 | -1.36% | TLT | 81.73 | +0.29% |
| IWM | 279.14 | -0.07% | HYG | 76.89 | -0.18% |
| DIA | 519.34 | +0.43% | LQD | 103.71 | -0.15% |
| SOXX | 453.65 | **-3.79%** | USO | 156.87 | **-7.08%** |
| SMH | 508.31 | -2.71% | XOP | 193.56 | -5.01% |
| XBI | 152.05 | -2.52% | OIH | 389.03 | -5.48% |
| IGV | 101.90 | -2.29% | UNG | 9.00 | -0.88% |

Note the dispersion: SPY -0.48% against SOXX -3.79%, and credit essentially flat (HYG -0.18%,
LQD -0.15%) while long Treasuries bid (TLT +0.29%). **Rates rallied, credit did not break** — this
was an equity de-risking inside a stable macro backdrop, not a risk-off event.

### The intraday shape

Early gains in technology and AI faded into the close. SPY traded 763.86 high / 751.60 low — a 1.6%
range — and closed at 752.10, within 10 cents of the session low. QQQ's range was wider still
(699.43 / 680.33). That is a distribution day in the index, executed on the mega-cap complex while
the median stock closed green.

## Sector rotation

Top 3 / bottom 3 only. Sector aggregates are **cap-weighted averages computed across 2,121 US
names with market cap ≥ $2B** (TradingView scanner; median shown for reference), cross-checked
against SPDR sector ETFs from the bridge.

| Rank | Sector (TV classification) | Cap-wtd | Median | n | Cross-check ETF |
|---|---|---|---|---|---|
| 1 | Consumer Services | +2.46% | +2.11% | 89 | XLY +2.41%, XLP +1.58% |
| 2 | Retail Trade | +2.45% | +2.40% | 71 | XHB +3.58%, ITB-adjacent strength |
| 3 | Non-Energy Minerals | +2.05% | +1.77% | 68 | XLB +1.76% |
| … | | | | | |
| 19 | Industrial Services | -1.51% | -2.03% | 75 | ITA +2.36% (defence sub-theme diverges) |
| 20 | Electronic Technology | -2.11% | -1.22% | 160 | XLK -2.95%, SMH -2.71% |
| 21 | **Energy Minerals** | **-4.01%** | -4.59% | 51 | XLE -3.96%, XOP -5.01% |

Three observations:

1. **Energy was the day's clear loser, and it was macro, not fundamental.** The sell-off traces to
   renewed US-Iran diplomatic signals; a published close had WTI settling around $96.26, down ~7.6%
   on the session. With the live quote now at $96.66 (+0.2% vs the futures' prior settle), oil has
   given back a sliver overnight but the risk premium is largely gone.
2. **Electronic Technology is where the damage concentrated** — 160 names, cap-weighted -2.11% but
   a -1.22% median, i.e. the *large* names did worse than the average one. That is the signature of
   a mega-cap de-rating, not a sector-wide demand downgrade.
3. **Housing was the best-kept sector ETF of the day** at +3.58%, and Consumer Durables carried a
   +4.28% median — consumer-facing sectors bid while the AI complex was sold. That is a rotation,
   not a de-risking.

## Universe EOD review

**Note on the watchlist:** `research/watchlist.yaml` does not exist in this Cloud runtime (the repo
paths `research/watchlist.yaml` and `cloud-prompts/research/watchlist.yaml` both 404), so — per the
skill's Cloud adaptation — there is **no watchlist section in this brief**. The universe below is the
**S&P 500**, used as the routine's deployed universe and labelled as such, not as a personal watchlist.

### Breadth

| Universe | Names | Advance | Decline | Unchanged |
|---|---|---|---|---|
| S&P 500 (matched) | 500 | **344** | 156 | 0 |
| US ≥ $2B mcap | 2,121 | **1,327** | 775 | 19 |

500 of the 503 Wikipedia S&P 500 symbols matched the scanner; `BRK-B`, `BF-B` and `KVUE` did not
(TradingView lists the Berkshire/Brown-Forman class-B lines under a different symbol form).

### Top movers — S&P 500

| Ticker | Close | Change | Notes |
|---|---|---|---|
| IDXX | 671.64 | **+21.85%** | Q3 beat + guidance raise (see below) |
| HWM | 212.99 | +6.91% | Electronic Technology — rallied *against* the sector |
| PNR | 70.56 | +6.49% | rvol 1.39 |
| CRH | 96.59 | +6.36% | rvol 2.11 — Non-Energy Minerals bid |
| DASH | 190.07 | +6.19% | Consumer/transport bid |
| CBRE | 136.75 | +6.13% | Finance +1.86% |
| SHW | 352.37 | +5.94% | Process Industries +1.36% |
| ARE | 42.57 | +5.90% | Real estate (XLRE +1.09%) |
| TDG | 1,213.62 | +5.83% | rvol 1.30 |
| BSX | 44.32 | +5.57% | Health Technology held up despite the sector's -0.24% |

### Bottom movers — S&P 500

| Ticker | Close | Change | rvol | Notes |
|---|---|---|---|---|
| LITE | 684.40 | **-18.59%** | 2.77 | Worst S&P 500 performer of the day |
| MRVL | 171.41 | **-12.72%** | 2.81 | Worst 3-day stretch since Oct 2000 |
| CIEN | 284.34 | -11.34% | 1.55 | Optical — sympathy with the deal |
| P | 113.78 | -10.40% | 1.41 | |
| INTC | 59.97 | -8.80% | 1.74 | Second leg after Friday's ~30% collapse |
| ORCL | 119.22 | -8.76% | 1.71 | $10B equity + $10B debt raise |
| DDOG | 216.10 | -8.15% | 1.47 | |
| STX | 593.76 | -7.88% | 0.92 | |
| SMCI | 30.44 | -7.62% | 1.09 | |
| APA | 48.82 | -7.57% | 1.30 | Energy Minerals |
| AMD | 466.84 | -7.52% | 1.53 | Reports tomorrow after the close |
| WDC | 338.59 | -7.52% | 0.78 | |

### Large movers outside the S&P 500 (≥ $2B mcap)

| Ticker | Close | Change | Notes |
|---|---|---|---|
| NWL | 5.96 | +15.06% | Q3 sales beat + FY sales guide raised to 2-3% (from 1-2%) |
| NXT | 91.13 | +14.87% | Named Jefferies' franchise pick |
| PHIN | 70.79 | +12.51% | Then **+4.44% more after the close** ($73.93) |
| SFM | 55.23 | +11.13% | Consumer staples strength |
| SAM | 221.37 | +9.96% | |
| LBRT | 14.68 | -13.03% | Oil services |
| VG | 12.87 | -12.98% | LNG — same oil complex |

## After-hours movers

Extended-hours prints from the TradingView scanner across 3,563 US names with market cap ≥ $300M.
**26 names are up ≥5% and 9 are down ≥5%.** Capped at 10 names shown (5 each side), as the skill
requires. "% of ADV" is after-hours volume ÷ average daily volume 30d — a ±20% gap on a handful of
shares is a quote, not a market.

| Ticker | Close | Day | After-hours | After-hours px | % of ADV | Mkt cap |
|---|---|---|---|---|---|---|
| BLZE | 7.40 | -2.50% | **+38.78%** | 10.27 | 77% | $0.46B |
| BRAI | 2.50 | +2.04% | +19.00% | 2.975 | 42% | $0.52B |
| HLIT | 10.19 | -0.39% | +17.27% | 11.95 | 42% | $1.11B |
| AEHR | 51.47 | -6.23% | +13.99% | 58.67 | 35% | $1.68B |
| IBTA | 50.07 | +2.98% | +13.06% | 56.61 | 38% | $1.16B |
| ADEA | 20.67 | -3.59% | **-23.51%** | 15.81 | 43% | $2.28B |
| BVS | 13.15 | -1.31% | -21.29% | 10.35 | 28% | $1.11B |
| EBS | 6.44 | -5.43% | -17.36% | 5.3217 | 20% | $0.33B |
| ALG | 152.73 | +3.36% | -14.88% | 130.00 | 20% | $1.86B |
| CWH | 5.35 | +7.00% | -12.15% | 4.70 | 14% | $0.55B |

Just outside the ±5% cut: LIFE +11.27% ($47.42), FN +10.42% ($347.50), UPWK +10.19% ($10.71),
AEIS +9.74% ($238.35), **LSCC +8.93% ($103.96, 47% of ADV)**, PHIN +4.44%, BRCC -14.60%,
PROK -6.64%, ALEC -6.05%, **BMRN -5.12% ($54.50)**.

Cross-check: an independent after-hours tape (Marketchameleon, 6:33 PM ET) listed BLZE +37.8%,
HLIT +16.6%, AEHR +15.1%, IBTA +13.0%, LIFE +11.8% as the top gainers and VCIG -22.9%,
ADEA -22.6%, EBS -20.5% as the top decliners — consistent with the scanner's ranking and prints.

### S&P 500 after-hours tone

**385 of 500 names printed higher after the close; 115 lower.** The index-level posture is mildly
constructive despite the cash-session drawdown. Largest movers:

- **Higher:** RVTY +4.07% ($157.77), BE +3.46% ($203.05), CLX +2.30% ($91.97), TWLO +1.71%, AXON +1.70%
- **Lower:** J -3.09% ($155.29), **PLTR -2.99% ($173.00)**, **AAPL -2.81% ($328.81)**, FE -2.70%, A -2.31%

The largest *gainers* were mostly the day's beaten-down AI names marking a small bounce:
MRVL +1.13%, AMD +1.11%, SMCI +1.36%, DDOG +1.34%, INTC +1.02%, CIEN +1.04%, SNDK +1.48%.
Momentum is buying the dip in exactly the names that fell hardest.

## After-hours earnings reactions

### Reported Monday (AMC)

**AAPL — close 338.32 (-1.83%), after-hours -2.81% to $328.81.**
FQ4 beat: EPS $2.10 vs $1.99 est; revenue $114.48B vs $113.38B est. iPhone revenue +17.5% y/y
(fourth consecutive quarter of double-digit iPhone growth), but **Services growth slowed to +9.8%
from 12.1%**. The stock is lower after hours on a weak gross-margin forecast (CNBC, via StockTitan).
Afternoon options implied a ~4.3% move — the -2.81% print is inside that band.

**PLTR — close 178.34 (-3.13%), after-hours -2.99% to $173.00.**
Q3 revenue +96% to $2.313B; adj. EPS $0.44 vs $0.41 est; FY revenue guidance raised to
$8.530-8.534B. US commercial revenue ($984M) passed US government revenue ($953M) for the first time.
A clean beat, and the stock is still down after hours. Note a published wrap described PLTR as
"slightly higher after hours" — the scanner's -2.99% is consistent with the other two sources that
described both AAPL and PLTR as lower, so the scanner print is the one used here.

**FN (Fabrinet) — close 314.70 (-3.85%), after-hours +10.42% to $347.50.**
Record fiscal Q1 revenue $1.47B, +51%; Q2 revenue guidance $1.60-1.65B. Implied move was ±21.4%.

**AEHR (Aehr Test Systems) — close 51.47 (-6.23%), after-hours +13.99% to $58.67.**
Record fiscal Q1 revenue $33.0M, +200%; full-year revenue outlook raised to $150M.

**BLZE (Backblaze) — close 7.40 (-2.50%), after-hours +38.78% to $10.27.**
Q3 revenue $46.7M, +26%. Biggest after-hours gainer of the session.

**LSCC (Lattice) — close 95.44 (+2.66%), after-hours +8.93% to $103.96.**
Beat on Q3 revenue and raised the full-year forecast; the print was reported at "+7%" by CNBC at an
earlier capture, and the scanner's later 8.93% reflects the moving tape.

**BMRN (BioMarin) — close 57.44 (-1.83%), after-hours -5.12% to $54.50.**

Also of note: **PHIN (Phinia)** closed +12.51% and added **+4.44% after the close** to $73.93 on
light volume (25% of ADV) — the weakest conviction of the top after-hours movers.

### Reported earlier this week (the day's cash-session drivers)

**IDXX — close 671.64, +21.85%. The day's single best S&P 500 name.**
Q3 revenue $1,214M, +10% as reported and organic; CAG Diagnostics recurring revenue +11%; EPS $4.01,
+18% reported / +22% comparable; 1,904 inVue Dx analyzers placed (installed base ~11,000).
**FY guidance raised**: revenue to $4,741-4,767M (reported growth 10.1-10.8%) and EPS to
$14.96-15.16 (+$0.25 at midpoint) — **but** full-year reported operating margin guidance was *lowered*
to 32.1-32.3%. Growth and earnings up, margin down.

**NWL (Newell Brands) — close 5.96, +15.06%.**
Q3 net sales $1.873B, +3.7% (core +3.3%, volume-driven, not price); normalized EPS $0.20 vs $0.17.
FY sales growth guidance raised to 2-3% from 1-2%; normalized EPS held at $0.74-0.76. GAAP net loss
of $81M on a $101M non-cash goodwill/intangible impairment.

**NXT (Nextracker) — close 91.13, +14.87%** after being named Jefferies' franchise pick, even with
revenue headwinds flagged.

## Tomorrow's setup — Tuesday, 2026-11-03

### Overnight futures (22:22 ET, bridge `market-recap`)

| Contract | Last | Change |
|---|---|---|
| ES=F (S&P 500) | 7,574.75 | 0.00% |
| NQ=F (Nasdaq 100) | 28,238.75 | **+0.40%** |
| YM=F (Dow) | 51,964 | -0.32% |
| RTY=F (Russell 2000) | 2,816.90 | -0.03% |
| CL=F (WTI) | 96.66 | +0.21% |
| GC=F (Gold) | 3,947.80 | -0.55% |
| SI=F (Silver) | 50.005 | -1.74% |

Asia is already trading (the session opens ~18:00 ET Sunday-Thursday): Nikkei 225 63,081.86 (-0.33%),
Hang Seng 23,495.72 (+0.44%), Shanghai Composite 3,612.25 (-0.71%), FTSE 100 10,761.33 (+0.29%),
DAX 25,981.09 (+0.63%). **Futures are flat to slightly green and are not pricing election risk.**

### The event of the day: US midterm elections

Tuesday, November 3, 2026 is a US general election day. This is the dominant scheduled risk into
the open — index option positioning into an event day typically carries an implied-vol premium, and
the aftermath (and the fiscal implications for a $115B-plus AI capex cycle) is the more important
read.

### Economic calendar — Tuesday, Nov 3

| Time (ET) | Event | Previous | Consensus |
|---|---|---|---|
| 10:00 | **JOLTS Job Openings (Sep)** | 7.079M | 7.13M |
| 10:00 | Factory Orders (Sep) | +0.1% m/m | — |
| 11:00 | LMI Logistics Managers Index (Oct) | 70.2 | — |
| 11:00 | Treasury buyback announcements | — | — |
| 11:30 | 6-week bill auction | — | — |
| 13:55 | Redbook YoY (Oct 31) | 9.3% | — |

**Week ahead:** Wed Nov 4 — ADP employment (prev +90k), trade balance (prev -$105.6B), ISM Services
(prev 54.9, cons 54.5), EIA crude inventories. Thu Nov 5 — Challenger job cuts, initial jobless
claims (prev 194k), productivity/unit labor costs, Fed's Barkin speaks. **Fri Nov 6 — the
Employment Situation (NFP consensus +55k vs +29k prior; unemployment 4.2%; UMich sentiment 48.0).**
Friday's payrolls is the week's real catalyst; Tuesday is the event-risk day.

Macro stance into the week: the Fed held at 3.75-4.00% on Wednesday, and market-implied odds of a
**December rate hike** were around 78% as of Monday's close — with ISM prices still in the mid-70s,
this is a tightening-expectation regime, not an easing one.

### Earnings — Tuesday, Nov 3

243 companies scheduled: 103 before the open, 140 after the close.

**Universe-relevant before the open:** PFE, ETN, FISV, MPC, KDP, RVTY, APO, YUM, ZBRA, ADT,
DD (DuPont), TEVA, TRI, AME, RACE, BNTX, ADM.

**Universe-relevant after the close:** **AMD** (consensus EPS ~$1.97, implied move ±7.9% — and AMD
fell -7.52% today), **SMCI** (also -7.62% today), **ANET**, **AMGN**, **BKNG**, **SU**, ALAB,
XYZ (Block), EA, LYV, AIG.

AMD is the one that matters: it reports into an AI complex that has just been de-rated, on a day when
SOXX fell -3.79%. Options imply ±7.9% — the largest single-name event risk on the board.

## Breadth & volatility

| Metric | Reading |
|---|---|
| VIX | 21.15, **+8.91%** (from 19.42) |
| VXN | 30.89, **+8.39%** (from 28.50) |
| CBOE total put/call | 0.90 |
| CBOE index put/call | 1.03 |
| CBOE equity put/call | 0.66 |
| CBOE ETP put/call | 0.93 |
| CBOE equity option volume | 4,816,835 (2,904,468 calls / 1,912,367 puts) |
| CNN Fear & Greed | 23 — Extreme Fear |

Read this carefully. **VIX +8.9% to 21.15 while the total put/call ratio sits at 0.90 — a neutral
reading — and the equity put/call at 0.66 is not elevated at all.** Volatility rose, but option
positioning does not show panic hedging. The equity/divergence is the tell: index hedging (index
P/C 1.03) is doing the work while single-name equity demand for puts stayed subdued (0.66, close
to its long-run ~0.6 average). This is a *narrow* de-risking expressed through index instruments,
not a market-wide flight to protection.

## Open research queue

1. **The Marvell/Lumentum arbitrage gap — the day's most important unresolved number.** LITE closed
   $684.40 against an implied deal value of **$1,132** (4.500 MRVL per LITE, $115B enterprise value,
   23.9% premium to the unaffected Oct 28 close, expected close H1 2028). LITE is trading ~39% below
   the implied value and both stocks fell. That is the market pricing a combination of deal-break
   risk, China regulatory approval risk, a very long close, and distrust of MRVL as the currency.
   Which of those is dominant is not resolvable from the tape — but the gap closing via MRVL
   re-rating (LITE up) versus via MRVL derating (LITE down further) is the cleanest expression of
   "is the AI trade being marked down?" and it will be the first thing to test on Wednesday.
2. **AI financing as a systemic theme, not an Oracle story.** ORCL -8.76% on a planned $10B equity +
   $10B debt raise, alongside Anthropic's disclosed ~$895.4B of compute commitments and ~$17B Q3
   revenue, is a financing-capacity question about the entire AI buildout. Watch SOXX/SMH (-3.79%/
   -2.71%) and whether the credit complex stays calm (HYG -0.18%). If HYG breaks, the story changes.
3. **IDXX's margin give-back.** Revenue guidance up $32M and EPS up $0.25, but operating margin
   guidance down to 32.1-32.3%. A +21.85% re-rating on a lower margin ceiling is a growth-multiple
   bet; a 60bp comparable margin improvement has to hold for it to be worth it.
4. **The oil round-trip.** WTI -7.6% on the session removed a supply-risk premium that had been
   supporting the energy complex. With XLE -3.96% and XOP -5.01%, the question is whether the
   diplomatic signal holds. Oil is the one macro variable in this brief with genuine headline risk
   in both directions, and it is the only thing that could make today's rotation reverse.
5. **Election-day volatility into Friday's payrolls.** ES futures are flat at 7,574.75, which does
   not price an election, a JOLTS print, and then NFP at +55k. Something will reprice by Friday.

## Source health

| Source | Endpoint / query | Status | Notes |
|---|---|---|---|
| MCP catalog probe | `probe_mcp.py` | **ok** — `catalog_ok total=133 finance_tools=0` | No financial MCP registered on this runtime (expected, not an error) |
| MCP bridge (packs) | `mcp_bridge.py --list-packs` | **ok** — tradier, fmp, market-recap | Bridge reachable over plain HTTPS JSON-RPC |
| Bridge `market-recap get_quotes` | 40 symbols across 3 batches | **ok** | Source of record for all prices, changes, volumes, `as_of` |
| Bridge `market-recap top_movers` | `{"category":"gainers"}` / `{"category":"losers"}` | **ok** | Only these two categories exist; `most_active` silently returns gainers |
| Bridge `market-recap market_snapshot` | `{}` | **ok** | Asia indices, futures, yields, FX, crypto |
| TradingView scanner | `POST https://scanner.tradingview.com/america/scan` | **ok** | 2,121 names ≥$2B; 3,563 names ≥$300M; 500 S&P 500 symbols. `postmarket_close` / `postmarket_change` / `postmarket_volume` confirmed present |
| Wikipedia S&P 500 list | MediaWiki `action=parse` wikitext | **ok** — 503 symbols | All three template forms parsed (`NyseSymbol`, `NasdaqSymbol`, `BZX link`); control check BRK-B / GOOGL / GOOG / FOX / CBOE all present |
| CBOE daily market statistics | cboe.com/markets/us/options/market-statistics/daily | **ok** | Put/call ratios for Nov 2; an earlier cached page showed a prior session's ratios (0.87/1.01/0.56) — the dated Nov 2 values were used |
| Investing.com market wrap | investopedia.com/stock-market-today-...-11022026 | **ok** | Used only for narrative + WTI session move + volume comparison |
| Marvell 8-K / press release | investor.marvell.com sec-filings 0001193125-26-442714 | **ok** | Deal terms, exchange ratio, implied value, close timing |
| MarketWatch | Marvell/Lumentum shareholders panning the deal | **ok** | LITE -18.59% = worst S&P 500 performer of the day |
| Company IR (IDEXX) | ir.idexx.com press release + transcript | **ok** | Q3 and guidance figures |
| StockTitan / CNBC / MarketChameleon | after-hours movers and earnings reactions | **ok** | Used as cross-check on the scanner's after-hours prints |
| Yahoo Finance earnings calendar | finance.yahoo.com/calendar/earnings?from=2026-11-03 | **ok** | EPS estimates and market caps for Nov 3 |
| Earnings Whispers | earningswhispers.com/calendar/20261103 | **ok** | 243 companies (103 BMO / 140 AMC) |
| Econoday / Trading Economics | economic calendar | **ok** | JOLTS, factory orders, auctions, week-ahead schedule |
| `research/watchlist.yaml` | repo `main` | **failed: 404** | Both candidate paths 404 — watchlist section omitted by design |
| Yahoo Finance JSON (direct) | — | **not used** | The bridge's market-recap is Yahoo-sourced and not rate-limited; no direct Yahoo call was needed |

**Unverified / caveats:**

- The bridge's `CL=F` prior-settle reference (96.46) differs slightly from the published WTI settle
  (~$96.26); both are shown with their own source rather than reconciled.
- Gold is quoted two ways and they are not the same instrument: GLD (the ETF) closed **+1.65%**,
  while GC=F is **-0.55%** versus its prior settle in the overnight session.
- One published wrap described PLTR as "slightly higher after hours" while the scanner showed
  -2.99%; the scanner value was used because two other sources described both AAPL and PLTR as
  lower after the bell.
- 3 of 503 S&P 500 symbols (`BRK-B`, `BF-B`, `KVUE`) did not match the scanner; the breadth and
  mover statistics above are therefore computed over 500 names, not 503.
- Extended-hours prints are the scanner's latest capture (a moving tape at ~22:22-22:35 ET), not
  closing-auction values.

**errors: 1** — one source failure (`research/watchlist.yaml`, 404), which removed the watchlist
section only. All other sources returned usable data. The absent `mcp__*` finance tools are **not**
counted as an error.
