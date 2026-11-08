# Reversal Bullish (Bonde) — 3:55 PM ET — 2026-10-26 (Mon)

> **CORRECTION — added 2026-10-30.** This artifact was produced by a manual
> (non-scheduled) execution of the pre-2026-10-28 cron prompt, and it applied Bonde's criteria
> as literal SQL floors. On review against the *published* criterion and the routine's own
> 2026-10-29 run, **two rules were not applied as filters**, and one name changes:
> **CBRE (tail:body 13.0×) falls outside Bonde's published 3–5× tail band and is rejected.**
> CELH remains the single clean qualifier; HIMS remains a floor-exact boundary pass. Full
> correction at the foot of this document.

**Data: 2026-10-26 (Mon) — FINAL 16:00 ET CLOSE** · **Universe:** 342 large/mega-caps · **Source:** `_source=tv_yahoo_fallback`_

> **First live-window run of this cron.** Every prior fire (2026-09-28 → 2026-10-24) landed at ~04:55 ET pre-market, so the scan ran on the *previous* session's close and the artifact was a planning snapshot for the later 15:55 ET run. This fire landed at **15:55 ET — inside Bonde's 15:30–16:00 ET window** — so the scan ran on **today's live session bar**, refreshed at 15:59:54 ET and then re-pulled post-close at 16:01–16:02 ET for **final 16:00 closes**. All 341 symbols carried today's bar; zero stale. Every number below is a settled close, not an intraday print. The 15:58–16:00 ET MOC entry window Bonde specifies is the operative one for this list.

## Results — 3 candidates passed all 8 Bonde criteria

| # | Symbol | Close | Chg% | DCR | Body% | Tail:Body | ADR% | 20d Trend | 2d Drop | 5d Low | Body Low Stop | Mkt Cap |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **CELH** | $28.15 | -1.65% | 0.899 | 0.17 | 4.3 | 4.01 | +0.54% | -0.74% | $27.90 | $28.00 | $7.1B |
| 2 | **CBRE** | $122.89 | -0.36% | 0.509 | 0.04 | 13.0 | 3.29 | -5.72% | -6.36% | $123.04 | $122.79 | $35.4B |
| 3 | **HIMS** | $27.58 | -0.27% | 0.500 | 0.10 | 4.1 | 6.04 | -4.17% | -5.32% | $27.30 | $27.51 | $6.4B |

### Notes per name (catalyst-checked)

- **CELH** ($28.15) — **Highest conviction.** DCR 0.90 (closed at 0.90 of the day's range), tail:body 4.27, body only 17% of range, 20d trend +0.54% (flat — no trend damage). Today's low $27.36 was a fresh 5-day low (prior 5d low $27.90), then the stock closed at $28.15 near the session high $28.24 — a textbook Bonde rejection-of-lows hammer. **Catalyst check:** Q3 earnings are *not* until Nov 5 (the Aug 6 Q2 print was the last report), so there is no imminent binary event inside the hold window. The overhang is legal, not operational: securities class action over Alani Nu cardiac/teen-marketing allegations (lead-plaintiff deadline Nov 3), a wrongful-death suit and a Texas AG probe. Offsetting: Q2 revenue was still a record ~$818M (+11% YoY), Alani Nu net sales +21%, and there was reported insider buying (TD Waterhouse Canada, Oct 21). The stock is rebounding from its October lows into that overhang — tradeable, but legal headlines can gap it. Note: the Q2 miss (EPS $0.36 vs $0.41 est, rev $818M vs $870M est) caused -18.5% in one session — this is a high-beta name.

- **CBRE** ($122.89) — **Best structural story, most fragile trend.** DCR 0.51 (just over the 0.50 floor), tail:body 13.0, body 3.6% of range — a near-doji with a long lower wick: O $122.79 / H $124.24 / L $121.49 / C $122.89. **Catalyst check is the story:** Q3 2026 reported Oct 22 pre-market — core EPS $2.05 beat (vs ~$1.96 est, +28% YoY), GAAP EPS $1.52 +26%, revenue $11.5B +13% but **missed** consensus (~$11.8B). The stock then fell ~6% Friday to $123.30 on 2x-average volume and closed today at $122.89, having tagged $121.49 intraday — **below the 52-week low of $121.69**. Management warned rising rates are delaying/repricing deals, capital-markets activity flat through H1 2027, and two facilities-management restructurings will pressure Q4. FY26 core EPS guidance held at $7.80–7.90; Evercore trimmed to $166, Morgan Stanley Buy $180. **The read:** exhaustion at support four sessions after an earnings de-rate, on a dataland/infrastructure growth story (+50% TTM infrastructure revenue). **The risk:** DCR 0.51 is not a passing grade, trend is -5.72%, and the name is explicitly fighting a guidance-tone problem in a rate-sensitive business. A break of $121.49 invalidates it.

- **HIMS** ($27.58) — **Boundary pass — treat as a fail unless you want it.** DCR computes to **exactly 0.500** on the final close (C $27.58, H $27.94, L $27.22) — it clears Bonde's floor by floating-point equality, nothing more. tail:body 4.14 is fine, ADR 6.04% is the best of the three, 20d trend -4.17%. **Catalyst check:** earnings Nov 9, outside the 1–3 day hold window, so no imminent binary — but there is a securities class action with a **Nov 2 lead-plaintiff deadline**, and the reminder/law-firm press is running continuously this week. Fundamentals are mixed: Q2 revenue $753M +38% YoY but EPS -$0.37 vs -$0.05 expected. **Only take this if you want a second, smaller position beside CELH** — the candle itself gives no margin of error.

### Bottom line

**One clean discretionary pick: CELH.** It is the only name that clears Bonde's filters with actual margin — DCR 0.90 against a 0.50 floor, tail:body 4.27, flat 20d trend, and no earnings event inside the hold window.

**CBRE** is the better *story* (earnings-driven de-rate, capitulation wick below the 52-week low) but the weaker *filter* — DCR 0.51 and a -5.72% trend. Take it only with a hard invalidation below $121.49.

**HIMS** passes on DCR = 0.500 exactly. That is a coin flip dressed as a signal. Bonde: *"select 1 to 3 ideas"* — but also *"do not pad with marginal setups."* Two ideas here, and one of them is optional at most.

**Execution:** entry 3:58–4:00 PM ET or MOC (this run is in-window; the 16:00 close has printed). Stop = low of the candle body next morning, sized ≤ 2.5% loss. Note that all three are near-doji bodies, so `body_low_stop` sits essentially at the close — the *effective* stop distance is the full body, not a tight wick, so size down rather than widen the stop.

## Near Misses — 3 stocks failed only F8 (long-term trend)

| # | Symbol | Close | DCR | Body% | Tail:Body | ADR% | 20d Trend |
|---|---|---|---|---|---|---|---|
| 1 | EGO | $31.69 | 0.72 | 0.23 | 3.1 | 3.74 | -19.64% |
| 2 | COIN | $159.60 | 0.60 | 0.01 | 122.6 | 5.43 | -16.78% |
| 3 | IONQ | $30.75 | 0.51 | 0.12 | 4.1 | 6.06 | -31.03% |

**COIN** deserves a specific note: DCR 0.60 and **tail:body 122.6** — a near-perfect doji hammer (body 0.5% of range) that printed a 5-day low at $155.31 and closed at $159.60. It fails F8 only because it is -16.78% from its 20-day-ago close. That is exactly the profile Bonde's common-rejections table calls *do not trade* — a reversal in a name still in free-fall. **EGO** (-19.64%) and **IONQ** (-31.03%) fail the same way. Logging them here because the candles themselves were excellent and someone reviewing by eye would want to know why they were excluded.

## Filter-chain diagnostic (out of 342 in universe)

| Stage | Rejected | Reason |
|---|---|---|
| F1 (5-day low) | 263 | Today low NOT below prior 5-day min low |
| F2 (DCR >= 0.5) | 62 | Closed in lower half of day range |
| F3 (tail:body >= 3) | 3 | Bottom tail too short |
| F4 (small body) | 2 | Body > 40% of day range |
| F5 (2-day decline) | 1 | No prior drop |
| F6 (ADR >= 3%) | 4 | Slow mover |
| F8 (close >= close_20d_ago x 0.92) | 3 | Long-term downtrend |
| F7 (close >= \$15) | 0 | Price floor |
| **PASSED ALL 8** | **3** | |

263 of 342 large-caps did not print a new 5-day low — on an up-tape that is the expected base rate. F1, not DCR, was the binding constraint again.

## Tape context — Monday 2026-10-26

| Index | Close | Chg |
|---|---|---|
| SPY | 765.29 | +0.70% |
| QQQ | 712.20 | +1.11% |
| IWM | 276.97 | +0.44% |
| ^VIX | 18.33 | -5.76% |

**A risk-on tape, and every candidate on this list is a laggard inside it.** That is the right backdrop for a reversal-bullish scan: capital rotated into the index while these three printed 5-day lows and closed off them. VIX at 18.3 and falling says the weakness was idiosyncratic, not systemic.

Deepest decliners in the universe (all idiosyncratic): `XP -47.4% · FICO -13.3% · CRCL -7.2% · CHTR -6.0% · AMKR -5.7% · PINS -5.3% · BMNR -5.3% · FIG -5.2% · TTAN -5.1%`

## Method, sources, and caveats

- **Source path:** shibui-finance / tradingview-advanced / yahoo-finance MCPs are **not registered in this sandbox** (verified via tool_search: 0 hits). Fallback chain used: **TradingView scanner** for the universe (342 rows, HTTP 200) → **Yahoo Finance v8 chart** for 90 days of OHLC (341/341 symbols) → **Finviz** skipped, behind a Cloudflare challenge. Chain stopped there per the zero-fallback policy.
- **Universe proxy:** `market_cap > $5B` stands in for Bonde's "owned by ≥1,000 institutional funds" rule, as the skill prescribes. TV's `market_cap_basic` is the source; shibui's `institutional_holders_count` is not available on this path.
- **Bar integrity:** universe scanned at 15:57 ET, OHLC refreshed at 15:59:54 ET (6 s before the bell), then **fully re-pulled at 16:01–16:02 ET** so every OHLC row is the settled 16:00 ET close. HIMS' DCR moved from 0.54 on the 15:59 print to exactly 0.500 on the official close — that single number is the difference between a pick and a reject, which is why the post-close pull was done.
- **What is *not* verified:** `institutional_holders_count`, and any intraday tape reading (RVOL, premarket gap) — no intraday source was available on this path.

## Recent runs

| Run date | Data date | Picks |
|---|---|---|
| 2026-10-09 | Fri 10-09 | 12 — RVTY, A, RGEN, ILMN, TEM, MAIR, PTCT, SWKS, GH, BMNR, ALGM, HBM |
| 2026-10-12 | Fri 10-09 | 1 — ALAB |
| 2026-10-15 | Wed 10-14 | 21 — broadest this month, semicap/optical heavy |
| 2026-10-16 | Thu 10-15 | 21 — JBL, INGM, VIAV, KLAC, SNPS, AMAT, CEG, LRCX, TER + 13 |
| 2026-10-19 | Fri 10-16 | 0 — setup exhaustion after broad selloff |
| 2026-10-20 | Mon 10-19 | 1 — META |
| 2026-10-21 | Tue 10-20 | 2 — META (Day 3), FRO (Day 1) — degraded universe |
| 2026-10-22 | Thu 10-21 | RUN ABORTED — sandbox egress fully blocked |
| 2026-10-23 | Thu 10-22 | 4 — SNX, CMC, FSLR, TGTX |
| 2026-10-26 | **Mon 10-26 (live)** | **3 — CELH, CBRE, HIMS** |

**Open items carried in:** META (Day 3 on 10-21, 3-day exit deadline passed while the 10-22 run was dark) and FRO (Day 1 on 10-21, went untracked past Day 1). Neither is a red-day setup today, so neither re-appeared. **FORM** (a 10-16 pick at $113.34) is now materially lower — the 10-16 semicap/optical cluster has been hit hard. **FSLR** carried an Oct 29 earnings date inside its hold window and remains a pass.

---

## CORRECTION (added 2026-10-30)

This artifact was written by a **manual** execution of the pre-2026-10-28 cron prompt in a
separate Scout session, not by the scheduled routine. The scan itself was sound — 341
large-caps, all 341 bars on today's session, final 16:00 ET closes — but **two of Bonde's
published rules were implemented as literal SQL floors rather than as the criteria are
published**, and one candidate changes as a result.

### Rule 1 — the tail band (this one changes a name)

The skill's criterion table is titled *"Tail 3-5x body — tail is 3 to 5 times the body"*, but
the SQL form printed beside it encodes only the **lower** bound: `(LEAST(open, close) - low)
>= 3 * ABS(close - open)`. This artifact implemented the SQL form, so it accepted any
tail ≥ 3× with no ceiling.

Bonde's published criterion is a **band**, and the scheduled routine's own 2026-10-29 run
enforced it as one — it rejected JAN at tail:body 7.00× as *"outside the published 3–5× band"*.
Applying the band to this artifact's candidates:

| Symbol | DCR | Tail:Body | Body% | Stop dist | Verdict under the published band |
|---|---|---|---|---|---|
| **CELH** | 0.899 | **4.27** ✓ in band | 0.171 | 0.53% | **QUALIFIED** — unchanged |
| **CBRE** | 0.509 | **13.00** ✗ outside 3–5× | 0.036 | 0.08% | **REJECTED** — tail band |
| **HIMS** | 0.500 (floor-exact) | 4.14 ✓ in band | 0.097 | 0.25% | BOUNDARY PASS — DCR exactly 0.500 |

The near-miss list changes too: **COIN** (tail:body 122.61) and **EGO** (3.15, in band) and
**IONQ** (4.13, in band) — COIN falls outside the band as well, though it was already rejected
on the long-term-trend filter, so the ranking is unchanged.

**Net: CELH is the one clean qualifier from 2026-10-26. CBRE must be struck.**

### Rule 2 — the 2.5% maximum-loss cap

The skill states the stop discipline under output discipline rather than as a numbered filter:
*"Bonde places stop at the low of the candle body next morning, sized so loss ≤ 2.5%."* This
artifact computed `body_low_stop` but never filtered on the resulting risk distance. Re-checked:
CELH 0.53%, CBRE 0.08%, HIMS 0.25% — **all three are inside the cap**, so this rule changes
nothing here. It would have mattered on other dates: the scheduled routine rejected JAN at a
4.07% stop distance on 2026-10-29 even though the setup *worked*.

### Rule 3 — which bar is the signal bar

This artifact scanned **today's live session bar** (Yahoo's in-progress bar at 15:57 ET,
re-pulled post-close at 16:01–16:02 ET for settled closes). The routine's shibui path is
**T+1** — the signal bar is the prior close — and the routine then resolves each setup
against the *next* session's close. The 2026-10-29 run does this explicitly: VLO and VIRT
are reported as `FAILED_STOP` because they broke their body-low stops on the session after the
signal bar, and FDXF and G are reported as held. **This artifact contains no such
next-session resolution check**, so it cannot say whether CELH held its body low after the
signal day.

**Where to look instead:** the scheduled routine's own 2026-10-29 artifact
(`daily-screens/2026-10-29/reversal-bullish-3:55.md`) applies all of the above correctly and is
the authoritative version of the workflow. This document is retained as a record of the
manual scan, with its results corrected as noted.

_Correction appended 2026-10-30 by the Scout session that produced the original scan._
