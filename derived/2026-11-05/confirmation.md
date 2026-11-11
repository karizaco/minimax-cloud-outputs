# Confirmation — how many routines saw each name

**Source:** derived join over daily-screens/<date>/{tier-a,focus}.csv, ntrt/<date>.md, options-flow/<date>.md, earnings/<date>-{reminders,reactions}.md (no source file is modified) · **Built:** 2026-11-11 · **Covers:** 380 distinct name(s) across 5 routines; 200 on the 200-name master board · read-only

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
| `gap_brief` | the 09:00 pre-open gap brief (ntrt) | 86 |
| `options_flow` | the 16:35 unusual-options-flow screen | 38 |
| `reminders` | the 06:00 earnings-reminder watchlist | 68 |
| `reactions` | the 08:00 earnings-reaction scanner | 221 |
| `master board` | the 200-name screen output the tiers are cut from | 200 |

The master board is not one of the five - it is the population the sweep's
tiers are cut from, and it is the baseline for how much overlap a
similarly-sized list would show by chance.

## Where the routines agree

| Pair | Shared names |
|---|---|
| gap_brief & reactions | 16 — AMD, APP, BE, DELL, ENOV, IREN, LYNX, MELI, MU, ONDS |
| options_flow & reactions | 12 — AMD, AMZN, AVGO, CDE, MRVL, MU, ONDS, PLTR, RIG, RIOT |
| options_flow & reminders | 8 — AAPL, AMZN, GLD, GOOGL, IWM, MSFT, NVDA, RKT |
| gap_brief & options_flow | 5 — AMD, JOBY, MU, ONDS, SNAP |
| reminders & reactions | 4 — AMZN, CI, CNQ, PH |
| screen & reactions | 2 — ENOV, OUST |
| gap_brief & reminders | 2 — CMI, TPR |
| screen & gap_brief | 1 — ENOV |
| screen & options_flow | 0 |
| screen & reminders | 0 |

## How many routines saw each name

| Routines that saw the name | Names |
|---|---|
| 3 | 5 |
| 2 | 35 |
| 1 | 340 |

**40 of 380 name(s) were seen by two or more routines.** The rest were seen
by exactly one, and which one is in the table below.

## Names seen by more than one routine

| Ticker | Routines | On master board | Tier-A | Focus |
|---|---|---|---|---|
| AMD | gap_brief, options_flow, reactions | no | no | no |
| AMZN | options_flow, reminders, reactions | no | no | no |
| ENOV | screen, gap_brief, reactions | yes | no | yes |
| MU | gap_brief, options_flow, reactions | no | no | no |
| ONDS | gap_brief, options_flow, reactions | yes | no | no |
| AAPL | options_flow, reminders | no | no | no |
| APP | gap_brief, reactions | yes | no | no |
| AVGO | options_flow, reactions | no | no | no |
| BE | gap_brief, reactions | yes | no | no |
| CDE | options_flow, reactions | no | no | no |
| CI | reminders, reactions | no | no | no |
| CMI | gap_brief, reminders | no | no | no |
| CNQ | reminders, reactions | no | no | no |
| DELL | gap_brief, reactions | yes | no | no |
| GLD | options_flow, reminders | no | no | no |
| GOOGL | options_flow, reminders | no | no | no |
| IREN | gap_brief, reactions | yes | no | no |
| IWM | options_flow, reminders | no | no | no |
| JOBY | gap_brief, options_flow | yes | no | no |
| LYNX | gap_brief, reactions | no | no | no |
| MELI | gap_brief, reactions | no | no | no |
| MRVL | options_flow, reactions | yes | no | no |
| MSFT | options_flow, reminders | no | no | no |
| NVDA | options_flow, reminders | no | no | no |
| OSCR | gap_brief, reactions | no | no | no |
| OUST | screen, reactions | yes | yes | yes |
| PH | reminders, reactions | no | no | no |
| PLTR | options_flow, reactions | no | no | no |
| QCOM | gap_brief, reactions | no | no | no |
| RIG | options_flow, reactions | no | no | no |
| RIOT | options_flow, reactions | yes | no | no |
| RKT | options_flow, reminders | yes | no | no |
| SEZL | gap_brief, reactions | yes | no | no |
| SNAP | gap_brief, options_flow | yes | no | no |
| SNDK | gap_brief, reactions | yes | no | no |
| SPCX | options_flow, reactions | no | no | no |
| TPR | gap_brief, reminders | no | no | no |
| TRIP | gap_brief, reactions | no | no | no |
| TSLA | options_flow, reactions | no | no | no |
| ZG | gap_brief, reactions | no | no | no |

## Names seen by exactly one routine

| Ticker | Routine | On master board | Tier-A | Focus |
|---|---|---|---|---|
| ACHC | gap_brief | yes | no | no |
| ADMA | gap_brief | yes | no | no |
| ALTO | gap_brief | no | no | no |
| ARQT | gap_brief | yes | no | no |
| ASM | gap_brief | no | no | no |
| ASPN | gap_brief | no | no | no |
| BKSY | gap_brief | no | no | no |
| BROS | gap_brief | no | no | no |
| CAI | gap_brief | yes | no | no |
| CELH | gap_brief | no | no | no |
| CIM | gap_brief | no | no | no |
| COHR | gap_brief | yes | no | no |
| CRON | gap_brief | no | no | no |
| CSV | gap_brief | no | no | no |
| DDD | gap_brief | no | no | no |
| DTIL | gap_brief | no | no | no |
| EOSE | gap_brief | no | no | no |
| EPAM | gap_brief | no | no | no |
| EWTX | gap_brief | no | no | no |
| FLNC | gap_brief | no | no | no |
| FSLR | gap_brief | no | no | no |
| FSLY | gap_brief | no | no | no |
| FUN | gap_brief | yes | no | no |
| GIL | gap_brief | no | no | no |
| GRAL | gap_brief | yes | no | no |
| GROY | gap_brief | no | no | no |
| HLP | gap_brief | no | no | no |
| HNST | gap_brief | no | no | no |
| HTZ | gap_brief | no | no | no |
| HUBS | gap_brief | no | no | no |
| INGR | gap_brief | no | no | no |
| IOVA | gap_brief | yes | no | no |
| IRWD | gap_brief | no | no | no |
| JAN | gap_brief | no | no | no |
| KEEL | gap_brief | no | no | no |
| KMDA | gap_brief | no | no | no |
| KRP | gap_brief | no | no | no |
| LXRX | gap_brief | no | no | no |
| LZ | gap_brief | no | no | no |
| MBUU | gap_brief | no | no | no |
| MGNI | gap_brief | no | no | no |
| MNTN | gap_brief | no | no | no |
| MTSI | gap_brief | no | no | no |
| NNBR | gap_brief | no | no | no |
| NVMI | gap_brief | no | no | no |
| PTLO | gap_brief | no | no | no |
| PTON | gap_brief | no | no | no |
| RDW | gap_brief | yes | no | no |
| RELY | gap_brief | no | no | no |
| ROCK | gap_brief | no | no | no |
| ROOT | gap_brief | no | no | no |
| RPD | gap_brief | no | no | no |
| RUN | gap_brief | yes | no | no |
| RZLV | gap_brief | no | no | no |
| SABR | gap_brief | no | no | no |
| STAA | gap_brief | no | no | no |
| SVCO | gap_brief | no | no | no |
| TBI | gap_brief | no | no | no |
| TDUP | gap_brief | no | no | no |
| TE | gap_brief | yes | no | no |
| TXO | gap_brief | no | no | no |
| VCYT | gap_brief | no | no | no |
| VERX | gap_brief | no | no | no |
| WMS | gap_brief | no | no | no |
| WRBY | gap_brief | no | no | no |
| XERS | gap_brief | no | no | no |
| **PUT** | options_flow | no | no | no |
| AMC | options_flow | yes | no | no |
| BBD | options_flow | no | no | no |
| FRMI | options_flow | yes | no | no |
| GRAB | options_flow | no | no | no |
| MARA | options_flow | yes | no | no |
| NIO | options_flow | no | no | no |
| NOK | options_flow | no | no | no |
| NU | options_flow | no | no | no |
| ORCL | options_flow | yes | no | no |
| PFE | options_flow | no | no | no |
| PLUG | options_flow | no | no | no |
| SKHY | options_flow | no | no | no |
| SMCI | options_flow | yes | no | no |
| STLA | options_flow | no | no | no |
| TSM | options_flow | no | no | no |
| WMT | options_flow | no | no | no |
| AADX | reactions | no | no | no |
| AAOI | reactions | yes | no | no |
| ACCV | reactions | no | no | no |
| ADI | reactions | no | no | no |
| AEHR | reactions | no | no | no |
| AEM | reactions | no | no | no |
| AF | reactions | no | no | no |
| AGI | reactions | no | no | no |
| AGX | reactions | no | no | no |
| AKAST | reactions | no | no | no |
| AKRBP | reactions | no | no | no |
| ALGM | reactions | no | no | no |
| ALNT | reactions | no | no | no |
| AMAT | reactions | no | no | no |
| AMBQ | reactions | no | no | no |
| ANDE | reactions | no | no | no |
| ANET | reactions | yes | no | no |
| APE | reactions | no | no | no |
| APH | reactions | no | no | no |
| APLD | reactions | yes | no | no |
| ARHS | reactions | yes | no | no |
| ASHM | reactions | no | no | no |
| ASST | reactions | yes | no | no |
| ASX | reactions | no | no | no |
| ATEC | reactions | no | no | no |
| ATT | reactions | no | no | no |
| AVAV | reactions | no | no | no |
| AXTI | reactions | yes | no | no |
| BAC | reactions | no | no | no |
| BELFA | reactions | no | no | no |
| BELFB | reactions | no | no | no |
| BTG | reactions | no | no | no |
| BUUU | reactions | no | no | no |
| BWLP | reactions | no | no | no |
| BWXT | reactions | no | no | no |
| CAMT | reactions | no | no | no |
| CAMX | reactions | no | no | no |
| CBRAIN | reactions | no | no | no |
| CEG | reactions | no | no | no |
| CIA | reactions | no | no | no |
| CIEN | reactions | yes | no | no |
| CIFR | reactions | yes | no | no |
| CLMT | reactions | no | no | no |
| CLS | reactions | no | no | no |
| CLSK | reactions | yes | no | no |
| CMM | reactions | no | no | no |
| CNC | reactions | yes | no | no |
| COF | reactions | no | no | no |
| COHU | reactions | no | no | no |
| COST | reactions | no | no | no |
| CQP | reactions | no | no | no |
| CRDO | reactions | yes | no | no |
| CRWD | reactions | no | no | no |
| CRWV | reactions | yes | no | no |
| CSCO | reactions | no | no | no |
| CYL | reactions | no | no | no |
| DASH | reactions | yes | no | no |
| DDOG | reactions | yes | no | no |
| DG | reactions | no | no | no |
| DOCN | reactions | no | no | no |
| DOX | reactions | yes | no | no |
| DXPE | reactions | no | no | no |
| ECO | reactions | no | no | no |
| EDV | reactions | no | no | no |
| EGTX | reactions | no | no | no |
| EMR | reactions | no | no | no |
| ENTG | reactions | no | no | no |
| EQX | reactions | yes | no | no |
| EROC | reactions | no | no | no |
| ESLT | reactions | no | no | no |
| ETN | reactions | no | no | no |
| EVN | reactions | no | no | no |
| EXK | reactions | no | no | no |
| EXPE | reactions | no | no | no |
| FIX | reactions | no | no | no |
| FLEX | reactions | no | no | no |
| FORM | reactions | no | no | no |
| FOUR | reactions | no | no | no |
| FPS | reactions | yes | no | no |
| FTAI | reactions | no | no | no |
| FTNT | reactions | no | no | no |
| GEV | reactions | no | no | no |
| GLW | reactions | no | no | no |
| GLXY | reactions | yes | no | no |
| GN | reactions | no | no | no |
| GOMX | reactions | no | no | no |
| GOOGM | reactions | no | no | no |
| GPGI | reactions | no | no | no |
| HAWK | reactions | no | no | no |
| HCA | reactions | no | no | no |
| HL | reactions | yes | no | no |
| HUT | reactions | yes | no | no |
| HYMC | reactions | no | no | no |
| IART | reactions | no | no | no |
| ICHR | reactions | no | no | no |
| IESC | reactions | yes | no | no |
| INIO | reactions | yes | no | no |
| INNV | reactions | no | no | no |
| INTC | reactions | yes | no | no |
| IQMX | reactions | no | no | no |
| KCN | reactions | no | no | no |
| KGS | reactions | no | no | no |
| KLAC | reactions | no | no | no |
| LASR | reactions | no | no | no |
| LGN | reactions | no | no | no |
| LIME | reactions | no | no | no |
| LITE | reactions | yes | no | no |
| LMAT | reactions | no | no | no |
| LMND | reactions | no | no | no |
| LRCX | reactions | no | no | no |
| LXS | reactions | no | no | no |
| MATAS | reactions | no | no | no |
| MGNS | reactions | no | no | no |
| MMYT | reactions | no | no | no |
| MOD | reactions | yes | no | no |
| MOH | reactions | no | no | no |
| MTRN | reactions | no | no | no |
| MXL | reactions | no | no | no |
| NASDAQ | reactions | no | no | no |
| NBIS | reactions | yes | no | no |
| NCOD | reactions | no | no | no |
| NEM | reactions | no | no | no |
| NEU | reactions | no | no | no |
| NEWP | reactions | no | no | no |
| NKR | reactions | no | no | no |
| NN | reactions | no | no | no |
| NRC | reactions | no | no | no |
| NVAX | reactions | yes | no | no |
| NVT | reactions | no | no | no |
| NVTS | reactions | yes | no | no |
| NXT | reactions | yes | no | no |
| NYSE | reactions | no | no | no |
| OGC | reactions | no | no | no |
| OMXCOP | reactions | no | no | no |
| OMXSTO | reactions | no | no | no |
| ONTO | reactions | no | no | no |
| PBF | reactions | no | no | no |
| PDI | reactions | no | no | no |
| PENG | reactions | no | no | no |
| PL | reactions | no | no | no |
| PLPC | reactions | no | no | no |
| POWL | reactions | no | no | no |
| PPLI | reactions | no | no | no |
| PWR | reactions | no | no | no |
| RGC | reactions | no | no | no |
| RHM | reactions | no | no | no |
| RMS | reactions | no | no | no |
| ROVI | reactions | no | no | no |
| RRL | reactions | no | no | no |
| RVLV | reactions | no | no | no |
| RYTM | reactions | no | no | no |
| SANM | reactions | no | no | no |
| SBET | reactions | no | no | no |
| SITM | reactions | no | no | no |
| SKE | reactions | no | no | no |
| SM | reactions | no | no | no |
| SMTC | reactions | no | no | no |
| SNOW | reactions | no | no | no |
| SNPS | reactions | no | no | no |
| SOI | reactions | no | no | no |
| SSMR | reactions | no | no | no |
| STRL | reactions | yes | no | no |
| STX | reactions | no | no | no |
| SVM | reactions | no | no | no |
| TECN | reactions | no | no | no |
| TER | reactions | no | no | no |
| TLN | reactions | no | no | no |
| TNK | reactions | no | no | no |
| TPL | reactions | no | no | no |
| TREX | reactions | no | no | no |
| TRMB | reactions | no | no | no |
| TRUP | reactions | no | no | no |
| TSEM | reactions | no | no | no |
| TTMI | reactions | no | no | no |
| TXN | reactions | no | no | no |
| UBER | reactions | no | no | no |
| UCTT | reactions | no | no | no |
| ULCC | reactions | no | no | no |
| VAU | reactions | no | no | no |
| VCEL | reactions | yes | no | no |
| VET | reactions | no | no | no |
| VICR | reactions | yes | no | no |
| VRT | reactions | yes | no | no |
| VST | reactions | yes | no | no |
| VUL | reactions | no | no | no |
| WDC | reactions | no | no | no |
| WFC | reactions | no | no | no |
| WMB | reactions | no | no | no |
| WULF | reactions | yes | no | no |
| XETR | reactions | no | no | no |
| YUBICO | reactions | no | no | no |
| ZIP | reactions | no | no | no |
| ABNB | reminders | no | no | no |
| AEE | reminders | no | no | no |
| AKAM | reminders | no | no | no |
| APD | reminders | no | no | no |
| AU | reminders | no | no | no |
| AXON | reminders | no | no | no |
| BDX | reminders | yes | no | no |
| CAH | reminders | no | no | no |
| COP | reminders | no | no | no |
| CPT | reminders | no | no | no |
| DHL.DE | reminders | no | no | no |
| DTE.DE | reminders | no | no | no |
| DUK | reminders | no | no | no |
| DVN | reminders | no | no | no |
| ED | reminders | no | no | no |
| ENGI.PA | reminders | no | no | no |
| EOG | reminders | no | no | no |
| EVRG | reminders | no | no | no |
| FER | reminders | no | no | no |
| FNV | reminders | no | no | no |
| GPN | reminders | no | no | no |
| HEI | reminders | no | no | no |
| IRM | reminders | no | no | no |
| KMB | reminders | no | no | no |
| LICI.NS | reminders | no | no | no |
| LYV | reminders | no | no | no |
| MCHP | reminders | no | no | no |
| MNST | reminders | no | no | no |
| MQG.AX | reminders | no | no | no |
| MTD | reminders | no | no | no |
| NG.L | reminders | no | no | no |
| NTRA | reminders | no | no | no |
| REG | reminders | no | no | no |
| RHM.DE | reminders | no | no | no |
| RL | reminders | no | no | no |
| ROK | reminders | no | no | no |
| RVMD | reminders | no | no | no |
| SHL.DE | reminders | no | no | no |
| SLF | reminders | no | no | no |
| SO | reminders | no | no | no |
| SOLV | reminders | no | no | no |
| SPG | reminders | no | no | no |
| SRE | reminders | no | no | no |
| SREN.SW | reminders | no | no | no |
| TEAM | reminders | no | no | no |
| TEVA | reminders | no | no | no |
| TLT | reminders | no | no | no |
| TRGP | reminders | no | no | no |
| TRP | reminders | no | no | no |
| VRSK | reminders | no | no | no |
| VTRS | reminders | no | no | no |
| WCN | reminders | no | no | no |
| WPM | reminders | no | no | no |
| WYNN | reminders | no | no | no |
| ZTS | reminders | no | no | no |
| ARRY | screen | yes | no | yes |
| CRCT | screen | yes | no | yes |
| DUOL | screen | yes | yes | yes |
| HELE | screen | no | no | yes |
| KD | screen | yes | yes | yes |
| LIVN | screen | yes | yes | yes |
| VRDN | screen | yes | yes | yes |
| XNCR | screen | yes | yes | yes |
| XYZ | screen | yes | no | yes |
| YOU | screen | no | no | yes |

## Method and caveats

| Field | Value |
|---|---|
| Sources | 5 families, listed above |
| Ticker extraction | the first ticker-shaped cell of every markdown table row, and the ticker column of every CSV |
| Counts | per family, per name; a name can be in a family's set even if that family listed it in a table the reader would skip |

**What this does not say.** It does not say the routines are wrong, and it
does not say a name seen once is a better or worse setup. It says the repo
currently contains no artifact that would tell you either.

