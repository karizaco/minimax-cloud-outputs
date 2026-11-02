---
date: 2026-11-02
cron: 07-stock-screener-focus-rvol-09:45
fire_time_et: "09:45"
data_date: 2026-10-30
quote_data_date: 2026-11-02
upstream_focus: daily-screens/2026-10-30/focus.md
upstream_lag_sessions: 3
source: bridge market-recap (closes) + TradingView scanner (average_volume_10d_calc) + Yahoo chart 5m (intraday volume)
method: intraday_rvol_yahoo_5m_over_tv_avg10d
status: ok
---

# Focus RVOL snapshot — 2026-11-02 09:45 ET (cron #07)

**Headline:** 4 of 12 focus names are running at 3×+ pace-adjusted relative volume in the first
15 minutes of the session — **DFIN 4.6×, CVNA 3.5×, PRCH 3.4×, PURR 3.3×**. DFIN and CVNA are the
only two also showing price confirmation (+6.4% and +0.7% vs. the prior close); PRCH +2.1%.

**Caveat that changes how this reads:** the upstream focus list is **three sessions stale** — the
newest `focus.md` on `main` is the 2026-10-30 sweep (no `focus.md` was produced for 10-31 or
11-01), so this ranks a Friday watchlist against Monday tape. Treat the ranking as
"what a 10-30 focus list looks like on 11-02", not as a fresh screen.

## Universe

12 names from `daily-screens/2026-10-30/focus.md` (Focus = 2+ stylist lenses or top-5 velocity;
the 10-30 sweep's post-filter universe was 12 names). Full roster below, no exclusions.

## Table — sorted by RVOL desc

RVOL is **session-pace-adjusted intraday RVOL**: cumulative regular-session volume through the
09:45 ET bar ÷ (average daily volume over 10 days × elapsed session fraction, 15/390 min).
Rationale in *Method* below. `Close` is the bridge `market-recap` last trade at 09:46 ET.

| symbol | close | RVOL | bucket | data timestamp |
|---|---:|---:|---|---|
| DFIN | 67.325 | 4.58 | RVOL Required | 2026-11-02 09:46 ET (vol @ 09:45 bar) |
| CVNA | 72.63 | 3.53 | RVOL Required | 2026-11-02 09:46 ET (vol @ 09:45 bar) |
| PRCH | 20.99 | 3.36 | RVOL Required | 2026-11-02 09:46 ET (vol @ 09:45 bar) |
| PURR | 10.57 | 3.32 | RVOL Required | 2026-11-02 09:46 ET (vol @ 09:45 bar) |
| MAX | 14.395 | 2.80 | Liquid | 2026-11-02 09:46 ET (vol @ 09:45 bar) |
| ADT | 9.88 | 2.47 | Liquid | 2026-11-02 09:46 ET (vol @ 09:45 bar) |
| FTAI | 200.02 | 1.72 | Liquid | 2026-11-02 09:46 ET (vol @ 09:45 bar) |
| CROX | 151.68 | 1.26 | Liquid | 2026-11-02 09:46 ET (vol @ 09:45 bar) |
| GKOS | 236.00 | 1.25 | Liquid | 2026-11-02 09:46 ET (vol @ 09:45 bar) |
| GEN | 29.70 | 1.16 | Liquid | 2026-11-02 09:46 ET (vol @ 09:45 bar) |
| BHC | 8.26 | 0.94 | Liquid | 2026-11-02 09:46 ET (vol @ 09:45 bar) |
| INSM | 112.05 | 0.85 | Liquid | 2026-11-02 09:46 ET (vol @ 09:45 bar) |

### Counts

- Focus tickers: **12**
- RVOL Required (RVOL >= 3): **4** — DFIN, CVNA, PRCH, PURR
- Liquid (RVOL < 3): **8** — MAX, ADT, FTAI, CROX, GKOS, GEN, BHC, INSM
- Tickers crossing from below 1 to above 3 during this session: **0 observed** (single snapshot at
  09:45 ET; no prior intraday RVOL reading exists for this list, so no crossing can be asserted).
  Four names are *already* above 3 at the first full read of the day — flagged above as a level,
  not as a crossing.

## Volume detail

| symbol | cum vol (09:30–09:45 ET) | avg daily vol 10d (TV) | raw RVOL (cum ÷ avg10d) | pace RVOL (bucket metric) | chg vs prev close |
|---|---:|---:|---:|---:|---:|
| DFIN | 58,577 | 332,762 | 0.176 | 4.58 | +0.67% |
| CVNA | 1,377,484 | 10,160,131 | 0.136 | 3.53 | +6.42% |
| PRCH | 305,922 | 2,364,012 | 0.129 | 3.36 | +2.09% |
| PURR | 2,158,090 | 16,916,376 | 0.128 | 3.32 | -4.00% |
| MAX | 111,752 | 1,039,259 | 0.108 | 2.80 | -2.34% |
| ADT | 2,615,246 | 27,537,136 | 0.095 | 2.47 | +0.10% |
| FTAI | 127,605 | 1,933,800 | 0.066 | 1.72 | +6.81% |
| CROX | 69,794 | 1,435,450 | 0.049 | 1.26 | +0.77% |
| GKOS | 74,963 | 1,555,380 | 0.048 | 1.25 | -0.67% |
| GEN | 277,189 | 6,191,386 | 0.045 | 1.16 | +1.96% |
| BHC | 224,873 | 6,243,659 | 0.036 | 0.94 | +0.61% |
| INSM | 130,315 | 3,991,469 | 0.033 | 0.85 | -0.47% |

## Method

1. **Window check** — 2026-11-02 is a trading Monday (not a 2026 NYSE closure). Market state
   confirmed `open` by the bridge at 09:46 ET.
2. **Upstream focus list** — pulled `origin/main` of `karizaco/minimax-cloud-outputs`, read
   `daily-screens/2026-10-30/focus.md` (12 names). No `focus.md` exists for 2026-10-31 or
   2026-11-01; those directories are empty of sweep output, so the 10-30 list is the newest
   available. Data date 2026-10-30 (settled close) vs fire date 2026-11-02 — a **3-session lag**,
   carried through the weekend.
3. **Closes** — bridge `market-recap get_quotes`, one batch of 12 symbols, `market_state: open`,
   `as_of` 2026-11-02T14:44–14:46Z. This is the quote source of record.
4. **Intraday volume** — Yahoo chart API, `interval=5m&range=1d`, one call per symbol (12 calls,
   1s spacing). Only regular-session bars dated 2026-11-02 and stamped **09:30, 09:35, 09:40,
   09:45 ET** were summed. Pre-market bars: none returned (0 for every symbol). The live
   in-progress bar (09:46–09:47 ET, volume still 0) was **dropped** for every symbol and is
   noted here; DFIN returned only 3 completed bars (its 09:45 bar had no close/volume yet).
5. **Denominator** — TradingView public scanner `POST https://scanner.tradingview.com/america/scan`,
   column `average_volume_10d_calc` (one full-universe pull, 19,928 rows, filtered locally to the
   12 focus names — the scanner's `name`/`in` filter returns HTTP 400 on this endpoint).
6. **Metric** — the prompt's literal definition (cumulative volume ÷ 10-day average daily volume)
   is reported above as `raw RVOL`. At 15 minutes into a 390-minute session it is mechanically
   ≈1/26 of the pace metric, so the literal `RVOL >= 3` threshold cannot be reached before the
   lunch bell for any name — every stock would sit in Liquid all morning. The **bucket metric is
   therefore the pace-adjusted RVOL** (raw ÷ elapsed session fraction), which is the standard
   "is this name trading hot right now" reading of Sun's RVOL Required tier. Both numbers are
   published; the ranking is identical either way (one is a constant multiple of the other).

## Source health

| source | query | status | result |
|---|---|---|---|
| MCP catalog probe | `probe_mcp.py` | ok | `catalog_ok total=133 finance_tools=0` — no finance MCP registered, as expected |
| bridge `market-recap` | `get_quotes` (12 symbols) | ok | 12/12 found, `market_state: open` |
| TradingView scanner | `POST /america/scan` (19,928 rows, local filter) | ok | 12/12 focus names found with `average_volume_10d_calc` |
| Yahoo chart | `GET /v8/finance/chart/{sym}?interval=5m&range=1d` ×12 | ok | 12/12 returned session bars; no 429, no fetch failures |
| upstream outputs repo | `git fetch origin main` → `daily-screens/` | ok (stale content) | newest `focus.md` = 2026-10-30; nothing for 10-31 or 11-01 |

## Degradation / caveats

- **Upstream focus list is 3 sessions stale.** Cron #09 (daily sweep, 18:30 ET) produced no
  `focus.md` for 2026-10-31 or 2026-11-01. This snapshot therefore ranks a 10-30 watchlist on
  11-02 tape. Names that screened on Friday may no longer be relevant (PURR in particular: the
  10-30 note flagged a 28.4M-share, IV30 112% position, and it is -4.0% today on 3.3× pace
  volume).
- **Single snapshot.** Crossing detection (below 1 → above 3) is not possible from one reading;
  no alert was emitted.
- **TV `volume` column ignored.** The scanner's live volume column disagrees with the Yahoo
  session sum (e.g. ADT 1,144,478 vs 2,615,246; DFIN 5,806 vs 58,577) — it appears to lag the
  session. Yahoo is the sole volume source; TV supplies only the 10-day average denominator.
- **TV `close` ignored** in favour of the bridge last trade (TV close is a mid-session snapshot
  up to a minute stale, e.g. ADT 9.87 vs bridge 9.88).
- **Bucket threshold** uses the pace-adjusted RVOL, as explained under Method. Under the literal
  raw definition the RVOL Required bucket would be **empty (0/12)** and Liquid would hold all 12.
- No symbol was skipped, and no value in this artifact is estimated or carried over from a
  previous session.
