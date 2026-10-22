# Daily sweep — 2026-10-22 (Thu) · data session 2026-10-21

**Cron #9 `stock-screener-daily-sweep-18:30`** · generated `2026-10-22T11:33:57Z` ·
skill `stock-screener-suite` (fetched from `karizaco/maxhermes-migration`, 336 lines, HTTP 200).

> **Schedule deviation — read this first.** This cron is scheduled for **18:30 ET** but fired at
> **07:32 ET**, 10h58m early, in the pre-market session. The window-check preamble only gates on
> day-of-week, so it passed cleanly (Thursday). The consequence: **the sweep reports the
> 2026-10-21 close, not an 2026-10-22 close.** Nothing here is a live 10/22 reading. Any downstream
> brief that assumes this artifact is an end-of-day 10/22 snapshot is wrong.

---

## 1. Data path — what actually ran

The skill's primary source is `shibui-finance` SQL (DuckDB on a remote host, 9,900 equities,
31M bars, 56 indicators). **That MCP is not bound in this sandbox.** Verified, not assumed:

| Source | Intended | Actual | Result |
|---|---|---|---|
| `mcp__shibui-finance__*` | PRIMARY (all sweeps + breadth) | not registered | **unavailable** — `tool_search` returns 0 hits |
| `mcp__tradingview__screen_stocks` / `screen_etf` | BATCH 2 | not registered | **unavailable** |
| `mcp__tradingview-advanced__*` | volume scanner, pre-market, RVOL | not registered | **unavailable** |
| TradingView public scanner (`scanner.tradingview.com/america/scan`) | fallback 3 | HTTP 200 | **used as primary** — 1 request, 2,928 rows |
| Yahoo Finance `/v8/finance/chart` | fallback 4 | HTTP 200 | **used** — breadth indices + independent verification |
| CBOE `VIX_History.csv` | regime input | HTTP 200 | **used** — authoritative VIX |
| Finviz GET screener | fallback 2 | not attempted | not needed |

Per the skill's fallback chain this is the MCP → TV-public → Yahoo ladder, with **one deviation
worth naming**: the skill's fallback order puts Finviz second, and Finviz is reachable from this
sandbox, but the TradingView scanner is the *same engine* as the skill's primary `screen_stocks`
MCP and returns far richer columns (ATR, SMA20/50/200, Perf.1M/3M/6M/YTD, 52w high, ADX,
Recommend.All, EPS). Going to Finviz would have degraded every screen to Finviz's column set. I
used the richer source and am flagging the ordering rather than hiding it.

**Transport note:** all calls used `curl -k` / unauthenticated HTTPS. The sandbox egress proxy is
a MITM whose per-host leaf certificate has an expired rolling 24h window (leaf `notAfter`
`Oct 21 23:10:54 2026 GMT`). Payloads were genuine — verified by TradingView and Yahoo agreeing on
all 15 spot-checked names — but **the transport was unauthenticated**. Treat the numbers as
single-run observations, not audited figures.

---

## 2. Universe (skill §1 prefilter)

One scanner call, server-side filter, no client-side paging:

```
type = stock · exchange not in [OTC] · close > 3 · market_cap_basic > 300,000,000
     · average_volume_30d_calc > 100,000
```

| | |
|---|---|
| Rows returned | **2,928** (`totalCount` 2,928, 1 page — skill budget allows this in one call) |
| Exchanges | NASDAQ 1,339 · NYSE 1,546 · AMEX 42 · CBOE 1 |
| Null `close` | 0 |
| Null `SMA200` | 115 (no 200-day history — sub-2-year names) |
| `update_mode` | `delayed_streaming_900` |

**Caveat on the CBOE row and on preferreds.** The skill's exchange filter is NYSE/NASDAQ/AMEX; one
row came back on CBOE, so the filter is enforced loosely by the scanner. Separately, `type=stock`
does **not** exclude preferred shares — `STRC` and `QVCG` appear in these lists as if they were
common stock. They trade like debt with capped upside. Screen them by hand before acting.

---

## 3. Session date — verified three independent ways

shibui's T+1 lag is the skill's central data hazard. With no shibui, T+1 was resolved by
corroboration instead:

1. **CBOE official history** ends `10/21/2026`, VIX close **16.68**.
2. **Yahoo daily bars** for SPY/RSP/QQQ/QQQE/IWM all end `2026-10-21`.
3. **Scanner `close` vs Yahoo daily close**, same session: AAPL 343.99/343.99,
   NVDA 221.97/221.97, TSLA 386.47/386.47 — **0.00pp** on all three.

→ Data session is unambiguously **2026-10-21**. Every figure below is a settled close.

---

## 4. Sub-screens — all 10 ran

Matched counts out of 2,928. Full rows and per-name data in the per-stylist files.

| Screen | Stylist | Matched | Rule as implemented |
|---|---|---|---|
| 4% breakout | Bonde / Stockbee | **12** | gain ≥4%, ≥$3, >50-DMA, within 3% of 1M high, volume ≥1.5× 30d avg |
| EP9M | Bonde / Stockbee | **52** | ⚠ proxy — see below |
| Anticipation coil | Bonde / Stockbee | **47** | ATR/close ≤2.5%, within 3% of 20-DMA, volume ≤0.9× avg, SMA20>SMA50 |
| 1M/3M/6M leaders | Kullamägi | **541** | all three windows positive, 6M ≥+10% |
| EP (earnings+price) | Qullamaggie | **268** | 3M ≥+15%, 1M ≥+5%, >50-DMA, earnings catalyst ≤45d |
| Parabolic short | Kullamägi | **1** | 5d ≥+20%, 1M ≥+40%, ≥1.30× 20-DMA, RVOL ≥1.5 |
| Parabolic long | Kullamägi | **10** | 5d ≤−20%, 1M ≤−30%, ≤0.85× 50-DMA |
| ADR + velocity | peoplewish | **66** | ADR ≥4%, 1M ≥+20%, avg30 vol ≥500k |
| CANSLIM compression | Sun / CFTe | **49** | ≥97% of 52w high, YTD ≥+15%, >SMA50>SMA200, rev YoY ≥10%, ATR ≤5%, Recommend.All ≥0.4 |
| Volume breakout | KSE cross-check | **17** | RVOL ≥2, gain ≥3%, >20-DMA |

### Where I substituted, and why

Four screens are **proxies, not the specified metric.** Each is labelled in the file it feeds:

- **EP9M** — the scanner has `earnings_per_share_diluted_ttm` and `..._fq` but **no quarterly EPS
  time series**, so Bonde's trailing-3-month EPS sum cannot be computed. I ranked annualised latest-
  fiscal-quarter EPS as a % of price. Related figures can diverge sharply; treat as a pre-filter.
- **CANSLIM "C"** — no quarterly EPS-growth column exists on this tier. Revenue YoY TTM is used.
- **CANSLIM "L"/RS** — `RS` and `relative_strength_index_14` return **null** on the free tier.
  `Recommend.All` + relative Perf ratios stand in.
- **Sector rotation** — the skill's ETF screener (`screen_etf`) is unavailable, so `ariel-hernandez.md`
  aggregates universe members by `sector`/`industry`. These are **universe means, not cap-weighted
  index returns**.

---

## 5. Breadth & regime

| Measure | Value | n |
|---|---|---|
| % of >$10B names above 20-DMA | **65.82%** | 869 |
| % of >$10B names above 50-DMA | 48.10% | 869 |
| % of >$10B names above 200-DMA | 51.82% | 869 |
| % of full universe above 20-DMA | 55.19% | 2,928 |
| % of full universe above 50-DMA | 38.65% | 2,926 |

The skill specifies a >$10B market-cap proxy for S&P 500 membership (no index table available).

| Index | Close | 50-DMA | ATR% | Extension (ATR) | % from 50-DMA |
|---|---|---|---|---|---|
| SPY | 773.09 | 768.34 | 0.915 | +0.67 | +0.62% |
| RSP | 216.64 | 215.53 | 0.930 | +0.55 | +0.51% |
| QQQ | 725.20 | 726.75 | 1.553 | −0.14 | −0.21% |
| QQQE | 119.37 | 120.67 | 1.331 | −0.82 | −1.08% |
| IWM | 276.48 | 287.49 | 1.403 | **−2.84** | **−3.83%** |

**Regime:** `size_cut_pct` **0** · `uncertainty` **false** · `late_cycle` **false**.
Breadth at 65.8% is well clear of the <40% trigger, no index is below its 20-DMA, and no index is
beyond 6× ATR extension.

**Read:** short-term tape constructive, but the 50-DMA is the line that matters — **IWM sits
3.83% below its 50-DMA while SPY is above its own**. Small caps are the weak leg, and the spread
is the story, not the level.

### Two regime inputs I could not source as specified

- **VIX/VXVCLS is not computable this run.** Yahoo returns no `timestamp` array for `^VXV` and
  **404s** on `^VIXCLS`; CBOE's `VXV_History.csv` redirects to `cdn-api.cboe.com` and returns
  **403 AccessDenied**. `^VXN` (NASDAQ-100 vol) is the substitute denominator:
  **VIX/VXN = 0.748**, no term-structure inversion. The `uncertainty=false` flag is therefore a
  *proxy* result, not the skill's specified test. Per the zero-fallback policy I stopped there
  rather than chaining deeper.
- **Unresolved data conflict:** Yahoo's `^VIX` quote returned **18.27** stamped `2026-10-22
  11:18 UTC`, contradicting CBOE's official 10/21 close of **16.68** — a ~9.5% gap on a pre-market
  timestamp, which is not a real print. **CBOE is authoritative; 16.68 is used.** Flagged, not
  smoothed.

---

## 6. Merged tiers

| Tier | Count | Rule |
|---|---|---|
| Master | **200** | deduped union of all 10 screens, capped at 200 (hit the cap) |
| Stalk | **54** | Master ∩ within 2% of 20-DMA or 50-DMA |
| Focus | **13** | Master ∩ ≥3 stylist flags, or top-5 1M velocity |
| Tier-A | **2** | Master ∩ ≥4 stylist flags |

**Tier-A: `RCEL`** ($15.29, +10.80% on the day, +38.5% 1M, +219.9% 3M — Bonde 4% · KSE volume ·
Kullamägi momentum · Qullamaggie EP) and **`LIFE`** ($44.22, +7.67%, +21.7% 1M — Bonde 4% ·
Kullamägi momentum · peoplewish · Qullamaggie EP).

Master hitting the 200 cap means the tail is truncated by design, not by a data limit.

**Parabolic short: 1 name** (`BRZE`, $45.68, +79.0% 1M, 99.7% of its 52-week high). Thin book by
design — the conjunction is demanding in a low-VIX tape. Note `short_float` came back null for all
2,928 names, so **no borrow, squeeze or short-interest check was possible**. This
is a candidate list, not an entry signal.

**Parabolic long: 10 names** (`GEMI`, `QVCG`, `BRUN`, …) — see `long-reversal-candidates.md`.

---

## 7. Verification

**15/15** spot-checked picks re-derived independently from Yahoo Finance (moving averages, 1M/3M/6M
returns, 52-week position, ATR%) matched the TradingView scanner's daily change to **0.00pp** —
no mismatches, no missing data.

Two bugs were caught by this pass and fixed before publishing, not after:
- A stale hardcoded epoch in the earnings-catalyst calculation silently zeroed the entire
  Qullamaggie EP screen (268 matched → 0). Caught by asking why a 2,428-name catalyst pool produced
  nothing.
- Tier-A was counting the synthetic `up4`/`dn4` daily-move tags toward its ≥4 "stylist flags"
  threshold, inflating Tier-A from 2 to 6 with names showing only 3 real flags. Fixed to count
  stylist screens only.

---

## 8. Not run — skill gating, not failure

| Item | Why |
|---|---|
| 3:55 PM reversal-bullish (Bonde) | Window-gated to weekdays **15:30–16:00 ET**; this fired 07:32 ET. No substitute published — a loose scan wearing the name of the real one would be worse than an absence. |
| Pre-market gapper (SKILL §6) | Scheduled 09:00 ET weekdays; not yet. |
| Live intraday RVOL re-rank (SKILL §7) | 09:45–11:15 ET slots. |
| `ipo.md`, `high-short-float.md` | **Sunday-only** weekly refresh; today is Thursday. |
| Finviz fallback tier | Not reached — no MCP failure forced it. |

---

## 9. Files

| File | Contents |
|---|---|
| `daily-sweep.md` | this file |
| `_summary.md` | digest — regime, Tier-A, short/long, verification |
| `_regime.json` | regime payload + inputs + provenance |
| `breadth.md`, `_breadth_raw.json` | breadth, index extension, volatility |
| `stockbee_4pct.{md,csv}` | Bonde breakout |
| `stockbee_ep9m.{md,csv}` | Bonde earnings power (proxy) |
| `stockbee_coil.{md,csv}` | Bonde anticipation coil |
| `qullamaggie_ep.{md,csv}` | Qullamaggie EP |
| `kullamagi_momentum.{md,csv}` | Kullamägi momentum leaders |
| `peoplewish.{md,csv}` | peoplewish ADR + velocity |
| `jeff-sun.{md,csv}` | Sun CANSLIM compression |
| `volume-breakout.{md,csv}` | KSE cross-check |
| `short-candidates.{md,csv}` | Kullamägi parabolic short |
| `long-reversal-candidates.{md,csv}` | Kullamägi parabolic long |
| `ariel-hernandez.md` | sector / industry relative strength |
| `master.{md,csv}` `stalk.{md,csv}` `focus.{md,csv}` `tier-a.{md,csv}` | merged tiers |

CSVs carry `_source=mcp` per row. **No row in this artifact used a fallback tier** — the fallback
was at the *source* level (TradingView public instead of the shibui MCP), and that is stated in
§1 rather than buried in a row tag.

---

## 10. Open items for the next run

1. **Egress proxy leaf certs still expired** (leaf `notAfter Oct 21 23:10:54 2026 GMT`). Needs the
   proxy to reissue; every cron in this sandbox is degraded until then.
2. **This cron fires ~11h before its schedule.** Worth checking whether the Cloud scheduler is
   dropping the 18:30 slot or firing a catch-up immediately — an EOD sweep that reports the prior
   session is misleading if the filename says today.
3. **VXV has no reachable free source.** If the regime's `uncertainty` flag is meant to be the
   real VIX/VXVCLS test, a data vendor is needed.
4. **`short_float` is null for 2,928 of 2,928 names**, which makes the short-candidate list un-actionable as
   specified.