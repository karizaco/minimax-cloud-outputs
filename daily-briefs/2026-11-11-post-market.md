---
date: 2026-11-11
cron: 23-agentic-post-market-brief
contract: postmkt-artifact-v2
fire_time_et: 22:30
snapshot_et: 22:35-22:50
session: 462444119859609
scheduled_at_ms: 1794454218848
status: ok
source: MCP bridge market-recap (get_quotes, price_history); TradingView /america/scan (postmarket_* columns); cron #20 us-eod/2026-11-11.csv; CBOE daily statistics + dated VIX/VXN close files; web_search
primary_source: MCP bridge market-recap for closes and history (keyless, Yahoo-sourced); TradingView scanner for the after-hours session
universe: cron #20 us-eod 2026-11-11.csv — 4,891 names (common stocks); liquid set = market_cap >= $2B = 1,822 names
degraded_sources: 2
---

# Post-market brief — Wednesday, 11 November 2026

## TL;DR

AI infrastructure led a broad, risk-on session — the S&P 500 closed **+1.31% at 7,619.38**, the Nasdaq **+1.60%**, the Dow **+0.49%** — and the participation was better than the headline index, not worse: **2,691 advancers against 1,955 decliners**, a **median_name_move_pct of +0.19%**, and a **liquid_adv_dec_ratio of 1.45** across the 1,822 names above $2B say the tape was broad. The counterweight is that **cap_weight_penalty_bp is +52** (SPY +1.32% versus RSP +0.80%), so the megacaps still did the heavy lifting on a day when semiconductors were the story (SOXX +6.01%, SMH +4.82%). **The caveat that matters most came after the bell:** a report that Nvidia's board was preparing to consider its chief executive's future knocked NVDA **-8.61% to 158.78** in extended trading, and the overnight futures are red (ES -0.34%, NQ -0.82%). Tomorrow is a two-print setup: jobless claims and existing home sales at 08:30 and 10:00 ET, then Cisco and Applied Materials after the close.

## Tomorrow's setup — Thursday, 12 November 2026

### Futures and the overnight setup

Live Globex prints, `as_of` 22:25 ET — five minutes before the fire. These are the **overnight** session, not the 16:00 ET cash settlement, so they already carry the Nvidia after-hours break.

| Contract | Last | Chg | Session high | Session low | vs prior settlement |
|---|---|---|---|---|---|
| ES=F (S&P 500 Dec 26) | 7,614.50 | -0.34% | 7,628.00 | 7,600.50 | -26.00 (-0.34%) |
| NQ=F (Nasdaq 100 Dec 26) | 28,238.75 | -0.82% | 28,368.50 | 28,131.75 | -234.50 (-0.82%) |
| YM=F (Dow Dec 26) | 52,656 | +0.15% | 52,692 | 52,527 | +78 (+0.15%) |
| RTY=F (Russell 2000 Dec 26) | 2,856.60 | +0.10% | 2,858.80 | 2,844.00 | +2.90 (+0.10%) |
| ZN=F (10-Year T-Note Dec 26) | 106.17188 | +0.13% | 106.29688 | 106.09375 | +0.1406 (+0.13%) |

The curve is telling one story: the Nasdaq 100 is carrying the overnight risk (-0.82%) while the Dow and small caps are flat-to-green. That is a single-stock event, not a market-wide de-risking. Note for context: **11 November was Veterans Day and the US bond market was closed**, so today's cash rate moves are thin and tomorrow's 30-year auction (13:00 ET) is the first real coupon event of the week.

### Economic calendar

| Time (ET) | Release | Consensus | Previous |
|---|---|---|---|
| 08:30 | Initial jobless claims (Nov 7) | 195K | 189K |
| 08:30 | Continuing jobless claims (Oct 31) | 1,710K | 1,718K |
| 08:30 | Jobless claims 4-week average | 192.5K | 194.75K |
| 09:00 | Fed's Hammack speaks | — | — |
| 10:00 | Existing home sales (Oct) | 3.85M | 3.99M |
| 10:00 | Fed's Barr speaks | — | — |
| 11:00 | EIA petroleum status report | distillates -1.0M | -3.565M |
| 11:15 | Fed's Goolsbee speaks | — | — |
| 13:00 | 30-year Treasury auction | 5.618% (Nov 10) | — |
| 13:10 / 13:30 | Fed's Daly and Schmid speak | — | — |
| 18:30 | Fed's Williams speaks | — | — |

Friday 13 November carries the US PPI release at 08:30 ET, so a soft claims print tomorrow gets amplified into a rate story on Friday.

### Earnings calendar

430 companies are scheduled to report on 12 November (340 before the open, 77 after the close). The large US names:

| Ticker | Timing | Consensus EPS | Options-implied move | Prior close |
|---|---|---|---|---|
| CSCO (Cisco, FQ1 FY27) | after the close (call 16:30 ET) | ~$1.35 | ±8.8% | 100.76 |
| AMAT (Applied Materials, FQ4) | after the close | ~$4.06–4.13 | ±7.9% | 395.08 |
| NBIS (Nebius) | before the open | n/a | n/a | not quoted in this brief |

Cisco confirmed the timing itself on 3 November (results released after Thursday's close, call at 4:30 PM ET). Nebius is the second neocloud name in two days and the direct read-through on CoreWeave's guidance. **No watchlist name reports tomorrow** — the watchlist's earnings risk is NVDA on 17 November.

### News to watch for the top movers

- **CRWV** — the day's driver: +24.71% to 60.77 on a Q3 beat and raised guidance, then **-6.37% in extended trading** to 56.90. The after-hours print is genuinely contested between vendors (Public showed -2.37% at 17:30 ET, MarketBeat -7.12% at 18:10 ET, the scanner -6.37%): a thin, moving tape, not a settled price.
- **NVDA** — the after-hours break: the Wall Street Journal reported the board was preparing to consider removing its chief executive, and the New York Times reported a separate relationship allegation. NVDA fell 8%+ in extended trading after rallying 2.92% in the regular session. The company had said only that an independent investigation was under way.
- **AZTA** — Q4 revenue $167M, +5% year on year, above the outlook; FY27 guidance $648–660M with a 200–250bp adjusted EBITDA margin expansion. Stock +20.80% to 48.90.
- **AXTI** — +19.49% to 46.97 on record-revenue commentary, with no 8-K filed on 10–11 November to explain it. Treat the move as unexplained rather than earnings-driven.
- **AMD / MU / AVGO** — the semiconductor melt-up: AMD +7.32%, Micron +11.89% to 811.30, Broadcom +3.99%. The question for tomorrow is whether this complex holds once the Nvidia headline is fully priced.

### Tomorrow's three things to watch

- NVDA — 158.78 after-hours last, 156.20 after-hours low, 173.73 regular close — the board-ousting report, not earnings, is what broke it; the next prints are the company's response and the 17 November report (options price ±9.5%).
- CSCO — 100.76 close — reports after tomorrow's close with a ~$1.35 consensus and a ±8.8% implied move; AI-network order commentary is the tell.
- AMAT — 395.08 close, up 6.05% today on the chip rally — reports after tomorrow's close with a ~$4.06 consensus and a ±7.9% implied move; the wafer-fab guide follows the melt-up it just rode.

## Day's tape

### Market read

| Metric | Value | Source |
|---|---|---|
| advancers | 2,691 | cron #20 us-eod/2026-11-11.csv |
| decliners | 1,955 | cron #20 us-eod/2026-11-11.csv |
| unchanged | 168 | cron #20 us-eod/2026-11-11.csv |
| median_name_move_pct | +0.19% | cron #20 us-eod/2026-11-11.csv |
| cap_weight_penalty_bp | +52 | bridge price_history (SPY +1.32% − RSP +0.80%) |
| liquid_adv_dec_ratio | 1.45 (1,058 adv / 730 dec, 34 flat) | cron #20 us-eod, market_cap >= $2B (1,822 names) |

The index was green and the median stock was green too — that is the difference from the narrow tapes of early November. The cap-weight penalty is still positive at +52bp, but the five-session average is **-11bp**, so today's flip is a change of direction rather than a continuation.

### Cap-weight penalty — 5-day history

| Session | SPY % | RSP % | cap_weight_penalty_bp |
|---|---|---|---|
| 2026-11-05 | -4.41 | -2.89 | -152 |
| 2026-11-06 | +0.31 | -0.38 | +69 |
| 2026-11-09 | +2.37 | +2.27 | +10 |
| 2026-11-10 | -0.37 | -0.03 | -34 |
| 2026-11-11 | +1.32 | +0.80 | +52 |

### Index, ETF and volatility levels

| Instrument | Close | Change | Day range | as_of (ET) |
|---|---|---|---|---|
| S&P 500 | 7,619.38 | +1.31% | 7,571.88 – 7,647.20 | 16:42 |
| Nasdaq Composite | 25,466.19 | +1.60% | 25,326.69 – 25,649.85 | 17:15 |
| Dow Jones | 52,486.49 | +0.49% | 52,055.14 – 52,512.72 | 16:43 |
| Russell 2000 | 2,846.26 | +0.88% | 2,832.42 – 2,852.14 | 16:30 |
| Nasdaq 100 | 28,374.25 | +2.28% | 28,102.75 – 28,593.52 | 17:15 |
| PHLX Semiconductor | 10,564.11 | +5.66% | 10,287.32 – 10,787.06 | 17:15 |
| VIX | 17.49 | -10.12% | 17.33 – 18.96 | 16:15 |
| VXN | 26.74 | -6.41% | 26.24 – 27.55 | 16:15 |
| SPY | 759.81 | +1.32% | 754.91 – 762.51 | 16:00 |
| QQQ | 690.38 | +2.31% | 683.60 – 695.57 | 16:00 |
| IWM | 283.09 | +0.89% | 281.49 – 283.72 | 16:00 |
| DIA | 524.44 | +0.52% | 520.07 – 524.63 | 16:00 |
| RSP | 222.65 | +0.80% | 220.92 – 222.82 | 16:00 |
| SMH | 506.96 | +4.82% | 496.01 – 516.65 | 16:00 |
| SOXX | 155.40 | +6.01% | n/a | 16:00 |
| GLD | 365.17 | -1.13% | 364.89 – 369.38 | 16:00 |
| TLT | 80.92 | +0.05% | 80.47 – 80.96 | 16:00 |

Volatility was repriced hard: VIX -10.12% to 17.49 and VXN -6.41% to 26.74, both dated to the 11 November session and both cross-checked to Cboe's own dated close files (identical to the cent).

### Cross-asset

Gold fell 1.13% to 365.17 and the 20-year bond ETF was flat (+0.05%, 80.92) — with the bond market closed for Veterans Day, that is a thin read on rates. Equities, not duration, carried the session.

### Day's movers

Regular session, $1B+ market cap, de-duplicated on the cap-carrying parent (cron #20 universe, closes confirmed against the bridge).

| Ticker | Close | Change | Day range | Volume |
|---|---|---|---|---|
| CRWV | 60.77 | +24.71% | 53.81 – 62.03 | 158,080,488 |
| DJT | 5.19 | +21.26% | 4.40 – 5.48 | 16,888,180 |
| AZTA | 48.90 | +20.80% | 43.67 – 50.06 | 2,485,615 |
| AXTI | 46.97 | +19.49% | 42.84 – 49.04 | 14,719,564 |
| REZI | 23.00 | +18.25% | 19.51 – 23.00 | 7,491,771 |
| AADX | 9.30 | -13.25% | 9.11 – 10.27 | 4,560,960 |
| RGTI | 11.11 | -8.56% | 11.07 – 12.93 | 32,674,202 |
| MIR | 17.70 | -8.10% | 17.22 – 18.63 | 9,130,666 |
| ZYME | 29.07 | -7.60% | 28.92 – 31.94 | 898,576 |
| TTEK | 37.61 | -7.48% | 37.08 – 40.33 | 11,836,358 |

### Watchlist EOD review

| Ticker | Close | Day change | Day range | Volume | Volume vs 30d avg | After-hours print |
|---|---|---|---|---|---|---|
| AAPL | 355.63 | +2.04% | 349.33 – 355.90 | 34.02M | 0.73× | 356.35 (+0.20%), 355.11 – 357.70 |
| MSFT | 521.13 | -2.26% | 518.45 – 534.76 | 28.57M | 1.16× | 520.50 (-0.12%), 519.25 – 523.50 |
| NVDA | 173.73 | +2.92% | 170.77 – 177.54 | 281.51M | 1.94× | 158.78 (-8.61%), 156.20 – 174.76 |
| GOOGL | 293.45 | +2.11% | 289.48 – 295.74 | 24.97M | 0.70× | 294.35 (+0.31%), 290.50 – 297.20 |
| AMZN | 266.17 | -1.74% | 265.62 – 274.87 | 37.22M | 0.82× | 267.30 (+0.42%), 264.60 – 269.00 |
| IWM | 283.09 | +0.89% | 281.49 – 283.72 | 17.37M | n/a | 282.43 (-0.23%), 282.22 – 283.30 |
| GLD | 365.17 | -1.13% | 364.89 – 369.38 | 5.74M | n/a | 365.88 (+0.19%), 363.66 – 366.00 |
| TLT | 80.92 | +0.05% | 80.47 – 80.96 | 26.43M | n/a | 80.87 (-0.06%), 80.82 – 81.06 |

Closes and volumes are the bridge's; the volume ratio is cron #20's `rel_volume` for the five common-stock names. The three funds have no row in that universe (it covers common stocks only), so their volume-versus-average is not published.

## Sector rotation

Cap-weighted sector returns, one row per `cap_source_symbol`, carrier rows dropped, `NO_CAP` rows excluded from the weighting, `NO_SECTOR` rows excluded from the ranking; each row cross-checked against its sector ETF.

| Sector | Cap-weighted % | Median name % | Sector ETF | ETF % | Gap (pp) |
|---|---|---|---|---|---|
| Information Technology | +2.94 | +2.18 | XLK | +3.23 | -0.29 |
| Energy | +1.91 | +2.34 | XLE | +1.86 | +0.05 |
| Communication Services | +0.98 | +1.10 | XLC | +0.78 | +0.20 |
| … | | | | | |
| Health Care | +0.20 | +0.54 | XLV | +0.04 | +0.16 |
| Real Estate | -0.03 | -0.24 | XLRE | +0.02 | -0.05 |
| Consumer Discretionary | -0.15 | -0.04 | XLY | -0.05 | -0.10 |

Every cap-weighted sector return sits inside ±20%, so no arithmetic bug is hiding in the column, and **no sector's gap against its ETF exceeds 0.5pp** — the rotation is broad, not a single-name effect. That is the day's most useful rotation fact: technology led on the chip melt-up (IT +2.94%, median +2.18%), energy's median (+2.34%) actually beat its cap-weighted return (+1.91%), and the three laggards were all within a quarter of a percent of flat. Health Care is the mild laggard in cap-weighted terms yet its median was +0.54% — the megacap healthcare names carried it down.

## After-hours movers

The screen is the contract's screen: US stocks above $1B of market cap with more than 50,000 after-hours shares, ranked by absolute after-hours change, five gainers and five losers, every row carrying the full level set. `gap_fill_level` follows the deterministic rule: the 16:00 close when the after-hours range straddles it, otherwise the after-hours midpoint.

| ticker | prior_close | ah_last | ah_high | ah_low | ah_volume | gap_pct | ah_range_pct | gap_fill_level |
|---|---|---|---|---|---|---|---|---|
| AVEX | 12.13 | 13.50 | 14.43 | 11.76 | 591,199 | +11.29% | 22.01% | 12.13 |
| TTEK | 37.61 | 40.80 | 42.74 | 37.30 | 1,709,056 | +8.48% | 14.46% | 37.61 |
| VERX | 17.83 | 18.73 | 18.73 | 17.83 | 183,188 | +5.05% | 5.05% | 17.83 |
| AMD | 552.90 | 576.80 | 584.00 | 552.00 | 5,274,967 | +4.32% | 5.79% | 552.90 |
| INGM | 28.00 | 29.08 | 29.60 | 28.00 | 285,674 | +3.86% | 5.71% | 28.00 |
| DGII | 66.96 | 57.00 | 67.50 | 55.40 | 208,709 | -14.87% | 18.07% | 66.96 |
| NVDA | 173.73 | 158.78 | 174.76 | 156.20 | 74,786,061 | -8.61% | 10.68% | 173.73 |
| CTVA | 12.14 | 11.17 | 12.28 | 11.13 | 3,287,803 | -8.02% | 9.47% | 12.14 |
| CRWV | 60.77 | 56.90 | 61.87 | 55.67 | 13,804,362 | -6.37% | 10.20% | 60.77 |
| ALVO | 4.92 | 4.62 | 4.92 | 4.501 | 105,030 | -6.10% | 8.51% | 4.92 |

**The table is not the whole after-hours tape — the screen has a $1B floor.** On the same screen with the floor removed, the leaders were PLCE +257.63% (close 0.1985, after-hours 0.7099), POAS +105.40%, ADXN +95.50%, ICMB +53.54% and SOS +31.64%; on the downside WHLR -25.48%, RKDA -24.31%, INLF -22.40%, OPRX -20.11% and YMT -18.19%. All are sub-$20M market caps. Every row in the table passed the self-check `postmarket_change == (postmarket_close − close) / close × 100`; no row was dropped for failing it. No catalyst was sourced for VERX or INGM, and none is claimed.

## After-hours earnings reactions

| Ticker | Reported | Consensus EPS | Result | After-hours reaction |
|---|---|---|---|---|
| TTEK | Q4 FY26, after the close | ~$0.47 | adjusted EPS $0.49 (beat 4.6%), revenue $1.34B (beat 16.4% vs ~$1.17B) | +8.48% to 40.80 |
| AVEX | AEVEX Q3 FY26, after the close | $0.08 (revenue $152.4M) | not verified in this run | +11.29% to 13.50 |
| DGII | Q4 FY26, after the close (4:00 PM ET, call 5:00 PM ET) | $0.76–0.78 | not verified in this run | -14.87% to 57.00 |
| CTVA | Q3, after the close | $0.10 (revenue $1.80B) | not verified in this run | -8.02% to 11.17 |
| ALVO | Q3, after the close | n/a | not verified in this run | -6.10% to 4.62 |
| CRWV | Q3, before the open — beat and raised guidance | n/a | beat, guidance raised | +24.71% in the session, then -6.37% to 56.90 |

Tetra Tech is the clean reaction of the night: it fell 7.48% in the regular session and then beat on both lines after the close and jumped 8.48% in extended trading. **DGII and CTVA are the two I could not verify a result for** — the reaction is published, the numbers are not, because this run did not open the press releases.

## Open research queue

1. **Is the after-hours Nvidia break a governance event or an AI-demand signal?** It matters because NVDA is the largest single weight in the index and options price ±9.5% for the 17 November report; if the break is governance-only it should not spread into the semiconductor complex, and if it is demand-related the whole AI cap-weight complex is mispriced. What would resolve it: the company's own statement, the 18 November House briefing, and whether SOXX/SMH hold the 11 November gains overnight.
2. **Did CoreWeave's result lift the AI-infrastructure complex, or only the top of it?** It matters because CRWV's +24.71% single-handedly distorts the cap-weighted Information Technology number (+2.94% against a +2.18% median), so the sector read is only as good as its breadth. What would resolve it: Nebius's pre-open print on 12 November, and whether CRWV holds above its 60.77 regular close after the -6.37% after-hours fade.
3. **Is the participation real or a one-day artefact?** It matters because today's 2,691 advancers against 1,955 decliners and +52bp cap-weight penalty came after a five-session average of -11bp — the direction of the breadth metric just flipped. What would resolve it: the next three sessions of RSP versus SPY and the daily adv/dec split in cron #20's published CSV.

## Source health

| Source | Endpoint / query | Status |
|---|---|---|
| MCP bridge, market-recap | `get_quotes` (indices, ETFs, futures, movers), `price_history` (SPY, RSP, ^VIX, ^VXN) | ok — 8 calls, no rate limit; all index rows carried `as_of` 2026-11-11 |
| TradingView scanner | `POST scanner.tradingview.com/america/scan`, `postmarket_*` columns | ok — 400 rows per direction; 0 rows failed the change identity |
| Cron #20 EOD universe | `minimax-cloud-outputs` `us-eod/2026-11-11.csv` | ok — 4,891 names |
| CBOE daily statistics | `cboe.com/us/options/market_statistics/daily/` | ok — payload `selectedDate` 2026-11-11; total put/call 0.92 |
| CBOE dated index closes | `cdn.cboe.com/.../VIX_History.csv`, `VXN_History.csv` | ok — VIX 17.49, VXN 26.74, identical to the bridge |
| Watchlist | `minimax-cloud-outputs` `refs/watchlist.yaml` | ok — 8 names, published 2026-11-06 |
| MCP availability probe | `_shared/probe_mcp.py` | ok — `catalog_ok total=135 finance_tools=0`, bridge reachable |
| Sub-$1B after-hours leaderboard | TradingView screen with the market-cap floor removed | **degraded — partial**: 400 of 2,950 names pulled in each direction, not paged to the end; the leaders quoted are the extremes of the pulled window |
| Watchlist volume-versus-average for IWM, GLD, TLT | cron #20 EOD universe | **degraded — coverage**: that universe is common stocks only, so the three funds have no volume average and their closes rest on the bridge alone |

Every index, ETF and volatility row in this brief carries `as_of` 2026-11-11, so no prior-session row was published as today's. The futures rows are dated 22:25 ET — the live overnight session, not a stale settlement. `degraded_sources: 2`.

## Method notes

- **Participation population**: cron #20's `us-eod/2026-11-11.csv` — 4,891 names, one population for advancers, decliners, unchanged, the median name move and the liquid adv/dec ratio. The liquid set is `market_cap >= $2B` (1,822 names); 34 of them closed flat.
- **Cap-weight penalty**: `(SPY daily_return_pct − RSP daily_return_pct) × 100`, both from one bridge `price_history` call, rounded to the nearest basis point. Signed: positive = the cap-weighted index outperformed the equal-weight index.
- **Sector weighting**: one row per `cap_source_symbol`; the 294 `CAP_CARRIED` carrier rows were dropped in favour of the primary listing; 157 `NO_CAP` rows were excluded from every cap-weighted column and from the denominator; 370 `NO_SECTOR` rows were excluded from the sector ranking (they are a bucket, not a sector); 18 `EX_DISTRIBUTION` rows were dropped. Medians use the full sector population including rows without a cap.
- **Volatility indices** were read from the bridge's dated `price_history` and cross-checked against Cboe's own dated close files; both agree to the cent on VIX 17.49 and VXN 26.74 for 11 November.
- **After-hours identity**: every published row satisfies `postmarket_change == (postmarket_close − close) / close × 100` within 0.06pp. `gap_fill_level` is the prior close when the after-hours range straddles it, otherwise the after-hours midpoint. No row was published with an unread field — missing values would read `n/a`.
- **After-hours prints are moving.** They are as of roughly 22:35 ET and vendors disagree materially on thin names (CRWV: -2.37% at 17:30 ET, -7.12% at 18:10 ET, -6.37% on the scanner). The scanner is the published source of record.
- **Put/call**: the CBOE payload for `selectedDate` 2026-11-11 carries total **0.92**, index 1.05, equity 0.59, exchange-traded products 1.13, SPX+SPXW+SPXO 1.08 and XSP 1.29 — all from the same object and reconciling with the total, so the split is published as sourced.
- **Read-only**: no trades placed, no positions sized.
