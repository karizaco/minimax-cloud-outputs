# Confirmation — how many routines saw each name

**Source:** derived join over daily-screens/<date>/{tier-a,focus}.csv, ntrt/<date>.md, options-flow/<date>.md, earnings/<date>-{reminders,reactions}.md (no source file is modified) · **Built:** 2026-11-15 · **Covers:** 261 distinct name(s) across 5 routines; 1173 on the 200-name master board · read-only

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
| `gap_brief` | the 09:00 pre-open gap brief (ntrt) | 55 |
| `options_flow` | the 16:35 unusual-options-flow screen | 38 |
| `reminders` | the 06:00 earnings-reminder watchlist | 18 |
| `reactions` | the 08:00 earnings-reaction scanner | 177 |
| `master board` | the 200-name screen output the tiers are cut from | 1173 |

The master board is not one of the five - it is the population the sweep's
tiers are cut from, and it is the baseline for how much overlap a
similarly-sized list would show by chance.

## Where the routines agree

| Pair | Shared names |
|---|---|
| gap_brief & reactions | 15 — AVEX, CRWV, DPC, EROC, EYE, FPS, IREN, NBIS, NVDA, QNT |
| screen & reactions | 9 — AAOI, AXTI, AZTA, CRWV, FPS, GLXY, LGN, NBIS, SNDK |
| gap_brief & options_flow | 7 — CRWV, CTVA, ENVX, LUNR, NBIS, NVDA, TE |
| options_flow & reactions | 7 — AMD, APLD, CRWV, INTC, MU, NBIS, NVDA |
| screen & gap_brief | 5 — CRWV, FPS, NBIS, SHAZ, SNDK |
| reminders & reactions | 3 — AMAT, NBIS, RKLB |
| screen & options_flow | 2 — CRWV, NBIS |
| screen & reminders | 1 — NBIS |
| gap_brief & reminders | 1 — NBIS |
| options_flow & reminders | 1 — NBIS |

## How many routines saw each name

| Routines that saw the name | Names |
|---|---|
| 5 | 1 |
| 4 | 1 |
| 3 | 3 |
| 2 | 26 |
| 1 | 230 |

**31 of 261 name(s) were seen by two or more routines.** The rest were seen
by exactly one, and which one is in the table below.

## Names seen by more than one routine

| Ticker | Routines | On master board | Tier-A | Focus |
|---|---|---|---|---|
| NBIS | screen, gap_brief, options_flow, reminders, reactions | yes | yes | yes |
| CRWV | screen, gap_brief, options_flow, reactions | yes | yes | yes |
| FPS | screen, gap_brief, reactions | yes | no | yes |
| NVDA | gap_brief, options_flow, reactions | yes | no | no |
| SNDK | screen, gap_brief, reactions | yes | no | yes |
| AAOI | screen, reactions | yes | no | yes |
| AMAT | reminders, reactions | yes | no | no |
| AMD | options_flow, reactions | yes | no | no |
| APLD | options_flow, reactions | yes | no | no |
| AVEX | gap_brief, reactions | yes | no | no |
| AXTI | screen, reactions | yes | no | yes |
| AZTA | screen, reactions | yes | no | yes |
| CTVA | gap_brief, options_flow | yes | no | no |
| DPC | gap_brief, reactions | yes | no | no |
| ENVX | gap_brief, options_flow | no | no | no |
| EROC | gap_brief, reactions | yes | no | no |
| EYE | gap_brief, reactions | no | no | no |
| GLXY | screen, reactions | yes | no | yes |
| INTC | options_flow, reactions | yes | no | no |
| IREN | gap_brief, reactions | yes | no | no |
| LGN | screen, reactions | yes | no | yes |
| LUNR | gap_brief, options_flow | yes | no | no |
| MU | options_flow, reactions | yes | no | no |
| QNT | gap_brief, reactions | yes | no | no |
| RKLB | reminders, reactions | yes | no | no |
| SHAZ | screen, gap_brief | yes | yes | yes |
| TE | gap_brief, options_flow | yes | no | no |
| TTEK | gap_brief, reactions | yes | no | no |
| TWST | gap_brief, reactions | yes | no | no |
| YETI | gap_brief, reactions | no | no | no |
| ZETA | gap_brief, reactions | yes | no | no |

## Names seen by exactly one routine

| Ticker | Routine | On master board | Tier-A | Focus |
|---|---|---|---|---|
| AAON | gap_brief | yes | no | no |
| AENT | gap_brief | no | no | no |
| ALLT | gap_brief | no | no | no |
| ALVO | gap_brief | no | no | no |
| BRUN | gap_brief | yes | no | no |
| CDNL | gap_brief | yes | no | no |
| CENN | gap_brief | no | no | no |
| CNCK | gap_brief | no | no | no |
| DGII | gap_brief | no | no | no |
| ENGS | gap_brief | no | no | no |
| EZPW | gap_brief | no | no | no |
| FA | gap_brief | no | no | no |
| FIGR | gap_brief | yes | no | no |
| FRMI | gap_brief | yes | no | no |
| FTK | gap_brief | no | no | no |
| HUBS | gap_brief | yes | no | no |
| HYMC | gap_brief | no | no | no |
| ICMB | gap_brief | no | no | no |
| INLF | gap_brief | no | no | no |
| LQDA | gap_brief | yes | no | no |
| MDU | gap_brief | no | no | no |
| NIQ | gap_brief | no | no | no |
| PARA | gap_brief | no | no | no |
| PLCE | gap_brief | no | no | no |
| POAS | gap_brief | no | no | no |
| PSFE | gap_brief | no | no | no |
| RZLV | gap_brief | no | no | no |
| SES | gap_brief | no | no | no |
| SMHI | gap_brief | no | no | no |
| SMX | gap_brief | no | no | no |
| SSYS | gap_brief | no | no | no |
| TII | gap_brief | no | no | no |
| VWAV | gap_brief | no | no | no |
| XAIR | gap_brief | no | no | no |
| XNDU | gap_brief | no | no | no |
| **CALL** | options_flow | no | no | no |
| **MIXED** | options_flow | no | no | no |
| AAPL | options_flow | yes | no | no |
| ABEV | options_flow | yes | no | no |
| AGNC | options_flow | yes | no | no |
| AMZN | options_flow | yes | no | no |
| AVGO | options_flow | yes | no | no |
| BABA | options_flow | yes | no | no |
| BTG | options_flow | yes | no | no |
| CCC | options_flow | yes | no | no |
| CDE | options_flow | yes | no | no |
| DNN | options_flow | yes | no | no |
| GLD | options_flow | no | no | no |
| GOOGL | options_flow | yes | no | no |
| IWM | options_flow | no | no | no |
| JBLU | options_flow | yes | no | no |
| KDP | options_flow | yes | no | no |
| MSFT | options_flow | yes | no | no |
| NFLX | options_flow | yes | no | no |
| NOK | options_flow | yes | no | no |
| ONDS | options_flow | yes | no | no |
| PLUG | options_flow | yes | no | no |
| RIOT | options_flow | yes | no | no |
| RKT | options_flow | yes | no | no |
| SOFI | options_flow | yes | no | no |
| SPCX | options_flow | yes | no | no |
| TSLA | options_flow | yes | no | no |
| ACMR | reactions | yes | no | no |
| ADEN | reactions | no | no | no |
| AEHR | reactions | yes | no | no |
| AEM | reactions | no | no | no |
| ALAB | reactions | yes | no | no |
| ALCE | reactions | no | no | no |
| ALGM | reactions | yes | no | no |
| ALNY | reactions | yes | no | no |
| AMBQ | reactions | yes | no | no |
| AMKR | reactions | yes | no | no |
| ANDF | reactions | no | no | no |
| APH | reactions | yes | no | no |
| ASST | reactions | yes | no | no |
| ASTS | reactions | yes | no | no |
| ASX | reactions | yes | no | no |
| BE | reactions | yes | no | no |
| BELA | reactions | no | no | no |
| BITTI | reactions | no | no | no |
| BLSH | reactions | yes | no | no |
| BME | reactions | no | no | no |
| BMNR | reactions | yes | no | no |
| BOE | reactions | no | no | no |
| BRBY | reactions | no | no | no |
| BSE | reactions | no | no | no |
| BTDR | reactions | yes | no | no |
| CBRS | reactions | yes | no | no |
| CIEN | reactions | yes | no | no |
| CIFR | reactions | yes | no | no |
| CLS | reactions | yes | no | no |
| CLSK | reactions | yes | no | no |
| CMB | reactions | no | no | no |
| COHR | reactions | yes | no | no |
| COHU | reactions | yes | no | no |
| CORZ | reactions | yes | no | no |
| CRDO | reactions | yes | no | no |
| DELL | reactions | yes | no | no |
| DJT | reactions | yes | no | no |
| DMP | reactions | no | no | no |
| DOCN | reactions | yes | no | no |
| ECO | reactions | yes | no | no |
| EDV | reactions | no | no | no |
| EGO | reactions | no | no | no |
| ENDUR | reactions | no | no | no |
| ENTG | reactions | yes | no | no |
| EQPT | reactions | yes | no | no |
| EQX | reactions | yes | no | no |
| ERA | reactions | no | no | no |
| EXTR | reactions | no | no | no |
| FCG | reactions | no | no | no |
| FG | reactions | no | no | no |
| FIX | reactions | yes | no | no |
| FLEXFO | reactions | no | no | no |
| FLS | reactions | no | no | no |
| FLY | reactions | yes | no | no |
| FN | reactions | yes | no | no |
| FORM | reactions | yes | no | no |
| FROG | reactions | yes | no | no |
| FRVO | reactions | yes | no | no |
| FSLY | reactions | yes | no | no |
| FUN | reactions | yes | no | no |
| GFS | reactions | yes | no | no |
| GLW | reactions | yes | no | no |
| GNRC | reactions | yes | no | no |
| HANA | reactions | no | no | no |
| HIMS | reactions | yes | no | no |
| HPE | reactions | yes | no | no |
| HUT | reactions | yes | no | no |
| ICHR | reactions | yes | no | no |
| INIO | reactions | yes | no | no |
| INOD | reactions | yes | no | no |
| KLAC | reactions | yes | no | no |
| KLIC | reactions | yes | no | no |
| LBW | reactions | no | no | no |
| LITE | reactions | yes | no | no |
| LLY | reactions | yes | no | no |
| LRCX | reactions | yes | no | no |
| MANE | reactions | yes | no | no |
| MEKO | reactions | no | no | no |
| MFT | reactions | no | no | no |
| MIM | reactions | no | no | no |
| MKSI | reactions | yes | no | no |
| MPWR | reactions | yes | no | no |
| MRNA | reactions | yes | no | no |
| MRVL | reactions | yes | no | no |
| MTHH | reactions | no | no | no |
| MTSI | reactions | yes | no | no |
| MXL | reactions | yes | no | no |
| NCOD | reactions | no | no | no |
| NEM | reactions | no | no | no |
| NEWP | reactions | no | no | no |
| NG | reactions | no | no | no |
| NORBT | reactions | no | no | no |
| NVMI | reactions | yes | no | no |
| NVTS | reactions | yes | no | no |
| NYSE | reactions | no | no | no |
| OBCK | reactions | no | no | no |
| OHB | reactions | no | no | no |
| ON | reactions | yes | no | no |
| ONTO | reactions | yes | no | no |
| ORCL | reactions | yes | no | no |
| PARR | reactions | yes | no | no |
| PBF | reactions | yes | no | no |
| PDFS | reactions | no | no | no |
| PENG | reactions | yes | no | no |
| PLPC | reactions | no | no | no |
| PLTR | reactions | yes | no | no |
| POWI | reactions | yes | no | no |
| PURR | reactions | yes | no | no |
| QCOM | reactions | yes | no | no |
| RAND | reactions | no | no | no |
| RBREW | reactions | no | no | no |
| RDDT | reactions | yes | no | no |
| RES | reactions | no | no | no |
| RMBS | reactions | yes | no | no |
| RSKD | reactions | yes | no | no |
| SECZ | reactions | no | no | no |
| SEI | reactions | yes | no | no |
| SGX | reactions | no | no | no |
| SITM | reactions | yes | no | no |
| SIVE | reactions | no | no | no |
| SMCI | reactions | yes | no | no |
| SMCIP | reactions | no | no | no |
| SSE | reactions | no | no | no |
| STG | reactions | no | no | no |
| STRL | reactions | yes | no | no |
| STX | reactions | yes | no | no |
| SUS | reactions | no | no | no |
| SZSE | reactions | no | no | no |
| TADAWUL | reactions | no | no | no |
| TER | reactions | yes | no | no |
| TH | reactions | no | no | no |
| TKN | reactions | no | no | no |
| TPRO | reactions | no | no | no |
| TRA | reactions | no | no | no |
| TRAX | reactions | yes | no | no |
| TRON | reactions | no | no | no |
| TSEM | reactions | yes | no | no |
| TTMI | reactions | yes | no | no |
| UCTT | reactions | yes | no | no |
| UNIX | reactions | no | no | no |
| VIAV | reactions | yes | no | no |
| VKTR | reactions | no | no | no |
| VLX | reactions | no | no | no |
| VRT | reactions | yes | no | no |
| VSH | reactions | yes | no | no |
| WAC | reactions | no | no | no |
| WDC | reactions | yes | no | no |
| WOLF | reactions | yes | no | no |
| WULF | reactions | yes | no | no |
| YPSN | reactions | no | no | no |
| YSN | reactions | no | no | no |
| AU | reminders | no | no | no |
| BN | reminders | no | no | no |
| BOLSY | reminders | no | no | no |
| CSCO | reminders | yes | no | no |
| EC | reminders | no | no | no |
| ENEL.MI | reminders | no | no | no |
| FER | reminders | no | no | no |
| FNV | reminders | no | no | no |
| HEI | reminders | no | no | no |
| NTRA | reminders | yes | no | no |
| NU | reminders | yes | no | no |
| SGAPY | reminders | no | no | no |
| TRI | reminders | no | no | no |
| UI | reminders | yes | no | no |
| WCN | reminders | no | no | no |
| AXGN | screen | yes | yes | yes |
| CAPR | screen | yes | no | yes |

## Method and caveats

| Field | Value |
|---|---|
| Sources | 5 families, listed above |
| Ticker extraction | the first ticker-shaped cell of every markdown table row, and the ticker column of every CSV |
| Counts | per family, per name; a name can be in a family's set even if that family listed it in a table the reader would skip |

**What this does not say.** It does not say the routines are wrong, and it
does not say a name seen once is a better or worse setup. It says the repo
currently contains no artifact that would tell you either.

