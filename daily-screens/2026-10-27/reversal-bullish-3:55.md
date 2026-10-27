# Reversal Bullish — 3:55 PM ET (Bonde / Stockbee) — 2026-10-27

> **Degraded data path — read first.** The `shibui-finance` MCP is **not registered** in this cloud
> sandbox and `finviz.com/screener.ashx` returns **HTTP 403** from this egress, so the canonical
> T+1-safe shibui SQL could not be executed. The eight Bonde filters were applied verbatim to daily
> bars pulled from the **Nasdaq public quote API** (`api.nasdaq.com/api/quote/<sym>/chart`), with the
> universe built from the Nasdaq screener API. Every row is tagged `_source=nasdaq_public_api` and the
> run is marked `degraded=true`. Signal bar = **2026-10-26** (the last settled session) — this is the T+1
> analogue of shibui's `MAX(date) <= <cron_date>` resolution. 1,414 of 1,420 universe names were scannable.

## Headline

**Three names passed all eight Bonde criteria, and only one of them is still tradeable.** CELH, HIMS and
CBRE cleared all eight filters on the 2026-10-26 signal bar. Measured against the 2026-10-27 16:00 ET
close — the price at which Bonde's 3:58–4:00 PM entry would have been filled — **CELH (-0.53%) and CBRE
(-0.99%) both closed below their body-low stop**, so those two are dead setups rather than entries.
**HIMS is the single live candidate**: it closed +1.23% at 27.93, leaving 1.50% of room to the 27.51
body-low stop, well inside Bonde's ≤2.5% loss cap.

## Candidates

| # | Symbol | Exchange | Signal close | Body-low stop | Stop risk | DCR (close in range) | Body ratio | Tail:body | ADR20 | 2d-ago | 20d-ago | Decline | Day |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **CELH** | NASDAQ-CM | 28.15 | 28.02 | 0.48% | 0.899 | 0.154 | 4.9x | 3.85% | 28.36 | 28.00 | 1 d | Day 1 |
| 2 | **HIMS** | NYSE | 27.59 | 27.51 | 0.29% | 0.514 | 0.111 | 3.6x | 6.00% | 29.13 | 28.78 | 3 d | Day 1 |
| 3 | **CBRE** | NYSE | 122.88 | 122.79 | 0.07% | 0.510 | 0.032 | 15.0x | 3.23% | 131.24 | 130.35 | 3 d | Day 1 |

| Symbol | 2026-10-27 close | Chg | Risk from close to stop | Stop status | After-hours last |
|---|---|---|---|---|---|
| CELH | 28.000 | -0.15 (-0.53%) | stop above price | **STOP BREACHED** | $27.72 (-1.00%) |
| HIMS | 27.930 | +0.34 (+1.23%) | 1.50% | **intact** | $27.956 (+0.09%) |
| CBRE | 121.665 | -1.215 (-0.99%) | stop above price | **STOP BREACHED** | $121.65 (-0.01%) |

### Entry alert (Bonde format, actionable names only)

```
REVERSAL-BULLISH 3:55: HIMS entry ~27.93 (2026-10-27 close) stop 27.51 funds held mcap>5B proxy
```

HIMS is the only name where the stop is still below the entry price. CELH closed at 28.000 against a
28.015 body-low stop and CBRE closed at 121.665 against a 122.79 stop; both would have been filled out
at the close, so they are reported for completeness and excluded from the entry alert.

## What the data shows

The screen is genuinely selective rather than merely strict-looking: across 1,414 scannable large-
caps, only three names cleared all eight gates, and the two most common failures are the two that
define the Bonde candle itself. **1184 names failed the tail>=3x-body test** and **1174 failed the
5-day-low test** - a name has to both print a long lower wick *and* be making a new 5-day low on the
same bar, and very few large-caps do that on any given session. ADR was the next most common
disqualifier (868 failures), which is the filter that removes slow movers such as utilities, staples
and gold miners; the price floor ($15) and the long-term-trend filter were the least binding (101
and 233 failures respectively).

Two further names passed all eight content criteria and were dropped only by the universe gate, which requires 30-day average volume above 1M shares (the `filters.md` proxy for the institutional-ownership set): **GGAL** (close 35.35, DCR 0.754, tail 3.45x, ADR 3.7%, adv30 948374) and **OGC** (close 24.79, DCR 0.557, tail 3.40x, ADR 3.3%, adv30 613715). Both are sub-1M-share names, so they sit outside the high-institutional-owned universe Bonde requires; they are listed here for transparency rather than as candidates.

On the strictness of the criteria themselves, two choices inside the published wording are worth flagging.
The skill's criteria table states DCR ≥ 0.5 while `references/filters.md` uses 0.6; **only CELH survives
the 0.6 variant** (DCR 0.899), so HIMS and CBRE are marginal on that gate at 0.514 and 0.510. And Bonde's
published shape is a tail of *3 to 5 times* the body, while the skill's SQL form only enforces a floor of
3x — **CBRE's tail is 15.0x** because its body is 3.2% of the range, so it is mechanically outside the
descriptive 3–5x band even though it satisfies the SQL gate. CELH (4.85x) and HIMS (3.63x) sit inside it.

## Method, definitions and caveats

- **Universe (Bonde's biggest filter):** `market_cap > $5B` on NYSE / NASDAQ / AMEX, the skill's stated
  proxy for "held by at least 1,000 institutional funds" (shibui exposes no `institutional_holders_count`).
  1,420 names qualified; 6 were not scannable (2 with no chart data, 2 newly listed with <21 bars, 2 with a
  zero-range bar). A 30-day average volume floor of 1M shares was also applied per `filters.md`.
- **Signal bar:** 2026-10-26 settled close, used for all eight criteria; the 2026-10-27 16:00 ET close is
  used only as the entry reference, because the signal bar is the previous session in the T+1 data flow.
- **Criterion 1 (5-day low):** signal bar low ≤ min(low) of the last 5 bars. **Criterion 3 (tail):**
  `min(open,close) − low ≥ 3 × |close − open|`. **Criterion 6 (ADR):** mean of `(high−low)/close` over the
  last 20 bars ≥ 3%. **Criterion 8 (trend):** `close ≥ close_20d_ago × 0.92`. Criteria 2, 4, 5 and 7 are
  as written in the skill's table.
- **`body_low_stop`** = `min(open, close)` of the signal bar, per the skill's `next_day_stop` rule. When
  `open == close` it equals the close. `stop_loss_pct` is measured from the signal close; the report's
  `risk_to_stop_pct` is measured from the 2026-10-27 close, which is the actionable entry.
- **Day tag:** "Day 1" = no immediately preceding session also printed a reversal-bar shape (DCR ≥ 0.6,
  body ≤ 0.4), i.e. this is the first day of the swing, per Bonde's rule. "Day 2" / "Day 3+" count
  consecutive prior sessions that did. All three candidates are Day 1. `decline_len` is the count of
  consecutive down closes ending on the signal bar; note CELH's is 1, so its criterion-5 pass comes from
  the 2-day-ago comparison rather than from a consecutive drop.
- **Live quotes** (2026-10-27 16:00 ET close and after-hours) come from the Nasdaq public `info` endpoint
  at 16:13 ET; the after-hours print is a thin-session trade and should not be read as a signal.
- **Not comparable to shibui runs** on a bar-for-bar basis: the shibui universe is its full 9,900-name
  table filtered to market cap > $5B, whereas this run's universe is the 1,420 US-listed common stocks
  the Nasdaq screener returns at the same market-cap floor, so the universe is narrower and any
  mcap > $5B name missing from the Nasdaq screen is out of scope.
  Known missing data: BRK-B and BF-B share classes return no chart from this endpoint (not in the
  1,420-name screen either, so no impact here).

## Files

- `daily-screens/2026-10-27/reversal-bullish-3:55.md` (this file)
- `daily-screens/2026-10-27/reversal-bullish-3:55.csv` (one row per candidate, `_source=nasdaq_public_api`)

## Fallback and errors

| Step | Result |
|---|---|
| `mcp__shibui-finance__stock_data_query` (primary) | **Unavailable** — not registered in this sandbox |
| Finviz screener GET (fallback 2) | **HTTP 403** from this egress (Cloudflare) |
| Nasdaq public quote/chart API (fallback 3) | **Used** — 2,840 requests, 0 transport failures (2 symbols returned no chart) |

Errors that triggered a fallback: **2**. The chain was not extended further; per the zero-fallback
policy the run accepted the substitute source, wrote the artifact, and stopped.
