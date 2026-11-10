# Confirmation — how many routines saw each name

**Source:** derived join over daily-screens/<date>/{tier-a,focus}.csv, ntrt/<date>.md, options-flow/<date>.md, earnings/<date>-{reminders,reactions}.md (no source file is modified) · **Built:** 2026-11-10 · **Covers:** 290 distinct name(s) across 5 routines; 456 on the 200-name master board · read-only

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
| `gap_brief` | the 09:00 pre-open gap brief (ntrt) | 35 |
| `options_flow` | the 16:35 unusual-options-flow screen | 10 |
| `reminders` | the 06:00 earnings-reminder watchlist | 73 |
| `reactions` | the 08:00 earnings-reaction scanner | 187 |
| `master board` | the 200-name screen output the tiers are cut from | 456 |

The master board is not one of the five - it is the population the sweep's
tiers are cut from, and it is the baseline for how much overlap a
similarly-sized list would show by chance.

## Where the routines agree

| Pair | Shared names |
|---|---|
| reminders & reactions | 13 — AMZN, ASX, BMY, GILD, INTC, LLY, MO, MRK, PWR, SBUX |
| gap_brief & reactions | 10 — FTNT, GOOGL, HLN, MRVL, NOW, NVCR, PGY, PRCH, SFM, TDOC |
| options_flow & reactions | 2 — AMZN, GOOGL |
| screen & reactions | 1 — SDGR |
| gap_brief & options_flow | 1 — GOOGL |
| gap_brief & reminders | 1 — NCLH |
| options_flow & reminders | 1 — AMZN |
| screen & gap_brief | 0 |
| screen & options_flow | 0 |
| screen & reminders | 0 |

## How many routines saw each name

| Routines that saw the name | Names |
|---|---|
| 3 | 2 |
| 2 | 23 |
| 1 | 265 |

**25 of 290 name(s) were seen by two or more routines.** The rest were seen
by exactly one, and which one is in the table below.

## Names seen by more than one routine

| Ticker | Routines | On master board | Tier-A | Focus |
|---|---|---|---|---|
| AMZN | options_flow, reminders, reactions | yes | no | no |
| GOOGL | gap_brief, options_flow, reactions | yes | no | no |
| ASX | reminders, reactions | no | no | no |
| BMY | reminders, reactions | no | no | no |
| FTNT | gap_brief, reactions | no | no | no |
| GILD | reminders, reactions | no | no | no |
| HLN | gap_brief, reactions | no | no | no |
| INTC | reminders, reactions | yes | no | no |
| LLY | reminders, reactions | yes | no | no |
| MO | reminders, reactions | no | no | no |
| MRK | reminders, reactions | no | no | no |
| MRVL | gap_brief, reactions | yes | no | no |
| NCLH | gap_brief, reminders | yes | no | no |
| NOW | gap_brief, reactions | no | no | no |
| NVCR | gap_brief, reactions | no | no | no |
| PGY | gap_brief, reactions | no | no | no |
| PRCH | gap_brief, reactions | yes | no | no |
| PWR | reminders, reactions | yes | no | no |
| SBUX | reminders, reactions | no | no | no |
| SDGR | screen, reactions | yes | yes | yes |
| SFM | gap_brief, reactions | no | no | no |
| SNDK | reminders, reactions | yes | no | no |
| TDOC | gap_brief, reactions | yes | no | no |
| TT | reminders, reactions | no | no | no |
| TTE | reminders, reactions | yes | no | no |

## Names seen by exactly one routine

| Ticker | Routine | On master board | Tier-A | Focus |
|---|---|---|---|---|
| ALKT | gap_brief | no | no | no |
| ALNY | gap_brief | no | no | no |
| CROX | gap_brief | yes | no | no |
| CYH | gap_brief | no | no | no |
| EGO | gap_brief | no | no | no |
| FVRR | gap_brief | no | no | no |
| GBFH | gap_brief | no | no | no |
| GEN | gap_brief | no | no | no |
| GKOS | gap_brief | yes | no | no |
| INSM | gap_brief | yes | no | no |
| IOVA | gap_brief | yes | no | no |
| MAX | gap_brief | yes | no | no |
| MESO | gap_brief | no | no | no |
| MNRO | gap_brief | no | no | no |
| NNBR | gap_brief | no | no | no |
| NUAI | gap_brief | no | no | no |
| OSK | gap_brief | no | no | no |
| PHAT | gap_brief | no | no | no |
| PURR | gap_brief | yes | no | no |
| PWP | gap_brief | yes | no | no |
| RES | gap_brief | no | no | no |
| TWI | gap_brief | no | no | no |
| VNDA | gap_brief | no | no | no |
| XRX | gap_brief | no | no | no |
| **CALL** | options_flow | no | no | no |
| AAPL | options_flow | yes | no | no |
| GLD | options_flow | no | no | no |
| IWM | options_flow | no | no | no |
| MSFT | options_flow | no | no | no |
| NVDA | options_flow | yes | no | no |
| PUT | options_flow | no | no | no |
| TLT | options_flow | no | no | no |
| AAOI | reactions | no | no | no |
| ABCL | reactions | yes | no | no |
| ACN | reactions | no | no | no |
| ADBE | reactions | no | no | no |
| ADP | reactions | no | no | no |
| AEM | reactions | yes | no | no |
| AER | reactions | no | no | no |
| AESI | reactions | no | no | no |
| ALAB | reactions | yes | no | no |
| ALMR | reactions | no | no | no |
| AMD | reactions | yes | no | no |
| AMGN | reactions | no | no | no |
| AMKR | reactions | yes | no | no |
| APLD | reactions | yes | no | no |
| APPN | reactions | yes | no | no |
| APR | reactions | no | no | no |
| AVGO | reactions | yes | no | no |
| AVOL | reactions | no | no | no |
| AXTI | reactions | yes | no | no |
| AZN | reactions | no | no | no |
| BE | reactions | yes | no | no |
| BEAM | reactions | yes | no | no |
| BFLY | reactions | no | no | no |
| BHC | reactions | yes | no | no |
| BINV | reactions | no | no | no |
| BKNG | reactions | no | no | no |
| BOQCD | reactions | no | no | no |
| BTDR | reactions | yes | no | no |
| BTU | reactions | no | no | no |
| CBO | reactions | no | no | no |
| CBRS | reactions | no | no | no |
| CIA | reactions | no | no | no |
| CIFR | reactions | yes | no | no |
| CLS | reactions | yes | no | no |
| CLSK | reactions | yes | no | no |
| CMPR | reactions | no | no | no |
| COHU | reactions | no | no | no |
| CORZ | reactions | yes | no | no |
| CPR | reactions | no | no | no |
| CPS | reactions | no | no | no |
| CRDO | reactions | yes | no | no |
| CRM | reactions | no | no | no |
| CRML | reactions | no | no | no |
| CRWD | reactions | no | no | no |
| CRWV | reactions | yes | no | no |
| CSTL | reactions | yes | no | no |
| DB | reactions | no | no | no |
| DDOG | reactions | no | no | no |
| DELL | reactions | no | no | no |
| DUR | reactions | no | no | no |
| DVP | reactions | no | no | no |
| ELS | reactions | no | no | no |
| ELV | reactions | no | no | no |
| ENTG | reactions | no | no | no |
| EU | reactions | no | no | no |
| FFM | reactions | no | no | no |
| FLEX | reactions | yes | no | no |
| FLOW | reactions | no | no | no |
| FN | reactions | yes | no | no |
| FPS | reactions | no | no | no |
| FRVO | reactions | no | no | no |
| FTAI | reactions | yes | no | no |
| FTRE | reactions | yes | no | no |
| GEV | reactions | no | no | no |
| GFL | reactions | no | no | no |
| GLW | reactions | no | no | no |
| GLXY | reactions | yes | no | no |
| GNP | reactions | no | no | no |
| GOOG | reactions | no | no | no |
| GOOGM | reactions | no | no | no |
| GOOGN | reactions | no | no | no |
| GRAL | reactions | yes | no | no |
| GUBRA | reactions | no | no | no |
| HONA | reactions | no | no | no |
| HP | reactions | no | no | no |
| HPE | reactions | no | no | no |
| IBM | reactions | no | no | no |
| ICHR | reactions | no | no | no |
| IDX | reactions | no | no | no |
| ILU | reactions | no | no | no |
| INIO | reactions | yes | no | no |
| INOD | reactions | no | no | no |
| INTU | reactions | no | no | no |
| IREN | reactions | yes | no | no |
| JNJ | reactions | no | no | no |
| KBX | reactions | no | no | no |
| KLAC | reactions | no | no | no |
| KOG | reactions | no | no | no |
| KYMR | reactions | no | no | no |
| LITE | reactions | yes | no | no |
| LYC | reactions | no | no | no |
| MAD | reactions | no | no | no |
| MAR | reactions | no | no | no |
| MARA | reactions | yes | no | no |
| MOD | reactions | yes | no | no |
| MS | reactions | yes | no | no |
| MSB | reactions | no | no | no |
| MU | reactions | yes | no | no |
| MYRG | reactions | no | no | no |
| NBIS | reactions | yes | no | no |
| NEO | reactions | no | no | no |
| NETC | reactions | no | no | no |
| NEU | reactions | no | no | no |
| NN | reactions | no | no | no |
| NTLA | reactions | yes | no | no |
| NVT | reactions | yes | no | no |
| NYSE | reactions | no | no | no |
| OHB | reactions | no | no | no |
| OMXCOP | reactions | no | no | no |
| OMXHEX | reactions | no | no | no |
| OMXSTO | reactions | no | no | no |
| ON | reactions | no | no | no |
| ONTO | reactions | no | no | no |
| OWL | reactions | no | no | no |
| PANW | reactions | no | no | no |
| PDX | reactions | no | no | no |
| PEP | reactions | no | no | no |
| PLS | reactions | no | no | no |
| PLT | reactions | no | no | no |
| PLX | reactions | no | no | no |
| POWL | reactions | yes | no | no |
| PRY | reactions | no | no | no |
| QNT | reactions | yes | no | no |
| RCL | reactions | no | no | no |
| REGN | reactions | no | no | no |
| RIOT | reactions | yes | no | no |
| RNO | reactions | no | no | no |
| SAIA | reactions | yes | no | no |
| SDZ | reactions | no | no | no |
| SEI | reactions | yes | no | no |
| SHA | reactions | no | no | no |
| SHAZ | reactions | no | no | no |
| SJF | reactions | no | no | no |
| SKS | reactions | no | no | no |
| SMOP | reactions | no | no | no |
| SNOW | reactions | no | no | no |
| SNPS | reactions | yes | no | no |
| STJ | reactions | no | no | no |
| STRL | reactions | no | no | no |
| STX | reactions | yes | no | no |
| SZG | reactions | no | no | no |
| TE | reactions | no | no | no |
| TEM | reactions | yes | no | no |
| TER | reactions | no | no | no |
| TEX | reactions | no | no | no |
| TMUS | reactions | no | no | no |
| TTMI | reactions | yes | no | no |
| TUA | reactions | no | no | no |
| TYL | reactions | yes | no | no |
| UBS | reactions | no | no | no |
| UCTT | reactions | yes | no | no |
| UEC | reactions | yes | no | no |
| ULCC | reactions | no | no | no |
| VIAV | reactions | yes | no | no |
| VRT | reactions | yes | no | no |
| VRTX | reactions | no | no | no |
| WDC | reactions | yes | no | no |
| WES | reactions | no | no | no |
| WFC | reactions | no | no | no |
| WMT | reactions | no | no | no |
| WOLF | reactions | yes | no | no |
| WULF | reactions | yes | no | no |
| ZIP | reactions | no | no | no |
| AJG | reminders | no | no | no |
| AMP | reminders | no | no | no |
| AOS | reminders | no | no | no |
| ARES | reminders | no | no | no |
| AVY | reminders | no | no | no |
| BAX | reminders | no | no | no |
| BBVA | reminders | no | no | no |
| BG | reminders | no | no | no |
| BUD | reminders | no | no | no |
| CARR | reminders | no | no | no |
| COIN | reminders | yes | no | no |
| CRH | reminders | yes | no | no |
| CTSH | reminders | no | no | no |
| DHI | reminders | no | no | no |
| DLR | reminders | no | no | no |
| DVA | reminders | yes | no | no |
| DXCM | reminders | no | no | no |
| EIX | reminders | no | no | no |
| EME | reminders | no | no | no |
| EPD | reminders | yes | no | no |
| ERIE | reminders | no | no | no |
| FDXF | reminders | no | no | no |
| FSLR | reminders | no | no | no |
| GDDY | reminders | no | no | no |
| HII | reminders | yes | no | no |
| HSY | reminders | no | no | no |
| HWM | reminders | no | no | no |
| ICE | reminders | no | no | no |
| ILMN | reminders | yes | no | no |
| INCY | reminders | yes | no | no |
| ING | reminders | no | no | no |
| IR | reminders | no | no | no |
| KIM | reminders | no | no | no |
| LHX | reminders | no | no | no |
| LIN | reminders | no | no | no |
| LNG | reminders | yes | no | no |
| LNT | reminders | no | no | no |
| LYG | reminders | no | no | no |
| MA | reminders | no | no | no |
| MDLZ | reminders | no | no | no |
| MPWR | reminders | no | no | no |
| MSTR | reminders | yes | no | no |
| RDDT | reminders | no | no | no |
| RMD | reminders | no | no | no |
| RSG | reminders | no | no | no |
| SHEL | reminders | no | no | no |
| SYK | reminders | no | no | no |
| TAK | reminders | no | no | no |
| TROW | reminders | no | no | no |
| TWLO | reminders | yes | no | no |
| TXT | reminders | yes | no | no |
| VALE | reminders | yes | no | no |
| VLTO | reminders | no | no | no |
| VMC | reminders | yes | no | no |
| WEC | reminders | yes | no | no |
| WST | reminders | yes | no | no |
| WTW | reminders | no | no | no |
| WY | reminders | no | no | no |
| XEL | reminders | no | no | no |
| AXGN | screen | yes | no | yes |
| FIGS | screen | yes | yes | yes |
| GMAB | screen | yes | yes | yes |
| HRI | screen | yes | no | yes |
| ICLR | screen | yes | no | yes |
| KIDS | screen | yes | no | yes |
| LQDA | screen | yes | no | yes |
| NTSK | screen | yes | no | yes |
| PRME | screen | yes | yes | yes |
| RRC | screen | yes | no | yes |
| SGRY | screen | yes | no | yes |

## Method and caveats

| Field | Value |
|---|---|
| Sources | 5 families, listed above |
| Ticker extraction | the first ticker-shaped cell of every markdown table row, and the ticker column of every CSV |
| Counts | per family, per name; a name can be in a family's set even if that family listed it in a table the reader would skip |

**What this does not say.** It does not say the routines are wrong, and it
does not say a name seen once is a better or worse setup. It says the repo
currently contains no artifact that would tell you either.

