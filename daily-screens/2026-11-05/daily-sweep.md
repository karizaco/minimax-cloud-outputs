# Daily screener sweep — 2026-11-05 (end-of-day, 18:30 ET)

**Cron #09 · stock-screener-daily-sweep-18:30 · fired 2026-11-05 18:30:46 ET · read from the settled regular-session close.**

## Headline

The market repriced the AI-infrastructure trade in a single session. After the 2026-11-03 midterms, state-level data-centre pushback (Texas Gov.-elect Gina Hinojosa's moratorium call, Ohio's Amy Acton on a conditional moratorium) became the trade's price: **SPY -4.41% to 733.00, QQQ -6.49%, SMH -11.21%, SOXX -12.15%, ARKK -8.98%** and the VIX went from 16.61 to **28.18** in one session. The damage was concentrated, not systemic — **58.31%** of the 981-name $10B+ universe closed above its 20-DMA and the median name fell 1.93%, while only **1 of the 5** index ETFs (RSP) is above its 20-DMA. That split is the whole session: the cap-weighted index is broken, the average stock is damaged but not broken. The screen itself is one session behind: shibui's newest settled session at fire time was **2026-11-04**, so every screen metric below describes the 11-04 tape while every "today" figure is the 11-05 settled close.

## The day

| Index | Close | Day | vs 20-DMA | vs 50-DMA |
|---|---|---|---|---|
| SPY | 733.00 | **-4.41%** | 765.53 (below) | 766.40 |
| RSP | 216.87 | **-2.89%** | 216.57 (above) | 214.89 |
| QQQ | 647.05 | **-6.49%** | 712.40 (below) | 722.27 |
| QQQE | 111.52 | -4.99% | 118.12 (below) | 119.36 |
| IWM | 270.98 | -4.59% | 277.11 (below) | 282.63 |
| DIA | 514.27 | -3.53% | — | — |

**VIX 28.18 / VIX3M 25.55 (Cboe, both stamped 16:15:01 ET) — ratio 1.1029.** One pair, used everywhere; no second volatility reading appears in this document. The ratio crossed above 1.0 for the first time in this leg: front-end stress now exceeds the long end, which is the `uncertainty` flag. The pair was pulled twice and both pulls were identical.

Breadth, full detail in `breadth.md`: 981-name universe (NYSE/NASDAQ/AMEX, type=stock, cap > $10B), 58.31% above 20-DMA, 48.93% above 50-DMA, 46.28% above 200-DMA, 145 advancers vs 832 decliners, median change -1.93%.

## Regime

`size_cut_pct = 0` · `uncertainty = true` · `late_cycle = false`

The size-cut rule needs the index below its 20-DMA **and** breadth under 40%. The first condition is met (20.0% of index ETFs above 20-DMA), the second is not (58.31%) — so the regime stays neutral on size. `uncertainty` flipped to true on the VIX/VIX3M inversion. `late_cycle` is false, but for the wrong reason: every index ETF is *below* its 50-DMA (QQQ -10.41%), which is the opposite of the extension case the flag was designed to catch.

## Leadership

| Theme | Evidence | Read |
|---|---|---|
| Defensive consumer | XLP -0.75% (1M +12.6%); Consumer Non-Durables 91.2% above 20-DMA, 97.1% above 50-DMA; Consumer Durables 94.7% above 20-DMA | the leadership group; barely down |
| Health care | XLV -2.50% (1M +10.1%, 6M +27.9%); Health Services 87.5% above 20-DMA; Health Technology 75.7% | still the best 6-month sector, but -3.07% median day |
| Utilities / real estate | XLU -0.71%, XLRE -1.82%, TLT **+0.21%**, GLD +0.81% | the rate-sensitive corner was bid |
| Financials | XLF -2.87%, KRE -2.46%, Finance 66.2% above 20-DMA but only 37.9% above 50-DMA | held up on the day; the 50-DMA damage is where the stress is |
| Metals | GDX **+1.37%** — the only sector ETF up on the day | miners decoupled from the AI complex |
| Semis (crushed) | SMH **-11.21%**, SOXX **-12.15%**, XLK -8.00%, Electronic Technology median day **-9.26%** with 18.8% above 20-DMA | the epicentre: AI hardware and connectivity |
| Software vs hardware | IGV -4.39% vs SOXX -12.15% | the split inside "technology" is hardware vs software, not tech vs non-tech |
| Energy | XLE -2.98%, Energy Minerals only 4.3% above 20-DMA (unchanged from 11-04), but USO +1.93% | crude bid, miners bid, the equity complex did not follow |

## Movers with a sourced catalyst

| Symbol | Day | Catalyst (source) |
|---|---|---|
| APP | **+31.04%** | AppLovin Q3 (Nov 4 AMC) revenue $2.18B (+55% YoY) vs $2.07B est., EPS $4.30 vs $4.03 est., Q4 guide $2.365–2.395B vs $2.25B consensus, buyback lifted to $3.6B ([Yahoo Finance](https://ca.finance.yahoo.com/news/applovin-stock-rises-31-revenue-150300935.html)) |
| ECPG | **+26.26%** | Encore Capital Q3 GAAP EPS $5.57 (+76% YoY), record global collections $754M (+14%), FY26 guidance raised to $15.50–16.00 EPS ([Nasdaq press release](https://www.nasdaq.com/press-release/encore-capital-group-announces-third-quarter-2026-financial-results-2026-11-04)) |
| ADMA | **+26.05%** | ADMA Q3 ASCENIV revenue +31% to $124.7M, total revenue +5% to $141.1M; raised FY26 minimum adjusted net income to ≥$180M and adjusted EBITDA to ≥$275M ([Benzinga](https://www.benzinga.com/trading-ideas/movers/26/11/62936143/12-health-care-stocks-moving-thursday-s-intraday-session)) |
| XERS | **+25.05%** | Xeris Q3 revenue $107.2M (+44% YoY), Recorlev +93% to >$71M; FY26 revenue guidance raised to $395–405M ([8-K](https://www.sec.gov/Archives/edgar/data/1867096/000186709626000114/exh991q32026earningsrelease.htm)) |
| WRBY | **+22.50%** | Warby Parker Q3 revenue $244.7M (+10.4% YoY), adjusted EBITDA $28.6M above guidance, FY26 revenue guidance narrowed to $966–976M ([8-K](https://www.sec.gov/Archives/edgar/data/0001504776/000150477626000022/warbyparkerincearningsrele.htm)) |
| ARDT | **+22.40%** | Ardent Health Q3 revenue $1,625M (+3.1%), adjusted EBITDA $138M; raised the low end of FY26 adjusted EBITDA guidance to $500M from $485M ([Q3 release](https://s204.q4cdn.com/127897503/files/content_files/ARDT-Q3-26-Earnings-Release.pdf)) |
| MGNI | **+20.75%** | Magnite Q3 non-GAAP EPS $0.33 vs $0.26 est., revenue $204.2M vs $190M, CTV contribution ex-TAC +39% to $105.4M; FY26 contribution ex-TAC growth raised to ~17% ([EarningsWhispers](https://www.earningswhispers.com/epsdetails/MGNI/202609)) |
| EPAM | **+20.63%** | EPAM Q3 non-GAAP EPS $3.51 vs $3.41 est., revenue $1.426B (+2.3%); FY26 guidance raised to 3.5–3.7% growth, buyback lifted to $1.8B ([IR](https://investors.epam.com/news/news-details/2026/EPAM-Reports-Results-for-Third-Quarter-2026/default.aspx)) |
| U | **+14.93%** | Unity Q3 revenue $622.1M (+32% YoY) vs $567.3M est., GAAP profit $121.6M, adjusted EBITDA doubled to $256.6M ([Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/1-turnaround-stock-own-just-212601519.html)) |
| PGNY | **+14.19%** | Progyny Q3 EPS $0.52 vs $0.31 est., record 1.3M covered lives, FY26 revenue raised to $1.365–1.385B; Wells Fargo PT $37→$38, Citizens $33→$38 ([Benzinga](https://www.benzinga.com/quote/PGNY)) |
| TPR | **+7.07%** | Tapestry FQ1 revenue $1.894B (+11%) vs $1.85B est., non-GAAP EPS $1.82 vs $1.56; FY27 adjusted EPS guidance raised to $8.25–8.35 ([IR](https://investors.tapestry.com/news-releases/news-release-details/tapestry-inc-reports-fiscal-2027-first-quarter-results-and)) |
| VRSK | **+6.88%** | Verisk Q3 adjusted EPS $1.96 vs $1.92 est., revenue $809M (+5.3%); FY26 guidance reaffirmed ([MarketBeat](https://www.marketbeat.com/instant-alerts/guidance-verisk-analytics-nasdaq-vrsk-issues-fy-2026-earnings-guidance-2026-11-05/)) |
| CPAY | **+6.78%** | Corpay Q3 revenue $1.38B (+18%), adjusted EPS $7.54 vs $7.19 est.; FY26 guidance raised, buyback +$1B ([Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/corpay-q3-earnings-beat-estimates-164900874.html)) |
| RGLD | **+6.18%** | Royal Gold Q3 record revenue $464.8M (+84% YoY), 109,000 GEOs sold, adjusted net income $238M, debt-free ([Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/royal-gold-rgld-q3-2026-211548457.html)) |
| MU | **-17.46%** | No company release; sold as part of the memory/data-centre complex on post-midterm fears that a Democratic Congress slows AI infrastructure spending ([Yahoo Finance](https://au.finance.yahoo.com/news/micron-declines-12-as-chip-sell-off-deepens-163137019.html)) |
| AMD | **-17.26%** | Record Q3 (revenue $13.38B +45%, adj EPS $2.09 vs $1.94 est., Q4 guide ~$17B) overwhelmed by the political repricing of the AI build-out ([Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/amd-tumbles-13-nvidia-slides-154601778.html)) |
| WDC / STX / SNDK | **-17.35% / -16.25% / -22.26%** | The storage complex de-rated with the AI trade — SNDK's own FQ1 beat ($11.03B vs $10.70B est.) — on post-midterm demand fears for NAND/HDD ([Yahoo Finance](https://finance.yahoo.com/markets/article/chip-stocks-slaughtered-as-wall-street-suffers-worst-post-midterm-day-since-1896-213204256.html)) |
| LITE | **-18.68%** | Sliding on the Nov 2 all-stock Marvell merger (4.500 MRVL per LITE, $115B EV) as MRVL fell harder, widening the merger spread ([Marvell IR](https://investor.marvell.com/news-events/press-releases/detail/1040/marvell-and-lumentum-to-combine-creating-a-category-leader-in-ai-connectivity)) |
| MRVL | **-16.43%** | The AI/data-centre rout plus shareholder backlash to the $115B Lumentum deal ([MarketWatch](https://www.marketwatch.com/story/marvell-and-lumentum-shareholders-unite-in-panning-merger-deal-its-a-trash-offer-53a9f307)) |
| BE | **-16.41%** | Fell even on its 900MW NTT DATA on-site power deal — the most data-centre-exposed name, and the one most exposed to the permitting pushback ([Morningstar/MarketWatch](https://www.morningstar.com/news/marketwatch/20261105193/bloom-energys-stock-is-one-of-the-sp-500s-biggest-losers-amid-fears-of-data-center-delays)) |
| FSLY | **-26.88%** | Beat (Q3 revenue $190.2M +20.2%, adj EPS $0.17 vs $0.12 est., FY26 raised) but top-10 customers jumped to 39% of revenue and the CRO plans to retire ([247wallst](https://247wallst.com/investing/2026/11/05/fastly-just-dropped-41-in-a-month-is-fsly-stock-dead-money-or-due-for-a-bounce/)) |
| BROS | **-21.41%** | Dutch Bros Q3 EPS $0.20 missed $0.25 est. on revenue $549.8M (+30%); FY adjusted EBITDA cut below consensus, and the Executive Chairman sold ~$106.4M of stock ([Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/bros-stock-plummets-15-overnight-042427151.html)) |
| ARQT | **-20.70%** | Arcutis Q3 EPS $0.06 vs $0.17 est. (revenue +45% to $143.9M), and a Nov 4 prospectus allowing up to $200M of stock sales ([StockTitan](https://www.stocktitan.net/overview/ARQT/)) |
| CAI | **-21.64%** | Caris Q3 EPS fell to $0.05 from $0.08 on margin pressure and negative operating cash flow, though revenue rose 27% to $275.4M ([Yahoo Finance](https://finance.yahoo.com/healthcare/articles/caris-life-sciences-q3-earnings-221014849.html)) |

Other large moves (cap > $2B) with **no catalyst sourced in this run**: ALAB -19.62% (no company news — it had just beaten, Q3 revenue +154% to $584.9M, Q4 guide $730–750M vs $656M est. — and fell with the complex, [Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/astera-labs-sinks-12-dell-144612431.html)), CRDO -17.71%, MTSI -18.35%, LRCX -16.36%, TER -15.24%, AXTI -22.76%, MXL -22.06%, AAOI -20.89%, ASX -20.77%.

## Tier-A — ≥ 3 distinct stylists (cap 8; pool was 6)

| Symbol | Stylists | Close | Today | Cap | Note |
|---|---|---|---|---|---|
| **VRDN** | hernandez, peoplewish, qullamaggie, stockbee | 28.55 | -1.74% | $3.2B | the only 4-stylist name; 6 screen origins; velocity 48.5 |
| **XNCR** | hernandez, peoplewish, qullamaggie, stockbee | 34.05 | -2.80% | $2.5B | 4 stylists; velocity 46.0; rvol 0.63 (no volume behind it) |
| **DUOL** | peoplewish, qullamaggie, stockbee | 157.02 | -2.64% | $7.3B | 5-session gain +25.0% → also on the parabolic-short list |
| **KD** | peoplewish, qullamaggie, stockbee | 16.18 | -3.92% | $3.5B | 5 origins, 3 stylists; velocity 27.7; m1 +15.2% |
| **LIVN** | hernandez, qullamaggie, stockbee | 91.14 | -3.24% | $5.0B | health care; m1 +12.2%; rvol 1.41 |
| **OUST** | peoplewish, qullamaggie, stockbee | 30.52 | **-9.00%** | $2.2B | electronic technology — the only Tier-A name in the crushed sector |

**The tier is not a bullish list, and today it is mostly a list of things that fell.** Five of the six closed down, and the screens are converging on *extension* rather than on strength: DUOL (m1 +25.0%) and OUST (m1 +14.8%) are also on the parabolic-short list, and OUST took the full -9.00% of the Electronic Technology de-rating. Two of the six (VRDN, XNCR) are health-care names caught by the theme funnel rather than by a momentum signal — and XNCR traded on 0.63× relative volume, which is not a conviction tape.

## Focus — ≥ 2 distinct stylists (cap 12)

ENOV +17.20% (2) · CRCT +4.17% (2) · HELE +1.97% (2) · ARRY -0.56% (2) · VRDN -1.74% (4) · DUOL -2.64% (3) · XNCR -2.80% (4) · LIVN -3.24% (3) · KD -3.92% (3) · XYZ -4.10% (2) · YOU -4.37% (2) · OUST -9.00% (3)

Only three of the twelve closed up. ENOV (+17.20%, rvol 2.98) is the one genuine exception — Q3 EPS $5.57, +76% YoY, with FY26 guidance raised. Treat the Focus list as a *watch* list, not a buy list: it is a list of names the screens liked on the 11-04 tape, and the tape then broke.

## Parabolic short candidates — 5-session gain ≥ +25% (16)

FMC +43.6% (today -5.45%) · CPRI +38.8% (today -0.47%) · GPK +37.6% (today -1.79%) · GKOS +36.0% (today -10.83%) · ADT +33.6% (today 0.00%) · CROX +33.5% (today -4.32%) · CVNA +31.3% (today -7.07%) · NXT +30.0% (today -6.67%) · YOU +29.9% (today -4.37%) · RKT +29.7% (today -1.27%) · FISV +29.6% (today +1.11%) · BOOT +28.5% (today -4.63%) · CVCO +27.4% (today -5.12%) · GEN +26.9% (today -0.94%) · ENPH +26.3% (today -8.18%) · FCN +25.1% (today -1.17%)

The signal is decaying fast and the tape confirmed it: **fourteen of the sixteen fell**, and the three worst (GKOS -10.83%, ENPH -8.18%, CVNA -7.07%) are names whose whole screen history was extension. Only FISV (+1.11%) and ADT (flat) held. Nothing on this list should be treated as a fresh short into a 28-handle VIX.

## Parabolic long / mean-reversion candidates — 5-session loss ≤ -25% (26)

NRIX -41.5% (today -6.96%) · IOVA -41.3% (today -11.03%) · FRMI -39.7% (today -15.93%) · INTC -39.0% (today -10.33%) · MRVL -36.5% (today -16.43%) · DDOG -32.2% (today -7.48%) · LITE -31.4% (today -18.68%) · MOD -31.3% (today -7.27%) · SUPN -31.3% (today -5.21%) · ALNY -30.7% (today -2.74%) · DOX -29.8% (today +0.39%) · HUT -29.5% (today -6.11%) · AAOI -27.9% (today -20.89%) · NOW -27.5% (today -5.93%) · STRL -27.1% (today -13.86%) · GLXY -26.8% (today -7.09%) · CIFR -26.7% (today -14.62%) · VICR -26.6% (today -15.07%) · AXTI -26.2% (today -22.76%) · SNDK -26.2% (today -22.26%) · FTNT -25.7% (today -5.32%) · DT -25.5% (today -6.58%) · MPT -25.5% (today -8.29%) · LBRT -25.3% (today -13.69%) · CIEN -25.0% (today -15.22%) · IESC -25.0% (today -13.89%)

The mean-reversion screen produced a list that kept falling — **twenty-five of the twenty-six are lower again today**. The only exception is DOX (+0.39%). This is the first day in this series where the "oversold" screen found no floor: names already down 25–40% kept going. A washout screen that has not yet produced a single green follow-through day is a watchlist, not an entry signal.

## Counts

| Set | Count |
|---|---|
| Unique candidates across 11 screen origins | 1,420 |
| Master (cap 200) | 200 |
| Stalk (Master within 2% of 10/20-DMA + a setup tag) | 8 |
| Focus (≥2 stylists, cap 12) | 12 |
| Tier-A (≥3 stylists, cap 8) | 6 (pool 6, not truncated) |

Per stylist: stockbee 1,103 · peoplewish 272 · jeff_sun 177 · qullamaggie 117 · hernandez 81.
Screen origins: `A_stockbee_4pct` 755 · `B_stockbee_ep9m` 318 · `G_peoplewish` 272 · `K_stockbee_anticipation` 144 · `jeff_sun_canslim` 98 · `H_hernandez_theme` 82 · `TV_volume_breakout` 82 · `C_qullamaggie_rs` 69 · `F_qullamaggie_5d_losers` 26 · `E_qullamaggie_5d_gainers` 16 · `D_qullamaggie_ep` 10.

**Coverage assertion passed for every branch** (`rows_kept == rows_passing`, no branch landed on a 30/50/60/200 cap): 755/755, 318/318, 144/144, 69/69, 10/10, 16/16, 26/26, 272/272, 82/82.

## Source health

| Source | URL / query | Status | Used for |
|---|---|---|---|
| MCP availability probe | `probe_mcp.py` | `catalog_ok total=135 finance_tools=0` | confirms no finance MCP is registered; the bridge is the path |
| shibui (MCP bridge) | 13 `stock_data_query` SQL calls: resolve_date, prefilter, 8 sweep branches (paged), breadth, 1-year breadth series, tier ranges | ok — every branch paged to `rows_passing` | screen metrics, T+1 breadth cross-check, percentile series, Stalk gate, skip flags |
| TradingView scanner | `POST https://scanner.tradingview.com/america/scan` — 8 calls | ok — $10B universe 981/981 unique; $1B universe 2,593/2,593 across 3 pages, no paging loss | settled close, SMA20/50/200, ATR, Perf 1M/3M/6M, sector, cap, RVOL |
| MCP bridge (`market-recap`) | `get_quotes` ×2 (15 index/ETF symbols + 8 small-caps), `top_movers` ×3 | ok — all symbols found, `as_of` 21:00 UTC (16:00 ET), `market_state: post` | index/ETF closes, movers, small-cap tier prices |
| Cboe delayed quotes | `cdn.cboe.com/api/global/delayed_quotes/quotes/{_VIX,_VIX3M,_SPX,_NDX,_RUT,_DJI}.json` | ok — VIX pair 16:15:01 ET (two pulls identical), indexes 16:14:59 / 16:09:55 ET; **`_DJI` stale at 2026-11-03** | VIX/VIX3M, index levels |
| Nasdaq `/info` | 12 Focus/Tier-A names | ok — 12/12 fetched; **2 names differ >0.6% from the bridge** and in both directions | third reading, checked against the bridge — not a confirmation (see caveat 2) |
| web_search | 30 catalyst queries | ok | catalyst sourcing for the table above |
| Finviz | — | not attempted | Cloudflare 403 from this egress (known, documented) |
| Yahoo JSON | — | not used | — |

**errors: 0 source failures.** No source was rate-limited, timed out, or returned an unparseable body. Two data-quality flags are recorded rather than counted as failures (the stale `_DJI` print and the two thin-name close differences).

## Caveats and degradations

1. **Two data dates in one artifact, on purpose.** Screen metrics (chg %, RS, ADR, velocity, 5-day moves) are shibui's **2026-11-04** session; "today" columns are the **2026-11-05** settled close from TradingView/bridge. Columns are named `*_resolved` vs `today_*` in every CSV so the two can never be conflated.
2. **The close is verified on 12 names.** The bridge and TradingView agreed **to the cent on 12/12** — that pair is the published source. Nasdaq's `secondaryData` differs by more than 0.6% on two thin names (ENOV -0.63%, ARRY -1.05%) and in both directions across the rest, so it was treated as a third reading to check, not as a confirmation: cron #20's same-day finding (`docs/IMPROVEMENTS-cron20-eod-watchlist.md` §1) established that on 2026-11-05 Nasdaq's `/info` served **pre-auction prints stamped "Closed at 4:00 PM ET"**. Nasdaq's `primaryData` is the 18:40 ET after-hours print and was not used.
3. **The skip-rule flags were recomputed and two of them are not computable** from the available feeds (`atr_63_median` and the three live-tape-only flags). `wicky_breakout` and `ma_shrink_5d` are computed for the tier lists from the 11-04 OHLC. A repo defect was fixed in this run: `screen.py::_compute_skip_flags` defaulted missing inputs to a **positive** flag (`0 < 0.5 × 1e-9` is True), so `ma_shrink_5d` was True on all 1,407 candidates; the flags are now `None` when not computable.
4. **TradingView's growth columns are null for every US name** (documented, measured), so Jeff Sun's CANSLIM screen was rebuilt on shibui's `fundamentals_derived_quarterly` (98 names) with decimal-fraction growth — the canonical recipe in `references/filters.md`.
5. **TradingView's relative volume runs tighter than a true trailing-10 average**, so `rvol_10d` is a ranking proxy, not a tradable ratio.
6. **The breadth universe is a market-cap proxy** (981 names > $10B), not an index membership list; shibui's equivalent population for 2026-11-04 is 909 names. The two breadth percentages are different series — see `breadth.md`.
7. `type=stock` includes REITs and non-US-domiciled US listings; no domicile filter was applied. Sector labels are TradingView's taxonomy, not GICS.
8. **The Hernandez theme funnel is TV-native this run.** The top three sector ETFs by composite 1M/3M/6M RS (XLV, IBB, XLP) were mapped to TradingView's sector taxonomy — shibui's `general_info` carries a null `gics_sector` for every ETF — and the leaders were taken as names ≥ $2B with 1M RS > +15% above their 20-DMA (82 names). The mapping is a judgement call and is published with the count.
9. **No reversal-bullish scan, no IPO refresh, no high-short-float refresh** — those belong to cron #91 and the Sunday weekly run. This routine is the end-of-day breadth + screen read.
10. Catalyst attribution is limited to the names sourced in this run; for every other mover the table says "no catalyst sourced" rather than guessing.

## Files in this directory

`daily-sweep.md` (this file) · `breadth.md` + `_regime.json` (+ `_regime-screener.json` alias) · `_summary.md` · `_results.json` · `_cache.json` · per-stylist `stockbee` / `qullamaggie` / `jeff-sun` / `ariel-hernandez` / `peoplewish` (`.md` + `.csv`) · `master` / `stalk` / `focus` / `tier-a` (`.md` + `.csv`) · `short-candidates` / `long-reversal-candidates` (`.md` + `.csv`).

The intraday counterpart for the same session is `daily-screens/2026-11-05/breadth-snapshot.md` (cron #10, 14:00 ET) — it is expected to differ from `breadth.md` (different VIX quote time, different breadth population, live tape vs settled close).
