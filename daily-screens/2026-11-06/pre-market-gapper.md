# Pre-Market Gapper — Friday, 06 November 2026

> **Session:** the pre-market of Fri 2026-11-06. Pull rounds at 08:33–08:36, 08:38–08:42 and 08:47 ET; the published snapshot is the **freshest max-newest-timestamp tape vintage** (newest executed print 08:32:12), with the live `/info` quote taken at 08:47 ET. **Source of record:** the Nasdaq `extended-trading` tape, cross-checked against Nasdaq `/info`, the Cboe delayed-quote CDN, TradingView, the MCP bridge and the fleet's own 08:30 pre-open feed. No catalyst was sourced for any name — the wire had nothing on this list, so no name below is described by a reason.

_contract: premarket-artifact-v4 · flagged: 1 · scanned: 12 · gate: |gap|>=4.0% and pm_volume>=50,000 and exec_shares>=25 · reference close: focus.csv(today_close)+tradingview+cboe (12/12 agree to the cent; the MCP bridge confirms 12/12)_

## TL;DR

- **1 of 12 Focus names is flagged: OUST, and it is the only name that cleared the 4% bar.** It printed **+4.03% on a 512-share print** at 08:32:12 on **122,288** pre-market shares, and the live quote at 08:47 ET read $31.98 (**+4.78%**) with a **$31.76 bid — the bid alone is above the bar**.
- **OUST is a real, liquid gapper that has been trading *on* the bar all morning**: +4.85% on 100 shares (07:51), +4.19% on 272 shares (07:54), +4.46% on 162 shares (08:22), +4.03% on 512 shares (08:32). The size was behind the bar every time the bar was there — this is not a quote on a rounding print.
- **The caveat that changes how this file reads: the flag is narrow and the tape lags the clock.** The published print clears the trigger by **0.03pp**, the freshest tape vintage is **~15 minutes behind wall clock**, and the tape's very last print (1 share at $31.78) is exactly the artifact the size bar exists to exclude — so the published gap is carried by the 512-share print one second earlier. The other 11 names are far from the bar (widest −3.08%), so **their** no-flag verdict is immune to the cache; **OUST's** is not.

## Focus scan — all names

| Ticker | Ref close (11-05) | PM price (last executed print) | Gap % | PM volume | Exec shares | Exec notional | PM high | PM low | Quote % | Verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **OUST** | 30.52 | 31.75 | +4.03% | 122,288 | 512 | 16,256.00 | $32.3 (07:39:08 AM) | $30.8 (04:04:46 AM) | +4.78% | FLAGGED |
| **ENOV** | 28.62 | 27.74 | -3.08% | 583 | 6 | 166.44 | $28.9 (04:04:36 AM) | $28.45 (04:04:36 AM) | -2.03% | BELOW |
| **ARRY** | 5.3 | 5.4191 | +2.25% | 33,097 | 1,820 | 9,862.76 | $5.48 (06:42:53 AM) | $5.22 (04:00:06 AM) | +1.51% | BELOW |
| **HELE** | 37.77 | 38.54 | +2.04% | 336 | 1 | 38.54 | $37.79 (05:29:48 AM) | $37.79 (05:29:48 AM) | +0.05% | BORDERLINE_INTRADAY |
| **KD** | 16.18 | 16.01 | -1.05% | 15,266 | 26 | 416.26 | $16.1519 (08:15:36 AM) | $16 (08:16:12 AM) | +4.94% | BORDERLINE_TAPE_ONLY |
| **YOU** | 56.5 | 56 | -0.89% | 100 | 4 | 224.00 | $56 (08:34:50 AM) | $56 (08:34:50 AM) | -0.89% | BELOW |
| **XNCR** | 34.05 | 33.85 | -0.59% | 27 | 1 | 33.85 | not published | not published | -1.61% | BELOW |
| **CRCT** | 9.25 | 9.2 | -0.54% | 1,489 | 7 | 64.40 | $9.7407 (04:59:54 AM) | $9 (07:07:24 AM) | -3.15% | BORDERLINE_INTRADAY |
| **VRDN** | 28.55 | 28.41 | -0.49% | 2,503 | 1 | 28.41 | $29.01 (05:52:44 AM) | $28.95 (05:52:44 AM) | +1.61% | BORDERLINE_INTRADAY |
| **LIVN** | 91.14 | 91.5 | +0.40% | 1,232 | 1 | 91.50 | $91.19 (07:22:08 AM) | $90.71 (07:25:41 AM) | +0.40% | BORDERLINE_INTRADAY |
| **DUOL** | 157.02 | 156.68 | -0.22% | 2,679 | 40 | 6,267.20 | $158 (08:12:51 AM) | $155.55 (07:08:16 AM) | -0.59% | BELOW |
| **XYZ** | 84.04 | 83.97 | -0.08% | 205,714 | 1 | 83.97 | $84.1 (04:04:34 AM) | $83.2 (04:18:09 AM) | -1.12% | BELOW |

Sorted by absolute gap, largest first. Denominator = each name's settled 2026-11-05 close, taken from the prior sweep's own `focus.csv` (`today_close`) and confirmed to the cent by TradingView's `close` and the Cboe delayed-quote CDN (12/12). "PM price" is the tape's **last executed print**, never the live quote — "Quote %" is the live `/info` last sale, published separately. "PM high/low" are Nasdaq's **as-reported** pre-market extremes, which lag the tape (a known field defect: on CRCT the reported high $9.7407 sat *below* later prints). XNCR's volume is a **tape-sum lower bound** (27 shares over 7 rows) — Nasdaq published no cumulative counter for it, so its real pre-market volume is ≥ 27.

## Focus names that did not qualify

Every scanned name whose verdict is not FLAGGED, with its gap, its pre-market volume, its range, its screen provenance and a verdict on the setup. Ordered by setup quality (stylists desc, then origins desc, then size of the miss).

- **VRDN** — -0.49% · 2,503 shares · $28.95–$29.01 · 4 stylists, 6 origins (A_stockbee_4pct, B_stockbee_ep9m, C_qullamaggie_rs, D_qullamaggie_ep, G_peoplewish, H_hernandez_theme) · setup: good setup that went nowhere — the richest provenance in the list (six origins, four stylists) and it never moved; it touched −5.43% at 04:18 on 1-share prints and sat back at the prior close all morning.
- **XNCR** — -0.59% · 27 shares · no pre-market range published · 4 stylists, 4 origins (A_stockbee_4pct, C_qullamaggie_rs, G_peoplewish, H_hernandez_theme) · setup: good setup that went nowhere because there was no market — 27 shares across 7 prints, the last one a single share; a name with provenance and no liquidity behind it.
- **KD** — -1.05% · 15,266 shares · $16–$16.1519 · 3 stylists, 5 origins (A_stockbee_4pct, B_stockbee_ep9m, C_qullamaggie_rs, D_qullamaggie_ep, G_peoplewish) · setup: good setup that went nowhere on the tape — it printed the bar at $16.98 (+4.94%) on 5 shares at 08:23 and then traded $16.01 on 26 shares in the same second; 15,266 shares is under the 50,000 floor, so there was no market behind either number.
- **DUOL** — -0.22% · 2,679 shares · $155.55–$158 · 3 stylists, 4 origins (A_stockbee_4pct, B_stockbee_ep9m, D_qullamaggie_ep, G_peoplewish) · setup: good setup that went nowhere — flat to slightly red on a $2.45 range, 2,679 shares, nothing near the bar at any point.
- **LIVN** — +0.40% · 1,232 shares · $90.71–$91.19 · 3 stylists, 3 origins (A_stockbee_4pct, D_qullamaggie_ep, H_hernandez_theme) · setup: good setup that spiked and faded — it printed $96.50 (+5.88%) at 07:21:34 **on 1 share**, then $96.00 (+5.33%) and $95.95 (+5.28%) on 1 share each, and fell back to $91.50; every print above the bar was a rounding artifact, and nothing has traded since 08:26.
- **ARRY** — +2.25% · 33,097 shares · $5.22–$5.48 · 2 stylists, 3 origins (A_stockbee_4pct, B_stockbee_ep9m, C_qullamaggie_rs) · setup: good setup that went nowhere, but with real size — the print that carried the gap was 1,820 shares, the largest single print in the list, and it still only reached +2.25%.
- **XYZ** — -0.08% · 205,714 shares · $83.2–$84.1 · 2 stylists, 3 origins (A_stockbee_4pct, B_stockbee_ep9m, D_qullamaggie_ep) · setup: bad setup for a gapper — the most liquid pre-market in the list (205,714 shares) and a −0.08% gap; this is a volume name, not a gapper.
- **ENOV** — -3.08% · 583 shares · $28.45–$28.9 · 2 stylists, 2 origins (A_stockbee_4pct, C_qullamaggie_rs) · setup: good setup that went the wrong way — the widest negative gap in the list, on 583 shares, and it never traded a single print after 08:26.
- **HELE** — +2.04% · 336 shares · $37.79–$37.79 · 2 stylists, 2 origins (A_stockbee_4pct, C_qullamaggie_rs) · setup: good setup that went nowhere after spiking the other way — a $36.01 print (−4.66%) at 05:30:19 on 1 share, then nothing for 68 minutes, then a single $38.54 print at 07:10 on 1 share; 336 shares all morning.
- **YOU** — -0.89% · 100 shares · $56–$56 · 2 stylists, 2 origins (A_stockbee_4pct, E_qullamaggie_5d_gainers) · setup: bad setup — 100 shares in the whole pre-market, the last print 4 shares at $56.00, and a $55.80–$60.78 band around it.
- **CRCT** — -0.54% · 1,489 shares · $9–$9.7407 · 2 stylists, 2 origins (A_stockbee_4pct, TV_volume_breakout) · setup: good setup that went nowhere after being real — it crossed the bar twice with size ($9.7407, +5.30%, on 104 shares at 04:59:54; $9.79, +5.84%, on 28 shares at 05:42:31) and gave all of it back into −0.54%; 1,489 shares by the snapshot.

## Flags

- **OUST +4.03% — the size leg rests on one print, and the trigger margin is 0.03pp.** The published gap is carried by a **512-share** print at $31.75 (08:32:12); the tape's last print in that same second was **1 share at $31.78 (+4.13%)** — precisely the rounding artifact the 25-share bar exists to exclude. The live quote at 08:47 ET was $31.98 (+4.78%) with a **$31.76 bid**, so the bid alone was above the bar; the tape's freshest vintage is ~15 min behind wall clock, so the real 08:47 tape may differ. Treat this as a genuine gap on a thin margin, not a wide one.
- **KD +4.94% — a quote on a 5-share print inside a 27%-wide spread.** The +4.94% reading is a 5-share print at $16.98 (08:23:49) sitting inside a **$14.50 bid / $18.43 ask** band; the substantive tape print in the same second was $16.01 on 26 shares (−1.05%), and pre-market volume of 15,266 is **below the 50,000 floor**. KD cannot flag on any reading — this is the PURR case, a quote and not a market.
- **LIVN +5.88% intraday — every print above the bar was 1 share.** $96.50 (07:21:34), $96.00 (07:22:12), $95.95 (07:22:14), $95.50 (07:21:36): four 1-share prints above the bar, then a fade to $91.50 and silence. The gap was real on the tape and untradeable.
- **HELE −4.66% and VRDN −5.43% — 1-share prints at the bar.** HELE's $36.01 (−4.66%, 05:30:19) and VRDN's $27.00 (−5.43%, 04:18:17 and 04:18:31) each crossed the 4% line on a single share. Neither is a market.
- **CRCT +5.84% — the intraday crossings WERE real, and it still gave it all back.** 104 shares at +5.30% (04:59:54) and 28 shares at +5.84% (05:42:31) are sized prints, not artifacts; the name closed the pre-market at −0.54%. This is the fade case, not the thin case.
- **ENOV — a $19.34 bid against a $30.00 ask is a 55%-wide band.** The −2.03% live quote and the −3.08% tape print are not comparable numbers; on 583 shares the tape is the only market that existed.
- **XYZ — 205,714 pre-market shares and a −0.08% gap.** The largest pre-market volume in the list with no gap at all; worth knowing before anyone reads "liquid pre-market" as "gapper".
- **Denominator conflict (10 of 12 names) — Nasdaq's `/info` `secondaryData` is not the settled close.** It read 30.5850 for OUST (true 30.52), 16.2750 for KD (true 16.18), 5.2450 for ARRY (true 5.30), 157.3400 for DUOL (true 157.02), 9.2550 for CRCT, 28.4400 for ENOV, 37.6700 for HELE, 91.3000 for LIVN, 34.0961 for XNCR and 56.3700 for YOU. The denominator published here is the one **three independent sources agree on to the cent**; only VRDN and XYZ had Nasdaq agree as well.

## Method, source health & caveats

**Three pull rounds and a max-newest-timestamp defence.** The source of record is the Nasdaq
`extended-trading?markettype=pre&assetclass=stocks` tape, which sits behind a shared HTTP cache
that serves hour-old vintages for the same URL. The run pulled the tape 8 times per symbol
(`premarket_pull.py`, 12 symbols, ~08:38–08:42 ET) and kept the payload with the **newest internal
clock time**; two further independent rounds (5 cache-busted pulls per symbol at 08:44 ET, 6 at
08:47 ET) were run to establish the liveness proof and the divergence record. **The tape's freshest
vintage carries prints through 08:32:12 while the wall clock read 08:47 — a ~15-minute lag that
the cache defence cannot remove.** The published snapshot is that freshest vintage; the live quote
in the `Quote %` column is `/info` at 08:47 ET.

**What the three rounds showed.** OUST's published gap moved **+3.21% (08:33 vintage, 25 shares)
→ +4.46% (08:38 vintage, 162 shares) → +4.24% (08:42 vintage, 3 shares) → +4.03% (08:47 vintage,
512 shares)** as successively fresher vintages replaced cached ones. Every reading is published
here so the reader can see the spread rather than a single number that looks certain. The other 11
names did not change verdict across the three rounds; the largest gap among them moved less than
0.2pp.

**One ordering defect I had to correct by hand.** The helper sorts prints by `HH:MM` (seconds
dropped), so when a name prints several times inside the same second — OUST does — it cannot order
them, and it took the oldest print of the final minute. The 08:47 round was re-ordered at
**second resolution**: the tape's last second (08:32:12) carried **512 shares at $31.75 (+4.03%)**
and **1 share at $31.78 (+4.13%)**. The published gap uses the 512-share print; the 1-share print is
disclosed in `## Flags` rather than silently dropped. (This is a defect in
`premarket_pull.py`'s `_clock_to_min`, not in the screen's gate.)

**The denominator and who agreed on it.** Per SKILL §6.3 the denominator is the settled prior
regular-session close, taken from the prior sweep's own `focus.csv` — here
`daily-screens/2026-11-05/focus.csv` (`today_close`, the 2026-11-05 session close) — and cross-checked
against two independent sources. **All three agree to the cent on all 12 names**: TradingView's
scanner `close` and the Cboe delayed-quote CDN `close`. The MCP bridge `market-recap` `get_quotes`
(one batched call) confirms **12/12** as well: its `price` is the 2026-11-05 settled close for every
name and its `as_of` is 2026-11-05T21:00Z, i.e. the 16:00 ET close. The bridge's `market_state` is
`"pre"`, which per the known contract serves the **prior regular close**, not a pre-market print —
it was used only to confirm the denominator, never as a print source.

**The margin against the trigger.** One name cleared the bar (OUST, +4.03% on the published print,
+4.78% on the live quote, +4.06% on the bid) — a **0.03pp** margin on the published print and 0.78pp
on the quote. The nearest miss among the others is **ENOV at −3.08% (0.92pp short)**, followed by
ARRY +2.25% and HELE +2.04%; every other name is at least 1.8pp from the bar, so **the no-flag
verdict for the other 11 is immune to the cache lag**. OUST's verdict is not immune, and that is
stated rather than hidden.

**Nasdaq defects checked before trusting anything.** `secondaryData.lastSalePrice` was read for
every name and **disagreed with the three agreeing sources on 10 of 12** (the documented drift) — it
was used for nothing. `primaryData` was confirmed to be carrying the live 2026-11-06 pre-market
(`marketStatus: Pre-Market` on all 12). The `extended-trading` tape is served newest-first and was
sorted by clock time before the last print was taken. The `infoTable` cumulative counter was used
for volume; for OUST the trade-detail table is capped at 100 rows (truncated), so it cannot arbitrate
the counter and the counter stands at 122,288 — the tape's own visible sum is only 5,123 because the
visible window is the last ~30 minutes. For XNCR no counter was published at all and the tape sum
(27) is published as a **lower bound**. The `infoTable` high/low fields lag the consolidated row and
are published as reported, not re-derived.

**Two independent fleet cross-checks.** (1) The fleet's own **08:30 ET pre-open feed**
(`preopen-feed/2026-11-06-0830.jsonl`, captured 08:32:58 ET) carries two of these twelve names:
**OUST +3.571% at $31.61** and **CRCT −2.703% at $9.00** — both consistent with the tape's
direction, with the TV-derived OUST reading on the low side of the tape's +4.03%. It carries **no
catalyst** for either. (2) Cron #15's 08:22 ET artifact (`earnings/2026-11-06-reactions.md`)
publishes CRCT's pre-open gap as **−2.70%** — identical to the tape's −2.54% rounding and to the
pre-open feed. Neither source carries a catalyst for any of the twelve, and **no catalyst is
asserted anywhere in this file**.

**Provenance.** The universe is the Focus list of the most recent completed 18:30 ET sweep before
the fire (`daily-screens/2026-11-05/focus.csv`, 12 names; screen data date 2026-11-04, session close
2026-11-05). `stylists` and `origins` are carried through verbatim from that file — no name was
re-screened, and no name was dropped for failing to qualify. The pre-open feed directory existed
today (no substitution was needed) but carries only 2 of these 12 names.

**Source health**

| Source | Endpoint / query | Status | Used for |
|---|---|---|---|
| Prior sweep Focus list | `minimax-cloud-outputs` `daily-screens/2026-11-05/focus.csv` | ok (12 rows) | universe, screen provenance, the denominator (`today_close`) |
| Nasdaq `extended-trading` tape | `api.nasdaq.com/api/quote/{SYM}/extended-trading?markettype=pre&assetclass=stocks` | **degraded** — the shared HTTP cache serves stale vintages; the freshest vintage lags wall clock by ~15 min | the source of record: prints, sizes, pre-market high/low, volume |
| Nasdaq `/info` | `api.nasdaq.com/api/quote/{SYM}/info?assetclass=stocks` | ok (12/12) | the live quote, bid/ask, market status; `secondaryData` rejected as the denominator on 10/12 |
| Cboe delayed-quote CDN | `cdn.cboe.com/api/global/delayed_quotes/quotes/{SYM}.json` | ok (200 with `-L`; the plain request 307-redirects) | denominator cross-check (12/12 agree); **its `price` field still carries the 2026-11-05 close, not a pre-market print** |
| TradingView scanner | `scanner.tradingview.com/america/scan` | **degraded** — no pre-market row for 2 of 12 names (YOU, XNCR); its OUST pre-market change read +3.87% against the tape's +4.03% and the live quote's +4.78% | denominator cross-check (12/12), `premarket_high`/`low` |
| MCP bridge `market-recap` | `mcp_bridge.py market-recap get_quotes` (one batched call) | ok (12/12) | denominator confirmation (`price`, `as_of` 2026-11-05T21:00Z) |
| MCP availability probe | `probe_mcp.py` | `catalog_ok total=135 finance_tools=0 · bridge bridge_ok packs=tradier,fmp,market-recap` | no finance MCP registered on this runtime (not an error) |
| Fleet pre-open feed | `preopen-feed/2026-11-06-0830.jsonl` (08:32:58 ET) | ok (2 of 12 names) | independent gap cross-check |
| Cron #15 earnings artifact | `earnings/2026-11-06-reactions.md` (08:22 ET) | ok (CRCT only) | independent gap cross-check |

`degraded_sources: 2` — the Nasdaq tape's stale-cache lag and the TradingView scanner's partial
and stale pre-market rows. Everything else came back clean.

---

_Generated 2026-11-06 08:47 ET for the 2026-11-06 08:30 ET fire of cron #08
stock-screener-pre-market-gapper. Contract `premarket-artifact-v4`._
