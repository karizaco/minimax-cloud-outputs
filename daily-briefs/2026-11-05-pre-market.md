---
date: 2026-11-05
cron: 26-agentic-pre-market-brief
artifact_contract: premarket-brief-artifact-v2
fire_time_et: 2026-11-05 08:30
reconstructed_at_et: 2026-11-06 05:55
screen_pull_et: 2026-11-05 10:10
source: TradingView america scanner (cron #26b's published 2026-11-05 screen) + Yahoo chart API
status: ok
themes: 5
up_3pct: 200
down_3pct: 383
csv: daily-briefs/2026-11-05-pre-market.csv
---

# Pre-market brief — Thursday 2026-11-05

**This artifact is a reconstruction.** The 2026-11-05 08:30 ET fire of cron #26 failed on the platform (Token Plan quota) and published nothing. The window check resolved this session's scheduled instant to 2026-11-05 08:30:28 ET, so the brief below is rebuilt for **2026-11-05**, not for the day it was written. It is point-in-time: every number is what the tape carried before the 09:30 open on Nov 5. What the Nov 5 session actually did is cron #23's business (`daily-briefs/2026-11-05-post-market.md`).

The pre-market screen is the fleet's own published Nov 5 screen — cron #26b's 10:10:24 ET TradingView pull of the completed 04:00–09:30 ET pre-market session (`preopen-feed/2026-11-05-0830.jsonl`, `daily-briefs/2026-11-05-pre-market-refresh.md`). The pre-market high/low on every published name comes from Yahoo's Nov 5 pre-market bars, the prior close and the prior session's move from cron #20's settled EOD file, and the liquidity columns from the same TradingView pull. The machine-readable companion for every name in the screen — 708 rows — is `daily-briefs/2026-11-05-pre-market.csv`; the tables below are built from that same merged table, so the prose and the CSV cannot disagree.

## Bottom line

- **The one setup** — APP +28.79% pre-market at 350 against a prior close of 271.8: the record Q3 (revenue $2.185B vs $2.078B est, adj EPS $4.30 vs $4.04, Q4 guide $2.365-2.395B) is the only large-cap bid worth chasing into the open. It stays a setup while it holds above 350.25 — the pre-market high — and the gap is invalidated on a loss of 309, the pre-market low.
- **The one risk** — the AI complex is being repriced for political reasons, not earnings: AMD, QCOM, AVGO, ANET, NET and the memory names are all lower while SMH sits under its 200-day moving average for the first time since May 2025, and Asia has already closed sharply lower (Nikkei {nikkei_chg}, Kospi -5.3% per AP). That is a risk to every long, not a single-name gap.
- **The one thing to watch** — the 08:30 ET claims-and-productivity block (initial claims 197K consensus against 194K prior; Q3 unit labour costs -0.1% consensus against +1.2% prior) lands with the open, and Cleveland Fed president Beth Hammack speaks at roughly 08:50 ET — the hawk who dissented in favour of a hike on Oct 28.

## 1. TL;DR

The day has one spine: **the post-election repricing of the AI build-out, and a violent earnings night underneath it.** Democrats took both chambers on Nov 4, and the tape is trading what that means for data-centre capex. The names that need AI silicon are sold; the names that reported are split by their print.

- **AI, semis and memory: a political repricing, not an earnings one.** Leader **AMD -7.52%** — **QCOM -13.36%**, **AVGO -4.42%**, **ANET -5.87%**, **NET -5.87%**, **CAMT -4.88%**, **MU -5.37%**, **SNDK -7.17%**, **WDC -6.14%**, **STX -6.54%**, **LITE -5.20%**, **MRVL -5.31%**, **INTC -3.11%**. Q3 (Nov 3) was a record — revenue $13.377B (+45% y/y), Data Center $8.546B (+97%), non-GAAP EPS $2.09, Q4 guide ~$17B, 2027 growth >80% — and the stock is being marked down on post-election data-centre politics, not the print.
- **AppLovin's record quarter, and the earnings-beat cohort it led.** Leader **APP +28.79%** — **SEZL +26.32%**, **LYNX +22.47%**, **U +13.17%**, **WRBY +20.95%**, **TPR +13.32%**, **EPAM +13.72%**, **RPD +13.03%**, **SABR +13.22%**, **PTON +9.16%**, **ALNT +12.27%**, **VCEL +10.53%**, **ULCC +8.04%**. Record Q3: revenue $2.185B (+55% y/y) vs $2.078B est, net income $1.439B (+72%), diluted EPS $4.30 vs $4.04, adj EBITDA $1.842B vs $1.732B, FCF $1.4B, Q4 revenue guide $2.365-2.395B vs $2.251B est, buyback raised by $3.2B.
- **The earnings cohort gets marked down.** Leader **MNTN -50.82%** — **TRIP -21.18%**, **FOUR -11.76%**, **BROS -14.64%**, **DAVE -12.37%**, **SNAP -10.64%**, **LMAT -6.73%**, **EXPE -9.78%**, **CAVA -8.91%**, **ZG -8.51%**, **MELI -7.98%**, **FICO -7.29%**, **HUBS +3.21%**. Cut its 2026 revenue forecast to $311-314M citing problems in its sales team, and named a new chief executive.
- **Small-cap and structural prints at the low end.** Leader **AEHL +103.67%** — **AMTX +38.40%**, **TBI +34.96%**, **ARQ +34.61%**, **ELPW +39.04%**, **LABT +101.15%**, **ZNB +91.32%**, **FLYE +59.99%**. No catalyst captured at the Nov 5 checkpoint; the print sits on 4,047,023 pre-market shares (401.2% of ADV).
- **Health-tech and single-name dispersion.** Leader **VCYT -44.00%** — **XERS +19.50%**, **IRWD +14.85%**, **ADMA +14.60%**, **RUN +19.34%**, **GROY +16.61%**, **FUN +16.02%**, **BKSY +15.44%**, **AKBA -26.62%**, **KPTI -27.30%**, **ANVS -28.10%**, **ROCK -26.55%**, **GIL -25.51%**, **LZ -24.71%**, **DDD -21.59%**, **TDUP -20.09%**, **PENG -6.93%**, **PH +5.47%**. Beat Q3 (adj EPS $0.51 vs $0.41 est, revenue $151.754M vs $147.439M est) but Decipher Prostate volume missed internal expectations; FY26 revenue guided to $590-593M from $590-596M, below the $593.894M Street number.

- **The watchlist is quiet.** AAPL +1.26%; MSFT -0.28%; NVDA -2.05%; GOOGL +1.51%; AMZN +2.07%; IWM +0.06% pre-market — none of the six names sits in the day's themes, and the file that carries the list was seeded after this fire (see §6).

## 2. Theme clusters

Levels on every published name: **prior close** is the 2026-11-04 settled close, **pre-market last** is the final pre-market print, **PM range** is the 04:00–09:30 ET pre-market low/high, **key level** is the extreme that has to break for the gap to extend (the high on a gap up, the low on a gap down) and **invalidation** is the opposite extreme — the level at which the pre-market order failed.
Market cap is on the **2026-11-04 close basis** throughout — the basis the fleet's screen publishes, because the screen was pulled before the Nov 5 close. MELI is absent from cron #20's settled file on both Nov 4 and Nov 5, so its cap is not published rather than guessed.

### C1 — AI, semis and memory: a political repricing, not an earnings one

Leader: **AMD** — a record quarter on Nov 3, marked down on post-election data-centre politics.

| Ticker | Name | Prior close | Pre-market last | PM range | Gap % | %ADV | Mkt cap | Key level | Invalidation | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|
| AMD | Advanced Micro Devices, Inc. | 488.8 | 452.02 | 450.1–478.69 | -7.52% | n/p | $699.34B | 450.1 | 478.69 | Q3 (Nov 3) was a record — revenue $13.377B (+45% y/y), Data Center $8.546B (+97%), non-GAAP EPS $2.09, Q4 guide ~$17B, 2027 growth >80% — and the stock is being marked down on post-election data-centre politics, not the print. |
| QCOM | QUALCOMM Incorporated | 173.2 | 150.06 | 150.06–158.59 | -13.36% | n/p | $167.16B | 150.06 | 158.59 | FQ4 revenue $10.442B (-7% y/y), non-GAAP EPS $2.17 (-28% y/y), handset revenue $5.137B (-26% y/y); the memory/AI complex sold with it. |
| AVGO | Broadcom Inc. | 325.5 | 311.1 | 311.1–321.1 | -4.42% | n/p | $1.48T | 311.1 | 321.1 | Caught in the AI-capex repricing after Qualcomm's handset quarter and a memory-led selloff. |
| ANET | Arista Networks Inc | 178.5 | 168 | 170.28–178.48 | -5.87% | n/p | $207.53B | 170.28 | 178.48 | AI-networking sympathy with the data-centre complex. |
| NET | Cloudflare Inc Class A | 266.8 | 250.94 | 254.61–266.58 | -5.87% | n/p | $86.05B | 254.61 | 266.58 | Cloudflare reported the prior evening; the name traded with the AI-capex complex. |
| CAMT | Camtek Ltd | 101.46 | 96.51 | 96.51–100.22 | -4.88% | n/p | $4.39B | 96.51 | 100.22 | Semiconductor capital-equipment sympathy with the same tape. |
| MU | Micron Technology, Inc. | 795.2 | 752.54 | 748.74–780.74 | -5.37% | n/p | $898.13B | 748.74 | 780.74 | Micron suspended plans for a $4.5B Taiwan memory plant over an extended labor dispute; SK Hynix and SanDisk fell over 5% overnight. |
| SNDK | Sandisk Corporation | 1037 | 963 | 953.2–1017.77 | -7.17% | n/p | $151.90B | 953.2 | 1017.77 | Memory selloff — SK Hynix and SanDisk both fell over 5% overnight on data-centre regulatory fears. |
| WDC | Western Digital Corporation | 323.8 | 303.96 | 303–316 | -6.14% | n/p | $116.75B | 303 | 316 | Memory and storage sympathy with SanDisk. |
| STX | Seagate Technology Holdings PLC | 557.1 | 520.65 | 520–542.51 | -6.54% | n/p | $126.25B | 520 | 542.51 | Storage hardware sympathy with the memory complex. |
| LITE | Lumentum Holdings, Inc. | 626.8 | 594.16 | 592.77–615.89 | -5.20% | n/p | $48.76B | 592.77 | 615.89 | Optical/AI-hardware sympathy with the data-centre complex. |
| MRVL | Marvell Technology, Inc. | 159.8 | 151.32 | 150–156.7 | -5.31% | n/p | $139.79B | 150 | 156.7 | Custom-silicon names repriced with the AI-capex complex. |
| INTC | Intel Corporation | 58.27 | 56.46 | 55.91–57.61 | -3.11% | n/p | $293.91B | 55.91 | 57.61 | Broadened out of the semiconductor selloff. |

Sources: https://247wallst.com/investing/2026/11/05/amd-tumbles-13-nvidia-slides-7-as-ai-regulation-fears-hit-chip-stocks-intel-sinks-8/ · https://www.tradingkey.com/analysis/stocks/us-stocks/262282182-memory-stocks-slide-sk-hynix-sandisk-5-qualcomm-9-applovin-20-tradingkey · https://investrade.com/morning-preview-november-05-2026/ · https://www.stocktitan.net/articles/stock-market-today-live-november-5-2026

### C2 — AppLovin's record quarter, and the earnings-beat cohort it led

Leader: **APP** — a record Q3 and a Q4 guide above consensus.

| Ticker | Name | Prior close | Pre-market last | PM range | Gap % | %ADV | Mkt cap | Key level | Invalidation | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|
| APP | AppLovin Corp. Class A | 271.8 | 350 | 309–350.25 | +28.79% | 21.78 | $120.33B | 350.25 | 309 | Record Q3: revenue $2.185B (+55% y/y) vs $2.078B est, net income $1.439B (+72%), diluted EPS $4.30 vs $4.04, adj EBITDA $1.842B vs $1.732B, FCF $1.4B, Q4 revenue guide $2.365-2.395B vs $2.251B est, buyback raised by $3.2B. |
| SEZL | Sezzle Inc. | 136.7 | 172.66 | 170.01–179.9 | +26.32% | 8.71 | $5.61B | 179.9 | 170.01 | Q3 beat reported Nov 4 after the close: adj EPS $1.37 vs $1.29 est, revenue $166.5M vs $154.9M est, FY26 revenue-growth guide ~42.5%, FY27 adj EPS guide $7.20 vs $6.65 est. |
| LYNX | Lyntris Inc | 9.4 | 11.5 | 11.11–12.1 | +22.47% | 4.9 | $1.32B | 12.1 | 11.11 | Q3 FY2026 reported Nov 4 at 16:15 ET: EPS $0.15 vs $0.08 est, revenue $194.4M (+90.4% y/y), backlog more than doubled; Baird upgraded to Outperform with an $18 target on Nov 5. |
| U | Unity Software, Inc. | 42.47 | 48.05 | 40.68–54.35 | +13.17% | n/p | $18.54B | 54.35 | 40.68 | Unity's Q3 beat; the ad-tech complex followed AppLovin higher. |
| WRBY | Warby Parker, Inc. Class A | 21.27 | 25.75 | 21.55–26.2 | +20.95% | 10.59 | $3.14B | 26.2 | 21.55 | Q3 results beat. |
| TPR | Tapestry, Inc. | 125.3 | 142 | 127–146.04 | +13.32% | n/p | $25.31B | 146.04 | 127 | Tapestry moved on the earnings/sector tape. |
| EPAM | EPAM Systems, Inc. | 137.4 | 156.2 | 132.48–172 | +13.72% | n/p | $7.18B | 172 | 132.48 | EPAM Systems moved on the earnings/sector tape. |
| RPD | Rapid7 Inc. | 15.04 | 17 | 16.23–17.4463 | +13.03% | n/p | $1.01B | 17.4463 | 16.23 | Rapid7 named in the pre-market earnings-mover list. |
| SABR | Sabre Corporation | 1.74 | 1.97 | 1.77–1.97 | +13.22% | n/p | $687.85M | 1.97 | 1.77 | Sabre named in the pre-market earnings-mover list. |
| PTON | Peloton Interactive, Inc. Class A | 5.46 | 5.96 | 5.47–6.06 | +9.16% | n/p | $2.28B | 6.06 | 5.47 | Peloton named in the pre-market earnings-mover list. |
| ALNT | Allient Inc. | 79.56 | 89.32 | 89.32–92.88 | +12.27% | n/p | $1.35B | 92.88 | 89.32 | Alent named in the pre-market earnings-mover list. |
| VCEL | Vericel Corporation | 45.48 | 50.27 | 47–48.99 | +10.53% | n/p | $2.79B | 48.99 | 47 | Vera Therapeutics moved on the earnings/sector tape. |
| ULCC | Frontier Group Holdings, Inc. | 7.09 | 7.66 | 7.29–7.66 | +8.04% | n/p | $1.63B | 7.66 | 7.29 | Ultragenyx named in the earnings-mover list. |

Sources: https://www.investopedia.com/5-things-investors-need-to-know-about-thursday-s-markets-12237605 · https://markets.businessinsider.com/news/stocks/morning-movers-applovin-surges-following-third-quarter-results-1036724997 · https://www.tradingkey.com/analysis/stocks/us-stocks/262282182-memory-stocks-slide-sk-hynix-sandisk-5-qualcomm-9-applovin-20-tradingkey · earnings/2026-11-05-reactions.md (cron #15)

### C3 — The earnings cohort gets marked down

Leader: **MNTN** — a 2026 revenue forecast cut to $311-314M on sales-team problems.

| Ticker | Name | Prior close | Pre-market last | PM range | Gap % | %ADV | Mkt cap | Key level | Invalidation | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|
| MNTN | MNTN, Inc Class A | 10.39 | 5.1 | 5.39–6.42 | -50.82% | 88.04 | $775.70M | 5.39 | 6.42 | Cut its 2026 revenue forecast to $311-314M citing problems in its sales team, and named a new chief executive. |
| TRIP | TripAdvisor, Inc. | 10.2 | 8.04 | 7.94–9.61 | -21.18% | 12.42 | $993.90M | 7.94 | 9.61 | Q3 2026 results posted pre-open on Nov 5 at 07:05 ET, with the call at 08:30 ET. |
| FOUR | Shift4 Payments, Inc. Class A | 44.81 | 39.55 | 37–44.75 | -11.76% | n/p | $3.05B | 37 | 44.75 | Shift4 Q3 2026 results released before the open on Nov 5. |
| BROS | Dutch Bros, Inc. Class A | 43.92 | 37.55 | 36.23–39.45 | -14.64% | n/p | $7.67B | 36.23 | 39.45 | Dutch Bros' muted full-year forecast — 'at least $2.1B' against $2.13B expected. |
| DAVE | Dave, Inc. Class A | 336.2 | 294.62 | 295.5–310.51 | -12.37% | n/p | $4.27B | 295.5 | 310.51 | Named in the pre-market earnings-mover list as a downside name. |
| SNAP | Snap, Inc. Class A | 5.91 | 5.29 | 5.17–5.43 | -10.64% | n/p | $9.79B | 5.17 | 5.43 | Q3 revenue $1.722B (+14% y/y) came in slightly below expectations. |
| LMAT | LeMaitre Vascular, Inc. | 87.92 | 82 | 82–82 | -6.73% | n/p | $2.01B | 82 | 82 | Named in the pre-market earnings-mover list as a downside name. |
| EXPE | Expedia Group, Inc. | 315.9 | 285 | 283.26–304 | -9.78% | n/p | $33.26B | 283.26 | 304 | Named in the pre-market earnings-mover list as a downside name. |
| CAVA | CAVA Group, Inc. | 61.77 | 56.46 | 54.24–57.98 | -8.91% | n/p | $7.19B | 54.24 | 57.98 | Named in the pre-market earnings-mover list as a downside name. |
| ZG | Zillow Group, Inc. Class A | 34.45 | 31.52 | 28.34–31.88 | -8.51% | n/p | $6.99B | 28.34 | 31.88 | Named in the pre-market earnings-mover list as a downside name. |
| MELI | MercadoLibre, Inc. | 1739.88 | 1601 | 1570–1648 | -7.98% | n/p | n/p | 1570 | 1648 | Named in the pre-market earnings-mover list as a downside name. |
| FICO | Fair Isaac Corporation | 703.1 | 649.9 | 620–701.03 | -7.29% | n/p | $16.31B | 620 | 701.03 | Named in the pre-market earnings-mover list as a downside name. |
| HUBS | HubSpot, Inc. | 216 | 223.59 | 191–209 | +3.21% | n/p | $11.06B | 209 | 191 | Named in the pre-market earnings-mover list as an upside name. |

Sources: https://investrade.com/morning-preview-november-05-2026/ · https://www.investopedia.com/5-things-investors-need-to-know-about-thursday-s-markets-12237605 · https://www.stocktitan.net/articles/stock-market-today-live-november-5-2026 · earnings/2026-11-05-reactions.md (cron #15)

### C4 — Small-cap and structural prints at the low end

Leader: **AEHL** — no catalyst captured at the checkpoint, on a 4.05M-share pre-market print.

| Ticker | Name | Prior close | Pre-market last | PM range | Gap % | %ADV | Mkt cap | Key level | Invalidation | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|
| AEHL | Antelope Enterprise Holdings Limited Class A | 6.27 | 12.77 | 8.88–13.48 | +103.67% | 401.2 | $200.90M | 13.48 | 8.88 | No catalyst captured at the Nov 5 checkpoint; the print sits on 4,047,023 pre-market shares (401.2% of ADV). |
| AMTX | Aemetis, Inc. | 1.25 | 1.73 | 1.28–1.78 | +38.40% | 82.33 | $134.20M | 1.78 | 1.28 | Q3 results reported. |
| TBI | TrueBlue, Inc. | 9.75 | 13.28 | 12.2–13.2774 | +34.96% | 49.54 | $376.00M | 13.2774 | 12.2 | TrueBlue moved on the earnings/sector tape. |
| ARQ | Arq, Inc. | 1.85 | 2.4903 | 2.21–2.69 | +34.61% | 701.32 | $107.90M | 2.69 | 2.21 | Q3 results beat, with strong pre-market volume. |
| ELPW | Elong Power Holding Limited Class A | 2.51 | 3.49 | 2.73–4.84 | +39.04% | 906.97 | $3.60M | 4.84 | 2.73 | Announced a $300M energy-storage cooperation agreement. |
| LABT | Lakewood-Amedex Biotherapeutics Inc. | 0.1914 | 0.385 | 0.18–0.4428 | +101.15% | 1119.02 | $453.60K | 0.4428 | 0.18 | No catalyst captured at the Nov 5 checkpoint — the move is a print with 149.2M pre-market shares (1119% of ADV). |
| ZNB | Zeta Network Group Class A | 0.622 | 1.19 | 0.9665–1.8298 | +91.32% | 1133.07 | $5.60M | 1.8298 | 0.9665 | No catalyst captured at the Nov 5 checkpoint. |
| FLYE | Fly-E Group, Inc. | 1.72 | 2.72 | 1.8182–3.36 | +59.99% | 178.54 | $3.80M | 3.36 | 1.8182 | No catalyst captured at the Nov 5 checkpoint. |

Sources: https://marketchameleon.com/Reports/PremarketTrading · preopen-feed/2026-11-05-0830.jsonl (cron #92a)

### C5 — Health-tech and single-name dispersion

Leader: **VCYT** — a Decipher volume miss and an FY26 revenue guide cut.

| Ticker | Name | Prior close | Pre-market last | PM range | Gap % | %ADV | Mkt cap | Key level | Invalidation | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|
| VCYT | Veracyte, Inc. | 52.52 | 29.41 | 29.34–39 | -44.00% | 14.82 | $4.22B | 29.34 | 39 | Beat Q3 (adj EPS $0.51 vs $0.41 est, revenue $151.754M vs $147.439M est) but Decipher Prostate volume missed internal expectations; FY26 revenue guided to $590-593M from $590-596M, below the $593.894M Street number. |
| XERS | Xeris Biopharma Holdings, Inc. | 10.46 | 12.5 | 10.55–12.56 | +19.50% | 5.58 | $2.46B | 12.56 | 10.55 | Q3 results beat. |
| IRWD | Ironwood Pharmaceuticals, Inc. Class A | 3.77 | 4.33 | 4.0498–4.34 | +14.85% | 11.72 | $686.60M | 4.34 | 4.0498 | Ironwood Pharmaceuticals moved on the earnings/sector tape. |
| ADMA | ADMA Biologics, Inc. | 10.48 | 12.01 | 11.8673–13.86 | +14.60% | 6.77 | $2.80B | 13.86 | 11.8673 | ADMA Biologics moved on the earnings/sector tape. |
| RUN | Sunrun Inc. | 8.79 | 10.49 | 9.71–11.0868 | +19.34% | 27.76 | $2.33B | 11.0868 | 9.71 | Sunrun moved on the earnings/sector tape. |
| GROY | Gold Royalty Corp. | 2.89 | 3.37 | 2.98–3.22 | +16.61% | 17.63 | $732.10M | 3.22 | 2.98 | Gold Royalty bid with the gold complex. |
| FUN | Six Flags Entertainment Corporation | 7.95 | 9.2 | 7.8423–9.5 | +16.02% | 22.01 | $983.30M | 9.5 | 7.8423 | Six Flags moved on the earnings/sector tape. |
| BKSY | BlackSky Technology Inc Class A | 16.78 | 19.36 | 16.76–21.1061 | +15.44% | 9.03 | $764.70M | 21.1061 | 16.76 | BlackSky moved on the earnings/sector tape. |
| AKBA | Akebia Therapeutics, Inc. | 0.6947 | 0.5098 | 0.4798–0.7355 | -26.62% | 8.8 | $131.70M | 0.4798 | 0.7355 | Revenue miss. |
| KPTI | Karyopharm Therapeutics, Inc. | 0.0729 | 0.053 | 0.0448–0.0857 | -27.30% | 70.61 | $1.30M | 0.0448 | 0.0857 | No catalyst captured at the Nov 5 checkpoint. |
| ANVS | Annovis Bio Inc | 1.2 | 0.87 | 0.82–0.9765 | -28.10% | 20.01 | $30.30M | 0.82 | 0.9765 | Public offering pricing announced. |
| ROCK | Gibraltar Industries, Inc. | 43.58 | 32.01 | 32–36.69 | -26.55% | 4.84 | $1.07B | 32 | 36.69 | Lowered its 2026 forecast on weaker-than-expected Q3 and a lower Q4 outlook; its CFO is leaving on Nov 20. |
| GIL | Gildan Activewear Inc. | 43.27 | 32.23 | 32.4–40 | -25.51% | 13.95 | $6.07B | 32.4 | 40 | Catalyst not sourced in this run. |
| LZ | LegalZoom.com, Inc. | 6.9 | 5.195 | 5.14–5.86 | -24.71% | 1.6 | $1.01B | 5.14 | 5.86 | Catalyst not sourced in this run. |
| DDD | 3D Systems Corporation | 2.635 | 2.07 | 2–2.65 | -21.59% | 17.19 | $304.90M | 2 | 2.65 | Entered a $42.5M at-the-market offering with Cantor Fitzgerald on Nov 5 after a mixed Q3 (revenue +8.8% to $99.3M, adj EBITDA +$3.1M, net loss $33.5M). |
| TDUP | thredUP, Inc. Class A | 2.19 | 1.75 | 1.6–1.76 | -20.09% | 9.06 | $207.50M | 1.6 | 1.76 | Catalyst not sourced in this run. |
| PENG | Penguin Solutions Incorporation | 48.35 | 45 | 45.27–47.9 | -6.93% | n/p | $2.48B | 45.27 | 47.9 | Catalyst not sourced in this run. |
| PH | Parker-Hannifin Corporation | 909.5 | 960 | 910.19–985.55 | +5.47% | n/p | $118.84B | 985.55 | 910.19 | Parker-Hannifin moved on the earnings/sector tape. |

Sources: https://www.benzinga.com/markets/earnings/26/11/62933735/why-is-veracyte-stock-sinking-thursday · https://hdfcsky.com/news/3d-systems-plunges-35-48percent-on-42-5m-offering-akebia-drops-34-28percent-on-revenue-miss-precision-bioscience-surges-22-76percent · https://www.stocktitan.net/articles/stock-market-today-live-november-5-2026 · earnings/2026-11-05-reactions.md (cron #15)

## 3. Pre-market gaps — top 25 market-wide (23 gate-verified)

Gate A (liquidity) and Gate B (market cap >= $100M) applied as pinned. 23 names clear both gates on the gainer screen and 89 on the decliner screen; the top 23 gainers are below.

**Two liquidity proofs are in play, and both are published.** For the names the fleet's 2026-11-05 screen carried a pre-market volume for, the %ADV column is that print against the 30-day average. For the names where only cron #15's 08:22 ET screen is available (a 10,000-share pre-market floor) the gate is met on market cap >= $200M with that floor, and %ADV is shown as `n/p` — not estimated, not filled in.

| Ticker | Name | Prior close | Pre-market last | PM range | Gap % | %ADV | Mkt cap | Key level | Invalidation |
|---|---|---|---|---|---|---|---|---|---|
| AEHL | Antelope Enterprise Holdings Limited Class A | 6.27 | 12.77 | 8.88–13.48 | +103.67% | 401.2 | $200.90M | 13.48 | 8.88 |
| AMTX | Aemetis, Inc. | 1.25 | 1.73 | 1.28–1.78 | +38.40% | 82.33 | $134.20M | 1.78 | 1.28 |
| TBI | TrueBlue, Inc. | 9.75 | 13.28 | 12.2–13.2774 | +34.96% | 49.54 | $376.00M | 13.2774 | 12.2 |
| ARQ | Arq, Inc. | 1.85 | 2.4903 | 2.21–2.69 | +34.61% | 701.32 | $107.90M | 2.69 | 2.21 |
| APP | AppLovin Corp. Class A | 271.8 | 350 | 309–350.25 | +28.79% | 21.78 | $120.33B | 350.25 | 309 |
| SEZL | Sezzle Inc. | 136.7 | 172.66 | 170.01–179.9 | +26.32% | 8.71 | $5.61B | 179.9 | 170.01 |
| LYNX | Lyntris Inc | 9.4 | 11.5 | 11.11–12.1 | +22.47% | 4.9 | $1.32B | 12.1 | 11.11 |
| WRBY | Warby Parker, Inc. Class A | 21.27 | 25.75 | 21.55–26.2 | +20.95% | 10.59 | $3.14B | 26.2 | 21.55 |
| XERS | Xeris Biopharma Holdings, Inc. | 10.46 | 12.5 | 10.55–12.56 | +19.50% | 5.58 | $2.46B | 12.56 | 10.55 |
| RUN | Sunrun Inc. | 8.79 | 10.49 | 9.71–11.0868 | +19.34% | 27.76 | $2.33B | 11.0868 | 9.71 |
| GROY | Gold Royalty Corp. | 2.89 | 3.37 | 2.98–3.22 | +16.61% | 17.63 | $732.10M | 3.22 | 2.98 |
| FUN | Six Flags Entertainment Corporation | 7.95 | 9.2 | 7.8423–9.5 | +16.02% | 22.01 | $983.30M | 9.5 | 7.8423 |
| BKSY | BlackSky Technology Inc Class A | 16.78 | 19.36 | 16.76–21.1061 | +15.44% | 9.03 | $764.70M | 21.1061 | 16.76 |
| IRWD | Ironwood Pharmaceuticals, Inc. Class A | 3.77 | 4.33 | 4.0498–4.34 | +14.85% | 11.72 | $686.60M | 4.34 | 4.0498 |
| ADMA | ADMA Biologics, Inc. | 10.48 | 12.01 | 11.8673–13.86 | +14.60% | 6.77 | $2.80B | 13.86 | 11.8673 |
| ENOV | Enovis Corporation | 24.4 | 27.47 | 25.77–27.25 | +12.49% | n/p | $1.40B | 27.25 | 25.77 |
| ALNT | Allient Inc. | 79.56 | 89.32 | 89.32–92.88 | +12.27% | n/p | $1.35B | 92.88 | 89.32 |
| VCEL | Vericel Corporation | 45.48 | 50.27 | 47–48.99 | +10.53% | n/p | $2.79B | 48.99 | 47 |
| ULCC | Frontier Group Holdings, Inc. | 7.09 | 7.66 | 7.29–7.66 | +8.04% | n/p | $1.63B | 7.66 | 7.29 |
| TPL | Texas Pacific Land Corporation | 286.9 | 304.94 | 299.363–304 | +6.01% | n/p | $19.79B | 304 | 299.363 |
| PH | Parker-Hannifin Corporation | 909.5 | 960 | 910.19–985.55 | +5.47% | n/p | $118.84B | 985.55 | 910.19 |
| LIME | Neutron Holdings, Inc. | 18.39 | 19.1 | 18.79–19.6 | +3.86% | n/p | $1.18B | 19.6 | 18.79 |
| TREX | Trex Company, Inc. | 57.13 | 59 | 57.16–58.69 | +3.24% | n/p | $5.94B | 58.69 | 57.16 |

### Cleared the cap, but no published pre-market volume

**23 names and not 25, and here is why.** The names below clear Gate B — they are above $100M of market cap — but their pre-market volume is not published in any 2026-11-05 artifact, so Gate A cannot be verified and they cannot top a headline table. They are published here rather than hidden, and they sit in the CSV with `liquid_screen=not-verifiable`. Several of them gapped more than names in the table above, so read this block before reading the table above.

| Ticker | Name | Prior close | Pre-market last | PM range | Gap % | Mkt cap | Key level | Invalidation |
|---|---|---|---|---|---|---|---|---|
| WW | WW International, Inc. | 12.13 | 14.49 | 12.4-14.75 | +19.46% | $121.14M | 14.75 | 12.4 |
| ACHC | Acadia Healthcare Company, Inc. | 32.25 | 37.49 | 33.5-37.25 | +16.25% | $2.97B | 37.25 | 33.5 |
| EWTX | Edgewise Therapeutics, Inc. | 37.53 | 43 | 40.85-43.55 | +14.58% | $4.04B | 43.55 | 40.85 |
| VERX | Vertex, Inc. Class A | 15.92 | 18.2 | 17.96-18.7 | +14.32% | $2.58B | 18.7 | 17.96 |
| JOBY | Joby Aviation, Inc. | 5.05 | 5.77 | 5.24-5.86 | +14.26% | $4.97B | 5.86 | 5.24 |
| EPAM | EPAM Systems, Inc. | 137.4 | 156.2 | 132.48-172 | +13.72% | $7.18B | 172 | 132.48 |
| MGNI | Magnite, Inc. | 22.79 | 25.89 | 24.4-26 | +13.60% | $3.26B | 26 | 24.4 |
| TPR | Tapestry, Inc. | 125.3 | 142 | 127-146.04 | +13.32% | $25.31B | 146.04 | 127 |
| SABR | Sabre Corporation | 1.74 | 1.97 | 1.77-1.97 | +13.22% | $687.85M | 1.97 | 1.77 |
| U | Unity Software, Inc. | 42.47 | 48.05 | 40.68-54.35 | +13.17% | $18.54B | 54.35 | 40.68 |

### Thin tape — cleared Gate A, below the $100M cap (17 gainers, 31 decliners)

Real moves on sub-$100M caps. They never top a headline table, but they carry the largest gaps on the board, so they are published here rather than hidden.

| Ticker | Name | Prior close | Pre-market last | PM range | Gap % | %ADV | Mkt cap | Key level | Invalidation |
|---|---|---|---|---|---|---|---|---|---|
| LABT | Lakewood-Amedex Biotherapeutics Inc. | 0.1914 | 0.385 | 0.18–0.4428 | +101.15% | 1119.02 | $453.60K | 0.4428 | 0.18 |
| ZNB | Zeta Network Group Class A | 0.622 | 1.19 | 0.9665–1.8298 | +91.32% | 1133.07 | $5.60M | 1.8298 | 0.9665 |
| FLYE | Fly-E Group, Inc. | 1.72 | 2.72 | 1.8182–3.36 | +59.99% | 178.54 | $3.80M | 3.36 | 1.8182 |
| ELPW | Elong Power Holding Limited Class A | 2.51 | 3.49 | 2.73–4.84 | +39.04% | 906.97 | $3.60M | 4.84 | 2.73 |
| SMX | SMX (Security Matters) Public Limited Company | 1.18 | 1.44 | 1.17–1.53 | +22.03% | 244.26 | $1.40M | 1.53 | 1.17 |
| JDZG | Jiade Limited Class A | 0.3016 | 0.3527 | 0.35–0.6391 | +16.94% | 1314.72 | $1.90M | 0.6391 | 0.35 |
| CCLD | CareCloud, Inc. | 1.8 | 2.09 | 1.9–2.2 | +16.11% | 133.24 | $93.60M | 2.2 | 1.9 |
| MTEK | Maris-Tech Ltd. | 0.26 | 0.297 | 0.277–0.35 | +14.23% | 24.61 | $3.20M | 0.35 | 0.277 |
| VRAX | Virax Biolabs Group Ltd. Class A | 1.2 | 1.33 | 1.2207–1.55 | +10.83% | 287.36 | $1.60M | 1.55 | 1.2207 |
| HIHO | Highway Holdings Limited | 0.84 | 0.9249 | 0.829–0.9663 | +10.11% | 758.56 | $4.10M | 0.9663 | 0.829 |
| PLCE | Children's Place, Inc. | 0.241 | 0.265 | 0.24–0.3668 | +9.96% | 637.06 | $7.30M | 0.3668 | 0.24 |
| NUR | Nuran Wireless Inc | 0.5015 | 0.55 | 0.5–0.55 | +9.67% | 20.48 | $6.30M | 0.55 | 0.5 |
| SPWR | SunPower Inc. | 0.242 | 0.2594 | 0.2446–0.2622 | +7.19% | 13.9 | $75.20M | 0.2622 | 0.2446 |
| BLNK | Blink Charging Co | 0.4514 | 0.478 | 0.4666–0.495 | +5.89% | 12.79 | $63.40M | 0.495 | 0.4666 |
| MOBX | Mobix Labs, Inc. | 0.5945 | 0.6369 | 0.59–0.65 | +4.43% | 4.47 | $13.80M | 0.65 | 0.59 |
| OMH | Ohmyhome Limited Class A | 15.55 | 16.2 | 11.05–18.3 | +4.18% | 70.2 | $31.20M | 18.3 | 11.05 |
| SLQT | SelectQuote Inc | 0.4851 | 0.51 | 0.4799–0.5179 | +3.79% | 25.97 | $81.50M | 0.5179 | 0.4799 |
| PARA | Parabolic Technologies, Inc. Class A | 0.319 | 0.218 | 0.2004–0.2799 | -31.66% | 66.39 | $121.40K | 0.2004 | 0.2799 |
| NWGL | CL Workshop Group Limited | 0.0555 | 0.039 | n/p | -29.73% | 17.51 | $3.10M | 0.0555 | 0.0555 |
| TEAD | Teads Holding Co. | 0.2753 | 0.195 | 0.1899–0.325 | -29.17% | 16.44 | $17.60M | 0.1899 | 0.325 |
| ANVS | Annovis Bio Inc | 1.2 | 0.87 | 0.82–0.9765 | -28.10% | 20.01 | $30.30M | 0.82 | 0.9765 |
| KPTI | Karyopharm Therapeutics, Inc. | 0.0729 | 0.053 | 0.0448–0.0857 | -27.30% | 70.61 | $1.30M | 0.0448 | 0.0857 |
| BZFD | BuzzFeed, Inc. Class A | 0.9207 | 0.6902 | 0.61–0.8514 | -25.04% | 311.44 | $51.70M | 0.61 | 0.8514 |
| ADGM | Adagio Medical Holdings, Inc | 0.0862 | 0.0695 | 0.069–0.084 | -19.37% | 10.96 | $1.80M | 0.069 | 0.084 |
| ARAY | Accuray Incorporated | 0.1491 | 0.1236 | 0.1126–0.1266 | -17.10% | 2.28 | $14.20M | 0.1126 | 0.1266 |
| HUBC | Hub Cyber Security Ltd. | 0.095 | 0.0789 | 0.0788–0.0904 | -16.95% | 6.88 | $136.50K | 0.0788 | 0.0904 |
| PMAX | Powell Max Limited Class A | 1.04 | 0.87 | 0.7751–0.9801 | -16.35% | 20.34 | $1.60M | 0.7751 | 0.9801 |
| CENN | Cenntro Inc. | 0.177 | 0.1486 | 0.1347–0.1586 | -16.05% | 28.97 | $2.30M | 0.1347 | 0.1586 |
| OSTX | OS Therapies Incorporated | 1.16 | 0.97 | 0.8999–1.1907 | -15.65% | 47.14 | $39.50M | 0.8999 | 1.1907 |
| INLF | Inlif Limited Class A | 0.3072 | 0.2627 | 0.254–0.2917 | -14.49% | 3.22 | $370.30K | 0.254 | 0.2917 |
| SHFS | SHF Holdings Inc Class A | 0.0318 | 0.0272 | 0.0264–0.0318 | -14.31% | 27.67 | $2.50M | 0.0264 | 0.0318 |
| CDT | CDT Equity Inc. | 0.0509 | 0.0438 | 0.0425–0.0858 | -13.95% | 362.71 | $375.70K | 0.0425 | 0.0858 |
| CRIS | Curis, Inc. | 1.11 | 0.968 | 0.8059–1.18 | -12.79% | 56.58 | $7.30M | 0.8059 | 1.18 |
| DKI | DarkIris Inc. Class A | 2.08 | 1.82 | 1.68–2.0496 | -12.50% | 9.85 | $1.70M | 1.68 | 2.0496 |
| HPAI | Helport AI Limited | 0.33 | 0.291 | 0.2433–0.3099 | -11.82% | 27.94 | $12.00M | 0.2433 | 0.3099 |
| RCT | RedCloud Holdings plc | 0.0334 | 0.0299 | 0.0276–0.0307 | -10.48% | 10.68 | $2.30M | 0.0276 | 0.0307 |
| GXAI | Gaxos.ai Inc. | 0.447 | 0.4003 | 0.4033–0.4533 | -10.45% | 73.8 | $4.40M | 0.4033 | 0.4533 |
| FTCI | FTC Solar, Inc. | 1.38 | 1.241 | 1.12–1.2596 | -10.07% | 12.29 | $22.90M | 1.12 | 1.2596 |
| VIVK | Vivakor, Inc. | 0.4826 | 0.44 | 0.4385–0.4885 | -8.83% | 7.15 | $701.00K | 0.4385 | 0.4885 |
| JAGX | Jaguar Health, Inc. | 0.4988 | 0.46 | 0.4499–0.4909 | -7.78% | 6 | $1.00M | 0.4499 | 0.4909 |
| MASK | 3 E Network Technology Group Ltd. Class A | 1.64 | 1.53 | 1.5–2.1556 | -6.71% | 286.68 | $2.20M | 1.5 | 2.1556 |
| BDMD | Baird Medical Investment Holdings Ltd | 0.1091 | 0.1022 | 0.0935–0.1804 | -6.32% | 807.63 | $3.80M | 0.0935 | 0.1804 |
| YFOR | YYForce Limited Class A | 0.128 | 0.12 | 0.1164–0.1245 | -6.25% | 7.51 | $1.50M | 0.1164 | 0.1245 |
| WFF | WF Holding Limited | 1.32 | 1.2398 | 1.2398–1.3003 | -6.08% | 4.65 | $7.10M | 1.2398 | 1.3003 |
| SDEV | Stablecoin Development Corporation | 0.9629 | 0.9107 | 0.913–0.9883 | -5.82% | 0.88 | $65.30M | 0.913 | 0.9883 |
| BURU | Nuburu, Inc. | 0.2345 | 0.2265 | 0.2238–0.2404 | -4.83% | 1.46 | $2.80M | 0.2238 | 0.2404 |
| MERC | Mercer International Inc. | 0.25 | 0.2383 | 0.2277–0.2498 | -4.68% | 2.19 | $15.00M | 0.2277 | 0.2498 |
| GPUS | Hyperscale Data, Inc. | 0.1609 | 0.1544 | 0.1507–0.1641 | -4.40% | 4.6 | $28.50M | 0.1507 | 0.1641 |

### Yesterday's tape — 2026-11-04 session (prior session, not pre-market)

The prior session's own outsized movers, restricted to the names that are still in today's screen so that every row carries its levels. The session change is the 2026-11-04 regular session (cron #20's settled file); the pre-market columns are the 2026-11-05 pre-market.

| Ticker | Name | Prior close | Session change % | Pre-market last | PM range | Gap % | Key level | Invalidation | Mkt cap |
|---|---|---|---|---|---|---|---|---|---|
| PARA | Parabolic Technologies, Inc. Class A | 0.319 | -88.27% | 0.218 | 0.2004–0.2799 | -31.66% | 0.2004 | 0.2799 | $121.40K |
| CRIS | Curis, Inc. | 1.11 | +55.48% | 0.968 | 0.8059–1.18 | -12.79% | 0.8059 | 1.18 | $7.30M |
| CENN | Cenntro Inc. | 0.177 | -40.54% | 0.1486 | 0.1347–0.1586 | -16.05% | 0.1347 | 0.1586 | $2.30M |
| CNSY | Cerenome, Inc. | 0.8916 | -31.42% | 0.85 | 0.82–0.8902 | -4.67% | 0.82 | 0.8902 | $6.14M |
| ECG | Everus Construction Group, Inc. | 79.72 | -29.29% | 77.43 | 76.113–79.5 | -2.86% | 76.113 | 79.5 | $4.07B |
| LIME | Neutron Holdings, Inc. | 18.39 | -27.83% | 19.1 | 18.79–19.6 | +3.86% | 19.6 | 18.79 | $1.18B |
| VIVK | Vivakor, Inc. | 0.4826 | -27.45% | 0.44 | 0.4385–0.4885 | -8.83% | 0.4385 | 0.4885 | $701.00K |
| TSQ | Townsquare Media, Inc. Class A | 2.185 | -27.41% | 2.11 | 2.16–2.24 | -3.21% | 2.16 | 2.24 | $39.23M |

## 4. Top losers — top 10 market-wide

From the same screen, the decliner side, same two gates.

| Ticker | Name | Prior close | Pre-market last | PM range | Gap % | %ADV | Mkt cap | Key level | Invalidation |
|---|---|---|---|---|---|---|---|---|---|
| MNTN | MNTN, Inc Class A | 10.39 | 5.1 | 5.39–6.42 | -50.82% | 88.04 | $775.70M | 5.39 | 6.42 |
| VCYT | Veracyte, Inc. | 52.52 | 29.41 | 29.34–39 | -44.00% | 14.82 | $4.22B | 29.34 | 39 |
| AKBA | Akebia Therapeutics, Inc. | 0.6947 | 0.5098 | 0.4798–0.7355 | -26.62% | 8.8 | $131.70M | 0.4798 | 0.7355 |
| ROCK | Gibraltar Industries, Inc. | 43.58 | 32.01 | 32–36.69 | -26.55% | 4.84 | $1.07B | 32 | 36.69 |
| HIMX | Himax Technologies, Inc. | 10.4399 | 7.76 | n/p | -25.67% | 29.72 | $1.78B | 10.4399 | 10.4399 |
| GIL | Gildan Activewear Inc. | 43.27 | 32.23 | 32.4–40 | -25.51% | 13.95 | $6.07B | 32.4 | 40 |
| LZ | LegalZoom.com, Inc. | 6.9 | 5.195 | 5.14–5.86 | -24.71% | 1.6 | $1.01B | 5.14 | 5.86 |
| DDD | 3D Systems Corporation | 2.635 | 2.07 | 2–2.65 | -21.59% | 17.19 | $304.90M | 2 | 2.65 |
| TRIP | TripAdvisor, Inc. | 10.2 | 8.04 | 7.94–9.61 | -21.18% | 12.42 | $993.90M | 7.94 | 9.61 |
| TDUP | thredUP, Inc. Class A | 2.19 | 1.75 | 1.6–1.76 | -20.09% | 9.06 | $207.50M | 1.6 | 1.76 |

### Thin decliners — cleared Gate A, below the $100M cap (31)

| Ticker | Name | Prior close | Pre-market last | PM range | Gap % | %ADV | Mkt cap | Key level | Invalidation |
|---|---|---|---|---|---|---|---|---|---|
| PARA | Parabolic Technologies, Inc. Class A | 0.319 | 0.218 | 0.2004–0.2799 | -31.66% | 66.39 | $121.40K | 0.2004 | 0.2799 |
| NWGL | CL Workshop Group Limited | 0.0555 | 0.039 | n/p | -29.73% | 17.51 | $3.10M | 0.0555 | 0.0555 |
| TEAD | Teads Holding Co. | 0.2753 | 0.195 | 0.1899–0.325 | -29.17% | 16.44 | $17.60M | 0.1899 | 0.325 |
| ANVS | Annovis Bio Inc | 1.2 | 0.87 | 0.82–0.9765 | -28.10% | 20.01 | $30.30M | 0.82 | 0.9765 |
| KPTI | Karyopharm Therapeutics, Inc. | 0.0729 | 0.053 | 0.0448–0.0857 | -27.30% | 70.61 | $1.30M | 0.0448 | 0.0857 |
| BZFD | BuzzFeed, Inc. Class A | 0.9207 | 0.6902 | 0.61–0.8514 | -25.04% | 311.44 | $51.70M | 0.61 | 0.8514 |
| ADGM | Adagio Medical Holdings, Inc | 0.0862 | 0.0695 | 0.069–0.084 | -19.37% | 10.96 | $1.80M | 0.069 | 0.084 |
| ARAY | Accuray Incorporated | 0.1491 | 0.1236 | 0.1126–0.1266 | -17.10% | 2.28 | $14.20M | 0.1126 | 0.1266 |
| HUBC | Hub Cyber Security Ltd. | 0.095 | 0.0789 | 0.0788–0.0904 | -16.95% | 6.88 | $136.50K | 0.0788 | 0.0904 |
| PMAX | Powell Max Limited Class A | 1.04 | 0.87 | 0.7751–0.9801 | -16.35% | 20.34 | $1.60M | 0.7751 | 0.9801 |
| CENN | Cenntro Inc. | 0.177 | 0.1486 | 0.1347–0.1586 | -16.05% | 28.97 | $2.30M | 0.1347 | 0.1586 |
| OSTX | OS Therapies Incorporated | 1.16 | 0.97 | 0.8999–1.1907 | -15.65% | 47.14 | $39.50M | 0.8999 | 1.1907 |
| INLF | Inlif Limited Class A | 0.3072 | 0.2627 | 0.254–0.2917 | -14.49% | 3.22 | $370.30K | 0.254 | 0.2917 |
| SHFS | SHF Holdings Inc Class A | 0.0318 | 0.0272 | 0.0264–0.0318 | -14.31% | 27.67 | $2.50M | 0.0264 | 0.0318 |
| CDT | CDT Equity Inc. | 0.0509 | 0.0438 | 0.0425–0.0858 | -13.95% | 362.71 | $375.70K | 0.0425 | 0.0858 |
| CRIS | Curis, Inc. | 1.11 | 0.968 | 0.8059–1.18 | -12.79% | 56.58 | $7.30M | 0.8059 | 1.18 |
| DKI | DarkIris Inc. Class A | 2.08 | 1.82 | 1.68–2.0496 | -12.50% | 9.85 | $1.70M | 1.68 | 2.0496 |
| HPAI | Helport AI Limited | 0.33 | 0.291 | 0.2433–0.3099 | -11.82% | 27.94 | $12.00M | 0.2433 | 0.3099 |
| RCT | RedCloud Holdings plc | 0.0334 | 0.0299 | 0.0276–0.0307 | -10.48% | 10.68 | $2.30M | 0.0276 | 0.0307 |
| GXAI | Gaxos.ai Inc. | 0.447 | 0.4003 | 0.4033–0.4533 | -10.45% | 73.8 | $4.40M | 0.4033 | 0.4533 |
| FTCI | FTC Solar, Inc. | 1.38 | 1.241 | 1.12–1.2596 | -10.07% | 12.29 | $22.90M | 1.12 | 1.2596 |
| VIVK | Vivakor, Inc. | 0.4826 | 0.44 | 0.4385–0.4885 | -8.83% | 7.15 | $701.00K | 0.4385 | 0.4885 |
| JAGX | Jaguar Health, Inc. | 0.4988 | 0.46 | 0.4499–0.4909 | -7.78% | 6 | $1.00M | 0.4499 | 0.4909 |
| MASK | 3 E Network Technology Group Ltd. Class A | 1.64 | 1.53 | 1.5–2.1556 | -6.71% | 286.68 | $2.20M | 1.5 | 2.1556 |
| BDMD | Baird Medical Investment Holdings Ltd | 0.1091 | 0.1022 | 0.0935–0.1804 | -6.32% | 807.63 | $3.80M | 0.0935 | 0.1804 |
| YFOR | YYForce Limited Class A | 0.128 | 0.12 | 0.1164–0.1245 | -6.25% | 7.51 | $1.50M | 0.1164 | 0.1245 |
| WFF | WF Holding Limited | 1.32 | 1.2398 | 1.2398–1.3003 | -6.08% | 4.65 | $7.10M | 1.2398 | 1.3003 |
| SDEV | Stablecoin Development Corporation | 0.9629 | 0.9107 | 0.913–0.9883 | -5.82% | 0.88 | $65.30M | 0.913 | 0.9883 |
| BURU | Nuburu, Inc. | 0.2345 | 0.2265 | 0.2238–0.2404 | -4.83% | 1.46 | $2.80M | 0.2238 | 0.2404 |
| MERC | Mercer International Inc. | 0.25 | 0.2383 | 0.2277–0.2498 | -4.68% | 2.19 | $15.00M | 0.2277 | 0.2498 |
| GPUS | Hyperscale Data, Inc. | 0.1609 | 0.1544 | 0.1507–0.1641 | -4.40% | 4.6 | $28.50M | 0.1507 | 0.1641 |

## 5. StockTwits lead read

**The StockTwits feed publishes no history, so a 2026-11-05 trending list cannot be reconstructed.** The feed was also unreachable from this runtime on Nov 5 — cron #15's own source health records the `mcp__stocktwits__*` tools as absent — and the MCP-over-HTTP bridge returns only the live list, which on this rebuild is the Nov 6 list. Publishing that as Nov 5's would be wrong, so it is not published.

What replaces it is the lead read the fleet *did* capture on Nov 5: the ten names whose catalyst was sourced at the pre-open checkpoint, with their thesis and their pre-market print.

| Ticker | Name | Pre-market last | Gap % | Thesis | Confidence |
|---|---|---|---|---|---|
| ELPW | Elong Power Holding Limited Class A | 3.49 | +39.04% | Announced $300M energy storage cooperation agreement | unverified |
| AMTX | Aemetis, Inc. | 1.73 | +38.40% | Q3 results reported | unverified |
| ARQ | Arq, Inc. | 2.4903 | +34.61% | Q3 results beat; strong pre-market volume | unverified |
| APP | AppLovin Corp. Class A | 350 | +28.79% | Q3 results beat expectations | unverified |
| SEZL | Sezzle Inc. | 172.66 | +26.32% | Q3 results and raised FY26 guidance for fourth time | high |
| WRBY | Warby Parker, Inc. Class A | 25.75 | +20.95% | Q3 results beat | high |
| U | Unity Software, Inc. | 48.05 | +13.17% | Q3 results beat expectations | unverified |
| ANVS | Annovis Bio Inc | 0.87 | -28.10% | Public offering pricing announced | high |
| VCYT | Veracyte, Inc. | 29.41 | -44.00% | Q3 results miss | unverified |
| MNTN | MNTN, Inc Class A | 5.1 | -50.82% | Q3 revenue miss and slashed FY guidance after sales force departures; downgrades issued | unverified |

Source: `preopen-feed/2026-11-05-0830.jsonl` (cron #92a checkpoint, 10:10:24 ET pull); the underlying catalyst reference is https://www.stocktitan.net/rankings/stock-movers-today/premarket. Cron #15's 08:22 ET `PRE_GAP` roster (`earnings/2026-11-05-reactions.md`) is the second lead read and is used throughout §2 and §9.

## 6. Watchlist

**The published watchlist did not exist on 2026-11-05.** `refs/watchlist.yaml` was seeded on 2026-11-06 (its own header says so), so this section is the list as it stands now, priced against the Nov 5 pre-market. Gaps are pre-market prints from Yahoo's Nov 5 pre-market bars; the prior close is cron #20's settled 2026-11-04 close.

| Ticker | Note | Prior close | Pre-market last | PM range | Gap % | Prior session % |
|---|---|---|---|---|---|---|
| AMZN | mega-cap core; earnings flag | 266 | 271.51 | 264.1–272.8 | +2.07% | +6.12% |
| NVDA | mega-cap core; earnings flag | 200.1 | 196 | 195.86–200 | -2.05% | -3.17% |
| GOOGL | mega-cap core; earnings flag | 288.9 | 293.27 | 286.4602–295.08 | +1.51% | +3.18% |
| AAPL | mega-cap core; earnings flag | 349.5 | 353.91 | 348.9–355.35 | +1.26% | +5.31% |
| MSFT | mega-cap core; earnings flag | 555.8 | 554.23 | 550.12–559.94 | -0.28% | +6.68% |
| IWM | small-cap beta leg | 284.02 | 284.19 | 283.71–286.13 | +0.06% | +1.51% |

## 7. Overnight

Futures, volatility, crypto and FX are the 08:30 ET pre-open prints; the cash index and the Asia lines are the 2026-11-04 close and the 2026-11-05 Asian close. Every row carries its own timestamp.

| Instrument | Level | Chg % | As of (ET) | Source |
|---|---|---|---|---|
| S&P 500 futures (ES=F, front month) | 7726.5 | +0.08% | 11-05 08:30 | Yahoo chart 5m |
| Nasdaq 100 futures (NQ=F, front month) | 28320 | -0.86% | 11-05 08:30 | Yahoo chart 5m |
| Dow futures (YM=F, front month) | 53837 | +0.62% | 11-05 08:30 | Yahoo chart 5m |
| Russell 2000 futures (RTY=F, front month) | 2871 | +0.18% | 11-05 08:30 | Yahoo chart 5m |
| VIX (overnight session print) | 16.86 | +1.51% | 11-05 08:30 | Yahoo chart 5m |
| SPY pre-market | 767.34 | +0.07% | 11-05 08:30 | Yahoo chart 5m |
| QQQ pre-market | 685.8401 | -0.88% | 11-05 08:30 | Yahoo chart 5m |
| DIA pre-market | 536.3 | +0.60% | 11-05 08:30 | Yahoo chart 5m |
| IWM pre-market | 284.36 | +0.12% | 11-05 08:30 | Yahoo chart 5m |
| SMH (semis) pre-market | 485.6503 | -3.69% | 11-05 08:30 | Yahoo chart 5m |
| XLK pre-market | 173.4465 | -1.73% | 11-05 08:30 | Yahoo chart 5m |
| XLF pre-market | 59.88 | +1.15% | 11-05 08:30 | Yahoo chart 5m |
| XBI pre-market | 158.52 | -0.36% | 11-05 08:20 | Yahoo chart 5m |
| Bitcoin | 79623.6484 | +4.85% | 11-05 08:30 | Yahoo chart 5m |
| Ether | 2387.1699 | +6.83% | 11-05 08:30 | Yahoo chart 5m |
| EUR/USD | 1.1218 | -0.15% | 11-05 08:30 | Yahoo chart 5m |
| USD/JPY | 158.472 | +0.07% | 11-05 08:30 | Yahoo chart 5m |
| US dollar index (DXY) | 101.63 | +0.12% | 11-05 08:30 | Yahoo chart 5m |
| US 10-year yield (^TNX) | 4.902 | +0.16% | 11-05 08:30 | Yahoo chart 5m |
| Gold (GC=F) | 4122.5 | +1.22% | 11-05 08:30 | Yahoo chart 5m |
| WTI crude (CL=F) | 89.61 | +1.69% | 11-05 08:30 | Yahoo chart 5m |
| S&P 500 cash (11-04 close) | 7688.6201 | +1.58% | 11-04 16:00 | Yahoo chart daily |
| Nasdaq Composite (11-04 close) | 25736.5098 | +1.44% | 11-04 16:00 | Yahoo chart daily |
| Dow (11-04 close) | 53356.1211 | +3.03% | 11-04 16:00 | Yahoo chart daily |
| Nikkei 225 (11-05 close) | 57434.7695 | -5.96% | 11-05 close | Yahoo chart daily |
| Hang Seng (11-05 close) | 24481.8594 | -1.27% | 11-05 close | Yahoo chart daily |
| Shanghai Composite (11-05 close) | 3649.1775 | -1.10% | 11-05 close | Yahoo chart daily |
| Euro Stoxx 50 (intraday) | 6305.4702 | +0.63% | 11-05 08:30 | Yahoo chart 5m |
| DAX (intraday) | 26619.4102 | +0.69% | 11-05 08:30 | Yahoo chart 5m |
| FTSE 100 (intraday) | 10915.7803 | +0.80% | 11-05 08:30 | Yahoo chart 5m |

The overnight picture is split, not uniform: US futures flat with the Nasdaq the weak leg, the semis already down hard (SMH -3.69% pre-market, under its 200-day average for the first time since May 2025), Europe modestly higher, and crypto and gold bidding. Asia has already taken the political read — the Nikkei closed -5.96%.

## 8. Macro calendar

- **Thursday Nov 5 is a Tier 2 day** — claims and productivity, no high-impact release (the fleet's `macro-calendar/2026-11-04-midweek.md`).
- **08:30 ET — Initial Jobless Claims (w/e Oct 31)**, 197K consensus against 194K prior, plus continuing claims and the 4-week average.
- **08:30 ET — Labor Productivity (Q3 prelim)**, +2.9% consensus against +1.4% prior; **Unit Labor Costs (Q3 prelim)**, -0.1% consensus against +1.2% prior.
- **~08:50 ET — Cleveland Fed president Beth Hammack**, and **09:10 ET — Richmond Fed president Thomas Barkin**. Hammack dissented in favour of a hike on Oct 28, so her remarks are the hawkish risk in the window.
- **Tomorrow, Friday Nov 6, 08:30 ET — the Employment Situation.** That print is the event this session is positioning around, and it is why the claims block matters.

## 9. Earnings today

Cron #19 published no `earnings/2026-11-05-reminders.md` — the file for Nov 5 does not exist on the outputs repo (the last one is 2026-11-04), so the roster is taken from cron #15's 08:22 ET `earnings/2026-11-05-reactions.md` and counted from that file, plus the published pre-open earnings notes. No range is published: every count below names its source.

### Already in the tape — reported before the open (BMO)

| Ticker | Company | Release | Gap % | Print |
|---|---|---|---|---|
| TRIP | TripAdvisor, Inc. | pre-open 07:05 ET, Nov 5 | -21.18% | Q3 2026 results posted before the open; call at 08:30 ET |
| FOUR | Shift4 Payments, Inc. Class A | before the open, Nov 5 | -11.76% | Shift4 Q3 2026 results released before the open |
| VCYT | Veracyte, Inc. | before the open, Nov 5 | -44.00% | Q3 beat on EPS $0.51 vs $0.41 and revenue $151.8M vs $147.4M, but Decipher volume missed internally and FY26 revenue was guided to $590-593M |
| MNTN | MNTN, Inc Class A | before the open, Nov 5 | -50.82% | 2026 revenue forecast cut to $311-314M on sales-team problems; new chief executive named |

### In the tape — reported on Nov 4 after the close, reacting on Nov 5

| Ticker | Company | Gap % | Print |
|---|---|---|---|
| APP | AppLovin Corp. Class A | +28.79% | Record Q3: revenue $2.185B vs $2.078B est, adj EPS $4.30 vs $4.04, adj EBITDA $1.842B vs $1.732B, Q4 revenue guide $2.365-2.395B vs $2.251B est, buyback raised by $3.2B |
| SEZL | Sezzle Inc. | +26.32% | Q3 beat: adj EPS $1.37 vs $1.29 est, revenue $166.5M vs $154.9M est, FY26 revenue-growth guide ~42.5%, FY27 adj EPS guide $7.20 vs $6.65 est |
| LYNX | Lyntris Inc | +22.47% | Q3 EPS $0.15 vs $0.08 est, revenue $194.4M (+90.4% y/y), backlog more than doubled |
| QCOM | QUALCOMM Incorporated | -13.36% | FQ4 revenue $10.442B (-7% y/y), non-GAAP EPS $2.17 (-28% y/y), handset revenue -26% y/y |
| BROS | Dutch Bros, Inc. Class A | -14.64% | Muted full-year forecast: at least $2.1B against $2.13B expected |
| SNAP | Snap, Inc. Class A | -10.64% | Q3 revenue $1.722B (+14% y/y), slightly below expectations |
| EXPE | Expedia Group, Inc. | -9.78% | Named in the overnight downside earnings list |
| MELI | MercadoLibre, Inc. | -7.98% | Named in the overnight downside earnings list |
| FICO | Fair Isaac Corporation | -7.29% | Named in the overnight downside earnings list |
| CAVA | CAVA Group, Inc. | -8.91% | Named in the overnight downside earnings list |
| ZG | Zillow Group, Inc. Class A | -8.51% | Named in the overnight downside earnings list |
| DAVE | Dave, Inc. Class A | -12.37% | Named in the overnight downside earnings list |
| HUBS | HubSpot, Inc. | +3.21% | Named in the overnight upside earnings list |

### Still ahead — reported after the close on Nov 5 (AMC)

Airbnb and Cloudflare are the large names reported after the close on Nov 5 (https://www.investopedia.com/5-things-investors-need-to-know-about-thursday-s-markets-12237605). Cron #19's roster for the date is absent, so this list is not enumerated beyond that source and no count is claimed.

## 10. Source health

| Source | Query / URL | Status |
|---|---|---|
| Pre-market screen (primary) | `preopen-feed/2026-11-05-0830.jsonl` + `daily-briefs/2026-11-05-pre-market-refresh.md` (cron #26b, TradingView pull 2026-11-05 10:10:24 ET) | ok — 702 names |
| Pre-market high/low, overnight levels | Yahoo chart API (5m + 1d bars, `includePrePost=true`) | ok — 748 symbols |
| Prior close and prior session | `us-eod/2026-11-04.csv` (cron #20, settled) | ok — 4,548 names |
| Market cap / sector / exchange fallback | `us-eod/2026-11-05.csv` | ok — 4,840 names |
| Earnings roster | `earnings/2026-11-05-reactions.md` (cron #15, 08:22 ET) | ok — 164 US rows |
| Earnings roster (cron #19) | `earnings/2026-11-05-reminders.md` | **failed — 404, the file does not exist**; fell back to cron #15 |
| Macro calendar | `macro-calendar/2026-11-04-midweek.md` | ok |
| Watchlist | `refs/watchlist.yaml` | ok — but seeded 2026-11-06, after this fire |
| News | investopedia, tradingkey, investrade, marketchameleon, benzinga, stocktitan, businessinsider | ok |
| StockTwits trending | MCP-over-HTTP bridge / `mcp__stocktwits__*` | **failed — live-only feed, no history for 2026-11-05**; §5 substitutes the checkpoint's captured catalysts |
| MCP availability probe | connector catalog | ok — no finance MCP registered (not an error) |

**Cross-check.** The screen's final pre-market prints and Yahoo's Nov 5 pre-market bars agree on the published names; the pre-market high/low on every published row is Yahoo's, and the last print and the gap are the fleet's screen.

## 11. Open research queue

1. The pre-market volume for the names that only cron #15's 08:22 ET screen covers is not published anywhere in the fleet for 2026-11-05 — their %ADV cannot be filled in, only their gate status. A pre-open pull that keeps the volume column would close that hole.
2. The StockTwits lead read has no replay path: the feed publishes no history, so a delayed rebuild loses the section entirely. A checkpoint file that stores the trending list would make the section replayable.
3. Leveraged single-stock ETFs (Tradr 2X Long APP at +58.8%, GraniteShares 2X Long QCOM at -26.3%) sit on the market-wide mover boards and are not stocks. The screen's universe filter should exclude them explicitly.
4. MNTN and VCYT were the two largest decliners and both were guidance cuts, not misses — check whether the brief's earnings tags distinguish a cut from a miss.
5. The Nov 4 brief published no key levels, so yesterday's calls can only be reviewed as did-the-gap-hold. Publishing a level per name would make the loop measurable.

## Yesterday's brief — what happened

Yesterday's 2026-11-04 08:30 ET brief published 105 named calls. The test applied here is whether the pre-market gap survived the session: **HELD** if the close finished on the far side of the prior close, **BROKE** if it closed back through it, **PARTIAL** if it closed within 0.5% of it, **UNJUDGED** where the name is not in cron #20's settled file.

| Ticker | 11-04 pre-market % | 11-04 session % | Outcome | Thesis held? |
|---|---|---|---|---|
| CRIS | +83.50% | +55.48% | closed 1.11 | HELD |
| PARA | -57.42% | -88.27% | closed 0.319 | HELD |
| CENN | -52.64% | -40.54% | closed 0.177 | HELD |
| DKI | +51.33% | n/p | not in cron #20's settled file | UNJUDGED |
| DOX | -37.03% | -30.07% | closed 43.66 | HELD |
| NRIX | -32.96% | -38.23% | closed 15.95 | HELD |
| AIOK | +25.63% | n/p | not in cron #20's settled file | UNJUDGED |
| ALIT | +24.21% | +25.89% | closed 12.74 | HELD |
| FTCI | +22.75% | -4.83% | closed 1.38 | BROKE |
| WORX | +22.38% | n/p | not in cron #20's settled file | UNJUDGED |
| FIS | -20.80% | -23.65% | closed 29.77 | HELD |
| TBLA | -20.59% | -19.41% | closed 2.74 | HELD |
| DUOL | +20.35% | +25.99% | closed 161.3 | HELD |
| XXII | -20.08% | -13.04% | closed 0.042 | HELD |
| INLF | -19.71% | n/p | not in cron #20's settled file | UNJUDGED |
| CPSH | +19.15% | +10.47% | closed 3.85 | HELD |
| DDOG | -18.37% | -14.42% | closed 188.7 | HELD |
| CIFR | -16.87% | -19.95% | closed 6.5 | HELD |
| NCEL | -16.67% | n/p | not in cron #20's settled file | UNJUDGED |
| HPAI | +14.30% | n/p | not in cron #20's settled file | UNJUDGED |
| MERC | -14.01% | n/p | not in cron #20's settled file | UNJUDGED |
| RIOT | +13.69% | +9.63% | closed 15.37 | HELD |
| BIVI | -13.29% | -22.54% | closed 1.34 | HELD |
| SHFS | -12.74% | -23.56% | closed 0.0318 | HELD |
| BDMD | -12.74% | n/p | not in cron #20's settled file | UNJUDGED |
| HELE | +12.73% | +25.39% | closed 37.04 | HELD |
| NVTS | +12.15% | +9.00% | closed 9.33 | HELD |
| CLSK | -11.90% | -16.56% | closed 6.8 | HELD |
| HUBC | -11.72% | n/p | not in cron #20's settled file | UNJUDGED |
| SWKS | -11.51% | -2.90% | closed 82.92 | HELD |
| OUST | +11.49% | +15.73% | closed 33.54 | HELD |
| NICE | -11.45% | n/p | not in cron #20's settled file | UNJUDGED |
| SGRX | -11.06% | -7.27% | closed 0.7011 | HELD |
| ARRY | +10.99% | +14.87% | closed 5.33 | HELD |
| METC | -10.98% | +3.56% | closed 6.98 | BROKE |
| KD | +10.74% | +30.06% | closed 16.83 | HELD |
| DJT | -10.61% | -24.54% | closed 4.49 | HELD |
| HUT | -10.59% | -23.23% | closed 48.94 | HELD |
| ARDX | +10.56% | +8.58% | closed 3.29 | HELD |
| FLYW | +10.55% | +13.89% | closed 21.81 | HELD |
| TE | +10.25% | -3.36% | closed 2.735 | BROKE |
| HL | +10.19% | +13.17% | closed 14.95 | HELD |
| MDLN | +10.00% | +18.36% | closed 40.35 | HELD |
| SEGG | +9.86% | -26.76% | closed 1.56 | BROKE |
| XYZ | +9.68% | +15.24% | closed 87.58 | HELD |
| GERN | +9.68% | +16.13% | closed 1.08 | HELD |
| CYH | +9.51% | +15.85% | closed 2.375 | HELD |
| SCZM | +9.31% | n/p | not in cron #20's settled file | UNJUDGED |
| SEDG | -9.06% | n/p | not in cron #20's settled file | UNJUDGED |
| MKDW | -8.98% | n/p | not in cron #20's settled file | UNJUDGED |
| SLGB | -8.95% | n/p | not in cron #20's settled file | UNJUDGED |
| GLXY | -8.79% | -16.99% | closed 13.97 | HELD |
| CORZ | -8.71% | -10.39% | closed 12.76 | HELD |
| HYMC | +8.70% | +8.58% | closed 17.47 | HELD |
| CRWV | -8.67% | -9.90% | closed 48.42 | HELD |
| BTDR | -8.60% | n/p | not in cron #20's settled file | UNJUDGED |
| YFOR | -8.50% | n/p | not in cron #20's settled file | UNJUDGED |
| USAS | +8.45% | n/p | not in cron #20's settled file | UNJUDGED |
| OSCR | +8.45% | +8.58% | closed 35.19 | HELD |
| ASM | +8.43% | n/p | not in cron #20's settled file | UNJUDGED |
| VNET | +8.39% | n/p | not in cron #20's settled file | UNJUDGED |
| RBNE | -8.31% | n/p | not in cron #20's settled file | UNJUDGED |
| VST | -8.30% | -13.86% | closed 120.2 | HELD |
| OCGN | +8.24% | +17.35% | closed 0.8745 | HELD |
| POLA | -8.24% | -28.23% | closed 0.3733 | HELD |
| SBSW | +8.14% | n/p | not in cron #20's settled file | UNJUDGED |
| ARIS | +7.98% | n/p | not in cron #20's settled file | UNJUDGED |
| SPCX | -7.83% | -3.81% | closed 135.9 | HELD |
| MUX | +7.77% | n/p | not in cron #20's settled file | UNJUDGED |
| EXK | +7.68% | n/p | not in cron #20's settled file | UNJUDGED |
| EGO | +7.51% | n/p | not in cron #20's settled file | UNJUDGED |
| LABT | -7.18% | -1.85% | closed 0.1914 | HELD |
| NAMM | +7.16% | n/p | not in cron #20's settled file | UNJUDGED |
| FSLR | +6.87% | +4.63% | closed 194.5 | HELD |
| ZNB | -6.59% | n/p | not in cron #20's settled file | UNJUDGED |
| IREN | -6.50% | n/p | not in cron #20's settled file | UNJUDGED |
| NBIS | -6.49% | n/p | not in cron #20's settled file | UNJUDGED |
| PLUG | +6.38% | +3.55% | closed 1.46 | HELD |
| GPUS | +6.11% | -5.41% | closed 0.1609 | BROKE |
| SPWR | +6.06% | +7.08% | closed 0.242 | HELD |
| APLD | -5.90% | -6.74% | closed 16.61 | HELD |
| NVO | +5.72% | n/p | not in cron #20's settled file | UNJUDGED |
| NXT | +5.65% | +11.12% | closed 106.7 | HELD |
| PMAX | +5.47% | n/p | not in cron #20's settled file | UNJUDGED |
| CHSN | +5.33% | n/p | not in cron #20's settled file | UNJUDGED |
| TSLA | -5.13% | -3.34% | closed 385.2 | HELD |
| NWGL | +5.03% | n/p | not in cron #20's settled file | UNJUDGED |
| ARAY | +4.60% | +3.97% | closed 0.1491 | HELD |
| ZEO | +4.54% | -1.21% | closed 0.2523 | BROKE |
| JAGX | -4.47% | -10.53% | closed 0.4988 | HELD |
| BATL | -4.33% | -5.34% | closed 0.7867 | HELD |
| ENPH | +4.16% | +3.71% | closed 31.55 | HELD |
| WFF | +4.14% | n/p | not in cron #20's settled file | UNJUDGED |
| ABOS | -4.01% | -7.72% | closed 0.2163 | HELD |
| DDC | -3.85% | +5.38% | closed 0.137 | BROKE |
| HXHX | -3.70% | n/p | not in cron #20's settled file | UNJUDGED |
| RADX | -3.26% | n/p | not in cron #20's settled file | UNJUDGED |
| EHGO | +3.20% | n/p | not in cron #20's settled file | UNJUDGED |
| MCD | +2.09% | +6.58% | closed 280.3 | HELD |
| NVDA | -1.37% | -3.17% | closed 200.1 | HELD |
| UBER | +1.11% | +4.91% | closed 69.87 | HELD |
| SMCI | +0.86% | -5.70% | closed 29.6 | BROKE |
| AMD | -0.67% | +1.01% | closed 488.8 | BROKE |
| BCRX | +0.44% | -3.85% | closed 8.24 | BROKE |
| WULF | -0.24% | -6.62% | closed 11.7 | HELD |

Of yesterday's 105 named calls, **58 held** their gap through the session, **10 broke**, 0 closed back inside the prior close and 37 could not be judged. The misses punished hardest: DOX, NRIX, FIS and DDOG all continued in the direction of the gap, while AMD, SMCI, TE, METC, SEGG and GPUS gave their gaps back. The Nov 4 brief published no key level for any name, so the test can only be a gap-survival test — see the open research queue.

