# CORRECTION — Reversal Bullish 3:55 PM ET, 2026-10-27

> **Correction added 2026-11-01** by the Scout session that produced the original
> 2026-10-27 artifact. The screen itself was sound — 1,420-name universe, 1,414 scannable,
> every bar settled — but **the rule set applied was the skill's literal SQL floors rather
> than Bonde's published criteria**, and the artifact's "actionable" pick was made on a
> mechanical tie-breaker instead of a discretionary read. One name changes, one verdict
> changes, and two structural defects are documented below.
>
> The original artifact is retained unedited at `reversal-bullish-3:55.md` / `.csv`.

## What the original run applied (the 8 gates, verbatim)

| # | Gate as run on 2026-10-27 | Threshold |
|---|---|---|
| F1 | 5-day low | `low <= MIN(low, last 5 bars)` |
| F2 | Close in top half of range (DCR) | `>= 0.50` |
| F3 | Tail vs body | `(min(open,close) - low) >= 3 * ABS(close-open)` (floor only, no ceiling) |
| F4 | Small body | `ABS(close-open) / (high-low) <= 0.40` |
| F5 | Prior decline | `close < close_2d_ago` |
| F6 | ADR | `AVG((high-low)/close, 20 bars) >= 3%` |
| F7 | Price floor | `close >= $15.00` |
| F8 | Long-term trend | `close >= close_20d_ago * 0.92` |
| U | Universe | NYSE/NASDAQ/AMEX, `market_cap > $5B`, `avg_vol_30d > 1M` |

**Data source:** the Nasdaq public quote API. The original run reported the shibui-finance MCP
as "not registered" and stopped there. **That was incomplete** — the MCP *servers* are reachable
over plain HTTPS JSON-RPC from this sandbox via `cloud-prompts/_shared/mcp_bridge.py`, and
shibui answered this re-analysis on the first try. The fallback was taken one step too early.
Numbers below are re-derived from shibui (`mcp.shibui.finance/mcp`, latest bar 2026-10-30).

## Bonde's published criteria, from the source

Pradeep Bonde, *stockbee.blogspot.com*, 2019-11-26 — "Reversal Bullish Scan I use":

```
l = minl5 and (o-l) > (c-o) and (c-l)/(h-l) >= .6 and v >= 290000 and c >= 5 and minv3.1 >= 100000
```

> "I look for sign of selling exhaustion after scanning. Stock which was lower intraday but
> recovers and closes near high and where the candle tail is 3 to 5 times the body is what I like.
> The trick in trading this setup is reducing down your list to just that 1 or 2 ideas…"

Same source, process: run the scan 3:30–3:55 PM, **select 1 to 3 ideas**, *prefer* higher-priced
stocks, enter 3:58–4:00 PM or MOC, stop less than 2%, exit on stop hit if it does not work by the
3rd day.

BreakoutsHappen (the full write-up of the same workflow) adds the discretionary conditions:

> "The reversal bullish is an **exhaustion pattern**… it does not chase strength; it buys the exact
> moment selling pressure runs out on a quality stock that has been beaten down for days."

> "First: this is an exhaustion pattern, so there must have been a **prior decline** in the
> preceding days. The drop should last at least **two to three days**."

> "Second: the candle itself. Red or green does not matter. What we must observe is a long,
> well-defined lower shadow and a small body — squat, or narrow and pushed toward the top of the
> range. A **hammer**, to be clear."

> "The other requirement is visual: the reversal bar has to **jump off the chart**. If you have to
> squint to distinguish it from the candles around it — if it could pass for one more bar in a
> range, or an ordinary pause inside a decline — it is not the signal."

Pradeep Bonde, TraderLion podcast transcript: "for the reversal bullish where it's a little bit more
of a wash out… **there has to be some sort of a wash out**."

### Gate-by-gate: the skill's version vs the published one

| # | Skill as applied | Bonde published | Verdict |
|---|---|---|---|
| F1 | `low <= MIN(low, 5)` | `l = minl5` | correct |
| F2 | DCR `>= 0.50` | `(c-l)/(h-l) >= 0.6` — close in the **top 40%** of the range | **too loose** |
| F3 | `(min(o,c)-l) >= 3*ABS(c-o)` | `(o-l) > (c-o)`; prose "tail 3 to 5 times the body" | **wrong formula + no ceiling** |
| F4 | body `<= 0.40` of range | "small body — squat, or narrow" | house rule, roughly right |
| F5 | `close < close_2d_ago` | prior decline of **2–3 days**, and a **washout** | **far too loose** |
| F6 | ADR `>= 3%` | not published | house rule (SMFG counter-example) |
| F7 | `close >= $15` | `c >= 5`; "prefer higher priced" is a **ranking preference, not a filter** | **too tight** |
| F8 | `close >= c20d * 0.92` | "exhaustion at support, not a falling knife" | house rule, directionally right |
| U | mcap > $5B | "owned by at least 1,000 institutional funds" | proxy; shibui also carries `ownership_stats.percent_institutions` |

Two of the failures run in opposite directions. **F2 is too loose** (0.50 vs the published 0.60),
which is exactly what let a doji with a dominating upper wick through as a "reversal". **F7 is too
tight** ($15 vs the published $5), which is throwing away legitimate setups for a stated
preference. And **F5 is the loose one that matters**: `close < close_2d_ago` is satisfied by a
single marginal down day, so a stock drifting sideways in a range passes it — no decline, no
washout, no exhaustion.

## The three candidates, gate by gate (signal bar 2026-10-26, shibui bars)

**CELH** — O 28.02 / H 28.24 / L 27.36 / C 28.15, vol 4,481,157

| Gate | Value | Skill floor | Published | Verdict |
|---|---|---|---|---|
| F1 5-day low | low 27.36 vs prior-5 min 27.90 | pass | pass | pass |
| F2 DCR | **0.899** | pass (≥0.5) | pass (≥0.6) | pass, with margin |
| F3 tail:body | 5.08× (Nasdaq-rounded 4.85×) | pass (floor 3) | **on the 3–5 band edge** | marginal |
| F3b hammer (lower shadow 0.66 vs upper 0.09) | 7.3× | — | pass | **true hammer** |
| F4 body ratio | 0.148 | pass | pass | pass |
| F5 prior decline | 2-day −0.74%, 3-day −0.57%; prior down-run **0**; 5-day slide −6.0% | pass | **fails "2–3 days"** | **weak** |
| F6 ADR20 | 3.85% | pass | n/a | pass |
| F7 price | 28.15 | pass | pass | pass |
| F8 trend 20d | +0.54% | pass | pass | pass |

**CBRE** — O 122.79 / H 124.27 / L 121.44 / C 122.88, vol 3,470,377

| Gate | Value | Skill floor | Published | Verdict |
|---|---|---|---|---|
| F1 5-day low | low 121.44 vs prior-5 min 123.04 | pass | pass | pass |
| F2 DCR | **0.510** | pass (≥0.5) | **FAIL (≥0.6)** | **fails** |
| F3 tail:body | **15.0×** | pass (floor 3) | **FAIL (outside 3–5 band)** | **fails** |
| F3b hammer (lower shadow 1.35 vs upper 1.39) | 0.97× | — | **FAIL** | **not a hammer** |
| F4 body ratio | 0.032 | pass | pass | pass |
| F5 prior decline | 2-day −6.36%, 3-day −8.74%, prior down-run **2** | pass | **pass — the best decline of the three** | pass |
| F6 ADR20 | 3.23% | pass | n/a | pass |
| F7 price | 122.88 | pass | pass | pass |
| F8 trend 20d | −5.72% | pass | pass | pass (but fails on a 21-session lag — see note) |

**HIMS** — O 27.51 / H 27.94 / L 27.22 / C 27.59, vol 5,755,606

| Gate | Value | Skill floor | Published | Verdict |
|---|---|---|---|---|
| F1 5-day low | low 27.22 vs prior-5 min 27.30 | pass | pass | pass |
| F2 DCR | **0.514** | pass (≥0.5) | **FAIL (≥0.6)** | **fails** |
| F3 tail:body | 3.63× | pass | pass (in band) | pass |
| F3b hammer (lower shadow 0.29 vs upper 0.35) | 0.83× | — | **FAIL** | **not a hammer** |
| F4 body ratio | 0.111 | pass | pass | pass |
| F5 prior decline | 2-day −5.55%, 3-day −5.55%, prior down-run **2** | pass | pass | pass |
| F6 ADR20 | 6.00% | pass | n/a | pass |
| F7 price | 27.59 | pass | pass | pass |
| F8 trend 20d | −4.17% | pass | pass | pass |

**Note on F8:** the correct comparison is `LAG(close, 20)` — 20 sessions back. The shibui query used
in this re-analysis initially used `LAG(close, 21)` and failed CBRE on trend by 0.8%; the value above
uses the correct 20-session lag. The original 2026-10-27 artifact used the correct lag.

## Why "HIMS" was called actionable — and why that was wrong

The original artifact picked HIMS because it was the only name whose body-low stop was still intact
at the 16:00 ET close. That is a **tie-breaker on stop arithmetic, not a discretionary read of the
setup**, and the user was right to challenge it:

- On the signal bar (2026-10-26) HIMS is a small-body doji whose **upper shadow (0.35) is longer
  than its lower shadow (0.29)**. By Bonde's own words it "could pass for one more bar in a range",
  and it fails the published DR floor of 0.6 at 0.514. The decline was real (−5.5% over two
  sessions); the *candle* was not a reversal.
- On the cron day itself (2026-10-27) HIMS printed **O 27.99 / H 28.46 / L 27.59 / C 27.92, +1.20%
  green** — DR 0.379, and its low did not make a 5-day low. It was not a reversal-bullish shape at
  all on the day the scan fired; it was a green bounce. The stock then ran **+5.01% on 10-28**,
  which is a momentum move, not an exhaustion reversal.

The three candidates split Bonde's two conditions, and the screen did not separate them:
**CELH has the candle** (DR 0.899, true hammer) but no preceding decline — its drop was a single
−5.51% session on 10-21 followed by a two-day bounce, so `prior_down_run = 0`.
**HIMS has the decline** (−5.5% over two down sessions) but not the candle.
**CBRE has both the decline and the wick** (three down sessions, −8.74%, low below the 52-week
low) but closes mid-range (DR 0.510) with a doji body.

## What actually happened (closes from shibui, from the 2026-10-26 signal bar)

| Name | 10-26 close | 10-27 | 10-28 | 10-29 | 10-30 | T+3 | Body stop | Shadow stop | Verdict under body stop | Verdict under shadow stop |
|---|---|---|---|---|---|---|---|---|---|---|
| CELH | 28.15 | 28.00 (−0.53%) | 27.98 | 28.16 | 29.12 | **+3.44%** | 28.015 | 27.36 | breached by 0.05% — **and the low 27.10 undercut the signal low 27.36** | **breached** |
| HIMS | 27.59 | 27.92 (+1.20%) | 29.32 (+6.27%) | 29.67 (+7.53%) | 27.68 | **+7.53%** | 27.51 | 27.22 | held (10-27 low 27.59) | held |
| CBRE | 122.88 | 121.65 (−1.00%) | 123.70 | 128.58 | 128.85 | **+4.86%** | 122.79 | 121.44 | breached by 0.91% | **held by $0.03** (10-27 low 121.47) |

Two defects are visible here, and they are the real story of this artifact:

1. **"Stop hit" conflated two different things.** CELH's stop hit was real — the stock made a new
   low intraday on 10-27 (27.10 < 27.36), so the exhaustion thesis was wrong and the artifact
   should have said *why*, not just "closed 0.05% below the stop". CBRE's stop hit was noise: the
   body was 3.2% of the range, so the body-low stop sat 0.07% away, and the next session's close
   (121.665) was inside the bar's own 1.16% range while the structural invalidation — the signal
   bar's low, 121.44 — **held by three cents**. CBRE then returned +4.86% over three sessions.
   Bonde's own source sanctions the alternative: *"If you prefer to place the stop at the low of
   the shadow instead, make sure that level does not exceed a 2.5% loss from your purchase price."*
   Under the shadow stop CBRE's risk is −1.17%, comfortably inside the cap, and the trade was
   never stopped out.
2. **A body-low stop on a near-doji body is inside the noise.** CBRE 0.07%, CELH 0.48%, HIMS 0.29%
   — all inside the bars' own daily ranges. The stop needs a floor (e.g. 1% of price) and, when
   the body is small, the shadow low is the correct invalidation.

## Structural defect: a 15:55 ET cron on a T+1 feed cannot make a 15:58 ET entry

Bonde's entry is the same session's close, five minutes after the scan. shibui's ingest is T+1, so
at the 15:55 fire the newest available bar is the **previous** session. The routine's own 2026-10-29
artifact says so plainly: *"Bonde's entry window has passed… A name taken today is a Day-2 entry by
Bonde's 'first day of the swing' rule, which his own published process rejects."* Every signal this
cron produces is therefore a **next-session planning artifact, not a same-day entry**, and the
"3:55 PM" name is misleading. The 2026-10-26 manual run, which pulled the live session bar and
re-pulled the settled close at 16:01, was the methodologically correct version for this setup.

## Proposed corrected rule set (validated on three signal bars)

| Gate | Corrected form | Rationale |
|---|---|---|
| F1 | `low <= MIN(low, last 5)` | unchanged (published) |
| F2 | DCR `>= 0.60` | published value (was 0.50) |
| F3 | `(o - l) > (c - o)` **and** lower shadow `>= 2 x` upper shadow **and** body `<= 30%` of range | published expression, plus a scale-free hammer test; the tail:body ratio explodes on doji bodies (CBRE 15×, CELH 17×) and is not a usable gate |
| F4 | body `<= 40%` of range | keep |
| F5 | **decline gate:** (D1) `>= 3%` down over the 3 sessions before the signal bar, **or** (D2) `>= 3%` down over 5 sessions **and** the signal bar's low undercuts the prior close by `>= 1.5%` (an intraday shakeout that got bought back) | Bonde's "drop should last at least 2–3 days" + "there has to be some sort of a wash out" |
| F6 | ADR `>= 3%` | keep (house rule) |
| F7 | price `>= $5` | published value (was $15); "prefer higher priced" becomes a ranking input |
| F8 | `close >= c20d * 0.92` with a **20**-session lag | keep; watch the off-by-one |
| S | stop = body low, but **if body `< 15%` of range use the signal bar's low**, and the stop must be `<= 2.5%` from the entry | a body-low stop on a doji is inside the noise; the shadow low is the structural invalidation Bonde sanctions |

**Validation on real bars (shibui, universe gate + 5-day low + DR ≥ 0.5 + body ≤ 0.4 pre-screen):**

| Signal bar | Skill gates (as run) | Corrected gates | Names passing the corrected set |
|---|---|---|---|
| 2026-10-26 | CELH, HIMS, CBRE | CELH, CPNG | **HIMS and CBRE drop out** (DR 0.514/0.510 < 0.6, and neither is a hammer); CELH is the one clean qualifier |
| 2026-10-27 | CELH, ELF, GEN, PPC, FLUT | SGI, ONON | a completely different list — neither HIMS nor CBRE reaches the shape filter on that bar at all |
| 2026-10-28 | FDXF, G (per the 2026-10-29 artifact) | BGC | the corrected set **rejects both of the routine's own qualified names** (G at DR 0.538 < 0.6; FDXF at a 4.48% shadow-stop risk, over the 2.5% cap) |

That last row is the honest limit: **Bonde's published numbers are a screen, not a checklist.** His
own best examples do not all satisfy them — the 2026-10-29 artifact qualified FDXF at a 12.3× tail
and G at DR 0.538, both outside the published thresholds, because "the final candle can deteriorate
right at the end of the day" and because the selection is explicitly discretionary ("reducing down
your list to just that 1 or 2 ideas", "the reversal bar has to jump off the chart").

So the right shape for this routine is: **publish the mechanical gates, then run the discretionary
step properly** — decline, washout, hammer, "would I have squinted at this bar?" — and let the
discretionary step reject marginal names rather than letting a floor-exact DCR or a stop-distance
tie-breaker promote one.

## Source health (2026-11-01 re-run)

| Source | Endpoint | Status | Result |
|---|---|---|---|
| shibui-finance via MCP-over-HTTP bridge | `mcp.shibui.finance/mcp` → `stock_data_query` | **ok** | 6 queries, 0 failures; authoritative bars for both signal bars |
| Nasdaq public quote/chart API | `api.nasdaq.com/api/quote/{SYM}/chart` | ok | used for the original artifact's bars; ~1¢–2¢ differences vs shibui on some bars, which flipped CELH's tail ratio across the 5× band edge |
| `mcp__shibui_finance__*` / `mcp__tradingview__*` MCP tools | n/a | **not registered** | confirmed via `tool_search` and `mcode-tools connector tools` (133 tools: matrix / email / github only) — unchanged since 2026-10-31's ledger |
| Yahoo JSON | `query1/query2.finance.yahoo.com` | ok (200) | no longer 429 as of 2026-10-31 |
| Finviz screener | `finviz.com/screener.ashx` | **403** | unchanged — egress-IP block, not a browser issue |

## Method

- Primary source for this re-analysis: shibui via `mcp_bridge.py` (JSON-RPC over HTTPS), 6 queries.
- Rule comparison implemented twice — once in SQL against shibui, once in Python over the pulled
  bars — and cross-checked against the Nasdaq bars used in the original artifact.
- Published criteria sourced from `stockbee.blogspot.com/2019/11/how-to-use-reversal-setup-to-make-money.html`
  and `breakoutshappen.com/stock-news/reversal-bullish-setup-the-complete-stockbee-workflow-from-universe-to-exit`
  plus the TraderLion podcast transcript with Pradeep Bonde.
- No trade was executed and no recommendation is made here; this is a rule audit.

_Correction added 2026-11-01 by the Scout session that produced the original 2026-10-27 scan._
