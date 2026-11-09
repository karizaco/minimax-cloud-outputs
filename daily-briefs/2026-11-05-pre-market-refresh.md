---
date: 2026-11-05
cron: 26b-agentic-pre-market-brief-refresh
fire_time_et: 2026-11-05 09:20
snapshot_et: 10:10
source: TradingView america scanner
status: ok
changes_since_morning: n/a
morning_brief: absent (cron #26 08:30 ET fire failed - Token Plan quota 2056)
pull_late: true
market_open_at_pull: true
---

# Pre-market refresh — Thursday 2026-11-05 (09:20 ET checkpoint · screen pulled 10:10 ET)

> **UPDATE — 2026-11-06 05:55 ET: the baseline resolved.** Cron #26's 08:30 ET fire was
> quota-killed, not dead: the platform resumed that conversation IN PLACE on 2026-11-06 and
> the morning brief was published at 05:52 ET (commit `73d1c5aa`, fix-forward `2adb42ef`),
> rebuilt for the 11-05 fire and citing THIS artifact and cron #92a's 10:10:24 ET checkpoint
> as its screen sources. The note below describes the state as it stood at this file's pull
> (10:10 ET) — at that moment the baseline had indeed not landed.

**This file was pulled at 2026-11-05 10:10:37 ET, not at 09:20 ET.** The platform created this fire at 09:20:12 ET but the first tool call did not execute until 10:09 ET — a 49-minute stall that spans the 09:30 open. Two consequences, stated up front:

1. **The 09:20 ET baseline does not exist.** Cron #26's 08:30 ET morning brief failed at 08:30:30 ET with `42212: Token Plan usage limit reached (2056)` and published neither `daily-briefs/2026-11-05-pre-market.md` nor its CSV. There is no same-screen 08:30 snapshot to diff against, so this file publishes the refreshed screen alone, with no "changed since" section. §5 substitutes a clearly-labelled cross-check against a *different* screen (cron #15's 08:22 ET file), not a same-screen baseline.
2. **The `premarket_*` columns are the completed 11-05 pre-market session, not a 09:20 snapshot.** TradingView freezes the pre-market session (04:00–09:30 ET) at the open; `premarket_time` reads 2026-11-05 04:00 ET on all 779 rows returned. The gaps below are the **final pre-market prints** — the last look before the bell, which is later than intended but not less complete. The regular-session columns (`close`, `change`, `volume`) are **live at 10:10** and are published only in §4, labelled as live; they are never presented as "yesterday's tape".

**Tape shape:** 379 names at or above +3% and 547 at or below -3% (up/down ratio 0.69) — a materially downside-tilted board. Of the 779 rows returned, 121 gainers and 181 decliners cleared the liquidity gate, and 104 and 150 cleared liquidity *and* the $100M quality floor. 258 gainers and 219 returned decliners failed the liquidity gate and are excluded entirely (a ±20% print on 100 shares is not a market). The decliner-side counts are lower bounds — the decliner screen returned 400 of 547 rows (see the truncation note in Source health).

---

## 1. Refreshed top-of-book — gainers (top 15)

_*%ADV below 5% is flagged `thin` — a thin print on almost no volume, not a market (brief skill, Step 2b). Pre-market session 04:00–09:30 ET, final prints; screen pulled 10:10 ET._*

| Ticker | Name | Pre-market | % | Pm vol | %ADV | Mkt cap | Sector | Snapshot (ET) |
|---|---|---|---|---|---|---|---|---|
| AEHL | Antelope Enterprise Holdings Limited | 12.77 | +103.67% | 4,047,023 | 401.20% | $200.9M | Producer Manufacturing | 10:10 |
| AMTX | Aemetis, Inc | 1.73 | +38.40% | 771,552 | 82.33% | $134.2M | Process Industries | 10:10 |
| TBI | TrueBlue, Inc. | 13.28 | +34.96% | 100,372 | 49.54% | $376.0M | Commercial Services | 10:10 |
| ARQ | Arq, Inc. | 2.4903 | +34.61% | 3,354,499 | 701.32% | $107.9M | Process Industries | 10:10 |
| APP | Applovin Corporation | 350 | +28.79% | 1,041,075 | 21.78% | $120.33B | Technology Services | 10:10 |
| SEZL | Sezzle Inc. | 172.66 | +26.32% | 44,326 | 8.71% | $5.61B | Technology Services | 10:10 |
| LYNX | Lyntris Inc. | 11.5 | +22.47% | 22,859 | 4.90% (thin) | $1.32B | Technology Services | 10:10 |
| WRBY | Warby Parker Inc. | 25.75 | +20.95% | 331,654 | 10.59% | $3.14B | Retail Trade | 10:10 |
| XERS | Xeris Biopharma Holdings, Inc. | 12.5 | +19.50% | 168,699 | 5.58% | $2.46B | Health Technology | 10:10 |
| RUN | Sunrun Inc. | 10.49 | +19.34% | 2,609,814 | 27.76% | $2.33B | Electronic Technology | 10:10 |
| GROY | Gold Royalty Corp. | 3.37 | +16.61% | 227,585 | 17.63% | $732.1M | Non-Energy Minerals | 10:10 |
| FUN | Six Flags Entertainment Corporation | 9.2 | +16.02% | 1,180,856 | 22.01% | $983.3M | Consumer Services | 10:10 |
| BKSY | BlackSky Technology Inc. | 19.36 | +15.44% | 82,742 | 9.03% | $764.7M | Technology Services | 10:10 |
| IRWD | Ironwood Pharmaceuticals, Inc. | 4.33 | +14.85% | 202,410 | 11.72% | $686.6M | Health Technology | 10:10 |
| ADMA | ADMA Biologics Inc | 12.01 | +14.60% | 221,434 | 6.77% | $2.80B | Health Technology | 10:10 |

*104 names clear both gates and are at or above +3%; the top 15 are shown.*

## 2. Refreshed top-of-book — decliners (top 10)

| Ticker | Name | Pre-market | % | Pm vol | %ADV | Mkt cap | Sector | Snapshot (ET) |
|---|---|---|---|---|---|---|---|---|
| MNTN | MNTN, Inc. | 5.1 | -50.82% | 715,507 | 88.04% | $775.7M | Technology Services | 10:10 |
| VCYT | Veracyte, Inc. | 29.41 | -44.00% | 195,413 | 14.82% | $4.22B | Health Technology | 10:10 |
| AKBA | Akebia Therapeutics, Inc. | 0.5098 | -26.62% | 688,765 | 8.80% | $131.7M | Health Technology | 10:10 |
| ROCK | Gibraltar Industries, Inc. | 32.01 | -26.55% | 18,444 | 4.84% (thin) | $1.07B | Producer Manufacturing | 10:10 |
| HIMX | Himax Technologies, Inc. | 7.76 | -25.67% | 325,081 | 29.72% | $1.78B | Electronic Technology | 10:10 |
| GIL | Gildan Activewear, Inc. | 32.23 | -25.51% | 225,826 | 13.95% | $6.07B | Consumer Non-Durables | 10:10 |
| LZ | LegalZoom.com, Inc. | 5.195 | -24.71% | 40,332 | 1.60% (thin) | $1.01B | Technology Services | 10:10 |
| DDD | 3D Systems Corporation | 2.07 | -21.59% | 423,496 | 17.19% | $304.9M | Technology Services | 10:10 |
| TRIP | TripAdvisor, Inc. | 8.04 | -21.18% | 410,270 | 12.42% | $993.9M | Consumer Services | 10:10 |
| TDUP | ThredUp Inc. | 1.75 | -20.09% | 147,978 | 9.06% | $207.5M | Retail Trade | 10:10 |

*150 names clear both gates and are at or below -3%; the top 10 are shown.*

### Thin tape — cleared Gate A, below the $100M cap (17 gainers, 31 decliners)

Real moves on sub-$100M caps. They never top a headline table, but they carry the largest gaps on the board, so they are published here rather than hidden.

**Thin gainers (17)**

| Ticker | Name | Pre-market | % | Pm vol | %ADV | Mkt cap | Sector | Snapshot (ET) |
|---|---|---|---|---|---|---|---|---|
| LABT | Lakewood-Amedex Biotherapeutics Inc. | 0.385 | +101.15% | 149,156,604 | 1119.02% | $453.6K | Health Technology | 10:10 |
| ZNB | Zeta Network Group | 1.19 | +91.32% | 47,211,055 | 1133.07% | $5.6M | Technology Services | 10:10 |
| FLYE | Fly-E Group, Inc. | 2.72 | +59.99% | 11,954,329 | 178.54% | $3.8M | Consumer Durables | 10:10 |
| ELPW | Elong Power Holding Limited | 3.49 | +39.04% | 28,960,873 | 906.97% | $3.6M | Producer Manufacturing | 10:10 |
| SMX | SMX (Security Matters) Public Limited Company | 1.44 | +22.03% | 1,638,664 | 244.26% | $1.4M | Technology Services | 10:10 |
| JDZG | JIADE LIMITED | 0.3527 | +16.94% | 51,416,508 | 1314.72% | $1.9M | Commercial Services | 10:10 |
| CCLD | CareCloud, Inc. | 2.09 | +16.11% | 305,517 | 133.24% | $93.6M | Technology Services | 10:10 |
| MTEK | Maris-Tech Ltd. | 0.297 | +14.23% | 457,546 | 24.61% | $3.2M | Consumer Durables | 10:10 |
| VRAX | Virax Biolabs Group Limited | 1.33 | +10.83% | 1,752,738 | 287.36% | $1.6M | Finance | 10:10 |
| HIHO | Highway Holdings Limited | 0.9249 | +10.11% | 210,854 | 758.56% | $4.1M | Producer Manufacturing | 10:10 |
| PLCE | Children's Place, Inc. (The) | 0.265 | +9.96% | 29,709,482 | 637.06% | $7.3M | Retail Trade | 10:10 |
| NUR | Nuran Wireless Inc. | 0.55 | +9.67% | 239,233 | 20.48% | $6.3M | Distribution Services | 10:10 |
| SPWR | SunPower Inc. | 0.2594 | +7.19% | 340,580 | 13.90% | $75.2M | Industrial Services | 10:10 |
| BLNK | Blink Charging Co. | 0.478 | +5.89% | 180,767 | 12.79% | $63.4M | Producer Manufacturing | 10:10 |
| MOBX | Mobix Labs, Inc. | 0.6369 | +4.43% | 283,308 | 4.47% (thin) | $13.8M | Electronic Technology | 10:10 |
| OMH | Ohmyhome Limited | 16.2 | +4.18% | 2,370,755 | 70.20% | $31.2M | Finance | 10:10 |
| SLQT | SelectQuote, Inc. | 0.51 | +3.79% | 370,046 | 25.97% | $81.5M | Finance | 10:10 |

**Thin decliners (31)**

| Ticker | Name | Pre-market | % | Pm vol | %ADV | Mkt cap | Sector | Snapshot (ET) |
|---|---|---|---|---|---|---|---|---|
| PARA | Parabolic Technologies, Inc. | 0.218 | -31.66% | 3,854,061 | 66.39% | $121.4K | Technology Services | 10:10 |
| NWGL | CL Workshop Group Limited | 0.039 | -29.73% | 7,582,281 | 17.51% | $3.1M | Non-Energy Minerals | 10:10 |
| TEAD | Teads Holding Co. | 0.195 | -29.17% | 273,928 | 16.44% | $17.6M | Technology Services | 10:10 |
| ANVS | Annovis Bio, Inc. | 0.87 | -28.10% | 203,562 | 20.01% | $30.3M | Health Technology | 10:10 |
| KPTI | Karyopharm Therapeutics Inc. | 0.053 | -27.30% | 5,136,946 | 70.61% | $1.3M | Health Technology | 10:10 |
| BZFD | BuzzFeed, Inc. | 0.6902 | -25.04% | 968,002 | 311.44% | $51.7M | Technology Services | 10:10 |
| ADGM | Adagio Medical Holdings, Inc | 0.0695 | -19.37% | 237,741 | 10.96% | $1.8M | Health Technology | 10:10 |
| ARAY | Accuray Incorporated | 0.1236 | -17.10% | 343,464 | 2.28% (thin) | $14.2M | Health Technology | 10:10 |
| HUBC | Hub Cyber Security Ltd. | 0.0789 | -16.95% | 1,616,129 | 6.88% | $136.5K | Commercial Services | 10:10 |
| PMAX | Powell Max Limited | 0.87 | -16.35% | 426,891 | 20.34% | $1.6M | Communications | 10:10 |
| CENN | Cenntro Inc. | 0.1486 | -16.05% | 1,215,582 | 28.97% | $2.3M | Consumer Durables | 10:10 |
| OSTX | OS Therapies Incorporated | 0.97 | -15.65% | 300,338 | 47.14% | $39.5M | Health Technology | 10:10 |
| INLF | INLIF LIMITED | 0.2627 | -14.49% | 1,041,760 | 3.22% (thin) | $370.3K | Producer Manufacturing | 10:10 |
| SHFS | SHF Holdings, Inc. | 0.0272 | -14.31% | 27,096,064 | 27.67% | $2.5M | Finance | 10:10 |
| CDT | CDT Equity Inc. | 0.0438 | -13.95% | 49,241,537 | 362.71% | $375.7K | Health Technology | 10:10 |
| CRIS | Curis, Inc. | 0.968 | -12.79% | 4,453,980 | 56.58% | $7.3M | Health Technology | 10:10 |
| DKI | DarkIris Inc. | 1.82 | -12.50% | 253,124 | 9.85% | $1.7M | Technology Services | 10:10 |
| HPAI | Helport AI Limited | 0.291 | -11.82% | 1,660,426 | 27.94% | $12.0M | Technology Services | 10:10 |
| RCT | RedCloud Holdings plc | 0.0299 | -10.48% | 4,256,262 | 10.68% | $2.3M | Technology Services | 10:10 |
| GXAI | Gaxos.ai Inc. | 0.4003 | -10.45% | 116,167 | 73.80% | $4.4M | Technology Services | 10:10 |
| FTCI | FTC Solar, Inc. | 1.241 | -10.07% | 439,150 | 12.29% | $22.9M | Technology Services | 10:10 |
| VIVK | Vivakor, Inc. | 0.44 | -8.83% | 154,782 | 7.15% | $701.0K | Process Industries | 10:10 |
| JAGX | Jaguar Health, Inc. | 0.46 | -7.78% | 203,864 | 6.00% | $1.0M | Health Technology | 10:10 |
| MASK | 3 E Network Technology Group Ltd | 1.53 | -6.71% | 2,269,931 | 286.68% | $2.2M | Technology Services | 10:10 |
| BDMD | Baird Medical Investment Holdings Ltd | 0.1022 | -6.32% | 82,451,499 | 807.63% | $3.8M | Health Technology | 10:10 |
| YFOR | YYForce Inc. | 0.12 | -6.25% | 433,761 | 7.51% | $1.5M | Commercial Services | 10:10 |
| WFF | WF Holding Limited | 1.2398 | -6.08% | 170,710 | 4.65% (thin) | $7.1M | Process Industries | 10:10 |
| SDEV | Stablecoin Development Corporation | 0.9107 | -5.82% | 303,993 | 0.88% (thin) | $65.3M | Finance | 10:10 |
| BURU | Nuburu, Inc. | 0.2265 | -4.83% | 763,564 | 1.46% (thin) | $2.8M | Electronic Technology | 10:10 |
| MERC | Mercer International Inc. | 0.2383 | -4.68% | 527,955 | 2.19% (thin) | $15.0M | Process Industries | 10:10 |
| GPUS | Hyperscale Data, Inc. | 0.1544 | -4.40% | 2,149,174 | 4.60% (thin) | $28.5M | Producer Manufacturing | 10:10 |

## 3. What changed since the morning brief

**Not published — the 08:30 baseline does not exist.** Cron #26's 08:30 ET fire failed at 08:30:30 ET with a Token Plan quota error (`42212 … (2056)`) and wrote no artifact and no CSV. The procedure's rule for a missing morning brief is to publish the refreshed screen alone; there is no same-screen earlier pull on this date to measure against, so no delta table is published here rather than a delta table measured against a different screen.

## 4. Where the tape landed after the 09:30 open (live session — NOT pre-market)

These are **live regular-session values at 10:10 ET**, measured against the 11-04 regular close. They are published here because the market was already open when the pull ran, and because the difference between the final pre-market print and the live tape is the only "what moved" read available without the 08:30 baseline. Sorted by the size of that change, not by the size of the gap. **Nothing in this section is a pre-market number.**

| Ticker | Pre-mkt % | Pre-mkt px | 11-04 close | Live px | Live % | Δ move (pp) | Live vol | Snapshot (ET) |
|---|---|---|---|---|---|---|---|---|
| AEHL | +103.67% | 12.77 | 6.27 | 10.5633 | +68.47% | -35.19 | 8,212,178 | 10:10 |
| VCYT | -44.00% | 29.41 | 52.52 | 22.58 | -57.01% | +13.00 | 3,199,841 | 10:10 |
| LZ | -24.71% | 5.195 | 6.9 | 5.9261 | -14.11% | -10.60 | 579,390 | 10:10 |
| AMTX | +38.40% | 1.73 | 1.25 | 1.86 | +48.80% | +10.40 | 6,348,327 | 10:10 |
| TBI | +34.96% | 13.28 | 9.84 | 12.3499 | +25.51% | -9.45 | 367,719 | 10:10 |
| XERS | +19.50% | 12.5 | 10.46 | 13.48 | +28.87% | +9.37 | 2,250,129 | 10:10 |
| RUN | +19.34% | 10.49 | 8.79 | 9.6732 | +10.05% | -9.29 | 9,430,049 | 10:10 |
| ROCK | -26.55% | 32.01 | 43.58 | 36 | -17.39% | -9.16 | 378,931 | 10:10 |
| DDD | -21.59% | 2.07 | 2.64 | 1.835 | -30.49% | +8.90 | 3,087,278 | 10:10 |
| TDUP | -20.09% | 1.75 | 2.19 | 1.58 | -27.85% | +7.76 | 1,170,164 | 10:10 |
| AKBA | -26.62% | 0.5098 | 0.6947 | 0.4754 | -31.57% | +4.95 | 3,756,920 | 10:10 |
| SEZL | +26.32% | 172.66 | 136.69 | 166.0725 | +21.50% | -4.82 | 574,433 | 10:10 |
| TRIP | -21.18% | 8.04 | 10.2 | 8.4801 | -16.86% | -4.31 | 2,238,450 | 10:10 |
| APP | +28.79% | 350 | 271.75 | 359.56 | +32.31% | +3.52 | 7,066,755 | 10:10 |
| MNTN | -50.82% | 5.1 | 10.37 | 4.875 | -52.99% | +2.17 | 3,053,879 | 10:10 |
| WRBY | +20.95% | 25.75 | 21.29 | 25.365 | +19.14% | -1.81 | 1,360,691 | 10:10 |
| HIMX | -25.67% | 7.76 | 10.44 | 7.915 | -24.19% | -1.48 | 1,284,268 | 10:10 |
| GIL | -25.51% | 32.23 | 43.27 | 32.76 | -24.29% | -1.22 | 1,490,949 | 10:10 |
| LYNX | +22.47% | 11.5 | 9.39 | 11.4 | +21.41% | -1.06 | 330,971 | 10:10 |
| ARQ | +34.61% | 2.4903 | 1.85 | 2.471 | +33.57% | -1.04 | 6,866,934 | 10:10 |

*Δ move = |live %| − |pre-market %|: **positive = the move EXTENDED further from the 11-04 close after the open; negative = it FADED back toward the 11-04 close.** It is not a signed price change.*

**Of these 20 leaders, 8 ended further from the 11-04 close than their pre-market print (5 decliners and 3 gainers) and 12 faded back toward it.** The pre-market gap was not the opening gap for the names that extended, and it overstated the move for the names that faded.

## 5. Cross-check — cron #15's 08:22 ET pre-market gap table (a different screen)

Cron #15 published `earnings/2026-11-05-reactions.md` at 08:22 ET with its own pre-market gap table. It is **not** the same screen — #15 scans a top-200-market-cap universe with a 10,000-share volume floor, this file scans the whole US market at ±3% — so it is used here only as an independent anchor, never as a baseline for a same-screen delta.

**The two sources agree on the reference close.** Of 79 tickers present in both, **79** carry an identical 11-04 regular close (within $0.006) — the pre-market gaps below are measured against the same denominator, so the comparison is apples-to-apples on price even though the universes differ.

| Ticker | 08:22 % (#15) | Final pre-mkt % (this pull) | Δ pp | Mkt cap | Pm vol |
|---|---|---|---|---|---|
| APP | +21.47% | +28.79% | +7.32 | $120.33B | 1,041,075 |
| ULCC | +4.09% | +8.04% | +3.95 | $1.63B | 129,952 |
| ZG | -11.95% | -8.51% | +3.44 | $6.99B | 71,766 |
| FOUR | -15.19% | -11.76% | +3.43 | $3.05B | 63,225 |
| SEZL | +29.49% | +26.32% | -3.17 | $5.61B | 44,326 |
| VCEL | +7.50% | +10.53% | +3.03 | $2.79B | 10,330 |
| QCOM | -10.39% | -13.36% | -2.97 | $167.16B | 586,461 |
| AMD | -4.56% | -7.52% | -2.96 | $699.34B | 1,281,674 |
| EXPE | -7.25% | -9.78% | -2.53 | $33.26B | 28,209 |
| ANET | -3.63% | -5.87% | -2.24 | $207.53B | 93,420 |
| PH | +7.67% | +5.47% | -2.20 | $118.84B | 11,848 |
| CAMT | -2.73% | -4.88% | -2.15 | $4.39B | 12,412 |
| PENG | -4.86% | -6.93% | -2.07 | $2.48B | 39,338 |
| NET | -3.92% | -5.87% | -1.95 | $86.05B | 46,104 |
| AVGO | -2.56% | -4.42% | -1.86 | $1,475.62B | 438,629 |

*58 overlapping names clear both gates; the 15 with the largest change are shown.*

## 6. Verdict

**Not answerable against 08:30 ET — there is no 08:30 ET brief to compare with, so the directional question this file exists to answer cannot be answered from the fleet's own artifacts.** What the board itself says at 10:10 ET:

- The tape is **downside-tilted**: 379 names at or above +3% against 547 at or below -3%, a ratio of 0.69.
- The tilt is **wider on the downside through the gates**: at least 150 decliners clear both gates against 104 gainers, even though the single largest gain (+103.67%, AEHL) beats the largest loss (-50.82%, MNTN).
- After the open the **extremes extended and the rest faded**: of the 20 leaders, 8 ended further from the 11-04 close than their pre-market print (5 decliners, 3 gainers) and 12 faded back toward it.
- No 08:30 comparison is published and none is estimated. The next fire that can answer the directional question is cron #23's post-market brief for 11-05, and tomorrow's 08:30 brief.

## Source health

| Source | Result |
|---|---|
| TradingView `america` scanner (one pull, both screens) | OK — 779 of 926 in-band rows returned (379 gainers, complete; 400 of 547 decliners) at 2026-11-05 10:10:37 ET; one pull feeds every table above |
| Morning brief CSV `daily-briefs/2026-11-05-pre-market.csv` | **ABSENT** — cron #26's 08:30 ET fire failed with `42212: Token Plan usage limit reached (2056)` at 08:30:30 ET; no artifact, no CSV, no baseline |
| Morning brief `daily-briefs/2026-11-05-pre-market.md` | **ABSENT** — same cause |
| Cron #15 `earnings/2026-11-05-reactions.md` | OK — published 08:22 ET; used only as the §5 cross-check anchor, never as a baseline |
| `cloud-prompts/_shared/premarket-refresh.md` (procedure) | OK — fetched from the GitHub contents API, SHA-256 `12680daf…` |
| Watchlist | not used by this refresh (the morning brief carries that section) |

**Decliner-screen truncation (disclosed).** The decliner screen returned 400 of 547 rows — the scanner's `range` cap of 400. The 147 omitted rows are the *least* negative decliners, so the top-10 table is complete and the headline decliner counts above are **lower bounds**, not exact. The gainer screen returned all 379 of 379 rows. Per the procedure's own rule, a thin screen is a valid result: what the pull has is published, and what it does not have is stated.

**Screen definition** (unchanged from cron #26, Step 2/2b of the brief skill): universe = US-listed common stock and ADRs on NASDAQ/NYSE/AMEX (`type` in `stock, dr`); Gate A = pre-market volume ≥ 100,000 shares, or market cap ≥ $200M with ≥ 10,000 pre-market shares; Gate B = market cap ≥ $100M, applied to the headline tables only. `%ADV` = pre-market volume ÷ 30-day average daily volume.

**Column contract at the pull.** `premarket_close` / `premarket_change` / `premarket_volume` are the 11-05 pre-market session (04:00–09:30 ET, final prints). `close` / `change` / `change_abs` / `volume` are the **live** 11-05 regular session at 10:10 ET, measured against the 11-04 regular close. `change` was verified against the spec's identity `close − close/(1 + change/100) == change_abs` on all 779 rows (779 ok, 0 bad), and the implied 11-04 close was independently confirmed against cron #15's file for every overlapping ticker.

_No catalysts in this file — it reports moves, not reasons._
