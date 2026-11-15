---
date: 2026-11-09
producer: grok-bot/stocktwits-sentiment-scan
contract: stocktwits-sentiment-v1
source: "Grok Bot box: StockTwits MCP scans by the Portfolio analyst agent (core + general lists)"
generated_at: 2026-11-09T20:00:00+07:00
status: ok
---

# StockTwits sentiment — 2026-11-09 (Asia/Bangkok)

**Provenance:** StockTwits MCP via Grok Bot (core run 2026-11-09T08:37:38+07:00, general run 2026-11-09T08:48:08+07:00) · built 2026-11-09T20:00:00+07:00 by scripts/emit_stocktwits_sentiment.py · covers 2026-11-09 (Asia/Bangkok)

## Deviations / degraded paths

- none

## Core list

- **path:** mcp · **ts_bkk:** 2026-11-09T08:37:38+07:00
- **trending ∩ core:** **CRSP** #10 (watchers 41,740, +3.11%), **IBRX** #32 (watchers 31,448, +7.80%) — both new vs prior (none)
- **quiet_ok:** false · **notable:** **CRSP**, **SRPT**, **CCJ**, **ABVX**, **QURE**, **IBRX**, **QUBT**, **CRML**, **SPRB**, **CCCC**, **ZIM**, **CHRS**
- Note: weekend run; prices are Fri close / extended. **SPRB** and **EMHLF** get_sentiment returned empty → sentiment taken from pulse.

### **ABVX**
- **Bias:** NEUTRAL 54 (bull 75 / bear 25)
- **Volume:** now 47 NORMAL; 1D 42 LOW (−10.64%); watchers 2,817; trend —
- **Themes:** SLS/GPS-AML crossposts (same promo post ×2); dip-buy/AI-basket chatter from Fri; Dec news-leak/110 target talk
- **Claims:** Dec news leak could push back over 110 _(unverified)_
- **Noise:** most recent posts are SLS pump crossposts, not ABVX substance
- **Vs prior:** BEARISH 39 → NEUTRAL 54 (flip); vol LOW 44 → NORMAL 47. Price 85.73 (+1.85%).

### **QURE**
- **Bias:** BULLISH 57 (bull 80 / bear 20)
- **Volume:** now 53 NORMAL; 1D 64 HIGH (+20.75%); watchers 8,112; trend —
- **Themes:** post-Q3 averaging down; approval conviction; PDUFA May 1, 2027
- **Claims:** BLA Priority Review, PDUFA May 1, 2027; cash $768.4M (runway into 2030); confirmatory study ~200 pts _(unverified, from Nov 2–5 posts; no new news since)_
- **Noise:** latest QURE posts are from Nov 5; thin
- **Vs prior:** EXTREMELY_BULLISH 75 → BULLISH 57 (−18, label step down); vol HIGH 65 → NORMAL 53. Price 21.70 (+3.28%).

### **UUUU**
- **Bias:** BULLISH 55 (bull 84.6 / bear 15.4)
- **Volume:** now 52 NORMAL; 1D 53 NORMAL (+1.92%); watchers 23,591; trend —
- **Themes:** long-hold/dip-buy; critical-minerals basket with CRML/ARRNF/TMC; China Nov 10 rare-earth deadline watch
- **Claims:** none solid
- **Noise:** basket cross-tags
- **Vs prior:** BULLISH 59 → 55 (same label); vol NORMAL 49 → 52. Price 6.69 (+0.45%).

### **SPRB**
- **Bias:** NEUTRAL 48 (pulse; bull/bear n/a)
- **Volume:** now 55 HIGH; 1D 56 HIGH (+1.82%); watchers 4,860; trend —
- **Themes:** "top biotech 2027" list-spam; Oct pricing debate (~$350K/drug); no posts since Nov 3
- **Claims:** none new
- **Noise:** stale/promo list posts
- **Vs prior:** BULLISH 57 → NEUTRAL 48 (flip, low-info); vol HIGH 56 → HIGH 55. Price 46.55 (+8.99%).

### **ZIM**
- **Bias:** NEUTRAL 50 (bull 100 / bear 0, thin)
- **Volume:** now 42 LOW; 1D 49 NORMAL (+16.67%); watchers 15,342; trend —
- **Themes:** deal-off worry vs buyout floor; Q3 ER/guide disappoint; dividend/Israel-tax; Maersk Q3 read-across
- **Claims:** "Active acquirer bidding $35; second party accumulating toward $37.50" _(unverified, single post Nov 6)_; Maersk Q3 net profit ~tripled to $3.0B _(unverified, via X link)_
- **Noise:** latest messages Nov 6; weekend quiet
- **Vs prior:** NEUTRAL 49 → 50 (flat); vol HIGH 61 → LOW 42 (−19). Price 27.95 (+1.90%).

### **SRPT**
- **Bias:** NEUTRAL 47 (bull 88.6 / bear 11.4)
- **Volume:** now 57 HIGH; 1D 57 HIGH (0%); watchers 26,678; trend —
- **Themes:** Q3 print read (mixed) + year-end DM1/FSHD data; FDA path/ENDEAVOR Cohort 8; Kim credibility fight; RGNX competitor BLA
- **Claims:** Q3 product rev $323.8M, PMO $240.3M, 2026 guide low-end raised to $1.25B; Elevidys $83.5M; ENDEAVOR Cohort 8 enrollment by YE, FDA talks Q1 2027; DM1/MAD data by year-end _(unverified, promo-account sourced)_; RGNX BLA Q1 2027 _(unverified)_
- **Noise:** BioSwings promo account repeated
- **Vs prior:** BULLISH 59 → NEUTRAL 47 (flip); vol HIGH 55 → HIGH 57. Price 17.82 (+1.42%).

### **BTG**
- **Bias:** BULLISH 59 (bull 100 / bear 0)
- **Volume:** now 58 HIGH; 1D 59 HIGH (+1.72%); watchers 8,097; trend —
- **Themes:** cheerleading; CEO communication praise; gold-price tailwind
- **Claims:** none
- **Noise:** low-substance
- **Vs prior:** BULLISH 58 → 59; vol HIGH 62 → 58. Price 5.46 (+1.11%).

### **CRSP**
- **Bias:** EXTREMELY_BULLISH 83 (bull 94.7 / bear 5.3)
- **Volume:** now 65 HIGH; 1D 60 HIGH (−7.69%); watchers 41,740; **trend #10**
- **Themes:** zugo-cel ACR data (SSc, IIM) as "valuation reset"; CTX310 AHA readout Mon 8am CT; CTX321 skepticism
- **Claims:** zugo-cel: 83% (5/6) SSc clinical response at Month 3, 9/9 IIM TIS responders, well tolerated in 21 patients (company IR release linked — verify); CTX310 phase 1b late-breaker at AHA 8am CT Mon Nov 9 _(unverified)_; "-20% tomorrow on closure of Novartis's cardiovascular Horizon trial" _(unverified, single bearish post)_
- **Noise:** BioSwings promo account several posts
- **Vs prior:** BULLISH 58 → EXTREMELY_BULLISH 83 (+25); vol NORMAL 54 → HIGH 65; new trending #10. Price 50.07 (+3.11%).

### **INBX**
- **Bias:** BEARISH 39 (tagged n/a)
- **Volume:** now 48 NORMAL; 1D 50 NORMAL (+4.17%); watchers 823; trend —
- **Themes:** value-trap vs cheap; no posts since Nov 3
- **Claims:** none
- **Noise:** stale
- **Vs prior:** BEARISH 37 → 39 (same); vol NORMAL 51 → 48. Price 82.41 (+2.65%).

### **IBRX**
- **Bias:** BEARISH 38 (bull 94.3 / bear 5.7 tagged; score canonical)
- **Volume:** now 41 LOW; 1D 42 LOW (+2.44%); watchers 31,448; **trend #32** (price 8.65, +7.80%, day vol 9.27M)
- **Themes:** weekend NVDA/China-select-committee political rants; "rocket this week"; sBLA this month / naive readout hype
- **Claims:** "sBLA this month, naive readout" _(unverified)_; "9.50 at open" speculation
- **Noise:** large share off-topic political/AI spam
- **Vs prior:** BEARISH 34 → 38 (same label); vol LOW 42 → LOW 41; new trending #32.

### **ALM**
- **Bias:** BEARISH 27 (tagged n/a)
- **Volume:** now 41 LOW; 1D 38 LOW (−7.32%); watchers 1,363; trend —
- **Themes:** Sangdong ramp (24h running since Nov 1; finished grade ~50%)
- **Claims:** Sangdong running 24 hrs since Nov 1, finished grade ~50% _(unverified)_
- **Noise:** thin
- **Vs prior:** BEARISH 28 → 27; vol NORMAL 50 → LOW 41. Price 8.21 (+3.27%).

### **CRML**
- **Bias:** BEARISH 41 (bull 84.3 / bear 15.7 tagged — posts skew bullish)
- **Volume:** now 48 NORMAL; 1D 51 NORMAL (+6.25%); watchers 15,258; trend —
- **Themes:** Ukraine/Velta titanium + DFC due diligence; China Nov 10 rare-earth export deadline; revenue-realism skeptic posts
- **Claims:** $250M four-year Velta program; DFC on-site due diligence; China Nov 10 deadline, no confirmed extension _(unverified)_; ~194M fully diluted vs 237M claim _(unverified)_
- **Noise:** AGLT robot-stock spam
- **Vs prior:** NEUTRAL 49 → BEARISH 41 (flip, −8); vol NORMAL 51 → NORMAL 48. Price 5.98 (+1.70%).

### **NOK**
- **Bias:** BEARISH 36 (bull 75.6 / bear 24.4)
- **Volume:** now 33 LOW; 1D 35 LOW (+6.06%); watchers 115,166; trend —
- **Themes:** black daily candle; meme-coin spam
- **Claims:** none
- **Noise:** TROLL.X spam
- **Vs prior:** BEARISH 36 → 36; vol LOW 36 → 33. Price 7.56 (−1.30%).

### **EMHLF**
- **Bias:** NEUTRAL 50 (pulse)
- **Volume:** now 35 LOW; 1D 35 LOW (0%); watchers 448; trend —
- **Themes:** dormant — newest post 2026-08-18
- **Claims:** none
- **Noise:** no activity
- **Vs prior:** NEUTRAL 50 → 50; vol LOW 37 → 35. Price 0.101 (+0.30%).

### **COUR**
- **Bias:** NEUTRAL 47 (bull 83.3 / bear 16.7)
- **Volume:** now 63 HIGH; 1D 69 HIGH (+9.52%); watchers 2,412; trend —
- **Themes:** Udemy-close Q3 (rev +94%), deferred commissions/RPO; CEO pay/Pale Fire activism; energy-basket posts
- **Claims:** Form 4 ~$31.45M insider purchase (Nov 5, filing link) — carried over; Q3 rev $376.7M, RPO $865.0M _(unverified)_
- **Noise:** repeat poster
- **Vs prior:** NEUTRAL 54 → 47 (same label); vol HIGH 73 → HIGH 63. Price 3.74 (−0.27%).

### **CCJ**
- **Bias:** BULLISH 57 (bull 47.4 / bear 52.6 tagged — conflicts w/ score)
- **Volume:** now 53 NORMAL; 1D 48 NORMAL (−9.43%); watchers 17,646; trend —
- **Themes:** "~$25M call bet"/March call flow; permitting-reform vote; dilution/data-centre bear posts
- **Claims:** institutional ~$25M call bet Fri _(unverified, Substack)_; Senate could vote Mon Nov 9 on permitting reform _(unverified)_; March 115/90c call volume _(unverified)_
- **Noise:** Substack promo
- **Vs prior:** BEARISH 43 → BULLISH 57 (flip +14); vol NORMAL 50 → NORMAL 53. Price 71.37 (+0.10%).

### **CCCC**
- **Bias:** NEUTRAL 49 (bull 100 / bear 0, thin)
- **Volume:** now 46 NORMAL; 1D 46 NORMAL (0%); watchers 2,567; trend —
- **Themes:** Q3 recap (EPS −$0.16, rev $8.47M); "load the boat/squeeze" hype
- **Claims:** Q3 GAAP EPS −$0.16, revenue $8.47M _(unverified)_
- **Noise:** thin
- **Vs prior:** BULLISH 55 → NEUTRAL 49 (minor flip); vol LOW 41 → NORMAL 46. Price 3.14 (+6.44%).

### **CHRS**
- **Bias:** NEUTRAL 45 (bull 66.7 / bear 33.3)
- **Volume:** now 43 LOW; 1D 49 NORMAL (+13.95%); watchers 5,033; trend —
- **Themes:** earnings expected Mon Nov 9; CVR sale/financing worries; Tagmo asset sale idea
- **Claims:** earnings tomorrow (per Sunday posts); CVR sold to shareholders; ex-US license hope _(unverified)_
- **Noise:** one poster dominates
- **Vs prior:** NEUTRAL 53 → 45 (same label); vol NORMAL 51 → LOW 43. Price 0.77 (+2.82%).

### **QUBT**
- **Bias:** NEUTRAL 47 (bull 82.4 / bear 17.6)
- **Volume:** now 54 NORMAL; 1D 47 NORMAL (−12.96%); watchers 33,556; trend —
- **Themes:** "Tuesday squeeze" hype; Reddit NewsImpact #1 mention
- **Claims:** Reddit scan top-3 ticker, mentions 12 _(unverified)_
- **Noise:** squeeze-wish posts
- **Vs prior:** BEARISH 26 → NEUTRAL 47 (flip +21); vol LOW 41 → NORMAL 54. Price 6.31 (−0.32%).

## General list

ts 2026-11-09T08:48:08+07:00; deep_n=24

### SMCI - EXTREMELY_BULLISH 84 | vol 74 HIGH (1D +1.35%) | trend 6 | watchers 94261
- vs prior: sent EXTREMELY_BULLISH 86 -> EXTREMELY_BULLISH 84; vol 76 EXTREMELY_HIGH -> 74 HIGH
- themes: Board #6; weekend NVDA/Jensen Huang scandal chatter dragging AI names; Claim of an "independent investigation" at SMCI ("SMCI 2.0"); Bear/bull split on Monday open
- claims: Independent investigation at SMCI (one post, unverified)
- material: False 

### RDW - EXTREMELY_BULLISH 82 | vol 71 HIGH (1D +1.41%) | trend 11 | watchers 24223
- vs prior: sent EXTREMELY_BULLISH 86 -> EXTREMELY_BULLISH 82; vol 76 EXTREMELY_HIGH -> 71 HIGH
- themes: Board #11 after +16.5% Fri; "Selected to power a planet" / contract hopes; Space sector sympathy vs AI-sector sell-off worry
- claims: "Selected to POWER A PLANET" (one post, unverified)
- material: True new trending #11

### ORCL - BULLISH 59 | vol 60 HIGH (1D +11.67%) | trend 13 | watchers 73258
- vs prior: new to general deep set
- themes: Board #13; dragged by NVDA headline fear; "Google thinks Oracle is a hyperscaler" (unverified); Dip-buy vs fear-mongering
- claims: Google views Oracle as hyperscaler (unverified)
- material: True new trending #13

### CRSP - EXTREMELY_BULLISH 83 | vol 65 HIGH (1D -7.69%) | trend 15 | watchers 41741
- vs prior: new to general deep set
- themes: Board #15; zugo-cel ACR data (83% SSc response, 9/9 myopathy, 21 pts well tolerated); Cardiovascular readout expected "tomorrow"; One bear: -20% on closure of Novartis CV Horizon trial
- claims: Company PR on zugo-cel ACR data (linked ir.crisprtx.com, corroborated by PR); Cardiovascular readout Monday (post, unverified); Novartis Horizon CV trial closure -> CRSP -20% (one post, unverified)
- material: True new trending #15; catalyst claim

### ZETA - BEARISH 44 | vol 38 LOW (1D -2.63%) | trend 29 | watchers 15584
- vs prior: new to general deep set
- themes: Board #29; earnings expected tomorrow (Tue); Bulls target $45 post-ER; Tagged posts ~98% bull but canonical label BEARISH 44 / vol LOW
- claims: Earnings "tomorrow" with guidance raise expected (post, unverified)
- material: True new trending #29

### IBRX - BEARISH 38 | vol 41 LOW (1D +2.44%) | trend 27 | watchers 31447
- vs prior: new to general deep set
- themes: Board #27; naive/readout + sBLA this month hype; Macro rant about AI trade collapse; Canonical BEARISH 38 despite ~94% tagged bulls
- claims: Naive readout / sBLA this month (posts, unverified)
- material: True new trending #27

### PENG - BEARISH 40 | vol 30 LOW (1D -3.33%) | trend 44 | watchers 4715
- vs prior: sent BEARISH 43 -> BEARISH 40; vol 26 LOW -> 30 LOW
- themes: Board #44 after +12.4% Fri; Rosenblatt $100 PT reconfirmed 11/4 (post); Data-center ballot-rejection selloff narrative; Senate bill to fast-track DC power (via post)
- claims: Rosenblatt reiterated $100 PT 11/4 (unverified); Bipartisan Senate bill to fast-track AI data centers, vote possibly next week (post citing The Verge, unverified)
- material: True catalyst claim

### IONQ - BULLISH 68 | vol 68 HIGH (1D +1.47%) | trend 45 | watchers 61790
- vs prior: sent BULLISH 67 -> BULLISH 68; vol 60 HIGH -> 68 HIGH
- themes: Board #45 after +23% Fri; Quantum-security/NSA PQC links; Rival-board chatter (AGLT/INFQ)
- claims: Regulators warn banks on quantum threat (The Banker link)
- material: False 

### ONDS - BEARISH 42 | vol 50 NORMAL (1D +2.0%) | trend 47 | watchers 37806
- vs prior: new to general deep set
- themes: Board #47 after +18% Fri; Earnings imminent; short-squeeze hope (~44-47% float short claim); Bears mocking $5 handle
- claims: Short interest ~44-47% of float (one post, unverified)
- material: True new trending #47; catalyst claim

### LUNR - BULLISH 74 | vol 70 HIGH (1D -7.14%) | trend 49 | watchers 39207
- vs prior: new to general deep set
- themes: Board #49 after +21% Fri; Space sector grouped w/ RDW RKLB SPCX; NVDA scandal sector-risk jokes
- claims: -
- material: True new trending #49

### DAL - BEARISH 43 | vol 45 NORMAL (1D -17.78%) | trend 50 | watchers 83877
- vs prior: new to general deep set
- themes: Board #50; Weekly channel breakout / calls above $90 (options post); Dem Congress airline "surveillance pricing" probe; $500M 5.5% 2029 notes
- claims: $500M 5.5% notes due 2029 (8-K link)
- material: True new trending #50

### AEHR - EXTREMELY_BULLISH 78 | vol 81 EXTREMELY_HIGH (1D +1.23%) | trend None | watchers 15490
- vs prior: sent EXTREMELY_BULLISH 78 -> EXTREMELY_BULLISH 78; vol 81 EXTREMELY_HIGH -> 81 EXTREMELY_HIGH
- themes: Hard-to-short squeeze talk; Q1 FY27 call: TSMC involved in qualification of lead AI customer; Single-customer concentration warning
- claims: CEO said TSMC involved in qualification on FQ1 call (post, unverified)
- material: True catalyst claim

### APP - EXTREMELY_BULLISH 88 | vol 84 EXTREMELY_HIGH (1D +0.0%) | trend None | watchers 26092
- vs prior: sent BULLISH 73 -> EXTREMELY_BULLISH 88; vol 87 EXTREMELY_HIGH -> 84 EXTREMELY_HIGH
- themes: "Safe haven" vs AI/NVDA crash; Short report/SEC probe overhang gone (post); Calls for $400+ open
- claims: -
- material: True score 73->88

### DUOL - EXTREMELY_BULLISH 79 | vol 85 EXTREMELY_HIGH (1D +1.18%) | trend None | watchers 9587
- vs prior: sent EXTREMELY_BULLISH 84 -> EXTREMELY_BULLISH 79; vol 89 EXTREMELY_HIGH -> 85 EXTREMELY_HIGH
- themes: Post-ER +26% Wed momentum; Support ~$133 / resistance ~$168; Securities-suit and AI-competition bears
- claims: Securities suit alleging hidden ads/AI content hit to DAU growth (post, unverified)
- material: False 

### CELH - EXTREMELY_BULLISH 83 | vol 74 HIGH (1D +0.0%) | trend None | watchers 31018
- vs prior: sent EXTREMELY_BULLISH 86 -> EXTREMELY_BULLISH 83; vol 80 EXTREMELY_HIGH -> 74 HIGH
- themes: Q3 record rev ~$847M +17% (video post, unverified); Rotation-into-CELH-Monday call; Flo Rida suit settled $85M ($60M paid, $25M Jan) per post
- claims: Flo Rida settlement $85M, $25M due Jan (one post, unverified)
- material: False 

### LITE - BULLISH 63 | vol 59 HIGH (1D +25.42%) | trend None | watchers 17060
- vs prior: sent EXTREMELY_BULLISH 75 -> BULLISH 63; vol 75 EXTREMELY_HIGH -> 59 HIGH
- themes: -36% last week with optics/storage; Optics "bottoming" calls from promo accounts; Post on 45% sell-off + all-stock MRVL deal (close 1H28)
- claims: Lumentum CEO comments on MRVL all-stock deal, close 1H28, regulatory hurdle (post, unverified)
- material: True vol 75->59; 1D vol chg +25.42%; catalyst claim

### PGEN - BULLISH 66 | vol 63 HIGH (1D +26.98%) | trend None | watchers 9487
- vs prior: sent EXTREMELY_BULLISH 91 -> BULLISH 66; vol 90 EXTREMELY_HIGH -> 63 HIGH
- themes: Papzimeos vs Inovio Voceryq durability debate (INO Yr2 CR 27%->50%); FDA label omission of INO Yr2 data; Add-on-Monday intent
- claims: INO-3107 Yr2 CR 50% vs PGEN 51% held (post w/ Laryngoscope link, unverified)
- material: True score 91->66; vol 90->63; 1D vol chg +26.98%

### COHR - EXTREMELY_BULLISH 77 | vol 73 HIGH (1D +2.74%) | trend None | watchers 11703
- vs prior: sent BULLISH 72 -> EXTREMELY_BULLISH 77; vol 78 EXTREMELY_HIGH -> 73 HIGH
- themes: Optics bottoming/"selling worn out" promo posts; Buyer pricing-power bears; Optics -36% week context
- claims: -
- material: False 

### PLTR - EXTREMELY_BULLISH 76 | vol 72 HIGH (1D +4.17%) | trend None | watchers 326090
- vs prior: sent EXTREMELY_BULLISH 80 -> EXTREMELY_BULLISH 76; vol 76 EXTREMELY_HIGH -> 72 HIGH
- themes: NVDA scandal/futures red chatter; $180-this-week vs -10% day calls; Closed long Fri, re-entry plans
- claims: -
- material: False 

### ALAB - EXTREMELY_BULLISH 85 | vol 72 HIGH (1D +1.39%) | trend None | watchers 13522
- vs prior: sent EXTREMELY_BULLISH 83 -> EXTREMELY_BULLISH 85; vol 74 HIGH -> 72 HIGH
- themes: Promo "bottoming" posts; Gamma flip ~$189.7, $200 call wall; Design-win moat bears
- claims: -
- material: False 

### SNAP - BEARISH 41 | vol 71 HIGH (1D +0.0%) | trend None | watchers 234419
- vs prior: sent BEARISH 42 -> BEARISH 41; vol 74 HIGH -> 71 HIGH
- themes: Other revenue ~$350M Q3 +84% YoY (subscriptions); "Cheap vs ~$10B cap" dip-buyers; Canonical BEARISH 41 despite ~71% tagged bulls
- claims: -
- material: False 

### CAPR - BULLISH 71 | vol 70 HIGH (1D +4.29%) | trend None | watchers 34055
- vs prior: sent BULLISH 68 -> BULLISH 71; vol 73 HIGH -> 70 HIGH
- themes: FDA decision by ~Nov 22 (post); 15-page letter to FDA urging deramiocel approval; Earnings Tuesday; NS arbitration hopes
- claims: PDUFA/FDA word by ~11/22; ER Tue (posts, unverified)
- material: True catalyst claim

### FSLY - EXTREMELY_BULLISH 76 | vol 70 HIGH (1D +0.0%) | trend None | watchers 36235
- vs prior: sent EXTREMELY_BULLISH 80 -> EXTREMELY_BULLISH 76; vol 77 EXTREMELY_HIGH -> 70 HIGH
- themes: Post-ER dip debate; FMR >10% holder via 13G (post); Growth slowing 16-23%, GAAP loss
- claims: FMR LLC >10% holder (13G, post)
- material: False 

### FLNC - NEUTRAL 54 | vol 69 HIGH (1D +4.35%) | trend None | watchers 8478
- vs prior: sent BULLISH 70 -> NEUTRAL 54; vol 73 HIGH -> 69 HIGH
- themes: Board replaced CEO/CFO/CCSO/COO within 45 days (post); Shareholder suits, execution delays; Insider-buy calls
- claims: C-suite replaced within 45 days (post, unverified)
- material: True bias flip down; score 70->54

## Coverage

The published rows contain 49 normalized ticker rows: 19 core and 30 general.
Crowd sentiment and claims describe StockTwits posts and are not independently verified facts.
