# Confirmation — how many routines saw each name

**Source:** derived join over daily-screens/<date>/{tier-a,focus}.csv, ntrt/<date>.md, options-flow/<date>.md, earnings/<date>-{reminders,reactions}.md (no source file is modified) · **Built:** 2026-11-11 · **Covers:** 348 distinct name(s) across 5 routines; 200 on the 200-name master board · read-only

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
| `gap_brief` | the 09:00 pre-open gap brief (ntrt) | 57 |
| `options_flow` | the 16:35 unusual-options-flow screen | 44 |
| `reminders` | the 06:00 earnings-reminder watchlist | 25 |
| `reactions` | the 08:00 earnings-reaction scanner | 258 |
| `master board` | the 200-name screen output the tiers are cut from | 200 |

The master board is not one of the five - it is the population the sweep's
tiers are cut from, and it is the baseline for how much overlap a
similarly-sized list would show by chance.

## Where the routines agree

| Pair | Shared names |
|---|---|
| gap_brief & reactions | 20 — AAOI, ABNB, AEHR, AMD, AXTI, BE, CECO, DIOD, FLY, FROG |
| options_flow & reactions | 13 — AMD, AVGO, CIFR, CORZ, IONQ, IREN, MARA, MU, NFLX, NVDA |
| gap_brief & options_flow | 7 — AMD, CRWV, DKNG, IREN, MU, SMCI, WULF |
| options_flow & reminders | 6 — AAPL, AMZN, GLD, GOOGL, IWM, NVDA |
| reminders & reactions | 4 — BAM, CHTR, MRNA, NVDA |
| screen & reactions | 2 — MRNA, SEZL |
| screen & options_flow | 1 — JOBY |
| screen & reminders | 1 — MRNA |
| screen & gap_brief | 0 |
| gap_brief & reminders | 0 |

## How many routines saw each name

| Routines that saw the name | Names |
|---|---|
| 3 | 6 |
| 2 | 36 |
| 1 | 306 |

**42 of 348 name(s) were seen by two or more routines.** The rest were seen
by exactly one, and which one is in the table below.

## Names seen by more than one routine

| Ticker | Routines | On master board | Tier-A | Focus |
|---|---|---|---|---|
| AMD | gap_brief, options_flow, reactions | yes | no | no |
| IREN | gap_brief, options_flow, reactions | yes | no | no |
| MRNA | screen, reminders, reactions | yes | yes | yes |
| MU | gap_brief, options_flow, reactions | yes | no | no |
| NVDA | options_flow, reminders, reactions | no | no | no |
| WULF | gap_brief, options_flow, reactions | yes | no | no |
| AAOI | gap_brief, reactions | yes | no | no |
| AAPL | options_flow, reminders | no | no | no |
| ABNB | gap_brief, reactions | yes | no | no |
| AEHR | gap_brief, reactions | no | no | no |
| AMZN | options_flow, reminders | no | no | no |
| AVGO | options_flow, reactions | no | no | no |
| AXTI | gap_brief, reactions | yes | no | no |
| BAM | reminders, reactions | no | no | no |
| BE | gap_brief, reactions | no | no | no |
| CECO | gap_brief, reactions | no | no | no |
| CHTR | reminders, reactions | no | no | no |
| CIFR | options_flow, reactions | yes | no | no |
| CORZ | options_flow, reactions | yes | no | no |
| CRWV | gap_brief, options_flow | yes | no | no |
| DIOD | gap_brief, reactions | no | no | no |
| DKNG | gap_brief, options_flow | no | no | no |
| FLY | gap_brief, reactions | no | no | no |
| FROG | gap_brief, reactions | yes | no | no |
| GLD | options_flow, reminders | no | no | no |
| GOOGL | options_flow, reminders | no | no | no |
| IONQ | options_flow, reactions | yes | no | no |
| IWM | options_flow, reminders | no | no | no |
| JOBY | screen, options_flow | yes | no | yes |
| LASR | gap_brief, reactions | no | no | no |
| MARA | options_flow, reactions | yes | no | no |
| NBIS | gap_brief, reactions | yes | no | no |
| NFLX | options_flow, reactions | no | no | no |
| OKLO | gap_brief, reactions | yes | no | no |
| ORCL | options_flow, reactions | yes | no | no |
| PLPC | gap_brief, reactions | no | no | no |
| SEZL | screen, reactions | yes | yes | yes |
| SITM | gap_brief, reactions | no | no | no |
| SMCI | gap_brief, options_flow | yes | no | no |
| SNDK | gap_brief, reactions | yes | no | no |
| SPCX | options_flow, reactions | no | no | no |
| VCEL | gap_brief, reactions | yes | no | no |

## Names seen by exactly one routine

| Ticker | Routine | On master board | Tier-A | Focus |
|---|---|---|---|---|
| AEHL | gap_brief | no | no | no |
| ATER | gap_brief | no | no | no |
| BDMD | gap_brief | no | no | no |
| BDSX | gap_brief | no | no | no |
| BNC | gap_brief | no | no | no |
| CIIT | gap_brief | no | no | no |
| DBGI | gap_brief | no | no | no |
| DXY | gap_brief | no | no | no |
| EFXT | gap_brief | no | no | no |
| ETON | gap_brief | no | no | no |
| EVCM | gap_brief | no | no | no |
| FEAM | gap_brief | no | no | no |
| FIVN | gap_brief | no | no | no |
| FNKO | gap_brief | no | no | no |
| GAUZ | gap_brief | no | no | no |
| HIMS | gap_brief | yes | no | no |
| HRZN | gap_brief | no | no | no |
| INDI | gap_brief | no | no | no |
| KOP | gap_brief | no | no | no |
| KRT | gap_brief | no | no | no |
| KRUS | gap_brief | no | no | no |
| NRDS | gap_brief | no | no | no |
| NTRA | gap_brief | no | no | no |
| RCT | gap_brief | no | no | no |
| SHAZ | gap_brief | no | no | no |
| SITC | gap_brief | no | no | no |
| STLN | gap_brief | no | no | no |
| SXTP | gap_brief | no | no | no |
| TLSI | gap_brief | no | no | no |
| UA | gap_brief | no | no | no |
| UI | gap_brief | no | no | no |
| VIVK | gap_brief | no | no | no |
| VIX | gap_brief | no | no | no |
| WK | gap_brief | no | no | no |
| **CALL** | options_flow | no | no | no |
| **MIXED** | options_flow | no | no | no |
| **PUT** | options_flow | no | no | no |
| ASTS | options_flow | yes | no | no |
| BAC | options_flow | no | no | no |
| BBD | options_flow | no | no | no |
| GRAB | options_flow | yes | no | no |
| HTZ | options_flow | no | no | no |
| INO | options_flow | no | no | no |
| ITUB | options_flow | no | no | no |
| KEEL | options_flow | no | no | no |
| MCHP | options_flow | no | no | no |
| NU | options_flow | no | no | no |
| ONDS | options_flow | yes | no | no |
| RIOT | options_flow | yes | no | no |
| SMR | options_flow | yes | no | no |
| SNAP | options_flow | yes | no | no |
| SOFI | options_flow | no | no | no |
| SOUN | options_flow | yes | no | no |
| STLA | options_flow | no | no | no |
| TSLA | options_flow | no | no | no |
| VALE | options_flow | no | no | no |
| ABBV | reactions | no | no | no |
| ABSI | reactions | no | no | no |
| ACMR | reactions | no | no | no |
| ACN | reactions | no | no | no |
| ADBE | reactions | no | no | no |
| ADEA | reactions | no | no | no |
| ADI | reactions | no | no | no |
| ADP | reactions | no | no | no |
| AEIS | reactions | no | no | no |
| AF | reactions | no | no | no |
| AGI | reactions | no | no | no |
| AIXA | reactions | no | no | no |
| AKAST | reactions | no | no | no |
| ALAB | reactions | yes | no | no |
| ALGM | reactions | no | no | no |
| AMAT | reactions | no | no | no |
| AMGN | reactions | no | no | no |
| AMKR | reactions | no | no | no |
| AMPX | reactions | no | no | no |
| ANET | reactions | no | no | no |
| APH | reactions | no | no | no |
| APLD | reactions | yes | no | no |
| ARDT | reactions | yes | no | no |
| ASST | reactions | yes | no | no |
| ASX | reactions | yes | no | no |
| ATT | reactions | no | no | no |
| AZN | reactions | no | no | no |
| BELFA | reactions | no | no | no |
| BFLY | reactions | no | no | no |
| BKNG | reactions | no | no | no |
| BMY | reactions | no | no | no |
| BTDR | reactions | yes | no | no |
| CAI | reactions | yes | no | no |
| CAMBI | reactions | no | no | no |
| CBRS | reactions | yes | no | no |
| CEG | reactions | no | no | no |
| CGNX | reactions | no | no | no |
| CHRN | reactions | no | no | no |
| CIEN | reactions | no | no | no |
| CL | reactions | no | no | no |
| CLS | reactions | no | no | no |
| CLSK | reactions | yes | no | no |
| CMCSA | reactions | no | no | no |
| COHR | reactions | yes | no | no |
| COHU | reactions | no | no | no |
| COKE | reactions | no | no | no |
| COST | reactions | no | no | no |
| CRCT | reactions | no | no | no |
| CRDO | reactions | yes | no | no |
| CRM | reactions | no | no | no |
| CRWD | reactions | yes | no | no |
| DASH | reactions | yes | no | no |
| DELL | reactions | yes | no | no |
| DGII | reactions | no | no | no |
| DIG | reactions | no | no | no |
| DIS | reactions | no | no | no |
| DNO | reactions | no | no | no |
| DOCN | reactions | no | no | no |
| DOM | reactions | no | no | no |
| DUR | reactions | no | no | no |
| DVP | reactions | no | no | no |
| ELV | reactions | no | no | no |
| EMG | reactions | no | no | no |
| ENTG | reactions | no | no | no |
| ERAS | reactions | no | no | no |
| EROC | reactions | no | no | no |
| ETN | reactions | no | no | no |
| EUR | reactions | no | no | no |
| FFM | reactions | no | no | no |
| FIX | reactions | no | no | no |
| FLEX | reactions | yes | no | no |
| FN | reactions | no | no | no |
| FORM | reactions | no | no | no |
| FPS | reactions | yes | no | no |
| FRVO | reactions | yes | no | no |
| FSLY | reactions | yes | no | no |
| FTNT | reactions | no | no | no |
| GENB | reactions | no | no | no |
| GENI | reactions | no | no | no |
| GEV | reactions | no | no | no |
| GLW | reactions | yes | no | no |
| GNG | reactions | no | no | no |
| GOOGN | reactions | no | no | no |
| GRAL | reactions | yes | no | no |
| HAG | reactions | no | no | no |
| HAYPP | reactions | no | no | no |
| HD | reactions | no | no | no |
| HEX | reactions | no | no | no |
| HPE | reactions | yes | no | no |
| IBKR | reactions | no | no | no |
| IBRX | reactions | yes | no | no |
| ICHR | reactions | no | no | no |
| IESC | reactions | no | no | no |
| IGO | reactions | no | no | no |
| IMD | reactions | no | no | no |
| INFQ | reactions | yes | no | no |
| INOD | reactions | no | no | no |
| INTC | reactions | yes | no | no |
| INTU | reactions | no | no | no |
| IPGP | reactions | no | no | no |
| ISRG | reactions | no | no | no |
| JCI | reactions | no | no | no |
| KKR | reactions | no | no | no |
| KLAC | reactions | no | no | no |
| KLIC | reactions | no | no | no |
| LBRT | reactions | yes | no | no |
| LGN | reactions | no | no | no |
| LIFE | reactions | yes | no | no |
| LIN | reactions | no | no | no |
| LITE | reactions | yes | no | no |
| LRCX | reactions | yes | no | no |
| LUNR | reactions | yes | no | no |
| LYNX | reactions | no | no | no |
| MA | reactions | no | no | no |
| MCD | reactions | no | no | no |
| MDLZ | reactions | no | no | no |
| MDT | reactions | yes | no | no |
| MDV | reactions | no | no | no |
| MLX | reactions | no | no | no |
| MNST | reactions | no | no | no |
| MO | reactions | no | no | no |
| MOS | reactions | no | no | no |
| MPWR | reactions | no | no | no |
| MRVL | reactions | yes | no | no |
| MSB | reactions | no | no | no |
| MTSI | reactions | no | no | no |
| MXL | reactions | no | no | no |
| NVT | reactions | no | no | no |
| NVTS | reactions | yes | no | no |
| NWS | reactions | no | no | no |
| NXT | reactions | no | no | no |
| NYSE | reactions | no | no | no |
| OKTA | reactions | no | no | no |
| OMXSTO | reactions | no | no | no |
| ON | reactions | no | no | no |
| ONTO | reactions | no | no | no |
| OSL | reactions | no | no | no |
| OVH | reactions | no | no | no |
| PANW | reactions | yes | no | no |
| PENG | reactions | no | no | no |
| PEP | reactions | no | no | no |
| PFE | reactions | no | no | no |
| PG | reactions | no | no | no |
| PI | reactions | no | no | no |
| PKN | reactions | no | no | no |
| PLT | reactions | no | no | no |
| PLTR | reactions | yes | no | no |
| PM | reactions | no | no | no |
| PNR | reactions | no | no | no |
| POWI | reactions | no | no | no |
| POWL | reactions | yes | no | no |
| PRDO | reactions | no | no | no |
| PRIM | reactions | no | no | no |
| PWR | reactions | no | no | no |
| QBTS | reactions | yes | no | no |
| QCOM | reactions | no | no | no |
| QUBT | reactions | no | no | no |
| RACE | reactions | no | no | no |
| RAL | reactions | no | no | no |
| RBRK | reactions | no | no | no |
| RDW | reactions | yes | no | no |
| RELY | reactions | no | no | no |
| RGTI | reactions | yes | no | no |
| RKLB | reactions | yes | no | no |
| RMBS | reactions | no | no | no |
| ROK | reactions | no | no | no |
| RVMD | reactions | no | no | no |
| RYN | reactions | no | no | no |
| SDR | reactions | no | no | no |
| SEDG | reactions | no | no | no |
| SEI | reactions | yes | no | no |
| SFR | reactions | no | no | no |
| SGM | reactions | no | no | no |
| SHW | reactions | no | no | no |
| SIVE | reactions | no | no | no |
| SIX | reactions | no | no | no |
| SKS | reactions | no | no | no |
| SLS | reactions | yes | no | no |
| SLX | reactions | no | no | no |
| SMMT | reactions | no | no | no |
| SMTC | reactions | no | no | no |
| SNOW | reactions | no | no | no |
| SOFF | reactions | no | no | no |
| SPOT | reactions | no | no | no |
| SRL | reactions | no | no | no |
| STRA | reactions | no | no | no |
| STRL | reactions | no | no | no |
| STX | reactions | yes | no | no |
| SXE | reactions | no | no | no |
| SYK | reactions | no | no | no |
| TBCG | reactions | no | no | no |
| TEP | reactions | no | no | no |
| TER | reactions | yes | no | no |
| TGLS | reactions | no | no | no |
| TMUS | reactions | no | no | no |
| TRV | reactions | no | no | no |
| TSEM | reactions | no | no | no |
| TTAM | reactions | no | no | no |
| TTMI | reactions | yes | no | no |
| TWST | reactions | yes | no | no |
| TXG | reactions | yes | no | no |
| TXN | reactions | no | no | no |
| UCTT | reactions | no | no | no |
| UPBD | reactions | no | no | no |
| USB | reactions | no | no | no |
| VERX | reactions | no | no | no |
| VIAV | reactions | yes | no | no |
| VICR | reactions | no | no | no |
| VIE | reactions | no | no | no |
| VISN | reactions | no | no | no |
| VOYG | reactions | no | no | no |
| VRT | reactions | yes | no | no |
| VSAT | reactions | no | no | no |
| VSH | reactions | yes | no | no |
| VUL | reactions | no | no | no |
| VYX | reactions | yes | no | no |
| WBT | reactions | no | no | no |
| WDC | reactions | yes | no | no |
| WMT | reactions | yes | no | no |
| WOLF | reactions | no | no | no |
| WS | reactions | no | no | no |
| XE | reactions | yes | no | no |
| XETR | reactions | no | no | no |
| YUBICO | reactions | no | no | no |
| ZIP | reactions | no | no | no |
| AU | reminders | no | no | no |
| BEN | reminders | no | no | no |
| CSU.TO | reminders | no | no | no |
| ENB | reminders | no | no | no |
| FER | reminders | no | no | no |
| FNV | reminders | no | no | no |
| HUM | reminders | no | no | no |
| MSFT | reminders | no | no | no |
| PPL | reminders | no | no | no |
| RKT | reminders | yes | no | no |
| SLF | reminders | no | no | no |
| TEAM | reminders | no | no | no |
| TEVA | reminders | no | no | no |
| TLT | reminders | no | no | no |
| VST | reminders | no | no | no |
| WCN | reminders | no | no | no |
| ACHC | screen | yes | yes | yes |
| APP | screen | yes | yes | yes |
| FUN | screen | yes | yes | yes |
| RUN | screen | yes | yes | yes |
| U | screen | yes | yes | yes |
| VRDN | screen | yes | no | yes |
| WRBY | screen | yes | no | yes |
| XERS | screen | yes | yes | yes |
| XNCR | screen | yes | no | yes |

## Method and caveats

| Field | Value |
|---|---|
| Sources | 5 families, listed above |
| Ticker extraction | the first ticker-shaped cell of every markdown table row, and the ticker column of every CSV |
| Counts | per family, per name; a name can be in a family's set even if that family listed it in a table the reader would skip |

**What this does not say.** It does not say the routines are wrong, and it
does not say a name seen once is a better or worse setup. It says the repo
currently contains no artifact that would tell you either.

