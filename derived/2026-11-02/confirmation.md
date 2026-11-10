# Confirmation — how many routines saw each name

**Source:** derived join over daily-screens/<date>/{tier-a,focus}.csv, ntrt/<date>.md, options-flow/<date>.md, earnings/<date>-{reminders,reactions}.md (no source file is modified) · **Built:** 2026-11-10 · **Covers:** 219 distinct name(s) across 5 routines; 200 on the 200-name master board · read-only

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
| `gap_brief` | the 09:00 pre-open gap brief (ntrt) | 73 |
| `options_flow` | the 16:35 unusual-options-flow screen | 11 |
| `reminders` | the 06:00 earnings-reminder watchlist | 19 |
| `reactions` | the 08:00 earnings-reaction scanner | 118 |
| `master board` | the 200-name screen output the tiers are cut from | 200 |

The master board is not one of the five - it is the population the sweep's
tiers are cut from, and it is the baseline for how much overlap a
similarly-sized list would show by chance.

## Where the routines agree

| Pair | Shared names |
|---|---|
| gap_brief & reactions | 8 — MAR, NANO, PARR, PGEN, RIVN, RSI, SECZ, TSEM |
| gap_brief & options_flow | 3 — GLD, IWM, TLT |
| gap_brief & reminders | 2 — IDXX, MAR |
| options_flow & reminders | 1 — AAPL |
| reminders & reactions | 1 — MAR |
| screen & gap_brief | 0 |
| screen & options_flow | 0 |
| screen & reminders | 0 |
| screen & reactions | 0 |
| options_flow & reactions | 0 |

## How many routines saw each name

| Routines that saw the name | Names |
|---|---|
| 3 | 1 |
| 2 | 12 |
| 1 | 206 |

**13 of 219 name(s) were seen by two or more routines.** The rest were seen
by exactly one, and which one is in the table below.

## Names seen by more than one routine

| Ticker | Routines | On master board | Tier-A | Focus |
|---|---|---|---|---|
| MAR | gap_brief, reminders, reactions | no | no | no |
| AAPL | options_flow, reminders | yes | no | no |
| GLD | gap_brief, options_flow | no | no | no |
| IDXX | gap_brief, reminders | no | no | no |
| IWM | gap_brief, options_flow | no | no | no |
| NANO | gap_brief, reactions | no | no | no |
| PARR | gap_brief, reactions | no | no | no |
| PGEN | gap_brief, reactions | yes | no | no |
| RIVN | gap_brief, reactions | yes | no | no |
| RSI | gap_brief, reactions | no | no | no |
| SECZ | gap_brief, reactions | no | no | no |
| TLT | gap_brief, options_flow | no | no | no |
| TSEM | gap_brief, reactions | no | no | no |

## Names seen by exactly one routine

| Ticker | Routine | On master board | Tier-A | Focus |
|---|---|---|---|---|
| **BRAI** | gap_brief | no | no | no |
| **CHKP** | gap_brief | no | no | no |
| **DRUG** | gap_brief | no | no | no |
| **EVGO** | gap_brief | no | no | no |
| **FLNC** | gap_brief | no | no | no |
| **IDXX** | gap_brief | no | no | no |
| **KOS** | gap_brief | no | no | no |
| **LITE** | gap_brief | no | no | no |
| **NSSC** | gap_brief | no | no | no |
| **OFRM** | gap_brief | no | no | no |
| **PERI** | gap_brief | no | no | no |
| **PGEN** | gap_brief | no | no | no |
| **QURE** | gap_brief | no | no | no |
| **TATT** | gap_brief | no | no | no |
| BRAI | gap_brief | no | no | no |
| CAPR | gap_brief | no | no | no |
| CHKP | gap_brief | no | no | no |
| CLPT | gap_brief | no | no | no |
| CNA | gap_brief | no | no | no |
| DIA | gap_brief | no | no | no |
| DMLP | gap_brief | no | no | no |
| DRUG | gap_brief | no | no | no |
| ECHO | gap_brief | no | no | no |
| EDIT | gap_brief | no | no | no |
| EGY | gap_brief | no | no | no |
| EQH | gap_brief | no | no | no |
| EVER | gap_brief | no | no | no |
| EVGO | gap_brief | no | no | no |
| FLNC | gap_brief | no | no | no |
| GBC | gap_brief | no | no | no |
| GTN.A | gap_brief | no | no | no |
| KGEI | gap_brief | no | no | no |
| KOS | gap_brief | no | no | no |
| KRYS | gap_brief | no | no | no |
| KWY | gap_brief | no | no | no |
| LITE | gap_brief | no | no | no |
| MFIN | gap_brief | no | no | no |
| MYGN | gap_brief | no | no | no |
| NEWP | gap_brief | no | no | no |
| NSSC | gap_brief | no | no | no |
| NX | gap_brief | no | no | no |
| OBE | gap_brief | no | no | no |
| OFRM | gap_brief | no | no | no |
| OPTX | gap_brief | no | no | no |
| ORCL | gap_brief | no | no | no |
| PERI | gap_brief | no | no | no |
| PSQL | gap_brief | no | no | no |
| QQQ | gap_brief | no | no | no |
| QURE | gap_brief | no | no | no |
| RZAI | gap_brief | no | no | no |
| SKE | gap_brief | no | no | no |
| SMH | gap_brief | no | no | no |
| SPY | gap_brief | no | no | no |
| TATT | gap_brief | no | no | no |
| THM | gap_brief | no | no | no |
| TROO | gap_brief | no | no | no |
| TSHA | gap_brief | no | no | no |
| USO | gap_brief | no | no | no |
| WTI | gap_brief | no | no | no |
| XLE | gap_brief | no | no | no |
| XLK | gap_brief | no | no | no |
| **CALL** | options_flow | no | no | no |
| **PUT** | options_flow | no | no | no |
| AMZN | options_flow | yes | no | no |
| GOOGL | options_flow | yes | no | no |
| MSFT | options_flow | yes | no | no |
| NVDA | options_flow | no | no | no |
| PUT | options_flow | no | no | no |
| AAOI | reactions | no | no | no |
| AAON | reactions | no | no | no |
| ABSI | reactions | no | no | no |
| ACMR | reactions | no | no | no |
| AEHR | reactions | no | no | no |
| AEIS | reactions | no | no | no |
| AGIO | reactions | no | no | no |
| ALHC | reactions | no | no | no |
| ALO | reactions | no | no | no |
| APLD | reactions | no | no | no |
| APP | reactions | no | no | no |
| AQUA | reactions | no | no | no |
| ARIS | reactions | no | no | no |
| ATEC | reactions | no | no | no |
| AUGO | reactions | no | no | no |
| AXTI | reactions | no | no | no |
| BMAG | reactions | no | no | no |
| BOQCD | reactions | no | no | no |
| BTDR | reactions | no | no | no |
| BUUU | reactions | no | no | no |
| CAMT | reactions | no | no | no |
| CBRAIN | reactions | no | no | no |
| CHRN | reactions | no | no | no |
| CIRSA | reactions | no | no | no |
| CMBN | reactions | no | no | no |
| COHR | reactions | no | no | no |
| CORZ | reactions | no | no | no |
| CRDO | reactions | no | no | no |
| CRML | reactions | no | no | no |
| CRWD | reactions | no | no | no |
| CRWV | reactions | yes | no | no |
| DDOG | reactions | no | no | no |
| DOCN | reactions | no | no | no |
| ELTEL | reactions | no | no | no |
| ERO | reactions | no | no | no |
| FAG | reactions | no | no | no |
| FDXF | reactions | yes | no | no |
| FGP | reactions | no | no | no |
| FIGR | reactions | no | no | no |
| FORM | reactions | no | no | no |
| FRVO | reactions | no | no | no |
| GDYN | reactions | yes | no | no |
| GLW | reactions | no | no | no |
| GLXY | reactions | no | no | no |
| GPW | reactions | no | no | no |
| GRAL | reactions | yes | no | no |
| HBM | reactions | no | no | no |
| HLI | reactions | no | no | no |
| HUNT | reactions | no | no | no |
| IAG | reactions | no | no | no |
| ICHR | reactions | no | no | no |
| INIO | reactions | no | no | no |
| JSW | reactions | no | no | no |
| KLIC | reactions | no | no | no |
| KNOW | reactions | no | no | no |
| LNG | reactions | no | no | no |
| LOOMIS | reactions | no | no | no |
| LSCC | reactions | no | no | no |
| MED | reactions | no | no | no |
| NBIS | reactions | no | no | no |
| NELLY | reactions | no | no | no |
| NEXA | reactions | no | no | no |
| NSKOG | reactions | no | no | no |
| NST | reactions | no | no | no |
| NTSK | reactions | yes | no | no |
| NVTS | reactions | no | no | no |
| OMXSTO | reactions | no | no | no |
| ONDS | reactions | yes | no | no |
| ONTO | reactions | no | no | no |
| OUST | reactions | no | no | no |
| PBF | reactions | no | no | no |
| PENG | reactions | no | no | no |
| PLPC | reactions | no | no | no |
| POWI | reactions | no | no | no |
| POWL | reactions | no | no | no |
| PPTA | reactions | no | no | no |
| PSX | reactions | yes | no | no |
| PTEN | reactions | no | no | no |
| QNT | reactions | no | no | no |
| RAPP | reactions | no | no | no |
| RIG | reactions | yes | no | no |
| RIOT | reactions | no | no | no |
| RMBS | reactions | no | no | no |
| RYA | reactions | no | no | no |
| SBET | reactions | no | no | no |
| SITM | reactions | no | no | no |
| SMTC | reactions | no | no | no |
| SNT | reactions | no | no | no |
| STDN | reactions | no | no | no |
| STX | reactions | no | no | no |
| SU | reactions | no | no | no |
| SVIK | reactions | no | no | no |
| SZG | reactions | no | no | no |
| TBBK | reactions | no | no | no |
| TEM | reactions | yes | no | no |
| TMUS | reactions | yes | no | no |
| TOR | reactions | no | no | no |
| TWST | reactions | yes | no | no |
| TXG | reactions | yes | no | no |
| UCTT | reactions | no | no | no |
| UI | reactions | no | no | no |
| VAL | reactions | no | no | no |
| VICR | reactions | no | no | no |
| VRT | reactions | no | no | no |
| VZ | reactions | no | no | no |
| WOLF | reactions | no | no | no |
| WULF | reactions | yes | no | no |
| XETR | reactions | no | no | no |
| XTB | reactions | no | no | no |
| YUBICO | reactions | no | no | no |
| BMO | reminders | no | no | no |
| CLX | reminders | no | no | no |
| DOC | reminders | no | no | no |
| EL | reminders | no | no | no |
| EPS | reminders | no | no | no |
| ETR | reminders | no | no | no |
| FANG | reminders | no | no | no |
| FOX | reminders | no | no | no |
| FOXA | reminders | no | no | no |
| ON | reminders | no | no | no |
| PEG | reminders | no | no | no |
| PLTR | reminders | no | no | no |
| SBAC | reminders | no | no | no |
| UDR | reminders | no | no | no |
| VRTX | reminders | no | no | no |
| WMB | reminders | no | no | no |
| ABCL | screen | yes | yes | yes |
| CAI | screen | yes | yes | yes |
| CDNA | screen | yes | yes | yes |
| CVI | screen | yes | yes | yes |
| HTFL | screen | yes | yes | yes |
| KOD | screen | yes | yes | yes |
| LQDA | screen | yes | no | yes |
| MRNA | screen | yes | yes | yes |
| MTZ | screen | yes | yes | yes |
| NOW | screen | yes | yes | yes |
| PURR | screen | yes | yes | yes |
| QLYS | screen | yes | yes | yes |

## Method and caveats

| Field | Value |
|---|---|
| Sources | 5 families, listed above |
| Ticker extraction | the first ticker-shaped cell of every markdown table row, and the ticker column of every CSV |
| Counts | per family, per name; a name can be in a family's set even if that family listed it in a table the reader would skip |

**What this does not say.** It does not say the routines are wrong, and it
does not say a name seen once is a better or worse setup. It says the repo
currently contains no artifact that would tell you either.

