#!/usr/bin/env python3
"""Write _summary.md and breadth.md for cron #9 from the computed run data."""
import json
import csv
import os
from datetime import datetime, timezone

OUT = "/workspace/daily-screens/2026-10-26"
DATA = "/workspace/data"
reg = json.load(open(f"{DATA}/regime_raw.json"))
tier = json.load(open(f"{DATA}/tier_out.json"))
stats = tier["stats"]

raw = json.load(open(f"{DATA}/tv_universe_raw.json"))
cols = raw["columns"]
idx = {c: i for i, c in enumerate(cols)}
funds = {r["d"][idx["name"]]: r["d"] for r in raw["rows"] if r["d"][idx["type"]] == "fund"}


def f2(v, nd=2):
    try:
        return f"{float(v):,.{nd}f}"
    except (TypeError, ValueError):
        return "—"


def f0(v):
    try:
        return f"{float(v):,.0f}"
    except (TypeError, ValueError):
        return "—"


focus = list(csv.DictReader(open(f"{OUT}/focus.csv")))
tier_a = list(csv.DictReader(open(f"{OUT}/tier-a.csv")))
shorts = list(csv.DictReader(open(f"{OUT}/qullamaggie_parabolic_short.csv")))
longs = list(csv.DictReader(open(f"{OUT}/qullamaggie_parabolic_long.csv")))
eps = list(csv.DictReader(open(f"{OUT}/qullamaggie_ep_gap.csv")))
pw = list(csv.DictReader(open(f"{OUT}/peoplewish_adr_velocity.csv")))[:5]

regime = json.load(open(f"{OUT}/_regime.json"))
b = reg["breadth"]
vix = reg["vix"]

# ---------------- _summary.md ----------------
lines = [
    f"# Daily screen digest — {stats['session']}",
    "",
    f"- **Regime state:** size_cut_pct = {regime['size_cut_pct']}% "
    f"(breadth {b['pct_above_20dma']}% of S&P 500 above 20-DMA, "
    f"{len([r for r in reg['index_atr'] if r.get('extension_x')])} indices tracked) | "
    f"uncertainty = {regime['uncertainty'] if regime['uncertainty'] is not None else 'null'} (VIX {f2(vix.get('price'))}, VXV unavailable) | "
    f"late_cycle = {regime['late_cycle']} (max ATR extension "
    f"{f2(max((r.get('extension_x') or 0) for r in reg['index_atr']))}×)",
    f"- **Tier-A names (convergence ≥ 3 stylists, {len(tier_a)}):** "
    + (", ".join(f"{r['name']} ({f2(r['change'])}%)" for r in tier_a) if tier_a else "none"),
    f"- **Parabolic short candidates ({len(shorts)}):** "
    + (", ".join(f"{r['name']} +{f2(r['perf5d'],1)}% over 5d, {f2(r['dist_sma200'],1)}% vs 200-DMA"
                 for r in shorts) if shorts else "none")
    + f" | **Parabolic long candidates ({len(longs)}):** "
    + (", ".join(f"{r['name']} {f2(r['perf5d'],1)}% over 5d, {f2(r['dist_sma200'],1)}% vs 200-DMA"
                 for r in longs) if longs else "none"),
    f"- **3:55 PM reversal-bullish list:** not run — this cron fires at 18:30 ET; that screen is "
    f"valid 15:30–16:00 ET only. See `daily-sweep.md` deviation 9.",
    "",
    "---",
    "",
    f"**Focus ({len(focus)})** — ",
    "",
    "| Ticker | Close | Day | ADR20% | ADV$ | Stylists |",
    "|---|---|---|---|---|---|",
]
for r in focus:
    lines.append(f"| {r['name']} | {f2(r['close'])} | {f2(r['change'])}% | {f2(r['adr20'])} | "
                 f"${f0(float(r['adv_dollar'])/1e6)}M | {r['_n_stylists']} |")
lines += [
    "",
    f"**Top peoplewish velocity** — " + ", ".join(
        f"{r['name']} {f2(r['velocity14d'],1)}%" for r in pw),
    "",
    f"**Screen counts:** " + ", ".join(f"{k}={v}" for k, v in tier["screen_counts"].items()),
    "",
    f"**Sources:** TradingView public scanner (20,095 rows, 100% of reported total) + Yahoo "
    f"daily bars. MCP tier unbound this session — tier-2 fallback, chain terminated there. "
    f"Full method and deviations: `daily-sweep.md`.",
    "",
    f"Regime payload from this sweep: `_regime-screener.json` (cron #10 owns `_regime.json` in "
    f"this directory).",
]
open(f"{OUT}/_summary.md", "w").write("\n".join(lines) + "\n")

# ---------------- breadth.md ----------------
bl = [
    f"# Breadth & regime — {stats['session']}",
    "",
    f"- **Session:** {stats['session']} US/Eastern close (no lag)",
    "- **Sources:** TradingView public scanner (S&P 500 membership from the Wikipedia constituent "
    "list, 502 tickers) + Yahoo Finance daily bars",
    "",
    "## Breadth",
    "",
    "| Metric | Value |",
    "|---|---|",
    f"| S&P 500 members evaluated | {b['sp500_members']} |",
    f"| Above 20-DMA | {b['above_20dma']} |",
    f"| Below 20-DMA | {b['below_20dma']} |",
    f"| No data | {b['no_data']} |",
    f"| **% above 20-DMA** | **{b['pct_above_20dma']}%** |",
    f"| Cross-check vs Yahoo-computed SMA20 | {b['yahoo_crosscheck']['agree']}/"
    f"{b['yahoo_crosscheck']['of']} agree |",
    "",
    "## Index ATR extension (late-cycle test)",
    "",
    "| Symbol | Close | ATR% | Median ATR% (252d) | Extension | Last bar |",
    "|---|---|---|---|---|---|",
]
for r in reg["index_atr"]:
    bl.append(f"| {r['symbol']} | {f2(r.get('close'))} | {f2(r.get('atr_pct'),3)}% | "
              f"{f2(r.get('median_atr_pct_252'),3)}% | {f2(r.get('extension_x'))}× | "
              f"{r.get('last_bar_utc','—')} |")
bl += [
    "",
    f"**Max extension {f2(max((r.get('extension_x') or 0) for r in reg['index_atr']))}× — "
    f"late_cycle = {regime['late_cycle']}** (threshold is 6×).",
    "",
    "## Volatility",
    "",
    "| Leg | Value | Note |",
    "|---|---|---|",
    f"| VIX | {f2(vix.get('price'))} ({f2(vix.get('change_pct'))}% vs prior close) | "
    f"last bar {vix.get('last_bar_utc','—')} |",
    f"| VXV | {reg['vxv'].get('error') or '—'} | Yahoo returns 0 bars for `^VXV` and `^VXVCLS`; "
    "the VIX/VXV ratio needs both legs, so `uncertainty` is left null rather than inferred. |",
    "",
    "## Sector ETF relative strength (Hernandez theme → group)",
    "",
    "| Rank | ETF | Sector | Perf 1M | Perf 3M | Perf 6M | Composite | > 20-DMA |",
    "|---|---|---|---|---|---|---|---|",
]
for i, e in enumerate(reg["sector_etf_rs"], 1):
    bl.append(f"| {i} | {e['etf']} | {e['sector']} | {f2(e.get('perf_1m'))}% | "
              f"{f2(e.get('perf_3m'))}% | {f2(e.get('perf_6m'))}% | {f2(e.get('composite'))} | "
              f"{'yes' if e.get('above_sma20') else 'no'} |")
bl += [
    "",
    "Composite = Perf.1M + Perf.3M + Perf.6M (equal weight). The top 3 ETFs define the "
    "themes used by `hernandez_theme_group`.",
    "",
    "## Regime payload",
    "",
    "```json",
    json.dumps({k: v for k, v in regime.items() if not k.startswith("_")}, indent=2),
    "```",
    "",
    "Interpretation: breadth is healthy, so `size_cut_pct` is 0 even though SPY, QQQ, QQQE and "
    "IWM closed below their 20-DMA — the size-cut rule requires BOTH an index below its 20-DMA "
    "AND breadth under 40%. No index is near the 6× ATR-extension threshold, so `late_cycle` is "
    "false. The uncertainty flag is uncomputable this session because the VXV leg is missing.",
]
open(f"{OUT}/breadth.md", "w").write("\n".join(bl) + "\n")
os.makedirs("/workspace/daily-screens/breadth", exist_ok=True)
open("/workspace/daily-screens/breadth/2026-10-26.md", "w").write("\n".join(bl) + "\n")
print("wrote _summary.md, breadth.md, breadth/2026-10-26.md")
