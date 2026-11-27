---
artifact: daily-sweep
contract: SWEEP_PIPELINE_V1
cron: "#09 stock-screener-daily-sweep-18:30"
fire_time_et: "2026-11-27 18:30:03 ET"
cron_date: "2026-11-27"
screen_data_date: "2026-11-25 (shibui is T+1 — the multi-session CONTEXT screens describe the previous session)"
fresh_data_date: "2026-11-27 (the cron-day settled bar — the TRIGGER screens: 4% breakout, EP9M, 10% gap, volume breakout)"
print_data_date: "2026-11-27 (official 16:00 ET close, bridge market-recap)"
regime: {size_cut_pct: 0, uncertainty: false, late_cycle: false, index_below_20sma: true, breadth_pct_spx: 50.64}
coverage: "9/9 branches complete (rows_kept == rows_passing on every branch)"
---

# Daily Screener Sweep — Friday 27 November 2026 (end-of-day, cron #09)

This run uses the **dual book**: the TRIGGER screens (4% breakout, EP9M, 10% gap, volume breakout) run on **2026-11-27's own settled bar**, while the multi-session CONTEXT screens (5-day gainers/losers, 14-day velocity, the coil, the 252-session RS window) stay on shibui's newest ingested session, **2026-11-25**. Every row publishes which session it describes (`data_as_of` + `source`), and the two are never blended.

## TL;DR

- **A broad risk-on close, with the index as the weak leg.** In the $10B+ universe 831 names advanced against 247 declining (net **+584**, ratio 3.36, median name +0.78%) and **50.64%** of names sit above their 20-DMA — yet only **1 of 5** index ETFs is above its own 20-DMA. That is a **+30.64 pp BROAD divergence**: the average large cap is healthier than the index, so this is a participation-led tape, not a megacap-led one.
- **The book is thin, and every Tier-A name is already extended.** Tier-A is **4 names** (CAR, CHTR, INIO, SHLS) and **all four are EXTENDED — 0 fresh**. CHTR and INIO carry a `debt_to_equity` flag, SHLS adds negative FCF yield plus an earnings-quality flag, and CAR has no trailing earnings at all (valuation gate `unknown` — disclosed, not cleared).
- **Read the dates before the numbers.** The TRIGGER screens (4% breakout, EP9M, 10% gap, volume breakout) run on the cron day's own settled bar (144 names, 21 of them fresh-only); the multi-session CONTEXT screens (5-day gainers/losers, 14-day velocity, the coil, the 252-session RS window) stay on shibui's newest ingested session, **2026-11-25**. Every row publishes which session it describes.

## Regime at the close

| Flag | Value |
|---|---|
| `size_cut_pct` | **0** (size cut is off - breadth 50.64% is not under the 40% trigger) |
| `uncertainty` | **false** (VIX 23.81 / VIX3M 23.82 = 0.9996) |
| `late_cycle` | **false** (no index ETF > 6% above its 50-DMA; extreme is RSP at +1.61%) |
| `index_below_20sma` | **true** (1 of 5 index ETFs above their 20-DMA) |
| Breadth divergence | **+30.6 pp — BROAD** |

Full breadth read: `breadth.md`. Machine payload: `_regime.json` (flat schema v2, all eight keys, non-empty `atr_extensions`).

## The two books — what each one is, and what it says

| Book | Session | Branches | Names |
|---|---|---|---|
| **FRESH** (primary) | **2026-11-27** — the cron day's settled bar | `A_tv_breakout_4pct` 39 · `B_tv_ep9m` 103 · `D_tv_gap_10pct` 5 · `TV_volume_breakout` 23 | 144 |
| **T+1** (cross-check) | **2026-11-25** — shibui's newest ingested session | 9 branches | 1244 |

| `source` | Meaning | Count |
|---|---|---|
| `fresh+t1` | in both books | 123 |
| `t1` | context screens only | 1121 |
| `fresh` | trigger screens only | 21 |

## Screen coverage — the assertion that makes the book publishable

Every branch was fetched as its own query, uncapped, and paged until the rows collected equalled `rows_passing`. **rows_kept == rows_passing on every branch**, and no branch carries a per-branch LIMIT — so no book is capped. No branch count lands on a cap value (30 / 50 / 60 / 200).

| Branch | Screen | rows_passing | rows_kept | Status |
|---|---|---|---|---|
| `A_stockbee_4pct` | Stockbee — Bonde 4% breakout (T+1) | 150 | 150 | complete |
| `B_stockbee_ep9m` | Stockbee — EP9M (T+1) | 213 | 213 | complete |
| `K_stockbee_anticipation` | Stockbee — anticipation / coil (T+1) | 493 | 493 | complete |
| `C_qullamaggie_rs` | Qullamägi — RS leaders, 252-session window (T+1) | 51 | 51 | complete |
| `D_qullamaggie_ep` | Qullamägi — EP 10% gap (T+1) | 0 | 0 | complete |
| `E_qullamaggie_5d_gainers` | Qullamägi — 5-day gainers, parabolic short (T+1) | 5 | 5 | complete |
| `F_qullamaggie_5d_losers` | Qullamägi — 5-day losers, parabolic long (T+1) | 3 | 3 | complete |
| `G_peoplewish` | peoplewish — ADR% + $vol + 14-day velocity (T+1) | 437 | 437 | complete |
| `H_hernandez_theme` | Hernandez — theme → group → leaders (T+1) | 67 | 67 | complete |

Total screened rows **1419** across the 9 branches → **1265 distinct candidates** after dedup and merge with the fresh book.

## Tier-A — ≥ 3 distinct stylists (4 names)

| Symbol | Stylists | Origins | Source | Close | **Chg** | ADR% | Velocity 14d | m1 (5d) | Ext |
|---|---|---|---|---|---|---|---|---|---|
| **CAR** | 3 | A_stockbee_4pct, C_qullamaggie_rs, G_peoplewish | `t1` | 144.54 | **+1.92%** | 6.05 | 17.75 | — | EXTENDED |
| **CHTR** | 3 | A_stockbee_4pct, C_qullamaggie_rs, G_peoplewish | `t1` | 153.87 | **+4.48%** | 5.57 | 17.01 | — | EXTENDED |
| **INIO** | 3 | A_stockbee_4pct, G_peoplewish, jeff_sun_canslim | `t1` | 13.02 | **+0.27%** | 9.10 | -2.59 | — | EXTENDED |
| **SHLS** | 3 | A_stockbee_4pct, G_peoplewish, jeff_sun_canslim | `t1` | 7.48 | **+5.35%** | 10.05 | -21.07 | — | EXTENDED |

### What Tier-A is saying

Not one of the four is a fresh setup — that is the finding, not a caveat.

- **CAR** (Avis Budget) — 3 stylists (4% breakout + RS leader + peoplewish), but +16.7% above its 20-DMA with RSI 76.2 and ATR 5.11% (84th pctile of the $10B+ universe): the extension label IS the signal here. Valuation gate `unknown` — no trailing P/E in the data, so it is disclosed, not cleared.
- **CHTR** (Charter) — 3 stylists, +17.9% above its 20-DMA, RSI 70.9, ADR 5.57%, +4.48% on the day with 2.69M shares. `debt_to_equity` flag: the growth screen says nothing about what the balance sheet already assumes.
- **INIO** — 3 stylists, ATR **11.16%** (98.7th pctile of the $10B+ universe) yet still **8.1% BELOW** its 20-DMA and 14-day velocity −2.59: extended by volatility, not by a run. `debt_to_equity` flag.
- **SHLS** — 3 stylists, +5.35% today on 2.54M shares, ATR 9.48% (96.8th pctile), RSI 48.6, but 14-day velocity **−21.07**: the velocity is negative while the price is up. `free_cash_flow_yield` + `earnings_quality_flags`.

The honest read: this is a book of names that have already run, not a book of setups. Nothing is dropped for tripping the rule — the split is published in `tier-a-fresh.md` (empty) and `tier-a-extended.md` (all four).

### The extension label — the honest answer to "have these already run?"

**Tier-A is 0 fresh / 4 extended.** Every row carries the label with its reasons; nothing is dropped for tripping it.

| Symbol | ATR% | ATR% pctile ($10B+) | % above 20-DMA | >15% rule |
|---|---|---|---|---|
| CAR | 5.11 | 84.0 | 16.74 | yes |
| CHTR | 4.81 | 81.9 | 17.86 | yes |
| INIO | 11.16 | 98.7 | -8.12 | no |
| SHLS | 9.48 | 96.8 | -4.73 | no |

## Focus — ≥ 2 stylists OR top-5 velocity (12 names)

| Symbol | Stylists | Origins | Source | Close | **Chg** | RVOL 10d | ATR% | RSI | ADR% |
|---|---|---|---|---|---|---|---|---|---|
| **AADX** | 2 | A_stockbee_4pct, jeff_sun_canslim | `t1` | 7.48 | **+5.95%** | 0.72 | 10.52 | 40.4 | 9.90 |
| **ARRY** | 2 | A_stockbee_4pct, B_stockbee_ep9m, G_peoplewish | `t1` | 4.44 | **+6.73%** | 0.57 | 9.21 | 53.2 | 10.43 |
| **ASTS** | 2 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, G_peoplewish | `fresh+t1` | 26.85 | **+3.19%** | 0.64 | 13.68 | 38.0 | 11.76 |
| **BTDR** | 2 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, G_peoplewish | `fresh+t1` | 3.10 | **+1.64%** | 0.44 | 24.26 | 30.8 | 14.37 |
| **CAR** | 3 | A_stockbee_4pct, C_qullamaggie_rs, G_peoplewish | `t1` | 144.54 | **+1.92%** | 0.72 | 5.11 | 76.2 | 6.05 |
| **CHTR** | 3 | A_stockbee_4pct, C_qullamaggie_rs, G_peoplewish | `t1` | 153.87 | **+4.48%** | 0.94 | 4.81 | 70.9 | 5.57 |
| **INIO** | 3 | A_stockbee_4pct, G_peoplewish, jeff_sun_canslim | `t1` | 13.02 | **+0.27%** | 0.70 | 11.16 | 42.1 | 9.10 |
| **JOBY** | 2 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, G_peoplewish | `fresh+t1` | 4.05 | **+3.85%** | 0.61 | 9.54 | 39.6 | 8.13 |
| **LI** | 2 | A_stockbee_4pct, A_tv_breakout_4pct, B_stockbee_ep9m, TV_volume_breakout | `fresh+t1` | 12.42 | **+4.55%** | 1.64 | 4.03 | 60.7 | 3.22 |
| **QXO** | 2 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, G_peoplewish | `fresh+t1` | 12.17 | **+1.67%** | 0.50 | 6.71 | 53.8 | 6.73 |
| **RH** | 2 | A_stockbee_4pct, G_peoplewish | `t1` | 111.10 | **-1.17%** | 0.63 | 6.96 | 39.7 | 6.06 |
| **SHLS** | 3 | A_stockbee_4pct, G_peoplewish, jeff_sun_canslim | `t1` | 7.48 | **+5.35%** | 0.41 | 9.48 | 48.6 | 10.05 |

Twelve names at ≥ 2 stylists. Five of them (`ASTS`, `BTDR`, `JOBY`, `LI`, `QXO`) are `fresh+t1` — they cleared the trigger screens on today's own bar AND the context screens on 2026-11-25 — and four of those five closed up on the day (ASTS +3.19%, JOBY +3.85%, LI +4.55%, QXO +1.67%, BTDR +1.64%).

- **The fresh-only book (21 names) is high-beta and thin**: ELPC +13.36%, SBS +11.32% (13.25M shares, RVOL 1.50), AGBK +9.09%, UGP +8.94%, TMS +8.68% — but relative volume is barely above 1 (0.88–1.20), so the volume-expansion leg of the 4% breakout gate is thin on most of them. SBS is the exception, and it is also in the large-cap movers table (+11.32%).
- **Two live tells in the fresh book**: **DV** printed **7.72× relative volume** on 21.2M shares — by far the most expanded tape in the book, and it closed +0.15%, which is what an intraday absorption looks like. **GOOG** cleared the EP9M gate on 14.0M shares but at **0.55× RVOL** — the megacap is where the *shares* were, not the volume.
- **RH** −1.17% is the only Focus name that closed down; **INIO** +0.27% and **CAR** +1.92% closed almost flat despite 3-stylist agreement — the tiering is telling you those names are extended, not that they are moving today.
- **ARRY** +6.73% on 4.59M shares is the strongest Focus name on the day, and it is `t1` only — the 2026-11-25 screen, not today's trigger set.

## The valuation / quality overlay

The CANSLIM screen asks for growth and strength and nothing else. The overlay adds what the price already assumes, per name, with the values next to the flags.

| Gate | Names | Meaning |
|---|---|---|
| `pass` | 373 | no red flag, and earnings data present |
| `fail` | 671 | at least one red flag (trailing P/E > 50, operating P/E > 40, PEG > 3, negative FCF yield, debt/equity > 1.5, shibui's own earnings-quality flags) |
| `unknown` | 101 | no red flag, **but no reported trailing earnings either** — disclosed, not cleared |

A missing value is a **disclosure, not a flag** and is never counted as a red flag.

## Today's tape — the settled close of 2026-11-27

| Metric | Value |
|---|---|
| Universe | 1090 names (NYSE/NASDAQ/AMEX, stock+dr, mcap > $10B) |
| % above 20 / 50 / 200-DMA | **50.64%** / 50.28% / 45.87% |
| Advance / decline / unchanged | **831 / 247 / 12** (ratio 3.36) |
| Median name | +0.78% |
| VIX / VIX3M | **23.81 / 23.82** (VIX -11.16% from 26.8) |
| SPY / QQQ / RSP / IWM / QQQE | 728.32 (+1.62%) / 650.99 (+2.69%) / 218.38 (+1.22%) / 273.79 (+1.83%) / 112.50 (+2.42%) |

**Biggest movers in the large-cap universe (today's close):**

| Ticker | Name | Close | Chg |
|---|---|---|---|
| XP | XP Inc. | 16.99 | **+18.07%** |
| BBDO | Banco Bradesco Sa | 2.60 | **+17.65%** |
| SNDK | Sandisk Corporation | 85.36 | **+15.96%** |
| BBD | Banco Bradesco Sa | 2.80 | **+15.23%** |
| COHR | Coherent Corp. | 223.79 | **+14.07%** |
| ITUB | Itau Unibanco Banco Holding SA | 7.66 | **+11.34%** |
| SBS | Companhia de saneamento Basico Do Estado De  | 5.41 | **+11.32%** |
| ANT | Anthropic, PBC Class A | 91.88 | **+10.98%** |

**Largest decliners:**

| Ticker | Name | Close | Chg |
|---|---|---|---|
| WSO.B | Watsco, Inc. | 296.40 | -5.38% |
| VRTX | Vertex Pharmaceuticals Incorporated | 534.57 | -5.24% |
| FRHC | Freedom Holding Corp. | 169.01 | -3.74% |
| BSP | Bending Spoons S.p.A. | 45.03 | -2.72% |
| SJM | The J.M. Smucker Company | 126.86 | -2.46% |
| DLTR | Dollar Tree, Inc. | 148.53 | -2.42% |
| GME | GameStop Corporation | 26.34 | -2.34% |
| CHTRP | Charter Communications, Inc. - Series A Cumu | 20.55 | -2.24% |

## Parabolic books — the 5-session move (T+1 context)

**Short candidates (5):** the names up 25%+ over five sessions.

| Symbol | m1 (5d) | ADR% | Close | Chg |
|---|---|---|---|---|
| CELC | 29.03 | 7.12 | 70.93 | -1.13% |
| COGT | 29.74 | 6.55 | 35.64 | -1.22% |
| INSM | 42.16 | 5.09 | 170.44 | +0.08% |
| KYMR | 43.46 | 6.69 | 175.53 | +1.01% |
| VRDN | 25.86 | 5.87 | 38.82 | +2.40% |

**Long / mean-reversion candidates (3):** the names down 25%+ over five sessions.

| Symbol | m1 (5d) | ADR% | Close | Chg |
|---|---|---|---|---|
| AMBA | -34.70 | 7.52 | 35.24 | -1.23% |
| SLS | -28.86 | 13.30 | 13.66 | +6.97% |
| SNEX | -32.70 | 5.37 | 38.05 | +5.02% |

## Per-stylist books

| Stylist | File |
|---|---|
| Stockbee — Pradeep Bonde | `stockbee.md` |
| Qullamägi — Kristjan Kullamägi | `qullamaggie.md` |
| Jeff Sun, CFTe | `jeff-sun.md` |
| Ariel Hernandez | `ariel-hernandez.md` |
| peoplewish — Alec Riffle | `peoplewish.md` |

The theme→group→leader funnel picked **IBB, XLV and XLP** (Health Care + Consumer Staples) from a 224-name pool, and the 67 published names are *leaders inside* sectors that already cleared another stylist screen — not every name in a top sector.

- **Defensive leadership on a strong up day is the notable thing.** The money bought Health Care and Staples while the tape's hottest groups were Semiconductors (+5.17% average) and Computer Peripherals (+7.38%) — but only **12.1%** of Semiconductors are above their own 20-DMA and **14.3%** of Computer Peripherals are, so those two are a bounce off a broken trend, not a trend. A Health Care/Staples leadership read is a rotation into defensives on strength, not a defensively-led market.
- Highest cross-stylist convergence inside the theme branch: **AXGN** (4 stylists, 21.7 14-day velocity), **INSM** (4 stylists, 56.6 velocity — and +42.2% over 5 sessions, so it is in the parabolic short book too), then **ADMA**, **CGON** and **GKOS** at 3.
- The theme branch runs on shibui's 2026-11-25 session, so it describes last week's relative strength, not today's.

## Method, source health & caveats

| Source | Query / endpoint | Status | Result |
|---|---|---|---|
| TradingView scanner (`POST scanner.tradingview.com/america/scan`) | fresh book, breadth universe, mover ranking | HTTP 200 | ok — 3743 names (totalCount 3743 = rows fetched, no truncation); breadth universe 1090 names; the movers tables are built from the same settled scan |
| shibui-finance via the MCP bridge (`stock_data_query`) | 9 sweep branches + enrichment + CANSLIM growth + valuation overlay | HTTP 200 | ok — 1419 rows across 9 branches; `rows_kept == rows_passing` on every branch |
| bridge `market-recap` `get_quotes` | today's official close for the book names | HTTP 200 | ok — `market_state: post`, official 16:00 ET prints |
| Nasdaq public quote API (`/quote/<SYM>/info`) | same-day print column | not called | not used this run — the print column came from the bridge batch below |
| **Cboe delayed-quote CDN** (`_VIX.json` / `_VIX3M.json`) | primary volatility pair | **HTTP 403 (Cloudflare)** | **failed** — blocked from this egress (first observed 2026-11-19, reproduced 2026-11-25 and 2026-11-27); fell back to the Yahoo chart API |
| Yahoo chart API (`^VIX`, `^VIX3M`) | volatility pair fallback | HTTP 200 | ok (fallback) — VIX 23.81 / VIX3M 23.82, quote time 2026-11-27 13:15:00 ET, both symbols from the same session bar, pulled once |

**degraded_sources: 1** — the Cboe delayed-quote CDN (HTTP 403). Every other source served its data, and the one failure was covered by the documented fallback.

The `D_qullamaggie_ep` branch (10% gap) returned **0 rows** on the 2026-11-25 session. That is a genuine zero, not a truncation: the branch carries no inner LIMIT and `rows_passing == rows_kept == 0`.

**The dual book and what each date means.** The TRIGGER screens (4% breakout, EP9M, 10% gap, volume breakout) are computed on **2026-11-27's own settled bar** from the TradingView scanner, whose `close` is the official 16:00 ET print — 144 names, of which 21 are fresh-only. The multi-session CONTEXT screens (5-day gainers/losers, the 14-day velocity, the anticipation/coil, the 252-session RS window) stay on shibui's newest ingested session, **2026-11-25** (T+1). Every row in `_results.json` carries `data_as_of` and `source` (`fresh` / `t1` / `fresh+t1`); the two books are published side by side and never blended, and they are never substituted for one another.

**Coverage assertion.** Every branch was fetched as its own uncapped query with `COUNT(*) OVER () AS rows_passing` computed inside the branch, then paged until the rows collected equalled `rows_passing`. **9/9 branches complete**, no branch carries an inner `LIMIT`, and no branch count lands on a cap value (30 / 50 / 60 / 200) — so a count of 150 or 213 here is a screen outcome, not a truncation. The coverage table is published in the method section above and in `_results.json` under `screen_coverage`.

**Universes are not interchangeable.** The screen pre-filter is close > $3, market cap > $300M, 30-day average volume > 100k, NYSE/NASDAQ/AMEX. The breadth universe is a different population — `market_cap_basic > $10B`, `type in {stock, dr}` — and the two are never mixed in one denominator. `Perf.W` is deliberately NOT used as the 5-session move: TradingView's weekly performance correlates r=0.997 with a SIX-session move against only r=0.924 with a five-session move, so the parabolic gates (+25% / −25% / −50%) stay on shibui and stay labelled T+1 rather than being silently shifted by a session.

**The overlay is a label, never a filter.** 671 of 1145 screened names carry at least one red flag (trailing P/E > 50, operating P/E > 40, PEG > 3, negative FCF yield, debt/equity > 1.5, shibui's own earnings-quality flags); 101 are `unknown` — no red flag but no reported trailing earnings either, which is a **disclosure, not a flag** and is never counted as one. Nothing is dropped from the book for tripping a rule; the extension label is published on every row for the same reason, and Tier-A is published twice (`tier-a-fresh.md`, `tier-a-extended.md`).

**Known feed caveat.** The scanner's `change` column can lag the `close` it is paired with on this feed, so where a move and a close are both published the close from the same pull is the anchor and the change field is labelled as the vendor's own.

**Volatility.** The Cboe delayed-quote CDN answered HTTP 403 from this egress, so the pair was served by the Yahoo chart-API fallback, read from a single session bar and published with its quote time. The pair was pulled **once**, so `vix_stable: true` reflects an absence of disagreement opportunity, not a demonstrated stability.

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
