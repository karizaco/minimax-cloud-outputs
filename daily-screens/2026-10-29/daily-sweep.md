# Daily screener sweep — 2026-10-29

The 18:30 ET sweep produced **456 equity candidates** after the pre-filter floor, of
which **12 reach the Focus tier** and **4 reach Tier-A** (≥3 distinct stylists).
The Tier-A list is **GMAB, SDGR, PRME, FIGS** — and all four sit in Health Care, which is
not a coincidence: IBB and XLV are two of the three strongest themes in the sector
table, and the 10-28 breakout book was overwhelmingly a biotech-and-medtech tape. GMAB carries the
strongest convergence in the sweep (4 stylists, 5 origins) after a Phase 3 head-and-neck readout that
halved the death risk versus Keytruda alone.

**Read the date column carefully.** The shibui side of the sweep is built on the **2026-10-28** close —
shibui had not yet ingested 2026-10-29 when this cron fired, so every screen metric (ADR%, relative
strength, velocity, moving averages, volume) describes Wednesday's settled session. The 10-29 columns are
the official 4:00 PM prints pulled separately from Nasdaq and are there so you can see what each candidate
did *today* — and that column is the story: **three of the four Tier-A names reversed on 10-29**, and the
market rotated hard out of technology into healthcare and defensives after Alphabet and Caterpillar
missed on AI capex.

## Deviations and caveats

- **shibui is one session behind (T+1).** Preflight `MAX(date)` resolved to 2026-10-28 against a
  2026-10-29 cron date. This is the skill's documented normal case; the signal is still valid for
  next-session execution.
- **Five defects in the skill's own published `scripts/screen.py` sweep SQL were found and repaired.**
  Three are hard failures: the stockbee CTE list is missing a comma, the Qullamägi RS screen references
  `close_252`/`close_126`/`close_63`/`close_21` while aliasing them `close_*d_ago`, and that same query's
  `UNION ALL` mixes CTEs of different column arity. Two are silent-corruption failures: the Qullamägi
  9-month lookback window is shorter than the 252-trading-day `LAG` it needs (the entire RS book came back
  empty and looked like a quiet tape), and in the stockbee `UNION ALL` the output column names are inherited
  from the first branch, so the EP9M rows published their close-location-in-range value under the header
  `chg_pct` and the anticipation rows published trend-intensity under `volume`. Every branch now emits an
  explicitly named, identical column set, and each candidate's session change is recomputed from the price
  series rather than taken from whichever screen found it.
- **CANSLIM was sourced from shibui, not TradingView.** TradingView's scanner returns `null` for
  `earnings_growth_quarterly_yoy` and `sales_growth_quarterly_yoy` on every US name, so the spec's filter
  can never match there. The equivalent screen was rebuilt on `fundamentals_derived_quarterly.eps_growth_yoy`
  and `revenue_growth_yoy` (both decimal fractions — 0.25 means 25%), keeping every other spec criterion
  intact. It returned 150 names.
- **The $300M pre-filter floor was enforced strictly.** 72 candidates
  carry no market-cap row (41 of them leveraged or inverse ETFs, 12 plain ETFs, 16 common stocks) and
  53 more fell below the $300M floor. Leveraged ETFs are the worst
  offenders: they clear momentum and volume screens purely through leverage, and shibui's `valuation` table
  has no row for them at all, so the floor removes them by construction.
- **A duplicate-safe breadth query was used.** `shibui.valuation` keeps one row per symbol per date, so the
  large-cap breadth population was computed latest-row-first via `QUALIFY` rather than by joining on date
  directly — otherwise a stale market-cap row can admit a phantom name.
- **The breadth universe is a large-cap proxy, and it flatters the market.** The universe —
  NYSE/NASDAQ/AMEX, market cap > $10B, 908 names — shows 63.8% above the 20-day MA, but an independent all-stock read for the same
  session puts only ~34% of *every* US stock above its 50-day average (3,531 advancers vs 2,993 decliners).
  Breadth inside the $10B+ cohort is far stronger than breadth across the whole market — the size cut rule
  reads that as a narrow, index-led tape, which is what it is.
- **Finviz was unreachable** (HTTP 403 Cloudflare from both curl and web_fetch), and Yahoo's JSON endpoints
  are HTTP 429 from this egress, so neither tier-2 fallback in the skill's chain was usable.

## Tier-A — 4 names with ≥3 distinct stylists

| Ticker | Company | Close 10-28 | Chg 10-28 | ADR% 20d | Vel 14d | MCap | Styl | Close 10-29 | Chg 10-29 | Origins |
|---|---|---|---|---|---|---|---|---|---|---|
| **GMAB** | Genmab | $57.29 | +28.25% | 5.2 | 58.9 | $36.81B | 4 | $56.49 | -1.40% | 4% breakout, RS leader, 5d gainer, ADR + velocity, theme→group leader |
| **SDGR** | Schrodinger Inc | $30.87 | +15.53% | 8.1 | 17.0 | $2.31B | 3 | $29.99 | -2.85% | 4% breakout, RS leader, 5d gainer, ADR + velocity |
| **PRME** | Prime Medicine Inc | $5.36 | +23.22% | 10.7 | 49.7 | $0.97B | 3 | $5.24 | -2.24% | 4% breakout, RS leader, theme→group leader |
| **FIGS** | Figs Inc - Class A | $20.66 | +0.88% | 5.5 | 37.9 | $3.45B | 3 | $21.55 | +4.31% | RS leader, ADR + velocity, CANSLIM |

Every Tier-A name is a Health Care name, which is the sweep's single clearest signal: the 10-28 breakout
book was a biotech/medtech tape, and the two leading themes (IBB biotech and XLV
health care) are the same GICS bucket. The stockbee and Qullamägi books found them, peoplewish found them,
and the CANSLIM screen independently picked FIGS.

**Three of the four gave the move back on 10-29.** GMAB slipped -1.40%, SDGR
-2.85% and PRME -2.24%; only FIGS continued, +4.31%, and it did
so on a fresh 52-week high. A Tier-A list that fades the same session it is published is a much weaker
signal than the screen implies.

## Focus — Master names with ≥2 stylists, plus the top-5 velocity names

| Ticker | Company | Close 10-28 | Chg 10-28 | ADR% 20d | Vel 14d | MCap | Styl | Close 10-29 | Chg 10-29 | Origins |
|---|---|---|---|---|---|---|---|---|---|---|
| **GMAB** | Genmab | $57.29 | +28.25% | 5.2 | 58.9 | $36.81B | 4 | $56.49 | -1.40% | 4% breakout, RS leader, 5d gainer, ADR + velocity, theme→group leader |
| **PRME** | Prime Medicine Inc | $5.36 | +23.22% | 10.7 | 49.7 | $0.97B | 3 | $5.24 | -2.24% | 4% breakout, RS leader, theme→group leader |
| **FIGS** | Figs Inc - Class A | $20.66 | +0.88% | 5.5 | 37.9 | $3.45B | 3 | $21.55 | +4.31% | RS leader, ADR + velocity, CANSLIM |
| **SDGR** | Schrodinger Inc | $30.87 | +15.53% | 8.1 | 17.0 | $2.31B | 3 | $29.99 | -2.85% | 4% breakout, RS leader, 5d gainer, ADR + velocity |
| **SGRY** | Surgery Partners Inc | $23.24 | -0.51% | 3.5 | 70.4 | $3.04B | 2 | $23.21 | -0.13% | 5d gainer, theme→group leader |
| **LQDA** | Liquidia Corp | $45.72 | +0.62% | 9.2 | 63.2 | $4.07B | 2 | $44.99 | -1.60% | ADR + velocity, theme→group leader |
| **KIDS** | OrthoPediatrics Corp | $30.80 | +29.30% | 4.4 | 41.5 | $0.79B | 2 | $31.52 | +2.34% | 4% breakout, theme→group leader |
| **RRC** | Range Resources Corp | $55.88 | -0.89% | 3.2 | 37.1 | $13.06B | 2 | $53.89 | -3.56% | 5d gainer, theme→group leader |
| **AXGN** | Axogen Inc | $49.25 | +31.47% | 4.5 | 36.1 | $2.62B | 2 | $49.63 | +0.77% | 4% breakout, gap up (EP), 5d gainer |
| **NTSK** | Netskope Inc - Class A | $26.52 | +1.41% | 6.1 | 35.2 | $10.71B | 2 | $26.19 | -1.24% | RS leader, ADR + velocity |
| **HRI** | Herc Holdings Inc | $166.17 | +6.48% | 5.9 | 34.2 | $5.56B | 2 | $173.78 | +4.58% | RS leader, 5d gainer, ADR + velocity |
| **ICLR** | Icon Plc | $214.16 | +17.04% | 4.9 | 30.2 | $16.52B | 2 | $215.48 | +0.62% | 4% breakout, RS leader |

## Top movers — 2026-10-28 4% breakouts, with their 2026-10-29 follow-through

| Ticker | Close 10-28 | Chg 10-28 | Volume 10-28 | Close 10-29 | Chg 10-29 | MCap | $300M floor |
|---|---|---|---|---|---|---|---|
| **ULBI** | $15.61 | +145.44% | 2,495,646 | $15.62 | +0.06% | $260M | below $300M |
| **ROMA** | $7.00 | +49.25% | 671,786 | $6.62 | -5.43% | $0.42B | kept |
| **BOOM** | $7.73 | +44.49% | 7,717,432 | $8.48 | +9.70% | $159M | below $300M |
| **VRTL** | $21.81 | +31.94% | 1,241,545 | — | — | — | no cap row |
| **AXGN** | $49.25 | +31.47% | 9,290,559 | $49.63 | +0.77% | $2.62B | kept |
| **KIDS** | $30.80 | +29.30% | 1,794,600 | $31.52 | +2.34% | $0.79B | kept |
| **GMAB** | $57.29 | +28.25% | 29,283,870 | $56.49 | -1.40% | $36.81B | kept |
| **SKHU** | $16.49 | +27.04% | 1,537,027 | — | — | — | no cap row |
| **SKUU** | $21.28 | +26.67% | 5,887,113 | — | — | — | no cap row |
| **HYNX** | $21.12 | +26.54% | 829,464 | — | — | — | no cap row |
| **SKHL** | $8.14 | +26.01% | 5,668,464 | — | — | — | no cap row |
| **PRME** | $5.36 | +23.22% | 15,200,751 | $5.24 | -2.24% | $0.97B | kept |

The 10-28 breakout list is the Stockbee book's **raw output, before the $300M market-cap floor** — the
last column shows which of them the floor removes. ULBI is the top line at +145.44% on the EnerSys
$16.00-per-share cash takeout (166% premium), but at a $260M market cap it never reaches the Master list.
VRTL, SKHU, SKUU, HYNX and SKHL are leveraged/inverse ETFs with no valuation row at all, and the Nasdaq
API returns `data: null` for them, which is why their 10-29 column is blank rather than zero.

The 10-29 column is the reason this table exists: **AXGN held (+0.77%) and HRI accelerated (+4.58%),
but AIOK round-tripped from +109.69% to -32.87%** — the parabolic-short book got paid. AIOK is worth a
note: it is *not* in the breakout table because its 10-28 volume (23.96M) came in **below** the prior
session's 30.30M, so it fails the screen's volume-expansion test even as the price surged 110%. It still
surfaced in the Qullamägi 5-day gainer book, which has no volume-expansion requirement — and it
round-tripped the very next session. FIGS is the only Tier-A name that continued.

**What drove the 10-28 book.** AXGN +31.47% on a Q3 beat (revenue $75.8M, +26.2% y/y; adjusted EPS $0.21
vs $0.14 consensus) and FY26 guidance raised to at least $290M. KIDS +29.30% on a record $72.7M Q3
revenue, FY26 guidance raised to $270–273M and an FDA 510(k) clearance. GMAB +28.25% on the Phase 3
LiGeR-HN1 readout (petosemtamab + Keytruda, 50% lower death risk, HR 0.50, both primary endpoints met).
PRME +23.22% on **no company-specific news** — it was a gene-editing sector move (BEAM, CRSP) on an FDA
proposal to speed personalised gene-therapy approvals. REPL +23.07% on an FQ2 EPS beat and a TUDRIQEV
rollout update.

## Volume breakout — relative volume ≥2× with a 3%+ move (TradingView, 2026-10-29 settle)

| Ticker | Close 10-29 | Chg 10-29 | Rel volume 10d | Volume | MCap |
|---|---|---|---|---|---|
| **ADT** | $9.87 | +33.20% | 22.30 | 163,857,766 | $6.67B |
| **BHC** | $8.91 | +28.76% | 13.20 | 33,763,165 | $3.33B |
| **GTN.A** | $6.74 | +29.37% | 11.58 | 46,309 | $0.58B |
| **LENZ** | $3.49 | +8.72% | 9.05 | 5,986,115 | $0.11B |
| **PARA** | $4.28 | +27.38% | 7.25 | 887,405 | $2.8M |
| **BWFG** | $69.65 | +4.13% | 7.03 | 346,193 | $0.56B |
| **CLGN** | $4.40 | +11.39% | 6.72 | 167,089 | $8.3M |
| **GNK** | $26.66 | +4.02% | 6.32 | 2,713,816 | $1.16B |
| **TOYO** | $4.70 | +23.04% | 5.46 | 1,962,258 | $0.20B |
| **PURR** | $12.29 | +23.27% | 5.45 | 59,750,428 | $3.42B |
| **TDOC** | $8.73 | +26.89% | 5.40 | 20,118,681 | $1.59B |
| **LUNG** | $3.17 | +25.60% | 5.24 | 5,350,759 | $0.14B |
| **PRTS** | $8.62 | +5.25% | 5.17 | 99,794 | $69.5M |
| **GKOS** | $242.48 | +33.65% | 5.10 | 5,415,857 | $14.30B |
| **EG** | $400.59 | +3.54% | 5.01 | 1,689,506 | $15.36B |
| **CROX** | $150.26 | +25.54% | 4.60 | 4,897,015 | $7.20B |

This is the one table in the artifact built on the 2026-10-29 session rather than 2026-10-28, because the
TradingView screener only publishes the settled bar after the close. ADT +33.20% is a $15.3B all-cash
take-private from Thrive Holdings at $10.00 per share; GKOS +31.8% on Q3 net sales of $211.03M (+58% y/y),
a swing to net income and 2026 guidance raised to $775–785M with a preliminary $1B 2027 sales outlook;
BHC +28.76% on Q3 revenue of $2.941B (+9.7%) and $1.15 of GAAP EPS.

TradingView's `average_volume_10d_calc` runs *looser* than a true trailing-10 average on most names
(measured 0.91×–2.87× across a sample on 2026-10-29), so **these relative volumes are generally
understated**, not overstated, and the ratio has no stable sign — read them as a ranking, not a ratio.

## Parabolic short candidates — Qullamägi 5-day gainers ≥+25%

| Ticker | Company | Close 10-28 | Chg 10-28 | Gain 5d | ADR% | Vel 14d | Close 10-29 | Chg 10-29 | MCap | $300M floor |
|---|---|---|---|---|---|---|---|---|---|---|
| **AIOK** | AI OKTO Corp | $28.14 | +109.69% | +481.40% | 31.8 | — | $18.89 | -32.87% | $122M | **excluded** |
| **AXGN** | Axogen Inc | $49.25 | +31.47% | +35.01% | 4.5 | 36.1 | $49.63 | +0.77% | $2.62B | kept |
| **GMAB** | Genmab | $57.29 | +28.25% | +44.78% | 5.2 | 58.9 | $56.49 | -1.40% | $36.81B | kept |
| **HRI** | Herc Holdings Inc | $166.17 | +6.48% | +26.14% | 5.9 | 34.2 | $173.78 | +4.58% | $5.56B | kept |
| **RRC** | Range Resources Corp | $55.88 | -0.89% | +30.14% | 3.2 | 37.1 | $53.89 | -3.56% | $13.06B | kept |
| **SDGR** | Schrodinger Inc | $30.87 | +15.53% | +29.16% | 8.1 | 17.0 | $29.99 | -2.85% | $2.31B | kept |
| **SGRY** | Surgery Partners Inc | $23.24 | -0.51% | +50.91% | 3.5 | 70.4 | $23.21 | -0.13% | $3.04B | kept |
| **VEEA** | Veea Inc | $5.61 | -9.22% | +40.95% | 17.3 | 45.0 | $5.22 | -6.95% | $14M | **excluded** |
| **VSAT** | Viasat Inc | $78.26 | +11.32% | +25.04% | 6.1 | 16.1 | $77.99 | -0.35% | $10.69B | kept |

This is the raw screen output, so the last two columns matter: **AIOK and VEEA are excluded by the $300M
market-cap floor** and never reach the Master list — but AIOK is the textbook parabolic case and should not
be hidden for that reason. It closed 2026-10-28 up +109.69% on the $18M sale of its Dream Arrax LPG
carrier, then closed 2026-10-29 at -32.87%. Its volume actually *fell* that session (23.96M vs 30.30M),
which is why it failed the Stockbee breakout screen and only surfaced here. VEEA faded -6.95% and RRC
-3.56%.

## Parabolic long candidates — Qullamägi 5-day losers between -25% and -50%

| Ticker | Company | Close 10-28 | Chg 10-28 | Loss 5d | ADR% | Vel 14d | Close 10-29 | Chg 10-29 | MCap | $300M floor |
|---|---|---|---|---|---|---|---|---|---|---|
| **CORT** | Corcept Therapeutics Inc | $86.28 | -1.50% | -25.80% | 5.3 | -27.2 | $85.95 | -0.38% | $9.26B | kept |
| **EWZS** | ISHARES MSCI BRAZIL SMALL-CAP ETF | $11.01 | -4.18% | -33.27% | 3.5 | -32.6 | — | — | no cap row | **excluded** |
| **INTR** | Inter & Co Inc - Class A | $4.11 | -7.22% | -41.87% | 6.0 | -43.2 | $4.17 | +1.46% | $1.81B | kept |
| **PAGS** | PagSeguro Digital Ltd - Class A | $8.15 | -2.98% | -28.76% | 4.8 | -23.7 | $8.08 | -0.86% | $2.49B | kept |
| **SBS** | Companhia de Saneamento Basico do Estado de Sao Paulo. | $4.66 | -1.89% | -26.27% | 3.5 | -29.3 | $4.65 | -0.21% | $15.93B | kept |
| **STNE** | StoneCo Ltd - Class A | $8.09 | -0.80% | -29.96% | 5.6 | -30.3 | $8.00 | -1.11% | $2.05B | kept |
| **XP** | XP Inc - Class A | $16.09 | +0.81% | -47.11% | 5.2 | -46.7 | — | — | $8.37B | kept |

These are the mean-reversion side of the same screen: names that fell 25–50% in five sessions on
$50M-plus average dollar volume, filtered to sit within 25% of their 200-day MA.

## Regime

| Flag | Value | Meaning |
|---|---|---|
| `size_cut_pct` | 0 | Percent to trim every Tier-A position. Zero means no size cut. |
| `uncertainty` | false | VIX above VIX3M signals front-end stress. |
| `late_cycle` | false | An index ETF more than 6% extended above its 50-day MA. |
| Large-cap breadth | 63.77% | Share of the 908 names above $10B trading above their 20-day MA. |
| Index breadth | 80% above 20-DMA | Share of SPY/RSP/QQQ/QQQE/IWM above their 20-day MA (4 of 5). |
| VIX / VIX3M | 16.91 / 19.22 (ratio 0.88) | Below 1.0 means no front-end stress premium. |

No size cut: the index ETFs are 4-of-5 above their 20-day MA, so the "index below its 20-day" condition
fails even though breadth is healthy at 63.8%. The VIX/VIX3M ratio of
0.88 shows no front-end stress premium. Note the volatility pair is pinned to the
2026-10-28 session — the 2026-10-29 settle is a different reading and is deliberately not mixed in here.

## Screen counts

| Screen | Rows | Note |
|---|---|---|
| Raw candidates before pre-filter | 581 | Union of all five stylist books |
| Kept after the $300M market-cap floor | 456 | Master list size |
| Stockbee 4% breakouts | 50 | Oct-28 session |
| Stockbee EP9M | 50 | Volume ≥8.9M |
| Stockbee anticipation (coil) | 30 | ATR(7)/ATR(65) ≥1.05, base ≤8% |
| Qullamägi RS leaders | 60 | 1M/3M/6M relative strength |
| Qullamägi gap-up (EP) | 5 | Open ≥+10% vs prior close |
| Qullamägi 5-day gainers | 9 | Parabolic short |
| Qullamägi 5-day losers | 7 | Parabolic long |
| peoplewish ADR + velocity | 200 | ADR ≥5%, ADV ≥$50M |
| CANSLIM (rebuilt on shibui) | 150 | mcap >$1B, EPS & revenue growth >25%, RSI 40–80 |
| Volume breakout (TradingView) | 109 | Rel volume ≥2×, move ≥3% |
| Theme→group leaders (Hernandez) | 10 | Top 5 per leading theme sector |
| Sun compression (ATR10/ATR50 <0.6) | 1 | Screen-within-a-screen on Master |
| Master / Stalk / Focus / Tier-A | 456 / 50 / 12 / 4 | Tier sizes |

## Source health

| Source | Endpoint / query | Status | Result |
|---|---|---|---|
| shibui-finance (MCP-over-HTTP bridge) | `stock_data_query` — resolve-date, stockbee, qullamaggie, peoplewish, CANSLIM, breadth, ATR-extension, sector, compression, enrichment | ok | 456 candidates + breadth on 2026-10-28 |
| shibui `valuation` | latest-row-first via `QUALIFY` | ok | market caps resolved without stale rows |
| Cboe daily_prices | `VIX_History.csv`, `VIX3M_History.csv` | ok | VIX 16.91, VIX3M 19.22 (2026-10-28 settle) |
| Cboe delayed-quote CDN | `quotes/_VIX.json` | ok | cross-check: `prev_day_close` 16.91 matches the 2026-10-28 settle |
| Nasdaq quote API | `/quote/{SYM}/info` (secondaryData) | ok | 2026-10-29 closes for 31 of 36 tickers; 5 failures were leveraged ETFs already dropped by the floor |
| TradingView scanner | `POST scanner.tradingview.com/america/scan` | ok | 109 volume-breakout names, sector/theme table (33 ETFs) |
| Finviz screener | `finviz.co` | failed: 403 Cloudflare | tier-2 fallback unavailable |
| Yahoo Finance JSON | `query1/query2.finance.yahoo.com` | failed: 429 rate-limited | tier-2 fallback unavailable |
| SEC EDGAR / press | `web_search` | ok | catalysts cross-checked for every top mover |
| Third-party all-stock breadth | stocksetups.com/today (2026-10-28 close) | ok | 3,531 advancers vs 2,993 decliners; ~34% of all US stocks above their 50-day MA (large-cap proxy reads 54.30%) |

_Every source above was reached from this run. `errors: 0` — no source failed in a way that forced a
degraded reading of the artifact._

_Data date 2026-10-28 (shibui T+1) · cron date 2026-10-29, fired 18:32 ET · universe NYSE/NASDAQ/AMEX,
market cap > $300M · intraday counterpart: `daily-screens/2026-10-29/breadth-snapshot.md` (cron #10)._
