# Confirmation — how many routines saw each name

**Source:** derived join over daily-screens/<date>/{tier-a,focus}.csv, ntrt/<date>.md, options-flow/<date>.md, earnings/<date>-{reminders,reactions}.md (no source file is modified) · **Built:** 2026-11-15 · **Covers:** 279 distinct name(s) across 5 routines; 1125 on the 200-name master board · read-only

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
| `options_flow` | the 16:35 unusual-options-flow screen | 36 |
| `reminders` | the 06:00 earnings-reminder watchlist | 16 |
| `reactions` | the 08:00 earnings-reaction scanner | 180 |
| `master board` | the 200-name screen output the tiers are cut from | 1125 |

The master board is not one of the five - it is the population the sweep's
tiers are cut from, and it is the baseline for how much overlap a
similarly-sized list would show by chance.

## Where the routines agree

| Pair | Shared names |
|---|---|
| options_flow & reactions | 10 — AMD, AVGO, CDE, CORZ, MU, NBIS, NVDA, ORCL, RGTI, SMR |
| gap_brief & options_flow | 5 — CRWV, GEVO, NBIS, NVDA, RGTI |
| gap_brief & reactions | 5 — IREN, NBIS, NVDA, RGTI, SNDK |
| screen & reactions | 4 — AAON, MARA, QNT, ZETA |
| screen & gap_brief | 1 — PEPG |
| screen & options_flow | 0 |
| screen & reminders | 0 |
| gap_brief & reminders | 0 |
| options_flow & reminders | 0 |
| reminders & reactions | 0 |

## How many routines saw each name

| Routines that saw the name | Names |
|---|---|
| 3 | 3 |
| 2 | 16 |
| 1 | 260 |

**19 of 279 name(s) were seen by two or more routines.** The rest were seen
by exactly one, and which one is in the table below.

## Names seen by more than one routine

| Ticker | Routines | On master board | Tier-A | Focus |
|---|---|---|---|---|
| NBIS | gap_brief, options_flow, reactions | yes | no | no |
| NVDA | gap_brief, options_flow, reactions | yes | no | no |
| RGTI | gap_brief, options_flow, reactions | yes | no | no |
| AAON | screen, reactions | yes | yes | yes |
| AMD | options_flow, reactions | yes | no | no |
| AVGO | options_flow, reactions | yes | no | no |
| CDE | options_flow, reactions | yes | no | no |
| CORZ | options_flow, reactions | yes | no | no |
| CRWV | gap_brief, options_flow | yes | no | no |
| GEVO | gap_brief, options_flow | yes | no | no |
| IREN | gap_brief, reactions | yes | no | no |
| MARA | screen, reactions | yes | no | yes |
| MU | options_flow, reactions | yes | no | no |
| ORCL | options_flow, reactions | yes | no | no |
| PEPG | screen, gap_brief | yes | no | yes |
| QNT | screen, reactions | yes | yes | yes |
| SMR | options_flow, reactions | yes | no | no |
| SNDK | gap_brief, reactions | yes | no | no |
| ZETA | screen, reactions | yes | yes | yes |

## Names seen by exactly one routine

| Ticker | Routine | On master board | Tier-A | Focus |
|---|---|---|---|---|
| ALC | gap_brief | yes | no | no |
| ARQQ | gap_brief | no | no | no |
| AUUD | gap_brief | no | no | no |
| BDMD | gap_brief | no | no | no |
| BMGL | gap_brief | no | no | no |
| BYAH | gap_brief | no | no | no |
| CANG | gap_brief | no | no | no |
| CDT | gap_brief | no | no | no |
| CHSN | gap_brief | no | no | no |
| DRTS | gap_brief | no | no | no |
| FOSL | gap_brief | yes | no | no |
| FRVO | gap_brief | yes | no | no |
| FTFT | gap_brief | no | no | no |
| GENK | gap_brief | no | no | no |
| HGTY | gap_brief | yes | no | no |
| HUHU | gap_brief | no | no | no |
| INLF | gap_brief | no | no | no |
| INVZ | gap_brief | no | no | no |
| IPDN | gap_brief | no | no | no |
| LWLG | gap_brief | yes | no | no |
| MGX | gap_brief | no | no | no |
| NRGV | gap_brief | yes | no | no |
| NXXT | gap_brief | no | no | no |
| NYAX | gap_brief | yes | no | no |
| OMH | gap_brief | no | no | no |
| PARA | gap_brief | no | no | no |
| PLPC | gap_brief | no | no | no |
| POET | gap_brief | yes | no | no |
| PRAX | gap_brief | yes | no | no |
| PRME | gap_brief | yes | no | no |
| PWCM | gap_brief | no | no | no |
| QXO | gap_brief | yes | no | no |
| RAYA | gap_brief | no | no | no |
| RCT | gap_brief | no | no | no |
| RSKD | gap_brief | yes | no | no |
| RUM | gap_brief | yes | no | no |
| SATL | gap_brief | yes | no | no |
| SFWL | gap_brief | no | no | no |
| SHFS | gap_brief | no | no | no |
| SMX | gap_brief | no | no | no |
| STAK | gap_brief | no | no | no |
| STIM | gap_brief | no | no | no |
| STXS | gap_brief | no | no | no |
| SUJA | gap_brief | no | no | no |
| TLSI | gap_brief | no | no | no |
| UONEK | gap_brief | no | no | no |
| VIVK | gap_brief | no | no | no |
| WRBY | gap_brief | yes | no | no |
| YMAT | gap_brief | no | no | no |
| **CALL** | options_flow | no | no | no |
| AAPL | options_flow | yes | no | no |
| ACHR | options_flow | yes | no | no |
| AMZN | options_flow | yes | no | no |
| APLD | options_flow | yes | no | no |
| AUR | options_flow | yes | no | no |
| BBD | options_flow | no | no | no |
| FRMI | options_flow | yes | no | no |
| GLD | options_flow | no | no | no |
| GOOGL | options_flow | yes | no | no |
| IWM | options_flow | no | no | no |
| MSFT | options_flow | yes | no | no |
| PBR | options_flow | yes | no | no |
| PLUG | options_flow | yes | no | no |
| QS | options_flow | yes | no | no |
| RIOT | options_flow | yes | no | no |
| SOFI | options_flow | yes | no | no |
| SPCX | options_flow | yes | no | no |
| STLA | options_flow | yes | no | no |
| TE | options_flow | yes | no | no |
| TLT | options_flow | no | no | no |
| TSLA | options_flow | yes | no | no |
| TTD | options_flow | yes | no | no |
| WULF | options_flow | yes | no | no |
| AAOI | reactions | yes | no | no |
| ABSI | reactions | no | no | no |
| ACCV | reactions | no | no | no |
| ADI | reactions | no | no | no |
| AIXA | reactions | no | no | no |
| AKAST | reactions | no | no | no |
| ALB | reactions | no | no | no |
| ALM | reactions | yes | no | no |
| AMAT | reactions | no | no | no |
| AMRC | reactions | yes | no | no |
| ANET | reactions | no | no | no |
| APH | reactions | yes | no | no |
| APR | reactions | no | no | no |
| ARIS | reactions | no | no | no |
| ASAN | reactions | yes | no | no |
| ASM | reactions | no | no | no |
| ASTS | reactions | yes | no | no |
| ATEC | reactions | no | no | no |
| ATRO | reactions | yes | no | no |
| ATS | reactions | no | no | no |
| AUGO | reactions | yes | no | no |
| AXTI | reactions | yes | no | no |
| AYA | reactions | no | no | no |
| BE | reactions | yes | no | no |
| BEAM | reactions | no | no | no |
| BESI | reactions | no | no | no |
| BICO | reactions | no | no | no |
| BWE | reactions | no | no | no |
| CAF | reactions | no | no | no |
| CAI | reactions | yes | no | no |
| CIFR | reactions | yes | no | no |
| CLSK | reactions | yes | no | no |
| COHR | reactions | yes | no | no |
| COTN | reactions | no | no | no |
| CRK | reactions | yes | no | no |
| CRSP | reactions | no | no | no |
| CRWD | reactions | yes | no | no |
| DELL | reactions | yes | no | no |
| DPC | reactions | yes | no | no |
| DVL | reactions | no | no | no |
| EGO | reactions | no | no | no |
| ELE | reactions | no | no | no |
| ELV | reactions | no | no | no |
| ENPH | reactions | yes | no | no |
| ENR | reactions | no | no | no |
| EQPT | reactions | yes | no | no |
| ERA | reactions | no | no | no |
| EROC | reactions | yes | no | no |
| ETN | reactions | no | no | no |
| ETOR | reactions | yes | no | no |
| FCX | reactions | yes | no | no |
| FIGR | reactions | yes | no | no |
| FLOMIC | reactions | no | no | no |
| FLS | reactions | yes | no | no |
| FN | reactions | yes | no | no |
| FNM | reactions | no | no | no |
| FPS | reactions | yes | no | no |
| FROG | reactions | yes | no | no |
| FTAI | reactions | yes | no | no |
| FUN | reactions | yes | no | no |
| GEV | reactions | yes | no | no |
| GLW | reactions | yes | no | no |
| GNS | reactions | no | no | no |
| HL | reactions | yes | no | no |
| HNSA | reactions | no | no | no |
| HRME | reactions | no | no | no |
| HUBN | reactions | no | no | no |
| HWM | reactions | yes | no | no |
| HYMC | reactions | no | no | no |
| IAG | reactions | no | no | no |
| IBKR | reactions | yes | no | no |
| ICOS | reactions | no | no | no |
| IE | reactions | no | no | no |
| IEL | reactions | no | no | no |
| IEP | reactions | no | no | no |
| IFCN | reactions | no | no | no |
| IFX | reactions | no | no | no |
| INGM | reactions | no | no | no |
| INIO | reactions | yes | no | no |
| INOD | reactions | yes | no | no |
| INTC | reactions | yes | no | no |
| JOBY | reactions | yes | no | no |
| KLAC | reactions | yes | no | no |
| KOMPL | reactions | no | no | no |
| LEU | reactions | yes | no | no |
| LIME | reactions | no | no | no |
| LRCX | reactions | yes | no | no |
| MANE | reactions | yes | no | no |
| MBLY | reactions | yes | no | no |
| MEL | reactions | no | no | no |
| MIM | reactions | no | no | no |
| MND | reactions | no | no | no |
| MRCY | reactions | yes | no | no |
| MRVL | reactions | yes | no | no |
| MTZ | reactions | yes | no | no |
| NASDAQ | reactions | no | no | no |
| NCAP | reactions | no | no | no |
| NESR | reactions | yes | no | no |
| NEWP | reactions | no | no | no |
| NN | reactions | no | no | no |
| NOVT | reactions | no | no | no |
| NSE | reactions | no | no | no |
| NTLA | reactions | yes | no | no |
| NTSK | reactions | yes | no | no |
| NXE | reactions | no | no | no |
| NXT | reactions | yes | no | no |
| NYSE | reactions | no | no | no |
| OKLO | reactions | yes | no | no |
| ONDS | reactions | yes | no | no |
| PANW | reactions | yes | no | no |
| PBF | reactions | yes | no | no |
| PGY | reactions | no | no | no |
| PLTR | reactions | yes | no | no |
| PS | reactions | no | no | no |
| PWR | reactions | yes | no | no |
| QBTS | reactions | yes | no | no |
| QCOM | reactions | yes | no | no |
| QLYS | reactions | yes | no | no |
| QUBT | reactions | yes | no | no |
| REGN | reactions | yes | no | no |
| REPL | reactions | yes | no | no |
| RGC | reactions | no | no | no |
| ROAD | reactions | yes | no | no |
| SA | reactions | no | no | no |
| SANM | reactions | yes | no | no |
| SCCO | reactions | no | no | no |
| SECZ | reactions | no | no | no |
| SEDG | reactions | yes | no | no |
| SENSO | reactions | no | no | no |
| SET | reactions | no | no | no |
| SGX | reactions | no | no | no |
| SHLS | reactions | yes | no | no |
| SIVE | reactions | no | no | no |
| SNOW | reactions | yes | no | no |
| SOI | reactions | no | no | no |
| SRL | reactions | no | no | no |
| SRPT | reactions | no | no | no |
| SRRK | reactions | no | no | no |
| SSE | reactions | no | no | no |
| SSRM | reactions | no | no | no |
| STX | reactions | yes | no | no |
| SVM | reactions | no | no | no |
| SZSE | reactions | no | no | no |
| TADAWUL | reactions | no | no | no |
| TDW | reactions | yes | no | no |
| TEM | reactions | yes | no | no |
| TENB | reactions | yes | no | no |
| THG | reactions | no | no | no |
| TPRO | reactions | no | no | no |
| TTMI | reactions | yes | no | no |
| TXN | reactions | yes | no | no |
| UEC | reactions | yes | no | no |
| USAR | reactions | yes | no | no |
| UUUU | reactions | yes | no | no |
| VLO | reactions | no | no | no |
| VOYG | reactions | no | no | no |
| VWS | reactions | no | no | no |
| WDC | reactions | yes | no | no |
| WMUU | reactions | no | no | no |
| WPM | reactions | no | no | no |
| XETR | reactions | no | no | no |
| XP | reactions | yes | no | no |
| XXI | reactions | no | no | no |
| YPSN | reactions | no | no | no |
| ABN.AS | reminders | no | no | no |
| AU | reminders | no | no | no |
| ENR.DE | reminders | no | no | no |
| EOAN.DE | reminders | no | no | no |
| FER | reminders | yes | no | no |
| FNV | reminders | no | no | no |
| NTRA | reminders | yes | no | no |
| POW.TO | reminders | no | no | no |
| RKT | reminders | yes | no | no |
| RVMD | reminders | yes | no | no |
| RWE.DE | reminders | no | no | no |
| TEVA | reminders | yes | no | no |
| TRI | reminders | no | no | no |
| UI | reminders | yes | no | no |
| VYLR | reminders | no | no | no |
| WCN | reminders | yes | no | no |
| BW | screen | yes | no | yes |
| CHTR | screen | yes | no | yes |
| GDYN | screen | yes | no | yes |
| HROW | screen | yes | no | yes |
| LQDA | screen | yes | yes | yes |
| LUMN | screen | yes | no | yes |
| TNGX | screen | yes | no | yes |

## Method and caveats

| Field | Value |
|---|---|
| Sources | 5 families, listed above |
| Ticker extraction | the first ticker-shaped cell of every markdown table row, and the ticker column of every CSV |
| Counts | per family, per name; a name can be in a family's set even if that family listed it in a table the reader would skip |

**What this does not say.** It does not say the routines are wrong, and it
does not say a name seen once is a better or worse setup. It says the repo
currently contains no artifact that would tell you either.

