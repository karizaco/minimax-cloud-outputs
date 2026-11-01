# Macro calendar — week ahead

- **Edition:** Sunday edition (forward week)
- **Issued:** 2026-11-01 15:0x ET / 2026-11-01 20:0x UTC
- **Covered week:** Monday 2026-11-02 → Sunday 2026-11-08 (ISO week **2026-W45**)
- **Scope:** US macro releases, FOMC communications, Treasury auctions. International central banks are out of scope per the skill spec; the RBA (Tue) and BoE (Thu) are noted only as cross-asset context.
- **Sources:** `web_search` + `curl` (FRED MCP is not registered in this runtime — see Source health)

---

## TL;DR

- **Tier 1 events this week: 3** — all on **Friday Nov 6, 8:30 ET** (Nonfarm Payrolls, Unemployment Rate, Average Hourly Earnings). There is **no CPI, no PPI, no PCE, no GDP and no FOMC decision** inside this window.
- **No FOMC meeting.** The last meeting was **Oct 27–28** (statement Oct 28: held 3.75%–4.00%, 10–2 vote, Hammack dissenting for a hike). The next decision is **Wed Dec 9**; **FOMC minutes land Wed Nov 18**. Any calendar showing a "rate decision" on Nov 4 is wrong.
- **Biggest risk day: Friday Nov 6** (`HIGH_IMPACT_DAY`) — the only Tier 1 day, and it lands two sessions after the election.
- **Second-biggest: Wednesday Nov 4** (`ELEVATED_IMPACT_DAY`) — **Treasury quarterly refunding statement 8:30 ET** (the long-end catalyst: Citi expects 20y/30y auction sizes trimmed by $3bn each) + ISM Services + ADP + trade balance.
- **Third: Tuesday Nov 3** (`ELEVATED_IMPACT_DAY`) — **US midterm elections** + JOLTS + factory orders. Election results are the week's real macro event; the data releases are secondary.
- **Fed speakers: 7 across 4 days** (Mon, Thu ×3, Fri ×3). Three of the seven are 2026 FOMC voters, one of them (Hammack) dissented at the last meeting.
- **Not in this window:** retail sales, durable goods, new/existing/pending home sales, industrial production, CB consumer confidence, TIC, Beige Book. First of those lands after the Nov 11 holiday.

---

## Calendar by date (all times ET)

### Monday, November 2

| Time | Event | Tier | Prior | Consensus | Tag |
|---|---|---|---|---|---|
| 9:45 AM | S&P Global US Manufacturing PMI (final, Oct) | 3 | 57.2 (flash) | — | |
| 10:00 AM | **ISM Manufacturing PMI (Oct)** | 2 | 54.7 | 54.5 | `HIGH_IMPACT_DAY` |
| 10:00 AM | ISM Mfg — prices paid (Oct) | 2 | 77.9 | 77.5 | inflation risk |
| 10:00 AM | Construction Spending (Sep) | 3 | 0.9% | 0.6% | |
| 11:00 AM | Atlanta Fed GDPNow (Q4) | 3 | 3.2% | — | |
| 11:15 AM | **Fed Goolsbee** — Chicago Fed, non-voter | 2 | — | — | `AUCTION_DAY` (bills) |
| 11:30 AM | 3-Month Bill auction (prev 4.014%) | 3 | 4.014% | — | `AUCTION_DAY` |
| 11:30 AM | 6-Month Bill auction (prev 4.210%) | 3 | 4.210% | — | `AUCTION_DAY` |
| 2:00 PM | Senior Loan Officer Survey (SLOOS) | 3 | — | — | |
| 3:00 PM | **Treasury Q4 financing estimates** (pre-refunding) | 2 | — | — | sets up Wed QRA |
| 4:00 PM | NY Fed Consumer Inflation Expectations (Oct) | 3 | 3.9% | — | |

### Tuesday, November 3

| Time | Event | Tier | Prior | Consensus | Tag |
|---|---|---|---|---|---|
| — | **US midterm elections** (all 435 House seats, 1/3 of Senate) | — | — | — | `ELEVATED_IMPACT_DAY` — fiscal/regulatory path |
| 10:00 AM | **JOLTS job openings (Sep)** | 2 | 7.079M (Aug) | 7.10M–7.13M | quits 1.9%, layoffs 1.0% prior |
| 10:00 AM | Factory Orders (Sep) | 3 | 1.1% | 0.1% | ex-transport 0.3% prior |
| 11:00 AM | NFIB Business Optimism (Oct) | 3 | 97.9 | — | |
| 11:30 AM | 6-Week Bill auction | 3 | 3.950% | — | |
| — | RBA rate decision (context only, out of scope) | — | — | — | |

### Wednesday, November 4

| Time | Event | Tier | Prior | Consensus | Tag |
|---|---|---|---|---|---|
| 8:15 AM | ADP National Employment (Oct) | 3 | 90K | 65K | |
| 8:30 AM | **Treasury Quarterly Refunding Statement (QRA)** | 2 | — | — | `ELEVATED_IMPACT_DAY` — **key long-end event** |
| 8:30 AM | Trade Balance (Sep) | 3 | −$105.6B | ≈−$107.9B | |
| 9:45 AM | S&P Global US Services PMI (final, Oct) | 3 | 57.9 (flash) | — | |
| 10:00 AM | **ISM Services PMI (Oct)** | 2 | 54.9 | 54.7–54.8 | prices paid prior 74.0 |
| 10:30 AM | EIA crude stocks | 3 | — | — | |

*No Fed speakers scheduled Wednesday.*

### Thursday, November 5

| Time | Event | Tier | Prior | Consensus | Tag |
|---|---|---|---|---|---|
| 8:30 AM | Initial Jobless Claims (wk of Oct 31) | 2 | 194K | 195K | 4-wk avg 196.75K prior |
| 8:30 AM | Continuing Jobless Claims | 2 | 1,701K | 1,710K | |
| 8:30 AM | Productivity & Costs, Q3 prelim | 2 | 1.4% q/q | 2.5% | ULC prior 1.2%, cons 0.3% |
| 8:50 AM | **Fed Hammack** — Cleveland, **voter** (dissented for a hike on Oct 28) | 2 | — | — | |
| 9:10 AM | **Fed Barkin** — Richmond, non-voter | 2 | — | — | |
| 11:30 AM | 8-Week Bill auction | 3 | 4.020% | — | `AUCTION_DAY` |
| 7:00 PM | **Fed Logan** — Dallas, **voter** (called for two more hikes) | 2 | — | — | after-hours reaction risk |
| — | BoE rate decision (context only, out of scope) | — | — | — | |

### Friday, November 6

| Time | Event | Tier | Prior | Consensus | Tag |
|---|---|---|---|---|---|
| 4:30 AM | **Fed Williams** — New York, **voter** | 2 | — | — | |
| 8:30 AM | **Nonfarm Payrolls (Oct)** | **1** | **+29K** | **+55K to +65K** | `HIGH_IMPACT_DAY` |
| 8:30 AM | **Unemployment Rate (Oct)** | **1** | **4.2%** | **4.2%** | Barclays 4.1% |
| 8:30 AM | **Average Hourly Earnings (Oct)** | **1** | +0.1% m/m, 3.0% y/y | +0.3% m/m, 2.9% y/y | |
| 8:30 AM | Private payrolls | 1 | +46K | +60K | |
| 8:30 AM | U-6 unemployment / participation | 1 | 7.6% / 61.8% | 7.6% / 61.9% | |
| 9:10 AM | **Fed Musalem** — St. Louis, non-voter | 2 | — | — | |
| 10:00 AM | U. Michigan Consumer Sentiment, prelim (Nov) | 2 | 48.0 (Oct final) | 47.0 | 1-yr infl. exp. prior 4.7%, 5-yr 3.5% |
| 12:15 PM | **Fed Bowman** — Board of Governors, **voter** | 2 | — | — | |

### Saturday / Sunday, November 7–8

Nothing scheduled. Next release is ISM Manufacturing on Mon Nov 9.

---

## Fed speakers — week of Nov 2

Times converted to ET. U.S. Bank publishes its calendar in CT; the ET conversion is corroborated exactly by the Finviz calendar (Goolsbee 11:15, Hammack 8:50, Barkin 9:10, Logan 7:00 PM, Williams 4:30 AM, Musalem 9:10, Bowman 12:15 PM).

| Date | Time (ET) | Speaker | Role | Note |
|---|---|---|---|---|
| Mon Nov 2 | 11:15 AM | Austan Goolsbee | Chicago Fed, non-voter | Financial Markets Group Fall Conference, moderated Q&A with BIS Deputy GM Andrea Maechler (10:15 CT, Chicago) |
| Thu Nov 5 | 8:50 AM | Beth Hammack | Cleveland Fed, **voter** | Dissented at the Oct 28 meeting in favour of another hike — first chance to reframe |
| Thu Nov 5 | 9:10 AM | Tom Barkin | Richmond Fed, non-voter | |
| Thu Nov 5 | 7:00 PM | Lorie Logan | Dallas Fed, **voter** | Called for two more hikes; after-hours remarks into Friday's payrolls |
| Fri Nov 6 | 4:30 AM | John Williams | New York Fed, **voter** | |
| Fri Nov 6 | 9:10 AM | Alberto Musalem | St. Louis Fed, non-voter | |
| Fri Nov 6 | 12:15 PM | Bowman | Board of Governors, **voter** | |

No Fed speakers are scheduled Tuesday Nov 3 or Wednesday Nov 4 — notably silent into the QRA and into election results.

---

## Treasury calendar

| Date | Event | Detail |
|---|---|---|
| Mon Nov 2 | 3-Month and 6-Month Bill auctions | 11:30 ET |
| Tue Nov 3 | 6-Week Bill auction | 11:30 ET |
| Wed Nov 4 | **Quarterly Refunding Statement (8:30 ET)** | Q4 financing estimates released Mon 3:00 PM ET. Watch for changes to the "maintaining nominal coupon and FRN auction sizes for at least the next several quarters" language, long-end buyback sizes, and any move to the 20y/30y auction sizes. Citi's Jason Williams team expects 20y and 30y sizes cut by $3bn each; Barclays expects no TIPS size change (Nov 10y TIPS reopening $19bn, Dec 5y $24bn, Jan 10y $21bn). |
| Wed Nov 4 | 3-Year and 10-Year note auction **announcement** | Per Treasury's tentative schedule the 3-year auctions Mon Nov 9 and the 10-year Tue Nov 10 — sizes are set at the Nov 4 statement, not yet published. |
| Thu Nov 5 | 8-Week Bill auction | 11:30 ET |

**No 2y/5y/7y/10y/20y/30y coupon auction falls inside this week** — the coupon calendar is a next-week-and-beyond story. Any calendar showing a coupon auction Mon Nov 2–Thu Nov 5 is misdated.

---

## Tier 3 / summary-only mentions

- **S&P Global PMIs** (final prints Mon and Wed), **NY Fed Consumer Inflation Expectations** (Mon 4:00 PM), **SLOOS** (Mon 2:00 PM), **Atlanta Fed GDPNow** (Mon 11:00 AM), **NFIB** (Tue 11:00 AM), **Challenger job cuts** (see date conflict below), **EIA crude stocks** (Wed 10:30 AM), weekly bill auctions, **BoE/RBA decisions** (out of scope, context only).
- **Fed Beige Book** (Oct 28), **TIC data** and **CB Consumer Confidence** (Oct reading: 91.7, +7.5 pts) are already out — nothing due this week.

---

## Date conflicts and low-confidence items

| Item | Conflict | Resolution |
|---|---|---|
| FOMC rate decision Nov 4 | One calendar (DipSonar) lists "Federal Funds Rate — 2026-11-04 14:00 ET"; another (ThriveInMarkets) says "Wednesday's FOMC held at 3.75–4.00% on a 10-2 vote" | **Rejected.** federalreserve.gov's 2026 calendar: Jan 27–28, Mar 17–18, Apr 28–29, Jun 16–17, Jul 28–29, Sep 15–16, **Oct 27–28**, Dec 8–9. The Oct 28 meeting (also a Wednesday) is what that text describes. Next decision Dec 9. |
| Challenger job cuts (Oct) | Finviz: Thu Nov 5, 5:30 AM ET. TradingEconomics: Tue Nov 3 | **Left unresolved** — Tier 3 only, no market impact either way. |
| Logan's speech | US Bank + Finviz: Thu Nov 5, 7:00 PM ET. Newsquawk lists Logan under Friday; one aggregator shows Fri 3:00 PM ET | **Resolved to Thu 7:00 PM ET** (two independent calendars agree on the same clock time and day; the outliers look like timezone renderings). |
| ISM Manufacturing day | U.S. Bank prose says Tuesday | **Resolved to Mon Nov 2** — ISM's own release calendar (Nov 2 / Nov 4) plus every other calendar agrees. |
| Midterm election day | Finviz lists "Midterm Elections 7:00 PM" under Mon Nov 2 | **Resolved to Tue Nov 3** (Election Day 2026 is Nov 3; polls close 7:00 PM ET). |
| MetaCap calendar | Day attribution and timezone labels are wrong (JOLTS/factory orders land under Monday, NFP shown as "3:30 AM ET") | **Not used** for dates/times; consulted only for cross-checks. |

---

## Next week (2026-W46) — preview

- **Tue Nov 10, 8:30 ET — CPI (Oct)**, the week's marquee release (consensus ~0.3% m/m core per TradingEconomics; Oct headline prior 0.6% m/m / 3.7% y/y per the same feed).
- **Wed Nov 11 — Veterans Day: US markets closed.** Volatility windows compress around the holiday.
- **Fri Nov 13, 8:30 ET — PPI (Oct).**
- **Wed Nov 18, 2:00 PM ET — FOMC minutes** from the Oct 27–28 meeting; the 20-year bond auction is scheduled for the same day per Treasury's tentative calendar.

---

## Source health

| Source | Query / URL | Status | Notes |
|---|---|---|---|
| Skill spec | `raw.githubusercontent.com/karizaco/maxhermes-migration/main/cloud-prompts/skills/macro-calendar-week/SKILL.md` | **ok** | 5,292 bytes, read in full |
| Window check | local bash, `TZ=America/New_York` | **ok** | 2026-11-01 15:01 ET, DOW=7 — in window |
| Federal Reserve (FOMC calendar) | `federalreserve.gov/monetarypolicy/fomccalendars.htm`, `.../monetarypolicy.htm` | **ok** | Authoritative for meeting dates; via search result content |
| BLS — JOLTS | `bls.gov/jlt/` | **ok** | Next release Nov 3, 10:00 AM ET; Aug level 7,079K |
| ISM — release calendar | `ismworld.org/supply-management-news-and-reports/reports/rob-report-calendar` | **ok** | Nov 2 (mfg) / Nov 4 (services) |
| U. Michigan — Surveys of Consumers | `sca.isr.umich.edu` | **ok** | Oct final 48.0; next prelim Nov 6, 10:00 AM ET |
| Treasury — refunding | `home.treasury.gov/.../quarterly-refunding/most-recent-quarterly-refunding-documents`, Aug 5 refunding statement | **ok** | Financing estimates Mon Nov 2 3:00 PM; statement Wed Nov 4 8:30 AM |
| Treasury — auction schedule | `home.treasury.gov/system/files/221/Tentative-Auction-Schedule.{pdf,xml}` | **ok** | Tentative; coupon auctions outside this window |
| U.S. Bank Weekly Economic Outlook | `usbank.com/corporate-and-commercial-banking/insights/economy/outlook/weekly.html` | **ok** (curl, HTTP 200) | Speaker calendar (CT) + forecasts; consensus as of Fri 10/30/2026. First `web_fetch` attempt **timed out**; retried via curl. |
| TradingEconomics calendar | `tradingeconomics.com/calendar` | **ok** (curl, HTTP 200) | Times in **UTC** — converted to ET (+4h) |
| Newsquawk / Economic Weekly / Nowflation / Polymarket / mitrade / macroodds | web_search | **ok** | Consensus cross-checks for NFP, ISM services, Michigan, JOLTS |
| Finviz economic calendar | `finviz.com/calendar/economic?dateFrom=2026-11-04` | **degraded** | Direct curl **HTTP 403** (Cloudflare interstitial); content used **only via web_search snippet** for prior/consensus and speaker ET times. Not used as sole source for any date. |
| MetaCap calendar | `metacap.si/calendar/economic/` | **ok but rejected** | Day/time labels demonstrably wrong — see Date conflicts |
| DipSonar calendar | `dipsonar.com/economic-calendar/` | **rejected** | Publishes a non-existent Nov 4 FOMC rate decision |
| thriveinmarkets.com | `thriveinmarkets.com/calendar/` | **failed** | `web_fetch` timed out (15 s); recovered via web_search snippet |
| litefinance.org weekly calendar | `litefinance.org/blog/...` | **failed** | `web_fetch` timed out; recovered via web_search snippet |
| FRED MCP (`mcp__fred__get_release_dates`) | — | **unavailable** | Not registered in this runtime; web fallback used per the runtime contract |
| `mcp__*` finance MCPs (yahoo/tradingview/shibui/stocktwits/financekit) | — | **not required** | This routine reads a release calendar, not market quotes — no quote path needed |

**errors: 0** — no MCP call was attempted, so no MCP fallback was triggered. Two `web_fetch` timeouts (litefinance, thriveinmarkets) were recovered via `web_search` snippets and by corroboration with primary sources.

**as_of_utc:** 2026-11-01 20:0x UTC. Consensus figures are pre-print and were compiled by sources between Oct 30 and Nov 1, 2026 — they can still move before each release.

---

*macro-calendar target=macro:2026-W45 tier1=3 fed_speakers=7 source=web_fallback*
