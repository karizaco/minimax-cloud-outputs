# Confirmation — how many routines saw each name

**Source:** derived join over daily-screens/<date>/{tier-a,focus}.csv, ntrt/<date>.md, options-flow/<date>.md, earnings/<date>-{reminders,reactions}.md (no source file is modified) · **Built:** 2026-11-11 · **Covers:** 113 distinct name(s) across 5 routines; 200 on the 200-name master board · read-only

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
| `screen` | the 18:30 sweep - Tier-A and Focus | 13 |
| `gap_brief` | the 09:00 pre-open gap brief (ntrt) | 58 |
| `options_flow` | the 16:35 unusual-options-flow screen | 10 |
| `reminders` | the 06:00 earnings-reminder watchlist | 32 |
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
| 1 | 113 |

**0 of 113 name(s) were seen by two or more routines.** The rest were seen
by exactly one, and which one is in the table below.

## Names seen by more than one routine

None on this date.

## Names seen by exactly one routine

| Ticker | Routine | On master board | Tier-A | Focus |
|---|---|---|---|---|
| **ABG** | gap_brief | no | no | no |
| **ALMR** | gap_brief | no | no | no |
| **AN** | gap_brief | no | no | no |
| **APLD** | gap_brief | no | no | no |
| **APPN** | gap_brief | no | no | no |
| **ASST** | gap_brief | no | no | no |
| **BE** | gap_brief | no | no | no |
| **CDLR** | gap_brief | no | no | no |
| **CELH** | gap_brief | no | no | no |
| **CIFR** | gap_brief | no | no | no |
| **CLMT** | gap_brief | no | no | no |
| **CMG** | gap_brief | no | no | no |
| **CRL** | gap_brief | no | no | no |
| **CRWV** | gap_brief | no | no | no |
| **DOWN** | gap_brief | no | no | no |
| **DXCM** | gap_brief | no | no | no |
| **DY** | gap_brief | no | no | no |
| **ECHO** | gap_brief | no | no | no |
| **EQPT** | gap_brief | no | no | no |
| **EXPE** | gap_brief | no | no | no |
| **FLY** | gap_brief | no | no | no |
| **FRPT** | gap_brief | no | no | no |
| **GLXY** | gap_brief | no | no | no |
| **GPI** | gap_brief | no | no | no |
| **GRDN** | gap_brief | no | no | no |
| **HSAI** | gap_brief | no | no | no |
| **INFQ** | gap_brief | no | no | no |
| **INOD** | gap_brief | no | no | no |
| **IREN** | gap_brief | no | no | no |
| **KOD** | gap_brief | no | no | no |
| **KYIV** | gap_brief | no | no | no |
| **LAD** | gap_brief | no | no | no |
| **LIFE** | gap_brief | no | no | no |
| **MANE** | gap_brief | no | no | no |
| **MHO** | gap_brief | no | no | no |
| **MSTR** | gap_brief | no | no | no |
| **NBIS** | gap_brief | no | no | no |
| **NFLX** | gap_brief | no | no | no |
| **NHC** | gap_brief | no | no | no |
| **NTSK** | gap_brief | no | no | no |
| **OFG** | gap_brief | no | no | no |
| **OKTA** | gap_brief | no | no | no |
| **PARTIAL** | gap_brief | no | no | no |
| **RCUS** | gap_brief | no | no | no |
| **SEI** | gap_brief | no | no | no |
| **SKYD** | gap_brief | no | no | no |
| **SMCI** | gap_brief | no | no | no |
| **SPCX** | gap_brief | no | no | no |
| **TAL** | gap_brief | no | no | no |
| **TLX** | gap_brief | no | no | no |
| **WFRD** | gap_brief | no | no | no |
| **WING** | gap_brief | no | no | no |
| **WULF** | gap_brief | no | no | no |
| **XMTR** | gap_brief | no | no | no |
| **XPEV** | gap_brief | no | no | no |
| **ZS** | gap_brief | no | no | no |
| OK | gap_brief | no | no | no |
| RVOL | gap_brief | no | no | no |
| **CALL** | options_flow | no | no | no |
| **MIXED** | options_flow | no | no | no |
| AAPL | options_flow | yes | no | no |
| AMZN | options_flow | no | no | no |
| GLD | options_flow | no | no | no |
| GOOGL | options_flow | no | no | no |
| IWM | options_flow | no | no | no |
| MSFT | options_flow | yes | no | no |
| NVDA | options_flow | no | no | no |
| TLT | options_flow | no | no | no |
| ALLE | reminders | no | no | no |
| ARGX | reminders | no | no | no |
| BCS | reminders | no | no | no |
| BE | reminders | yes | no | no |
| BX | reminders | no | no | no |
| CBRE | reminders | no | no | no |
| CMCSA | reminders | no | no | no |
| DECK | reminders | no | no | no |
| DGX | reminders | no | no | no |
| DOV | reminders | no | no | no |
| DOW | reminders | no | no | no |
| FIX | reminders | no | no | no |
| HBAN | reminders | no | no | no |
| HON | reminders | no | no | no |
| LMT | reminders | no | no | no |
| NDAQ | reminders | no | no | no |
| NEM | reminders | no | no | no |
| NOK | reminders | no | no | no |
| NSC | reminders | no | no | no |
| NVR | reminders | no | no | no |
| OMC | reminders | no | no | no |
| PCG | reminders | no | no | no |
| PG | reminders | no | no | no |
| PHM | reminders | no | no | no |
| ROP | reminders | no | no | no |
| SNA | reminders | no | no | no |
| SPOT | reminders | no | no | no |
| TSCO | reminders | no | no | no |
| UNP | reminders | no | no | no |
| VLO | reminders | no | no | no |
| VRSN | reminders | no | no | no |
| WDC | reminders | no | no | no |
| APPN | screen | yes | no | yes |
| BMBL | screen | yes | no | yes |
| BRZE | screen | yes | no | yes |
| CD | screen | yes | no | yes |
| HAS | screen | yes | no | yes |
| IOVA | screen | yes | no | yes |
| KOD | screen | yes | no | yes |
| LIFE | screen | yes | yes | yes |
| MEDP | screen | yes | no | yes |
| MRNA | screen | yes | no | yes |
| RCEL | screen | yes | yes | yes |
| TEAM | screen | yes | no | yes |
| TJGC | screen | yes | no | yes |

## Method and caveats

| Field | Value |
|---|---|
| Sources | 5 families, listed above |
| Ticker extraction | the first ticker-shaped cell of every markdown table row, and the ticker column of every CSV |
| Counts | per family, per name; a name can be in a family's set even if that family listed it in a table the reader would skip |

**What this does not say.** It does not say the routines are wrong, and it
does not say a name seen once is a better or worse setup. It says the repo
currently contains no artifact that would tell you either.

