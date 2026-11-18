# Earnings reaction scanner — 2026-11-18

- Cron: `0 8 * * 1-5` America/New_York (weekdays, 08:00 ET)
- Fire time (ET): 2026-11-18 08:08:32 Wed
- Run type: `scheduled_scan`
- Source: TradingView public screener (`scanner.tradingview.com/<market>/scan`);
  Yahoo chart API as the independent reference-close source.
- Method: 6 passes (US top-200 mcap, US prior-session movers, US pre-market gaps,
  EU/UK movers, ASX movers, APAC/Gulf movers). Volume floor 10,000 on every session-volume
  pass; Pass B2 floors PRE-market volume at 10,000 shares; `country` filter for
  primary listings; exchange drop-list applied.
- artifact_contract: REACTION_ARTIFACT_V2
- settlement_state: every foreign row carries a `Settle` cell - `live` when the row's
  session bar is an in-progress bar, `settled` when it is a completed session. The
  EU/UK session is still OPEN at the 08:00 ET fire (it closes 11:30 ET in winter), so
  its rows read `live`: the move is a mid-session snapshot, not the session's result.
- ref_close_source: yahoo_chart_daily (Yahoo Finance daily chart bars; the base
  every published row is measured against)
- Status: `ok`

## TL;DR

- 0 AMC reactions, 49 pre-market gaps, 103 without extended-hours data; 29 EU/UK and 4 ASX movers, 20 APAC/Gulf movers.
- Pass B2 (the US pre-market gap scan) met the filter on 16 names (9 up, 7 down); 3 were already a Pass A/B row and are recorded as dedupes, and 13 reached a table.
- Biggest US extended-hours move: GLBE PRE_GAP (12.58%).
- Biggest EU/UK move: DAD (-10.48%, poland).
- Biggest ASX move: NXL (+45.28%).
- Biggest APAC/Gulf move: NZIA (+34.48%, indonesia).
- 0 of the 29 EU/UK rows are SETTLED and 29 are LIVE (mid-session). The 12:15 ET settlement pass publishes where those
  live moves actually closed.
- EU/AU/APAC earnings-driven tagging is keyword-based on headlines (best-effort). A row
  whose lookup was not performed carries NO verdict — only a researched row does.

## Actionable read

- **Move vs this name's own history.** The `Move vs avg daily` column divides the
  reaction by the name's own mean absolute daily move over its last
  20 completed sessions. A -27% move in a name that averages +-3% is a
  different event from a -8% move in a name that averages +-7%.
- **US-listed and tradeable vs foreign-only.** 64 published US rows are on a
  US venue; 0 more foreign reactions have a US ADR line
  (the `US tradeable` column carries the ticker); 29 are foreign-only and
  cannot be bought directly by a US reader.
- **Not yet fully priced — US (hypothesis, not a recommendation).**
  GLBE — -12.58%, 2.16% mean absolute daily move over the last 20 completed sessions, 5.8x that average, reference close 41.38 dated 2026-11-16, US access: US-listed, the move now (-12.58%) is larger than the move it follows (-3.79%); the reaction is still being repriced. Hypothesis only: this artifact states no
  direction and no trade.
- **Not yet fully priced — EU/UK (hypothesis, not a recommendation).**
  CTEC — +9.97%, 1.21% mean absolute daily move over the last 20 completed sessions, 8.3x that average, reference close 246.80 dated 2026-11-17, US access: none, the move now (+9.97%) is larger than the move it follows (-2.37%); the reaction is still being repriced. Hypothesis only: this artifact states no
  direction and no trade.
- **Not yet fully priced — AU (ASX) (hypothesis, not a recommendation).**
  NXL — +45.28%, 5.07% mean absolute daily move over the last 20 completed sessions, 8.9x that average, reference close 1.59 dated 2026-11-16, US access: none, the move now (+45.28%) is larger than the move it follows (-2.15%); the reaction is still being repriced. Hypothesis only: this artifact states no
  direction and no trade.

## US — Headline table

| Ticker | Venue | Close | Chg % | Pre-mkt % | Post-mkt % | Move vs avg daily | Ref close | Ref source | Ref asof | US tradeable | Last earnings | Tag | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GLBE | NASDAQ | 39.81 | -3.79 | -12.58 | — | 5.8x | 41.38 | yahoo_chart_daily | 2026-11-16 | US-listed | 2026-11-18 (0d ago) | PRE_GAP | Y | Q3 2026 results (reported 2026-11-18, 06:02 ET): adjusted EPS $0.37 vs $0.33 consensus, revenue $314.1m +42% y/y, GMV $2,042m +35%, adjusted EBITDA $63.7m at a 20.3% margin, FY26 guidance raised on every metric - but non-GAAP gross margin fell to 44.8% from 46.3% on Passport logistics mix, free cash flow slipped to $66.4m from $73.6m, and the Q4 revenue guide of $464-488m only modestly clears consensus; a textbook sell-the-news, and the shares are down double digits in pre-market |
| AAOI | NASDAQ | 45.22 | 0.13 | -9.95 | — | 1.3x | 45.16 | yahoo_chart_daily | 2026-11-16 | US-listed | 2026-11-05 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| CHRN | NASDAQ | 9.74 | 3.73 | -9.14 | — | 1.2x | 9.39 | yahoo_chart_daily | 2026-11-16 | US-listed | 2026-10-15 (34d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BRBR | NYSE | 11.01 | 4.36 | 8.99 | — | 2.8x | 10.55 | yahoo_chart_daily | 2026-11-16 | US-listed | 2026-11-18 (0d ago) | PRE_GAP | Y | Q4 FY2026 results (reported 2026-11-18, 07:00 ET): net sales $692.0m +7% y/y on 14.9% volume growth, but a $16m inventory-related charge cut gross margin to 22.0% (adjusted 20.1%) from 28.9% and net earnings to $35.6m, $0.31 diluted EPS vs $0.48 a year ago; FY27 outlook $2.32-2.42bn of sales and $310-350m of adjusted EBITDA |
| BLSH | NYSE | 19.27 | -2.43 | 8.72 | — | 1.9x | 19.75 | yahoo_chart_daily | 2026-11-16 | US-listed | 2026-11-18 (0d ago) | PRE_GAP | Y | Q3 2026 results (reported 2026-11-18, 06:45 ET): net income $576.3m vs $18.5m, lifted by a $598.4m fair-value gain on digital assets held, diluted EPS $3.57 vs $0.10; adjusted revenue $84.4m +13% y/y and adjusted EBITDA $35.6m +24%, but digital asset sales fell to $32.1bn from $41.6bn; the board authorised a $300m share repurchase |
| BORR | NYSE | 3.18 | -0.31 | 8.17 | — | 1.8x | 3.19 | yahoo_chart_daily | 2026-11-16 | US-listed | 2026-11-18 (0d ago) | PRE_GAP | Y | Q3 2026 results are due after today's NYSE close (issuer's release date 2026-11-18, call Nov 19 at 09:00 ET) - no published figures yet; the Street expects revenue to fall about 6% y/y after last year's $232.3m quarter, so the pre-market gap is positioning ahead of the print rather than a reaction to reported numbers |
| CAPR | NASDAQ | 8.41 | 1.33 | 7.95 | — | 1.0x | 8.30 | yahoo_chart_daily | 2026-11-16 | US-listed | 2026-11-10 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PEPG | NASDAQ | 3.88 | -7.40 | 7.57 | — | 0.8x | 4.19 | yahoo_chart_daily | 2026-11-16 | US-listed | 2026-11-10 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TJX | NYSE | 129.85 | -0.95 | 6.28 | — | 3.6x | 131.09 | yahoo_chart_daily | 2026-11-16 | US-listed | 2026-11-18 (0d ago) | PRE_GAP | Y | Q3 FY2027 results (reported 2026-11-18, 07:30 ET): net sales $15.95bn +6% vs the $15.84bn LSEG estimate, comparable sales +4% and above plan (Marmaxx +2%, HomeGoods +5%, Canada +6%, International +8%), pretax margin 13.0%, diluted EPS $1.39 +9% and adjusted EPS $1.34 excluding a $0.05 tariff-refund benefit; FY27 adjusted EPS guidance of $5.17-5.20 sits just under the $5.25 consensus, Q4 adjusted EPS guided to $1.42-1.45 |
| TTWO | NASDAQ | 203.93 | -4.47 | 6.05 | — | 2.3x | 213.47 | yahoo_chart_daily | 2026-11-16 | US-listed | 2026-11-09 (9d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| HYMC | NASDAQ | 15.69 | 2.55 | -5.93 | — | 1.1x | 15.30 | yahoo_chart_daily | 2026-11-16 | US-listed | 2026-10-27 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SVRA | NASDAQ | 4.48 | 0.34 | 5.79 | — | 1.5x | 4.46 | yahoo_chart_daily | 2026-11-16 | US-listed | 2026-11-09 (9d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ANGX | NYSE | 4.14 | -7.80 | 5.56 | — | 1.3x | 4.49 | yahoo_chart_daily | 2026-11-16 | US-listed | 2026-11-10 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| PRMB | NYSE | 24.25 | 0.83 | -5.36 | — | 3.0x | 24.05 | yahoo_chart_daily | 2026-11-16 | US-listed | 2026-11-05 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| TNDM | NASDAQ | 17.06 | -7.68 | 5.28 | — | 1.0x | 18.48 | yahoo_chart_daily | 2026-11-16 | US-listed | 2026-11-05 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| USAS | AMEX | 2.26 | -0.88 | -5.16 | — | 0.9x | 2.28 | yahoo_chart_daily | 2026-11-16 | US-listed | 2026-11-13 (5d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-13 (Nasdaq earnings calendar; no headline lookup), consensus EPS $0.03 |
| GAU | AMEX | 2.15 | -3.15 | -5.12 | — | 1.0x | 2.22 | yahoo_chart_daily | 2026-11-16 | US-listed | 2026-11-05 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AG | NYSE | 12.77 | 0.79 | -5.03 | — | 1.4x | 12.67 | yahoo_chart_daily | 2026-11-16 | US-listed | 2026-11-05 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| LOW | NYSE | 220.46 | -1.99 | -4.74 | — | 2.4x | 224.93 | yahoo_chart_daily | 2026-11-16 | US-listed | 2026-11-18 (0d ago) | PRE_GAP | Y | Q3 FY2026 results (reported 2026-11-18, 06:00 ET): adjusted EPS $3.10 vs the $2.86-2.88 consensus, net sales $22.76bn +9.3% (est $22.38bn), comparable sales +1.8% with online +17.4%; FY26 sales guidance raised to $92.5bn and comps to about +0.5% with the $12.25 EPS guide held - but $0.34 of the EPS came from IEEPA tariff refunds and the underlying comp is barely positive |
| NEM | NYSE | 111.26 | 0.86 | -3.74 | — | 1.4x | 110.31 | yahoo_chart_daily | 2026-11-16 | US-listed | 2026-10-22 (27d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SA | NYSE | 26.28 | 7.27 | -3.58 | — | 1.0x | 24.50 | yahoo_chart_daily | 2026-11-16 | US-listed | 2026-11-12 (6d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-12 (Nasdaq earnings calendar; no headline lookup), consensus EPS ($0.05) |
| QBTS | NASDAQ | 8.08 | -6.81 | 3.47 | — | 0.6x | 8.67 | yahoo_chart_daily | 2026-11-16 | US-listed | 2026-11-10 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FLUT | NYSE | 75.57 | -4.52 | 3.41 | — | 1.4x | 79.15 | yahoo_chart_daily | 2026-11-16 | US-listed | 2026-11-04 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| COHR | NYSE | 210.86 | 3.65 | 3.39 | — | 0.5x | 203.43 | yahoo_chart_daily | 2026-11-16 | US-listed | 2026-11-04 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| SCCO | NYSE | 155.42 | 1.01 | -3.36 | — | 1.1x | 153.87 | yahoo_chart_daily | 2026-11-16 | US-listed | 2026-10-21 (28d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BSP | NASDAQ | 42.33 | 3.29 | 3.35 | — | 1.4x | 40.98 | yahoo_chart_daily | 2026-11-16 | US-listed | 2026-08-13 (97d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| BELFB | NASDAQ | 218.2 | 4.78 | 3.35 | — | 0.8x | 208.24 | yahoo_chart_daily | 2026-11-16 | US-listed | 2026-10-28 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FCX | NYSE | 55.3 | 0.20 | -3.24 | — | 1.2x | 55.19 | yahoo_chart_daily | 2026-11-16 | US-listed | 2026-10-27 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AMBQ | NYSE | 45.55 | 3.45 | 3.21 | — | 0.5x | 44.03 | yahoo_chart_daily | 2026-11-16 | US-listed | 2026-11-10 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| IE | AMEX | 6.3 | -5.55 | -3.17 | — | 0.6x | 6.67 | yahoo_chart_daily | 2026-11-16 | US-listed | 2026-11-05 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| GENB | NASDAQ | 9.84 | -6.20 | 3.15 | — | 0.5x | 10.49 | yahoo_chart_daily | 2026-11-16 | US-listed | 2026-11-12 (6d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-12 (Nasdaq earnings calendar; no headline lookup), consensus EPS ($0.50) |
| SMMT | NASDAQ | 10.67 | -9.73 | -3.09 | — | 0.5x | 11.82 | yahoo_chart_daily | 2026-11-16 | US-listed | 2026-11-04 (14d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| DELL | NYSE | 322.79 | 0.70 | 2.85 | — | 0.5x | 320.55 | yahoo_chart_daily | 2026-11-16 | US-listed | 2026-09-01 (78d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NVDA | NASDAQ | 155.46 | -0.44 | 2.85 | — | 1.0x | 156.14 | yahoo_chart_daily | 2026-11-16 | US-listed | 2026-11-17 (1d ago) | PRE_GAP | Y | Q3 FY2027 results (reported 2026-11-17, after the close): revenue $115.84bn +103% y/y, data center $107.6bn, non-GAAP EPS $2.68 vs the $2.48 estimate, non-GAAP gross margin 74.9%, and Q4 revenue guided to about $130bn against a $125.1bn consensus; the first report after co-founder Jensen Huang's exit as CEO |
| AEM | NYSE | 173.01 | 1.29 | -2.78 | — | 0.8x | 170.81 | yahoo_chart_daily | 2026-11-16 | US-listed | 2026-10-28 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| INFQ | NYSE | 7.54 | -4.56 | 2.65 | — | 0.5x | 7.90 | yahoo_chart_daily | 2026-11-16 | US-listed | 2026-11-16 (2d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-16 (Nasdaq earnings calendar; no headline lookup), consensus EPS ($0.05) |
| FIX | NYSE | 1099.02 | 3.91 | 2.45 | — | 0.4x | 1057.68 | yahoo_chart_daily | 2026-11-16 | US-listed | 2026-10-22 (27d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| AXTI | NASDAQ | 36.42 | -5.30 | 2.42 | — | 0.3x | 38.46 | yahoo_chart_daily | 2026-11-16 | US-listed | 2026-10-29 (20d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| ALAB | NASDAQ | 211.6 | 4.58 | 2.41 | — | 0.4x | 202.34 | yahoo_chart_daily | 2026-11-16 | US-listed | 2026-11-03 (15d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| STX | NASDAQ | 504.4 | 1.08 | 2.38 | — | 0.5x | 499.00 | yahoo_chart_daily | 2026-11-16 | US-listed | 2026-10-27 (22d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FPS | NYSE | 21.2 | 3.06 | 2.36 | — | 0.3x | 20.57 | yahoo_chart_daily | 2026-11-16 | US-listed | 2026-11-12 (6d ago) | PRE_GAP | — | Q3 2026 results, report date 2026-11-12 (Nasdaq earnings calendar; no headline lookup), consensus EPS $0.18 |
| RGTI | NASDAQ | 8.46 | -6.62 | 2.25 | — | 0.4x | 9.06 | yahoo_chart_daily | 2026-11-16 | US-listed | 2026-11-10 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| IONQ | NYSE | 24.84 | -6.09 | 2.21 | — | 0.4x | 26.45 | yahoo_chart_daily | 2026-11-16 | US-listed | 2026-11-05 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FUN | NYSE | 10.96 | -5.60 | -2.19 | — | 0.4x | 11.61 | yahoo_chart_daily | 2026-11-16 | US-listed | 2026-11-05 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| FLY | NASDAQ | 21.45 | -4.58 | 2.19 | — | 0.3x | 22.48 | yahoo_chart_daily | 2026-11-16 | US-listed | 2026-11-10 (8d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| NXT | NASDAQ | 78.48 | -12.13 | 2.08 | — | 0.4x | 89.31 | yahoo_chart_daily | 2026-11-16 | US-listed | 2026-10-28 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MRVL | NASDAQ | 148.74 | 2.33 | 2.06 | — | 0.3x | 145.36 | yahoo_chart_daily | 2026-11-16 | US-listed | 2026-08-27 (83d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| KLAC | NASDAQ | 144.56 | 0.42 | 2.03 | — | 0.4x | 143.96 | yahoo_chart_daily | 2026-11-16 | US-listed | 2026-10-28 (21d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |
| MTSI | NASDAQ | 227.36 | 3.14 | 2.00 | — | 0.3x | 220.44 | yahoo_chart_daily | 2026-11-16 | US-listed | 2026-11-05 (13d ago) | PRE_GAP | — | no catalyst lookup (outside the per-run budget) |

## US — QUIET one-liners

| Ticker | Venue | Chg % | Pre-mkt % | Post-mkt % | Move vs avg daily | Ref close | Ref source | Ref asof | US tradeable | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|
| SNDK | NASDAQ | -1.47 | 1.98 | — | 0.2x | 809.11 | yahoo_chart_daily | 2026-11-16 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| LRCX | NASDAQ | -0.07 | 1.97 | — | 0.0x | 210.83 | yahoo_chart_daily | 2026-11-16 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| NKE | NYSE | -6.30 | -1.95 | — | 2.9x | 38.26 | yahoo_chart_daily | 2026-11-16 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| WDC | NASDAQ | 0.85 | 1.90 | — | 0.2x | 280.93 | yahoo_chart_daily | 2026-11-16 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| DDS | AMEX | -4.27 | 1.77 | — | 1.2x | 583.00 | yahoo_chart_daily | 2026-11-16 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| DB | NYSE | -5.47 | -1.77 | — | 2.1x | 35.84 | yahoo_chart_daily | 2026-11-16 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| TRMD | NASDAQ | -6.42 | -1.76 | — | 2.1x | 36.04 | yahoo_chart_daily | 2026-11-16 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| SECZ | NYSE | -5.46 | 1.73 | — | 0.8x | 7.33 | yahoo_chart_daily | 2026-11-16 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| ANET | NYSE | -0.32 | 1.71 | — | 0.1x | 187.02 | yahoo_chart_daily | 2026-11-16 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| GLW | NYSE | 2.19 | 1.71 | — | 0.5x | 106.17 | yahoo_chart_daily | 2026-11-16 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| SHLS | NASDAQ | -12.22 | 1.70 | — | 2.1x | 8.02 | yahoo_chart_daily | 2026-11-16 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| AVGO | NASDAQ | 2.46 | 1.69 | — | 0.6x | 333.40 | yahoo_chart_daily | 2026-11-16 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| AMAT | NASDAQ | -0.29 | 1.65 | — | 0.1x | 350.25 | yahoo_chart_daily | 2026-11-16 | US-listed | — | Q4 2026 results, report date 2026-11-12 (Nasdaq earnings calendar; no headline lookup), consensus EPS $4.06 |
| MU | NASDAQ | -0.92 | 1.63 | — | 0.2x | 719.02 | yahoo_chart_daily | 2026-11-16 | US-listed | — | no catalyst lookup (outside the per-run budget) |
| BB | NYSE | -6.96 | 1.59 | — | 1.7x | 8.77 | yahoo_chart_daily | 2026-11-16 | US-listed | — | no catalyst lookup (outside the per-run budget) |

## EU/UK — Headline table

| Ticker | Market | Venue | Close | Chg % | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | Session asof | Settle | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DAD | poland | GPW | 82 | -10.48 | PLN | 7.8x | 91.60 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | live | none | 2026-11-17 (1d ago) | — | no catalyst lookup (outside the per-run budget) |
| CTEC | uk | LSE | 271.4 | +9.97 | GBX | 8.3x | 246.80 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | live | none | 2026-08-04 (106d ago) | — | no catalyst lookup (outside the per-run budget) |
| SEYE | sweden | OMXSTO | 51.2 | +8.75 | SEK | 3.2x | 47.08 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | live | none | 2026-11-17 (1d ago) | — | no catalyst lookup (outside the per-run budget) |
| ALO | france | EURONEXT | 9.24 | -7.78 | EUR | 2.8x | 10.02 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | live | none | 2026-11-17 (1d ago) | — | no catalyst lookup (outside the per-run budget) |
| WAF | germany | XETR | 56.3 | +7.14 | EUR | 1.8x | 52.55 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | live | none | 2026-11-04 (14d ago) | — | no catalyst lookup (outside the per-run budget) |
| TPRO | italy | MIL | 21.52 | +6.85 | EUR | 1.6x | 20.14 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | live | none | 2026-08-05 (105d ago) | — | no catalyst lookup (outside the per-run budget) |
| JET2 | uk | LSE | 1392.533 | -6.35 | GBX | 5.1x | 1487.00 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | live | US line (OTC:DRTGF) | 2026-11-18 (0d ago) | — | no catalyst lookup (outside the per-run budget) |
| SENSO | finland | OMXHEX | 20.7 | +6.15 | EUR | 1.9x | 19.50 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | live | none | — | — | no catalyst lookup (outside the per-run budget) |
| XTB | poland | GPW | 108.52 | -5.83 | PLN | 2.1x | 115.24 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | live | none | 2026-10-28 (21d ago) | — | no catalyst lookup (outside the per-run budget) |
| HEM | sweden | OMXSTO | 50.85 | -5.75 | SEK | 1.4x | 53.95 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | live | none | 2026-10-22 (27d ago) | — | no catalyst lookup (outside the per-run budget) |
| SMOP | norway | OSL | 55.6 | +5.70 | NOK | 1.6x | 52.60 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | live | none | 2026-10-29 (20d ago) | — | no catalyst lookup (outside the per-run budget) |
| SILEX | sweden | OMXSTO | 141.7 | +5.63 | SEK | 1.6x | 134.15 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | live | US line (OTC:SILXF) | 2026-11-04 (14d ago) | — | no catalyst lookup (outside the per-run budget) |
| HOC | uk | LSE | 418 | -5.52 | GBX | 1.7x | 442.40 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | live | none | 2026-08-26 (84d ago) | — | no catalyst lookup (outside the per-run budget) |
| KEOC | sweden | OMXSTO | 5.8 | +5.45 | SEK | 1.6x | 5.50 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | live | none | 2026-08-31 (79d ago) | N | KEO Capital: completed the acquisition of the remaining 40% of Odebrecht E&P Espana from Novonor for a USD 22.15m closing instalment (USD 37.5m of the total paid), lifting its indirect interest in the Venezuelan producer PetroUrdaneta from 24% to 40% (PdVSA 60% / KEO Energy 40%), with KEO Energy still to be separated and spun off; the shares rebounded off fresh 52-week lows (SEK 5.49-5.52) and the Q3 report is only due on 24 Nov |
| PRX | netherlands | EURONEXT | 32.415 | -5.37 | EUR | 3.9x | 34.26 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | live | none | 2026-06-29 (142d ago) | — | no catalyst lookup (outside the per-run budget) |
| MRB | poland | GPW | 11.16 | +5.28 | PLN | 3.5x | 10.60 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | live | none | 2026-08-25 (85d ago) | — | no catalyst lookup (outside the per-run budget) |
| ANTO | uk | LSE | 2862 | -5.20 | GBX | 1.8x | 3019.00 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | live | none | 2026-08-13 (97d ago) | — | no catalyst lookup (outside the per-run budget) |
| SPG | germany | XETR | 23.3 | +5.19 | EUR | 4.3x | 22.15 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | live | none | 2026-08-05 (105d ago) | — | no catalyst lookup (outside the per-run budget) |
| HLUN_A | denmark | OMXCOP | 60.8 | +5.19 | DKK | 2.7x | 57.80 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | live | none | — | — | no catalyst lookup (outside the per-run budget) |
| KGH | poland | GPW | 251.4 | -4.88 | PLN | 1.9x | 264.30 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | live | none | 2026-08-18 (92d ago) | N | KGHM: the copper and silver sell-off hit the shares -4.9% to about PLN 252, a 2026 low and a sixth straight down session - with copper at its lowest since May (about -4% on the day to multi-month lows) and silver its weakest since October 2025; a broad metals de-rating, not an earnings reaction, and the Q3/9M 2026 report is due after today's close (consensus revenue PLN 12.4bn, adjusted EBITDA PLN 3.56bn) |
| SOI | france | EURONEXT | 100.6 | +4.86 | EUR | 0.9x | 95.94 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | live | none | 2026-11-18 (0d ago) | Y | Soitec: H1 FY2027 results are due after today's Paris close (issuer's results date 2026-11-18) and no figures are published yet - consensus looks for revenue of EUR 314.1m and a EUR 27.5m net loss, and the 2 Sep trading update had guided Q2'27 revenue to about +50% y/y in constant FX; the shares fell about 22% over the prior month, so today's move is results-day positioning rather than a reaction to printed numbers |
| PEN | norway | OSL | 28.85 | -4.79 | NOK | 2.5x | 30.30 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | live | none | 2026-11-18 (0d ago) | Y | Panoro Energy: Q3 2026 trading statement (reported 2026-11-18): revenue USD 114.3m, IFRS EBITDA USD 33.8m, record pro forma production of 20,049 boepd, the FY26 pro forma forecast raised to about 19,000 boepd and a NOK 50m cash distribution (NOK 0.356/sh) - but capex guidance was withdrawn after the 24 Oct Prospector 5 rig sinking at Dussafu (four fatalities) and the MaBoMo Phase 2 drilling delay; the shares fell 4.8% to NOK 28.85 |
| AG1 | germany | XETR | 13.29 | -4.53 | EUR | 1.7x | 13.92 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | live | none | 2026-11-04 (14d ago) | — | no catalyst lookup (outside the per-run budget) |
| IQMX | finland | OMXHEX | 6.125 | +4.52 | EUR | 1.1x | 5.86 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | live | none | 2026-11-05 (13d ago) | — | no catalyst lookup (outside the per-run budget) |
| ASM | netherlands | EURONEXT | 682 | +4.44 | EUR | 1.3x | 653.00 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | live | US line (OTC:ASMXF) | 2026-10-27 (22d ago) | — | no catalyst lookup (outside the per-run budget) |
| VU | france | EURONEXT | 145.4 | -4.22 | EUR | 1.7x | 151.80 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | live | none | 2026-09-21 (58d ago) | — | no catalyst lookup (outside the per-run budget) |
| XPLRA | norway | OSL | 22.95 | -3.97 | NOK | 1.2x | 23.90 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | live | none | 2026-11-12 (6d ago) | — | no catalyst lookup (outside the per-run budget) |
| AC | france | EURONEXT | 50.5 | -3.85 | EUR | 2.6x | 52.52 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | live | US line (NASDAQ:ACIU) | 2026-07-30 (111d ago) | — | no catalyst lookup (outside the per-run budget) |
| NOD | norway | OSL | 184.2 | +3.77 | NOK | 1.7x | 177.50 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | live | none | 2026-10-22 (27d ago) | — | no catalyst lookup (outside the per-run budget) |

## AU (ASX) — Headline table

| Ticker | Venue | Close | Chg % | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | Session asof | Settle | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NXL | ASX | 2.31 | +45.28 | AUD | 8.9x | 1.59 | yahoo_chart_daily | 2026-11-16 | 2026-11-18 | settled | none | 2026-08-23 (87d ago) | N | Nuix: Haveli Investments Software Fund I made an unsolicited, conditional non-binding indicative proposal to acquire all Nuix shares by scheme for A$2.75 cash (about A$945m), a 73% premium to the 17 Nov close of A$1.59; Nuix signed a five-week process and exclusivity deed, the board intends to recommend a binding offer at A$2.75 or higher, and Macquarie (about 28%) is supportive - the shares are +45.3% to A$2.31, a 13-month high |
| LLC | ASX | 1.72 | -16.91 | AUD | 4.5x | 2.07 | yahoo_chart_daily | 2026-11-16 | 2026-11-18 | settled | none | 2026-08-16 (94d ago) | N | Lendlease: Morgan Stanley downgraded the stock to Underweight and cut its target 30% to A$2.24, sending it -16.9% to a new all-time low A$1.72, the worst ASX 200 performer; it compounds the 13 Nov decision to redeem about A$1.22bn of bonds (roughly A$7m of make-whole plus A$50m of hedge termination costs) and the failed MSG North sale, with about A$160m of project obligations due by 31 Dec 2026; ASX Supervision issued an LR 18.7 price query at 12:57 AEDT and Lendlease answered 'no' to unannounced information |
| OBM | ASX | 1.31 | -9.66 | AUD | 2.1x | 1.45 | yahoo_chart_daily | 2026-11-16 | 2026-11-18 | settled | none | 2026-08-25 (85d ago) | — | no catalyst lookup (outside the per-run budget) |
| TEA | ASX | 8.87 | -9.49 | AUD | 3.6x | 9.80 | yahoo_chart_daily | 2026-11-16 | 2026-11-18 | settled | none | 2026-08-26 (84d ago) | — | no catalyst lookup (outside the per-run budget) |

## APAC/Gulf — Headline table

| Ticker | Market | Venue | Close | Chg % | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | Session asof | Settle | US tradeable | Last earnings | Earn | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NZIA | indonesia | IDX | 117 | +34.48 | IDR | 6.6x | 87.00 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| SOLA | indonesia | IDX | 79 | +33.90 | IDR | 7.1x | 59.00 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| 301391 | china | SZSE | 46.66 | +20.01 | CNY | 3.7x | 38.88 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | settled | none | 2026-04-29 (203d ago) | — | no catalyst lookup (outside the per-run budget) |
| 300991 | china | SZSE | 22.68 | +20.00 | CNY | 4.8x | 18.90 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| 300324 | china | SZSE | 4.44 | +20.00 | CNY | 4.1x | 3.70 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| OMPOWER | india | NSE | 152.74 | +19.99 | INR | 5.1x | 127.29 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| KESARPE | india | BSE | 14.07 | +19.95 | INR | 3.3x | 11.73 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| JTS | thailand | SET | 12.15 | -19.80 | THB | 5.1x | 15.15 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| BALAXI | india | NSE | 31.65 | +19.57 | INR | 4.4x | 26.47 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| MEDEZE | thailand | SET | 6.26 | +12.59 | THB | 5.9x | 5.56 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | settled | none | 2026-11-11 (7d ago) | — | no catalyst lookup (outside the per-run budget) |
| 4144 | ksa | TADAWUL | 76.95 | -10.00 | SAR | 2.2x | 85.50 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | settled | none | — | — | no catalyst lookup (outside the per-run budget) |
| PLANB | thailand | SET | 7.38 | -7.05 | THB | 2.8x | 7.94 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | settled | none | 2026-11-12 (6d ago) | — | no catalyst lookup (outside the per-run budget) |
| 6017 | ksa | TADAWUL | 9.17 | -6.24 | SAR | 2.1x | 9.78 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | settled | none | 2026-11-10 (8d ago) | — | no catalyst lookup (outside the per-run budget) |
| 4292 | ksa | TADAWUL | 28.6 | -6.17 | SAR | 2.6x | 30.48 | yahoo_chart_daily | 2026-11-17 | 2026-11-18 | settled | none | 2026-09-09 (70d ago) | N | Ataa Educational: no fresh catalyst found - no announcement on 18 Nov; the last issuer news is the 10 Nov withdrawal of a 2.1m-share buyback and the 9 Sep FY26 results (net profit SAR 97.3m, H2 dividend 7.5%), and the next results are expected on 9 Dec; the -6.2% move to SAR 28.60 continues a three-month downtrend of about -33% |
| VHP | newzealand | NZX | 1.69 | -5.59 | NZD | 4.2x | 1.79 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | settled | none | 2026-02-18 (273d ago) | — | no catalyst lookup (outside the per-run budget) |
| ME8U | singapore | SGX | 1.66 | -4.05 | SGD | 3.7x | 1.73 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | settled | none | 2026-10-27 (22d ago) | N | Mapletree Industrial Trust: a broad Singapore REIT sell-off with no company announcement - the units fell 4.05% to S$1.66 on S$42.6m of turnover (2.8x the 20-day average) as all seven SGX REITs fell, the FTSE ST REITs index dropped 1.56% against the STI -1.06%, and data-centre names were traded ahead of Nvidia's Q3 FY2027 print |
| IFT | newzealand | NZX | 13.68 | +3.64 | NZD | 2.5x | 13.20 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | settled | none | 2026-11-17 (1d ago) | — | no catalyst lookup (outside the per-run budget) |
| M44U | singapore | SGX | 1.07 | -3.60 | SGD | 3.7x | 1.11 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | settled | none | 2026-10-28 (21d ago) | N | Mapletree Logistics Trust: the same sector-wide SGX REIT de-rating with no company-specific announcement - the units fell 3.60% to S$1.07 on S$13.0m of turnover as the FTSE ST REITs index lost 1.56% and the STI fell 1.06% for a fifth straight session |
| AWX | singapore | SGX | 6.55 | +3.48 | SGD | 0.6x | 6.33 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | settled | none | 2026-08-12 (98d ago) | — | no catalyst lookup (outside the per-run budget) |
| THL | newzealand | NZX | 2.65 | -3.28 | NZD | 2.7x | 2.74 | yahoo_chart_daily | 2026-11-16 | 2026-11-17 | settled | none | 2026-08-24 (86d ago) | — | no catalyst lookup (outside the per-run budget) |

## Source health

- scanner_calls: 57 | scanner_errors: 0
- markets_scanned: US + 17 EU/UK + ASX + 7 APAC/Gulf (india, thailand, indonesia, china, singapore, newzealand, ksa)
- pipeline_version: 2026-11-16.2
- et_clock: zoneinfo America/New_York (DST-aware; a fixed UTC-4 mislabels every winter fire)
- premarket_window: 04:00-09:30 ET, resolved with zoneinfo (09:00-14:30 UTC in winter, 08:00-13:30 UTC in summer)
- session_selection: by DATE and order, never by a modal time-of-day. Yahoo stamps a daily bar at the session open, so the ET stamp of the SAME session shifts by one hour across a DST boundary; a modal filter kept the OLDER bars and discarded the NEWEST ones, which rolled the base back to the prior-prior session (66 US + 21 ASX rows lost on 2026-11-03, 24 of 25 ASX rows lost on 2026-11-04).
- yahoo_calls: 129 | yahoo_429: 0 | yahoo_errors: 0 | yahoo_breaker: closed
- reference_close (screener vs Yahoo, resolved BEFORE the tables were built): agree=117 mismatch=2 unverified=0 stale_reference=2
  method: the screener's implied reference close (close / (1 + change/100)) is compared
  with Yahoo's own reference close. A match proves the move was measured against the
  TRUE prior close; a mismatch means the row sits on a STALE reference (phantom move).
  Coverage: every row of the US headline, US QUIET, EU/UK and ASX tables is checked.
  Yahoo bar mode: {"closed": 88, "live": 29} (closed = last completed session bar;
  live = in-progress EU/UK session bar, which is what a weekday 08:00 ET EU move needs)
  live drift between the screener snapshot and the later Yahoo print: median=0.00pp max=0.97pp (expected on a live market)
- cross_check mismatches: [{"region": "germany", "symbol": "DEZ.DE", "tv": -13.467, "yahoo": -11.765, "delta": -1.702, "ref_delta_pct": 0.708, "tv_implied_ref": 9.245, "yahoo_ref": 9.18, "yahoo_date": "2026-11-18", "yahoo_ref_date": "2026-11-17", "verdict": "stale_reference"}, {"region": "indonesia", "symbol": "MKNT.JK", "tv": 33.333, "yahoo": 0.0, "delta": 33.333, "ref_delta_pct": -25.0, "tv_implied_ref": 24.0, "yahoo_ref": 32.0, "yahoo_date": "2026-11-16", "yahoo_ref_date": "2026-11-15", "verdict": "stale_reference"}]
- rows_dropped_stale_ref: 2 (rows whose screener-implied reference close disagreed with Yahoo's by more than 0.5%; they are dropped, not published)
- rows_dropped_unresolved_ref: 0 (rows whose reference close could not be resolved from Yahoo at all - the base of the move is unverifiable, so the row is dropped rather than published with a '—' base)
- us_premarket_check (Yahoo 1-min pre/post feed vs the screener pre-market column, base = the IMMEDIATELY prior session's close): checked=10 within_1pp=5 within_3pp=8 unavailable=0
  us_premarket outliers (>3pp; thin pre-market books, not a screener error): [{"symbol": "CHRN", "tv": -9.138, "yahoo": -2.098, "delta": 7.04, "yahoo_asof": "04:00"}, {"symbol": "BRBR", "tv": 8.992, "yahoo": 12.062, "delta": 3.07, "yahoo_asof": "08:06"}]
- markets_with_lt5_rows: ['uk:egreater=4', 'france:egreater=1', 'netherlands:egreater=3', 'netherlands:less=1', 'belgium:egreater=0', 'belgium:less=1', 'portugal:egreater=0', 'portugal:less=0', 'ireland:egreater=0', 'ireland:less=0', 'italy:egreater=3', 'italy:less=0', 'switzerland:less=0', 'spain:egreater=0', 'spain:less=2', 'denmark:egreater=3', 'denmark:less=4', 'finland:egreater=2', 'finland:less=1', 'austria:egreater=0', 'austria:less=1', 'greece:egreater=0', 'greece:less=1', 'singapore:egreater=4', 'newzealand:egreater=2', 'newzealand:less=3']
  NOTE: this fires per market AND direction, so it is NOT a coverage-failure signal on
  its own. A 'less' count of 0-3 means almost nothing fell more than 2.5% that session
  (a broad up-day); a small 'egreater' count usually means a small market with few
  names above the $1B market-cap floor. Check the median change before calling it a gap.
- filters: volume>10000 (removes stale-reference rows), country=home for EU/UK/AU,
  exchange drop-list for US, US venue allow-list, US preferred (slash ticker) excluded
- pass_b2 (US pre-market gap scan - "gapped today, flat yesterday"): candidates=16 deduped_against_pass_a_b=3 published=13 (up=9 down=7)
  filter: US venues, market_cap_basic > $200,000,000, close > $2, |premarket_change| >= 5.0%, premarket_volume >= 10,000 shares; two scans (up and down) because a scanner filter is AND-ed
  why it exists: on 2026-11-13 a name that was FLAT in the prior session and is not a $20bn mega-cap fell through Pass A and Pass B, so LFTO (+30.63% on the day) and SBC (+37.64%) were both missed by the routine that exists to catch same-session earnings reactions
  column measurement (2026-11-15, market `america`, US stocks): `premarket_change` and `premarket_volume` are available as BOTH a column and a FILTER (an unknown field returns 200 with zero rows, so the counts are the proof); `gap` also exists but it is the REGULAR SESSION OPEN gap, which is not knowable at the 08:00 ET fire, so `premarket_change` is the column used
  the pre-market volume floor is a DIFFERENT measure from the session-volume floor: at the 08:00 ET fire the regular session has not opened, so `volume` is 0 for every candidate and no session-volume filter is applied to this pass
- volume_floor_note: volume>10000 removes MOST stale-reference rows, but a row can
  still sit on a stale reference when its only volume came from one thin day (verified
  2026-10-26: LSE 50GP cleared the floor on 12,000 shares dated 2026-10-15 while Yahoo
  showed no bar for the scan date). The reference-close cross-check is what catches
  those; rows that fail it are dropped from the tables, not published.
- us_preferred_dropped: 59
- bod_no_extended_hours: 103 (deferred to the next scan; not in the headline table)
- earnings_source: screener `earnings_release_date` (last FULL report) + `earnings_release_next_date` (next scheduled)
- earnings_caveat: `earnings_release_date` does NOT capture preliminary, guidance or
  restructuring releases. On 2026-10-23 LKQ fell 22.47% on a preliminary Q3 miss while
  the field still read 2026-07-30. ALWAYS confirm the earnings-driven flag against the
  headline itself; the calendar field is a screen, not a verdict.
- us_line_index: ok (US-listed lines for the 25 foreign home countries, both scanner types; the `US tradeable` column is ADR / US-listed / none)
- catalyst_note: Catalyst lookups: 7 US + 4 EU + 2 AU + 3 APAC/Gulf = 16 per run - the skill's cap, allocated by the evidence gap.
- catalyst_merge: region-matched - a row may only use a catalog entry from its OWN region;
  the same ticker on another venue is a different company and is not used.
- catalyst_budget: 7 US + 4 EU + 2 AU + 3 APAC/Gulf = 16 lookups per run (cap 16), allocated by the evidence gap: the US slice covers the rows whose earnings event can still explain today's move, the EU/AU/APAC floors are never squeezed because no bulk calendar reaches those markets, and whatever the US slice does not need goes to the region with the most unexplained rows
- earnings_calendar: Nasdaq public earnings calendar (calls=8 errors=0 symbols=984) - the source of record for the US earnings date, and the ranking key for the search budget
- earnings_field_stale_rows: 3 (the screener's earnings_release_date disagreed with the calendar; the calendar's date is published)
- earnings_field_stale_detail: [{"ticker": "BORR", "screener": "2026-08-11", "calendar": "2026-11-18"}, {"ticker": "LOW", "screener": "2026-08-19", "calendar": "2026-11-18"}, {"ticker": "SA", "screener": "2026-11-13", "calendar": "2026-11-12"}]
- earnings_dates: the published `Last earnings` date by source - catalog (researched) 9, calendar 5, asx 0, screener 88. The chain is researched -> calendar (US) -> ASX feed (AU) -> the screener's field, which is the FALLBACK and the one that lags (2026-11-12: NBIS carried the previous quarter's date on the morning it reported, and MEKO, NORBT and FG carried July and August dates on the morning they all reported).
- asx_announcements: 3 results-classified announcement(s) for the last ASX session (calls=1 errors=0); the announcement date IS the report date, and the meeting/AGM/offer/assay headlines are excluded because they are not reports
- earnings_date_quality: 4 of 19 markets publish a FRESH earnings date (median age <= 14d); the table below gives each market's rows, the rows with NO date at all, the median age of the published date and the rows within 7 and 30 days - the reader sees the input quality instead of trusting it
| market | rows | no date | median age | <=7d | <=30d |
|---|---|---|---|---|---|
| au | 4 | 0 | 87d | 0 | 0 |
| china | 3 | 2 | 203d | 0 | 0 |
| denmark | 1 | 1 | n/a | 0 | 0 |
| finland | 2 | 1 | 13d | 0 | 1 |
| france | 4 | 0 | 58d | 2 | 2 |
| germany | 3 | 0 | 14d | 0 | 2 |
| india | 3 | 3 | n/a | 0 | 0 |
| indonesia | 2 | 2 | n/a | 0 | 0 |
| italy | 1 | 0 | 105d | 0 | 0 |
| ksa | 3 | 1 | 70d | 0 | 1 |
| netherlands | 2 | 0 | 142d | 0 | 1 |
| newzealand | 3 | 0 | 86d | 1 | 1 |
| norway | 4 | 0 | 20d | 2 | 4 |
| poland | 4 | 0 | 85d | 1 | 2 |
| singapore | 3 | 0 | 22d | 0 | 2 |
| sweden | 4 | 0 | 27d | 1 | 3 |
| thailand | 3 | 1 | 7d | 2 | 2 |
| uk | 4 | 0 | 97d | 1 | 1 |
| us | 49 | 0 | 13d | 12 | 45 |
- earnings_tiers: fresh=6 near=1 (fresh = the report is dated on the scan date, near = the previous session)
- one_table_rule: each name appears exactly once, in exactly one table, with its
  catalyst in that row's last column. There is no separate catalysts section.
- data_date: US regular session close of the prior trading day; extended-hours columns
  carry the prior session's prints
- settlement_state: 24 settled, 29 live (a live row's move is a mid-session snapshot, not the session's result)
- rows_per_market (EU/UK, cap 4/market): {'germany': 4, 'poland': 4, 'uk': 4, 'sweden': 4, 'france': 4, 'italy': 3, 'finland': 3, 'norway': 4, 'netherlands': 4, 'denmark': 4, 'spain': 2, 'switzerland': 4, 'greece': 1, 'belgium': 1, 'austria': 1} — the cap stops one thin market taking the table; the EU/UK table was 28% Sweden over nine runs (73 of 264 rows) while Belgium and Greece never appeared once.
- rows_per_market (APAC/Gulf, cap 3/market): {'indonesia': 3, 'china': 3, 'india': 3, 'thailand': 3, 'ksa': 3, 'newzealand': 3, 'singapore': 3}
- deprecations: mcp__tradingview-advanced__*, mcp__tradingview__*, mcp__financekit__*,
  mcp__stocktwits__* are ABSENT in Cloud sessions (tool_search 0 hits; connector catalog
  holds only media + credential tools). The public screener replaces them.

- degraded_sources: 0
  (none - every source answered for every published row)

## Audit line

`earnings-reaction target=earnings-reactions:2026-11-18 candidates=431 amc_reactions=0 pre_gaps=49 eu_reactions=29 asx_reactions=4 apac_reactions=20 catalyst_lookups=16 bod=103 pass_b2_candidates=16 pass_b2_dedup=3 pass_b2_published=13 earnings_calendar_rows=984 earnings_tiers_fresh=6 earnings_tiers_near=1 earnings_field_stale_rows=3 earnings_dates_catalog=9 earnings_dates_asx=0 asx_ann_rows=3 rows_dropped_stale_ref=2 rows_dropped_unresolved_ref=0 degraded_sources=0`
