---
artifact: daily-sweep
contract: SWEEP_PIPELINE_V1
cron: "#09 stock-screener-daily-sweep-18:30"
fire_time_et: "18:30 ET, 2026-11-25 (scheduled fire; window check OK, stall_min 0 — not a replay)"
cron_date: "2026-11-25"
screen_data_date: "2026-11-24 (shibui is T+1 — the multi-session CONTEXT screens describe the previous session)"
fresh_data_date: "2026-11-25 (the cron-day settled bar — the TRIGGER screens: 4% breakout, EP9M, 10% gap, volume breakout)"
print_data_date: "2026-11-25 (official 16:00 ET close, bridge market-recap)"
regime: {size_cut_pct: 0, uncertainty: true, late_cycle: false, index_below_20sma: true, breadth_pct_spx: 41.07}
coverage: "9/9 branches complete (rows_kept == rows_passing on every branch)"
---

# Daily Screener Sweep — Wednesday 25 November 2026 (end-of-day, cron #09)

This run uses the **dual book**: the TRIGGER screens (4% breakout, EP9M, 10% gap, volume breakout) run on **2026-11-25's own settled bar**, while the multi-session CONTEXT screens (5-day gainers/losers, 14-day velocity, the coil, the 252-session RS window) stay on shibui's newest ingested session, **2026-11-24**. Every row publishes which session it describes (`data_as_of` + `source`), and the two are never blended.

## TL;DR

- **Broad tape, broken index posture.** 775 names advanced against 294 declined on the 2026-11-25 close (ratio **2.64**, net +481, median name +0.67%), yet **0 of 5 index ETFs are above their 20-DMA** and only **41.07%** of the $10B+ universe is above its own — a **+41.07 pp BROAD divergence**. The average large cap is healthier than the index; this was not a megacap-led advance.
- **Volatility is the caution flag.** The single VIX/VIX3M pair reads **28.29 / 26.29** (ratio **1.0761**, the VIX itself **+7.32%** on the day) → `uncertainty: true`. `size_cut_pct` stays 0 because breadth sits 1.07 pp above its 40% trigger; `late_cycle` is false (no index more than 6% above its 50-DMA, RSP the extreme at +0.43%).
- **The book is 1,366 names — but Tier-A is 1 fresh / 6 extended.** Seven names cleared ≥3 stylists and six of them already trip the extension label: INSM is +35.9% above its 20-DMA at RSI 82.9, STOK +28.4% at 79.9, NAMS +19.7% at ATR 6.40%. The only unextended name, **IRON**, is a T+1 name — it is not in today's book.
- **Today's own settled bar produced 372 trigger-screen names** (4% breakout 154 · EP9M 219 · volume breakout 82 · 10% gap **0** — only SVRE and ZOAR opened ≥ +10% in the whole $300M+ universe and both fail the $3 close / $50M ADV gates, so the zero is a screen outcome). 83 of them appear only in the fresh book, led by **AGLT +20.4%** and **ACDC +12.7%**.
- **Two branch counts landed on legacy cap values** (`B_stockbee_ep9m` 200, `C_qullamaggie_rs` 60) and both were verified complete — `rows_passing` (COUNT computed inside an uncapped branch) equals `rows_kept`, and no branch SQL carries a per-branch LIMIT. Nothing is truncated.

## Regime at the close

| Flag | Value |
|---|---|
| `size_cut_pct` | **0** (size cut is off - breadth 41.07% is not under the 40% trigger) |
| `uncertainty` | **true** (VIX 28.29 / VIX3M 26.29 = 1.0761) |
| `late_cycle` | **false** (no index ETF > 6% above its 50-DMA; extreme is RSP at +0.43%) |
| `index_below_20sma` | **true** (0 of 5 index ETFs above their 20-DMA) |
| Breadth divergence | **+41.1 pp — BROAD** |

Full breadth read: `breadth.md`. Machine payload: `_regime.json` (flat schema v2, all eight keys, non-empty `atr_extensions`).

## The two books — what each one is, and what it says

| Book | Session | Branches | Names |
|---|---|---|---|
| **FRESH** (primary) | **2026-11-25** — the cron day's settled bar | `A_tv_breakout_4pct` 154 · `B_tv_ep9m` 219 · `D_tv_gap_10pct` 0 · `TV_volume_breakout` 82 | 372 |
| **T+1** (cross-check) | **2026-11-24** — shibui's newest ingested session | 9 branches | 1283 |

| `source` | Meaning | Count |
|---|---|---|
| `fresh+t1` | in both books | 289 |
| `t1` | context screens only | 994 |
| `fresh` | trigger screens only | 83 |

## Screen coverage — the assertion that makes the book publishable

Every branch was fetched as its own query, uncapped, and paged until the rows collected equalled `rows_passing`. **rows_kept == rows_passing on every branch**, and no branch carries a per-branch LIMIT — so no book is capped. A branch count landing on a legacy cap value (30 / 50 / 60 / 200) is only a truncation fingerprint when the SQL could have produced it; 2 branch count(s) land on such a value today and each was verified complete.

| Branch | Screen | rows_passing | rows_kept | Status |
|---|---|---|---|---|
| `A_stockbee_4pct` | Stockbee — Bonde 4% breakout (T+1) | 207 | 207 | complete |
| `B_stockbee_ep9m` | Stockbee — EP9M (T+1) | 200 | 200 | complete — count lands on a legacy cap value, verified: no per-branch LIMIT, rows_passing == rows_kept |
| `K_stockbee_anticipation` | Stockbee — anticipation / coil (T+1) | 496 | 496 | complete |
| `C_qullamaggie_rs` | Qullamägi — RS leaders, 252-session window (T+1) | 60 | 60 | complete — count lands on a legacy cap value, verified: no per-branch LIMIT, rows_passing == rows_kept |
| `D_qullamaggie_ep` | Qullamägi — EP 10% gap (T+1) | 4 | 4 | complete |
| `E_qullamaggie_5d_gainers` | Qullamägi — 5-day gainers, parabolic short (T+1) | 4 | 4 | complete |
| `F_qullamaggie_5d_losers` | Qullamägi — 5-day losers, parabolic long (T+1) | 4 | 4 | complete |
| `G_peoplewish` | peoplewish — ADR% + $vol + 14-day velocity (T+1) | 415 | 415 | complete |
| `H_hernandez_theme` | Hernandez — theme → group → leaders (T+1) | 64 | 64 | complete |

Total screened rows **1454** across the 9 branches → **1366 distinct candidates** after dedup and merge with the fresh book.

## Tier-A — ≥ 3 distinct stylists (7 names)

| Symbol | Stylists | Origins | Source | Close | **Chg** | ADR% | Velocity 14d | m1 (5d) | Ext |
|---|---|---|---|---|---|---|---|---|---|
| **ANF** | 3 | A_stockbee_4pct, A_tv_breakout_4pct, D_qullamaggie_ep, G_peoplewish | `fresh+t1` | 176.96 | **+5.27%** | 5.17 | -1.75 | 13.13 | EXTENDED |
| **COGT** | 3 | A_stockbee_4pct, A_tv_breakout_4pct, G_peoplewish, TV_volume_breakout | `fresh+t1` | 36.08 | **+9.30%** | 6.25 | 4.83 | — | EXTENDED |
| **INSM** | 4 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, C_qullamaggie_rs, D_qullamaggie_ep, E_qullamaggie_5d_gainers, G_peoplewish, H_hernandez_theme | `fresh+t1` | 170.31 | **+0.09%** | 5.29 | 54.68 | 39.63 | EXTENDED |
| **IRON** | 3 | A_stockbee_4pct, G_peoplewish, H_hernandez_theme | `t1` | 89.32 | **+1.11%** | 5.08 | 6.08 | — | — |
| **KSS** | 3 | A_stockbee_4pct, A_tv_breakout_4pct, B_stockbee_ep9m, B_tv_ep9m, G_peoplewish, TV_volume_breakout | `fresh+t1` | 26.70 | **+5.41%** | 5.59 | -0.12 | — | EXTENDED |
| **NAMS** | 3 | A_stockbee_4pct, C_qullamaggie_rs, H_hernandez_theme | `t1` | 24.18 | **-1.10%** | 7.26 | — | — | EXTENDED |
| **STOK** | 4 | A_stockbee_4pct, A_tv_breakout_4pct, C_qullamaggie_rs, H_hernandez_theme, TV_volume_breakout | `fresh+t1` | 35.41 | **+7.83%** | 5.13 | — | — | EXTENDED |

### What Tier-A is saying

- **ANF** — 3 stylists / 4 origins, `fresh+t1`, **+5.27%** to 176.96. The only Tier-A name whose overlay is `pass` (trailing P/E 13.9, operating P/E 10.2, FCF yield +7.6%, D/E 0.95). Extension: ATR 5.46% alone (85th pctile of the $10B+ sub-universe), plus a 4-session up streak.
- **COGT** — 3 stylists, **+9.30%** to 36.08 — the biggest Tier-A move today. Two extension hits (ATR 5.78%, +19.57% above its 20-DMA) and a negative FCF yield (-5.7%) with no reported trailing earnings: momentum, unpriced by fundamentals.
- **INSM** — 4 stylists / 8 origins, the widest agreement in the book — and the most extended name on it: RSI 82.9, +35.89% above its 20-DMA, +39.63% over five sessions, 14-day velocity 54.7. It closed **+0.09%**: the move stopped, the book did not. FCF yield -1.7%.
- **IRON** — 3 stylists and **the only unextended Tier-A name** (no ATR / RSI / 20-DMA / streak hit). It is also the only Tier-A name the fresh book does not contain (`t1`, 2026-11-24; +1.11% today). Overlay flags negative FCF yield (-5.6%).
- **KSS** — 3 stylists / 6 origins, **+5.41%** to 26.70. The cheapest-looking name here (trailing P/E 10.6, FCF yield +37.1%) but debt/equity **1.54** trips the flag. Extension: ATR 5.70% only.
- **NAMS** — 3 stylists, `t1` only (no fresh-book hit), **-1.10%** today. Highest ATR on the list (6.40%, 90th pctile) and +19.69% above its 20-DMA, with price/sales 99 and negative FCF yield — the weakest fundamentals in Tier-A.
- **STOK** — 4 stylists, **+7.83%** to 35.41. RSI 79.9, +28.39% above its 20-DMA, price/sales 75, FCF yield -10.2%. Extension hit twice; the overlay reads `fail` on the yield.

### The extension label — the honest answer to "have these already run?"

**Tier-A is 1 fresh / 6 extended.** Every row carries the label with its reasons; nothing is dropped for tripping it.

| Symbol | ATR% | ATR% pctile ($10B+) | % above 20-DMA | >15% rule |
|---|---|---|---|---|
| ANF | 5.46 | 84.9 | 14.73 | no |
| COGT | 5.78 | 86.5 | 19.57 | yes |
| INSM | 4.35 | 77.3 | 35.89 | yes |
| IRON | 4.91 | 81.8 | 10.48 | no |
| KSS | 5.70 | 86.0 | 11.33 | no |
| NAMS | 6.40 | 90.2 | 19.69 | yes |
| STOK | 4.95 | 81.8 | 28.39 | yes |

## Focus — ≥ 2 stylists OR top-5 velocity (12 names)

| Symbol | Stylists | Origins | Source | Close | **Chg** | RVOL 10d | ATR% | RSI | ADR% |
|---|---|---|---|---|---|---|---|---|---|
| **AMTM** | 2 | A_stockbee_4pct, B_stockbee_ep9m, D_qullamaggie_ep | `t1` | 24.86 | **+0.24%** | 2.28 | 4.64 | 69.5 | 4.31 |
| **ANF** | 3 | A_stockbee_4pct, A_tv_breakout_4pct, D_qullamaggie_ep, G_peoplewish | `fresh+t1` | 176.96 | **+5.27%** | 1.46 | 5.46 | 66.3 | 5.17 |
| **CELC** | 2 | A_stockbee_4pct, G_peoplewish | `t1` | 71.74 | **+5.47%** | 0.94 | 6.66 | 59.3 | 6.82 |
| **COGT** | 3 | A_stockbee_4pct, A_tv_breakout_4pct, G_peoplewish, TV_volume_breakout | `fresh+t1` | 36.08 | **+9.30%** | 2.20 | 5.78 | 66.8 | 6.25 |
| **DKS** | 2 | A_stockbee_4pct, D_qullamaggie_ep | `t1` | 158.59 | **+3.54%** | 1.42 | 4.66 | 61.6 | 4.23 |
| **INSM** | 4 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, C_qullamaggie_rs, D_qullamaggie_ep, E_qullamaggie_5d_gainers, G_peoplewish, H_hernandez_theme | `fresh+t1` | 170.31 | **+0.09%** | 2.70 | 4.35 | 82.9 | 5.29 |
| **IRON** | 3 | A_stockbee_4pct, G_peoplewish, H_hernandez_theme | `t1` | 89.32 | **+1.11%** | 0.62 | 4.91 | 65.2 | 5.08 |
| **KSS** | 3 | A_stockbee_4pct, A_tv_breakout_4pct, B_stockbee_ep9m, B_tv_ep9m, G_peoplewish, TV_volume_breakout | `fresh+t1` | 26.70 | **+5.41%** | 1.89 | 5.70 | 62.9 | 5.59 |
| **MMED** | 2 | A_stockbee_4pct, B_stockbee_ep9m, G_peoplewish | `t1` | 18.84 | **-1.21%** | 1.21 | 5.89 | 54.2 | 5.83 |
| **NAMS** | 3 | A_stockbee_4pct, C_qullamaggie_rs, H_hernandez_theme | `t1` | 24.18 | **-1.10%** | 0.73 | 6.40 | 64.8 | 7.26 |
| **NNNN** | 2 | A_stockbee_4pct, TV_volume_breakout | `fresh+t1` | 3.65 | **+8.63%** | 2.44 | 15.00 | 46.9 | 12.09 |
| **STOK** | 4 | A_stockbee_4pct, A_tv_breakout_4pct, C_qullamaggie_rs, H_hernandez_theme, TV_volume_breakout | `fresh+t1` | 35.41 | **+7.83%** | 1.75 | 4.95 | 79.9 | 5.13 |

- **Six of the twelve are on today's settled bar** (ANF, COGT, INSM, KSS, NNNN, STOK) and six are context-only from the 2026-11-24 session (AMTM, CELC, DKS, IRON, MMED, NAMS) — a context-only name did not re-trigger today, which is the T+1 lag the dual book exists to expose.
- **IRON is the only Focus name that is unextended.** Every other Focus name trips at least one extension rule (ATR% > 5, RSI > 75, > 15% above the 20-DMA, or a 3+ up-session streak) — the Focus list is structurally biased toward names that have already run.
- **Overlay split: 3 `pass` (AMTM, ANF, DKS), 8 `fail`, 1 `unknown` (NNNN).** The `unknown` is a disclosure, not a clearance: NNNN has no reported trailing earnings.
- **NNNN is the tail risk in the book** — 3.65 close, ATR **15.00%**, ADR% 12.09, +8.63% today. The volatility is the fact here; the screen simply caught a thin, violent name.
- **DKS** (+3.54%, 2 stylists, `t1`, overlay `pass`) is the one Focus name that is both fundamentally unflagged and cheap — trailing P/E 16.3, PEG 0.31 — but it did not re-trigger on today's bar.
- **AMTM** (+0.24%, `t1`, overlay `pass`, trailing P/E 29.7) and **CELC** (+5.47%, `t1`, FCF yield -7.9%) are context-only; CELC's move came without a volume or stylist confirmation on today's bar.
- The four parabolic longs (BTDR +9.71%, SHAZ -0.30%, SLS -3.62%, SNEX -5.03%) sit in the same five-session drawdown band the mean-reversion screen is built on, with ADR% 13.8-14.6 — that spread is the volatility, not a signal.

## The valuation / quality overlay

The CANSLIM screen asks for growth and strength and nothing else. The overlay adds what the price already assumes, per name, with the values next to the flags.

| Gate | Names | Meaning |
|---|---|---|
| `pass` | 359 | no red flag, and earnings data present |
| `fail` | 729 | at least one red flag (trailing P/E > 50, operating P/E > 40, PEG > 3, negative FCF yield, debt/equity > 1.5, shibui's own earnings-quality flags) |
| `unknown` | 93 | no red flag, **but no reported trailing earnings either** — disclosed, not cleared |

A missing value is a **disclosure, not a flag** and is never counted as a red flag.

## Today's tape — the settled close of 2026-11-25

| Metric | Value |
|---|---|
| Universe | 1086 names (NYSE/NASDAQ/AMEX, stock+dr, mcap > $10B) |
| % above 20 / 50 / 200-DMA | **41.07%** / 47.05% / 43.28% |
| Advance / decline / unchanged | **775 / 294 / 17** (ratio 2.64) |
| Median name | +0.67% |
| VIX / VIX3M | **28.29 / 26.29** (VIX +7.32% from 26.36) |
| SPY / QQQ / RSP / IWM / QQQE | 716.70 (-0.29%) / 633.93 (-0.65%) / 215.74 (+0.83%) / 268.87 (+0.65%) / 109.84 (+0.24%) |

**Biggest movers in the large-cap universe (today's close):**

| Ticker | Name | Close | Chg |
|---|---|---|---|
| HPQ | HP Inc. | 31.15 | **+11.49%** |
| LI | Li Auto Inc. | 11.88 | **+11.03%** |
| ASTS | AST SpaceMobile, Inc. | 26.02 | **+10.25%** |
| QXO | QXO, Inc. | 11.97 | **+8.62%** |
| CHTR | Charter Communications, Inc. | 147.27 | **+8.39%** |
| QXO/PB | QXO, Inc. Depositary Shares, each representi | 36.28 | **+8.36%** |
| BSP | Bending Spoons S.p.A. | 46.29 | **+8.00%** |
| CNH | CNH Industrial N.V. | 11.88 | **+8.00%** |

**Largest decliners:**

| Ticker | Name | Close | Chg |
|---|---|---|---|
| NTNX | Nutanix, Inc. | 46.30 | -15.19% |
| LRCX | Lam Research Corporation | 185.01 | -5.68% |
| SNDK | Sandisk Corporation | 73.61 | -5.57% |
| WSO.B | Watsco, Inc. | 296.40 | -5.38% |
| ORCL | Oracle Corporation | 103.88 | -5.13% |
| MU | Micron Technology, Inc. | 601.25 | -4.53% |
| DDOG | Datadog, Inc. | 158.25 | -4.31% |
| J | Jacobs Solutions Inc. | 145.49 | -4.27% |

## Parabolic books — the 5-session move (T+1 context)

**Short candidates (4):** the names up 25%+ over five sessions.

| Symbol | m1 (5d) | ADR% | Close | Chg |
|---|---|---|---|---|
| BRBR | 37.24 | 6.65 | 15.66 | +3.64% |
| INSM | 39.63 | 5.29 | 170.31 | +0.09% |
| KYMR | 43.12 | 6.62 | 173.77 | -0.09% |
| ZS | 25.07 | 6.24 | 230.86 | -0.33% |

**Long / mean-reversion candidates (4):** the names down 25%+ over five sessions.

| Symbol | m1 (5d) | ADR% | Close | Chg |
|---|---|---|---|---|
| BTDR | -30.50 | 13.78 | 3.05 | +9.71% |
| SHAZ | -25.81 | 14.56 | 16.71 | -0.30% |
| SLS | -30.81 | 14.21 | 12.77 | -3.62% |
| SNEX | -30.52 | 5.18 | 36.23 | -5.03% |

## Per-stylist books

| Stylist | File |
|---|---|
| Stockbee — Pradeep Bonde | `stockbee.md` |
| Qullamägi — Kristjan Kullamägi | `qullamaggie.md` |
| Jeff Sun, CFTe | `jeff-sun.md` |
| Ariel Hernandez | `ariel-hernandez.md` |
| peoplewish — Alec Riffle | `peoplewish.md` |

The Hernandez **theme → group → leaders** funnel ranked the 29 sector ETFs by composite 1M/3M/6M relative strength and selected **IBB, XLV and XLP** — two health-care themes and staples — which map to the GICS buckets **Health Care** and **Consumer Staples**. The fresh-book candidate pool (187 names) was enriched with the shibui GICS mapping and narrowed to the **64-name theme book**. Inside those buckets the multi-stylist names are **INSM** (4 stylists, 14-day velocity 54.7), **CGON** and **DNTH** (4 each), and **GMAB, IMVT, ADMA, KNSA** (3 each) — the health-care cluster carries the theme, while the staples side is thinner (CPB, ELAN, BHC). This lines up with today's industry-breadth table, where Biotechnology sits at 72.2% above its 20-DMA and Pharmaceuticals: Major at 70.0%, against Semiconductors at 3.0% and Integrated Oil at 4.5%: leadership is defensive, not cyclical.

## Method, source health & caveats

**Source health — per source, per call, with status.**

| Source | Endpoint / call | Status |
|---|---|---|
| TradingView scanner | `POST scanner.tradingview.com/america/scan` — fresh universe 3,728 names; breadth universe 1,086 names | **ok** (`totalCount` = rows fetched on both pulls) |
| shibui-finance (MCP-over-HTTP bridge) | `stock_data_query` — 9 branches, ADR%/streak/GICS enrichment, CANSLIM growth half, overlay on 1,181 symbols | **ok** |
| bridge `market-recap` | `get_quotes` batch for the book names (`market_state: post`) | **ok** |
| bridge `market-recap` | `top_movers` for the large-cap movers table | **ok** |
| Yahoo chart API | `^VIX` / `^VIX3M`, same session bar, quote time 2026-11-25 16:15:01 ET | **ok** (fallback) |
| Cboe delayed-quote CDN | `cdn.cboe.com/api/global/delayed_quotes/quotes/_VIX.json` | **failed: HTTP 403 (Cloudflare)** → Yahoo fallback used, named in the artifact |
| Nasdaq public quote API | same-day prints | not used — the bridge's official close served this column |
| Finviz | — | not used (retired from the source chain) |

**degraded_sources: 1** (Cboe VIX CDN → Yahoo chart-API fallback). No other source failed, and no symbol was dropped for an unqueried source.

**Sources — every one named, with its status.**

| Source | Used for | Status |
|---|---|---|
| TradingView scanner (`POST scanner.tradingview.com/america/scan`) | the FRESH trigger book (3,728 names, mcap > $300M) and the settled breadth layer (1,086 names, mcap > $10B) | **ok** — `totalCount` equals rows fetched on both pulls, so neither book is truncated |
| shibui-finance over the MCP-over-HTTP bridge (`shibui stock_data_query`) | 9 context branches on the 2026-11-24 session, the ADR%/streak/GICS enrichment, the CANSLIM growth half, the valuation/quality overlay (1,181 symbols) | **ok** |
| bridge `market-recap get_quotes` | the official 16:00 ET close for every book name (`market_state: post`) | **ok** |
| Yahoo chart API (`^VIX` / `^VIX3M`) | the single volatility pair (quote time 2026-11-25 16:15:01 ET) | **ok** — but see the degraded source below |
| Cboe delayed-quote CDN | the primary volatility pair | **failed: HTTP 403 (Cloudflare)** from this egress |
| Finviz | — | not used (retired from the source chain) |

**degraded_sources: 1** — the Cboe delayed-quote CDN. The volatility pair came from the documented Yahoo chart-API fallback instead, with `^VIX` and `^VIX3M` read from the **same session bar** and published as one pair everywhere in these files.

**Sessions and lag.** The SCREEN metrics in `daily-sweep.md` describe shibui's newest ingested session, **2026-11-24** — shibui is T+1. The breadth numbers and the trigger book describe the **2026-11-25 settled close**. Every row publishes `data_as_of` and `source` (`fresh` / `t1` / `fresh+t1`); the two books are never blended.

**Coverage.** All 9 context branches and all 4 fresh branches were fetched as one query per branch, uncapped, and paged until the rows collected equalled `rows_passing` (`COUNT(*) OVER ()` computed inside the branch, before any cap). `rows_kept == rows_passing` on every branch. Two context counts land on a legacy cap value — `B_stockbee_ep9m` 200 and `C_qullamaggie_rs` 60 — and both were verified complete: the branch SQL carries no per-branch LIMIT, so `rows_passing` is the true passing count rather than a cap. The 10% gap branch's 0 is a screen outcome (two names in the universe opened ≥ +10%, both failing the $3 close and $50M ADV gates).

**What could not be verified.** The same-day close column comes from the bridge's `market-recap` batch (`market_state: post`) rather than a Nasdaq `/info` `secondaryData` pull — both carry the official 16:00 ET print, but they are different publishers and were not cross-checked against each other here. No catalyst was sourced for any name in this artifact: the movers tables are price facts, and nothing in them should be read as an explained move.

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
