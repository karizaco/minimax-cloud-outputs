# Confirmation — how many routines saw each name

**Source:** derived join over daily-screens/<date>/{tier-a,focus}.csv, ntrt/<date>.md, options-flow/<date>.md, earnings/<date>-{reminders,reactions}.md (no source file is modified) · **Built:** 2026-11-15 · **Covers:** 185 distinct name(s) across 5 routines; 1188 on the 200-name master board · read-only

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
| `gap_brief` | the 09:00 pre-open gap brief (ntrt) | 50 |
| `options_flow` | the 16:35 unusual-options-flow screen | 41 |
| `reminders` | the 06:00 earnings-reminder watchlist | 10 |
| `reactions` | the 08:00 earnings-reaction scanner | 85 |
| `master board` | the 200-name screen output the tiers are cut from | 1188 |

The master board is not one of the five - it is the population the sweep's
tiers are cut from, and it is the baseline for how much overlap a
similarly-sized list would show by chance.

## Where the routines agree

| Pair | Shared names |
|---|---|
| options_flow & reactions | 4 — AMD, AVGO, CSCO, NBIS |
| screen & reactions | 3 — AMD, FIGR, PLBL |
| gap_brief & options_flow | 3 — CBRS, MRLN, SPCE |
| gap_brief & reactions | 2 — SLS, VIR |
| screen & options_flow | 1 — AMD |
| reminders & reactions | 1 — MSTR |
| screen & gap_brief | 0 |
| screen & reminders | 0 |
| gap_brief & reminders | 0 |
| options_flow & reminders | 0 |

## How many routines saw each name

| Routines that saw the name | Names |
|---|---|
| 3 | 1 |
| 2 | 11 |
| 1 | 173 |

**12 of 185 name(s) were seen by two or more routines.** The rest were seen
by exactly one, and which one is in the table below.

## Names seen by more than one routine

| Ticker | Routines | On master board | Tier-A | Focus |
|---|---|---|---|---|
| AMD | screen, options_flow, reactions | yes | yes | yes |
| AVGO | options_flow, reactions | yes | no | no |
| CBRS | gap_brief, options_flow | yes | no | no |
| CSCO | options_flow, reactions | yes | no | no |
| FIGR | screen, reactions | yes | no | yes |
| MRLN | gap_brief, options_flow | no | no | no |
| MSTR | reminders, reactions | yes | no | no |
| NBIS | options_flow, reactions | yes | no | no |
| PLBL | screen, reactions | yes | no | yes |
| SLS | gap_brief, reactions | yes | no | no |
| SPCE | gap_brief, options_flow | no | no | no |
| VIR | gap_brief, reactions | yes | no | no |

## Names seen by exactly one routine

| Ticker | Routine | On master board | Tier-A | Focus |
|---|---|---|---|---|
| AAON | gap_brief | yes | no | no |
| ACCV | gap_brief | yes | no | no |
| ALOY | gap_brief | no | no | no |
| ANDG | gap_brief | yes | no | no |
| BGIN | gap_brief | yes | no | no |
| CADL | gap_brief | no | no | no |
| CYPH | gap_brief | no | no | no |
| DGXX | gap_brief | no | no | no |
| DXY | gap_brief | no | no | no |
| ENHA | gap_brief | no | no | no |
| FBYD | gap_brief | no | no | no |
| FCUV | gap_brief | no | no | no |
| FLO | gap_brief | yes | no | no |
| HAWK | gap_brief | yes | no | no |
| KGEI | gap_brief | no | no | no |
| KLC | gap_brief | no | no | no |
| LFTO | gap_brief | yes | no | no |
| LQDA | gap_brief | yes | no | no |
| LRMR | gap_brief | yes | no | no |
| MOD | gap_brief | yes | no | no |
| MSB | gap_brief | no | no | no |
| NMAX | gap_brief | yes | no | no |
| NPCE | gap_brief | no | no | no |
| NUAI | gap_brief | yes | no | no |
| OFRM | gap_brief | no | no | no |
| OGEN | gap_brief | no | no | no |
| OPTT | gap_brief | no | no | no |
| OWLT | gap_brief | no | no | no |
| PURR | gap_brief | yes | no | no |
| QNT | gap_brief | yes | no | no |
| RIME | gap_brief | no | no | no |
| RMIX | gap_brief | no | no | no |
| RZLT | gap_brief | no | no | no |
| SBC | gap_brief | yes | no | no |
| SES | gap_brief | no | no | no |
| SHFS | gap_brief | no | no | no |
| SST | gap_brief | no | no | no |
| STNE | gap_brief | yes | no | no |
| TMC | gap_brief | no | no | no |
| TNDM | gap_brief | yes | no | no |
| VTSI | gap_brief | no | no | no |
| YSS | gap_brief | no | no | no |
| ZBAO | gap_brief | no | no | no |
| ZETA | gap_brief | yes | no | no |
| ZVRA | gap_brief | no | no | no |
| **CALL** | options_flow | no | no | no |
| **MIXED** | options_flow | no | no | no |
| AAPL | options_flow | yes | no | no |
| AGNC | options_flow | yes | no | no |
| AMZN | options_flow | yes | no | no |
| BBD | options_flow | no | no | no |
| BTG | options_flow | yes | no | no |
| CTVA | options_flow | yes | no | no |
| FRMI | options_flow | yes | no | no |
| GLD | options_flow | no | no | no |
| GOOGL | options_flow | yes | no | no |
| GRAB | options_flow | yes | no | no |
| HL | options_flow | yes | no | no |
| INTC | options_flow | yes | no | no |
| IWM | options_flow | no | no | no |
| KDP | options_flow | yes | no | no |
| MARA | options_flow | yes | no | no |
| MRVL | options_flow | yes | no | no |
| MSFT | options_flow | yes | no | no |
| MU | options_flow | yes | no | no |
| NFLX | options_flow | yes | no | no |
| NOK | options_flow | yes | no | no |
| NU | options_flow | yes | no | no |
| NVDA | options_flow | yes | no | no |
| ORCL | options_flow | yes | no | no |
| RIOT | options_flow | yes | no | no |
| SMCI | options_flow | yes | no | no |
| SMR | options_flow | yes | no | no |
| SPCX | options_flow | yes | no | no |
| STLA | options_flow | yes | no | no |
| STLN | options_flow | yes | no | no |
| TE | options_flow | yes | no | no |
| TLT | options_flow | no | no | no |
| TSLA | options_flow | yes | no | no |
| AAOI | reactions | yes | no | no |
| ABSI | reactions | no | no | no |
| AEHR | reactions | yes | no | no |
| AGBK | reactions | yes | no | no |
| AKAST | reactions | no | no | no |
| ALM | reactions | yes | no | no |
| ANA | reactions | no | no | no |
| ANE | reactions | no | no | no |
| ANUP | reactions | no | no | no |
| ASX | reactions | yes | no | no |
| ATS | reactions | no | no | no |
| AWX | reactions | no | no | no |
| AYA | reactions | yes | no | no |
| BMAG | reactions | no | no | no |
| BOUV | reactions | no | no | no |
| BSE | reactions | no | no | no |
| CDLR | reactions | no | no | no |
| CFR | reactions | no | no | no |
| CMB | reactions | no | no | no |
| CNA | reactions | no | no | no |
| CRCL | reactions | yes | no | no |
| CRML | reactions | yes | no | no |
| CRWD | reactions | yes | no | no |
| DHT | reactions | no | no | no |
| ERA | reactions | no | no | no |
| ESIP | reactions | no | no | no |
| FCG | reactions | no | no | no |
| FCT | reactions | no | no | no |
| FTNT | reactions | no | no | no |
| GENB | reactions | no | no | no |
| GENO | reactions | no | no | no |
| GLXY | reactions | yes | no | no |
| GOMX | reactions | no | no | no |
| GRE | reactions | no | no | no |
| HEM | reactions | no | no | no |
| HOS | reactions | yes | no | no |
| HPK | reactions | yes | no | no |
| HTECH | reactions | no | no | no |
| III | reactions | no | no | no |
| INFQ | reactions | yes | no | no |
| IREN | reactions | yes | no | no |
| LOW | reactions | yes | no | no |
| MDLN | reactions | yes | no | no |
| MMK | reactions | no | no | no |
| MOL | reactions | no | no | no |
| MSTCLTD | reactions | no | no | no |
| NTLA | reactions | yes | no | no |
| NYSE | reactions | no | no | no |
| OBCK | reactions | no | no | no |
| OCUL | reactions | no | no | no |
| OHB | reactions | no | no | no |
| OMXSTO | reactions | no | no | no |
| OVH | reactions | no | no | no |
| PANW | reactions | yes | no | no |
| PAX | reactions | no | no | no |
| PDN | reactions | no | no | no |
| RPL | reactions | no | no | no |
| SECZ | reactions | no | no | no |
| SGC | reactions | no | no | no |
| SGX | reactions | no | no | no |
| SMOP | reactions | no | no | no |
| SNDK | reactions | yes | no | no |
| SVOA | reactions | no | no | no |
| SZSE | reactions | no | no | no |
| TADAWUL | reactions | no | no | no |
| TOR | reactions | no | no | no |
| TRV | reactions | yes | no | no |
| TXG | reactions | yes | no | no |
| UHR | reactions | no | no | no |
| VBK | reactions | no | no | no |
| VGL | reactions | no | no | no |
| VOYG | reactions | no | no | no |
| WGS | reactions | yes | no | no |
| WISE | reactions | no | no | no |
| WMUU | reactions | no | no | no |
| XETR | reactions | no | no | no |
| AU | reminders | no | no | no |
| FER | reminders | no | no | no |
| FNV | reminders | no | no | no |
| NTRA | reminders | yes | no | no |
| RKLB | reminders | yes | no | no |
| SLF | reminders | no | no | no |
| TRI | reminders | no | no | no |
| UI | reminders | yes | no | no |
| WCN | reminders | yes | no | no |
| ANET | screen | yes | no | yes |
| CHA | screen | yes | yes | yes |
| DPC | screen | yes | yes | yes |
| HUBS | screen | yes | no | yes |
| IBP | screen | yes | no | yes |
| IRTC | screen | yes | yes | yes |
| LMND | screen | yes | no | yes |
| LUNR | screen | yes | yes | yes |
| TOP | screen | yes | no | yes |

## Method and caveats

| Field | Value |
|---|---|
| Sources | 5 families, listed above |
| Ticker extraction | the first ticker-shaped cell of every markdown table row, and the ticker column of every CSV |
| Counts | per family, per name; a name can be in a family's set even if that family listed it in a table the reader would skip |

**What this does not say.** It does not say the routines are wrong, and it
does not say a name seen once is a better or worse setup. It says the repo
currently contains no artifact that would tell you either.

