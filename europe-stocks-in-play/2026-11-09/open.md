---
date: 2026-11-09
market: europe
slot: open
producer: grok-bot/europe-stocks-in-play
contract: intl-stocks-in-play-v1
source: Grok Bot box digest (Fundamental europe stocks-in-play routine)
generated_at: 2026-11-09T20:00:00+07:00
status: degraded
---

Provenance: Fundamental digest at /home/box/europe-in-play/2026-11-09-open.md; built at 2026-11-09T20:00:00+07:00; covered session open.

**Deviations:** digest reports a skipped section; 2 box-local path references un-backticked

# Europe stocks in play — 2026-11-09 (Mon) — open

**Run:** ~08:36–09:05 London (15:36–16:05 Asia/Bangkok). LSE, Xetra, Euronext, GPW, SIX, Nasdaq Nordic, Oslo, Borsa Italiana all open (no holiday).
**Sort:** tier (A → Soft-A → TECH_WATCH → B → C), then EUR session turnover desc. Price, chg%, gap, € turnover and RVol from TradingView Local `get_symbol_data_batch` (2 calls, 76/76 resolved, ~08:45 London). RVol = TV `relative_volume_10d_calc`, **not time-of-day adjusted** (~45 min / ~9% of session elapsed). € via Frankfurter ECB 2026-11-06 (GBP 0.83415, PLN 4.3925, CHF 0.9143, DKK 7.4752, NOK 10.526, SEK 11.026).
**Important data note:** TV HTML movers pages served **Friday-close rows for many non-UK names** this pass (e.g. DNP −6.2%, OUT1V −15.7%, KESKOA −16.2%, MDV +5.3%, BILN −19% in HTML vs flat-ish live). All tier figures below are from the live TV batch, not HTML.
**Market colour:** DAX 25,955 +1.12% (onvista ticker bar ~08:40 London); FTSE MIB 50,560 +1.01%, FTSE 100 10,710 +0.34%, DAX 25,919 +0.38% at 09:20 CET (Teleborsa header). Poland WIG +0.54%, WIG20 +0.80% (Stooq, 09:21/09:37 CET).
**Themes:** Italian bank M&A Monday — **Crédit Agricole proposes a Banco BPM tie-up** (BAMI +11%, €70M) and **UniCredit Q3 / €4.5B dividend** (UCG +5.4%, €157M). **ACS denies Hochtief bid report** (HOT −4.8%, gap −6.4%). **Svea Bank cash offer for Qliro** at SEK 23.50 (QLIRO +79.5%). UK: Kainos interims sold (−9%) despite +37% revenue. Swiss semis soft (COMET, INFICON).

## Tier A
| Ticker | Venue | Price | Chg% | Gap% | €vt | RVol | Why |
|---|---|---|---|---|---|---|---|
| BAMI | Borsa Italiana | €14.94 | +11.12 | +9.97 | €69.9M | 1.03 | Crédit Agricole proposes to Banco BPM to "create together a new leading Italian bank" (Crédit Agricole release, Euronext 07:00 CET; DJ/Reuters/WSJ). RVol 1.03 unadjusted at ~9% of session = full-day average volume already traded. mcap €21.0B |

## Soft-A
| Ticker | Venue | Price | Chg% | Gap% | €vt | RVol | Why |
|---|---|---|---|---|---|---|---|
| UCG | Borsa Italiana | €80.94 | +5.39 | +3.65 | €157.2M | 0.44 | 3Q26/9M26 results (ESPI 78/2026 07:56 Warsaw, dual-listed) + interim dividend approval; TV key facts: profit **+23.9%**, **€4.5B** dividend, Commerzbank merger push. DJ market talk: forecasts set for upgrades |
| HOT | Xetra | €348.2 | −4.76 | −6.40 | €6.0M | 0.25 | **ACS denies Hochtief bid report** (onvista/dpa-AFX headline) — unwinds last week's takeover-report jump (TV weekly recap). Gap meets trigger |
| KNOS | LSE | 1119p | −9.00 | −2.44 | €1.8M | 0.60 | COMPANY_RNS Interim results: revenue **£268.8m (+37%)**, adj PBT **£41.7m (+30%)**, adj margin flat 16%, bookings £402.3m (+27%, methodology changed), cash £86.5m (−18% YoY). Sold on margin/cash |
| VLA | Euronext Paris | €2.648 | +5.84 | +5.92 | €790k | 0.84 | Positive **Phase 2** results for tetravalent Shigella vaccine candidate **S4V2** (Euronext 07:00 CET) |
| CICN | SIX | CHF143.0 | +8.01 | +3.32 | €617k | 0.37 | Cicor wins awards for **two major defence programmes**, expects close to **CHF 20M** revenue from them in 2027 (EQS / TV 06:00 London) |
| SRT | LSE (AIM) | 72p | +5.11 | +1.87 | €321k | 1.96 | COMPANY_RNS Final Results: five active sovereign customers + sixth contracted; pipeline grown to **£2.4bn** (12% of prior £1.8bn converted). RVol <2 → Soft-A |

## TECH_WATCH
| Ticker | Venue | Price | Chg% | Gap% | €vt | RVol | Why |
|---|---|---|---|---|---|---|---|
| PHARM | Euronext Amsterdam | €1.171 | +6.31 | +3.09 | €8.1M | 0.45 | Day-2 after Fri MHRA approval of Joenja for children (Fri 06:00 London) — no same-session catalyst. `TECH_WATCH` |
| AUTO | Oslo | NOK14.98 | +5.87 | +5.94 | €2.5M | 0.35 | Gap-up; last catalyst Thu Q3 (record orders, FY26 guide ~$750M). No same-session news. `TECH_WATCH` |
| COTN | SIX | CHF283.0 | −5.03 | −3.15 | €1.5M | 0.12 | Swiss semi-cap weakness; no fresh news (last: Oct Q3). `TECH_WATCH` |
| IFCN | SIX | CHF143.6 | −4.65 | −0.13 | €1.4M | 0.16 | Same semi-cap tape as COTN; no fresh news. `TECH_WATCH` |
| FIA1S | Helsinki | €5.265 | +5.85 | 0.00 | €1.2M | 0.83 | Follow-through after Fri October traffic (pax up YoY); no same-session catalyst. `TECH_WATCH` |
| MEGP | LSE | 107.2p | −4.96 | +0.18 | €909k | 0.48 | No RNS today; LSE ticker news (browser) newest company item 21 Oct (CFO leave) — none today. `TECH_WATCH` |
| ALCPB | Euronext Paris | €5.439 | −6.30 | −3.53 | €588k | 0.37 | Capital B (bitcoin treasury); no same-session filing. `TECH_WATCH` |
| KOO | LSE | 181.6p | −5.91 | +0.78 | €296k | 0.79 | No RNS; sub-midday-scale turnover → file only. `TECH_WATCH` |

## Tier B
| Ticker | Venue | Price | Chg% | €vt | Why |
|---|---|---|---|---|---|
| NXR | LSE | 294p | −4.85 | €609k | RVol 5.47; no same-session RNS and LSE ticker news newest 15 Oct — RVol ≥2 no catalyst → B |
| CBK | Xetra | €39.46 | +3.27 | €9.2M | Bank sympathy with UCG (Commerzbank merger push in UCG key facts); under day-move bar |
| NWL | Borsa Italiana | €25.20 | +4.30 | €1.2M | NewPrinces; no catalyst found; under 5% bar |
| CHEMM | Copenhagen | DKK735.5 | +4.18 | €2.1M | No catalyst; under 5% bar |
| GMAB | Copenhagen | DKK3646 | +3.37 | €5.5M | No catalyst; under bar |

## Tier C / halt watch
- **QLIRO** (Nasdaq Stockholm) — SEK22.80, **+79.53%**, gap +80.3%, €1.33M, RVol 10.0. **Svea Bank public cash offer SEK 23.50/share** (inside info 08:00 CET); Svea holds 3.48% + conditional deals for another 38.82%; Qliro board appointed advisers. Spread ~3% to offer. `BUYOUT_NEAR` **fresh — chat count 1/2**. (mcap €37M; clears on turnover floor.)
- **MTG** Meier Tobler (SIX) — CHF45.15 (0.00%), €988k. Ahlsell offer; `BUYOUT_NEAR` count stays **1/2** — file only, no new deal event.
- **CNE** Capricorn Energy (LSE) — DNO offer **lapsed** (RNS 07:00); 418.8p +0.2%, €2k turnover — illiquid reaction, file only.
- **AKVA** (Oslo) — 90% minimum acceptance satisfied on recommended offer; NOK159 +0.6% — file only.
- **BMPS** (file note, not quoted): Intesa Sanpaolo OPAS on MPS — Consob approved offer document, acceptance 24 Nov 2026 → 22 Jan 2027 (eMarket Storage, Sun 20:29).
- **TRAF** Trafalgar — suspension RNS 07:30 (sub-floor, file only).

## Near-misses (≥3% or catalyst but failed floor/move)
- **SEE** Seeing Machines — Q1 FY27 KPIs RNS; −11.9% (TV) / −16.9% (lse.co.uk, 72 trades), €252k — **fails £0.50 price floor** (3.3p).
- **DAT** DataWalk (GPW) — US patent ESPI (Fri 16:25); +4.5% TV / +5.6% Stooq, €249k — clears € floor, misses ≥8% small-cap move bar with RVol 0.37.
- **MQR** MultiQure (GPW) — ESPI 45/2026 deal with Apertura Gene Therapy; +5.7%, €170k — price zł1.48 < zł2 floor.
- **WAS** Wasko (GPW) +7.8% (Stooq), ~€121k — turnover floor.
- **LIT** Litigation Capital — Permission to Appeal rejected; −15.8% (lse.co.uk, 6 trades) — thin.
- **G1A** GEA strong Q3 (EQS) — −0.07% flat; **COK** Cancom prelims — +0.49%; **ERA** Eramet roadmap — +1.83%; **NDX1** Nordex Albania entry — flat.
- **TGP** Tekmar framework agreement +7.1% — €4k turnover; **BGO** Bango/Ooredoo +2.6% — €9k.
- **TBCG** +3.89% (day-3 after Q3) €359k; **HNSA** +4.7% €335k; **XK4** Gabler +3.3% RVol 1.33 €342k — no catalyst found.
- **Airbus** buyback launch (EQS ad-hoc 08:15) ~+1.5% — under bar.
- Illiquid ESPI: Telestrada Q3, Tenderhut Q3, Gaming Factory licence, Medicalgorithmics US deal (+1.5%, €14k), Coal Energy strategy.

## Poland (GPW) — core
- **ESPI dual-source: ok.** Biznesradar temat/76 pp.1–3 (HTTP, 60 items, Fri 15:40 → Mon 08:54) + wyniki temat/6 (HTTP, 20) + **Bankier komunikaty pp.1–2 (browser, Cloudflare passed; Fri 17:07 → Mon 08:53)** + n8n 2026-11-08.jsonl (10) / 2026-11-09.jsonl (15), triage exec **2056**, no feed_warning. Feeds agree.
- **Today's ESPI with tape:** UCG results (Soft-A, Milan primary), MQR (near-miss, price floor), MDG (+1.5%, illiquid), Telestrada/Tenderhut Q3 (illiquid), Gaming Factory licence, Coal Energy strategy.
- **Weekend/after-close ESPI:** Esotiq prelim Oct revenue (Sun 17:46), Equnico corrected Q3 estimates, LUG Q3 estimates (Fri 22:37), CI Games full repayment of PKO/Erste loans (Fri 20:14), Grupa Azoty / Police court approval of partial arrangement (Fri 18:42), DataWalk US patent (Fri 16:25), Lokum conditional land sale — none cleared floors + move live.
- **Stooq (browser, 09:21 CET):** WIG +0.54%, WIG20 +0.80%; adv 191 / dec 163. Top risers WAS +7.8%, MQR +5.7%, DAT +5.6%, TOA +3.4%, ATT +3.0%; fallers mostly NewConnect. DNP flat (HTML −6% was Friday's row).
- No floor-cleared GPW mover lacked a why-line → no ticker-news pass needed. **Poland is not quiet** — ESPI flow normal, just no liquid GPW reaction above the bars yet.

## Overnight → open annex (from 2026-11-06-open.md `overnight_carry`; no 11-06 midday file — middays paused)
| Ticker | Fri note | Now | Status |
|---|---|---|---|
| BILN | −18% trading-update | 334.75p +0.83%, €60k | settled — clear |
| TEP | Q3 / guide cut −15% | €68.88 +0.64%, €881k | stabilised — clear |
| OUT1V | interim −13% | €3.686 −2.85%, €1.6M | mild continuation — under bar, clear |
| TOKMAN | Q3 miss / bounce | €6.53 −0.08% | clear |
| TBCG | 3Q + buyback | +3.89%, €359k | near-miss (no new catalyst) |
| MDV | prelim Q3 ESPI | zł103.6 +1.27%, €1.4M | faded — clear |
| MTG | Ahlsell offer 1/2 | CHF45.15 flat | file C; count stays 1/2 |
| RAIVV | profit warning | €2.195 +0.69%, €13k | clear |

## overnight_carry
- **BAMI / UCG / CBK:** Italian/German bank M&A — watch Crédit Agricole terms, BPM board response and any UniCredit counter at midday.
- **HOT:** ACS denial — watch for follow-up statements.
- **QLIRO:** Svea offer SEK 23.50 — BUYOUT_NEAR **1/2** chatted; file-only unless a competing bid or new terms.
- **KNOS / VLA / CICN:** midday continuation check.

## ⚠️ Skipped
⚠️ Skipped: finanzen.net ad-hoc — Akamai "Access Denied" (edgesuite.net reference) on load and after one reload; consent wall never shown. German ad-hoc covered by EQS AD-HOC (browser) + onvista feed.

## Source health
| Source | Status | Notes |
|--------|--------|-------|
| TV HTML movers (11 slugs × 4) | ok | 44/44 HTTP 200; 3686 rows / 2432 unique; CH 345 / DK 182 rows merged. **Many non-UK rows were Friday-close** (stale) — all tiers re-quoted live |
| TradingView Local `get_symbol_data_batch` | ok | 2 calls, 76/76 resolved (~08:45 London) |
| TradingView Local `get_news` | ok | 10 calls (PHARM, HOT, AUTO, FIA1S, CICN, NXR, MEGP, COTN, UCG, BAMI); total TV MCP 12 |
| Investegate | ok | p1–10, 500 items 09 Nov 08:28 → 06 Nov 07:00 |
| LSE risers / fallers | browser | Rendered; only 10 rows each without registration. Trade-count filter applied (BAMI 0RLA 290 trades = dual of primary; SEE 72 trades) |
| LSE Hot Chat Topics | browser | MKA 49, MATD 33, GEX 29, GGP 21, HPOW 17, GST 16, SEE 16… — `CHAT_HEAT` seed only; none promoted |
| LSE ticker news (NXR, MEGP, KOO) | browser | HTTP 403 → browser ok; none same-session |
| Biznesradar ESPI (temat/76 pp.1–3) | ok | HTTP 200, 60 items parsed + merged (Fri 15:40 → Mon 08:54) |
| Biznesradar wyniki (temat/6) | ok | HTTP 200, 20 items parsed |
| Biznesradar session stats | ok | HTTP 200 |
| Bankier komunikaty | browser | HTTP 403 → browser, Cloudflare passed on wait; pp.1–2 parsed (Fri 17:07 → Mon 08:53) and merged |
| n8n ESPI file | ok | 11-08: 10 lines; 11-09: 15 lines; triage exec 2056, WARNINGS none |
| Stooq PL session stats | browser | Browser-only; WIG +0.54%, WIG20 +0.80% (09:21/09:37 CET) |
| EQS AD-HOC | browser | Airbus buyback, Sandoz Brazil semaglutide, NEXTDC; Fri ABO Energy bond interest suspension |
| finanzen.net ad-hoc | skipped | Akamai Access Denied after one reload (see ⚠️ Skipped) |
| onvista agentur-meldungen | browser | HTTP 429 → browser ok (~1h of items): ACS denies Hochtief bid report; Crédit Agricole/BPM; DAX +1.12% |
| Euronext Paris / Amsterdam company news | ok | HTTP 200; Crédit Agricole/BPM, Valneva Ph2, Eramet, CTP Vietnam deal |
| Boursorama palmarès | ok | HTTP 200 (seed only) |
| Nasdaq Nordic company news | ok | API, 200 items (Svea/Qliro offer, European Energy solar sale, Reima Q3) |
| NewsWeb Oslo (API) | ok | 47 items today (AKVA 90% acceptance, DNO lapse, Hunter update) |
| 1Info COMUNICATI | browser | Nothing dated 09.11 in regulated table yet; weekend Recordati/BidCo, Iveco |
| eMarket Storage | browser | HTTP shell → browser ok; UniCredit Q3 + dividend, Energy Time tenders, Intesa OPAS MPS doc |
| Teleborsa Comunicati | ok | HTTP 200 with items (DiaSorin IVDR CE); index header |
| Frankfurter FX | ok | ECB 2026-11-06 rates |
| Prior overnight_carry | ok | 2026-11-06-open.md loaded |
