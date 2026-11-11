# Confirmation — how many routines saw each name

**Source:** derived join over daily-screens/<date>/{tier-a,focus}.csv, ntrt/<date>.md, options-flow/<date>.md, earnings/<date>-{reminders,reactions}.md (no source file is modified) · **Built:** 2026-11-11 · **Covers:** 102 distinct name(s) across 5 routines; 200 on the 200-name master board · read-only

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
| `gap_brief` | the 09:00 pre-open gap brief (ntrt) | 41 |
| `options_flow` | the 16:35 unusual-options-flow screen | 10 |
| `reminders` | the 06:00 earnings-reminder watchlist | 39 |
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
| 1 | 102 |

**0 of 102 name(s) were seen by two or more routines.** The rest were seen
by exactly one, and which one is in the table below.

## Names seen by more than one routine

None on this date.

## Names seen by exactly one routine

| Ticker | Routine | On master board | Tier-A | Focus |
|---|---|---|---|---|
| **AAIGF** | gap_brief | no | no | no |
| **ACHV** | gap_brief | no | no | no |
| **ARTV** | gap_brief | no | no | no |
| **ATEYY** | gap_brief | no | no | no |
| **BESVF** | gap_brief | no | no | no |
| **BRAI** | gap_brief | no | no | no |
| **BRUN** | gap_brief | no | no | no |
| **CLS** | gap_brief | no | no | no |
| **CVLT** | gap_brief | no | no | no |
| **EEFT** | gap_brief | no | no | no |
| **ELVR** | gap_brief | no | no | no |
| **ETRA** | gap_brief | no | no | no |
| **FER** | gap_brief | no | no | no |
| **GMTL** | gap_brief | no | no | no |
| **HRI** | gap_brief | no | no | no |
| **HSBC** | gap_brief | no | no | no |
| **HWKN** | gap_brief | no | no | no |
| **IMSR** | gap_brief | no | no | no |
| **INIO** | gap_brief | no | no | no |
| **INOD** | gap_brief | no | no | no |
| **ISD** | gap_brief | no | no | no |
| **ITJTY** | gap_brief | no | no | no |
| **IVBXF** | gap_brief | no | no | no |
| **JBLU** | gap_brief | no | no | no |
| **KNSA** | gap_brief | no | no | no |
| **MFIC** | gap_brief | no | no | no |
| **NBTX** | gap_brief | no | no | no |
| **NEWP** | gap_brief | no | no | no |
| **OSCUF** | gap_brief | no | no | no |
| **PII** | gap_brief | no | no | no |
| **SAIQ** | gap_brief | no | no | no |
| **SOFI** | gap_brief | no | no | no |
| **SVRE** | gap_brief | no | no | no |
| **SXC** | gap_brief | no | no | no |
| **VGM** | gap_brief | no | no | no |
| **VLKPF** | gap_brief | no | no | no |
| **WHR** | gap_brief | no | no | no |
| **WSO** | gap_brief | no | no | no |
| **XYL** | gap_brief | no | no | no |
| **YDES** | gap_brief | no | no | no |
| QC | gap_brief | no | no | no |
| **CALL** | options_flow | no | no | no |
| AAPL | options_flow | yes | no | no |
| AMZN | options_flow | yes | no | no |
| GLD | options_flow | no | no | no |
| GOOGL | options_flow | no | no | no |
| IWM | options_flow | no | no | no |
| MIXED | options_flow | no | no | no |
| MSFT | options_flow | no | no | no |
| NVDA | options_flow | yes | no | no |
| TLT | options_flow | no | no | no |
| ACGL | reminders | no | no | no |
| AMC | reminders | no | no | no |
| AMT | reminders | no | no | no |
| BA | reminders | no | no | no |
| BKNG | reminders | no | no | no |
| BKR | reminders | no | no | no |
| CNC | reminders | no | no | no |
| DB | reminders | no | no | no |
| ECL | reminders | no | no | no |
| FCX | reminders | no | no | no |
| GLW | reminders | no | no | no |
| GSK | reminders | no | no | no |
| HCA | reminders | no | no | no |
| HLT | reminders | no | no | no |
| HOOD | reminders | no | no | no |
| HSBC | reminders | no | no | no |
| IQV | reminders | no | no | no |
| ITW | reminders | no | no | no |
| JCI | reminders | yes | no | no |
| KO | reminders | no | no | no |
| NEE | reminders | no | no | no |
| NVS | reminders | no | no | no |
| NXPI | reminders | yes | no | no |
| OKE | reminders | no | no | no |
| PCAR | reminders | no | no | no |
| PYPL | reminders | no | no | no |
| RCL | reminders | no | no | no |
| SAN | reminders | no | no | no |
| SHW | reminders | no | no | no |
| SKHY | reminders | no | no | no |
| SPGI | reminders | no | no | no |
| STX | reminders | yes | no | no |
| SYY | reminders | no | no | no |
| TER | reminders | no | no | no |
| UNH | reminders | no | no | no |
| UPS | reminders | no | no | no |
| URL | reminders | no | no | no |
| VTR | reminders | no | no | no |
| WM | reminders | no | no | no |
| ALAB | screen | yes | no | yes |
| CRML | screen | yes | yes | yes |
| CYPH | screen | yes | yes | yes |
| GLXY | screen | yes | yes | yes |
| HRI | screen | yes | yes | yes |
| LUNR | screen | yes | no | yes |
| MXL | screen | yes | yes | yes |
| ON | screen | yes | yes | yes |
| OUST | screen | yes | no | yes |
| RDW | screen | yes | yes | yes |
| RKLB | screen | yes | yes | yes |
| SDGR | screen | yes | no | yes |

## Method and caveats

| Field | Value |
|---|---|
| Sources | 5 families, listed above |
| Ticker extraction | the first ticker-shaped cell of every markdown table row, and the ticker column of every CSV |
| Counts | per family, per name; a name can be in a family's set even if that family listed it in a table the reader would skip |

**What this does not say.** It does not say the routines are wrong, and it
does not say a name seen once is a better or worse setup. It says the repo
currently contains no artifact that would tell you either.

