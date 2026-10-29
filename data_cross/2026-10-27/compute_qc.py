#!/usr/bin/env python3
"""Cron #12 cross-asset correlation engine (Cloud, Yahoo chart fallback).

Aligns 8 proxies on the America/New_York calendar date, computes Pearson
correlations on daily log returns (primary) and price levels (appendix),
and runs the week-rolled + in-window regime comparisons.
"""
import json, os, datetime as dt
from zoneinfo import ZoneInfo
import numpy as np
import pandas as pd

NY = ZoneInfo("America/New_York")
SYMS = ["SPY", "QQQ", "IWM", "TLT", "GLD", "UUP", "EEM", "^VIX"]
DATA = "/workspace/data_cross"


def load(sym):
    d = json.load(open(f"{DATA}/{sym}.json"))["chart"]["result"][0]
    ts = d["timestamp"]
    ac = d["indicators"].get("adjclose")
    if not ac or not ac[0].get("adjclose"):
        ac = d["indicators"]["quote"][0]
    vals = ac[0]["adjclose"]
    dates, series = [], []
    for t, v in zip(ts, vals):
        if v is None:
            continue
        dte = dt.datetime.fromtimestamp(t, tz=dt.timezone.utc).astimezone(NY).date()
        dates.append(dte)
        series.append(float(v))
    s = pd.Series(series, index=pd.to_datetime(dates), name=sym).sort_index()
    s = s[~s.index.duplicated(keep="last")]
    return s, d["meta"]


frames, metas = {}, {}
for s in SYMS:
    series, meta = load(s)
    frames[s] = series
    metas[s] = meta

px = pd.DataFrame(frames)
print("=== raw per-symbol bar counts / first / last ===")
for s in SYMS:
    print(f"{s:5s} n={len(frames[s]):4d} first={frames[s].index[0].date()} last={frames[s].index[-1].date()} "
          f"regMktTime={dt.datetime.fromtimestamp(metas[s]['regularMarketTime'], tz=dt.timezone.utc).astimezone(NY).isoformat()}")

# ---- alignment on intersection of NY dates ----
common = sorted(set.intersection(*[set(frames[s].index) for s in SYMS]))
px = px.loc[common]
print(f"\nintersect dates: {len(common)}  {common[0].date()} -> {common[-1].date()}")

# dates dropped by the intersection (VIX-only sessions)
allv = set(frames["^VIX"].index)
etf = set(frames["SPY"].index)
print("VIX-only sessions dropped:", sorted(str(d.date()) for d in (allv - etf)))
print("ETF-only sessions dropped:", sorted(str(d.date()) for d in (etf - allv)))

# ---- window helper: first session strictly after (end - 6 months) ----
def window(end_date):
    end = pd.Timestamp(end_date)
    start_limit = end - pd.DateOffset(months=6)
    idx = [d for d in common if d > start_limit and d <= end]
    return idx

def corr_block(idx, basis="returns"):
    w = px.loc[idx]
    if basis == "levels":
        m = w.corr(method="pearson")
    else:
        m = np.log(w).diff().dropna().corr(method="pearson")
    return m, w

def pair_rows(m):
    out = []
    for i, a in enumerate(SYMS):
        for b in SYMS[i + 1:]:
            out.append((a, b, m.loc[a, b]))
    return out

def show_pairs(pairs, title, n=8):
    pairs = sorted(pairs, key=lambda t: -abs(t[2]))
    print(f"\n--- {title}: strongest {n} ---")
    for a, b, v in pairs[:n]:
        print(f"  {a:5s}-{b:5s} {v:+.4f}")
    print(f"--- {title}: weakest {n} ---")
    for a, b, v in pairs[-n:][::-1]:
        print(f"  {a:5s}-{b:5s} {v:+.4f}")

# ================= headline window =================
END = "2026-10-26"          # last COMPLETED session (today 10-27 is partial)
idx = window(END)
m_ret, w = corr_block(idx, "returns")
m_lvl, _ = corr_block(idx, "levels")
print(f"\n=== HEADLINE window {idx[0].date()} -> {idx[-1].date()} : {len(idx)} sessions, "
      f"{len(idx)-1} return obs ===")
print("returns matrix:\n", m_ret.round(4).to_string())

pairs = pair_rows(m_ret)
show_pairs(pairs, "HEADLINE returns", 6)
print(f"\nstrong |r|>0.7: {sum(1 for _,_,v in pairs if abs(v)>0.7)} / {len(pairs)}")
print(f"negative: {sum(1 for _,_,v in pairs if v<0)}")
print(f"near-orthogonal |r|<0.2: {[(a,b,round(v,3)) for a,b,v in pairs if abs(v)<0.2]}")

# window cumulative performance (levels basis, adjclose)
perf = (w.iloc[-1] / w.iloc[0] - 1) * 100
print("\nwindow cumulative perf %:")
for s in SYMS:
    print(f"  {s:5s} {perf[s]:+7.2f}%")

# ================= week-rolled comparison =================
PREV_END = "2026-10-16"
idx_prev = window(PREV_END)
m_prev, _ = corr_block(idx_prev, "returns")
m_prev_lvl, _ = corr_block(idx_prev, "levels")
print(f"\n=== WEEK-ROLLED prior window {idx_prev[0].date()} -> {idx_prev[-1].date()} : {len(idx_prev)} sessions ===")

deltas = []
for a, b, v in pair_rows(m_ret):
    d = v - m_prev.loc[a, b]
    deltas.append((a, b, m_prev.loc[a, b], v, d))
deltas_sorted = sorted(deltas, key=lambda t: -abs(t[4]))
print("largest |delta| (week-rolled):")
for a, b, p, c, d in deltas_sorted[:8]:
    flag = "REGIME_SHIFT" if abs(d) > 0.20 else ""
    print(f"  {a:5s}-{b:5s} {p:+.3f} -> {c:+.3f}  delta {d:+.3f} {flag}")
print(f"max |delta| = {max(abs(t[4]) for t in deltas):.4f}")

# ================= WoW vs PRIOR PUBLISHED FILE (2026-10-26.md) =================
# prior file window was 2026-04-24 -> 2026-10-23 ; reproduce it
prior_idx = [d for d in common if pd.Timestamp("2026-04-24") <= d <= pd.Timestamp("2026-10-23")]
m_prior_repro, _ = corr_block(prior_idx, "returns")
print(f"\n=== REPRO of prior file window {prior_idx[0].date()} -> {prior_idx[-1].date()} : {len(prior_idx)} sessions ===")

# published prior matrices (2026-10-26.md): FIRST matrix = returns, LATER = levels appendix.
# Must not let the later levels table overwrite the earlier returns table.
import re
txt = open("/workspace/prior_2026-10-26.md").read()
order_pub = ["SPY", "QQQ", "IWM", "TLT", "GLD", "UUP", "EEM", "^VIX"]
ROW_RE = re.compile(r"^\|\s*\*\*(\^?VIX|SPY|QQQ|IWM|TLT|GLD|UUP|EEM)\*\*\s*\|(.*)\|\s*$")
blocks, cur = [], {}
for line in txt.splitlines():
    mm = ROW_RE.match(line)
    if mm:
        cells = [c.strip().replace("**", "") for c in mm.group(2).split("|")]
        vals = [None if c in ("", "---") else float(c) for c in cells]
        cur[mm.group(1)] = vals
        if len(cur) == 8:
            blocks.append(cur); cur = {}
if cur:
    blocks.append(cur)
print(f"published matrices parsed: {len(blocks)}  (block0=returns, block1=levels appendix)")
pub_ret = blocks[0]
pub_lvl = blocks[1] if len(blocks) > 1 else None

def devs_vs(m, pubtab):
    out = []
    for i, a in enumerate(order_pub):
        for j, b in enumerate(order_pub):
            if j <= i:
                continue
            out.append((a, b, pubtab[a][j], m.loc[a, b], m.loc[a, b] - pubtab[a][j]))
    return out

devs = devs_vs(m_prior_repro, pub_ret)
worst = max(devs, key=lambda t: abs(t[4]))
print(f"REPRO vs published RETURNS matrix: max unrounded dev = {worst[4]:+.4f} "
      f"({worst[0]}-{worst[1]}, published {worst[2]:+.2f} vs repro {worst[3]:+.4f})")
if pub_lvl:
    m_plvl, _ = corr_block(prior_idx, "levels")
    dl = devs_vs(m_plvl, pub_lvl)
    wl = max(dl, key=lambda t: abs(t[4]))
    print(f"REPRO vs published LEVELS matrix:  max unrounded dev = {wl[4]:+.4f} "
          f"({wl[0]}-{wl[1]}, published {wl[2]:+.2f} vs repro {wl[3]:+.4f})")
    pub_lvl_repro_dev = round(wl[4], 5)
print(f"published vs current (true WoW) largest |delta|:")
wow = []
for a, b, pv, rv, _ in devs:
    wow.append((a, b, pv, m_ret.loc[a, b], m_ret.loc[a, b] - pv))
for a, b, p, c, d in sorted(wow, key=lambda t: -abs(t[4]))[:8]:
    flag = "REGIME_SHIFT" if abs(d) > 0.20 else ""
    print(f"  {a:5s}-{b:5s} {p:+.2f} -> {c:+.3f}  delta {d:+.3f} {flag}")
print(f"max true-WoW |delta| = {max(abs(t[4]) for t in wow):.4f}")

# ================= partial-session sensitivity =================
idx_part = [d for d in common if d > (pd.Timestamp(END) - pd.DateOffset(months=6))]
m_part, _ = corr_block(idx_part, "returns")
m_part_lvl, _ = corr_block(idx_part, "levels")
print(f"\n=== SENSITIVITY: incl. partial session {idx_part[-1].date()} ({len(idx_part)} sessions) ===")
d_ret = (m_part - m_ret).abs().max().max()
d_lvl = (m_part_lvl - m_lvl).abs().max().max()
print(f"max |delta| returns = {d_ret:.4f} ; levels = {d_lvl:.4f}")

# ================= early-half vs recent-half drift =================
half = len(idx) // 2
ie, ir = idx[:half], idx[half:]
m_e, _ = corr_block(ie, "returns")
m_r, _ = corr_block(ir, "returns")
split_date = ie[-1]
print(f"\n=== REGIME DRIFT: early {ie[0].date()}..{ie[-1].date()} ({len(ie)}) vs recent {ir[0].date()}..{ir[-1].date()} ({len(ir)}) ===")
drift = []
for a, b, v in pair_rows(m_ret):
    drift.append((a, b, m_e.loc[a, b], m_r.loc[a, b], m_r.loc[a, b] - m_e.loc[a, b]))
for a, b, e, r, d in sorted(drift, key=lambda t: -abs(t[4]))[:10]:
    flag = "REGIME_DRIFT" if abs(d) > 0.20 else ""
    print(f"  {a:5s}-{b:5s} {e:+.3f} -> {r:+.3f}  delta {d:+.3f} {flag}")

# ================= dump json for artifact writer =================
out = {
    "fetched_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
    "fetched_at_et": dt.datetime.now(NY).isoformat(),
    "headline": {
        "start": str(idx[0].date()), "end": str(idx[-1].date()),
        "sessions": len(idx), "return_obs": len(idx) - 1,
        "returns": m_ret.round(4).to_dict(),
        "levels": m_lvl.round(4).to_dict(),
        "perf_pct": {k: round(v, 2) for k, v in perf.items()},
    },
    "weekrolled": {
        "start": str(idx_prev[0].date()), "end": str(idx_prev[-1].date()),
        "sessions": len(idx_prev),
        "deltas": [{"a": a, "b": b, "prev": round(p, 4), "cur": round(c, 4), "d": round(d, 4)} for a, b, p, c, d in deltas],
    },
    "wow_vs_published": {
        "prior_file": "2026-10-26.md",
        "prior_window": [str(prior_idx[0].date()), str(prior_idx[-1].date())],
        "repro_max_dev": round(worst[4], 5),
        "repro_worst_pair": [worst[0], worst[1], worst[2], round(worst[3], 4)],
        "repro_max_dev_levels": pub_lvl_repro_dev,
        "repro_worst_pair_levels": [wl[0], wl[1], wl[2], round(wl[3], 4)],
        "pairs": [{"a": a, "b": b, "pub": p, "cur": round(c, 4), "d": round(d, 4)} for a, b, p, c, d in wow],
    },
    "partial_sensitivity": {
        "partial_date": str(idx_part[-1].date()),
        "max_delta_returns": round(d_ret, 4),
        "max_delta_levels": round(d_lvl, 4),
    },
    "drift": {
        "early": [str(ie[0].date()), str(ie[-1].date())], "early_n": len(ie),
        "recent": [str(ir[0].date()), str(ir[-1].date())], "recent_n": len(ir),
        "pairs": [{"a": a, "b": b, "e": round(e, 4), "r": round(r, 4), "d": round(d, 4)} for a, b, e, r, d in drift],
    },
    "alignment": {
        "vix_only_sessions": sorted(str(d.date()) for d in (allv - etf)),
        "etf_only_sessions": sorted(str(d.date()) for d in (etf - allv)),
        "intersect_n": len(common),
        "raw_bars": {s: len(frames[s]) for s in SYMS},
        "last_bar": {s: str(frames[s].index[-1].date()) for s in SYMS},
    },
}
json.dump(out, open("/workspace/corr_out.json", "w"), indent=1)
print("\nWROTE /workspace/corr_out.json")
