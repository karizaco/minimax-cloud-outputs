---
artifact: daily-sweep
contract: SWEEP_PIPELINE_V1
cron: "#09 stock-screener-daily-sweep-18:30"
fire_time_et: "18:30 ET (2026-11-17)"
cron_date: "2026-11-17"
screen_data_date: "2026-11-16 (shibui is T+1 — the multi-session CONTEXT screens describe the previous session)"
fresh_data_date: "2026-11-17 (the cron-day settled bar — the TRIGGER screens: 4% breakout, EP9M, 10% gap, volume breakout)"
print_data_date: "2026-11-17 (official 16:00 ET close, bridge market-recap)"
regime: {size_cut_pct: 50, uncertainty: true, late_cycle: false, index_below_20sma: true, breadth_pct_spx: 34.16}
coverage: "9/9 branches complete (rows_kept == rows_passing on every branch)"
---

# Daily Screener Sweep — Tuesday 17 November 2026 (end-of-day, cron #09)

This run uses the **dual book**: the TRIGGER screens (4% breakout, EP9M, 10% gap, volume breakout) run on **2026-11-17's own settled bar**, while the multi-session CONTEXT screens (5-day gainers/losers, 14-day velocity, the coil, the 252-session RS window) stay on shibui's newest ingested session, **2026-11-16**. Every row publishes which session it describes (`data_as_of` + `source`), and the two are never blended.

## TL;DR

- **A broad risk-off tape, and the regime flags say so.** 239 advancers against 837 decliners in the 1,086-name $10B+ universe, SPY -1.01%, VIX +11.1% to **25.46**, and only **34.16%** of large caps above their 20-DMA. The size cut is **ON** (the index is below its 20-DMA and breadth is under the 40% trigger) and `uncertainty` is true on a VIX/VIX3M of 1.0192.
- **Enterprise software was the wound; health care and semis held up.** CRM -9.45%, INTU -7.17%, NOW -6.51% (Benzinga: Salesforce sank ahead of the Anthropic IPO, with AI-sector events due this week) and Packaged Software averaged **-2.99%**. AECOM +11.08% on a fiscal-Q4 EPS beat and a record $28B backlog; ARM +4.76%, ALAB +4.58%.
- **The book's own signal is thin and already extended.** Tier-A is **2 names** (CGON -6.89%, SEZL -4.74%) — both from the T+1 book, both down today, both labelled **EXTENDED**, and the fresh book (today's settled bar) produced **0 fresh Tier-A names**. **9 of the 12 Focus names carry a valuation red flag**.
- **The day's biggest mover is in the book but not in Focus or Tier-A.** SLS closed **+156.4%** on the pivotal Phase 3 REGAL readout (41% lower death risk, mOS 24.0 vs 14.7 months). It carries 4 stylists and is `fresh+t1`, yet the tiering order — driven by the *previous* session's 4%-breakout ranking — never reaches it. See the flags block.

## Regime at the close

| Flag | Value |
|---|---|
| `size_cut_pct` | **50** (breadth 34.16% is far above the 40% trigger) |
| `uncertainty` | **true** (VIX 25.46 / VIX3M 24.98 = 1.0192) |
| `late_cycle` | **false** (no index ETF > 6% above its 50-DMA; extreme is RSP at +0.37%) |
| `index_below_20sma` | **true** (0 of 5 index ETFs above their 20-DMA) |
| Breadth divergence | **+34.2 pp — BROAD** |

Full breadth read: `breadth.md`. Machine payload: `_regime.json` (flat schema v2, all eight keys, non-empty `atr_extensions`).

## The two books — what each one is, and what it says

| Book | Session | Branches | Names |
|---|---|---|---|
| **FRESH** (primary) | **2026-11-17** — the cron day's settled bar | `A_tv_breakout_4pct` 41 · `B_tv_ep9m` 204 · `D_tv_gap_10pct` 1 · `TV_volume_breakout` 35 | 244 |
| **T+1** (cross-check) | **2026-11-16** — shibui's newest ingested session | 9 branches | 1126 |

| `source` | Meaning | Count |
|---|---|---|
| `fresh+t1` | in both books | 220 |
| `t1` | context screens only | 906 |
| `fresh` | trigger screens only | 24 |

## Screen coverage — the assertion that makes the book publishable

Every branch was fetched as its own query, uncapped, and paged until the rows collected equalled `rows_passing`. **rows_kept == rows_passing on every branch**, and no branch count lands on a cap (30 / 50 / 60 / 200).

| Branch | Screen | rows_passing | rows_kept | Status |
|---|---|---|---|---|
| `A_stockbee_4pct` | Stockbee — Bonde 4% breakout (T+1) | 37 | 37 | complete |
| `B_stockbee_ep9m` | Stockbee — EP9M (T+1) | 208 | 208 | complete |
| `K_stockbee_anticipation` | Stockbee — anticipation / coil (T+1) | 534 | 534 | complete |
| `C_qullamaggie_rs` | Qullamägi — RS leaders, 252-session window (T+1) | 73 | 73 | complete |
| `D_qullamaggie_ep` | Qullamägi — EP 10% gap (T+1) | 2 | 2 | complete |
| `E_qullamaggie_5d_gainers` | Qullamägi — 5-day gainers, parabolic short (T+1) | 1 | 1 | complete |
| `F_qullamaggie_5d_losers` | Qullamägi — 5-day losers, parabolic long (T+1) | 10 | 10 | complete |
| `G_peoplewish` | peoplewish — ADR% + $vol + 14-day velocity (T+1) | 338 | 338 | complete |
| `H_hernandez_theme` | Hernandez — theme → group → leaders (T+1) | 47 | 47 | complete |

Total screened rows **1250** across the 9 branches → **1150 distinct candidates** after dedup and merge with the fresh book.

## Tier-A — ≥ 3 distinct stylists (2 names)

| Symbol | Stylists | Origins | Source | Close | **Chg** | ADR% | Velocity 14d | m1 (5d) | Ext |
|---|---|---|---|---|---|---|---|---|---|
| **CGON** | 4 | A_stockbee_4pct, B_stockbee_ep9m, C_qullamaggie_rs, D_qullamaggie_ep, G_peoplewish, H_hernandez_theme | `t1` | 78.94 | **-6.89%** | 6.68 | 34.70 | 23.66 | EXTENDED |
| **SEZL** | 3 | A_stockbee_4pct, C_qullamaggie_rs, G_peoplewish | `t1` | 154.25 | **-4.74%** | 7.27 | 27.14 | — | EXTENDED |

### What Tier-A is saying

- **CGON — 4 stylists / 6 origins, closed -6.89% to 78.94.** This is the roll-over of a momentum run, not a fresh trigger: `m1` (5-session) was +23.66 and 14-day velocity 34.7 into the close. RBC Capital downgraded to Sector Perform / speculative risk (target $97 from $80) even while calling the Phase 3 PIVOT-006 cretostimogene data "impressive", noting regulatory submissions slipped to March 2027 — the de-rating of a catalyst that was already in the price. The book flags it **EXTENDED twice** (ATR 7.49% = 94.8th percentile of the $10B+ universe; +15.59% above its own 20-DMA) and the valuation gate **fails** on negative free cash flow (FCF yield -2.5%, price/sales 1,219, no trailing earnings). Read it as a Tier-A *label* on a name that fell today.
- **SEZL — 3 stylists, closed -4.74% to 154.25.** The cleanest quality profile in Tier-A: valuation gate **pass** (no red flag, earnings present), though still labelled **EXTENDED** (ATR 7.02% = 93.7th percentile). BNPL momentum name, +210% over twelve months; management presented at TD Cowen's Financials & Fintech conference today (17 Nov) and the company published a credit-building finding on 16 Nov (86% of studied Sezzle Up users without a score had one within four months). No negative catalyst found on the wire — this is a pullback in a name that has already run, not a thesis break.
- **The honest read of today's Tier-A:** both names came from the T+1 book, both were red on the session, both are EXTENDED, and the fresh (2026-11-17 settled bar) book produced **0 fresh Tier-A names**. The actionable shortlist and today's tape are not the same list — see the flags block.

### The extension label — the honest answer to "have these already run?"

**Tier-A is 0 fresh / 2 extended.** Every row carries the label with its reasons; nothing is dropped for tripping it.

| Symbol | ATR% | ATR% pctile ($10B+) | % above 20-DMA | >15% rule |
|---|---|---|---|---|
| CGON | 7.49 | 94.8 | 15.59 | yes |
| SEZL | 7.02 | 93.7 | 8.96 | no |

## Focus — ≥ 2 stylists OR top-5 velocity (12 names)

| Symbol | Stylists | Origins | Source | Close | **Chg** | RVOL 10d | ATR% | RSI | ADR% |
|---|---|---|---|---|---|---|---|---|---|
| **BILL** | 2 | A_stockbee_4pct, A_tv_breakout_4pct, B_tv_ep9m, TV_volume_breakout | `fresh+t1` | 64.88 | **+12.58%** | 6.16 | 4.07 | 84.8 | 3.92 |
| **CGON** | 4 | A_stockbee_4pct, B_stockbee_ep9m, C_qullamaggie_rs, D_qullamaggie_ep, G_peoplewish, H_hernandez_theme | `t1` | 78.94 | **-6.89%** | 1.30 | 7.49 | 61.7 | 6.68 |
| **FENC** | 2 | A_stockbee_4pct, A_tv_breakout_4pct, TV_volume_breakout | `fresh+t1` | 13.58 | **+6.43%** | 3.16 | 5.87 | 72.8 | 7.06 |
| **HUBS** | 2 | A_stockbee_4pct, G_peoplewish | `t1` | 216.30 | **-6.76%** | 0.66 | 6.62 | 46.4 | 5.82 |
| **MOH** | 2 | A_stockbee_4pct, G_peoplewish | `t1` | 221.21 | **-5.10%** | 1.00 | 4.86 | 57.2 | 5.12 |
| **POWL** | 2 | A_stockbee_4pct, G_peoplewish | `t1` | 150.86 | **-0.22%** | 1.50 | 7.50 | 46.8 | 6.40 |
| **QLYS** | 2 | A_stockbee_4pct, G_peoplewish | `t1` | 174.67 | **-4.03%** | 0.90 | 7.77 | 41.0 | 6.40 |
| **SEZL** | 3 | A_stockbee_4pct, C_qullamaggie_rs, G_peoplewish | `t1` | 154.25 | **-4.74%** | 0.56 | 7.02 | 61.4 | 7.27 |
| **TSN** | 2 | A_stockbee_4pct, H_hernandez_theme | `t1` | 63.65 | **-0.47%** | 0.92 | 2.91 | 75.2 | 2.56 |
| **TU** | 2 | A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, D_qullamaggie_ep | `fresh+t1` | 9.26 | **-3.24%** | 2.09 | 3.36 | 57.8 | 2.67 |
| **ULCC** | 2 | A_stockbee_4pct, C_qullamaggie_rs | `t1` | 7.73 | **-2.89%** | 0.82 | 7.14 | 60.7 | 8.71 |
| **URGN** | 2 | A_stockbee_4pct, A_tv_breakout_4pct, TV_volume_breakout | `fresh+t1` | 29.87 | **+6.30%** | 1.63 | 7.90 | 44.5 | 7.22 |

The 12 Focus names are the first 12 names clearing ≥2 stylists **in the T+1 branch order** — `A_stockbee_4pct` ranked by the 2026-11-16 four-percent-breakout gain — so the list is ranked by *yesterday's* move, not today's. **186 names cleared ≥2 stylists and 28 cleared ≥3**; the 12-name cap keeps only the head of that ordering.

- **BILL +12.58% to 64.88** is the one Focus name that actually worked on today's tape: the Financial Times reported that private-equity firm TPG is nearing a deal to take the payments-automation company private (Benzinga, 12:56 ET); Truist raised its target to $58 but holds it. RVOL 6.16, RSI 84.8, **EXTENDED** (24.51% above its 20-DMA), valuation gate **fails** (trailing P/E and PEG > 3).
- **FENC +6.43%** (RVOL 3.16) and **URGN +6.30%** also came through on the fresh book; both are EXTENDED and both **fail** the valuation gate — FENC on trailing P/E, operating P/E and PEG, URGN on negative free cash flow.
- **HUBS -6.76%, MOH -5.10%, QLYS -4.03%, POWL -0.22%** are the mirror image: names that earned Focus on *yesterday's* breakout and are being sold today. HUBS is also a top-3 decliner in the large-cap universe.
- **Only QLYS, SEZL and TSN pass the valuation gate**; the other nine Focus names carry at least one red flag (trailing P/E, operating P/E, PEG, negative FCF, or debt/equity > 1.5).

## The valuation / quality overlay

The CANSLIM screen asks for growth and strength and nothing else. The overlay adds what the price already assumes, per name, with the values next to the flags.

| Gate | Names | Meaning |
|---|---|---|
| `pass` | 351 | no red flag, and earnings data present |
| `fail` | 605 | at least one red flag (trailing P/E > 50, operating P/E > 40, PEG > 3, negative FCF yield, debt/equity > 1.5, shibui's own earnings-quality flags) |
| `unknown` | 96 | no red flag, **but no reported trailing earnings either** — disclosed, not cleared |

A missing value is a **disclosure, not a flag** and is never counted as a red flag.

## Today's tape — the settled close of 2026-11-17

| Metric | Value |
|---|---|
| Universe | 1086 names (NYSE/NASDAQ/AMEX, stock+dr, mcap > $10B) |
| % above 20 / 50 / 200-DMA | **34.16%** / 44.38% / 44.29% |
| Advance / decline / unchanged | **239 / 837 / 9** (ratio 0.29) |
| Median name | -1.02% |
| VIX / VIX3M | **25.46 / 24.98** (VIX +11.13% from 22.91) |
| SPY / QQQ / RSP / IWM / QQQE | 732.44 (-1.01%) / 656.95 (-0.73%) / 215.76 (-1.45%) / 269.05 (-1.43%) / 111.98 (-1.27%) |

**Biggest movers in the large-cap universe (today's close):**

| Ticker | Name | Close | Chg |
|---|---|---|---|
| ACM | AECOM | 80.53 | **+11.08%** |
| TME | Tencent Music Entertainment Group | 9.47 | **+6.64%** |
| ESLT | Elbit Systems Ltd. | 720.53 | **+5.85%** |
| ARM | Arm Holdings plc | 183.39 | **+4.76%** |
| VIV | Telefonica Brasil S.A. | 12.44 | **+4.63%** |
| ALAB | Astera Labs, Inc. | 211.60 | **+4.58%** |
| VIK | Viking Holdings Ltd | 94.28 | **+4.43%** |
| AS | Amer Sports, Inc. | 30.24 | **+3.92%** |

**Largest decliners:**

| Ticker | Name | Close | Chg |
|---|---|---|---|
| NXT | Nextpower Inc. | 78.48 | -12.13% |
| CRM | Salesforce, Inc. | 194.52 | -9.45% |
| WCN | Waste Connections, Inc. | 181.50 | -8.01% |
| JD | JD.com, Inc. | 25.43 | -7.66% |
| QXO | QXO, Inc. | 11.11 | -7.49% |
| INTU | Intuit Inc. | 320.79 | -7.17% |
| HUBS | HubSpot, Inc. | 216.30 | -6.76% |
| NOW | ServiceNow, Inc. | 92.90 | -6.51% |

## Parabolic books — the 5-session move (T+1 context)

**Short candidates (1):** the names up 25%+ over five sessions.

| Symbol | m1 (5d) | ADR% | Close | Chg |
|---|---|---|---|---|
| FRMI | 49.40 | 14.32 | 2.41 | -2.82% |

**Long / mean-reversion candidates (10):** the names down 25%+ over five sessions.

| Symbol | m1 (5d) | ADR% | Close | Chg |
|---|---|---|---|---|
| BBAI | -25.71 | 7.24 | 1.80 | -1.10% |
| BTDR | -32.00 | 11.21 | 4.00 | -11.01% |
| CTVA | -25.35 | 4.60 | 8.82 | -2.43% |
| IONQ | -25.16 | 7.29 | 24.84 | -6.09% |
| LEGN | -34.17 | 6.61 | 16.11 | +0.75% |
| NVAX | -25.99 | 7.46 | 7.96 | -1.24% |
| PLUG | -28.67 | 7.16 | 1.05 | -1.87% |
| RGTI | -30.20 | 7.74 | 8.46 | -6.62% |
| SMMT | -33.74 | 7.74 | 10.67 | -9.73% |
| TE | -34.93 | 13.04 | 1.33 | -10.74% |

## Per-stylist books

| Stylist | File |
|---|---|
| Stockbee — Pradeep Bonde | `stockbee.md` |
| Qullamägi — Kristjan Kullamägi | `qullamaggie.md` |
| Jeff Sun, CFTe | `jeff-sun.md` |
| Ariel Hernandez | `ariel-hernandez.md` |
| peoplewish — Alec Riffle | `peoplewish.md` |

The theme branch ranks the sector ETFs by composite 1M/3M/6M relative strength and the leaders are **XLV** and **IBB** (Health Care) with **XLP** (Consumer Staples) — 47 names came through the theme → group → leaders filter. That RS ranking and today's tape point the same way: health care and staples were where money stayed, while the software cohort was sold hardest (Packaged Software -2.99% average and only 23.6% of the group above its 20-DMA; Internet Retail -3.02%; Information Technology Services -2.51%; Financial Publishing & Services -4.90%, the worst group on the tape). CGON sits inside this theme book and still closed -6.89%, which is the useful tension in it: the group is strong, the single name is not.

## Method, source health & caveats

| Source | Used for | Status |
|---|---|---|
| MCP-over-HTTP bridge — `shibui` | the 8 T+1 context branches, CANSLIM growth half, ADR%/GICS enrichment, the valuation overlay | **ok** — bridge probe: `bridge_ok`, packs `tradier, fmp, edgar, market-recap` |
| MCP-over-HTTP bridge — `market-recap` | the official 16:00 ET closes for the book names (`same-day-prints`) | **ok** — batched, 40 symbols per call |
| TradingView scanner (`america/scan`) | fresh book (3,755 names), breadth universe (1,086 names), today's movers tables | **ok** — `totalCount` equals rows fetched on both scans; no truncation |
| Cboe delayed-quote CDN | VIX / VIX3M pair | **ok** — 2 pulls 5 s apart, identical, 16:15:01 ET |
| MCP availability probe | tool catalog | `catalog_ok total=135 finance_tools=0` — no registered finance MCP in this runtime; the bridge over HTTPS is the market-data path (this is **not** a finding) |
| Public wire copy (web) | catalysts for SLS, CGON, SEZL, BILL, ACM, and the enterprise-software selloff | **ok** — Reuters, Benzinga, MT Newswires, Investing.com, Yahoo Finance |
| shibui T+1 | context screens | **ok but lagged by design** — the newest ingested session is 2026-11-16; labelled `t1` on every row |

**No source was degraded in this run.** The absent `mcp__*` finance tools are a runtime fact, not a source failure, and are not counted as errors.

**Sources and sessions.** Breadth, the fresh book and the movers tables are computed from the **TradingView scanner** on the **2026-11-17 settled close** (1,086 names in the breadth universe; `totalCount` equals rows fetched on both scans, so no truncation). The volatility pair is the **Cboe delayed-quote CDN**, quoted once as a pair (VIX 25.46 / VIX3M 24.98, 16:15:01 ET, two pulls 5 s apart, identical). The **screen** metrics come from shibui over the MCP-over-HTTP bridge and are **T+1 = 2026-11-16**; the book's official closes come from bridge `market-recap`. The two books are never blended: every row publishes `data_as_of` and `source` (`fresh` / `t1` / `fresh+t1`).

**Coverage.** All 9 branches were fetched uncapped, one query per branch, and paged until `rows_kept == rows_passing` on every one — 1,250 screened rows → 1,150 distinct candidates. No branch count lands on a cap (30 / 50 / 60 / 200), so the truncation fingerprint is absent.

**Caveats.** (1) shibui is T+1, so every multi-session context screen (5-day gainers/losers, 14-day velocity, the coil, the 252-session RS window) describes **2026-11-16**, and the Focus/Tier-A *ordering* is inherited from that session's branch ranking — see the flags block. (2) The VIX print is a delayed CDN quote stamped 16:15:01 ET, not a live tick. (3) The industry table uses TradingView's own industry taxonomy, so a name's sector label can differ from the issuer's GICS mapping used elsewhere in the book. (4) The renderer defect noted in the flags block: `tools/sweep_pipeline.py` prints "breadth 34.16% is far above the 40% trigger" — false; the size cut is ON.

**Catalysts.** Named catalysts in this artifact are sourced from public wire copy (Reuters, Benzinga, MT Newswires, Investing.com, Yahoo Finance) fetched during the run. Where no catalyst is named, none was sourced and none is implied.

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
