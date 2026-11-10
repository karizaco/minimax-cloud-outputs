# Confirmation — how many routines saw each name

**Source:** derived join over daily-screens/<date>/{tier-a,focus}.csv, ntrt/<date>.md, options-flow/<date>.md, earnings/<date>-{reminders,reactions}.md (no source file is modified) · **Built:** 2026-11-10 · **Covers:** 57 distinct name(s) across 5 routines; 200 on the 200-name master board · read-only

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
| `screen` | the 18:30 sweep - Tier-A and Focus | 5 |
| `gap_brief` | the 09:00 pre-open gap brief (ntrt) | 37 |
| `options_flow` | the 16:35 unusual-options-flow screen | 10 |
| `reminders` | the 06:00 earnings-reminder watchlist | 5 |
| `reactions` | the 08:00 earnings-reaction scanner | 0 |
| `master board` | the 200-name screen output the tiers are cut from | 200 |

The master board is not one of the five - it is the population the sweep's
tiers are cut from, and it is the baseline for how much overlap a
similarly-sized list would show by chance.

## Where the routines agree

| Pair | Shared names |
|---|---|
| screen & gap_brief | 0 |
| screen & options_flow | 0 |
| screen & reminders | 0 |
| screen & reactions | 0 |
| gap_brief & options_flow | 0 |
| gap_brief & reminders | 0 |
| gap_brief & reactions | 0 |
| options_flow & reminders | 0 |
| options_flow & reactions | 0 |
| reminders & reactions | 0 |

## How many routines saw each name

| Routines that saw the name | Names |
|---|---|
| 1 | 57 |

**0 of 57 name(s) were seen by two or more routines.** The rest were seen
by exactly one, and which one is in the table below.

## Names seen by more than one routine

None on this date.

## Names seen by exactly one routine

| Ticker | Routine | On master board | Tier-A | Focus |
|---|---|---|---|---|
| **AAOI** | gap_brief | no | no | no |
| **AEIS** | gap_brief | no | no | no |
| **AXTI** | gap_brief | no | no | no |
| **BHVN** | gap_brief | no | no | no |
| **BMI** | gap_brief | no | no | no |
| **CNXC** | gap_brief | no | no | no |
| **COHR** | gap_brief | no | no | no |
| **COHU** | gap_brief | no | no | no |
| **CRS** | gap_brief | no | no | no |
| **CRWV** | gap_brief | no | no | no |
| **CSQR** | gap_brief | no | no | no |
| **DOWN** | gap_brief | no | no | no |
| **ENTG** | gap_brief | no | no | no |
| **FCFS** | gap_brief | no | no | no |
| **FORM** | gap_brief | no | no | no |
| **FPS** | gap_brief | no | no | no |
| **GGG** | gap_brief | no | no | no |
| **KSS** | gap_brief | no | no | no |
| **MRNA** | gap_brief | no | no | no |
| **MTRN** | gap_brief | no | no | no |
| **MTSI** | gap_brief | no | no | no |
| **MXL** | gap_brief | no | no | no |
| **NBIS** | gap_brief | no | no | no |
| **NOK** | gap_brief | no | no | no |
| **NVT** | gap_brief | no | no | no |
| **OII** | gap_brief | no | no | no |
| **OK** | gap_brief | no | no | no |
| **POOL** | gap_brief | no | no | no |
| **SEI** | gap_brief | no | no | no |
| **SIMO** | gap_brief | no | no | no |
| **SMCI** | gap_brief | no | no | no |
| **TTMI** | gap_brief | no | no | no |
| **UCTT** | gap_brief | no | no | no |
| **VIAV** | gap_brief | no | no | no |
| **VICR** | gap_brief | no | no | no |
| OK | gap_brief | no | no | no |
| RVOL | gap_brief | no | no | no |
| **CALL** | options_flow | no | no | no |
| **MIXED** | options_flow | no | no | no |
| AAPL | options_flow | yes | no | no |
| AMZN | options_flow | no | no | no |
| GLD | options_flow | no | no | no |
| GOOGL | options_flow | no | no | no |
| IWM | options_flow | no | no | no |
| MSFT | options_flow | no | no | no |
| NVDA | options_flow | no | no | no |
| TLT | options_flow | no | no | no |
| AXP | reminders | no | no | no |
| INFY | reminders | no | no | no |
| SAFRY | reminders | no | no | no |
| SLB | reminders | no | no | no |
| VLVLY | reminders | no | no | no |
| CD | screen | yes | no | yes |
| KOD | screen | yes | no | yes |
| MRNA | screen | yes | no | yes |
| TJGC | screen | yes | no | yes |
| XLAB | screen | yes | yes | yes |

## Method and caveats

| Field | Value |
|---|---|
| Sources | 5 families, listed above |
| Ticker extraction | the first ticker-shaped cell of every markdown table row, and the ticker column of every CSV |
| Counts | per family, per name; a name can be in a family's set even if that family listed it in a table the reader would skip |

**What this does not say.** It does not say the routines are wrong, and it
does not say a name seen once is a better or worse setup. It says the repo
currently contains no artifact that would tell you either.

