---
artifact: breadth-snapshot
cron: "#10 stock-screener-breadth-snapshot"
fire_time_et: "2026-11-04 14:00:54 ET"
schedule: "0 14 * * 1-5 America/New_York"
data_date: "LIVE layer = 2026-11-04 intraday (quotes stamped 14:50 ET); shibui breadth + ATR layer = 2026-11-03 settled close (shibui is T+1)"
breadth_universe: "NYSE/NASDAQ/AMEX, market cap > $10B, 905 names (shibui settled 905/905). Live layer resolves 902/905 on TradingView; BF-B, BRK-B, MOG-A have no TV row under their shibui ticker (TV uses BRK.B / BF.B / MOG.A)"
vix_quote_time: "2026-11-04 14:50:16 ET"
vix_source: "MCP bridge market-recap get_quotes (Yahoo keyless, primary); corroborated by CBOE delayed-quote CDN (15-min delayed feed, 13:49:31 ET)"
vix: 16.99
vix3m: 19.06
vix_vix3m_ratio: 0.8914
regime: "size_cut_pct=0 | uncertainty=false | late_cycle=false"
cross_reference: "end-of-day counterpart: daily-screens/2026-11-04/breadth.md (cron #09, 18:30 ET)"
sources: "TradingView america scanner (live) | shibui via MCP-over-HTTP bridge (settled) | CBOE delayed-quote CDN | MCP bridge market-recap"
---

# Breadth / regime snapshot — 2026-11-04, 14:00 ET fire

**This is the INTRADAY read.** It is not the end-of-day read. Cron #09 fires at 18:30 ET and writes
`daily-screens/2026-11-04/breadth.md` from the settled daily close; the two files are *supposed* to
differ, and today they will differ in breadth, in the volatility quote time, and in the sector table.

## Headline

Breadth improved sharply intraday and volatility crushed, but the improvement is a **rotation, not a
broad repair**. Large-cap breadth went from 63.98% above its 20-DMA at the 2026-11-03 close to
**68.63% live**, with 642 of 902 large caps advancing. At the same time the VIX fell 18.4% to 16.99
and the VIX3M to 19.06 — a 0.891 ratio, deep contango.

The rotation is the story: **energy was sold (−5.10% in XLE, 3.2% of energy names above their
20-DMA) while healthcare, staples and consumer cyclicals ripped**. Equal-weight RSP (+1.82%) is
essentially matching cap-weight SPY (+1.77%), so this is not a mega-cap-only squeeze. But 615
US-listed names fell 5% or more against 1,113 that rose 5% or more — the tape is violently
bifurcated, and dispersion is the risk, not the index level.

No regime flag fires: **size_cut_pct = 0, uncertainty = false, late_cycle = false.**

## Breadth — large caps, market cap > $10B

| Measure | Settled 2026-11-03 | Live 2026-11-04 ~14:50 ET | Change |
|---|---:|---:|---:|
| % above 20-DMA (905-name universe) | 63.98% | **68.63%** | +4.65 pp |
| % above 50-DMA (905-name universe) | 60.00% | **64.86%** | +4.86 pp |
| Advancing / declining (large caps) | — | 642 / 260 | 2.47 : 1 |
| Index ETFs above their 20-DMA | 2 of 5 | **3 of 5** | +1 |
| Index ETFs above their 50-DMA | 1 of 5 | **3 of 5** | +2 |

Settled figures are shibui's own (905/905 names). Live figures are the TradingView scanner on the
same 902 names — one universe, two dates. TradingView's SMA20/SMA50 are live-updated (they include
the in-progress close), verified exactly: TV SPY SMA20 = 767.6050 = mean(19 settled closes through
2026-11-03 + live 767.43); shibui SPY SMA20 = 768.0945 = mean(20 settled closes) — both to 4 dp.

### Breadth by sector (live, % above 20-DMA, same 905-name universe)

Sorted descending; left pane ranks 1–10, right pane ranks 11–20.

| Sector (1–10) | Above 20-DMA | | Sector (11–20) | Above 20-DMA |
|---|---:|---|---|---:|
| Consumer Durables | 100.0% (21/21) | | Process Industries | 70.8% (17/24) |
| Health Services | 100.0% (18/18) | | Distribution Services | 61.5% (8/13) |
| Health Technology | 92.8% (77/83) | | Communications | 58.8% (10/17) |
| Consumer Non-Durables | 92.1% (35/38) | | Non-Energy Minerals | 57.6% (19/33) |
| Consumer Services | 91.7% (33/36) | | Producer Manufacturing | 50.0% (26/52) |
| Commercial Services | 88.0% (22/25) | | Technology Services | 49.5% (47/95) |
| Finance | 87.4% (160/183) | | Industrial Services | 36.7% (11/30) |
| Retail Trade | 86.1% (31/36) | | Electronic Technology | 29.8% (28/94) |
| Transportation | 78.6% (22/28) | | **Energy Minerals** | **3.2% (1/31)** |
| Utilities | 76.7% (33/43) | | Miscellaneous | 0.0% (0/2) |

Energy is the outlier in both directions — **only 1 of 31 energy names is above its 20-DMA**, and
Electronic Technology is at 29.8%. These two sectors are the whole rotation.

## Index levels and moving averages (live)

| Symbol | Last | Day | vs 20-DMA | vs 50-DMA |
|---|---:|---:|---|---|
| SPY | 767.67 | +1.77% | above (+0.01%) | above |
| RSP (equal weight) | 223.245 | +1.82% | above | above |
| QQQ | 693.67 | +1.22% | **below** | below |
| QQQE (NDX equal weight) | 117.47 | +1.31% | **below** | below |
| IWM | 283.87 | +1.46% | above | above |
| DIA | 532.37 | +2.96% | above | above |

**SPY is 0.01% above its own live 20-DMA** — it crossed back above intraday and is sitting on the
line. RSP/SPY spread is +0.05 pp, i.e. the equal-weight tape is fractionally *ahead* of the
cap-weight tape, which is what a genuine rotation looks like. Nasdaq 100 is still the laggard
(QQQ, QQQE and the NDX all remain below both moving averages), so this is a broad-market advance
with tech still in repair.

CBOE index levels, 15-min delayed (13:46:35 ET): SPX 7,697.17 (+1.69%), DJIA 53,294 (+2.91%),
NDX 28,494.56 (+1.12%), RUT 2,854.86 (+1.51%).

## Volatility

**One pair is used everywhere in this document: VIX 16.99, VIX3M 19.06, ratio 0.891.**

| Measure | Value | Prior close | Change |
|---|---:|---:|---:|
| VIX | **16.99** | 20.83 | −18.43% |
| VIX3M | **19.06** | 21.27 | −10.39% |
| VIX / VIX3M | 0.891 | 0.980 | contango |

Quote time 2026-11-04 14:50:16 ET, MCP bridge `market-recap get_quotes` (Yahoo keyless, primary).
Corroboration: CBOE delayed-quote CDN served VIX 16.98 / VIX3M 19.06 at 13:49:31 ET — the same
instrument from a 15-minute-stale feed, consistent to 0.01. The VIX intraday range was 19.22 high /
16.67 low, so the level is not a stale print sitting at the close of a spike.

The ratio at 0.891 is textbook contango and puts `uncertainty = false` (the spec's band is
VIX/VIX3M > 1.0). There is **no November 2026 FOMC meeting** — the last decision was 27–28 October
and the next is 8–9 December — so this volatility crush is not an event-day artifact.

## ATR extension (true, vs 252-session median ATR%)

The skill's emitted `atr_252d_avg` is degenerate (its window runs over a CTE already filtered to a
single date, so it collapses to `atr_14` and `extension_pct` is really just distance from the
50-DMA). These are recomputed with a real 252-session `MEDIAN(atr_pct)` window, on the 2026-11-03
settled bars:

| Symbol | Close 11-03 | 50-DMA | Extension | ATR% now | 252d median ATR% | Extension multiple |
|---|---:|---:|---:|---:|---:|---:|
| SPY | 754.35 | 767.04 | −1.65% | 1.038% | 1.081% | −1.53× |
| RSP | 219.26 | 214.96 | +2.00% | 0.948% | 1.040% | +1.92× |
| QQQ | 685.28 | 723.93 | −5.34% | 1.864% | 1.613% | −3.31× |
| QQQE | 115.95 | 119.68 | −3.12% | 1.385% | 1.295% | −2.41× |
| IWM | 279.79 | 283.49 | −1.31% | 1.352% | 1.673% | −0.78× |

Every index except RSP sits **below** its own 50-DMA, and the most stretched (QQQ, −3.31×) is the
one that rallied today from the deepest hole. No index is more than +6× its historical ATR
extension, so `late_cycle = false` — but note that all five multiples are *negative*, meaning this
market has not recovered its 50-DMA at all. A `late_cycle` flag computed over an empty collection
would read the same way; this one is computed on five real rows.

## Sector rotation

Day change is the live TradingView print (~14:50 ET). The 1M and 3M relative-strength columns are
shibui's settled daily bars through 2026-11-03, calendar-anchored, with SPY as the benchmark.

| Sector | Today | 1M RS vs SPY | 3M RS vs SPY |
|---|---:|---:|---:|
| XLV Health Care | +2.73% | **+12.72 pp** | **+13.86 pp** |
| XLP Staples | +3.75% | +12.44 pp | +5.26 pp |
| XLY Cons. Discretionary | +4.61% | +8.61 pp | −0.31 pp |
| XLF Financials | +3.05% | +8.90 pp | +0.11 pp |
| XLRE Real Estate | +2.90% | +8.99 pp | −2.90 pp |
| XLB Materials | +2.16% | +9.62 pp | +3.54 pp |
| XLU Utilities | +0.66% | +11.00 pp | −1.68 pp |
| XLK Technology | +0.20% | −9.67 pp | −0.42 pp |
| XLC Communication | +3.68% | −6.06 pp | −8.45 pp |
| XLI Industrials | −1.09% | +2.79 pp | −6.03 pp |
| **XLE Energy** | **−5.10%** | +8.13 pp | **+13.86 pp** |

The shape is unambiguous: healthcare and staples lead on every horizon, technology and
communication services lag on every horizon, and **energy was today the single most-sold sector
despite having the best 3-month relative strength of the group.** That is a violent unwind of the
one trade that had been working.

Note the source split: TradingView's own `Perf.3M` column anchors differently and reads XLE at
+8.37% against shibui's +13.42% (SPY −0.33% vs −0.44%). The table above uses shibui only for the
multi-month columns so that one source owns each field.

## Market-wide advance / decline

Computed from the TradingView scanner across **all 6,091 US-listed common stocks and ADRs**
(NYSE/NASDAQ/AMEX, `type` in {stock, dr}) at ~14:50 ET:

| Bucket | Count |
|---|---:|
| Advancing | 4,016 |
| Declining | 1,917 |
| Unchanged | 158 |
| **A/D ratio** | **2.09** |
| Up ≥ 5% | 1,113 |
| Down ≤ −5% | 615 |

A 2.09 A/D ratio is a genuinely strong tape. But **1,728 names moved 5% or more in one direction** —
roughly 28% of the listed market — in a single session. That is the signature of a catalyst-driven
bifurcation, not a calm grind, and it is the reason dispersion matters more than the index level
today.

## What moved, and why

Largest movers in the 905-name large-cap universe, all cross-checked against the CBOE delayed-quote
CDN (agreement within 0.15 pp on 10 of 10):

| Movers | Move | Read |
|---|---|---|
| MDLN | +16.78% | Health technology leads the healthcare bid |
| SWK | +16.17% | Consumer durables |
| XYZ | +15.70% | Commercial services |
| ZBH | +15.11% | Health services |
| PFGC | +14.93% | Transportation |
| FIS | **−24.23%** | Q3 adj. EPS $1.61 beat, but **2026 guidance trimmed** + CFO transition announced |
| STRL | −21.69% | Levered MSTR-linked ETF — the AI-risk unwind |
| INIO | −20.51% | Producer manufacturing |
| UNM | −18.08% | Financials |
| DDOG | −14.95% | Technology services |

The macro backdrop for the session: the **Democratic midterm sweep** of both chambers was confirmed
and President Trump accepted the results, easing the policy-uncertainty discount; AAPL (+6.29%) hit
an all-time high above a $5 trillion market cap after its Nov-2 fiscal-Q4 beat; and oil fell ~2.3%
as hopes grew for a diplomatic resolution to the Middle East war, which is what took XLE down 5%.

## Regime

| Flag | Value | Rule |
|---|---|---|
| `size_cut_pct` | **0** | 50 when index < 20-DMA **and** breadth < 40% |
| `uncertainty` | **false** | VIX/VIX3M > 1.0 (actual 0.891) |
| `late_cycle` | **false** | any index > 6× its 252-session ATR extension |

The settled 2026-11-03 read had `index_below_20sma = true` (only 2 of 5 index ETFs above their
20-DMA). Live, that flips to 3 of 5 — **the index is no longer in a sub-20-DMA posture.** The size-cut
rule never triggered on either basis because breadth was 64–69%, far above the 40% threshold.

So: no regime flag fires, and the reason is that the two offsetting conditions are cancelling —
the index has recovered off its 20-DMA, but not one index is extended at all, and volatility term
structure is in healthy contango. This is a *recovering* tape, not a *stretched* one.

## Source health

| Source | Used for | Status |
|---|---|---|
| MCP bridge `market-recap get_quotes` | VIX, VIX3M, SPY/QQQ/RSP/IWM/QQQE spot + prior close | ok — as_of 2026-11-04 18:50:16Z; all five prior closes match shibui's 2026-11-03 exactly |
| MCP bridge `shibui stock_data_query` | settled breadth, ATR extension, sector RS, universe list | ok — 6 calls, all returned; latest session 2026-11-03 (T+1) |
| TradingView america scanner | live closes, changes, SMA20/SMA50, breadth, A/D | ok — 6,091 market-wide rows, 902/905 large caps; liveness re-proved by a second pull |
| CBOE delayed-quote CDN | index levels, spot cross-checks | ok — 15-min delayed feed; timestamps 13:46–13:49 ET |
| `probe_mcp.py` | MCP availability | `catalog_ok total=135 finance_tools=0` — no finance MCP registered; the bridge is the path |
| FOMC calendar (federalreserve.gov) | event context | ok — **no November 2026 meeting** |

Known gaps and caveats:

- **CBOE is a 15-minute delayed feed.** Its prints are stamped 13:46–13:49 ET while the TradingView
  layer is live at ~14:50 ET. Every table labels which layer it came from.
- **3 of 905 universe names did not resolve live** (BF-B, BRK-B, MOG-A). TradingView indexes those
  share classes as BRK.B / BF.B / MOG.A. The live percentages are therefore computed on 902 names and
  the settled percentages on 905 — a 0.3% denominator difference, not a definition change.
- **The two breadth columns use different MA bases by construction** (shibui's 20-DMA is settled
  through 2026-11-03; TradingView's is live-updated). The basis gap was measured, not assumed: for
  SPY it is 0.65 index points, because the basis swap is worth `(today's price − yesterday's close)/20`.
  The +4.65 pp breadth move is a price effect, not a basis effect.
- **No live advance/decline total exists on any standard feed** (Nasdaq's `marketmovers` payload
  carries no A/D totals). The A/D figures here are computed from the TradingView scanner's own
  `change` column across all 6,091 listed names, which is a first-party computation rather than a
  published vendor total.
- shibui remains **T+1**: its newest bar is 2026-11-03, so the ATR-extension and multi-month
  relative-strength columns describe the prior session. The intraday columns do not.

## Method

The canonical breadth SQL was taken from the skill's own
`scripts/screen.py::emit_breadth_sql()` rather than retyped, and run against the latest available
session (2026-11-03). The live layer was built on the TradingView `america` scanner with an explicit
`sort` by name and a single wide range, per the paging trap. Two skill defects were repaired before
the numbers were published, and both are recorded in `_regime-intraday.json`:

1. `compute_regime()` reads `row["symbol"]` while `emit_breadth_sql()` emits `ticker`, so
   `atr_extensions` came back empty and `late_cycle` was hard-wired to `False` regardless of the
   data. The key is normalised before the call.
2. `atr_252d_avg` is computed over a CTE filtered to a single date, so its window holds one row.
   A separate query with a real 252-session window supplies the ATR extension multiples.

The regime dict was produced by calling the skill's own `compute_regime()`, so the artifact and the
`_regime-intraday.json` sidecar cannot drift apart.
