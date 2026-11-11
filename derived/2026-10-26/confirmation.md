# Confirmation — how many routines saw each name

**Source:** derived join over daily-screens/<date>/{tier-a,focus}.csv, ntrt/<date>.md, options-flow/<date>.md, earnings/<date>-{reminders,reactions}.md (no source file is modified) · **Built:** 2026-11-11 · **Covers:** 165 distinct name(s) across 5 routines; 200 on the 200-name master board · read-only

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
| `gap_brief` | the 09:00 pre-open gap brief (ntrt) | 40 |
| `options_flow` | the 16:35 unusual-options-flow screen | 9 |
| `reminders` | the 06:00 earnings-reminder watchlist | 12 |
| `reactions` | the 08:00 earnings-reaction scanner | 98 |
| `master board` | the 200-name screen output the tiers are cut from | 200 |

The master board is not one of the five - it is the population the sweep's
tiers are cut from, and it is the baseline for how much overlap a
similarly-sized list would show by chance.

## Where the routines agree

| Pair | Shared names |
|---|---|
| gap_brief & reactions | 5 — AGBK, INTR, MELI, RRC, XP |
| reminders & reactions | 1 — CLS |
| screen & gap_brief | 0 |
| screen & options_flow | 0 |
| screen & reminders | 0 |
| screen & reactions | 0 |
| gap_brief & options_flow | 0 |
| gap_brief & reminders | 0 |
| options_flow & reminders | 0 |
| options_flow & reactions | 0 |

## How many routines saw each name

| Routines that saw the name | Names |
|---|---|
| 2 | 6 |
| 1 | 159 |

**6 of 165 name(s) were seen by two or more routines.** The rest were seen
by exactly one, and which one is in the table below.

## Names seen by more than one routine

| Ticker | Routines | On master board | Tier-A | Focus |
|---|---|---|---|---|
| AGBK | gap_brief, reactions | no | no | no |
| CLS | reminders, reactions | no | no | no |
| INTR | gap_brief, reactions | no | no | no |
| MELI | gap_brief, reactions | no | no | no |
| RRC | gap_brief, reactions | yes | no | no |
| XP | gap_brief, reactions | yes | no | no |

## Names seen by exactly one routine

| Ticker | Routine | On master board | Tier-A | Focus |
|---|---|---|---|---|
| **AFYA** | gap_brief | no | no | no |
| **AGBK** | gap_brief | no | no | no |
| **ARCO** | gap_brief | no | no | no |
| **BRAI** | gap_brief | no | no | no |
| **DLO** | gap_brief | no | no | no |
| **INTR** | gap_brief | no | no | no |
| **LYCA** | gap_brief | no | no | no |
| **MELI** | gap_brief | no | no | no |
| **NU** | gap_brief | no | no | no |
| **PAGS** | gap_brief | no | no | no |
| **PAX** | gap_brief | no | no | no |
| **PICS** | gap_brief | no | no | no |
| **RRC** | gap_brief | no | no | no |
| **SGRY** | gap_brief | no | no | no |
| **SSII** | gap_brief | no | no | no |
| **STNE** | gap_brief | no | no | no |
| **VINP** | gap_brief | no | no | no |
| **VTEX** | gap_brief | no | no | no |
| **XNCR** | gap_brief | no | no | no |
| **XP** | gap_brief | no | no | no |
| AFYA | gap_brief | no | no | no |
| ARCO | gap_brief | no | no | no |
| BRAI | gap_brief | no | no | no |
| DLO | gap_brief | no | no | no |
| LYCA | gap_brief | no | no | no |
| NU | gap_brief | no | no | no |
| PAGS | gap_brief | no | no | no |
| PAX | gap_brief | no | no | no |
| PICS | gap_brief | no | no | no |
| SGRY | gap_brief | yes | no | no |
| SSII | gap_brief | no | no | no |
| STNE | gap_brief | yes | no | no |
| VINP | gap_brief | no | no | no |
| VTEX | gap_brief | no | no | no |
| XNCR | gap_brief | yes | no | no |
| AAPL | options_flow | yes | no | no |
| AMZN | options_flow | yes | no | no |
| CBOE | options_flow | no | no | no |
| GLD | options_flow | no | no | no |
| GOOGL | options_flow | no | no | no |
| IWM | options_flow | no | no | no |
| MSFT | options_flow | yes | no | no |
| NVDA | options_flow | yes | no | no |
| TLT | options_flow | no | no | no |
| ABCL | reactions | yes | no | no |
| ADPT | reactions | yes | no | no |
| ALGT | reactions | no | no | no |
| ALLEI | reactions | no | no | no |
| AOF | reactions | no | no | no |
| APA | reactions | no | no | no |
| APE | reactions | no | no | no |
| ASX | reactions | no | no | no |
| ATEN | reactions | no | no | no |
| AVBP | reactions | no | no | no |
| BE | reactions | yes | no | no |
| BFG | reactions | no | no | no |
| BFIT | reactions | no | no | no |
| BITTI | reactions | no | no | no |
| BMN | reactions | no | no | no |
| BOE | reactions | no | no | no |
| BTDR | reactions | yes | no | no |
| BTE | reactions | no | no | no |
| BWE | reactions | no | no | no |
| CCC | reactions | yes | no | no |
| COHU | reactions | no | no | no |
| CRGY | reactions | no | no | no |
| CTD | reactions | no | no | no |
| CVL | reactions | no | no | no |
| CYL | reactions | no | no | no |
| DGT | reactions | no | no | no |
| DNORD | reactions | no | no | no |
| DVN | reactions | no | no | no |
| ELV | reactions | no | no | no |
| FFM | reactions | no | no | no |
| FIX | reactions | yes | no | no |
| FORM | reactions | no | no | no |
| FRO | reactions | yes | no | no |
| FRVIA | reactions | no | no | no |
| GALP | reactions | no | no | no |
| GGP | reactions | no | no | no |
| GMAB | reactions | no | no | no |
| GTT | reactions | no | no | no |
| INA | reactions | no | no | no |
| KCC | reactions | no | no | no |
| KLAC | reactions | no | no | no |
| LRCX | reactions | no | no | no |
| LYC | reactions | no | no | no |
| MCAP | reactions | no | no | no |
| MDATA | reactions | no | no | no |
| MGM | reactions | no | no | no |
| MLX | reactions | no | no | no |
| MRNA | reactions | yes | no | no |
| MRVI | reactions | no | no | no |
| MU | reactions | yes | no | no |
| NANO | reactions | no | no | no |
| NASDAQ | reactions | no | no | no |
| NCOD | reactions | no | no | no |
| NEM | reactions | no | no | no |
| NEU | reactions | no | no | no |
| NN | reactions | yes | no | no |
| NTG | reactions | no | no | no |
| OBM | reactions | no | no | no |
| OHB | reactions | no | no | no |
| OMXCOP | reactions | no | no | no |
| OMXSTO | reactions | no | no | no |
| ORIC | reactions | no | no | no |
| ORNAV | reactions | no | no | no |
| OTEC | reactions | no | no | no |
| PBF | reactions | yes | no | no |
| PBLS | reactions | no | no | no |
| PDI | reactions | no | no | no |
| PEN | reactions | no | no | no |
| PLS | reactions | no | no | no |
| PNR | reactions | no | no | no |
| PSX | reactions | no | no | no |
| RGC | reactions | no | no | no |
| RIG | reactions | no | no | no |
| RRL | reactions | no | no | no |
| RSG | reactions | no | no | no |
| SDRL | reactions | no | no | no |
| SM | reactions | no | no | no |
| SMTC | reactions | yes | no | no |
| SNDK | reactions | no | no | no |
| TALO | reactions | no | no | no |
| TDW | reactions | no | no | no |
| TPW | reactions | no | no | no |
| TSLA | reactions | yes | no | no |
| TUA | reactions | no | no | no |
| VET | reactions | no | no | no |
| VG | reactions | yes | no | no |
| VLO | reactions | no | no | no |
| WAF | reactions | no | no | no |
| WGS | reactions | yes | no | no |
| WTTR | reactions | no | no | no |
| YUBICO | reactions | no | no | no |
| ZIP | reactions | no | no | no |
| ARE | reminders | no | no | no |
| BRO | reminders | no | no | no |
| CDNS | reminders | no | no | no |
| CINF | reminders | no | no | no |
| HIG | reminders | no | no | no |
| NUE | reminders | no | no | no |
| PFG | reminders | no | no | no |
| PSA | reminders | no | no | no |
| VZ | reminders | no | no | no |
| WELL | reminders | no | no | no |
| WUXAY | reminders | no | no | no |
| ADI | screen | yes | yes | yes |
| CSCO | screen | yes | yes | yes |
| FIGS | screen | yes | no | yes |
| HEI | screen | yes | yes | yes |
| NXPI | screen | yes | yes | yes |
| OKTA | screen | yes | no | yes |
| ORKA | screen | yes | yes | yes |
| P | screen | yes | yes | yes |
| PENG | screen | yes | no | yes |
| RNG | screen | yes | yes | yes |
| SDGR | screen | yes | no | yes |
| TENB | screen | yes | yes | yes |

## Method and caveats

| Field | Value |
|---|---|
| Sources | 5 families, listed above |
| Ticker extraction | the first ticker-shaped cell of every markdown table row, and the ticker column of every CSV |
| Counts | per family, per name; a name can be in a family's set even if that family listed it in a table the reader would skip |

**What this does not say.** It does not say the routines are wrong, and it
does not say a name seen once is a better or worse setup. It says the repo
currently contains no artifact that would tell you either.

