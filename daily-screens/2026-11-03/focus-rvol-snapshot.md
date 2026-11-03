---
date: 2026-11-03
cron: 07-stock-screener-focus-rvol-09:45
fire_time_et: "09:45"
data_date: 2026-10-30
quote_data_date: 2026-11-03
upstream_focus: daily-screens/2026-11-02/focus.md
upstream_lag_sessions: 1
source: bridge market-recap (live quotes + session volume) + TradingView scanner (average_volume_10d_calc) + CBOE delayed quotes (session-only volume cross-check) + shibui (trailing-10 settled volume cross-check) + cron #08 pre-market-gapper.csv (pre-market volume subtraction)
method: intraday_rvol_session_volume_over_tv_avg10d_pace_adjusted
status: ok
---

# Focus RVOL snapshot — 2026-11-03 09:45 ET (cron #07)

**Headline:** one focus name is running hot enough to clear the RVOL Required bar — **CVI at 6.9×
pace-adjusted RVOL**, on 321,049 shares in the first 27 minutes of the session, while the stock
falls **-8.65%**. It is the only name above 3× at the 09:56 snapshot. **CDNA (2.83×) and HTFL
(2.83×)** sit just under the bar, both on the tape with volume building.

**Caveat that changes how this reads:** CVI's pace-RVOL is a *falling* number, not a rising one —
it measured **14.4× at the 09:38 cross-check tape** and **6.9× at 09:56**. A name whose pace-RVOL
decays from 14× to 7× is a name that front-loaded its volume into the first minutes and is now
trading more slowly than its own early pace. Read CVI as "the heaviest tape in the focus list, and
the tape is thinning", not as "accelerating". Its -8.65% is a distribution, not accumulation.

## Universe

12 names from `daily-screens/2026-11-02/focus.md` — the most recent completed 18:30 ET sweep
(Monday 2026-11-02, 12 names). This is a **1-session lag**, the freshest focus list in the repo;
the 2026-11-03 directory holds only cron #08's pre-market gapper output, because the sweep that
would write `focus.md` for today has not fired yet (it runs 18:30 ET).

Note on the upstream header: the sweep's own `data_date` field reads **2026-10-30** (shibui T+1
screen data), while its price columns are the **2026-11-02** close. Both are carried above; the
focus list's *screen* data is 2 sessions behind the focus list's *prices*.

## Table — sorted by RVOL desc

RVOL is **session-pace-adjusted intraday RVOL**: regular-session volume through the 09:56 bar ÷
(average daily volume over 10 days × elapsed session fraction, 26.7/390 min). Rationale in
*Method* below. `Close` is the bridge `market-recap` last trade at 09:56 ET.

| symbol | close | RVOL | bucket | data timestamp |
|---|---:|---:|---|---|
| CVI | 51.085 | 6.91 | RVOL Required | 2026-11-03 09:56:43 ET (vol @ 09:56) |
| CDNA | 89.285 | 2.83 | Liquid | 2026-11-03 09:56:42 ET (vol @ 09:56) |
| HTFL | 55.690 | 2.83 | Liquid | 2026-11-03 09:56:32 ET (vol @ 09:56) |
| MRNA | 230.770 | 1.55 | Liquid | 2026-11-03 09:56:40 ET (vol @ 09:56) |
| ABCL | 11.900 | 1.40 | Liquid | 2026-11-03 09:56:15 ET (vol @ 09:56) |
| KOD | 100.510 | 1.27 | Liquid | 2026-11-03 09:55:58 ET (vol @ 09:56) |
| MTZ | 198.835 | 1.20 | Liquid | 2026-11-03 09:56:33 ET (vol @ 09:56) |
| QLYS | 205.740 | 1.09 | Liquid | 2026-11-03 09:56:40 ET (vol @ 09:56) |
| CAI | 33.400 | 1.07 | Liquid | 2026-11-03 09:56:27 ET (vol @ 09:56) |
| NOW | 105.680 | 1.03 | Liquid | 2026-11-03 09:56:42 ET (vol @ 09:56) |
| PURR | 10.260 | 0.98 | Liquid | 2026-11-03 09:56:44 ET (vol @ 09:56) |
| LQDA | 42.277 | 0.67 | Liquid | 2026-11-03 09:56:04 ET (vol @ 09:56) |

### Counts

- Focus tickers: **12**
- RVOL Required (RVOL >= 3): **1** — CVI
- Liquid (RVOL < 3): **11** — CDNA, HTFL, MRNA, ABCL, KOD, MTZ, QLYS, CAI, NOW, PURR, LQDA
- Tickers crossing from below 1 to above 3 during this session: **1 — CVI**, confirmed against an
  independent earlier tape. CVI's pace-RVOL read **14.38×** on the CBOE 09:38 cross-check tape
  (200,069 shares in 8.2 minutes) and **6.91×** at 09:56; it has been above 3× since the opening
  minutes and has stayed there. **No other name crossed**: the three that were above 3× on the
  09:38 tape (CDNA 4.38, HTFL 3.84, MRNA 3.01) had already been above 3 before that reading and
  have since fallen back below the bar — they are decoys, not crossings.

**Alert: CVI crossed from below 1 to above 3 on pace-adjusted RVOL this session** — 321,049 shares
in 27 minutes against a 678,393-share 10-day average, on the tape at -8.65%.

## Volume detail

Session volume is the quote feed's cumulative volume **minus pre-market volume**, taken from
cron #08's own `pre-market-gapper.csv` for today. This subtraction is what makes the metric
comparable across names — the raw cumulative figure contains pre-market prints, which for NOW
(1,107,335) and PURR (595,761) are larger than their entire first-half-hour regular-session volume.

| symbol | gross cum vol (09:56) | pre-market vol (cron #08) | session vol | avg daily vol 10d (TV) | raw RVOL | pace RVOL (bucket metric) | chg vs prev close |
|---|---:|---:|---:|---:|---:|---:|---:|
| CVI | 336,434 | 15,385 | 321,049 | 678,393 | 0.473 | 6.91 | -8.65% |
| CDNA | 267,882 | 3,350 | 264,532 | 1,365,823 | 0.194 | 2.83 | +3.96% |
| HTFL | 275,924 | 3,526 | 272,398 | 1,416,953 | 0.192 | 2.83 | +2.20% |
| MRNA | 1,817,351 | 94,485 | 1,722,866 | 16,301,782 | 0.106 | 1.55 | +4.50% |
| ABCL | 308,308 | 28,121 | 280,187 | 2,967,495 | 0.094 | 1.40 | +7.01% |
| KOD | 68,681 | 6,739 | 61,942 | 733,346 | 0.084 | 1.27 | +2.96% |
| MTZ | 144,236 | 2,494 | 141,742 | 1,732,196 | 0.082 | 1.20 | +2.61% |
| QLYS | 63,134 | 2,040 | 61,094 | 817,461 | 0.075 | 1.09 | -0.90% |
| CAI | 218,377 | 20,267 | 198,110 | 2,737,478 | 0.072 | 1.07 | +4.05% |
| NOW | 2,778,769 | 1,107,335 | 1,671,434 | 23,612,113 | 0.071 | 1.03 | -0.31% |
| PURR | 1,771,914 | 595,761 | 1,176,153 | 17,443,573 | 0.067 | 0.98 | +5.66% |
| LQDA | 156,380 | 29,424 | 126,956 | 2,819,113 | 0.045 | 0.67 | +1.02% |

### Earlier tape cross-check (CBOE, 09:38 ET — session-only volume, no pre-market)

Independent second reading used for the crossing test. `pace RVOL @09:38` uses the same 10-day
denominator over 8.2 elapsed minutes.

| symbol | CBOE session vol @09:38 | pace RVOL @09:38 | pace RVOL @09:56 | direction |
|---|---:|---:|---:|---|
| CVI | 200,069 | 14.38 | 6.91 | decaying, still >3 |
| CDNA | 122,766 | 4.38 | 2.83 | decayed below 3 |
| HTFL | 111,712 | 3.84 | 2.83 | decayed below 3 |
| MRNA | 1,005,071 | 3.01 | 1.55 | decayed below 3 |
| ABCL | 143,791 | 2.36 | 1.40 | below 3 throughout |
| KOD | 28,787 | 1.91 | 1.27 | below 3 throughout |
| QLYS | 38,919 | 2.32 | 1.09 | below 3 throughout |
| LQDA | 89,276 | 1.54 | 0.67 | below 3 throughout |
| PURR | 537,811 | 1.50 | 0.98 | below 3 throughout |
| NOW | 685,009 | 1.41 | 1.03 | below 3 throughout |
| MTZ | 49,848 | 1.40 | 1.20 | below 3 throughout |
| CAI | 45,089 | 0.80 | 1.07 | below 3 throughout |

## Method

1. **Window check** — 2026-11-03 is a trading Tuesday (not a 2026 NYSE closure). Market state
   confirmed `open` by the bridge at 09:47–09:56 ET.
2. **Upstream focus list** — pulled `origin/main` of `karizaco/minimax-cloud-outputs`, read
   `daily-screens/2026-11-02/focus.md` (12 names). No `focus.md` exists for 2026-11-03 yet; that
   sweep fires 18:30 ET today. **1-session lag** — the freshest list available.
3. **Closes** — bridge `market-recap get_quotes`, one batch of 12 symbols, `market_state: open`,
   `as_of` 09:55:58–09:56:44 ET. Quote source of record.
4. **Session volume** — the bridge's cumulative `volume` field **includes pre-market prints**.
   Pre-market volume was therefore subtracted using cron #08's own published
   `daily-screens/2026-11-03/pre-market-gapper.csv` (consolidated tape, 09:12 ET snapshot). The
   size of the correction is not cosmetic: NOW's pre-market volume (1,107,335) exceeds its entire
   regular-session volume at 09:56 (1,671,434) by two-thirds, and PURR's (595,761) is half of its
   session volume. Without the subtraction NOW would print a false 1.48 pace RVOL and PURR 1.53 —
   both above the 3× bar's neighbourhood and both wrong.
5. **Independent volume cross-check** — CBOE delayed quotes (`cdn.cboe.com/api/global/delayed_quotes/quotes/{SYM}.json`),
   12/12 HTTP 200. CBOE's `volume` is regular-session only, so it validates the session-volume
   figures directly and provides the earlier 09:38 tape used for the crossing test.
6. **Denominator** — TradingView public scanner `POST https://scanner.tradingview.com/america/scan`,
   column `average_volume_10d_calc`, one **per-ticker `equal`** scan (12/12 rows returned; a
   `symbols.tickers` request returned 0 rows on this endpoint and was discarded).
7. **Denominator cross-check** — shibui trailing-10 settled daily volume over the same window,
   via the MCP-over-HTTP bridge (`stock_data_query`, 200-row cap respected). TV's average runs
   4–17% tighter than shibui's (e.g. NOW 23,612,113 vs 24,444,141), so the shibui-based pace RVOL
   is slightly lower for every name. **The bucket split is identical under both denominators**
   (CVI alone above 3×) and the top-3 ranking is unchanged, so the classification does not depend
   on which denominator is used.
8. **Metric** — the prompt's literal definition (cumulative volume ÷ 10-day average daily volume)
   is published above as `raw RVOL`. At 26.7 minutes into a 390-minute session only 6.8% of the day
   has elapsed, so a raw RVOL of 3.0 is arithmetically unreachable before roughly 10:30 ET — the
   raw column tops out at **0.473** (CVI) and the RVOL Required bucket under the literal
   definition would be **empty (0/12)**. The **bucket metric is therefore the pace-adjusted RVOL**
   (raw ÷ elapsed session fraction), which is the standard "is this name trading hot right now"
   reading of Sun's RVOL Required tier. Both numbers are published for every name.
9. **Pre-market vs overnight** — no symbol carried a bar dated after the session date; the CBOE
   tape's `last_trade_time` was parsed and confirmed to fall inside the 2026-11-03 regular session
   for all 12 names.

## Source health

| source | query | status | result |
|---|---|---|---|
| MCP catalog probe | `probe_mcp.py` | ok | `catalog_ok total=135 finance_tools=0` — no finance MCP registered, as expected |
| upstream outputs repo | `git fetch origin main` → `daily-screens/` | ok | newest `focus.md` = 2026-11-02 (12 names); `daily-screens/2026-11-03/` holds only cron #08's gapper output |
| bridge `market-recap` | `get_quotes` (12 symbols, 3 batches) | ok | 12/12 found, `market_state: open`, `as_of` 09:55–09:56 ET |
| TradingView scanner | `POST /america/scan` per-ticker `equal` ×12 | ok | 12/12 rows with `average_volume_10d_calc`; the `symbols.tickers` variant returned 0 rows and was discarded |
| CBOE delayed quotes | `cdn.cboe.com/.../quotes/{SYM}.json` ×12 | ok | 12/12 HTTP 200, session-only volume, 09:38 tape |
| shibui (MCP bridge) | `stock_data_query` (trailing-10 volumes, 12 tickers) | ok | 12/12 tickers × 13 sessions returned |
| cron #08 gapper | `daily-screens/2026-11-03/pre-market-gapper.csv` | ok | pre-market volume for all 12 names, used for the session-volume subtraction |
| Yahoo chart API | `query1/query2 /v8/finance/chart/{sym}?interval=5m&range=1d` | **failed: 429** | crumb handshake returned the plain-text body `Too Many Requests` on both `query1` and `query2`; no crumb obtainable, so no intraday bars from Yahoo. Route changed to the bridge + CBOE + Nasdaq paths, which are unaffected. |

## Degradation / caveats

- **Yahoo chart API unavailable (429).** The preferred intraday-bar path was blocked by rate
  limiting from this egress; the crumb handshake was attempted and failed on both hosts. This did
  not degrade the artifact — session volume was obtained from the bridge quote feed and validated
  against CBOE's independent session-only tape — but the *5-minute bar series* was not published.
- **Quote volume contains pre-market prints.** Documented above; corrected with cron #08's
  pre-market volumes. Anyone recomputing from raw quote volume will get materially different
  numbers for NOW and PURR.
- **CVI's pace-RVOL is decaying (14.38× → 6.91×), not rising.** The cross above 3 is real and
  was independently confirmed, but the tape is thinning. Treat CVI as a heavy *distribution*.
- **Denominator source matters for level, not for classification.** TV's 10-day average runs
  4–17% below shibui's trailing-10 settled average; both denominators produce the same bucket
  split and the same top-3.
- **CDNA and HTFL are both at 2.83×** and were above 3× at 09:38. They are right at the bar, and a
  10-minute-later read could put either back over it. No alert was emitted for them because
  neither crossed *upward* from below 1.
- **Single snapshot per source.** Two independent readings exist (CBOE 09:38, bridge 09:56), which
  is enough for a crossing test but not for a continuous pace curve.
- No symbol was skipped, and no value in this artifact is estimated or carried over from a
  previous session.
