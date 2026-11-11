# Confirmation — how many routines saw each name

**Source:** derived join over daily-screens/<date>/{tier-a,focus}.csv, ntrt/<date>.md, options-flow/<date>.md, earnings/<date>-{reminders,reactions}.md (no source file is modified) · **Built:** 2026-11-11 · **Covers:** 244 distinct name(s) across 5 routines; 1356 on the 200-name master board · read-only

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
| `gap_brief` | the 09:00 pre-open gap brief (ntrt) | 66 |
| `options_flow` | the 16:35 unusual-options-flow screen | 38 |
| `reminders` | the 06:00 earnings-reminder watchlist | 10 |
| `reactions` | the 08:00 earnings-reaction scanner | 134 |
| `master board` | the 200-name screen output the tiers are cut from | 1356 |

The master board is not one of the five - it is the population the sweep's
tiers are cut from, and it is the baseline for how much overlap a
similarly-sized list would show by chance.

## Where the routines agree

| Pair | Shared names |
|---|---|
| gap_brief & reactions | 5 — APP, APPS, RKLB, SNDK, TTD |
| screen & reactions | 4 — LUNR, MPWR, PL, TTD |
| gap_brief & options_flow | 4 — PEPG, QBTS, RKLB, TTD |
| options_flow & reactions | 4 — ASTS, RKLB, SPCX, TTD |
| screen & gap_brief | 2 — BW, TTD |
| screen & options_flow | 1 — TTD |
| screen & reminders | 0 |
| gap_brief & reminders | 0 |
| options_flow & reminders | 0 |
| reminders & reactions | 0 |

## How many routines saw each name

| Routines that saw the name | Names |
|---|---|
| 4 | 1 |
| 3 | 1 |
| 2 | 11 |
| 1 | 231 |

**13 of 244 name(s) were seen by two or more routines.** The rest were seen
by exactly one, and which one is in the table below.

## Names seen by more than one routine

| Ticker | Routines | On master board | Tier-A | Focus |
|---|---|---|---|---|
| TTD | screen, gap_brief, options_flow, reactions | yes | no | yes |
| RKLB | gap_brief, options_flow, reactions | yes | no | no |
| APP | gap_brief, reactions | yes | no | no |
| APPS | gap_brief, reactions | yes | no | no |
| ASTS | options_flow, reactions | yes | no | no |
| BW | screen, gap_brief | yes | no | yes |
| LUNR | screen, reactions | yes | no | yes |
| MPWR | screen, reactions | yes | no | yes |
| PEPG | gap_brief, options_flow | no | no | no |
| PL | screen, reactions | yes | no | yes |
| QBTS | gap_brief, options_flow | yes | no | no |
| SNDK | gap_brief, reactions | yes | no | no |
| SPCX | options_flow, reactions | yes | no | no |

## Names seen by exactly one routine

| Ticker | Routine | On master board | Tier-A | Focus |
|---|---|---|---|---|
| ACHC | gap_brief | yes | no | no |
| ADGM | gap_brief | no | no | no |
| ADUR | gap_brief | no | no | no |
| CISS | gap_brief | no | no | no |
| CSQR | gap_brief | yes | no | no |
| DBGI | gap_brief | no | no | no |
| DXST | gap_brief | no | no | no |
| EJH | gap_brief | no | no | no |
| EMAT | gap_brief | no | no | no |
| ETD | gap_brief | no | no | no |
| ETOR | gap_brief | no | no | no |
| FA | gap_brief | yes | no | no |
| FCNCP | gap_brief | no | no | no |
| FF | gap_brief | no | no | no |
| FUN | gap_brief | yes | no | no |
| GFL | gap_brief | yes | no | no |
| GILT | gap_brief | no | no | no |
| GRPN | gap_brief | yes | no | no |
| HROW | gap_brief | yes | no | no |
| HTOO | gap_brief | no | no | no |
| IHRT | gap_brief | no | no | no |
| JBI | gap_brief | no | no | no |
| JDZG | gap_brief | no | no | no |
| KLTR | gap_brief | no | no | no |
| KPTI | gap_brief | no | no | no |
| LICN | gap_brief | no | no | no |
| MI | gap_brief | no | no | no |
| MNDO | gap_brief | no | no | no |
| MRNA | gap_brief | yes | no | no |
| MVST | gap_brief | no | no | no |
| NFGC | gap_brief | no | no | no |
| NTCL | gap_brief | no | no | no |
| OGG | gap_brief | no | no | no |
| PARA | gap_brief | no | no | no |
| PHOE | gap_brief | no | no | no |
| PXLW | gap_brief | no | no | no |
| QMCO | gap_brief | yes | no | no |
| ROC | gap_brief | no | no | no |
| RUBI | gap_brief | no | no | no |
| RUN | gap_brief | yes | no | no |
| SECZ | gap_brief | yes | no | no |
| SENS | gap_brief | yes | no | no |
| SEV | gap_brief | no | no | no |
| SEZL | gap_brief | yes | no | no |
| SKYE | gap_brief | no | no | no |
| SMA | gap_brief | no | no | no |
| SMX | gap_brief | no | no | no |
| TGE | gap_brief | no | no | no |
| THRY | gap_brief | no | no | no |
| TLSI | gap_brief | no | no | no |
| TTEC | gap_brief | no | no | no |
| UONEK | gap_brief | no | no | no |
| VIVK | gap_brief | no | no | no |
| WFF | gap_brief | no | no | no |
| WYFI | gap_brief | no | no | no |
| XERS | gap_brief | yes | no | no |
| YFOR | gap_brief | no | no | no |
| ZJYL | gap_brief | no | no | no |
| **CALL** | options_flow | no | no | no |
| AAL | options_flow | yes | no | no |
| AAPL | options_flow | yes | no | no |
| ACHR | options_flow | yes | no | no |
| AMD | options_flow | yes | no | no |
| AMZN | options_flow | yes | no | no |
| AUR | options_flow | yes | no | no |
| AVGO | options_flow | yes | no | no |
| BBD | options_flow | no | no | no |
| CDE | options_flow | yes | no | no |
| CRWV | options_flow | yes | no | no |
| DBX | options_flow | yes | no | no |
| DNN | options_flow | yes | no | no |
| GLD | options_flow | no | no | no |
| GOOGL | options_flow | yes | no | no |
| HIMS | options_flow | yes | no | no |
| IWM | options_flow | no | no | no |
| JHX | options_flow | yes | no | no |
| LCID | options_flow | yes | no | no |
| MARA | options_flow | yes | no | no |
| MSFT | options_flow | yes | no | no |
| MU | options_flow | yes | no | no |
| NFLX | options_flow | yes | no | no |
| NU | options_flow | yes | no | no |
| NVDA | options_flow | yes | no | no |
| PFE | options_flow | yes | no | no |
| PLUG | options_flow | yes | no | no |
| RIG | options_flow | yes | no | no |
| RIOT | options_flow | yes | no | no |
| SMR | options_flow | yes | no | no |
| SOFI | options_flow | yes | no | no |
| VALE | options_flow | yes | no | no |
| AAON | reactions | yes | no | no |
| AEHR | reactions | yes | no | no |
| AEM | reactions | yes | no | no |
| ASX | reactions | yes | no | no |
| ATEN | reactions | no | no | no |
| AUGO | reactions | yes | no | no |
| AUSS | reactions | no | no | no |
| AVAV | reactions | yes | no | no |
| AXTI | reactions | yes | no | no |
| AYA | reactions | yes | no | no |
| AZT | reactions | no | no | no |
| BE | reactions | yes | no | no |
| BICO | reactions | no | no | no |
| BTDR | reactions | yes | no | no |
| CEG | reactions | yes | no | no |
| CGS | reactions | no | no | no |
| CIA | reactions | no | no | no |
| CIEN | reactions | yes | no | no |
| CLMT | reactions | yes | no | no |
| CLSK | reactions | yes | no | no |
| COA | reactions | no | no | no |
| COHR | reactions | yes | no | no |
| DOW | reactions | no | no | no |
| ECG | reactions | yes | no | no |
| EDEN | reactions | no | no | no |
| ELG | reactions | no | no | no |
| ELPE | reactions | no | no | no |
| ENTG | reactions | yes | no | no |
| EROC | reactions | no | no | no |
| ETN | reactions | no | no | no |
| FDC | reactions | no | no | no |
| FG | reactions | yes | no | no |
| FLR | reactions | no | no | no |
| FLY | reactions | yes | no | no |
| FN | reactions | yes | no | no |
| FOUR | reactions | yes | no | no |
| FPS | reactions | yes | no | no |
| GENO | reactions | no | no | no |
| GEV | reactions | yes | no | no |
| GLW | reactions | yes | no | no |
| GNS | reactions | no | no | no |
| GOMX | reactions | no | no | no |
| HEX | reactions | no | no | no |
| HUNT | reactions | no | no | no |
| HYMC | reactions | yes | no | no |
| IMD | reactions | no | no | no |
| INFQ | reactions | yes | no | no |
| INTC | reactions | yes | no | no |
| IONQ | reactions | yes | no | no |
| KEOC | reactions | no | no | no |
| KOMPL | reactions | no | no | no |
| LEU | reactions | yes | no | no |
| LIF | reactions | no | no | no |
| LITE | reactions | yes | no | no |
| LRCX | reactions | yes | no | no |
| MAD | reactions | no | no | no |
| MKSI | reactions | yes | no | no |
| MLX | reactions | no | no | no |
| MMK | reactions | no | no | no |
| MND | reactions | no | no | no |
| MOD | reactions | yes | no | no |
| MPC | reactions | yes | no | no |
| MRVL | reactions | yes | no | no |
| MTSI | reactions | yes | no | no |
| MXL | reactions | yes | no | no |
| NBIS | reactions | yes | no | no |
| NEM | reactions | no | no | no |
| NTG | reactions | no | no | no |
| NVTS | reactions | yes | no | no |
| NWH | reactions | no | no | no |
| NXL | reactions | no | no | no |
| NYSE | reactions | no | no | no |
| OBM | reactions | no | no | no |
| OKLO | reactions | yes | no | no |
| OMXCOP | reactions | no | no | no |
| OMXHEX | reactions | no | no | no |
| OMXSTO | reactions | no | no | no |
| ONDS | reactions | yes | no | no |
| ONTO | reactions | yes | no | no |
| OPTIMA | reactions | no | no | no |
| OUST | reactions | yes | no | no |
| OVZON | reactions | no | no | no |
| PDN | reactions | no | no | no |
| PENG | reactions | yes | no | no |
| PLT | reactions | no | no | no |
| PPTA | reactions | no | no | no |
| PWR | reactions | yes | no | no |
| QAN | reactions | no | no | no |
| QUBT | reactions | yes | no | no |
| RDW | reactions | yes | no | no |
| RGTI | reactions | yes | no | no |
| ROSE | reactions | no | no | no |
| SANM | reactions | yes | no | no |
| SEI | reactions | yes | no | no |
| SG | reactions | yes | no | no |
| SHA | reactions | no | no | no |
| SKS | reactions | no | no | no |
| SKYD | reactions | yes | no | no |
| SLC | reactions | no | no | no |
| SMCRT | reactions | no | no | no |
| SMTC | reactions | yes | no | no |
| SOLS | reactions | no | no | no |
| SRG | reactions | no | no | no |
| SRPT | reactions | no | no | no |
| SRRK | reactions | yes | no | no |
| STX | reactions | yes | no | no |
| SVM | reactions | yes | no | no |
| SXE | reactions | no | no | no |
| TEM | reactions | yes | no | no |
| TER | reactions | yes | no | no |
| TPW | reactions | no | no | no |
| TRLV | reactions | no | no | no |
| TTMI | reactions | yes | no | no |
| TTWO | reactions | yes | no | no |
| UBS | reactions | no | no | no |
| VIAV | reactions | yes | no | no |
| VICR | reactions | yes | no | no |
| VOYG | reactions | no | no | no |
| VRT | reactions | yes | no | no |
| VUL | reactions | no | no | no |
| WBT | reactions | no | no | no |
| WIX | reactions | yes | no | no |
| WOLF | reactions | yes | no | no |
| XETR | reactions | no | no | no |
| FER | reminders | yes | no | no |
| HEI | reminders | no | no | no |
| NTRA | reminders | yes | no | no |
| RKT | reminders | yes | no | no |
| SE.SI | reminders | no | no | no |
| SLF | reminders | no | no | no |
| TDG | reminders | no | no | no |
| TRI | reminders | no | no | no |
| UI | reminders | yes | no | no |
| WCN | reminders | no | no | no |
| FRVO | screen | yes | yes | yes |
| IAM | screen | yes | no | yes |
| IMVT | screen | yes | no | yes |
| PRAX | screen | yes | yes | yes |
| QXO | screen | yes | yes | yes |
| TLS | screen | yes | no | yes |
| WRBY | screen | yes | yes | yes |

## Method and caveats

| Field | Value |
|---|---|
| Sources | 5 families, listed above |
| Ticker extraction | the first ticker-shaped cell of every markdown table row, and the ticker column of every CSV |
| Counts | per family, per name; a name can be in a family's set even if that family listed it in a table the reader would skip |

**What this does not say.** It does not say the routines are wrong, and it
does not say a name seen once is a better or worse setup. It says the repo
currently contains no artifact that would tell you either.

