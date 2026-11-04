# Pre-market Gapper — 2026-11-04

- **Routine:** cron #08 `stock-screener-pre-market-gapper` | Fire: 2026-11-04 08:30 ET (08:31:14 dispatched)
- **Universe:** the 12 names in the prior sweep's Focus list (`daily-screens/2026-11-03/focus.csv`, produced by cron #09 on 2026-11-03; screen data date 2026-11-02, session close 2026-11-03)
- **Trigger (SKILL.md §6):** gap > 4% AND pre-market volume > 50,000
- **Snapshot:** live pre-market reads pulled 08:37–08:51 ET (three snapshots; final prices at 08:39–08:51 ET)
- **Result: 0 of 12 names flagged.** No Focus name gapped more than 4% on volume above the 50,000 floor.
- `_source=nasdaq_premarket_tape+info | tv_scanner_crosscheck | cboe_close_confirm`
- `derived_from_data: true`

## Headline

**Nothing on the Focus list qualifies as a pre-market gapper this morning.** The widest live gap is
**MRNA +3.30%** on **243,400** pre-market shares — the only name that is both near the trigger and
carrying real volume — and it is still **0.70pp short** of the 4% line. The widest number that
appears on *any* source for *any* name is **CLF +3.82%** (its pre-market high of $14.68 against a
$14.14 close), a **0.18pp** margin, so the "no flags" verdict does not depend on which cached
vintage a source happens to serve.

**The caveat that matters more than the gaps: pre-market volume is negligible on every name.** The
largest pre-market turnover in the list is TEM at 127,119 shares, which is **1.84%** of its 30-day
average volume; MRNA's 243,400 is 1.38%, CVNA's 52,347 is 0.54%, and nine of the twelve names are
under 0.6%. On this much volume a gap is a quote, not a market — the widest spreads here ran to
±2.3% (KOD bid $98.30 / ask $103.00). Treat every gap in this file as an opening-auction
*indication*, not a tradeable pre-market print.

## Pre-market table

| Ticker | Close 11-03 | PM price | Gap % | PM volume | % of 30d avg | Widest gap on any source | Flag |
|---|---:|---:|---:|---:|---:|---:|---|
| MRNA | 228.44 | 235.97 | **+3.30%** | **243,400** | 1.38% | +3.52% | no |
| FIGS | 20.82 | 21.59 | +3.70% | 6,025 | 0.15% | +3.70% | no |
| WING | 161.57 | 165.56 | +2.47% | 1,181 | 0.08% | +2.74% | no |
| CLF | 14.14 | 14.44 | +2.12% | 46,492 | 0.20% | +3.82% | no |
| CAI | 32.85 | 33.54 | +2.10% | 20,462 | 0.56% | +3.35% | no |
| KVYO | 21.33 | 21.771 | +2.07% | 2,781 | 0.05% | +2.23% | no |
| TEM | 77.80 | 79.30 | +1.93% | 127,119 | 1.84% | +2.63% | no |
| CVNA | 71.28 | 72.018 | +1.04% | 52,347 | 0.54% | +2.55% | no |
| HTFL | 54.40 | 54.87 | +0.86% | 5,942 | 0.36% | +1.86% | no |
| VSEC | 162.96 | 163.01 | +0.03% | 32 | 0.01% | +0.81% | no |
| FTAI | 200.74 | 198.00 | −1.37% | 4,324 | 0.24% | −2.41% | no |
| KOD | 98.89 | 96.11 | −2.81% | 1,356 | 0.05% | −2.81% | no |

Denominator = each name's settled 2026-11-03 close from the prior sweep's own `focus.csv`
(independently confirmed by the Cboe `close` field and the TradingView scanner `close` — all 12 agree
to the cent). "Widest gap on any source" = the largest absolute gap implied by any of the four
readings available per name (live `/info` print, tape consolidated print, tape last executed print,
and the tape's pre-market high/low).

## The three names worth watching

- **MRNA — +3.30% on 243,400 shares.** The only name combining a near-trigger gap with meaningful
  volume. Pre-market range $229.26–$236.47. It never touched +4% at any point in the session so far.
- **TEM — +1.93% on 127,119 shares.** Highest volume-to-normal ratio in the list (1.84%), but the gap
  is a third of the trigger.
- **CVNA — +1.04% on 52,347 shares.** Volume-qualified, gap nowhere near the line.

Two names look interesting on the live price and are not: **FIGS +3.70%** rests on 6,025 shares
(0.15% of normal) with a stale tape vintage reading −0.34% for the same name, and **KOD −2.81%**
moved from +1.12% at 08:35 to −2.81% at 08:51 on 1,356 shares with a $4.70 bid/ask spread — a quote,
not a market.

## Method & caveats

- **The stale-cache defence was necessary and it fired.** `api.nasdaq.com`'s `extended-trading`
  endpoint is served through a shared HTTP cache that returns hours-old snapshots for the same URL;
  every pull carried a `cache-hit` header (`3001`/`3002`). Each tape was therefore pulled **4 times**
  per symbol and the payload with the **newest internal trade-detail timestamp** was kept — TEM
  alone showed two vintages in the same run (`08:17:08` and `08:18:04`). Three snapshots were taken
  across the run (≈08:37, 08:40, 08:51 ET) as the liveness proof; prices moved between them (MRNA
  $234.33 → $235.63 → $235.97, KOD $100.00 → $96.11), so the tape is live.
- **`/info` primaryData can carry the prior close instead of a pre-market print.** On the 08:35
  snapshot KOD and HTFL came back with `netChange` empty and `deltaIndicator: "unch"` — the field
  was holding yesterday's close while the tape already held newer executed pre-market prints (KOD
  tape $100.75 vs `/info` $98.89). The published price uses `/info` **only when it carries a
  pre-market change**; otherwise the tape's consolidated print is used and the source is labelled
  in `pre-market-gapper.csv`. Every name in this final snapshot carried a live pre-market change,
  so all 12 published prices are live `/info` prints.
- **Cboe is not a pre-market source here.** Its `last_trade_time` is `2026-11-03T15:59:59` on all 12
  names and its `timestamp` was as old as 01:04 ET, so it confirms the prior close but carries no
  pre-market print. It is used for close confirmation only, not for the gap.
- **TradingView's `premarket_change` is not a last print and was not published as the gap.** On
  several names it equals the pre-market *extreme* rather than the last trade (KOD +2.66% is exactly
  its $101.52 pre-market high; FIGS −0.34% is exactly its $20.75 pre-market low; MRNA +3.52% is
  its $236.47 high), and on others it is a last print (CLF +1.98% = $14.42). TV's
  `premarket_volume` is a second venue's count and runs roughly half the Nasdaq tape's (MRNA
  106,957 vs 243,400; TEM 58,969 vs 127,119). Both are reported as a cross-check in the CSV only.
- **Pre-market volume counts are the Nasdaq `extended-trading` cumulative counter**, except VSEC,
  where no counter is published and the 4-print tape sum (32 shares) is used as a lower bound. The
  counter-vs-tape arbitration rule (a complete tape of <100 prints can overrule a faulty counter)
  was not triggered for any name in the final snapshot.
- **The screen behind the universe is itself one session stale.** The Focus list was built on
  shibui data for 2026-11-02 with 2026-11-03 closing prices, so the gapper is two sessions removed
  from the original screen. The Focus membership is not re-screened here by design.
- No Focus name printed a pre-market gap while volume exceeded 50,000, so there are no chat alerts
  to send; the "one line per flagged name" rule produced zero lines.

## Source health

| Source | Endpoint | Status | Used for |
|---|---|---|---|
| Nasdaq `/info` | `api.nasdaq.com/api/quote/{SYM}/info` | ok (200, 12/12; `marketStatus: Pre-Market`) | live pre-market price, bid/ask, timestamp |
| Nasdaq extended-trading tape | `api.nasdaq.com/api/quote/{SYM}/extended-trading?markettype=pre` | ok (200, 12/12, 4 pulls each; `cache-hit` headers present — stale vintages defended against) | executed prints, pre-market high/low, volume |
| Nasdaq `/info` pre-market field | same endpoint | degraded for 2 names on the 08:35 snapshot only (`unch` = prior close carried forward) | handled by the tape fallback, resolved by the 08:51 snapshot |
| TradingView scanner | `scanner.tradingview.com/america/scan` | ok (200, 12/12) | close confirmation, `premarket_volume`/`premarket_high`/`premarket_low` cross-check |
| Cboe delayed-quote CDN | `cdn.cboe.com/api/global/delayed_quotes/quotes/{SYM}.json` | ok (200, 12/12) but stale for pre-market (`last_trade_time` = 2026-11-03 15:59:59) | prior-close confirmation only |
| MCP bridge `market-recap` | `mcp_bridge.py market-recap get_quotes` | ok (12/12) | prior-session close + `market_state: pre` confirmation; carried no pre-market print |
| MCP availability probe | `probe_mcp.py` | `catalog_ok total=135 finance_tools=0` | no finance MCP registered on this runtime (not an error) |

## Files

- `daily-screens/2026-11-04/pre-market-gapper.md` — this report
- `daily-screens/2026-11-04/pre-market-gapper.csv` — machine-readable table, one row per Focus name (gap, volume, per-source provenance, TV cross-check)
- `daily-screens/2026-11-04/_premarket-pull.json` — full pull provenance per symbol (tape vintages seen, cache-hit headers, price source, divergence in pp)
- `daily-screens/2026-11-03/focus.csv` — the input universe, fetched from the outputs repo (prior session)

_Generated 2026-11-04 08:52 ET by cron #08 stock-screener-pre-market-gapper._
