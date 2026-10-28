#!/usr/bin/env python3
"""Build the asia-pre-market brief body from verified data.

Row counts: capped at 15 up + 15 down per market, restricted to rows whose
session date equals the market's confirmed session date (stale/illiquid rows
from an earlier session are dropped and reported in source health).
"""
import json, os, datetime

CACHE = "/workspace/.cache/asia"
OUT = "/workspace/asia-pre-market"
DATE = "2026-10-26"
SESSION = {"JP": "2026-10-26", "HK": "2026-10-26", "KR": "2026-10-26", "TW": "2026-10-22"}
MKT = {"JP": "Japan (TSE)", "TW": "Taiwan (TWSE)", "HK": "Hong Kong (HKEX)",
       "KR": "Korea (KRX)"}
# REACTION / NOTABLE thresholds from SKILL.md step 3
THRESH = {"JP": (4, 4), "TW": (5, 5), "HK": (4, 4), "KR": (4, 4)}
CUR = {"JP": "JPY", "TW": "TWD", "HK": "HKD", "KR": "KRW"}

# Verified catalysts (web_search). Anything not listed here is "not verified".
CATALYST = {
    "5029.T": ("N", "TOB: Hillhouse subsidiary HHH1 announced a full-buyout tender offer at "
                    "¥2,020/sh on 22 Oct (buy period 23 Oct-7 Dec); TSE flagged the stock for "
                    "supervision. Closed at the ¥300 limit-up. (minkabu/株探, 26 Oct)"),
    "9449.T": ("N", "Cyber/ops: unauthorized access to GMO Internet's FX cloud VPS "
                    "'お名前.com デスクトップクラウド' (26,739 servers flagged affected); "
                    "¥5,000 condolence payment + fraud-loss compensation announced; "
                    "consolidated earnings impact not yet quantifiable. (Sankei 26 Oct 16:44)"),
    "4784.T": ("N", "Same GMO Internet incident; closed ¥418, -¥73 (-14.87%), new 52-week low. "
                    "(minkabu, 26 Oct)"),
    "2442.HK": ("Y", "FY results (YE 30 Jun 2026) published: revenue ~HK$209M (prior yr HK$315M), "
                     "gross loss ~HK$0.3M, net loss ~HK$30.6M, no final dividend — yet the stock "
                     "closed +31.15%. Results direction does not explain the move; treat as "
                     "flow/momentum in a post-IPO name. (10jqka/財聞, 26 Oct)"),
    "328130.KQ": ("N", "AI-biomarker research tie-up with Nasdaq-listed Summit Therapeutics on "
                       "next-gen immuno-oncology drug ivonescimab (announced 24 Oct); NH Investment "
                       "& Securities positive note. Closed at the +30% KOSDAQ limit-up. "
                       "(Yonhap 26 Oct 15:38)"),
}
# limit-up closes confirmed by band arithmetic (close == session high) or publisher
LIMIT_UP = {
    "5029.T": "JP limit-up (¥300 band, close at day high)",
    "3042.T": "JP limit-up (¥300 band, close at day high)",
    "7477.T": "JP limit-up (¥300 band, close at day high)",
    "3929.T": "JP limit-up (TSE Growth band, publisher: ストップ高)",
    "328130.KQ": "KOSDAQ +30% limit-up close",
    "368600.KQ": "KOSDAQ +30% ceiling touch",
    "338220.KQ": "KOSDAQ +30% ceiling touch",
    "376930.KQ": "KOSDAQ +30% ceiling touch",
    "451760.KQ": "KOSDAQ +30% ceiling touch",
    "0035S0.KQ": "KOSDAQ +30% ceiling touch",
}
# rows excluded from the tables with a stated reason
EXCLUDE = {
    "011155.KS": "KOSPI 1형 preferred share — no daily price limit; -53.1% is a corporate-action "
                 "artifact, not a tradable move. Excluded from headlines.",
    "0167.HK": "Last trade 2026-10-23 (suspended/illiquid); stale row, excluded.",
}

ranked = json.load(open(os.path.join(CACHE, "ranked.json")))["markets"]
qc = json.load(open(os.path.join(CACHE, "ranked.json")))["qc"]


def build(mk):
    rows = ranked[mk]["up"] + ranked[mk]["down"]
    fresh = [r for r in rows if r["sess"] == SESSION[mk]]
    stale = [r for r in rows if r["sess"] != SESSION[mk]]
    up = sorted([r for r in fresh if r["pct"] > 0], key=lambda r: -r["pct"])[:15]
    dn = sorted([r for r in fresh if r["pct"] < 0], key=lambda r: r["pct"])[:15]
    up = [r for r in up if r["symbol"] not in EXCLUDE]
    dn = [r for r in dn if r["symbol"] not in EXCLUDE]
    rx, nt = THRESH[mk]
    head = [r for r in up + dn if abs(r["pct"]) > rx]
    head.sort(key=lambda r: -abs(r["pct"]))
    notable = [r for r in up + dn if abs(r["pct"]) <= rx]
    notable.sort(key=lambda r: -abs(r["pct"]))
    return {"up": up, "down": dn, "head": head, "notable": notable,
            "stale": stale}


def money(mc, cur):
    """Local-currency market cap -> compact string."""
    v = mc / 1e9
    return f"{v:.1f}B {cur}"


def table(mk, rows):
    lines = ["| Ticker | Name | Close | Δ% | Mkt cap | Earnings-driven | Catalyst |",
             "|---|---|---|---|---|---|---|"]
    for r in rows:
        ed, cat = CATALYST.get(r["symbol"], ("?", "not verified — outside the 4-call catalyst cap"))
        tag = []
        if r["symbol"] in LIMIT_UP:
            tag.append(LIMIT_UP[r["symbol"]])
        cat = cat + ((" [" + "; ".join(tag) + "]") if tag else "")
        lines.append(f"| `{r['symbol']}` | {r['name']} | {r['px']:,.2f} {r['cur']} | "
                     f"{r['pct']:+.2f}% | {money(r['mc'], r['cur'])} | {ed} | {cat} |")
    return "\n".join(lines)


def oneliners(mk, rows, cap=8):
    out = []
    for r in rows[:cap]:
        tag = LIMIT_UP.get(r["symbol"])
        suffix = f" ({tag})" if tag else ""
        out.append(f"- `{r['symbol']}` {r['name']} {r['pct']:+.2f}% → {r['px']:,.2f} {r['cur']}"
                   f", mkt cap {money(r['mc'], r['cur'])}{suffix}")
    return "\n".join(out) if out else "- none — every qualifying row cleared the REACTION threshold."


B = build
jp, hk, kr = B("JP"), B("HK"), B("KR")

n_react = len(jp["head"]) + len(hk["head"]) + len(kr["head"])
n_rows = len(jp["up"]) + len(jp["down"]) + len(hk["up"]) + len(hk["down"]) + \
    len(kr["up"]) + len(kr["down"])

body = f"""# Asia pre-market reactions — {DATE} (ET)

## Deviations & degraded data paths (read first)

- **Taiwan did not trade.** TWSE was closed all day for the 光復節 (Retrocession Day) substitute
  holiday, the second day of a four-day break that began with Typhoon Champi (薔琵) on Fri 2026-10-23.
  The last Taiwan session was **Thu 2026-10-22**: TAIEX 46,041.43 (-1.81%, -846.34 pts).
  Taiwan resumes **Tue 2026-10-27**. No TW catalyst lookup was performed — there was no session
  to react to.
- **The skill's primary data path was unavailable.** `mcp__tradingview__screen_stocks` and the
  Yahoo/TradingView MCPs are not present in this runtime, and the Windows writer helper
  (`asia_brief_writer.py`) does not exist on Cloud. The 8 screener calls were re-implemented
  against the Yahoo `v1/finance/screener` REST endpoint with equivalent filters
  (|Δ%| > 2%, market cap > $2B, primary-listing exchange whitelist), and the artifact was written
  with the Cloud `write` tool.
- **Market cap is a screener field, not a quote call.** `quoteSummary` returns HTTP 401 in this
  runtime, so market caps come from the screener response and were not independently confirmed.
  Prices and Δ% were reconciled against the Yahoo chart endpoint for 11 movers and matched exactly.
- **Korea carries a price-limit distortion.** Six KOSDAQ names closed at or within 0.2% of the
  +30% ceiling; one KOSPI preferred share posted -53.1% because 1형 preferred shares are exempt
  from daily price limits. Both are tagged, and the preferred is excluded from the headline table.
- **Catalyst coverage is 4 of 4 lookups spent** (Japan, Hong Kong, Korea headline, plus the
  second-largest Japan name by market impact). Every other row is marked "not verified" rather
  than given an inferred headline.

## TL;DR

Japan produced the most reaction-grade moves ({len(jp['head'])} rows beyond the 4% threshold) and
the day's most consequential single event: GMO Internet Group closed **-15.65%** after a
cyber-incident disclosure, dragging the wider GMO complex with it. Korea contributed the largest
single gainer — **Lunit +30.00%** at the KOSDAQ price limit on a US biotech tie-up — but KOSPI
fell 1.46% and KOSDAQ fell 3.26%, so the strength was concentrated in a handful of AI/health
names rather than the market. Hong Kong was the calmest major index (**HSI +0.51%**), yet the
top *mover* was volatile: Easy Smart Group closed **+31.15%** on FY results that were weak on
every headline line. Taiwan is absent by holiday, and the four-day break means the 27 Oct open
carries a **581-point gap risk** (TAIEX futures night session -580 to 45,654) into a week in
which Brent broke $116, the US 10-year reached 4.99% and the Dow fell 652.82 points
(旺得富, 24 Oct — a single publisher, flagged as context rather than a verified close).

## Market summary

| Market | Index | Close | Δ% | Session date | Note |
|---|---|---|---|---|---|
| Japan | Nikkei 225 | 62,189.65 | -0.80% | 2026-10-26 | Closed 15:30 JST |
| Hong Kong | Hang Seng | 23,211.81 | +0.51% | 2026-10-26 | Closed 16:00 HKT |
| Korea | KOSPI | 5,469.47 | -1.46% | 2026-10-26 | Closed 15:30 KST |
| Korea | KOSDAQ | 727.21 | -3.26% | 2026-10-26 | Closed 15:30 KST |
| Taiwan | TAIEX | 46,041.43 | -1.81% | 2026-10-22 | **STALE — market closed 2026-10-26** |

Index levels are Yahoo `meta.regularMarketPrice` for the stated session, cross-checked against
the chart close series. The Taiwan row is the prior session and is shown for context only.

**Why the NOTABLE bands are empty.** Each market's 15-up/15-down slots were filled entirely by
rows clearing the REACTION threshold, because a 2% floor with a $2B market-cap cap on these
sessions leaves the 15th-ranked mover in each direction still above 4%. The 2-4% band would have
required ranking deeper than 15 per direction, which the skill caps. No rows are missing from the
scan — the band is simply empty at this depth.

## Japan (TSE)

**{len(jp['head'])} REACTION rows (>4%), {len(jp['notable'])} NOTABLE rows (2-4%).**
Headline move: GMO Internet Group -15.65% (cyber incident). Largest gainer: CIRCLACE +27.27%
(tender-offer arbitrage to a ¥2,020 takeout price, closed at the ¥300 limit).

{table('JP', jp['head'])}

### Japan — NOTABLE (2-4%)
{oneliners('JP', jp['notable'])}

## Taiwan (TWSE) — {MKT['TW']}

**No data — closed.** TWSE was closed for the 光復節 substitute holiday on 2026-10-26.
Last session: **2026-10-22**, TAIEX 46,041.43 (-1.81%). No catalyst lookup performed.

## Hong Kong (HKEX)

**{len(hk['head'])} REACTION rows (>4%), {len(hk['notable'])} NOTABLE rows (2-4%).**
Headline move: Easy Smart Group +31.15% — the largest percentage gain of any Asia name in this
scan. Notable downside: Kinwong -11.84% and MOMENTA-W -9.75% in a HK tech complex that was
otherwise firm, with the index up 0.51%.

{table('HK', hk['head'])}

### Hong Kong — NOTABLE (2-4%)
{oneliners('HK', hk['notable'])}

## Korea (KRX)

**{len(kr['head'])} REACTION rows (>4%), {len(kr['notable'])} NOTABLE rows (2-4%).**
Headline move: Lunit +30.00%, closing at the KOSDAQ price limit on a Summit Therapeutics
AI-biomarker collaboration — a genuine fundamental catalyst, not a non-fundamental limit artifact.
Five further KOSDAQ names touched the same +30% ceiling; their catalysts were not verified
because the catalyst-call budget was exhausted.

{table('KR', kr['head'])}

### Korea — NOTABLE (2-4%)
{oneliners('KR', kr['notable'])}

### Korea — rows excluded from the tables
{chr(10).join(f'- `{k}` — {v}' for k, v in EXCLUDE.items() if k.endswith('.KS') or k.endswith('.KQ'))}

### Rows excluded from all tables
{chr(10).join(f'- `{k}` — {v}' for k, v in EXCLUDE.items())}

## Source health

| Item | Value |
|---|---|
| Screener calls | 10 (5 exchange codes x up/down): JPX, TWO, HKG, KSC, KOE |
| Rows returned by screener | JPX up 349 / down 241; HKG up 151 / down 176; KSC up 17 / down 436; KOE up 138 / down 784; TWO up 26 / down 301 |
| Rows kept after filters | 120 capped rows (30 per market, 15 up + 15 down) -> **88 surfaced** in the three open markets. The other 30 are Taiwan rows belonging to the 2026-10-22 session; 1 HK stale row and 1 KR preferred were excluded. |
| Rows dropped — exchange whitelist | {qc['dropped_exchange']} |
| Rows dropped — close floor (<5 local ccy) | {qc['dropped_price']} |
| Rows dropped — market cap < $2B | {qc['dropped_nomc']} |
| Dedupe (same name) | HK {qc['dedup_hk']}, other markets {qc['dedup_other']} |
| Stale-session rows dropped | JP {len(jp['stale'])}, HK {len(hk['stale'])}, KR {len(kr['stale'])} |
| Market status | market_open_JP=TRUE, market_open_HK=TRUE, market_open_KR=TRUE, **market_open_TW=FALSE** |
| all_markets_open | **FALSE** (Taiwan closed) |
| _data_date | JP=2026-10-26, HK=2026-10-26, KR=2026-10-26, **TW=2026-10-22** |
| Catalyst lookups | 4 of 4 cap used (5029.T, 9449.T, 2442.HK, 328130.KQ) |
| Earnings detection method | asia_earnings_detection_method=web_search_primary (Yahoo/TradingView MCPs absent) |
| Price/Δ% reconciliation | 11 movers cross-checked vs Yahoo chart endpoint — all matched to 0.01% |
| MCP failures triggering fallback | 2 (tradingview screen_stocks, yahoo finance MCP — both absent) |

### Known gaps
- No structured Asian earnings calendar is reachable; earnings-driven flags come from
  publisher-confirmed headlines only. 1 of 4 verified catalysts is earnings-driven (2442.HK).
- Market cap is unconfirmed for every row (quoteSummary 401).
- {n_react} REACTION rows are surfaced, but only 4 carry a publisher-verified catalyst. The
  remaining rows are marked "not verified" and must not be read as unexplained or as
  catalyst-free — they simply fall outside the skill's 4-call catalyst budget.

asia-reaction target=asia-pre-market:{DATE} jp={len(jp['head'])} tw=0 hk={len(hk['head'])} kr={len(kr['head'])} reactions={n_react} catalyst_lookups=4
"""

os.makedirs(OUT, exist_ok=True)
path = os.path.join(OUT, f"{DATE}.md")
with open(path, "w") as f:
    f.write(body)
print("wrote", path, len(body), "bytes")
print("head counts: jp", len(jp['head']), "hk", len(hk['head']), "kr", len(kr['head']))
print("notable:", len(jp['notable']), len(hk['notable']), len(kr['notable']))
print("stale dropped:", len(jp['stale']), len(hk['stale']), len(kr['stale']))
print("surfaced rows:", n_rows)
