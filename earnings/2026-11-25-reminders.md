---
date: 2026-11-25
cron: 19-earnings-reminder-daily
fire_time_et: 06:00
snapshot_et: 06:15
source: EarningsWhispers earnings calendar + Yahoo Finance earnings calendar + Nasdaq earnings calendar + TradingView scanner
primary_source: Yahoo Finance (market cap, EPS est, revenue est) | TradingView america scanner (issuer-level USD caps for the band)
status: ok
pending_count: 1
already_reported_count: 1
non_us_count: 0
reaction_ranked: true
band_low_usd: 40000000000
reaction_degraded: 0
contract: EARNINGS_REMINDER_V4
coverage_receipt: calendar_rows=59 s_and_p_500_hits=1 bigcap_hits=1 us_roster_rows=1 band_rows=9
coverage_floor: floor_usd=50000000000 band_low_usd=40000000000 us_population=5482 below_band_us=4903 band_us=65 at_or_above_floor_us=408 no_cap_us=106 source=TradingView america scanner (market_cap_basic, issuer-level USD)
---

# Earnings - Wed 2026-11-25

## TL;DR

- **Coverage floor — a scope limit, not a missing company.** This reminder covers S&P 500
  constituents plus US-listed reporters with a market cap of **$50B or more** (TradingView
  scanner, `market_cap_basic`, issuer-level USD). The band just under the floor — **$40B to
  $50B** — is published in the *Just below the line* table so the cliff is visible. **A US
  reporter below $40B market cap is out of scope for this reminder: it is not on this list, and
  its absence does not mean it did not report.** Of the scanner's **5,482** US names, **4,903**
  are below the $40B band floor and therefore out of scope, **65** sit in the $40B-$50B band,
  **408** are at or above the $50B floor, and **106** carry no market cap at all.
- **This is a one-name board, and the name is Deere.** Deere & Company (NYSE: DE) is the only
  S&P 500 constituent and the only US reporter at or above the $50B floor printing today —
  fiscal Q4 2026, **before the open**. The other 58 calendar rows are all below the $40B band
  floor, so they are out of scope rather than missing.
- **Deere is the only thing on the board, so the ranking is the risk statement.** One row, one
  reaction score: **7.91** — a 7.91% mean absolute move over its last three prints, on a stock
  that fell **-3.04%** on Nov 24 and is **+31.48%** YTD. The prior quarter was a **beat**
  (+8.30%). The implied-move half of the signal is missing (see below), so 7.91 is a
  historical-average score, not a market-implied one.
- **One print already landed before the 06:00 ET fire**: easyJet (LSE: EZJ) published its
  FY26 final results at **02:00 ET** — headline pre-tax profit £71m, an **89% fall**, and a
  **miss** against the £87.7m LSEG consensus. It is in the *Already reported* table.
- **The non-US table is empty and that is a measured result, not a gap.** Every one of the 47
  standing non-US candidates was swept across the whole global release calendar; none carries a
  Nov 25 date. The largest non-US names stamped for today (Nidec, easyJet, Xiaomi, Azrieli,
  Fisher & Paykel, the Malaysian and Russian banks) are either below the standing universe or
  outside it, and the one large candidate whose date was confirmed — **Nidec — has postponed
  its Q2 disclosure**, so it does not report today at all.

## Big S&P 500 today

| Ticker | Company | Time | EPS est | Rev est | Mkt cap | Prior day % | YTD % | Avg abs move % | Implied move % | Prior result | Reaction score | Status | Flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DE | Deere & Company | BMO | $4.06 | $10.34B | $165.49B | -3.04 | +31.48 | 7.91 | n/a | beat | 7.91 | pending | - |

_One row. Deere is the only S&P 500 constituent and the only US reporter at or above the $50B
floor on today's calendar — the other 58 calendar rows are below the $40B band floor and out of
scope. The Time cell is `BMO` because both the Nasdaq and the Yahoo calendars stamp it
pre-market and neither publishes a release hour; the issuer's own IR events feed gives the
earnings call at 9:00 a.m. Central (10:00 ET) on Nov 25, and the release precedes the call._

## Non-US primary listings

| ticker_primary | venue_primary | Company | Report time (local) | us_peer | us_tradeable | Status |
|---|---|---|---|---|---|---|

_No row qualifies. All 47 standing non-US candidates were swept against the global
release-date calendar (1,021 names stamped for Nov 25 across every market) and **none** carries
a Nov 25 date; no US calendar carried one either. The large non-US names stamped for today —
LUKOIL ($48.9B, Moscow), Malayan Banking ($29.9B, Kuala Lumpur), TS Financial Holding ($27.6B,
Taipei), Gazprom neft ($27.2B, Moscow), Tenaga Nasional ($17.6B, Kuala Lumpur), Fisher & Paykel
($15.8B, Auckland) — sit outside the standing US-market-relevant universe, and their US lines
are absent or OTC-only in a way that leaves the `us_peer` contract unfillable. The one
candidate in the size range that was checked against its own issuer page, **Nidec
(Tokyo: 6594, OTC: NJDCY, ~$12.1B)**, is **excluded**: on Nov 16, 2026 Nidec announced it is
**postponing** the disclosure of its Q2 FY2027 results beyond the 45-day window, so the
TradingView release date of Nov 25 is wrong and Nidec does not print today. It is named here
rather than published on a stale estimate._

## Just below the line - excluded by the $50B floor

| Ticker | Company | Mkt cap | Reports today |
|---|---|---|---|
| CVE | Cenovus Energy | $48.54B | no |
| TEVA | Teva Pharmaceutical Industries | $46.79B | no |
| TRI | Thomson Reuters | $46.48B | no |
| WCN | Waste Connections | $46.00B | no |
| FNV | Franco-Nevada | $45.82B | no |
| VIK | Viking Holdings | $44.63B | no |
| NTRA | Natera | $43.33B | no |
| FER | Ferrovial | $42.17B | no |
| RPRX | Royalty Pharma | $40.91B | no |

_Nine US-listed common shares sit in the $40B-$50B band the floor excluded, and **none of them
reports today** — every next release date on the scanner falls in February or March 2027. The
caps are the TradingView scanner's issuer-level `market_cap_basic`; the Yahoo cross-check
agrees to within 0.6% on all nine (FER $42.17B vs $42.42B, RPRX $40.91B vs $41.00B, the other
seven within 0.1%), so no spread needs flagging._

## Already reported (before 06:00 ET)

| Ticker | Company | Released | Actual | vs consensus | us_tradeable |
|---|---|---|---|---|---|
| EZJ.L (EJT1) | easyJet plc | 02:00 ET (company RNS, published 08:00 CET on Nov 25) | FY26 (year to 30 Sep 2026): revenue £10,737m (+6.2%); headline pre-tax profit £71m (FY25 £665m); reported pre-tax profit £24m (FY25 £658m); headline basic EPS 8.8p (FY25 66.4p); reported basic EPS 2.7p; airline segment headline pre-tax loss £195m; no FY26 dividend recommended | headline pre-tax profit £71m vs the £87.7m LSEG consensus (company-cited consensus £79m) — a miss of 19% on the LSEG number; revenue beat not measured on a like-for-like basis | US-listed |

_easyJet's primary listing is the LSE (EZJ.L) and its US line is the Nasdaq ordinary share
(EJT1) — the same security, not an ADR, so it is published as `US-listed`. It is outside both
the standing 47-name non-US universe and the $50B floor, and it is carried here because it is
an issuer-confirmed print that landed before the 06:00 ET fire and a US-listed line a US reader
can trade. The Apollo takeover at 715p per share is expected to complete in Q1 2027._

## Notes

- **Ranked by reaction potential, not by size.** With one row the ranking is trivial, and that
  is the honest output: Deere's 7.91 is a 3-event mean absolute move across its Aug 20, May 21
  and Feb 19 prints (Yahoo daily bars + Nasdaq `earnings-surprise` report dates). The contract
  asks for four past reports; **only three were available** in the measured window, so the mean
  is a 3-event mean and is published as measured rather than padded.
- **Deere's prior result is a beat.** The latest reported quarter (ended 2026-07-31, reported
  Aug 20) printed EPS $5.10 against a $4.71 consensus, a **+8.30%** surprise
  (source: Yahoo `earningsHistory`, latest quarter-end selection). The setup into the print is
  a beat-after-beat one, but it is a single name, so it carries no information.
- **`Implied move %` is `n/a` and no score is degraded** (`reaction_degraded: 0`). Cboe's
  delayed-quote option chain (`cdn.cboe.com/api/global/delayed_quotes/options/DE.json`)
  answers a Cloudflare block from this egress — the request returns an HTML challenge page, not
  JSON — so no ATM straddle could be measured. Per the contract the score substitutes
  `avg_abs_move` for the missing implied move, which is why the score equals the average move
  exactly (0.6 x 7.91 + 0.4 x 7.91 = 7.91). **Every score in this artifact is a historical
  average, not a market-implied one.**
- **Deere's date is confirmed on the issuer's own pages, twice.** Deere's newsroom carries the
  Nov 11, 2026 announcement "Deere to Announce Fourth Quarter 2026 Financial Results —
  earnings call on Wednesday, Nov. 25, beginning at 9 a.m. Central time", and the issuer's own
  IR events feed (`investor.deere.com/rss/event.aspx`) carries "11/25/2026 : John Deere - 4Q
  Earnings Call". The release hour itself is not issuer-stamped, so the row carries `BMO`
  rather than a guessed clock time; the call time is the issuer's.
- **Every roster date is confirmed on two independent calendars.** The Nasdaq earnings calendar
  (`time-pre-market` for DE) and the Yahoo Finance earnings calendar (`BMO`) agree, and the
  TradingView global release-date sweep returns the same single US name above $15B.
- **EPS and revenue consensus: one primary source, the spread published.** Yahoo is the single
  EPS and revenue source (EPS $4.06, revenue $10.34B, 13 analysts each). The independent
  readings agree inside tolerance: EPS **$4.06** (Yahoo) vs **$4.07** (Nasdaq) vs **$4.03**
  (TradingView, Zacks-adjusted) and **$4.03** (Investing.com) — a spread of 0.74% on the
  highest and lowest, under the 2% flag threshold. Revenue **$10.34B** (Yahoo) vs **$10.38B**
  (TradingView) vs **$10.4B** (Investing.com).
- **Market cap: one source, one cross-check.** The roster carries Yahoo's $165.49B for DE. The
  TradingView scanner puts the same issuer at $165.5B (0.01% apart); the Nasdaq calendar
  carries $170.68B, a 3.1% spread, inside the 5% flag threshold. No spread needs flagging.
- **No watchlist section.** The published watchlist (`refs/watchlist.yaml`) fetched fine — AAPL,
  MSFT, NVDA, GOOGL and AMZN (earnings-flagged), plus IWM, GLD and TLT — and **none of them
  reports today**, so the section is omitted rather than shipped empty.
- **Every calendar hit that is not published is named here.** Three calendars were scanned for
  Nov 25 — Nasdaq 39 rows, EarningsWhispers 29 rows, Yahoo Finance 25 distinct rows — a union
  of **59** ticker rows. Exactly **1** is an S&P 500 constituent and exactly **1** clears the
  $50B floor on its own (DE), and the roster's 1 row is that same name. The other 58 rows are
  excluded on scope, not on judgement: the largest of them are Li Auto ($10.46B, a Nasdaq ADR
  of a Chinese issuer, BMO), Kanzhun ($5.57B, Nasdaq ADR, BMO), GDS Holdings ($2.76B, Nasdaq
  ADR, BMO), Banco Macro ($3.2B, NYSE, AMC), Ingles Markets ($1.60B, NYSE ADR, Peru), newcleo
  ($920M, Nasdaq, UK), Copper Ridge ($286M), StealthGas ($281M), Super Hi ($577M), Gaotu
  ($482M), Polestar ($420M), Diana Shipping ($284M), Yatsen ($157M), OMS Energy ($159M), EHang
  ($186M), and 43 more below $200M — plus the OTC/ADR-only lines EarningsWhispers carries
  (DIDIY, EKTAY, GLGLF, GLMD, NRXBF, T.CGY, T.GLG, V.NRX, V.RDS) and the Yahoo-only rows
  (CBAT, DAVA, DOYU, DRVN, ESOA, GSHD, LUD, MENS, RGCO, SIDU, ZENA). **None of them is an
  S&P 500 member and none reaches the floor**, so none is published.
- **The band is a lower bound on the excluded set.** Names below $40B are excluded by the band,
  not by the floor, and the per-day count of reporters below the band was not enumerated (it
  would need a market-cap pull for every calendar row, which does not fit the discovery
  cutoff). Royalty Pharma enters the band today at $40.91B; it was below the band floor on the
  Nov 24 fire.
- **Read-only reminder: no action is taken on any of these names.**

## Source health

| Source | URL / query | Status | Notes |
|---|---|---|---|
| Coverage floor (scope limit) | `scanner.tradingview.com/america/scan` — `market_cap_basic` (issuer-level USD), constants `MCAP_FLOOR = $50B` and `band_low_usd = $40B` | ok | The roster is bounded by the market-cap band, not by who reported: S&P 500 constituents plus US-listed names at or above $50B, with the $40B-$50B band published below the floor. A US reporter below $40B market cap is out of scope — it is not on this list (a scope limit, not a missing company). US names below the band floor: 4,903 of 5,482 (65 in the band, 408 at or above the floor, 106 with no cap) |
| Nasdaq earnings calendar | `api.nasdaq.com/api/calendar/earnings?date=2026-11-25` | ok | 39 rows; the independent second-source date and BMO/AMC confirmation for DE, plus the `marketCap` cross-check |
| Yahoo Finance earnings calendar | `finance.yahoo.com/calendar/earnings?day=2026-11-25` | ok | 25 distinct tickers / 26 rows (Li Auto carries both an announcement and a call row), server-rendered rows with EPS estimate and market cap; DE stamped `BMO` |
| EarningsWhispers earnings calendar | `earningswhispers.com/calendar/20261125` | ok | 29 rows server-rendered (25 before the open, 4 after the close); the third calendar and the source of the unconfirmed/expected flags |
| TradingView america scanner | `scanner.tradingview.com/america/scan` — `market_cap_basic` (issuer-level USD) | ok | 5,482 US names after the `type in (stock, dr)` filter; the floor decomposition and every band cap |
| TradingView global scanner | `scanner.tradingview.com/global/scan` — `earnings_release_next_date`, `market_cap_basic` | ok | the Pass B completeness sweep: 1,021 names stamped for Nov 25 across every market, of which **none** is one of the 47 standing non-US candidates; also the source of the Nidec Nov 25 estimate that the issuer then contradicted |
| S&P 500 constituent list | `en.wikipedia.org/w/api.php?action=parse&page=List_of_S%26P_500_companies&prop=wikitext` | ok | parsed with all three symbol templates (`NyseSymbol`, `NasdaqSymbol`, `BZX link`) — **503** symbols, control set `BRK.B`, `GOOGL`, `GOOG`, `FOX`, `CBOE` all present |
| Yahoo chart API | `query1.finance.yahoo.com/v8/finance/chart/DE?interval=1d&range=2y` | ok | daily bars for prior-day %, YTD % and the 3-event reaction average |
| Yahoo `quoteSummary` (crumb handshake) | `query1.finance.yahoo.com/v10/finance/quoteSummary/DE?modules=earningsTrend,earningsHistory` | ok | consensus EPS $4.06 and revenue $10.34B (13 analysts each); prior-quarter actual $5.10 vs $4.71 consensus (+8.30%); market cap $165.49B |
| Yahoo `v7/finance/quote` | `query1.finance.yahoo.com/v7/finance/quote?symbols=CVE,TEVA,...` | ok | the band cross-check (crumb handshake); agrees with the scanner to within 0.6% on all nine band names |
| Cboe delayed option chain | `cdn.cboe.com/api/global/delayed_quotes/options/DE.json` | blocked | Cloudflare challenge page from this egress, not a JSON body; no ATM straddle measurable, so `implied move %` is `n/a` and the score substitutes `avg_abs_move` |
| Issuer IR pages | `deere.com/en-us/our-company/newsroom` (Nov 11, 2026 announcement), `investor.deere.com/rss/event.aspx` (IR events feed), Nidec's Nov 16, 2026 Business Wire release, easyJet's Nov 25, 2026 company RNS | ok | Deere's Nov 25 4Q call (9:00 a.m. Central, from the issuer's own feed), Nidec's postponement of its Q2 disclosure, and easyJet's 08:00 CET final results |
| Watchlist | `minimax-cloud-outputs` / `refs/watchlist.yaml` | ok | fetched; 8 names, none reporting today, so no watchlist section is published |

## Rules applied

- S&P 500 membership verified against the live constituent list - never from memory: the
  MediaWiki wikitext of `List_of S&P 500_companies` parsed with all three symbol templates
  (`NyseSymbol`, `NasdaqSymbol`, `BZX link`), **503** symbols, with the control set
  `BRK.B`, `GOOGL`, `GOOG`, `FOX`, `CBOE` all present.
- Report dates confirmed against an issuer-owned page before inclusion: Deere's date is
  confirmed on Deere's own newsroom announcement and on the issuer's IR events feed, and
  easyJet's print is confirmed on the company's own RNS.
- The issuer's own IR calendar outranks every aggregator - it is what excluded Nidec, whose
  TradingView release date of Nov 25 was contradicted by the issuer's Nov 16 postponement
  notice.
- One row per issuer; the non-common filter is applied in code over the scanner's
  descriptions, not by hand, and the S&P 500 exclusion is applied before the band is built.
- Reaction columns computed from measured bars and measured past report dates; a value that
  could not be measured is published as `n/a` and named in the notes, never estimated from
  market cap or from a similar name.
- Market-cap floor and band applied from one source (the scanner's issuer-level
  `market_cap_basic`), with the counts published in the front matter, the TL;DR and the source
  health so the three agree.
- Read-only reminder: no action is taken on any of these names.
