#!/usr/bin/env python3
"""Final tiering + artifact writer for Cloud cron #9 (stock-screener-daily-sweep-18:30).

Takes the TradingView universe + Yahoo bar cache and produces every file in the
skill's output contract under /workspace/daily-screens/2026-10-26/.

Method notes that MUST be reproduced in the artifact:
  * ADR gates are re-applied with TRUE 20-day ADR from Yahoo bars, not the ATR proxy.
  * Rows whose last Yahoo bar is not the session date are dropped as stale carry-overs.
  * Hernandez's theme->group funnel and the compression (VCP) screen are implemented
    with TradingView/Yahoo columns because their MCP calls are unbound.
"""
import csv
import json
import os
import statistics
import sys
from datetime import datetime, timezone

sys.path.insert(0, "/workspace/data")
from yahoo_enrich import atr14  # noqa: E402

SESSION = os.environ.get("SCREENER_SESSION", "2026-10-27")  # overridable by the runner
OUTDIR = f"/workspace/daily-screens/{SESSION}"
DATA = "/workspace/data"

STYLIST_OF = {
    "stockbee_4pct_breakout": "Stockbee", "stockbee_ep9m": "Stockbee",
    "bonde_anticipation_coil": "Stockbee",
    "qullamaggie_rs_leaders": "Qullamaggie", "qullamaggie_ep_gap": "Qullamaggie",
    "qullamaggie_parabolic_short": "Qullamaggie", "qullamaggie_parabolic_long": "Qullamaggie",
    "jeff_sun_canslim": "Jeff Sun",
    "hernandez_theme_group": "Ariel Hernandez", "hernandez_compression_vcp": "Ariel Hernandez",
    "peoplewish_adr_velocity": "Peoplewish",
}
SCREEN_TITLE = {
    "stockbee_4pct_breakout": "Stockbee / Bonde - 4% Breakout",
    "stockbee_ep9m": "Stockbee / Bonde - EP9 Million",
    "bonde_anticipation_coil": "Stockbee / Bonde - Anticipation (Coil)",
    "qullamaggie_rs_leaders": "Qullamaggie - Multi-timeframe RS Leaders",
    "qullamaggie_ep_gap": "Qullamaggie - EP (10%+ Gap)",
    "qullamaggie_parabolic_short": "Qullamaggie - 5-day Gainers (Parabolic Short)",
    "qullamaggie_parabolic_long": "Qullamaggie - 5-day Losers (Parabolic Long)",
    "jeff_sun_canslim": "Jeff Sun - CANSLIM-calibrated (partial: no sales-growth leg)",
    "hernandez_theme_group": "Ariel Hernandez - Theme -> Group -> Leaders",
    "hernandez_compression_vcp": "Ariel Hernandez - Compression (VCP)",
    "peoplewish_adr_velocity": "Peoplewish - ADR + Dollar Volume + Velocity",
}


def load_tv():
    raw = json.load(open(f"{DATA}/tv_universe_raw.json"))
    cols = raw["columns"]
    idx = {c: i for i, c in enumerate(cols)}
    rows = []
    for r in raw["rows"]:
        d = dict(zip(cols, r["d"]))
        rows.append(d)
    return rows, raw


def ycomp(sym, bars):
    b = bars.get(sym, {}).get("bars", [])
    if not b:
        return {}
    closes = [x[4] for x in b]
    out = {"y_bars": len(b),
           "y_last_bar_et": datetime.fromtimestamp(b[-1][0] - 4 * 3600, tz=timezone.utc).strftime("%Y-%m-%d"),
           "y_close": b[-1][4], "y_prev_close": closes[-2] if len(closes) > 1 else None}
    out["y_change_pct"] = (closes[-1] / closes[-2] - 1) * 100 if len(closes) > 1 else None
    win = b[-20:]
    vals = [(x[2] - x[3]) / x[4] for x in win if x[2] and x[3] and x[4]]
    out["y_adr20_pct"] = sum(vals) / len(vals) * 100 if len(vals) == 20 else None
    a14, med = atr14(b)
    out["y_atr14"] = a14
    out["y_atr_pct"] = a14 / closes[-1] * 100 if a14 else None
    out["y_atr14_median63"] = med
    out["y_atr_shrink"] = bool(a14 and med and a14 < 0.6 * med)
    if len(b) >= 20:
        h5 = max(x[2] for x in b[-5:] if x[2])
        l5 = min(x[3] for x in b[-5:] if x[3])
        h20 = max(x[2] for x in b[-20:] if x[2])
        l20 = min(x[3] for x in b[-20:] if x[3])
        out["y_range5_pct"] = (h5 - l5) / closes[-1] * 100
        out["y_range20_pct"] = (h20 - l20) / closes[-1] * 100
        out["y_ma_shrink_5d"] = bool((h5 - l5) < 0.5 * (h20 - l20))
        # VCP contraction ratio: mean 10d range / mean 50d range
        r10 = [((x[2] - x[3]) / x[4]) for x in b[-10:] if x[2] and x[3] and x[4]]
        r50 = [((x[2] - x[3]) / x[4]) for x in b[-50:] if x[2] and x[3] and x[4]]
        if len(r10) == 10 and len(r50) >= 40:
            out["y_contraction_ratio"] = (sum(r10) / 10) / (sum(r50) / len(r50))
    if len(closes) >= 15:
        out["y_velocity_14d_pct"] = (closes[-1] / closes[-15] - 1) * 100
    if len(closes) >= 6:
        out["y_gain_5d_pct"] = (closes[-1] / closes[-6] - 1) * 100
    for n in (20, 50, 200):
        out[f"y_sma{n}"] = sum(closes[-n:]) / n if len(closes) >= n else None
    if out.get("y_sma200"):
        out["y_dist_sma200_pct"] = (closes[-1] / out["y_sma200"] - 1) * 100
    return out


def fmt(v, nd=2, dash="—"):
    if v is None or v == "":
        return dash
    if isinstance(v, bool):
        return "yes" if v else "no"
    if isinstance(v, (int, float)):
        return f"{v:,.{nd}f}"
    return str(v)


def md_table(headers, rows):
    out = ["| " + " | ".join(headers) + " |",
           "|" + "|".join(["---"] * len(headers)) + "|"]
    for r in rows:
        out.append("| " + " | ".join(str(x) for x in r) + " |")
    return "\n".join(out)


def main():
    os.makedirs(OUTDIR, exist_ok=True)
    tvrows, rawmeta = load_tv()
    bars = json.load(open(f"{DATA}/yahoo_bars.json"))
    regime_raw = json.load(open(f"{DATA}/regime_raw.json"))
    stats = {"session": SESSION}

    # ---------- universe ----------
    universe = []
    for d in tvrows:
        if d["type"] != "stock" or d["exchange"] not in ("NYSE", "NASDAQ", "AMEX"):
            continue
        if not (d["close"] and d["close"] > 3):
            continue
        if not (d["market_cap_basic"] and d["market_cap_basic"] > 300_000_000):
            continue
        if not (d["average_volume_30d_calc"] and d["average_volume_30d_calc"] > 100_000):
            continue
        universe.append(d)
    stats["universe_prefilter"] = len(universe)

    # index/sector ETF rows (funds)
    funds = {d["name"]: d for d in tvrows if d["type"] == "fund"}

    def y(sym):
        return ycomp(sym, bars)

    # enrich universe with Yahoo where available (candidate names already fetched)
    ycache = {n: y(n) for n in {d["name"] for d in universe} if n in bars}
    stats["universe_with_bars"] = len(ycache)

    def row(d):
        n = d["name"]
        c = ycache.get(n, {})
        chg = d["change"]
        prev = d["close"] / (1 + chg / 100) if chg is not None and chg != -100 else None
        gap = (d["open"] / prev - 1) * 100 if (d["open"] and prev) else None
        adr_proxy = d["ATR"] / d["close"] * 100 if d["ATR"] else None
        adv = d["close"] * d["average_volume_30d_calc"] if d["average_volume_30d_calc"] else None
        dist200 = (d["close"] / d["SMA200"] - 1) * 100 if d["SMA200"] else None
        # skip-rule flags
        atr_shrink = c.get("y_atr_shrink")
        ma_shrink = c.get("y_ma_shrink_5d")
        wicky = None
        if chg is not None and chg >= 4 and d["high"] and d["low"] and d["open"]:
            wick = d["high"] - max(d["open"], d["close"])
            body = abs(d["close"] - d["open"])
            rvol = d["relative_volume_10d_calc"]
            wicky = bool(wick > body and rvol is not None and rvol < 1.2)
        d2 = None
        if c.get("y_prev_close") and c.get("y_bars", 0) >= 3:
            b = bars[n]["bars"]
            pm = (b[-2][2] + b[-2][3]) / 2
            d2 = bool(c["y_close"] < pm)
        return {
            "name": n, "exchange": d["exchange"], "sector": d["sector"],
            "industry": d["industry"], "close": d["close"], "change": chg,
            "volume": d["volume"], "mcap": d["market_cap_basic"],
            "adr_proxy": adr_proxy, "adr20": c.get("y_adr20_pct"),
            "adv_dollar": adv, "gap_pct": gap, "dist_sma200": dist200,
            "rs1m": d["Perf.1M"], "rs3m": d["Perf.3M"], "rs6m": d["Perf.6M"], "rs12m": d["Perf.Y"],
            "rvol10": d["relative_volume_10d_calc"], "sma20": d["SMA20"], "sma50": d["SMA50"],
            "sma200": d["SMA200"], "atr": d["ATR"], "perf5d": d["Perf.5D"],
            "velocity14d": c.get("y_velocity_14d_pct"),
            "gain5d": c.get("y_gain_5d_pct"),
            "last_bar": c.get("y_last_bar_et"), "y_close": c.get("y_close"),
            "y_change": c.get("y_change_pct"),
            "atr_shrink": atr_shrink, "ma_shrink_5d": ma_shrink, "wicky_breakout": wicky,
            "day2_no_follow": d2, "contraction": c.get("y_contraction_ratio"),
            "pe": d["price_earnings_ttm"], "eps_growth": d["earnings_per_share_diluted_yoy_growth_ttm"],
            "high5": d["High.5D"], "low5": d["Low.5D"], "high1m": d["High.1M"], "low1m": d["Low.1M"],
            "trend_intensity": (d["close"] / d["SMA50"]) if d["SMA50"] else None,
        }

    R = {}
    for d in universe:
        r = row(d)
        R.setdefault(r["name"], r)

    # ---------- freshness ----------
    stale = [n for n, r in R.items() if r["last_bar"] and r["last_bar"] != SESSION]
    nobar = [n for n, r in R.items() if not r["last_bar"]]
    stats["stale_rows_dropped"] = len(stale)
    stats["rows_without_yahoo_bars"] = len(nobar)
    for n in stale:
        R[n]["_stale"] = True

    def live(r):
        return not r.get("_stale") and r.get("last_bar") == SESSION

    # ---------- the screens ----------
    screens = {}

    # A. Stockbee 4% breakout
    screens["stockbee_4pct_breakout"] = [
        r for r in R.values() if live(r) and r["change"] is not None and r["change"] >= 4.0
        and r["rvol10"] is not None and r["rvol10"] > 1.0]

    # B. Stockbee EP9 million
    screens["stockbee_ep9m"] = [
        r for r in R.values() if live(r) and r["volume"] and r["volume"] >= 8_900_000]

    # K. Bonde anticipation (coil) - proxies: close/SMA50 for 7d/65d intensity, 1M range for 10d base
    screens["bonde_anticipation_coil"] = [
        r for r in R.values() if live(r) and r["trend_intensity"] and r["trend_intensity"] >= 1.05
        and r["high1m"] and r["low1m"] and (r["high1m"] - r["low1m"]) / r["close"] <= 0.08
        and r["close"] >= r["low1m"] + 0.5 * (r["high1m"] - r["low1m"])
        and r["change"] is not None and r["change"] < 4.0]

    # C. Qullamaggie RS leaders - TRUE ADR gate + stacked-MA structure
    tv150 = {d["name"]: d["SMA150"] for d in universe}
    tvrsi = {d["name"]: d["RSI"] for d in universe}
    screens["qullamaggie_rs_leaders"] = [
        r for r in R.values() if live(r)
        and ((r["rs1m"] or -999) >= 25 or (r["rs3m"] or -999) >= 50 or (r["rs6m"] or -999) >= 150)
        and r["adr20"] is not None and r["adr20"] >= 4.5
        and r["adv_dollar"] and r["adv_dollar"] >= 20_000_000
        and r["sma200"] and r["sma50"] and tv150.get(r["name"])
        and r["close"] > r["sma200"] and r["sma50"] > tv150[r["name"]] > r["sma200"]]

    # D. Qullamaggie EP 10%+ gap
    screens["qullamaggie_ep_gap"] = [
        r for r in R.values() if live(r) and r["gap_pct"] is not None and r["gap_pct"] >= 10.0
        and r["rvol10"] is not None and r["rvol10"] >= 10
        and r["adv_dollar"] and r["adv_dollar"] >= 50_000_000]

    # E. parabolic short - TRUE ADR gate
    screens["qullamaggie_parabolic_short"] = [
        r for r in R.values() if live(r) and r["perf5d"] is not None and r["perf5d"] >= 25
        and r["adv_dollar"] and r["adv_dollar"] >= 50_000_000
        and r["adr20"] is not None and r["adr20"] >= 5]

    # F. parabolic long
    screens["qullamaggie_parabolic_long"] = [
        r for r in R.values() if live(r) and r["perf5d"] is not None and -50 <= r["perf5d"] <= -25
        and r["adv_dollar"] and r["adv_dollar"] >= 50_000_000
        and r["dist_sma200"] is not None and abs(r["dist_sma200"]) < 25]

    # G. peoplewish - TRUE ADR + dollar volume, sorted by TRUE 14d velocity
    screens["peoplewish_adr_velocity"] = sorted(
        [r for r in R.values() if live(r) and r["adr20"] is not None and r["adr20"] >= 5
         and r["adv_dollar"] and r["adv_dollar"] >= 50_000_000],
        key=lambda r: -(r["velocity14d"] if r["velocity14d"] is not None else -999))

    # H. Jeff Sun CANSLIM (partial - no sales growth leg)
    screens["jeff_sun_canslim"] = [
        r for r in R.values() if live(r) and r["mcap"] and r["mcap"] > 1_000_000_000
        and r["eps_growth"] is not None and r["eps_growth"] > 25
        and r["close"] > 5 and r["change"] is not None and r["change"] > 0
        and tvrsi.get(r["name"]) is not None and 40 <= tvrsi[r["name"]] <= 80]

    # I. Hernandez theme -> group -> leaders (top-3 sector ETFs)
    top_sectors = [e["sector"] for e in regime_raw["sector_etf_rs"][:3] if e.get("sector")]
    theme_names = [e["etf"] for e in regime_raw["sector_etf_rs"][:3]]
    screens["hernandez_theme_group"] = sorted(
        [r for r in R.values() if live(r) and r["sector"] in top_sectors
         and r["pe"] is not None and r["pe"] > 0
         and r["eps_growth"] is not None and r["eps_growth"] > 0],
        key=lambda r: -(r["rs1m"] if r["rs1m"] is not None else -999))[:30]

    # J. Hernandez compression (VCP) - "screen within a screen" on the Master list
    master_names = set()
    for k, v in screens.items():
        if k != "hernandez_compression_vcp":
            master_names.update(r["name"] for r in v)
    comp = [r for r in R.values() if r["name"] in master_names and live(r)
            and r.get("contraction") is not None and r["contraction"] < 0.6
            and r["sma20"] and r["close"] > r["sma20"]]
    screens["hernandez_compression_vcp"] = comp

    # ---------- master / stalk / focus / tier-a ----------
    origins = {}
    for k, v in screens.items():
        for r in v:
            origins.setdefault(r["name"], set()).add(k)
    for n, o in origins.items():
        R[n]["_origins"] = sorted(o)
        R[n]["_stylists"] = sorted({STYLIST_OF[o] for o in o})
        R[n]["_n_stylists"] = len(R[n]["_stylists"])
        R[n]["_convergence"] = len(o)

    master = sorted([R[n] for n in origins], key=lambda r: (-r["_n_stylists"], -r["_convergence"],
                     -(r["change"] or 0)))[:200]
    stats["master"] = len(master)

    def tags(r):
        t = []
        if r.get("contraction") is not None and r["contraction"] < 0.6 and r["sma20"] and r["close"] > r["sma20"]:
            t.append("compression")
        if r.get("gap_pct") is not None and r["gap_pct"] > 4 and r.get("rvol10") and r["rvol10"] > 2:
            t.append("gap-up ready")
        if r.get("high5") and r.get("low5") and r.get("high1m") and r.get("low1m"):
            if (r["high5"] - r["low5"]) / r["close"] < 0.08 and r["close"] > r["low5"]:
                t.append("higher-low base")
        return t

    stalk = []
    for r in master:
        near = False
        if r["sma20"] and abs(r["close"] / r["sma20"] - 1) <= 0.02:
            near = True
        if r["sma50"] and abs(r["close"] / r["sma50"] - 1) <= 0.02:
            near = True
        t = tags(r)
        r["_tags"] = t
        if near and t:
            stalk.append(r)
    stalk = sorted(stalk, key=lambda r: (-r["_n_stylists"], -(r["change"] or 0)))[:50]
    stats["stalk"] = len(stalk)

    vel_sorted = sorted([r for r in master if r.get("velocity14d") is not None],
                         key=lambda r: -r["velocity14d"])[:5]
    vel_top = {r["name"] for r in vel_sorted}
    focus_pool = [r for r in master if r["_n_stylists"] >= 2 or r["name"] in vel_top]
    focus = sorted(focus_pool, key=lambda r: (-r["_n_stylists"], -r["_convergence"],
                                              -(r["change"] or 0)))[:12]
    stats["focus"] = len(focus)
    tier_a = [r for r in focus if r["_n_stylists"] >= 3][:8]
    stats["tier_a"] = len(tier_a)
    stats["screen_counts"] = {k: len(v) for k, v in screens.items()}

    # ---------- regime.json ----------
    breadth = regime_raw["breadth"]["pct_above_20dma"]
    idx_below20 = []
    for r in regime_raw["index_atr"]:
        f = funds.get(r["symbol"])
        if f and f["SMA20"] and f["close"] and f["close"] < f["SMA20"]:
            idx_below20.append(r["symbol"])
    size_cut = 50 if (idx_below20 and breadth < 40) else 0
    vix = regime_raw["vix"]
    vxv = regime_raw["vxv"]
    ratio = (vix["price"] / vxv["price"]) if (vix.get("price") and vxv.get("price")) else None
    late_cycle = any((r.get("extension_x") or 0) > 6 for r in regime_raw["index_atr"])
    regime = {"size_cut_pct": size_cut, "uncertainty": ratio > 1 if ratio else None,
              "late_cycle": late_cycle,
              "_notes": {
                  "size_cut": "size_cut_pct=50 requires (index < 20-DMA) AND (breadth<40%); "
                              f"breadth={breadth}%, indices below 20-DMA={idx_below20 or 'none'}",
                  "uncertainty": "vix_vxv_ratio is null: ^VXV and ^VXVCLS return 0 bars from Yahoo "
                                 "(Not Found). VIX leg = %.2f." % (vix.get("price") or 0),
                  "late_cycle": "max ATR%% extension vs 252d median ATR%% = %.2fx" % max(
                      (r.get("extension_x") or 0) for r in regime_raw["index_atr"]),
              }}
    json.dump(regime, open(f"{OUTDIR}/_regime-screener.json", "w"), indent=2)

    # ---------- writers ----------
    def write_csv(path, rows, cols):
        with open(path, "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
            w.writeheader()
            for r in rows:
                w.writerow(r)

    def write_screen_md(key, rows, extra_note=""):
        title = SCREEN_TITLE.get(key, key)
        lines = [f"# {title}", "",
                 f"- **Session:** {SESSION} (US/Eastern close)",
                 f"- **Source:** TradingView public scanner + Yahoo Finance daily bars",
                 f"- **Rows:** {len(rows)}",
                 f"- **Filter basis:** see `daily-sweep.md` method section", ""]
        if extra_note:
            lines += [extra_note, ""]
        if rows:
            lines.append(md_table(
                ["Ticker", "Close", "Chg%", "ADR20%", "ADV$", "RVOL10", "RS1M", "RS3M",
                 "RS6M", "DistSMA200%", "Vel14D%", "Stylists", "Flags"],
                [[r["name"], fmt(r["close"]), fmt(r["change"]), fmt(r.get("adr20")),
                  fmt(r.get("adv_dollar"), 0), fmt(r.get("rvol10")), fmt(r.get("rs1m"), 1),
                  fmt(r.get("rs3m"), 1), fmt(r.get("rs6m"), 1), fmt(r.get("dist_sma200"), 1),
                  fmt(r.get("velocity14d"), 1), r.get("_n_stylists", 1),
                  " ".join(x for x in ["atr_shrink" if r.get("atr_shrink") else "",
                                       "wicky" if r.get("wicky_breakout") else "",
                                       "ma_shrink" if r.get("ma_shrink_5d") else "",
                                       "d2_nofollow" if r.get("day2_no_follow") else ""] if x)]
                 for r in rows[:120]]))
            if len(rows) > 120:
                lines += ["", f"_Showing top 120 of {len(rows)} rows; full set in the matching CSV._"]
        else:
            lines.append("_No qualifying rows for this session._")
        lines += ["", f"_Rows are live-session only: any name whose last Yahoo bar was not "
                      f"{SESSION} was dropped as a stale carry-over._"]
        open(f"{OUTDIR}/{key}.md", "w").write("\n".join(lines) + "\n")
        write_csv(f"{OUTDIR}/{key}.csv", rows, list(rows[0].keys()) if rows else ["name"])

    # per-stylist files
    ariel = {r["name"]: r for r in screens["hernandez_theme_group"]}
    ariel.update({r["name"]: r for r in screens["hernandez_compression_vcp"]})
    stylist_rows = {
        "stockbee": [r for r in master if "Stockbee" in r["_stylists"]],
        "qullamaggie": [r for r in master if "Qullamaggie" in r["_stylists"]],
        "jeff-sun": screens["jeff_sun_canslim"],
        "ariel-hernandez": sorted(ariel.values(),
                                  key=lambda r: (-r["_n_stylists"], -(r["change"] or 0))),
        "peoplewish": screens["peoplewish_adr_velocity"],
    }
    for fn, rows in stylist_rows.items():
        lines = [f"# {fn.replace('-', ' ').title()} - {SESSION}", "",
                 f"- **Rows:** {len(rows)}",
                 f"- **Source:** TradingView public scanner (tier-2 fallback) + Yahoo Finance daily bars", ""]
        if rows:
            lines.append(md_table(
                ["Ticker", "Close", "Chg%", "ADR20%", "ADV$", "Vel14D%", "Screens", "Stylists"],
                [[r["name"], fmt(r["close"]), fmt(r["change"]), fmt(r.get("adr20")),
                  fmt(r.get("adv_dollar"), 0), fmt(r.get("velocity14d"), 1),
                  ", ".join(r.get("_origins", [])), r.get("_n_stylists", 1)] for r in rows[:120]]))
            if len(rows) > 120:
                lines += ["", f"_Showing top 120 of {len(rows)} rows; full set in the matching CSV._"]
        else:
            lines.append("_No qualifying rows for this session._")
        open(f"{OUTDIR}/{fn}.md", "w").write("\n".join(lines) + "\n")
        write_csv(f"{OUTDIR}/{fn}.csv", rows, list(rows[0].keys()) if rows else ["name"])

    for key, rows in screens.items():
        write_screen_md(key, rows)

    # merged tiers
    for fname, rows, title in (
        ("master", master, "Master list (union of all stylist screens, deduped, cap 200)"),
        ("stalk", stalk, "Stalk list (Master near 10/20-DMA with a setup-confirming tag, cap 50)"),
        ("focus", focus, "Focus list (>=2 stylists or top-5 velocity, cap 12)"),
        ("tier-a", tier_a, "Tier-A (Focus with >=3 distinct stylists, cap 8)"),
    ):
        lines = [f"# {title} - {SESSION}", "",
                 f"- **Rows:** {len(rows)}",
                 f"- **Regime:** size_cut={regime['size_cut_pct']}%, uncertainty={regime['uncertainty']}, "
                 f"late_cycle={regime['late_cycle']}", ""]
        if rows:
            lines.append(md_table(
                ["Ticker", "Close", "Chg%", "ADR20%", "ADV$", "Vel14D%", "Stylists", "Origins", "Tags", "Flags"],
                [[r["name"], fmt(r["close"]), fmt(r["change"]), fmt(r.get("adr20")),
                  fmt(r.get("adv_dollar"), 0), fmt(r.get("velocity14d"), 1), r.get("_n_stylists", 1),
                  ", ".join(r.get("_origins", []))[:70], ", ".join(r.get("_tags", [])) or "—",
                  " ".join(x for x in ["atr_shrink" if r.get("atr_shrink") else "",
                                       "wicky" if r.get("wicky_breakout") else "",
                                       "ma_shrink" if r.get("ma_shrink_5d") else "",
                                       "d2_nofollow" if r.get("day2_no_follow") else ""] if x) or "—"]
                 for r in rows]))
        else:
            lines.append("_No qualifying rows for this session._")
        open(f"{OUTDIR}/{fname}.md", "w").write("\n".join(lines) + "\n")
        write_csv(f"{OUTDIR}/{fname}.csv", rows, list(rows[0].keys()) if rows else ["name"])

    json.dump({"stats": stats, "screen_counts": {k: len(v) for k, v in screens.items()},
               "master": [r["name"] for r in master], "focus": [r["name"] for r in focus],
               "tier_a": [r["name"] for r in tier_a],
               "top_velocity": [(r["name"], r["velocity14d"]) for r in vel_sorted]},
              open(f"{DATA}/tier_out.json", "w"), indent=1)
    print(json.dumps(stats, indent=2))


if __name__ == "__main__":
    main()
