---
date: 2026-11-09
market: taiwan
slot: open
producer: grok-bot/taiwan-stocks-in-play
contract: intl-stocks-in-play-v1
source: Grok Bot box digest (Fundamental taiwan stocks-in-play routine)
generated_at: 2026-11-09T20:00:00+07:00
status: ok
---

Provenance: Fundamental digest at /home/box/taiwan-in-play/2026-11-09-open.md; built at 2026-11-09T20:00:00+07:00; covered session open.

**Deviations:** none

# Taiwan stocks in play — 2026-11-09 open
Run: 09:30–09:50 Asia/Taipei (data as of 09:28–09:30). Session: early; TAIEX 41,197.5 vs 39,701.6 prev (+3.8%); TPEx 318.88 vs 304.02 (+4.9%) at 09:30 (TWSE MIS). Broad AI-hardware / memory / passive-component melt-up with many ±10% locks.
Sort: tier, then TWD turnover desc. RelVol = Yahoo session volume vs 10-session average of full-day volume at 09:30, so it reads low everywhere (not time-adjusted); treat as soft, not as missing.

## Tier A
None (no elevated-RVol + catalyst name; RVol not time-adjusted).

## Soft-A (SOFT_A)
| Ticker | Company | Move | RelVol | Turnover (TWD / US$) | Catalyst |
|---|---|---|---|---|---|
| 6669 | Wiwynn (緯穎) | +6.1% | 0.3× | 22.9億 / US$70m | MOPS 11/06 evening: Q3 results; board approved cash raise via overseas GDR plus cash injections into Malaysia, Wiwynn Technology subsidiaries |
| 8039 | Taiflex (台虹) LIMIT_UP | +9.8% | 0.4× | 14.8億 / US$45m | MOPS 11/06 (E Ink 8069 release): material cooperation letter of intent signed with Taiflex |
| 6538.TPEX | Brave Screen (倉和) | +8.4% | 1.2× | 13.4億 / US$41m | MOPS 11/06: Q3 results; subsidiary in Suzhou signed cooperation contract and investment with 安吉光翼創新能源科技 |
| 7769 | Hon Precision (鴻勁) | +5.7% | 0.3× | 11.5億 / US$35m | MOPS 11/06 20:36: board approved share buyback |
| 8069.TPEX | E Ink (元太) | +4.2% | 0.3× | 3.2億 / US$10m | MOPS 11/06: LOI with Taiflex; board OK to join SinoPac Holdings cash raise; property purchase from related party China Pulp |
| 6919 | Caliway (康霈*) LIMIT_UP | +10.0% | 0.4× | 2.1億 / US$6m | MOPS 11/06 17:49: board approved share buyback (multi-day LU follow-through) |

## TECH_WATCH (liquid, no same-session catalyst; turnover well above floor)
2330 TSMC (台積電) +3.5%, 0.3×, 292.8億 US$891m | 2454 MediaTek (聯發科) +5.2%, 0.4×, 165.0億 US$502m | 2308 Delta Electronics (台達電) +9.0%, 0.6×, 124.4億 US$379m | 3037 Unimicron (欣興) +2.5%, 0.6×, 113.7億 US$346m | 2383 EMC (台光電) +2.4%, 0.4×, 65.1億 US$198m | 2303 UMC (聯電) +4.6%, 0.4×, 60.6億 US$185m | 2408 Nanya Tech (南亞科) +6.7%, 0.3×, 60.3億 US$183m | 3443 GUC (創意) +3.1%, 0.3×, 58.4億 US$178m | 2344 Winbond (華邦電) +8.3%, 0.3×, 28.7億 US$87m (only routine CB conversion-price notices)

## Tier B
3363.TPEX FOCI (上詮) +4.7%, 1.3×, 13.6億 | 3605 ACES (宏致) -5.4%, 1.3×, 12.3億 (MOPS: property acquisition) | 6443 TSEC (元晶) +5.4%, 1.9×, 5.7億

## Tier C — LIMIT_UP with size (no catalyst)
1303 Nan Ya Plastics (南亞) +9.8%, 94.1億 US$286m | 2327 Yageo (國巨) +9.9%, 58.0億 US$177m | 3105.TPEX WIN Semi (穩懋) +10.0%, 52.2億 US$159m | 1802 Taiwan Glass (台玻) +9.9%, 34.5億 US$105m | 2492 Walsin Tech (華新科) +9.9%, 31.2億 US$95m | 6488.TPEX GlobalWafers (環球晶) +10.0%, 27.4億 US$83m | 6770 PSMC (力積電) +9.8%, 24.7億 US$75m (Q3 results 11/06 evening)
Also ±10% locks below US$75m omitted (see cands.json). Negative note: 6456 GIS-KY (-2.7%, US$65m) — Q3 results plus board-approved cash raise (MOPS 11/06 20:08), dilution; file only.

## Overnight → open annex (from 11-06 open overnight_carry)
Prior carry (Formosa/BizLink/PEC Soft-A bounce; 6919/1558; AI supply-chain TECH_WATCH cluster; 3287.TPEX Kworld LU) re-checked: BizLink 3665 +4.1%, PEC 6446 +5.9%, Caliway 6919 LU (promoted to Soft-A on buyback), AI cluster (EMC/GUC/Unimicron/Kinsus/TUC/MediaTek/Wiwynn) all green. Midday slot 11-06 not run; midday routines paused. No stale halts.

## overnight_carry
For next midday/open: whether Taiflex 8039 stays locked and E Ink 8069 follows through on the Taiflex LOI; whether Wiwynn holds after GDR cash-raise news; whether the broad ±10% LU cluster (Yageo, WIN, GlobalWafers, PSMC, NPC) keeps volume on day 2; Caliway 6919 multi-day LU.

## ⚠️ Skipped
None for this run. MOPS covered via headed-browser scrape; CMoney buzz / Wantgoo / TradingView / MoneyDJ not hit (Yahoo + exchange rosters + MOPS sufficient given a broad tape); noted as skipped-by-design, not blocked.

## Source health
| Source | Status | Notes |
|---|---|---|
| Yahoo TW ranks (TAI/TWO × 4) | ok | HTTP 200 ×8, rankTime 09:28–09:30 Taipei, 578 symbols |
| TWSE MIS getStockInfo (indices) | ok | 09:30 prints |
| TWSE MI_INDEX 11-06 / TPEx dailyQuotes 11-06 | ok | History window 14 sessions, last 10 used for RVol |
| TWSE / TPEx rosters (co-twse/co-tpex) | ok | Reused from 11-06 scratch |
| MOPS SPA t05st02 (browser) | browser | 173 rows 11/06 17:30 → 11/09; saved _scratch-20261109-open/mops-browser.txt |
| TWSE OpenAPI t187ap04_L | ok | Only 4 recent rows, not material |
| CMoney ranks / buzz | skipped | fetched HTTP 200 but not parsed this run (broad-tape slot); no buzz-only promotions made |
| MoneyDJ, TradingView, Wantgoo | skipped | not needed; no TV MCP calls |

Intraday-bar check: not applicable (Yahoo quote session volume/turnover).

## FX
USD/TWD 32.851 (open.er-api.com, 2026-11-09). US$ = TWD ÷ 32.851.
