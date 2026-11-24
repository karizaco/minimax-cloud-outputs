---
artifact: breadth-snapshot
contract: breadth-artifact-v1
cron: "#10 stock-screener-breadth-snapshot"
fire_time_et: "2026-11-24 14:00:05 ET"
data_date: "2026-11-23"
live_date: "2026-11-24"
breadth_universe: "NYSE/NASDAQ/AMEX, market cap > $10B, 870 names"
vix_quote_time: "2026-11-24 13:48:31 ET (Yahoo chart API, 5m bar pinned to the fire clock)"
vix_pair: "VIX 26.45 / VIX3M 25.54 — single pair, used everywhere in this document"
cross_reference: "end-of-day counterpart: daily-screens/2026-11-24/breadth.md (cron #09, 18:30 ET)"
size_cut_pct: 50
uncertainty: true
late_cycle: false
degraded_sources: 1
---
_contract: breadth-artifact-v1 · data_date 2026-11-23 · universe 870 names · breadth 29.08% (pctile 12.6 · BELOW_NORMAL) · divergence +29.08 pp (BROAD) · AD 734/132/4_

# Breadth & Regime Snapshot — Tuesday, 24 November 2026 (intraday, cron #10)

**Intraday breadth read — 2026-11-24, snapshot at 14:00:05 ET.** The breadth, advance/decline and index-positioning layers describe the *settled* 2026-11-23 session (shibui is T+1). The tape and the volatility pair are *live* 2026-11-24. The two layers are never blended. Source of record for prices: the MCP bridge's `market-recap`; for the settled breadth series: shibui via the same bridge.

## TL;DR

- **Breadth is still a washout, one violent session deeper.** Only **29.08%** of the 870 large caps are above their own 20-DMA — the **12.6th percentile** of the past year (BELOW_NORMAL), up from the 2026-11-20 washout low of 16.69% but still nowhere near repaired, and **0 of 5** index ETFs are above theirs. The 2026-11-23 advance/decline tally was **734 advancing / 132 declining / 4 unchanged** (ratio 5.561) — a genuine breadth thrust — but the ten-session net is still **-1761** and the ADL slope **-270.81 net advances per session**.
- **The divergence is the number that changes position sizing: +29.08 pp, BROAD (80.5th percentile).** The average large cap is materially healthier than the index — with 0 of 5 index ETFs above their 20-DMA, the *index* is the weak leg. Today's live tape shows the same shape intraday: RSP **+0.52%** and IWM **+0.65%** against SPY **-0.67%**, QQQ **-2.09%** and SMH **-7.06%**.
- **Read this as a rotation, not a repair — and the volatility pair flatters it.** The AI-hardware complex is unwinding Monday's Nvidia-led bounce (Nvidia's reinstatement of Jensen Huang as CEO drove Monday's +31.5% session) while defensives bid — health care **+3.09%**, staples **+1.70%**. VIX is quoted at **26.45** but hit **32.38** in the pre-market before decaying through the session, and VIX/VIX3M = **1.0356** keeps `uncertainty` ON. Regime stays defensive: size cut **ON** (50), index below its 20-DMA, not late cycle.

## Breadth — 2026-11-23 settled session (shibui)

| Metric | Value |
|---|---|
| Universe | NYSE/NASDAQ/AMEX, market cap > $10B |
| Names in universe | 870 |
| Above 20-DMA | 253 (29.08%) |
| Below 20-DMA | 617 (70.92%) |
| Above 50-DMA | 414 (47.59%) |
| Index ETFs above their own 20-DMA | 0 of 5 (0.0%) |
| Index ETFs above their own 50-DMA | 0 of 5 (0.0%) |
| Advance/decline — settled session | 734 advancing / 132 declining / 4 unchanged (A/D ratio 5.561) |

The universe is **not frozen** — the market-cap floor is applied to the latest `valuation` row, so the count moves as those rows refresh. Today's universe: **870 names**.

## Participation — advance/decline and the 10-session ADL

| Date | Advancing | Declining | Unchanged | Net | ADL (cumulative) | ADL slope (10d) |
|---|---|---|---|---|---|---|
| 2026-11-10 | 392 | 471 | 6 | -79 | -511 | 29.32 |
| 2026-11-11 | 564 | 301 | 4 | +263 | -248 | 26.75 |
| 2026-11-12 | 216 | 650 | 3 | -434 | -682 | 19.21 |
| 2026-11-13 | 522 | 339 | 8 | +183 | -499 | 13.41 |
| 2026-11-16 | 229 | 635 | 5 | -406 | -905 | -0.03 |
| 2026-11-17 | 161 | 706 | 1 | -545 | -1450 | -50.45 |
| 2026-11-18 | 376 | 489 | 3 | -113 | -1563 | -72.39 |
| 2026-11-19 | 75 | 790 | 3 | -715 | -2278 | -156.22 |
| 2026-11-20 | 174 | 691 | 4 | -517 | -2795 | -260.13 |
| 2026-11-23 | 734 | 132 | 4 | +602 | -2193 | -270.81 |

**A/D ratio 5.561 today** (734 advancing / 132 declining). Over the last 10 sessions the net advances total **-1761** and the ADL slope is **-270.81 net advances per session** (10-session A/D ratio 0.662). The ADL is cumulative from 2026-08-28, so it is a LEVEL; the slope is the rate.

## Breadth percentile — where today's level sits in its own history

Percentiles are against the trailing 1-year distribution of the same series (261 sessions, 2025-11-10 → 2026-11-23). A level without a percentile is a number without a context.

| Metric | Value | Percentile | Band |
|---|---|---|---|
| `breadth_pct` | 29.08% | — | — |
| `breadth_pctile_1y` | 12.6 | — | BELOW_NORMAL |
| `breadth_pct_50dma` | 47.59% | — | — |
| `breadth_pctile_1y_50dma` | 23.8 | — | NORMAL |
| `index_etfs_above_20dma` | 0 of 5 | 16.5 | BELOW_NORMAL |

## Breadth divergence — broad market versus index ETFs

| Metric | Value | Band | 1-year percentile |
|---|---|---|---|
| `breadth_divergence` | +29.08 pp | BROAD | 80.5 |

`breadth_divergence` = the large-cap universe's share above its own 20-DMA minus the index ETFs' share above their own 20-DMA. **BROAD** means the average large cap is materially healthier than the index; **NARROW** means the index is healthier than the average large cap — the cap-weighted index is carried by its biggest names while the average stock is not participating; **MATCHED** means they agree.

| Date | Divergence (pp) |
|---|---|
| 2026-11-17 | +39.17 |
| 2026-11-18 | +36.98 |
| 2026-11-19 | +23.48 |
| 2026-11-20 | +16.69 |
| 2026-11-23 | +29.08 |

## Index positioning — distance from the 50-DMA

| Symbol | Close | 20-DMA | 50-DMA | Distance from 50-DMA | ATR multiple |
|---|---|---|---|---|---|
| IWM | 265.74 | 275.66 | 277.82 | -4.35% | -2.65 |
| QQQ | 651.03 | 675.47 | 709.79 | -8.28% | -5.16 |
| QQQE | 110.62 | 114.58 | 117.66 | -5.98% | -4.58 |
| RSP | 212.82 | 217.86 | 214.75 | -0.90% | -0.88 |
| SPY | 722.29 | 745.65 | 759.41 | -4.89% | -4.59 |

## Live tape — 2026-11-24

| Instrument | Sector | Last | Change | Day range (low – high) |
|---|---|---|---|---|
| SPY | S&P 500 | 717.44 | -0.67% | 712.14 – 720.92 |
| QQQ | Nasdaq-100 | 637.40 | -2.09% | 631.15 – 643.47 |
| RSP | S&P 500 equal-weight | 213.94 | +0.52% | 211.28 – 214.76 |
| QQQE | Nasdaq-100 equal-weight | 109.67 | -0.85% | 108.75 – 110.16 |
| IWM | Russell 2000 | 267.47 | +0.65% | 263.97 – 268.25 |
| | | | | |
| SMH | VanEck Semiconductor | 427.67 | -7.06% | 418.46 – 442.97 |
| XLK | Technology | 156.79 | -3.44% | 154.90 – 158.79 |
| XLV | Health care | 184.96 | +3.09% | 179.27 – 185.00 |
| XLP | Consumer staples | 91.92 | +1.70% | 90.44 – 92.37 |
| XLE | Energy | 60.48 | +1.01% | 59.56 – 60.69 |
| XLC | Communication services | 104.54 | +0.91% | 103.02 – 105.22 |
| XLRE | Real estate | 43.22 | +0.73% | 42.52 – 43.40 |
| XLF | Financials | 56.00 | +0.63% | 55.31 – 56.33 |
| XLB | Materials | 50.10 | +0.40% | 49.36 – 50.16 |
| XLY | Consumer discretionary | 117.44 | +0.44% | 116.06 – 118.03 |
| XLU | Utilities | 43.45 | +0.29% | 42.92 – 43.63 |
| XLI | Industrials | 161.44 | -0.63% | 159.78 – 162.02 |

**The tape is a rotation, not a liquidation.** The AI-hardware complex is giving back
Monday's governance-driven bounce — SMH **-7.06%**, XLK
**-3.44%**, QQQ **-2.09%** — while the
equal-weight market is **green**: RSP **+0.52%**, IWM
**+0.65%**. Defensive sectors took the money: XLV
**+3.09%**, XLP **+1.70%**, XLE
**+1.01%**. SPY **-0.67%** — the cap-weighted
index is the weak leg of the session while the average name is not.

All 17 quotes were cross-checked against a second feed inside the bridge call
(`agreement: agrees`, 17/17, max difference 0.04%). Snapshot time
**2026-11-24T19:03:06.313Z**; `market_state: open` — this is a live mid-session print, not a
settled close.

## Volatility — single pair, live

| | Value | Prior close | Change |
|---|---|---|---|
| **VIX** | **26.45** | 26.61 | -0.60% |
| **VIX3M** | **25.54** | 25.81 | -1.05% |
| **VIX / VIX3M** | **1.0356** | — | inverted (front month above second month) |

**One pair, one source, one moment.** VIX 26.45 / VIX3M 25.54, quoted
**2026-11-24 13:48:31 ET**, both symbols read from the **same** 5-minute bar. The pair is a
**live print** — the feed's latest bar for this session is the one pinned to the fire clock,
so nothing here is reconstructed. It is used everywhere in this document.

**The ratio is above 1.0, so `uncertainty` is ON** — and the front month is *above* the
second month, which is the classic near-term-event-risk structure. The pair is also
down on the day (-0.60%) even though the tape sold off, because
the fear premium was taken out *earlier in the session*: the same Yahoo 5-minute series
carried VIX to **32.38** in the pre-market at 09:05 ET, opened the
regular session at **29.94** and had decayed to a **26.21 – 26.81**
band by 13:30–14:05, when the 26.45 above was printed. The published pair is the
honest *fire-clock* print, but it sits near the low end of the day's range — read it as
"volatility normalised by 14:00 ET", not as "the morning never happened".

## Regime

| Flag | Value | Rule |
|---|---|---|
| `size_cut_pct` | 50 | size cut triggers only when the index is below its 20-DMA **and** breadth < 40% |
| `uncertainty` | true | VIX/VIX3M > 1.0 |
| `late_cycle` | false | any index ETF more than 6% above its own 50-DMA |
| `index_below_20sma` | true | fewer than 3 of the 5 index ETFs above their own 20-DMA |

## Flags

- **The published volatility pair sits near the low end of today's range.** VIX traded
  **32.38** in the pre-market at 09:05 ET, opened the regular session
  at **29.94** and was quoted at **26.45** at the fire clock — the regular
  session's low was 26.18. The pair is correct for its timestamp, and it is the
  number the `uncertainty` flag reads — but it understates the stress the session carried at
  the open.
- **The `BROAD` divergence band is an artifact of the index posture, not a disagreement
  between two sources.** With **0 of 5** index ETFs above
  their own 20-DMA, the index leg of the spread is floored at zero, so a
  +29.08 pp reading is what "29.08% of large caps above their
  20-DMA against 0% of index ETFs" mechanically produces. It measures how far the trend
  structure lags the tape, not a source disagreement.
- **QQQE is the weakest single link in the live tape relative to its own index.**
  QQQE **-0.85%** is a smaller decline than QQQ
  **-2.09%**, but its volume is only 96,333 shares
  against QQQ's 38,854,349 — the equal-weight Nasdaq leg is thin enough that the
  two should not be read as the same signal.
- **The advance/decline tally is the 2026-11-23 SETTLED session, and no live A/D figure is
  published.** The intraday participation for 2026-11-24 is not computed here; the tape
  section reports the index and sector prints only, and nothing in this artifact should be
  read as a live advance/decline tally.

## Method, source health & caveats

### Method

- **Two layers, never blended.** The breadth layer is the **SETTLED 2026-11-23 session**
  from shibui (T+1 — the newest ingested session at the 14:00 ET fire). The tape and the
  volatility pair are **LIVE 2026-11-24**. They live in separate sections, carry separate
  labels, and the front matter carries both dates (`data_date` / `live_date`).
- **The universe is the contract's, not a new one:** NYSE/NASDAQ/AMEX, market cap > $10B,
  **870 names**. It is **not frozen** — the market-cap floor is applied to the latest
  `valuation` row, so the count moves as those rows refresh. It was 869 on 2026-11-20
  and is 870 on 2026-11-23; the drift is disclosed here rather than smoothed away.
- **The advance/decline tally uses the SAME population as the breadth percentage** — the
  indicator-joined large-cap set — so 734 + 132 + 4
  = 870, the published universe count. The A/D window is 60 sessions;
  the ADL is cumulative from **2026-08-28** (a level) and the published slope
  (**-270.81 net advances per session**) is the rate over the last
  10 sessions.
- **Percentile windows.** The level percentiles are expanding ranks against the trailing
  261-session distribution (2025-11-10 → 2026-11-23).
- **`atr_extensions` is non-empty** — all five index ETFs are carried, read from the `ticker`
  key the SQL actually emits, so `late_cycle` can fire rather than sitting permanently false.
  Every one of the five is *below* its own 50-DMA, so `late_cycle` is genuinely false today.
- **One number per field, one source per field.** Prices and the tape come from the bridge's
  `market-recap`; the breadth, A/D and index-ETF rows come from shibui; the volatility pair
  comes from Yahoo's chart API. Where two sources could serve the same field, one was chosen
  and named here.

### Source health

| Source | What it served | Status |
|---|---|---|
| shibui MCP (`stock_data_query`) via the bridge | the settled breadth series, the advance/decline tally, the five index-ETF rows, the ATR extensions | **ok** — newest ingested session 2026-11-23 (T+1) |
| MCP bridge `market-recap` `get_quotes` | the live tape — 17 symbols (5 index ETFs, 11 sector ETFs, SMH); 17/17 cross-checked against a second feed, `agreement: agrees`, max difference 0.04% | **ok** |
| Yahoo chart API (`^VIX` / `^VIX3M`) | the volatility pair, both symbols from the same 5m bar pinned to the fire clock | **ok** — *fallback* |
| Cboe delayed-quote CDN | the primary volatility source | **failed: HTTP 403 (Cloudflare)** — the Yahoo fallback served the pair |
| Web search (Reuters / Benzinga / MarketWatch / Investopedia / Dow Jones) | the day's driver only — Nvidia's governance overhang (congressional interviews scheduled 1–2 Dec), the Sanofi–Insmed $41bn deal, and the pending inflation print before the Fed's December meeting | **ok** — no published number comes from it |

**Degraded sources: 1** — the Cboe delayed-quote CDN (HTTP 403 from this egress). The
volatility pair was published from the Yahoo fallback instead, and the `source` string names
it.

### Caveats

- **The breadth numbers describe 2026-11-23, not today.** Today's tape is a rotation out of
  AI hardware into health care, staples and energy; the settled layer does not yet contain
  any of it.
- **The 2026-11-23 breadth figure is itself a bounce.** The 10-session ADL net is still
  **-1761** and the slope **-270.81 net advances per
  session** — one 734/132 session did not turn the ten-day rate. The single-session A/D
  ratio of 5.561 and the ten-session ratio of 0.662 are different
  facts about different windows.
- **The volatility pair is a fire-clock print, not a settled close.** It will be superseded
  by the 16:00 ET settle, and the end-of-day counterpart
  (`daily-screens/2026-11-24/breadth.md`, cron #09, 18:30 ET) is the file that carries the
  settled version of today's session.
- **Not verified:** no intraday path, no options-chain or flow confirmation, no per-name
  catalyst check, and the sector rotation is read from index ETFs rather than from the
  constituent stocks.
