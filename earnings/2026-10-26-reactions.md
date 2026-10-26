# Earnings reaction scanner — 2026-10-26

- Cron: `0 8 * * 1-5` America/New_York (weekdays, 08:00 ET)
- Fire time (ET): 2026-10-26 08:27:46 Mon
- Run type: `scheduled_scan`
- Source: TradingView public screener (`scanner.tradingview.com/<market>/scan`);
  Yahoo chart API as an independent cross-check on the reported movers.
- Method: 4 passes (US top-200 mcap, US prior-session movers, EU/UK movers,
  ASX movers). Volume floor 10,000 on every pass; `country` filter for
  primary listings; exchange drop-list applied.
- Status: `ok`

## TL;DR

- 0 AMC reactions, 35 pre-market gaps, 140 without extended-hours data; 29 EU/UK and 25 ASX movers.
- Biggest US extended-hours move: XP PRE_GAP (47.91%).
- Biggest EU/UK move: YUBICO (+16.59%, sweden).
- Biggest ASX move: TUA (-30.49%).
- EU/AU earnings-driven tagging is keyword-based on headlines (best-effort).

## US — Headline table

| Ticker | Venue | Close | Chg % | Pre-mkt % | Post-mkt % | Last earnings | Tag |
|---|---|---|---|---|---|---|---|
| XP | NASDAQ | 30.41 | 3.61 | -47.91 | — | 2026-08-17 (70d ago) | PRE_GAP |
| INTR | NASDAQ | 7.19 | 6.68 | -35.88 | — | 2026-08-05 (82d ago) | PRE_GAP |
| AGBK | NYSE | 7.58 | 4.26 | -21.50 | — | 2026-08-05 (82d ago) | PRE_GAP |
| MELI | NASDAQ | 1810.15 | -0.81 | -14.42 | — | 2026-08-05 (82d ago) | PRE_GAP |
| RRC | NYSE | 45.52 | 3.78 | 11.38 | — | 2026-07-21 (97d ago) | PRE_GAP |
| MRNA | NASDAQ | 200.1 | -1.25 | -8.39 | — | 2026-07-31 (87d ago) | PRE_GAP |
| ADPT | NASDAQ | 25.51 | 4.51 | -6.00 | — | 2026-07-29 (89d ago) | PRE_GAP |
| AVBP | NASDAQ | 21 | 9.38 | 3.81 | — | 2026-08-12 (75d ago) | PRE_GAP |
| PBLS | NASDAQ | 24.44 | -9.21 | 3.72 | — | 2026-08-13 (74d ago) | PRE_GAP |
| CLS | NYSE | 260.01 | -3.35 | 3.65 | — | 2026-07-27 (91d ago) | PRE_GAP |
| SDRL | NYSE | 52.35 | 6.42 | -3.17 | — | 2026-08-10 (77d ago) | PRE_GAP |
| ENTG | NASDAQ | 134.52 | 4.84 | 3.07 | — | 2026-08-04 (83d ago) | PRE_GAP |
| SMTC | NASDAQ | 132 | 5.50 | 3.03 | — | 2026-08-25 (62d ago) | PRE_GAP |
| VG | NYSE | 14 | 9.29 | -2.86 | — | 2026-08-11 (76d ago) | PRE_GAP |
| PTEN | NASDAQ | 11.97 | 5.56 | -2.84 | — | 2026-07-29 (89d ago) | PRE_GAP |
| RGC | NASDAQ | 7.67 | -21.81 | 2.83 | — | — | PRE_GAP |
| ABCL | NASDAQ | 11.82 | 3.96 | 2.79 | — | 2026-08-05 (82d ago) | PRE_GAP |
| FORM | NASDAQ | 98.51 | 3.66 | 2.53 | — | 2026-07-29 (89d ago) | PRE_GAP |
| WGS | NASDAQ | 56.15 | -16.37 | 2.49 | — | 2026-08-03 (84d ago) | PRE_GAP |
| BE | NYSE | 193.3 | -11.24 | 2.41 | — | 2026-10-22 (4d ago) | PRE_GAP |
| TDW | NYSE | 86.07 | 8.11 | -2.41 | — | 2026-08-03 (84d ago) | PRE_GAP |
| TSLA | NASDAQ | 372.22 | -0.63 | 2.37 | — | 2026-10-21 (5d ago) | PRE_GAP |
| APA | NASDAQ | 51.9 | 4.98 | -2.31 | — | 2026-08-05 (82d ago) | PRE_GAP |
| NN | NASDAQ | 10.08 | 9.45 | -2.28 | — | 2026-08-11 (76d ago) | PRE_GAP |
| MGM | NYSE | 28.06 | -4.88 | 2.28 | — | 2026-07-29 (89d ago) | PRE_GAP |
| ATEN | NYSE | 25.45 | 3.62 | -2.27 | — | 2026-08-05 (82d ago) | PRE_GAP |
| ORIC | NASDAQ | 13.17 | -3.37 | -2.20 | — | 2026-08-03 (84d ago) | PRE_GAP |
| PBF | NYSE | 76.17 | -3.89 | -2.19 | — | 2026-07-30 (88d ago) | PRE_GAP |
| PSX | NYSE | 283.18 | -0.51 | -2.18 | — | 2026-08-05 (82d ago) | PRE_GAP |
| MU | NASDAQ | 877.55 | 2.46 | 2.15 | — | 2026-09-30 (26d ago) | PRE_GAP |
| DVN | NYSE | 51.39 | 4.49 | -2.14 | — | 2026-08-04 (83d ago) | PRE_GAP |
| TNGX | NASDAQ | 23.34 | -16.43 | 2.14 | — | 2026-08-11 (76d ago) | PRE_GAP |
| KLAC | NASDAQ | 145.61 | -1.50 | 2.13 | — | 2026-07-28 (90d ago) | PRE_GAP |
| SM | NYSE | 40.11 | 4.40 | -2.08 | — | 2026-08-05 (82d ago) | PRE_GAP |
| FRO | NYSE | 52.94 | 3.36 | 2.02 | — | 2026-08-28 (59d ago) | PRE_GAP |

## US — QUIET one-liners

| Ticker | Venue | Chg % | Pre-mkt % | Post-mkt % |
|---|---|---|---|---|
| AMAT | NASDAQ | 0.44 | 1.99 | — |
| WTTR | NYSE | 3.42 | -1.98 | — |
| CRGY | NYSE | 3.75 | -1.95 | — |
| BAND | NASDAQ | 9.09 | 1.95 | — |
| SNDK | NASDAQ | -1.82 | 1.94 | — |
| LRCX | NASDAQ | -0.02 | 1.93 | — |
| GLW | NYSE | -0.24 | 1.92 | — |
| CRDO | NASDAQ | -9.51 | 1.92 | — |
| VET | NYSE | 3.49 | -1.87 | — |
| VLO | NYSE | -1.64 | -1.86 | — |
| RIG | NYSE | 5.43 | -1.84 | — |
| NEM | NYSE | -4.59 | 1.84 | — |
| BTE | NYSE | 3.38 | -1.82 | — |
| ALGT | NASDAQ | -3.82 | 1.82 | — |
| COF | NYSE | -1.03 | 1.80 | — |

## EU/UK — Headline table

| Ticker | Market | Venue | Close | Chg % | Currency | Last earnings |
|---|---|---|---|---|---|---|
| YUBICO | sweden | OMXSTO | 146.9 | +16.59 | SEK | 2026-08-06 |
| OTEC | norway | OSL | 18.86 | -16.36 | NOK | 2022-02-15 |
| SBB_D | sweden | OMXSTO | 6.99 | +13.66 | SEK | — |
| GTT | france | EURONEXT | 177.8 | -13.27 | EUR | 2026-07-28 |
| GMAB | denmark | OMXCOP | 2971 | +12.37 | DKK | 2026-08-06 |
| BETCO_DKK | denmark | OMXCOP | 45 | -12.28 | DKK | 2026-08-20 |
| CCC | uk | LSE | 5070 | +10.46 | GBX | 2026-09-08 |
| GALP | portugal | EURONEXT | 20.7 | -9.84 | EUR | 2026-07-27 |
| NCOD | norway | OSL | 19.7 | +9.75 | NOK | 2025-02-13 |
| OHB | germany | XETR | 225 | +8.70 | EUR | 2026-08-06 |
| BITTI | finland | OMXHEX | 36.4 | +8.49 | EUR | 2022-02-10 |
| NTG | denmark | OMXCOP | 339 | +8.48 | DKK | 2026-09-22 |
| AOF | germany | XETR | 94.5 | +8.25 | EUR | 2026-07-27 |
| NANO | france | EURONEXT | 27.9 | +8.22 | EUR | 2026-09-24 |
| ALLEI | sweden | OMXSTO | 103.6 | -8.07 | SEK | 2026-07-16 |
| ROKO_B | sweden | OMXSTO | 1978 | -7.79 | SEK | 2026-10-23 |
| KCC | norway | OSL | 108 | +7.57 | NOK | 2026-08-25 |
| BWE | norway | OSL | 61.2 | -7.41 | NOK | 2026-07-30 |
| MSAB_B | sweden | OMXSTO | 116 | +7.41 | SEK | 2026-10-23 |
| IBT_B | sweden | OMXSTO | 75.9 | -6.87 | SEK | 2026-08-26 |
| PEN | norway | OSL | 31.65 | -6.64 | NOK | 2026-08-20 |
| FRVIA | france | EURONEXT | 8.556 | +6.44 | EUR | 2026-07-31 |
| MCAP | sweden | OMXSTO | 564 | -6.08 | SEK | 2026-10-23 |
| ORNAV | finland | OMXHEX | 97.3 | +5.99 | EUR | 2026-07-17 |
| BFIT | netherlands | EURONEXT | 30.4 | +5.92 | EUR | 2026-07-27 |
| ORNBV | finland | OMXHEX | 97.55 | +5.69 | EUR | 2026-07-17 |
| WAF | germany | XETR | 59.1 | +5.54 | EUR | 2026-07-30 |
| DNORD | denmark | OMXCOP | 381.6 | +5.53 | DKK | 2026-08-13 |
| MDATA | norway | OSL | 12.98 | +5.53 | NOK | 2026-08-26 |

## AU (ASX) — Headline table

| Ticker | Venue | Close | Chg % | Currency | Last earnings |
|---|---|---|---|---|---|
| TUA | ASX | 1.265 | -30.49 | AUD | 2026-03-24 |
| ZIP | ASX | 1.62 | +10.96 | AUD | 2026-08-19 |
| CTD | ASX | 3.38 | -8.89 | AUD | 2026-08-31 |
| PLS | ASX | 2.84 | +8.40 | AUD | 2026-08-23 |
| APE | ASX | 20.03 | +7.75 | AUD | 2026-08-26 |
| PDI | ASX | 3.8 | +7.34 | AUD | 2026-09-30 |
| GGP | ASX | 9.29 | +7.03 | AUD | 2026-08-26 |
| TPW | ASX | 5.05 | -7.00 | AUD | 2026-08-18 |
| OBM | ASX | 1.185 | +6.76 | AUD | 2026-08-25 |
| PNR | ASX | 2.74 | +6.20 | AUD | 2026-09-28 |
| BOE | ASX | 1.27 | +5.39 | AUD | 2026-08-26 |
| RSG | ASX | 1.09 | +5.31 | AUD | 2026-08-19 |
| FFM | ASX | 1.29 | +5.31 | AUD | 2026-09-17 |
| LYC | ASX | 11.27 | +5.23 | AUD | 2026-08-25 |
| INA | ASX | 5 | +5.04 | AUD | 2026-08-25 |
| BMN | ASX | 3.15 | +5.00 | AUD | 2026-09-23 |
| CVL | ASX | 1.615 | +4.87 | AUD | 2026-08-26 |
| CAT | ASX | 3.26 | +4.82 | AUD | 2026-05-18 |
| NEU | ASX | 18.65 | -4.75 | AUD | 2026-08-24 |
| MLX | ASX | 1.545 | +4.75 | AUD | 2026-08-27 |
| RRL | ASX | 6.32 | +4.46 | AUD | 2026-08-20 |
| C79 | ASX | 6.61 | -4.20 | AUD | 2026-08-09 |
| DGT | ASX | 2.02 | +4.12 | AUD | 2026-08-20 |
| ELV | ASX | 3.54 | +4.12 | AUD | 2026-08-27 |
| CYL | ASX | 4.94 | +4.00 | AUD | 2026-08-31 |

## Catalysts

Catalyst lookups: 5 US + 3 EU + 2 AU = 10, the skill's per-run cap. Every headline below was
located with a web search on 2026-10-26; nothing is written from inference. Earnings-driven
flag follows the skill's rule - Y when the move is an earnings event (US: a report date
within 7 days, confirmed against the headline; EU/AU: the earnings keyword test), N
otherwise. Where the screener's `earnings_release_date` field disagrees with the headline,
the headline wins and the field is noted.

| Ticker | Region | Catalyst | Earnings-driven |
|---|---|---|---|
| XP | US | Not earnings. Lula da Silva beat Flávio Bolsonaro in Brazil's presidential runoff (about 51.8% of the vote), unwinding the post-first-round rally in Brazilian assets (EWZ ETF -19%, a 10% implied decline in the real). XP's own overhang compounded it: board member Escobari resigned on 16 Oct with a Microsoft executive named Interim Director, and Assenagon cut its stake by about 7.9%. No quarterly report is due until late November. (Investing.com, 26 Oct 06:30 ET) | N |
| INTR | US | Not earnings. Inter & Co, the Brazilian digital bank, is hit by the same Brazil runoff shock; strategists expect a sell-off and a jump in rate futures, which is the core problem for a Brazilian digital bank. Friday's +6.7% close had followed UBS and JPMorgan target hikes and the buy-out of the remaining 39.75% of Inter Seguros. (Perplexity Finance, 26 Oct) | N |
| AGBK | US | Not earnings. AGI Inc, the Banco Agibank holding company, under Brazil runoff pressure given its concentrated Brazilian payroll and INSS lending and the fiscal and rate uncertainty; Q3 earnings are due 11 Nov. Friday's close had followed a roughly 30% 30-day rebound. (Perplexity Finance, 26 Oct) | N |
| MELI | US | Not earnings. Brazil runoff shock: the real and Brazilian rates repriced on fiscal risk, which compresses MercadoLibre's dollar-reported earnings, with the MSCI Brazil ETF down nearly 19% overnight. Q3 is due in early November, so the move is not the report. (Investing.com, 26 Oct 05:30 ET) | N |
| RRC | US | Not earnings - acquisition. EQT and Range Resources signed a definitive all-stock merger: 0.987 EQT shares per Range share, pro forma enterprise value above $50bn, about $12.83bn of equity value and an implied $54.91 per share, roughly 20.6% above Friday's close. Range holders take about 27% of the combined group, close expected in Q1 2027, and both companies moved their Q3 results to 27 Oct. (EQT press release and Reuters, 26 Oct) | N |
| OTEC | EU | Earnings, scheduled but not yet confirmed. Otello's Q3 2026 report was scheduled for 26 Oct (Investing.com earnings calendar, period 09-2026) but no release text was found on Otello's IR feed or filing list at scan time, so the -15% intraday move has no located company explanation; the screener's own `earnings_release_date` field is stale at 2022-02-15. Next scheduled event is the FY26 year-end report on 17 Feb 2027. | Y |
| YUBICO | EU | Not earnings. The cybersecurity complex rallied after last week's discovery of security flaws in the PHP programming language, which led several countries to shut down government sites, and a strong Friday rally in the US cybersecurity sector drove Monday's move; social-media interest in the stock as an AI-security hedge amplified it. Q3 report due 5 Nov. (Dagens Industri via Direkt and Placera, 26 Oct) | N |
| GTT | EU | Earnings. 9M 2026 revenue was €570.1m, down 4.9% year on year, with Q3 revenue of €183m against €193m consensus and €196m at Jefferies, on fewer LNG carriers under construction. FY26 guidance was confirmed (revenue €740-780m, EBITDA €490-530m, dividend policy maintained), while Bernstein cut its target from €245 to €210. Worst SBF 120 performer of the morning. (Zonebourse, Boursedirect and MarketScreener, 26 Oct) | Y |
| TUA | AU | Not earnings. Singapore's IMDA served Simba Telecom, Tuas' wholly-owned Singapore subsidiary, a formal Show Cause Notice with six allegations, including unauthorised dynamic spectrum sharing at about 133 sites in 2022-23 and unauthorised 2340-2360 MHz use at about 92 sites in 2023-26. Possible sanctions are a fine of the higher of 10% of annual turnover or S$1m and suspension or cancellation of spectrum licences; a formal response is due 16 Nov 2026. (ASX release, 26 Oct 09:35 AEDT) | N |
| ZIP | AU | Earnings-reaction rebound, not a fresh report. After Friday's -29.5% fall on the 1Q FY27 update, which disclosed a US fraud incident and a rise in bad debts, Macquarie and UBS reiterated Buy and called the reaction an overreaction, and Zip filed a buy-back update on 26 Oct. FY27 cash EBTDA guidance of $340m was reconfirmed and transaction volume rose 18% to $4.6bn. Short interest of 13.3% of the register added squeeze dynamics. (Investing.com, 26 Oct) | Y |

## Source health

- scanner_calls: 39 | scanner_errors: 0
- yahoo_calls: 100 | yahoo_429: 0 | yahoo_errors: 0
- cross_check (screener vs Yahoo, reference-close validation): agree=89 mismatch=1 unverified=0 stale_reference=1
  method: the screener's implied reference close (close / (1 + change/100)) is compared
  with Yahoo's own reference close. A match proves the move was measured against the
  TRUE prior close; a mismatch means the row sits on a STALE reference (phantom move).
  Coverage: every row of the US headline, EU/UK and ASX tables is checked. The US QUIET
  one-liner table is NOT cross-checked.
  Yahoo bar mode: {"closed": 60, "live": 29} (closed = last completed session bar;
  live = in-progress EU/UK session bar, which is what a weekday 08:00 ET EU move needs)
  live drift between the screener snapshot and the later Yahoo print: median=0.00pp max=1.35pp (expected on a live market)
- cross_check mismatches: [{"region": "uk", "symbol": "50GP.L", "tv": -9.145, "yahoo": 0.0, "delta": -9.145, "ref_delta_pct": 10.065, "tv_implied_ref": 84.75, "yahoo_ref": 77.0, "yahoo_date": "2026-10-23", "verdict": "stale_reference"}]
- stale_rows_dropped: US=none EU=['50GP'] AU=none
- us_premarket_check (Yahoo 1-min pre/post feed vs the screener pre-market column): checked=9 within_1pp=8 within_3pp=9 unavailable=1
- markets_with_lt5_rows: ['uk:less=1', 'germany:less=0', 'france:less=1', 'netherlands:less=1', 'belgium:egreater=2', 'belgium:less=1', 'portugal:egreater=0', 'portugal:less=1', 'ireland:egreater=1', 'ireland:less=0', 'italy:less=1', 'switzerland:less=0', 'spain:less=2', 'norway:less=4', 'denmark:less=1', 'finland:less=0', 'poland:less=1', 'austria:egreater=1', 'austria:less=2', 'greece:egreater=1', 'greece:less=0']
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
- bod_no_extended_hours: 140 (deferred to the next scan; not in the headline table)
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

`earnings-reaction target=earnings-reactions:2026-10-26 candidates=539 amc_reactions=0 pre_gaps=35 eu_reactions=29 asx_reactions=25 catalyst_lookups=10 bod=140`
