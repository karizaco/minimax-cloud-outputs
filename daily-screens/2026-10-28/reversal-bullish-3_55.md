# Reversal Bullish — 3:55 PM ET (Bonde / Stockbee)

- **Cron:** #4 `reversal-bullish-3:55` — fired 2026-10-28 15:55 ET, weekday, in-window
- **Signal candle:** 2026-10-27 (the screen's data source is T+1 — see Method)
- **Status as of:** 2026-10-28 16:02 ET — **after the close**, so every "live" number below is the official 2026-10-28 close
- **Universe:** NYSE / NASDAQ / AMEX, market cap > $5B (institutional-ownership proxy)
- **Result:** 5 names passed all 8 Bonde criteria on the 10-27 candle. After scoring Day 1 (10-28) against each setup, **none is a clean long entry**: 1 worked and should be trailed, 2 are rejected on live follow-through, 2 are watch-only.

## Headline

Five names cleared every one of Pradeep Bonde's published reversal-bullish criteria on the 2026-10-27 candle.
Because the scan's data source runs a day behind, that candle is one session old — and this run finished *after*
the 16:00 ET bell, which means Day 1 of each setup (2026-10-28) has already closed and can be scored rather
than guessed at. The scoring is what matters: of the five, **ELF** worked and closed 2.26% above its
body-low stop, **CELH** slipped 0.25% under its stop and failed to hold, **FLUT** ran to 80.10 and closed back
at its stop line after a bull trap, **PPC** broke 2.44% below its stop on a new 5-day low, and **GEN** is the
only name still above its stop — but it did so by printing a *new* 5-day low and reversing, and its tail
finished at 1.83× body, short of the 3× test. **No name qualified as a clean actionable long at the bell.**
GEN and CELH go on the watchlist with explicit re-entry conditions; ELF is a trail, not a chase; and GEN
carries a fiscal-earnings print landing in roughly 90 minutes.

## Watchlist

### 1. GEN — Gen Digital · signal close 24.25 · 10-28 close 24.22

The cleanest fit for Bonde's *stated* criteria in the whole set: tail at **3.83× the body**, the only
candidate inside Bonde's published 3–5× band, and the largest company here at **$14.6B** with 5.38M shares
traded. It satisfies every other test — DCR 0.580, body ratio 0.120, a fresh 5-day low at 23.96, a two-day
decline into that low, ADR 3.24%, and the 20-day trend filter passing comfortably (24.25 against a
close_20d_ago of 20.85).

Today it did something more interesting: GEN printed a **new 5-day low at 23.88** and reversed to close
**76% of the day's range** on a small body (0.247), so a second, fresher hammer is forming on top of the
10-27 one. But it does not complete — the tail finished at **1.83× body, short of the 3× test**, and the close
of 24.22 sits just **+0.124% above the 24.19 invalidation level**. There is effectively no cushion, and the
shape is a near-miss rather than a pass.

**The disqualifier is not technical.** Gen Digital reports fiscal Q2 2027 **after the close tonight**
(announced 10/09; consensus ~$0.72 EPS on $1.33–1.34B revenue). A binary print on a setup whose invalidation
level is 12 basis points away is not a risk Bonde's framework was designed for. The CEO's 10/26 LinkedIn post
saying results track to the higher end of guidance is mildly supportive — the stock was +0.76% after hours on
that news — but consensus is still Hold with RBC at $24 and Jefferies cut to $27.

**Action:** do not treat this as a 10-29 open entry. Let the earnings print resolve first. A post-earnings
bar that holds above 24.19 and re-forms a ≥3× tail is the setup; anything that gaps through 24.19 is invalid.

### 2. CELH — Celsius Holdings · signal close 28.00 · 10-28 close 27.88

The best *candle* of the group and the best structure on 10-27: it closed **92.8% of the day's range**
(DCR 0.928) with a body of $0.05 inside a $0.97 range, made a fresh 5-day low at **27.10** after a two-day
decline, and carried an ADR of 3.81% with 4.71M shares traded on a $7.16B cap. Q3 earnings are not until
Nov 5–9, so **there is no binary event in the window**.

Two honest caveats about the signal itself. The body is so small that tail/body comes to **17×** — a doji
rather than the 3–5× hammer Bonde describes (the published SQL only requires ≥3×, so it passes as written,
but a trader applying the verbal rule would rank it lower). And the reversal formed on **light volume
(0.86× the prior-10-session average)**, with the Alani Nu securities-class-action notices (lead-plaintiff
deadline Nov 3) and a Texas AG probe still live.

**It failed on Day 1.** CELH closed at 27.88, **0.25% below the 27.95 body-low stop**, and today's bar carries
no lower tail at all (0.38× body) — so it is not a replacement hammer, just a quiet drift down that has not
yet broken the 27.10 low. The 10-27 reversal did not hold.

**Action:** not an entry. Watch 27.10 — a fresh 5-day low *with* a ≥3× tail that closes back above it restores
the setup for 10-29. Until then the 10-27 signal is dead.

### 3. ELF — e.l.f. Beauty · signal close 113.17 · 10-28 close 115.50

ELF was the best-behaved setup of the five and **it worked**: closed +2.06% at 115.50, broke the signal
candle's high of 114.29 on the way to 117.77, and sits **+2.26% above** its 112.95 body-low stop. Today's bar
was a green momentum candle (body ratio 0.496), not a hammer — so there is no fresh reversal to buy, only a
winner to manage. Earnings are Nov 4, so no overnight event risk here.

**Action:** trail it. The 10-27 body low at 112.95 is the disciplined stop; the 10-28 body low at 112.65 is the
tighter alternative. Do not chase a +2% extension.

## Full screen — all 5 passers

Signal candle 2026-10-27. `body_low_stop` is the body low of the signal candle, which is where Bonde places
the stop (targeted at ≤2% loss). `rel_volume` is signal-day volume against the prior 10 sessions.

| Symbol | Close | Body-low stop | Stop % | DCR | Tail/body | ADR20 | Rel vol | Cap |
|---|---|---|---|---|---|---|---|---|
| CELH | 28.00 | 27.95 | -0.18% | 0.928 | 17.00× | 3.81% | 0.86× | $7.2B |
| ELF | 113.17 | 112.95 | -0.19% | 0.757 | 14.86× | 3.32% | 1.06× | $6.7B |
| GEN | 24.25 | 24.19 | -0.25% | 0.580 | 3.83× | 3.24% | 0.84× | $14.6B |
| FLUT | 78.26 | 78.26 | 0.00% | 0.536 | 3.51× | 4.44% | 1.17× | $13.6B |
| PPC | 27.09 | 27.03 | -0.22% | 0.576 | 3.08× | 3.43% | 0.87× | $6.4B |

The screen is tight and the funnel shows where the attrition happens. DCR and the tail/body test are the brutal
gates: of 1,344 names over $5B, 242 made a 5-day low, 94 closed in the top half of the range, and only **26**
produced a tail at least 3× the body. The 20-day ADR filter then cut 21 down to 7, the $15 price floor took it
to 6, and the long-term-trend filter left **5**.

| Criterion (cumulative) | Names passing |
|---|---|
| Symbols with ≥21 sessions in window | 5,440 |
| + market cap > $5B | 1,344 |
| + 5-day low (criterion 1) | 242 |
| + DCR ≥ 0.5 (criterion 2) | 94 |
| + tail ≥ 3× body (criterion 3) | 26 |
| + body ≤ 0.4 of range (criterion 4) | 26 |
| + 2-day decline (criterion 5) | 21 |
| + ADR20 ≥ 3% (criterion 6) | 7 |
| + close ≥ $15 (criterion 7) | 6 |
| + close ≥ 0.92 × close_20d_ago (criterion 8) | **5** |

## Day 1 scorecard — 2026-10-28 close

`vs stop` is the close against the signal candle's body-low stop. A negative number means the reversal already
failed its own invalidation level. The last column asks the harder question: does today's bar itself form a
*new* Bonde hammer (5-day low, DCR ≥ 0.5, tail ≥ 3× body, body ≤ 0.4)?

| Symbol | Close | Chg | vs stop | New 5d low? | DCR | Tail/body | New hammer? |
|---|---|---|---|---|---|---|---|
| GEN | 24.220 | -0.12% | +0.124% | **yes** | 0.764 | 1.83× | no |
| CELH | 27.880 | -0.43% | -0.250% | no | 0.503 | 0.38× | no |
| ELF | 115.500 | +2.06% | +2.258% | no | 0.589 | 0.14× | no |
| FLUT | 78.240 | -0.03% | -0.026% | no | 0.317 | 3.30× | no |
| PPC | 26.370 | -2.66% | -2.442% | **yes** | 0.481 | 8.67× | no |

Four readings matter. **PPC is dead** — 2.44% under its stop, -2.66% on the day, on a new 5-day low at 25.85.
**FLUT is a bull trap** — it ran to 80.095 intraday, above the signal candle's high, then faded to close
78.24, right back at its 78.26 stop, in the bottom third of the range. **CELH failed** and never put a tail
under the 10-27 candle. **GEN is the only name still above its stop**, and it got there by making a *lower*
low and reversing — but with a 1.83× tail it is a near-miss, not a pass. **ELF worked** and needs trailing, not
buying.

## Rejected — universe gate (2 names)

Two other names passed the *shape* test but fail Bonde's institutional-ownership proxy, so they are out of
scope regardless of how the candle looks.

| Symbol | Company | Mkt cap (shibui) | Mkt cap (TradingView) | 10-28 close |
|---|---|---|---|---|
| LIF | Life360, Inc. | $3.50B | $3.58B | 43.96 (+1.81%) |
| TREE | LendingTree, Inc. | $0.37B | $0.37B | 26.62 (+1.56%) |

This exclusion came out of a data-integrity issue worth recording. `shibui.valuation` retains **older rows**
per symbol, and filtering `market_cap > 5B` *before* selecting the latest row per symbol picks up those stale
rows — on the first pass it admitted LIF on a $5.24B row and TREE on a $5.02B row, even though their current
caps are $3.50B and $0.37B. Re-running the gate *after* the latest-row selection drops both, and the retained
current rows agree with TradingView to within 3% (LIF $3.50B vs $3.58B, TREE $0.366B vs $0.374B). Had that
ordering bug gone unnoticed, the scan would have shipped two names that do not belong in a $5B-plus universe.

## Market context

SPY closed 771.38 (+0.22%) and QQQ 724.20 (+0.41%) on
2026-10-28. A mildly green tape, so there is no index-level reason to pass on an individual reversal setup —
the rejections above are name-specific.

## Method

The screen is Bonde's published criteria applied literally, run as a single DuckDB query against
`shibui.stock_quotes` / `shibui.valuation`:

| # | Criterion | SQL |
|---|---|---|
| 1 | 5-day low | `low <= MIN(low, last 5 sessions)` |
| 2 | Close in top half of day range | `(close - low) / (high - low) >= 0.5` |
| 3 | Tail 3–5× body | `(LEAST(open,close) - low) >= 3 * ABS(close - open)` |
| 4 | Small body | `ABS(close - open) / (high - low) <= 0.4` |
| 5 | Prior decline 2–3 days | `close < close_2d_ago` |
| 6 | ADR ≥ 3% | `AVG((high-low)/close, 20 sessions) >= 0.03` |
| 7 | Close ≥ $15 | `close >= 15.0` |
| 8 | Long-term trend | `close >= close_20d_ago * 0.92` |
| U | Universe | exchange IN (NYSE, NASDAQ, AMEX) AND market_cap > $5,000,000,000 |

The default `emit_reversal_bullish_sql()` from the skill was **not** used — it carries three documented bugs
(date hard-coded instead of resolved to latest, the LAG window collapsed to one row by the CTE filter, and no
Bonde-quality filters at all). The T+1-safe form was used instead: the inner CTE is windowed over
`2026-08-14 … 2026-10-27` with `ROW_NUMBER() OVER (PARTITION BY symbol ORDER BY date DESC)`, the latest row per
symbol is taken as `rn = 1`, the market-cap gate is applied **after** the latest-row selection, and all eight
filters run in the outer WHERE.

**T+1 caveat.** shibui's latest available date is 2026-10-27, one session behind the cron date, so the signal
candle is 10-27 and the entry window Bonde describes (3:58–4:00 PM or MOC) belonged to 10-28. That window
closed while this report was being written, so **the setups below are actionable for the 10-29 open, not for a
market-on-close order today.** Every candidate was re-checked against the live 10-28 bar before being named.

**Independence check.** TradingView's change percentages reconcile exactly with shibui's 2026-10-27 closes for
all seven symbols — GEN's 10-28 close of 24.22 against a 24.25 prior close is -0.12%, which is what TradingView
reports. That is a stronger confirmation than a press quote, because it proves shibui's close is the real prior
close and the live tape is the real current one. Press pages independently confirmed the signal closes for
CELH ($28.00), ELF ($113.17) and GEN ($24.25).

## Source health

| Source | Endpoint / query | Status | Notes |
|---|---|---|---|
| shibui-finance (MCP over HTTPS bridge) | `stock_data_query` — Bonde-strict scan | **ok** (HTTP 200, valid JSON) | 5 passers of 5,440; 200-row server limit not hit |
| shibui-finance | `stock_data_query` — 12-session detail + valuation rows | **ok** | 84 rows; implied share counts cross-checked against TradingView |
| TradingView public screener | `POST https://scanner.tradingview.com/america/scan` | **ok** | 7/7 symbols + SPY/QQQ; 10-28 closing bars and current market caps |
| web_search | GEN / CELH / ELF earnings dates, consensus, closes | **ok** | earnings dates and the three signal closes confirmed |
| Yahoo JSON (spark / chart / screener) | — | **not used** | known 429 from this egress per the runtime contract; the bridge + TradingView path covered everything |
| Finviz fallback | — | **not used** | the primary path succeeded, so no fallback tier was entered |

**errors: 0** — no MCP call failed and no fallback tier was triggered.

## Caveats

- **The 10-28 MOC entry window has closed.** This report was finalised at 16:02 ET. Anything here is a 10-29
  decision, and the two watchlist levels (GEN 24.19, CELH 27.95 / 27.10) have to be re-checked against the
  10-29 open before acting.
- **GEN's earnings print is tonight, after the close.** The single largest risk in this artifact, and invisible
  to every price-based filter.
- **Institutional ownership is a proxy.** shibui does not expose `institutional_holders_count`, and TradingView
  returned `null` for that field on all seven symbols, so the ≥1,000-funds universe test is approximated by
  market cap alone. CELH at $7.16B is the marginal name under that proxy.
- **Tail/body has no upper bound in the canonical SQL.** CELH (17×) and ELF (14.9×) pass a filter that only
  requires ≥3×; if Bonde's verbal 3–5× band is treated as a hard rule, both fall out and only GEN, FLUT and
  PPC remain — of which FLUT and PPC are already rejected on Day 1, which leaves GEN alone.
- **No earnings-date filter was applied** beyond checking the three names discussed here by hand; FLUT and PPC
  were not screened for near-term reports.
- **Day-1 scoring uses the official close**, but the closing-auction print can still be revised in the official
  tape of 10-29.

## Files

- `daily-screens/2026-10-28/reversal-bullish-3:55.md` — this report
- `daily-screens/2026-10-28/reversal-bullish-3:55.csv` — one row per passer with all filter metrics, 10-28
  close-bar metrics, and the decision notes
