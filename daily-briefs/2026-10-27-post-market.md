# Post-Market Brief — Tuesday, October 27, 2026

**Session:** US cash close 2026-10-27 (Tue) · **Brief generated** 2026-10-27 22:32–22:52 ET
**Cron:** #23 `agentic-post-market-brief` · **Intended slot** 16:30 ET weekdays (skill spec: 16:13 ET) · **Actual fire** 22:32 ET
**Sources of record:** Yahoo Finance v7/v8 · TradingView public screener · CNBC quote API · Nasdaq API · Cboe daily stats · web_search
**All HTTP pulls completed 22:32–22:52 ET.** Every figure below carries a source and a freshness stamp; per-region tables, QC and caveats live in this file.

---

## Read this first — deviations and data-path notes

1. **No watchlist exists in this sandbox.** `research/watchlist.yaml` (skill Step 1/Step 4) is absent — same condition as the sibling pre-market cron. The skill's *Watchlist EOD review* section is therefore **omitted rather than fabricated**; no default watchlist was created. This is a missing-input condition, not a data failure.
2. **The MCP finance tier does not exist in this Cloud session.** The catalog holds 15 tools across two providers (`matrix`, `email_workbench_credentials`), `partial=false`, no provider failures, and a keyword search for yahoo/tradingview/stock/screener returned **0 hits**. No MCP finance call was ever attempted, so there are **zero MCP call failures**; the run executed on the public-HTTP stack (one fallback, terminated there).
3. **Fire time is ~6 hours late relative to the intended slot.** The upside: the after-hours session (ends 20:00 ET) is complete, so every after-hours print below is a *final* 20:00 ET mark, not a snapshot. The downside: this brief is published long after the tape it describes.
4. **TradingView's `change` column carried a stale reference on 1 of 44 cross-checked names** (MSGK, apparent +40.18% vs Yahoo +5.54%). All published percentage changes use Yahoo's `regularMarketChangePercent`; TV supplied the universe, the closes and the after-hours prints.
5. **CNBC's `last` is the last *trade*, not the official close** (MSGK: CNBC $289.39 "UNCH" vs official close $305.42). Official closes are taken from Yahoo; CNBC is used for identity, market cap, relative volume and the timestamped after-hours print.
6. **Cboe's put/call markup carries no date stamp.** The page was fetched at 22:45 ET, so the session is *inferred* as 2026-10-27 (Cboe publishes at 20:00 ET). Treat the ratio as a same-session figure with an inferred date, not a stamped one.
7. **One apparent cross-source conflict was left standing rather than smoothed:** the Nikkei. Reuters' Oct 27 Tokyo close was **+1.7%**; Yahoo's `^N225` at 22:19 ET reads **+1.07%** — but that is the *live Oct 28 Tokyo session*, a different session, not a disagreement about the same close. Both are labelled where used.
8. **A multi-hour "second read" was not possible on the after-hours tape** (the session is closed), so the AH spread is evidenced by an independent third source instead (see §6).

---

## TL;DR

A **narrow, AI-led risk-on day with a violent single-name tail**. The Nasdaq Composite gained **+1.18%** to 26,477.81 — its best session in nearly a month — while the **Dow was flat at +0.03%**, and the S&P 500 added **+0.60%** to 7,722.60. Breadth was genuinely broad (**58.4%** of 5,716 US listings advanced, median **+0.32%**), and the move was **one-sided at the tails**: 717 names rose ≥5% versus 216 that fell ≥5%, and in large caps the skew was **225 up vs 41 down**. The engine was semiconductors (SOX **+3.6%**), the continuation of the AI-optimism trade after Anthropic's Nasdaq IPO filing, Nvidia's commitment to invest in Meta's equity offering, and CLS's EMS commentary; small caps did not lag (Russell 2000 **+1.16%**). Volatility collapsed — **VIX −4.73% to 17.52**, VXN −5.64% — and Cboe equity put/call printed **0.59**.

Two things broke the surface. **Boeing fell 10.69% to $168.18** on a Q3 miss *and* a production slippage confession, which is most of the reason the Dow went nowhere. And the **refining complex was gutted** (VLO −9.24%, MPC −7.36%, PSX −7.03%, DK −10.41%, PARR −10.39%, PBF −8.59%, DINO −8.81%, CVI −7.40%) — the worst refining session since April 2025 — on a **crack-spread repricing, not an oil story**: WTI settled only −1.83% to $99.90 while refiners fell three to five times harder than the products they sell, as Iran de-escalation talk and a Russian-diesel waiver compressed the distillate-risk premium.

After the bell, the tape split hard: **Manhattan Associates +10.27%**, **ICON +9.85%**, **Ultra Clean +9.75%** and **DMC Global +16.45%** against **Rapport Therapeutics −20.04%**, **Intapp −16.67%**, **Enphase −15.49%**, **Beta Bionics −10.38%**, **CoStar −8.15%**, **Robinhood −7.63%**, **NXP −7.31%** and **Seagate −5.52%** — the last two despite beating and raising. **Tomorrow is the FOMC decision (2:00 PM ET, Chair Warsh at 2:30 PM ET) with Microsoft and Alphabet reporting after the close.**

---

## 1. Day's tape

**US indices and ETF proxies** — Yahoo official close (`regularMarketPrice`), stamped at the 16:00 ET close; index quote stamps range 16:00–17:16 ET as the vendors refresh.

| Asset | Close | Chg | Prior close | Volume | Read |
|---|---:|---:|---:|---:|---|
| S&P 500 | 7,722.60 | **+0.60%** | 7,676.77 | 2.81bn sh | 16:48 ET |
| Nasdaq Composite | 26,477.81 | **+1.18%** | 26,169.38 | 7.12bn sh | 17:16 ET |
| Dow Jones | 52,377.57 | **+0.03%** | 52,361.58 | 401mn sh | 16:48 ET |
| Russell 2000 | 2,818.87 | **+1.16%** | 2,786.42 | — | 16:30 ET |
| VIX | 17.52 | **−4.73%** | 18.39 | — | 16:15 ET |
| VXN | 24.91 | **−5.64%** | 26.40 | — | 16:15 ET |
| SPY | 769.66 | +0.56% | 765.37 | 28.07mn | 16:00 ET |
| QQQ | 721.25 | +1.27% | 712.20 | 30.10mn | 16:00 ET |
| IWM | 280.18 | +1.15% | 276.99 | 18.76mn | 16:00 ET |
| DIA | 523.28 | +0.06% | 522.97 | 2.60mn | 16:00 ET |
| GLD | 372.28 | +1.21% | 367.82 | 5.15mn | 16:00 ET |
| TLT | 81.63 | −0.06% | 81.68 | 19.53mn | 16:00 ET |

All five index levels were **independently confirmed by CNBC to 0.0000%** (`.SPX`/`.DJI`/`.IXIC`/`.RUT`/`.VIX`). The cross-check is a genuine one: CNBC's `last` and Yahoo's `regularMarketPrice` are different fields from different vendors and agree to the cent.

**The shape of the day.** The Dow's flatness was not a flat tape — it was one $133bn company (Boeing, −10.69%) offsetting a strong Nasdaq, plus a −2.05% energy sector. Six of eleven GICS sectors rose and five fell (Reuters). The **10-year Treasury yield closed at 4.993%** (+0.7bp, 14:59 ET) and TLT was flat, so rates did not drive anything: this was an equity-flow event, not a macro-rate event. The **Conference Board consumer confidence** print for October came in at its **highest since June** and beat expectations. The **FOMC's two-day meeting opened on Oct 27** and concludes tomorrow.

**Global round-up** (Reuters, Oct 27 closes): South Korea **+3%**, Japan **+1.7%**, Europe **+0.5%**, UK **−0.8%**, China **−1.3%**, Brazil **−0.5%**. Yahoo's `^STOXX` closed **+0.47%** at 643.68. Yahoo's `^N225` read **+1.07%** at 22:19 ET, which is the *live Oct 28 Tokyo session* rather than the Oct 27 close Reuters reported.

**Where the volume was.** The most-traded US listings by share volume were overwhelmingly sub-$1 micro-caps (AXG $0.04 −25.65% on 318mn sh; SHFS $0.1158 +23.19% on 270mn; DVLT $0.067 −49.55% on 249mn; XXII +18.55% on 236mn; NEXR +21.77% on 210mn; WFF −33.07% on 120mn). Among names with real market value the leaders were **SOFI** (161.0mn sh), **SPCX** (95.8mn sh, $2.02tn cap), **INTC** (90.5mn, +3.61%), **NU** (99.7mn, −1.51%) and **NVDA** (84.8mn, +0.90%). A tape whose volume leader is a 4-cent micro-cap is a retail-driven one; treat the equal-weight read as more informative than the cap-weight read today.

---

## 2. Sector rotation

**GICS sector proxies** — Yahoo official close, 11/11 confirmed by CNBC to 0.0000%.

| Rank | Sector | ETF | Close | Chg |
|---:|---|---|---:|---:|
| 1 | Information Technology | XLK | 189.49 | **+1.70%** |
| 2 | Consumer Discretionary | XLY | 115.45 | **+1.04%** |
| 3 | Materials | XLB | 51.78 | +0.78% |
| 4 | Utilities | XLU | 42.85 | +0.71% |
| 5 | Industrials | XLI | 167.92 | +0.58% |
| 6 | Health Care | XLV | 179.18 | −0.06% |
| 7 | Financials | XLF | 55.88 | −0.25% |
| 8 | Communication Services | XLC | 103.58 | −0.26% |
| 9 | Real Estate | XLRE | 42.44 | −0.84% |
| 10 | Consumer Staples | XLP | 87.15 | −0.92% |
| 11 | **Energy** | XLE | 68.21 | **−2.05%** |

**Top 3 / bottom 3 (as the skill requires):** Technology, Consumer Discretionary, Materials led; **Energy, Consumer Staples and Real Estate lagged.** The defensives-plus-REITs group falling alongside Energy tells you this was not a risk-off tape — money rotated *within* equities, into growth, and out of the defensives and the energy complex simultaneously.

**Cross-check at the sub-industry level** (TradingView's own 20 industry buckets, median % change, n≥8): strongest were **Non-Energy Minerals +3.89%** (n=179, 92% advancing), **Electronic Technology +3.43%** (n=342, 81%) and **Health Technology +1.72%** (n=830, 72%); weakest were **Energy Minerals −1.16%** (n=103, 39% advancing), **Commercial Services −0.90%** (n=226, 39%) and **Health Services −0.64%** (n=80, 39%). The two views agree: semis and critical minerals up, energy down, and commercial services — the basket that contains the weakest earnings cohort — lagging.

*Note on taxonomy:* TradingView's `sector` field is a sub-industry classification (e.g. "Health Technology", "Non-Energy Minerals"), not the 11 GICS sectors. The ETF table above is the GICS view; the bucket table is the finer one. They are reported separately rather than merged.

---

## 3. Breadth & volatility

**Breadth across the full US universe** (TradingView screener, `type=stock`, `exchange ≠ OTC`; **5,716 rows pulled, 5,716 priced, 0 missing**, read 22:34 ET):

| Measure | Value |
|---|---:|
| Advancing / declining / unchanged | **3,337 / 2,180 / 199** |
| Advancing share | **58.4%** |
| Median change | **+0.32%** |
| Mean change | +1.03% |
| p10 / p25 / p75 / p90 / p99 | −2.39 / −0.68 / +2.46 / +5.79 / +14.75 % |
| Names ≥$1bn cap | 2,621 (57.6% advancing, median +0.28%) |
| \|move\| ≥ 5% | **933** (717 up / 216 down) |
| \|move\| ≥ 10% | **244** (176 up / 68 down) |
| \|move\| ≥ 20% | 50 (29 up / 21 down) |

The distribution is the story: **mean (+1.03%) sits well above median (+0.32%)**, so the index gains were carried by a long right tail rather than by the average stock. Breadth was better than the headline index suggested — small caps matched the Nasdaq — but the *quality* of the advance is thin at the median, and the dispersion is extreme: 933 names moved 5% or more in one session.

**Volatility and options** (Cboe daily stats, fetched 22:45 ET, session date inferred):

| Series | Put/Call |
|---|---:|
| **Total** | **0.93** |
| Equity | 0.59 |
| Index | 1.06 |
| SPX + SPXW | 1.16 |
| ETP | 1.09 |
| DJX | 0.65 |

Equity put/call at 0.59 is call-heavy and consistent with the VIX at 17.52; the index and SPX ratios above 1.0 show hedging was concentrated in index products, not single names. Schwab noted **>53% of S&P stocks above their 50-day average**, up from ~20% at the end of September — the breadth repair is real, not a one-day artefact.

---

## 4. The day's movers

**Top gainers** (TradingView universe, sanity-filtered, % change from Yahoo, caps from CNBC, relative volume = regular volume ÷ 10-day average):

| # | Ticker | Name | Close | Chg | Cap | Rel vol | Catalyst |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | BRAI | Braiin | 3.31 | **+56.13%** | $682M | **53.6×** | none identified this run |
| 2 | CRML | Critical Metals | 8.13 | +27.43% | $1.20bn | — | not researched (critical-minerals complex) |
| 3 | ENVX | Enovix | 3.35 | +25.00% | $735M | — | not researched |
| 4 | HRI | Herc Holdings | 156.06 | +22.76% | $5.22bn | 2.7× | Q3 EPS $3.91 vs $3.08 est; revenue $1.36bn; FY guidance raised; H&E synergies |
| 5 | MFIC | MidCap Financial Investment | 10.26 | +22.73% | $845M | **13.6×** | **Ares Capital acquisition, ~$2.6bn, ≈$10.88/sh** |
| 6 | KNSA | Kiniksa Pharmaceuticals | 89.20 | +22.23% | $6.96bn | 2.7× | Q3 GAAP EPS $0.56; revenue $286mn; ARCALYST +58% y/y; FY26 revenue guide raised to $1.045–1.050bn |
| 7 | PRME | Prime Medicine | 4.35 | +20.50% | $789M | — | not researched |
| 8 | CHRN | Chronoscale | 17.49 | +19.55% | $2.55bn | — | not researched (recent listing) |
| 9 | JBLU | JetBlue Airways | 2.82 | +18.99% | $1.06bn | 1.6× | not researched |
| 10 | USAR | USA Rare Earth | 10.40 | +16.72% | $3.90bn | — | not researched |

Also notable: **SOFI +13.42%** ($16.40, $21.18bn cap, 2.8× rel vol) on a Q3 beat-and-raise — adjusted EPS $0.18 vs $0.17 expected, revenue $1.385bn (+44% y/y), FY26 adjusted net revenue lifted to $5.04bn and adjusted EBITDA to $1.66bn, EPS to $0.61, and **FY27 guidance initiated at $6.4bn revenue and $0.90 EPS** (Street at $0.82), with a record 1.2mn new members and $16.9bn of originations; the stock is still ~44% lower year-to-date. **CTOS +16.65%, HWKN +13.59%, TE +16.04%, TMC +15.06%, AEHR +12.99%, XNDU +14.84%** completed the mid-cap gainer cohort.

**Top losers:**

| # | Ticker | Name | Close | Chg | Cap | Rel vol | Catalyst |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | INOD | Innodata | 44.74 | **−25.32%** | $1.54bn | 9.8× | not researched |
| 2 | XYL | Xylem | 92.86 | **−14.21%** | $21.68bn | 4.9× | Q3 revenue $2.20bn vs $2.28bn est; adj EPS $1.44 vs $1.45; **FY26 revenue guide cut to ~$8.95bn, adj EPS to $5.40–5.45** (from $5.55–5.70) |
| 3 | PICS | Pics NV | 7.59 | −13.55% | $984M | — | not researched |
| 4 | BA | Boeing | 168.18 | **−10.69%** | $132.9bn | 7.1× | Q3 adj EPS −$0.34 vs −$0.20/−0.21 est; **737 delivery target of 500 jets missed**; 787 deliveries to ~90; BCA margin −6.5% (from −2.7%); $700mn 777X charge |
| 5 | UNF | UniFirst | 250.40 | −10.46% | $4.53bn | — | not researched |
| 6 | DK | Delek US | 70.30 | −10.41% | $4.31bn | 0.9× | refiner complex (see below) |
| 7 | PARR | Par Pacific | 74.53 | −10.39% | $3.73bn | — | refiner complex |
| 8 | LYCA | Lycia Therapeutics | 26.11 | −9.50% | n/a | — | not researched |
| 9 | VLO | Valero Energy | 387.34 | −9.24% | $111.5bn | 2.1× | refiner complex |
| 10 | EYE | National Vision | 16.20 | −8.99% | $1.28bn | — | not researched |

Also: **INTA −8.91%, DINO −8.81%, PBF −8.59%, AIT −8.35%, GWRE −8.05%, EEFT −7.72%, CVI −7.40%, MPC −7.36%, PSX −7.03%**.

**The Boeing read.** The loss narrowed to $116mn (26c/share; adjusted −34c) and free cash flow rose to $464mn, and backlog hit a record **$745bn** — but revenue of $24.19bn missed, adjusted EPS missed by 14–69% depending on the consensus used, commercial-airplanes margin went to **−6.5%**, and CEO Kelly Ortberg said the 737 Max rate stays at 47/month with **52/month not until 2H 2027**, meaning the 500-jet 2026 target is missed. A supply-chain dispute with supplier Vaero over a wing component is in the background. Shares closed at their **lowest since April 2025**, down more than 22% year-to-date — the second-worst DJIA performer — on volume roughly **7× the 10-day average**. The market punished the *schedule*, not the quarter.

**The refiner read — why refiners fell 3–5× harder than oil.** WTI settled **−1.83% to $99.90** and Brent −1.67% to $113.88; gasoline futures lost 2.2% and heating oil 2.7%. Refiners fell three to five times that. The margin story, not the barrel: the **3-2-1 crack spread has compressed to roughly $50/bbl from over $72 a month earlier**; Iran de-escalation talk (Khamenei and his security chief discussing conditions to end the conflict) removed part of the geopolitical risk premium that had made the trade work; the **Trump-backed Russian diesel waiver** threatened the distillate tightness that produced Valero's record $39.24/bbl Q3 margin; **Freedom Broker downgraded VLO to Sell (target $358)** against a Wells Fargo $489; **Michael Burry** flagged Valero as a stretched holding he may trim; and **BTIG** warned of a correction after the refining index's ~124% year-to-date gain. Marathon ended a **10-month winning streak** (the record run since 2012–13). Note the irony: Valero's Q3 was a blowout (adjusted EPS $23.89 vs ~$21.28 consensus, revenue $46.1bn) and the stock still fell 9.24% to its worst day since April 2025.

---

## 5. After-hours movers

**Top 10 by absolute move**, with the final extended-hours print and its timestamp (CNBC `ExtendedMktQuote`, cross-checked against TradingView `postmarket_close`; 24/24 agreed within 1pp except the three flagged below).

| Ticker | Name | Close | AH print | AH chg | AH volume | Print (ET) | Cap | Driver |
|---|---|---:|---:|---:|---:|---|---:|---|
| BRAI | Braiin | 3.31 | **5.16** | **+56.00%** | 7,782,348 | 19:59:59 | $682M | no catalyst identified |
| BOOM | DMC Global | 5.35 | 6.23 | **+16.45%** | 1,080,418 | 19:59:24 | $110M | not researched |
| RAPP | Rapport Therapeutics | 27.54 | 22.02 | **−20.04%** | 174,630 | 19:59:37 | $1.32bn | reported after the close; not researched |
| INTA | Intapp | 42.95 | 35.79 | **−16.67%** | 169,579 | 19:35:19 | $3.29bn | reported after the close; not researched |
| ENPH | Enphase Energy | 29.76 | 25.15 | **−15.49%** | 5,098,546 | 19:59:54 | $3.93bn | Q3 adj EPS $0.41 vs $0.51 est; revenue $293.3mn vs $304.6mn; **Q4 guide $225–255mn vs $297.6mn consensus**; sell-through +1% q/q vs +10% expected |
| UCTT | Ultra Clean Holdings | 51.48 | 56.50 | **+9.75%** | 413,646 | 19:52:30 | $2.33bn | record Q3 revenue $759.0mn (+49% y/y); adj EPS $1.15 vs $0.94; Q4 guide $800–860mn |
| ICLR | ICON plc | 182.98 | 201.00 | **+9.85%** | 70,813 | 18:12:24 | $14.12bn | reported after the close; beat (not researched in detail) |
| MANH | Manhattan Associates | 233.98 | 258.00 | **+10.27%** | 84,879 | 19:47:02 | $13.64bn | adj EPS $1.55 vs $1.46 est; revenue $306.2mn vs $297.0mn; cloud subs +28%; RPO $2.59bn (+25%); **FY guide raised to $5.54–5.56 adj EPS** (Street $5.50) |
| BBNX | Beta Bionics | 21.39 | 19.17 | **−10.38%** | 91,868 | 19:28:21 | $1.13bn | reported after the close; not researched |
| CSGP | CoStar Group | 32.01 | 29.40 | **−8.15%** | 463,872 | 19:58:54 | $12.97bn | adj EPS $0.38 vs $0.34 est; revenue $952mn (+14%) vs $945mn; **net new bookings $37mn vs $84mn** prior year; record adj EBITDA $229mn; FY26 EBITDA guide raised to $820–840mn |
| HOOD | Robinhood | 94.56 | 87.34 | **−7.63%** | 8,848,655 | 19:59:59 | $85.02bn | adj EPS $0.60 vs $0.55 est; **net revenue $1.40bn vs $1.43bn est** on softer crypto/equity velocity; FY26 opex high end lowered; ARPU $200 vs $201.09 |
| NXPI | NXP Semiconductors | 253.50 | 234.98 | **−7.31%** | 426,841 | 19:59:51 | $63.92bn | Q4 revenue guide $3.85bn ±$100mn vs $3.86bn consensus; adj op income $1.374–1.442bn vs $1.44bn |
| STX | Seagate | 667.85 | 631.00 | **−5.52%** | 2,073,421 | 19:59:55 | $152.97bn | **beat and raised** (FQ1 adj EPS $7.68 vs $7.39; revenue $4.20bn; FQ2 guide $4.70–4.90bn vs $4.56bn) — sell-the-news after a multi-quarter AI nearline run |
| LOGI | Logitech | 111.82 | 104.85 | −6.23% | 58,258 | 19:50:44 | $17.46bn | reported after the close; not researched |
| PPG | PPG Industries | 113.44 | 121.36 | +6.98% | 159,695 | 19:39:11 | $25.22bn | reported after the close |
| ICHR | Ichor Holdings | 40.75 | 43.31 | +6.29% | 113,099 | 18:19:46 | $1.53bn | reported after the close |
| KIDS | OrthoPediatrics | 23.82 | 25.50 | +7.05% | 13,803 | 19:53:09 | $622M | reported after the close; **thin (13.8k shares)** |

**Three AH prints where the two feeds disagree, flagged rather than averaged:** PRLD (TV +6.94% @16:22 vs CNBC +9.54% @16:22, 15.9k shares), WNEB (TV +9.54% vs CNBC +10.26%, **1,301 shares**), ICHR (TV +5.57% vs CNBC +6.29%). SUN (+5.57% @16:20) rests on **619 shares** and is not a real signal. Where the two feeds differ, **CNBC's later timestamped print is published**.

**The braiin print is the one to sit with.** Braiin closed the regular session **+56.13% at $3.31 on 38.1mn shares (53.6× its 10-day average)** and then added **another +56.00% to $5.16 after hours on 7.78mn shares** — a cumulative ~+137% on the day, with no catalyst identified in this run. It is the largest after-hours move in the US universe this session, and it is a $682mn-cap company with no verified news behind it. That is a fact to verify before acting on it, not a signal.

**After-hours breadth** (TradingView, `postmarket_change`, 2,409 rows carried a print; 1,715 usable after a volume ≥1k / cap >$100mn filter): **39 names moved ≥5%** (23 up / 16 down), 10 moved ≥10%, 3 moved ≥20%, and the median after-hours move was **+0.075%** — i.e. the extended session was quiet, and the action was entirely in the earnings cohort. Of the 40 after-close reporters carried in the panel below, 35 printed, 28 moved ≥2% and **22 moved ≥5%**.

---

## 6. After-hours earnings reactions

The Nasdaq calendar listed **82 after-close reporters for 2026-10-27** (170 rows total: 82 AMC, 60 pre-market, 28 time-not-supplied) — one of the heaviest prints of the year, with Visa, Seagate, Waste Management, Robinhood, NXP, ONEOK, Baker Hughes, Teradyne, Ventas, Arch Capital, EQT and F5 among the largest.

| Ticker | Name | Close | Reg chg | AH print | AH chg | AH vol | Print (ET) | Read |
|---|---|---:|---:|---:|---:|---:|---|---|
| STX | Seagate | 667.85 | +3.67% | 631.00 | **−5.52%** | 2,073,421 | 19:59:55 | beat **and** raised; sold on the news |
| ENPH | Enphase | 29.76 | −1.98% | 25.15 | **−15.49%** | 5,098,546 | 19:59:54 | EPS and revenue miss; Q4 guide far below consensus |
| RAPP | Rapport Therapeutics | 27.54 | +8.72% | 22.02 | **−20.04%** | 174,630 | 19:59:37 | not researched |
| UCTT | Ultra Clean | 51.48 | +10.21% | 56.50 | **+9.75%** | 413,646 | 19:52:30 | record revenue +49%; guide up |
| MANH | Manhattan Associates | 233.98 | −1.02% | 258.00 | **+10.27%** | 84,879 | 19:47:02 | beat and raise; cloud +28% |
| ICLR | ICON plc | 182.98 | −0.44% | 201.00 | +9.85% | 70,813 | 18:12:24 | beat (details not researched) |
| CSGP | CoStar | 32.01 | −5.01% | 29.40 | **−8.15%** | 463,872 | 19:58:54 | beat on EPS/revenue, bookings collapsed to $37mn |
| HOOD | Robinhood | 94.56 | +1.85% | 87.34 | **−7.63%** | 8,848,655 | 19:59:59 | revenue miss, opex guide lowered |
| NXPI | NXP | 253.50 | +3.12% | 234.98 | **−7.31%** | 426,841 | 19:59:51 | Q4 guide in line — "good enough" punished |
| TER | Teradyne | 323.68 | +4.75% | 307.05 | −5.14% | 360,469 | 19:59:45 | not researched |
| LPLA | LPL Financial | 317.56 | +0.10% | 301.68 | −5.00% | 178,625 | 19:56:50 | not researched |
| UHS | Universal Health | 177.32 | −4.52% | 169.00 | −4.69% | 126,312 | 19:12:44 | not researched |
| OI | O-I Glass | 6.43 | −0.16% | 5.95 | −7.47% | 160,620 | 19:30:01 | not researched |
| V | Visa | 401.86 | −0.57% | 397.25 | −1.15% | 332,092 | 19:59:41 | FQ4 beat, **weak FY2027 outlook** |
| CAKE | Cheesecake Factory | 108.47 | −1.51% | 104.90 | −3.29% | 249,146 | 19:52:17 | not researched |
| NOV | NOV Inc. | 20.55 | +1.78% | 19.99 | −2.73% | 150,417 | 19:03:30 | not researched |
| MIR | Mirion Technologies | 15.41 | +3.28% | 14.70 | −4.61% | 70,668 | 19:56:54 | not researched |
| WM | Waste Management | 235.81 | −2.16% | 230.93 | −2.07% | 104,271 | 18:12:46 | not researched |
| FFIV | F5 | 459.36 | −0.48% | 451.54 | −1.70% | 206,481 | 19:58:45 | not researched |
| BKR | Baker Hughes | 59.00 | +5.34% | 58.70 | −0.51% | 826,356 | 19:56:45 | energy earnings: no reaction |
| OKE | ONEOK | 96.01 | −0.36% | 95.85 | −0.17% | 151,247 | 18:25:59 | energy earnings: no reaction |
| EQT | EQT Corp | 56.27 | +2.59% | 56.00 | −0.48% | 166,303 | 19:57:11 | gas: no reaction |
| RNR | RenaissanceRe | 341.22 | −2.97% | 340.75 | −0.14% | 7,994 | 16:00:35 | no extended trade |
| WPC | W. P. Carey | 63.51 | −1.37% | 63.60 | +0.14% | 252,441 | 18:17:58 | flat |
| VTR | Ventas | 83.34 | −4.67% | 83.34 | — | 36,478 | 16:04:19 | **no extended-hours trade** |
| ACGL | Arch Capital | 100.34 | −1.95% | 100.34 | — | 76,733 | 16:41:34 | no extended-hours trade |
| EXR | Extra Space Storage | 144.55 | +0.82% | 144.55 | — | 22,634 | 16:41:59 | no extended-hours trade |
| FE | FirstEnergy | 46.27 | +0.19% | 46.27 | — | 304,883 | 16:26:32 | no extended-hours trade |
| ZWS | Zurn Elkay | 49.15 | −0.34% | 49.15 | — | 29,355 | 16:02:36 | no extended-hours trade |

**The pattern in the after-hours tape is dispersion, not direction.** Eleven of the 28 names that moved ≥2% fell and 11 rose — but the *magnitudes* are what differ: the two biggest gainers (UCTT +9.75%, MANH +10.27%) beat and raised, and the two biggest losers (ENPH −15.49%, RAPP −20.04%) had guidance or print problems. Three names that **beat and raised** (Seagate, and CoStar on the headline numbers) still fell, which is the market pricing *quality of guidance and bookings* rather than the headline EPS. And the energy reporters (BKR +5.34% regular, OKE, EQT) drew **no after-hours reaction at all**, which is a useful contrast with the refining rout earlier in the day: the energy read was a crack-spread story, not an earnings story.

**Print spread, second read.** A second live read was impossible (the session is closed), but a third source captured the *early* after-hours marks: Ultra Clean was **+16.16% at $59.80** and Enphase **−12.63% at $26.00** in the first prints, versus **+9.75% at $56.50** and **−15.49% at $25.15** at the 19:52/19:59 ET close. The final prints are published above; the early prints are not treated as equivalent numbers.

---

## 7. Tomorrow's setup (Wednesday, October 28)

**Futures** — Yahoo, live print at **22:23–22:24 ET**, percentage measured against the prior settle (not a cash-close comparison):

| Contract | Level | vs prior settle |
|---|---:|---:|
| S&P 500 (ES) | 7,753.75 | −0.06% |
| Nasdaq 100 (NQ) | 29,854.00 | +0.14% |
| Dow (YM) | 52,431 | −0.28% |
| Russell 2000 (RTY) | 2,821.5 | −0.25% |
| **WTI crude (CL)** | **101.25** | **+1.35%** |
| Gold (GC) | 4,059.20 | −0.38% |
| Bitcoin | 80,806.77 | +1.42% |
| Dollar index (DXY) | 102.416 | +0.10% |

The futures curve is a **flat, slightly lower cash tone with oil bouncing ~1.35% off the $99.90 settle**. If the crack-spread story is right, a crude bounce compresses the refiner trade further rather than rescuing it. Note the futures are **~10 minutes stale** relative to this artifact's write time and are labelled as a live quote, not a close.

**Macro calendar, Wed 2026-10-28 (all times ET):**

| Time | Event | Why it matters |
|---|---|---|
| 8:30 AM | **Advance Economic Indicators, Sep** (Census) — advance goods trade balance, retail inventories | First hard trade/inventory print; sets the pre-FOMC tone |
| 9:45 AM | **Bank of Canada decision + MPR** | The BoC is the other G10 in the same 24h window |
| 10:00 AM | Housing Vacancies & Homeownership, Q3 (Census) | Second-tier; REITs underperformed today |
| 10:00 AM | Metro Area Employment & Unemployment (Sep) + Business Employment Dynamics (Q1) (BLS) | Second-tier labour detail |
| 10:30 AM | **EIA Weekly Petroleum Status** | Lands before the Fed; direct read on the distillate tightness that drove the refiner trade |
| 11:30 AM | Treasury 17-week bill and 2-year FRN auctions | Front-end supply into an FOMC day |
| **2:00 PM** | **FOMC statement** | **The event.** No projections (non-SEP meeting) |
| **2:30 PM** | **FOMC press conference — Chair Kevin Warsh** | Where the December path gets repriced |

Already in progress at the time of this pull: the **RBNZ** decision was scheduled for 9:00 PM ET on Oct 27 (approx. 80–85% priced for a 25bp hike to 3.00%).

**The Fed setup.** The target range is **3.75–4.00%** (raised 25bp on 16 September). A **hold is the base case**: 94 of 100 economists in a Reuters poll (16–20 Oct) expect no change, 6 expect a 25bp hike, and CME FedWatch showed roughly a **90–93% hold probability** at today's close. The live question is not this meeting but the next one: **all 100 economists expect a December hike** while futures price only ~71–80% of one, and 16 of the 18 September projections implied at least one more increase in 2026 with none for a cut. Inflation is running 3.7%. The gap between the economists' 100% and the market's ~71% is the number the statement language moves. The next SEP arrives 8–9 December.

**Thursday's follow-on risk:** 8:30 AM ET on Oct 29 brings **September PCE and advance Q3 GDP** (PCE m/m consensus 0.3%, y/y 3.6%, core 3.0%; GDP q/q consensus 3.1% vs 3.2% prior). That print lands one session after the Fed and is directly on the December-hike path.

**Earnings tomorrow (Nasdaq calendar, 227 rows: 134 AMC, 86 pre-market, 7 no-time):**

*After the close* — **Microsoft** (EPS est. $4.71) and **Alphabet** (est. $2.94) are the two events of the week, alongside **KLA, ServiceNow, T-Mobile US, Fortinet, Equinix, Agnico Eagle, Canadian Pacific Kansas City, O'Reilly Automotive, FedEx, Carvana** and BBVA.

*Before the open* — **GE Vernova, Amphenol, Banco Santander, UBS, ADP, Phillips 66, GSK, Vertiv, American Electric Power, Boston Scientific, Aon, TE Connectivity, Garmin, United Microelectronics.**

Two notes. **Phillips 66 reports before the open tomorrow**, which puts a fourth large refiner into the crack-spread question on a day when the group has already lost 7–10%. And **MSFT + GOOG after the close tomorrow** is the first real test of the AI-capex trade that carried today's session: the SOX's +3.6% and the Nasdaq's best-day-in-a-month both rest on continued AI capex optimism, and both names report on the same evening.

**Global overnight:** the Nikkei is +1.07% live into the Oct 28 Tokyo session (Yahoo, 22:19 ET); the Oct 27 Tokyo close was +1.7% (Reuters).

---

## 8. Watchlist EOD review — **omitted (input file absent)**

`research/watchlist.yaml` does not exist in this sandbox. The skill's Step 1 and Step 4 both depend on it, and the skill's own post-market procedure has no defined behaviour for a missing watchlist. Following the precedent set by the companion pre-market cron, **no watchlist section was written and no default watchlist was created** — inventing a basket and reporting it as "the watchlist" would be fabrication. Everything a watchlist review would have covered (close, day change, day range, after-hours print, volume vs average) was collected for the full 5,716-name universe and is available in the movers and after-hours tables above; naming which of those names matter for tomorrow is the one thing this brief cannot do.

---

## 9. Open research queue

1. **What drove Braiin?** +56.13% regular and +56.00% after hours on a $682mn cap with no identifiable news. A $2.6bn-scale event or a microcap squeeze — the data alone cannot tell, and this is the single largest after-hours move in the universe.
2. **Is the refiner drawdown a margin repricing or the start of a de-rating?** Test the 3-2-1 crack (reported ~$50/bbl vs >$72 a month ago) against the EIA petroleum status release tomorrow 10:30 AM ET, and against whether WTI's overnight +1.35% bounce compresses it further.
3. **Does the MSFT/GOOG print confirm or interrupt the AI trade?** Today's entire index story rests on AI optimism continuing; both report tomorrow after the close.
4. **The Fed's December path:** does the statement language close the gap between 100% of economists and ~71% of futures pricing a December hike?
5. **TradingView's stale `change` reference on MSGK** (+40.18% vs a true +5.52%, verified against the 5-day series: 10-26 close 289.45 → 10-27 close 305.42). Ticker/issuer renames may leave other rows with a stale reference; the fix is to compare `close` against a second feed, never the percentage.
6. **Unresearched single names in the tail** — INOD −25.32%, PICS −13.55%, UNF −10.46%, PRME +20.50%, CHRN +19.55%, USAR +16.72%, JBLU +18.99%, ENVX +25.00%, CRML +27.43% — catalysts not verified in this run; no cause is inferred for them.
7. **Why the Nasdaq gained 1.18% while the Dow gained 0.03%** beyond Boeing: index-level attribution (sector weights) was not computed, and the SOX's +3.6% likely carries a disproportionate share of the Nasdaq move.

---

## 10. Source health & method

**Endpoints used** (all read 2026-10-27, 22:32–22:52 ET; TLS verified, no proxy fallback needed):

| Source | Endpoint | Rows / coverage | Freshness stamp | Status |
|---|---|---|---|---|
| Yahoo Finance | `query2.finance.yahoo.com/v7/finance/spark` | 36 + 44 symbols, 0 missing | `regularMarketTime` 16:00–17:16 ET | OK (short `Mozilla/5.0` UA, 12 symbols/batch) |
| Yahoo Finance | `query2.finance.yahoo.com/v8/finance/chart` | MSGK 5-day series | daily bars 10-21 → 10-27 | OK |
| TradingView | `scanner.tradingview.com/america/scan` | **5,716 / 5,716 rows** (one call, `range [0,40000]`) | `postmarket_time` = 16:00 ET session boundary | OK — closes validated against Yahoo 44/44 |
| CNBC | `quote.cnbc.com/.../restQuote` | 28 core + 65 named + 40 AMC | `last_time` per print | OK; `last` ≠ official close on 1 row |
| Nasdaq | `api.nasdaq.com/api/calendar/earnings` | 170 (10-27), 227 (10-28) rows | session dates | OK; foreign issuers absent (coverage gap) |
| Nasdaq | `api.nasdaq.com/api/marketmovers` | 0 rows returned | — | **Returned empty for both asset classes — not used** |
| Cboe | `cboe.com/us/options/market_statistics/daily` | put/call table | **no date stamp; session inferred** | OK with caveat |
| web_search | catalyst research | 9 queries | 2026-10-27 | OK; secondary sources discounted |

**Cross-checks performed and their results:**

- **TV close vs Yahoo official close: 44/44 exact, max |diff| 0.0000%.** This validates the TradingView US feed as a close source *at this read time* (the 900-second delay does not affect a post-close read), and it is why the TV `change` artifact on MSGK was caught rather than published.
- **CNBC vs Yahoo on indices: 5/5 exact (0.0000%).** Sector ETFs: 11/11 exact.
- **TV postmarket vs CNBC after-hours: 24/24 within 1pp**, except PRLD, WNEB and ICHR (flagged individually).
- **A stale-reference test, not a % comparison**, was used to validate the movers: the 5-day Yahoo series confirmed MSGK's true prior close (289.45), matching Yahoo's `regularMarketChangePercent` and contradicting TV's +40.18%.
- **Relative volume** is regular-session volume ÷ CNBC's 10-day average — a consistent single-vendor denominator, not a blended one.

**What is not in this brief:** no position sizing, no P&L, no trade instruction (read-only by design, per the skill's hard rules). No watchlist-derived claims. No cause is asserted for any name whose catalyst was not verified against a fetched source. The Nasdaq market-movers endpoint returned no rows and was therefore not used as a source.

**Primary source links for the factual claims above:**

- Boeing Q3 and production targets — https://www.cnbc.com/2026/10/27/-boeing-ba-q3-2026-earnings.html · https://www.investors.com/news/boeing-earnings-q3-2026-ba-stock-dow-jones-737-max-orders-defense/
- Xylem guidance cut — https://www.barrons.com/articles/xylem-earnings-stock-price-728f2d11 · https://finance.yahoo.com/markets/stocks/articles/why-xylem-xyl-stock-nosediving-211847634.html
- Refiner rout and crack spreads — https://www.benzinga.com/markets/equities/26/10/62634697/refiner-stocks-valero-marathon-worst-day-since-april-2025-iran-russian-diesel
- SoFi beat-and-raise — https://finance.yahoo.com/markets/stocks/articles/sofi-says-had-exceptional-quarter-163128685.html
- MFIC/Ares Capital and KNSA — https://www.benzinga.com/markets/market-summary/26/10/62628860/crude-oil-moves-lower-corning-earnings-top-views
- After-hours movers panel — https://www.cnbc.com/2026/10/27/stocks-making-the-biggest-moves-after-hours-v-hood-nxp-stx-more-.html · https://www.investing.com/news/stock-market-news/afterhours-movers-stx-enph-hood-v-csgp-boom-cake-ppg-oi-ter-432SI-4976906 · https://www.thecorequant.com/the-wall-street-wrap-october-27-2026
- CoStar results (Business Wire) — https://www.businesswire.com/news/home/20261027046911/en/
- Manhattan Associates results — https://sg.finance.yahoo.com/news/manhattan-associates-soars-11-strong-211934499.html
- Session narrative and global round-up — https://www.reuters.com/5f374b32b07b/commentary/reuters-open-interest/global-markets-trading-day-graphic-2026-10-27/ · https://www.cnbc.com/amp/2026/10/26/stock-market-today-live-updates.html · https://www.eoption.com/market-review-october-27-2026/
- FOMC expectations — https://www.piptheory.com/research/fomc-october-2026-preview-october-28-dollar-december-hike · https://www.kiplinger.com/investing/live/fed-meeting-updates-and-commentary-october-2026 · https://www.stocktitan.net/articles/fed-rate-decision-october-28-2026
- Oct 28 macro calendar — https://www.bls.gov/schedule/2026/10_sched_list.htm · https://tradingeconomics.com/united-states/calendar/news/585099 · https://smalltax.com/tools/economic-calendar/

*Generated by Cloud cron #23 `agentic-post-market-brief` on 2026-10-27. Read-only research output; no trade was placed or recommended.*
