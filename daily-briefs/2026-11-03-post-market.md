---
date: 2026-11-03
cron: 23-agentic-post-market-brief
fire_time_et: 22:30
snapshot_et: 22:30-22:50
session: 459612762210450
scheduled_at_ms: 1793763000000
status: ok
source: MCP bridge market-recap (closes, movers, futures, macro) + TradingView public scanner (sector ETFs cross-check, breadth, extended hours) + us-eod/2026-11-03.csv (cron #20 universe, 4,896 names) + web (catalysts, earnings/econ calendars, options stats)
primary_source: bridge market-recap for all closes and movers | TradingView scanner for breadth and extended-hours prints | us-eod CSV for the EOD universe | issuer IR/press releases for catalysts
universe: 4,896 US-listed names (cron #20 us-eod/2026-11-03.csv); 1,621 names with market cap > $2B used as the liquid set; after-hours screen = TradingView `type=stock`, mcap > $1B, extended volume > 50k shares
---

# Post-market brief — Tuesday, 2026-11-03 (ET)

## TL;DR

**The headline was the semiconductor complex and the actual breadth was the opposite.** The S&P 500
closed **7,568.92 +0.36%** and the Nasdaq Composite **25,372.01 +0.83%** — the first up-day after
three straight declines, and the best session since 27 October — while the Dow fell **197.26
(-0.38%)** on Apple. Underneath, **the median US-listed name fell**: 2,489 of 4,896 names closed
lower, and in the liquid set (cap > $2B) only **689 advanced against 921 decliners, a 0.75:1 ratio**.
**SPY +0.30% against RSP -0.33% is a 63bp cap-weight penalty** — the index was carried by a handful
of mega-caps and semiconductors, not by the market.

**The second thing that changed the tape is more durable than the index: AMD reported record
results after the close and the entire AI-supply chain repriced upward.** AMD's Q3 revenue was a
record **$13.4B (+45% y/y, data centre +97% to $8.5B)** with non-GAAP EPS **$2.09 vs $1.94
consensus** and a **Q4 revenue guide of ~$17B** — a ~27% sequential step-up. Arista (+9.5% after
hours), Super Micro (+7.2%), Duolingo (+11.2%), Astera Labs and the AI-hardware suppliers all
followed. The counterweight was **Amdocs (DOX -44.6%) and Skyworks (SWKS -17.4%)**, where guidance,
not the headline, was the problem.

**The caveat that changes how to read this:** every one of the day's biggest index-level drivers
landed *after* 16:00 ET, and the **overnight futures move is a different tape again** — the market
was already repricing on election results. As of ~22:30 ET, **ES -1.14% from its prior settle**
(**-0.78% vs the cash close**), **NQ -1.99% (-1.56% vs cash)**, with Treasury yields easing and the
dollar softer. So the closing index print — which reads as a clean bounce — is **stale relative to
what the market actually believes this morning**.

## Day's tape

Settled closes, 2026-11-03 (source: bridge `market-recap` → `get_quotes`, Yahoo-sourced).

| Index | Close | Change |
|---|---|---|
| S&P 500 (^GSPC) | 7,568.92 | **+0.36%** |
| Nasdaq Composite (^IXIC) | 25,372.01 | **+0.83%** |
| Nasdaq 100 (^NDX) | 28,180.26 | +0.68% |
| Dow Jones (^DJI) | 51,786.72 | **-0.38%** |
| Russell 2000 (^RUT) | 2,812.45 | +0.23% |
| PHLX Semiconductor (^SOX) | 10,600.40 | **+2.63%** |
| VIX | 20.83 | -1.51% |
| VXN | 30.53 | -1.17% |

Exchange volume: ^GSPC 3.11B shares, ^IXIC 7.51B, ^DJI 423M.

### ETF proxies

| Proxy | Close | Change | Proxy | Close | Change |
|---|---|---|---|---|---|
| SPY | 754.35 | +0.30% | RSP (equal-weight) | 219.26 | **-0.33%** |
| QQQ | 685.28 | **+0.62%** | SMH (semis) | 518.52 | **+2.01%** |
| IWM | 279.79 | +0.23% | SOXX (semis) | 465.00 | **+2.50%** |
| DIA | 517.06 | **-0.44%** | HYG (credit) | 76.98 | +0.12% |
| GLD | 359.26 | -0.66% | TLT | 81.11 | -0.76% |

**The cap-weight spread is the story.** SMH +2.01% and SOXX +2.50% against RSP -0.33% is not a
broad rally — it is a semiconductor squeeze inside a flat-to-down tape. Credit was calm (HYG
+0.12%), which argues this was a rotation, not a risk-off.

### Macro and cross-asset

| Asset | Level | Change |
|---|---|---|
| US 2Y (^IRX is 13-week; 5Y ^FVX used as proxy) | 4.743% | +1.07% |
| US 10Y (^TNX) | 4.952% | **+5.8 bp (from 4.894%)** |
| US 30Y (^TYX) | 5.324% | +1.04% |
| DXY | 101.40 | -0.45% |
| WTI crude (CL=F) | 95.62 | -0.49% |
| Gold (GC=F) | 3,947.20 | +0.18% |
| Bitcoin | 76,418.03 | -1.19% |

**Yields rose on a strong labour print, not on risk appetite.** The 10-year at 4.952% is a
+5.8bp move on the day — the JOLTS release beat (7.11M vs 7.079M prior) and it is the main reason
the Dow lagged. Gold flat, oil flat, credit flat: this was a **rates-and-tech session**, not a
macro-risk session.

### Overnight (as of ~22:30 ET, 03:30 UTC)

| Instrument | Level | vs prior settle | vs cash close |
|---|---|---|---|
| ES=F (S&P 500 Dec) | 7,510.25 | **-1.14%** | -0.78% |
| NQ=F (Nasdaq 100 Dec) | 27,742.00 | **-1.99%** | -1.56% |
| YM=F (Dow Dec) | 51,506 | -0.75% | -0.54% |
| RTY=F (Russell Dec) | 2,803.40 | -0.76% | -0.32% |
| Nikkei 225 (^N225) | 60,835.36 | **-3.56%** | — |
| FTSE 100 (^FTSE) | 10,638.43 | -1.14% | — |
| DAX (^GDAXI) | 25,864.62 | -0.45% | — |
| Hang Seng (^HSI) | 23,475.89 | -0.21% | — |

*Futures `change_pct` is measured against the prior futures settle, not the cash index close; the
"vs cash close" column is the derived overnight move and is the more actionable number. The
Nasdaq-100's outsized -1.56% vs the cash close reflects election-driven AI-regulatory repricing, not
the earnings news — AMD's guide was positive.*

## Sector rotation

Ranked by cap-weighted % change of all sector names with market cap > $300M in the cron #20 EOD
universe (4,896 names; 3,824 pass the cap filter).

| Rank | Sector | Cap-weighted | Median | n |
|---|---|---|---|---|
| 1 | Industrials | **+1.56%** | +0.24% | 414 |
| 2 | Information Technology | +1.43% | **+0.90%** | 334 |
| 3 | Communication Services | +0.91% | +0.98% | 96 |
| … | Real Estate | +0.03% | -0.45% | 144 |
| 9 | Utilities | -0.48% | -0.76% | 74 |
| 10 | Financials | -0.49% | -0.39% | 771 |
| 11 | Energy | -0.77% | -0.61% | 134 |
| 12 | Materials | -1.39% | -1.35% | 128 |
| 13 | Consumer Staples | **-1.78%** | **-1.90%** | 101 |

Sector-ETF read-through (bridge `get_quotes`): **XLK +1.31%, XLC +1.18%, XLI +0.95%** at the top;
**XLP -2.07%, XLB -2.01%, XLE -0.85%** at the bottom.

**Top 3:** Information Technology (XLK +1.31%) · Communication Services (XLC +1.18%) ·
Industrials (XLI +0.95%).
**Bottom 3:** Consumer Staples (XLP -2.07%) · Materials (XLB -2.01%) · Energy (XLE -0.85%).

Two notes on how to read this. **Healthcare's cap-weighted print is 0.00% while its median is
+1.12%** — a large-cap drag (AAPL is tech, but the healthcare cohort's heavyweights gave back
earlier gains) sitting on top of a healthy median; that is dispersion inside the sector, not
sector weakness. And **staples at -1.78% cap-weighted / -1.90% median with 771 financial names
flat-to-down** is the defensive unwind: money left the safe havens *into* tech, which is the
opposite of what a falling tape does. **Financials -0.49%** alongside a +5.8bp 10-year is
interest-rate sensitivity doing its job.

## Universe EOD review (no watchlist)

**`research/watchlist.yaml` does not exist in this Cloud runtime** — it lives only on the local
Mavis host, and both candidate repo paths 404. Per the skill's Cloud adaptation, **no watchlist
section is published**. The universe below is the routine's **deployed EOD universe** — cron #20's
`us-eod/2026-11-03.csv`, 4,896 names — and it is labelled as such, not as a personal watchlist.

**Liquid set (cap > $2B): 1,621 names — 689 advanced, 921 declined (0.75:1). 92 names gained ≥5%,
33 lost ≥5%.** The full universe was 2,193 up / 2,489 down.

### Biggest movers, liquid set

| Ticker | % | Close | Volume | Cap | Sector | What happened |
|---|---|---|---|---|---|---|
| **AEHR** | **+26.50%** | 65.11 | 8.4M | $2.0B | Technology | FQ1 rev $33.0M **+200% y/y** (est $27.1M), adj EPS **$0.28 vs $0.11**, swung to $7.18M net income from -$2.08M; bookings $46.7M (book-to-bill 1.4), effective backlog $109.3M; **FY27 revenue raised to $150M** (from $130-150M). Both Jefferies and Lake Street *cut* price targets on multiple compression. |
| **GPK** | **+21.54%** | 11.34 | 20.1M | $3.4B | Materials | Q3 net sales $2,192M (flat y/y, vs $2,164M est), adj EPS **$0.23 vs $0.22**; adj EBITDA $289M (13.2% margin, -190bp y/y on $83M input-cost inflation); **FY26 guidance reaffirmed** ($8.6B sales / $1.05B EBITDA / $0.65 EPS). |
| **RIOT** | **+18.41%** | 14.02 | 37.3M | $5.3B | Technology | AI-data-centre-leasing complex rebounded off a −30-45% month; **KBW cut the target to $20 from $35** on a "lease catalyst drought". Reports Wed AM. |
| **CIFR** | **+18.37%** | 8.12 | 65.1M | $3.3B | Financials | Same cohort. Q3 revenue $26.7M missed the $37.5M consensus; first HPC lease revenue $5.9M. JPM Overweight, PT $18 (from $22). |
| **XMTR** | **+16.55%** | 111.30 | 2.4M | $5.9B | Industrials | Q3 rev **$252.4M (+40%) vs $235.6M est**, adj EPS **$0.28 vs $0.18**, **first GAAP-profitable quarter** ($1.9M vs -$11.6M); FY26 growth outlook raised to ≥37%; new all-time high $117.50 intraday. |
| **HUT** | **+15.90%** | 63.75 | 8.2M | $7.2B | Financials | Rebound ahead of Wed AM earnings; $7.5B project financing on 949MW; KBW PT $92 from $154. |
| **WULF** | **+14.53%** | 12.53 | 48.4M | $6.2B | Financials | Cohort bounce; holds a 20-year Anthropic lease at Justified. |
| **NBIX** | **+13.42%** | 164.80 | 4.0M | $16.6B | Health Care | Adj EPS **$3.29 vs $1.91 est**, revenue **$1.12B +41%**, first quarter of net product sales above $1B; 2026 INGREZZA guidance raised to $2.9-2.925B; five brokers raised targets. |
| **DT** | **-14.59%** | 47.09 | 20.8M | $13.7B | Technology | Beat and trimmed: adj EPS $0.54 vs $0.49, revenue $580M vs $568M, ARR $2.21B +16% — **but FY27 adj operating income cut to $653-661M from $682-690M** (Arize dilution 175bp) and FY adj EPS to $1.88-1.90 from $1.97-1.99. |
| **IT** | **-13.26%** | 204.10 | 3.0M | $13.7B | Technology | **Beat and raised, and fell**: adj EPS $3.59 vs $2.84, revenue $1.505B vs $1.49B, FY adj EPS guidance raised to ≥$14.65 from ≥$14.00 — but GAAP revenue **-1.3% y/y** on contract value +1.1% sequentially only. |
| **CVI** | **-13.10%** | 48.59 | 3.0M | $4.9B | Energy | Q3 miss (reported AM). |
| **PAY** | **-11.50%** | 31.02 | 1.6M | $3.9B | Financials | Q3 miss (reported AM). |
| **STVN** | **-28.57%** | 14.10 | 4.8M | ~$3.9B | Health Care | The day's worst liquid name. Revenue +8% to €326.1M and FY26 guidance maintained, **but lower expected GLP-1 volumes drove only low-single-digit FY27 growth**; Morningstar cut fair value 15%. GLP-1 revenue was ~17-18% of total and *fell* in Q3. |
| **SYY** | **-9.32%** | 74.12 | 7.4M | $35.4B | Consumer Staples | Q1 FY27 miss — the read that dragged the whole staples sector. |
| **TRI** | **-9.87%** | 110.18 | 3.0M | — | Industrials | Q3 adj EPS $0.81 vs $0.89, revenue $1.83B vs $1.91B (Zacks); legal-segment margin fell to 46.6% from 49% on $22M AI spend + $22M severance; FY organic revenue outlook *raised* to 8.5-9.0%. |
| **AAPL** | **-1.90%** | 331.90 | 56.7M | $4,874B | Technology | The Dow's drag. Q4 beat ($2.10 EPS, $114.48B rev) **but** Dec-qtr gross margin guided 45-46% vs 46.3% consensus, Services growth 8-9% vs ~10.7% expected, on "unprecedented" memory pricing; purchase obligations +$33B to $89.7B. |

### Most active, liquid set

| Ticker | Volume | % | Sector |
|---|---|---|---|
| INTC | 140.8M | +0.97% | Technology |
| NVDA | 82.4M | +2.29% | Technology |
| SPCX | 69.2M | +3.62% | Industrials |
| ORCL | 67.2M | **+5.86%** | Technology |
| RKT | 66.7M | +0.36% | Financials |
| CIFR | 65.1M | **+18.37%** | Financials |
| AAPL | 56.7M | -1.90% | Technology |
| SMCI | 51.5M | +3.12% | Technology |
| PLTR | 50.7M | -1.65% | Technology |

## After-hours movers

TradingView scanner extended-hours prints, `type=stock`, market cap > $1B, extended volume > 50k
shares. Extended-hours percentages are **vs the same day's 16:00 ET close**.

### Top 5 gainers

| Ticker | After-hours | Regular | AH volume | Catalyst |
|---|---|---|---|---|
| **PCOR** | **+11.26%** | +1.09% | 1.27M | Q3 results (reported AMC) — Procore Technologies. |
| **DUOL** | **+11.17%** | -5.37% | 0.39M | Q3 revenue **$309M vs $303M est**, DAU **+29% y/y to 64.9M** (accelerating from +23%), bookings $316.1M +12%; adj EPS $0.54 **missed** $0.57; FY26 bookings/revenue guidance **raised**; Max tier to be sunset. |
| **PRIM** | **+9.65%** | +7.91% | 0.35M | Q3 results — Primoris. |
| **ANET** | **+9.47%** | +3.50% | 2.81M | Q3 revenue **$3.66B, +58.5%**, EPS $1.20 vs $1.08; **Q4 guide $3.9-4.0B / EPS $1.26-1.30 vs $3.60B / $1.15** expected. |
| **FLYW** | **+8.09%** | -1.74% | 0.68M | Q3 results — Flywire. |

### Top 5 losers

| Ticker | After-hours | Regular | AH volume | Catalyst |
|---|---|---|---|---|
| **DOX** | **-44.61%** | -1.75% | 0.63M | Amdocs FQ4: adj EPS $1.98 (in line), revenue $1.19B — but **guided lower revenue for the new fiscal year**; trading was halted 16:00-17:00 ET for pending news. |
| **NRIX** | **-32.61%** | +0.47% | 2.71M | Sanofi ended work on a partnered drug candidate; Nurix no longer expects the associated payments. |
| **SWKS** | **-17.35%** | +0.27% | 1.11M | Skyworks FQ4 adj EPS $1.28 vs $1.27 est, revenue $1.046B vs $1.03B est — **but** first combined post-Qorvo guide: FQ1 revenue $1.80-1.90B vs ~$2.00B expected, EPS $1.25 vs $1.50; only ~$150M of opex synergies in FY27 against a $500M+ target. |
| **UNM** | -9.10% | +0.14% | 0.47M | United Nuclear — no catalyst sourced in this run. |
| **ALAB** | -3.61% | +1.72% | 1.68M | Astera Labs — Q3 revenue +154% to a record $584.9M, but the extended print gave back part of the move. |

### The rest of the AI-hardware reaction (after-hours)

| Ticker | After-hours | Regular | Read |
|---|---|---|---|
| AMD | **+5.02%** | +3.65% | Record Q3 rev $13.4B (+45%), data centre $8.5B (+97%), adj EPS $2.09 vs $1.94; **Q4 guide ~$17B** vs $16.23B est. |
| SMCI | **+7.20%** | +3.12% | Revenue $19.9B beat; **FY27 net sales guided $72-82B vs $69.17B consensus**. |
| ASTERA (ALAB) | -3.61% | +1.72% | Strong print, weaker extended tape. |
| XYZ (Block) | +5.84% | -1.45% | Adjusted EPS **+109% to a record $1.13**. |
| MCHP | -3.13% | +2.35% | Microchip — no sourced catalyst. |
| TOST | -3.76% | +0.24% | Toast — no sourced catalyst. |

## After-hours earnings reactions

| Name | Reaction | The number |
|---|---|---|
| **AMD** | +5.02% AH | Rev $13.4B vs $13.09B est; adj EPS $2.09 vs $1.94; Q4 rev ~$17B (implies ~27% q/q vs 16% in Q3). Closed $483.90 (+3.65%). |
| **ANET** | +9.47% AH | Rev $3.66B (+58.5%) vs $3.33B; EPS $1.20 vs $1.08; Q4 guide $3.9-4.0B / $1.26-1.30. |
| **SMCI** | +7.20% AH | Rev $19.9B, FY27 guide $72-82B vs $69.17B. |
| **DUOL** | +11.17% AH | Rev $309M vs $303M; DAU +29%; adj EPS $0.54 vs $0.57 (miss). |
| **SWKS** | -17.35% AH | Guide miss post-Qorvo. |
| **DOX** | -44.61% AH | New-year revenue guide lower. |
| **XYZ (Block)** | +5.84% AH | Adj EPS +109% to record $1.13 on payments volume. |
| **PCOR / PRIM / FLYW / CRCT / LMB / FTK / ALIT** | +8% to +19% AH | Q3 results; individual detail not sourced in this run. |
| **NRIX** | -32.61% AH | Sanofi partnership terminated. |
| **UNM / CDW / RRR / RARE / SSRM / MDU** | -5% to -9% AH | No sourced catalyst in this run — see Flags. |

## Tomorrow's setup — Wednesday 2026-11-04

### Futures and the overnight setup

The post-close futures move is the setup, and it is **negative**: **ES -0.78% and NQ -1.56% vs the
cash close** at ~22:30 ET, with the Dow futures least affected (-0.54%). The driver is
**election results**, not earnings: Democrats took the first Senate seats, prediction markets
priced a Democratic House at 91-93% and a Senate at 70%+, and the market is pricing the AI
complex for the regulatory scrutiny a Democratic Congress implies. Asia confirms it — **Nikkei
-3.56%**. Yields and the dollar both eased, which is the classic "political risk plus lower
growth expectations" mix. **AMD's beat was priced into the earlier session and has been
overwhelmed by the election tape since.**

### Economic calendar (Wed 2026-11-04, ET)

| Time | Release | Forecast | Prior |
|---|---|---|---|
| 07:00 | MBA mortgage applications | — | — |
| **08:15** | **ADP employment (Oct)** | **68K** | 90K |
| 08:30 | International trade balance (Sep) | — | — |
| 08:30 | Treasury refunding announcement (3Y/10Y/30Y) | — | — |
| 09:45 | S&P Global PMI composite final | — | — |
| **10:00** | **ISM services PMI (Oct)** | **54.8** | 54.9 |
| 10:30 | EIA petroleum status report | — | — |
| 11:30 | 4-month bill auction | — | — |

**ADP at 68K vs 90K prior and ISM services at 54.8 vs 54.9 is a soft-morning calendar stacked
behind an election-driven futures decline.** Also on the radar: **Thursday** has initial jobless
claims (197K est), Q3 productivity, Challenger job cuts and Fed speakers (Hammack 08:50, Barkin
09:10); **Friday** has **October nonfarm payrolls (63K est, unemployment 4.2%)** — the week's
dominant event, and it lands immediately after ADP has already softened the labour read.

### Earnings calendar (Wed 2026-11-04)

**Before the open (~196 names; the ones that matter):** **UBER**, **DDOG** (Datadog), **NVO**
(Novo Nordisk), **CVS**, **MCD**, **GFS** (GlobalFoundries), **KHC** (Kraft Heinz), **FIS**,
**RIOT**, **HUT** (both crypto/AI-leasing names, +18% and +16% yesterday), **SEDG** (SolarEdge),
**EMR**, **OC** (Owens Corning), **Q** (Qnity Electronics), **W** (Wayfair), **CRCL** (Circle),
**VSH / VPG**, **TRMB**, **BRKR**, **ADNT**, **SWK**, **MLM**, **BCO**.

**After the close (~350 names; the ones that matter):** **QCOM** (Qualcomm, EPS est $2.20, rev
est $10.3B — the single largest name on the calendar), **ARM**, **APP** (AppLovin, EPS est $4.08),
**MELI** (MercadoLibre), **MCK**, **COHR** (Coherent), **CAVA**, **FSLY**, **AMC**, **FICO** (Fair
Isaac), **ALB** (Albemarle), **BYND**, **JOBY**, **LUMN**, **SNAP**, **FIG** (Figma), **RUN**,
**RVMD**, **AEVA**, **BROS**, **DAVE**.

*Consensus counts differ by provider (EarningsWhispers 546 for the day; MarketBeat/Digrin 373-788;
RapidTradeView 467). The named roster is consistent across them.*

### News to watch for the top movers

- **AAPL** — the memory-cost squeeze. Price-inelasticity is the open question; Apple raised Mac,
  iPad and iPhone prices in June/September and the December-quarter guide assumes no relief.
- **SWKS** — whether the -17% extended print holds into the open; guidance credibility after the
  Qorvo merger is the test.
- **DOX** — a 44% extended decline on a new-year revenue guide is a rare print; watch for
  contagion into the software complex.
- **RIOT / HUT / CIFR / WULF** — three of these report tomorrow morning on exactly the metric the
  market is arguing about: whether signed AI leases start converting to rent on schedule.
- **Gold and the 10-year** — 4.952% and a -1.19% dollar; if the political premium unwinds, the
  10-year is the cleanest expression of it.

## Open research queue

1. **Did the AI-complex after-hours gains survive the election-driven futures decline?** AMD, ANET
   and SMCI were up in the after-hours session while ES was -1.14% and NQ -1.99%. The two forces
   are pointing in opposite directions and the open will resolve it. Highest-information item.
2. **Is the "blue wave" risk actually about AI, or about the market's own positioning?** Reuters
   analysts explicitly attribute the sharper Nasdaq-futures decline to regulatory scrutiny of AI
   and Big Tech rather than to fiscal policy. Worth testing against the sector's own tape.
3. **The cap-weight penalty is now two days running** (63bp today, 158bp on 30 Oct). Whether the
   equal-weight index keeps bleeding while the cap-weighted index bounces is the cleanest read on
   how much of this is positioning rather than fundamentals.
4. **GLP-1 volume is now a first-order sector variable** — STVN fell 28.6% on lower expected
   GLP-1 volumes with the stock at ~$3.9B cap and FY26 guidance intact. Which other names have
   GLP-1 revenue in the 10-20% band is a tractable screen.
5. **The software "beat-and-raise-and-fall" cluster** (IT -13.3% on a raised guide, DT -14.6% on
   trimmed FY27 operating income, TRI -9.9% on an EPS miss with revenue guidance raised) suggests
   a regime where guidance credibility, not the beat, sets the price. Unclear how long that lasts.
6. **ADP 68K vs 90K and ISM services 54.8 vs 54.9** with Friday's NFP at 63K — if ADP undershoots,
   the labour market re-rates before the Fed does anything about it.

## Source health

| Source | Query / URL | Status |
|---|---|---|
| Bridge `market-recap` → `get_quotes` | 4 batched calls (indices+ETFs, sectors, futures+movers, macro) | **ok** — 17/17, 13/13, 11/11, 14/14 found |
| Bridge `market-recap` → `top_movers` | `category=losers` / `gainers` | **ok** — note: `most_active` returned the gainers list, so most-active was taken from the scanner and the us-eod CSV instead |
| Bridge `market-recap` → `market_snapshot` | overnight groups | **ok** |
| Bridge `market-recap` → `price_history` | — | not used |
| TradingView scanner `america/scan` | sector ETFs, breadth counts, extended-hours (4 calls) | **ok** — HTTP 200, 533 names in the unfiltered extended set, 36 liquid gainers / 40 liquid losers, 300-row range ceiling respected |
| `us-eod/2026-11-03.csv` (cron #20) | `raw.githubusercontent.com/karizaco/minimax-cloud-outputs/main/us-eod/2026-11-03.csv` | **ok** — 4,896 rows; 1,621 names > $2B cap; 0 rows with a blank `change_pct` |
| MCP availability probe (`probe_mcp.py`) | connector catalog | **ok** — `catalog_ok total=135 finance_tools=0`; bridge packs answering: tradier, fmp, market-recap |
| `research/watchlist.yaml` | repo `main` | **failed: 404** — both candidate paths 404; watchlist section omitted by design |
| CBOE put/call | `cboe.com/data/mktstat.aspx` + `marketindicators.net` | **partial** — see below |
| CBOE ratio CSVs | `cdn.cboe.com/.../totalpc.csv` et al | **failed: stale** — the served CSVs end at 10/04/2019 and contain no Nov-2026 rows |
| Web (catalysts) | issuer IR releases, StockTitan, CNBC, Reuters, Yahoo Finance, MarketBeat, Investing.com, Benzinga, TradingKey, Longbridge, 24/7 Wall St. | **ok** — every catalyst in this brief is sourced to a company release or a named outlet |
| Web (calendars) | EarningsWhispers, MarketWatch, Econoday, Scotiabank, Liquid.trade, investing.com | **ok** — ADP 68K/90K and ISM services 54.8/54.9 agree across two independent providers |

**Degraded / unverifiable items, stated plainly:**

- **Put/call ratio — sources conflict.** The Cboe daily statistics page shows total put/call
  **0.87**, index **1.01**, equity **0.56**, VIX **0.53**; marketindicators.net, dated Tuesday
  3 November, shows total **0.87** but index **0.96**, equity **0.67**, VIX **0.28**. The total
  agrees; the components do not, and the marketindicators equity print (0.67) matches
  Schaeffer's description of **Monday's** session, so that table may be a day stale. **The total
  0.87 is the number published for 3 November** and is what this brief uses; the component split is
  reported above with both readings rather than a single invented figure. The CBOE CSV endpoints
  could not arbitrate — they serve data through 2019 only.
- **After-hours prints move.** Every extended-hours number here is a snapshot at roughly 22:30 ET
  from the TradingView scanner and will differ from earlier published marks — AMD was quoted at
  +6.56% at 19:00 ET and +7.73% at 18:00 ET before settling at +5.02% in this snapshot. The
  regular-session closes are settled and not subject to this.
- **STVN and TRI are absent from the cron #20 us-eod universe** (both are priced in the bridge and
  the scanner). STVN's -28.57% comes from the bridge `top_movers` list and the Yahoo quote page;
  TRI's -9.87% from the bridge movers list and a market wrap. Both are single-sourced to the
  bridge for the percentage.
- **No watchlist file** — the personal watchlist lives on the local Windows Mavis host and is not
  reachable from the Cloud sandbox.
- **Futures `change_pct` is vs the prior futures settle, not the cash index close.** The "vs cash
  close" column is derived by this brief, not published by the source.
- **CVI (-13.10%) and PAY (-11.50%) catalysts were not sourced** in this run; both are reported
  here with the price move only. Same for UNM, CDW, RRR, RARE, SSRM and MDU in the after-hours
  table — no catalyst is asserted for them.

**No `mcp__*` finance tool is registered on this runtime** (catalog: 135 tools, 0 finance) — that
is the expected state and is not counted as an error.

## Method notes

- **One source per field.** All closes, movers and macro levels come from the bridge
  `market-recap` (Yahoo-sourced, not rate-limited). Sector rotation comes from the cron #20 EOD
  universe and is cross-checked against bridge sector-ETF quotes. Extended-hours prints come from
  the TradingView scanner only. Catalysts come from issuer releases and named outlets only.
- **Breadth denominators.** "Liquid set" = market cap > $2B (1,621 names). "Full universe" = all
  4,896 names in cron #20's file. Advancers/decliners counts for the whole market use the scanner
  (cap > $2B filter: 1,414 advancing, 1,780 declining, 267 names up ≥5%, 187 down ≤-5%) and are
  consistent in direction with the us-eod CSV counts.
- **No audit log** is written on Cloud, per the shared runtime contract.
- **Read-only by design.** No trades, no positions, no sizing.
