# Bonde Reversal Bullish — 3:55 PM ET scan (2026-11-03)

- **Signal session**: **2026-11-03** — the LIVE US session, read at ~15:55 ET (the candle is ~99% complete; the 16:00 print can still move it).
- **Entry window**: 2026-11-03 3:58–4:00 PM ET (Bonde: "enter between 3.58 to 4PM, or MOC").
- **Universe**: NYSE / NASDAQ / AMEX, type=stock, market cap > $5B, avg volume (10d) > 1M → **893 names** scanned.
- **Passing every Bonde gate**: **2** (candle gates left 55) — **1 promoted as an idea** after Bonde's discretionary review (see below).
- **Source**: `_source=mcp` — TradingView public scanner (live session OHLC) + shibui (settled history) over the MCP-over-HTTP bridge.

## Session alignment — proof this scan is for today

Before computing anything the routine proves which session the scanner is describing:

- TV implied previous close vs shibui's latest settled close: **12/12 agree** (100.0%) → the scanner is on today's live session.
- Verdict: **LIVE**.

## Candidates

| Ticker | Company | Entry (live) | Stop | Stop % | DCR | Body | Lower shdw | Tail | ADR | Drop days | 1-day chg | Mkt cap |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **CRM** | Salesforce, Inc. | **222.10** | 216.55 | 2.50% | 0.842 | 0.033 | 7.44 | 25.20x | 3.40% | 3 | -1.80% | $182.79B |
| **PATH** | UiPath, Inc. | **13.21** | 12.88 | 2.50% | 0.773 | 0.144 | 0.30 | 4.36x ✓ | 3.85% | 3 | -0.97% | $6.88B |

### Stops

- **CRM** — stop **216.55** (2.50% from entry), basis: bar low (body < 15% of range) (tightened to the 2.5% cap). Signal bar O 222.40 H 223.50 L 214.67 C 222.10.
- **PATH** — stop **12.88** (2.50% from entry), basis: bar low (body < 15% of range) (tightened to the 2.5% cap). Signal bar O 13.14 H 13.32 L 12.84 C 13.21.

## Bonde's discretionary review — **1 idea promoted** (of 2 mechanical passers)

Bonde's screen returns candidates; the review reduces them to 1–3 ideas ("no catalyst, no
trade", "the reversal bar has to jump off the chart"). Two names cleared every mechanical gate.
**One is promoted.**

### ✅ IDEA 1 — CRM (Salesforce, Inc.) · entry ≈ $222.10 · stop 216.55 (-2.50%) · Day 1

**Named catalyst (today, dated):** Salesforce announced a definitive agreement to acquire
**Cresta**, an AI voice-agent / customer-service startup, on **Nov 2, 2026** (after the close)
— reported price ≈ **$2.7B**, financial terms not disclosed by the company. It is Salesforce's
**fifth announced acquisition of 2026** (eight signed; five disclosed prices ≈ $15.5B) while
**Informatica is still being integrated**, and the market punished the news: CRM gapped down
in the pre-market and **flushed to $214.80 by 09:40 ET (-5.1% from the prior close)**, its
worst intraday print of the day. Two further dated items sit on top of it: **Veeva Systems'
Citi TMT conference remarks today (Nov 3)** disclosed that of the top-20 pharma CRM
migrations, **12 chose Veeva Vault CRM and only 6 chose Salesforce** (a competitive-share
data point, pharma vertical), and a renewed **shelf registration for 609,118 shares
(~$139.6M)** keeps the dilution question alive. Sector context: the market is punishing
application software for AI disruption (NOW -27% on Oct 28, Twilio -18% Oct 30, DDOG -23%),
and **IGV fell 2.29% on Nov 2**.

**Why the reversal bar qualifies.** The flush was at the **open** and the recovery was
through the rest of the session, not a dead-cat bounce into the close:

| Clock (ET) | CRM |
|---|---|
| 09:30 open | 222.88 (gapped down from 226.18) |
| 09:40 | **214.80 — the day's low** (-5.1%) |
| 13:10 | 223.45 — the day's high |
| 15:55 | 222.04–222.17 (live) |

That is a textbook Bonde reversal: an intraday washout, a close in the **top 16% of the day's
range (DCR 0.842)**, a **7.44 lower shadow vs 1.10 upper shadow**, a **3.3% body** (near-doji,
so the stop is taken at the bar's LOW, not the body low), on a day the rest of software was
bidding (**NOW +2.75%, DDOG +2.47%, TEAM +2.04%, IGV +0.82%, XLK +1.34%**). CRM's weakness was
**idiosyncratic, not sector beta** — and the specific bad news is already public, which is
what a reversal trade needs.

**What makes it the better of the two:** $183B cap and 80.4% institutional ownership (Bonde's
≥1,000-fund universe proxy, comfortably met) vs $6.9B for PATH; 8.3M avg daily volume vs
PATH's 20M on a $6.9B cap; price $222 vs $13 (Bonde's "prefer higher priced stocks" ranking);
BofA's Oct 12 upgrade to Buy (PT $285), a raised FY27 revenue outlook ($46.10–46.40B), and
~14× forward P/E. The Cresta news is **over-reaction to a single-vertical datapoint** — a
$44B-revenue company losing some pharma-CRM share is not a $2.7B thesis-breaker.

**Risks — read before sizing.** (1) **The stop conflicts with the structure.** The bar low is
**214.70**, i.e. **-3.33%** from entry, which breaches Bonde's 2.5% cap, so the stop was
tightened to **216.55** — a level *inside* the bar's own range (214.70–223.50). A print
through 216.55 tomorrow is therefore a **noise breach, not a structural failure**; only a
trade under **214.70** kills the setup. Decide deliberately which risk you are taking: the
tighter stop (≤2.5%, higher false-exit odds) or the true structural stop at 214.70 (-3.33%,
above Bonde's cap). (2) **The flush was low-volume** — ~560k shares in the first three 5-min
bars vs an 8.25M/day average; the day was tracking ≈5.2M (~63% of the 30-session mean of
7.79M), so there was **no capitulation and no conviction**. (3) A fifth acquisition in a year
means the M&A narrative can re-fire on any headline; the $2.7B price was reported, not
disclosed, so the true economics are unknown. (4) The 16:00 print can still move the close,
the DCR and the stop.

### ❌ NOT PROMOTED — PATH (UiPath, Inc.) · entry 13.21 · stop 12.88 (-2.50%) · watchlist only

PATH passes **every mechanical Bonde gate** (DCR 0.773, hammer: 0.305 lower vs 0.110 upper
shadow, 14.4% body, ADR 3.85%, 3-day -4.14%, new 5-day low, mcap $6.9B, avg vol 30.8M). It is
still **not promoted**, on Bonde's own rule: **no catalyst, no trade.**

- **No named catalyst today.** Verified against the day's UiPath news flow: nothing
  company-specific on Nov 3 (the last two headlines are Nov 2 comparison pieces). The stock
  fell with no news of its own — which is the exact condition Bonde's rule rejects, because
  a decline with no visible cause is the one that keeps going.
- **The overhang is structural, not an event.** DA Davidson has an **Underperform, $10 target**
  (Sep 28, cut from $16) — *below* today's price — alongside ~25% of float sold short, ~$43.6M
  of insider selling over 90 days, and a **Hold** consensus with a $15.65 PT.
- **Thin relative to its own history.** ~16M shares at 15:56 vs ~20M in its last five
  sessions and a 28.8M 30-session mean (inflated by the Sept 3 earnings spike: 42–50M).
  A -1.3% day on that volume is drift, not a flush-and-reverse.
- Same stop conflict as CRM: the bar low is **12.835 (-2.84%)**, so the stop had to be
  tightened to 12.88, inside the bar's range.
- **Next scheduled event: Q3 FY2027 earnings, Dec 2, 2026** (consensus EPS $0.17, revenue
  ~$442.7M). That is the date the setup should be re-underwritten against, not today.

### Ideas promoted: **1** (CRM) · Mechanical passers: 2 (CRM, PATH) · Watchlist: 1 (PATH)

> **Stop provenance — read this before sizing.** For both names the bar's structural low is
> *further* than 2.5% from entry (CRM: 214.70 = -3.33%; PATH: 12.835 = -2.84%), so Bonde's
> 2.5% maximum-loss cap could not be honoured at the shadow low and each stop was **tightened
> to the 2.5% level** (CRM 216.55, PATH 12.88). Both stops therefore sit **inside the signal
> bar's own range** — a print through them is a *noise breach*, not a structural failure. The
> structural failure level is the bar low (CRM 214.70 / PATH 12.835). See the discretionary
> review for how to choose between the two.

## Bonde gate matrix

| Ticker | 1. 5-day low | 2. DCR ≥ .60 | 3. shadow > body | 3b. hammer | 3c. body ≤ .30 | 5. decline + washout | 6. ADR ≥ 3% | 7. price ≥ $5 | 8. trend | vol | minv3 | avolv30 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CRM | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| PATH | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

## Filter funnel

| Step | Filter | Left |
|---|---|---|
| 1 | NYSE/NASDAQ/AMEX, type=stock, mcap > $5B, close ≥ $5, avg vol(10d) > 1M | 893 |
| 2 | DCR ≥ 0.60 (close in the top 40% of the day's range) | 55 |
| 3 | + published shadow > body, hammer (lower ≥ 2× upper), body ≤ 0.30, volume ≥ 290k | 55 |
| 4 | + 5-day low, decline+washout, ADR ≥ 3%, trend, minv3, avg vol 30d | 2 |

## Source health

| Source | Used for | Status |
|---|---|---|
| TradingView public scanner | live session OHLC for the universe | ok (893 names) |
| shibui-finance (bridge) | settled history, latest close | ok (latest session ['2026-11-02']) |
| market-recap (bridge) | market state / index backdrop | see caveats |

## Method & caveats

- **The signal is TODAY's live candle, not yesterday's.** The routine proves this at runtime (see the alignment section); it no longer resolves the screen date as "shibui's latest settled date", which was a one-session lag.
- **The candle is read at ~15:55 ET, five minutes before the close.** The 16:00 print can change the close, the DCR and the stop. Treat the entry as the 16:00 close.
- **`v ≥ 290,000` uses a partial day's volume** (as of ~15:55 ET). A name that clears 290k only after the close was wrongly excluded.
- **ADR(20) is computed over the 20 SETTLED sessions before today**, not over a window that includes the incomplete live bar.
- **The market-cap gate uses TradingView's live `market_cap_basic`**, not shibui's `valuation` table, which stores stale rows per symbol and can admit a phantom name if the cap filter is applied before the latest-row pick.
- **"Prefer higher priced stocks" is a ranking preference, not a filter** — the published gate is `c >= 5`; names are ordered by DCR then ADR.
- **Bonde's discretionary step is mandatory**: the mechanical screen returns candidates, then the review reduces them to **1–3 ideas** ("no catalyst, no trade", "the reversal bar has to jump off the chart").
- **Both names were verified against the live tape and the day's news flow** — intraday 5-minute bars (bridge `chart_data`), index/sector backdrop (SPY, QQQ, XLK, IGV and a software peer basket), shibui 30-session volume history, and dated company headlines.

_Generated by cron #4 `reversal-bullish-3:55` · tool `tools/reversal_bullish.py` · session 2026-11-03 · `_source=mcp`_
_Signal session 2026-11-03 (LIVE, alignment 12/12) · history: shibui via MCP-over-HTTP bridge · backdrop + catalysts: bridge `market-recap`/`chart_data`, TradingView, dated public news (Invezz, TradingView/GuruFocus, 247WallSt, MarketBeat, StockAnalysis Veeva transcript) · scheduled date resolved from `scheduled_at_ms` 1793739300000 = 2026-11-03 15:55 ET (not a replay)._
