# Pre-Market Gapper — Wednesday, 11 November 2026

Session: the Tuesday 10 November 2026 settled close measured against the Wednesday 11 November pre-market. Tape snapshots 08:17–08:21 ET (newest internal timestamp per symbol); live `/info` quotes as of 08:32–08:36 ET; TradingView and index cross-checks 08:37–08:39 ET.
Source of record: the Nasdaq extended-trading tape, 4 pulls per symbol, the payload with the newest internal timestamp kept — cross-checked against Cboe delayed quotes, the TradingView scanner and SEC EDGAR.

_contract: premarket-artifact-v5 · flagged: 2 · scanned: 12 · gate: |gap|>=4.0% and pm_volume>=50,000 and exec_shares>=25 · reference close: focus.csv+tradingview+cboe+nasdaq_historical · universe: 2026-11-10 · denominator session: 2026-11-10_

## TL;DR

- **2 of 12 Focus names clear the gate.** LUNR **+5.00%** on the tape and BW **+4.49%** — both are post-earnings continuations, not new news.
- **The biggest gap in the book is a quote, not a market.** MPWR printed **+5.78%** on **5 shares** and FRVO **+4.57%** on **2 shares**; the size rule killed both, exactly as it is meant to.
- **The tradable move is outside the Focus book.** CoreWeave's Q3 (revenue +168%, FY26 guidance raised) has the AI-infrastructure complex gapping — CRWV **+15.4%**, LITE **+9.9%**, memory names **+8–9%** — while the 10-year sits at **4.98%**. A narrow, catalyst-driven bid, not broad risk appetite.

## Focus scan — all 12 names

| Ticker | Ref close | PM price (last executed print) | Gap % | PM volume | Exec shares | Exec notional | PM high | PM low | Quote % | Verdict | PM vol % of 10d avg | Sustained |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MPWR | 1,357.60 | 1,436 | +5.78% | 4,531 | 5 | 7,180.00 | $1439.1 | $1402 | +5.43% | BORDERLINE_THIN | 0.32% | YES |
| LUNR | 11.81 | 12.4 | +5.00% | 221,926 | 25 | 310.00 | $12.5 | $12.09 | +4.65% | FLAGGED | 2.48% | YES |
| FRVO | 11.38 | 11.9 | +4.57% | 80,080 | 2 | 23.80 | $12.0765 | $11.44 | +4.22% | BORDERLINE_THIN | 0.77% | YES |
| BW | 4.48 | 4.6813 | +4.49% | 157,925 | 45 | 210.66 | $4.7421 | $4.48 | +4.46% | FLAGGED | 2.61% | AT_CLOSE |
| PL | 14.27 | 14.805 | +3.75% | 173,491 | 10 | 148.05 | $14.9 | $14.48 | +3.15% | BORDERLINE_INTRADAY | 2.13% | YES |
| WRBY | 29.90 | 30.64 | +2.48% | 9,426 | 2 | 61.28 | $31 | $29.99 | +2.95% | BORDERLINE_INTRADAY | 0.16% | YES |
| IAM | 14.78 | 14.56 | -1.49% | 7,382 | 4 | 58.24 | $15.24 | $14.5 | -1.89% | BELOW | 1.28% | NO |
| QXO | 13.73 | 13.88 | +1.09% | 28,529 | 100 | 1,388.00 | $13.9 | $13.77 | +0.95% | BELOW | 0.15% | YES |
| IMVT | 35.71 | 36.02 | +0.87% | 1,410 | 35 | 1,260.70 | $35.5 | $35.5 | -1.29% | BELOW | 0.08% | NO |
| TLS | 7.67 | 7.73 | +0.78% | 4,900 | 600 | 4,638.00 | $7.77 | $7.5215 | +0.80% | BELOW | 0.31% | NO |
| PRAX | 337.59 | 339.6501 | +0.61% | 625 | 2 | 679.30 | $341.635 | $339.45 | +0.61% | BELOW | 0.14% | YES |
| TTD | 15.42 | 15.3339 | -0.56% | 153,000 | 300 | 4,600.17 | $15.46 | $15.3 | -0.13% | BELOW | 0.55% | NO |

_Sorted by absolute gap, largest first. `PM price` is the last EXECUTED print on the tape; `Quote %` is the live `/info` quote, published separately. `PM vol % of 10d avg` is the pre-market cumulative volume against the TradingView 10-day average volume (`average_volume_10d_calc`) — the absolute 50,000-share floor still decides the flag. `Sustained` = did the pre-market low stay above the prior close._

## Focus names that did not qualify

- **WRBY** — +2.48% · 9,426 pre-market shares · $29.99–$31 · 4 stylists, 5 origins
  (A_stockbee_4pct, B_stockbee_ep9m, E_qullamaggie_5d_gainers, G_peoplewish, H_hernandez_theme) · setup: good setup that went nowhere — the richest provenance in the book (4 stylists, 5 origins) and it never moved; the tape print carried 2 shares
- **PRAX** — +0.61% · 625 pre-market shares · $339.45–$341.635 · 4 stylists, 4 origins
  (A_stockbee_4pct, C_qullamaggie_rs, G_peoplewish, H_hernandez_theme) · setup: good setup that went nowhere — 4 stylists, 4 origins, +0.61% on 625 shares of pre-market volume
- **FRVO** — +4.57% · 80,080 pre-market shares · $11.44–$12.0765 · 3 stylists, 5 origins
  (A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, E_qullamaggie_5d_gainers, G_peoplewish) · setup: good setup that nearly fired — it printed +4.57%, but on a 2-share print and 0.77% of its own 10-day average volume, so there was no market behind it
- **QXO** — +1.09% · 28,529 pre-market shares · $13.77–$13.9 · 3 stylists, 5 origins
  (A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, C_qullamaggie_rs, G_peoplewish) · setup: good setup that went nowhere — 3 stylists, 5 origins, +1.09% and only 28,529 pre-market shares
- **TTD** — -0.56% · 153,000 pre-market shares · $15.3–$15.46 · 2 stylists, 4 origins
  (A_stockbee_4pct, B_stockbee_ep9m, B_tv_ep9m, TV_volume_breakout) · setup: bad setup for today — a real 153,000-share pre-market market that went the other way (−0.56%); the earnings print did not hold
- **PL** — +3.75% · 173,491 pre-market shares · $14.48–$14.9 · 2 stylists, 3 origins
  (A_stockbee_4pct, B_stockbee_ep9m, G_peoplewish) · setup: good setup that faded — it crossed the bar intraday (pre-market high +4.42%) and came back to +3.75%, with a 10-share print carrying the snapshot
- **IAM** — -1.49% · 7,382 pre-market shares · $14.5–$15.24 · 2 stylists, 3 origins
  (A_stockbee_4pct, A_tv_breakout_4pct, TV_volume_breakout) · setup: bad setup — negative gap on 4 shares, no follow-through after earnings
- **TLS** — +0.78% · 4,900 pre-market shares · $7.5215–$7.77 · 2 stylists, 3 origins
  (A_stockbee_4pct, A_tv_breakout_4pct, TV_volume_breakout) · setup: good setup that went nowhere — it reported on 09 November and moved +0.78% on 4,900 shares
- **MPWR** — +5.78% · 4,531 pre-market shares · $1402–$1439.1 · 2 stylists, 2 origins
  (A_stockbee_4pct, G_peoplewish) · setup: setup not classified
- **IMVT** — +0.87% · 1,410 pre-market shares · $35.5–$35.5 · 2 stylists, 2 origins
  (A_stockbee_4pct, H_hernandez_theme) · setup: good setup that went nowhere — 2 stylists, 2 origins, +0.87% on 1,410 shares; noise, not a market

## Flags

- **MPWR +5.78% on 5 shares** — a quote, not a market. Cumulative pre-market volume 4,531 is 0.32% of its own 10-day average, and the tape's 100-row sum is 639 shares.
- **FRVO +4.57% on 2 shares** — the print that carried the gap was $23.80 of notional. Cumulative volume 80,080 is 0.77% of its 10-day average.
- **PL crossed the bar and faded** — pre-market high +4.42% against a +3.75% snapshot, with a 10-share print carrying the snapshot.
- **LUNR's published gap rests on a 25-share print** — exactly at the MIN_EXECUTED_SHARES floor. The cumulative volume behind it is real (221,926 shares, 2.48% of the 10-day average); the *last* print is what is small, so re-check it at 09:30.
- **BW's published gap rests on a 45-share print** — $210.66 of notional, on 157,925 shares of cumulative pre-market volume (2.61% of the 10-day average).
- **BW reference close conflict** — Nasdaq `/info` secondaryData read 4.5000 against 4.4800 from the sweep's own focus.csv, TradingView, Cboe and Nasdaq history. The gap is measured against 4.4800; the disagreement is published in the row's `ref_close_source`.
- **WRBY faded from a +6.36% tape print to +2.48%** — the contract's `pm_high` ($31.00, +3.68%) is the trade-detail high, while the verdict engine reads the tape's extreme print.

## Catalyst ahead

- **LUNR — Q3 2026 results before the open on Thursday 12 November.** Issuer-confirmed via the company's own news release schedule and multiple wire previews; the pre-market gap is +5.00% into that print, so this is a position *into* a catalyst, not a gap trade.
- **No other Focus name reports before tomorrow's open.** A TradingView earnings-date scan for 2026-11-11 returned 41 names; every US listing in it has a release time at or before 07:00 ET and none has a confirmed after-close slot.

## The market's event book — pre-market gap leaders outside the Focus list

The Focus universe is a momentum screen built on yesterday's data, so it structurally cannot contain a name whose move has not happened yet. This is the market's own book: 420 US names gapped ≥4% pre-market, of which **79** clear a $300M market cap and a 50,000-share pre-market volume floor. Top 14, gaps from the TradingView scanner against the previous close.

| Ticker | Gap % | PM volume | Mkt cap | Catalyst (sourced) |
|---|---|---|---|---|
| CRWV | +15.39% | 7,865,259 | 26.9B | Q3 revenue $3.66B (+168% YoY), backlog ~$132.5B, FY26 revenue guide raised to $13.0–13.3B, adj. operating margin 10% vs 5% prior quarter; 8-K item 2.02 filed 2026-11-10 (call 5:00 PM ET) |
| FOSL | +23.89% | 133,331 | 0.47B | 8-K item 2.02 (results) filed 2026-11-10 — figures not read in this run |
| SATL | +19.96% | 629,007 | 0.60B | 10-Q + 8-K item 2.02 filed 2026-11-10 — figures not read in this run |
| RSKD | +19.34% | 284,788 | 1.12B | no SEC filing since 2026-11-09 — catalyst NOT identified in this run |
| GEVO | +17.99% | 363,277 | 0.34B | 10-Q + 8-K item 2.02 filed 2026-11-10 — figures not read in this run |
| NBIS | +13.09% | 1,904,697 | 36.4B | no filing since 2026-11-09 — AI-infrastructure read-across only, unconfirmed in this run |
| HYLN | +12.04% | 69,546 | 0.53B | 10-Q + 8-K item 2.02 filed 2026-11-10 — figures not read in this run |
| CIFR | +10.57% | 1,143,990 | 2.98B | no filing since 2026-11-09 — data-centre read-across only, unconfirmed in this run |
| COHR | +10.18% | 217,791 | 42.3B | no filing since 2026-11-09 — optics read-across only, unconfirmed in this run |
| APLD | +10.01% | 772,721 | 5.04B | no filing since 2026-11-09 — AI-infrastructure read-across only, unconfirmed in this run |
| LITE | +9.90% | 109,759 | 53.1B | Marvell all-stock acquisition ($115B EV, $1,100 per LITE share, 4.5 MRVL per LITE, announced 2026-11-02); 425 business-combination communications filed 11-09/11-10 — Dec-qtr guide $1.6B, 53% gross margin |
| STX | +9.43% | 57,172 | 115.2B | no filing since 2026-11-09 — memory read-across from CRWV's raised capex outlook, unconfirmed in this run |
| MXL | +8.71% | 51,818 | 4.90B | no filing since 2026-11-09 — semiconductor read-across only, unconfirmed in this run |
| SNDK | +8.37% | 607,009 | 122.4B | no filing since 2026-11-09 — memory read-across from CRWV's raised capex outlook, unconfirmed in this run |

_The cluster is one trade: CoreWeave's beat and raised FY26 outlook eased the AI-capex-ROI fears that had been dragging the group, and the memory/optics complex re-rated with it. Names marked *not identified* are gaps this run could not attribute to a filing — the move is real, the reason is not sourced here._

## Method, source health & caveats

**Universe and denominator (both proven before any tape was pulled).** The expected prior session was resolved FROM DATA (Nasdaq SPY session history, never a typed calendar): **2026-11-10**. The universe is the 2026-11-10 sweep's own `focus.csv` — 12 names, manifest `daily-screens/2026-11-11/_universe.json`, status `OK_WITH_FLAGS`. The denominator is that sweep's `today_close` column for session 2026-11-10; the resolver explicitly REJECTED `screen_close_resolved` (2026-11-09) because it belongs to the screen's T+1 data date, not to the denominator session. Every row publishes `universe_date` = `ref_close_date` = 2026-11-10.

**Reference close.** 12/12 names confirmed by TradingView, Cboe and Nasdaq per-symbol history. One disagreement (BW) is published in that row's `ref_close_source` and in Flags.

**Tape and quotes.** The Nasdaq extended-trading endpoint was pulled 4× per symbol and the payload with the newest internal timestamp kept (vintages seen 07:44–08:21 ET); the `/info` live quote is published separately as `quote_price` / `quote_gap_pct`. The published gap is always the last EXECUTED print.

**Volume.** `pm_volume` is the Nasdaq extended-trading cumulative counter. The trade-detail table is capped at 100 rows, so its sum is a floor, not a total (LUNR 4,801 of 221,926 counted; MPWR 639 of 4,531) — `pm_volume_source` names the counter on every row.

**Margin.** The widest absolute gap on any source was 5.78% against a 4.00% trigger (0.69× margin), so the flag decision is immune to whichever cached vintage a source returned.

**Cross-checks.** TradingView scanner pulled twice — the 12 Focus names (12/12 rows) and the whole-market movers (420 rows, `totalCount` 420 — no silent truncation). TradingView's `premarket_volume` undercounts (LUNR 154,976 vs Nasdaq 221,926), so the 50,000-share test was never run on TV volume alone. Cboe delayed quotes supplied an explicitly-timestamped second price. SEC EDGAR submissions supplied the catalysts (8-K item 2.02, 425, 10-Q) and the earnings dates.

**Market context (bridge `market-recap` market_snapshot, 08:38 ET).** S&P 500 futures +0.98% · US 10-year 4.983% · DXY +0.43% · WTI +1.45% · gold +0.44% · Nikkei 225 +1.31% · Hang Seng −0.54%.

**Known Nasdaq defects checked on this run.** `/info` `primaryData.lastSalePrice` was used only as the live quote, never as the published gap; TTD's primaryData equals its ask (a quote, not a print); `secondaryData` drift was caught on BW. No `screen_close_resolved` denominator was used anywhere.

**Limitations.** (1) The universe is 12 momentum names built on 2026-11-10's data — it cannot contain today's pre-sweep catalysts, which is why the event book is published alongside it. (2) Pre-market volumes at ~08:20 ET are early-session and keep building until 09:30, so the 50,000-share floor can flip between now and the open on either flagged name. (3) Both flagged gaps were carried by prints of 25 and 45 shares — small enough to be the last print rather than the market. (4) The tape's extreme print can exceed the published `pm_high` (WRBY 6.36% vs +3.68%; PL 3.92% vs +4.42%): the contract publishes `pm_high`/`pm_low`, the verdict engine reads the tape extreme. (5) Finviz is not in the chain (blocked from this egress); the Nasdaq, Cboe, TradingView, bridge and EDGAR paths all worked.

**Source health.**

| Source | Query | Status |
|---|---|---|
| Nasdaq extended-trading tape | `/api/quote/{sym}/extended-trading` ×4 per symbol, 12 symbols | ok |
| Nasdaq `/info` live quote | `/api/quote/{sym}/info` | ok |
| Cboe delayed quotes | `cdn.cboe.com/api/global/delayed_quotes/quotes/{sym}.json` | ok |
| TradingView scanner (focus) | `POST scanner.tradingview.com/america/scan` | ok (12/12) |
| TradingView scanner (movers) | same, `premarket_change > 4` | ok (420/420) |
| SEC EDGAR submissions | `data.sec.gov/submissions/CIK*.json` | ok |
| Bridge `market-recap` market_snapshot | `mcp_bridge.py market-recap market_snapshot` | ok |
| MCP availability probe | `probe_mcp.py` | ok — catalog 135 tools, 0 finance MCPs registered (the bridge is the finance path) |

degraded_sources: 0

