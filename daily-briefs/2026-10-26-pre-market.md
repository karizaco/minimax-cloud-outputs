# Pre-Market Brief — Monday, 2026-10-26

**Snapshot:** 2026-10-26 08:52 ET (12:52 UTC) · US cash open 09:30 ET · Last completed US session: **Friday 2026-10-23**
**Sources:** TradingView scanner (universe breadth) · CNBC quote API (live pre-market prints) · Nasdaq API (cross-check, earnings calendar) · Coinbase (crypto spot) · `web_search` (catalysts, macro)
**Source tier:** Yahoo Finance was hard-blocked (HTTP 429 on every endpoint) — see *Deviations* below. No number in this brief is estimated or carried from a prior session.

---

## Deviations from the standard data path (read first)

| # | Deviation | Impact | Substitute used |
|---|---|---|---|
| 1 | **Yahoo Finance fully unavailable.** `query1/query2.finance.yahoo.com` returned HTTP 429 on every endpoint from 12:40Z onward — screener, `/v8/finance/chart`, `/v7/finance/spark`, and `/v7/finance/quote` (401, no crumb). Six retries with backoff, then a background patient-retry loop for 30 min; the bucket never cleared. | The skill's primary source for the market-wide screen, pre-market gaps, index levels and futures was unavailable. | TradingView `scanner.tradingview.com/america/scan` (5,715 US equities, with pre-market columns) for breadth; CNBC quote API for every published price; Nasdaq API for cross-checks. |
| 2 | **Yahoo predefined-screener tier unavailable.** | The `day_gainers` / `day_losers` / `most_actives` screen could not be pulled. | Full TradingView US universe pulled and screened client-side; every published row then re-verified against a live CNBC pre-market print. |
| 3 | **TradingView pre-market prints lag the live tape.** Measured across 61 names where both sources had a print: median absolute divergence **0.32pp**, mean 0.52pp, worst case **3.55pp on XP** (the fastest-moving name on the tape, which was still quoting −47.5% against CNBC's live −51.0%). | TV was unsafe to publish directly. | All prices, percentages and volumes in this brief come from **CNBC live pre-market prints** (timestamped 08:41–08:52 ET). TV was used only to *discover* candidates and cross-check direction. |
| 3b | **Reported Friday share volume is implausibly thin for some mega-caps** — MELI shows 338,837 Friday shares from both TradingView *and* CNBC against a $91.8bn market cap (~$0.6bn of turnover), and AFYA shows ~118k on a $1.4bn cap. | A hard >500k volume filter would have silently dropped MELI (−14.5% pre-market) and AFYA (−21.1%) from the screen. | The skill's >500k volume filter was applied as a **soft** filter for candidate discovery only; no published row was excluded on volume alone, and every row carries its own reported volume so the thinness is visible. |
| 4 | **Futures quotes are ~10 minutes stale** (CNBC futures timestamp 08:41 ET; TradingView futures flagged `delayed_streaming_600`). | Futures levels and implied gaps are as of ~08:41 ET, not 08:52. | Stated in-line on every futures row. Cash pre-market prints are 08:41–08:52 ET. |
| 5 | **Watchlist file absent.** `research/watchlist.yaml` does not exist in this sandbox. | No watchlist section, per skill rule (never fabricate a default). | Surfaced in *Source health*. The market-wide screen stands on its own. |
| 6 | **10-year cash yield not directly retrievable** (CNBC `.US10Y` symbol absent; Stooq CSV endpoint returned empty bodies). | No spot 10-year yield. | 10-Year yield *futures* level from TradingView (4.989) and the 10-Yr Treasury future (Dec'26) from CNBC — both labelled as futures. |

---

## 1. TL;DR

- **Brazil's election result is the whole story.** Lula won a surprise reelection in Sunday's runoff, and every Brazil-linked US-listed name is being repriced violently: **XP −51.0%** ($14.90), **STNE −38.2%**, **PAGS −33.7%**, **BBD −28.8%**, **ITUB −27.6%**, **EWZ −27.4%** ($30.93 on 29.8M shares), **NU −25.3%** (21.6M pre-market shares), **PBR −21.6%**, **AFYA −21.1%**, **MELI −14.5%**, **DLO −9.2%**. The market's objection is fiscal: spending, inflation and the real.
- **US index futures are up anyway.** ES +0.27% (7,680.25), NQ +0.50% (29,263.75), YM +0.32% (52,563), RTY +0.10% (2,787.3) against a Friday close of SPX 7,623.68 / DJI 52,215.16 / COMP 25,955.34 / RUT 2,775.90. VIX 19.23, −1.13% on the session. The Brazil shock is a *country* event, not yet a US-market event.
- **Memory/AI hardware is bid pre-market.** MU +2.55% ($899.90), SNDK +2.50%, LITE +3.42%, COHR +3.68%, AXTI +4.45%, MXL +3.36%, TSEM +3.17%, AMAT +1.65%, LRCX +1.95%, INTC +1.66%, NVDA +1.09%. SOXX +1.63%, SMH +1.35%.
- **Two live corporate events.** EQT is acquiring Range Resources in a $50B+ all-stock deal — **RRC +11.56%** ($50.78), **EQT −6.24%** ($52.16). Xencor's ESMO kidney-cancer data reset the biotech tape — **XNCR +33.64%** ($33.65).
- **Energy is giving back Friday's spike.** USO was +4.32% Friday and is now −2.33%; WTI Dec'26 futures $101.13, −2.07% from a $103.27 Friday settle; XLE Friday +2.60% → pre-market −1.39%.
- **Crypto complex is soft.** BTC $80,254, ETH $2,323, SOL $101.55. MSTR −1.79%, COIN −2.36%, IREN −2.55%, CRCL −3.31%, CRWV −3.59%.
- **Biotech is a two-way tape.** XNCR +33.6% and SGRY +23.6% (Bon Secours take-private) against MRNA −7.17% (sell-the-news on the intismeran Phase 3).
- **Watchlist:** no watchlist file exists in this environment, so no watchlist section — the screen above is market-wide by design.

**Read the tape this way:** a violent single-country repricing is sitting on top of an otherwise firm, semis-led US pre-market. If the Brazil complex stabilises, the US tape is a continuation bid; if it spreads to EM financials, the +0.3% futures signal is not safe. The single most useful cross-check today is whether EWZ's 29.8M-share pre-market volume finds a bid in the first hour.

---

## 2. Theme clusters

### Cluster A — Brazil election shock (the dominant cluster)
**Leader:** XP Inc. −51.00% ($14.90, 5.16M pre-market shares). **Corroborators:** NU −25.28% (21.6M shares), EWZ −27.38% (29.8M), BBD −28.75% (5.44M), ITUB −27.61% (4.66M).

Lula's surprise reelection in Sunday's runoff defied the rightward shift priced in since the first round, and the sell-off is concentrated in exactly the high-beta, rate-sensitive Brazil exposure that rallied into the vote. XP had roughly doubled off its August lows and closed Friday up 3.61% at $30.41 near its 52-week high of $32.73; it is now trading at the bottom of its 52-week range ($14.80 low). Overhangs layered on the election: the 16 October board disruption (board member Escobari's resignation, Rodrigo Kede Lima named interim director), and Assenagon cutting roughly 7.9% of its stake in the days before the move. Q3 results are not due until the week of 16 November, so no earnings release is the catalyst. PBR and PBR.A are down with the complex on fiscal read-through to the oil budget, and MELI (−14.5%) and DLO (−9.2%) are also lower — their own country drivers are not in the coverage, so treat them as regional risk-off rather than confirmed Brazil-election casualties.
- Sources: [Investing.com — Why is XP stock plummeting 45% today?](https://www.investing.com/news/stock-market-news/why-is-xp-stock-plummeting-45-today-93CH-4971958) · [TradingKey — US Pre-Market: Brazilian assets sold off](https://www.tradingkey.com/analysis/stocks/us-stocks/262239293-us-spacex-ewz-nu-xp-petrobras-skhynix-tradingkey) · [Perplexity Finance — XP](https://www.perplexity.ai/finance/XP)

### Cluster B — Memory / AI hardware bid
**Leader (magnitude):** AXTI +4.45% ($54.40). **Leaders (magnitude + liquidity):** MU +2.55% ($899.90, 736k pre-market shares, $993B cap), SNDK +2.50% ($1,269). **Corroborators:** LITE +3.42%, COHR +3.68%, MXL +3.36%, TSEM +3.17%, SMTC +2.65%, AAOI +2.46%, KLAC +2.06%, LRCX +1.95%, AMAT +1.65%, MRVL +1.52%, INTC +1.66%, AMD +1.20%, AVGO +1.08%, NVDA +1.09%.

Bank of America's Vivek Arya reiterated Buy with a $1,550 target on Micron, arguing memory supply stays tight through 2027–2028 and that multi-year strategic customer agreements (about 35% of MU sales, targeted near 50% by 2030) give unusual revenue visibility. SK Hynix scrapped its Solidigm Nasdaq IPO (+4.42% in Seoul, ADR +4.05%) and is reported to be weighing a roughly $12bn special dividend, which pulled the memory complex with it; Mizuho expects NAND pricing to stay firm through 2027. The counterweight is real: Morgan Stanley has flagged a 10–15% extension of the semiconductor correction into mid-November, and AI-financing stress (CoreWeave, −3.59% pre-market) is unresolved.
- Sources: [TipRanks — Why are Micron, SanDisk, and SK Hynix rising in premarket](https://www.tipranks.com/news/why-are-micron-sandisk-and-sk-hynix-stocks-rising-in-premarket-today-october-26) · [Benzinga — What's going on with Micron Monday](https://www.benzinga.com/markets/tech/26/10/62585814/whats-going-on-with-micron-technology-stock-monday-7) · [Infos达克 Daily — 10/26 개장체크](https://kr.investing.com/news/stock-market-news/article-2140352)

### Cluster C — Biotech dispersion on ESMO read-through
**Leader:** XNCR +33.64% ($33.65, 1.70M pre-market shares). **Corroborator:** SGRY +23.62% ($19.47, 115k shares). **Counterweight:** MRNA −7.17% ($185.80, 1.01M shares).

Xencor presented Phase 1 XmAb819 (ENPP3 x CD3 bispecific) data at the ESMO Congress in Madrid and selected 400 mcg/kg as the proposed IV Phase 3 dose: 45.5% confirmed ORR (5 of 11), 55% uORR, 82% six-month Kaplan-Meier PFS, with 18 confirmed partials plus one complete response in the PD-(L)1-experienced / two-VEGFR-TKI subgroup (n=42). Management plans FDA discussions on an accelerated-approval pathway in 1H27 and a global randomised trial versus tivozanib, with a registration-enabling study targeted by end-2027; cash funds operations into 2029. The caveats are real: an n=11 cohort, no randomised control, and grade 3+ treatment-related adverse events in 72% of expansion patients (mostly liver-enzyme elevations). Separately, the FT reported Surgery Partners has agreed to be taken private by Bon Secours Mercy Health at roughly $20 per share, about $6bn including debt, with Bain Capital retaining its nearly 40% stake. Moderna is the mirror image — a Phase 3 result (intismeran autogene + Keytruda cut melanoma recurrence-or-death risk by 42%, HR 0.58) that fell short of the 49% seen in the smaller Phase 2b, after an abstract leaked two days early, sustaining a sell-the-news reaction.
- Sources: [Xencor press release via StockWatch](https://www.stockwatch.com/News/Item/U-b20261025921014-U!XNCR-20261025/U/XNCR) · [Xencor IR — webcast announcement](https://investors.xencor.com/news-releases/news-release-details/xencor-host-webcast-discuss-results-phase-1-study-xmab819) · [Investing.com — Premarket movers: Moderna, Brazil ADRs drop](https://ph.investing.com/news/stock-market-news/premarket-movers-moderna-brazil-adrs-drop-spacex-rises-2649220) · [Benzinga — Moderna slides again](https://www.benzinga.com/markets/biotech/26/10/62556311/moderna-stock-slides-again-friday-whats-going-on)

### Cluster D — EQT / Range Resources: a $50bn all-stock gas merger
**Leader:** RRC +11.56% ($50.78, 301k pre-market shares). **Counterparty:** EQT −6.24% ($52.16, 401k shares).

EQT will acquire Range Resources in an all-stock transaction at 0.987 EQT shares per Range share, creating a combined company with pro-forma enterprise value above $50bn, over 9 Bcfe/d of net production, more than 30 years of inventory across nearly 3M net acres, and $325m of targeted annual synergies within two years (long-term path above $600m). Range holders take roughly 27% of the combined entity; both boards approved unanimously, shareholder and regulatory approval are pending, and the deal is expected to close in Q1 2027. Both companies will still report Q3 results after the close on 27 October, and the 28 October earnings calls were cancelled. The exchange ratio is what carries RRC above its prior 52-week high and takes EQT down — the classic merger-arb asymmetry. Raymond James raised its RRC target to $48 from $45 the same morning while Gerdes Energy Research downgraded to Neutral with a $49 target, calling the move a ~24% rally since mid-June.
- Sources: [Range Resources IR — EQT announces strategic acquisition](https://ir.rangeresources.com/news-releases/news-release-details/eqt-announces-strategic-acquisition-range-resources-creating) · [Investing.com — Why is Range Resources stock surging?](https://ng.investing.com/news/stock-market-news/why-is-range-resources-stock-surging-today-93CH-2756831) · [Yahoo Finance — EQT to acquire Range Resources in $50 billion all-stock deal](https://finance.yahoo.com/energy/articles/eqt-acquire-range-resources-50-105220741.html)

### Cluster E — Oil gives back Friday's geopolitical spike
**Leader:** USO −2.33% pre-market after +4.32% Friday; WTI Dec'26 futures $101.13, −2.07% (08:41 ET). **Corroborators:** XLE Friday +2.60% → pre-market −1.39%; XOM −1.37%; CVX −1.19%; OXY −1.81%; RIG −1.95%; FRO +2.19%.

Friday's tape was an energy-led tape — XLE +2.60%, USO +4.32%, XOM +2.79%, CVX +2.88% — driven by crude reaching five-month highs on Middle East supply risk. Overnight that premium is unwinding: WTI Dec'26 has fallen back to $101.13 from a $103.27 Friday settle, giving back roughly two-thirds of Friday's USO move, and XLE is giving back more than a point of Friday's gain. Natural gas is a separate story — around $2.77/MMBtu on mild weather, with Goldman's mixed gas view (strong Permian associated-gas supply growth versus El Niño-related winter-demand risk) cited against Range's move. This is the tape the FOMC is being asked to price.
- Sources: [Investing.com — Range Resources surging today](https://ng.investing.com/news/stock-market-news/why-is-range-resources-stock-surging-today-93CH-2756831) · [Perplexity Finance — RRC](https://www.perplexity.ai/finance/RRC?comparing=RRC,AR,CPK,CRK,EQT,TPL)

### Cluster F — Cybersecurity: Friday's theme, still live (carry-over)
Friday's tape was led by identity and security software on AI-discovered PHP flaws (PHP runs on more than 70% of websites) plus NSA and FBI advisories telling organisations to patch or take vulnerable legacy systems offline. CRWD +8.25%, NTSK +9.37%, FSLY +8.73%, SAIL +8.62%, BAND +9.09%, NN +9.45%, PANW +7.22%, ZS +7.31%, NET +7.29%, OKTA +5.82%; an Evercore ISI channel-partner survey of firming security budgets pointing at identity and data protection was the proximate trigger, and Sam Altman's "I no longer think we're gonna be able to just patch all the bugs" (23 Oct) kept the theme alive into this morning. Today it is quiet rather than gone: CRWD +0.76% pre-market, IGV +0.00% (110.59 on 28.8k pre-market shares). Note the valuation flag — CRWD trades around 232x trailing earnings and above its $247.25 consensus target.
- Sources: [Yahoo Finance — SailPoint Soars 11%, CrowdStrike Up 6% as Cybersecurity Stocks Rally](https://finance.yahoo.com/markets/stocks/articles/sailpoint-soars-11-palo-alto-170741321.html) · [Yahoo Finance — Altman: "I No Longer Think We're Gonna Be Able To Just Patch All The Bugs"](https://finance.yahoo.com/technology/ai/articles/altman-says-no-longer-think-105235640.html) · [Business Insider — Cybersecurity stocks climb](https://markets.businessinsider.com/news/stocks/cybersecurity-stocks-climb-with-cloudflare-net-and-netskope-ntsk-up-7-here-s-why-1036661750)

### Cluster G — Crypto complex: lower, with AI-datacenter credit stress
BTC $80,253.95 (24h range 79,255–80,859), ETH $2,323.46 (24h range 2,290–2,362), SOL $101.55 — all from Coinbase's live ticker at 08:52 ET. Equities: MSTR −1.79% ($143.40), COIN −2.36% ($160.60), IREN −2.55% ($24.27, 3.82M pre-market shares), CLSK −1.65%, MARA −1.57%, RIOT −1.12%, BMNR −2.59%, CRCL −3.31%, CRWV −3.59% (4.90M pre-market shares), IONQ −2.11% (897k shares), CORZ −2.21%. Spot is essentially flat over 24 hours; the damage is in the leveraged/credit-sensitive names, where CoreWeave is the principal drag.

---

## 3. Pre-market gaps — top 25 market-wide

Universe: 5,715 US equities (TradingView, OTC excluded). Filters: pre-market print ≥ ~1.9%, pre-market price > $10, market cap > $1bn. All values are live CNBC pre-market prints (08:41–08:52 ET); Friday close and Friday % change for context.

| # | Ticker | Pre-mkt | Pre-mkt % | P-mkt vol | Fri close | Fri % | Mkt cap | Cluster |
|---|---|---|---|---|---|---|---|---|
| 1 | XNCR | 33.65 | **+33.64%** | 1,704,974 | 25.18 | −2.55% | 1.87B | C — ESMO data |
| 2 | SGRY | 19.47 | **+23.62%** | 114,566 | 15.75 | −0.94% | 2.06B | C — take-private |
| 3 | MACI | 12.32 | +12.00% | 39,123 | 11.00 | −3.21% | 105M | micro/SPAC |
| 4 | RRC | 50.78 | **+11.56%** | 300,694 | 45.52 | +3.78% | 10.64B | D — EQT merger |
| 5 | AXTI | 54.40 | +4.45% | 420,360 | 52.08 | +1.01% | 3.42B | B — semis |
| 6 | COHR | 217.00 | +3.68% | 199,135 | 209.30 | +0.71% | 41.22B | B — optical |
| 7 | LITE | 782.00 | +3.42% | 166,597 | 756.20 | +0.48% | 68.50B | B — optical |
| 8 | MXL | 65.59 | +3.36% | 52,053 | 63.46 | −2.79% | 5.77B | B — semis |
| 9 | TSEM | 172.90 | +3.17% | 61,045 | 167.60 | −0.09% | 19.02B | B — semis |
| 10 | SMTC | 135.50 | +2.65% | 34,755 | 132.00 | +5.50% | 12.32B | B — semis |
| 11 | MU | 899.90 | +2.55% | 736,317 | 877.50 | +2.46% | 992.88B | B — memory |
| 12 | TSLA | 381.70 | +2.55% | 1,108,953 | 372.20 | −0.63% | 1.47T | — |
| 13 | SNDK | 1,269.00 | +2.50% | 277,136 | 1,238.00 | −1.82% | 178.93B | B — memory |
| 14 | AAOI | 69.17 | +2.46% | 417,064 | 67.51 | −0.82% | 5.73B | B — optical |
| 15 | SKE | 28.70 | +2.43% | 36,528 | 28.02 | −2.51% | 3.52B | E — gas/mining |
| 16 | ABCL | 12.10 | +2.37% | 31,264 | 11.82 | +3.96% | 3.83B | C — biotech |
| 17 | VRT | 198.60 | +2.20% | 248,834 | 194.30 | −0.65% | 74.81B | B — AI power |
| 18 | FRO | 54.10 | +2.19% | 42,811 | 52.94 | +3.36% | 3.9B | E — tanker |
| 19 | BE | 197.50 | +2.16% | 884,622 | 193.30 | −11.24% | 57.15B | B — AI power |
| 20 | CRDO | 150.40 | +2.11% | 157,024 | 147.30 | −9.51% | 27.70B | B — AI networking |
| 21 | KLAC | 148.60 | +2.06% | 228,924 | 145.60 | −1.50% | 190.02B | B — semi-cap |
| 22 | MGM | 28.61 | +1.96% | 34,742 | 28.06 | −4.88% | 7.06B | — |
| 23 | LRCX | 234.60 | +1.95% | 89,968 | 230.10 | −0.02% | 287.43B | B — semi-cap |
| 24 | HYMC | 15.73 | +1.88% | 34,580 | 15.44 | −2.03% | 0.6B | E — mining |
| 25 | VSH | 27.20 | +1.87% | 36,285 | 26.70 | −1.22% | 4.10B | B — semis |

**What this table says.** Three of the top four are single-catalyst events, not a theme: an ESMO readout, an FT take-private report, and a merger ratio. Below that, the tape turns into a clean factor bet — 13 of the 25 are AI hardware, optical or semi-cap names, and the two large-cap momentum entries (TSLA +2.55%, BE +2.16% after Friday's −11.24%) are the same trade. MACI at a $105m market cap with 39k pre-market shares is noise by construction and is flagged as such rather than dressed up as a signal.

---

## 4. Top losers — top 10 market-wide

| # | Ticker | Pre-mkt | Pre-mkt % | P-mkt vol | Fri close | Fri % | Mkt cap | Note |
|---|---|---|---|---|---|---|---|---|
| 1 | XP | 14.90 | **−51.00%** | 5,155,001 | 30.41 | +3.61% | 15.71B | Brazil election + governance overhang |
| 2 | STNE | 7.09 | −38.24% | 4,120,310 | 11.48 | +2.96% | 2.65B | StoneCo, Brazil |
| 3 | PAGS | 7.59 | −33.65% | 919,593 | 11.44 | +1.42% | 3.20B | PagSeguro, Brazil |
| 4 | BBD | 2.90 | −28.75% | 5,435,924 | 4.07 | +3.04% | 45.57B | Banco Bradesco |
| 5 | ITUB | 7.00 | −27.61% | 4,661,358 | 9.67 | +1.90% | 106.63B | Itaú Unibanco |
| 6 | EWZ | 30.93 | −27.38% | 29,767,027 | 42.59 | +1.77% | ETF (AUM 7.64B) | iShares MSCI Brazil ETF |
| 7 | NU | 11.33 | −25.28% | 21,628,154 | 15.16 | +2.92% | 73.23B | Nu Holdings |
| 8 | SBS | 4.90 | −23.44% | 648,358 | 6.40 | +2.07% | 22.56B | Saneamento Básico, Brazil |
| 9 | PBR.A | 18.27 | −22.35% | 1,896,879 | 23.53 | +2.75% | 151.64B | Petrobras preferred |
| 10 | PBR | 20.50 | −21.64% | 5,040,369 | 26.16 | +2.11% | 168.59B | Petrobras |

*Next in line:* AFYA −21.14% ($11.90, 1.33B cap), MELI −14.47% ($1,548.14, 91.77B cap), DLO −9.23% ($13.67, 4.34B), MRNA −7.17% ($185.80), BBAR −6.00% ($12.38, 2.69B), EQT −6.24% ($52.16), SAN −3.74% ($12.36, 186.91B), CRWV −3.59% ($52.29), CRCL −3.31% ($83.07).

*Market caps for the Brazil complex are whole-company figures from the CNBC quote feed, not ADR float.*

**What this table says.** Every one of the top ten is Brazil, and that is the point: the loss is not being priced as a US-market event, it is being priced as a repricing of one sovereign's policy path. Three things make this more than a headline reaction. First, the *breadth* is total — banks, brokerages, payments, water utility, the oil major, the country ETF and a healthcare roll-up all down 20–38% together. Second, the pre-market volume is enormous for a US session: EWZ 29.8M shares, NU 21.6M, XP 5.2M, BBD 5.4M, ITUB 4.7M, PBR 5.0M. Third, there is no earnings release anywhere in this group to absorb the flow — XP's Q3 is not until the week of 16 November, so this repricing runs on fiscal expectations alone, with no scheduled catalyst to close it. The one genuine counter-signal is that US index futures are positive while all of this is happening, and the Dow futures are up more than the Nasdaq futures (+0.32% vs +0.50% inverted, but both positive) — if this is a Brazil event, the US tape should absorb it.

---

## 5. StockTwits lead read

StockTwits' retired `trending-symbols.json` endpoint 404s (confirmed again today). The live substitute, `api.stocktwits.com/api/2/streams/trending.json`, returned 30 messages timestamped 12:29–12:32 UTC. This endpoint carries **no** thesis text or trending score, so symbols are ranked by mention count across the feed. The feed's embedded prices are unreliable and are not used — every price below comes from the live CNBC pre-market tape.

| Ticker | Mentions | Pre-mkt | Pre-mkt % | Fri % | Read |
|---|---|---|---|---|---|
| SPY | 6 | 762.25 | +0.30% | −0.52% | Index chatter, no directional conviction |
| META | 6 | 637.50 | −0.80% | −0.96% | Repeated complaint about ~$100bn of new share issuance and capex spend; also noting the stock was 770 two weeks ago |
| CRWV | 5 | 52.29 | −3.59% | −2.46% | Retail asking "how realistic is $60 in a day or two" — sentiment is still long despite the price |
| QQQ | 5 | 708.69 | +0.61% | −0.01% | META-vs-index banter, no new information |
| CRML | 2 | 6.31 | −0.79% | +2.75% | Catalyst cited: Critical Metals' European Lithium acquisition approved by the Supreme Court of Western Australia — no pre-market response yet |
| NBIS | 2 | 159.00 | +0.16% | −0.27% | "Fair value 200, should gap up this week" — pure opinion, no flow |
| MELI | 1 | 1,548.00 | −14.47% | −0.81% | "Brazil is uninvestable at this point" — the Brazil view is the dominant retail narrative |
| XP | 1 | 14.90 | −51.00% | +3.61% | Taunting the Friday bulls |
| MRNA | 1 | 185.80 | −7.17% | −1.25% | Bearish reaction to the intismeran data |
| PBR | 1 | 20.50 | −21.64% | +2.11% | Fiscal-policy commentary on the Brazilian congress |
| IREN | 1 | 24.27 | −2.55% | −2.37% | Options pain — Nov 6 calls "severely underwater" |
| VKTX | 1 | 24.38 | −0.10% | −5.54% | Position commentary; no catalyst |
| AMZN | 1 | 250.40 | +0.97% | −0.95% | Long-term target discussion, no tape relevance |

**What this says.** The social tape is not where the news is — it is reacting to it, and one theme dominates even the low-mention tail: Brazil. There is no chatter on XP, NU or the Brazilian banks beyond the single Brazil-is-uninvestable comment on MELI, which means the Brazil repricing has not yet been argued out in either direction, and no pre-market dip-buying is visible in the message flow. CRML is the one genuine un-priced catalyst in the feed (a court approval in Western Australia that the tape has not traded yet). Note that the feed carries abusive third-party text; anything in that category is redacted in this brief rather than reproduced.

---

## 6. Watchlist

**Not available.** The skill reads `research/watchlist.yaml`; that file does not exist in this Cloud environment (the workspace was empty at run start — no `research/` tree, no watchlist of any name). Per the skill's explicit rule, no default watchlist was created and the brief proceeds without a watchlist section rather than inventing one. If a watchlist should apply to this brief, it needs to be deployed into the sandbox.

---

## 7. Overnight / futures / index / crypto

**Cash index levels — Friday 2026-10-23 close (cash is closed pre-market):**

| Index | Level (Fri close) | Fri % |
|---|---|---|
| S&P 500 | 7,623.68 | −0.52% |
| Dow Jones Industrial Average | 52,215.16 | −1.23% |
| NASDAQ Composite | 25,955.34 | −0.21% |
| NASDAQ-100 | 28,957.53 | 0.00% |
| Russell 2000 | 2,775.90 | −0.29% |
| VIX (live 08:51 ET) | 19.23 | −1.13% |

**Index futures (Dec'26 contracts, as of 08:41 ET — ~10 min stale):**

| Contract | Level | Change vs prior settle | Prior settle |
|---|---|---|---|
| S&P 500 (ES) | 7,680.25 | +0.27% | 7,659.75 |
| Nasdaq-100 (NQ) | 29,263.75 | +0.50% | 29,117.75 |
| Dow (YM) | 52,563.00 | +0.32% | 52,394.00 |
| Russell 2000 (RTY) | 2,787.30 | +0.10% | 2,784.50 (derived from TV change %) |

**Commodities, rates, FX:**

| Asset | Level | Change |
|---|---|---|
| WTI Crude Dec'26 | $101.13 | −2.07% |
| Gold COMEX Dec'26 | $4,032.40 | +0.61% |
| US Dollar Index (DX) | 101.889 | +0.08% (live 08:51 ET) |
| 10-Yr Treasury future Dec'26 | 106.125 | −0.03% |
| 10-Yr yield futures (proxy for spot 10Y) | 4.989 | −0.18% on session |
| USD 6E (EUR) | 1.12195 | +0.03% |

**Crypto spot (Coinbase live ticker, 08:52 ET):**

| Asset | Spot | 24h open | 24h high | 24h low |
|---|---|---|---|---|
| BTC-USD | $80,253.95 | 80,347.89 | 80,859.26 | 79,255.00 |
| ETH-USD | $2,323.46 | 2,331.74 | 2,361.83 | 2,290.00 |
| SOL-USD | $101.55 | — | — | — |

**Crypto-related equities (pre-market):** MSTR $143.40 −1.79% · COIN $160.60 −2.36% · MARA −1.57% · RIOT $12.39 −1.12% · CLSK −1.65% · IREN $24.27 −2.55% · BMNR −2.59% · CRCL $83.07 −3.31% · CRWV $52.29 −3.59% · IONQ −2.11% · CORZ −2.21%

**Sector rotation (Friday close → pre-market):**

| ETF | Friday % | Pre-mkt % | Read |
|---|---|---|---|
| XLE (energy) | +2.60% | −1.39% | Friday's leader gives it all back |
| XLK (tech) | +0.49% | +0.68% | Continues Friday's bid |
| XLB (materials) | −0.74% | +0.71% | Leadership broadening |
| XLI (industrials) | −1.27% | +0.66% | Rebound |
| XLC (comm. services) | −1.78% | +0.67% | Rebound |
| XLY (cons. disc.) | −1.66% | +0.81% | Rebound |
| XLF (financials) | −1.32% | +0.04% | Flat — no US financial contagion |
| XLV (health care) | −1.11% | +0.03% | Flat |
| XLP (staples) | −1.92% | −0.09% | Friday's loser stays a loser |
| XLU (utilities) | −0.72% | −0.02% | Flat |
| XLRE (real estate) | +0.12% | −0.02% | Flat — rates not moving |
| SOXX (semis) | +0.53% | +1.63% | The day's cleanest leadership |
| SMH (semis) | +0.74% | +1.35% | Confirms |
| IGV (software) | +1.72% | +0.00% (110.59, 28.8k sh) | Friday's cyber bid not extended |
| USO (oil) | +4.32% | −2.33% | Oil premium unwinding |
| GLD (gold) | −0.65% | +0.49% | Bid |
| TBT (long bonds) | +1.12% | −0.34% | Friday's rate rally giving back |
| HYG (credit) | −0.06% | −0.09% | No credit stress in the US |
| JETS (airlines) | −2.50% | +2.30% | Oil relief — a clean read-through |
| XBI (biotech) | −1.38% | +0.31% | Slightly bid on the XNCR print |

**What this block says.** The futures curve is mildly risk-on at the index level and then narrows sharply at the bottom: RTY +0.10% versus NQ +0.50% is a large-cap-only bid, and IWM's pre-market print is +0.04%, effectively flat. That is what a 27% drawdown in a sovereign's equity market does to a risk appetite even when the direct exposure is a handful of tickers — nothing is priced for small-cap stress yet, and that is the gap most likely to fill today. HYG flat and TBT down confirm this is not a rates or credit event; it is an idiosyncratic country repricing. The oil reversal is the cleanest read-through in the block: JETS +2.30% pre-market after −2.50% Friday is an airline margin call, and it only makes sense if crude is genuinely coming off the spike. Gold bid +0.49% alongside a flat dollar says the market is not rotating out of risk in general.

---

## 8. Macro calendar

**Today, Monday 26 October (all times ET):**
- 08:30 — Chicago Fed National Activity Index (already released as of this snapshot)
- 10:30 — Dallas Fed Manufacturing Survey
- 13:00 — 2-Year Note Auction
- No top-tier US data today. Overnight Asia carried Japan's Leading Indicators (final) and South Korea's Q3 GDP; both are listed on the published calendars without a reliable ET conversion, so no time is asserted here.

**The week ahead (this is the real event risk):**
- **Tue 27 Oct** — FOMC meeting begins; Durable Goods (08:30), FHFA + Case-Shiller (09:00), New Home Sales and Consumer Confidence (10:00), Richmond Fed (10:00)
- **Wed 28 Oct** — **FOMC decision 14:00 ET, press conference 14:30 ET**; consensus is a hold at 3.75–4.00% (a September hike was unanimous; CME implies ~10% odds of another hike, and September CPI at 3.7% y/y has pushed inflation risk up). Also Trade in Goods and wholesale inventories (08:30), BoC and RBNZ decisions
- **Thu 29 Oct** — Q3 GDP (08:30, consensus ~3.0–3.2% SAAR), jobless claims, PCE inflation and Personal Income/Outlays (08:30; headline PCE consensus 3.7% y/y, core 3.1%); ECB decision 14:15 ET
- **Fri 30 Oct** — Employment Cost Index (08:30), Chicago PMI (09:45)
- **Mon–Wed 27–28 Oct** — hyperscaler capex commentary and Big Tech earnings: Alphabet, Microsoft and Amazon all report this week, plus Micron's fiscal Q4 on Wednesday. The AI-capex narrative that drives the semis bid is being tested inside the FOMC window.

**Background:** September CPI came in at 3.7% y/y against 3.6% expected, and the Iran conflict keeps energy costs elevated — that combination is what puts a hike on the table at a meeting where the base case is a hold.

---

## 9. Earnings today

72 companies report on the Nasdaq calendar. Material by size, not by count:

**Before the open:** Verizon (VZ, $188bn cap, EPS est. $1.27) · Cemex (CX, $15.3bn, $0.25) · MakeMyTrip (MMYT, $4.3bn, $0.36, +2.16% pre-market after −7.17% Friday) · Alliance Resource Partners (ARLP, $3.3bn, +3.21% pre-market) · Bank of Hawaii · Lakeland Financial · HBT Financial · Easterly Government Properties · Business First Bancshares.

**After the close:** Welltower (WELL, $171bn, $1.64) · **Cadence Design Systems (CDNS, $85.3bn, $1.61, +0.48% pre-market)** · **Nucor (NUE, $58.5bn, $5.71, +1.51% pre-market)** · Public Storage (PSA, $57.8bn) · The Hartford (HIG, $37.8bn) · **Celestica (CLS, $30.8bn, $2.89, +3.68% pre-market after −3.35% Friday)** · Cincinnati Financial · Brown & Brown · Principal Financial · Sun Communities · Gerdau · **Amkor Technology (AMKR, $9.7bn, +0.66%)** · **Rambus (RMBS, $9.3bn, +0.76%)** · Noble Corporation · Brixmor · Alexandria Real Estate · PriceSmart · Phillips Edison · Dorman Products.

Two names to watch from this list. **CDNS** is a direct read on the AI-chip design cycle that the semi complex is trading on. **CLS** is up +3.68% pre-market after −3.35% Friday, and it is a direct AI-datacenter-hardware supplier — if the memory/AI-hardware bid is real rather than a bounce, CLS's print is the cleanest single-name confirmation available tonight.

Separately and already scheduled: **EQT and Range Resources** both report Q3 after the close on Tuesday 27 October (their 28 October calls were cancelled for the merger), and **Verizon** reports pre-market this morning.

---

## 10. Source health

| Source | Role | Status | Notes |
|---|---|---|---|
| `scanner.tradingview.com/america/scan` | US universe, pre-market breadth, sectors, futures, crypto | ✅ OK | 5,715 US equities (OTC excluded), 2,603 with pre-market prints. Used for candidate discovery only — its pre-market values lag CNBC by 5–15 min and its `volume` field is unreliable (MELI 383k vs 12M+ actual). Futures flagged `delayed_streaming_600` (10 min). |
| CNBC quote API | Every published price, % and volume; index levels; futures; ETFs | ✅ OK | Live pre-market prints, timestamped 08:41–08:52 ET. Cash indices carry Friday's close (correct — cash is closed). `.US10Y` symbol absent; `@RT.1` absent (Russell futures taken from TradingView instead). |
| `api.nasdaq.com` | Cross-check of pre-market prints, Friday-session movers, earnings calendar | ✅ OK | Live, `isRealTime: true`. Used to confirm CNBC on 26 names: median divergence **0.38pp**, 23 of 26 within 1pp, worst case 2.25pp on XNCR — every divergence explained by print timestamp (Nasdaq 08:33–08:41 ET vs CNBC 08:39–08:52 ET). |
| `api.exchange.coinbase.com` | BTC/ETH/SOL spot and 24h stats | ✅ OK | Live, timestamped 12:51 UTC. |
| `api.stocktwits.com/api/2/streams/trending.json` | Social lead read | ⚠️ DEGRADED | Live (200, 30 messages, 12:29–12:32 UTC) but carries **no** thesis text and no trending score — ranked by mention count instead. Embedded prices track but do not match the live tape (CRWV $52.93 vs $52.29 live, MRNA $183.85 vs $185.80, SPY $762.88 vs $762.25) and were not used. The retired `trending-symbols.json` endpoint 404s. |
| `web_search` | Catalysts, macro calendar, earnings | ✅ OK | Separate egress path; worked throughout. |
| `query1/query2.finance.yahoo.com` | **Primary source** — screener, chart, spark, quote | ❌ UNAVAILABLE | Hard HTTP 429 on every endpoint from 12:40Z; 6 retries with backoff plus a 30-minute background patient-retry loop never cleared. `/v7/finance/quote` additionally 401 (no crumb/cookie). Replaced as described in *Deviations*. |
| `stooq.com` | Index close cross-check | ❌ UNAVAILABLE | Returned empty bodies for every symbol tested. Not needed once CNBC/Nasdaq index quotes worked. |
| `openssl` leaf-cert check | TLS transport | ✅ OK | Leaf valid 2026-09-29 → 2026-11-18. All fetches ran on **verified TLS** (`--cacert /etc/ssl/certs/agent-identity/sandbox-gateway-ca.crt`); no `-k` was used anywhere. |
| MCP tools (`mcp__yahoo_finance__*`, `mcp__tradingview*`, `mcp__stocktwits__*`) | — | ❌ NOT BOUND | None are registered in this Cloud runtime, as the cron prompt anticipated. All equivalents were called at source over HTTPS. |
| `research/watchlist.yaml` | Watchlist section | ❌ MISSING | File does not exist in the sandbox; no watchlist section produced, per skill rule. |

**Count of source tiers that failed and forced a fallback: 3** (Yahoo predefined screener; Yahoo chart/spark; Stooq index CSV).

**Body-level verification:** every JSON response was parsed before use, not just status-checked, because the sandbox proxy can return HTTP 200 with a plain-text error page. The Yahoo 429s arrived as 19-byte bodies reading `Too Many Requests`, which is why they were not mistaken for valid payloads.

---

## 11. Open research queue

1. **Yahoo Finance availability is the standing infrastructure risk.** It was the designated primary source for this skill and is now hard-blocked from this egress IP. Until it recovers, every run depends on TradingView breadth plus CNBC/Nasdaq verification — workable, but it costs roughly 4× the API calls and leaves no `chartPreviousClose`-grade depth. Worth a decision on whether to swap the skill's primary tier to the CNBC quote API permanently, which also removes the crumb/cookie fragility.
2. **Confirm whether the Brazil repricing is contained or contagious.** The open question at 08:52 ET is whether EWZ's 29.8M-share pre-market volume finds a bid by 10:00. Watch US financial ETFs (KRE +0.26% pre-market, XLF +0.04%) and the small-cap complex (IWM +0.04%, RTY futures +0.10%) — both are currently pricing zero contagion, which is the fragile assumption.
3. **Quantify the oil round-trip.** WTI at $101.13 after a $110+ print changes the Fed's inflation path more than the headline suggests. Watch whether the pre-market pullback holds through the 09:30 open, and whether the JETS +2.30% move confirms it.
4. **Test the semis bid against tonight's reports.** CDNS and CLS both report after the close; MU reports Wednesday. If CLS's print validates the pre-market bid, Cluster B is a fundamental bid rather than a short-covering bounce. Morgan Stanley's 10–15% extension call is the bear case to falsify.
5. **Re-rate the Brazil complex once fiscal specifics land.** The market is trading an election outcome, not a policy path. There is no scheduled catalyst in the cluster (XP's Q3 is the week of 16 November), so the repricing has no natural closing mechanism — watch for fiscal-team announcements and any read-through to PBR's oil revenue assumptions.

---

*Generated by Cloud Mavis cron #26 (`agentic-pre-market-brief`) · skill spec fetched 2026-10-26 08:33 ET from `raw.githubusercontent.com/karizaco/maxhermes-migration` · all timestamps ET unless stated · read-only, no trading advice.*
