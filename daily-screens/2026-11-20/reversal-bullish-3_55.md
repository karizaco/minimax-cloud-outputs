# Bonde Reversal Bullish — Friday, 20 November 2026

## TL;DR

- **Mechanical passers: 0** of 817 names scanned · mode **LIVE** · signal session **2026-11-20** · entry 15:58–16:00 ET.
- **Ideas promoted: 0** — no name passed every gate, so there is nothing to promote: the one candle survivor (IFF) failed the washout, ADR and long-term-trend gates.
- **The candle is read at ~15:55 ET** — the 16:00 print can still move the close, the DCR and the stop.

## Candidates

| Ticker | Company | Entry | Stop | Stop % | Stop class | Stop basis | Body low | Bar low | Bar high | Stop vs bar low | DCR | Body | Lower shdw | Tail | ADR | Drop days | 1-day chg | Vol vs 30d avg | Capitulation | Mkt cap |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

_No name passed every gate today._

## Promoted ideas

_No idea promoted: zero names passed every gate on 2026-11-20, so there is no entry, no stop and no catalyst to write here. The single candle survivor is accounted for under `## Not promoted`._

## Not promoted

- **IFF** (International Flavors & Fragrances, NYSE, $19.86B cap) — **passed every candle gate**: fresh 5-day low **78.30**, DCR **0.777** (close 79.31 in the top 22% of the day's range), hammer (lower shadow 0.80 vs upper 0.29, 3.8× the body — descriptive, not a gate), body ratio 0.162, volume 2.33M vs the 290k floor (95% of the 30-session mean → LOW_VOLUME, no capitulation), close 79.31 ≥ $5, and it closed **+0.89%** on the day off that low. **Failed three history gates**: (1) *no washout* — the low 78.30 undercut the prior close 78.61 by only **−0.39%** (needs ≤ −1.5%), and there was just **1 down day** in the last 5 sessions, so Bonde's "2–3 day decline with a washout" is absent; (2) *ADR(20) 2.65% < 3%* — a slow mover; (3) *long-term trend* — 79.31 vs the 20-session-ago close 94.15 is **84.2%**, under the 92% floor, i.e. a multi-month downtrend, not exhaustion at support. **Not promoted:** a textbook hammer inside a long-term downtrend with no prior decline is not the setup Bonde buys, and there is no dated catalyst behind the bar — the last company news is the 18 Nov Brazil Forest Lab release, the last earnings were 3 Nov, and BofA cut the stock to Underperform on 8 Nov (no fresh catalyst, no trade). **Invalidated if** IFF closes below **78.30** (the signal bar's low) / it fails to reclaim **81.16** (the 5-session-ago close) within 3 sessions of 2026-11-20.

## Bonde gate matrix

_No candidates._

## Filter funnel

| Step | Filter | Left |
|---|---|---|
| 1 | NYSE/NASDAQ/AMEX, type=stock, mcap > $5B, close ≥ $5, avg vol(10d) > 1M | 817 |
| 2 | DCR ≥ 0.60 (close in the top 40% of the day's range) | 1 |
| 3 | + published shadow > body, hammer (lower ≥ 2× upper), body ≤ 0.30, volume ≥ 290k | 1 |
| 4 | + 5-day low, decline+washout, ADR ≥ 3%, trend, minv3, avg vol 30d | 0 |

## Method, source health & caveats

- **Session alignment — proof this scan is for today:** TV implied previous close vs shibui's latest settled close: **12/12 agree** (100.0%) → mode **LIVE**. The scanner's session is pinned before any gate is applied.
- **The signal is TODAY's live candle, not yesterday's.** The routine proves this at runtime (alignment above); it no longer resolves the screen date as "shibui's latest settled date", which was a one-session lag.
- **The candle is read at ~15:55 ET, five minutes before the close.** The 16:00 print can change the close, the DCR and the stop. Treat the entry as the 16:00 close.
- **`v ≥ 290,000` uses a partial day's volume** (as of ~15:55 ET). A name that clears 290k only after the close was wrongly excluded.
- **ADR(20) is computed over the 20 SETTLED sessions before today**, not over a window that includes the incomplete live bar.
- **`vol_vs_30d_avg_pct` compares a partial day's volume with a full-day 30-session mean**, so it reads slightly low at 15:55 ET. `capitulation = CAPITULATION` at ≥ 150% of that mean, `LOW_VOLUME` below it.
- **The market-cap gate uses TradingView's live `market_cap_basic`**, not shibui's `valuation` table, which stores stale rows per symbol and can admit a phantom name if the cap filter is applied before the latest-row pick.
- **"Prefer higher priced stocks" is a ranking preference, not a filter** — the published gate is `c >= 5`; names are ordered by DCR then ADR.
- **`stop_class` is published on every row, not buried in prose.** `STRUCTURAL` = the published stop IS the signal bar's low, the level where the exhaustion thesis is structurally dead; `BODY_LOW` = the published stop is Bonde's default body low, which sits INSIDE the bar's own range and is therefore tighter than the structural level; `CAPPED` = the 2.5% max-loss cap bound the stop; `NO_LEGAL_STOP` = no stop Bonde's rule accepts, so the name is not a trade. `stop_vs_bar_low_pct` is signed: positive = the stop is ABOVE the bar low (inside the bar).
- **The stop rule is Bonde's, not the house's.** His default is the **low of the candle body** of the signal day; the shadow (bar) low is his explicitly sanctioned ALTERNATIVE and is legal only when it is within 2.5% of the purchase price. So the body low is used whenever it is a real level, and the shadow low is used only when the body low is degenerate (it sits on the entry). A shadow low more than 2.5% away is not a legal stop, so the body low stands. `body_low`, `body_stop_pct`, `shadow_stop_pct` and `body_stop_degenerate` are published on every row so both levels are visible.
- **The stop is placed the NEXT MORNING, not at the entry.** Bonde buys at 15:55-15:58 **without a stop** and puts the stop in the next morning, after the open, at the level above. So the published stop is a LEVEL to take the next session, not an order resting on the 15:58 fill, and the signal bar's own low (printed before the stop existed) does not count as a breach of it.
- **Bonde's discretionary step is mandatory**: the mechanical screen returns candidates, then the review reduces them to **1–3 ideas** ("no catalyst, no trade", "the reversal bar has to jump off the chart"). Every promoted idea carries a named catalyst and an invalidation test.

| Source | Used for | Status |
|---|---|---|
| TradingView public scanner | live session OHLC for the universe | ok (817 names) |
| shibui-finance (bridge) | settled history, latest close | ok for every PUBLISHED candidate (the day-alignment check resolved against shibui's latest settled close) |
| market-recap (bridge) | market state / index backdrop | not used by this screen — the day-alignment proof is the TradingView + shibui pair |

_Generated by cron #4 `reversal-bullish-3:55` · tool `tools/reversal_bullish.py` · session 2026-11-20 · contract `bonde-artifact-v4` · `_source=mcp`_
