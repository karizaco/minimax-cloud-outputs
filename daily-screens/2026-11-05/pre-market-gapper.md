# Pre-Market Gapper — Thursday, 05 November 2026

_contract: premarket-artifact-v4 · flagged: 0 · scanned: 12 · gate: |gap|>=4.0% and pm_volume>=50,000 and exec_shares>=25 · reference close: focus.csv+yahoo_chart+bridge (12/12 agree to the cent)_

> **Session:** the pre-market of Thu 2026-11-05, snapshot reconstructed at the routine's 08:30 ET mark
> (last pre-market print at or before 08:30; window 04:00–08:30 ET). **Source of record:** Yahoo Finance
> 1-minute chart bars with extended hours, cross-checked against the prior sweep, the MCP bridge,
> Nasdaq, Cboe and three fleet artifacts. **This is a late reconstruction** — the fire was dispatched
> 2026-11-05 08:30:56 ET and resumed 2026-11-06 05:26 ET (~21h later). The 08:30 tape itself did
> not survive; the price path did. Nothing below is tradeable advice.

## TL;DR

- **0 of 12 Focus names are flagged — and that is a statement about missing evidence, not about the
  tape.** Three names printed a pre-market gap at or beyond the 4% bar (**AEHR −6.31%**, **FN −4.58%**,
  **CIFR −4.00%**), but the 08:30 pre-market tape's volume counter and per-print sizes are gone, so the
  size leg of the gate cannot be evidenced and none of the three is counted as a flag.
- **The most consequential name is AEHR** — a −6.31% gap at the 08:30 mark, a −7.96% pre-market low at
  07:55, and a −7.56% opening print; it closed the session at −19.20%. FN (−4.58% → −5.75% at the open)
  and CIFR (−4.00% → −4.89%) both printed the bar too and both ended down double digits.
- **The caveat that changes how this file reads: it is a price-only reconstruction.** `exec_shares`
  is published as **0 = unevidenced** (not "no trade") and `pm_volume` is **empty** for every row,
  because the Nov 5 08:30 tape, its volume counter and its per-print sizes are permanently
  unrecoverable after the fact. Treat every gap here as a price fact and every size as unknown.

## Focus scan — all 12 names

| Ticker | Ref close (11-04) | PM price (last print ≤08:30) | Gap % | PM volume | Exec shares | Exec notional | PM high | PM low | Open gap % (09:30 print) | Verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **AEHR** | 60.84 | 57.00 | -6.31% | not recoverable | 0 (unevidenced) | 0 (unevidenced) | 59.30 | 56.00 | -7.56% | BORDERLINE_THIN |
| **FN** | 341.64 | 326.00 | -4.58% | not recoverable | 0 (unevidenced) | 0 (unevidenced) | 334.08 | 325.00 | -5.75% | BORDERLINE_THIN |
| **CIFR** | 6.50 | 6.24 | -4.00% | not recoverable | 0 (unevidenced) | 0 (unevidenced) | 6.50 | 6.19 | -4.89% | BORDERLINE_THIN |
| **APLD** | 16.61 | 15.95 | -3.97% | not recoverable | 0 (unevidenced) | 0 (unevidenced) | 16.60 | 15.80 | -4.21% | BORDERLINE_INTRADAY |
| **CLSK** | 6.80 | 6.64 | -2.35% | not recoverable | 0 (unevidenced) | 0 (unevidenced) | 6.84 | 6.62 | -3.09% | BELOW |
| **FRVO** | 8.90 | 8.70 | -2.25% | not recoverable | 0 (unevidenced) | 0 (unevidenced) | 8.91 | 8.61 | -3.26% | BELOW |
| **ECG** | 79.71 | 78.39 | -1.66% | not recoverable | 0 (unevidenced) | 0 (unevidenced) | 79.50 | 78.39 | -4.64% | BELOW |
| **BETA** | 25.31 | 24.90 | -1.62% | not recoverable | 0 (unevidenced) | 0 (unevidenced) | 25.23 | 24.90 | -1.22% | BELOW |
| **AEIS** | 211.56 | 209.11 | -1.16% | not recoverable | 0 (unevidenced) | 0 (unevidenced) | 209.11 | 209.11 | -5.28% | BELOW |
| **FISV** | 62.05 | 62.21 | +0.26% | not recoverable | 0 (unevidenced) | 0 (unevidenced) | 62.26 | 61.78 | +0.35% | BELOW |
| **CORZ** | 12.76 | 12.77 | +0.08% | not recoverable | 0 (unevidenced) | 0 (unevidenced) | 13.60 | 12.50 | -2.12% | BORDERLINE_INTRADAY |
| **EVER** | 30.60 | 30.60 | +0.00% | not recoverable | 0 (unevidenced) | 0 (unevidenced) | 30.60 | 30.60 | -0.49% | BELOW |

Sorted by absolute gap, largest first. Denominator = each name's settled 2026-11-04 close, taken from
the prior sweep's own `focus.csv` (`today_close`) and confirmed to the cent by Yahoo's
`chartPreviousClose` and the MCP bridge (12/12). "PM high/low" = the pre-market extremes in the
04:00–08:30 window, i.e. up to the snapshot. "Open gap %" = the executed 09:30 opening print against
the same denominator — the one gap on this page backed by a settled executed print.

## Focus names that did not qualify

Every scanned name whose verdict is not FLAGGED, with its gap, its pre-market range, its screen
provenance and a verdict on the setup. Ordered by setup quality (stylists desc, then origins desc,
then size of the miss).

- **AEHR** — -6.31% · pre-market range 56.00–59.30 · 3 stylists, 3 origins (A_stockbee_4pct, D_qullamaggie_ep, G_peoplewish) · setup: good setup that moved hard — it did not go nowhere: the −6.31% gap printed on the pre-market tape. The size behind it is unevidenced, so the screen's best setup of the morning is unverified rather than actionable. It closed the session at −19.20%.
- **ECG** — -1.66% · pre-market range 78.39–79.50 · 3 stylists, 3 origins (A_stockbee_4pct, G_peoplewish, jeff_sun_canslim) · setup: good setup that went nowhere at the snapshot — and the reading is stale: the last pre-market print before 08:30 was 08:13 (−1.66%); the −4.51% low came at 08:55, after the snapshot. Closed −9.12%.
- **AEIS** — -1.16% · pre-market range 209.11–209.11 · 3 stylists, 3 origins (A_stockbee_4pct, G_peoplewish, jeff_sun_canslim) · setup: good setup that went nowhere at the snapshot and then broke: the 08:30 reading rests on a single 04:13 print (−1.16%); the −5.23% low came at 09:29, after the snapshot. Closed −12.24%.
- **FISV** — +0.26% · pre-market range 61.78–62.26 · 3 stylists, 3 origins (A_stockbee_4pct, TV_volume_breakout, H_hernandez_theme) · setup: good setup that went nowhere: +0.26% on a 61.78–62.26 range, and the only name in the list that closed green (+1.11%).
- **CIFR** — -4.00% · pre-market range 6.19–6.50 · 2 stylists, 3 origins (A_stockbee_4pct, B_stockbee_ep9m, G_peoplewish) · setup: good setup that moved: the gap printed exactly on the bar (−4.00% at 08:30) and deepened to −4.89% at the open. Size unevidenced. Closed −14.62%.
- **APLD** — -3.97% · pre-market range 15.80–16.60 · 2 stylists, 3 origins (A_stockbee_4pct, B_stockbee_ep9m, G_peoplewish) · setup: good setup that touched the bar and gave it back: −4.88% at 08:10, −3.97% at 08:30 — 0.03pp short of the trigger — and −4.21% at the open. Closed −14.69%.
- **FN** — -4.58% · pre-market range 325.00–334.08 · 2 stylists, 2 origins (A_stockbee_4pct, G_peoplewish) · setup: good setup that moved: −4.58% printed at 08:30 and −5.75% at the open. Size unevidenced. Closed −14.25%.
- **CLSK** — -2.35% · pre-market range 6.62–6.84 · 2 stylists, 2 origins (A_stockbee_4pct, G_peoplewish) · setup: good setup that went nowhere at the snapshot (−2.35%, range +0.59% to −2.65%) and then fell hard after the open. Closed −16.47%.
- **FRVO** — -2.25% · pre-market range 8.61–8.91 · 2 stylists, 2 origins (A_stockbee_4pct, G_peoplewish) · setup: good setup that went nowhere at the snapshot (−2.25% on a +0.11% / −3.26% range) and then fell to −12.47% on the day.
- **BETA** — -1.62% · pre-market range 24.90–25.23 · 2 stylists, 2 origins (A_stockbee_4pct, TV_volume_breakout) · setup: good setup that went nowhere: −1.62% at 08:30 on eight pre-market bars, and the range never came close to the bar. Closed −4.98%.
- **CORZ** — +0.08% · pre-market range 12.50–13.60 · 2 stylists, 2 origins (A_stockbee_4pct, G_peoplewish) · setup: good setup that spiked and gave it all back: +6.58% at 07:01, +0.08% by 08:30, −2.12% at the open. Closed −10.82%.
- **EVER** — +0.00% · pre-market range 30.60–30.60 · 2 stylists, 2 origins (A_stockbee_4pct, TV_volume_breakout) · setup: bad setup: no pre-market activity at all — one print at 07:00 at the prior close and nothing else. Closed −0.92%.

## Flags

- **AEHR −6.31%** — the gap printed on the pre-market tape at 08:30, but `exec_shares` is published
  as **0 = unevidenced, not "no trade"**, and `pm_volume` is unrecoverable. The price is a fact; the
  size behind it is unknown, so the name is NOT a flag and must not be treated as one.
- **CIFR −4.00%** — printed **exactly** on the 4.00% bar: **0.00pp of margin**. A rounding
  difference in the denominator would move this name across the line in either direction. Size
  unevidenced.
- **FN −4.58%** — over the bar by 0.58pp, and the pre-market low reached −4.87% at 08:30. Size
  unevidenced; the same caution as AEHR applies.
- **APLD −3.97%** — 0.03pp short of the bar at 08:30, but it **did** trade at −4.88% at 08:10, inside
  the snapshot window. The nearest near-miss in the list, and the reason the verdict is
  `BORDERLINE_INTRADAY`.
- **CORZ +6.58% at 07:01, +0.08% at 08:30** — a 6.5pp swing inside the pre-market session. Its 08:30
  reading is not a measure of the day's risk: it closed −10.82%.
- **Thin bar coverage — AEIS (1 bar, last 04:13), ECG (4 bars, last 08:13), EVER (1 bar, 07:00), BETA
  (8 bars)** — these four 08:30 readings rest on a very short pre-market series, so "no gap at 08:30"
  is weaker evidence for them than for the eight names with 16+ bars. AEIS in fact collapsed to
  −5.23% at 09:29 and ECG to −4.51% at 08:55, both after the snapshot.
- **Denominator conflict (not on the denominator):** Nasdaq's `/info` `secondaryData` reads 48.91 for
  AEHR's 11-05 close where Yahoo, TradingView, the bridge, Nasdaq's own chart endpoint and Cboe all
  read 49.16 — the documented Nasdaq drift. The 11-04 denominator used here is unaffected:
  focus.csv, Yahoo and the bridge agree to the cent on all 12 names.

## Method, source health & caveats

**This run is a reconstruction.** The scheduler dispatched the fire at 2026-11-05 08:30:56 ET; the
platform resumed this conversation on 2026-11-06 at 05:26 ET, ~21 hours later, and the gate was
judged against the fire's scheduled instant (`window_check.sh --scheduled-at-ms`), which returned
`fire-date: 2026-11-05 · replay: yes`. The artifact is therefore rebuilt for the 2026-11-05 session
and no SKIPPED marker was written. The gate and the artifact path agree on the day.

**What the 08:30 tape cost, and what it bought.** The routine's source of record is the Nasdaq
`extended-trading` tape plus `/info`: a 4-pull, max-newest-timestamp defence against a shared HTTP
cache that serves hour-old vintages. That defence is irrelevant here — those endpoints serve only
the live session, and the live session is now 2026-11-06. The Nov 5 08:30 tape, its volume counter and
its per-print sizes are gone for good. What survived is the **price path**: Yahoo's 1-minute chart
bars with `includePrePost=true` carry every pre-market print of the Nov 5 session, so the snapshot
price, the pre-market range, the intraday crossings and the 09:30 opening print are all recoverable
as prices — but **not as sizes**: Yahoo reports extended-hours volume as 0 (not "no trading", a
non-report), and no other source in the fleet archived the Nov 5 pre-market volume for these names.
That is why `pm_volume` is empty on every row and `exec_shares` is 0 on every row.

**The denominator and who agreed on it.** Per SKILL §6.3 the denominator is the settled prior
regular-session close, taken from the prior sweep's own `focus.csv` — here `daily-screens/
2026-11-04/focus.csv` (`today_close`, the 2026-11-04 session close). It was cross-checked against
two independent sources and **all three agree to the cent on all 12 names**: Yahoo
`chartPreviousClose` on the Nov 5 chart, and the MCP bridge `market-recap` `previous_close`
(`market_state: "pre"`, `as_of` 2026-11-05T21:00Z — the prior regular close, exactly the role the
skill assigns it). `ref_close_source` = `focus.csv(today_close)+yahoo_chart_previousClose+bridge`.

**Three independent fleet cross-checks on the reconstruction.** (1) Cron #17's Nov 5 09:50 ET board
(`us-stocks-in-play/2026-11-05-open-candidates.csv`) publishes its own Yahoo-derived gap and open
gap for 10 of these names; they match this reconstruction to four decimals — AEHR −7.5279 /
−7.5608, CIFR −4.7692 / −4.8923, APLD −3.7628 / −4.2143, FN −5.1633 / −5.7487, ECG −3.8013 /
−4.6418, CORZ −1.7241 / −2.1160, AEIS −5.2278 / −5.2845, CLSK −2.2059 / −3.0882, BETA −1.3829 /
−1.2248, FRVO −3.0337 / −3.2584. (2) Cron #15's 08:22 ET artifact (`earnings/2026-11-05-reactions.md`)
publishes an independent pre-market gap for AEHR of **−6.31%** — identical to this 08:30 reading —
plus CIFR −4.14% and APLD −3.78%. (3) The fleet's own 08:30 pre-open feed
(`preopen-feed/2026-11-05-0830.jsonl`, captured 10:10 ET) carries TradingView's frozen final
pre-market print for 7 of the 12 (AEHR −6.97, FN −5.69, AEIS −5.23, CIFR −4.77, APLD −3.67,
FRVO −3.03, ECG −2.86) — all consistent with the reconstructed path.

**The margin against the trigger.** Three names were at or beyond the 4% bar at the snapshot
(AEHR −6.31%, FN −4.58%, CIFR −4.00%) and one was 0.03pp short (APLD −3.97%). Four more crossed
the bar inside the pre-market session and were not there at the snapshot (APLD −4.88% at 08:10,
CORZ +6.58% at 07:01, plus AEIS and ECG after the snapshot) — the session-wide extremes are in the
CSV and the provenance file. Because the size and volume legs cannot be evidenced, **the "no flags"
verdict here is a statement about missing tape evidence, not a clean bill of health for the three
names that printed the bar.**

**Nasdaq defects checked before trusting anything.** `secondaryData.lastSalePrice` was read for
AEHR and returned 48.91 against 49.16 from five other sources (the documented drift — it is why the
denominator is taken from the sweep + two agreeing sources, not from `/info`); `primaryData` was
confirmed to be carrying the **2026-11-06** pre-market ($53.60 with `marketStatus: Pre-Market`), so
it was not used at all; the `extended-trading` tape returned 0 rows for the current pre-market and
cannot return Nov 5 rows; the `chart` endpoint was used instead and returns the settled 11-05 daily
bar (open 56.11, high 57.9993, low 47.01, close 49.16, volume 4,867,458) matching Yahoo and
TradingView.

**Snapshot timestamps.** The snapshot instant is the routine's 08:30 ET mark. The last pre-market
print at or before it is per name and published in the CSV (`pm_last_print_et`): 08:30 for AEHR,
APLD, CIFR, CLSK, CORZ, FN; 08:29 FRVO; 08:26 FISV; 08:13 ECG; 08:08 BETA; 04:13 AEIS; 07:00 EVER.
The window is 04:00–08:30 ET. Bar coverage per name is published (`pm_bars_to_0830`).

**What the session actually did** (context for the next fire, not a gapper finding): the tape was
sharply lower — 9 of these 12 names closed down between −4.98% and −19.20% (AEHR −19.20, CLSK
−16.47, APLD −14.69, CIFR −14.62, FN −14.25, FRVO −12.47, AEIS −12.24, CORZ −10.82, ECG −9.12),
BETA −4.98%, EVER −0.92%, and only FISV was green (+1.11%). The pre-market gaps were the early
warning on most of them, but the pre-market print was not the opening print for the names that
extended and overstated the move for the names that faded — the same pattern cron #26b documented
for the whole market.

**Provenance.** The universe is the Focus list of the most recent completed 18:30 ET sweep before
the fire (`daily-screens/2026-11-04/focus.csv`, 12 names; screen data date 2026-11-03, session
close 2026-11-04). `stylists` and `origins` are carried through verbatim from that file — no name
was re-screened, and no name was dropped for failing to qualify.

**Source health**

| Source | Endpoint / query | Status | Used for |
|---|---|---|---|
| Prior sweep Focus list | `minimax-cloud-outputs` `daily-screens/2026-11-04/focus.csv` | ok (12 rows) | universe, screen provenance, the denominator (`today_close`) |
| Yahoo 1-minute chart, extended hours | `query1.finance.yahoo.com/v8/finance/chart/{SYM}` `interval=1m&includePrePost=true` | ok (12/12) | the pre-market price path, the snapshot print, the 09:30 open, `chartPreviousClose` |
| Yahoo daily chart | same endpoint, `interval=1d` | ok (12/12) | the 11-04 and 11-05 settled closes |
| MCP bridge `market-recap` `get_quotes` | `mcp_bridge.py market-recap get_quotes` (one batched call) | ok (12/12) | denominator cross-check (`previous_close`), the 11-05 close, high/low |
| Nasdaq `chart` endpoint | `api.nasdaq.com/api/quote/{SYM}/chart` for 11-04 / 11-05 | ok | the settled 11-05 daily bar (spot check on AEHR) |
| Cboe delayed-quote CDN | `cdn.cboe.com/api/global/delayed_quotes/quotes/{SYM}.json` | ok (200 with `-L`; the plain request 307-redirects) | 11-05 close cross-check (AEHR, FN) |
| TradingView scanner | `scanner.tradingview.com/america/scan` | **degraded** — the scanner now serves the 2026-11-06 pre-market session (`premarket_time` = 2026-11-06 04:00 ET); the 11-05 pre-market fields are not retrievable, and the frozen 11-05 values that survive in the fleet's 08:30 pre-open feed carry **no volume** | 11-05 close cross-check only |
| Nasdaq `extended-trading` tape + `/info` | `api.nasdaq.com/api/quote/{SYM}/extended-trading`, `/info` | **degraded** — live-session only; the 11-05 08:30 tape, its volume counter and its per-print sizes are permanently unrecoverable after the fact | nothing — this is the source of record the routine normally uses |
| MCP availability probe | `probe_mcp.py` | `catalog_ok total=135 finance_tools=0 · bridge bridge_ok packs=tradier,fmp,market-recap` | no finance MCP registered on this runtime (not an error) |
| Fleet cross-checks | cron #17 09:50 board, cron #15 08:22 artifact, `preopen-feed/2026-11-05-0830.jsonl` | ok | independent corroboration of the reconstructed gaps (see Method) |

`degraded_sources: 2` — the two live-session-only pre-market sources (TradingView's pre-market
fields, Nasdaq's tape and `/info`) cannot serve a 21-hour-old session. The gaps and their
corroboration were recovered; the **sizes were not**.

---

_Generated 2026-11-06 05:26 ET as a late reconstruction of the 2026-11-05 08:30 ET fire by cron #08
stock-screener-pre-market-gapper. Contract `premarket-artifact-v4`._
