---
date: 2026-10-28
cron: "#7 stock-screener-focus-rvol-09:45"
fire_time_et: "2026-10-28 09:45 ET"
data_date: 2026-10-28
upstream_data_date: 2026-10-27
source: "yahoo_finance_chart_api (5m intraday volume + live close) + tradingview_public_scanner (average_volume_10d_calc denominator)"
method: intraday_rvol_yahoo_5m
status: ok
upstream_focus_md: /workspace/daily-screens/2026-10-27/focus.md
upstream_cron_date: 2026-10-27
capture_window_et: "09:47 ET (all 12 symbols); run completed 09:48 ET"
elapsed_session_minutes: 18.0 (of 390)
rvol_required_count: 0
liquid_count: 12
no_data_count: 0
alert_emitted: false
---

# Focus RVOL snapshot - 2026-10-28 09:45 ET

**The RVOL Required bucket is empty again, and on the contract metric that is arithmetic rather than a signal.** Cumulative volume-to-date is normalized against a *full day's* average volume, and only 18 minutes (4.6%) of the 390-minute regular session had elapsed at capture, so a raw RVOL of 3.0 was not reachable for any of the 12 focus names. The pace-adjusted column exists to test whether that empty bucket is hiding anything, and it partly is: **CRML is printing at 5.7x full-day average volume pace** (0.2637 contract RVOL on 1,740,580 shares so far) and **SDGR at 3.6x**. Both are above the 3.0 threshold on a pace basis and neither is reclassified, because the bucketing metric is the contract metric and reclassifying on a pace estimate is exactly the kind of silent reclassification this run is meant to avoid.

**The focus list is one session old, and it is the freshest one that can exist.** It comes from the 2026-10-27 18:30 ET sweep, whose data date is the settled **2026-10-27 close** (Tuesday). Today's sweep fires at 18:30 ET and had not run at capture time, so the list reflects yesterday's close, not this morning. The live RVOL readings are today's (2026-10-28 regular-session bars). The 2026-10-28 directory holds only the pre-market gapper artifacts at capture; there is no same-day `focus.md` to find, which is the expected state at 09:45 ET rather than a missing upstream.

## Snapshot

| Symbol | Close | RVOL | Bucket | Data timestamp (ET) |
| --- | ---: | ---: | --- | --- |
| CRML | 7.62 | 0.2637 | Liquid | 09:47 ET |
| SDGR | 28.57 | 0.1667 | Liquid | 09:47 ET |
| HRI | 164.51 | 0.1062 | Liquid | 09:47 ET |
| RKLB | 57.33 | 0.1061 | Liquid | 09:47 ET |
| ALAB | 288.99 | 0.0971 | Liquid | 09:47 ET |
| LUNR | 11.26 | 0.0960 | Liquid | 09:47 ET |
| ON | 75.55 | 0.0906 | Liquid | 09:47 ET |
| RDW | 8.78 | 0.0903 | Liquid | 09:47 ET |
| MXL | 75.37 | 0.0852 | Liquid | 09:47 ET |
| GLXY | 17.17 | 0.0787 | Liquid | 09:47 ET |
| OUST | 32.55 | 0.0729 | Liquid | 09:47 ET |
| CYPH | 3.05 | 0.0713 | Liquid | 09:47 ET |

Sorted by RVOL descending. Closes are live regular-session prints from Yahoo's chart payload; every data timestamp is the payload's own quote stamp (09:47 ET), not the cron's fire time. All 12 focus names returned intraday bars - there is no `no_intraday_bars` symbol in this run, and no name fell back to a daily proxy.

## Counts

| Bucket | Count | Tickers |
| --- | ---: | --- |
| RVOL Required (RVOL >= 3) | 0 | — |
| Liquid (RVOL < 3) | 12 | CRML, SDGR, HRI, RKLB, ALAB, LUNR, ON, RDW, MXL, GLXY, OUST, CYPH |
| No data | 0 | — |

The empty RVOL Required bucket is a real result, not a failure: 12 of 12 focus names were priced and measured, and the arithmetic ceiling on the contract metric at 09:48 ET is roughly 0.046 x 3.0 = 0.139 of a full day's average volume. Every name in the table is below that ceiling, so a non-empty bucket was not reachable for any universe today.

## Volume detail and pace

| Symbol | Cum volume (shares) | Avg 10d vol (TV) | RVOL (contract) | Pace-adjusted RVOL | Change vs prior close |
| --- | ---: | ---: | ---: | ---: | ---: |
| CRML | 1,740,580 | 6,600,733 | 0.2637 | 5.71x | -6.21% |
| SDGR | 242,782 | 1,456,804 | 0.1667 | 3.61x | +6.92% |
| HRI | 89,678 | 844,516 | 0.1062 | 2.30x | +5.42% |
| RKLB | 2,010,179 | 18,945,521 | 0.1061 | 2.30x | -1.68% |
| ALAB | 310,438 | 3,195,914 | 0.0971 | 2.10x | +0.80% |
| LUNR | 579,961 | 6,041,684 | 0.0960 | 2.08x | -2.60% |
| ON | 766,233 | 8,458,956 | 0.0906 | 1.96x | -3.97% |
| RDW | 947,174 | 10,493,795 | 0.0903 | 1.96x | -1.29% |
| MXL | 325,142 | 3,814,938 | 0.0852 | 1.85x | +0.94% |
| GLXY | 644,608 | 8,194,188 | 0.0787 | 1.70x | -0.06% |
| OUST | 187,198 | 2,567,142 | 0.0729 | 1.58x | -0.73% |
| CYPH | 829,238 | 11,632,204 | 0.0713 | 1.54x | -2.87% |

Pace-adjusted RVOL divides the contract RVOL by the elapsed-session fraction (18 min / 390 min = 0.0462), which projects the volume accumulated so far across a full session. It is **supplementary context only** and no bucket above was assigned from it. CRML is the standout: it opened 2026-10-28 at 7.88 against an 8.13 prior close and is still around 7.63, but it has already traded 1.74M shares in eighteen minutes against a 10-day average of 6.60M. SDGR is the second-most active name on the same basis, up from 26.72 to 28.57 on the session. The rest of the list is printing between 1.5x and 2.3x pace, which is ordinary participation for a Wednesday open.

## Method

1. **Focus list** - pulled from the upstream `minimax-cloud-outputs` remote (`git fetch origin main`, then `daily-screens/2026-10-27/focus.md`). 12 tickers, 3 stylist flags each, from the 2026-10-27 18:30 ET sweep.
2. **Numerator** - Yahoo Finance chart API, `interval=5m&range=1d&includePrePost=false`, one request per symbol. Cumulative volume is the sum of the regular-session 5-minute bars for 2026-10-28.
3. **Denominator** - TradingView public scanner (`POST https://scanner.tradingview.com/america/scan`), column `average_volume_10d_calc`, one batched call for all 12 symbols.
4. **Cross-check denominator** - each symbol's own trailing-10-session average daily volume, computed from a second Yahoo chart call (`interval=1d&range=3mo`, today excluded). This is a sensitivity check, not the bucketing input.
5. **Bucketing** - sorted by contract RVOL descending; RVOL >= 3 is *RVOL Required*, everything else is *Liquid*.

## Caveats and degradation

- **In-progress bar dropped.** Each symbol's final bar (stamped 09:47 ET) is the live in-progress bar and carries volume 0, so it was excluded from the cumulative sum; the partial 09:45 bar was kept because it holds real traded volume. No bar was dated after the 2026-10-28 session date, and no symbol was affected by a next-session or overnight print.
- **Denominator bias, and which way it cuts.** TradingView's `average_volume_10d_calc` ran consistently *below* the Yahoo trailing-10-session average for all 12 names, with ratios of 0.862-0.937 (median ~0.90). The tighter TV denominator therefore **overstates** contract RVOL by roughly 6-16% relative to a Yahoo denominator. It does not matter today - the gap to the 3.0 bucket is an order of magnitude - but a name near 2.9 on this metric would still sit below the bar on the Yahoo denominator. The Yahoo-denominator RVOL column is included in `focus-rvol-snapshot.csv` for anyone who wants the conservative read.
- **One session of lag on the focus list.** The list is built from the 2026-10-27 close, so today's RVOL is being measured on names selected yesterday, not on a list refreshed for this morning. This is structural: the sweep runs at 18:30 ET.
- **No alert emitted.** The crossing rule is a move from below 1 to above 3 on the contract metric. SDGR is the only focus name that also appeared in the 2026-10-27 09:45 snapshot (prior contract RVOL 0.0645, now 0.1667); the other 11 have no prior baseline in yesterday's artifact because yesterday's list was a different set. No name crossed above 3 on the contract metric, so no chat alert fired.
- **TV live quote columns lag.** The scanner's `volume` column returned 614,593 for CRML against Yahoo's 1,740,580 for the same symbol minutes earlier, so TV's live fields were not used for prices or volume - only for the 10-day average, which is a settled statistic.
- **Validation.** CRML's prior close of 8.13 and its +27.43% 2026-10-27 move were confirmed against independent quotes (Barron's and Perplexity Finance), and the trailing daily volume series matched an independent Yahoo history page to within rounding on 9 of 10 sessions.

## Source health

| Source | Request | Status |
| --- | --- | --- |
| Upstream outputs repo | `git fetch origin main` -> `daily-screens/2026-10-27/focus.md` | ok |
| Yahoo cookie/crumb | `fc.yahoo.com` seed + `query2.finance.yahoo.com/v1/test/getcrumb` | ok |
| Yahoo chart API (5m) | 12 requests, one per focus symbol | ok (12/12) |
| Yahoo chart API (1d/3mo) | 12 requests, trailing-10-session volume | ok (12/12) |
| TradingView public scanner | 1 batched POST, 12 symbols, `average_volume_10d_calc` | ok (totalCount 12) |
| StockTwits chart feed (MCP bridge) | `chart_data` period=1M and 1d, CRML | ok - cross-check only |

Total source health entries: 25; failures: 0. No source was rate-limited in this run, and no daily-proxy fallback was used.

## Files

- `daily-screens/2026-10-28/focus-rvol-snapshot.md` - this artifact
- `daily-screens/2026-10-28/focus-rvol-snapshot.csv` - machine-readable table (symbol, close, RVOL, both denominators, pace, timestamps, bucket)

## Errors

errors: 0
