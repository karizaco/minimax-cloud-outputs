# Confirmation — how many routines saw each name

**Source:** derived join over daily-screens/<date>/{tier-a,focus}.csv, ntrt/<date>.md, options-flow/<date>.md, earnings/<date>-{reminders,reactions}.md (no source file is modified) · **Built:** 2026-11-10 · **Covers:** 93 distinct name(s) across 5 routines; 409 on the 200-name master board · read-only

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
| `screen` | the 18:30 sweep - Tier-A and Focus | 20 |
| `gap_brief` | the 09:00 pre-open gap brief (ntrt) | 42 |
| `options_flow` | the 16:35 unusual-options-flow screen | 12 |
| `reminders` | the 06:00 earnings-reminder watchlist | 20 |
| `reactions` | the 08:00 earnings-reaction scanner | 0 |
| `master board` | the 200-name screen output the tiers are cut from | 409 |

The master board is not one of the five - it is the population the sweep's
tiers are cut from, and it is the baseline for how much overlap a
similarly-sized list would show by chance.

## Where the routines agree

| Pair | Shared names |
|---|---|
| screen & gap_brief | 1 — CDNA |
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
| 2 | 1 |
| 1 | 92 |

**1 of 93 name(s) were seen by two or more routines.** The rest were seen
by exactly one, and which one is in the table below.

## Names seen by more than one routine

| Ticker | Routines | On master board | Tier-A | Focus |
|---|---|---|---|---|
| CDNA | screen, gap_brief | yes | yes | no |

## Names seen by exactly one routine

| Ticker | Routine | On master board | Tier-A | Focus |
|---|---|---|---|---|
| ABR | gap_brief | no | no | no |
| ACCO | gap_brief | yes | no | no |
| AEHR | gap_brief | no | no | no |
| AGIO | gap_brief | no | no | no |
| AMD | gap_brief | yes | no | no |
| ARI | gap_brief | no | no | no |
| ASUR | gap_brief | no | no | no |
| ATEC | gap_brief | no | no | no |
| BBUC | gap_brief | no | no | no |
| BFAM | gap_brief | no | no | no |
| BRUN | gap_brief | no | no | no |
| CACC | gap_brief | no | no | no |
| CPRI | gap_brief | yes | no | no |
| CVEO | gap_brief | yes | no | no |
| CYPH | gap_brief | no | no | no |
| DELL | gap_brief | yes | no | no |
| DVA | gap_brief | no | no | no |
| FMC | gap_brief | no | no | no |
| GDYN | gap_brief | yes | no | no |
| GRRR | gap_brief | no | no | no |
| HPQ | gap_brief | no | no | no |
| HRTG | gap_brief | no | no | no |
| IAM | gap_brief | no | no | no |
| ICHR | gap_brief | no | no | no |
| ILMN | gap_brief | yes | no | no |
| INTC | gap_brief | yes | no | no |
| MXL | gap_brief | no | no | no |
| NPB | gap_brief | no | no | no |
| NPKI | gap_brief | no | no | no |
| OABI | gap_brief | no | no | no |
| ONTO | gap_brief | no | no | no |
| OSPN | gap_brief | yes | no | no |
| OVID | gap_brief | no | no | no |
| QSI | gap_brief | no | no | no |
| RBLX | gap_brief | no | no | no |
| RDDT | gap_brief | no | no | no |
| RMNI | gap_brief | no | no | no |
| SENS | gap_brief | no | no | no |
| STRZ | gap_brief | no | no | no |
| TWLO | gap_brief | yes | no | no |
| UCTT | gap_brief | yes | no | no |
| **MIXED** | options_flow | no | no | no |
| AAPL | options_flow | yes | no | no |
| AMZN | options_flow | yes | no | no |
| CALL | options_flow | no | no | no |
| GLD | options_flow | no | no | no |
| GOOGL | options_flow | yes | no | no |
| IWM | options_flow | no | no | no |
| MIXED | options_flow | no | no | no |
| MSFT | options_flow | yes | no | no |
| NVDA | options_flow | yes | no | no |
| TLT | options_flow | no | no | no |
| VIX | options_flow | no | no | no |
| ABBV | reminders | no | no | no |
| AZN | reminders | no | no | no |
| BMO | reminders | no | no | no |
| BP | reminders | yes | no | no |
| CBOE | reminders | no | no | no |
| CHD | reminders | no | no | no |
| CL | reminders | no | no | no |
| CNI | reminders | no | no | no |
| CVX | reminders | yes | no | no |
| EXC | reminders | no | no | no |
| FRT | reminders | no | no | no |
| GD | reminders | no | no | no |
| IITSF | reminders | no | no | no |
| IMO | reminders | yes | no | no |
| KVUE | reminders | no | no | no |
| LYB | reminders | no | no | no |
| NWG | reminders | no | no | no |
| REGN | reminders | yes | no | no |
| SNY | reminders | no | no | no |
| XOM | reminders | yes | no | no |
| ADT | screen | yes | no | yes |
| BHC | screen | yes | no | yes |
| CROX | screen | yes | no | yes |
| CVNA | screen | yes | no | yes |
| DFIN | screen | yes | no | yes |
| FIGS | screen | yes | yes | no |
| FTAI | screen | yes | yes | yes |
| GEN | screen | yes | no | yes |
| GKOS | screen | yes | no | yes |
| GRAL | screen | yes | yes | no |
| HTFL | screen | yes | yes | no |
| INSM | screen | yes | no | yes |
| IOVA | screen | yes | yes | no |
| KOD | screen | yes | yes | no |
| MAX | screen | yes | no | yes |
| MRNA | screen | yes | yes | no |
| P | screen | yes | yes | no |
| PRCH | screen | yes | no | yes |
| PURR | screen | yes | yes | yes |

## Method and caveats

| Field | Value |
|---|---|
| Sources | 5 families, listed above |
| Ticker extraction | the first ticker-shaped cell of every markdown table row, and the ticker column of every CSV |
| Counts | per family, per name; a name can be in a family's set even if that family listed it in a table the reader would skip |

**What this does not say.** It does not say the routines are wrong, and it
does not say a name seen once is a better or worse setup. It says the repo
currently contains no artifact that would tell you either.

