---
date: 2026-11-20
cron: 23-agentic-post-market-brief
contract: postmkt-artifact-v2
fire_time_et: 22:30
snapshot_et: 22:30-23:10
session: 465625634095262
scheduled_at_ms: 1795231804548
status: ok
source: MCP-over-HTTP bridge (market-recap: get_quotes, price_history, market_snapshot) | TradingView public scanner | cron #20 us-eod/2026-11-20.csv | CBOE daily market statistics | CBOE dated index files | web_search
primary_source: bridge market-recap (Yahoo-sourced, not rate-limited)
universe: cron #20 us-eod/2026-11-20.csv — 4,881 names, 4,852 priced (2,132 flagged rows excluded from cap-weighted columns)
degraded_sources: 3
---

# Post-market brief — Friday, 20 November 2026

## TL;DR

The AI trade broke, and it broke in the one place it was most concentrated. The S&P 500 fell 3.70% to 6,910.39 and the Nasdaq Composite fell 5.28% to 22,617.73 — both indices are now in correction territory — while the semiconductor index lost 10.73% and Nvidia fell 14.01%. The tape was not merely green-for-red: **advancers 804 against decliners 3,895**, **median_name_move_pct -1.88** on the 4,852-name cron #20 universe, and a **liquid_adv_dec_ratio 0.23** (320 vs 1,416 above a $2B market-cap floor). The **cap_weight_penalty_bp was -166** (SPY -3.64% vs RSP -1.98%), the largest negative reading in the five-session history below: the selling was led by mega-cap technology, and the equal-weight index fell less than half as far. Volatility repriced hard (VIX 35.89, +26.20%; VXN 45.25, +24.04%) while the 10-year yield fell 14bp to 4.912% — a growth scare, not an inflation scare. After the close the one live story was corporate: Bloomberg and Reuters reported CrowdStrike is in talks to acquire Zscaler, and Zscaler printed +16.35% in extended hours while CrowdStrike fell 4.84%. Read this brief with one caveat: **there is no overnight print to find on a Friday** — the CME equity-index week closed and Globex reopens Sunday 18:00 ET, so the futures numbers below are Friday's settlement, not a Monday setup.

## Tomorrow's setup — Monday, 23 November 2026

### Futures and the overnight setup

**There is no overnight print on this fire.** CME equity-index futures trade Sunday 18:00 ET to Friday 17:00 ET and the week closed at Friday's settlement; the first opportunity to read a Monday setup is Sunday 18:00 ET, and the Asia cash leg follows Monday morning. Every futures row below carries `as_of` 16:59:56–16:59:59 ET — that is the Friday **settlement**, not a post-settlement trade.

| Contract | Friday settle | vs prior settle | vs the cash index close |
|---|---|---|---|
| ES=F (S&P 500) | 6,966.75 | -3.20% (prior settle 7,197.25) | **+0.82%** vs SPX 6,910.39 |
| NQ=F (Nasdaq-100) | 25,291.00 | -4.92% (prior settle 26,600.25) | **+1.05%** vs NDX 25,028.98 |
| YM=F (Dow) | 48,391.00 | -1.60% (prior settle 49,180) | **+0.51%** vs DJI 48,147.33 |
| RTY=F (Russell 2000) | 2,599.90 | -2.38% (prior settle 2,663.30) | **+0.70%** vs RUT 2,581.79 |
| ZN=F (10-year note) | 106.609 | +0.69% | 10-year yield 4.912%, -14bp |

Both denominators matter and they say different things. Measured against the prior settle the futures read as another leg down; measured against the cash index close they finished **0.5–1.0% above** it — the settlement was a small bounce off the lows, not a continuation. Judge the Monday open on the cash-close comparison.

The Asia cash leg was already closed before the US session ended (Friday's own session): **Nikkei 225 56,436.65, -5.06%**; Hang Seng 22,410.80, -3.79%; Shanghai Composite 3,533.79, -1.22%. Japanese chip names led the Asian leg lower (Tokyo Electron -7.06%, Lasertec -9.21%, Renesas -7.02%), so Friday was one continuous global de-rating of the AI supply chain rather than a US-only event. There is no stamped live Asian index for Sunday evening yet — that print does not exist.

One observation, not a setup: the TradingView futures feed carried a post-close **indicative** print stamped 19:54 ET (ES1! 6,935, -3.64% vs its own settle). Its timestamp is a feed stamp, not a trade, and the CME session was closed.

### Economic calendar

Monday, 23 November (the next trading session):

| Time (ET) | Release | Prior | Consensus |
|---|---|---|---|
| 8:30 | Chicago Fed National Activity Index (Oct) | 0.07 | — |
| 9:45 | S&P Global Manufacturing PMI (Nov flash) | 54.9 | 54.5 |
| 9:45 | S&P Global Services PMI (Nov flash) | 56.1 | 55.0 |
| 9:45 | S&P Global Composite PMI (Nov flash) | 55.9 | — |
| 13:00 | $69B 2-year note auction | last 4.708% | — |

The week's heavier prints sit behind Monday: Tuesday has Consumer Confidence (Nov, prior 91.7, consensus 94.4) and the Richmond Fed; **Wednesday 25 November carries core PCE (Oct), the 3Q GDP second estimate (prior 3.4%, consensus 3.5%), durable goods and initial claims, plus the 2:00 ET Beige Book**; Thursday 26 November is Thanksgiving and the market is closed; Friday 27 November has the preliminary December consumer sentiment and existing home sales. The October FOMC minutes were released on 18 November, so no minutes release is pending. The 2-year auction on Monday afternoon is the first live read on whether the 14bp fall in the 10-year is demand or flight-to-quality. Note one calendar disagreement: Scotiabank's release calendar lists Monday 23 November as having no US releases, while the JPMorgan, Investrade and MarketWatch calendars all carry the flash PMIs that morning.

### Earnings calendar

Vendor calendars disagree on both the count and the names for Monday. Nasdaq-derived (StockTitan): 9 companies worth $2B+ report, **all after the close**, none before the open. EarningsWhispers: 23 companies, 4 before the open and 19 after. Nexqual (US names above $300M): 19, of which 2 before the open. Seeking Alpha: 35. The roster below is the **intersection of at least two sources**; EPS estimates are published as each vendor states them, and they disagree materially.

| Ticker | Company | When | EPS est. (vendor) | Sources |
|---|---|---|---|---|
| HPE | Hewlett Packard Enterprise | AMC, 5:00 PM | 1.17 (Nasdaq) / 1.28 (Nexqual) / 1.27 (SuperCharting) | 4 |
| A | Agilent Technologies | AMC, 4:30 PM | 1.72 (Nasdaq) / 1.73 (Nexqual) / 1.73 (SuperCharting) | 4 |
| ZM | Zoom Communications | AMC, 5:00 PM | 1.00 (Nasdaq) / 1.50 (Nexqual) / 1.49 (SuperCharting) | 4 |
| SYM | Symbotic | AMC, 5:00 PM | 0.08 (Nasdaq) / 0.16 (Nexqual) | 3 |
| J | Jacobs Solutions | AMC, 4:30 PM | 2.11 (Nasdaq) / 2.12 (Nexqual) | 3 |
| SMTC | Semtech | AMC | 1.13 (Nexqual) | 3 |
| AMTM | Amentum Holdings | AMC | 0.66 (Nexqual) | 2 |
| DAC | Danaos | AMC | — | 3 |
| CENT | Central Garden & Pet | AMC | -0.06 (Nexqual) | 3 |
| CMP | Compass Minerals | AMC | -0.03 (Nexqual) | 3 |
| FLNC | Fluence Energy | AMC | -0.61 (Nexqual) | 2 |
| VNET | VNET Group | BMO | -0.22 (Nexqual) | 2 |

Further names appearing in two or more vendors below $2B: TUYA, PFLT, ALCO, ZEPP, LOCL, EPSN, FSCO, PNNT, BLRX, CRGO, THCH, HTT. The count disagreement is real and is not reconciled here — what is reconciled is the roster.

### News to watch for the top movers

The day's three largest liquid decliners had **no company-specific news**; the driver was sector-wide.

- **APLD -17.81% to 11.49** — AI data-centre/neocloud builder; no press release or filing on the day. The proximate trigger was the Anthropic listing failing to revive the trade, and the group's debt-funded growth capital being repriced; Nvidia has trimmed committed neocloud volume to roughly $32B from $36B, with new commitments conditioned on customers financing themselves.
- **HUT -17.65% to 45.95** — same neocloud/crypto-miner-to-AI cohort (with CORZ, IREN, NBIS, CRWV); an index-level de-rating of the group, not a single-name event.
- **AAOI -16.55% to 32.93** — optical transceivers; Thursday's optics rebound unwound, on top of a $550M at-the-market equity programme disclosed 17 November. Guidance for Q4 revenue is $385M–$420M and the next test is whether it holds while the sell-off continues.

Also worth carrying into Monday: **GAP +11.44% to 20.94** (Q3 net sales $4.0B, +2%, comps flat, full-year sales and adjusted EPS guidance lowered) and **GPN +9.95% to 91.83** (earnings). On the other side, **SVRA -18.23% to 4.26** — the day's largest decliner, but a $875M market cap, so it sits outside the liquid screen used here — after the FDA said it would not act on its molgramostim application by the 22 November target date; and **BLTE -15.65% to 127.38** after the FDA extended its tinlarebant review by three months to 12 May 2027.

### Tomorrow's three things to watch

- **HPE** — 40.91 close, 41.97 after-hours — reports after the close Monday, consensus EPS 1.17 to 1.28 depending on vendor; the AI-server read-across for a complex that just lost 10.73%, and the guidance is the tell.
- **SMTC** — 87.63 close, 90.25 after-hours — reports after the close Monday, consensus EPS 1.13; AI/data-centre connectivity, so it is a second opinion on whether demand is actually slowing.
- **CRWD** — 218.35 after-hours, 229.44 close — the reported Zscaler talks: a signed deal at a premium puts a floor under large-cap security, while a Zscaler fade back below its pre-bid close says the market disbelieves the price.

## Day's tape

### Market read

Population: cron #20's `us-eod/2026-11-20.csv` — 4,881 names, 4,852 with a settled close. The liquid set is the 1,748 names with a market cap above $2B.

| metric | value |
|---|---|
| advancers | 804 |
| decliners | 3,895 |
| unchanged | 153 |
| median_name_move_pct | -1.88 |
| cap_weight_penalty_bp | -166 |
| liquid_adv_dec_ratio | 0.23 (320 advancers vs 1,416 decliners, $2B market-cap floor) |

The distribution was brutally one-sided — 80% of the universe closed lower, the median name lost 1.88%, and the equal-weight index fell less than half as far as the cap-weighted one. The cap-weight penalty of **-166bp** says the sellers were concentrated in the largest names.

### Cap-weight penalty — 5-day history

| Session | SPY % | RSP % | cap_weight_penalty_bp |
|---|---|---|---|
| 2026-11-16 | -1.91 | -1.01 | -90 |
| 2026-11-17 | -1.02 | -1.45 | +43 |
| 2026-11-18 | -0.31 | -0.15 | -15 |
| 2026-11-19 | -1.96 | -1.76 | -20 |
| 2026-11-20 | -3.64 | -1.98 | -166 |

The penalty has been negative in four of the last five sessions — mega caps have been leading the tape down for a week — but today's -166bp is more than double the worst of the prior four.

### Index, ETF and volatility levels

| Instrument | Close | Change | Day range | as_of (ET) |
|---|---|---|---|---|
| S&P 500 | 6,910.39 | -3.70% | 6,882.66–7,198.67 | 16:35 |
| Nasdaq Composite | 22,617.73 | -5.28% | 22,513.01–23,837.76 | 17:15 |
| Dow Jones | 48,147.33 | -1.93% | 47,998.86–49,594.90 | 16:35 |
| Nasdaq-100 | 25,028.98 | -5.61% | 24,910.48–26,429.09 | 17:15 |
| Russell 2000 | 2,581.79 | -2.76% | 2,577.09–2,665.14 | 16:30 |
| PHLX Semiconductor | 8,408.59 | -10.73% | 8,342.21–9,204.42 | 17:15 |
| VIX | 35.89 | +26.20% | 26.94–40.03 | 16:15 |
| VXN | 45.25 | +24.04% | 35.58–48.74 | 16:15 |
| SPY | 689.81 | -3.64% | 686.75–718.29 | 16:00 |
| QQQ | 608.45 | -5.67% | 606.23–643.28 | 16:00 |
| IWM | 256.61 | -2.88% | 256.32–265.85 | 16:00 |
| DIA | 481.08 | -1.87% | 479.41–495.28 | 16:00 |
| RSP | 207.44 | -1.98% | 206.90–213.59 | 16:00 |
| SMH | 400.06 | -10.60% | 396.85–438.44 | 16:00 |
| GLD | 322.87 | -3.67% | 320.95–328.60 | 16:00 |
| TLT | 81.45 | +1.37% | 80.69–81.71 | 16:00 |

Every index row's `as_of` was date-checked against the fire date; all carry 2026-11-20. The volatility indices were read from the dated history (`price_history`) rather than the quote rows and cross-checked to the cent against CBOE's own dated close files: VIX 35.89 and VXN 45.25 for 2026-11-20 in both. The week was the worst since the April 2025 tariff turmoil — Dow -8%, S&P 500 -8.6%, Nasdaq -10% — and both the Dow and the S&P 500 closed in correction territory, more than 10% below their record highs.

Put/call (CBOE daily market statistics): **total 1.01**, index 1.20, equity 0.62, ETP 1.09, VIX 1.10, SPX+SPXW+SPXO 1.21, XSP 1.33, total volume 17,766,692 contracts, open interest 740,262,454 — all from one payload. The session stamp on that payload reads **2026-11-19**, not the fire date; see `## Source health`.

### Cross-asset

| Instrument | Level | Change |
|---|---|---|
| US 10-year yield (^TNX) | 4.912% | -14bp |
| Gold (Dec future, GC=F) | 3,539.00 | -3.98% vs prior settle |
| GLD ETF (session close) | 322.87 | -3.67%; extended-hours print 324.48, +0.50% |
| WTI crude (CL=F) | 83.62 | +1.43% |
| US dollar index (DXY) | 103.84 | +0.03% |
| Bitcoin | 56,788.53 | -3.43% |
| Nikkei 225 (Friday close) | 56,436.65 | -5.06% |
| Hang Seng (Friday close) | 22,410.80 | -3.79% |
| Shanghai Composite (Friday close) | 3,533.79 | -1.22% |
| FTSE 100 | 10,346.34 | -1.02% |
| DAX | 24,802.78 | -2.60% |

Gold deserves two numbers, not one blended figure: the December future settled **-3.98%** against its own prior settle of 3,685.50, while the GLD ETF's thin extended-hours book printed only **+0.50%** against its own 16:00 close. The futures are the session signal; the ETF's after-hours book reprices lazily. Rates and gold falling together with equities is the signature of a growth scare, while oil was the one commodity that rose — consistent with the Iran risk in the tape, not with a demand shock.

### Day's movers

Bridge `get_quotes` as the quote source of record (one source per field); the universe screen is the $2B market-cap floor.

| Ticker | Close | Change | Catalyst |
|---|---|---|---|
| GAP | 20.94 | +11.44% | Q3 net sales $4.0B, +2%, comps flat; full-year sales and adjusted EPS guidance lowered (released Thursday 16:15 ET) |
| GPN | 91.83 | +9.95% | quarterly results |
| BKE | 44.15 | +5.67% | retail read-through from the apparel complex |
| HTFL | 46.69 | +4.62% | medtech bid |
| PLMR | 163.59 | +4.41% | insurance |
| APLD | 11.49 | -17.81% | AI data-centre complex de-rating; no company news |
| HUT | 45.95 | -17.65% | neocloud complex de-rating; no company news |
| AAOI | 32.93 | -16.55% | optics unwind; $550M ATM programme disclosed 17 Nov |
| CIFR | 5.435 | -16.13% | neocloud/compute complex de-rating |
| SNDK | 79.24 | -16.05% | memory/AI-storage unwind |
| NVDA | 125.53 | -14.01% | SEC probing Nvidia's accounting practices; chip export restrictions; leadership vacuum |
| MU | 594.51 | -13.89% | memory capex doubts |
| AMD | 424.39 | -13.25% | firmware-security scrutiny and Chinese-entity questions |
| BLTE | 127.38 | -15.65% | FDA extended the tinlarebant review by three months |
| BE | 142.39 | -15.30% | AI infrastructure unwind |
| CRDO | 99.86 | -15.20% | connectivity unwind |
| INTU | 270.44 | -12.77% | Mailchimp sale to Bending Spoons; Credit Karma revenue outlook trimmed |
| AVGO | 304.41 | -12.19% | AI networking unwind |
| GLW | 94.38 | -10.94% | optical components unwind |
| ANT | 88.91 | -8.50% | Anthropic gave back most of its +17% debut-day gain, priced at $83 |
| TSLA | 345.82 | -7.64% | high-beta risk-off |

### Watchlist EOD review

| Ticker | Close | Day change | Day range | Volume | Volume vs avg | After-hours print |
|---|---|---|---|---|---|---|
| AAPL | 342.56 | -1.90% | 340.56–354.34 | 80,568,107 | 1.49x | 344.87, +0.67% |
| MSFT | 484.52 | -2.77% | 481.03–503.80 | 47,191,205 | 1.53x | 489.50, +1.03% |
| NVDA | 125.53 | -14.01% | 124.50–143.73 | 630,309,205 | 2.88x | 130.01, +3.57% |
| GOOGL | 265.29 | -2.70% | 264.22–283.15 | 57,606,333 | 1.50x | 270.18, +1.84% |
| AMZN | 246.82 | -4.10% | 245.31–259.97 | 74,362,636 | 1.30x | 251.00, +1.69% |
| IWM | 256.61 | -2.88% | 256.32–265.85 | 57,460,818 | n/a (ETF, not in the equity universe) | 258.67, +0.80% |
| GLD | 322.87 | -3.67% | 320.95–328.60 | 23,643,329 | n/a (ETF) | 324.48, +0.50% |
| TLT | 81.45 | +1.37% | 80.69–81.71 | 65,439,820 | n/a (ETF) | 81.09, -0.44% |

Every watchlist name but TLT fell. The extended-hours tape was mildly constructive across the mega caps — Nvidia +3.57% off a 14% collapse, Alphabet +1.84% — which is a bounce, not a reversal.

## Sector rotation

Cap-weighted returns are computed on one row per `cap_source_symbol` (share classes de-duplicated, `CAP_CARRIED` carrier rows dropped in favour of the primary listing), excluding `EX_DISTRIBUTION`, `NO_CAP` and `NO_SECTOR` rows. Coverage: **4,193 of 4,881 names** (86%) enter the cap-weighted columns. Every published cap-weighted return was asserted inside ±20%.

| Sector | Cap-weighted % | Median % | Sector ETF | ETF % | Gap | Dominant constituent |
|---|---|---|---|---|---|---|
| **Consumer Staples** (top 1) | +0.71 | -0.50 | XLP | +0.67 | +0.04pp | WMT +1.59%, +0.39pp of the sector |
| **Health Care** (top 2) | -0.41 | -2.73 | XLV | -0.12 | -0.29pp | LLY -0.22%, -0.04pp |
| **Energy** (top 3) | -0.69 | -2.62 | XLE | -0.62 | -0.07pp | XOM +0.69%, +0.16pp |
| **Utilities** | -0.82 | -0.33 | XLU | -0.74 | -0.08pp | NEE -0.33% |
| **Real Estate** | -0.92 | -0.71 | XLRE | -0.98 | +0.06pp | WELL -1.15% |
| **Financials** | -1.83 | -0.80 | XLF | -1.82 | -0.01pp | BRK-B -0.35% |
| **Materials** | -2.94 | -3.88 | XLB | -2.19 | **-0.75pp** | LIN -1.45% |
| **Communication Services** | -2.98 | -2.68 | XLC | -2.66 | -0.32pp | GOOGL -2.71%, -1.40pp |
| **Consumer Discretionary** (bottom 3) | -3.55 | -2.21 | XLY | -2.95 | **-0.60pp** | AMZN -4.12%, -1.46pp; ex-AMZN **-3.24%** |
| **Industrials** (bottom 2) | -4.14 | -3.85 | XLI | -3.09 | **-1.05pp** | SPCX -7.66%, -1.58pp; ex-SPCX **-3.22%** |
| **Information Technology** (bottom 1) | -6.53 | -6.60 | XLK | -7.27 | **+0.74pp** | AAPL -1.89%, -0.43pp; ex-AAPL **-7.88%** |

Two gaps exceed 0.5pp and are constituent effects, not rotations. **Industrials** is the clearest: Space Exploration Technologies ($1.68T cap, -7.66%) is -1.58pp of the sector's -4.14%; ex-SPCX the sector was -3.22%, against XLI's -3.09% — a 0.13pp gap, i.e. the whole gap was one constituent. **Consumer Discretionary** is similar: ex-AMZN the sector was -3.24% against XLY's -2.95%. For **Information Technology** the direction reverses — the cap-weighted column (-6.53%) is *better* than XLK (-7.27%), and removing the single largest constituent (Apple, -1.89%) makes the sector worse (-7.88%), because the ETF's heavier semiconductor weighting is what dragged it lower. The cap-weighted column inherits mega-cap concentration in general: Apple, Microsoft, Nvidia and Broadcom alone carry roughly $12.2T of the sector's $22.2T.

The defensiveness was in the index, not in the stocks: Consumer Staples' cap-weighted return is positive but its **median name still fell 0.50%**, and Health Care's median (-2.73%) is far worse than its cap-weighted print (-0.41%). Staples survived because of Walmart, not because the sector held up.

## After-hours movers

TradingView extended-hours screen: US stocks and DRs above $1B market cap with more than 50,000 after-hours shares. Every row was verified against the identity `postmarket_change == (postmarket_close - close) / close x 100` — **10 of 10 pass** — and every prior close was confirmed against the bridge `get_quotes` (10 of 10 match). All ten venues are NASDAQ, NYSE or AMEX; no OTC line is published.

| ticker | prior_close | ah_last | ah_high | ah_low | ah_volume | gap_pct | ah_range_pct | gap_fill_level |
|---|---|---|---|---|---|---|---|---|
| ZS | 194.82 | 226.68 | 246.06 | 194.82 | 1,432,504 | +16.35 | 26.30 | 194.82 |
| KYMR | 115.31 | 124.06 | 133.70 | 115.01 | 297,146 | +7.59 | 16.21 | 115.31 |
| FRMI | 1.95 | 2.0876 | 2.1495 | 1.90 | 2,560,864 | +7.06 | 12.79 | 1.95 |
| LBRT | 10.755 | 11.4949 | 11.4949 | 10.755 | 605,196 | +6.88 | 6.88 | 10.755 |
| ACMR | 39.80 | 42.49 | 42.49 | 39.80 | 246,465 | +6.76 | 6.76 | 39.80 |
| PRAX | 300.43 | 275.00 | 300.55 | 275.00 | 128,928 | -8.46 | 8.50 | 300.43 |
| CRWD | 229.44 | 218.345 | 231.16 | 201.11 | 3,169,370 | -4.84 | 13.10 | 229.44 |
| LFST | 13.82 | 13.1857 | 13.98 | 13.1857 | 1,408,646 | -4.59 | 5.75 | 13.82 |
| CBRL | 70.75 | 67.62 | 70.75 | 67.62 | 94,723 | -4.42 | 4.42 | 70.75 |
| UVE | 48.49 | 46.4449 | 48.49 | 46.4449 | 50,369 | -4.22 | 4.22 | 48.49 |

`gap_fill_level` is the prior close wherever the after-hours low traded at or below it and the high at or above it — true for all ten rows — otherwise the after-hours midpoint. The gap fills at the close in every case here, so a Monday gap that retraces the whole move hands the level back.

Two readings worth flagging. Zscaler printed as much as **+18%** intraday after hours (a high of 246.06 against a 194.82 close) and was last at +16.35% in this snapshot; vendors quote the move at different minutes, so the level moved while the brief was being written. CrowdStrike's after-hours book is wide — a 201.11 low against a 231.16 high on 3.2M shares, a 13.10% range — because the merger headline hit at 16:11 ET and the book never settled.

**The table is not the whole after-hours tape.** The screen has a $1B market-cap floor, and the session's actual leaderboard sits below it: WETO +373.48%, MRM +79.13% and NAK +25.00% on the upside, and CAPR -78.33%, VWAV -28.65% and TOVX -25.08% on the downside. Those are micro-cap prints and are named here only so the published table is not mistaken for the night.

## After-hours earnings reactions

Only one name on the published screen had a company-specific after-hours catalyst, and it was not an earnings report at all.

- **ZS +16.35% (last 226.68, high 246.06)** — Bloomberg and Reuters reported at ~16:11 ET that **CrowdStrike is in talks to acquire Zscaler**; Bloomberg said the two sides are discussing a transaction that could come together soon but that there is no certainty of a deal. No price or financing terms were disclosed. Zscaler separately released a partnership announcement at 16:05 ET (Anthropic's Claude model integrated into its Exploit Paths feature, plus European service work with Mistral). The reported combination would be worth roughly $265B, among the largest deals in cybersecurity.
- **CRWD -4.84% (last 218.345, low 201.11)** — the same report, the other side of it. The post-headline book traded from -12.3% at the low to -4.84% at the last print.
- **PRAX -8.46% (300.43 to 275.00)** — no sourced company release was found for the move; the after-hours range is wide on 128,928 shares.
- **KYMR +7.59%, FRMI +7.06%, LBRT +6.88%, ACMR +6.76%, LFST -4.59%, CBRL -4.42%, UVE -4.22%** — no company release was found for these prints; they are continuation of the day's factor moves (Kymera and ACMR in biotech/semis, Liberty and Fluence in energy and storage, LifeStance and Cracker Barrel in consumer services) rather than earnings reactions.

No name on the watchlist reported after the close.

## Open research queue

1. **Is this an AI-capex de-rating, a financing event, or both?** It matters because the two have different follow-through: a de-rating resolves on capex guidance, a financing event resolves on credit spreads. What would resolve it: the Monday $69B 2-year auction (a tail means the discount rate is doing the work) against Wednesday's core PCE and 3Q GDP; if the auction clears and the complex still sells, it is pure de-rating.
2. **Does the CrowdStrike–Zscaler talk reprice enterprise software as a whole?** A signed deal at a double-digit premium would put a floor under large-cap security and pull a bid into a sector that sold off today; a fade in Zscaler below its pre-bid 194.82 close says the market disbelieves the price. Resolves on the Monday open and any confirmation language.
3. **How much of this is a growth scare and how much is a funding scare?** Rates and gold fell together (10-year -14bp, gold -3.98%) while oil rose on Iran risk — a growth scare with an inflation tail. Resolves on WTI, the 11 December federal funding deadline, and whether the two-year auction clears; if oil and the 10-year both keep falling while equities fall, it is the growth leg.

## Source health

| Source | URL / query | Status | What it changed |
|---|---|---|---|
| Bridge `market-recap` `get_quotes` | `^GSPC,^IXIC,^DJI,^RUT,^VIX,^VXN,^NDX,^SOX,SPY,QQQ,IWM,DIA,RSP,SMH,GLD,TLT,ES=F,NQ=F,YM=F,RTY=F,ZN=F,GC=F` + 62 follow-up symbols | ok (7 calls, batched) | quote source of record; every index row's `as_of` date-checked against the fire date |
| Bridge `market-recap` `price_history` | SPY, RSP, ^VIX, ^VXN, 2026-11-03 to 2026-11-20 | ok | cap-weight penalty 5-session history; the dated volatility closes |
| Bridge `market-recap` `market_snapshot` | {} | ok | Asia/Europe closes, 10-year yield, DXY, crude, gold, bitcoin |
| TradingView scanner (validated client `tv_scan.py`, marker TV_SCAN_V2) | 4 scans: after-hours up/down, small-cap up/down; 1 targeted pull for the watchlist; 1 targeted pull for the earnings-calendar names | ok | after-hours levels; watchlist after-hours prints |
| TradingView futures scanner | `CME_MINI:ES1!,NQ1!,RTY1!`, `CBOT_MINI:YM1!` | ok, **degraded** | returned only a post-close **indicative** print (ES1! 6,935, update_time 19:54 ET) — the CME week was closed; an observation, not an overnight setup. One duplicate row (`ASX24:ES1!`, an electricity future) was discarded |
| CBOE daily market statistics | `https://www.cboe.com/us/options/market_statistics/daily/` | ok, **degraded** | payload's `selectedDate` is **2026-11-19**, one session before the fire date — the 20 November statistics were not published at the 22:30 fire. Ratios are from the 19 November session |
| CBOE dated index closes | `cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv`, `VXN_History.csv` | ok | cross-check of the VIX/VXN closes to the cent |
| cron #20 EOD universe | `karizaco/minimax-cloud-outputs` `us-eod/2026-11-20.csv` | ok, **degraded** | two row-level defects: SNDK's `change_pct` reads **-89.51%** against an unadjusted prior close (bridge: -16.05% on the same 79.24 close) and is flagged `EX_DISTRIBUTION|SPLIT_ADJUSTED`; NVDA's row is flagged `settle_status=UNCONFIRMED` with close 128.10 against the bridge's 125.53. SNDK was therefore published from the bridge, and NVDA's change from the bridge. The participation counts are unaffected (both names closed lower either way) |
| Watchlist | `refs/watchlist.yaml` on the outputs repo | ok | 8 names, published as the universe's watchlist |
| `web_search` | market drivers, Zscaler/CrowdStrike report, earnings and economic calendars | ok | catalysts and calendars; see the vendor disagreements disclosed above |

**Degraded sources: 3** — (1) the futures source, which on a Friday cannot supply an overnight print at all; (2) the CBOE put/call page, whose latest published session is 19 November rather than the fire date; (3) the cron #20 universe CSV, whose SNDK and NVDA rows forced two published mover numbers to be taken from the bridge instead. The absent `mcp__*` tool names are not a degraded source; the bridge reached its server over plain HTTPS JSON-RPC throughout.

## Method notes

- **The fire is a Friday fire.** `scheduled_at_ms` 1795231804548 resolves to 2026-11-20 22:30 ET; the next session is Monday 23 November. The Asia figures published above are Friday's own closed cash session, which ran during the US session — there is no Sunday-open leg to publish, and the post-18:00 ET Globex move does not exist yet.
- **One source per field.** Prices, changes and levels come from the bridge `market-recap`; the TradingView scanner supplies the extended-hours prints and the universe screen; cron #20's CSV supplies the participation population and the sector classification (its taxonomy is carried forward, its moves and caps are not used for the published mover table); CBOE supplies the put/call ratio and the dated volatility closes. Where two sources disagree by more than 0.6% the bridge wins and the other is named in `## Source health`.
- **Cap-weighted columns** use one row per `cap_source_symbol`, keep the non-`CAP_CARRIED` listing, and drop `EX_DISTRIBUTION`, `NO_CAP` and `NO_SECTOR` rows (2,132 flagged rows excluded). Every published cap-weighted return was asserted inside ±20% before publication, and each sector was cross-checked against its ETF with the gap published.
- **After-hours rows** were accepted only after passing the identity check and a venue check; `gap_fill_level` follows the fixed rule (prior close when the after-hours range brackets it, otherwise the after-hours midpoint). The print is a snapshot as of the fire and the tape was still moving while the brief was written.
- The put/call components published above all come from the same CBOE payload and reconcile with the total; no component split was invented across sources.
- Read-only. No trades, no positions, no advice.
