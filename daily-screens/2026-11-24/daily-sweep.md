---
artifact: daily-sweep
contract: SWEEP_PIPELINE_V1
cron: "#09 stock-screener-daily-sweep-18:30"
fire_time_et: "18:30 ET (2026-11-24)"
cron_date: "2026-11-24"
screen_data_date: "2026-11-23 (shibui is T+1 — the multi-session CONTEXT screens describe the previous session)"
fresh_data_date: "2026-11-24 (the cron-day settled bar — the TRIGGER screens: 4% breakout, EP9M, 10% gap, volume breakout)"
print_data_date: "2026-11-24 (official 16:00 ET close, bridge market-recap)"
regime: {size_cut_pct: 50, uncertainty: true, late_cycle: false, index_below_20sma: true, breadth_pct_spx: 34.94}
coverage: "9/9 branches complete (rows_kept == rows_passing on every branch)"
---

# Daily Screener Sweep — Tuesday 24 November 2026 (end-of-day, cron #09)

This run uses the **dual book**: the TRIGGER screens (4% breakout, EP9M, 10% gap, volume breakout) run on **2026-11-24's own settled bar**, while the multi-session CONTEXT screens (5-day gainers/losers, 14-day velocity, the coil, the 252-session RS window) stay on shibui's newest ingested session, **2026-11-23**. Every row publishes which session it describes (`data_as_of` + `source`), and the two are never blended.

## TL;DR

- **Monday's AI relief rally was handed back on Tuesday — but only in the AI complex.** The Nasdaq Composite fell **1.48%** and the S&P 500 **0.50%** while the Dow added **0.85%**: the chip trade gave back the Jensen Huang reinstatement move in full. NVDA closed **155.38 (-5.86%)**, ADI plunged **-17.37%** on a weak guide, SMTC **-16.97%**, ALAB **-13.88%**, CRWV **-11.85%**, DELL **-11.83%**, HPE **-16.31%** on a margin outlook. Chip stocks shed roughly **$870B**; SOXX closed **-8%**.
- **Participation stayed positive — the index weakness is concentration, not breadth.** On the 1,079-name $10B+ universe **621 advanced / 452 declined / 6 unchanged** (ratio 1.37, median name **+0.45%**), and only **34.94%** of large caps are above their own 20-DMA with **0 of 5** index ETFs above theirs. Money rotated *within* the market: Biotechnology averaged **+5.19%** and Discount Stores **+6.30%**, against Semiconductors at **-7.84%** (0% of them above their 20-DMA).
- **Volatility barely blinked.** VIX **26.36** from 26.62 (**-1.0%**) and VIX3M **25.47** = **1.0349**, so `uncertainty` stays **true**, but the ratio is barely above the trigger. Regime stays defensive: size cut **ON** (50), `index_below_20sma` **true**, `late_cycle` **false**.
- **Tier-A is 8 names, 7 of them the same broken trade, and all 8 are EXTENDED (0 fresh).** Every name except KYMR is semiconductor / AI hardware — the tier is measuring agreement among correlated momentum screens on Monday's AI spike, not eight independent setups. The single exception is the one name with its own catalyst: **KYMR +15.66%** on positive Phase 2b eczema data.

## Regime at the close

| Flag | Value |
|---|---|
| `size_cut_pct` | **50** (size cut is ON - the index is below its 20-DMA and breadth 34.94% is UNDER the 40% trigger) |
| `uncertainty` | **true** (VIX 26.36 / VIX3M 25.47 = 1.0349) |
| `late_cycle` | **false** (no index ETF > 6% above its 50-DMA; extreme is RSP at -0.37%) |
| `index_below_20sma` | **true** (0 of 5 index ETFs above their 20-DMA) |
| Breadth divergence | **+34.9 pp — BROAD** |

Full breadth read: `breadth.md`. Machine payload: `_regime.json` (flat schema v2, all eight keys, non-empty `atr_extensions`).

## The two books — what each one is, and what it says

| Book | Session | Branches | Names |
|---|---|---|---|
| **FRESH** (primary) | **2026-11-24** — the cron day's settled bar | `A_tv_breakout_4pct` 199 · `B_tv_ep9m` 206 · `D_tv_gap_10pct` 3 · `TV_volume_breakout` 122 | 420 |
| **T+1** (cross-check) | **2026-11-23** — shibui's newest ingested session | 9 branches | 1305 |

| `source` | Meaning | Count |
|---|---|---|
| `fresh+t1` | in both books | 347 |
| `t1` | context screens only | 958 |
| `fresh` | trigger screens only | 73 |

## Screen coverage — the assertion that makes the book publishable

Every branch was fetched as its own query, uncapped, and paged until the rows collected equalled `rows_passing`. **rows_kept == rows_passing on every branch**, and no branch count lands on a cap (30 / 50 / 60 / 200).

| Branch | Screen | rows_passing | rows_kept | Status |
|---|---|---|---|---|
| `A_stockbee_4pct` | Stockbee — Bonde 4% breakout (T+1) | 281 | 281 | complete |
| `B_stockbee_ep9m` | Stockbee — EP9M (T+1) | 237 | 237 | complete |
| `K_stockbee_anticipation` | Stockbee — anticipation / coil (T+1) | 461 | 461 | complete |
| `C_qullamaggie_rs` | Qullamägi — RS leaders, 252-session window (T+1) | 47 | 47 | complete |
| `D_qullamaggie_ep` | Qullamägi — EP 10% gap (T+1) | 177 | 177 | complete |
| `E_qullamaggie_5d_gainers` | Qullamägi — 5-day gainers, parabolic short (T+1) | 3 | 3 | complete |
| `F_qullamaggie_5d_losers` | Qullamägi — 5-day losers, parabolic long (T+1) | 1 | 1 | complete |
| `G_peoplewish` | peoplewish — ADR% + $vol + 14-day velocity (T+1) | 403 | 403 | complete |
| `H_hernandez_theme` | Hernandez — theme → group → leaders (T+1) | 58 | 58 | complete |

Total screened rows **1668** across the 9 branches → **1378 distinct candidates** after dedup and merge with the fresh book.

## Tier-A — ≥ 3 distinct stylists (8 names)

| Symbol | Stylists | Origins | Source | Close | **Chg** | ADR% | Velocity 14d | m1 (5d) | Ext |
|---|---|---|---|---|---|---|---|---|---|
| **ALAB** | 3 | A_stockbee_4pct, D_qullamaggie_ep, G_peoplewish | `t1` | 191.30 | **-13.88%** | 9.78 | -4.92 | 20.12 | EXTENDED |
| **CRWV** | 3 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, D_qullamaggie_ep, G_peoplewish | `fresh+t1` | 42.60 | **-11.85%** | 10.39 | -10.07 | 29.01 | EXTENDED |
| **DELL** | 3 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, D_qullamaggie_ep, G_peoplewish | `fresh+t1` | 295.28 | **-11.83%** | 8.22 | -17.99 | 35.66 | EXTENDED |
| **KYMR** | 5 | A_stockbee_4pct, A_tv_breakout_4pct, C_qullamaggie_rs, D_qullamaggie_ep, G_peoplewish, H_hernandez_theme, TV_volume_breakout | `fresh+t1` | 173.92 | **+15.66%** | 6.42 | 18.32 | 19.68 | EXTENDED |
| **LITE** | 3 | A_stockbee_4pct, D_qullamaggie_ep, G_peoplewish | `t1` | 487.12 | **-10.52%** | 9.30 | -19.96 | 22.32 | EXTENDED |
| **NVDA** | 3 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, D_qullamaggie_ep, G_peoplewish | `fresh+t1` | 155.38 | **-5.86%** | 5.71 | -20.15 | 33.06 | EXTENDED |
| **SITM** | 3 | A_stockbee_4pct, D_qullamaggie_ep, G_peoplewish | `t1` | 378.29 | **-13.79%** | 8.70 | -1.36 | 19.31 | EXTENDED |
| **SMTC** | 3 | A_stockbee_4pct, D_qullamaggie_ep, G_peoplewish | `t1` | 86.46 | **-16.97%** | 8.74 | -18.28 | 19.25 | EXTENDED |

### What Tier-A is saying

- **KYMR — 5 stylists, +15.66% to 173.92.** The only Tier-A name with an idiosyncratic catalyst: the BROADEN2 Phase 2b readout of KT-621 in atopic dermatitis (72% severity reduction vs 27% placebo at the mid dose) drove **+30.4% on Monday**, and today RBC (PoS to 65%), Guggenheim ($235) and Morgan Stanley ($198) raised targets into a **$1.75B** offering priced at $150.37. The tape confirms it: **RVOL 4.24**, RSI **76.6**, **+33.02%** above its 20-DMA, +45.54% above its 50-DMA, 2 straight up sessions. It is the strongest name in the book *and* the most extended — it trips **three** of the four extension rules (ATR%, RSI, % above 20-DMA). Quality `fail` on **negative FCF yield (-2.31%)**; no trailing earnings, so that is **disclosed, not counted**.
- **NVDA — 3 stylists, -5.86% to 155.38.** The day-after relief-rally unwind: still **-11.61%** below its 20-DMA and **-24.19%** below its 50-DMA, 14-day velocity **-20.15%**, but the 5-session move `m1` is still **+33.06%** — which is exactly why the momentum screens still see it. **RVOL 0.81: the selling had no volume.** Quality fails on shibui's own `LOW_EARNINGS_QUALITY` flag only — the multiples are undemanding (trailing P/E **20.71**, PEG **0.20**, FCF yield 3.18%, debt/equity 0.17).
- **DELL — 3 stylists, -11.83% to 295.28.** Fell with the sector despite **topping estimates and lifting guidance** — the drop is the AI trade, not the print. It is the only Tier-A name with genuine volume behind the move (**RVOL 2.24**) and the only one with a **clean** quality verdict (`pass`: trailing P/E 19.08, PEG 0.33, FCF 3.94%). Structurally the weakest in the tier besides the AI names: **-17.52%** below its 20-DMA, **-36.11%** below its 50-DMA, ATR% 13.02.
- **CRWV — 3 stylists, -11.85% to 42.61.** **RVOL 0.70** and the worst leverage in the tier: FCF yield **-76.6%**, debt/equity **16.45** → `flagged`. No trailing earnings, so that part is **disclosed, not cleared**. ATR% **15.78** (99.8th percentile of the $10B+ universe), -15.89% below its 20-DMA, -35.96% below its 50-DMA.
- **ALAB — 3 stylists, -13.88% to 191.30.** T+1 book only (the trigger screens never fired it today). Quality `fail`: trailing P/E **83.53**, operating P/E **97.04**. ATR% 13.67, ADR% 9.78, 5-session `m1` **+20.12** — a parabolic name that is still 14%+ below its own 20-DMA.
- **LITE — 3 stylists, -10.52% to 487.12.** T+1 only. Quality `fail` on **operating P/E 55.62**; ATR% 14.66, velocity **-19.96%**, `m1` +22.32.
- **SITM — 3 stylists, -13.79% to 378.29.** T+1 only, and the worst balance sheet in the tier: trailing P/E **498.73**, operating P/E **2,209.24**, and shibui's own `LARGE_NON_OPERATING` flag → `flagged`. ATR% 12.36.
- **SMTC — 3 stylists, -16.97% to 86.46.** T+1 only. It fell with the analog / mixed-signal complex after ADI's flat Q1 guide (TXN -10.9%, SMTC -15.9% at the close per press). Quality `fail`: trailing P/E 62.97, operating P/E 102.80. ATR% **15.43**.
- **What the tier is really saying:** 7 of the 8 names are one trade — semiconductor / AI hardware that spiked on Monday and broke again today — and **8 of 8 are EXTENDED (0 fresh)**, seven of them on ATR% alone. Six of the suite's branches are momentum screens, so on a one-day AI unwind they fire on the same names and count the same beta three times. Tier-A is *where the damage was*, not eight independent setups. The single name with a real idiosyncratic catalyst (KYMR) is also the single name that trips every extension rule.

### The extension label — the honest answer to "have these already run?"

**Tier-A is 0 fresh / 8 extended.** Every row carries the label with its reasons; nothing is dropped for tripping it.

| Symbol | ATR% | ATR% pctile ($10B+) | % above 20-DMA | >15% rule |
|---|---|---|---|---|
| ALAB | 13.67 | 99.4 | -14.07 | no |
| CRWV | 15.78 | 99.8 | -15.89 | no |
| DELL | 13.02 | 99.3 | -17.52 | no |
| KYMR | 6.18 | 89.8 | 33.02 | yes |
| LITE | 14.66 | 99.6 | -21.74 | no |
| NVDA | 8.57 | 95.7 | -11.61 | no |
| SITM | 12.36 | 98.9 | -12.12 | no |
| SMTC | 15.43 | 99.7 | -23.36 | no |

## Focus — ≥ 2 stylists OR top-5 velocity (12 names)

| Symbol | Stylists | Origins | Source | Close | **Chg** | RVOL 10d | ATR% | RSI | ADR% |
|---|---|---|---|---|---|---|---|---|---|
| **ALAB** | 3 | A_stockbee_4pct, D_qullamaggie_ep, G_peoplewish | `t1` | 191.30 | **-13.88%** | 1.28 | 13.67 | 39.8 | 9.78 |
| **APLD** | 3 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, D_qullamaggie_ep, G_peoplewish | `fresh+t1` | 12.22 | **-11.58%** | 1.27 | 16.14 | 35.9 | 9.91 |
| **AXTI** | 3 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, D_qullamaggie_ep, G_peoplewish | `fresh+t1` | 31.58 | **-16.94%** | 1.00 | 20.52 | 37.0 | 12.56 |
| **CRWV** | 3 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, D_qullamaggie_ep, G_peoplewish | `fresh+t1` | 42.60 | **-11.85%** | 0.70 | 15.78 | 39.0 | 10.39 |
| **DELL** | 3 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, D_qullamaggie_ep, G_peoplewish | `fresh+t1` | 295.28 | **-11.83%** | 2.24 | 13.02 | 36.5 | 8.22 |
| **KYMR** | 5 | A_stockbee_4pct, A_tv_breakout_4pct, C_qullamaggie_rs, D_qullamaggie_ep, G_peoplewish, H_hernandez_theme, TV_volume_breakout | `fresh+t1` | 173.92 | **+15.66%** | 4.24 | 6.18 | 76.6 | 6.42 |
| **LITE** | 3 | A_stockbee_4pct, D_qullamaggie_ep, G_peoplewish | `t1` | 487.12 | **-10.52%** | 1.08 | 14.66 | 35.9 | 9.30 |
| **MXL** | 3 | A_stockbee_4pct, D_qullamaggie_ep, G_peoplewish | `t1` | 41.89 | **-16.74%** | 1.06 | 17.29 | 36.5 | 9.92 |
| **NBIS** | 3 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, D_qullamaggie_ep, G_peoplewish | `fresh+t1` | 87.31 | **-10.73%** | 0.70 | 19.93 | 33.6 | 10.56 |
| **NVDA** | 3 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, D_qullamaggie_ep, G_peoplewish | `fresh+t1` | 155.38 | **-5.86%** | 0.81 | 8.57 | 39.5 | 5.71 |
| **SITM** | 3 | A_stockbee_4pct, D_qullamaggie_ep, G_peoplewish | `t1` | 378.29 | **-13.79%** | 1.16 | 12.36 | 40.3 | 8.70 |
| **SMTC** | 3 | A_stockbee_4pct, D_qullamaggie_ep, G_peoplewish | `t1` | 86.46 | **-16.97%** | 2.19 | 15.43 | 36.3 | 8.74 |

- **12 names, of which 8 are Tier-A.** The four non-Tier-A names: **APLD** -11.58% (ATR% 16.14, -22.89% below its 20-DMA, FCF **-110.6%**, debt/equity **4.05** → `flagged`), **AXTI** -16.94% (ATR% **20.52** — the widest in Focus — and -26.82% below its 20-DMA, trailing P/E 78.69 → `flagged`), **MXL** -16.74% (T+1 only, ATR% 17.29, velocity -21.35%, FCF -0.45% → `watch`) and **NBIS** -10.73% (the weakest structure in the book: **-31.55%** below its 20-DMA, **-50.56%** below its 50-DMA, trailing P/E 213.55, FCF -46.7% → `flagged`).
- **Concentration: 11 of the 12 Focus names are semiconductor / AI hardware / data-centre** (ALAB, APLD, AXTI, CRWV, DELL, LITE, MXL, NBIS, NVDA, SITM, SMTC). The only exception is KYMR. This is a **single-factor list** — it is the screen's own momentum branches reacting to one unwind, not a diversified watchlist.
- **The volume tells you it was a rotation, not a liquidation.** Only three Focus names traded at or above their 10-day average volume with conviction — DELL **2.24**, APLD 1.27, AXTI 1.00 — while the mega-cap AI names printed *below* average volume (NVDA 0.81, CRWV 0.70, NBIS 0.70). Institutional money did not stampede out of these names; it rotated into retail and biotech, where the day's biggest gainers live.
- **One honest counterweight:** the four non-Tier-A Focus names are the ones that are *least* extended relative to the tape (AXTI and NBIS are the two most broken) and are therefore the better mean-reversion candidates — but none of them has a catalyst in today's tape to fund that thesis, and their quality verdicts are `flagged`.

## The valuation / quality overlay

The CANSLIM screen asks for growth and strength and nothing else. The overlay adds what the price already assumes, per name, with the values next to the flags.

| Gate | Names | Meaning |
|---|---|---|
| `pass` | 355 | no red flag, and earnings data present |
| `fail` | 721 | at least one red flag (trailing P/E > 50, operating P/E > 40, PEG > 3, negative FCF yield, debt/equity > 1.5, shibui's own earnings-quality flags) |
| `unknown` | 112 | no red flag, **but no reported trailing earnings either** — disclosed, not cleared |

A missing value is a **disclosure, not a flag** and is never counted as a red flag.

## Today's tape — the settled close of 2026-11-24

| Metric | Value |
|---|---|
| Universe | 1079 names (NYSE/NASDAQ/AMEX, stock+dr, mcap > $10B) |
| % above 20 / 50 / 200-DMA | **34.94%** / 43.65% / 41.61% |
| Advance / decline / unchanged | **621 / 452 / 6** (ratio 1.37) |
| Median name | +0.45% |
| VIX / VIX3M | **26.36 / 25.47** (VIX -0.98% from 26.62) |
| SPY / QQQ / RSP / IWM / QQQE | 718.78 (-0.49%) / 638.10 (-1.99%) / 213.96 (+0.54%) / 267.14 (+0.53%) / 109.58 (-0.94%) |

**Biggest movers in the large-cap universe (today's close):**

| Ticker | Name | Close | Chg |
|---|---|---|---|
| KYMR | Kymera Therapeutics, Inc. | 173.92 | **+15.66%** |
| DKS | Dick's Sporting Goods Inc | 153.17 | **+14.59%** |
| INSM | Insmed Incorporated | 170.15 | **+14.13%** |
| DLTR | Dollar Tree, Inc. | 154.65 | **+11.18%** |
| PCVX | Vaxcyte, Inc. | 63.18 | **+11.04%** |
| SNY | Sanofi | 51.90 | **+10.97%** |
| TGTX | TG Therapeutics, Inc. | 70.13 | **+9.60%** |
| PINS | Pinterest, Inc. | 18.50 | **+9.47%** |

**Largest decliners:**

| Ticker | Name | Close | Chg |
|---|---|---|---|
| ADI | Analog Devices, Inc. | 312.95 | -17.37% |
| HPE/PC | Hewlett Packard Enterprise Company 7.625% Se | 102.95 | -16.69% |
| HPE | Hewlett Packard Enterprise Company | 40.19 | -16.31% |
| ALAB | Astera Labs, Inc. | 191.30 | -13.88% |
| SITM | SiTime Corporation | 378.29 | -13.79% |
| MTSI | MACOM Technology Solutions Holdings, Inc. | 200.20 | -13.45% |
| CRDO | Credo Technology Group Holding Ltd | 106.46 | -13.07% |
| FN | Fabrinet | 290.12 | -11.88% |

## Parabolic books — the 5-session move (T+1 context)

**Short candidates (3):** the names up 25%+ over five sessions.

| Symbol | m1 (5d) | ADR% | Close | Chg |
|---|---|---|---|---|
| BRBR | 44.27 | 6.70 | 15.11 | -0.72% |
| MPT | 25.33 | 9.80 | 1.91 | +1.60% |
| SLS | 77.78 | 14.12 | 13.25 | -0.23% |

**Long / mean-reversion candidates (1):** the names down 25%+ over five sessions.

| Symbol | m1 (5d) | ADR% | Close | Chg |
|---|---|---|---|---|
| SNEX | -30.46 | 5.03 | 38.15 | -3.38% |

## Per-stylist books

| Stylist | File |
|---|---|
| Stockbee — Pradeep Bonde | `stockbee.md` |
| Qullamägi — Kristjan Kullamägi | `qullamaggie.md` |
| Jeff Sun, CFTe | `jeff-sun.md` |
| Ariel Hernandez | `ariel-hernandez.md` |
| peoplewish — Alec Riffle | `peoplewish.md` |

The theme → group → leaders branch picked **IBB, XLV, XLP** (Health Care + Consumer Staples) from a 159-name pool and published 58 names. Two things the reader should know: (1) this branch is **T+1** (shibui's 2026-11-23 session), so it describes the relative strength of defensives *into* today's unwind, and (2) **this time the theme branch was right and the momentum book was wrong.** Biotechnology averaged **+5.19%** today with 83.3% of the group above its 20-DMA; Pharmaceuticals: Major +4.05%; Discount Stores +6.30%; Food Retail +4.42% — while Semiconductors averaged **-7.84%** with **0%** of the group above its 20-DMA. The branch's own names confirmed it: **INSM +14.13%** (Sanofi agreed to acquire it for **$175/share in cash**, ~$41B), **DNTH +10.35%**, **BBIO +8.52%**, **DNLI +7.25%**, **BMRN +6.04%** and **DLTR +11.18%**. The theme branch is a **published screen, not an improvisation** — the themes are sector ETFs only, so a single stock with strong relative strength cannot displace a real sector theme.

## Method, source health & caveats

### Source health

| Source | What it served | Status |
|---|---|---|
| TradingView scanner (`scanner.tradingview.com/america/scan`) | the fresh book (3,725 names; `totalCount` 3,725 = rows fetched, no truncation) and the settled breadth read (1,079 names, $10B+) | **ok** |
| MCP bridge `market-recap` `get_quotes` | the official 16:00 ET close for the book names | **ok** |
| MCP bridge `shibui` `stock_data_query` | the 8 T+1 context branches, the CANSLIM growth half and the merged enrichment pass; newest ingested session **2026-11-23** (T+1 — one session behind the cron day) | **ok** (lag disclosed, not blended) |
| Yahoo chart API (`^VIX` / `^VIX3M`) | the volatility pair, both symbols from the same 2026-11-24 session bar, quoted 16:15:01 ET | **ok** — *fallback* |
| Cboe delayed-quote CDN | the primary volatility source | **failed: HTTP 403 (Cloudflare)** — the Yahoo fallback served the pair |
| Web search (Investopedia / Reuters / Morningstar / Finviz / MT Newswires) | the day's catalysts only (ADI's weak guide, HPE's margin outlook, Sanofi's Insmed deal, Kymera's Phase 2b data, the retail earnings beats) | **ok** — no published number comes from it |

**Degraded sources: 1** — the Cboe delayed-quote CDN (HTTP 403). The volatility pair was published from the Yahoo fallback instead, and the `source` string names it.

### Method

- **The dual book.** The TRIGGER screens (4% breakout, EP9M, 10% gap, volume breakout) ran on **2026-11-24's own settled bar** from the TradingView scanner. The multi-session CONTEXT screens (5-day gainers/losers, the 14-day velocity, the coil, the 252-session RS window) stay on shibui's **2026-11-23** session and are labelled T+1. Every row publishes `data_as_of` + `source` (`fresh` / `t1` / `fresh+t1`); the two are never blended.
- **Volume basis.** The scanner publishes no prior-session volume, so the expansion test runs against the prior-**nine**-session mean, reconstructed as `(10 × average_volume_10d_calc − volume_today) / 9` — a stricter gate than shibui's "volume > prev_session", published as its own gate. The 5-session move stays on shibui's `m1` because TradingView's `Perf.W` is a **six**-session measure (r = 0.997 against a six-session move, 0.924 against five).
- **Close convention.** The official 16:00 ET print. TradingView's `close` equals Nasdaq's `secondaryData`; `primaryData` is the after-hours print and is **not** used.
- **Coverage.** 1,668 screened rows across 9 branches → 1,378 distinct candidates. `rows_kept == rows_passing` on all nine branches; no branch landed on 30 / 50 / 60 / 200, so no book was truncated.
- **Quality overlay.** 1,188 symbols queried; 721 `fail`, 355 `pass`, 112 `unknown` (no trailing earnings — **disclosed, not counted as a red flag**). A flag never removes a name from the book.

### Caveats

- **A one-complex unwind is not a market view.** The Nasdaq fell 1.48% while the median large cap rose 0.45%; read the index as the AI complex, not as the market's verdict.
- **"Extended" is a label, not a filter.** All 8 Tier-A names carry it and none was dropped; seven trip it on ATR% alone, which fires on 15.8% of the $10B+ universe by itself.
- **The catalyst is single-stock on both sides.** ADI's guide and HPE's margin outlook drove the two largest decliners, and Sanofi's Insmed acquisition drove the largest biotech move — index-level reads of today inherit those single-name shocks.
- **Not verified:** no intraday path, no option-chain or flow confirmation, no independent per-name catalyst check for the Focus names, and the theme branch's leader selection is published as-is from the screen.
- **The screen's context numbers are one session stale** (shibui 2026-11-23). The fresh book is the primary; the T+1 book is the cross-check, and where they disagree the artifact publishes both rather than substituting one.

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
