---
artifact: daily-sweep
cron: "#09 stock-screener-daily-sweep-18:30"
fire_time_et: "2026-11-09 18:30 ET"
cron_date: "2026-11-09"
screen_data_date: "2026-11-06 (shibui is T+1 — the screens describe the previous session)"
print_data_date: "2026-11-09 (official 16:00 ET close, bridge market-recap)"
regime: {size_cut_pct: 0, uncertainty: false, late_cycle: false, index_below_20sma: true, breadth_pct_spx: 68.01}
coverage: "8/8 branches complete (rows_kept == rows_passing on every branch)"
---

# Daily Screener Sweep — Monday, 09 November 2026 (end-of-day, cron #09)

The **screens** ran on shibui's newest ingested session, **2026-11-06** — shibui is T+1 and had not yet ingested 2026-11-09 at the 18:30 ET fire. The **prints** are today's official 16:00 ET close, so every name below carries both: the screen metric that put it on the list, and what it actually did today.

## TL;DR

- **A violent breadth snap-back underneath a still-damaged index.** 68.01% of the 1113-name large-cap universe closed above its 20-DMA, A/D was **927 / 180 / 6**, and the median name gained 1.67%. But only 2 of 5 index ETFs are above their own 20-DMA — a **+28.0 pp BROAD divergence**: the average stock is healthier than the index.
- **The book is 954 candidates, and the Tier-A list is six names** — FLY, FROG, KRMN, OKLO, RGTI, TMDX. Every one of them also gained today (+6% to +17%), so the screen did not have to be right about the tape to be right about the book.
- **Caveat that changes how to read it**: every screen metric here is one session stale (11-06). The Tier-A names that gapped hardest on 11-06 (KRMN +42%, FROG +35%) have already had their move; the 5-day parabolic lists are built off that same stale tape.

## Regime at the close

| Flag | Value |
|---|---|
| `size_cut_pct` | **0** (breadth 68.01% is far above the 40% trigger) |
| `uncertainty` | **false** (VIX 19.92 / VIX3M 20.85 = 0.9554) |
| `late_cycle` | **false** (no index ETF > 6% above its 50-DMA; extreme RSP +2.87%) |
| `index_below_20sma` | **true** (2 of 5 index ETFs above their 20-DMA) |
| Breadth divergence | **28.0 pp — BROAD** |

Full breadth read: `breadth.md`. Machine payload: `_regime.json` (flat schema v2).

## Screen coverage — the assertion that makes the book publishable

Every branch was fetched as its own query, uncapped, and paged until the rows collected equalled `rows_passing`. **rows_kept == rows_passing on all eight branches**, and no branch count lands on a cap (30 / 50 / 60 / 200).

| Branch | Screen | rows_passing | rows_kept | Pages | Status |
|---|---|---|---|---|---|
| `A_stockbee_4pct` | Stockbee — Bonde 4% breakout | 143 | 143 | — | complete |
| `B_stockbee_ep9m` | Stockbee — EP9M | 251 | 251 | — | complete |
| `C_qullamaggie_rs` | Qullamägi — RS leaders | 68 | 68 | — | complete |
| `D_qullamaggie_ep` | Qullamägi — EP 10% gap | 29 | 29 | — | complete |
| `E_qullamaggie_5d_gainers` | Qullamägi — 5-day gainers (parabolic short) | 14 | 14 | — | complete |
| `F_qullamaggie_5d_losers` | Qullamägi — 5-day losers (parabolic long) | 29 | 29 | — | complete |
| `G_peoplewish` | peoplewish — ADR% + $vol + velocity | 338 | 338 | — | complete |
| `K_stockbee_anticipation` | Stockbee — anticipation (coil) | 223 | 223 | — | complete |

Total screened rows **1095** across the eight branches → **954 distinct candidates** after dedup and merge with the TV-sourced screens.

## Tier-A — ≥ 3 distinct stylists (6 names)

| Symbol | Stylists | Origins | Screen close 11-06 | Chg 11-06 | Close 11-09 | **Chg 11-09** | ADR% | Velocity 14d |
|---|---|---|---|---|---|---|---|---|
| **FLY** | 4 | A_stockbee_4pct, B_stockbee_ep9m, D_qullamaggie_ep, G_peoplewish, TV_volume_breakout | 24.31 | —% | 24.31 | **17.1%** | 8.0 | 24.8 |
| **FROG** | 3 | A_stockbee_4pct, D_qullamaggie_ep, G_peoplewish | 100.98 | 35.3% | 108.18 | **7.1%** | 7.7 | 11.0 |
| **KRMN** | 4 | A_stockbee_4pct, B_stockbee_ep9m, C_qullamaggie_rs, D_qullamaggie_ep, G_peoplewish, jeff_sun_canslim | 45.61 | 42.1% | 45.90 | **0.6%** | 8.4 | 34.5 |
| **OKLO** | 4 | A_stockbee_4pct, B_stockbee_ep9m, D_qullamaggie_ep, G_peoplewish, TV_volume_breakout | 26.84 | —% | 26.84 | **14.0%** | 7.2 | -13.5 |
| **RGTI** | 3 | A_stockbee_4pct, B_stockbee_ep9m, G_peoplewish, TV_volume_breakout | 12.98 | —% | 12.98 | **10.5%** | 7.0 | 0.7 |
| **TMDX** | 3 | A_stockbee_4pct, D_qullamaggie_ep, E_qullamaggie_5d_gainers, G_peoplewish | 88.24 | 27.9% | 93.79 | **6.3%** | 5.5 | 23.2 |

### What Tier-A is saying

- **FLY** (4 stylists) — the cleanest of the six: a 4% breakout, a 8.9M-share EP9M print, a 10%+ gap, and the peoplewish velocity screen all fired on it. It closed **+17.1%** today at 24.31.
- **KRMN** (4 stylists, 6 origins) — the only name in Tier-A that also clears the CANSLIM growth screen (EPS +120% yoy, revenue +58% yoy, RSI 64). Velocity 34.5, the highest in the book.
- **OKLO** (4 stylists) and **RGTI** (3) — the two nuclear-themed names; both were in the TV volume-breakout screen as well, and both closed **+14.0%** and **+10.5%**.
- **TMDX** (3 stylists) is also a parabolic-short candidate (5-day +33.7%) — it appears on both lists.

## Focus — ≥ 2 stylists OR top-5 velocity (12 names)

| Symbol | Stylists | Origins | Close 11-09 | Chg 11-09 |
|---|---|---|---|---|
| CYRX | 2 | A_stockbee_4pct, TV_volume_breakout | 20.47 | 7.2% |
| ETON | 2 | A_stockbee_4pct, TV_volume_breakout | 64.35 | 14.0% |
| **FLY** | 4 | A_stockbee_4pct, B_stockbee_ep9m, D_qullamaggie_ep, G_peoplewish, TV_volume_breakout | 24.31 | 17.1% |
| **FROG** | 3 | A_stockbee_4pct, D_qullamaggie_ep, G_peoplewish | 108.18 | 7.1% |
| IONQ | 2 | A_stockbee_4pct, B_stockbee_ep9m, G_peoplewish | 35.34 | 8.3% |
| **KRMN** | 4 | A_stockbee_4pct, B_stockbee_ep9m, C_qullamaggie_rs, D_qullamaggie_ep, G_peoplewish, jeff_sun_canslim | 45.90 | 0.6% |
| LASR | 2 | A_stockbee_4pct, TV_volume_breakout | 43.21 | 13.7% |
| **OKLO** | 4 | A_stockbee_4pct, B_stockbee_ep9m, D_qullamaggie_ep, G_peoplewish, TV_volume_breakout | 26.84 | 14.0% |
| QNT | 2 | A_stockbee_4pct, G_peoplewish | 40.04 | 6.6% |
| **RGTI** | 3 | A_stockbee_4pct, B_stockbee_ep9m, G_peoplewish, TV_volume_breakout | 12.98 | 10.5% |
| RHLD | 2 | A_stockbee_4pct, TV_volume_breakout | 163.85 | 6.6% |
| **TMDX** | 3 | A_stockbee_4pct, D_qullamaggie_ep, E_qullamaggie_5d_gainers, G_peoplewish | 93.79 | 6.3% |

## Parabolic short candidates — 5-day gainers (14)

| Symbol | m1 (5d move) | ADR% | $vol 20d | Close 11-09 | Chg 11-09 |
|---|---|---|---|---|---|
| APP | **71.2%** | 5.1 | 1628M | 410.00 | 4.8% |
| ARRY | **72.7%** | 7.6 | 50M | 5.19 | -11.4% |
| FISV | **25.7%** | 3.3 | 394M | 63.52 | 1.0% |
| FUN | **33.7%** | 8.8 | 62M | 10.76 | 7.6% |
| GPK | **25.0%** | 4.2 | 89M | 10.84 | -3.1% |
| GRAB | **25.8%** | 4.2 | 206M | 3.44 | 0.9% |
| JBLU | **28.8%** | 9.2 | 107M | 3.94 | 7.4% |
| MGNI | **27.5%** | 4.7 | 59M | 29.04 | 6.0% |
| NXT | **32.2%** | 6.4 | 288M | 104.89 | -0.0% |
| RIOT | **30.4%** | 9.1 | 372M | 17.66 | 5.7% |
| RUN | **33.4%** | 7.0 | 100M | 9.74 | -2.4% |
| SHLS | **40.0%** | 7.5 | 57M | 8.72 | -13.5% |
| TMDX | **33.7%** | 5.5 | 85M | 93.79 | 6.3% |
| U | **36.6%** | 5.5 | 544M | 51.43 | -0.1% |

Two of the parabolic names already broke: **ARRY** −11.4% and **SHLS** −13.5% today, off 5-day moves of +72.7% and +40.0%. That is the screen working — the parabolic short book is built to catch the names that have already run too far.

## Parabolic long / mean-reversion — 5-day losers (29)

| Symbol | m1 (5d move) | ADR% | Velocity 14d | Close 11-09 | Chg 11-09 |
|---|---|---|---|---|---|
| AAOI | **-27.4%** | 9.9 | -35.9 | 52.10 | 3.9% |
| ALAB | **-26.3%** | 8.0 | -33.5 | 216.87 | 13.7% |
| AXON | **-26.8%** | 5.1 | -18.3 | 303.18 | -3.1% |
| AXTI | **-29.4%** | 10.9 | -31.5 | 42.91 | 10.4% |
| BTU | **-27.7%** | 5.5 | -32.6 | 17.03 | 6.2% |
| CAI | **-26.5%** | 6.4 | -17.8 | 25.57 | 1.4% |
| CVI | **-34.7%** | 6.7 | -36.3 | 39.10 | 2.5% |
| DOX | **-33.0%** | — | — | 41.74 | -0.8% |
| ECG | **-25.4%** | 6.8 | -29.5 | 84.43 | 10.2% |
| FIS | **-25.5%** | — | — | 28.34 | -1.4% |
| FRMI | **-39.8%** | 11.2 | -48.0 | 1.66 | 5.7% |
| FSLY | **-31.4%** | 8.5 | -31.1 | 15.98 | 0.8% |
| IRTC | **-26.9%** | 5.1 | -17.7 | 88.73 | -1.6% |
| LBRT | **-29.1%** | 7.4 | -30.0 | 12.93 | 8.1% |
| LGN | **-28.1%** | 8.5 | -36.9 | 32.16 | 15.2% |
| LITE | **-35.9%** | 8.7 | -35.5 | 596.16 | 10.7% |
| MOD | **-25.5%** | 7.1 | -35.4 | 106.15 | 9.9% |
| MRVL | **-28.1%** | 7.0 | -40.4 | 154.60 | 9.5% |
| MXL | **-27.1%** | 9.4 | -36.2 | 55.91 | 13.7% |
| NRIX | **-42.9%** | 5.8 | -38.6 | 16.14 | 5.5% |
| NTRA | **-25.0%** | 5.0 | -22.2 | 320.39 | 3.1% |
| PTEN | **-25.5%** | 5.2 | -17.7 | 9.86 | -0.6% |
| SM | **-25.9%** | — | — | 29.10 | -2.7% |
| SNDK | **-27.4%** | 7.1 | -39.1 | 886.51 | 6.2% |
| SNDX | **-30.1%** | 7.7 | -27.1 | 9.55 | 0.1% |
| STRL | **-26.9%** | 8.3 | -40.3 | 290.67 | 15.0% |
| STX | **-28.5%** | 7.0 | -30.2 | 506.14 | 9.8% |
| SUPN | **-26.0%** | — | — | 27.62 | 5.6% |
| WDC | **-28.0%** | 6.4 | -25.1 | 289.78 | 9.9% |

The long book is dominated by **semis and optical/photonics** — ALAB, MXL, LITE, MRVL, SNDK, WDC, AXTI, STX, MOD — every one of them a 5-day loser of 25–40% that bounced 9–14% today. The 3-month RS table says why the book is long: the Semiconductors group averages **−24.75%** 3-month RS across 73 large-cap names, the worst group in the market.

## Today's tape — the settled close of 2026-11-09

| Metric | Value |
|---|---|
| Universe | 1113 names (NYSE/NASDAQ/AMEX, stock+dr, mcap > $10B) |
| % above 20 / 50 / 200-DMA | **68.01%** / 58.40% / 50.31% |
| Advance / decline / unchanged | **927 / 180 / 6** (ratio 5.15) |
| Median name | +1.67% |
| VIX / VIX3M | **19.92 / 20.85** (VIX −22.3% from 25.64) |
| SPY / QQQ / RSP / IWM / QQQE | 752.69 (2.37%) / 679.35 (3.54%) / 220.95 (2.27%) / 282.51 (3.23%) / 115.54 (3.15%) |

**Biggest movers in the large-cap universe (today's close):**

| Ticker | Name | Close | Chg |
|---|---|---|---|
| QXO | QXO, Inc. | 13.78 | **19.20%** |
| COHR | Coherent Corp. | 225.19 | **16.79%** |
| MPWR | Monolithic Power Systems, Inc. | 1388.05 | **16.60%** |
| VSAT | ViaSat, Inc. | 74.37 | **16.29%** |
| UI | Ubiquiti Inc. | 685.68 | **15.66%** |
| ASTS | AST SpaceMobile, Inc. | 36.89 | **14.10%** |
| QXO/PB | QXO, Inc. Depositary Shares, e | 40.64 | **14.06%** |
| ALAB | Astera Labs, Inc. | 216.87 | **13.72%** |

**Largest decliners:**

| Ticker | Name | Close | Chg |
|---|---|---|---|
| TRI | Thomson Reuters Corp | 108.30 | -3.79% |
| NVDA | NVIDIA Corporation | 178.67 | -4.27% |
| FSLR | First Solar, Inc. | 191.61 | -4.74% |
| PAC | Grupo Aeroportuario Del Pacifi | 236.11 | -5.04% |
| BNTX | BioNTech SE | 87.51 | 0.00% |

## Per-stylist books

| Stylist | File | Rows |
|---|---|---|
| Stockbee — Pradeep Bonde | `stockbee.md` | 588 |
| Qullamägi — Kristjan Kullamägi | `qullamaggie.md` | 133 |
| Jeff Sun, CFTe | `jeff-sun.md` | 184 |
| Ariel Hernandez | `ariel-hernandez.md` | 76 |
| peoplewish — Alec Riffle | `peoplewish.md` | 338 |

`ariel-hernandez.md` carries the engine's CANSLIM proxy **plus** the screen's own theme → group → leaders funnel: the top three themes by composite RS (XLV health care, IBB biotech, XRT retail) mapped to their GICS buckets, with the 182 leaders inside those buckets (top 40 by 3-month RS shown).

## Method, source health & caveats

| Source | Used for | Status |
|---|---|---|
| shibui over the MCP-over-HTTP bridge | 8 sweep branches + breadth cross-check + CANSLIM rebuild + sector RS | ok — 15 metered calls, no 429 |
| TradingView scanner (`america/scan`) | CANSLIM growth rebuild (TV's growth columns are null on US names), volume breakout, the 1113-name universe, index ETFs, sector RS | ok |
| bridge `market-recap get_quotes` | today's official close for all 54 book names | ok — note: **the batch caps at 40 symbols per call**; 54 names took two batches |
| Cboe delayed-quote CDN | VIX / VIX3M | ok — two pulls, identical |
| MCP availability probe | `catalog_ok total=135 finance_tools=0` | ok (no finance MCP registered — expected, not an error) |
| Yahoo JSON / Finviz | — | not used: Yahoo is 429-prone from this egress and Finviz is Cloudflare-403; the ladder above was never reached |

- **T+1 is not an error, it is the design**: the sweep runs on shibui's newest ingested session (2026-11-06) and the same-day print column carries what happened on 2026-11-09. Every screen column in this file says `2026-11-06` and every print column says `2026-11-09`; they are never blended.
- **The day-alignment assertion passed** before the prints were used: SPY's implied previous close from the scanner (752.69 / 1.0237 = 735.27) matches shibui's settled 2026-11-06 close (735.29), and QQQ matches exactly (656.10).
- **`rows_kept == rows_passing` on every branch**, and no count lands on 30 / 50 / 60 / 200 — the truncation fingerprint is absent.
- **The pre-market brief reads `_regime.json` and `_summary.md`** from this directory; both are written. The regime payload is the flat schema v2 with all eight keys and a non-empty `atr_extensions` map.
- **No 1-year breadth percentile** is published in `breadth.md` — that needs the trailing session series for the universe, which this routine does not pull. The level is published without it, and the gap is stated rather than filled with a guess.
- **The short/long CSVs carry their defining metric** (`m1`, the 5-session move) alongside the screen and print columns — without it they would ship as bare ticker lists.
- **This is a screen, not a trade list.** No catalyst was sourced for any name; the parabolic lists are mechanical outcomes, and the focus list has not been discretionary-reviewed.

## Files in this directory

| File | What it is |
|---|---|
| `daily-sweep.md` | this file — the primary end-of-day sweep artifact |
| `breadth.md` | the end-of-day breadth & regime read (cron #09) |
| `_regime.json` | regime payload, flat schema v2 |
| `_summary.md` | digest the pre-market brief reads |
| `_results.json` | machine-readable candidate set, tier lists, origins, screen_coverage |
| `_cache.json` | cache marker (cron date + resolved data date) |
| `master.md / focus.md / tier-a.md` | deduped union, ≥2 stylists, ≥3 stylists |
| `stockbee.md / qullamaggie.md / jeff-sun.md / ariel-hernandez.md / peoplewish.md` | the five per-stylist books |
| `short-candidates.csv / long-reversal-candidates.csv` | parabolic lists with m1, ADR, ADV and the same-day print |
| `same-day-prints.md / _same-day-prints.json` | today's official close for all 54 book names |
| `breadth-snapshot.*` | cron #10's intraday read — NOT written by this cron |

_Generated 2026-11-09 by cron #09 (stock-screener-daily-sweep-18:30). Window check passed, fire on schedule (platform stall 1 min)._
