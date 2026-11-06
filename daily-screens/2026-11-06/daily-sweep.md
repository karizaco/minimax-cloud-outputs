# Daily screener sweep — 2026-11-06 (end-of-day, 18:30 ET)

**Cron #09 · stock-screener-daily-sweep-18:30 · fired 2026-11-06 18:30:58 ET · read from the settled regular-session close.**

## Headline

Friday was a **duration rally inside a rising-rate tape**, not a risk-on session. The October jobs report printed **+165,000 payrolls** against roughly 59,000–70,000 expected with unemployment down to **4.1%**, which put a **December Fed hike back at ~75–85% odds** and pushed the 10-year back above 4.87%. The market bought the long-duration end of it: **QQQ +1.40%**, **SMH +3.62%**, **SOXX +3.51%**, **NDX +1.35%**, **SPX +0.31%** — while the equal-weight **RSP fell -0.38%** and the Dow proxy **DIA -0.40%**. Breadth says the same thing in one number: **57.26%** of the 986-name $10B+ universe closed above its 20-DMA, **425 advancers against 549 decliners**, median **-0.23%** — and **0 of the 5** index ETFs are above their 20-DMA. The divergence is **+57.26 pp (BROAD)**, the widest of this series and the fourth straight session in which the cap-weighted index is below its 20-day mean while the broad universe is not. The screen itself is one session behind: shibui's newest settled session at fire time was **2026-11-05**, so every screen metric below describes the 2026-11-05 tape while every "today" figure is the 2026-11-06 settled close.

## The day

| Index | Close | Day | vs 20-DMA | vs 50-DMA |
|---|---|---|---|---|
| SPY | 735.29 | **+0.31%** | 763.36 (below) | 765.68 |
| RSP | 216.05 | **-0.38%** | 216.72 (below) | 214.78 |
| QQQ | 656.10 | **+1.40%** | 707.64 (below) | 720.97 |
| QQQE | 112.01 | **+0.44%** | 117.63 (below) | 119.14 |
| IWM | 273.67 | **+0.99%** | 276.84 (below) | 282.11 |
| DIA | 512.22 | -0.40% | — | — |

**VIX 25.64 / VIX3M 24.6 (Cboe, both stamped 16:15:01 ET) — ratio 1.0423.** One pair, used everywhere; no second volatility reading appears in this document. The VIX fell 9.01% on the day but the ratio stayed **above 1.0**, so the `uncertainty` flag holds for a second session: front-end stress still exceeds the long end. The pair was pulled twice and both pulls were identical.

Breadth, full detail in `breadth.md`: 986-name universe (NYSE/NASDAQ/AMEX, type=stock, cap > $10B), 57.26% above 20-DMA, 48.68% above 50-DMA, 46.94% above 200-DMA, 425 advancers vs 549 decliners, median change -0.23%.

## Regime

`size_cut_pct = 0` · `uncertainty = true` · `late_cycle = false`

The size-cut rule needs the index below its 20-DMA **and** breadth under 40%. The first condition is met (0% of index ETFs above 20-DMA), the second is not (57.26%) — so the regime stays neutral on size even though the divergence is at its widest. `uncertainty` remains true on the VIX/VIX3M inversion. `late_cycle` is false, but for the wrong reason: every index ETF is *below* its 50-DMA (QQQ -9.00%), which is the opposite of the extension case the flag was designed to catch.

## Leadership

| Theme | Evidence | Read |
|---|---|---|
| AI semis (rebound) | SMH **+3.62%**, SOXX **+3.51%**, XLK +1.45%; Electronic Technology median day **+2.66%** but only **23.3%** above 20-DMA and 1M RS **-17.1%** | a relief bounce inside a broken structure, not a repair |
| AI cloud / neoclouds | IREN +20.02%, CIFR +17.93%, CRWV +6.28%, NBIS +7.58%, AMD +11.04%, MU +5.12%, INTC +7.71% | the day's real leadership, and it is a *funding* story: IREN's "fully contracted and fully funded" language relit the group |
| Ad-tech (two-day) | APP +9.86% (after +31.04% Thursday), U +5.51%, XERS +16.21% | the earnings complex that led the whole move |
| Defensive | XLV -0.06%, XLP -1.28%, XLU -0.39%, XLE -0.02%; Health Services 75.0% above 20-DMA, Consumer Non-Durables 85.3% | did not participate in the bounce — the rates move took them out of favour |
| Damaged and unsold | Energy Minerals only **4.3%** above 20-DMA (unchanged from 11-04), 1M RS -2.3%; Producer Manufacturing 30.0% above 20-DMA | the two sectors with no bounce at all |
| Rate-sensitive corner | DIA -0.40%, RSP -0.38%, GLD -0.79%, TLT -0.01% | the October jobs print took the other side of the trade |
| Software vs hardware | IGV -0.13% vs SOXX +3.51% | the split inside "technology" is still hardware vs software, now with software lagging on the up day too |

## Movers with a sourced catalyst

| Symbol | Day | Catalyst (source) |
|---|---|---|
| KRMN | **+42.13%** | Q3 FY26 record: revenue $202M (+66% y/y), adj EBITDA $61M (+60%), adj EPS $0.19 (≈2× y/y), backlog $1.7B (more than doubled); FY26 revenue guidance raised to $755–760M and adj EBITDA to $225–227M; a second $218M THAAD long-term agreement with Lockheed Martin ([Q3 call transcript](https://finance.yahoo.com/markets/stocks/articles/karman-holdings-krmn-q3-2026-061343531.html), [Benzinga](https://www.benzinga.com/trading-ideas/movers/26/11/62988477/moderna-jfrog-transmedics-ubiquiti-and-other-big-stocks-moving-higher-on-friday)) |
| FLY | **+36.80%** | A **$1.3 billion agreement with AST SpaceMobile** to supply rocket engines and license its propulsion technology ([Morningstar market movers](https://www.morningstar.com/markets)) |
| FROG | **+35.33%** | Q3 revenue $179.2M (+31%) vs $165.9M est., adj EPS $0.32 vs $0.23; cloud revenue $101.5M (+60%, 57% of sales); Q4 guide $183–185M vs $167.9M; FY26 revenue raised to $680–682M and adj EPS to $1.14–1.16; NDR 124% ([Benzinga](https://www.benzinga.com/trading-ideas/movers/26/11/62975075/jfrog-cloud-business-surges-as-ai-and-security-adoption-expand), [Investing.com](https://www.investing.com/news/stock-market-news/why-is-jfrog-stock-surging-today-93CH-5008231)) |
| LASR | **+29.58%** | Q3 revenue $73.8M (+10.5% y/y) and adj EBITDA $11.1M (+55.4% y/y) ([Morningstar market movers](https://www.morningstar.com/markets)) |
| QNT | **+25.99%** | FY26 revenue outlook raised to **$31–34M** from $28–32M on Q3 revenue of $9.1M, **+233% y/y** ([Morningstar market movers](https://www.morningstar.com/markets)) |
| TMDX | **+27.92%** | Q3 results released Nov 5 (8-K + 10-Q); no further detail sourced in this run ([Nexqual movers](https://nexqual.com/discover/movers)) |
| IREN | **+20.02%** | FQ1 FY27: revenue $228M vs ~$221M cons., **AI Cloud revenue $200M, nearly tripled** from $71M; adj EBITDA $66M (29% margin); net loss narrowed to $263M from $684M; the **>$4B annualised target is "fully contracted and fully funded"**, and a new 5-year contract carries 90% GPU prepayments ([Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/stock-market-today-nov-6-221801072.html), [24/7 Wall St](https://247wallst.com/investing/2026/11/06/cloudflare-soars-20-iren-surges-15-as-earnings-beats-spark-ai-cloud-rebound-coreweave-jumps-10/)) |
| CIFR | **+17.93%** | No news of its own — the IREN funding read-through. Cipher carries **$5.62B of debt against $660M of cash**, so the bounce is a relief move, not a funding event ([Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/cipher-digital-soars-5-rival-161048670.html)) |
| APP | **+9.86%** | The post-earnings rally extended: Q3 revenue $2.18B (+55.5%) vs $2.07B est., EPS $4.30 vs $4.03; Q4 guide $2.365–2.395B vs $2.25B est.; buyback lifted to $3.6B; BTIG $450, Needham $475, RBC $520 ([Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/applovin-jumps-8-post-earnings-180522619.html)) |
| U | **+5.51%** | Unity's first GAAP-profitable quarter since IPO: revenue $622.1M (+32%), Vector +126%, adj EBITDA $256.6M; Q4 strategic revenue guided $683–691M (+65–67%) ([Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/1-turnaround-stock-own-just-212601519.html)) |
| IRTC | **-30.70%** | Q3 results Nov 5 (8-K + 10-Q); Wells Fargo kept Overweight but cut its price target to $135 ([WeeklyTrader](https://weeklytrader.io/volume.php)) |
| DKNG | **-21.30%** | Q3 adj EPS **-$0.53 vs -$0.19 est**, revenue $1.33B vs $1.40B est; FY26 revenue guidance cut to $6.35–6.55B and **adj EBITDA guidance slashed to $175–275M from $700–900M** as Predictions investment rises to $650–700M ([Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/draftkings-plunges-cutting-outlook-etfs-185746807.html)) |
| AXON | **-18.18%** | Q3 EPS $1.72 vs $1.90 est, revenue $908.6M vs $931.1M est; **FY26 revenue guidance cut to $3.61–3.63B** (~30% growth) from 32–34% on three delayed federal Dedrone deals (~$130M); FCF guide trimmed to $350–400M from $450M; Taser revenue -2% y/y — its first decline; $1.2B Skydio investment takes the stake to 37% ([Zacks](https://finance.yahoo.com/technology/ai/articles/axon-q3-earnings-call-highlights-142100006.html), [Barrons](https://finance.yahoo.com/m/f618d712-0042-3c1b-b668-b3697989fba4/axon-stock-plunges-as-delayed.html)) |
| TEAM | **-16.15%** | FQ1 beat (adj EPS $1.65 vs $1.43, revenue $1.77B +24%) but **FY27 subscription ARR growth guided to ~18.5% from 23%**, total revenue growth ~13.75%, cloud growth moderating to ~26% and data-centre revenue to fall ~14%; Truist cut its target to $200 from $250 ([Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/atlassian-shares-fall-16-cautious-110846490.html)) |
| NTRA | **-14.59%** | Investor concern over a **sudden CEO change** ([Insider Monkey](https://www.insidermonkey.com/news/stock-market-movers-biggest-gainers-and-losers-on-6-november-2026-1862660/)) |
| MCHP | **-10.02%** | Q2 FY27 results Nov 5 with soft December guidance; the CEO said the **"data center is in the bubble"** ([Microchip IR](https://ir.microchip.com/news-events), [WeeklyTrader](https://weeklytrader.io/volume.php)) |
| AMN / BL | **-23.68% / -23.11%** | Q3 results released Nov 5 / Nov 6 (8-K + 10-Q) ([Nexqual movers](https://nexqual.com/discover/movers)) |

Other large moves (cap > $1B) with **no catalyst sourced in this run**: IONQ +23.42%, OKLO +22.66%, RGTI +19.29%, INFQ +19.49%, ONDS +18.03%, QBTS +18.01%, LEU +17.49%, SITM +17.44%, WOLF +16.85%, HALO -15.72%, WK -14.90%, GMED -12.76%, ASTH -11.56%.

## Tier-A — ≥ 3 distinct stylists (cap 8; pool was 12, list truncated)

| Symbol | Stylists | Close | Today | Cap | RVOL | Velocity | Origins |
|---|---|---|---|---|---|---|---|
| **RUN** | jeff_sun|peoplewish|qullamaggie|stockbee | 9.98 | +1.11% | $2.4B | 1.06 | 35.2 | A_stockbee_4pct, B_stockbee_ep9m, C_qullamaggie_rs, D_qullamaggie_ep, E_qullamaggie_5d_gainers, G_peoplewish, jeff_sun_canslim |
| **SEZL** | jeff_sun|peoplewish|qullamaggie|stockbee | 149.43 | -3.59% | $5.0B | 1.00 | 21.4 | A_stockbee_4pct, C_qullamaggie_rs, D_qullamaggie_ep, G_peoplewish, jeff_sun_canslim |
| **XERS** | hernandez|jeff_sun|qullamaggie|stockbee | 15.20 | +16.21% | $2.8B | 2.11 | — | A_stockbee_4pct, B_stockbee_ep9m, C_qullamaggie_rs, H_hernandez_theme, TV_volume_breakout |
| **ACHC** | hernandez|peoplewish|qullamaggie|stockbee | 37.00 | +6.35% | $3.4B | 1.55 | 16.0 | A_stockbee_4pct, D_qullamaggie_ep, G_peoplewish, H_hernandez_theme |
| **MRNA** | hernandez|peoplewish|qullamaggie|stockbee | 254.19 | +5.27% | $101.5B | 1.28 | 10.8 | B_stockbee_ep9m, C_qullamaggie_rs, G_peoplewish, H_hernandez_theme |
| **APP** | jeff_sun|qullamaggie|stockbee | 391.22 | +9.86% | $130.9B | 1.49 | — | A_stockbee_4pct, B_stockbee_ep9m, C_qullamaggie_rs, D_qullamaggie_ep, E_qullamaggie_5d_gainers, jeff_sun_canslim |
| **U** | peoplewish|qullamaggie|stockbee | 51.49 | +5.51% | $22.7B | 1.42 | 20.8 | A_stockbee_4pct, B_stockbee_ep9m, D_qullamaggie_ep, G_peoplewish |
| **FUN** | peoplewish|qullamaggie|stockbee | 10.00 | +8.23% | $1.0B | 1.61 | 13.9 | A_stockbee_4pct, B_stockbee_ep9m, D_qullamaggie_ep, G_peoplewish |

**The tier is a momentum list, and today it mostly worked.** 7 of the eight closed up — RUN +1.11%, XERS +16.21%, ACHC +6.35%, MRNA +5.27%, APP +9.86%, U +5.51%, FUN +8.23% — and the laggards are SEZL -3.59%. The screen's own metrics resolve to the **11-05** session, which is why APP (which rose 31.04% on 11-05) and XERS are already on the list: the tier is one session behind the move it is flagging, and today is that move's second leg. The read is not "buy" — it is that the screens were early on this move. Note the pool was **12 names with ≥3 stylists** and the list is truncated to 8; the four dropped names are published in `_results.json` under `tier_a_pool_members`.

## Focus — ≥ 2 distinct stylists (cap 12, ranked by stylists → origins → velocity)

RUN +1.11% (4) · SEZL -3.59% (4) · XERS +16.21% (4) · ACHC +6.35% (4) · MRNA +5.27% (4) · APP +9.86% (3) · U +5.51% (3) · FUN +8.23% (3) · JOBY +11.89% (3) · WRBY -2.30% (3) · VRDN -0.21% (3) · XNCR +4.99% (3)

9 of the twelve closed up. The most convergent names are the 5 with 4 stylists — **RUN, SEZL, XERS, ACHC, MRNA** — and they are split: XERS +16.21% and ACHC +6.35% against SEZL -3.59% (FY26 revenue growth guidance raised to ~42.5% from 35%, adjusted EPS to $5.45–5.50, on Nov 4). Treat the Focus list as a *watch* list: 9 of 12 are green, and the two reds (SEZL, WRBY) are both names with genuine company news this week.

## Parabolic short candidates — 5-session gain ≥ +25% (7)

APP 39.7% (today +9.86%) · CPRI 31.6% (today -2.79%) · FISV 29.4% (today +0.22%) · FMC 27.8% (today -7.25%) · GPK 31.0% (today -3.03%) · GRAB 26.1% (today -2.01%) · RUN 30.0% (today +1.11%)

Only **3 of 7** rose again today, and the book is thin — 7 names on a tape where the median large cap fell. The names that rose (APP, XERS, U, FUN, JOBY) rose on their own earnings, not on extension, which is the opposite of what this screen wants to short.

## Parabolic long / mean-reversion candidates — 5-session loss ≤ -25% (92)

AAOI -40.8% (today +6.91%) · AAON -27.7% (today +5.09%) · AGX -26.8% (today +6.24%) · ALAB -38.2% (today +6.26%) · AMD -28.6% (today +11.04%) · AMKR -26.0% (today +7.64%) · APLD -27.0% (today +9.74%) · ARM -27.1% (today n/a%) · ASTS -29.9% (today +7.05%) · ASX -33.3% (today n/a%) · AXTI -39.7% (today +5.88%) · BTDR -29.9% (today +13.28%) · BTU -27.9% (today +0.06%) · CAI -28.0% (today -3.07%) · CAMT -27.4% (today +5.58%) · CBRS -29.0% (today +9.75%) · CIEN -34.0% (today +5.45%) · CIFR -31.5% (today +17.93%) · CLS -27.3% (today +0.51%) · CLSK -30.7% (today +8.45%) · COHR -28.4% (today +13.58%) · COHU -34.6% (today +10.29%) · CRDO -32.0% (today +7.28%) · CRWV -28.1% (today +6.28%) · CVI -29.9% (today -4.29%) · DDOG -34.3% (today +2.54%) … and 66 more in the artifact file.

**82 of 92 are higher today** — the first session in this series in which the oversold book actually produced follow-through, and the rebound names are the AI-cloud complex that got sold on Thursday (IREN +20.02%, CIFR +17.93%, AMD +11.04%, INTC +7.71%, MU +5.12%). The exception is that the *worst* names in the book are still falling: AXON -18.18%, TEAM -16.15%, MCHP -10.02%, DKNG -21.30%. The washout screen found a floor in the AI complex and did not find one in the guidance-cut names.

## Counts

| Set | Count |
|---|---|
| Unique candidates across 11 screen origins | 900 |
| Master (cap 200) | 200 |
| Stalk (Master within 2% of 10/20-DMA + a setup tag) | 2 |
| Focus (≥2 stylists, cap 12) | 12 |
| Tier-A (≥3 stylists, cap 8) | 8 (pool 12, truncated) |

Per stylist: stockbee 595, peoplewish 315, qullamaggie 160, hernandez 99, jeff_sun 41.
Screen origins: `B_stockbee_ep9m` 364, `G_peoplewish` 315, `K_stockbee_anticipation` 181, `H_hernandez_theme` 99, `F_qullamaggie_5d_losers` 92, `A_stockbee_4pct` 83, `C_qullamaggie_rs` 57, `jeff_sun_canslim` 27, `TV_volume_breakout` 14, `D_qullamaggie_ep` 12, `E_qullamaggie_5d_gainers` 7.

**Coverage assertion passed for every branch** (`rows_kept == rows_passing`, no branch landed on a 30/50/60/200 cap): A_stockbee_4pct 83/83, B_stockbee_ep9m 364/364, K_stockbee_anticipation 181/181, C_qullamaggie_rs 57/57, D_qullamaggie_ep 12/12, E_qullamaggie_5d_gainers 7/7, F_qullamaggie_5d_losers 92/92, G_peoplewish 315/315, jeff_sun_canslim 27/27, TV_volume_breakout 14/14, H_hernandez_theme 99/99.

**The Focus and Tier-A cap rule.** The skill caps Focus at 12 and Tier-A at 8 but does not define the ordering, so this run ranks by **stylists desc → origins desc → velocity desc** and publishes the rule in every file it touches. 240 names cleared the ≥2-stylist bar, so the 12-name Focus list is a ranked cut of a much larger set — `_results.json` carries the full candidate set.

## Source health

| Source | URL / query | Status | Used for |
|---|---|---|---|
| MCP availability probe | `probe_mcp.py` | `catalog_ok total=135 finance_tools=0` | confirms no finance MCP is registered; the bridge is the path |
| shibui (MCP bridge) | 18 `stock_data_query` SQL calls: 1 schema probe, resolve_date, 8 sweep branches (paged), breadth, 1-year breadth series, CANSLIM, 2 master-detail chunks | ok — every branch paged to `rows_passing` | screen metrics, T+1 breadth cross-check, percentile series, Stalk gate, skip flags |
| TradingView scanner | `POST https://scanner.tradingview.com/america/scan` — 2 calls (5,711 stocks + 6,751 funds, both complete against totalCount) | ok — no paging loss | settled close, SMA20/50/200, ATR, Perf 1M/3M/6M, sector, cap, RVOL |
| MCP bridge (`market-recap`) | `get_quotes` ×1 (36 index/ETF symbols), `top_movers` ×3 (gainers, losers, most-active) | ok — all 36 symbols found, `as_of` 21:00 UTC (16:00 ET), `market_state: post`; the most-active request echoed the gainers list, so most-active was ranked locally from TradingView volume | index/ETF closes, movers |
| Cboe delayed quotes | `cdn.cboe.com/api/global/delayed_quotes/quotes/{_VIX,_VIX3M,_SPX,_NDX,_RUT,_DJI}.json` | ok — VIX pair 16:15:01 ET (two pulls identical), indexes 16:14:59 / 16:09:55 ET; **`_DJI` stale at 2026-11-03** | VIX/VIX3M, index levels |
| Nasdaq `/info` | 12 Focus names | ok — 12/12 fetched; `secondaryData` (the 4:00 PM settle) agrees with the published close on **12 of 12** | third reading, confirmed |
| web_search | 11 catalyst/macro queries | ok | catalyst sourcing for the table above |
| Finviz | — | not attempted | Cloudflare 403 from this egress (known, documented) |
| Yahoo JSON | — | not used | — |

**errors: 0 source failures.** No source was rate-limited, timed out, or returned an unparseable body. Two data-quality flags are recorded rather than counted as failures (the stale `_DJI` print, and the Nasdaq after-hours `primaryData` field).

## Caveats and degradations

1. **Two data dates in one artifact, on purpose.** Screen metrics (chg %, RS, ADR, velocity, 5-day moves) are shibui's **2026-11-05** session; "today" columns are the **2026-11-06** settled close from TradingView/bridge. Columns are named `*_resolved` vs `today_*` in every CSV so the two can never be conflated.
2. **The close is verified on 12 names.** The bridge and TradingView agreed **to the cent on 12/12** Focus names, and Nasdaq's `secondaryData` — stamped "Closed at Nov 6, 2026 4:00 PM ET" — agreed on **12 of 12** as well. Nasdaq's `primaryData` is the 18:36 ET after-hours print (SEZL 152.00 vs the 149.43 settle) and was not used.
3. **The skip-rule flags were recomputed for the tier lists** from the 2026-11-05 OHLC. `atr_shrink` and `wicky_breakout` are computed where the inputs exist; `day2_no_follow`, `no_reclaim_15m` and `second_bite_d2` are live-tape-only and are published as `None` (not computable), never as `False`.
4. **TradingView's growth columns are null for every US name** (documented, measured), so Jeff Sun's CANSLIM screen was rebuilt on shibui's `fundamentals_derived_quarterly` (27 names) with decimal-fraction growth — the canonical recipe in `references/filters.md`.
5. **TradingView's relative volume runs tighter than a true trailing-10 average**, so `rvol_10d` is a ranking proxy, not a tradable ratio.
6. **The breadth universe is a market-cap proxy** (986 names > $10B), not an index membership list; shibui's equivalent population for 2026-11-05 is 891 names. The two breadth percentages are different series — see `breadth.md`.
7. `type=stock` includes REITs and non-US-domiciled US listings; no domicile filter was applied. Sector labels are TradingView's taxonomy, not GICS.
8. **The Hernandez theme funnel is TV-native this run.** The top three sector ETFs by composite 1M/3M/6M RS (**XLV, IBB, XLP**) were mapped to TradingView's sector taxonomy, and the leaders were taken as names ≥ $2B with 1M RS ≥ +15% above their 20-DMA (99 names). The mapping is a judgement call and is published with the count.
9. **The Jeff Sun volume-breakout proxy is TV-native** (cap > $1B, volume ≥ 1.5× the 10-day average, close above the 20-DMA, positive day — 14 names). The filter is published here because the underlying `mcp__tradingview-advanced__volume_breakout_scanner` is not reachable from this runtime.
10. **No reversal-bullish scan, no IPO refresh, no high-short-float refresh** — those belong to cron #91 and the Sunday weekly run. This routine is the end-of-day breadth + screen read.
11. Catalyst attribution is limited to the names sourced in this run; for every other mover the table says "no catalyst sourced" rather than guessing.

## Files in this directory

`daily-sweep.md` (this file) · `breadth.md` + `_regime.json` (+ `_regime-screener.json` alias) · `_summary.md` · `_results.json` · `_cache.json` · per-stylist `stockbee` / `qullamaggie` / `jeff-sun` / `ariel-hernandez` / `peoplewish` (`.md` + `.csv`) · `master` / `stalk` / `focus` / `tier-a` (`.md` + `.csv`) · `short-candidates` / `long-reversal-candidates` (`.md` + `.csv`).

The intraday counterpart for the same session is `daily-screens/2026-11-06/breadth-snapshot.md` (cron #10, 14:00 ET) — it is expected to differ from `breadth.md` (different VIX quote time, different breadth population, live tape vs settled close).
