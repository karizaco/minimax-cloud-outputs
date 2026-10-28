# Daily screener sweep — 2026-10-28

The 18:30 ET sweep produced **426 equity candidates** across five stylist screens, of which
**12 reach the Focus tier** and **8 reach Tier-A**
(≥3 distinct stylists). The Tier-A list is **NTSK, DXC, TENB, QLYS, IOVA, KNSA, PRME, SOFI**, and it splits cleanly in two:
**NTSK, DXC, TENB, QLYS and IOVA** are relative-strength and velocity names carried by the Qullamägi and
peoplewish books — NTSK has the highest 14-day velocity in the whole sweep at +35.9% — while **KNSA, PRME and
SOFI** are breakout names that also cleared the CANSLIM growth screen. Three of the eight continued higher on
10-28, PRME best of them at +23.2% and KNSA +6.7%.

The regime is **no size cut**: only 40% of the five index ETFs are above their
20-day moving average, but 65.9% of the 905 large caps above $10B
are, so the index weakness is narrow rather than broad, and the VIX/VIX3M ratio of 0.88
shows no front-end stress premium.

**Read the date column carefully.** The shibui-side of the sweep is built on the **2026-10-27** close —
shibui had not yet ingested 2026-10-28 when this cron fired, so every screen metric (ADR%, relative strength,
velocity, moving averages, volume) describes Tuesday's settled session. The 10-28 columns are the official
4:00 PM prints pulled separately from Nasdaq and are there so you can see what each candidate did *today*.

## Deviations and caveats

- **shibui is one session behind (T+1).** Preflight `MAX(date)` resolved to 2026-10-27 against a 2026-10-28 cron date.
  This is the skill's documented normal case; the signal is still valid for next-session execution.
- **Five defects in the skill's own published `scripts/screen.py` sweep SQL were found and repaired.**
  Three are hard failures: the stockbee CTE list is missing a comma, the Qullamägi RS screen references
  `close_252`/`close_126`/`close_63`/`close_21` while aliasing them `close_*d_ago`, and that same query's
  `UNION ALL` mixes CTEs of different column arity. Two are silent-corruption failures: the Qullamägi 9-month
  lookback window is shorter than the 252-trading-day `LAG` it needs (the entire RS book came back empty and
  looked like a quiet tape), and in the stockbee `UNION ALL` the output column names are inherited from the first
  branch, so the EP9M rows published their close-location-in-range value under the header `chg_pct` and the
  anticipation rows published trend-intensity under `volume` — SMCI's apparent "+93.9%" move was really a
  93.9% close-location. Every branch now emits an explicitly named, identical column set, and each candidate's
  session change is recomputed from the price series rather than taken from whichever screen found it.
- **CANSLIM was sourced from shibui, not TradingView.** TradingView's scanner returns `null` for
  `earnings_growth_quarterly_yoy` and `sales_growth_quarterly_yoy` on every US name, so the spec's filter can never
  match there. The equivalent screen was rebuilt on `fundamentals_derived_quarterly.eps_growth_yoy` and
  `revenue_growth_yoy` (both decimal fractions — 0.25 means 25%), keeping every other spec criterion intact.
- **The $300M pre-filter floor was enforced strictly.** 67 candidates were dropped because
  they carry no market-cap row — 52 ETFs (mostly 2x/3x leveraged products), 14 preferred shares and one microcap.
  Leveraged ETFs were the worst offenders: they clear momentum and volume screens purely through leverage, and two
  of them (TSLG, TSLL, both 2x TSLA) had reached Tier-A before the floor was applied.
- **A duplicate-safe breadth query was used.** `shibui.valuation` keeps multiple rows per symbol, so the
  large-cap breadth population was computed latest-row-first via `QUALIFY` rather than by joining on date directly.
- **Finviz was unreachable** (HTTP 403 Cloudflare from both curl and web_fetch), and Yahoo's JSON endpoints are
  HTTP 429 from this egress, so neither tier-2 fallback in the skill's chain was usable.

## Tier-A — 8 names with ≥3 distinct stylists

| Ticker | Close 10-27 | Chg 10-27 | Close 10-28 | Chg 10-28 | ADR% 20d | Vel 14d | Styl | Origins |
|---|---|---|---|---|---|---|---|---|
| **NTSK** | $26.15 | +3.73% | $26.52 | +1.41% | 6.1 | 35.9 | 3 | RS leader, 5d gainer, ADR + velocity, theme→group leader |
| **DXC** | $15.84 | -2.82% | $16.09 | +1.58% | 5.1 | 31.8 | 3 | RS leader, ADR + velocity, theme→group leader |
| **TENB** | $48.65 | +0.91% | $48.72 | +0.14% | 5.5 | 24.9 | 3 | RS leader, ADR + velocity, theme→group leader |
| **QLYS** | $227.90 | +1.22% | $223.52 | -1.92% | 5.0 | 17.0 | 3 | RS leader, ADR + velocity, theme→group leader |
| **IOVA** | $14.58 | +5.81% | $14.81 | +1.58% | 6.5 | 12.9 | 3 | RS leader, ADR + velocity, theme→group leader |
| **KNSA** | $89.20 | +22.23% | $95.18 | +6.70% | 4.3 | — | 3 | 4% breakout, gap up (EP), CANSLIM |
| **PRME** | $4.35 | +20.50% | $5.36 | +23.22% | 9.8 | — | 3 | 4% breakout, volume breakout, theme→group leader |
| **SOFI** | $16.40 | +13.42% | $17.14 | +4.51% | 3.9 | — | 3 | 4% breakout, EP9M volume, gap up (EP), CANSLIM |

10 names cleared the ≥3-stylist bar; the list is capped at the skill's documented size of 8.

## Focus — Master names with ≥2 stylists, plus the top-5 velocity names

| Ticker | Close 10-27 | Chg 10-27 | Close 10-28 | Chg 10-28 | ADR% 20d | Vel 14d | Styl | Origins |
|---|---|---|---|---|---|---|---|---|
| **NTSK** | $26.15 | +3.73% | $26.52 | +1.41% | 6.1 | 35.9 | 3 | RS leader, 5d gainer, ADR + velocity, theme→group leader |
| **DXC** | $15.84 | -2.82% | $16.09 | +1.58% | 5.1 | 31.8 | 3 | RS leader, ADR + velocity, theme→group leader |
| **TENB** | $48.65 | +0.91% | $48.72 | +0.14% | 5.5 | 24.9 | 3 | RS leader, ADR + velocity, theme→group leader |
| **SMCI** | $35.09 | +7.34% | $35.81 | +2.05% | 5.5 | -21.9 | 3 | EP9M volume, ADR + velocity, CANSLIM |
| **QLYS** | $227.90 | +1.22% | $223.52 | -1.92% | 5.0 | 17.0 | 3 | RS leader, ADR + velocity, theme→group leader |
| **IOVA** | $14.58 | +5.81% | $14.81 | +1.58% | 6.5 | 12.9 | 3 | RS leader, ADR + velocity, theme→group leader |
| **SDGR** | $26.72 | +9.06% | $30.87 | +15.53% | 7.7 | -2.1 | 3 | RS leader, ADR + velocity, volume breakout |
| **KNSA** | $89.20 | +22.23% | $95.18 | +6.70% | 4.3 | — | 3 | 4% breakout, gap up (EP), CANSLIM |
| **PRME** | $4.35 | +20.50% | $5.36 | +23.22% | 9.8 | — | 3 | 4% breakout, volume breakout, theme→group leader |
| **SOFI** | $16.40 | +13.42% | $17.14 | +4.51% | 3.9 | — | 3 | 4% breakout, EP9M volume, gap up (EP), CANSLIM |
| **LQDA** | $45.44 | +3.89% | $45.72 | +0.62% | 15.9 | 70.3 | 2 | 5d gainer, ADR + velocity |
| **FIGS** | $20.48 | -1.68% | $20.66 | +0.90% | 5.5 | 45.7 | 2 | RS leader, ADR + velocity |

## Top movers — 2026-10-27 4% breakouts, with their 2026-10-28 follow-through

| Ticker | Close 10-27 | Chg 10-27 | Volume 10-27 | Close 10-28 | Chg 10-28 |
|---|---|---|---|---|---|
| **BRAI** | $3.31 | +56.13% | 51,785,552 | $3.60 | +8.76% |
| **CRML** | $8.13 | +27.43% | 20,283,620 | $7.79 | -4.18% |
| **ENVX** | $3.35 | +25.00% | 19,705,860 | $3.52 | +5.07% |
| **HRI** | $156.06 | +22.76% | 2,040,012 | $166.24 | +6.52% |
| **MFIC** | $10.26 | +22.73% | 7,926,076 | $10.24 | -0.19% |
| **KNSA** | $89.20 | +22.23% | 2,320,725 | $95.18 | +6.70% |
| **PRME** | $4.35 | +20.50% | 8,824,720 | $5.36 | +23.22% |
| **ZURA** | $4.27 | +19.94% | 5,089,326 | $4.35 | +1.87% |
| **CHRN** | $17.49 | +19.55% | 247,972 | $17.02 | -2.69% |
| **NB** | $3.41 | +17.59% | 4,379,611 | $3.51 | +2.93% |
| **BETR** | $20.80 | +17.38% | 1,310,627 | $21.54 | +3.56% |
| **USAR** | $10.40 | +16.72% | 21,291,339 | $10.48 | +0.77% |

The 10-27 breakout list is the Stockbee book's raw output. The 10-28 column is the reason this column exists:
several of Tuesday's breakouts continued, which is what makes the next session's entry decision rather than a
theoretical one.

## Volume breakout — relative volume ≥2× with a 3%+ move (TradingView, live 10-28)

| Ticker | Close 10-28 | Chg 10-28 | Rel volume 10d | Volume |
|---|---|---|---|---|
| **BRAI** | $3.60 | +8.76% | 9.64 | 56,767,913 |
| **BLCO** | $20.41 | +15.81% | 8.37 | 4,106,216 |
| **AXGN** | $49.25 | +31.47% | 7.24 | 9,288,622 |
| **WEN** | $7.07 | +15.15% | 6.51 | 34,816,622 |
| **KIDS** | $30.80 | +29.30% | 6.14 | 1,794,232 |
| **GENB** | $15.38 | +16.43% | 5.22 | 3,927,790 |
| **LCII** | $97.36 | +8.37% | 4.93 | 2,535,964 |
| **ICLR** | $214.16 | +17.04% | 4.42 | 3,947,027 |
| **DIN** | $34.72 | +8.47% | 4.26 | 1,860,861 |
| **BHC** | $6.97 | +10.46% | 4.14 | 7,980,774 |

TradingView's `average_volume_10d_calc` runs 6-16% tighter than a true trailing-10 average, so these relative
volumes are overstated by roughly that margin — read them as a ranking, not a ratio.

## Screen counts

| Stylist | Candidates | Sub-screens hit |
|---|---|---|
| peoplewish (Riffle) | 176 | ADR + velocity (176) |
| Jeff Sun (CFTe) | 168 | volume breakout (58), CANSLIM (111) |
| Stockbee (Bonde) | 61 | 4% breakout (28), EP9M volume (34), anticipation (coil) (1) |
| Qullamägi | 54 | RS leader (43), gap up (EP) (3), 5d loser (5), 5d gainer (4) |
| Hernandez | 43 | theme→group leader (43) |

## Method

The sweep follows the skill's procedure: one shibui preflight resolves the latest available date, then three
shibui sweeps (Stockbee group, Qullamägi group, peoplewish) run as batched `UNION ALL` queries, complemented by
a shibui CANSLIM query, a TradingView scanner pass for sector/industry relative strength and the volume-breakout
cross-check, and a shibui breadth/regime query. Results are merged in memory, tiered into Master (≤200),
Stalk (≤50), Focus (≤12) and Tier-A (≤8), and tagged with setup patterns and skip-rule flags. Stylist buckets
follow the skill's origin map, with the TradingView volume-breakout screen folded into Jeff Sun (his volume
proxy), which yields the five stylist buckets the tiering thresholds are calibrated for.

Not applicable at 18:30 ET and therefore not run: the 3:55 PM reversal-bullish screen (15:30-16:00 ET window),
the pre-market gapper (09:00 ET), the live intraday RVOL re-rank (09:45-11:15 ET), and the Sunday-only IPO and
high-short-float refreshes.

## Source health

| Source | Endpoint / query | Status |
|---|---|---|
| shibui MCP (bridge) | https://mcp.shibui.finance/mcp — `stock_data_query` | ok — 12 queries |
| shibui preflight | `SELECT MAX(date) ... WHERE date <= '2026-10-28'` | ok — latest_date 2026-10-27 |
| shibui sweeps | stockbee / qullamaggie / peoplewish UNION ALL | ok — after repairing 5 defects in the published templates |
| shibui breadth | large-cap breadth + index ATR extension | ok — 905-name large-cap proxy |
| shibui CANSLIM | `fundamentals_derived_quarterly` growth join | ok — 111 names |
| shibui theme stocks | `general_info` GICS sector / industry group | ok — 43 names |
| shibui enrichment | per-candidate stats, 4 chunks of 140 | ok — 530 candidates enriched |
| TradingView scanner | POST https://scanner.tradingview.com/america/scan | ok, degraded — growth columns null, CANSLIM rebuilt on shibui |
| CBOE delayed quotes | cdn.cboe.com/api/global/delayed_quotes/quotes/_VIX.json | ok — VIX 16.91 |
| CBOE delayed quotes | cdn.cboe.com/api/global/delayed_quotes/quotes/_VIX3M.json | ok — VIX3M 19.22 |
| Nasdaq public quote API | api.nasdaq.com/api/quote/{{SYM}}/info | ok — 56/56 names |
| Finviz screener | finviz.com/screener.ashx | failed — HTTP 403 Cloudflare challenge (curl and web_fetch) |
| Yahoo Finance JSON | query1/query2 chart + screener | failed — HTTP 429 rate-limited from this egress |

## Files

All 27 artifacts live in `daily-screens/2026-10-28/`. `daily-sweep.md` is this file and
`daily-sweep.csv` carries the same candidate set in tabular form (tier, both session closes, ADR, velocity,
stylist origins, setup tags and skip flags). Alongside it: the five per-stylist books (`stockbee.md`,
`qullamaggie.md`, `jeff-sun.md`, `ariel-hernandez.md`, `peoplewish.md`), the four tier files (`master.md`,
`stalk.md`, `focus.md`, `tier-a.md`), the two parabolic books (`short-candidates.md`,
`long-reversal-candidates.md`), `breadth.md`, `_summary.md` (the digest the pre-market brief reads) and
`_regime.json` (the machine-readable regime payload). A CSV sits beside every tier and per-stylist Markdown.
