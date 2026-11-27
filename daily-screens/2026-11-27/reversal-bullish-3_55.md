# Bonde Reversal Bullish — Friday, 27 November 2026

## TL;DR

- **Mechanical passers: 0** of 845 names scanned · mode **LIVE** · signal session **2026-11-27** · entry = the settled 16:00 ET close (cross-checked against market-recap: 0.00% difference on 5/5 names).
- **Ideas promoted: 0** — _the discretionary review found nothing Bonde would take; there was no reversal bar to reduce._
- **The session was a melt-up, not a washout** — SPY +1.62%, QQQ +2.69%, 701 of 844 names advancing; only 6 names made a new 5-day low and every one failed the candle geometry, so gate 1 alone rejected all 117 candle-gate survivors.

## Candidates

| Ticker | Company | Entry | Stop | Stop % | Stop class | Stop basis | Body low | Bar low | Bar high | Stop vs bar low | DCR | Body | Lower shdw | Tail | ADR | Drop days | 1-day chg | Vol vs 30d avg | Capitulation | Mkt cap |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

_No name passed every gate today._

## Promoted ideas

_No idea promoted today._ The mechanical screen returned **0 passers**, so the discretionary step had nothing to reduce to 1–3. Bonde's own filter points the same way — "no catalyst, no trade" — and today's tape offered no flush to reverse: the index closed up 1.62% and only 6 names in the universe printed a new 5-day low.

The six new-low names are reviewed under **Not promoted** below. None of them is a signal, and none is promoted here.

## Not promoted

_Zero names passed every gate, so there is no candidate to promote or dismiss. The review below records the six names that DID make a new 5-day low — gate 1 is the filter that eliminated all 117 candle-gate survivors, and a reviewer should see what the tape actually offered. Each line names the gates it passed, why it was not promoted, and its invalidation test._

- **VRTX** (Vertex Pharmaceuticals) — passed 9 of 12 gates: new 5-day low 502.90 (prior 4-session low 513.80), DCR 0.973, ADR 3.15%, close $534.57. **Rejected:** the lower shadow (14.47) is SMALLER than the body (17.20 = 52.8% of the range), and the 3-session change is only −0.74%, so it is a gap-down-and-rally, not a washout into a reversal. Invalidation: a close below 502.90 kills the reversal thesis.
- **GME** (GameStop) — passed the washout gate (−3.00% under the prior close intraday, −3.52% over 3 sessions) and made a new 5-day low 26.16. **Rejected:** DCR 0.194 — it closed in the bottom fifth of its range, not the top 40%. Invalidation: a close below 26.16.
- **AVTR** (Avantor) — passed the washout gate (−2.75% intraday, −5.97% over 3 sessions), new 5-day low 14.52. **Rejected:** DCR 0.255, body 69.1% of range, and it sits 12.11% under its 20-day close (trend gate). Invalidation: a close below 14.52.
- **HRL** (Hormel Foods) — new 5-day low 22.66. **Rejected:** DCR 0.095, ADR 2.43% below the 3% floor, and the washout was only −1.86% intraday / −1.56% over 3 sessions. Invalidation: a close below 22.66.
- **PRMB** (Primo Brands) — the closest miss: new 5-day low 22.77, body only 3.1% of range, washout gate passed (−3.15% over 3 sessions). **Rejected:** DCR 0.508 (needs ≥ 0.60) and the lower shadow (0.32) is not 2× the upper shadow (0.30) — not a hammer. Invalidation: a close below 22.77.
- **WMG** (Warner Music Group) — new 5-day low 31.77, body 8.6% of range. **Rejected:** DCR 0.543, the lower shadow is not 2× the upper (0.63 vs 0.43), ADR 3.00% sits on the floor, and the washout was only −2.13% intraday / −1.10% over 3 sessions. Invalidation: a close below 31.77.

_Gate attribution across the 117 candle-gate survivors: gate 1 (5-day low) 0/117 · gate 5 (decline + washout) 6/117 · gate 8 (trend) 59/117 · gate 6 (ADR) 88/117 · gate 30-day average volume 115/117. The binding constraint was gate 1, and it was not a near miss: on a day when only 6 of 844 names made a new 5-day low, none of the six was a reversal bar._

## Bonde gate matrix

_No candidates._

## Filter funnel

| Step | Filter | Left |
|---|---|---|
| 1 | NYSE/NASDAQ/AMEX, type=stock, mcap > $5B, close ≥ $5, avg vol(10d) > 1M | 845 |
| 2 | DCR ≥ 0.60 (close in the top 40% of the day's range) | 117 |
| 3 | + published shadow > body, hammer (lower ≥ 2× upper), body ≤ 0.30, volume ≥ 290k | 117 |
| 4 | + 5-day low, decline+washout, ADR ≥ 3%, trend, minv3, avg vol 30d | 0 |

_Funnel note: rows 2 and 3 publish the same figure because the screen reports the count left after ALL candle-side gates. Measured on this session's live pull: DCR ≥ 0.60 alone left 473 of 845; the full candle chain (DCR + shadow > body + hammer + body ≤ 0.30 + price ≥ $5 + volume ≥ 290k) left 117; the history gates left 0. Only 4 of 845 names were dropped on the volume floor (SLF 170.6k, VIRT 259.8k, RVTY 285.6k, SITE 285.6k), and all four were up 0.3–1.5% on the day, so none of them was a reversal bar._

## Method, source health & caveats

- **Session alignment — proof this scan is for today:** TV implied previous close vs shibui's latest settled close: **12/12 agree** (100.0%) → mode **LIVE**. The scanner's session is pinned before any gate is applied.
- **The signal is TODAY's live candle, not yesterday's.** The routine proves this at runtime (alignment above); it no longer resolves the screen date as "shibui's latest settled date", which was a one-session lag.
- **Session regime — the reason nothing passed.** SPY +1.62% (728.32), QQQ +2.69% (650.99), IWM +1.83% (273.79), DIA +1.26% (507.60) on the official 16:00 ET close; **701 of 844 names advancing** (median change +1.08%) on the same live scanner pull the screen uses. A reversal bar needs a flush to reverse; today the tape flushed almost nothing.
- **How scarce a new 5-day low was.** Only **6 of the 844 names with history** printed a low under their prior 4-session low, and all six failed the candle geometry (see *Not promoted*). That is why gate 1 removed 117 of 117 survivors — a regime fact, not a near miss, and not a data failure: settled history resolved for all 117 survivors, with no ticker falling back to Nasdaq.
- **The candle was read at 15:55–15:59 ET, at or just before the close.** The 16:00 print can still move the close, the DCR and the stop. Treat the entry as the 16:00 close.
- **The published bar was cross-checked against the official close.** The screen's close was compared with `market-recap get_quotes` for AAPL, NVDA, TSLA, VRTX and WMG: **5/5 identical (0.00% difference)**, and each `previous_close` matched shibui's 11-25 settled close. So the bar is the settled 16:00 ET bar, not a pre-auction print.
- **`v ≥ 290,000` uses the session's volume as read at 15:55–15:59 ET**, i.e. essentially the full day but not the official settled volume. 4 of 845 names fell below the floor (see the funnel note); none of them was a reversal bar.
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
| TradingView public scanner | live session OHLC for the universe, breadth | ok (845 names; 844 with settled history) |
| shibui-finance (bridge) | settled history, latest close | ok for every PUBLISHED candidate (the day-alignment check resolved against shibui's latest settled close; latest settled session 2026-11-25) |
| market-recap (bridge) | official 16:00 ET close cross-check + index backdrop | ok — 5/5 closes identical to the scanner (0.00%); SPY +1.62%, QQQ +2.69%, IWM +1.83%, DIA +1.26% |

_Generated by cron #4 `reversal-bullish-3:55` · tool `tools/reversal_bullish.py` · session 2026-11-27 · contract `bonde-artifact-v4` · `_source=mcp`_
