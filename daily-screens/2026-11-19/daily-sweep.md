---
artifact: daily-sweep
contract: SWEEP_PIPELINE_V1
cron: "#09 stock-screener-daily-sweep-18:30"
fire_time_et: "18:30 ET"
cron_date: "2026-11-19"
screen_data_date: "2026-11-18 (shibui is T+1 — the multi-session CONTEXT screens describe the previous session)"
fresh_data_date: "2026-11-19 (the cron-day settled bar — the TRIGGER screens: 4% breakout, EP9M, 10% gap, volume breakout)"
print_data_date: "2026-11-19 (official 16:00 ET close, bridge market-recap)"
regime: {size_cut_pct: 50, uncertainty: true, late_cycle: false, index_below_20sma: true, breadth_pct_spx: 21.2}
coverage: "9/9 branches complete (rows_kept == rows_passing on every branch)"
---

# Daily Screener Sweep — Thursday 19 November 2026 (end-of-day, cron #09)

This run uses the **dual book**: the TRIGGER screens (4% breakout, EP9M, 10% gap, volume breakout) run on **2026-11-19's own settled bar**, while the multi-session CONTEXT screens (5-day gainers/losers, 14-day velocity, the coil, the 252-session RS window) stay on shibui's newest ingested session, **2026-11-18**. Every row publishes which session it describes (`data_as_of` + `source`), and the two are never blended.

## TL;DR

- **A reversal day, and the size-cut regime is ON.** Anthropic's Nasdaq debut (opened +34%, closed +17%) triggered broad profit-taking: the Dow lost 1,101 points to 49,097.06 (-2.19%, its first close below 50,000 since June), the S&P 500 fell 2.02% to 7,175.83 - a sixth straight down day, the worst streak since April 2024 - and the Nasdaq Composite gave up 2.25% to 23,879.20 after being 2% higher intraday. Our own settled-close read: **939 decliners vs 117 advancers** in the $10B+ universe, median name -1.50%, only **21.2%** of that universe above its 20-DMA. With the index below its 20-DMA and breadth under 40%, the regime's `size_cut_pct` reads **50** - the size-cut posture is on.
- **Volatility is the story.** VIX closed at **28.44 (+15.80%)**, its highest close since 30 March, against VIX3M 27.03 - a ratio of **1.0522**, so `uncertainty` is **true**. All five index ETFs closed below their 20-DMA (`index_below_20sma: true`).
- **The book found the one real bid: cybersecurity.** Three of the five Tier-A names are the same trade - Palo Alto's fiscal Q1 (revenue +39% to $3.44bn, Next-Gen Security ARR +66% to $9.73bn), a raised FY27 guide and the $4.5bn Applied Compute acquisition lifted **PANW +6.42%**, **OKTA +5.75%** and **NTSK +5.51%**, with CrowdStrike, Zscaler and Fortinet up 5-7% alongside them.
- **Two more Tier-A names are single-name news.** **INSM +20.58%** - the largest move in the large-cap universe - on Bloomberg's report that Sanofi is weighing an acquisition of the ~$27bn rare-disease drugmaker (temporarily halted by a volatility circuit breaker). **BRBR +10.61%** - BellRing Brands' second leg after +24.07% on Wednesday's fiscal Q4, with five brokers lifting targets.
- **Tier-A is 0 fresh / 5 extended.** Every Tier-A name trips the extension label; BRBR (RSI 84.4, 47.5% above its 20-DMA) and NUAI (ATR 11.81% at the 99.3rd percentile) are extended in the most literal sense. Read Tier-A as *what the tape was strong in*, not as *what to buy at the open*.
- **Coverage is clean: 9 of 9 branches complete**, `rows_kept == rows_passing` on every branch, 1,269 screened rows -> 1,129 distinct candidates. The fresh book (today's settled bar) carries 270 names; the T+1 context book carries 1,093.

## Regime at the close

| Flag | Value |
|---|---|
| `size_cut_pct` | **50** (size cut is ON - the index is below its 20-DMA and breadth 21.20% is UNDER the 40% trigger) |
| `uncertainty` | **true** (VIX 28.44 / VIX3M 27.03 = 1.0522) |
| `late_cycle` | **false** (no index ETF > 6% above its 50-DMA; extreme is RSP at -1.54%) |
| `index_below_20sma` | **true** (0 of 5 index ETFs above their 20-DMA) |
| Breadth divergence | **+21.2 pp — BROAD** |

Full breadth read: `breadth.md`. Machine payload: `_regime.json` (flat schema v2, all eight keys, non-empty `atr_extensions`).

## The two books — what each one is, and what it says

| Book | Session | Branches | Names |
|---|---|---|---|
| **FRESH** (primary) | **2026-11-19** — the cron day's settled bar | `A_tv_breakout_4pct` 44 · `B_tv_ep9m` 231 · `D_tv_gap_10pct` 0 · `TV_volume_breakout` 35 | 270 |
| **T+1** (cross-check) | **2026-11-18** — shibui's newest ingested session | 9 branches | 1093 |

| `source` | Meaning | Count |
|---|---|---|
| `fresh+t1` | in both books | 234 |
| `t1` | context screens only | 859 |
| `fresh` | trigger screens only | 36 |

## Screen coverage — the assertion that makes the book publishable

Every branch was fetched as its own query, uncapped, and paged until the rows collected equalled `rows_passing`. **rows_kept == rows_passing on every branch**, and no branch count lands on a cap (30 / 50 / 60 / 200).

| Branch | Screen | rows_passing | rows_kept | Status |
|---|---|---|---|---|
| `A_stockbee_4pct` | Stockbee — Bonde 4% breakout (T+1) | 145 | 145 | complete |
| `B_stockbee_ep9m` | Stockbee — EP9M (T+1) | 198 | 198 | complete |
| `K_stockbee_anticipation` | Stockbee — anticipation / coil (T+1) | 452 | 452 | complete |
| `C_qullamaggie_rs` | Qullamägi — RS leaders, 252-session window (T+1) | 54 | 54 | complete |
| `D_qullamaggie_ep` | Qullamägi — EP 10% gap (T+1) | 0 | 0 | complete |
| `E_qullamaggie_5d_gainers` | Qullamägi — 5-day gainers, parabolic short (T+1) | 3 | 3 | complete |
| `F_qullamaggie_5d_losers` | Qullamägi — 5-day losers, parabolic long (T+1) | 20 | 20 | complete |
| `G_peoplewish` | peoplewish — ADR% + $vol + 14-day velocity (T+1) | 352 | 352 | complete |
| `H_hernandez_theme` | Hernandez — theme → group → leaders (T+1) | 45 | 45 | complete |

Total screened rows **1269** across the 9 branches → **1129 distinct candidates** after dedup and merge with the fresh book.

## Tier-A — ≥ 3 distinct stylists (5 names)

| Symbol | Stylists | Origins | Source | Close | **Chg** | ADR% | Velocity 14d | m1 (5d) | Ext |
|---|---|---|---|---|---|---|---|---|---|
| **BRBR** | 3 | A_stockbee_4pct, A_tv_breakout_4pct, B_stockbee_ep9m, B_tv_ep9m, C_qullamaggie_rs, TV_volume_breakout | `fresh+t1` | 15.11 | **+10.61%** | 5.75 | — | — | EXTENDED |
| **NTSK** | 4 | A_stockbee_4pct, A_tv_breakout_4pct, B_tv_ep9m, C_qullamaggie_rs, G_peoplewish, TV_volume_breakout | `fresh+t1` | 24.80 | **+5.51%** | 7.83 | -10.25 | — | EXTENDED |
| **NUAI** | 3 | A_stockbee_4pct, A_tv_breakout_4pct, B_stockbee_ep9m, B_tv_ep9m, C_qullamaggie_rs, TV_volume_breakout | `fresh+t1` | 4.28 | **+7.27%** | 16.17 | — | — | EXTENDED |
| **OKTA** | 3 | A_stockbee_4pct, A_tv_breakout_4pct, G_peoplewish, TV_volume_breakout | `fresh+t1` | 206.85 | **+5.75%** | 6.94 | -11.83 | — | EXTENDED |
| **PANW** | 3 | A_stockbee_4pct, A_tv_breakout_4pct, B_stockbee_ep9m, B_tv_ep9m, G_peoplewish, TV_volume_breakout | `fresh+t1` | 361.73 | **+6.42%** | 5.31 | -10.68 | — | EXTENDED |

### What Tier-A is saying

- **BRBR - BellRing Brands, $15.11 (+10.61%)**, 3 stylists, `fresh+t1`. The second leg of Wednesday's fiscal Q4: net sales +6.8% to $692m beat consensus, adjusted EPS $0.22 missed $0.23, FY27 sales guided to $2.32-2.42bn (implying flat-to-down). Five brokers lifted targets after the print - Bernstein $13->$15, Stifel and JP Morgan $15->$18. Two sessions, +37%. RSI 84.4 and 47.5% above its own 20-DMA; ADR 5.75% means a normal day is +-6% on a $15 stock. The label is not a formality here.
- **PANW - Palo Alto Networks, $361.73 (+6.42%)**, 3 stylists, `fresh+t1`. The anchor of the cyber bid: fiscal Q1 FY27 revenue +39% to $3.44bn, Next-Gen Security ARR +66% to $9.73bn, FY27 revenue guided to $14.52-14.57bn, and the $4.5bn Applied Compute acquisition announced Wednesday. The most interesting geometry on the board - ATR 5.60% and only 4.0% above its 20-DMA - so it is the Tier-A name least dependent on the tape that made the screen fire.
- **OKTA - $206.85 (+5.75%)**, 3 stylists, `fresh+t1`. Sympathy on Palo Alto's guide, with CrowdStrike, Zscaler and Fortinet +5-7%; Okta's own Q3 FY27 print is due after the close on 1 December. It was +12.07% on Wednesday, so this is day two of the bid. RSI is a mild 57.6 and ATR 6.72% - the extension risk here is a de-rating into its own earnings, not a stretched chart.
- **NTSK - Netskope, $24.80 (+5.51%)**, 4 stylists - the broadest stylist agreement on the board. The same cyber bid (+12.7% on Wednesday). ATR 7.25% is the 94.7th percentile of the $10B+ universe, so a 10-cent day is ordinary for it, and the valuation gate **fails** on negative free-cash-flow yield and debt/equity.
- **NUAI - New Era Energy & Digital, $4.28 (+7.27%)**, 3 stylists, ~$601m cap. A data-centre-power story with a thin float: +24.7% on Wednesday, Roth Capital's target raised $7->$17 on 13 November, 33.2m shares short (3.1 days to cover) after a $64m private placement on 28 October, and a $0.15-per-share loss reported on 12 November. Every quality measure is against it - the valuation gate **fails** on negative FCF yield, ATR is 11.81% at the 99.3rd percentile, and it is 52.3% above its 20-DMA. The biggest raw move on Tier-A is also its lowest-quality name.
- **Common ground:** all five are `fresh+t1` (both books agree), all five are EXTENDED, and three of five are one sector. A Tier-A list that is one sector on a -2% tape is a narrow book, not a broad one.

### The extension label — the honest answer to "have these already run?"

**Tier-A is 0 fresh / 5 extended.** Every row carries the label with its reasons; nothing is dropped for tripping it.

| Symbol | ATR% | ATR% pctile ($10B+) | % above 20-DMA | >15% rule |
|---|---|---|---|---|
| BRBR | 5.72 | 89.1 | 47.54 | yes |
| NTSK | 7.25 | 94.7 | 6.99 | no |
| NUAI | 11.81 | 99.3 | 52.31 | yes |
| OKTA | 6.72 | 93.1 | 6.73 | no |
| PANW | 5.60 | 88.3 | 4.01 | no |

## Focus — ≥ 2 stylists OR top-5 velocity (12 names)

| Symbol | Stylists | Origins | Source | Close | **Chg** | RVOL 10d | ATR% | RSI | ADR% |
|---|---|---|---|---|---|---|---|---|---|
| **ATEN** | 2 | A_stockbee_4pct, C_qullamaggie_rs | `t1` | 32.54 | **+0.56%** | 1.30 | 4.89 | 71.2 | 5.46 |
| **BRBR** | 3 | A_stockbee_4pct, A_tv_breakout_4pct, B_stockbee_ep9m, B_tv_ep9m, C_qullamaggie_rs, TV_volume_breakout | `fresh+t1` | 15.11 | **+10.61%** | 2.39 | 5.72 | 84.4 | 5.75 |
| **FSLY** | 2 | A_stockbee_4pct, B_stockbee_ep9m, G_peoplewish | `t1` | 16.86 | **-5.81%** | 1.03 | 11.62 | 39.5 | 7.90 |
| **GNRC** | 2 | A_stockbee_4pct, G_peoplewish | `t1` | 205.09 | **-0.18%** | 1.39 | 5.96 | 55.7 | 5.64 |
| **NTSK** | 4 | A_stockbee_4pct, A_tv_breakout_4pct, B_tv_ep9m, C_qullamaggie_rs, G_peoplewish, TV_volume_breakout | `fresh+t1` | 24.80 | **+5.51%** | 1.78 | 7.25 | 61.6 | 7.83 |
| **NUAI** | 3 | A_stockbee_4pct, A_tv_breakout_4pct, B_stockbee_ep9m, B_tv_ep9m, C_qullamaggie_rs, TV_volume_breakout | `fresh+t1` | 4.28 | **+7.27%** | 1.69 | 11.81 | 61.5 | 16.17 |
| **OKTA** | 3 | A_stockbee_4pct, A_tv_breakout_4pct, G_peoplewish, TV_volume_breakout | `fresh+t1` | 206.85 | **+5.75%** | 1.84 | 6.72 | 57.6 | 6.94 |
| **PANW** | 3 | A_stockbee_4pct, A_tv_breakout_4pct, B_stockbee_ep9m, B_tv_ep9m, G_peoplewish, TV_volume_breakout | `fresh+t1` | 361.73 | **+6.42%** | 2.51 | 5.60 | 54.6 | 5.31 |
| **QLYS** | 2 | A_stockbee_4pct, G_peoplewish | `t1` | 192.43 | **-2.44%** | 0.90 | 7.61 | 49.6 | 6.80 |
| **S** | 2 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, G_peoplewish | `fresh+t1` | 24.01 | **+2.87%** | 1.04 | 6.21 | 54.0 | 5.99 |
| **SAIL** | 2 | A_stockbee_4pct, G_peoplewish | `t1` | 22.04 | **-0.94%** | 1.13 | 5.86 | 58.6 | 6.00 |
| **TENB** | 2 | A_stockbee_4pct, G_peoplewish | `t1` | 44.09 | **-1.32%** | 1.18 | 7.14 | 53.3 | 6.85 |

- Six of the twelve focus names - ATEN, FSLY, GNRC, QLYS, SAIL, TENB - carry **no fresh trigger**: their `source` is `t1`, so their screen metric describes 18 November, not today's settled bar. Only six names (BRBR, NTSK, NUAI, OKTA, PANW and S) were triggered by today's tape, and five of those are Tier-A.
- The one fresh focus name that is not Tier-A is **S - SentinelOne, $24.01 (+2.87%)**, 2 stylists: the low-beta tail of the same cyber trade.
- The T+1-only names are Wednesday's winners selling into Thursday's reversal, and their screen metrics should not be read as current: **FSLY -5.81%** (a -26% 5-session name that also sits on the parabolic-long book), **QLYS -2.44%** (up 12.9% on Wednesday on the cyber bid), **TENB -1.32%**, **SAIL -0.94%**, **GNRC -0.18%**, **ATEN +0.56%**.
- 14-day velocity is still negative across the board (NTSK -10.25, OKTA -11.83, PANW -10.68), which says the multi-session context is still describing a distribution phase. That is why the book is thin on names that were **not** already extended: in a reversal tape the fresh triggers are late-stage momentum, not early-stage leadership.

## The valuation / quality overlay

The CANSLIM screen asks for growth and strength and nothing else. The overlay adds what the price already assumes, per name, with the values next to the flags.

| Gate | Names | Meaning |
|---|---|---|
| `pass` | 335 | no red flag, and earnings data present |
| `fail` | 618 | at least one red flag (trailing P/E > 50, operating P/E > 40, PEG > 3, negative FCF yield, debt/equity > 1.5, shibui's own earnings-quality flags) |
| `unknown` | 92 | no red flag, **but no reported trailing earnings either** — disclosed, not cleared |

A missing value is a **disclosure, not a flag** and is never counted as a red flag.

## Today's tape — the settled close of 2026-11-19

| Metric | Value |
|---|---|
| Universe | 1066 names (NYSE/NASDAQ/AMEX, stock+dr, mcap > $10B) |
| % above 20 / 50 / 200-DMA | **21.20%** / 38.18% / 38.56% |
| Advance / decline / unchanged | **117 / 939 / 10** (ratio 0.12) |
| Median name | -1.50% |
| VIX / VIX3M | **28.44 / 27.03** (VIX +15.80% from 24.56) |
| SPY / QQQ / RSP / IWM / QQQE | 715.87 (-1.96%) / 645.04 (-2.19%) / 211.63 (-1.76%) / 264.22 (-2.18%) / 109.89 (-1.89%) |

**Biggest movers in the large-cap universe (today's close):**

| Ticker | Name | Close | Chg |
|---|---|---|---|
| INSM | Insmed Incorporated | 144.46 | **+20.58%** |
| TU | Telus Corporation | 10.78 | **+13.35%** |
| PDD | PDD Holdings Inc. | 86.00 | **+11.04%** |
| PANW | Palo Alto Networks, Inc. | 361.73 | **+6.42%** |
| OKTA | Okta, Inc. | 206.85 | **+5.75%** |
| NTSK | Netskope, Inc. | 24.80 | **+5.51%** |
| WWD | Woodward, Inc. | 335.72 | **+5.22%** |
| FUTU | Futu Holdings Limited | 87.21 | **+4.84%** |

**Largest decliners:**

| Ticker | Name | Close | Chg |
|---|---|---|---|
| WSM | Williams-Sonoma, Inc. | 220.66 | -15.16% |
| NTES | NetEase, Inc. | 104.94 | -11.39% |
| ZM | Zoom Communications, Inc. | 83.82 | -9.56% |
| NBIS | Nebius Group N.V. | 96.92 | -9.39% |
| PS | Pershing Square Inc. | 36.84 | -9.26% |
| TWLO | Twilio Inc. | 178.78 | -8.75% |
| TEVA | Teva Pharmaceutical Industries Limited | 38.54 | -8.74% |
| AMD | Advanced Micro Devices, Inc. | 489.19 | -7.72% |

## Parabolic books — the 5-session move (T+1 context)

**Short candidates (3):** the names up 25%+ over five sessions.

| Symbol | m1 (5d) | ADR% | Close | Chg |
|---|---|---|---|---|
| FRMI | 35.91 | 14.77 | 2.06 | -16.26% |
| MOD | 29.26 | 7.80 | 134.56 | -2.41% |
| SLS | 113.18 | 13.12 | 14.86 | -17.21% |

**Long / mean-reversion candidates (20):** the names down 25%+ over five sessions.

| Symbol | m1 (5d) | ADR% | Close | Chg |
|---|---|---|---|---|
| AAOI | -26.98 | 10.95 | 39.46 | -3.26% |
| ACHR | -33.54 | 7.99 | 3.20 | -0.93% |
| ASST | -26.08 | 8.08 | 16.61 | -3.15% |
| ASTS | -30.39 | 10.53 | 25.55 | +0.24% |
| BETA | -27.67 | 7.87 | 18.83 | -6.08% |
| BTDR | -44.67 | 11.80 | 3.41 | -12.34% |
| CTVA | -31.14 | 4.80 | 8.12 | -2.87% |
| FCEL | -29.13 | 9.25 | 7.59 | -2.19% |
| GDS | -30.77 | 6.31 | 14.76 | -5.75% |
| IONQ | -31.06 | 7.87 | 22.71 | -3.28% |
| IREN | -26.87 | 9.76 | 14.41 | -5.45% |
| JOBY | -28.74 | 6.62 | 3.93 | -6.21% |
| MSTR | -26.18 | 5.68 | 86.13 | -4.64% |
| NBIS | -30.86 | 9.17 | 96.92 | -9.39% |
| NVTS | -27.51 | 8.19 | 7.17 | -1.78% |
| QBTS | -27.79 | 7.79 | 7.31 | -4.94% |
| RGTI | -25.02 | 8.15 | 8.06 | -3.24% |
| SMMT | -36.90 | 8.43 | 10.57 | +0.67% |
| SMR | -25.24 | 8.19 | 3.81 | -2.56% |
| TE | -34.74 | 13.57 | 1.29 | -7.19% |

## Per-stylist books

| Stylist | File |
|---|---|
| Stockbee — Pradeep Bonde | `stockbee.md` |
| Qullamägi — Kristjan Kullamägi | `qullamaggie.md` |
| Jeff Sun, CFTe | `jeff-sun.md` |
| Ariel Hernandez | `ariel-hernandez.md` |
| peoplewish — Alec Riffle | `peoplewish.md` |

- The Hernandez branch drew a 165-name theme pool, and the top three sector themes were **XLV, IBB and XLP** - two buckets, **Health Care** (XLV + IBB) and **Consumer Staples** (XLP). 45 names were published.
- That is the textbook defensive bid for a -2% tape with the VIX +15.8%: healthcare and staples led the sector table while semiconductors and packaged software lagged. INSM's +20.58% on the Sanofi report is the loudest single name inside the winning bucket.
- Read it as rotation into defensives, not as a new uptrend - the breadth underneath it (21.2% above the 20-DMA, 939 decliners, the size-cut flag on) is not a healthy tape.

## Method, source health & caveats

**Source health — 2026-11-19**

| Source | Used for | Health |
|---|---|---|
| TradingView scanner (`america/scan`) | fresh trigger book, breadth universe (1,066 names, `totalCount` = rows fetched - no truncation), index ETFs, movers tables | **OK** — the cron day's settled bar, `close` = the official 16:00 ET print |
| shibui-finance (MCP bridge) | 8 context branches, ADR%, CANSLIM growth half, GICS map, valuation/quality overlay | **OK (T+1)** — newest ingested session 2026-11-18; one transient gateway error on the enrichment pass, retried and succeeded |
| Cboe delayed-quote CDN | VIX / VIX3M pair | **DEGRADED — HTTP 403** (Cloudflare) from this egress. Pair read from Yahoo's chart API instead, both symbols from the same session bar; value matches the published session close exactly |
| Bridge `market-recap` | the book's official same-day prints | **OK** — `same-day-prints.md` / `_same-day-prints.json` |
| Yahoo chart API | volatility pair (fallback only) | **OK** — one UA is throttled from this egress, another answers; one pull, session-pinned |

**Degraded sources: 1** (the Cboe volatility CDN). Nothing else was unavailable, and no row was published from a missing value without being disclosed.

**Sources.** TradingView's per-country scanner is the primary source for everything measured on the cron day's settled bar (the fresh trigger book, the breadth universe, the index ETFs and the movers tables); shibui-finance over the MCP-over-HTTP bridge supplies the multi-session context screens (T+1), the ADR%, the CANSLIM growth half and the valuation/quality overlay; the volatility pair comes from the Cboe delayed-quote CDN, or - on this run - from Yahoo's chart API, because the Cboe CDN answered HTTP 403 from this egress (see the flags).

**The two clocks.** The TRIGGER screens (4% breakout, EP9M, 10% gap, volume breakout) are computed on **2026-11-19's own settled bar**; the CONTEXT screens (5-day gainers/losers, 14-day velocity, the coil, the 252-session RS window) stay on shibui's newest ingested session, **2026-11-18**. Every row publishes `data_as_of` and `source` (`fresh` / `t1` / `fresh+t1`), and the two books are never blended. The breadth read in `breadth.md` is NOT T+1 - it is computed from the cron day's settled close.

**Coverage.** Every branch was fetched as its own query, uncapped, and paged until the rows collected equalled `rows_passing`; `rows_kept == rows_passing` on **9 of 9** branches and no branch count lands on a cap (30 / 50 / 60 / 200). 1,269 screened rows -> 1,129 distinct candidates; fresh book 270 names, T+1 book 1,093.

**What could not be verified.** (1) The Cboe volatility CDN was unavailable from this egress, so the VIX/VIX3M pair was served by Yahoo's chart API - cross-checked against the published session close, which matched to the cent, but it is a different vendor than the suite normally uses. (2) The screen metrics are one session behind the close, so the four trigger branches and the context branches describe different tapes by construction. (3) shibui's own quotes are T+1 and its valuation rows are the latest available at or before the resolved date, so the market-cap floor and the overlay inherit that lag. (4) No analyst-consensus or fundamentals feed was used for the multi-session context beyond shibui's quarterly growth columns; the overlay's PEG and P/E come from shibui's `fundamentals_derived_daily` and are as stale as that table is.

**One degraded source, one retry.** The Cboe volatility CDN (HTTP 403) is the only degraded input on this run; the shibui enrichment gateway error was retried and succeeded, so it is not counted as a degradation.

## Files in this directory

| File | What it is |
|---|---|
| `daily-sweep.md` | this file — the primary end-of-day sweep artifact |
| `breadth.md` | the end-of-day breadth & regime read (cron #09) |
| `_regime.json` | regime payload, flat schema v2 — **the canonical slot** |
| `_summary.md` | digest the pre-market brief reads |
| `_results.json` | machine-readable candidate set, tier lists, origins, screen_coverage, the fresh/t1 book split |
| `_cache.json` | cache marker (cron date + resolved data date) |
| `master.md` / `master.csv` | deduped union |
| `focus.md` / `focus.csv` | ≥2 stylists — cron #07 and cron #08 read these |
| `tier-a.md` / `tier-a.csv` | ≥3 stylists |
| `tier-a-fresh.md` / `tier-a-extended.md` | the Tier-A extension split |
| `stockbee.md` / `qullamaggie.md` / `jeff-sun.md` / `ariel-hernandez.md` / `peoplewish.md` | the five per-stylist books |
| `short-candidates.csv` / `long-reversal-candidates.csv` | the parabolic lists, with their defining metric |
| `same-day-prints.md` / `_same-day-prints.json` | today's official close for the book names |
| `breadth-snapshot.*` | cron #10's intraday read — **NOT written by this cron** |
