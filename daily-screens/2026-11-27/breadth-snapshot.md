---
artifact: breadth-snapshot
contract: breadth-artifact-v1
cron: "#10 stock-screener-breadth-snapshot"
fire_time_et: "2026-11-27 14:00:03 ET"
data_date: "2026-11-25"
live_date: "2026-11-27"
breadth_universe: "NYSE/NASDAQ/AMEX, market cap > $10B, 881 names"
vix_quote_time: "2026-11-27 13:00:00 ET (Yahoo chart API ^VIX/^VIX3M, 5-minute bar — the last bar of the 13:00 ET early close)"
vix_pair: "VIX 24.10 / VIX3M 23.93 — single pair, used everywhere in this document"
cross_reference: "end-of-day counterpart: daily-screens/2026-11-27/breadth.md (cron #09, 18:30 ET)"
size_cut_pct: 0
uncertainty: true
late_cycle: false
degraded_sources: 1
---
_contract: breadth-artifact-v1 · data_date 2026-11-25 · universe 881 names · breadth 44.15% (pctile 23.4 · NORMAL) · divergence +44.15 pp (BROAD) · AD 670/204/7_

# Breadth & Regime Snapshot — Friday, 27 November 2026 (intraday, cron #10)

**Intraday breadth read — 2026-11-27, snapshot at 14:00:03 ET.** The breadth, advance/decline and index-positioning layers describe the *settled* 2026-11-25 session (shibui is T+1, and 2026-11-26 was Thanksgiving, so the newest ingested session is two sessions behind the cron day). The tape and the volatility pair are the *settled* 2026-11-27 close — the NYSE and Nasdaq closed early at 13:00 ET for the Friday after Thanksgiving, so this is a completed half-session, not a mid-session print. The two layers are never blended. Source of record for prices: the MCP-over-HTTP bridge's `market-recap`; for the settled breadth series: shibui over the same bridge. Not a replay — the fire was dispatched on schedule (`stall_min: 0`).

## TL;DR

- **Breadth is repairing off the washout and the settled participation read is strong, but one session does not repair a ten-session deficit.** On the settled 2026-11-25 session **44.15%** of the 881 large caps sit above their own 20-DMA — the **23.4th percentile** of the past year (NORMAL), up from 36.34% on 2026-11-24 — and the 50-DMA split is **54.26%** (37.5th percentile). The settled advance/decline tally was **670 advancing / 204 declining / 7 unchanged** — ratio **3.284**, net **+466** — yet the ten-session net is still **-1232** and the ADL slope **-172.71 net advances per session**. Participation is healing; the rate of repair is still negative.
- **The divergence is the number that changes position sizing: +44.15 pp, BROAD (95.4th percentile) — the widest spread in a year, and it has widened five sessions running (+23.75 → +16.70 → +29.17 → +36.21 → +44.15 pp).** With **0 of 5** index ETFs above their own 20-DMA, the index is the weak leg, not the market: the average large cap is materially healthier in trend terms than the cap-weighted index. Today's tape runs the *other* way — SPY **+1.62%** against RSP **+1.22%** (**-0.40 pp**, index-led) with QQQ **+2.69%** and SMH **+4.17%** — so today's bounce repairs the index faster than the average stock, which is what should compress this spread.
- **Read the tape as a holiday-shortened half-session, and read the breadth layer as two sessions stale.** The exchange closed early at **13:00 ET** and the fire fired at 14:00:03 ET, so the published tape is the completed Black Friday close, not a live mid-session print and not a full day's volume. The breadth layer is the settled **2026-11-25** session because 2026-11-26 was Thanksgiving, so today's +1.62% rally has **not yet entered** the breadth series. Volatility says the same thing: VIX **24.10** (-10.07%) against VIX3M 23.93 = **1.0071**, so `uncertainty` is still ON — by a hair. Regime: `size_cut_pct` **0** (the index is below its 20-DMA, but breadth at 44.15% is above the 40% trigger), `uncertainty` **true**, `late_cycle` **false**.

## Breadth — 2026-11-25 settled session (shibui)

| Metric | Value |
|---|---|
| Universe | NYSE/NASDAQ/AMEX, market cap > $10B |
| Names in universe | 881 |
| Above 20-DMA | 389 (44.15%) |
| Below 20-DMA | 492 (55.85%) |
| Above 50-DMA | 478 (54.26%) |
| Index ETFs above their own 20-DMA | 0 of 5 (0.0%) |
| Index ETFs above their own 50-DMA | 1 of 5 (20.0%) |
| Advance/decline — settled session | 670 advancing / 204 declining / 7 unchanged (A/D ratio 3.284) |

The universe is **not frozen** — the market-cap floor is applied to the latest `valuation` row, so the count moves as those rows refresh. Today's universe: **881 names**.

## Participation — advance/decline and the 10-session ADL

| Date | Advancing | Declining | Unchanged | Net | ADL (cumulative) | ADL slope (10d) |
|---|---|---|---|---|---|---|
| 2026-11-12 | 217 | 660 | 3 | -443 | -39 | 20.03 |
| 2026-11-13 | 528 | 344 | 8 | +184 | 145 | 14.12 |
| 2026-11-16 | 234 | 641 | 5 | -407 | -262 | 0.4 |
| 2026-11-17 | 162 | 716 | 1 | -554 | -816 | -50.77 |
| 2026-11-18 | 381 | 495 | 3 | -114 | -930 | -72.98 |
| 2026-11-19 | 77 | 799 | 3 | -722 | -1652 | -157.75 |
| 2026-11-20 | 175 | 701 | 4 | -526 | -2178 | -263.26 |
| 2026-11-23 | 745 | 132 | 4 | +613 | -1565 | -273.99 |
| 2026-11-24 | 574 | 303 | 4 | +271 | -1294 | -253.72 |
| 2026-11-25 | 670 | 204 | 7 | +466 | -828 | -172.71 |

**A/D ratio 3.284 today** (670 advancing / 204 declining). Over the last 10 sessions the net advances total **-1232** and the ADL slope is **-172.71 net advances per session** (10-session A/D ratio 0.753). The ADL is cumulative from 2026-09-01, so it is a LEVEL; the slope is the rate.

## Breadth percentile — where today's level sits in its own history

Percentiles are against the trailing 1-year distribution of the same series (261 sessions, 2025-11-12 → 2026-11-25). A level without a percentile is a number without a context.

| Metric | Value | Percentile | Band |
|---|---|---|---|
| `breadth_pct` | 44.15% | — | — |
| `breadth_pctile_1y` | 23.4 | — | NORMAL |
| `breadth_pct_50dma` | 54.26% | — | — |
| `breadth_pctile_1y_50dma` | 37.5 | — | NORMAL |
| `index_etfs_above_20dma` | 0 of 5 | 17.2 | BELOW_NORMAL |

## Breadth divergence — broad market versus index ETFs

| Metric | Value | Band | 1-year percentile |
|---|---|---|---|
| `breadth_divergence` | +44.15 pp | BROAD | 95.4 |

`breadth_divergence` = the large-cap universe's share above its own 20-DMA minus the index ETFs' share above their own 20-DMA. **BROAD** means the average large cap is materially healthier than the index; **NARROW** means the index is healthier than the average large cap — the cap-weighted index is carried by its biggest names while the average stock is not participating; **MATCHED** means they agree.

| Date | Divergence (pp) |
|---|---|
| 2026-11-19 | +23.75 |
| 2026-11-20 | +16.70 |
| 2026-11-23 | +29.17 |
| 2026-11-24 | +36.21 |
| 2026-11-25 | +44.15 |

## Index positioning — distance from the 50-DMA

| Symbol | Close | 20-DMA | 50-DMA | Distance from 50-DMA | ATR multiple |
|---|---|---|---|---|---|
| IWM | 268.87 | 274.39 | 277.16 | -2.99% | -1.82 |
| QQQ | 633.93 | 666.73 | 707.05 | -10.34% | -6.38 |
| QQQE | 109.84 | 113.59 | 117.38 | -6.42% | -4.88 |
| RSP | 215.74 | 217.60 | 214.82 | +0.43% | 0.41 |
| SPY | 716.70 | 740.33 | 757.89 | -5.43% | -5.06 |

## Live tape — 2026-11-27

Live quotes via the bridge's `market-recap` (`get_quotes`), Yahoo-sourced and cross-checked inside the same call against a second quote source — **27/27 `agrees`**, max difference **0.00%**. Snapshot **2026-11-27 19:03 UTC (14:03 ET)**, the completed **early close**: the NYSE and Nasdaq shut at **13:00 ET** for the Friday after Thanksgiving, and every instrument carries `market_state: post` with `as_of` 13:00 ET. These are settled closes, not a mid-session print.

| Instrument | Role | Last | Chg % | Day range (low – high) | Volume |
|---|---|---|---|---|---|
| SPY | S&P 500 | 728.32 | +1.62% | 719.62 – 729.15 | 38,759,705 |
| QQQ | Nasdaq-100 | 650.99 | +2.69% | 636.72 – 651.34 | 34,995,978 |
| RSP | S&P 500 equal-weight | 218.38 | +1.22% | 216.68 – 218.40 | 6,760,473 |
| QQQE | Nasdaq-100 equal-weight | 112.50 | +2.42% | 110.52 – 112.50 | 224,978 |
| IWM | Russell 2000 | 273.79 | +1.83% | 270.69 – 273.92 | 14,115,567 |
| | | | | | |
| SMH | VanEck Semiconductor | 440.06 | +4.17% | 421.88 – 440.27 | 7,666,558 |
| XLK | Technology | 160.15 | +2.80% | 156.18 – 160.30 | 6,858,456 |
| XLC | Communication services | 107.48 | +1.99% | 106.48 – 107.62 | 2,768,363 |
| XLY | Consumer discretionary | 119.97 | +2.11% | 118.39 – 120.05 | 5,353,014 |
| XLP | Consumer staples | 92.68 | +0.41% | 91.95 – 92.74 | 9,642,436 |
| XLE | Energy | 61.67 | +1.26% | 61.55 – 62.07 | 20,627,193 |
| XLF | Financials | 57.16 | +1.15% | 56.89 – 57.34 | 19,305,245 |
| XLV | Health care | 184.20 | +0.28% | 182.75 – 184.41 | 5,043,879 |
| XLI | Industrials | 165.56 | +1.60% | 164.12 – 165.69 | 5,160,442 |
| XLB | Materials | 52.15 | +1.84% | 51.57 – 52.19 | 8,435,085 |
| XLRE | Real estate | 44.14 | +0.64% | 43.95 – 44.17 | 4,205,467 |
| XLU | Utilities | 43.73 | +0.28% | 43.57 – 43.78 | 13,760,899 |
| | | | | | |
| ^GSPC | S&P 500 index | 7,297.49 | +1.60% | 7,211.46 – 7,304.10 | 1,715,427,000 |
| ^IXIC | Nasdaq Composite | 24,129.50 | +2.31% | 23,690.60 – 24,149.09 | 4,748,627,000 |
| ^DJI | Dow Jones Industrial Average | 50,774.94 | +1.18% | 50,398.29 – 50,830.19 | 365,405,114 |
| ^RUT | Russell 2000 index | 2,750.30 | +1.71% | 2,721.39 – 2,751.42 | — |
| | | | | | |
| NVDA | Nvidia | 150.49 | +0.80% | 145.39 – 151.98 | 180,940,449 |
| MU | Micron | 646.95 | +7.60% | 607.27 – 654.33 | 26,547,049 |
| AMD | Advanced Micro Devices | 424.54 | +4.56% | 398.59 – 426.81 | 22,152,138 |
| TSM | TSMC ADR | 353.34 | +3.21% | 344.60 – 354.36 | 9,345,564 |
| AVGO | Broadcom | 312.34 | +3.82% | 304.75 – 313.13 | 17,045,811 |
| XBI | SPDR S&P Biotech | 158.50 | +1.21% | 155.38 – 158.50 | 3,994,195 |

**The tape in one line: an AI- and semiconductor-led Black Friday rally, and the index led it.** SPY closed **+1.62%** at 728.32, QQQ **+2.69%**, SMH **+4.17%**, IWM **+1.83%**, the Dow **+1.18%** and the Nasdaq Composite **+2.31%**. The leadership was concentrated in memory and semis: **MU +7.60%**, AMD **+4.56%**, AVGO **+3.82%**, TSM **+3.21%**.

**But the average stock did not lead — equal-weight lagged the cap-weighted index.** RSP **+1.22%** against SPY **+1.62%** is **-0.40 pp** of equal-weight underperformance, and RSP closed a hair below its own session high (218.40) while sitting 0.78% above its low (216.68). Tech (**+2.80%**) and discretionary (**+2.11%**) led the sectors; staples (**+0.41%**), health care (**+0.28%**), utilities (**+0.28%**) and real estate (**+0.64%**) barely moved. On a day the index rose 1.6%, the defensives stood still and the equal-weight index rose less: this was a narrow, risk-on session.

**Nvidia was the weak leg of its own complex.** NVDA closed **+0.80%** on a day MU rose 7.60% and SMH 4.17%, after trading as low as **145.39 (-2.62%** from its 149.30 prior close. The AI complex rallied around Nvidia rather than through it — the same name that drove the historic Monday rebound on Jensen Huang's reinstatement as CEO is now the laggard of a chip rally.

**Cross-asset and overnight** (bridge `market_snapshot`, same pull):

| Instrument | Level | Chg |
|---|---|---|
| Nikkei 225 | 58,711.11 | +2.11% |
| Hang Seng | 22,694.77 | +3.32% |
| Shanghai Composite | 3,606.49 | +3.74% |
| FTSE 100 | 10,698.81 | +0.84% |
| DAX | 25,441.24 | +0.90% |
| S&P 500 future (live) | 7,308.25 | +1.56% |
| US 10-year yield | 4.936 | +1.82% |
| US Dollar Index (DXY) | 104.046 | +0.37% |
| WTI crude | 82.91 | -0.92% |
| Gold | 3,668.50 | +2.91% |
| Bitcoin | 59,894.14 | -0.99% |

**Overnight risk appetite confirmed the rally.** Asia led — the Nikkei **+2.11%**, the Hang Seng **+3.32%**, the Shanghai Composite **+3.74%** — and Europe followed (DAX +0.90%, FTSE 100 +0.84%). The 10-year yield rose **1.82%** to **4.936%** and gold **+2.91%** to 3,668.50 while WTI fell **-0.92%** and Bitcoin **-0.99%**: equities up with a rising yield and a rising gold is a growth-and-hedge tape, not a flight to safety. The S&P 500 futures quote was **7,308.25 (+1.56%)** at the snapshot — a live futures print, not a settlement, so it is context and not a published close.

## Volatility — single pair, live

**One pair, one source, one moment.** VIX **24.10** / VIX3M **23.93**, quoted **2026-11-27 13:00:00 ET**, both symbols read from the **same** 5-minute bar of the same session — the last bar the Yahoo feed carries for that session, because the exchange closed at 13:00 ET.

| | Value | Prior close | Change |
|---|---|---|---|
| **VIX** | **24.10** | 26.80 | -10.07% |
| **VIX3M** | **23.93** | 26.17 | -8.56% |
| **VIX / VIX3M** | **1.0071** | — | front month **above** the 3-month — inverted by 0.17 points |

**The ratio is above 1.0, so `uncertainty` is ON — but only just.** The front month sits **0.17 points** above the three-month after falling 10.07% on a 1.62% SPY rally while the three-month fell only 8.56%: the near-term event-risk premium is being compressed, but the term structure is still inverted. The pair is the **live print** for this session — the fire clock is 14:00:03 ET and the 13:00 bar is the latest bar the feed carries for that session, so this is the session's closing volatility print, not a reconstruction. The Cboe delayed-quote CDN (the venue's own feed, the primary source for this routine) answered **HTTP 403** from this egress, so this pair is the Yahoo chart-API fallback and the `source` string in `_regime-intraday.json` names it.

## Regime

| Flag | Value | Rule |
|---|---|---|
| `size_cut_pct` | 0 | size cut triggers only when the index is below its 20-DMA **and** breadth < 40% |
| `uncertainty` | true | VIX/VIX3M > 1.0 |
| `late_cycle` | false | any index ETF more than 6% above its own 50-DMA |
| `index_below_20sma` | true | fewer than 3 of the 5 index ETFs above their own 20-DMA |

## Flags

- **The published tape is a completed half-session, not a full day.** The NYSE and Nasdaq closed early at 13:00 ET on the Friday after Thanksgiving, so every printed volume is roughly three hours of trading and the closing auction was compressed. Do not compare these volumes with a normal session's, and do not read +1.62% as a full-day trend read.
- **The breadth layer is two sessions behind the tape, not one.** The settled session is 2026-11-25 because 2026-11-26 was Thanksgiving, so today's rally has not entered the breadth series at all and the +44.15 pp divergence has not had a chance to narrow.
- **The `BROAD` band is mechanically floored by the index leg.** With **0 of 5** index ETFs above their own 20-DMA the index side of the spread is zero, so +44.15 pp is what "44.15% of large caps above their 20-DMA against 0% of the index ETFs" produces. It measures how far the trend structure lags the index, not a disagreement between two sources.
- **QQQE is too thin to read as the equal-weight Nasdaq.** Its volume was 224,978 shares against QQQ's 34,995,978 — a factor of 156. Its +2.42% is not the same signal as QQQ's; the equal-weight read in this document is RSP and IWM.
- **No advance/decline figure is published for 2026-11-27.** Every advancing/declining number in this artifact is the **settled 2026-11-25** count (670 / 204 / 7). The participation for 2026-11-27 is not computed here; the tape section reports index, sector and single-name prints only.
- **The universe moved again: 881 names**, against 875 on the 2026-11-24 settled session. The filter is unchanged (NYSE/NASDAQ/AMEX, market cap > $10B); the count moves because the market-cap floor is applied to the latest `valuation` row. The drift is disclosed, not smoothed away.
- **The volatility pair is one feed's fallback, not the venue's print.** The Cboe delayed-quote CDN answered HTTP 403 (Cloudflare) for every User-Agent from this egress — the one degraded source of this run. The pair comes from Yahoo's chart API with both symbols read from the same 5-minute bar, and it is used everywhere in this document.
- **NVDA's session range is far wider than its close.** It traded -2.62% low and closed +0.80%, so the published change understates the intraday fight; the same name that rallied 31% on Monday's Huang reinstatement is now the laggard of a chip rally.

## Method, source health & caveats

### Method

- **Two layers, never blended.** The breadth, advance/decline, percentile and index-positioning layers describe the **settled 2026-11-25** session from shibui (T+1, and 2026-11-26 was Thanksgiving, so the newest ingested session is two sessions behind the 14:00:03 ET fire on 2026-11-27). The tape and the volatility pair are the **settled 2026-11-27 close** — the 13:00 ET early close. The front matter carries both dates (`data_date` / `live_date`) and no number in this artifact mixes the two.
- **The universe is the contract's, not a new one:** NYSE/NASDAQ/AMEX, market cap > $10B taken from the latest `valuation` row, **881 names**. It is not frozen — the count moves as valuation rows refresh (875 on the 2026-11-24 session, 881 on 2026-11-25). The advance/decline tally uses the **same** indicator-joined population as the breadth percentage, so 670 + 204 + 7 = 881, the published universe count.
- **Percentile windows.** The level percentiles are ranks against the trailing 261-session distribution of the same series (2025-11-12 → 2026-11-25); the ADL window is 60 sessions and the ADL is cumulative from **2026-09-01** (a level, currently **-828**), with the published slope (**-172.71 net advances per session**) as the rate over 10 sessions.
- **`atr_extensions` is non-empty** — all five index ETFs are carried, read from the `ticker` key the SQL actually emits, so `late_cycle` is computable rather than vacuously false. Every one of the five is *below* its own 50-DMA (QQQ -10.34%, QQQE -6.42%, SPY -5.43%, IWM -2.99%; only RSP is marginally above at +0.43%), so `late_cycle` is genuinely false today.
- **One number per field, one source per field.** Prices and the tape come from the bridge's `market-recap` (cross-checked inside the call against a second quote source); the breadth, A/D and index-ETF rows come from shibui; the volatility pair comes from Yahoo's chart API. Where two feeds could serve the same field, one was chosen and named here.

### Source health

| Source | What it served | Status |
|---|---|---|
| shibui `stock_data_query` over the MCP-over-HTTP bridge | the settled breadth series, the A/D tally, the index-ETF positioning (newest ingested session **2026-11-25**, T+1 plus the Thanksgiving holiday) | **ok** (lag disclosed, not blended) |
| bridge `market-recap` `get_quotes` | the tape — 17 instruments (17/17 `agrees` against a second quote source) and the index/single-name pull (10/10 `agrees`) | **ok** |
| bridge `market-recap` `market_snapshot` | the cross-asset block (Asia, Europe, futures, yields, FX, commodities, crypto) | **ok** |
| Yahoo chart API (`^VIX` / `^VIX3M`) | the volatility pair, both symbols from the same 5-minute bar stamped 2026-11-27 13:00:00 ET | **ok** — *fallback* |
| Cboe delayed-quote CDN | the primary volatility source | **failed: HTTP 403 (Cloudflare)** — the Yahoo fallback served the pair |
| web search (Investopedia, Reuters, Yahoo Finance, Investing.com) | the day's catalysts only — the AI/semiconductor rebound, the holiday-shortened close, the weekly gain; no published number comes from it | **ok** |

**Degraded sources: 1** — the Cboe delayed-quote CDN (HTTP 403). The volatility pair was published from the Yahoo fallback instead, and the `source` string in `_regime-intraday.json` names it.

### MCP availability probe

`catalog_ok total=138 finance_tools=0` — no finance MCP is registered on this runtime, so the MCP-over-HTTP bridge is the data path. The absent `mcp__*` tools are **not** an error and are not counted in the degraded-source tally.

### What happened on the tape (context, not a published number)

- **The AI complex rebounded hard.** Semiconductor stocks returned to favour as concerns about AI profitability eased after a bruising November: MU **+7.60%**, AMD **+4.56%**, AVGO **+3.82%**, TSM **+3.21%**, SMH **+4.17%**, with SanDisk, Intel and Marvell also up sharply in the tape. Micron had shed nearly 40% over the prior month on memory-chip oversupply and weakening NAND prices and was treated as a buy-the-dip candidate.
- **Nvidia was the outlier inside the complex**, closing +0.80% after a -2.62% intraday low, having fallen 5.86% on Tuesday and 3.9% on Wednesday — the name that drove Monday's historic rally on Jensen Huang's reinstatement as CEO was the laggard of Friday's chip rally.
- **The week was the story.** The S&P 500 gained roughly 4% on the week, its best week since April, the Nasdaq its best since August and the Dow its strongest since April 2025 — after the S&P's seven-session losing streak (the longest since February 2020) took it into correction territory, and Monday's rebound on the Huang news.
- **Holiday-week mechanics.** Markets were closed Thursday 26 November for Thanksgiving and closed early on Friday 27 November at 13:00 ET; no major earnings or economic releases were on Friday's calendar. Friday's close therefore sets the benchmark ahead of next week's month-end rebalancing, the MSCI index review, the US employment report and the December FOMC meeting.
