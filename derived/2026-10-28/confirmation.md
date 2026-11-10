# Confirmation — how many routines saw each name

**Source:** derived join over daily-screens/<date>/{tier-a,focus}.csv, ntrt/<date>.md, options-flow/<date>.md, earnings/<date>-{reminders,reactions}.md (no source file is modified) · **Built:** 2026-11-10 · **Covers:** 84 distinct name(s) across 5 routines; 200 on the 200-name master board · read-only

> **Read this before the table.**
>
> 1. **The five routines are not looking at the same thing, and that is the
>    finding.** The sweep describes the PREVIOUS session's tape (its metrics
>    are T+1), the gap brief describes THIS morning's pre-market, and the
>    flow screen describes the close. A name can appear in more than one
>    only if it persisted across that boundary.
> 2. **A count of one is not a weak signal; it is an unconfirmed one.** It means
>    no other routine saw the name, which is a fact worth having and not the
>    same thing as the routine being wrong.
> 3. **This artifact counts. It does not score.** No name is ranked, sized or
>    recommended, and no name is called a setup.

## What each routine published

| Routine | What it is | Names |
|---|---|---|
| `screen` | the 18:30 sweep - Tier-A and Focus | 12 |
| `gap_brief` | the 09:00 pre-open gap brief (ntrt) | 34 |
| `options_flow` | the 16:35 unusual-options-flow screen | 10 |
| `reminders` | the 06:00 earnings-reminder watchlist | 34 |
| `reactions` | the 08:00 earnings-reaction scanner | 0 |
| `master board` | the 200-name screen output the tiers are cut from | 200 |

The master board is not one of the five - it is the population the sweep's
tiers are cut from, and it is the baseline for how much overlap a
similarly-sized list would show by chance.

## Where the routines agree

| Pair | Shared names |
|---|---|
| gap_brief & reminders | 4 — APH, BSX, GEV, VRT |
| options_flow & reminders | 2 — GOOGL, MSFT |
| screen & gap_brief | 0 |
| screen & options_flow | 0 |
| screen & reminders | 0 |
| screen & reactions | 0 |
| gap_brief & options_flow | 0 |
| gap_brief & reactions | 0 |
| options_flow & reactions | 0 |
| reminders & reactions | 0 |

## How many routines saw each name

| Routines that saw the name | Names |
|---|---|
| 2 | 6 |
| 1 | 78 |

**6 of 84 name(s) were seen by two or more routines.** The rest were seen
by exactly one, and which one is in the table below.

## Names seen by more than one routine

| Ticker | Routines | On master board | Tier-A | Focus |
|---|---|---|---|---|
| APH | gap_brief, reminders | no | no | no |
| BSX | gap_brief, reminders | no | no | no |
| GEV | gap_brief, reminders | no | no | no |
| GOOGL | options_flow, reminders | no | no | no |
| MSFT | options_flow, reminders | no | no | no |
| VRT | gap_brief, reminders | no | no | no |

## Names seen by exactly one routine

| Ticker | Routine | On master board | Tier-A | Focus |
|---|---|---|---|---|
| CSGP | gap_brief | no | no | no |
| EAT | gap_brief | no | no | no |
| ENPH | gap_brief | no | no | no |
| ENS | gap_brief | no | no | no |
| EVR | gap_brief | no | no | no |
| EXTR | gap_brief | no | no | no |
| FLEX | gap_brief | no | no | no |
| FPS | gap_brief | no | no | no |
| GEHC | gap_brief | no | no | no |
| HOOD | gap_brief | no | no | no |
| IMSR | gap_brief | no | no | no |
| INTA | gap_brief | no | no | no |
| IP | gap_brief | no | no | no |
| LOGI | gap_brief | no | no | no |
| MIR | gap_brief | no | no | no |
| MOD | gap_brief | no | no | no |
| NVT | gap_brief | no | no | no |
| NXPI | gap_brief | no | no | no |
| PPG | gap_brief | no | no | no |
| RUN | gap_brief | yes | no | no |
| SEDG | gap_brief | yes | no | no |
| SKHY | gap_brief | no | no | no |
| STLA | gap_brief | yes | no | no |
| TER | gap_brief | no | no | no |
| UCTT | gap_brief | no | no | no |
| UHS | gap_brief | no | no | no |
| ULBI | gap_brief | no | no | no |
| ULCC | gap_brief | yes | no | no |
| WEN | gap_brief | no | no | no |
| WING | gap_brief | no | no | no |
| **CALL** | options_flow | no | no | no |
| AAPL | options_flow | no | no | no |
| AMZN | options_flow | no | no | no |
| GLD | options_flow | no | no | no |
| IWM | options_flow | no | no | no |
| MIXED | options_flow | no | no | no |
| NVDA | options_flow | yes | no | no |
| TLT | options_flow | no | no | no |
| ADP | reminders | no | no | no |
| AEM | reminders | no | no | no |
| AEP | reminders | no | no | no |
| ALGN | reminders | no | no | no |
| AMC | reminders | no | no | no |
| AON | reminders | no | no | no |
| BBVA | reminders | no | no | no |
| CMG | reminders | no | no | no |
| CP | reminders | no | no | no |
| CVNA | reminders | no | no | no |
| EBAY | reminders | no | no | no |
| EQIX | reminders | no | no | no |
| EQNR | reminders | no | no | no |
| ETSY | reminders | no | no | no |
| FDX | reminders | no | no | no |
| FTNT | reminders | no | no | no |
| GOOG | reminders | no | no | no |
| GSK | reminders | no | no | no |
| KLAC | reminders | no | no | no |
| NOW | reminders | no | no | no |
| ORLY | reminders | no | no | no |
| PSX | reminders | no | no | no |
| SAN | reminders | no | no | no |
| TEL | reminders | no | no | no |
| TMUS | reminders | no | no | no |
| UBS | reminders | no | no | no |
| URL | reminders | no | no | no |
| VFC | reminders | no | no | no |
| DXC | screen | yes | yes | yes |
| FIGS | screen | yes | no | yes |
| IOVA | screen | yes | yes | yes |
| KNSA | screen | yes | yes | yes |
| LQDA | screen | yes | no | yes |
| NTSK | screen | yes | yes | yes |
| PRME | screen | yes | yes | yes |
| QLYS | screen | yes | yes | yes |
| SDGR | screen | yes | no | yes |
| SMCI | screen | yes | no | yes |
| SOFI | screen | yes | yes | yes |
| TENB | screen | yes | yes | yes |

## Method and caveats

| Field | Value |
|---|---|
| Sources | 5 families, listed above |
| Ticker extraction | the first ticker-shaped cell of every markdown table row, and the ticker column of every CSV |
| Counts | per family, per name; a name can be in a family's set even if that family listed it in a table the reader would skip |

**What this does not say.** It does not say the routines are wrong, and it
does not say a name seen once is a better or worse setup. It says the repo
currently contains no artifact that would tell you either.

