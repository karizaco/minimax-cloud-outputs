# Confirmation — how many routines saw each name

**Source:** derived join over daily-screens/<date>/{tier-a,focus}.csv, ntrt/<date>.md, options-flow/<date>.md, earnings/<date>-{reminders,reactions}.md (no source file is modified) · **Built:** 2026-11-10 · **Covers:** 327 distinct name(s) across 5 routines; 200 on the 200-name master board · read-only

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
| `screen` | the 18:30 sweep - Tier-A and Focus | 19 |
| `gap_brief` | the 09:00 pre-open gap brief (ntrt) | 86 |
| `options_flow` | the 16:35 unusual-options-flow screen | 13 |
| `reminders` | the 06:00 earnings-reminder watchlist | 47 |
| `reactions` | the 08:00 earnings-reaction scanner | 213 |
| `master board` | the 200-name screen output the tiers are cut from | 200 |

The master board is not one of the five - it is the population the sweep's
tiers are cut from, and it is the baseline for how much overlap a
similarly-sized list would show by chance.

## Where the routines agree

| Pair | Shared names |
|---|---|
| gap_brief & reactions | 34 — AMZN, ANET, AXTI, BTDR, CBLL, CIFR, CLSK, CORZ, CRWV, DJT |
| screen & reactions | 9 — AEHR, APLD, CIFR, CLSK, CORZ, ECG, FN, FRVO, MRNA |
| screen & gap_brief | 3 — CIFR, CLSK, CORZ |
| gap_brief & reminders | 3 — DDOG, FIS, TRMB |
| reminders & reactions | 3 — CVS, EMR, MCD |
| options_flow & reactions | 2 — AMZN, MSFT |
| gap_brief & options_flow | 1 — AMZN |
| screen & options_flow | 0 |
| screen & reminders | 0 |
| options_flow & reminders | 0 |

## How many routines saw each name

| Routines that saw the name | Names |
|---|---|
| 3 | 4 |
| 2 | 43 |
| 1 | 280 |

**47 of 327 name(s) were seen by two or more routines.** The rest were seen
by exactly one, and which one is in the table below.

## Names seen by more than one routine

| Ticker | Routines | On master board | Tier-A | Focus |
|---|---|---|---|---|
| AMZN | gap_brief, options_flow, reactions | yes | no | no |
| CIFR | screen, gap_brief, reactions | yes | no | yes |
| CLSK | screen, gap_brief, reactions | yes | no | yes |
| CORZ | screen, gap_brief, reactions | yes | no | yes |
| AEHR | screen, reactions | yes | no | yes |
| ANET | gap_brief, reactions | no | no | no |
| APLD | screen, reactions | yes | no | yes |
| AXTI | gap_brief, reactions | no | no | no |
| BTDR | gap_brief, reactions | no | no | no |
| CBLL | gap_brief, reactions | no | no | no |
| CRWV | gap_brief, reactions | yes | no | no |
| CVS | reminders, reactions | no | no | no |
| DDOG | gap_brief, reminders | yes | no | no |
| DJT | gap_brief, reactions | no | no | no |
| DUOL | gap_brief, reactions | yes | no | no |
| ECG | screen, reactions | yes | no | yes |
| EMR | reminders, reactions | no | no | no |
| ENPH | gap_brief, reactions | no | no | no |
| FIS | gap_brief, reminders | no | no | no |
| FIX | gap_brief, reactions | yes | no | no |
| FLNC | gap_brief, reactions | no | no | no |
| FN | screen, reactions | yes | no | yes |
| FRVO | screen, reactions | yes | no | yes |
| GLXY | gap_brief, reactions | yes | no | no |
| HUT | gap_brief, reactions | yes | no | no |
| IREN | gap_brief, reactions | yes | no | no |
| KD | gap_brief, reactions | yes | no | no |
| LEN.B | gap_brief, reactions | no | no | no |
| LIME | gap_brief, reactions | no | no | no |
| MARA | gap_brief, reactions | yes | no | no |
| MCD | reminders, reactions | no | no | no |
| MRNA | screen, reactions | yes | yes | no |
| MSFT | options_flow, reactions | no | no | no |
| NBIS | gap_brief, reactions | no | no | no |
| NVTS | gap_brief, reactions | no | no | no |
| NYT | gap_brief, reactions | no | no | no |
| OC | gap_brief, reactions | no | no | no |
| ORCL | gap_brief, reactions | yes | no | no |
| OSCR | gap_brief, reactions | no | no | no |
| RUN | gap_brief, reactions | yes | no | no |
| SEDG | gap_brief, reactions | no | no | no |
| SHLS | gap_brief, reactions | yes | no | no |
| SNDK | gap_brief, reactions | no | no | no |
| SPCX | gap_brief, reactions | no | no | no |
| STRL | gap_brief, reactions | no | no | no |
| TRMB | gap_brief, reminders | no | no | no |
| TSLA | gap_brief, reactions | no | no | no |

## Names seen by exactly one routine

| Ticker | Routine | On master board | Tier-A | Focus |
|---|---|---|---|---|
| AAOI | gap_brief | no | no | no |
| ALAB | gap_brief | no | no | no |
| ALIT | gap_brief | no | no | no |
| ARRY | gap_brief | yes | no | no |
| ASM | gap_brief | no | no | no |
| AUDC | gap_brief | no | no | no |
| BLDP | gap_brief | no | no | no |
| BRKR | gap_brief | yes | no | no |
| CRCT | gap_brief | yes | no | no |
| CSIQ | gap_brief | no | no | no |
| DOX | gap_brief | no | no | no |
| EXK | gap_brief | no | no | no |
| FLYW | gap_brief | yes | no | no |
| FNV | gap_brief | no | no | no |
| FSLR | gap_brief | no | no | no |
| FTK | gap_brief | no | no | no |
| HELE | gap_brief | no | no | no |
| KODK | gap_brief | no | no | no |
| LIVN | gap_brief | yes | no | no |
| LMB | gap_brief | no | no | no |
| MOD | gap_brief | no | no | no |
| NFGC | gap_brief | no | no | no |
| NRIX | gap_brief | yes | no | no |
| NRP | gap_brief | no | no | no |
| OCGN | gap_brief | no | no | no |
| OPRT | gap_brief | no | no | no |
| OUST | gap_brief | yes | no | no |
| PLUG | gap_brief | no | no | no |
| PXED | gap_brief | no | no | no |
| RIOT | gap_brief | yes | no | no |
| RVLV | gap_brief | no | no | no |
| RWT | gap_brief | no | no | no |
| SCZM | gap_brief | no | no | no |
| SLDP | gap_brief | no | no | no |
| SMRT | gap_brief | no | no | no |
| SWKS | gap_brief | no | no | no |
| TBLA | gap_brief | no | no | no |
| TE | gap_brief | no | no | no |
| THM | gap_brief | no | no | no |
| TLRY | gap_brief | no | no | no |
| TOYO | gap_brief | no | no | no |
| TREX | gap_brief | yes | no | no |
| TRLV | gap_brief | no | no | no |
| UNM | gap_brief | no | no | no |
| USAS | gap_brief | no | no | no |
| USNA | gap_brief | no | no | no |
| VMET | gap_brief | no | no | no |
| VRDN | gap_brief | yes | no | no |
| VST | gap_brief | yes | no | no |
| AAPL | options_flow | yes | no | no |
| CALL | options_flow | no | no | no |
| DIA | options_flow | no | no | no |
| GLD | options_flow | no | no | no |
| GOOGL | options_flow | no | no | no |
| IWM | options_flow | no | no | no |
| NVDA | options_flow | no | no | no |
| PUT | options_flow | no | no | no |
| QQQ | options_flow | no | no | no |
| SPY | options_flow | no | no | no |
| TLT | options_flow | no | no | no |
| ABNB | reactions | no | no | no |
| ABT | reactions | no | no | no |
| ACN | reactions | no | no | no |
| ADP | reactions | no | no | no |
| AEM | reactions | no | no | no |
| AGX | reactions | yes | no | no |
| AIXA | reactions | no | no | no |
| ALHC | reactions | yes | no | no |
| ALK | reactions | no | no | no |
| AMGN | reactions | no | no | no |
| AMRC | reactions | no | no | no |
| AMRZ | reactions | no | no | no |
| ASKER | reactions | no | no | no |
| AUGO | reactions | no | no | no |
| AXP | reactions | no | no | no |
| AZN | reactions | no | no | no |
| BAM | reactions | no | no | no |
| BAX | reactions | no | no | no |
| BE | reactions | no | no | no |
| BEWI | reactions | no | no | no |
| BFLY | reactions | no | no | no |
| BINT | reactions | no | no | no |
| BJY | reactions | no | no | no |
| BMRN | reactions | no | no | no |
| BOUV | reactions | no | no | no |
| BUUU | reactions | yes | no | no |
| BX | reactions | no | no | no |
| CBK | reactions | no | no | no |
| CCEP | reactions | no | no | no |
| CEG | reactions | no | no | no |
| CGAU | reactions | no | no | no |
| CGEM | reactions | no | no | no |
| CHEF | reactions | no | no | no |
| CLS | reactions | no | no | no |
| CNQ | reactions | no | no | no |
| CRCL | reactions | no | no | no |
| CRDO | reactions | yes | no | no |
| CRM | reactions | no | no | no |
| DBK | reactions | no | no | no |
| DELL | reactions | no | no | no |
| DHI | reactions | no | no | no |
| DIS | reactions | no | no | no |
| DRTS | reactions | no | no | no |
| DT | reactions | no | no | no |
| DXC | reactions | no | no | no |
| EBS | reactions | no | no | no |
| ELE | reactions | no | no | no |
| ERO | reactions | no | no | no |
| EROC | reactions | yes | no | no |
| ETN | reactions | no | no | no |
| EU | reactions | no | no | no |
| EUR | reactions | no | no | no |
| FCX | reactions | no | no | no |
| FLEX | reactions | yes | no | no |
| FPS | reactions | yes | no | no |
| FTRE | reactions | no | no | no |
| GD | reactions | no | no | no |
| GEV | reactions | no | no | no |
| GILD | reactions | no | no | no |
| GLW | reactions | no | no | no |
| HCA | reactions | yes | no | no |
| HD | reactions | no | no | no |
| HEI | reactions | no | no | no |
| HOC | reactions | no | no | no |
| IBTA | reactions | yes | no | no |
| INBX | reactions | no | no | no |
| INIO | reactions | yes | no | no |
| INSM | reactions | no | no | no |
| INTC | reactions | yes | no | no |
| INTU | reactions | no | no | no |
| IOVA | reactions | no | no | no |
| IP | reactions | no | no | no |
| ISRG | reactions | yes | no | no |
| IT | reactions | no | no | no |
| JNJ | reactions | no | no | no |
| KEOC | reactions | no | no | no |
| KGC | reactions | no | no | no |
| LBTYA | reactions | yes | no | no |
| LDOS | reactions | no | no | no |
| LEN | reactions | no | no | no |
| LINK | reactions | no | no | no |
| LKQ | reactions | no | no | no |
| LLY | reactions | no | no | no |
| LMT | reactions | no | no | no |
| LOW | reactions | no | no | no |
| LZ | reactions | no | no | no |
| MAR | reactions | no | no | no |
| MGA | reactions | no | no | no |
| MMM | reactions | yes | no | no |
| MMT | reactions | no | no | no |
| MOS | reactions | no | no | no |
| MPC | reactions | no | no | no |
| MRVL | reactions | yes | no | no |
| MTRO | reactions | no | no | no |
| MU | reactions | no | no | no |
| MYRG | reactions | yes | no | no |
| NASDAQ | reactions | no | no | no |
| NEE | reactions | no | no | no |
| NEM | reactions | no | no | no |
| NFLX | reactions | no | no | no |
| NOBI | reactions | no | no | no |
| NVT | reactions | yes | no | no |
| NXT | reactions | yes | no | no |
| NYSE | reactions | no | no | no |
| OHB | reactions | no | no | no |
| OMXSTO | reactions | no | no | no |
| ORRON | reactions | no | no | no |
| PAGS | reactions | no | no | no |
| PEP | reactions | no | no | no |
| PFGC | reactions | yes | no | no |
| PHM | reactions | no | no | no |
| PLPC | reactions | no | no | no |
| PLTR | reactions | no | no | no |
| PNC | reactions | no | no | no |
| PNDORA | reactions | no | no | no |
| POWI | reactions | no | no | no |
| POWL | reactions | yes | no | no |
| PWR | reactions | yes | no | no |
| RAL | reactions | no | no | no |
| RBI | reactions | no | no | no |
| RCUS | reactions | no | no | no |
| REGN | reactions | no | no | no |
| RH | reactions | no | no | no |
| RRX | reactions | yes | no | no |
| RTX | reactions | no | no | no |
| RUG | reactions | no | no | no |
| RVTY | reactions | no | no | no |
| SCCO | reactions | no | no | no |
| SEI | reactions | yes | no | no |
| SEZL | reactions | yes | no | no |
| SHW | reactions | no | no | no |
| SMG | reactions | no | no | no |
| SMMT | reactions | yes | no | no |
| SMTC | reactions | no | no | no |
| SNDX | reactions | no | no | no |
| SNOW | reactions | no | no | no |
| SOI | reactions | no | no | no |
| SOLS | reactions | no | no | no |
| SRAD | reactions | no | no | no |
| STDN | reactions | no | no | no |
| STX | reactions | no | no | no |
| SYK | reactions | no | no | no |
| TH | reactions | no | no | no |
| TJX | reactions | no | no | no |
| TLN | reactions | yes | no | no |
| TMUS | reactions | no | no | no |
| TRV | reactions | no | no | no |
| TWST | reactions | no | no | no |
| UBS | reactions | no | no | no |
| ULCC | reactions | no | no | no |
| UNH | reactions | no | no | no |
| VERX | reactions | no | no | no |
| VRT | reactions | yes | no | no |
| VRTX | reactions | no | no | no |
| VSH | reactions | no | no | no |
| VZ | reactions | no | no | no |
| WCC | reactions | no | no | no |
| WDC | reactions | yes | no | no |
| WEIR | reactions | no | no | no |
| WGS | reactions | no | no | no |
| WLK | reactions | no | no | no |
| WMT | reactions | no | no | no |
| WRBY | reactions | no | no | no |
| WULF | reactions | yes | no | no |
| WY | reactions | no | no | no |
| XETR | reactions | no | no | no |
| XPEL | reactions | no | no | no |
| ZAP | reactions | no | no | no |
| ZG | reactions | yes | no | no |
| AFL | reminders | no | no | no |
| ALB | reminders | no | no | no |
| ALL | reminders | no | no | no |
| AMCR | reminders | no | no | no |
| APA | reminders | no | no | no |
| APP | reminders | no | no | no |
| ARM | reminders | no | no | no |
| ATO | reminders | no | no | no |
| CDW | reminders | yes | no | no |
| CF | reminders | no | no | no |
| COHR | reminders | no | no | no |
| COR | reminders | no | no | no |
| CPAY | reminders | no | no | no |
| CRL | reminders | no | no | no |
| CVE | reminders | no | no | no |
| ES | reminders | no | no | no |
| EW | reminders | no | no | no |
| EXPE | reminders | yes | no | no |
| FICO | reminders | yes | no | no |
| GWW | reminders | no | no | no |
| HST | reminders | no | no | no |
| KHC | reminders | no | no | no |
| MCK | reminders | no | no | no |
| MELI | reminders | no | no | no |
| MET | reminders | no | no | no |
| MFC | reminders | no | no | no |
| MLM | reminders | no | no | no |
| MSI | reminders | no | no | no |
| NWS | reminders | no | no | no |
| NWSA | reminders | no | no | no |
| PODD | reminders | yes | no | no |
| PTC | reminders | no | no | no |
| QCOM | reminders | no | no | no |
| STE | reminders | no | no | no |
| SWK | reminders | yes | no | no |
| TECH | reminders | no | no | no |
| TKO | reminders | no | no | no |
| TPL | reminders | yes | no | no |
| UBER | reminders | no | no | no |
| VMRK | reminders | no | no | no |
| ZBH | reminders | yes | no | no |
| AEIS | screen | yes | no | yes |
| BETA | screen | yes | no | yes |
| CDNA | screen | yes | yes | no |
| EVER | screen | yes | no | yes |
| FISV | screen | yes | yes | yes |
| FTAI | screen | yes | yes | no |
| GKOS | screen | yes | yes | no |
| GPK | screen | yes | yes | no |
| KVYO | screen | yes | yes | no |
| LSCC | screen | yes | yes | no |

## Method and caveats

| Field | Value |
|---|---|
| Sources | 5 families, listed above |
| Ticker extraction | the first ticker-shaped cell of every markdown table row, and the ticker column of every CSV |
| Counts | per family, per name; a name can be in a family's set even if that family listed it in a table the reader would skip |

**What this does not say.** It does not say the routines are wrong, and it
does not say a name seen once is a better or worse setup. It says the repo
currently contains no artifact that would tell you either.

