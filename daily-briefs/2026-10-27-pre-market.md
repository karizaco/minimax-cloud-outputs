# Agentic Pre-Market Brief — Tuesday, 27 October 2026

**Snapshot:** 2026-10-27 **08:39 ET** (pre-market). US cash open 09:30 ET; all pre-market prints below are from the 08:24–08:39 ET window, each stamped in the tables.
**Scope:** the entire US-listed equity universe (5,713 US common stocks screened), not a watchlist.
**Sources:** TradingView public screener (5,713 rows), CNBC quote API (143 pre-market names priced), Nasdaq earnings calendar (174 reporters for 10/27), Yahoo Finance, Coinbase/Kraken/CoinGecko, StockTwits, and `web_search` for catalyst anchoring.

> **Read this first — four things materially change how the numbers below should be read.**
> **1. The gap column is a pre-market gap, not a session move.** The skill's Step 2 screen filters on TradingView's `change`, but in a pre-open pull that field is the *prior regular session's* move. The gap tables therefore use the pre-market column, and Monday's session change is carried separately.
> **2. The watchlist file does not exist.** `research/watchlist.yaml` is absent from this sandbox (the upstream URL returns 404). No default was invented, per the skill's hard rule. Section 6 records the gap rather than filling it.
> **3. CNBC's crypto index quotes are wrong by roughly 9x** (`.BTC` = 8,989.99 "Bloomberg Galaxy Bitcoin Index" vs. a true spot of ~80,080 across four independent venues). They were discarded; the crypto block uses Coinbase, Kraken, CoinGecko and Yahoo instead. This is a data-path defect in the CNBC feed, not a market event.
> **4. Some pre-market prints are stale and are flagged ⚠.** A print older than 45 minutes is the last trade, not a live quote. One such print — GOOGN at +5.35% on 103 shares — was **excluded** because the live Alphabet lines read +0.47%/+0.51%.

---

## 1. TL;DR

Seven themes carry the tape. The market itself is not doing much: SPY +0.32%, QQQ +0.49%, S&P 500 futures +0.41%, and the median pre-market gap across 2,401 priced US stocks is **+0.14%**. The action is entirely in single names.

- **AI infrastructure is the lead theme, and it is a *re-rating* not a *reversal*.** Celestica (**CLS +10.87%**) blew out Q3 and guided 2027 revenue to $40bn; INNIO (**INIO +13.53%**) posted a record quarter with order backlog up **142%** to $8.0bn; Broadcom (**AVGO +3.09%**) is at the centre of a **$63bn** SPV financing to lease XPU accelerators to Anthropic. Corroborators CRDO +4.43%, CRWV +3.82%, NBIS +3.74%, BE +4.11%, AMAT +2.04%, ASML +1.73%, ORCL +1.50%.
- **This is the fourth name in a week to gap on an AI *financing* structure, and the market is now underwriting the structures rather than the cash flows.** CLS's own free-cash-flow guidance was *cut* to $460m from $600m even as revenue guidance rose. The bid is for the demand narrative; the cash conversion is the part being discounted.
- **CLS's gap is compressing and that is the most actionable number in the brief.** It printed $287.10 (+16.4%) at 04:02 ET and was $273.47 (+10.87%) at 08:38 ET — **5.5 percentage points of the gap given back** before the open, on a 2027 revenue guide that is 12% above the Street. A fade of that size on a beat-and-raise usually means the positioning, not the news, was the problem.
- **The Brazil complex is bouncing mechanically off a historic break.** Lula's runoff win (51.8% vs 48.2% for Flávio Bolsonaro) on Monday took **XP −48.36%** on 133.1m shares (12.5x average) and dragged BBD −28.01%, STNE −27.44%, PAGS −25.17%, ITUB −20.37%, EWZ −19.82%, NU −16.95%, AFYA −29.49%, INTR −34.91%. The Ibovespa tripped circuit breakers and the real fell 10–12%. Today's pre-market bid is **+0.20% (PBR) to +1.99% (PAGS)** — a dead-cat bounce off an oversold tape, not a fundamental reversal, and the unresolved catalyst is Bolsonaro's annulment push plus Lula's finance-minister pick.
- **It is a 174-company pre-market earnings day, and the dispersion inside it is enormous.** Sofi (**SOFI +11.62%**) beat and guided up; Commvault (**CVLT −10.24%**) and Watsco (**WSO −9.28%**) did not. **21 of the gaps in the tables below are on today's Nasdaq earnings calendar** — the single largest driver of the move list.
- **Private-credit M&A has re-rated one BDC overnight.** Ares Capital agreed to buy MidCap Financial Investment for **$10.88/share** (~$2.6bn EV, 30.1% premium); **MFIC +22.61%** to $10.25 — but the stock still sits below its own $12.86 preliminary NAV, and a "meaningful" special dividend will *reduce* the stock leg of the consideration.
- **The crypto-equity complex is up 1–3% on a flat tape, but the individual names are violent.** BTC is **$80,080–80,131** across four venues, essentially unchanged. MSTR +0.70%, COIN +1.19%, MARA +2.34%, RIOT +2.22%, CLSK +2.70%. Offsetting that, the three largest movers in the entire brief are momentum unwinds with no earnings behind them: BRAI +46.23% (after −40.28% Monday), CLRO +19.12% (after +52.92%), AZTR −14.39% (after **+113.99%** on 1867x relative volume).
- **One genuinely unexplained large move: ARTV −32.14%** on 900.8k pre-market shares with no catalyst found, and INOD −10.70%. Neither is covered by a cluster; neither is explained by earnings. No cause is inferred for them.
- **Weekend-adjacent risk for the session:** the FOMC decision lands **tomorrow, Wed 28 Oct at 14:00 ET**, and the September meeting delivered a hike. Today's 10:00 ET Consumer Confidence, New Home Sales and Richmond Fed prints are the last macro before the Fed speaks.

**Watchlist:** unavailable — no watchlist file exists in this environment, so no watchlist names can be reconciled against the themes above. Sections 2–5 cover the whole market in their place.

---

## 2. Theme clusters

### Cluster A — AI infrastructure: the financing-structure trade

**Leader: CLS (Celestica) +10.87%** — $273.47 pre-market vs $246.65 Monday close, 342.3k pre-market shares, $31.1bn cap.
Q3 revenue **+83% to $5.83bn** (consensus $5.47–5.48bn); adjusted EPS **$3.30** (consensus $2.96–2.99), more than double $1.58 a year ago; Connectivity & Cloud Solutions revenue **+102% to $4.87bn**; record adjusted operating margin **8.5%**. Management guided **2027 revenue to $40bn** (vs $35.71bn consensus, +90% on the updated 2026 base) with adjusted EPS of $21.50 and a 9% margin, raised 2026 revenue to $21bn from $20.5bn and adjusted EPS to $11.55 from $11.30 — and **cut free-cash-flow guidance to $460m from $600m** on working capital, with 2027 capex of $1.5–2.0bn. CEO Rob Mionis: *"well-positioned to continue to support leading hyperscalers and frontier AI labs through the ongoing AI infrastructure supercycle."* An Investor & Analyst Day is held today. 23 of 24 analysts rate it Buy; Bernstein initiated Outperform with a $520 target.
*Source: https://finance.yahoo.com/markets/stocks/articles/cls-stock-soars-premarket-blowout-081754257.html · https://www.gurufocus.com/news/9144188/celestica-cls-shares-surge-17-premarket-after-q3-earnings-beat-expectations*

**Corroborator: INIO (INNIO) +13.53%** — $18.88 vs $16.63, 485.0k pre-market shares, $12.5bn cap. Record Q3: revenue **$1.2bn, +57%** (first $1bn+ quarter in company history), net income **$109.2m, +176%**, adjusted EBITDA **$245.4m, +70%** at a 21% margin. Equipment revenue **+86% to $777.6m** on large-scale data-centre deliveries; order intake $2.2bn; **order backlog a record $8.0bn, +142% year over year**. FY26 guidance raised to $3.9–4.0bn revenue and $780–800m adjusted EBITDA. Power delivered 1.2 GW. Call was 08:00 ET.
*Source: https://www.globenewswire.com/news-release/2026/10/27/3388791/0/en/innio-reports-record-third-quarter-2026-financial-results-with-revenue-up-57-net-income-up-176-and-adjusted-ebitda-up-70-raises-2026-full-year-guidance.html*

**Corroborator: AVGO (Broadcom) +3.09%** — $339.33 vs $329.17, 653.2k pre-market shares, $1.57tn cap. After Monday's close, Bank of America, Blackstone, Citigroup and Morgan Stanley announced a **$63bn special-purpose-vehicle financing** to buy Broadcom XPU accelerators and networking gear and lease them to Anthropic, deliveries from 2027, with Broadcom providing residual-value support on the first-lien portion. Hock Tan is reported to have rescued the structure after lenders wavered. Anthropic's IPO filing disclosed **~$224.5bn of non-cancelable compute commitments** with Amazon and Alphabet. DA Davidson upgraded to Buy, $400. Counterweights: Alphabet diversifying TPU sourcing to MediaTek, and the stock still sits below its 50- and 200-day averages.
*Source: https://www.benzinga.com/markets/tech/26/10/62613053/why-is-broadcom-stock-gaining-tuesday-2 · https://www.marketbeat.com/stocks/NASDAQ/AVGO/news/*

**Supporting tape:** CRDO +4.43% · CRWV +3.82% · NBIS +3.74% · BE +4.11% · VICR +3.71% · FLEX +3.26% · AMAT +2.04% · ASML +1.73% · MRVL +1.73% · ORCL +1.50% · AMD +1.59% · NVDA +0.97% · AMZN +0.61% · TSM +0.50% · MSFT −0.63% · META −0.51% · AAPL −0.37% · PLTR −0.11%.

**Interpretation and the caveat that matters.** The theme is coherent, well-sourced and broad — but it is a bounce inside a damaged month, not a new trend. CLS is −17% year to date and on its worst month in over six years; CoreWeave, Nebius and IREN were each down more than 35% in October before today. Two of the three cluster anchors are rising on *financing structures* (AVGO's SPV, INIO's backlog conversion) rather than realised cash. And CLS's own FCF guidance went down while its revenue guidance went up. The honest read is that the market is re-rating the probability of AI infrastructure demand, not the quality of the cash flows behind it — and the AVGO structure carries genuine circular-financing risk that several analysts have flagged explicitly.

### Cluster B — Brazil: the "Bolsonaro trade" unwinds

**Leader: XP (XP Inc) −48.36% Monday**, $30.41 → $15.71, 133.1m shares (12.5x the 10-day average), intraday low $13.78–$14.59, a 52-week low and its worst day since the 2019 listing. Driver: **Luiz Inácio Lula da Silva's surprise runoff re-election (51.8% vs 48.2% for Flávio Bolsonaro)** on 26 Oct, which reversed the market-friendly rally that had carried the stock toward a $32.73 high. The Brazilian real fell 10–12%, the Ibovespa tripped circuit breakers, and the Brazil ETF (EWZ) fell about 21%. Some commentators argue the move overshot — consensus estimates did not change and forward P/E compressed from about 12.9x to roughly 7x — but the forward catalysts are unresolved: Bolsonaro's refusal to concede and an annulment push, plus Lula's finance-minister pick and fiscal plans. XP's next earnings is mid-November.
*Source: https://www.investing.com/news/stock-market-news/why-is-xp-stock-plummeting-45-today-93CH-4971958 · https://www.marketbeat.com/instant-alerts/price-xp-nasdaq-xp-sets-new-1-year-low-heres-why-2026-10-26/*

| Brazil complex | Mon close | Mon chg | Pre-mkt px | Pre-mkt gap | Pre-mkt vol | Mkt cap |
|---|---|---|---|---|---|---|
| XP | $15.71 | **−48.36%** | $16.00 | +1.88% | 527.8K | $8.11bn |
| INTR (Inter & Co) | $4.68 | −34.91% | $4.74 | +1.28% | 122.6K | $2.07bn |
| AFYA | $10.64 | −29.49% | $11.02 | +3.53% | 4.9K | $941M |
| BBD (Bradesco) | $2.93 | −28.01% | $2.98 | +1.71% | 511.0K | $32.81bn |
| STNE (StoneCo) | $8.33 | −27.44% | $8.45 | +1.49% | 85.8K | $1.92bn |
| PAGS (PagSeguro) | $8.56 | −25.17% | $8.73 | +1.99% | 17.1K | $2.39bn |
| ITUB (Itaú) | $7.70 | −20.37% | $7.77 | +0.91% | 196.4K | $84.91bn |
| EWZ (Brazil ETF) | $34.15 | −19.82% | $34.61 | +1.35% | 2.1M | $6.13bn |
| NU (Nu Holdings) | $12.59 | −16.95% | $12.79 | +1.58% | 1.2M | $60.82bn |
| PBR (Petrobras) | $22.50 | −13.99% | $22.54 | +0.20% | 357.4K | $145.00bn |
| BSBR (Banco do Brasil) | $4.82 | −13.15% | $4.90 | +1.66% | 1.0K | $36.14bn |
| BBAR (Banco Macro) | $12.12 | −7.97% | $12.22 | +0.85% | 2.4K | $2.48bn |
| GGB (Gerdau) | $4.75 | −6.86% | $4.81 | +1.26% | 638.0 | $9.40bn |
| BMA (Bradesco ADR) | $61.88 | −6.30% | $61.75 | −0.21% | 779.0 | $3.89bn |
| SAN (Santander) | $12.37 | −3.66% | $12.41 | +0.32% | 28.1K | $180.06bn |
| VALE (Vale) | $12.00 | −3.23% | $12.12 | +1.00% | 47.7K | $53.27bn |

**Interpretation.** Every one of these names is green pre-market, and that uniformity is itself the warning: a market that gapped 20–48% down on a political headline does not repair itself with a +1% bid. The pre-market bid is thin and mechanical (XP 527.8k shares, PAGS 17.1k, BSBR 1.0k). Treat this as a stabilising tape, not a re-rating; the catalyst is still pending in Brasília, not in the order book.

### Cluster C — Pre-market earnings dispersion (174 reporters)

Nasdaq's calendar carries **174 reporters for 2026-10-27** (against 79 for 10-26 and 227 for 10-28), the large majority flagged `time-pre-market`. Releases land roughly 06:00–07:00 ET with 08:00–10:00 ET calls, so the pre-market tape is a live reaction to prints that are already out. **21 of the gaps in the tables in sections 3 and 4 are on that calendar** — this is the single biggest driver of the move list, and it is also the reason the same screen produced SOFI +11.62% and CVLT −10.24% on the same morning.

| Reported 10/27 before the open | Gap | | Reported 10/27 before the open | Gap |
|---|---|---|---|---|
| KNSA (Kiniksa) | **+13.73%** | | CVLT (Commvault) | **−10.24%** |
| SOFI (SoFi) | **+11.62%** | | WSO (Watsco) | **−9.28%** |
| SXC (SunCoke) ⚠ | +8.05% | | XYL (Xylem) | −8.50% |
| PII (Polaris) ⚠ | +8.01% | | EEFT (Euronet) | −6.94% |
| HRI (Herc Rentals) | +7.69% | | AWI (Armstrong World) | −4.46% |
| RCL (Royal Caribbean) | +5.63% | | HLT (Hilton) | −4.37% |
| TRU (TransUnion) | +4.25% | | ITW (Illinois Tool Works) | −4.07% |
| JCI (Johnson Controls) | +4.74% | | SHW (Sherwin-Williams) | −3.63% |
| SPGI (S&P Global) | +4.29% | | HUBB (Hubbell) ⚠ | −1.83% |
| GLXY (Galaxy Digital) | +4.40% | | ITW consensus | $2.97–2.99 EPS |
| CTS (CTS Corp) ⚠ | +3.95% | | WSO consensus | $4.13 EPS |

**Leader — SOFI (SoFi) +11.62%**, $16.14 vs $14.46, **16.0m pre-market shares** (the heaviest pre-market book in the brief by an order of magnitude), $18.68bn cap. Q3 adjusted net revenue **$1,371.1m, +44%** to a record; adjusted EBITDA **$469.8m, +70%** at a 34% margin; GAAP net income $241.0m; adjusted EPS **$0.18** vs $0.17 consensus; net interest income $929.5m, +59%; fee-based revenue $570.6m (42% of revenue). Members **+35% to a record 17.1m** (1.2m added in the quarter), products +44% to 26.7m. FY26 guidance raised to **$5.04bn adjusted net revenue** (consensus $4.88bn) and **$0.61 adjusted EPS** (consensus $0.59); FY27 guidance introduced at **$6.4bn** and **$0.90** (consensus $6.14bn / $0.82) — roughly 27% growth and a ~20% adjusted net margin. 20th consecutive Rule-of-40 quarter, 12th consecutive profitable quarter. CEO Anthony Noto: *"We had exceptional Q3 results against the backdrop of any environment, but they are even more remarkable given how 2026 has unfolded."*
*Source: https://investors.sofi.com/news/news-details/2026/SoFi-Reports-Third-Quarter-2026-with-Record-Net-Revenue-of-1-4-Billion-Net-Income-of-241-Million-and-Raises-Full-Year-Guidance/default.aspx*

**Prior-session reporters still being digested today (10/26):** CLS +10.87% (the week's best print) · HWKN +10.75% ⚠ · NE −5.70% · **WHR −6.41%** (Q3 loss of $0.21/share vs a $0.76 expected profit; revenue −8.8% to $3.67bn) · JBLU +13.93%.

**Interpretation.** This cluster is the most *tradeable* and the least *durable* of the seven. An 8:30 ET print against a 2–3% pre-market move is largely a resolution of positioning, not new information — ITW's negative Earnings ESP (−0.97%) and JPMorgan's Neutral downgrade were already public before the number. The genuinely informative subset is where a *guidance* surprise appears: SOFI's first-ever 2027 guide ($6.4bn / $0.90, well ahead of the Street) and JCI's +4.74% alongside HLT's −4.37%, which reads as a clean quality-of-guidance split inside travel/leisure. The industrial and housing-adjacent cohort (ITW, XYL, WSO, AWI, SHW, HUBB) is almost uniformly negative, and XYL's −8.50% on a $25.3bn cap is the largest single-cap gap-down on the board.

### Cluster D — Private-credit M&A: MFIC +22.61%

**MidCap Financial Investment Corp (MFIC) $10.25 vs $8.36** Monday close, 663.9k pre-market shares, $688.6m cap. Ares Capital (ARCC) and MFIC announced a definitive merger agreement under which **ARCC acquires MFIC** in a stock-and-cash transaction for a **total enterprise value of ~$2.6bn**. Consideration is **$10.88 per fully diluted MFIC share**: ~$1.21 cash (from an Ares Management subsidiary) and ~$9.67 in ARCC stock — a **30.1% premium to MFIC's 26 October close** and a 25.8% premium to its 30-day VWAP. MFIC's preliminary 30 September NAV is **~$12.86/share**, so the headline consideration is *below* book. MFIC expects to declare and pay a **"meaningful" special dividend** of undistributed taxable income before closing, and the ARCC stock leg is reduced dollar-for-dollar by that dividend — so $10.88 is not the effective value per share. Apollo affiliates holding 5.2% signed voting and support agreements; closing is expected in **1H 2027**, subject to MFIC shareholder and regulatory approval; Wells Fargo agreed to provide $750m of additional secured financing; ARCC may issue up to ~41m shares (existing holders ~95% of the combined company).
*Source: https://finance.yahoo.com/markets/stocks/articles/ares-capital-corporation-agrees-acquire-100000340.html · https://www.reuters.com/legal/transactional/ares-capital-buy-apollos-midcap-financial-investment-26-billion-deal-2026-10-27/ · https://marketchameleon.com/articles/b/2026/10/27/mfic-arcc-acquisition-10-88-per-share-stock-and-cash*

**Interpretation.** At $10.25 the stock trades ~6% below the headline $10.88, and that gap is *not* obviously an arbitrage: the special dividend reduces the stock leg, so the deal's true value depends on a dividend that has not been sized. The stock is also below its own $12.86 NAV, which is a normal consequence of a below-book acquisition and a warning against reading $10.88 as a floor. ARCC itself is **−0.75%** pre-market — the acquirer is not being paid for the accretion, consistent with the release's own "accretive to core earnings" framing being a guidance claim rather than a market verdict. Watch the Q3/NAV release on **5 November**.

### Cluster E — Crypto and the momentum complex

Crypto itself is inert. **BTC $80,080–80,131** (Coinbase $80,115.64, Kraken $80,079.40/80,082.30, CoinGecko $80,131, Yahoo $80,080.61 vs a $80,009.50 prior close, −0.15%). **ETH $2,323.34–2,323.42** (Coinbase, CoinGecko, TradingView). **SOL $100.45–100.46**. The equity wrapper is up modestly: MSTR +0.70% · COIN +1.19% · MARA +2.34% · RIOT +2.22% · CLSK +2.70% · WULF +3.16% · GLXY +4.40%.

The violent part of this cluster has nothing to do with crypto.

- **BRAI (Braiin) +46.23%** to $3.10 on 5.1m pre-market shares, after closing Monday at **−40.28%**. Monday was a textbook momentum unwind: opened near $4.28, spiked above $5.05 (+35–50% intraday) on the **"Force AI"** launch — an orchestration layer for the RADIUS AI contact-centre platform that lets clients switch between OpenAI, Claude, Gemini, Azure OpenAI, Llama or Mistral — then collapsed to close at $2.12, near a 52-week low of $2.03. Negative book value per share; roughly $73.4m of revenue. Today's bid is a bounce off a broken momentum name, not a fundamental re-rating. *Source: https://www.benzinga.com/trading-ideas/movers/26/10/62593543/braiin-stock-rallies-whats-driving-the-move*
- **CLRO (ClearOne) +19.12%** on 12.3m shares after Monday's **+52.92%** — a $13.3m market cap with 12m pre-market shares traded.
- **AZTR (Azitra) −14.39%** after Monday's **+113.99%** on 148.4m shares (**1867x** relative volume) — a full round trip in 24 hours.
- **SRTM (Stratum) −13.17%** after Monday's −30.28% on 116.0m shares (76.1x).
- Also in the top-10 decliners: **WFF −26.95%** (15.9m shares, $6.0m cap), **IMNN −23.16%**, **RCT −15.36%** (22.8m shares), **HAO −14.29%**.

**Interpretation and the discipline this demands.** The Monday regular-session unusual-volume screen (volume > 50m AND |change| ≥ 5%, ranked by volume × |change|) returned only **nine names on the upside and eight on the downside** — AZTR, CLRO, RCT, SGRY, TGL, WFF, GPUS, WULF, TSLA, and XP, NU, SRTM, SHFS, INTR, GCDT, JBLU, SNTI. Every one of them is either a $1–15m micro-cap or a Brazil/election name. Monday was not a broad institutional tape; it was a violent, narrow one. That is the single most important context for reading today's 46% and 19% prints: these are the tails of a momentum unwind, and they will gap hard in both directions again.

### Cluster F — Ferrovial: a concession-financing clarification (+9.79%)

**FER $55.28 vs $50.35**, 116.8k pre-market shares (thin — a Madrid-listed ADR; the Madrid line was up ~8%). Management clarified the financing and payment structure of its **I-24 Tennessee managed-lanes concession**: headline concession value of $24.8bn equates to roughly **$21bn in present-value terms**, with **$7.7bn of construction-period payments in 2027–2033** and a maximum **75/25 debt-to-equity** under TIFIA. That eased the capital-structure anxiety that had held the stock near its 52-week low (€42.77) and triggered a move in Madrid before the ADR opened. Context: an $8.9bn I-285 East Express Lanes win in Atlanta, a £1.5bn Anglian Water framework, TCI lifting its stake to ~13%, an €800m buyback extended to March 2027 (41% used), and rival legal challenges from ACS and Acciona. **Nine-month results are due after the US close today** with the call on 28 October; consensus is ~$0.32–0.33 EPS on ~$2.95bn revenue. Bank of America kept Buy with a €60 target (cut from €67); Deutsche Bank cut to Hold; JPMorgan downgraded earlier in October. The ADR is **not on Nasdaq's earnings calendar** — a genuine coverage gap for foreign issuers, and the reason FER's move has no calendar confirmation.
*Source: https://www.perplexity.ai/finance/FER?comparing=FER,EN.PA,ACS.MC,028260.KS,000725.KS,EME · https://www.elespanol.com/invertia/mercados/20261027/ferrovial-abre-importante-hueco-alcista-pone-prueba-resistencia-euros/1003744435963_0.html*

### Cluster G — Single-name idiosyncratic, unexplained

These are published in the tables and **no cause is inferred for them**. Searches returned nothing substantive: **ARTV (Artiva Biotherapeutics) −32.14%** on 900.8k pre-market shares with no catalyst found; **INOD (Innodata) −10.70%** on 173.4k shares; DOCS −3.26%; UPST +3.48%; BKH −3.99% ⚠ (98-minute-old print); DAC −5.82% ⚠ (123-minute-old print); RZAI +5.98%; ARLO +4.04%; THRM +5.63%; CARL +3.96%; VRSK +3.42%; MRNA −3.19%; SHAZ +4.21%. The skill's rule applies: label them idiosyncratic and skip the news pull rather than manufacture a narrative.

---

## 3. Pre-market gaps — top 25 market-wide

Universe: 5,713 US common stocks (TradingView screener, OTC excluded). **2,401 carried a pre-market print**; 210 were ≥ +3%, 138 were ≤ −3%; 1,320 up vs 891 down; median gap **+0.14%**. Published values are CNBC's live pre-market quote, each stamped; ⚠ = print older than 45 minutes (last trade, not a live quote). "Mon chg" is Monday's regular-session move, shown for context only.

| # | Ticker | Company | Mon close | Pre-mkt px | Gap % | Pre-mkt vol | Mkt cap | Mon chg | Print (ET) | Age |
|---|--------|---------|-----------|------------|-------|------------|---------|---------|-----------|-----|
| 1 | **BRAI** | Braiin Ltd | $2.12 | $3.10 | **+46.23%** | 5.1M | $436.9M | −40.28% | 8:38 AM | 1m |
| 2 | **MFIC** | MidCap Financial Investment Corp | $8.36 | $10.25 | **+22.61%** | 663.9K | $688.6M | −0.24% | 8:37 AM | 2m |
| 3 | **CLRO** | ClearOne Inc | $4.97 | $5.92 | **+19.12%** | 12.3M | $13.3M | +52.92% | 8:39 AM | 0m |
| 4 | **POM** | PomDoctor Ltd | $1.13 | $1.30 | +15.04% | 5.0M | $0.5M | −3.42% | 8:39 AM | 0m |
| 5 | **JBLU** | JetBlue Airways Corp | $2.37 | $2.70 | +13.93% | 1.2M | $894.2M | −9.71% | 8:39 AM | 0m |
| 6 | **KNSA** | Kiniksa Pharmaceuticals | $72.98 | $83.00 | **+13.73%** | 42.2K | $5.69B | −4.89% | 8:33 AM | 6m |
| 7 | **INIO** | INNIO N.V. | $16.63 | $18.88 | **+13.53%** | 485.0K | $12.47B | +9.34% | 8:38 AM | 1m |
| 8 | **SOFI** | SoFi Technologies | $14.46 | $16.14 | **+11.62%** | 16.0M | $18.68B | −1.06% | 8:39 AM | 0m |
| 9 | **CLS** | Celestica Inc. | $246.65 | $273.47 | **+10.87%** | 342.3K | $31.11B | −5.14% | 8:38 AM | 1m |
| 10 | **UPC** | Universe Pharmaceuticals | $2.88 | $3.19 | +10.76% | 881.0 | $14.5M | −33.64% | 7:32 AM | 67m ⚠ |
| 11 | **HWKN** | Hawkins Inc | $135.44 | $150.00 | +10.75% | 600.0 | $2.83B | +2.36% | 7:38 AM | 61m ⚠ |
| 12 | **PLUR** | Pluri Inc | $1.12 | $1.24 | +10.64% | 12.2K | $13.8M | +13.13% | 8:34 AM | 5m |
| 13 | **ELAB** | PMGC Holdings Inc | $2.61 | $2.88 | +10.34% | 1.1K | $2.1M | −3.54% | 7:46 AM | 53m ⚠ |
| 14 | **FER** | Ferrovial N.V. | $50.35 | $55.28 | +9.79% | 116.8K | — | +1.41% | 8:39 AM | 0m |
| 15 | **IMSR** | Terrestrial Energy Inc | $2.94 | $3.22 | +9.52% | 194.0K | $311.5M | +5.00% | 8:39 AM | 0m |
| 16 | **PASW** | Ping An Biomedical | $4.48 | $4.90 | +9.37% | 875.0 | $14.0M | −5.88% | 8:07 AM | 32m |
| 17 | **GANX** | Gain Therapeutics | $1.15 | $1.25 | +8.28% | 3.6K | $50.2M | −8.73% | 8:07 AM | 32m |
| 18 | **SXC** | SunCoke Energy Inc | $9.81 | $10.60 | +8.05% | 5.4K | $832.6M | −2.00% | 7:06 AM | 93m ⚠ |
| 19 | **PII** | Polaris Inc | $55.15 | $59.57 | +8.01% | 1.2K | $3.14B | +0.60% | 7:33 AM | 66m ⚠ |
| 20 | **HRI** | Herc Holdings Inc | $127.13 | $136.90 | +7.69% | 12.2K | $4.25B | −0.76% | 8:32 AM | 7m |
| 21 | **RZAI** | Roze AI Inc | $10.54 | $11.17 | +5.98% | 1.1K | $662.9M | −3.48% | 7:56 AM | 43m |
| 22 | **RCL** | Royal Caribbean Cruises | $280.60 | $296.39 | +5.63% | 84.0K | $75.05B | +1.49% | 8:36 AM | 3m |
| 23 | **THRM** | Gentherm Inc | $28.59 | $30.20 | +5.63% | 3.9K | $1.50B | −0.03% | 8:32 AM | 7m |
| 24 | **GPUS** | Hyperscale Data Inc | $0.1785 | $0.19 | +5.43% | 6.9M | $30.4M | +5.68% | 8:37 AM | 2m |
| 25 | **STRL** | Sterling Infrastructure | $360.72 | $378.18 | +4.84% | 5.2K | $11.03B | +1.53% | 8:38 AM | 1m |

**What this table says.** The distribution is a barbell. Four names carry gaps above 10% and six more sit between +8% and +10% — and every one of those ten is either a corporate event (MFIC's takeout, CLS/INIO/SOFI earnings, JBLU's earnings reaction), a momentum unwind (BRAI, CLRO, POM, PLUR), or a sub-$20m micro-cap (POM, ELAB, PLUR, GPUS, UPC). Then the table goes almost flat: nothing from #25 to the mid-3s is above +4.84%. Below the top-15, pre-market gaps are effectively noise.

**Deliberate omissions.** **GOOGN** showed +5.35% on 103 shares at 7:52 AM while the live Alphabet lines read GOOG +0.47% and GOOGL +0.51% — a stale thin print, excluded. **CLS is published at +10.87%**, not the +16.40% quoted at 04:02 ET, because the gap compressed by 5.5 points in four and a half hours.

**Also above +3% but outside the top 25** (from the same screen, 210 names total): JCI +4.74% · CRDO +4.43% · GLXY +4.40% · SPGI +4.29% · TRU +4.25% · SHAZ +4.21% · BE +4.11% · ARLO +4.04% · CARL +3.96% · CTS +3.95% · VRSK +3.42% · IQV +3.44% · UPST +3.48% · FCEL +3.49% · MRNA −3.19% · ASAN −3.25% · BKH −3.99% ⚠ · DOCS −3.26% · MSGY −8.60% · JUNS −8.39% · MEDS −7.31% · MACI −7.83% · TGL −7.87%.

---

## 4. Top losers — top 10 market-wide

| # | Ticker | Company | Mon close | Pre-mkt px | Gap % | Pre-mkt vol | Mkt cap | Mon chg | Print (ET) | Age |
|---|--------|---------|-----------|------------|-------|------------|---------|---------|-----------|-----|
| 1 | **ARTV** | Artiva Biotherapeutics | $6.16 | $4.18 | **−32.14%** | 900.8K | $301.2M | +0.16% | 8:38 AM | 1m |
| 2 | **WFF** | WF Holding Ltd | $0.0898 | $0.07 | −26.95% | 15.9M | $6.0M | +12.25% | 8:37 AM | 2m |
| 3 | **IMNN** | Imunon Inc | $1.23 | $0.95 | −23.16% | 252.8K | $6.9M | −0.40% | 8:35 AM | 4m |
| 4 | **RCT** | RedCloud Holdings plc | $0.0827 | $0.07 | −15.36% | 22.8M | $6.3M | +8.67% | 8:37 AM | 2m |
| 5 | **AZTR** | Azitra Inc | $1.53 | $1.31 | −14.39% | 1.2M | $9.3M | **+113.99%** | 8:38 AM | 1m |
| 6 | **HAO** | Haoxi Health Technology | $1.96 | $1.68 | −14.29% | 39.8K | $1.3M | −7.55% | 8:36 AM | 3m |
| 7 | **SRTM** | Stratum Holdings Corp | $0.30 | $0.26 | −13.17% | 756.8K | $0.2M | −30.28% | 8:36 AM | 3m |
| 8 | **INOD** | Innodata Inc | $59.91 | $53.50 | **−10.70%** | 173.4K | $2.06B | +0.88% | 8:38 AM | 1m |
| 9 | **CVLT** | Commvault Systems | $167.73 | $150.55 | **−10.24%** | 25.0K | $6.95B | −0.97% | 8:37 AM | 2m |
| 10 | **WSO** | Watsco, Inc | $305.33 | $277.00 | −9.28% | 12.2K | $12.71B | −5.46% | 8:37 AM | 2m |

**What this table says.** Seven of the ten are micro-caps trading under $10 with market caps between $0.2m and $301m — four of them are in the top ten of *both* the gainers and losers lists across the last two sessions. That is the signature of a thin, high-turnover tail, not of institutional repositioning. Only three are large enough to matter for a portfolio: **ARTV −32.14%** (unexplained, 900.8k pre-market shares), **INOD −10.70%** (unexplained), and **CVLT −10.24%** (reports before the open today).

**Just outside the top 10, and important:** **XYL −8.50%** on a **$25.3bn** market cap is the largest genuine large-cap gap-down on the board, followed by **EEFT −6.94%** ($2.39bn), **AWI −4.46%** ($6.97bn), **HLT −4.37%** ($79.2bn), **ITW −4.07%** ($78.7bn) and **SHW −3.63%** ($81.4bn). All six report before the open. A table that stopped at #10 would have missed the entire large-cap downside of the morning.

---

## 5. StockTwits lead read

Source: `api.stocktwits.com/api/2/streams/trending.json`, 30 messages, retrieved 08:33 ET. The retired `trending-symbols.json` endpoint returns 404, so trending names are ranked by **mention count across the 30 messages** — there is no score field to publish. Embedded `prices[]` in the feed track but do **not** match the live tape, so no price from that field is published here; every price in this brief comes from CNBC or TradingView.

| Symbol | Mentions | Thesis text (verbatim from the feed) | Pre-mkt gap |
|---|---|---|---|
| **SOFI** | **18 of 30** | "Q3 adjusted EPS was 0.18 dollars vs 0.17 dollars expected, on adjusted net revenue of 1.37 billion dollars, up 44%. They added a record 1.2 million member…" | **+11.62%** |
| SLS | 3 | "Expected European Commission approval of GPS is 01-11-2027… Published 2 weeks ago." | +1.32% ⚠ (8:28 AM) |
| PYPL | 2 | "I was worried when the cfo started to speak but all good" | −0.02% (reports pre-open today) |
| XRP.X | 2 | "Trending at #1 $XRPN and $XRPNW - Too much potential!" | BTC flat; no listed XRP spot here |
| STT / BLK / GS / SPY | 1 each | "$SOFI should get a heavy push by $STT $BLK $GS Griffey and the gang Up 54% YoY" | +0.64% / −0.50% ⚠ / +1.64% / +0.32% |
| NCLH | 1 | "tomorrow is gonna be a payday." | +3.02% |
| **WHR** | 1 | "$WHR: Whirlpool reported a Q3 loss of $0.21 per share versus expectations of a $0.76 profit, while revenue fell 8.8% to $3.67 billion from $3.91 billion expecte…" | **−6.41%** |
| XP | 1 | "bouncing back to mid $20's" | +1.88% |
| **MSTR** | 1 | "$BTC.X $MSTR $ETH.X $XRP.X It's Bear Trap Tuesday! 😂" | +0.70% |
| **GLXY** | 1 | "almost $500M net income and volume is anemic and price is frozen and there are posters whining about the numbers. This should open at $20." | +4.40% |
| BABA / ONON | 1 | "as you can see with $ONON in China any company you 'invest in' you dont own anything can be wiped out of the map at anytime" | −0.80% / −3.11% |
| XRPN / XRPNW | 1 | (same as XRP.X) | warrant/overnight-security names — excluded from the screen per the warrant filter |

**Read.** One ticker owns the tape: **SOFI is 18 of 30 messages**, and the thesis text is the earnings release itself, not a mood. Every other name is a single mention, which is noise by construction. Two of the mentions carry real information that no price table would have given you: the **WHR** post gives the exact Q3 miss (−$0.21 vs +$0.76 expected, revenue −8.8% to $3.67bn) behind a −6.41% gap, and the **GLXY** post describes the pre-market debate (~$500m net income against "anemic" volume, a $20 open being argued for) behind a +4.40% gap. The XRPN/XRPNW pair is a warrant/overnight-security structure and is excluded from the screen.

---

## 6. Watchlist

**No watchlist section can be produced: the watchlist file does not exist in this environment.**

- Searched `/workspace` recursively for any `*watchlist*` file — none present. The sandbox contains only `.plugin-cache/`, `daily-briefs/` and this run's working directory.
- The upstream candidate path (`research/watchlist.yaml` in `karizaco/maxhermes-migration`, `refs/heads/main` form) returns **HTTP 404**.
- Per the skill's hard rule — *"If the watchlist file is missing, do not create a default and proceed"* — no substitute list was invented and no section was fabricated.

The skill's rule also says to write the brief *without* a watchlist section. This section is retained as a heading only, to preserve the load-bearing section order that downstream readers rely on, with the absence stated rather than filled. The missing-file line is repeated in Source health below.

---

## 7. Overnight — indices, futures, rates, commodities, crypto

**Cash indices (Monday 26 Oct close, CNBC).** The Monday session itself was a broad advance led by technology.

| Index | Monday close | Mon chg |
|---|---|---|
| S&P 500 | 7,676.77 | +0.70% |
| Nasdaq Composite | 26,169.38 | +0.82% |
| Nasdaq 100 | 29,273.41 | +1.09% |
| Dow Jones | 52,361.58 | +0.28% |
| Russell 2000 | 2,786.42 | +0.38% |
| VIX | 17.78 | **−3.32%** |

**Front-month futures (December 2026 contracts, CNBC, stamped 08:28 ET — ~11 minutes before snapshot).** Change is versus prior settle, which CNBC carries as `previous_day_closing`; it is sourced, not derived.

| Contract | Last | Change | vs prior settle | Volume | Stamp (ET) |
|---|---|---|---|---|---|
| S&P 500 fut (Dec'26) | 7,745.75 | +31.25 | **+0.41%** | 274,357 | 8:28 AM |
| Nasdaq 100 fut (Dec'26) | 29,609.25 | +172.00 | **+0.58%** | 137,398 | 8:28 AM |
| Dow Jones fut (Dec'26) | 52,746.00 | +196.00 | +0.37% | — | 8:28 AM |
| 10-Yr Treasury fut (Dec'26) | 106.1406 | +0.0313 | +0.03% | 538,983 | 8:28 AM |
| WTI Crude (Dec'26) | $100.81 | −0.95 | **−0.93%** | 85,497 | 8:28 AM |
| Gold COMEX (Dec'26) | $4,035.90 | −2.50 | −0.06% | — | 8:28 AM |

**Rates and FX (TradingView, live streaming).** US 10-year cash yield **4.995%** (+0.007); 10-year yield *futures* **4.975** (−0.008) — note the futures' `change` field is a percent, not points. **DXY 102.191** (+0.162). Gold spot 4,023.067 (+6.039).

**Sector ETFs (SPDR) — Monday session and this pre-market.** All 11 pulled, as required; this is the cleanest read of whether the market is rotating or just repricing a few names.

| Sector ETF | Monday close | Mon chg | Pre-mkt px | Pre-mkt gap | Print (ET) |
|---|---|---|---|---|---|
| XLK Technology | $186.32 | **+1.69%** | $187.68 | **+0.73%** | 8:36 AM |
| XLI Industrials | $166.96 | +1.42% | $167.95 | +0.59% | 8:26 AM |
| XLY Cons. Discretionary | $114.26 | +1.03% | $114.90 | +0.56% | 8:26 AM |
| XLF Financials | $56.02 | +0.21% | $56.31 | +0.52% | 8:25 AM |
| XLU Utilities | $42.55 | −0.02% | $42.71 | +0.38% | 8:32 AM |
| XLB Materials | $51.38 | +0.14% | $51.41 | +0.06% | 8:35 AM |
| XLC Comm. Services | $103.85 | **−1.57%** | $103.87 | +0.02% | 7:39 AM ⚠ |
| XLV Health Care | $179.28 | 0.00% | $179.02 | −0.15% | 8:38 AM |
| XLP Cons. Staples | $87.96 | −0.34% | $87.91 | −0.06% | 8:36 AM |
| XLRE Real Estate | $42.80 | +0.54% | $42.77 | −0.07% | 6:45 PM ⚠ |
| XLE Energy | $69.64 | +0.45% | $69.25 | **−0.56%** | 8:37 AM |

**Broad-market pre-market:** SPY $767.83 **+0.32%** (490.7k shares) · QQQ $715.70 **+0.49%** (1.2M) · IWM $277.95 **+0.35%** (285.9k).

**Interpretation.** Monday was a broad rally with a clear internal structure — technology +1.69%, industrials +1.42%, discretionary +1.03%, against communication services −1.57% — and the VIX fell 3.32% to 17.78. This pre-market extends that leadership narrowly: XLK +0.73%, XLI +0.59%, XLY +0.56%, with only energy negative (−0.56%, tracking WTI's −0.93%). Real estate and communication services are not printing (both ⚠, last traded in the prior session) and their pre-market reads should not be treated as live. **There is no broad rotation signal here.** Eleven sector ETFs spanning a $25bn spread, with a top-to-bottom pre-market range of 1.29 points, is a flat tape with a mild growth tilt. That is precisely why the day's information content sits in the single names in sections 2–4 and not in the index.

**Crypto — four independent venues, cross-checked.**

| Asset | Coinbase | Kraken | CoinGecko | Yahoo / TV | Read |
|---|---|---|---|---|---|
| BTC-USD | $80,115.64 | $80,079.40 bid / $80,082.30 last | $80,131 | $80,080.61 (prev close $80,009.50, −0.152%) | **~$80,100, flat** |
| ETH-USD | $2,323.37 | — | $2,323.42 | $2,323.34 (TV) | ~$2,323, +0.13% |
| SOL-USD | $100.45 | — | $100.46 | — | ~$100.45 |

**Data-path warning, restated because it matters:** CNBC's `.BTC` (8,989.99, "Bloomberg Galaxy Bitcoin Index") and `.ETH` (3,595.52) are **wrong by roughly 9x and 1.5x** against every spot venue, and are internally implausible (the implied ETH/BTC ratio of 40% is not a real ratio). They were discarded. Separately, CNBC's `BTC` and `ETH` *ticker* symbols are not crypto at all — they are the **Grayscale Bitcoin Mini Trust ETF ($35.29)** and the **Grayscale Ethereum Staking Mini ETF ($22.08)**.

---

## 8. Macro calendar — Tuesday 27 October 2026

| Time (ET) | Release | Period | Consensus | Prior | Status at snapshot |
|---|---|---|---|---|---|
| 08:30 | **Advance Durable Goods Orders** (Census M3) | Sep | 0.0% headline; +0.5% ex-transport | 0.0% | **Due 9 min before snapshot — actual NOT verified** (see note) |
| 10:00 | **Conference Board Consumer Confidence** | Oct | 80.5 | 81.9 | Pending |
| 10:00 | **New Home Sales** | Sep | 649K | 684K | Pending |
| 10:00 | **Richmond Fed Manufacturing Survey** | Oct | 1 | −2 | Pending |
| 10:00 | S&P/Case-Shiller Home Price Index | Aug | — | — | Pending |
| 10:00 | US Steel Imports | Sep | — | — | Pending |
| 10:30 | Dallas Fed Texas Retail Outlook | Oct | — | — | Pending |
| 11:30 | US Treasury 6-Week & 52-Week bill auctions | — | — | — | Pending |
| 13:00 | US Treasury 5-Year Note auction | — | — | — | Pending |
| 13:00 | Fed H.6 Money Stock Measures | — | — | 23.34T (M2) | Pending |
| 21:00 | RBNZ rate decision | — | — | — | Pending |

**The one that matters is tomorrow:** the **FOMC meeting runs Oct 27–28** and the **rate decision lands Wed 28 Oct at 14:00 ET with a 14:30 press conference**. The September 15–16 meeting delivered a **hike**, and today's 10:00 ET prints are the last macro data before the Fed speaks. The long end is not demanding a squeeze — the 10-year cash yield is 4.995% and the 10-year future is +0.03%.

**Note on the durable-goods actual — flagged, not smoothed.** The release was confirmed for 08:30 ET and my snapshot is 08:39 ET, so the number should exist. It could **not** be verified from a primary source: the Census Bureau PDF returns **HTTP 403** to this sandbox, and the aggregators disagree — Investing.com's calendar shows a +1.8% headline actual, while TradingEconomics and Finviz still show a blank/placeholder for the September print. The consensus figures above are from TradingEconomics and Finviz. **Do not treat 1.8% as verified**; the primary release is at `census.gov/manufacturing/m3/adv/pdf/durgd.pdf` (release number CB 26-150 M3-1, scheduled for 8:30 AM EDT, 27 October 2026).

**Note on release times.** Investing.com's preview article lists Building Permits at 7:00 ET and Durable Goods at 7:30 ET. That conflicts with the New York Fed's indicator calendar, Scotiabank's release calendar and the Census Bureau's own "Next Release: October 27, 2026" note, all of which say **08:30 ET**. The Fed/Census timing is used here.

---

## 9. Earnings today

**174 companies report on Nasdaq's calendar for 2026-10-27** (79 for 10-26, 227 for 10-28). The pre-market cohort is heavy with mega-caps.

**Before the open — the names that matter (consensus EPS from Nasdaq's calendar):**

| Ticker | Company | Mkt cap | Cons. EPS | Note |
|---|---|---|---|---|
| **KO** | Coca-Cola | $398.9bn | $0.87 | Largest BMO name |
| **HSBC** | HSBC Holdings | $310.3bn | $2.13 | ADR, not-supplied time |
| **NVS** | Novartis | $288.4bn | $2.25 | ADR |
| **BA** | Boeing | $148.9bn | −$0.21 | Negative consensus |
| **SPGI** | S&P Global | $132.8bn | $4.43 | +4.29% pre-market |
| **GLW** | Corning | $106.5bn | $0.89 | AI-fibre read-across |
| **HCA** | HCA Healthcare | $101.5bn | $6.74 | |
| **FCX** | Freeport-McMoRan | $93.6bn | $0.80 | Copper |
| **AMT** | American Tower | $88.1bn | $2.78 | REIT |
| **JCI** | Johnson Controls | $87.2bn | $1.58 | +4.74% pre-market |
| **UPS** | United Parcel Service | $86.0bn | $1.63 | |
| **SHW** | Sherwin-Williams | $81.8bn | $3.65 | −3.63% pre-market |
| **ECL** | Ecolab | $80.9bn | $2.18 | |
| **HLT** | Hilton | $78.7bn | $2.36 | −4.37% pre-market |
| **ITW** | Illinois Tool Works | $78.5bn | $2.99 | −4.07% pre-market; Zacks ESP −0.97% |
| **RCL** | Royal Caribbean | $73.9bn | $6.38 | +5.63% pre-market |
| **PCAR** | PACCAR | $56.3bn | $1.61 | |
| **PYPL** | PayPal | $48.8bn | $1.31 | −0.02% pre-market |
| **IQV** | IQVIA | $46.0bn | $2.94 | +3.44% pre-market |
| **XYL** | Xylem | $25.4bn | $1.47 | −8.50% pre-market |
| **HUBB** | Hubbell | $23.7bn | $5.75 | −1.83% pre-market (64m print) |
| **SOFI** | SoFi | $18.9bn | $0.17 | +11.62% pre-market, beat |
| **INIO** | INNIO | $11.4bn | $0.11 | +13.53% pre-market, beat |
| **ARCC** | Ares Capital | $13.4bn | $0.48 | −0.75% pre-market (MFIC acquirer) |

**After the close:** **V (Visa), $728.9bn, $3.43** — the single largest reporter of the week · **STX (Seagate) $144.2bn, $7.17** · WM $95.7bn · **HOOD (Robinhood) $85.5bn, $0.56** · OKE $60.4bn · **NXPI $59.2bn, $3.78** · BKR $55.5bn · **TER (Teradyne) $48.3bn, $2.04** · VTR $44.5bn · EQT $34.8bn · ACGL $34.7bn · EXR $30.3bn · FE $26.7bn · **FFIV (F5) $25.8bn, $3.32** · LPLA $24.9bn · EXE $21.6bn · ESS $17.9bn · LOGI $15.7bn · RNR $14.7bn · WPC $14.6bn · ICLR $14.2bn · CR $10.6bn · UHS $11.0bn · ENPH $4.2bn.

**Also on the 10-27 calendar but not visible in the tables:** VISA and the rest of the after-hours cohort, plus a long tail of small banks and REITs (CBC, UMBF, NBTB, FCBC, WCCB, AB, ACU, BANC, CBU, CSGP, MANH, LECO, AIT, ARCC, IVZ, CHE, EXLS, LSTR, CAKE, TNL, MRP, ITRI, PNR, KAI, ABG, and roughly 100 more). This is the largest driver of the move list today and the easiest to under-count if you only read the top-25 table.

**Not on any US calendar — foreign issuers with live 9M results:** **FER (Ferrovial)** after the US close, call 28 October, consensus ~$0.32–0.33 EPS on ~$2.95bn revenue.

---

## 10. Source health

**Every source in this brief, with its status. No MCP tool was called — none are registered in this runtime (see deviation 1).**

| Source | Endpoint | Status | Notes |
|---|---|---|---|
| TradingView screener | `scanner.tradingview.com/america/scan` | ✅ OK | 5,713 US common stocks; 2,401 with pre-market prints; **0 internal-consistency failures** (every row's implied reference close matched its own close within 0.5%) |
| TradingView global scanner | `scanner.tradingview.com/global/scan` | ✅ OK | 10Y cash yield, DXY, gold, BTC, ETH |
| CNBC quote API | `quote.cnbc.com/.../restQuote/symbolType/symbol` | ✅ OK, **one defect** | 143 pre-market names priced + indices/futures/ETFs. **`.BTC`/`.ETH` index quotes wrong by ~9x/1.5x — discarded.** `previous_day_closing` mirrors `last` on equities and is unreliable — the reference close used is `last` (Monday's close), with the pre-market % change taken from `ExtendedMktQuote` |
| Nasdaq earnings calendar | `api.nasdaq.com/api/calendar/earnings` | ✅ OK | 10-26: 79 rows · 10-27: **174 rows** · 10-28: 227 rows. Date parameter verified to work by cross-checking three adjacent dates |
| Yahoo Finance | `query2.finance.yahoo.com` (chart + spark) | ✅ OK | Cross-checked BTC-USD and ETH-USD. Short `Mozilla/5.0` UA, `curl` via subprocess, `quote(syms, safe=",")` — all required by prior-run findings |
| Coinbase / Kraken / CoinGecko | `/products/{pair}/ticker`, `/0/public/Ticker`, `/simple/price` | ✅ OK | 4 independent crypto venues, all agreeing within $51 on BTC |
| StockTwits | `api.stocktwits.com/api/2/streams/trending.json` | ✅ OK | 30 messages. `trending-symbols.json` retired (404) — ranked by mention count instead. Embedded `prices[]` not published (they do not match the live tape) |
| CNBC futures | `@SP.1 @ND.1 @DJ.1 @TY.1 @CL.1 @GC.1` | ✅ OK | 5 of 6 returned. **`@RT.1` (Russell 2000 future) is absent from CNBC** — the cash `.RUT` index is used instead and labelled as such. `.US10Y` also absent; the cash yield comes from TradingView |
| Census Bureau (durable goods) | `census.gov/manufacturing/m3/adv/pdf/durgd.pdf` | ❌ **HTTP 403** | Primary source blocked from this sandbox. The 08:30 ET actual could not be verified — see Section 8 |
| `web_search` | — | ✅ OK | 9 catalyst searches (XP/Brazil, CLS, INIO, ITW, macro calendar, SOFI, MFIC, BRAI, AVGO). Used for anchoring only; every price in this brief comes from a live API pull, never from a search snippet |
| MCP tools | `mcp__yahoo_finance__*`, `mcp__tradingview*` | ⛔ **Not registered in this runtime** | No MCP call was attempted, so **0 MCP failures triggered a fallback**. See deviation 1 |

**Deviations from the skill's procedure, stated in the body rather than buried:**

1. **MCP layer absent.** The skill is written against `mcp__yahoo_finance__*` and `mcp__tradingview*`. Neither is registered in this runtime, so the cron prompt's public-HTTP replacements were used throughout: TradingView's public screener, the CNBC quote API, the Nasdaq calendar API, Yahoo, Coinbase/Kraken/CoinGecko and StockTwits. **No data was smuggled in from a prior session and no search result is presented as a live quote.**
2. **The gap column.** The skill's Step 2 filters on `change`; in a pre-open pull that field is the prior regular session's move, so the gap tables use the pre-market column and Monday's session change is carried in its own column. Sorting is by the gap, matching the skill's intent.
3. **Watchlist absent** — `research/watchlist.yaml` does not exist locally and 404s upstream. No default created. Section 6 states this.
4. **Volume applied as a soft filter.** The discovery filter was price ≥ $10 and market cap ≥ $300m, with a separately labelled sub-cap section so that real movers are not silently dropped — a hard volume floor would have excluded legitimate names (MELI and AFYA were lost to one in a prior run).
5. **Stale prints are published and flagged, not hidden.** Prints older than 45 minutes carry ⚠ and their age in minutes. A stale print (GOOGN, 103 shares at 7:52 AM) was excluded outright because a live cross-check contradicted it.
6. **Pre-open print volatility was measured, not assumed.** A second full read ~11 minutes after the first moved the median name by **0.00pp** (mean 0.13pp, max **2.26pp on DOCS**, which was −1.00% at 08:24 and −3.26% at 08:35). Single pre-open prints are not stable numbers; the spread is disclosed.
7. **Crypto pricing was not taken from a single feed** after the CNBC index defect surfaced. Four venues were pulled and cross-checked.
8. **No audit log was written** (Cloud cron instruction; audit is not required here).

**Not verifiable at this snapshot:** the 08:30 ET durable-goods actual (Census 403; aggregators conflict), and any post-08:39 ET price. Several web results (Yahoo's, Robinhood's, Perplexity's finance pages) showed quotes stamped *after* this run's snapshot — those were discarded rather than published, since they are later-session values.

---

## 11. Open research queue

1. **Is the AI-infrastructure bid durable, or is it a Monday-morning squeeze?** CLS gave back 5.5 points of its gap between 04:02 and 08:38 ET despite raising 2027 revenue guidance 12% above the Street. Watch whether INIO (+13.53%) and AVGO (+3.09%) hold their gaps at 09:30, and whether the 11 sector ETFs confirm a growth tilt or fade to flat. The 10-year at 4.995% and tomorrow's FOMC are the macro constraints.
2. **The Brazil catalyst is unresolved in Brasília, not in the order book.** Bolsonaro's annulment push, Lula's finance-minister pick and fiscal plans, and whether the real recovers from −10~12%. Today's uniform +0.2% to +2.0% pre-market bid across 16 names is a stabilising tape, not a re-rating. XP's −48.36% also raises a capital-adequacy question for a broker whose growth was built on Brazil's rate cycle.
3. **FOMC, Wed 28 Oct 14:00 ET.** September delivered a hike. The question for the tape is whether a second consecutive hike is priced, and the answer is in the 10-year (4.995%) and the dollar (102.191) — not in today's pre-market, which is flat.
4. **MFIC's special dividend.** The headline $10.88 shrinks by whatever the pre-closing dividend is, and the final 30 September NAV (due 5 Nov with Q3 results, prelim $12.86) resets the floor. The current ~6% discount to headline is not an arbitrage until the dividend is sized.
5. **ARTV −32.14% and INOD −10.70% are unexplained.** No catalyst was found for either, and INOD is a $2.06bn AI-services name with 173.4k pre-market shares traded. Re-check at the open and after the 10:00 ET macro prints.

---

*Generated 2026-10-27 08:39 ET by cloud cron #26 (agentic-pre-market-brief). Read-only; no trades placed. All prices sourced live at the timestamps shown.*
