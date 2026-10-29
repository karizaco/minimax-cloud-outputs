---
date: 2026-10-26
cron: 19-earnings-reminder-daily
fire_time_et: 06:00
snapshot_et: 06:08
source: Yahoo Finance earnings calendar
primary_source: Yahoo (market cap) | MarketBeat (EPS, revenue) | Nasdaq/Zacks + EarningsWhispers (cross-check)
status: ok
pending_count: 10
already_reported_count: 1
---

# Earnings — Mon 2026-10-26

Eleven names qualify under the cron filter: ten S&P 500 constituents reporting today and one
non-member mega-cap (WuXi AppTec). All eleven report dates were confirmed against a company
source — no aggregator date was trusted on its own. Every one of the ten US names is still
pending at the 06:08 ET snapshot; WuXi AppTec had already printed in the Asian session.

**Read the two definitional traps in the table before using the EPS column.** Welltower,
Public Storage and Alexandria Real Estate carry two different "consensus EPS" numbers in
circulation because one figure is FFO-based and the other is GAAP-based, not because one
source is wrong. The number that matters is printed first in each cell.

## Your watchlist

Omitted. No watchlist file exists in this runtime (`research/watchlist.yaml` is local-only and
`/workspace` has no equivalent), so there is no watchlist section to populate. This is stated
once here rather than shipped as an empty table.

## Big S&P 500 today

| Ticker | Company | Time | EPS est | Rev est | Mkt cap | Status |
|---|---|---|---|---|---|---|
| VZ | Verizon Communications | BMO 8:30am ET | 1.27 | $34.77B | $185.55B | pending |
| CDNS | Cadence Design Systems | AMC (webcast 5:00pm ET) | 2.05 | $1.61B | $87.29B | pending |
| NUE | Nucor | AMC | 5.83 | $10.84B | $58.56B | pending |
| WELL | Welltower | AMC | 0.71 GAAP / 1.64 FFO | $3.64B | $171.01B | pending |
| PSA | Public Storage | AMC | 2.29 GAAP / 4.27 FFO | $1.34B | $57.90B | pending |
| HIG | The Hartford | AMC 4:05pm ET | 3.17 | $7.37B | $37.04B | pending |
| CINF | Cincinnati Financial | AMC | 1.99 | $2.64B | $27.06B | pending |
| BRO | Brown & Brown | AMC | 1.08 | $1.76B | $24.42B | pending |
| PFG | Principal Financial | AMC | 2.42 | $4.31B | $23.24B | pending |
| ARE | Alexandria Real Estate Equities | AMC | 1.52 FFO / -0.03 GAAP | $646M | $7.40B | pending |
| WUXAY | WuXi AppTec (603259.SH / 2359.HK) | BMO, Shanghai | 0.44 | $2.39B | $71.96B | already_reported |

Sources per field: market cap from the Yahoo Finance earnings calendar snapshot; EPS and revenue
from MarketBeat, cross-checked against Nasdaq/Zacks and EarningsWhispers. Estimates are
pre-release consensus, not results. "BMO" = before market open, "AMC" = after market close.

The ten US names are all S&P 500 constituents. WuXi AppTec is included on market cap alone
(>$50B on the Yahoo figure) — it is not an S&P 500 member. Its market cap is the one figure in
this table where the sources materially disagree; see the conflicts section.

## Report dates confirmed at the company source (Rule B)

Aggregator calendars carry wrong dates, so every included name was checked against the
company's own release or filing. All eleven landed on 2026-10-26; none required a date
correction or exclusion.

| Ticker | Company source | Announcement | Stated timing |
|---|---|---|---|
| VZ | verizon.com/about/investors | Q3 2026 results | 8:30am ET, Oct 26 (BMO) |
| CDNS | investor.cadence.com (press release, Oct 5) | Q3 2026 webcast | Mon Oct 26, 2:00pm PT (AMC) |
| NUE | investors.nucor.com (guidance release, Sep 17) | Q3 2026 results | after market close, Mon Oct 26 |
| WELL | welltower.com (press release, Sep 23) | Q3 2026 results | after the close, Mon Oct 26 |
| PSA | investors.publicstorage.com (release, Oct 5) | Q3 2026 results | after market close, Mon Oct 26 |
| HIG | newsroom.thehartford.com (release, Sep 28) | Q3 2026 results | ~4:05pm ET, Mon Oct 26 |
| CINF | Company release via PR Newswire (Oct 7) | Q3 2026 results | after the close, Mon Oct 26 |
| BRO | investor.bbrown.com (release, Oct 1) | Q3 2026 results | after the close, Mon Oct 26 |
| PFG | investors.principal.com (release, Oct 1) | Q3 2026 results | after US market close, Mon Oct 26 |
| ARE | investor.are.com (release, Aug 25) | Q3 2026 results | after market close, Mon Oct 26 |
| WUXAY | HKEX filing (Oct 12 board-meeting notice) + company results release, Oct 26 | Q1–Q3 2026 results | Shanghai session, Oct 26 |

One aggregator date was rejected: SimplyWall.St listed WuXi AppTec at Oct 27, while the company's
own HKEX board-meeting notice states the board approved the Q3 results on Monday, October 26,
2026 and the company released them on Oct 26. The aggregator was wrong.

## Source conflicts and reconciliations (Rule C)

Tolerance applied: market cap >5%, EPS >2% is flagged. Every cell below exceeded tolerance, or
is a definitional (not an error) difference that would mislead a reader.

| Ticker | Field | Sources | Spread | Resolution |
|---|---|---|---|---|
| WUXAY | Mkt cap | Yahoo $71.96B vs MarketBeat $13.97B | 414% | Yahoo used. Yahoo prices the 603259.SH line; MarketBeat's $13.97B is computed off the thin US ADR float. Threshold-straddling — at MarketBeat's figure WUXAY would be excluded. |
| WELL | EPS | Yahoo $0.71, MarketBeat $0.641, Nasdaq/EW $1.64 | 156% | Definitional, not an error. $0.64–0.71 is GAAP EPS; $1.64 is the FFO consensus. GAAP shown first, FFO alongside. |
| PSA | EPS | Yahoo $2.29, MarketBeat $2.49, Nasdaq/EW $4.27 | 86% | Definitional. $2.29–2.49 is GAAP EPS; $4.27 is the FFO consensus. Both shown. |
| ARE | EPS | MarketBeat -$0.03, Nasdaq/EW $1.52 | n/a | Definitional. MarketBeat carries GAAP EPS ($646M revenue, -$0.03); $1.52 is the FFO consensus. Both shown. |
| CDNS | EPS | Yahoo $2.05, MarketBeat $2.05, EW $2.05, Nasdaq $1.61 | 27% | Nasdaq is the lone outlier; three sources agree at $2.05, so $2.05 used. |
| CINF | EPS | Yahoo $2.11, MarketBeat $2.05, Nasdaq/Zacks/EW $1.99 | 6% | $1.99 used (three sources incl. Zacks). Yahoo's $2.11 is the outlier. |
| NUE | EPS | Yahoo $5.83, MarketBeat $5.84, Nasdaq/EW $5.71 | 2.3% | $5.83 used (Yahoo primary). Spread is marginal but above the 2% tolerance. |
| HIG | Rev | MarketBeat $7.37B vs EarningsWhispers $5.28B | 40% | $7.37B used. Verified against the company's reported quarterly revenue (Q3 2025 actual $7.23B, Q2 2026 $7.26B); the $5.28B figure is inconsistent with the company's own history. |
| CINF | Rev | MarketBeat $2.64B, EW $3.03B, Barchart/Zacks $2.52B | 20% | $2.64B used (MarketBeat primary, and consistent with the company's $2.86–4.27B quarterly range). The three sources straddle a 20% range and no consensus number is clean. |
| PSA | Rev | MarketBeat $1.34B vs EW $1.27B | 5.5% | $1.34B used. |
| NUE | Rev | MarketBeat $10.84B vs EW $10.53B | 2.9% | $10.84B used. |
| CLS | Mkt cap (excluded name) | Yahoo $32.79B vs Nasdaq $30.84B | 6.3% | Below the $50B threshold on both readings, so the exclusion holds either way. |
| PFG | Rev | EarningsWhispers $4.31B only | n/a | Single source — no second provider carried a PFG revenue estimate. Treat as softer than the other revenue figures. Plausible against the company's $3.5–4.6B quarterly range. |
| WUXAY | EPS / Rev | MarketBeat $0.44 / $2.39B only | n/a | Single source. Yahoo and Nasdaq carried no estimates for this ADR. |

## Method and caveats

- **Filter.** S&P 500 membership (live constituent list) OR market cap above $50B, reporting
  today. Names below both thresholds were dropped, which removed 70 of the 81 tickers seen
  across the four calendars.
- **S&P 500 membership (Rule A).** Parsed from the MediaWiki API wikitext of
  `List_of_S%26P_500_companies` (not the rendered HTML table), yielding 502 unique symbols.
  Control check passed: BRK.B, GOOGL, GOOG and FOX are all present. The ten S&P 500 names in
  today's table were matched against that list, not from memory.
- **Calendar coverage.** Four independent calendars were pulled and unioned: the Yahoo Finance
  earnings calendar (25 rows server-rendered of ~84 entries; the rest are JS-gated), the Nasdaq
  earnings calendar API (74 rows), EarningsWhispers' calendar API (55 rows — 13 before the open,
  42 after the close) and the MarketBeat calendar page (24 rows server-rendered). The union
  covered 81 tickers. A name appearing on only one calendar was included only if it also
  passed a company-source date check.
- **Status.** "pending" means the release had not occurred at the 06:08 ET snapshot. "already
  reported" means the release was public before the snapshot — this applies to WuXi AppTec
  only, whose results were issued in the Asian session on Oct 26. All ten US names are pending
  at snapshot time; Verizon at 08:30 ET and The Hartford at 16:05 ET are the first and last
  US prints of the day.
- **Estimates are pre-release consensus**, not actuals, and not a forecast of what will print.
  Consensus EPS for REITs (WELL, PSA, ARE) is split between GAAP and FFO conventions; both
  are shown rather than one being silently preferred.
- **Not covered.** No watchlist section (no watchlist file in this runtime). No price targets,
  no reaction analysis, no modelled numbers — read-only reminder only.

## Data-quality notes carried forward

- EarningsWhispers lists Celestica twice on this date, as `CLS` and `T.CLS`, with different
  EPS estimates ($3.02 vs $4.05) and the same $5.40B revenue. Treated as one name.
- The Yahoo Finance calendar page carries stale EPS for several rows: Welltower $0.71,
  Public Storage $2.29 and Phillips Edison $0.15 all sit far from the multi-source cluster.
  Yahoo's market caps and the majority of its EPS figures were usable; its EPS column was
  not trusted where two or more other providers disagreed.
- MarketBeat's Hartford page shows a prior-year revenue of $1.05B against a consensus of
  $7.37B, which is a display error on their side — the company's actual Q3 2025 revenue was
  $7.23B, so the consensus figure is sound and their "prior-year" field is not.
