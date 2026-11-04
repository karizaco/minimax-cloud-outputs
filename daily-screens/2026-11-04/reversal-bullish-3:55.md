# Bonde Reversal Bullish — 3:55 PM ET scan (2026-11-04)

**Verdict: 1 mechanical passer out of 921 (NTRA) — and on the OFFICIAL close it is a CONDITIONAL idea, not a clean one.**
Every published Bonde gate passes, but two things force the caveats: the closing auction turned the
signal bar into a near-doji (body = 9% of range), which pushes the stop rule onto the bar's low
(−5.50% from entry, over Bonde's 2.5% loss cap), and Natera reports Q3 2026 **after tomorrow's
close** — inside the intended 1–3 day hold.

- **Signal session**: **2026-11-04** — the LIVE US session, scanned at 15:55 ET and re-verified against
  the official close after the bell.
- **Entry window**: 2026-11-04 3:58–4:00 PM ET (Bonde: "enter between 3.58 to 4PM, or MOC").
  **Official close / MOC fill: $391.03** (Nasdaq official, 4:00 PM ET).
- **Universe**: NYSE / NASDAQ / AMEX, type=stock, market cap > $5B, avg volume (10d) > 1M → **921 names** scanned.
- **Passing every Bonde gate**: **1** (candle gates left 97).

## Session alignment — proof this scan is for today

The routine proves which session the scanner is describing before it computes anything:

- TV implied previous close vs the **settled-history source's** latest close (Nasdaq fallback this run):
  **12/12 agree** (100.0%) → the scanner was on today's live session.
- Verdict: **LIVE**.

## Candidates

| Ticker | Company | Entry (official close) | Stop | Stop % | DCR | Body | Lower shdw | Upper shdw | ADR | 3d chg | 5d chg | Mkt cap |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **NTRA** | Natera, Inc. | **391.03** | **381.25** | 2.50% | 0.838 | 0.093 | 21.52 | 1.78 | 4.54% | −5.62% | −7.87% | $55.9B |

**Session bar (regular session, settled):** O 393.42 · H 395.20 · L 369.51 · **C 391.03** · V 2,731,889
Prev close 388.63 → **+0.62% on the day, after a −4.92% washout to 369.51 at 10:50 ET.**
It gapped up +1.23% at the open, sold off hard through late morning, then reversed 5.4% off the low
and closed in the top 16% of the range. Relative strength: flat on a day when DIA +3.10% and SPY +1.64%.

### Stops

- **NTRA** — stop **381.25** (−2.50% from the official close), basis: bar low 369.51 is 5.50% away,
  which breaches Bonde's 2.5% maximum-loss cap, so the level is tightened to the cap.
  **Read that stop carefully**: 381.25 sits one cent above the 381.00 the stock printed at 14:40 ET —
  it is inside the signal bar's own noise, and it is a "the reversal failed" stop, not a structural one.
- At the 15:55 snapshot the body was 21.3% of range, so the body-low rule applied and the stop was
  $387.57 — **exactly the entry, i.e. zero cushion**. The closing auction erased the body and turned
  that degenerate stop into the capped 381.25 above. Neither reading gives a comfortable stop.

### Bonde gate matrix (NTRA)

| 1. 5-day low | 2. DCR ≥ .60 | 3. shadow > body | 3b. hammer | 3c. body ≤ .30 | 5. decline + washout | 6. ADR ≥ 3% | 7. price ≥ $5 | 8. trend | vol | minv3 | avolv30 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

- 5-day low: 369.51 vs prior-5 min low **376.375** (2026-11-02) ✓
- Washout: low 369.51 = **−4.92%** below the prior close (gate: ≥ 1.5% intraday) ✓
- Prior decline: **−5.62% over 3 sessions, −7.87% over 5** (gate: ≥ 3%) ✓
- Hammer: lower shadow 21.52 vs upper 1.78 (12.1×) ✓ — the tail:body ratio is quoted as
  description only, never as a gate
- DCR **0.838** on the official close; ADR(20) **4.54%**; mcap **$55.9B**; avg vol(30) **1.76M** ✓

### Filter funnel

| Step | Filter | Left |
|---|---|---|
| 1 | NYSE/NASDAQ/AMEX, type=stock, mcap > $5B, close ≥ $5, avg vol(10d) > 1M | 921 |
| 2 | DCR ≥ 0.60 (close in the top 40% of the day's range) | 97 |
| 3 | + published shadow > body, hammer (lower ≥ 2× upper), body ≤ 0.30, volume ≥ 290k | 97 |
| 4 | + 5-day low, decline+washout, ADR ≥ 3%, trend, minv3, avg vol 30d | 1 |

## Discretionary review — Bonde's step, and where this one fails

**Bonde: "the reversal bar has to jump off the chart", "no catalyst, no trade".**

**Catalyst (named, sourced):**
- **2026-11-04 (today)** — Natera IR: *Signatera™ in Head and Neck Cancer: Three New Publications*
  (npj Precision Oncology, JAMA Otolaryngology, Advances in Radiation Oncology). Recurrence detected a
  median **4.3 months before radiographic progression** (91.7% sens / 96.4% spec); **35% absolute
  reduction in 2-year locoregional recurrence** for Signatera-positive patients on chemo; 100%
  sensitivity in the HPV+ subgroup.
  https://www.natera.com/company/news/signatera-in-head-and-neck-cancer-three-new-publications-demonstrate-strong-clinical-performance-and-actionability/
- **2026-11-03** — Medicare expands coverage for the Signatera MRD test in hepatocellular carcinoma
  (Business Wire).
- **2026-11-05 after the close** — **Q3 2026 results, 4:30 PM ET call.** This is the dominant catalyst
  and it is a **binary event inside the trade window**, not a tailwind. Consensus expects revenue
  +19.8% y/y (slowing from +34.7%); 23 analysts, avg PT $394.31–$416.39.

**Why this is conditional, not clean:**
1. **The entry bar is a doji, not a thrust.** Body 9.3% of range (2.39 on a 25.69 range). Every
   published gate accepts it — body ≤ 0.30 is Bonde's own prose rule — but "the reversal bar has to
   jump off the chart" is weaker on a doji close than on the 15:55 red body.
2. **The stop is inside the bar's noise** (381.25 vs the 14:40 print of 381.00). It gets you out on
   a failed reversal, but it is a tight stop on a name that already swung 5.4% intraday.
3. **Earnings tomorrow after the close.** A 1–3 day swing hold cannot survive a binary print. If you
   will not carry the position into the Nov 5 release, this is not a trade — it is a watch.
4. **The tape was not helping.** NTRA closed flat while DIA +3.10% / SPY +1.64%. The reversal came
   from its own 10:50 washout, not from sponsorship. Insider Form 144s filed Nov 2–3 and CFO sales
   Oct 27–28 (10b5-1, vesting-driven) sit in the background; Zacks cut the name to Strong Sell on
   Oct 16, though BTIG raised its target to $430 on Oct 27.

**How to size it, if you take it:** half size or less, stop 381.25, and either exit before the
Nov 5 print or treat it as an event bet with a defined loss — not as a clean Bonde swing.

## Backdrop (close, 2026-11-04)

| Instrument | Close | Change |
|---|---|---|
| SPY | 766.72 | **+1.64%** |
| DIA | 533.10 | **+3.10%** |
| IWM | 283.90 | **+1.47%** |
| QQQ | 691.95 | +0.97% |
| US 10-yr | 4.894 | −5.8 bp (−1.17%) |
| DXY | 101.515 | −0.35% |

## Source health

| Source | Used for | Status |
|---|---|---|
| TradingView public scanner | live session OHLC for the universe | ok (921 names) — but see the two traps below |
| Nasdaq settled history (fallback) | settled history, alignment reference | ok (latest settled session 2026-11-03) |
| Nasdaq official quote (`/api/quote/NTRA/info`) | official close + session volume | ok — close $391.03, +0.62%, 4:00 PM ET, V 2,731,889 |
| market-recap (MCP bridge) | entry quotes + index backdrop | ok (market_state `post` after the bell; NTRA 390.975 at 16:00:01 ET) |
| Yahoo chart API (5m + daily) | intraday path, pre-market bars, settled history | ok — Yahoo's last 5m print (389.45) lagged the closing auction vs Nasdaq's official 391.03 |
| Natera IR / Business Wire / MarketBeat / StockStory | catalysts, earnings date, analyst context | ok |
| MCP catalog probe | tool inventory | `catalog_ok total=135 finance_tools=0` — no finance MCP registered; the MCP-over-HTTP bridge was used instead |
| shibui-finance (MCP bridge) | settled history | **failed at screen time** — the bridge script was not yet on disk when the screen ran; the documented Nasdaq fallback carried the run (`history_source=nasdaq`), so the artifact was not degraded |

**Two data traps found this run (both generalisable):**

1. **TradingView's `high` column carried the PRE-MARKET high.** TV reported H = 397.00 for NTRA;
   Yahoo's 5m bars show 397.00 printed at **07:05 and 08:45 ET**, before the open, and a regular-session
   high of **395.20**. TV's inflated range depresses DCR (0.783 vs 0.838) — conservative here, but it
   means a TV range is not always the regular-session range.
2. **The TV scanner's `close` lagged the closing auction.** TV held 387.59 while the official close was
   391.03 (+0.88%). A 15:55 scan is ~5 minutes from the bell, so the entry print must be taken from
   the official close, not from the scanner's last trade. The same lag changed the body ratio from
   0.213 (non-doji) to 0.093 (doji) and therefore flipped the stop rule.

## Method & caveats

- **The signal is TODAY's live session, not yesterday's settled bar.** The routine proves it at runtime
  (12/12 alignment hits, 100%).
- **The 15:55 screen was re-verified against the official close** after the bell; every published gate
  still passes, but the body and the stop changed (see trap 2).
- **`v ≥ 290,000` is judged on a partial day's volume** at scan time. NTRA cleared it by 7× (2.07M at
  15:55) and finished at 2.73M, so the gate is not marginal here.
- **ADR(20) is computed over the 20 SETTLED sessions before today**, not over a window including the
  incomplete live bar.
- **The market-cap gate uses TradingView's live `market_cap_basic`** ($55.9B), not shibui's `valuation`
  table, which stores stale rows per symbol.
- **"Prefer higher priced stocks" is a ranking preference, not a filter** — the published gate is
  `c >= 5`. NTRA at $391.03 ranks first on that preference anyway.
- **The CSV beside this file holds the raw 15:55 screen output** (entry 387.57, stop 387.57, DCR 0.657)
  as produced by `tools/reversal_bullish.py`. The values in this document supersede it: they are the
  settled close and the capped stop.

_Generated by cron #4 `reversal-bullish-3:55` · tool `tools/reversal_bullish.py` · screen started 2026-11-04T15:55:44-05:00 · post-close verification 16:01 ET · `_source=mcp` (live) + `_source=nasdaq_settled` (history fallback)_
