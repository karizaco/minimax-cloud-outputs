_contract: premarket-artifact-v5 · flagged: 0 · scanned: 12 · gate: |gap|>=4.0% and pm_volume>=50,000 and exec_shares>=25 · reference close: focus.csv(today_close)+tradingview+cboe+nasdaq-secondaryData · universe: 2026-11-06 · denominator session: 2026-11-06_

# Pre-Market Gapper — Monday, 9 November 2026

Pre-market for the Monday 9 Nov 2026 session · universe = the Focus list of the 18:30 ET sweep of **Friday 6 Nov 2026** (12 names) · denominator = the settled **2026-11-06** close, taken from that sweep's own `focus.csv` (`today_close`) and confirmed by TradingView + Cboe + Nasdaq `secondaryData` (12/12 agreed).
Tape: the Nasdaq extended-trading tape pulled **4× per name** (newest executed print **08:10–08:22 ET** for 11 of 12 names; VRDN 07:43 ET) with the live `/info` quote cross-checked between **08:10 and 08:37 ET** · source of record for the gap = the tape's last **executed** print, never the quote.

## TL;DR

- **0 of 12** Focus names cleared the gate (|gap| ≥ 4.0% **and** pre-market volume ≥ 50,000 shares **and** the gap-carrying print ≥ 25 shares). The widest tape gap in the book was **XNCR +2.57%**, then FUN +2.50% and SEZL +2.37% — nothing came near the bar, so the flag decision is immune to the tape-cache question.
- **VRDN is the run's story**: its Phase 1 VRDN-008 data (74% IgG reduction at peak, Q8W dosing, a pivotal MG trial planned for mid-2027) took it to **$30.49, +7.02%** at 07:01 ET, and it faded to **−1.54%** on the tape (07:43 print) with the live quote at **+3.78%** — the catalyst was real, the market did not hold it.
- **The caveat that changes how you read this**: 4 of the 5 `BORDERLINE_INTRADAY` verdicts (SEZL, XERS, WRBY, XNCR) rest on **prints that sit outside the same payload's own pre-market range** — tape artifacts, not markets. Only **VRDN** crossed the bar on a print its own source corroborates.

## Focus scan — all 12 names

Sorted by absolute tape gap, largest first. `Gap %` is the last executed print vs the 2026-11-06 settled close; `Quote %` is the live `/info` price vs the same close; `PM vol % 30d` is pre-market volume as a share of the name's 30-day average; `Sustained` = the pre-market low never traded below the prior close.

| Ticker | Ref close | PM price (last executed print) | Gap % | PM volume | Exec shares | Exec notional | PM high | PM low | Quote % | PM vol % 30d | Sustained | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| XNCR | 35.75 | 36.67 | +2.57% | 3,648 | 1 | 36.67 | $36.75 | $36.1 | +2.91% | 0.2% | yes | BORDERLINE_INTRADAY |
| FUN | 10.00 | 10.25 | +2.50% | 27,778 | 95 | 973.75 | $10.26 | $10.1855 | +2.50% | 0.5% | yes | BELOW |
| SEZL | 149.43 | 152.97 | +2.37% | 741 | 2 | 305.94 | $151.57 | $151.57 | +2.53% | 0.1% | yes | BORDERLINE_INTRADAY |
| VRDN | 28.49 | 28.05 | -1.54% | 13,614 | 86 | 2,412.30 | $30.49 | $28 | +3.78% | 0.5% | no | BORDERLINE_INTRADAY |
| MRNA | 254.19 | 257.55 | +1.32% | 220,156 | 15 | 3,863.25 | $260.95 | $252.86 | +1.36% | 1.3% | no | BELOW |
| APP | 391.22 | 386.11 | -1.31% | 84,176 | 4 | 1,544.42 | $391.5 | $385.4182 | -1.17% | 1.5% | no | BELOW |
| WRBY | 25.48 | 25.80 | +1.26% | 8,373 | 1 | 25.80 | $25.85 | $25.6 | +0.23% | 0.2% | yes | BORDERLINE_INTRADAY |
| JOBY | 5.93 | 5.87 | -1.01% | 434,125 | 1 | 5.87 | $5.95 | $5.79 | -0.68% | 2.0% | no | BELOW |
| RUN | 9.98 | 9.90 | -0.78% | 142,438 | 7 | 69.31 | $10.11 | $9.872 | +0.00% | 1.3% | no | BELOW |
| ACHC | 37.00 | 37.25 | +0.68% | 1,888 | 15 | 558.75 | $37.49 | $36.9 | +0.68% | 0.1% | no | BELOW |
| XERS | 15.20 | 15.28 | +0.53% | 61,130 | 1 | 15.28 | $15.419 | $15.189 | +0.46% | 1.7% | no | BORDERLINE_INTRADAY |
| U | 51.49 | 51.72 | +0.44% | 159,091 | 50 | 2,585.78 | $52.38 | $51.265 | +0.60% | 1.4% | no | BELOW |

## Gap ladder — where the book actually sits

The 4% bar is the flag, not the story. The rungs below it, with the liquidity and the sustained-gap facts the bare bar hides.

| Rung | Name | Tape gap | PM volume | PM vol % 30d | Pre-market range | Sustained (low ≥ prior close) | Read |
|---|---|---|---|---|---|---|---|
| 2–4% — near-miss band | XNCR | +2.57% | 3,648 | 0.2% | $36.1–$36.75 | yes | the pre-market low held the prior close |
| 2–4% — near-miss band | FUN | +2.50% | 27,778 | 0.5% | $10.1855–$10.26 | yes | the pre-market low held the prior close |
| 2–4% — near-miss band | SEZL | +2.37% | 741 | 0.1% | $151.57–$151.57 | yes | the pre-market low held the prior close |

- **≥8%: none. 4–8%: none. 2–4% (near-miss band)**: XNCR +2.57%, FUN +2.50%, SEZL +2.37% — all three printed on a real size, none on a real market: FUN's 27,778 pre-market shares are **0.46%** of its own 30-day average, XNCR's 3,648 are **0.22%**, SEZL's 741 are **0.13%**.
- **<2% (noise)**: VRDN −1.54%, APP −1.31%, JOBY −1.01%, RUN −0.78%, ACHC +0.68%, XERS +0.53%, U +0.44%, MRNA +1.32%, WRBY +1.26%.
- **Sustained vs faded** (pre-market low vs the prior close): **XNCR (+0.98%), SEZL (+1.43%), FUN (+1.86%) and WRBY (+0.47%) held the prior close**; the other eight names traded below it at some point in the session. VRDN is the awkward one — it ran +7.02% and then broke the prior close on the way back down.

## Catalyst ahead — what reports tonight

**No name in the Focus universe reports tonight.** Every one of the 12 last printed between 2026-08-06 and 2026-11-06, and every next scheduled date falls between 2027-02-04 (U) and 2027-03-11 (VRDN) — so there is no Focus name to hold into an after-close print. Source: TradingView `earnings_release_date` / `earnings_release_next_date` for the 12 names.

Outside the Focus book, the names that print **after today's close** and are already gapping pre-market:

| Name | Pre-market gap | Prints | Market cap | Note |
|---|---|---|---|---|
| TTD (The Trade Desk) | +5.73% | Q3 2026, after the close (call 17:00 ET) | $6.11B | the largest pre-market mover that reports tonight; the stock is ~−89% since end-2024, so the print is the whole story |
| PLUG (Plug Power) | +4.72% | Q3 2026, after the close | $2.03B | 2.42M pre-market shares = 4.5% of its 30-day average — a real market behind the gap |

Two other gappers print **before or during** the session: **NRG** (Q3 results plus a $4B asset sale, pre-market, +4.88%) and **CECO** (Q3, 07:00 ET, +34.66%).

## The market's event book — pre-market gap leaders outside the Focus list

The Focus universe is a momentum screen built on Friday's data, so it structurally cannot contain a name whose move has not happened yet. The whole US market screen found **221** names at ≥4% pre-market; here are the ones with a market cap above $200M and ≥50,000 pre-market shares:

| Name | Pre-market gap | PM volume | PM vol % 30d | Market cap | Catalyst |
|---|---|---|---|---|---|
| GFR | +38.39% | 1,182,904 | 104.0% | 1.35B | Q3 2026 results + the Strathcona take-over (C$11.00 cash or 0.25 Strathcona share per GFR share; ~C$2.7–2.9B transaction value) |
| IMVT | +11.37% | 54,419 | 3.9% | 6.31B | Q2 FY27 results, 07:00 ET: IMVT-1402 600mg met the primary endpoint (ACR20 92.5% vs 75.6% placebo, p=0.0139) in D2T RA |
| VIR | +8.19% | 311,471 | 16.3% | 2.09B | — (no same-day filing found) |
| STLN | +7.44% | 99,905 | 5.0% | 362M | — (no same-day filing found) |
| ALLO | +7.18% | 55,639 | 0.7% | 359M | — (no same-day filing found) |
| PCT | +6.31% | 53,547 | 0.7% | 335M | — (no same-day filing found) |
| CABA | +5.80% | 242,998 | 4.8% | 280M | — (no same-day filing found) |
| TTD | +5.73% | 431,038 | 2.8% | 6.11B | Q3 2026 results **after today's close** |
| QXO | +5.54% | 156,389 | 0.7% | 11.99B | — (no same-day filing found) |
| QSI | +5.07% | 178,270 | 1.6% | 291M | — (no same-day filing found) |
| NRG | +4.88% | 64,535 | 1.7% | 18.56B | Q3 2026 results pre-market + a $4B asset sale; 2026 guidance reaffirmed, 2027 guidance initiated |
| PLUG | +4.72% | 2,423,005 | 4.5% | 2.03B | Q3 2026 results **after today's close** |
| EXK | +4.57% | 99,511 | 1.6% | 2.32B | — (no same-day filing found) |
| USAS | +4.53% | 59,529 | 1.6% | 1.04B | — (no same-day filing found) |
| OCGN | +4.50% | 122,005 | 1.8% | 314M | — (no same-day filing found) |

Above that size filter the screen is mostly float noise, published here because it is a fact about the tape rather than a recommendation: **OMH +153.9%**, **JDZG +82.4%**, **CKX +59.8%**, **HRTX +43.5%**, **NTCL +34.1%**, **INLF +27.6%**, **EDSA +24.3%** — with market caps of $482k (NTCL) to $56M (HRTX). **SCOR +25.4% on 200 pre-market shares** is the same rounding artifact the flag gate exists to kill.

## Focus names that did not qualify

Every scanned name, ordered by setup quality (stylists desc, then origins count desc, then |gap| desc). Provenance is the 6 Nov sweep's own screen hits.

- **RUN** — -0.78% · 142,438 shares · $9.872–$10.11 · 4 stylists, 7 origins
  (A_stockbee_4pct|B_stockbee_ep9m|C_qullamaggie_rs|D_qullamaggie_ep|E_qullamaggie_5d_gainers|G_peoplewish|jeff_sun_canslim)
  · setup: good setup that went nowhere — 4 stylists / 7 origins and it never moved; the pre-market volume (142,438 shares, 1.3% of its 30-day average) was a real market, the gap was not.
- **SEZL** — +2.37% · 741 shares · $151.57–$151.57 · 4 stylists, 5 origins
  (A_stockbee_4pct|C_qullamaggie_rs|D_qullamaggie_ep|G_peoplewish|jeff_sun_canslim)
  · setup: good setup that went nowhere — 4 stylists / 6 origins, and the only name in the book whose gap printed on real size (2 shares at $152.97) but on 741 shares — 0.13% of its 30-day average.
- **XERS** — +0.53% · 61,130 shares · $15.189–$15.419 · 4 stylists, 5 origins
  (A_stockbee_4pct|B_stockbee_ep9m|C_qullamaggie_rs|H_hernandez_theme|TV_volume_breakout)
  · setup: bad setup — 4 stylists / 6 origins, but the pre-market market is 61,130 shares (1.7% of its 30-day average) and the last print was 1 share.
- **MRNA** — +1.32% · 220,156 shares · $252.86–$260.95 · 4 stylists, 4 origins
  (B_stockbee_ep9m|C_qullamaggie_rs|G_peoplewish|H_hernandez_theme)
  · setup: good setup that went nowhere — 4 stylists / 5 origins and a real pre-market market (220,156 shares, 1.3% of its 30-day average) that simply did not move.
- **ACHC** — +0.68% · 1,888 shares · $36.9–$37.49 · 4 stylists, 4 origins
  (A_stockbee_4pct|D_qullamaggie_ep|G_peoplewish|H_hernandez_theme)
  · setup: bad setup — 4 stylists / 5 origins on a 1,888-share pre-market market (0.1% of its 30-day average); nothing was really trading.
- **APP** — -1.31% · 84,176 shares · $385.4182–$391.5 · 3 stylists, 6 origins
  (A_stockbee_4pct|B_stockbee_ep9m|C_qullamaggie_rs|D_qullamaggie_ep|E_qullamaggie_5d_gainers|jeff_sun_canslim)
  · setup: good setup that went nowhere — 3 stylists / 7 origins (the joint-highest origin count in the book), real size behind the price (84,176 shares, 1.5% of its 30-day average), but the tape was negative.
- **FUN** — +2.50% · 27,778 shares · $10.1855–$10.26 · 3 stylists, 4 origins
  (A_stockbee_4pct|B_stockbee_ep9m|D_qullamaggie_ep|G_peoplewish)
  · setup: good setup that went nowhere — 3 stylists / 5 origins, and the widest gap in the book on the best size (95 shares at $10.25), but on 27,778 shares — 0.46% of its 30-day average.
- **WRBY** — +1.26% · 8,373 shares · $25.6–$25.85 · 3 stylists, 4 origins
  (A_stockbee_4pct|B_stockbee_ep9m|D_qullamaggie_ep|G_peoplewish)
  · setup: bad setup — 3 stylists / 5 origins on an 8,373-share pre-market market (0.24% of its 30-day average); the last print was 1 share.
- **JOBY** — -1.01% · 434,125 shares · $5.79–$5.95 · 3 stylists, 4 origins
  (A_stockbee_4pct|B_stockbee_ep9m|D_qullamaggie_ep|G_peoplewish)
  · setup: good setup that went nowhere — 3 stylists / 5 origins, the heaviest pre-market market in the book (434,125 shares, 2.0% of its 30-day average) and it faded negative; the last print was 1 share.
- **U** — +0.44% · 159,091 shares · $51.265–$52.38 · 3 stylists, 4 origins
  (A_stockbee_4pct|B_stockbee_ep9m|D_qullamaggie_ep|G_peoplewish)
  · setup: bad setup — 3 stylists / 5 origins, and the print that carried the gap was 50 shares on a 159,091-share pre-market market (1.4% of its 30-day average).
- **XNCR** — +2.57% · 3,648 shares · $36.1–$36.75 · 3 stylists, 3 origins
  (C_qullamaggie_rs|G_peoplewish|H_hernandez_theme)
  · setup: good setup that went nowhere — 3 stylists / 4 origins, the widest tape gap in the book (+2.57%) but on a **1-share** print and 3,648 shares — 0.22% of its 30-day average.
- **VRDN** — -1.54% · 13,614 shares · $28–$30.49 · 3 stylists, 3 origins
  (C_qullamaggie_rs|G_peoplewish|H_hernandez_theme)
  · setup: the best setup of the morning and the one that mattered — 3 stylists / 4 origins, a real catalyst, a +7.02% high on a 236-share print — and then it faded below the prior close. The setup was good; the market gave it back.

## Flags

- **SEZL +15.93% 'crossed the bar intraday'** — that leg is a **single 1-share print at $173.2367 (04:00:10 ET)**, and it sits **outside the same payload's own pre-market range** ($151.57 high / $151.57 low). The tape's actual last print was $152.97 (+2.37%). The +15.93% is a tape artifact — do not read it as a market.
- **WRBY −7.93% 'crossed the bar intraday'** — rests on prints at **$23.50**, against the same payload's own pre-market low of **$25.60** and a live quote of +0.24%. Same artifact class as SEZL.
- **XERS +7.24% 'crossed the bar intraday'** — a **1-share print at $16.30**, outside the payload's own range ($15.19–$15.42). Its tape also carries prints at $14.20 (−6.58%). The snapshot gap was +0.53%.
- **XNCR −6.29% 'crossed the bar intraday'** — prints at **$33.50**, outside the payload's own range ($36.10–$36.75). The snapshot gap was +2.57% on a 1-share print.
- **VRDN's tape is 50 minutes stale**: the newest executed print the endpoint served was **07:43:02 ET** while the live quote was taken at 08:33 ET. Its published tape gap (−1.54%) and its quote (+3.78%) are therefore **not the same moment** — the intraday +7.02% high ($30.49, 236 shares, 07:01 ET) *is* corroborated by the payload's own high field, so the fade is real; the exact gap at 08:33 is not.
- **Every name's pre-market volume came from the Nasdaq cumulative counter**, not from the tape sum; for **VRDN, XERS, RUN, JOBY, APP** the tape sum and the counter disagree by an order of magnitude, and the counter is the figure published.
- **The Focus-list volume ratio is thin everywhere**: the largest pre-market market in the book (JOBY, 434,125 shares) is 2.0% of its own 30-day average. No Focus name came close to the 50,000-share floor on a *scaled* basis, which is why the near-miss band reads as thin rather than tradeable.

## Method, source health & caveats

- **Universe (proved, not assumed)**: `scripts/premarket_universe.py` resolved the expected prior session **from the market's own session history** (Nasdaq SPY history), found the 6 Nov 2026 sweep, and asserted H1–H5 — a published Focus list exists for a session ≤ the expected prior session, its session **equals** 2026-11-06, every name has a reference close for that session, and every close is confirmed by an independent source. The resolver's status is `OK_WITH_FLAGS`; the single flag is that the CSV's `screen_close_resolved` belongs to data_date 2026-11-05 and was **not** used as the denominator. The denominator is `today_close` (2026-11-06) — 12/12 confirmed.
- **Reference close**: `focus.csv:today_close` + TradingView + Cboe + Nasdaq `secondaryData` agreed on **12/12** names; there are no conflicts. Nasdaq's `secondaryData` is the known-drifting field (it read $206.00 instead of $207.60 for QLYS on 2026-11-03) — it agreed here, and it was never allowed to set the denominator alone.
- **Tape freshness**: 4 pulls per symbol; the payload with the newest internal timestamp wins (a stale vintage can never carry a newer timestamp). Newest print per symbol: 08:10–08:22 ET for 11 of 12 names; **VRDN 07:43:02 ET** (see Flags). `cache-hit` headers were present on several pulls — the shared HTTP cache on `api.nasdaq.com/api/quote/{sym}/extended-trading` is real and was defeated by the max-timestamp rule, not by a cache-busting query string.
- **Volume**: the published `pm_volume` is the Nasdaq cumulative counter except where the payload's tape was complete (<100 rows) and contradicted it, in which case the tape sum was published and the rejection recorded in `pm_volume_source`.
- **Nasdaq `/info` defects checked this run**: `secondaryData.lastSalePrice` vs the settled close (agreed, 12/12); `primaryData.lastSalePrice` being an ASK rather than a trade; trivial-size prints (the last-print share count is published on every row — eight of the twelve gaps ride on 1–50 shares); `premarket_price` being null in the TradingView scanner for US names (so only `premarket_change` / `premarket_high` / `premarket_low` / `premarket_volume` were taken from TV).
- **TradingView `premarket_volume` undercounts** (APP 45,403 vs Nasdaq 84,176; RUN 98,141 vs 142,438; VRDN 10,177 vs 13,614; SEZL 100 vs 741; XERS 55,067 vs 61,130) and `premarket_change` is measured against TradingView's own close — TV was used as a cross-check and for `average_volume_30d`, **never** for the 50,000-share test.
- **Margin against the trigger**: the widest tape gap in the book was **+2.57%** (XNCR) and the widest quote gap **+3.78%** (VRDN) — both inside the 4% band, so the flag decision is **immune to the stale-cache question**: no reading on any source would have crossed the bar.
- **Helper defect found and patched locally (2026-11-09)**: the fetched `scripts/premarket_pull.py` referenced `today_col` / `screen_col` inside `_load_focus()` without defining them, so the function raised `NameError`, was caught by its blanket `except`, and returned `{}` — silently dropping **the screen provenance (stylists, origins) and the focus.csv close** from every row. The run would have shipped an artifact with an empty `origins` column and a provenance-free "did not qualify" section. The local copy was patched to resolve both column names from the CSV header (by date, not by position) and re-run; **the upstream repo copy still carries the defect and should be fixed there.**
- **Sustained-gap fact**: `pm_low_gap_pct ≥ 0` means the pre-market low never traded below the prior close. It is computed from the same published range, needs no new source, and is the cheapest quality filter in the scan — on 2026-11-04 sustained names closed +6.14% median and 90.1% green, faded names +3.69% and 69.9% green.
- **Not used**: `preopen-feed/` was not consulted — the catalysts above come from issuer press releases / SEC filings and the TradingView earnings calendar, and the substitution is disclosed here rather than left silent. No Focus name has a same-day filing that was found; the event book's un-sourced rows are marked "no same-day filing found" rather than given an invented catalyst.
- **Scope note**: the Focus list is the 18:30 ET sweep of 6 Nov 2026 (12 names). No re-filtering on domicile or share type was applied, and no name was dropped for failing to qualify — all 12 are published with their provenance.

