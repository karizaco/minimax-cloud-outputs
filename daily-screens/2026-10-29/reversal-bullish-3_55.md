---
cron: "#4 reversal-bullish-3:55"
run_date_et: "2026-10-29"
run_time_et: "15:55"
signal_bar_date: "2026-10-28"
skill: "stock-screener-suite §5 — Pradeep Bonde / Stockbee 3:55 PM Reversal Bullish"
universe: "NYSE / NASDAQ / AMEX, market_cap > $5B (institutional proxy), avg_vol_30d > 1M"
candidates_passed: 5
candidates_qualified: 2
_source: "mcp+nasdaq"
shibui_lag: "T+1 (shibui latest bar = 2026-10-28; cron day = 2026-10-29)"
---

# Reversal Bullish — 3:55 PM ET — 2026-10-29

Two names clear every published Pradeep Bonde criterion: **FDXF** (FedEx Freight Holding Co.) and **G** (Genpact Limited). Both printed a lower-shadow reversal bar on the 2026-10-28 session and held it on 2026-10-29. Three more passed the mechanical screen and were rejected on Bonde's own rules — VLO and VIRT already broke their body-low stops on the following session, and JAN worked but carried a 4.07% stop distance, well past Bonde's 2.5% maximum-loss rule.

> **Read this first — two things change how the list should be used.**
>
> **1. The signal bar is 2026-10-28, not today.** shibui's end-of-day ingest is T+1, so at the 15:55 fire time the newest available bar was 2026-10-28's close. Per the skill spec the scan was run against that bar and the lag is disclosed here rather than papered over. The practical consequence: **Bonde's entry window (3:58–4:00 PM on the signal day, or a Market-On-Close order) has already passed.** The actionable entry for a name is the next session's open, not today's close.
>
> **2. The 2026-10-29 session already resolved, and it split the list in two.** Every quote below was pulled live from Nasdaq at 15:59 ET on the cron day, so this report shows how each setup behaved on the session immediately after the signal bar — not a forecast. VLO and VIRT broke their body-low stops on that session; FDXF and G held. FDXF also reports earnings *after* today's close, so its setup carries a binary event between signal and entry (see the entry rules below).

## Qualified ideas

### 1. FDXF — FedEx Freight Holding Company, Inc. (NYSE)

**Signal bar 2026-10-28:** open 108.89, high 108.89, low 103.475, close 108.33, volume 1,781,937.
**Entry reference (10-29 close):** $109.39 (+0.98%), day range $106.37–$110.60 — closed at the high of the range after holding the signal-bar low.
**Stop (Bonde body low):** $108.33 → **0.97% risk**. Signal-bar low $103.475 was also a fresh 52-week low.
**Setup:** a 5.0% range capitulation bar that closed back at its open with a 4.9% lower shadow — close-location 0.897, body 0.103 of range, tail 8.67× body, ADR(20d) 3.56%. Reclaiming $103.475, the lowest print since the June spin-off, is textbook exhaustion-at-support.
**Context:** spun off from FedEx on 2026-06-01, still ~46% below its $200 52-week high and well under its $120.26 50-DMA; the post-spin slide has been driven by a wave of analyst target cuts (Stifel $129, Truist $115, BMO $130, JPMorgan $149, Evercore $135) and heavy $105-strike put hedging into the print. Market cap $16.3B, 30-day average volume 1.47M.
**Catalyst:** **first standalone earnings release after today's close** (four-month transition period ended 2026-09-30); consensus EPS $1.38–$1.43 on ~$9.08B FY26 revenue, Zacks Rank #2, Earnings ESP +5.07%, consensus rating Moderate Buy (avg target $158.85). Management guided the June–Dec transition period to ~$605–645M adjusted operating income and ~11.8% adjusted operating margin, with ~60% of period revenue growth and ~75% of adjusted EPS expected to land in the four months to September.
**Entry rule:** do not take this blind into the print. It is actionable only if the post-earnings open holds **above $108.33** — the body low. Below that, the reversal is invalidated and the setup is dead regardless of how the earnings read. If the print is good and the stock gaps above $110.60, it is no longer an entry at this level.

### 2. G — Genpact Limited (NYSE)

**Signal bar 2026-10-28:** open 38.93, high 39.26, low 38.35, close 38.84, volume 2,112,639.
**Entry reference (10-29 close):** $38.91 (+0.18%), day range $38.57–$39.23 — held the signal low and closed in the upper half of the range.
**Stop (Bonde body low):** $38.84 → **0.18% risk**. Signal-bar low $38.35 is the wider structural invalidation.
**Setup:** the cleanest criteria match of the day. A four-session slide (41.78 → 40.83 → 40.48 → 39.20 → 38.84, −4.05% over two days, −4.87% over three) into a fresh 5-day low, with a 0.49 lower shadow against a 0.09 body — tail 5.44× body, close-location 0.538, body 0.099 of range, ADR(20d) 3.33%. Critically, the long-term trend is intact (+19.4% over 20 sessions), which is what Bonde's filter 8 is there to separate exhaustion from a falling knife.
**Context:** market cap $6.50B, 96% institutional ownership, 30-day average volume 1.80M. The pullback is sector-driven — IT-services pricing pressure after Infosys trimmed FY27 growth guidance, plus caution ahead of Cognizant's 10-29 print. Company-specific flow has been positive: NelsonHall Leader (10-28), Everest Group Growth Honor (10-19), Agentic AR Suite launch (10-14), $0.1875 quarterly dividend (10-15). Analyst consensus Hold, average target $39.67 — essentially the current price, so the name is not priced for the earnings re-rating.
**Catalyst:** Q3 results 2026-11-05 after the close; consensus ~$1.38B revenue and ~$1.04 EPS against Q2's $1.343B (+7.1%) and Advanced Technology Solutions +24.1%. Also on deck: a special shareholder vote on the Bermuda-to-Delaware redomiciliation on 2026-11-10.
**Entry rule:** the 0.18% body-low stop is effectively at the entry, so treat $38.84 as a *close-below* invalidation rather than a resting order, and use $38.35 (the signal-bar low) as the hard risk line. The stock is still +19% over 20 sessions, so this is a pullback in an uptrend, not a base — size accordingly.

## Full screen result (5 of 5 mechanical passers)

| Ticker | Signal close | Entry ref (10-29) | Body-low stop | Stop risk | DCR | Body | Tail:body | ADR 20d | 2-day | 20-day | 10-29 | Held signal low | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FDXF | 108.33 | 109.39 | 108.33 | 0.97% | 0.897 | 0.103 | 8.67× | 3.56% | −1.02% | −0.96% | +0.98% | yes | **QUALIFIED** |
| G | 38.84 | 38.91 | 38.84 | 0.18% | 0.538 | 0.099 | 5.44× | 3.33% | −4.05% | +19.40% | +0.18% | yes | **QUALIFIED** |
| VIRT | 55.44 | 54.16 | 55.27 | −2.05% | 0.877 | 0.131 | 5.71× | 3.87% | −0.82% | +0.51% | −2.31% | no | FAILED — stop hit |
| VLO | 388.48 | 384.52 | 388.48 | −1.03% | 0.550 | 0.132 | 4.18× | 4.25% | −8.97% | +0.22% | −1.02% | no | FAILED — stop hit |
| JAN | 27.37 | 28.53 | 27.37 | 4.07% | 0.700 | 0.100 | 7.00× | 3.23% | −4.33% | −7.63% | +4.24% | yes | REJECTED — risk rules |

All five are **Day 1** setups: the 5-day low was made on the signal bar itself in every case, so none is a stale Day-2/Day-3+ signal.

## Rejected names and why

**VLO — Valero Energy.** Mechanically the best-looking bar of the group (tail 4.18× body, ADR 4.25%, in-band) and still wrong. The decline was a **single** −9.24% gap-down session on 2026-10-27 (426.76 → 387.34, worst day since April 2025) triggered by a refining-margin repricing — crude slipped under $100 on Middle East diplomacy hopes, diesel and RBOB futures fell faster than crude, and Russian diesel supply under a sanctions waiver plus a president's promise of cheaper gasoline hit the crack spread. Bonde's criterion 5 wants the drop to last **2–3 days**; this was one day with a 2% bounce on 10-26 inside it. On 10-29 VLO printed a new low of $377.47, below the signal bar's $380.74 low — the stop was hit and the "reversal" is a continuation. The stock is still +141% YTD after record Q3 results (EPS $23.90 vs $20.30 consensus, $39.24/bbl margin), so this is a parabolic name unwinding, not exhaustion at support.

**VIRT — Virtu Financial.** The screen's weakest structural pass. Its "decline" was one down session ($55.90 → $54.99) followed by a bounce, so criterion 5 is satisfied only technically — the two-day change is just −0.82% and the three-day −0.88%, versus the 2–3 day decline Bonde describes. On 10-29 it closed at $54.16, **below** the body-low stop of $55.27, and broke the signal-bar low of $54.30 as well. Stop hit, setup void.

**JAN — Janus Living.** The one name that actually worked on the follow-through session (+4.24% to $28.53, closing at the day high), and still rejected — on Bonde's own rules. The body-low stop of $27.37 sits **4.07%** below the entry, more than double the 2.5% maximum loss Bonde allows, so a correctly-sized position could not be carried. Filter 8 (long-term trend) also passed only marginally: the 20-day change is −7.63%, i.e. JAN is in a downtrend that the −8% tolerance barely accommodates — the exact rejection pattern the skill flags for XPEV/TFII/ERIC. Tail 7.00× body is outside the published 3–5× band. No company-specific catalyst was identified; the bid looks sector-driven.

## Method

Bonde's eight published criteria plus the universe gate were applied as hard filters in a single shibui SQL pass, in this order:

| # | Criterion | Implementation | Threshold |
|---|---|---|---|
| 1 | Making a 5-day low | `low <= MIN(low) over prior 5 sessions` | hard |
| 2 | Close in top half of range | `(close − low) / (high − low)` | ≥ 0.50 |
| 3 | Tail 3–5× the body | `(LEAST(open,close) − low) / ABS(close − open)` | ≥ 3.0 |
| 4 | Small body | `ABS(close − open) / (high − low)` | ≤ 0.40 |
| 5 | Prior decline of 2–3 days | `close < close_2d_ago` | hard |
| 6 | ADR ≥ 3% | `AVG((high − low) / close, 20 rows)` | ≥ 3.0% |
| 7 | Close ≥ $15 | `close` | ≥ 15.00 |
| 8 | Long-term trend intact | `close >= close_20d_ago × 0.92` | hard |
| U | Universe | NYSE/NASDAQ/AMEX, `market_cap > $5B`, `avg_vol_30d > 1M` | hard |

**Funnel:** 10,380 NYSE/NASDAQ/AMEX bars on the signal date → 60 names passing the day-shape filters (criteria 2, 3, 4, 7 and the universe gate) → 5 passing all eight criteria and the universe gate → 2 qualified after the discretionary review (Bonde: "select 1 to 3 ideas — do not pad with marginal setups").

Two details that change the numbers and are worth stating explicitly:

- **Market cap is read latest-row-first.** `shibui.valuation` keeps stale rows per symbol, so a naive `date <= X AND market_cap > 5B` admits old rows whose cap no longer qualifies. The cap filter is applied after picking each symbol's most recent valuation row via `QUALIFY ROW_NUMBER() ... ORDER BY date DESC = 1`. Every surviving cap was then re-verified against an independent source (Nasdaq) — all five clear $5B on both (G: $6.50B Nasdaq / $6.58B shibui; FDXF $16.31B / $16.13B; VLO $110.60B / $115.35B; VIRT $8.41B / $8.60B; JAN $8.82B / $7.89B). No phantom names in the result.
- **T+1-safe SQL shape.** The inner CTE is windowed over `date BETWEEN '2026-09-20' AND '2026-10-28'` and the outer query selects `rn = 1`, so `LAG(close, 2)` and the 5-day/20-day windows all see a full history. The naive form — filtering `WHERE date = '<today>'` before the LAG window — leaves one row per symbol, returns NULL for `close_2d_ago`, and drops the entire result set.

## Caveats

- **The signal bar is T+1.** Everything on the screen is 2026-10-28's close. Today (10-29) never entered the SQL; it was used only to check what happened after the signal.
- **Bonde's entry window has passed.** With the signal bar on 10-28, the 3:58–4:00 PM / MOC entry was 2026-10-28's close. A name taken today is a Day-2 entry by Bonde's "first day of the swing" rule, which his own published process rejects. The stops above are therefore reference levels for a next-session entry, not instructions to buy at today's close.
- **The market was soft into the close.** SPY 769.27 (−0.39%), QQQ 714.90 (−1.48%) at 15:59 ET on 10-29, with the Fed holding rates on 10-28. G's sector (IT services) and FDXF's freight peers both had sector-level headwinds into the close.
- **FDXF carries a binary event tonight.** Its earnings release lands after the 10-29 close. An overnight gap can exceed the 0.97% stop distance by a wide margin — the stop only works on a tradable open.
- **G's stop is effectively at the entry.** A 0.18% body-low stop is noise-level; treat it as a close-below-$38.84 invalidation with $38.35 as the hard line, and do not read the tight number as low risk.
- **`market_cap > $5B` is a proxy**, not a count of institutional holders — shibui exposes no `institutional_holders_count`. G's 96% institutional ownership is sourced separately, not from the screen.
- Prices and prints are Nasdaq real-time quotes at 15:59 ET; the 10-29 figures are late-session values, not official closing prints.

## Source health

| Source | Endpoint / query | Status | Result |
|---|---|---|---|
| shibui-finance MCP (via `mcp_bridge.py`, JSON-RPC over HTTPS) | `stock_data_query` — 6 calls: `MAX(date)` resolve, recent-distinct-dates, 3× DESCRIBE, signal-day shape screen, Bonde-strict screen, 6-session history pull | ok | 5 qualifying rows, all closes independently confirmed |
| Nasdaq quote API | `GET api.nasdaq.com/api/quote/{SYM}/info?assetclass=stocks` — VLO, G, VIRT, JAN, FDXF | ok | 2026-10-29 live prints, day ranges, volumes, 52-week ranges |
| Nasdaq quote API | `GET api.nasdaq.com/api/quote/{SYM}/summary?assetclass=stocks` — VLO, G, VIRT, JAN, FDXF | ok | independent market caps used to check the $5B proxy |
| Nasdaq quote API | `GET api.nasdaq.com/api/quote/SPY/info?assetclass=etf`, `.../QQQ/info?assetclass=etf` | ok | market context (SPY needs `assetclass=etf`, not `stocks`) |
| Nasdaq quote API | `GET api.nasdaq.com/api/quote/VIX/info?assetclass=index` | **failed:400** — symbol not exists | Non-essential; no VIX field in this scan's output |
| web_search | 3 queries — Genpact October 2026 news, FedEx Freight FDXF news, Valero 10-27 decline | ok | catalyst and rejection-reason sourcing |
| Yahoo Finance JSON (chart/screener) | not called | skipped by design — RUNTIME-CONTRACT records a persistent 429 | Nasdaq ladder served every quote instead |
| `mcp__yahoo_finance__*` / `mcp__tradingview__*` / `mcp__shibui_finance__*` | not callable in this runtime | n/a | shibui reached over the MCP-over-HTTP bridge instead |

## Files

- `daily-screens/2026-10-29/reversal-bullish-3:55.md` — this report
- `daily-screens/2026-10-29/reversal-bullish-3:55.csv` — 5 rows, one per mechanical passer, with every criterion metric, the live 10-29 quote, the body-low stop, the verdict and `_source`
