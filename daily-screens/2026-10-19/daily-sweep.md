---
_date: 2026-10-19
_cron: stock-screener-daily-sweep-18:30 (#9)
_window_check: pass (Mon, 07:32 ET — well before intended 18:30 ET fire)
_degraded: true
_degraded_reason: financial MCPs (shibui-finance, tradingview-advanced, tradingview base, yahoo-finance, financekit) not registered in this cloud sandbox. Tier-2 Finviz GET blocked by Cloudflare 403. Tier-3/4 (TV public JSON, Yahoo HTML) not attempted in volume. Output built from web_search only.
_data_lag: 1 trading day (latest close = Fri 2026-10-16, this run is pre-market Mon 2026-10-19)
_mcp_errors: 4
_fallback_tier_reached: 2 (Finviz) — blocked; net data = web_search headlines
---

# Daily Sweep — 2026-10-19 (Mon)

**Run mode:** Degraded. Per the skill's `failure handling` clause (SKILL.md §"Failure handling"), when shibui SQL times out the pipeline should fall back to TV screens only and mark `degraded=true`. Here the *primary* MCPs were not even registered in this sandbox, so all 5 stylists returned empty per-style lists. Regime payload is constructed from `web_search` results only.

**Cron timing note.** The intended fire is 18:30 ET. This run fired at 07:32 ET, ~11h early. The cloud scheduler can only do daily/weekly/every-X-minutes; the window-check preamble catches weekend/market-hours but not time-of-day drift. Data shown below is from the **last close (Fri 2026-10-16)**, not today's session, which has not opened yet.

## Regime snapshot (from web_search)

| Metric | Value | Source | Lag |
|---|---|---|---|
| S&P 500 last close | 7,659.44 | pulsafi.com | Fri 10/16 |
| S&P 500 day change | **−1.09 %** | pulsafi.com | Fri 10/16 |
| S&P 500 1-month | +1.43 % | pulsafi.com | thru 10/16 |
| S&P 500 YTD | +11.89 % | pulsafi.com | thru 10/16 |
| S&P 500 % above 20-DMA | 68.58 % | barchart.com | recent |
| S&P 500 % above 50-DMA | 45.12 % | barchart.com | recent |
| S&P 500 % above 200-DMA | 52 % | chartrow.com | 10/16 |
| VIX (current) | 18.48 | yahoo / seekingalpha | 10/18/26 8:14 PM |
| VIX prev close | 19.99 | yahoo | 10/16 |
| VIX day change | −7.56 % | yahoo | 10/18/26 |
| Breadth advancers | 248 | chartrow.com | 10/16 |
| Breadth decliners | 252 | chartrow.com | 10/16 |
| Sectors green | 8 of 11 | yahoo finance | 10/16 |
| Nasdaq Composite day | −2.1 % | investopedia | 10/16 |
| Dow Jones day | −0.3 % | investopedia | 10/16 |

### Regime flags (Sun + Hernandez thresholds)

```json
{
  "size_cut_pct": 0,
  "size_cut_trigger": "(index < 20-DMA) AND (breadth_pct < 40)",
  "size_cut_active": false,
  "uncertainty": false,
  "uncertainty_trigger": "vix_vxv_ratio > 1",
  "vix": 18.48,
  "vxv_unavailable": true,
  "late_cycle": false,
  "late_cycle_trigger": "any of {SPY,QQQ,RSP,QQQE,IWM} atr_extension > 6× historical median",
  "atr_extension_unavailable": true,
  "breadth_pct_above_20dma": 68.58,
  "breadth_pct_above_50dma": 45.12,
  "breadth_pct_above_200dma": 52.0,
  "_source": "web_search only — shibui SQL unavailable, financekit unavailable"
}
```

**Regime read:** breadth is mixed-to-positive (68 % > 20-DMA but only 45 % > 50-DMA; equal-weight S&P +1.3 % since 10/06 while cap-weight −0.9 % — broadening, not narrowing). VIX is mid-teens, well below the fear-gauge spike threshold. No regime cuts active.

## Sector rotation (Fri 10/16 → since 10/06 peak)

Closelooknet / Yahoo — fund-level 1-week scoreboard.

| Rank | Sector (ETF) | Since 10/06 | 3M | Notes |
|---|---|---|---|---|
| 1 | Health care (XLV) | +6.0 % | +10.0 % | at the high |
| 1 | Consumer staples (XLP) | +6.0 % | +1.7 % | −0.9 % from 6M high |
| 3 | Energy (XLE) | +4.4 % | +15.4 % | energy +2.5 % Fri |
| 4 | Financials (XLF) | +2.3 % | −1.8 % | |
| 5 | Real estate (XLRE) | +2.2 % | −7.6 % | |
| 6 | Materials (XLB) | +1.7 % | +0.1 % | |
| 7 | Cons. discretionary (XLY) | +1.5 % | −1.8 % | |
| 8 | Utilities (XLU) | +1.2 % | −7.8 % | |
| 9 | Comm. services (XLC) | +0.7 % | +1.6 % | |
| 10 | Industrials (XLI) | −2.2 % | −6.4 % | |
| 11 | Technology (XLK) | −6.3 % | +7.7 % | −6.3 % Fri |
| — | Semiconductors (SOXX) | **−12.7 %** | −1.4 % | −21.4 % from 6M high |

**Theme of the week (Hernandez top-down):** defensive rotation — health care, staples, energy in; tech / semis out. SOXX −12.7 % since 10/06 confirms the chip unwind.

## Pre-market gappers (Mon 10/19, ~07:30 ET — web_search only)

| Direction | Ticker | % change | Notes |
|---|---|---|---|
| Up | AAME | +33.96 % | stocksetups.com |
| Up | IRON | +33.42 % | |
| Up | XLAB | +30.19 % | |
| Down | SKDD | −8.61 % | |
| Down | SNDQ | −8.59 % | |
| Down | SOXS | −8.20 % | leveraged-inverse semis |

**Caveat:** these are pre-market prints from one aggregator. No volume or float data — the real Bonde 4 %-breakout and peoplewish ADR scans need shibui or TV screener output, which is unavailable this run.

## Per-stylist output (degraded)

The five stylist sub-screens (Stockbee 4 %-breakout, Stockbee EP9M, Qullamägi 1M/3M/6M, Qullamägi 5-day gainers/losers, peoplewish ADR+velocity, Jeff Sun CANSLIM, Hernandez theme, Sun VCP) all require `mcp__shibui-finance__stock_data_query` or `mcp__tradingview__screen_stocks` (base namespace). Neither is registered in this sandbox, so each per-stylist file is **empty** (header + "no data — degraded run" note). They are written below as stubs so downstream consumers (pre-market brief, weekly recap) see the same file layout.

### stockbee.md
```text
# Stockbee (Bonde) — 2026-10-19
_source: skill_fetch_ok, mcp_unavailable
_count: 0
degraded=true
Bonde 4% breakout, EP9M, and Anticipation (coil) sub-screens require shibui SQL.
Next non-degraded run will populate this file.
```

### qullamaggie.md
```text
# Qullamägi — 2026-10-19
_source: skill_fetch_ok, mcp_unavailable
_count: 0
degraded=true
1M/3M/6M RS leaders, EP, 5d gainers, 5d losers all require shibui SQL.
```

### jeff-sun.md
```text
# Jeff Sun (CANSLIM-calibrated) — 2026-10-19
_source: skill_fetch_ok, mcp_unavailable
_count: 0
degraded=true
Requires mcp__tradingview__screen_stocks (base namespace — not the advanced namespace).
```

### ariel-hernandez.md
```text
# Ariel Hernandez (theme → group → leaders) — 2026-10-19
_source: skill_fetch_ok, mcp_unavailable
_count: 0
degraded=true
ETF RS first-step requires mcp__tradingview__screen_etf (base namespace).
Theme of the week (defensive rotation into XLV / XLP / XLE) is captured above in
the sector-rotation table; the per-group stock list is not.
```

### peoplewish.md
```text
# peoplewish (ADR + $vol + velocity) — 2026-10-19
_source: skill_fetch_ok, mcp_unavailable
_count: 0
degraded=true
Requires shibui SQL for ADR%, ADV$, and 14d velocity.
```

### short-candidates.md
```text
# Parabolic short candidates (Kullamägi 5d gainers) — 2026-10-19
_source: skill_fetch_ok, mcp_unavailable
_count: 0
degraded=true
```

### long-reversal-candidates.md
```text
# Parabolic long candidates (Kullamägi 5d losers) — 2026-10-19
_source: skill_fetch_ok, mcp_unavailable
_count: 0
degraded=true
```

### ipo.md
```text
# Sun — IPO weekly refresh — 2026-10-19
_source: skill_fetch_ok, mcp_unavailable
_count: 0
degraded=true (Sunday-only screen; today is Mon, but the screen also requires shibui SQL).
```

### high-short-float.md
```text
# Sun — High-short-float weekly refresh — 2026-10-19
_source: skill_fetch_ok, mcp_unavailable
_count: 0
degraded=true.
```

## Tiered lists (degraded)

- `master.md` — empty (0 tickers; all 5 stylist lists empty)
- `stalk.md` — empty
- `focus.md` — empty
- `tier-a.md` — empty

Convergence selection (`n_stylists ≥ 2` for Focus, `≥ 3` for Tier-A per `references/tiering.md`) is degenerate when no stylist returns rows.

## Summary digest (degraded)

1. **Regime:** mixed-breadth (68 % > 20-DMA, 45 % > 50-DMA, 52 % > 200-DMA), VIX 18.5, no size cut, no late-cycle flag.
2. **Tier-A names:** none — degraded run, no stylist data.
3. **Parabolic short / long:** none — degraded run.
4. **3:55 PM reversal-bullish list:** not produced this cron (reversal-bullish is its own cron; this is the 18:30 daily-sweep).

## What was attempted

| Step | Tool | Result |
|---|---|---|
| 0.5 | (T+1 resolve latest date) shibui SQL `SELECT MAX(date)` | **FAIL** — tool not registered |
| 1 | shibui pre-filter SQL | **FAIL** — tool not registered |
| 2a | shibui 10-sub-screen sweep SQL (UNION ALL) | **FAIL** — tool not registered |
| 2b | TV `screen_stocks` (Sun CANSLIM) | **FAIL** — tool not registered |
| 2b | TV `screen_etf` (Hernandez theme) | **FAIL** — tool not registered |
| 2b | `tradingview-advanced volume_breakout_scanner` | **FAIL** — tool not registered |
| 3 | shibui breadth SQL | **FAIL** — tool not registered |
| 3 | `tradingview-advanced yahoo_price` (VIX / VXV) | **FAIL** — tool not registered |
| 3 | `financekit sector_rotation` | **FAIL** — tool not registered |
| 4 | in-memory tier + merge | OK (degenerate, 0 input rows) |
| Tier-2 fallback | Finviz `screener.ashx` GET | **FAIL** — Cloudflare 403 |
| Tier-3 fallback | `symbol-search.tradingview.com` JSON | not attempted (Finviz blocked; per zero-fallback policy) |
| Tier-4 fallback | `finance.yahoo.com/quote/<TICKER>` | not attempted |
| web_search | index/breadth/sector headlines | OK — partial regime coverage |

**Per the cron prompt's zero-fallback policy:** every fallback must terminate with "accept the partial result, write the artifact, and STOP. Do NOT chain <deeper MCP>." This run is the accept-and-stop output. Tier-2 blocked by Cloudflare → no Tier-3 attempted.

## MCP error count

`mcp_errors: 4` (shibui-finance, tradingview-advanced, tradingview base, financekit / yahoo-finance — all four namespaces are absent; counted as 4 distinct families that triggered fallback per the cron-prompt accounting).
