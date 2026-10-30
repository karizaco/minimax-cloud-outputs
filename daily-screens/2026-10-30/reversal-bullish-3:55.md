# Bonde Reversal Bullish — 3:55 PM ET scan

- **Cron**: #4 `reversal-bullish-3:55` · fired 2026-10-30 15:55 ET
- **Signal bar**: 2026-10-29 close (shibui latest available date — see *Data lag* below)
- **Live reference**: 2026-10-30 session, in-progress at ~15:57 ET (regular close 16:00 ET)
- **Universe**: NYSE / NASDAQ / AMEX, market cap > $5B, 30-day avg volume > 1M
- **Screened**: 5,472 names with a bar on 2026-10-29 → **10 names pass all 8 Bonde filters**
- **Source**: `_source=mcp` (shibui-finance over the MCP-over-HTTP bridge); market caps independently confirmed via the Nasdaq public API

## Data lag — read this before using the list

shibui is a T+1 feed. At 15:55 ET on the cron day, **2026-10-29's close was the newest bar available**; today's (2026-10-30) close is not yet ingested. Every signal in this file is therefore built on the 2026-10-29 bar, and the entry window is **2026-10-30 3:58–4:00 PM ET** (or the next session) — exactly Bonde's stated window, applied one session later than the original playbook.

Because the entry is still ahead of the trader, the live 2026-10-30 session below is used as a **pre-entry validity check**, not as a stop-out test: a name trading below its body-low stop at the close has *failed the setup*, not been stopped out.

Tape on 2026-10-30: **SPY 755.55 (-1.79%)**, **QQQ 690.46 (-3.48%)**, IWM 279.19 (-1.70%). A broad risk-off session — the green setups below are holding against a -3.5% Nasdaq tape.

## How to read the tiers

| Tier | Meaning | Names |
|---|---|---|
| **T1** | Clears every Bonde filter, sits inside the published 3–5x tail band, and has not touched its body-low stop today. Actionable at today's close. | WDAY, DOCU |
| **T2** | Clears every filter and is working, but today's intraday low broke the body-low stop, so the body-low stop is too loose — use Bonde's ≤2% stop instead. | XPO, IOT |
| **T3** | Clears every filter but the setup has failed on today's session. Listed for the record, **not actionable**. | PLTR, RNG, CRM, KNX, LYFT, PCOR |

> Bonde's output discipline is "select 1 to 3 ideas". T1 + T2 = **4 actionable names**, of which
> **WDAY and DOCU** are the two cleanest by every published criterion.

## T1 — actionable now

Entry at the 3:58–4:00 PM ET close on 2026-10-30. Body-low stop is valid and untouched today.

| Ticker | Company | Signal close (10/29) | Live (10/30) | Live chg | Body-low stop | ≤2% stop | DCR | Tail | ADR | Drop days | 2-day chg | Mkt cap (Nasdaq) | 52-wk range |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **DOCU** | DocuSign, Inc. | 81.54 | **82.13** | +0.72% | 81.09 | 80.49 | 0.953 | 3.98x ✓ | 3.55% | 0 | -0.61% | $15.35B | 40.16 - 85.90 |
| **WDAY** | Workday, Inc. Class A | 195.46 | **197.54** | +1.06% | 195.46 | 193.59 | 0.507 | 3.86x ✓ | 3.23% | 3 | -4.87% | $47.59B | 110.36 - 241.32 |

**Setup / catalyst**

- **DOCU** — No company-specific news; pullback inside a +21.7% one-month advance off the 52-week high $85.90 (Oct 26) on software beta. Reversal bar closed at 0.953 of its range (essentially on the high); tail 3.98x body (inside the 3-5x band); ADR 3.55%. Live 82.13 (+0.72%), today's low 81.54 (+0.55% vs the body-low stop).
- **WDAY** — Software-sector unwind (ServiceNow -25%, Fortinet -21% post-Q3 on slowing cRPO; Alphabet -12% on its own print) hit WDAY -4.36%; reversal bar closed off the 5-day low $190.72 and the stock is back green today. 3-day decline into a fresh 5-day low; tail 3.86x body (inside Bonde's 3-5x band); DCR 0.507; ADR 3.23%. Live 197.54 (+1.06%), today's low 196.25 (+0.40% vs the body-low stop).

## T2 — working, but the body-low stop must be replaced

Today's low broke the body-low stop. Enter at the close, then use Bonde's ≤2% stop from the live entry price rather than the body low.

| Ticker | Company | Signal close (10/29) | Live (10/30) | Live chg | Body-low stop | ≤2% stop | DCR | Tail | ADR | Drop days | 2-day chg | Mkt cap (Nasdaq) | 52-wk range |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **IOT** | Samsara Inc. Class A | 41.65 | **42.11** | +1.10% | 41.64 | 41.27 | 0.637 | 99.00x | 4.43% | 3 | -4.27% | $24.65B | 23.38 - 47.47 |
| **XPO** | XPO, Inc. | 183.01 | **190.40** | +4.04% | 183.01 | 186.59 | 0.636 | 6.98x | 3.47% | 1 | -2.61% | $22.28B | 124.82 - 232.05 |

**Setup / catalyst**

- **IOT** — CEO Sanjit Biswas and CTO John Bicket each sold 263,900 shares (~$11.3M apiece) under trading plans on Oct 29; 95 insider sales and zero buys over 12 months ($452.5M); stock -3.16% on the day. 3-day decline into a fresh 5-day low; doji hammer with a 99x tail; ADR 4.43% (most liquid of the ten); DCR 0.637. Live 42.11 (+1.10%), today's low 40.57 (-2.57% vs the body-low stop).
- **XPO** — Q3 2026 reported pre-market Oct 29: adj EPS $1.70 vs $1.57 consensus, adj operating ratio 80.1% (-260bps y/y), FY margin outlook raised to >=250bps; shares still sold off (midday -3.7%) on fuel-surcharge-boosted earnings, printing a capitulation low at $169.11 before closing at 183.01. Earnings-day capitulation-and-reversal, 11.9% daily range; ADR 3.47%; today +4.04% to 190.40. Live 190.40 (+4.04%), today's low 179.61 (-1.86% vs the body-low stop).

## T3 — setup failed on today's session

Listed for completeness. Do not enter these into today's close.

| Ticker | Company | Signal close (10/29) | Live (10/30) | Live chg | Body-low stop | ≤2% stop | DCR | Tail | ADR | Drop days | 2-day chg | Mkt cap (Nasdaq) | 52-wk range |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **RNG** | RingCentral, Inc. Class A | 83.70 | **81.04** | -3.18% | 83.70 | 79.42 | 0.674 | 6.41x | 5.34% | 0 | -2.22% | $6.85B | 24.14 - 98.14 |
| **PLTR** | Palantir Technologies Inc. Class A | 196.42 | **184.07** | -6.29% | 196.42 | 180.39 | 0.744 | 3.11x ✓ | 4.07% | 2 | -1.16% | $441.62B | 106.37 - 212.94 |
| **PCOR** | Procore Technologies, Inc. | 61.12 | **61.24** | +0.20% | 60.92 | 60.02 | 0.672 | 6.70x | 3.59% | 0 | -0.99% | $9.30B | 38.03 - 82.32 |
| **LYFT** | Lyft, Inc. Class A | 16.41 | **16.16** | -1.55% | 16.40 | 15.84 | 0.930 | 59.00x | 3.43% | 2 | -2.26% | $6.11B | 12.46 - 25.54 |
| **CRM** | Salesforce, Inc. | 230.90 | **228.67** | -0.97% | 230.16 | 224.10 | 0.656 | 6.92x | 3.36% | 0 | -4.15% | $188.12B | 146.32 - 269.11 |
| **KNX** | Knight-Swift Transportation Holdings Inc. | 61.15 | **60.63** | -0.85% | 61.15 | 59.42 | 0.614 | 10.62x | 3.19% | 1 | -2.97% | $9.87B | 41.24 - 82.86 |

**Setup / catalyst**

- **RNG** — Q3 2026 on Oct 22 beat (adj EPS $1.33 vs $1.27, FY26 guidance raised) and the stock is +182% over 12 months - this is a parabolic name rolling over, not an exhaustion-at-support reversal. Only a 1-day decline before the signal bar; price is 3.2% below the body-low stop and now below the signal close. Live 81.04 (-3.18%), today's low 80.14 (-4.25% vs the body-low stop).
- **PLTR** — JPMorgan initiated at Overweight with a $262 target on Oct 29 and Oppenheimer raised its target to $235, but the stock is -6.29% today ahead of Q3 FY26 earnings on Nov 2 after the close. Reversal bar failed hard - price is 6.5% below the body-low stop; tail 3.11x body was the cleanest in the set. Live 184.07 (-6.29%), today's low 183.71 (-6.47% vs the body-low stop).
- **PCOR** — No fresh catalyst; the signal bar is a shallow 1% pullback inside an +18.3% 20-day advance - filter 5 is satisfied only technically. Dipped 1.0% below the body-low stop intraday and closed +0.20% at 61.24. Live 61.24 (+0.20%), today's low 60.29 (-1.03% vs the body-low stop).
- **LYFT** — No fresh catalyst; Q3 earnings are due Nov 5. 5-day change -5.85%, YTD -15.28%, and the $16.41 signal close sat only $1.41 above Bonde's $15 floor. Signal bar was a doji hammer (59x tail) at the bottom of a 2-day slide; price is 1.6% below the body-low stop. Live 16.16 (-1.55%), today's low 15.84 (-3.41% vs the body-low stop).
- **CRM** — Caught in the same software unwind (CRM -4.63% Oct 29) and now trading under both its 20-day SMA ($237.59) and 50-day SMA ($238.40), with the 20-day below the 50-day. Only a 1-day decline; 20-day change -2.45% is the weakest long-term trend in the set; price is below the body-low stop. Live 228.67 (-0.97%), today's low 227.71 (-1.06% vs the body-low stop).
- **KNX** — Q3 2026 on Oct 21 was strong (revenue $2.2B +14.2% y/y, adj EPS $0.83 vs $0.32, Q4 guide $0.78-0.84) but the setup itself is broken - 20-day change -6.51% is a genuine downtrend, not exhaustion at support. Price is 0.9% below the body-low stop; 2-day change -2.97%. Live 60.63 (-0.85%), today's low 60.13 (-1.67% vs the body-low stop).

## Full metrics — all 10 names

| Ticker | Tier | Open | High | Low | Close | DCR | Body | Tail | In 3–5x band | ADR | 5-day low | Drop days | 2-day chg | 20-day chg | Mkt cap shibui | Mkt cap Nasdaq |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DOCU | T1 | 81.09 | 81.65 | 79.30 | 81.54 | 0.953 | 0.192 | 3.98x | yes | 3.55% | 79.30 | 0 | -0.61% | +16.92% | $15.57B | $15.35B |
| WDAY | T1 | 196.69 | 200.08 | 190.72 | 195.46 | 0.507 | 0.131 | 3.86x | yes | 3.23% | 190.72 | 3 | -4.87% | +4.66% | $48.28B | $47.59B |
| IOT | T2 | 41.64 | 42.22 | 40.65 | 41.65 | 0.637 | 0.006 | 99.00x | no | 4.43% | 40.65 | 3 | -4.27% | +4.02% | $24.27B | $24.65B |
| XPO | T2 | 185.00 | 190.98 | 169.11 | 183.01 | 0.636 | 0.091 | 6.98x | no | 3.47% | 169.11 | 1 | -2.61% | +1.82% | $21.49B | $22.28B |
| RNG | T3 | 84.02 | 84.69 | 81.65 | 83.70 | 0.674 | 0.105 | 6.41x | no | 5.34% | 81.65 | 0 | -2.22% | +6.88% | $6.99B | $6.85B |
| PLTR | T3 | 198.37 | 198.51 | 190.36 | 196.42 | 0.744 | 0.239 | 3.11x | yes | 4.07% | 190.36 | 2 | -1.16% | +3.36% | $470.88B | $441.62B |
| PCOR | T3 | 60.92 | 61.87 | 59.58 | 61.12 | 0.672 | 0.087 | 6.70x | no | 3.59% | 59.58 | 0 | -0.99% | +18.31% | $9.22B | $9.30B |
| LYFT | T3 | 16.40 | 16.45 | 15.81 | 16.41 | 0.930 | 0.015 | 59.00x | no | 3.43% | 15.81 | 2 | -2.26% | +7.89% | $6.23B | $6.11B |
| CRM | T3 | 230.16 | 233.97 | 225.04 | 230.90 | 0.656 | 0.083 | 6.92x | no | 3.36% | 225.04 | 0 | -4.15% | -2.45% | $189.11B | $188.12B |
| KNX | T3 | 61.31 | 62.22 | 59.45 | 61.15 | 0.614 | 0.058 | 10.62x | no | 3.19% | 59.45 | 1 | -2.97% | -6.51% | $9.95B | $9.87B |

## Bonde criteria matrix

| Ticker | 1. 5-day low | 2. Close top half | 3. Tail ≥3x body | 4. Small body | 5. 2-day decline | 6. ADR ≥3% | 7. Close ≥$15 | 8. Trend (≥92% of 20d) |
|---|---|---|---|---|---|---|---|---|
| DOCU | ✓ (79.30 vs low5 79.30) | ✓ (0.953) | ✓ (3.98x) | ✓ (0.192) | ✓ (-0.61%) | ✓ (3.55%) | ✓ (81.54) | ✓ (+16.92%) |
| WDAY | ✓ (190.72 vs low5 190.72) | ✓ (0.507) | ✓ (3.86x) | ✓ (0.131) | ✓ (-4.87%) | ✓ (3.23%) | ✓ (195.46) | ✓ (+4.66%) |
| IOT | ✓ (40.65 vs low5 40.65) | ✓ (0.637) | ✓ (99.00x, over the 5x cap) | ✓ (0.006) | ✓ (-4.27%) | ✓ (4.43%) | ✓ (41.65) | ✓ (+4.02%) |
| XPO | ✓ (169.11 vs low5 169.11) | ✓ (0.636) | ✓ (6.98x, over the 5x cap) | ✓ (0.091) | ✓ (-2.61%) | ✓ (3.47%) | ✓ (183.01) | ✓ (+1.82%) |
| RNG | ✓ (81.65 vs low5 81.65) | ✓ (0.674) | ✓ (6.41x, over the 5x cap) | ✓ (0.105) | ✓ (-2.22%) | ✓ (5.34%) | ✓ (83.70) | ✓ (+6.88%) |
| PLTR | ✓ (190.36 vs low5 190.36) | ✓ (0.744) | ✓ (3.11x) | ✓ (0.239) | ✓ (-1.16%) | ✓ (4.07%) | ✓ (196.42) | ✓ (+3.36%) |
| PCOR | ✓ (59.58 vs low5 59.58) | ✓ (0.672) | ✓ (6.70x, over the 5x cap) | ✓ (0.087) | ✓ (-0.99%) | ✓ (3.59%) | ✓ (61.12) | ✓ (+18.31%) |
| LYFT | ✓ (15.81 vs low5 15.81) | ✓ (0.930) | ✓ (59.00x, over the 5x cap) | ✓ (0.015) | ✓ (-2.26%) | ✓ (3.43%) | ✓ (16.41) | ✓ (+7.89%) |
| CRM | ✓ (225.04 vs low5 225.04) | ✓ (0.656) | ✓ (6.92x, over the 5x cap) | ✓ (0.083) | ✓ (-4.15%) | ✓ (3.36%) | ✓ (230.90) | ✓ (-2.45%) |
| KNX | ✓ (59.45 vs low5 59.45) | ✓ (0.614) | ✓ (10.62x, over the 5x cap) | ✓ (0.058) | ✓ (-2.97%) | ✓ (3.19%) | ✓ (61.15) | ✓ (-6.51%) |

## Filter funnel

| Step | Filter | Names left |
|---|---|---|
| 1 | NYSE/NASDAQ/AMEX with a bar on 2026-10-29 and full 20-day history | 5472 |
| 2 | market_cap > $5B (institutional-funds proxy) | 1352 |
| 3 | avg_volume_30d > 1M (liquid institutional set) | 1004 |
| 4 | close ≥ $15 (Bonde: prefer higher-priced) | 924 |
| 5 | low ≤ 5-day low | 135 |
| 6 | DCR ≥ 0.5 (close in top half of range) | 79 |
| 7 | tail ≥ 3x body | 21 |
| 8 | body ≤ 0.4 of range (small body) | 21 |
| 9 | close < close_2d_ago (2–3 day decline) | 18 |
| 10 | ADR(20d) ≥ 3% | 12 |
| 11 | close ≥ 92% of close_20d_ago (long-term trend) | 10 |
| 12 | tail ≤ 5x (the literal "3 to 5 times" band) | 3 |

Step 12 is not a Bonde filter — the published SQL form is `tail >= 3 * body` with no upper cap. It is shown because the prose says "3 to 5 times", and only PLTR, DOCU and WDAY land inside that band. The other seven pass the SQL form as written but carry a longer tail than the prose describes.

## Stop construction — read before sizing

Bonde's stop is the **low of the signal candle's body** (`min(open, close)`). For a down-close signal bar that reversed up off the low, the body low *is* the close — so the stop lands exactly on the entry and is worthless. That affects 7 of the 10 names here (RNG, XPO, WDAY, PLTR, KNX and the near-cases IOT, LYFT all have a body low within 0.6% of the close).

| Ticker | Signal open | Signal close | Body low | Body-low distance from signal close | Live px | Live low vs body low |
|---|---|---|---|---|---|---|
| DOCU | 81.09 | 81.54 | 81.09 | -0.55% | 82.13 | +0.55% |
| WDAY | 196.69 | 195.46 | 195.46 | +0.00% | 197.54 | +0.40% |
| IOT | 41.64 | 41.65 | 41.64 | -0.02% | 42.11 | -2.57% |
| XPO | 185.00 | 183.01 | 183.01 | +0.00% | 190.40 | -1.86% |
| RNG | 84.02 | 83.70 | 83.70 | +0.00% | 81.04 | -4.25% |
| PLTR | 198.37 | 196.42 | 196.42 | +0.00% | 184.07 | -6.47% |
| PCOR | 60.92 | 61.12 | 60.92 | -0.33% | 61.24 | -1.03% |
| LYFT | 16.40 | 16.41 | 16.40 | -0.06% | 16.16 | -3.41% |
| CRM | 230.16 | 230.90 | 230.16 | -0.32% | 228.67 | -1.06% |
| KNX | 61.31 | 61.15 | 61.15 | +0.00% | 60.63 | -1.67% |

Where the body-low distance is below ~0.6% the level is degenerate. Bonde's own rule — "put stop of less than 2%" — is the fallback, and the `≤2% stop` column in the tier tables is that number computed off the live entry price. Note that a body low also has to survive the entry session: today's low is below the body-low stop for IOT (-2.57%), PCOR (-1.03%) and XPO (-1.86%).

## Day tag

Every one of the ten signal bars made its 5-day low **on the signal bar itself** (`low = min(low, last 5)`), so all ten are Day-1 setups — none is a stale Day-2/Day-3 signal that has already missed the entry window. Bonde's "exit on the third day if it does not work" therefore applies from the next session onward.

## Source health

| Source | Used for | Endpoint / query | Status |
|---|---|---|---|
| shibui-finance (MCP-over-HTTP bridge) | signal bars, ADR, 5-day low, valuation | `mcp.shibui.finance/mcp` → `stock_data_query`, `SELECT MAX(date) ... WHERE date <= '2026-10-30'` → 2026-10-29 | ok (2 calls + 1 funnel call, 0 errors) |
| shibui `valuation` | market cap | latest row per symbol via `QUALIFY ROW_NUMBER() OVER (PARTITION BY symbol ORDER BY date DESC) = 1` | ok — **latest row picked before the cap filter** so stale rows cannot admit phantom names |
| Nasdaq public API | independent market cap, 52-week range, session day range | `api.nasdaq.com/api/quote/{SYM}/summary` and `/info` | ok for market cap + `keyStats.dayrange`; the top-level `lastSalePrice`/`percentageChange` fields returned **null** on `/info`, so live prices came from the stocktwits bridge and were cross-checked against Nasdaq's `dayrange` |
| stocktwits (MCP-over-HTTP bridge) | live 2026-10-30 session bars, index levels | `chart_data {period:"1M"}` — last bar is the in-progress session | ok (10 candidates + SPY/QQQ/IWM) |
| `web_search` | catalysts, analyst actions, earnings dates | per-ticker news queries | ok |
| Yahoo Finance JSON API | — | not used | **not reachable — HTTP 429 persistent** (documented pre-existing rate limit) |

## Method & caveats

- **T+1 lag is the headline caveat.** The scan is built on 2026-10-29's close, one session before the entry window opens. The signal is valid for 2026-10-30 3:58–4:00 PM ET entry, not for 2026-10-29.
- **Market cap is a proxy, not a fact.** shibui has no `institutional_holders_count`, so Bonde's "stocks owned by ≥1,000 institutional funds" universe is approximated by market cap > $5B plus avg_volume_30d > 1M. Every one of the ten was then confirmed against the Nasdaq market cap; all ten cleared $5B by a wide margin, so the proxy did not decide the outcome.
- **Market-cap figures differ by up to ~7%** between shibui and Nasdaq (PLTR $470.9B vs $441.6B) because the two snapshots use different share counts. The gap is far too small to change any filter result.
- **The "3 to 5x tail" criterion was applied as the published SQL form** (`tail >= 3 * body`, no upper cap). The stricter prose band would cut the list from 10 names to 3 (PLTR, DOCU, WDAY) — and PLTR has already failed, leaving DOCU and WDAY.
- **Filter 5 (a 2–3 day decline) is satisfied technically by several names.** The SQL tests `close < close_2d_ago`, which a single down day passes. Only WDAY (3), IOT (3), PLTR (2) and LYFT (2) had a genuine multi-session decline into the signal bar.
- **Live prices are an in-progress session**, captured ~15:57 ET with five minutes to the close; the final 16:00 ET print can move them.
- **Event risk:** PLTR reports Q3 FY26 after the close on 2026-11-02; LYFT on 2026-11-05.

_Generated by cron #4 `reversal-bullish-3:55` on 2026-10-30 15:55 ET · skill: stock-screener-suite step 5 · screen date 2026-10-29 · `_source=mcp`_
