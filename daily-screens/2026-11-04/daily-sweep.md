# Daily screener sweep — 2026-11-04 (end-of-day, 18:30 ET)

**Cron #09 · stock-screener-daily-sweep-18:30 · fired 2026-11-04 18:30:54 ET · read from the settled regular-session close.**

## Headline

A broad, health-care-led rally with a violent internal split: the equal-weight index beat the cap-weight index, **71.0%** of the $10B+ universe closed above its 20-DMA, and **756 names advanced against 243 decliners** — but only **2 of the 5** index ETFs sit above their 20-DMA, so the index level still describes a market that has not repaired its short-term trend. Leadership was health care, staples, financials and consumer; **semis and energy were sold hard** (Electronic Technology 1M -11.3% with 31% of names above their 20-DMA; Energy Minerals median day -5.17%). The screen itself is one session behind: shibui's newest settled session at fire time was **2026-11-03**, so every screen metric below describes the 11-03 tape while every "today" figure is the 11-04 settled close.

## The day

| Index | Close | Day | vs 20-DMA | vs 50-DMA |
|---|---|---|---|---|
| SPY | 766.81 | **+1.65%** | 767.57 (below) | 767.06 |
| RSP | 223.33 | **+1.86%** | 216.32 (above) | 214.99 |
| QQQ | 691.95 | +0.97% | 717.42 (below) | 723.56 |
| QQQE | 117.38 | +1.23% | 118.60 (below) | 119.58 |
| IWM | 284.02 | +1.51% | 277.44 (above) | 283.19 |

**VIX 16.61 / VIX3M 18.80 (Cboe, both stamped 16:15:01 ET) — ratio 0.8835.** One pair, used everywhere; no second volatility reading appears in this document. Front-end stress is absent: the front of the curve carries a *discount* to the long end.

Breadth, full detail in `breadth.md`: 1,001-name universe (NYSE/NASDAQ/AMEX, type=stock, cap > $10B), 71.0% above 20-DMA, 59.6% above 50-DMA, 54.7% above 200-DMA, median change +2.22%.

## Regime

`size_cut_pct = 0` · `uncertainty = false` · `late_cycle = false`

The size-cut rule needs the index below its 20-DMA **and** breadth under 40%. The first condition is met (40.0% of index ETFs above 20-DMA), the second is not (71.0%) — so the regime stays neutral despite the index being below its 20-day mean. That divergence, not the headline breadth number, is the thing to watch into tomorrow.

## Leadership

| Theme | Evidence | Read |
|---|---|---|
| Health care | XLV +3.06% (1M +14.3%, 6M +31.2%); Health Technology 90.4% above 20-DMA; IBB +2.63%, XBI +2.67% | the clear leadership group; MRNA +13.11% on the mRNA-2808 myeloma readout |
| Defensive consumer | XLP +3.36%, Consumer Durables 100% above 20-DMA, Consumer Services 92.3% | broad participation, not one stock |
| Financials | XLF +3.51% | but FIS -23.67% on its own deleveraging news |
| Semis (sold) | SMH **-2.75%**, XLK -0.01%, Electronic Technology 1M **-11.3%**, 31.0% above 20-DMA | the weakest sector on every horizon; the drag on QQQ |
| Energy (split) | XLE **-4.74%**, Energy Minerals median **-5.17%** and only 4.3% above 20-DMA — yet GDX **+9.01%**, TAN +5.65%, JETS +6.70% | metals and solar bid, integrated energy sold |
| Crypto/AI-datacenter complex | CIFR -19.95%, CLSK -16.56%, HUT -23.23%, CORZ -10.39% | political + financing risk, not a tape risk |

## Movers with a sourced catalyst

| Symbol | Day | Catalyst (source) |
|---|---|---|
| DUOL | **+25.99%** | Q3 revenue $309M (+13.7%) vs $303.4M est; Q4 guide $322M vs $314.8M est; DAU +29% to 64.9M. Offsetting: GAAP EPS $0.54 vs $0.56 est, operating margin 7.8% vs 12.9% a year ago ([Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/why-duol-stock-surging-over-080159800.html), [Benzinga](https://www.benzinga.com/trading-ideas/movers/26/11/62854845/duolingo-plans-monetization-push-in-2027-after-strong-user-growth)) |
| MRNA | **+13.11%** | Early mRNA-2808 myeloma data — 4 confirmed responses in 11 evaluable heavily pretreated patients, 41.7% Grade 3+ AEs; new 52-week high $258.72. Q3 reports Friday ([Yahoo Finance](https://finance.yahoo.com/healthcare/articles/moderna-soars-8-early-multiple-164119870.html), [MarketBeat](https://www.marketbeat.com/stocks/NASDAQ/MRNA/news/)) |
| FISV | **+6.25%** | Q3 (Nov 3) +12.46%; $500M buyback; 5-day streak +23.2%; KBW raises PT 60→70, Morgan Stanley 59→61 ([Yahoo Finance](https://finance.yahoo.com/quote/FISV/), [Trefis](https://www.trefis.com/stock/fisv/articles/622456/a-5-day-winning-streak-has-fiserv-stock-up-23/2026-11-04)) |
| GKOS | **+5.86%** | Glaukos — new 52-week high ($249.37 intraday), Q3 reported Oct 28 ([MarketBeat](https://www.marketbeat.com/instant-alerts/price-glaukos-nyse-gkos-reaches-new-12-month-high-whats-next-2026-11-04/)) |
| GPK | **+3.89%** | Q3 (Nov 3) beat, 2026 guidance maintained, 2027 EBITDA inflection; RBC raises PT $9→$12; +36% over the past month ([StockAnalysis](https://stockanalysis.com/stocks/gpk/), [Massive](https://massive.com/quote/gpk)) |
| LSCC | +1.26% | Lattice Semiconductor — record 3Q26 revenue, +118% YoY (reported Nov 2). Stock still -22% over 1M and -38% YTD ([StockTitan](https://www.stocktitan.net/overview/LSCC/)) |
| CDNA | **-2.95%** | CareDx — Q3 revenue $139M (+39%), FY26 guidance raised to $520–530M and adj. EBITDA to $90–100M, but 94% 90-day gain leaves the stock at risk of a valuation reset ([Simply Wall St](https://simplywall.st/stocks/us/pharmaceuticals-biotech/nasdaq-cdna/caredx/news/caredx-cdna-raises-2026-outlook-after-strong-quarter-while-v), [8-K](https://last10k.com/sec-filings/cdna/0001217234-26-000059.htm)) |
| KVYO | +0.14% | no catalyst sourced |
| FTAI | **-10.54%** | Q3 EPS $1.43 vs $1.47 consensus; Morgan Stanley and Barclays cut PTs to $310; $1B senior notes priced Nov 2 ([StockAnalysis](https://stockanalysis.com/stocks/ftai/), [Simply Wall St](https://simplywall.st/stocks/us/capital-goods/nasdaq-ftai/ftai-aviation/news/is-strong-earnings-altering-the-investment-case-for-ftai-avi)) |
| ECG | **-29.29%** | Everus Construction Group — Q3 (Nov 3 AMC) actually beat: EPS $1.79 vs $1.31, revenue $1.38B vs $1.19B, +40.3% YoY. The stock gapped from $112.73 to a $99.72 open and closed $79.71 — the worst reaction in the group, on guidance/margin, not on the headline print ([MarketBeat](https://www.marketbeat.com/instant-alerts/price-everus-construction-group-nyse-ecg-shares-gap-down-heres-what-happened-2026-11-04/), [MarketChameleon](https://marketchameleon.com/Overview/ECG/Earnings/Earnings-Dates)) |
| FIS | **-23.67%** | Pauses buybacks and tuck-in M&A to deleverage toward ~2.8x gross leverage; CFO James Kehoe stepping down; FY pro-forma organic revenue growth guided to 3.4% vs 3.7% in Q3. Worst day in four years ([Bloomberg](https://news.bloomberglaw.com/mergers-and-acquisitions/fis-plunges-as-fintech-halts-buybacks-some-m-a-to-deleverage), [Motley Fool](https://finance.yahoo.com/markets/stocks/articles/why-fidelity-national-information-services-210137551.html)) |
| CIFR | **-19.95%** | Texas governor race: Gina Hinojosa (D) defeated Greg Abbott after campaigning for a moratorium on new data centres; compounded by a KBW downgrade to Market Perform ($9.50 PT). Cipher's first HPC lease revenue ($5.9M) was small against mining revenue that fell to $20.8M from $71.7M ([crypto.news](https://crypto.news/cipher-digital-shares-fall-texas-governor-election/), [MarketBeat](https://www.marketbeat.com/instant-alerts/price-cipher-mining-nasdaq-cifr-shares-gap-down-following-analyst-downgrade-2026-11-04/)) |

Other large moves (cap > $2B) with **no catalyst sourced in this run**: KD +30.14%, RYTM +28.04%, YOU +23.70%, PCOR +19.68%, MDLN +18.36%, LIVN +17.88%, UFPT +17.66%, MOS +17.37%, OUST +15.73%, VRDN +15.53%, XYZ +15.30%, SUPN **-32.71%**, DOX -30.07%, HUT -23.23%, STRL -21.46%, MOD -21.43%, INIO -19.50%, LGN -17.95%, UNM -17.84%, MTRN -17.66%, BTU -17.62%, FPS -17.32%, TRMB -17.31%.

## Tier-A — ≥ 3 distinct stylists (cap 8; pool was 13, truncated)

| Symbol | Stylists | Close | Today | Cap | Note |
|---|---|---|---|---|---|
| **LSCC** | jeff_sun, peoplewish, qullamaggie, stockbee | 107.25 | +1.26% | $15.2B | the only 4-stylist name; record Q3 revenue +118% YoY |
| **GKOS** | hernandez, peoplewish, qullamaggie | 246.70 | +5.86% | $14.6B | 52-week high; +28.6% over 5 sessions (parabolic-short list) |
| **CDNA** | jeff_sun, peoplewish, qullamaggie | 85.86 | -2.95% | $4.5B | raised FY26 guide; +25.4% over 5 sessions |
| **KVYO** | jeff_sun, peoplewish, qullamaggie | 21.36 | +0.14% | $6.1B | no catalyst sourced |
| **FTAI** | jeff_sun, peoplewish, qullamaggie | 179.58 | **-10.54%** | $18.4B | PT cuts after a consensus-missing Q3 |
| **MRNA** | hernandez, peoplewish, qullamaggie | 258.38 | **+13.11%** | $103.2B | 52-week high on the myeloma readout |
| **FISV** | hernandez, jeff_sun, stockbee | 62.05 | +6.25% | $33.0B | buyback + 5-day streak; rvol 2.15 |
| **GPK** | jeff_sun, qullamaggie, stockbee | 11.75 | +3.89% | $3.5B | Q3 beat; rvol 2.03 |

**The tier is not a bullish list.** Four of the eight names are *also* on the parabolic-short list and two of those fell hard today (FTAI -10.5%, CDNA -3.0%) — these are screens converging on extension, and the Tier-A screen has no direction. Three of the eight (GKOS, MRNA, FISV) rose on genuine company news; the other five did not have a fresh catalyst.

## Focus — ≥ 2 distinct stylists (cap 12)

AEHR -6.56% (3) · AEIS -11.15% (3) · APLD -6.74% (2) · BETA +7.06% (2) · **CIFR -19.95%** (2) · CLSK -16.56% (2) · CORZ -10.39% (2) · **ECG -29.29%** (3) · EVER +5.12% (2) · FISV +6.25% (3) · FN -5.97% (2) · FRVO -4.51% (2)

Six of the twelve are the crypto/AI-datacenter complex (CIFR, CLSK, CORZ, APLD, FRVO, plus AEHR/AEIS in semis) — the day's political shock is showing up here because that group was already on the screens. Treat the Focus list as a *watch* list, not a buy list.

## Parabolic short candidates — 5-session gain ≥ +25% (11)

ADT +43.4% (today +0.51%) · AXGN +32.1% (+3.74%) · WING +30.8% (+3.74%) · GPK +30.1% (+3.89%) · CPRI +30.1% (+5.83%) · FMC +29.3% (+5.42%) · GKOS +28.6% (+5.86%) · CROX +28.5% (+4.06%) · HAYW +26.6% (+2.91%) · FTAI +26.5% (**-10.54%**) · CDNA +25.4% (-2.95%)

The signal is decaying: seven of the eleven were up on the day anyway, and the two that actually broke (FTAI, CDNA) were the two with company news pushing against the setup.

## Parabolic long / mean-reversion candidates — 5-session loss ≤ -25% (12)

IOVA -39.4% (today -1.47%) · INTC -35.4% (-3.77%) · SUPN -31.3% (**-32.71%**) · FTNT -30.8% (+1.00%) · RDDT -29.5% (+5.97%) · ALNY -29.5% (+0.74%) · NOW -29.5% (-0.32%) · MRVL -29.4% (-7.08%) · FFIV -27.9% (-0.43%) · SLS -27.1% (+3.04%) · DT -26.2% (-0.53%) · MPT -25.7% (+1.49%)

Nine of the twelve were flat-to-up today — the washout these screens want has already started to bounce, and SUPN (-32.7%) is the one name still selling. Nothing here has been confirmed by a follow-through day.

## Counts

| Set | Count |
|---|---|
| Unique candidates across 11 screen origins | 848 |
| Master (cap 200) | 200 |
| Stalk (Master within 2% of 10/20-DMA) | 17 |
| Focus (≥2 stylists, cap 12) | 12 |
| Tier-A (≥3 stylists, cap 8) | 8 (pool 13, truncated) |

Per stylist: jeff_sun 538 · peoplewish 200 · stockbee 122 · qullamaggie 68 · hernandez 30.
Screen origins: `TV_volume_breakout` 462 · `G_peoplewish` 200 · `jeff_sun_canslim` 85 · `A_stockbee_4pct` 50 · `B_stockbee_ep9m` 50 · `C_qullamaggie_rs` 44 · `K_stockbee_anticipation` 30 · `H_hernandez_theme` 30 · `F_qullamaggie_5d_losers` 12 · `E_qullamaggie_5d_gainers` 11 · `D_qullamaggie_ep` 6.

## Source health

| Source | URL / query | Status | Used for |
|---|---|---|---|
| MCP availability probe | `probe_mcp.py` | `catalog_ok total=135 finance_tools=0` | confirms no finance MCP is registered; the bridge is the path |
| shibui (MCP bridge) | 6 `stock_data_query` SQL calls: resolve_date, stockbee, qullamaggie, peoplewish, breadth, CANSLIM rebuild | ok — 130 / 73 / 200 / 7 / 85 rows | screen metrics, T+1 breadth cross-check, growth screen |
| TradingView scanner | `POST https://scanner.tradingview.com/america/scan` — 11 calls | ok — large-cap 1,001/1,001 unique, volume breakout 462/462, no paging loss (explicit `sort` by name, de-duplicated) | settled close, SMA10/20/50/200, ATR, Perf 1M/3M/6M, sector, cap, movers |
| Cboe delayed quotes | `cdn.cboe.com/api/global/delayed_quotes/quotes/{_VIX,_VIX3M,SPY,RSP,QQQ,QQQE,IWM}.json` | ok — `last_trade_time` 16:15:01 ET (VIX pair), 15:59:59/16:00:00 ET (indexes) | VIX/VIX3M, index levels |
| Nasdaq `/info` | 15 Focus/Tier-A names | ok — 15/15 | official 4:00 PM close cross-check |
| web_search | 12 catalyst queries | ok | catalyst sourcing for the table above |
| Finviz | — | not attempted | Cloudflare 403 from this egress (known, documented) |
| Yahoo JSON | — | not used | — |

**errors: 0 source failures.** No source was rate-limited, timed out, or returned an unparseable body.

## Caveats and degradations

1. **Two data dates in one artifact, on purpose.** Screen metrics (chg %, RS, ADR, velocity, 5-day moves) are shibui's **2026-11-03** session; "today" columns are the **2026-11-04** settled close from TradingView. Columns are named `*_resolved` vs `today_*` in every CSV so the two can never be conflated.
2. **The close is verified, twice.** TradingView's `close` matched Nasdaq's official 4:00 PM close (`secondaryData`) on 15 of 15 sampled names. Nasdaq's `primaryData` on the same pulls was the *after-hours* print stamped 18:36 ET — it is not the official close and was not used.
3. **5 of the 6 skip-rule flags are not computable** from the available feeds (`atr_63_median`, 5d/20d range, and the three live-tape-only flags). Only `wicky_breakout` was computed. The others are `null` in the CSVs, not `false`.
4. **TradingView's growth columns are null for every US name** (documented, measured), so Jeff Sun's CANSLIM screen was rebuilt on shibui's `fundamentals_derived_quarterly` (85 names) with decimal-fraction growth — the canonical recipe in `references/filters.md`.
5. **TradingView's relative volume runs 6–16% tighter than a true trailing-10 average**, so `rvol_10d` is a ranking proxy, not a tradable ratio.
6. **The breadth universe is a market-cap proxy** (1,001 names > $10B), not an index membership list; shibui's equivalent population for 2026-11-03 is 905 names. The two breadth percentages are different series — see `breadth.md`.
7. `type=stock` includes REITs and non-US-domiciled US listings; no domicile filter was applied. Sector labels are TradingView's taxonomy, not GICS.
8. **No reversal-bullish scan, no IPO refresh, no high-short-float refresh** — those belong to cron #91 and the Sunday weekly run. This routine is the end-of-day breadth + screen read.
9. Catalyst attribution is limited to the names sourced in this run; for every other mover the table says "no catalyst sourced" rather than guessing.

## Files in this directory

`daily-sweep.md` (this file) · `breadth.md` + `_regime.json` (+ `_regime-screener.json` alias) · `_summary.md` · `_results.json` · `_cache.json` · per-stylist `stockbee` / `qullamaggie` / `jeff-sun` / `ariel-hernandez` / `peoplewish` (`.md` + `.csv`) · `master` / `stalk` / `focus` / `tier-a` (`.md` + `.csv`) · `short-candidates` / `long-reversal-candidates` (`.md` + `.csv`).

The intraday counterpart for the same session is `daily-screens/2026-11-04/breadth-snapshot.md` (cron #10, 14:00 ET) — it is expected to differ from `breadth.md` (different VIX quote time, different breadth population, live tape vs settled close).
