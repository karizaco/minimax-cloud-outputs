---
date: 2026-11-02
cron: 04-reversal-bullish-3:55
fire_time_et: 15:55
snapshot_et: 16:00 (settled close, 21:00:00Z)
status: ok
primary_source: shibui canonical Bonde SQL via MCP-over-HTTP bridge (signal bar 2026-10-30)
live_bar_source: Yahoo chart API settled 2026-11-02 daily bar + TradingView scanner (universe)
canonical_passers: 3
live_bar_passers: 0
actionable_same_day_entry: 0
carry_forward_candidate: FUTU
errors: 0
---

# Reversal Bullish — 3:55 PM ET, Monday 2026-11-02

## Headline

**Zero names are actionable for a same-day (2026-11-02) entry under Bonde's published criteria, and the
canonical scan's three passers all failed the stop-discipline test once today's session was resolved.**

Two independent scans were run, because the routine's canonical source is a T+1 feed and Bonde's own
process scans the *live* bar:

| Scan | Signal bar | Universe | Passers |
|---|---|---|---|
| **A — canonical** (`screen.py emit-sql reversal_bullish`, shibui via MCP bridge) | 2026-10-30 (Fri) | shibui US equities | **3** (BSP, FUTU, CDW) |
| **B — live bar** (Bonde's actual 3:30–3:55 PM process, on today's settled bar) | 2026-11-02 (Mon) | 978 names, $5B+ cap, >1M ADV | **0** |

Scan B is the one that matches Bonde's published workflow (scan the live bar, enter 3:58–4:00 PM ET or
MOC the same day). It produced **nothing**: 25 names cleared the candle-geometry stage and every one of
them was then rejected by a history/quality gate. Scan A's three names were real setups on Friday's bar,
but a Monday-close entry no longer honors the ≤2.5% stop rule for any of them.

**The one name worth carrying forward is FUTU** — the cleanest hammer of the three — but at today's close
it is 6.84% above its stop, so it is a watch, not an entry.

## Scan A — canonical shibui SQL (signal bar 2026-10-30)

shibui's latest available date at 15:55 ET was **2026-10-30** (`MAX(date) WHERE date <= 2026-11-02`),
i.e. the feed is T+1 as documented. The canonical SQL is already T+1-safe and Bonde-strict, and it
returned exactly three names.

| | **BSP** | **FUTU** | **CDW** |
|---|---|---|---|
| Exchange / type | NASDAQ · common | NASDAQ · **ADR** | NASDAQ · common |
| Signal bar 10-30 O/H/L/C | 45.98 / 45.99 / **43.25** / 45.52 | 98.75 / 99.39 / **96.20** / 98.45 | 156.19 / 158.82 / **144.34** / 153.79 |
| Signal volume | 1,654,035 | 1,223,812 | 2,444,774 |
| F1 5-day low (low = min of 5 sessions) | ✅ 43.25 | ✅ 96.20 | ✅ 144.34 |
| F2 DCR ≥ 0.60 | ✅ 0.828 | ✅ 0.705 | ✅ 0.653 |
| F3 (o−l) > (c−o) | ✅ | ✅ | ✅ |
| F3b hammer (lower ≥ 2× upper) | ✅ 2.27 / 0.01 | ✅ 2.25 / 0.64 | ✅ 9.45 / 2.64 |
| F3c body ≤ 0.30 | ✅ 0.168 | ✅ 0.094 | ✅ 0.165 |
| F5 washout (low vs prior close ≤ −1.5%) | ✅ −7.55% | ✅ −5.19% | ✅ −12.63% |
| F5 prior decline (3d or 5d ≤ −3%) | ✅ −3.09% (3d) | ✅ −3.82% (3d) | ✅ −4.72% (3d) / −6.86% (5d) |
| F6 ADR20 ≥ 3% | ✅ 9.64% | ✅ 3.48% | ✅ 3.50% |
| F7 close ≥ $5 | ✅ | ✅ | ✅ |
| F8 trend intact (close ≥ 0.92 × close₂₀) | ✅ 45.52 vs 29.47 | ✅ 98.45 vs 94.00 | ✅ 153.79 vs 122.63 |
| U cap > $5B, ADV30 > 1M | ✅ $28.92B / 3.57M | ✅ $13.80B / 1.09M | ✅ $19.65B / 1.48M |
| Published volume floor (min 3-session ≥ 100k) | ✅ | ✅ | ✅ |
| **Stop** | 45.52 (body low) | **96.20** (shadow — body 9.4% < 15%) | 153.79 (body low) |

All three passed every published gate on the 2026-10-30 bar. That is the mechanical output of the screen.

## Resolution against today's session (2026-11-02, settled close)

The next session after the signal bar is today, so the tradeable entry is **today's close** (16:00 ET,
MOC). Settled closes from Yahoo's `regularMarketTime = 21:00:00Z` print:

| | **BSP** | **FUTU** | **CDW** |
|---|---|---|---|
| Today O/H/L/C | 46.20 / 46.90 / 44.645 / **45.38** | 100.48 / 107.07 / 100.48 / **103.26** | 154.80 / 156.65 / 147.89 / **150.55** |
| Today volume | 1,013,275 | 1,465,575 | 1,596,716 |
| vs signal close | −0.31% | **+4.89%** | −2.11% |
| Stop level | 45.52 | 96.20 | 153.79 |
| Stop breached today? | **yes** (closed 45.38 < 45.52; low 44.645) | no (low 100.48) | **yes** (closed 150.55 < 153.79; low 147.89) |
| Undercut the signal bar's LOW? | no (44.645 > 43.25) | no (100.48 > 96.20) | no (147.89 > 144.34) |
| Risk from entry to stop | **−0.31%** (stop already above entry) | **6.84%** | **−2.15%** (stop already above entry) |
| Risk to shadow stop | 4.69% | 6.84% | 4.12% |
| Volume quality (TV RVOL-10d) | 0.42 (weak) | 1.50 | 0.94 |
| **Verdict** | ❌ reject | ⚠️ watch | ❌ reject |

**BSP — reject.** The body stop (45.52, the Friday close, because Friday's candle closed below its open)
was invalidated during today's session: the stock traded to 44.645 and closed at 45.38, below the stop.
The only meaningful level left is Friday's low at 43.25, 4.69% away — nearly double Bonde's 2.5% cap —
on the weakest volume of the three (RVOL 0.42). Structurally it is still alive (today never undercut
43.25), so this is a *stale setup*, not a failed one: it is now a Day-2 entry, which Bonde's own
"first day of the swing" rule rejects.

**FUTU — watch, not entryable today.** Friday's bar was the best hammer on the list (DCR 0.705, a 9.4%
body with a 7.5× tail, washout −5.19%, ADR 3.48%, trend intact). But it rallied **+4.89% in one
session**, so at today's 103.26 close the 96.20 stop sits 6.84% below — well outside the 2.5% cap that
Bonde requires of the stop he places. The setup is intact (today's low 100.48 never touched 96.20), so
this is a *chase* problem, not a broken one: **an entry at ≤ $98.67 restores the full 2.5% stop
discipline** (96.20 ÷ 0.975). Below that, it is the one genuine reversal-bullish candidate on the board.

**CDW — reject.** Same failure mode as BSP: the body stop at 153.79 was invalidated today (closed
150.55, low 147.89), leaving Friday's low at 144.34, 4.12% away. Structurally intact — today's low
147.89 stayed above 144.34 — so again a stale Day-2 setup rather than a structural failure.

> **Spec defect worth flagging.** The canonical SQL's stop formula is
> `CASE WHEN body_ratio < 0.15 THEN low ELSE LEAST(open, close) END`. On a **red** candle
> (`close < open`) `LEAST(open, close) = close`, so the "body low" stop equals the entry price and the
> computed stop risk is **0.00%** — the ≤2.5% filter then passes anything, no matter how wide the real
> risk is. BSP (body_ratio 0.168) and CDW (0.165) are both in that blind spot: the query returned them
> with `stop_risk_pct = 0.0`. The real risk is only visible once the *shadow* stop is used. Every stop
> figure in this report is recomputed against the live entry price and reported honestly, but the
> canonical query itself should be amended (use `LEAST(open, close)` only when it sits **below** the
> close, otherwise fall back to the bar low).

## Scan B — live bar on today's settled close (Bonde's actual process)

Bonde runs the scan between 3:30 and 3:55 PM on the **live** bar and enters 3:58–4:00 PM the same day.
Re-running every gate on today's settled 2026-11-02 bar across the full universe:

- Universe: **978 names** — NYSE 646 / NASDAQ 331 / AMEX 4, close ≥ $5, market cap > $5B,
  30-day average volume > 1M, type in (common stock, ADR).
- **25 names** cleared candle geometry (DCR ≥ 0.60, lower shadow > body, hammer, body ≤ 0.30, volume ≥ 290k).
- **0 names** passed all gates.

Rejection reasons across the 25 geometry survivors:

| Gate | Rejected |
|---|---|
| F6 ADR20 ≥ 3% (slow movers) | 21 |
| F5 prior decline ≥ 3% (no washout into the bar) | 20 |
| F1 5-day low | 19 |
| F5 intraday washout (low vs prior close) | 19 |
| Stop ≤ 2.5% | 3 |
| F8 long-term trend intact | 2 |

The reason is the session itself: the tape rose for most of the day and then reversed hard into the bell
(SPY high 763.86 → low 751.62 → close 751.95, closing on the low). Most large caps never printed a
5-day low, never had a 2–3 day decline into the close, and their 20-day ATR stayed compressed.

**Closest live candidate: ARXS** — 2026-11-02 O 50.74 / H 51.28 / L 49.445 / C 50.70, body 2.2%,
DCR 0.684, ADR20 5.49%, 3-day decline −6.34%, stop 49.445 at 2.48% risk. It fails **one** gate: today's
low (49.445) is above the 5-day low of 46.38 set on 2026-10-29, so it is not making a 5-day low. Not a setup.

> Cross-check: the same scan built from TradingView's live snapshot instead of Yahoo's settled bar gave
> 37 geometry survivors and **0** passers, with the same leading rejection pattern (no 5-day low 30,
> no prior decline 30, ADR < 3% 27, no washout 25). Both constructions agree on the headline.

## Market context (2026-11-02 settled)

| Index | Close | Change |
|---|---|---|
| SPY | 751.95 | −0.50% |
| QQQ | 681.09 | −1.36% |
| IWM | 279.06 | −0.10% |
| DIA | 519.26 | +0.41% |
| ^VIX | 21.32 | **+9.78%** |

A broad-market decline with a volatility spike and a clean growth-to-value rotation (QQQ −1.36% vs DIA
+0.41%) — and a late reversal that closed the index on its low. That is the environment in which
Bonde's own reversal setup should be plentiful; it is not, because the reversal came *after* the lows
rather than into them.

## Method

- **Scan A** — `scripts/screen.py emit-sql reversal_bullish 2026-10-30`, run against shibui via the
  MCP-over-HTTP bridge (`shibui stock_data_query`). The emitted SQL is the canonical one: 60-day
  windowed CTE, `rn = 1` per symbol, `shibui.valuation` de-duplicated to each symbol's latest row,
  every Bonde gate applied in-query. The date 2026-10-30 came from
  `SELECT MAX(date) FROM shibui.stock_quotes WHERE date <= '2026-11-02'` — shibui is T+1.
- **Scan B** — the same gate set re-implemented against today's settled bar: universe and live OHLC from
  the TradingView scanner (`POST scanner.tradingview.com/america/scan`), history and the settled bar from
  the Yahoo chart API (`query1.finance.yahoo.com/v8/finance/chart`, 6-month daily, `includePrePost=true`),
  978/978 names returning a 2026-11-02 bar.
- **Entry prices** are the settled 16:00:00 ET closes. **Signal-bar values** are from shibui; Yahoo's
  Friday bars were used only as an independent cross-check and agree to the cent (BSP 45.98/45.99/43.25/45.52,
  FUTU 98.75/99.39/96.20/98.45, CDW 156.19/158.82/144.34/153.79).
- **Stops** are recomputed against the live entry price, not the query's `stop_risk_pct` (see the spec
  defect note above). Shadow stop is used whenever the body is under 15% of the range, per Bonde.

## Source health

| Source | Use | Status |
|---|---|---|
| MCP availability probe (`probe_mcp.py`) | catalog check | `catalog_ok total=133 finance_tools=0` — no finance MCP registered on the platform; `bridge_ok packs=tradier,fmp,market-recap` |
| MCP bridge → `shibui stock_data_query` | canonical SQL, latest-date probe | **ok** — `MAX(date) ≤ 2026-11-02` = `2026-10-30`; canonical query returned 3 rows |
| MCP bridge → `market-recap get_quotes` | intraday cross-check | **ok but stale for the settled close** — `as_of 15:58:45 ET` (a pre-bell tick), volumes below the official session (BSP 935,606 vs 1,013,275). Used for cross-check only; **entry prices are not taken from this source** |
| TradingView scanner `POST /america/scan` | universe, live OHLC, market cap, RVOL | **ok** — HTTP 200, 978 names (type in stock+dr; note `type=stock` alone silently drops 91 large ADRs/REITs, FUTU among them) |
| Yahoo chart API (`query1`) | settled daily bars, history for all gates | **ok** — HTTP 200, 978/978 names, `regularMarketTime 21:00:00Z`, no 429s; 3 symbol formats needed a retry (`BRK-B`, `PBR-A`, `BF-B`) |
| Finviz | fallback tier | not reached — no fallback required |

**Cross-source disagreement, disclosed:** TradingView's post-bell snapshot printed BSP 45.655 and
CDW 149.265 against Yahoo's official 16:00:00 ET closes of 45.38 and 150.55 (0.60% and 0.86%). Yahoo's
`regularMarketTime` is exactly the 16:00:00 ET bell and its volumes match the full session, so Yahoo is
published here as the single source for entry prices. The bridge's 15:58:45 ET tick is not the closing
print and is not published as an entry price either.

**errors: 0** — no source failed; the only degradations were the bridge's pre-bell quote timestamp and
the TradingView snapshot drift, both disclosed above and neither affecting the published numbers.

## Files

- `daily-screens/2026-11-02/reversal-bullish-3:55.md` (this file)
- `daily-screens/2026-11-02/reversal-bullish-3:55.csv` — 3 canonical passers + 1 live-bar near-miss, with
  every gate value, both stop treatments, and a `verdict` column
