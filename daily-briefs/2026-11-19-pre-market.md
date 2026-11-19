# Agentic pre-market brief — 2026-11-19

One pull of the tape at 08:34 ET. The ±3% band is COMPLETE (514 gainers, 188 decliners, `len(rows) == totalCount` asserted on both screens). The tail screen returned 400 rows against a totalCount of 2,714, so the tail tier below is a FLOOR of that cohort, not the whole cohort. The companion machine-readable screen is `daily-briefs/2026-11-19-pre-market.csv` (914 rows) and this brief is built from that same table.

---
date: 2026-11-19
cron: 26-agentic-pre-market-brief
contract: premarket-brief-artifact-v2
fire_time_et: 2026-11-19 08:30
snapshot_et: 08:34
source: TradingView america scanner + MCP-bridge market-recap
status: ok
themes: 6
up_3pct: 514
down_3pct: 188
screen_complete: true
tail_tier: premarket-brief-tail-v1
tail_rows: 24
---

## Bottom line

1. **The one setup** — RERE **+4.76%** at 4.18: long above the 3.99 prior close, and the invalidation is a trade back below 3.99. ATRenew beat on adjusted EPS at RMB0.99 against RMB0.84 and guided Q4 revenue growth to 24.4%-26.0%, the gap is still holding its pre-market high of 4.20, and the book is 8.3% of the 30-day average — the only ticker on the screen that clears all six setup tests.
2. **The one risk** — gold at a 14-month low, $3,693.13 overnight and still the pressure point after a 3.2% Wednesday, with the Fed's October minutes pointing to a December hike: the rate complex is what broke the metals, and **SA -9.78%** shows how fast a leveraged miner can go when the complex does not agree.
3. **The one thing to watch** — Anthropic's Nasdaq debut as **ANT** at $83 a share: the IPO priced above its range and the whole AI complex is trading on it, so a weak open gives back the **PANW +10.01%** gap and a strong one makes it a second leg.

**The setup rule, published so the pick can be audited.** A candidate must clear all six tests: a catalyst for that ticker sourced in this run, a catalyst that is not a scheduled binary verdict, the gap running the way the setup bets, the pre-market last within 1% of the pre-market high on a gap-up or of the pre-market low on a gap-down, pre-market volume at 5% of the 30-day average or more, and a published market cap of $100m or more. RERE clears all six. The near-misses: **PANW +10.01%** fails the book at 2.52% of ADV, **PDD +5.50%** fails the hold at 4.77% below its pre-market high, **NBIS +6.15%** fails the book at 3.15% of ADV, and **SLS -20.61%** fails the hold at 6.74% above its pre-market low.

## Yesterday's brief — what happened

Reviewed the **2026-11-18** pre-market brief. "Yesterday's close" is the close of the last completed regular session (**2026-11-18**); "Today's move" is that session's % change vs its own prior close. "Thesis held?" is tested against the invalidation level the 2026-11-18 brief published, across every session from 2026-11-18 to 2026-11-18: **WORKED** = the invalidation held, the setup's trigger was reached and the session moved with it, **HELD** = the invalidation held and the session moved with the setup but the trigger could not be resolved, **SURVIVED** = the invalidation held but the trigger was never reached, so the setup never activated, **BROKE** = the level was traded through, **PARTIAL** = the level held but the session moved against it, **UNJUDGED** = no level or no price. Price cross-check: closes agree with the 2026-11-18 post-market brief.

| Name | Setup (yesterday) | Yesterday's close | Today's move | Thesis held? |
|---|---|---|---|---|
| NVDA | C2 — The AI complex after Nvidia's beat-and-raise | 150.96 | -2.90% | BROKE (the 155.46 invalidation was traded through on 2026-11-18) |
| MDLN | C4 — Sponsor blocks: secondary supply sets the anchor | 39.16 | +3.93% | HELD (the 35.5 invalidation held and the session moved with the setup) |
| NBIS | C2 — The AI complex after Nvidia's beat-and-raise | 106.96 | +0.87% | BROKE (the 106.03 invalidation was traded through on 2026-11-18) |
| AAOI | C2 — The AI complex after Nvidia's beat-and-raise | 40.79 | -9.80% | BROKE (the 40.01 invalidation was traded through on 2026-11-18) |
| WULF | C2 — The AI complex after Nvidia's beat-and-raise | 12.00 | +2.83% | BROKE (the 11.67 invalidation was traded through on 2026-11-18) |
| SLS | C6 — Biotech and the FDA-approval complex | 17.95 | -6.27% | PARTIAL (the 16.9 invalidation held but the session moved against the setup) |
| CIFR | C2 — The AI complex after Nvidia's beat-and-raise | 6.57 | +2.34% | BROKE (the 6.42 invalidation was traded through on 2026-11-18) |
| PONY | C5 — Autonomy, gaming and crypto prints | 3.70 | -7.27% | BROKE (the 3.99 invalidation was traded through on 2026-11-18) |
| BE | C2 — The AI complex after Nvidia's beat-and-raise | 170.98 | -1.43% | BROKE (the 173.46 invalidation was traded through on 2026-11-18) |
| MRVL | C2 — The AI complex after Nvidia's beat-and-raise | 145.54 | -2.15% | BROKE (the 148.74 invalidation was traded through on 2026-11-18) |
| IAUX | C1 — Precious metals and the miners: the Fed's hawkish turn breaks gold | 1.13 | -7.38% | BROKE (the 1.14 invalidation was traded through on 2026-11-18) |
| SNDK | C2 — The AI complex after Nvidia's beat-and-raise | 776.22 | -2.64% | BROKE (the 797.24 invalidation was traded through on 2026-11-18) |
| TJX | C3 — US retail, consumer and media prints: the beats the market sold | 140.30 | +8.05% | WORKED (the 129.85 invalidation held, the 141 pre-market-high break was reached on 2026-11-18, and the session moved with the setup) |
| TGT | C3 — US retail, consumer and media prints: the beats the market sold | 165.93 | +4.01% | HELD (the 153.4 invalidation held and the session moved with the setup) |
| APLD | C2 — The AI complex after Nvidia's beat-and-raise | 14.45 | +1.62% | BROKE (the 14.22 invalidation was traded through on 2026-11-18) |
| TTWO | C5 — Autonomy, gaming and crypto prints | 216.61 | +6.22% | WORKED (the 203.93 invalidation held, the 219.9 pre-market-high break was reached on 2026-11-18, and the session moved with the setup) |
| SBSW | C1 — Precious metals and the miners: the Fed's hawkish turn breaks gold | 7.76 | -8.17% | BROKE (the 7.92 invalidation was traded through on 2026-11-18) |
| COHR | C2 — The AI complex after Nvidia's beat-and-raise | 212.84 | +0.94% | BROKE (the 210.86 invalidation was traded through on 2026-11-18) |
| CAPR | C6 — Biotech and the FDA-approval complex | 8.03 | -4.52% | BROKE (the 8.41 invalidation was traded through on 2026-11-18) |
| RYDE | C5 — Autonomy, gaming and crypto prints | 1.12 | +0.00% | BROKE (the 1.12 invalidation was traded through on 2026-11-18) |
| EXK | C1 — Precious metals and the miners: the Fed's hawkish turn breaks gold | 6.56 | -7.99% | BROKE (the 6.76 invalidation was traded through on 2026-11-18) |
| CORZ | C2 — The AI complex after Nvidia's beat-and-raise | 14.05 | +4.00% | BROKE (the 13.51 invalidation was traded through on 2026-11-18) |
| LOW | C3 — US retail, consumer and media prints: the beats the market sold | 222.78 | +1.05% | HELD (the 209.93 invalidation held and the session moved with the setup) |
| BRBR | C3 — US retail, consumer and media prints: the beats the market sold | 13.66 | +24.07% | WORKED (the 11.01 invalidation held, the 12.91 pre-market-high break was reached on 2026-11-18, and the session moved with the setup) |
| FRMI | C2 — The AI complex after Nvidia's beat-and-raise | 2.46 | +2.08% | BROKE (the 2.41 invalidation was traded through on 2026-11-18) |
| AEHR | C2 — The AI complex after Nvidia's beat-and-raise | 49.48 | -0.52% | BROKE (the 49.74 invalidation was traded through on 2026-11-18) |
| IAG | C1 — Precious metals and the miners: the Fed's hawkish turn breaks gold | 15.85 | -7.20% | BROKE (the 16.22 invalidation was traded through on 2026-11-18) |
| BLSH | C5 — Autonomy, gaming and crypto prints | 20.36 | +5.66% | WORKED (the 19.27 invalidation held, the 21.75 pre-market-high break was reached on 2026-11-18, and the session moved with the setup) |
| FCX | C1 — Precious metals and the miners: the Fed's hawkish turn breaks gold | 51.45 | -6.96% | BROKE (the 53.15 invalidation was traded through on 2026-11-18) |
| AU | C1 — Precious metals and the miners: the Fed's hawkish turn breaks gold | 79.48 | -6.13% | BROKE (the 80.23 invalidation was traded through on 2026-11-18) |
| HSAI | C5 — Autonomy, gaming and crypto prints | 13.00 | +3.26% | WORKED (the 12.59 invalidation held, the 13.19 pre-market-high break was reached on 2026-11-18, and the session moved with the setup) |
| ARDT | C4 — Sponsor blocks: secondary supply sets the anchor | 14.40 | -18.87% | BROKE (the 14 invalidation was traded through on 2026-11-18) |
| JMIA | C3 — US retail, consumer and media prints: the beats the market sold | 2.74 | -40.82% | BROKE (the 3.61 invalidation was traded through on 2026-11-18) |
| IPHA | C6 — Biotech and the FDA-approval complex | 1.03 | -22.56% | BROKE (the 1.09 invalidation was traded through on 2026-11-18) |
| DLB | C3 — US retail, consumer and media prints: the beats the market sold | 56.77 | -3.48% | PARTIAL (the 55.84 invalidation held but the session moved against the setup) |
| NEM | C1 — Precious metals and the miners: the Fed's hawkish turn breaks gold | 104.53 | -6.05% | BROKE (the 106.95 invalidation was traded through on 2026-11-18) |
| GDX | C1 — Precious metals and the miners: the Fed's hawkish turn breaks gold | 74.82 | -5.97% | BROKE (the 76.33 invalidation was traded through on 2026-11-18) |
| GDXU | C1 — Precious metals and the miners: the Fed's hawkish turn breaks gold | 53.55 | -17.98% | BROKE (the 57.25 invalidation was traded through on 2026-11-18) |
| GLD | C1 — Precious metals and the miners: the Fed's hawkish turn breaks gold | 341.19 | -3.20% | BROKE (the 342.96 invalidation was traded through on 2026-11-18) |
| SLV | C1 — Precious metals and the miners: the Fed's hawkish turn breaks gold | 40.70 | -4.55% | BROKE (the 40.75 invalidation was traded through on 2026-11-18) |

**The scorecard: 30 BROKE, 5 WORKED, 3 HELD, 2 PARTIAL.** The 2026-11-18 brief's AI cluster was the day's worst performer: its names are the ones that traded through the invalidation it published, and the pattern worth carrying into this morning is that a gap which gives its move back on the day is not a gap that holds. That is the test RERE has to pass today at 3.99.

## 1. TL;DR

- **Anthropic's record IPO is the day's spine, and it is a re-rating of the AI complex, not a new one.** Anthropic priced 980 million shares at $83, above the $70-$78 range, raising $81.31bn at a ~$1.5 trillion valuation; the shares trade on Nasdaq today as ANT. **PANW +10.01%** leads on its own news (fiscal Q1 EPS $1.05 vs $0.97 expected, NGS ARR +66%, FY27 guidance raised, and a $4.5bn all-stock deal for Applied Compute), and the read-across carries the group: **CRWD +6.16%**, **GOOGL +4.11%** on its 1.8 billion Anthropic shares, **ORCL +3.52%**, **NBIS +6.15%**, **NVDA +1.46%**.
- **The picks-and-shovels are where the tape is actually sorted: optics, memory, storage and power.** **COHR +8.25%** leads the optical group, **BE +6.88%** on a BMO upgrade to Outperform, **STX +5.87%**, **SKHY +4.76%**, **MU +4.68%**, **SNDK +4.94%**, **WDC +5.49%**, **P +6.78%** on raised Everpure guidance, plus **AAOI +5.12%**, **LITE +4.85%**, **MRVL +4.07%** and **POET +4.00%**.
- **China internet earnings are split, and the split is the trade.** **PDD +5.50%** on a $3.14 adjusted EPS against $2.78 expected, **RERE +4.76%** on an EPS beat at RMB0.99, **BABA -1.23%** on a revenue beat and an EPS miss, **NTES -6.00%** missing on both, and the rest of the group moving with the ADR tape: BIDU **-0.51%**, KWEB **-0.64%**, DAO **-6.08%**.
- **Financing, not fundamentals, is the biggest single loser.** **SLS -20.61%** on an 11,538,462-share offering priced at $13.00, a 27.6% discount to Wednesday's close — the Phase 3 REGAL result behind the +156% on Tuesday is intact, the share count is what changed. **WSM -8.49%** is a sell-the-news: a 5.1% comparable and EPS of $2.19 non-GAAP, and the stock traded at $275.15 pre-market before round-tripping the whole move. **TTWO -2.02%** into the GTA VI launch. **WMT -1.02%** on a beat-and-raise.
- **Crypto-beta is back, and it is the thinnest signal on the tape.** Bitcoin at $63,631.00 is up 1.02% after a second bounce off $62,000, and with it **RIOT +5.92%**, **CYPH +6.29%**, **ASST +4.81%**, **GLXY +4.35%**, **HOOD +4.31%**, **BMNR +3.81%**, **MSTR +3.80%**, **COIN +3.36%**.
- **Precious metals are still the broken leg.** Spot gold printed a 14-month low at $3,693.13 in Asian trade before rebounding to $3,735.72, silver closed at $45.00 down 4.8%, and the cause is the Fed's October minutes. The complex is only about 1% lower pre-market (**NEM -1.27%**, **GFI -1.10%**, **EXK -1.05%**, **PAAS -0.74%**, **AU -0.49%**, **GLD -0.23%**) — with **SA -9.78%** the one name that is not explained by the metal.
- **Watchlist:** the published list is quiet and half of it is not even in today's themes — **GOOGL +4.11%** and **NVDA +1.46%** are the only two with a theme behind them, and the other six sit inside a 2.3% band. **GLD -0.23%** and **TLT -0.50%** are the two that sit against the day's other trade.
- **The post-open limit:** most of the day's biggest moves happen **post-open** — measured across seven sessions, 71% of every session's 20%+ moves land after 09:30 — so this brief cannot name them. It names what is in the pre-market tape at 08:34 ET.

## 2. Theme clusters

Every cluster is anchored to a catalyst sourced in this run. A name with no sourced catalyst gets a move and no story.

### C1 — Anthropic's IPO resets the AI trade

Anthropic priced 980 million shares at **$83** above its $70-$78 marketed range, raising **$81.31bn** and valuing the Claude maker at about $1.5 trillion fully diluted, and the shares begin trading on Nasdaq today under the ticker **ANT**. That is the day's catalyst: Nasdaq 100 futures are up about 2% and the S&P 500 futures about 1.2% after five straight down sessions. The leader is a company with its own news on top of it — **PANW +10.01%** on a fiscal Q1 beat, a raised FY27 guide and a $4.5bn all-stock agreement to acquire Applied Compute, the open-weight model platform. Cybersecurity follows the read-across (**CRWD +6.16%**), the hyperscalers follow the read-through (**GOOGL +4.11%**, which owns 1.8 billion Anthropic shares, and **ORCL +3.52%**), and the neocloud group follows Nvidia's guide (**NBIS +6.15%**). The exception is the anchor itself: **NVDA +1.46%** after falling 2.89% on Wednesday despite $115.8bn of revenue and about $130bn guided.

| Ticker | Prior close ($) | Pre-market last ($) | Gap % | PM range ($) | Key level | Invalidation | %ADV | Mkt cap | Prior session chg % |
|---|---|---|---|---|---|---|---|---|---|
| PANW | 339.92 | 373.96 | +10.01% | 369.08–376.75 | prior close 339.92 | back to/below prior close 339.92 | 2.5% | $278.3B | +9.90% |
| CRWD | 237.03 | 251.63 | +6.16% | 250.50–253.79 | prior close 237.03 | back to/below prior close 237.03 | 0.9% | $242.7B | +7.95% |
| GOOGL | 282.44 | 294.05 | +4.11% | 287.80–294.77 | prior close 282.44 | back to/below prior close 282.44 | 2.2% | $3,434.4B | +0.80% |
| ORCL | 113.89 | 117.90 | +3.52% | 116.17–117.94 | prior close 113.89 | back to/below prior close 113.89 | 0.7% | $344.4B | -0.97% |
| NBIS | 106.96 | 113.54 | +6.15% | 110.96–114.65 | prior close 106.96 | back to/below prior close 106.96 | 3.2% | $31.3B | +0.87% |
| NVDA | 150.96 | 153.17 | +1.46% | 152.45–154.80 | prior close 150.96 | back to/below prior close 150.96 | 3.3% | $3,638.1B | -2.89% |

Sources: Bloomberg/Swissinfo 2026-11-19 12:59 ET; MarketScreener 2026-11-19 04:51 ET; Invezz 2026-11-19; Barron's 2026-11-19; CNBC 2026-11-18 16:47 ET; <https://www.swissinfo.ch/eng/us-stock-futures-rise-on-anthropic,-aussie-drops:-markets-wrap/92404209>; <https://www.cnbc.com/2026/11/18/palo-alto-networks-panw-q1-2027-earnings-.html>

### C2 — The AI hardware chain: memory, storage, optics and power

If Anthropic's listing is the sentiment, the picks-and-shovels are the expression: **COHR +8.25%** leads the optical group, with POET, CIEN, AAOI and LITE alongside it (**AAOI +5.12%**, **LITE +4.85%**, **POET +4.00%**); memory and storage follow with **SKHY +4.76%**, **MU +4.68%**, **SNDK +4.94%**, **WDC +5.49%** and **STX +5.87%**; and the power leg is the strongest single name group in the tape, with **BE +6.88%** after BMO upgraded it to Outperform (target cut to $230 from $260) and **P +6.78%** after Everpure raised its fiscal-year revenue guidance to $5.20bn-$5.21bn. One note on the trade's other leg: the hosting names that also mine bitcoin — **HUT +6.31%**, **APLD +5.88%**, **CIFR +5.94%**, **WULF +5.80%** — are moving on the same AI-power demand and on bitcoin, and the two catalysts are not separable this morning.

| Ticker | Prior close ($) | Pre-market last ($) | Gap % | PM range ($) | Key level | Invalidation | %ADV | Mkt cap | Prior session chg % |
|---|---|---|---|---|---|---|---|---|---|
| COHR | 212.84 | 230.40 | +8.25% | 219.65–231.39 | prior close 212.84 | back to/below prior close 212.84 | 2.7% | $41.9B | +0.94% |
| BE | 170.98 | 182.74 | +6.88% | 177.01–185.66 | prior close 170.98 | back to/below prior close 170.98 | 3.2% | $50.6B | -1.43% |
| STX | 515.90 | 546.20 | +5.87% | 532.00–550.94 | prior close 515.90 | back to/below prior close 515.90 | 0.6% | $118.4B | +2.28% |
| MU | 705.27 | 738.31 | +4.68% | 728.88–749.20 | prior close 705.27 | back to/below prior close 705.27 | 2.7% | $798.0B | -1.00% |
| SNDK | 776.22 | 814.54 | +4.94% | 800.34–822.55 | prior close 776.22 | back to/below prior close 776.22 | 3.6% | $110.4B | -2.64% |
| WDC | 288.19 | 304.01 | +5.49% | 297.20–306.00 | prior close 288.19 | back to/below prior close 288.19 | 1.2% | $107.9B | +1.72% |
| SKHY | 122.47 | 128.30 | +4.76% | 127.89–130.03 | prior close 122.47 | back to/below prior close 122.47 | 2.6% | $87.1B | -0.11% |
| AAOI | 40.79 | 42.88 | +5.12% | 42.12–43.49 | prior close 40.79 | back to/below prior close 40.79 | 2.1% | $3.7B | -9.80% |
| LITE | 551.07 | 577.77 | +4.85% | 565.50–580.08 | prior close 551.07 | back to/below prior close 551.07 | 0.8% | $50.0B | -1.59% |
| MRVL | 145.54 | 151.46 | +4.07% | 149.63–153.00 | prior close 145.54 | back to/below prior close 145.54 | 1.2% | $127.6B | -2.15% |
| POET | 4.25 | 4.42 | +4.00% | 4.37–4.49 | prior close 4.25 | back to/below prior close 4.25 | 2.1% | $735M | -3.41% |
| P | 100.74 | 107.57 | +6.78% | 102.00–108.50 | prior close 100.74 | back to/below prior close 100.74 | 0.8% | $33.6B | -1.03% |

Sources: TradingKey pre-market report 2026-11-19; Barron's 2026-11-19; CNBC 2026-11-19 07:55 ET; Investing.com 2026-11-19 08:11 ET; <https://www.mitrade.com/en/articulo/news/live-news/article-8-2265512-20261119>; <https://www.barrons.com/articles/stock-movers-ddc27426>

### C3 — China ADR earnings: PDD beats, NetEase and Alibaba miss

The China internet complex repriced overnight, and the results are split rather than directional. **PDD +5.50%** on adjusted EPS of $3.14 against a $2.78 consensus and adjusted operating profit of RMB32.6bn against RMB27.9bn expected — but revenue was flat at RMB108.3bn and missed the RMB115.2bn estimate, with transaction services down 12%. **BABA -1.23%** on a revenue beat (RMB271.52bn) and a miss on adjusted EPS (RMB8.10 against about RMB10.75 expected), with cloud up 53%. **NTES -6.00%** missed on both revenue and EPS. **RERE +4.76%** is the cleanest print in the group: ATRenew beat on adjusted EPS at RMB0.99 against RMB0.84 and guided Q4 revenue growth to 24.4%-26.0%, though its revenue of RMB6.45bn missed the RMB7.58bn estimate. The rest of the group is moving with the ADR tape rather than on its own news: BIDU **-0.51%** against a Hong Kong close of -4.9%, KWEB **-0.64%**, TIGR **+3.10%**, FUTU **+2.91%**, JMIA **+2.92%**, DAO **-6.08%**.

| Ticker | Prior close ($) | Pre-market last ($) | Gap % | PM range ($) | Key level | Invalidation | %ADV | Mkt cap | Prior session chg % |
|---|---|---|---|---|---|---|---|---|---|
| PDD | 77.45 | 81.71 | +5.50% | 75.05–85.80 | prior close 77.45 | back to/below prior close 77.45 | 22.2% | $110.2B | +0.08% |
| RERE | 3.99 | 4.18 | +4.76% | 4.01–4.20 | prior close 3.99 | back to/below prior close 3.99 | 8.3% | $876M | -2.21% |
| BABA | 84.37 | 83.33 | -1.23% | 81.98–88.01 | prior close 84.37 | below PM low 81.98 | 22.5% | $216.2B | -2.63% |
| NTES | 118.43 | 111.33 | -6.00% | 110.00–114.20 | prior close 118.43 | below PM low 110.00 | 7.5% | $76.4B | -0.99% |

Sources: GlobeNewswire 2026-11-19 06:30 ET; EarningsWhispers 2026-11-19; el-fondo 2026-11-19; ChinaLastNight 2026-11-19; PRNewswire 2026-11-19; <https://www.stocktitan.net/news/PDD/pdd-holdings-announces-third-quarter-2026-unaudited-financial-zyjmlok1y30l.html>; <https://www.el-fondo.com/en/news/alibaba-net-income-triples-to-96b-on-ai-and-commerce>

### C4 — Crypto-beta and the digital-asset complex

Bitcoin is at $63,631.00, up 1.02% after bouncing off $62,000 for the second time in four days, and the whole digital-asset complex is with it: **RIOT +5.92%**, **CYPH +6.29%**, **BMNR +3.81%**, **MSTR +3.80%**, **COIN +3.36%**, **GLXY +4.35%**, **HOOD +4.31%** and **ASST +4.81%**. No company-specific catalyst is sourced for these names — this is the group's beta to a recovering bitcoin, amplified by the risk-on tone in the AI complex, and it is a thinner signal than the cluster above.

| Ticker | Prior close ($) | Pre-market last ($) | Gap % | PM range ($) | Key level | Invalidation | %ADV | Mkt cap | Prior session chg % |
|---|---|---|---|---|---|---|---|---|---|
| RIOT | 18.24 | 19.32 | +5.92% | 18.61–19.50 | prior close 18.24 | back to/below prior close 18.24 | 2.9% | $6.8B | +6.98% |
| MSTR | 90.32 | 93.75 | +3.80% | 92.77–95.10 | prior close 90.32 | back to/below prior close 90.32 | 2.4% | $38.1B | -6.40% |
| COIN | 110.51 | 114.22 | +3.36% | 113.48–115.02 | prior close 110.51 | back to/below prior close 110.51 | 1.1% | $29.3B | -3.92% |
| HOOD | 69.17 | 72.15 | +4.31% | 71.40–72.59 | prior close 69.17 | back to/below prior close 69.17 | 1.8% | $62.3B | -0.03% |
| BMNR | 15.47 | 16.06 | +3.81% | 15.98–16.26 | prior close 15.47 | back to/below prior close 15.47 | 1.4% | $9.7B | -2.46% |
| GLXY | 13.32 | 13.90 | +4.35% | 13.66–14.14 | prior close 13.32 | back to/below prior close 13.32 | 0.5% | $5.1B | +2.23% |
| CYPH | 1.75 | 1.86 | +6.29% | 1.79–1.96 | prior close 1.75 | back to/below prior close 1.75 | 2.6% | $261M | -8.14% |
| ASST | 17.15 | 17.98 | +4.81% | 17.70–18.20 | prior close 17.15 | back to/below prior close 17.15 | 2.7% | $2.2B | -5.20% |

Sources: Market snapshot 2026-11-19 13:34:59 UTC (BTC-USD $63,630.99, +1.02%); upside.pandobit 2026-11-19; Swissinfo/Bloomberg 2026-11-19 12:59 ET

### C5 — Precious metals: gold at a 14-month low

Gold fell 3.2% on Wednesday to its weakest close since September 2025 and then set a 14-month low of $3,693.13 in Asian trade this morning before rebounding about 0.8% to $3,735.72 at 07:00 ET. The cause is the Fed: the October minutes published Wednesday pointed to further tightening, with Governor Waller outlining 50bp in December or 25bp in December and January, and the dollar near a 19-month high. Silver closed at $45.00, down 4.8% at a 14-month low. The complex is only about 1% lower pre-market — **NEM -1.27%**, **GFI -1.10%**, **EXK -1.05%**, **PAAS -0.74%**, **AU -0.49%** and **GLD -0.23%** — with one exception: **SA -9.78%** is at its pre-market low and is not explained by the metal. No catalyst is sourced for Seabridge in this run, so it carries a move and no story; treat the -9.78% as idiosyncratic until the filing appears.

| Ticker | Prior close ($) | Pre-market last ($) | Gap % | PM range ($) | Key level | Invalidation | %ADV | Mkt cap | Prior session chg % |
|---|---|---|---|---|---|---|---|---|---|
| SA | 25.55 | 23.05 | -9.78% | 23.05–25.63 | prior close 25.55 | below PM low 23.05 | 12.5% | $2.8B | -2.78% |
| NEM | 104.53 | 103.20 | -1.27% | 103.20–104.54 | prior close 104.53 | below PM low 103.20 | 0.8% | $108.6B | -6.05% |
| GFI | 33.51 | 33.14 | -1.10% | 33.10–33.79 | prior close 33.51 | below PM low 33.10 | 1.1% | $29.6B | -6.63% |
| AU | 79.48 | 79.09 | -0.49% | 79.09–80.85 | prior close 79.48 | below PM low 79.09 | 1.5% | $40.1B | -6.13% |
| PAAS | 33.66 | 33.41 | -0.74% | 33.39–33.90 | prior close 33.66 | below PM low 33.39 | 1.9% | $13.9B | -5.61% |
| EXK | 6.56 | 6.49 | -1.05% | 6.45–6.60 | prior close 6.56 | below PM low 6.45 | 0.4% | $1.9B | -7.99% |
| GLD | 341.19 | 340.40 | -0.23% | 339.89–342.65 | prior close 341.19 | below PM low 339.89 | 3.2% | n/a | -3.20% |

Sources: Admiral Markets 2026-11-19 (Reuters spot gold $3,693.13 low); CNBC TV18 2026-11-19; Economies.com 2026-11-19 08:05 UTC; azcentral 2026-11-19 07:00 ET; <https://admiralmarkets.com/analytics/traders-blog/why-is-gold-falling-november-2026>

### C6 — Financing, sell-the-news and a launch week

Three separate mechanics, one section. **SLS -20.61%** is dilution: SELLAS priced 11,538,462 shares at $13.00, a 27.6% discount to Wednesday's $17.95 close, for $150.0m gross with a 1,730,769-share option for J.P. Morgan and TD Cowen and an expected close on 2026-11-20 — the Phase 3 REGAL result that drove the +156% on Tuesday is intact, the share count is what changed. **WSM -8.49%** is a sell-the-news on a good print: a 5.1% comparable, GAAP EPS of $2.38 and non-GAAP $2.19 with the FY2026 outlook reiterated, and the stock traded up to $275.15 pre-market — above its own $260.09 close — before round-tripping the entire move. **TTWO -2.02%** is GTA VI: the release is today with near-perfect reviews and strong preorder estimates, and the shares already gave back 6.22% on Wednesday. **WMT -1.02%** is the opposite case, a beat-and-raise that the market sold in a $1.01 trillion company.

| Ticker | Prior close ($) | Pre-market last ($) | Gap % | PM range ($) | Key level | Invalidation | %ADV | Mkt cap | Prior session chg % |
|---|---|---|---|---|---|---|---|---|---|
| SLS | 17.95 | 14.25 | -20.61% | 13.35–15.69 | $13.00 offering price (GlobeNewswire pricing release, 2026-11-18) | below $13.00 offering price | 38.4% | $3.7B | -6.27% |
| WSM | 260.09 | 238.00 | -8.49% | 232.00–275.15 | prior close 260.09 | below PM low 232.00 | 1.4% | $30.6B | +4.02% |
| WMT | 127.36 | 126.06 | -1.02% | 124.65–129.73 | prior close 127.36 | below PM low 124.65 | 6.6% | $1,010.4B | -0.13% |
| TTWO | 216.61 | 212.23 | -2.02% | 205.73–220.99 | prior close 216.61 | below PM low 205.73 | 6.6% | $40.6B | +6.22% |

Sources: GlobeNewswire 2026-11-18 (SELLAS pricing); Business Wire 2026-11-19 08:00 ET (Williams-Sonoma); StockTwits 2026-11-19 08:13 ET; Invezz 2026-11-19; <https://www.globenewswire.com/news-release/2026/11/19/3406277/0/en/sellas-life-sciences-announces-pricing-of-150-0-million-underwritten-public-offering.html>; <https://www.businesswire.com/news/home/20261119434480/en/Williams-Sonoma-Inc.-announces-strong-third-quarter-2026-results>

## 3. Pre-market gaps — top 25 market-wide

From the gainer screen (`premarket_*` columns only), Gate A (liquidity) and Gate B ($100m quality floor) applied to the reconciled market cap. Every name carries its levels. %ADV is the pre-market print against the 30-day average daily volume — under 5% is a thin book, not a market.

| Ticker | Prior close ($) | Pre-market last ($) | Gap % | PM range ($) | Key level | Invalidation | %ADV | Mkt cap | Prior session chg % |
|---|---|---|---|---|---|---|---|---|---|
| SLNH | 0.3880 | 0.4357 | +12.29% | 0.3969–0.4396 | prior close 0.3880 | back to/below prior close 0.3880 | 2.3% | $100M | -4.79% |
| UMAC | 9.61 | 10.58 | +10.09% | 9.65–10.70 | prior close 9.61 | back to/below prior close 9.61 | 2.8% | $499M | -4.28% |
| PANW | 339.92 | 373.96 | +10.01% | 369.08–376.75 | prior close 339.92 | back to/below prior close 339.92 | 2.5% | $278.3B | +9.90% |
| SHAZ | 21.99 | 24.10 | +9.60% | 22.95–24.10 | prior close 21.99 | back to/below prior close 21.99 | 1.1% | $846M | -2.66% |
| ASTS | 25.49 | 27.85 | +9.26% | 26.35–28.10 | prior close 25.49 | back to/below prior close 25.49 | 2.8% | $9.9B | -7.61% |
| COHR | 212.84 | 230.40 | +8.25% | 219.65–231.39 | prior close 212.84 | back to/below prior close 212.84 | 2.7% | $41.9B | +0.94% |
| PL | 12.05 | 12.99 | +7.80% | 12.33–13.11 | prior close 12.05 | back to/below prior close 12.05 | 1.9% | $4.4B | -3.52% |
| EROC | 7.35 | 7.87 | +7.07% | 7.60–7.94 | prior close 7.35 | back to/below prior close 7.35 | 0.4% | $1.6B | -2.78% |
| BE | 170.98 | 182.74 | +6.88% | 177.01–185.66 | prior close 170.98 | back to/below prior close 170.98 | 3.2% | $50.6B | -1.43% |
| P | 100.74 | 107.57 | +6.78% | 102.00–108.50 | prior close 100.74 | back to/below prior close 100.74 | 0.8% | $33.6B | -1.03% |
| FWDI | 4.01 | 4.28 | +6.73% | 4.06–4.28 | prior close 4.01 | back to/below prior close 4.01 | 1.1% | $306M | -2.43% |
| DDD | 1.38 | 1.47 | +6.52% | 1.45–1.50 | prior close 1.38 | back to/below prior close 1.38 | 0.4% | $230M | +0.00% |
| DGXX | 2.14 | 2.28 | +6.44% | 2.19–2.28 | prior close 2.14 | back to/below prior close 2.14 | 3.6% | $217M | +4.90% |
| HUT | 57.19 | 60.80 | +6.31% | 58.69–61.34 | prior close 57.19 | back to/below prior close 57.19 | 0.4% | $6.9B | +5.97% |
| CYPH | 1.75 | 1.86 | +6.29% | 1.79–1.96 | prior close 1.75 | back to/below prior close 1.75 | 2.6% | $261M | -8.14% |
| CRWD | 237.03 | 251.63 | +6.16% | 250.50–253.79 | prior close 237.03 | back to/below prior close 237.03 | 0.9% | $242.7B | +7.95% |
| NBIS | 106.96 | 113.54 | +6.15% | 110.96–114.65 | prior close 106.96 | back to/below prior close 106.96 | 3.2% | $31.3B | +0.87% |
| CIFR | 6.57 | 6.96 | +5.94% | 6.78–7.05 | prior close 6.57 | back to/below prior close 6.57 | 0.8% | $3.0B | +2.34% |
| RIOT | 18.24 | 19.32 | +5.92% | 18.61–19.50 | prior close 18.24 | back to/below prior close 18.24 | 2.9% | $6.8B | +6.98% |
| RBRK | 110.00 | 116.50 | +5.91% | 113.00–117.00 | prior close 110.00 | back to/below prior close 110.00 | 1.0% | $22.8B | +9.26% |
| APLD | 14.45 | 15.30 | +5.88% | 14.97–15.45 | prior close 14.45 | back to/below prior close 14.45 | 1.2% | $4.4B | +1.62% |
| STX | 515.90 | 546.20 | +5.87% | 532.00–550.94 | prior close 515.90 | back to/below prior close 515.90 | 0.6% | $118.4B | +2.28% |
| WULF | 12.00 | 12.70 | +5.80% | 12.41–12.70 | prior close 12.00 | back to/below prior close 12.00 | 1.2% | $6.0B | +2.83% |
| BHVN | 12.90 | 13.64 | +5.74% | 12.85–14.00 | prior close 12.90 | back to/below prior close 12.90 | 0.6% | $1.9B | -2.57% |
| BRUN | 4.54 | 4.80 | +5.73% | 4.57–4.89 | prior close 4.54 | back to/below prior close 4.54 | 0.6% | $381M | -2.99% |

### Thin tape — Gate A pass, Gate B fail (cap under $100m)

Real moves, not liquid ones: these names print, but the book and the cap do not qualify them for the headline table.

| Ticker | Prior close ($) | Pre-market last ($) | Gap % | PM range ($) | Key level | Invalidation | %ADV | Mkt cap | Prior session chg % |
|---|---|---|---|---|---|---|---|---|---|
| SEAT | 1.28 | 2.03 | +58.48% | 1.10–2.80 | prior close 1.28 | back to/below prior close 1.28 | 24473.2% | $15M | +2.40% |
| VIVS | 0.1200 | 0.1748 | +45.67% | 0.1183–0.2044 | prior close 0.1200 | back to/below prior close 0.1200 | 4969.4% | $2M | -0.08% |
| LGHL | 0.8601 | 1.23 | +43.01% | 0.9002–2.28 | prior close 0.8601 | back to/below prior close 0.8601 | 3469.5% | $39,688 | -20.36% |
| INHD | 2.30 | 3.20 | +39.08% | 2.90–4.40 | prior close 2.30 | back to/below prior close 2.30 | 993.3% | $6M | -2.13% |
| GMM | 1.55 | 2.02 | +30.32% | 1.76–2.22 | prior close 1.55 | back to/below prior close 1.55 | 220.7% | $13M | +11.51% |
| GNLN | 0.6010 | 0.7410 | +23.29% | 0.6866–1.25 | prior close 0.6010 | back to/below prior close 0.6010 | 134829.4% | $417,421 | -12.81% |
| GMEX | 0.3059 | 0.3515 | +14.91% | 0.2805–0.6000 | prior close 0.3059 | back to/below prior close 0.3059 | 3265.1% | $480,453 | -15.38% |
| LASE | 0.3923 | 0.4500 | +14.70% | 0.4000–0.4600 | prior close 0.3923 | back to/below prior close 0.3923 | 47.0% | $24M | -8.10% |
| SPRC | 0.2701 | 0.3080 | +14.03% | 0.2900–0.8000 | prior close 0.2701 | back to/below prior close 0.2701 | 1661.0% | $665,377 | -18.08% |
| INLF | 0.2273 | 0.2586 | +13.77% | 0.2420–0.2936 | prior close 0.2273 | back to/below prior close 0.2273 | 19.2% | $346,700 | -36.81% |
| MRKR | 0.8532 | 0.9668 | +13.31% | 0.8740–1.01 | prior close 0.8532 | back to/below prior close 0.8532 | 206.8% | $14M | +1.98% |
| NCPL | 2.89 | 3.20 | +10.73% | 2.98–3.43 | prior close 2.89 | back to/below prior close 2.89 | 3.8% | $23M | +21.94% |

### Yesterday's tape — the prior session (2026-11-18, settled)

The prior session's own biggest movers in the whole screen, with where they sit in this morning's pre-market. `Prior session chg %` is the settled move; the other columns are this morning's pre-market tape.

| Ticker | Prior close ($) | Pre-market last ($) | Gap % | PM range ($) | Key level | Invalidation | %ADV | Mkt cap | Prior session chg % |
|---|---|---|---|---|---|---|---|---|---|
| SVRE | 0.8647 | 0.8099 | -6.34% | 0.7450–0.9600 | prior close 0.8647 | below PM low 0.7450 | 29.0% | $2M | +111.01% |
| AKAN | 4.03 | 3.73 | -7.56% | 3.58–4.13 | prior close 4.03 | below PM low 3.58 | 8.3% | $11M | +96.59% |
| SKYA | 4.13 | 4.09 | -0.97% | 3.85–4.35 | prior close 4.13 | below PM low 3.85 | 4.7% | $210M | +90.32% |
| CHSN | 0.1020 | 0.0890 | -12.75% | 0.0815–0.1011 | prior close 0.1020 | below PM low 0.0815 | 53.2% | $236,884 | -78.30% |
| CUE | 4.76 | 4.62 | -2.92% | 4.55–5.00 | prior close 4.76 | below PM low 4.55 | 25.3% | $40M | +68.20% |
| VWAV | 0.7808 | 0.7192 | -7.89% | 0.6500–0.7200 | prior close 0.7808 | below PM low 0.6500 | 14.5% | $3M | +57.07% |
| GDHG | 0.1548 | 0.1318 | -14.86% | 0.1254–0.1450 | prior close 0.1548 | below PM low 0.1254 | 33.9% | $9M | -46.84% |
| CLRO | 6.90 | 6.88 | -0.29% | 6.42–7.20 | prior close 6.90 | below PM low 6.42 | 1.2% | $18M | +46.19% |
| AZI | 1.04 | 0.7009 | -32.61% | 0.6800–0.9767 | prior close 1.04 | below PM low 0.6800 | 29.5% | $69M | +42.45% |
| HY | 15.44 | 15.98 | +3.52% | 15.42–16.14 | prior close 15.44 | back to/below prior close 15.44 | 1.1% | $277M | -41.07% |
| JMIA | 2.74 | 2.82 | +2.92% | 2.77–2.85 | prior close 2.74 | back to/below prior close 2.74 | 5.0% | $341M | -40.82% |
| STEM | 0.7424 | 0.7679 | +3.43% | 0.7500–0.7992 | prior close 0.7424 | back to/below prior close 0.7424 | 12.2% | $7M | -38.13% |

### Tail — the names the gates and the table cap left out

Ranked by absolute gap, not by gap. Cohorts: `gate-fail` = failed Gate A or Gate B; `flat-print` = printed with a gap inside 3%; `unranked` = cleared both gates but did not make the top-25 table. This tier is a watchlist, not a second set of setups.

| Ticker | Prior close ($) | Pre-market last ($) | Gap % | PM range ($) | Key level | Invalidation | %ADV | Mkt cap | Prior session chg % | Cohort |
|---|---|---|---|---|---|---|---|---|---|---|
| SOS | 4.29 | 0.1900 | -95.57% | 0.1900–0.2690 | prior close 4.29 | below PM low 0.1900 | 33.1% | $28M | +1.80% | gate-fail |
| FCHL | 0.5651 | 0.2472 | -56.26% | 0.2412–0.3903 | prior close 0.5651 | below PM low 0.2412 | 49.8% | $756,156 | -14.12% | gate-fail |
| BOXL | 1.91 | 1.28 | -32.81% | 1.05–1.85 | prior close 1.91 | below PM low 1.05 | 165.4% | $1M | +4.96% | gate-fail |
| NIKI | 1.60 | 1.21 | -24.38% | 1.21–1.54 | prior close 1.60 | below PM low 1.21 | 4.1% | $5M | +6.67% | gate-fail |
| EJH | 1.10 | 1.35 | +22.73% | 1.35–1.35 | prior close 1.10 | back to/below prior close 1.10 | 0.7% | $83M | +0.00% | gate-fail |
| JDZG | 0.1200 | 0.0950 | -20.83% | 0.0797–0.1200 | prior close 0.1200 | below PM low 0.0797 | 11.3% | $717,781 | -10.38% | gate-fail |
| INVZ | 0.1447 | 0.1155 | -20.18% | 0.1099–0.1299 | prior close 0.1447 | below PM low 0.1099 | 11.3% | $43M | +0.84% | gate-fail |
| XCH | 3.34 | 4.00 | +19.76% | 4.00–4.00 | prior close 3.34 | back to/below prior close 3.34 | 0.1% | $15M | -0.60% | gate-fail |
| CYAB | 0.0841 | 0.0678 | -19.38% | 0.0670–0.0857 | prior close 0.0841 | below PM low 0.0670 | 4.1% | $1M | -15.73% | gate-fail |
| CDT | 0.3430 | 0.2790 | -18.66% | 0.2414–0.4065 | prior close 0.3430 | below PM low 0.2414 | 81.3% | $19,285 | -4.72% | gate-fail |
| CSAI | 0.7419 | 0.6166 | -16.89% | 0.5838–0.6385 | prior close 0.7419 | below PM low 0.5838 | 6.3% | $643,577 | -23.76% | gate-fail |
| RYET | 0.5288 | 0.4448 | -15.88% | 0.4448–0.5000 | prior close 0.5288 | below PM low 0.4448 | 1.8% | $21M | +1.68% | gate-fail |
| ZOAR | 6.39 | 5.40 | -15.49% | 5.23–5.50 | prior close 6.39 | below PM low 5.23 | n/a | $55M |  | gate-fail |
| RRGB | 7.95 | 6.75 | -15.09% | 6.40–6.77 | prior close 7.95 | below PM low 6.40 | 11.1% | $150M | -2.57% | gate-fail |
| FCDH | 2.47 | 2.10 | -14.97% | 2.10–2.13 | prior close 2.47 | below PM low 2.10 | 1.0% | $2M | -3.52% | gate-fail |
| MODD | 1.82 | 1.56 | -14.29% | 1.56–1.56 | prior close 1.82 | below PM low 1.56 | 0.8% | $18M | +1.11% | gate-fail |
| ZNB | 0.4600 | 0.3953 | -14.07% | 0.3668–0.4398 | prior close 0.4600 | below PM low 0.3668 | 10.7% | $2M | -24.70% | gate-fail |
| FXHO | 4.90 | 5.56 | +13.47% | 5.56–5.56 | prior close 4.90 | back to/below prior close 4.90 | 0.3% | $129M | -2.10% | gate-fail |
| SRTM | 0.1293 | 0.1119 | -13.46% | 0.1105–0.1352 | prior close 0.1293 | below PM low 0.1105 | 5.2% | $71,499 | +3.44% | gate-fail |
| AVX | 3.30 | 3.73 | +12.90% | 3.73–3.84 | prior close 3.30 | back to/below prior close 3.30 | 0.3% | $31M | -8.84% | gate-fail |
| HOVR | 1.17 | 1.32 | +12.82% | 1.32–1.32 | prior close 1.17 | back to/below prior close 1.17 | 0.0% | $79M | -0.43% | gate-fail |
| OLOX | 0.6748 | 0.5900 | -12.57% | 0.5836–0.6500 | prior close 0.6748 | below PM low 0.5836 | 1.5% | $1M | +19.14% | gate-fail |
| SCLX | 0.6273 | 0.7059 | +12.53% | 0.5598–0.7059 | prior close 0.6273 | back to/below prior close 0.6273 | 1.2% | $4M | -2.29% | gate-fail |
| LICN | 0.0155 | 0.0136 | -12.26% | 0.0130–0.0170 | prior close 0.0155 | below PM low 0.0130 | 77.9% | $253,066 | -29.55% | gate-fail |

Two rows in this tier are corporate-action artefacts rather than catalysts and are published as moves with no story: **SOS -95.57%** and **FCHL -56.26%** are sub-$30m shells whose gaps are the size of a reverse split, and no filing or press release for either was sourced in this run. Nothing in this tier is published as a setup.

## 4. Top losers — top 10 market-wide

From the loser screen (`premarket_*` columns only), same gates. Eight names clear both gates on the loser screen; the other 180 decliners carry their move in the tail tier above, where they are ranked by absolute gap. The invalidation on a gap-down is below the pre-market low, except where the catalyst publishes the level that decides it.

| Ticker | Prior close ($) | Pre-market last ($) | Gap % | PM range ($) | Key level | Invalidation | %ADV | Mkt cap | Prior session chg % |
|---|---|---|---|---|---|---|---|---|---|
| SLS | 17.95 | 14.25 | -20.61% | 13.35–15.69 | $13.00 offering price (GlobeNewswire pricing release, 2026-11-18) | below $13.00 offering price | 38.4% | $3.7B | -6.27% |
| SA | 25.55 | 23.05 | -9.78% | 23.05–25.63 | prior close 25.55 | below PM low 23.05 | 12.5% | $2.8B | -2.78% |
| WSM | 260.09 | 238.00 | -8.49% | 232.00–275.15 | prior close 260.09 | below PM low 232.00 | 1.4% | $30.6B | +4.02% |
| MANU | 21.90 | 20.25 | -7.53% | 19.00–21.01 | prior close 21.90 | below PM low 19.00 | 4.6% | $3.8B | +1.01% |
| NTES | 118.43 | 111.33 | -6.00% | 110.00–114.20 | prior close 118.43 | below PM low 110.00 | 7.5% | $76.4B | -0.99% |
| MNSO | 11.70 | 11.02 | -5.81% | 11.00–11.24 | prior close 11.70 | below PM low 11.00 | 0.8% | $3.6B | -3.94% |
| VZLA | 2.98 | 2.85 | -4.36% | 2.84–3.01 | prior close 2.98 | below PM low 2.84 | 2.4% | $1.1B | +0.34% |
| BBWI | 18.66 | 18.10 | -3.00% | 16.90–19.00 | prior close 18.66 | below PM low 16.90 | 4.7% | $3.8B | +1.41% |

**MANU -7.53%** is the one loser here with no sourced catalyst in this run — it carries a move and no story. **SA -9.78%** is the other: the metal is only about 1% lower, so the move is idiosyncratic and unexplained here.

## 5. StockTwits lead read

The trending list is a lead indicator, not a sidebar: every name below was priced against the same pull. Theses are the platform's own trend summaries, truncated.

| Ticker | Score | Pre-market and thesis |
|---|---|---|
| BABA | 1 | 83.33 (-1.23%) — Alibabas quarterly results are driving attention: traders are weighing strong revenue, AI-cloud growth and improved e-commerce profitability against an earnings miss, heavier AI infrastructure spending and weaker free cash flow. Bulls call the shares undervalued and focus on clou… |
| WMT | 2 | 126.06 (-1.02%) — Walmarts quarterly earnings beat expectations and management raised its full-year outlook, with strong e-commerce growth drawing praise. The muted share reaction reflects debate over its rich valuation and softer U.S. comparable-sales growth, despite the upbeat guidance. |
| TTWO | 3 | 212.23 (-2.02%) — GTA VIs launch is driving attention, with near-perfect reviews and estimates of strong demand fueling bullish interest in Take-Twos sales and future online and PC opportunities. Traders are divided over whether the excitement is already priced in, with some calling the stock acti… |
| PANW | 4 | 373.96 (+10.01%) — Palo Alto Networks better-than-expected quarterly results and raised outlook are driving attention, alongside its planned Applied Compute acquisition to expand enterprise AI security. Bulls point to strong cybersecurity demand and AI-related opportunities, while skeptics question… |
| BIDU | 5 | 68.86 (-0.51%) — Baidus post-earnings slide to multiyear lows is the dominant focus, as traders weigh weak advertising and declining overall revenue against rapid AI-cloud growth; an analyst price-target cut has added to the pressure. The community is split between buyers calling the shares overs… |
| PDD | 6 | 81.71 (+5.50%) — PDD is drawing attention after quarterly results showed stronger-than-expected profit and lower marketing costs, despite flat, below-estimate revenue. Traders are split between viewing cost control and strong cash generation as evidence of resilience and seeing slowing sales as a… |
| KWEB | 7 | 21.57 (-0.64%) — KWEB is drawing attention amid a broad selloff in Chinese internet stocks, with traders pointing to weak domestic demand, limited stimulus and persistent outflows as reasons for the sectors underperformance. Some see the funds steep decline as an oversold buying opportunity, whil… |
| CAPR | 8 | 8.03 (+0.00%) — Attention centers on the FDAs Nov. 22 PDUFA decision on deramiocel for Duchenne muscular dystrophy, with discussion focused on the narrowed upper-limb indication and HOPE-3 data. Many traders expect approval, while others cite regulatory and efficacy concerns and warn of a possib… |
| P | 9 | 107.57 (+6.78%) — Everpures quarterly results beat expectations and its FY27 revenue outlook was raised, with traders pointing to strong product sales and AI/hyperscaler demand. The bullish reaction is tempered by concern over falling gross margins and price cuts, alongside debate over whether the… |
| SHIB.X | 10 | not a US-listed equity — no pre-market print on the US screen |
| FSLY | 11 | 18.51 (+3.41%) — Fastly and Comcast are extending their content-delivery model to gaming, using Comcasts distributed network to bring large game files closer to customers and reduce latency. Traders are reacting positively to the partnerships potential, while questioning whether wider adoption wi… |
| ASTS | 12 | 27.85 (+9.26%) — no thesis text published |
| CAVA | 13 | 52.30 (-0.86%) — no thesis text published |
| CHFJPY | 14 | not a US-listed equity — no pre-market print on the US screen |
| ABVX | 15 | 84.50 (+0.80%) — no thesis text published |

Two names on the list are worth pulling out of the social feed and into the tape: **PANW +10.01%** is on the list at rank 4 with a thesis that matches the printed move, and **CAPR 0.00%** at rank 8 has a scheduled binary in it — the FDA's 2026-11-22 PDUFA decision on deramiocel — which is exactly why a flat pre-market is not the same as no event.

## 6. Watchlist

From `refs/watchlist.yaml` on the outputs repo (published file, fetched at run time). Sorted by absolute pre-market move.

| Ticker | Prior close ($) | Pre-market last ($) | Gap % | PM range ($) | Key level | Invalidation | %ADV | Mkt cap | Prior session chg % |
|---|---|---|---|---|---|---|---|---|---|
| GOOGL | 282.44 | 294.05 | +4.11% | 287.80–294.77 | prior close 282.44 | back to/below prior close 282.44 | 2.2% | $3,434.4B | +0.80% |
| AMZN | 267.74 | 273.87 | +2.29% | 272.10–274.69 | prior close 267.74 | back to/below prior close 267.74 | 1.6% | $2,895.1B | +3.82% |
| MSFT | 507.31 | 516.73 | +1.66% | 513.20–517.88 | prior close 507.31 | back to/below prior close 507.31 | 0.5% | $3,767.4B | -0.19% |
| NVDA | 150.96 | 153.17 | +1.46% | 152.45–154.80 | prior close 150.96 | back to/below prior close 150.96 | 3.3% | $3,638.1B | -2.89% |
| AAPL | 352.45 | 354.67 | +0.63% | 353.58–355.26 | prior close 352.45 | back to/below prior close 352.45 | 0.4% | $5,121.9B | +0.15% |
| IWM | 270.12 | 271.75 | +0.60% | 271.12–272.29 | prior close 270.12 | back to/below prior close 270.12 | 0.9% | n/a | +0.40% |
| TLT | 80.22 | 79.82 | -0.50% | 79.79–80.20 | prior close 80.22 | below PM low 79.79 | 2.0% | n/a | +0.84% |
| GLD | 341.19 | 340.40 | -0.23% | 339.89–342.65 | prior close 341.19 | below PM low 339.89 | 3.2% | n/a | -3.20% |

Two of the eight have a theme behind them: **GOOGL +4.11%** on the Anthropic read-through and **NVDA +1.46%** on Nvidia's own guide. The other six sit inside a 2.3% band with no company news of their own, which is the quietest the published list has been this month.

## 7. Overnight / futures / index / crypto

US cash levels are the settled 2026-11-18 session; futures, FX, commodities and crypto are live prints with their own timestamps.

| Instrument | Level | Change | As of |
|---|---|---|---|
| S&P 500 (SPY) | 730.2 | -0.31% | settled 2026-11-18 |
| Nasdaq 100 (QQQ) | 659.51 | +0.39% | settled 2026-11-18 |
| Russell 2000 (IWM) | 270.12 | +0.40% | settled 2026-11-18 |
| Dow (DIA) | 501.73 | -1.10% | settled 2026-11-18 |
| Gold ETF (GLD) | 341.19 | -3.20% | settled 2026-11-18 |
| 20+yr Treasury (TLT) | 80.22 | +0.84% | settled 2026-11-18 |
| S&P 500 futures (ES=F) | 7427.5 | +1.19% | 13:25 UTC |
| Nasdaq 100 futures (NQ=F) | 27745 | +2.05% | 13:25 UTC |
| Dow futures (YM=F) | 50583 | +0.62% | 13:25 UTC |
| Russell 2000 futures (RTY=F) | 2738.8 | +0.62% | 13:25 UTC |
| 10-year Treasury (^TNX) | 5.066 | +0.00% | 13:35 UTC |
| Dollar index (DXY) | 103.725 | -0.13% | 13:35 UTC |
| WTI crude (CL=F) | 83.17 | +1.04% | 13:35 UTC |
| Gold (GC=F) | 3716.1 | -0.69% | 13:35 UTC |
| Bitcoin (BTC-USD) | 63630.99 | +1.02% | 13:35 UTC |
| Nikkei 225 (^N225) | 59444.21 | +0.71% | 13:35 UTC |
| Hang Seng (^HSI) | 22841.62 | -2.84% | 13:35 UTC |
| Shanghai Composite | 3577.617 | -0.19% | 13:35 UTC |
| FTSE 100 (^FTSE) | 10504.55 | -0.44% | 13:35 UTC |
| DAX (^GDAXI) | 25706.52 | -0.12% | 13:35 UTC |
| S&P 500 (^GSPC) | 7323.63 | -0.23% | 13:35 UTC |

The cash tape fell on Wednesday — the S&P 500 -0.23% and the Dow -1.11% — and futures are recovering hard on Anthropic's pricing: Nasdaq 100 futures +2.05% against S&P 500 futures +1.19%, so the recovery is concentrated in the AI complex rather than the index. The rate complex is the counterweight: the 10-year is flat at 5.066 and the dollar index is little changed at 103.725, while gold sits at a 14-month low and bitcoin has bounced off $62,000 twice in four days.

## 8. Macro calendar

- **Initial jobless claims and the Philadelphia Fed manufacturing survey — both due at 08:30 ET, and neither actual is published here.** The Department of Labor's release PDF for 19 November was not yet posted at `oui.doleta.gov` at the time of this pull (the 12 November release is the newest there), and the Philadelphia Fed's survey page renders empty for a non-browser client. A consensus of 198,000 claims is carried by a calendar aggregator and is labelled as a consensus, not an actual.
- **No Empire State and no payrolls print today.** The New York Fed's own release page still carries the Empire State general business conditions index at **7.8** for the survey released on 2026-11-16 — read from the Fed's page at 08:35 ET, not from a calendar — and the Empire State publishes around the 15th, so there is no release this morning. The BLS keyless tier's newest observation is the October 2026 employment report (nonfarm payrolls +165,000, unemployment rate 4.1%).
- **The Fed's October minutes were released Wednesday at 14:00 ET**, and they are the event behind the rate trade in this tape: Governor Waller outlined 50bp in December or 25bp in December and January, which is what took spot gold to $3,693.13 — a 14-month low.
- No US CPI release is scheduled today. The next scheduled inflation print is the CPI.

## 9. Earnings today

Roster taken from cron #19's published file `earnings/2026-11-19-reminders.md` (06:00 ET), cross-checked against the scanner's own earnings calendar and against each issuer's release.

| Ticker | Company | Release | EPS est | Mkt cap | Status |
|---|---|---|---|---|---|
| WMT | Walmart Inc. | BMO 7:00 ET | $0.64 | $1,010.4B | beat and raise |
| PDD | PDD Holdings Inc. | BMO 6:30 ET | $2.78 | $110.2B | beat on EPS, revenue miss |
| WSM | Williams-Sonoma, Inc. | BMO 8:00 ET | $2.18 | $30.6B | beat; stock sold |
| BABA | Alibaba Group (9988.HK) | reported 05:02 ET | — | $209.9B | revenue beat, adjusted EPS miss |
| NTES | NetEase, Inc. (9999.HK) | reported 03:30 ET | — | $76.4B | miss on both |
| KEYS | Keysight Technologies Inc. | AMC 4:05 PM ET | $3.36 | $48.7B | pending |
| INTU | Intuit Inc. | AMC 4:00 PM ET | $2.47 | $83.7B | pending |
| ROST | Ross Stores, Inc. | AMC 4:00 PM ET | $1.85 | $72.7B | pending |

Three US reporters were already in the tape when this pull ran, and the split is the story: PDD and WMT beat and were bought (or held), Williams-Sonoma beat and was sold — it traded up to $275.15 pre-market before round-tripping to $238.00. Two Hong Kong issuers had already printed overnight, Alibaba at 05:02 ET and NetEase at 03:30 ET, both of them lower on the ADR. Still ahead: Keysight, Intuit and Ross Stores after the close, and Keysight carries the highest reaction score on the roster (9.76) against a 9.41% implied move — the number to watch if this afternoon's read-through on the AI complex survives the open.

## 10. Source health

| Source | Status | Role |
|---|---|---|
| TradingView america scanner | ok | the whole screen — band, tail, watchlist and targeted pull, one call, 514 gainers / 188 decliners / 400 tail rows of a 2,714 cohort |
| MCP-bridge market-recap `get_quotes` | ok | prior-close and market-cap cross-check on 10 names (WSM, SA, TTWO, PANW, PDD, BABA, COHR, BE, CRWD, STX) — the bridge agreed with the scanner's prior close on all ten |
| MCP-bridge market-recap `market_snapshot` | ok | overnight futures, indices, FX, commodities and crypto |
| MCP-bridge stocktwits `trending_symbols` | ok | the 15-name trending list and its own thesis summaries |
| Cron #19 `earnings/2026-11-19-reminders.md` | ok | the earnings roster, BMO/AMC split and per-name estimates |
| Cron #15 `earnings/2026-11-19-reactions.md` | ok | read as a cross-check on the pre-market gap table; this brief screens the whole market and takes the broader screen |
| `refs/watchlist.yaml` | ok | the published 8-name watchlist |
| `macro_actual.py` (Empire State) | partial | the Fed's page carries the 2026-11-16 release at 7.8; there is no release today |
| `macro_actual.py --release bls` | not_yet_posted | the BLS API's newest payroll observation is 2026-10 |
| DOL weekly claims release (primary) | unavailable | `oui.doleta.gov/press/2026/111926.pdf` is not posted yet; the 12 November release is the newest there |
| Philadelphia Fed manufacturing survey (primary) | unavailable | the survey page returns an empty shell for a non-browser client |
| Yahoo chart API | not used | the scanner carried every price the brief publishes |

**Market caps that had to be rebuilt.** The sweep flagged 90 of 914 screened names for a cap disagreement above 15%, and five of them were rebuilt rather than taken, because the share count they carry sits on the ordinary-share basis against an ADS-priced quote:

| Ticker | Name | Scanner cap | Published cap | Source that won |
|---|---|---|---|---|
| SVRE | SaverOne 2014 Ltd. | $329,054,092 | $1,975,120 | median implied shares x close — the stockanalysis count was rejected as an ordinary-share basis |
| NIVF | NewGenIvf Group Limited | $210,872 | $210,872 | median implied shares x close — the stockanalysis count was rejected as an ordinary-share basis |
| FGL | Founder Group Limited | $47,760 | $47,760 | median implied shares x close — the stockanalysis count was rejected as an ordinary-share basis |
| ADXN | Addex Therapeutics Ltd | $3,684,889 | $3,684,889 | median implied shares x close — the stockanalysis count was rejected as an ordinary-share basis |
| PPBT | Purple Biotech Ltd. | $9,878,262 | $3,714,440 | median implied shares x close — the stockanalysis count was rejected as an ordinary-share basis |

The 90 flagged names were resolved against Nasdaq's `/summary` (907 of 909 resolved), shibui's dated valuation rows and a direct share count, and the published cap is always shares x close so it sits on the gate's own basis. A close-versus-gap reconciliation sweep over all 914 screened rows flagged zero rows — every published gap reconciles with its prior close.

## 11. Open research queue

1. **Anthropic's debut is the day's event and it lands during the session.** The brief's whole AI cluster is priced on an IPO that has not traded yet; if ANT opens below $83 the cluster's gaps are the first thing to give back, and there is no screen in this brief that can price that.
2. **SA -9.78% is unexplained.** The metals complex is about 1% lower and Seabridge is at its pre-market low. Nothing was sourced — an offering, a ratio change or a corporate action is the usual answer and none was found in this run.
3. **The 180 gate-failing decliners are a floor, not a list.** The loser screen's 188 rows are complete, but the tail cohort came back at 400 rows against a totalCount of 2,714, so the tail tier's ordering is a floor on the day's extremes and not the whole set.
4. **Today's 08:30 ET prints were not readable from their primary sources.** The claims release and the Philadelphia Fed survey are both missing at the time of the pull, and both should be in tomorrow's brief as facts rather than as a schedule.
5. **MANU -7.53% is a move with no story**, and it is on the winner's screen at a $3.8bn cap with a real book. A name that size does not move 7.5% on nothing; the search that would explain it did not run in this brief.

