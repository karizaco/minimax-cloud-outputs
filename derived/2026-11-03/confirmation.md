# Confirmation — how many routines saw each name

**Source:** derived join over daily-screens/<date>/{tier-a,focus}.csv, ntrt/<date>.md, options-flow/<date>.md, earnings/<date>-{reminders,reactions}.md (no source file is modified) · **Built:** 2026-11-10 · **Covers:** 156 distinct name(s) across 5 routines; 200 on the 200-name master board · read-only

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
| `gap_brief` | the 09:00 pre-open gap brief (ntrt) | 37 |
| `options_flow` | the 16:35 unusual-options-flow screen | 10 |
| `reminders` | the 06:00 earnings-reminder watchlist | 51 |
| `reactions` | the 08:00 earnings-reaction scanner | 54 |
| `master board` | the 200-name screen output the tiers are cut from | 200 |

The master board is not one of the five - it is the population the sweep's
tiers are cut from, and it is the baseline for how much overlap a
similarly-sized list would show by chance.

## Where the routines agree

| Pair | Shared names |
|---|---|
| gap_brief & reminders | 4 — FISV, RACE, SHOP, ZBRA |
| reminders & reactions | 3 — LITE, MPC, RACE |
| gap_brief & reactions | 2 — AXTI, RACE |
| screen & gap_brief | 0 |
| screen & options_flow | 0 |
| screen & reminders | 0 |
| screen & reactions | 0 |
| gap_brief & options_flow | 0 |
| options_flow & reminders | 0 |
| options_flow & reactions | 0 |

## How many routines saw each name

| Routines that saw the name | Names |
|---|---|
| 3 | 1 |
| 2 | 6 |
| 1 | 149 |

**7 of 156 name(s) were seen by two or more routines.** The rest were seen
by exactly one, and which one is in the table below.

## Names seen by more than one routine

| Ticker | Routines | On master board | Tier-A | Focus |
|---|---|---|---|---|
| RACE | gap_brief, reminders, reactions | no | no | no |
| AXTI | gap_brief, reactions | yes | no | no |
| FISV | gap_brief, reminders | yes | no | no |
| LITE | reminders, reactions | yes | no | no |
| MPC | reminders, reactions | no | no | no |
| SHOP | gap_brief, reminders | no | no | no |
| ZBRA | gap_brief, reminders | no | no | no |

## Names seen by exactly one routine

| Ticker | Routine | On master board | Tier-A | Focus |
|---|---|---|---|---|
| **AAPL** | gap_brief | no | no | no |
| **GRAB** | gap_brief | no | no | no |
| **PLTR** | gap_brief | no | no | no |
| **SHOP** | gap_brief | no | no | no |
| ADEA | gap_brief | no | no | no |
| AEHR | gap_brief | yes | no | no |
| AEIS | gap_brief | no | no | no |
| BLZE | gap_brief | no | no | no |
| BNC | gap_brief | no | no | no |
| BRAI | gap_brief | no | no | no |
| BRCC | gap_brief | no | no | no |
| BVS | gap_brief | no | no | no |
| CERS | gap_brief | no | no | no |
| CMCO | gap_brief | no | no | no |
| CWH | gap_brief | no | no | no |
| DRVN | gap_brief | no | no | no |
| DT | gap_brief | no | no | no |
| EBS | gap_brief | no | no | no |
| GPRO | gap_brief | no | no | no |
| GRAB | gap_brief | no | no | no |
| HLIT | gap_brief | no | no | no |
| IBTA | gap_brief | no | no | no |
| INGM | gap_brief | no | no | no |
| KMDA | gap_brief | no | no | no |
| LIFE | gap_brief | no | no | no |
| LSCC | gap_brief | no | no | no |
| MDGL | gap_brief | no | no | no |
| POET | gap_brief | no | no | no |
| SNDK | gap_brief | yes | no | no |
| STVN | gap_brief | no | no | no |
| VITL | gap_brief | no | no | no |
| XMAX | gap_brief | no | no | no |
| **CALL** | options_flow | no | no | no |
| **MIXED** | options_flow | no | no | no |
| AAPL | options_flow | no | no | no |
| AMZN | options_flow | no | no | no |
| GLD | options_flow | no | no | no |
| GOOGL | options_flow | no | no | no |
| IWM | options_flow | no | no | no |
| MSFT | options_flow | no | no | no |
| NVDA | options_flow | no | no | no |
| TLT | options_flow | no | no | no |
| ACAD | reactions | no | no | no |
| ACP | reactions | no | no | no |
| AESI | reactions | no | no | no |
| ALO | reactions | no | no | no |
| APLD | reactions | yes | no | no |
| AVGO | reactions | no | no | no |
| BAYN | reactions | no | no | no |
| BCHN | reactions | no | no | no |
| BIM | reactions | no | no | no |
| BJY | reactions | no | no | no |
| BMAG | reactions | no | no | no |
| BPT | reactions | no | no | no |
| CRM | reactions | no | no | no |
| DAR | reactions | no | no | no |
| DHI | reactions | no | no | no |
| DRX | reactions | no | no | no |
| DVYSR | reactions | no | no | no |
| ECO | reactions | no | no | no |
| EU | reactions | no | no | no |
| EVD | reactions | no | no | no |
| FRO | reactions | no | no | no |
| GENO | reactions | no | no | no |
| GLW | reactions | no | no | no |
| HLMN | reactions | no | no | no |
| HMC | reactions | no | no | no |
| HVN | reactions | no | no | no |
| ICE | reactions | no | no | no |
| JDW | reactions | no | no | no |
| KRYS | reactions | no | no | no |
| MULTI | reactions | no | no | no |
| NCOD | reactions | no | no | no |
| NEM | reactions | no | no | no |
| NHC | reactions | no | no | no |
| NORCO | reactions | no | no | no |
| OMXSTO | reactions | no | no | no |
| PGR | reactions | no | no | no |
| PHIA | reactions | no | no | no |
| PPGN | reactions | no | no | no |
| PURR | reactions | yes | no | no |
| QAN | reactions | no | no | no |
| RIOT | reactions | yes | no | no |
| SILEX | reactions | no | no | no |
| TMV | reactions | no | no | no |
| ULCC | reactions | no | no | no |
| UPWK | reactions | yes | no | no |
| VER | reactions | no | no | no |
| VMM | reactions | no | no | no |
| WBT | reactions | no | no | no |
| WGS | reactions | no | no | no |
| ZAL | reactions | no | no | no |
| ADM | reminders | no | no | no |
| AES | reminders | no | no | no |
| AIG | reminders | no | no | no |
| AIZ | reminders | no | no | no |
| AMD | reminders | no | no | no |
| AME | reminders | no | no | no |
| AMGN | reminders | no | no | no |
| ANET | reminders | no | no | no |
| APO | reminders | no | no | no |
| APTV | reminders | no | no | no |
| BALL | reminders | no | no | no |
| BKNG | reminders | no | no | no |
| BR | reminders | no | no | no |
| DD | reminders | no | no | no |
| EA | reminders | no | no | no |
| ET | reminders | no | no | no |
| ETN | reminders | no | no | no |
| EXPD | reminders | no | no | no |
| FIS | reminders | no | no | no |
| GPN | reminders | no | no | no |
| HSIC | reminders | no | no | no |
| IFF | reminders | no | no | no |
| IITSF | reminders | no | no | no |
| IT | reminders | no | no | no |
| ITUB | reminders | no | no | no |
| JKHY | reminders | no | no | no |
| KDP | reminders | yes | no | no |
| LDOS | reminders | no | no | no |
| LYV | reminders | no | no | no |
| MOS | reminders | no | no | no |
| MPLX | reminders | no | no | no |
| PFE | reminders | no | no | no |
| PNW | reminders | no | no | no |
| PRU | reminders | no | no | no |
| RVTY | reminders | no | no | no |
| SMCI | reminders | yes | no | no |
| SU | reminders | no | no | no |
| SWKS | reminders | no | no | no |
| SYY | reminders | no | no | no |
| TECH | reminders | no | no | no |
| TEVA | reminders | yes | no | no |
| TRI | reminders | no | no | no |
| WAT | reminders | no | no | no |
| XYZ | reminders | no | no | no |
| YUM | reminders | no | no | no |
| CAI | screen | yes | yes | yes |
| CLF | screen | yes | yes | yes |
| CVNA | screen | yes | yes | yes |
| FIGS | screen | yes | yes | yes |
| FTAI | screen | yes | yes | yes |
| HTFL | screen | yes | no | yes |
| KOD | screen | yes | no | yes |
| KVYO | screen | yes | yes | yes |
| MRNA | screen | yes | no | yes |
| TEM | screen | yes | yes | yes |
| VSEC | screen | yes | no | yes |
| WING | screen | yes | yes | yes |

## Method and caveats

| Field | Value |
|---|---|
| Sources | 5 families, listed above |
| Ticker extraction | the first ticker-shaped cell of every markdown table row, and the ticker column of every CSV |
| Counts | per family, per name; a name can be in a family's set even if that family listed it in a table the reader would skip |

**What this does not say.** It does not say the routines are wrong, and it
does not say a name seen once is a better or worse setup. It says the repo
currently contains no artifact that would tell you either.

