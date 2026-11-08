# Macro calendar — week ahead

- **Edition:** Sunday edition (forward week)
- **Issued:** 2026-11-08 15:10 ET / 2026-11-08 20:10 UTC
- **Covered week:** Monday 2026-11-09 → Sunday 2026-11-15 (ISO week **2026-W46**)
- **Scope:** US macro releases, FOMC communications, Treasury auctions. International central banks are out of scope per the skill spec.
- **Sources:** `web_search` + `curl` against primary publishers (Federal Reserve, U.S. Treasury, Census, BLS via corroboration, EIA, USDA). FRED MCP is not registered in this runtime — see Source health.

---

## TL;DR

- **Tier 1 events this week: 4 line items across 2 release days** — **CPI + Core CPI (Oct) Tue Nov 10, 8:30 ET** and **PPI + Core PPI (Oct) Fri Nov 13, 8:30 ET**. There is **no NFP, no PCE, no GDP and no FOMC decision** inside this window.
- **No FOMC meeting this week.** The last meeting was **Oct 27–28**; the **minutes land Wed Nov 18, 2:00 PM ET** and the **next decision is Wed Dec 9** (Dec 8–9 meeting, with projections). Any calendar showing a rate decision on Nov 10–13 is wrong.
- **Biggest risk day: Tuesday Nov 10** (`HIGH_IMPACT_DAY`) — CPI *and* the **10-year note auction ($42bn)** on the same day, plus the Dallas/KC energy conference (Logan, Schmid). The **$42bn 10y** is the coupon auction most sensitive to a hot core CPI print.
- **Second: Friday Nov 13** (`HIGH_IMPACT_DAY`) — **PPI**, the confirmation print for the CPI surprise, with a **$25bn 30-year bond** the day before.
- **Wednesday Nov 11 is Veterans Day: the US BOND market is fully closed (SIFMA recommendation), the STOCK market trades a normal session.** Federal Reserve statistical releases due Wed move to Thu Nov 12, and the **EIA petroleum report moves to Thu Nov 12, 12:00 PM ET**. *This corrects the Nov 1 edition's next-week preview, which said "US markets closed" — the equity market is open.*
- **Fed speakers: 13 distinct officials across 19 slots** (Mon 3, Tue 6, Wed 0, Thu 5, Fri 5). Tuesday carries two voters after CPI (Paulson 6:30 PM, Bowman 3:30 PM and 6:30 PM) and Wednesday is completely silent — into a holiday-shortened session.
- **Not in this window:** retail sales, durable goods, new home sales, industrial production, ISM, consumer sentiment, JOLTS, Beige Book. Retail sales and IP land Tue Nov 17, the FOMC minutes Wed Nov 18, U. Michigan prelim Fri Nov 20.

---

## Calendar by date (all times ET)

### Monday, November 9

| Time | Event | Tier | Prior | Consensus | Tag |
|---|---|---|---|---|---|
| 8:40 AM | **Fed Bowman** — Board of Governors, **voter** — Discussion, "Community Banking", Mutual Board Summit Conference, Boston MA | 2 | — | — | |
| 10:00 AM | **Wholesale Inventories & Sales (Sep final)** | 2 | +0.5% | — | Census release |
| 10:00 AM | CB Employment Trends Index (Oct) | 3 | 107.56 | — | |
| 10:00 AM | Atlanta Fed GDPNow (Q4) | 3 | 3.4% | — | |
| 10:20 AM | NY Fed Bill Purchases, 1–4 months | 3 | $3.653bn | — | |
| 10:30 AM | Dallas Fed Banking Conditions Survey | 3 | — | — | |
| 11:00 AM | **NY Fed Survey of Consumer Expectations (Oct)** | 3 | 1-yr infl. exp. 3.9% | 3.78% | highest prior since May 2023 |
| 11:30 AM | 6-Week, 13-Week and 26-Week Bill auctions | 3 | — | — | `AUCTION_DAY` |
| 12:15 PM | **Fed Barkin** — Richmond Fed, non-voter | 2 | — | — | |
| 1:00 PM | **3-Year note auction — $58bn** | 2 | — | — | `AUCTION_DAY` — refunding week |

### Tuesday, November 10

| Time | Event | Tier | Prior | Consensus | Tag |
|---|---|---|---|---|---|
| 4:00 AM | **Fed Waller** — Board of Governors, **voter** — Speech, "Economic Outlook", Bank of England and its Watchers Conference, London | 2 | — | — | overnight risk |
| 6:00 AM | NFIB Small Business Optimism (Oct) | 3 | 97.9 | — | |
| 8:30 AM | **CPI (Oct)** | **1** | **+0.6% m/m, 3.7% y/y** | **+0.3% m/m** | `HIGH_IMPACT_DAY` |
| 8:30 AM | **Core CPI (Oct)** | **1** | **+0.3% m/m, 2.6% y/y** | **+0.2% m/m** | `HIGH_IMPACT_DAY` |
| 8:30 AM | Real earnings (Oct, with CPI) | 3 | — | — | BLS companion release |
| 9:35 AM | **Fed Logan** — Dallas Fed, **voter** — opening remarks, "Energy and the Economy" (Houston, hosted with Kansas City) | 2 | — | — | |
| 10:50 AM | **Fed Logan** — morning keynote, same conference | 2 | — | — | |
| 12:00 PM | **USDA WASDE (Nov)** + World Agricultural Production | 3 | — | corn 281.5, wheat 281.8 (DJ survey) | ag complex |
| 1:00 PM | **10-Year note auction — $42bn** | 2 | — | — | `AUCTION_DAY` — **same day as CPI** |
| 1:30 PM | **Fed Schmid** — Kansas City Fed, non-voter — luncheon keynote, Houston | 2 | — | — | |
| 3:30 PM | **Fed Bowman** — Board, **voter** — Speech, "Economic Outlook", C. Peter McColough Series, Washington DC | 2 | — | — | post-CPI read |
| 4:30 PM | API crude oil inventories | 3 | — | — | |
| 6:30 PM | **Fed Bowman** — Board, **voter** — "Economic Outlook" (virtual) | 2 | — | — | |
| 6:30 PM | **Fed Paulson** — Philadelphia Fed, **voter** | 2 | — | — | post-CPI read |

### Wednesday, November 11 — Veterans Day

| Time | Event | Tier | Prior | Consensus | Tag |
|---|---|---|---|---|---|
| — | **US Veterans Day — federal holiday** | — | — | — | **Bond market CLOSED (SIFMA full close); stock market OPEN** |
| — | Fed statistical releases due Wed move to **Thu Nov 12** | — | — | — | Federal Reserve calendar |
| — | EIA Weekly Petroleum Status moves to **Thu Nov 12, 12:00 PM ET** (week ending Nov 6) | 3 | — | — | government closure |
| 7:00 AM | MBA mortgage applications | 3 | — | — | |

*No Fed speakers scheduled Wednesday, and no US data releases of consequence.*

### Thursday, November 12

| Time | Event | Tier | Prior | Consensus | Tag |
|---|---|---|---|---|---|
| 8:30 AM | Initial Jobless Claims (wk of Nov 7) | 2 | 189K | 196K | 4-wk avg prior 194.75K |
| 8:30 AM | Continuing Jobless Claims | 2 | 1,718K | 1,722K | |
| 8:30 AM | Jobless Claims, 4-week average | 3 | 194.75K | 192.5K | |
| 9:00 AM | **Fed Hammack** — Cleveland Fed, **voter** | 2 | — | — | |
| 10:00 AM | **Existing Home Sales (Oct)** | 2 | 3.99M (+1.5% m/m) | **3.80M (−4.8% m/m)** | first negative month of the year |
| 10:00 AM | **Fed Barr** — Board of Governors, **voter** — Speech, "Artificial Intelligence and Inequality" | 2 | — | — | |
| 11:30 AM | 4-Week, 8-Week and 17-Week Bill auctions | 3 | — | — | `AUCTION_DAY` |
| 11:30 AM | **Fed Goolsbee** — Chicago Fed, non-voter | 2 | — | — | |
| 12:00 PM | **EIA Weekly Petroleum Status** (moved from Wed) | 3 | — | — | government closure |
| 1:00 PM | **30-Year bond auction — $25bn** | 2 | — | — | `AUCTION_DAY` |
| 1:10 PM | **Fed Daly** — San Francisco Fed, non-voter | 2 | — | — | |
| 2:00 PM | Monthly Federal Budget (Oct) | 3 | −$284bn (Oct 2025) | — | |
| 4:30 PM | H.4.1 — Factors Affecting Reserve Balances (Fed) | 3 | — | — | |
| 6:30 PM | **Fed Williams** — New York Fed, **voter** | 2 | — | — | |

### Friday, November 13

| Time | Event | Tier | Prior | Consensus | Tag |
|---|---|---|---|---|---|
| 8:30 AM | **PPI (Oct)** | **1** | **+1.3% m/m, 6.3% y/y** | **+0.4% m/m, +6.7% y/y** | `HIGH_IMPACT_DAY` |
| 8:30 AM | **Core PPI (Oct)** | **1** | **+0.7% m/m, 5.0% y/y** | **+0.3% m/m** | `HIGH_IMPACT_DAY` |
| 8:30 AM | PPI ex food, energy & trade (Oct) | 2 | +0.5% m/m | — | |
| 9:40 AM | **Fed Logan** — Dallas Fed, **voter** — opening remarks, Bank Funding Conference (hosted with Boston) | 2 | — | — | low confidence — see Date conflicts |
| 10:00 AM | **Fed Collins** — Boston Fed, **voter** (unattributed remarks) | 2 | — | — | low confidence — see Date conflicts |
| 10:50 AM | **Fed Bowman** — Board, **voter** — Discussion, "Supervision and Regulation", Connecticut Bankers Association (virtual) | 2 | — | — | |
| 12:00 PM | **Fed Daly** — San Francisco Fed, non-voter — moderated discussion, UNLV CBER Forecast Event, Las Vegas | 2 | — | — | |
| 4:15 PM | H.8 / H.15 (Fed statistical releases) | 3 | — | — | |
| 7:00 PM | **Fed Jefferson** — Vice Chair, Board of Governors, **voter** — Speech, "New Technology, Old Questions", UCSD Economics Roundtable, La Jolla CA | 2 | — | — | |

### Saturday / Sunday, November 14–15

Nothing scheduled. Next release is import/export prices and retail sales on Tue Nov 17.

---

## Fed speakers — week of Nov 9

Times are ET. The Fed's own calendar (`federalreserve.gov/newsevents/2026-november.htm`, parsed from raw HTML) covers **Board governors only**; regional presidents are reconciled from the U.S. Bank FOMC roster (published in **Central**, converted +1h), the Dow Jones weekly data-ahead article, Capital.com's Fed events feed, and each Reserve Bank's own event agenda. Every Board-governor slot reconciles exactly across the Fed calendar and the converted U.S. Bank roster, and every regional-president slot reconciles across at least two independent sources.

| Date | Time (ET) | Speaker | Role | Note |
|---|---|---|---|---|
| Mon Nov 9 | 8:40 AM | Michelle Bowman | Board of Governors, **voter** | Discussion, "Community Banking", Mutual Board Summit Conference, Boston MA |
| Mon Nov 9 | 10:00 AM | Austan Goolsbee | Chicago Fed, non-voter | |
| Mon Nov 9 | 12:15 PM | Thomas Barkin | Richmond Fed, non-voter | |
| Tue Nov 10 | 4:00 AM | Christopher Waller | Board of Governors, **voter** | "Economic Outlook", Bank of England and its Watchers Conference, London (9:00 AM London) |
| Tue Nov 10 | 9:35 AM | Lorie Logan | Dallas Fed, **voter** | Opening remarks, "Energy and the Economy: Tail Risks, Tailwind and Resiliency", Houston (co-hosted with Kansas City) |
| Tue Nov 10 | 10:50 AM | Lorie Logan | Dallas Fed, **voter** | Morning keynote, same conference |
| Tue Nov 10 | 1:30 PM | Jeffrey Schmid | Kansas City Fed, non-voter | Luncheon keynote, same conference |
| Tue Nov 10 | 3:30 PM | Michelle Bowman | Board of Governors, **voter** | "Economic Outlook", C. Peter McColough Series, Washington DC |
| Tue Nov 10 | 6:30 PM | Michelle Bowman | Board of Governors, **voter** | "Economic Outlook", virtual |
| Tue Nov 10 | 6:30 PM | Anna Paulson | Philadelphia Fed, **voter** | |
| Thu Nov 12 | 9:00 AM | Beth Hammack | Cleveland Fed, **voter** | |
| Thu Nov 12 | 10:00 AM | Michael Barr | Board of Governors, **voter** | "Artificial Intelligence and Inequality" |
| Thu Nov 12 | 11:30 AM | Austan Goolsbee | Chicago Fed, non-voter | |
| Thu Nov 12 | 1:10 PM | Mary Daly | San Francisco Fed, non-voter | |
| Thu Nov 12 | 6:30 PM | John Williams | New York Fed, **voter** | |
| Fri Nov 13 | 9:40 AM | Lorie Logan | Dallas Fed, **voter** | Opening remarks, Bank Funding Conference, Dallas — *low confidence* |
| Fri Nov 13 | 10:00 AM | Susan Collins | Boston Fed, **voter** | *Low confidence — unattributed remarks, two aggregators only* |
| Fri Nov 13 | 10:50 AM | Michelle Bowman | Board of Governors, **voter** | Discussion, "Supervision and Regulation", Connecticut Bankers Association (virtual) |
| Fri Nov 13 | 12:00 PM | Mary Daly | San Francisco Fed, non-voter | Moderated discussion, UNLV CBER Forecast Event, Las Vegas |
| Fri Nov 13 | 7:00 PM | Philip Jefferson | Vice Chair, Board of Governors, **voter** | "New Technology, Old Questions", UCSD Economics Roundtable, La Jolla CA |

**Wednesday Nov 11 is completely silent** — no Fed speaker is scheduled, and the holiday means no Fed communication into the pre-PPI window.

---

## Treasury calendar

| Date | Event | Detail |
|---|---|---|
| Mon Nov 9 | 6-Week, 13-Week, 26-Week Bill auctions | 11:30 ET |
| Mon Nov 9 | **3-Year note auction — $58bn** | 1:00 PM ET; settles Mon Nov 16 |
| Tue Nov 10 | **10-Year note auction — $42bn** | 1:00 PM ET; settles Mon Nov 16. **Same day as CPI** — the week's key auction risk |
| Thu Nov 12 | 4-Week, 8-Week, 17-Week Bill auctions | 11:30 ET |
| Thu Nov 12 | **30-Year bond auction — $25bn** | 1:00 PM ET; settles Mon Nov 16 |

**All three coupon auctions come from the November refunding: $125bn total, refunding ~$97bn of notes and bonds maturing Nov 15, 2026, raising ~$28bn of new cash.** This is the first full week of the November refunding cycle — the coupon calendar is busy for the first time since the October/November QRA.

**No auction falls on Wednesday Nov 11** — the bond market is closed for Veterans Day, and the 30-year was scheduled for Thursday rather than Wednesday.

---

## Tier 3 / summary-only mentions

- **CB Employment Trends Index** (Mon 10:00 AM), **Atlanta Fed GDPNow** (Mon 11:00 AM), **NY Fed Bill Purchases** (Mon 10:20 AM), **Dallas Fed Banking Conditions Survey** (Mon 10:30 AM), **NFIB Small Business Optimism** (Tue 6:00 AM), **real earnings** (Tue 8:30 AM, BLS companion to CPI), **USDA WASDE + World Agricultural Production** (Tue 12:00 PM), **API crude inventories** (Tue 4:30 PM), **MBA mortgage applications** (Wed 7:00 AM), **EIA petroleum + natural gas storage** (Thu, delayed from Wed), **Monthly Federal Budget for October** (Thu 2:00 PM), **Fed H.8/H.15/H.4.1 statistical releases** (Thu–Fri).

---

## Date conflicts and low-confidence items

| Item | Conflict | Resolution |
|---|---|---|
| Fed speaker roster | The Fed's own November calendar lists **Board governors only**; a web extraction initially presented a combined list including regional presidents and later times | **Resolved against raw HTML.** `federalreserve.gov/newsevents/2026-november.htm` was fetched and parsed (23 rows); the Board-governor rows are authoritative. Regional presidents are sourced separately and each carries ≥2 independent confirmations, except the two flagged below. |
| U.S. Bank speaker times | Published in **Central time**, one hour behind ET | **Converted +1h**, then validated: every Board slot matches the Fed calendar to the minute (Bowman Nov 9 8:40 ET, Waller Nov 10 4:00 ET, Bowman Nov 10 3:30 and 6:30 PM, Barr Nov 12 10:00 ET, Bowman Nov 13 10:50 ET). |
| Fed speakers on Wed Nov 11 | Two aggregators list a Bowman appearance on Wednesday | **Rejected.** The Fed calendar shows Nov 11 as a holiday with no speeches, and the U.S. Bank FOMC roster has no Nov 11 entries. |
| Logan's Tue Nov 10 slot | U.S. Bank roster omits Logan; Dallas Fed's own agenda and Capital.com list him | **Kept** — the Dallas Fed agenda and Capital.com agree on both the opening remarks (8:35 CT / 9:35 ET) and the morning keynote (9:50 CT / 10:50 ET), and the Schmid luncheon keynote (12:30 CT / 1:30 ET) matches the U.S. Bank roster. |
| Logan's Fri Nov 13 slot | Only the Dallas Fed's own Bank Funding Conference agenda lists him (8:40 CT); the U.S. Bank FOMC roster omits Nov 13 entirely | **Kept at low confidence** — sourced to the Dallas Fed agenda, not to a Fed-wide roster. |
| Collins on Fri Nov 13 | Listed by two aggregators (14:10 GMT on one) and implied by the jointly-hosted Boston/Dallas conference; no Fed-wide roster confirms | **Kept at low confidence** and explicitly flagged in the Fed speakers table. |
| Jefferson's slot | One aggregator renders it as 00:00 GMT under Friday | **Resolved to Fri Nov 13, 7:00 PM ET** from the Fed's own calendar (UCSD Economics Roundtable). |
| CPI y/y consensus | WSJ median survey has **no** y/y median (only m/m); Nowflation's FMP street estimate says 3.7%; Cleveland Fed nowcast says 3.74%; one calendar shows a 3.9% forecast | **Published as —** for the WSJ y/y median, with the nowcasts listed in the CPI commentary below. |
| Jobless claims consensus | WSJ median 196K vs FMP/TradingEconomics 195K | **Published as 196K (WSJ median survey of 6 economists)**; the 195K alternative is noted here. |
| Existing home sales consensus | WSJ 3.80M / −4.8% m/m vs TradingEconomics/Nowflation 3.98M / +0.3% m/m | **Published the WSJ figures** — they are internally consistent with the 3.99M prior (3.80/3.99 = −4.8%), while 3.98M against a 3.99M prior implies ≈0%, not +0.3%. The 3.98M reading is treated as a calendar artifact. |
| New Home Sales (Oct) | TradingEconomics' US calendar dump places New Home Sales on Nov 12 with a 0.676M prior | **Rejected.** Census's own release schedule puts **New Residential Sales (Oct) on Nov 25**, and the 0.676M figure is the *September* print. New Home Sales is **not** in this week. |
| Veteran Day market status | The Nov 1 edition's next-week preview said "US markets closed" | **Corrected.** SIFMA recommends a **full close for US fixed income** on Wed Nov 11; the **NYSE/Nasdaq trade a normal session** — it is a federal holiday the exchange does not observe. |
| Wholesale inventories consensus | WSJ median is NA; one aggregator shows an estimate of +0.2% m/m | **Published as —** (no survey median); the single-aggregator estimate is not treated as consensus. |

### CPI (Tue Nov 10) — consensus detail

| Measure | Prior (Sep) | Consensus | Nowcast / alternative |
|---|---|---|---|
| CPI m/m | +0.6% | **+0.3%** (WSJ, 9 economists) | Cleveland Fed nowcast +0.24% |
| Core CPI m/m | +0.3% | **+0.2%** (WSJ, 9 economists) | Cleveland Fed nowcast +0.21% |
| CPI y/y | 3.7% | — (no WSJ median) | Street (FMP) 3.7%; Cleveland Fed 3.74% |
| Core CPI y/y | 2.6% | — (no WSJ median) | Cleveland Fed nowcast 2.5% |
| CPI index (SA) | 336.94 | 337 (TradingEconomics) | core index prior 338.90 |

**PPI (Fri Nov 13) — consensus detail:** headline m/m prior +1.3%, consensus +0.4% (WSJ, 8 economists); core m/m prior +0.7%, consensus +0.3% (WSJ, 5 economists); PPI y/y prior +6.3%, consensus +6.7% (WSJ, 3 economists); core PPI y/y prior 5.0%; PPI index prior 159.78. Yardeni's read is that October PPI is likely hotter than September's 6.3% / 5.0% headline and core.

---

## Next week (2026-W47) — preview

- **Tue Nov 17, 8:30 AM ET — Retail Sales (Oct)** plus import/export prices; **9:15 AM ET — Industrial Production (Oct)**.
- **Wed Nov 18, 2:00 PM ET — FOMC minutes** from the Oct 27–28 meeting, with the **20-year bond auction** the same day.
- **Fri Nov 20, 10:00 AM ET — U. Michigan consumer sentiment, prelim (Nov)**.
- **Wed Nov 25 — Durable goods (Oct)** (8:30 AM), **New home sales (Oct)** (10:00 AM) and the **Beige Book**, all confirmed against the Census release schedule and the Fed's own calendar.
- **Wed Dec 9 — next FOMC decision** (Dec 8–9 meeting, with a Summary of Economic Projections).

---

## Source health

| Source | Query / URL | Status | Notes |
|---|---|---|---|
| Skill spec | `api.github.com/.../cloud-prompts/skills/macro-calendar-week/SKILL.md` | **ok** | 5,292 bytes, read in full |
| Shared prompt blocks | `api.github.com/.../cloud-prompts/_shared/PROMPT-BLOCKS.md` | **ok** | 26,487 bytes, read in full |
| Window check | `_shared/window_check.sh` (`WINDOW_CHECK_V2`), `--scheduled-at-ms 1794168079445` | **ok** | `window-check: OK (2026-11-08)`, `fire-date: 2026-11-08`, `replay: no` |
| MCP availability probe | `_shared/probe_mcp.py` | **ok** | `catalog_ok total=135 finance_tools=0` — no finance MCP registered; this routine needs no quote path |
| Federal Reserve — November calendar | `federalreserve.gov/newsevents/2026-november.htm` (curl, HTTP 200) | **ok** | Parsed all 23 rows from raw HTML; authoritative for Board governors, the Veterans Day holiday and the release-shift note |
| Federal Reserve — monetary policy | `federalreserve.gov/monetarypolicy.htm` (curl, HTTP 200) | **ok** | Confirms Nov 18 minutes (Oct 27–28 meeting), Dec 8–9 meeting, Dec 30 minutes |
| U.S. Treasury — refunding statement | `home.treasury.gov/news/press-releases/sb0678/` (curl, HTTP 200) | **ok** | Authoritative for auction sizes ($58bn 3y / $42bn 10y / $25bn 30y) and 1:00 PM ET auction times |
| U.S. Treasury — auction schedule | `home.treasury.gov/system/files/221/TentativeAuctionScheduleQ42026.xml` (curl, HTTP 200) | **ok** | Parsed the Q4 calendar; bill and coupon auction dates inside this week |
| U.S. Census Bureau | `census.gov/economic-indicators/calendar-listview-2026.html`, `census.gov/construction/soc/schedule.html` | **ok** | Wholesale trade Nov 9; retail sales Nov 17; New Residential Sales **Nov 25** — used to reject the Nov 12 placement |
| SIFMA — Veterans Day | `sifma.org` holiday recommendation (Oct 28, 2026) | **ok** | Full close for US fixed income on Wed Nov 11; equity market unaffected |
| EIA — Weekly Petroleum Status | `eia.gov/petroleum/supply/weekly/` + release schedule | **ok** | Confirms the Thursday Nov 12 12:00 PM ET move caused by the government closure |
| USDA | `usda.gov/.../wasde-report` | **ok** | November WASDE confirmed for Nov 10, 12:00 PM ET |
| BLS release schedule | `bls.gov/schedule/news_release/cpi.htm` | **degraded** | Direct fetch **HTTP 403**; CPI/PPI dates confirmed via BLS-citing calendars (Dow Jones data-ahead, financecalendar.com, multiple aggregators) |
| WSJ / Dow Jones — Data Week Ahead | `morningstar.com` reprint of Dow Jones Newswires, 2026-11-06 14:15 ET | **ok** | Primary consensus source for CPI, PPI, claims, existing home sales, wholesale inventories, NFIB, federal budget |
| Nowflation calendar | `nowflation.com/calendar` | **ok** | Street (FMP) CPI 3.7% as of Nov 8; Cleveland Fed 3.74%; Nowflation forecast 3.78% |
| Cleveland Fed nowcast | via Yardeni Economic Week Ahead (Nov 7) | **ok** | Oct CPI +0.24% m/m headline, +0.21% m/m core; headline 3.7% y/y, core 2.5% y/y |
| FHLB NY weekly update | `fhlbny.com` weekly market update (Nov 6) | **ok** | NY Fed SCE consensus 3.78% vs 3.90% prior |
| Capital.com — Fed events | `capital.com/en-ke/news/federal-reserve-events` | **ok** | Logan Tue 9:35 ET; Schmid Tue 1:30 ET; Daly Fri 12:00 ET |
| U.S. Bank FOMC speaker roster | `usbank.com/.../weekly.html` + weekly PDF (Nov 6) | **ok** | Speaker times in **Central** — converted +1h and validated against the Fed calendar |
| Dallas Fed event agendas | `dallasfed.org/events/2026/26energy`, `.../26bankfunding` | **ok** | Logan's Tue keynote and Fri opening remarks; Schmid's Tue luncheon keynote |
| Yahoo Finance / Dow Jones weekly data-ahead | `finance.yahoo.com` | **ok** | Independent corroboration of speaker ET times and release times |
| Finviz economic calendar | `finviz.com/calendar/economic?dateFrom=2026-11-09` | **degraded** | Direct curl **HTTP 403** (Cloudflare interstitial); used **only via web_search snippet** for prior values and as a cross-check. Not the sole source for any date. |
| fedcal.io | `fedcal.io` | **failed** | Did not load; not needed — the Fed's own calendar superseded it |
| FRED MCP (`mcp__fred__get_release_dates`) | — | **unavailable** | Not registered in this runtime; web fallback used per the runtime contract |
| `mcp__*` finance MCPs | — | **not required** | This routine reads a release calendar, not market quotes |

**degraded_sources: 2** — `bls.gov` release schedule (HTTP 403, dates corroborated elsewhere) and Finviz (HTTP 403, used via search snippet only).

**errors: 2** — no MCP call was attempted, so no MCP fallback was triggered; the two degraded sources are HTTP 403s on sites whose content was recovered and cross-checked, not missing data.

**as_of_utc:** 2026-11-08 20:10 UTC. Consensus figures are pre-print: the WSJ median survey was compiled 2026-11-06 14:15 ET, the Cleveland Fed nowcast and Nowflation calls are as of Nov 7–8, and they can still move before each release. Release *dates* were confirmed against primary publishers (Federal Reserve, Treasury, Census, EIA, USDA) rather than aggregators wherever a primary source exists.

---

*macro-calendar target=macro:2026-W46 tier1=4 fed_speakers=13 source=web_fallback*
