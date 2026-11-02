# Earnings reaction scanner — 2026-11-02

- Cron: `0 8 * * 1-5` America/New_York (weekdays, 08:00 ET)
- Fire time (ET): 2026-11-02 08:11:11 Mon
- Run type: `scheduled_scan`
- Source: TradingView public screener (`scanner.tradingview.com/<market>/scan`);
  Yahoo chart API as an independent cross-check on the reported movers.
- Method: 4 passes (US top-200 mcap, US prior-session movers, EU/UK movers,
  ASX movers). Volume floor 10,000 on every pass; `country` filter for
  primary listings; exchange drop-list applied.
- Status: `ok`

## TL;DR

- 0 AMC reactions, 73 pre-market gaps, 85 without extended-hours data; 29 EU/UK and 3 ASX movers.
- Biggest US extended-hours move: PGEN PRE_GAP (30.55%).
- Biggest EU/UK move: ALO (-25.02%, france).
- Biggest ASX move: HLI (-7.93%).
- EU/AU earnings-driven tagging is keyword-based on headlines (best-effort).

## US — Headline table

| Ticker | Venue | Close | Chg % | Pre-mkt % | Post-mkt % | Last earnings | Tag |
|---|---|---|---|---|---|---|---|
| PGEN | NASDAQ | 6.94 | 4.52 | -30.55 | — | 2026-08-04 (90d ago) | PRE_GAP |
| RSI | NYSE | 12.12 | -11.01 | -5.86 | — | 2026-10-28 (5d ago) | PRE_GAP |
| CHRN | NASDAQ | 14.38 | -7.91 | 4.38 | — | 2026-10-15 (18d ago) | PRE_GAP |
| COHR | NYSE | 210.32 | -11.34 | 4.35 | — | 2026-08-12 (82d ago) | PRE_GAP |
| INIO | NASDAQ | 16.3 | -6.96 | 4.29 | — | 2026-10-27 (6d ago) | PRE_GAP |
| TEM | NASDAQ | 72.22 | -7.22 | 3.85 | — | 2026-11-02 (0d ago) | PRE_GAP |
| RIG | NYSE | 6.94 | 3.74 | -3.79 | — | 2026-08-05 (89d ago) | PRE_GAP |
| WULF | NASDAQ | 11.73 | -8.00 | 3.75 | — | 2026-08-05 (89d ago) | PRE_GAP |
| CRWV | NASDAQ | 54.87 | -9.66 | 3.43 | — | 2026-08-11 (83d ago) | PRE_GAP |
| NTSK | NASDAQ | 24.3 | -7.22 | 3.29 | — | 2026-09-02 (61d ago) | PRE_GAP |
| FORM | NASDAQ | 87.53 | -10.19 | 3.28 | — | 2026-10-28 (5d ago) | PRE_GAP |
| GRAL | NASDAQ | 143.43 | -9.75 | 3.21 | — | 2026-08-05 (89d ago) | PRE_GAP |
| RIVN | NASDAQ | 12.16 | 6.20 | 3.21 | — | 2026-10-29 (4d ago) | PRE_GAP |
| RAPP | NASDAQ | 25.05 | 3.47 | 3.19 | — | 2026-08-05 (89d ago) | PRE_GAP |
| MAR | NASDAQ | 399.3 | -0.09 | 3.18 | — | 2026-11-02 (0d ago) | PRE_GAP |
| STDN | NYSE | 11.97 | -6.92 | 3.09 | — | 2026-08-26 (68d ago) | PRE_GAP |
| AEHR | NASDAQ | 54.89 | -10.33 | 3.08 | — | 2026-07-14 (111d ago) | PRE_GAP |
| AXTI | NASDAQ | 55.06 | -9.56 | 3.03 | — | 2026-10-29 (4d ago) | PRE_GAP |
| POWI | NASDAQ | 43.86 | -10.54 | 3.03 | — | 2026-08-05 (89d ago) | PRE_GAP |
| ACMR | NASDAQ | 45.47 | -7.75 | 2.93 | — | 2026-08-07 (87d ago) | PRE_GAP |
| PENG | NASDAQ | 51.93 | -11.67 | 2.91 | — | 2026-10-06 (27d ago) | PRE_GAP |
| CRWD | NASDAQ | 250.43 | -4.10 | 2.90 | — | 2026-08-26 (68d ago) | PRE_GAP |
| AAON | NASDAQ | 67.4 | -10.49 | 2.80 | — | 2026-08-10 (84d ago) | PRE_GAP |
| UCTT | NASDAQ | 49.71 | -9.12 | 2.80 | — | 2026-10-27 (6d ago) | PRE_GAP |
| ATEC | NASDAQ | 7.04 | -38.08 | 2.80 | — | 2026-10-29 (4d ago) | PRE_GAP |
| LNG | NYSE | 330.32 | 3.57 | -2.79 | — | 2026-10-29 (4d ago) | PRE_GAP |
| ALHC | NASDAQ | 7.27 | -9.80 | 2.75 | — | 2026-10-29 (4d ago) | PRE_GAP |
| RMBS | NASDAQ | 84.65 | -6.97 | 2.74 | — | 2026-10-26 (7d ago) | PRE_GAP |
| DOCN | NYSE | 89.65 | -10.32 | 2.73 | — | 2026-08-04 (90d ago) | PRE_GAP |
| TSEM | NASDAQ | 166.48 | -11.41 | 2.72 | — | 2026-11-02 (0d ago) | PRE_GAP |
| AGIO | NASDAQ | 30.55 | -17.94 | 2.65 | — | 2026-07-30 (95d ago) | PRE_GAP |
| SITM | NASDAQ | 447.06 | -8.40 | 2.63 | — | 2026-08-05 (89d ago) | PRE_GAP |
| APP | NASDAQ | 228.5 | -10.36 | 2.63 | — | 2026-08-05 (89d ago) | PRE_GAP |
| FRVO | NASDAQ | 8.275 | -7.95 | 2.60 | — | 2026-08-12 (82d ago) | PRE_GAP |
| PBF | NYSE | 78 | 3.26 | -2.55 | — | 2026-10-29 (4d ago) | PRE_GAP |
| NBIS | NASDAQ | 154.14 | -10.38 | 2.54 | — | 2026-08-12 (82d ago) | PRE_GAP |
| SECZ | NYSE | 7.56 | -10.32 | 2.51 | — | 2026-08-12 (82d ago) | PRE_GAP |
| WOLF | NYSE | 21.98 | -11.90 | 2.46 | — | 2026-08-19 (75d ago) | PRE_GAP |
| ABSI | NASDAQ | 11.13 | -8.02 | 2.43 | — | 2026-08-11 (83d ago) | PRE_GAP |
| KLIC | NASDAQ | 74.21 | -6.86 | 2.43 | — | 2026-08-05 (89d ago) | PRE_GAP |
| SU | NYSE | 79.42 | 2.31 | -2.42 | — | 2026-08-04 (90d ago) | PRE_GAP |
| ICHR | NASDAQ | 38.9 | -8.32 | 2.42 | — | 2026-08-03 (91d ago) | PRE_GAP |
| FIGR | NASDAQ | 21.58 | -8.52 | 2.41 | — | 2026-08-13 (81d ago) | PRE_GAP |
| POWL | NASDAQ | 156.26 | -7.25 | 2.39 | — | 2026-08-03 (91d ago) | PRE_GAP |
| AUGO | NASDAQ | 66.22 | -15.43 | 2.39 | — | 2026-08-05 (89d ago) | PRE_GAP |
| PLPC | NASDAQ | 291.15 | -9.02 | 2.36 | — | 2026-10-28 (5d ago) | PRE_GAP |
| UI | NYSE | 563.81 | -7.07 | 2.34 | — | 2026-08-21 (73d ago) | PRE_GAP |
| PTEN | NASDAQ | 13.32 | 4.96 | -2.33 | — | 2026-10-28 (5d ago) | PRE_GAP |
| GDYN | NASDAQ | 13.36 | 40.78 | -2.32 | — | 2026-10-29 (4d ago) | PRE_GAP |
| TMUS | NASDAQ | 156.44 | 6.21 | -2.29 | — | 2026-10-28 (5d ago) | PRE_GAP |
| BUUU | NASDAQ | 6.11 | 4.62 | -2.29 | — | — | PRE_GAP |
| ARIS | NYSE | 14.43 | -9.13 | 2.29 | — | 2026-07-29 (96d ago) | PRE_GAP |
| CRML | NASDAQ | 7.16 | -9.94 | 2.29 | — | 2026-09-25 (38d ago) | PRE_GAP |
| VAL | NYSE | 105.31 | 3.54 | -2.28 | — | 2026-08-05 (89d ago) | PRE_GAP |
| CAMT | NASDAQ | 116.68 | -7.89 | -2.26 | — | 2026-08-10 (84d ago) | PRE_GAP |
| AAOI | NASDAQ | 69.05 | -12.80 | 2.24 | — | 2026-08-06 (88d ago) | PRE_GAP |
| VZ | NYSE | 44.73 | 2.45 | -2.24 | — | 2026-10-26 (7d ago) | PRE_GAP |
| VICR | NASDAQ | 191.09 | -7.52 | 2.23 | — | 2026-10-20 (13d ago) | PRE_GAP |
| AEIS | NASDAQ | 222.06 | -7.38 | 2.23 | — | 2026-08-03 (91d ago) | PRE_GAP |
| OUST | NASDAQ | 29.74 | -7.47 | 2.22 | — | 2026-08-06 (88d ago) | PRE_GAP |
| BTDR | NASDAQ | 6.71 | -11.48 | 2.22 | — | 2026-08-10 (84d ago) | PRE_GAP |
| IAG | NYSE | 15.45 | -7.71 | 2.20 | — | 2026-08-06 (88d ago) | PRE_GAP |
| TBBK | NASDAQ | 46.75 | -7.46 | 2.14 | — | 2026-10-29 (4d ago) | PRE_GAP |
| TXG | NASDAQ | 70.11 | -14.03 | 2.13 | — | 2026-08-06 (88d ago) | PRE_GAP |
| GLW | NYSE | 123.31 | -4.32 | 2.12 | — | 2026-10-27 (6d ago) | PRE_GAP |
| PPTA | NASDAQ | 16.65 | -7.81 | 2.10 | — | 2026-08-15 (79d ago) | PRE_GAP |
| LSCC | NASDAQ | 92.97 | -9.74 | 2.09 | — | 2026-08-04 (90d ago) | PRE_GAP |
| APLD | NASDAQ | 17.815 | -8.22 | 2.09 | — | 2026-10-07 (26d ago) | PRE_GAP |
| SBET | NASDAQ | 6.74 | -6.78 | 2.08 | — | 2026-08-10 (84d ago) | PRE_GAP |
| SMTC | NASDAQ | 127.38 | -9.56 | 2.06 | — | 2026-08-25 (69d ago) | PRE_GAP |
| PARR | NYSE | 76.24 | 4.00 | -2.03 | — | 2026-08-04 (90d ago) | PRE_GAP |
| ERO | NYSE | 29.05 | -6.65 | 2.03 | — | 2026-08-05 (89d ago) | PRE_GAP |
| DDOG | NASDAQ | 235.27 | -11.50 | 2.02 | — | 2026-08-06 (88d ago) | PRE_GAP |

## US — QUIET one-liners

| Ticker | Venue | Chg % | Pre-mkt % | Post-mkt % |
|---|---|---|---|---|
| CRDO | NASDAQ | -8.65 | 1.99 | — |
| NEXA | NYSE | -7.67 | 1.99 | — |
| TWST | NASDAQ | -11.92 | 1.96 | — |
| HBM | NYSE | -7.11 | 1.94 | — |
| NVTS | NASDAQ | -7.83 | 1.93 | — |
| ONTO | NYSE | -9.16 | 1.90 | — |
| ONDS | NASDAQ | -8.14 | 1.90 | — |
| VRT | NYSE | -5.46 | 1.89 | — |
| CORZ | NASDAQ | -8.18 | 1.89 | — |
| GLXY | NASDAQ | -11.75 | 1.88 | — |
| QNT | NASDAQ | -10.39 | 1.87 | — |
| RIOT | NASDAQ | -6.77 | 1.87 | — |
| FDXF | NYSE | 14.91 | -1.87 | — |
| STX | NASDAQ | -7.98 | 1.85 | — |
| PSX | NYSE | 3.37 | -1.83 | — |

## EU/UK — Headline table

| Ticker | Market | Venue | Close | Chg % | Currency | Last earnings |
|---|---|---|---|---|---|---|
| ALO | france | EURONEXT | 11.855 | -25.02 | EUR | 2026-05-13 |
| CBRAIN | denmark | OMXCOP | 104.4 | +9.89 | DKK | 2026-08-20 |
| YUBICO | sweden | OMXSTO | 134.7 | -8.86 | SEK | 2026-08-06 |
| BMAG | austria | VIE | 37.3 | +8.59 | EUR | — |
| CMBN | switzerland | SIX | 82 | -8.02 | CHF | 2026-07-23 |
| MED | switzerland | SIX | 104.2 | +7.31 | CHF | 2026-08-18 |
| FAG | sweden | OMXSTO | 12.16 | -6.89 | SEK | 2026-10-28 |
| GPW | poland | GPW | 96.2 | -6.05 | PLN | 2026-09-03 |
| XTB | poland | GPW | 131.28 | -6.05 | PLN | 2026-07-29 |
| ACT0 | germany | XETR | 140.4 | -5.90 | EUR | 2026-10-29 |
| LOOMIS | sweden | OMXSTO | 525 | -5.75 | SEK | 2026-10-30 |
| NSKOG | norway | OSL | 34.55 | -5.73 | NOK | 2026-10-22 |
| XANO_B | sweden | OMXSTO | 40.65 | -5.57 | SEK | — |
| HUNT | norway | OSL | 18.34 | +5.28 | NOK | 2024-05-30 |
| AQUA | norway | OSL | 8.68 | -5.24 | NOK | 2026-10-29 |
| JSW | poland | GPW | 26.11 | -5.23 | PLN | 2026-09-15 |
| SVIK | sweden | OMXSTO | 196.2 | -5.22 | SEK | 2026-10-23 |
| FGP | uk | LSE | 227.2 | +4.80 | GBX | 2025-11-18 |
| SNT | poland | GPW | 312 | -4.59 | PLN | 2026-08-05 |
| ENGCON_B | sweden | OMXSTO | 56.6 | -4.55 | SEK | 2026-10-29 |
| NANO | france | EURONEXT | 26.84 | -4.55 | EUR | 2026-09-24 |
| SZG | germany | XETR | 49.24 | +4.54 | EUR | 2026-08-11 |
| NELLY | sweden | OMXSTO | 34.2 | -4.52 | SEK | 2023-02-02 |
| KNOW | sweden | OMXSTO | 122.2 | +4.27 | SEK | 2026-10-23 |
| CIRSA | spain | BME | 19.08 | +4.26 | EUR | 2026-07-30 |
| RYA | ireland | EURONEXT | 23.86 | +4.19 | EUR | 2026-07-20 |
| ELTEL | sweden | OMXSTO | 16 | -4.19 | SEK | 2026-10-29 |
| TOR | poland | GPW | 65 | -4.13 | PLN | 2026-08-20 |
| HEBA_B | sweden | OMXSTO | 22.7 | +4.13 | SEK | 2026-10-21 |

## AU (ASX) — Headline table

| Ticker | Venue | Close | Chg % | Currency | Last earnings |
|---|---|---|---|---|---|
| HLI | ASX | 4.99 | -7.93 | AUD | 2026-08-10 |
| NST | ASX | 24.07 | -4.75 | AUD | 2026-08-19 |
| BOQCD | ASX | 7.05 | -4.08 | AUD | 2026-10-13 |

## Catalysts

| Ticker | Region | Catalyst | Earnings-driven |
|---|---|---|---|
| PGEN | US | -30.55% pre-mkt: Inovio's rival Voceryq won FDA accelerated approval (announced Fri Oct 30) for recurrent respiratory papillomatoma, competing directly with Precigen's Papzimeos; retail buyout chatter persists. Q3 due Nov 4. | N |
| RSI | US | -5.86% pre-mkt after -11.01% on Oct 30: Q3 results (Oct 28) — revenue $385.9M, +39% y/y but below analyst estimates, GAAP net income $28.7M (+93%), adj EBITDA $62.2M (+73%), MAUs 907,881 (+42%); FY guidance reiterated ($1.56-1.60B revenue, $245-265M adj EBITDA). | Y |
| CHRN | US | +4.38% pre-mkt: no fresh catalyst found (last news: Oct 21 Soluna 50MW Texas LOI; $500M mixed shelf filed Oct 6; Compass Point Buy/$25 initiation was Oct 16). Bounce after the Oct 30 -7.91% session. | N |
| COHR | US | +4.35% pre-mkt after -11.34% on Oct 30: analyst target cuts into the print — Morgan Stanley $375->$325 (Equal-Weight), B. Riley $297->$262 (Neutral); options imply ~8.5% move for Q1 FY2027 results due after the close Nov 4 (consensus adj EPS $1.98 on $2.30B revenue). | N |
| INIO | US | +4.29% pre-mkt after -6.96% on Oct 30: Q3 results (Oct 27) — record revenue $1.17B (+57% y/y, first $1B quarter), net income +176%, adj EBITDA +70%, FY2026 guidance raised, $8B backlog; Wall Street Zen upgraded to Buy on Oct 31. | Y |
| ALO | EU | -25.02%: second FY guidance cut — adjusted EBIT margin to ~1% (from 6.5%), free cash flow to -EUR1.5bn (from positive), rail-car output to ~4,000 (from 4,400-4,500), organic sales growth to low-to-mid single digit; H1 adjusted EBIT margin -4% vs +6.4% a year ago on Coradia Max German certification delays, plus a EUR2bn deleveraging plan. | Y |
| CBRAIN | EU | +9.89%: no fresh catalyst found. Most recent company news is the Oct 27 multi-year framework agreement with Deutsche Rentenversicherung Bund; Q3 2026 report due Nov 4. | N |
| BMAG | EU | +8.59%: no fresh catalyst found (Bajaj Mobility AG, Vienna line; H1 2026 results released Aug 27, Q3 2026 call listed for Nov 3). | N |
| HLI | AU | -7.93%: 3Q26 trading update (Oct 30) — year-to-date gross written premiums -53% after the loss of Commonwealth Bank and the expanded government deposit scheme, with rising delinquencies and claim costs as house prices fall. | Y |
| NST | AU | -4.75%: no fresh catalyst found (gold-linked move; most recent company events were the Sept 21 quarterly report and the rejected Gold Fields $27bn bid on Sep 28). | N |

## Source health

- scanner_calls: 39 | scanner_errors: 0
- pipeline_version: 2026-10-26.2
- yahoo_calls: 138 | yahoo_429: 0 | yahoo_errors: 0
- cross_check (screener vs Yahoo, reference-close validation): agree=104 mismatch=23 unverified=1 stale_reference=23
  method: the screener's implied reference close (close / (1 + change/100)) is compared
  with Yahoo's own reference close. A match proves the move was measured against the
  TRUE prior close; a mismatch means the row sits on a STALE reference (phantom move).
  Coverage: every row of the US headline, EU/UK and ASX tables is checked. The US QUIET
  one-liner table is NOT cross-checked.
  Yahoo bar mode: {"closed": 75, "live": 29} (closed = last completed session bar;
  live = in-progress EU/UK session bar, which is what a weekday 08:00 ET EU move needs)
  live drift between the screener snapshot and the later Yahoo print: median=0.00pp max=8.12pp (expected on a live market)
- cross_check mismatches: [{"region": "germany", "symbol": "AIXA.DE", "tv": 5.599, "yahoo": 4.7, "delta": 0.899, "ref_delta_pct": -0.588, "tv_implied_ref": 32.15, "yahoo_ref": 32.34, "yahoo_date": "2026-11-02", "verdict": "stale_reference"}, {"region": "AU", "symbol": "AMP.AX", "tv": -7.48, "yahoo": 1.195, "delta": -8.675, "ref_delta_pct": 1.195, "tv_implied_ref": 2.54, "yahoo_ref": 2.51, "yahoo_date": "2026-10-29", "verdict": "stale_reference"}, {"region": "AU", "symbol": "CYL.AX", "tv": -7.398, "yahoo": -24.76, "delta": 17.362, "ref_delta_pct": -24.76, "tv_implied_ref": 3.92, "yahoo_ref": 5.21, "yahoo_date": "2026-10-29", "verdict": "stale_reference"}, {"region": "AU", "symbol": "4DX.AX", "tv": 6.557, "yahoo": -25.61, "delta": 32.167, "ref_delta_pct": -25.61, "tv_implied_ref": 2.44, "yahoo_ref": 3.28, "yahoo_date": "2026-10-29", "verdict": "stale_reference"}, {"region": "AU", "symbol": "DVP.AX", "tv": -6.138, "yahoo": -1.013, "delta": -5.125, "ref_delta_pct": -1.013, "tv_implied_ref": 3.91, "yahoo_ref": 3.95, "yahoo_date": "2026-10-29", "verdict": "stale_reference"}, {"region": "AU", "symbol": "QAL.AX", "tv": 5.983, "yahoo": -0.847, "delta": 6.83, "ref_delta_pct": -0.847, "tv_implied_ref": 2.34, "yahoo_ref": 2.36, "yahoo_date": "2026-10-29", "verdict": "stale_reference"}, {"region": "AU", "symbol": "REH.AX", "tv": 5.968, "yahoo": 8.439, "delta": -2.471, "ref_delta_pct": 8.439, "tv_implied_ref": 17.09, "yahoo_ref": 15.76, "yahoo_date": "2026-10-29", "verdict": "stale_reference"}, {"region": "AU", "symbol": "TUA.AX", "tv": 5.882, "yahoo": 1.594, "delta": 4.288, "ref_delta_pct": 1.594, "tv_implied_ref": 1.275, "yahoo_ref": 1.255, "yahoo_date": "2026-10-29", "verdict": "stale_reference"}, {"region": "AU", "symbol": "BRE.AX", "tv": -5.867, "yahoo": -7.635, "delta": 1.768, "ref_delta_pct": -7.635, "tv_implied_ref": 1.875, "yahoo_ref": 2.03, "yahoo_date": "2026-10-29", "verdict": "stale_reference"}, {"region": "AU", "symbol": "CU6.AX", "tv": -5.732, "yahoo": -5.988, "delta": 0.256, "ref_delta_pct": -5.988, "tv_implied_ref": 1.57, "yahoo_ref": 1.67, "yahoo_date": "2026-10-29", "verdict": "stale_reference"}, {"region": "AU", "symbol": "NUF.AX", "tv": 5.678, "yahoo": 1.603, "delta": 4.075, "ref_delta_pct": 1.603, "tv_implied_ref": 3.17, "yahoo_ref": 3.12, "yahoo_date": "2026-10-29", "verdict": "stale_reference"}, {"region": "AU", "symbol": "BMN.AX", "tv": 5.341, "yahoo": -7.163, "delta": 12.504, "ref_delta_pct": -7.163, "tv_implied_ref": 3.37, "yahoo_ref": 3.63, "yahoo_date": "2026-10-29", "verdict": "stale_reference"}, {"region": "AU", "symbol": "VUL.AX", "tv": -5.217, "yahoo": -12.548, "delta": 7.331, "ref_delta_pct": -12.548, "tv_implied_ref": 1.15, "yahoo_ref": 1.315, "yahoo_date": "2026-10-29", "verdict": "stale_reference"}, {"region": "AU", "symbol": "WA1.AX", "tv": -4.904, "yahoo": -9.032, "delta": 4.128, "ref_delta_pct": -9.032, "tv_implied_ref": 8.36, "yahoo_ref": 9.19, "yahoo_date": "2026-10-29", "verdict": "stale_reference"}, {"region": "AU", "symbol": "EOS.AX", "tv": -4.812, "yahoo": -5.228, "delta": 0.416, "ref_delta_pct": -5.228, "tv_implied_ref": 8.52, "yahoo_ref": 8.99, "yahoo_date": "2026-10-29", "verdict": "stale_reference"}, {"region": "AU", "symbol": "SLX.AX", "tv": 4.805, "yahoo": -4.31, "delta": 9.115, "ref_delta_pct": -4.31, "tv_implied_ref": 3.33, "yahoo_ref": 3.48, "yahoo_date": "2026-10-29", "verdict": "stale_reference"}, {"region": "AU", "symbol": "C79.AX", "tv": -4.775, "yahoo": -2.466, "delta": -2.309, "ref_delta_pct": -2.466, "tv_implied_ref": 7.12, "yahoo_ref": 7.3, "yahoo_date": "2026-10-29", "verdict": "stale_reference"}, {"region": "AU", "symbol": "G6M.AX", "tv": -4.762, "yahoo": 6.329, "delta": -11.091, "ref_delta_pct": 6.329, "tv_implied_ref": 2.52, "yahoo_ref": 2.37, "yahoo_date": "2026-10-29", "verdict": "stale_reference"}, {"region": "AU", "symbol": "MSB.AX", "tv": -4.425, "yahoo": -2.586, "delta": -1.839, "ref_delta_pct": -2.586, "tv_implied_ref": 2.26, "yahoo_ref": 2.32, "yahoo_date": "2026-10-29", "verdict": "stale_reference"}, {"region": "AU", "symbol": "GGP.AX", "tv": -4.365, "yahoo": -1.598, "delta": -2.767, "ref_delta_pct": -1.598, "tv_implied_ref": 9.85, "yahoo_ref": 10.01, "yahoo_date": "2026-10-29", "verdict": "stale_reference"}, {"region": "AU", "symbol": "EHL.AX", "tv": 4.12, "yahoo": 2.692, "delta": 1.428, "ref_delta_pct": 2.692, "tv_implied_ref": 1.335, "yahoo_ref": 1.3, "yahoo_date": "2026-10-29", "verdict": "stale_reference"}, {"region": "AU", "symbol": "PRN.AX", "tv": 4.061, "yahoo": 0.51, "delta": 3.551, "ref_delta_pct": 0.51, "tv_implied_ref": 1.97, "yahoo_ref": 1.96, "yahoo_date": "2026-10-29", "verdict": "stale_reference"}, {"region": "AU", "symbol": "DRR.AX", "tv": -4.04, "yahoo": -1.0, "delta": -3.04, "ref_delta_pct": -1.0, "tv_implied_ref": 3.96, "yahoo_ref": 4.0, "yahoo_date": "2026-10-29", "verdict": "stale_reference"}]
- stale_rows_dropped: US=none EU=['AIXA'] AU=['AMP', 'CYL', '4DX', 'DVP', 'QAL', 'REH', 'TUA', 'BRE', 'CU6', 'NUF', 'BMN', 'VUL', 'WA1', 'EOS', 'SLX', 'C79', 'G6M', 'MSB', 'GGP', 'EHL', 'PRN', 'DRR']
- us_premarket_check (Yahoo 1-min pre/post feed vs the screener pre-market column): checked=10 within_1pp=7 within_3pp=10 unavailable=0
- markets_with_lt5_rows: ['uk:less=1', 'germany:less=3', 'france:egreater=4', 'france:less=3', 'netherlands:egreater=0', 'netherlands:less=1', 'belgium:egreater=0', 'belgium:less=0', 'portugal:egreater=0', 'portugal:less=0', 'ireland:egreater=1', 'ireland:less=0', 'italy:egreater=3', 'italy:less=0', 'switzerland:egreater=1', 'switzerland:less=1', 'spain:egreater=3', 'spain:less=1', 'denmark:less=3', 'finland:egreater=1', 'finland:less=0', 'poland:egreater=1', 'austria:egreater=2', 'austria:less=0', 'greece:egreater=0', 'greece:less=2']
  NOTE: this fires per market AND direction, so it is NOT a coverage-failure signal on
  its own. A 'less' count of 0-3 means almost nothing fell more than 2.5% that session
  (a broad up-day); a small 'egreater' count usually means a small market with few
  names above the $1B market-cap floor. Check the median change before calling it a gap.
- filters: volume>10000 (removes stale-reference rows), country=home for EU/UK/AU,
  exchange drop-list for US, US venue allow-list, US preferred (slash ticker) excluded
- volume_floor_note: volume>10000 removes MOST stale-reference rows, but a row can
  still sit on a stale reference when its only volume came from one thin day (verified
  2026-10-26: LSE 50GP cleared the floor on 12,000 shares dated 2026-10-15 while Yahoo
  showed no bar for the scan date). The reference-close cross-check is what catches
  those; rows that fail it are dropped from the tables, not published.
- us_preferred_dropped: 59
- bod_no_extended_hours: 85 (deferred to the next scan; not in the headline table)
- earnings_source: screener `earnings_release_date` (last FULL report) + `earnings_release_next_date` (next scheduled)
- earnings_caveat: `earnings_release_date` does NOT capture preliminary, guidance or
  restructuring releases. On 2026-10-23 LKQ fell 22.47% on a preliminary Q3 miss while
  the field still read 2026-07-30. ALWAYS confirm the earnings-driven flag against the
  headline itself; the calendar field is a screen, not a verdict.
- data_date: US regular session close of the prior trading day; extended-hours columns
  carry the prior session's prints
- deprecations: mcp__tradingview-advanced__*, mcp__tradingview__*, mcp__financekit__*,
  mcp__stocktwits__* are ABSENT in Cloud sessions (tool_search 0 hits; connector catalog
  holds only media + credential tools). The public screener replaces them.

## Audit line

`earnings-reaction target=earnings-reactions:2026-11-02 candidates=480 amc_reactions=0 pre_gaps=73 eu_reactions=29 asx_reactions=3 catalyst_lookups=10 bod=85`
