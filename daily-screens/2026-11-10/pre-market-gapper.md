_contract: premarket-artifact-v5 · flagged: 0 · scanned: 12 · gate: |gap|>=4.0% and pm_volume>=50,000 and exec_shares>=25 · reference close: tradingview+cboe+nasdaq-secondaryData+nasdaq_historical (the 2026-11-09 sweep published no close column) · universe: 2026-11-09 · denominator session: 2026-11-09_

# Pre-Market Gapper — Tuesday, 10 November 2026

Pre-market for the Tuesday 10 Nov 2026 session · universe = the Focus list of the 18:30 ET sweep of **Monday 9 Nov 2026** (12 names) · denominator = the settled **2026-11-09** close, confirmed on 12/12 names by TradingView + Cboe + Nasdaq per-symbol history (the sweep published no close column of its own).
Tape: the Nasdaq extended-trading tape pulled **4× per name** (newest executed print **08:31–08:39 ET** for 11 of 12 names; RHLD 07:43 ET) with the live `/info` quote cross-checked at **08:38–08:39 ET** · source of record for the gap = the tape's last **executed** print, never the quote.

## TL;DR

- **0 of 12** Focus names cleared the gate (|gap| ≥ 4.0% **and** pre-market volume ≥ 50,000 shares **and** the gap-carrying print ≥ 25 shares). The widest *tape* gap in the book was **RHLD −4.42%**, and it rode on a **1-share print** — so the flag decision is immune to the tape-cache question: nothing cleared the bar on size.
- **The book is red, not gapping up.** Four names sit **outside the 4% bar on the live quote but inside it on the executed tape** — FLY (−4.73% quote / −3.54% tape), IONQ (−5.50% / −3.31%), RGTI (−5.39% / −3.16%), OKLO (−4.47% / −2.39%). A quote is not a market; the tape is where the market is, and the tape never got there.
- **The caveat that changes how you read this**: RHLD is the only name that touched the bar, its gap-carrying print is **1 share at $156.61 — below its own tape's $158.00–$160.01 range** — and its newest print is **07:43 ET, 55 minutes stale**. Treat RHLD −4.42% as a rounding artifact, not a gap.

## Focus scan — all 12 names

Sorted by absolute tape gap, largest first. `Gap %` is the last executed print vs the 2026-11-09 settled close; `Quote %` is the live `/info` price vs the same close; `PM vol % 30d` is pre-market volume as a share of the name's 30-day average (TradingView `average_volume_30d_calc`); `Sustained` = the pre-market low never traded below the prior close.

| Ticker | Ref close | PM price (last executed print) | Gap % | PM volume | Exec shares | Exec notional | PM high | PM low | Quote % | PM vol % 30d | Sustained | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RHLD | 163.8500 | 156.6100 | -4.42% | 1,986 | 1 | 156.61 | $162.72 | $158 | -1.68% | 1.5% | no | BORDERLINE_THIN |
| FLY | 24.3100 | 23.4493 | -3.54% | 134,697 | 100 | 2,344.93 | $24.07 | $23 | -4.73% | 3.7% | no | BORDERLINE_TAPE_ONLY |
| IONQ | 35.3400 | 34.1700 | -3.31% | 1,085,423 | 8 | 273.36 | $35.26 | $33.1223 | -5.50% | 4.7% | no | BORDERLINE_TAPE_ONLY |
| RGTI | 12.9800 | 12.5700 | -3.16% | 474,890 | 15 | 188.55 | $12.9 | $12.24 | -5.39% | 3.2% | no | BORDERLINE_TAPE_ONLY |
| OKLO | 26.8400 | 26.1986 | -2.39% | 269,452 | 1 | 26.20 | $27.2 | $25.464 | -4.47% | 2.5% | no | BORDERLINE_TAPE_ONLY |
| KRMN | 45.9000 | 45.0000 | -1.96% | 3,086 | 99 | 4,455.00 | $45.57 | $44.66 | -2.00% | 0.1% | no | BELOW |
| QNT | 40.0400 | 39.3800 | -1.65% | 43,467 | 2 | 78.76 | $40.3 | $38.81 | -2.83% | 1.9% | no | BELOW |
| LASR | 43.2100 | 42.5000 | -1.64% | 6,710 | 1 | 42.50 | $44.25 | $41.51 | -3.84% | 0.6% | no | BELOW |
| FROG | 108.1800 | 108.8500 | +0.62% | 6,936 | 50 | 5,442.50 | $108.24 | $106 | -1.78% | 0.3% | no | BELOW |
| ETON | 64.3500 | 64.7400 | +0.61% | 2,087 | 77 | 4,984.98 | $64.78 | $64.36 | +0.68% | 0.4% | yes | BORDERLINE_INTRADAY |
| CYRX | 20.4700 | 20.5427 | +0.35% | 1,195 | 4 | 82.17 | $20.32 | $20.32 | -0.73% | 0.1% | no | BELOW |
| TMDX | 93.7900 | 93.5000 | -0.31% | 755 | 100 | 9,350.00 | $94 | $92.92 | -1.26% | 0.1% | no | BELOW |

## Gap ladder — where the book actually sits

The 4% bar is the flag, not the story. The rungs below it, with the liquidity and the sustained-gap facts the bare bar hides.

| Rung | Name | Tape gap | PM volume | PM vol % 30d | Pre-market range | Sustained (low ≥ prior close) | Read |
|---|---|---|---|---|---|---|---|
| 4–8% — at the bar | RHLD | -4.42% | 1,986 | 1.5% | $158–$162.72 | no | the pre-market low broke the prior close |
| 2–4% — near-miss band | FLY | -3.54% | 134,697 | 3.7% | $23–$24.07 | no | the pre-market low broke the prior close |
| 2–4% — near-miss band | IONQ | -3.31% | 1,085,423 | 4.7% | $33.1223–$35.26 | no | the pre-market low broke the prior close |
| 2–4% — near-miss band | RGTI | -3.16% | 474,890 | 3.2% | $12.24–$12.9 | no | the pre-market low broke the prior close |
| 2–4% — near-miss band | OKLO | -2.39% | 269,452 | 2.5% | $25.464–$27.2 | no | the pre-market low broke the prior close |

- **≥8%: none. 4–8%: none** — the only name that touched the bar was **RHLD**, and it touched it on **1 share**. **2–4% (near-miss band)**: RHLD −4.42% (1,986 shares, 1.5% of its 30-day average), FLY −3.54% (134,697 shares, 3.7%), IONQ −3.31% (1,085,423 shares, 4.7%), RGTI −3.16% (474,890 shares, 3.2%), OKLO −2.39% (269,452 shares, 2.5%).
- **<2% (noise)**: KRMN -1.96%, QNT -1.65%, LASR -1.64%, FROG +0.62%, ETON +0.61%, CYRX +0.35%, TMDX -0.31%.
- **Sustained vs faded** (pre-market low vs the prior close): **ETON (+0.02%)** held the prior close; the other 11 names traded below it at some point in the pre-market session.

## Catalyst ahead — what reports tonight

**Two Focus names print after today's close**, and both are pre-market red — the setup is a position to hold INTO the catalyst, not a pre-market gap:

| Name | Pre-market gap (tape) | Pre-market gap (quote) | Prints | Market cap | Note |
|---|---|---|---|---|---|
| FLY (Firefly Aerospace) | −3.54% | −4.73% | Q3 2026, after the close (call 17:00 ET) | $4.07B | 4 stylists / 5 origins — the richest setup in the book, and it is red into the print |
| RGTI (Rigetti Computing) | −3.16% | −5.39% | Q3 2026, after the close (call 17:00 ET) | $4.33B | the print is the next test on the $8.4M C-DAC system acceptance; consensus revenue ~$3.68M |

The other ten Focus names report between 2027-02-11 and 2027-04-13 (TradingView `earnings_release_next_date`); RHLD has no scheduled earnings date. Source: TradingView earnings calendar, cross-checked against each issuer's own release (Firefly IR: "Third Quarter 2026 Financial Results Conference Call, November 10, 2026 | 5:00 PM EST"; Rigetti IR: "will release third quarter 2026 results on Tuesday, November 10, 2026, after market close"; call at 5:00 p.m. ET).

Outside the Focus book, the names that print **before or during** today's session and are already gapping: **GDRX** (GoodRx, Q3 after the close — consensus EPS $0.08, +4.87% pre-market), **VG** (Venture Global, Q3 at 07:30 ET, +4.24%), **EMBJ** (Embraer ADR, +5.13%), **IFNNF** (Infineon, +5.24%), **CEPU** (Central Puerto, +6.32%).

## The market's event book — pre-market gap leaders outside the Focus list

The Focus universe is a momentum screen built on the 9 Nov session's data, so it structurally cannot contain a name whose move has not happened yet. The whole US market screen found **220** names at ≥4% pre-market (snapshot 08:42 ET ET); here are the ones with a market cap above $200M and ≥50,000 pre-market shares:

| Name | Pre-market gap | PM volume | PM vol % 30d | Market cap | Catalyst |
|---|---|---|---|---|---|
| SECZ | +27.10% | 547,497 | 18.2% | 1.14B | Q3 2026 results (9 Nov, 16:15 ET): revenue $18.6M +13% y/y, tokenization revenue +29% to $11.5M, record $5.0B average tokenized assets (+39% y/y), $66.3M net loss (mostly non-cash), FY26 revenue outlook held at $70–80M; planned acquisition of River One (credit origination/underwriting) |
| HROW | +18.16% | 69,437 | 11.2% | 1.03B | Q3 2026 results (9 Nov, after the close): record revenue $99.3M (+39% y/y, +41% q/q), branded revenue $83.5M (+62% y/y), GAAP net income $9.8M vs a $17.3M loss in Q2, adj. EBITDA $21.2M; FY26 revenue guidance reaffirmed at $350–365M but FY26 adj. EBITDA guidance **cut** to >$40M from $80–100M |
| KLTR | +16.78% | 98,677 | 46.4% | 0.22B | Q3 2026 results (9 Nov, 16:05 ET): record revenue $47.3M (+8% y/y), subscription revenue $45.9M (+9%), adj. EBITDA $6.0M (+45% y/y), new subscription bookings more than doubled q/q, FY26 guidance raised — but the Q4 outlook (adj. EBITDA $2–3M) disappointed and the stock fell 5.92% in the regular session before gapping |
| SENS | +16.48% | 61,816 | 9.4% | 0.52B | Q3 2026 results (9 Nov, 16:30 ET): revenue $19.6M +140% y/y (US +160%), gross margin ~62%, FY26 revenue guidance raised to $68–70M from $62–66M; net loss $32.7M (−$0.50 vs −$0.49 consensus); EON Care network >100 inserters, Beta Bionics pump partnership |
| QMCO | +15.89% | 82,609 | 4.8% | 0.67B | Fiscal Q2 2027 results (9 Nov, after the close): adj. EPS $0.25 vs $0.13 consensus, revenue $89.6M +42.9% y/y vs $82.3M expected, gross margin 41%, adj. EBITDA $11.1M, record backlog ~$100M; FQ3 guidance $89–93M |
| PDPHF | +10.33% | 1,057,934 |  | 0.48B | Egetis Therapeutics AB (OTC ADR) — no US filing found for the move |
| BW | +9.01% | 385,445 | 8.0% | 0.56B | Q3 2026 results (9 Nov, 18:33 ET): revenue $290.8M +109% y/y, net income $93.9M (incl. warrant revaluation), EPS $0.61 vs $0.30, adj. EBITDA $17.7M (+88%), bookings $228M (+112%), **backlog $2.5B (+571%)**; FY26 adj. EBITDA target $80–105M reiterated |
| ASX | +5.94% | 116,669 | 1.2% | 75.56B | October 2026 net revenue NT$88.615B, +47.1% y/y and +0.6% m/m (ATM segment +57.7% y/y) — a monthly-revenue print, not an earnings release |
| GDRX | +4.87% | 58,451 | 5.5% | 1.25B | Q3 2026 results **after today's close** (consensus EPS $0.08); pre-market is +4.87% into the print |
| PLUG | +4.65% | 2,848,610 | 5.3% | 2.10B | Q3 2026 results (9 Nov, 16:02 ET): revenue ~$201M +13% y/y, gross margin −2.7% vs −68% a year earlier, net cash use down to ~$28M from $61M in Q2, FY26 revenue growth guidance 15–16% reaffirmed; net income $99.8M included $192M of non-cash convertible/warrant gains |
| TTWO | +4.58% | 55,088 | 2.0% | 38.78B | Fiscal Q2 2027 results: net bookings ~$1.5–1.6B vs ~$1.58B consensus, FY27 bookings outlook $8.0–8.2B reiterated, and **GTA VI confirmed for 19 Nov 2026** with pre-orders above initial expectations — the stock gapped up despite the bookings miss |
| VG | +4.24% | 652,980 | 4.3% | 29.50B | Q3 2026 results (10 Nov, 07:30 ET): revenue $4.8B, +43% y/y, year-to-date revenue ~$14B; guidance on the 09:00 ET call |

Above that size filter the screen is mostly float noise, published here because it is a fact about the tape rather than a recommendation: **PEPG +115.5%**, **SMX +77.2%**, **MNDO +46.0%**, **MI +45.7%**, **HTOO +21.8%**, **PXLW +21.7%**, **SKYE +20.7%**, **BNR +19.5%** — with market caps below $200M and pre-market volumes that are rounding artifacts rather than markets.

## Focus names that did not qualify

Every scanned name, ordered by setup quality (stylists desc, then origins count desc, then |gap| desc). Provenance is the 9 Nov sweep's own screen hits.

- **KRMN** — -1.96% · 3,086 shares · $44.66–$45.57 · 4 stylists, 6 origins
  (A_stockbee_4pct|B_stockbee_ep9m|C_qullamaggie_rs|D_qullamaggie_ep|G_peoplewish|jeff_sun_canslim)
  · setup: good setup that went nowhere — 4 stylists / 6 origins, the richest origin count in the book, and it faded to −1.96% on a 3,086-share pre-market market (0.1% of its 30-day average). Nothing was really trading.
- **FLY** — -3.54% · 134,697 shares · $23–$24.07 · 4 stylists, 5 origins
  (A_stockbee_4pct|B_stockbee_ep9m|D_qullamaggie_ep|G_peoplewish|TV_volume_breakout)
  · setup: good setup that went nowhere, and it is the one to watch — 4 stylists / 5 origins on the best size in the book (100 shares at $23.4493, 134,697 shares = 3.7% of its 30-day average), red into its own 16:10 ET print.
- **OKLO** — -2.39% · 269,452 shares · $25.464–$27.2 · 4 stylists, 5 origins
  (A_stockbee_4pct|B_stockbee_ep9m|D_qullamaggie_ep|G_peoplewish|TV_volume_breakout)
  · setup: good setup that went nowhere — 4 stylists / 5 origins, 269,452 pre-market shares (2.5% of its 30-day average), and the gap-carrying print was **1 share** at $26.1986.
- **RGTI** — -3.16% · 474,890 shares · $12.24–$12.9 · 3 stylists, 4 origins
  (A_stockbee_4pct|B_stockbee_ep9m|G_peoplewish|TV_volume_breakout)
  · setup: good setup that went nowhere — 3 stylists / 4 origins, 474,890 pre-market shares (3.2% of its 30-day average), and the gap-carrying print was 15 shares at $12.57; it reports after the close.
- **TMDX** — -0.31% · 755 shares · $92.92–$94 · 3 stylists, 4 origins
  (A_stockbee_4pct|D_qullamaggie_ep|E_qullamaggie_5d_gainers|G_peoplewish)
  · setup: bad setup — 3 stylists / 4 origins, but 755 pre-market shares is 0.1% of its 30-day average and the last print moved it −0.31%. Nothing was really trading.
- **FROG** — +0.62% · 6,936 shares · $106–$108.24 · 3 stylists, 3 origins
  (A_stockbee_4pct|D_qullamaggie_ep|G_peoplewish)
  · setup: bad setup — 3 stylists / 3 origins on a 6,936-share pre-market market (0.3% of its 30-day average); the last print was $108.85, above the payload's own pre-market high of $108.24.
- **IONQ** — -3.31% · 1,085,423 shares · $33.1223–$35.26 · 2 stylists, 3 origins
  (A_stockbee_4pct|B_stockbee_ep9m|G_peoplewish)
  · setup: good setup that went nowhere — 3 stylists / 3 origins and the heaviest pre-market market in the book (1,085,423 shares, 4.7% of its 30-day average), and the gap-carrying print was 8 shares.
- **RHLD** — -4.42% · 1,986 shares · $158–$162.72 · 2 stylists, 2 origins
  (A_stockbee_4pct|TV_volume_breakout)
  · setup: bad setup — 2 stylists / 2 origins; the only name that touched the 4% bar, and it did so on a **1-share** print at $156.61, below its own tape's $158.00–$160.01 range, on 1,986 shares (1.5% of its 30-day average).
- **QNT** — -1.65% · 43,467 shares · $38.81–$40.3 · 2 stylists, 2 origins
  (A_stockbee_4pct|G_peoplewish)
  · setup: bad setup — 2 stylists / 2 origins on a 43,467-share pre-market market (1.9% of its 30-day average) and a 2-share print carrying the gap.
- **LASR** — -1.64% · 6,710 shares · $41.51–$44.25 · 2 stylists, 2 origins
  (A_stockbee_4pct|TV_volume_breakout)
  · setup: bad setup — 2 stylists / 2 origins on a 6,710-share pre-market market (0.6% of its 30-day average); the gap-carrying print was 1 share at $42.50.
- **ETON** — +0.61% · 2,087 shares · $64.36–$64.78 · 2 stylists, 2 origins
  (A_stockbee_4pct|TV_volume_breakout)
  · setup: bad setup — 2 stylists / 2 origins, the only name in the book whose pre-market low **held** the prior close (+0.02%), but the market behind it was 2,087 shares (0.4% of its 30-day average). Its "crossed the bar intraday" leg is a tape artifact — see Flags.
- **CYRX** — +0.35% · 1,195 shares · $20.32–$20.32 · 2 stylists, 2 origins
  (A_stockbee_4pct|TV_volume_breakout)
  · setup: bad setup — 2 stylists / 2 origins on 1,195 pre-market shares (0.1% of its 30-day average) and a 4-share print carrying the gap.

## Flags

- **RHLD −4.42% "crossed the bar"** — the print that carries the gap is **1 share at $156.61**, and it sits **below its own tape's range** ($158.00–$160.01). The market that actually traded was −1.3% to −2.35%; the −4.42% is a rounding artifact, not a gap.
- **RHLD's tape is 55 minutes stale**: the newest executed print the endpoint served was **07:43:39 ET** while the live quote was taken at **08:38 ET** (quote $161.09, −1.68%). Its published tape gap (−4.42%) and its quote (−1.68%) are **not the same moment**.
- **ETON's "crossed the bar intraday" leg is a tape artifact** — it rests on a single print at **−12.88%** (≈$56.06) against the same payload's own pre-market range of **$64.36–$64.78**. The snapshot gap was +0.61% and the name was the only one in the book whose low held the prior close.
- **FLY, IONQ, RGTI and OKLO are past the bar on the live quote but inside it on the executed tape** — FLY −4.73% quote vs −3.54% tape; IONQ −5.50% vs −3.31%; RGTI −5.39% vs −3.16%; OKLO −4.47% vs −2.39%. The bid/ask bands were not returned by the quote payload, so the divergence is published as the gap pair rather than as a band.
- **OKLO's gap-carrying print was 1 share** at $26.1986 (269,452 pre-market shares behind it) — the 2.39% tape reading is on a rounding-sized print.
- **Every name's pre-market volume came from the Nasdaq cumulative counter**, not from the tape sum; the `pm_volume_source` column carries the source on every row.
- **The Focus-list volume ratio is thin everywhere**: the heaviest pre-market market in the book (IONQ, 1,085,423 shares) is 4.7% of its own 30-day average. No Focus name came close to the 50,000-share floor on a *scaled* basis, which is why the near-miss band reads as thin rather than tradeable.
- **KRMN's reference close disagreed with one source**: Nasdaq `secondaryData` read $45.8650 against the $45.9000 settled close that TradingView, Cboe and Nasdaq's own per-symbol history all carry. The settled close was published; the drifting field is named here and was not allowed to set the denominator.

## Method, source health & caveats

- **Universe (proved, not assumed)**: `scripts/premarket_universe.py` resolved the expected prior session **from the market's own session history** (Nasdaq SPY history) as **2026-11-09** and asserted H1–H5: a published Focus list exists for that session, its session **equals** 2026-11-09, every name has a reference close for that session, and every close is confirmed by an independent source (12/12). The resolver's status is `OK_WITH_FLAGS`.
- **The sweep published its Focus list as MARKDOWN, not CSV**: `daily-screens/2026-11-09/` contains `focus.md` (12 names with provenance) but **no `focus.csv`** — the `focus` screen's manifest entry says "no .csv for this screen". The fetched resolver looks only for `focus.csv` and its walk aborted on the 404, so a resolver that had not been patched would have walked back to the **2026-11-06** sweep and measured today's gaps against the wrong day's names. The local copy was patched to read the markdown Focus list (with the stylist names recovered from the sweep's canonical `_results.json`) and to treat a missing file as "not published" instead of an exception. **That fix was landed in the repo on 2026-11-10** — `scripts/premarket_universe.py` marker `premarket-universe-v2`, merged into `main`, with the fetch ladder now demanding the new marker, so the next fire picks it up with no prompt change and no redeploy; the repo's own regression test, which could not run at all until the resolver path was fixed, now pins 31 checks. **Cron #09 should publish `focus.csv` again**: a markdown-only Focus list is a degraded publish, and the next routine that needs a machine-readable universe will hit the same door.
- **Reference close**: the universe carried no close column, so the denominator comes from the **independent sources only** — TradingView `close`, Cboe delayed-quote `close` and Nasdaq's session-exact per-symbol history agreed on **12/12** names. Nasdaq `secondaryData` agreed on 11/12 (KRMN drifted, see Flags) and was never allowed to set the denominator alone. The denominator session is **2026-11-09** for every row (`universe_date` = `ref_close_date` = 2026-11-09).
- **Tape freshness**: 4 pulls per symbol; the payload with the newest internal timestamp wins (a stale vintage can never carry a newer timestamp). Newest print per symbol: **08:31–08:39 ET** for 11 of 12 names; **RHLD 07:43:39 ET** (see Flags). The shared HTTP cache on `api.nasdaq.com/api/quote/{sym}/extended-trading` is real — it was defeated by the max-timestamp rule, not by a cache-busting query string.
- **Volume**: the published `pm_volume` is the Nasdaq cumulative counter; where the payload's tape was complete (<100 rows) it arbitrated the counter and the source is recorded per row in `pm_volume_source`.
- **Nasdaq `/info` defects checked this run**: `secondaryData.lastSalePrice` vs the settled close (agreed 11/12, KRMN drifted); `primaryData.lastSalePrice` being an ASK rather than a trade; trivial-size prints (the last-print share count is published on every row — five of the twelve gaps ride on ≤15 shares); `premarket_price` being null in the TradingView scanner for US names (so only `premarket_change` / `premarket_high` / `premarket_low` / `premarket_volume` were taken from TV).
- **TradingView `premarket_volume` undercounts** (FLY 101,881 vs Nasdaq 134,697; IONQ 431,122 vs 1,085,423; RGTI 239,466 vs 474,890; OKLO 165,419 vs 269,452; QNT 20,502 vs 43,467) and `premarket_change` is measured against TradingView's own close — TV was used as a cross-check and for `average_volume_30d_calc`, **never** for the 50,000-share test.
- **Margin against the trigger**: the widest *tape* gap in the book was **−4.42% (RHLD)** and the widest *quote* gap **−5.50% (IONQ)**. RHLD's −4.42% rests on a 1-share print and its tape is 55 minutes stale, so no reading on any source would have produced a flag: **the flag decision is immune to the stale-cache question.**
- **Sustained-gap fact**: `pm_low_gap_pct ≥ 0` means the pre-market low never traded below the prior close. Only **ETON** held (+0.02%); the other eleven broke the prior close at some point. It is computed from the same published range, needs no new source, and is the cheapest quality filter in the scan.
- **Not used**: `preopen-feed/` was not consulted — the catalysts above come from issuer press releases / SEC filings and the TradingView earnings calendar, and the substitution is disclosed here rather than left silent. TTWO's EPS figure was reported inconsistently across wires (Benzinga: $0.99 vs a $0.94 consensus; a second outlet: a $0.29 loss vs $0.97 expected), so only the bookings and the GTA VI release date — which both wires agree on — are published here.
- **Scope note**: the Focus list is the 18:30 ET sweep of 9 Nov 2026 (12 names). No re-filtering on domicile or share type was applied, and no name was dropped for failing to qualify — all 12 are published with their provenance.
