#!/usr/bin/env python3
"""One-shot patch: retarget cron #9 pipeline from session 2026-10-26 to 2026-10-27.

Changes applied (all mechanical, all asserted):
  1. SESSION / OUTDIR / hardcoded date strings in final.py, regime.py, write_summary.py.
  2. final.py writes `_regime-screener.json` (NOT `_regime.json`) -- cron #10 owns
     `_regime.json` in the same directory and cron #9 must not clobber it.
  3. yahoo_enrich.fetch gains a Yahoo symbol-alias map for class shares / preferreds
     (BRK.B -> BRK-B, ALL/PH -> ALL-PH, ...), which otherwise 404 on the chart endpoint.
  4. write_summary.py reads `_regime-screener.json`.
"""
import re
import sys

D = "/workspace/data"
OLD = "2026-10-26"
NEW = "2026-10-27"


def patch(path, fn):
    src = open(path).read()
    out = fn(src)
    if out == src:
        print(f"already patched (no-op): {path}")
        return
    open(path, "w").write(out)
    print(f"patched {path}")


# ---------------- final.py ----------------
def p_final(s):
    s = s.replace(f'SESSION = "{OLD}"', f'SESSION = "{NEW}"')
    s = s.replace('json.dump(regime, open(f"{OUTDIR}/_regime.json", "w"), indent=2)',
                  'json.dump(regime, open(f"{OUTDIR}/_regime-screener.json", "w"), indent=2)')
    assert f'SESSION = "{NEW}"' in s
    assert '_regime-screener.json' in s
    assert 'open(f"{OUTDIR}/_regime.json"' not in s
    return s


# ---------------- regime.py ----------------
def p_regime(s):
    s = s.replace(f'SESSION = "{OLD}"', f'SESSION = "{NEW}"')
    assert f'SESSION = "{NEW}"' in s
    return s


# ---------------- write_summary.py ----------------
def p_summary(s):
    s = s.replace(f'OUT = "/workspace/daily-screens/{OLD}"', f'OUT = "/workspace/daily-screens/{NEW}"')
    s = s.replace('open(f"{OUT}/_regime.json")', 'open(f"{OUT}/_regime-screener.json")')
    s = s.replace(f'/workspace/daily-screens/breadth/{OLD}.md',
                  f'/workspace/daily-screens/breadth/{NEW}.md')
    s = s.replace(f'breadth/{OLD}.md', f'breadth/{NEW}.md')
    assert NEW in s
    assert '_regime-screener.json' in s
    assert OLD not in s, "stale date left in write_summary.py"
    return s


# ---------------- yahoo_enrich.py : alias map ----------------
ALIAS_BLOCK = '''
# Yahoo symbol aliases for class shares / preferreds. TradingView writes "BRK.B" and
# "ALL/PH"; Yahoo's chart endpoint only accepts "BRK-B" and "ALL-PH". Without this the
# affected rows return 404 and are silently dropped from every screen.
ALIASES = {
    "BRK.B": "BRK-B", "BRK-B": "BRK-B", "BF.B": "BF-B", "HEI.A": "HEI-A",
    "HEI-A": "HEI-A", "ALL/PH": "ALL-PH", "ALL-PH": "ALL-PH", "MFA/PB": "MFA-PB",
    "MFA-PB": "MFA-PB", "NUE/PH": "NUE-PH", "NUE-PH": "NUE-PH", "PBF/PH": "PBF-PH",
    "PBF-PH": "PBF-PH", "RDS.A": "RDS-A", "RDS-A": "RDS-A", "WFC/WS": "WFC-PW",
    "BXP.PR": "BXP-PH", "AEP/CL": "AEP-CL", "KMB/WS": "KMB-PH", "MER.PR": "MER-PH",
    "CMA/WS": "CMA-PH", "MET/WS": "MET-PH", "ES/WS": "ES-PH", "MS/WS": "MS-PH",
    "USB/WS": "USB-PH", "TFC/WS": "TFC-PH", "DTE/WS": "DTE-PH", "PFE/WS": "PFE-PH",
    "CVX/WS": "CVX-PH", "BAC/WS": "BAC-PW", "PNC/WS": "PNC-PH", "TFC/CL": "TFC-CL",
    "SCHW/WS": "SCHW-PH", "KEY/WS": "KEY-PH", "FIT/WS": "FIT-PH", "KEY/CL": "KEY-CL",
}


def ysym(s):
    return ALIASES.get(s, s)
'''


def p_yahoo(s):
    if "def ysym(" in s:
        return s
    anchor = "def fetch(sym, tries=3):"
    assert anchor in s
    s = s.replace(anchor, ALIAS_BLOCK.strip() + "\n\n\n" + anchor, 1)
    # route the URL through the alias map
    old_url = ('f"https://query2.finance.yahoo.com/v8/finance/chart/{sym}?range=1y&interval=1d"')
    new_url = ('f"https://query2.finance.yahoo.com/v8/finance/chart/{ysym(sym)}?range=1y&interval=1d"')
    assert old_url in s
    s = s.replace(old_url, new_url)
    return s


patch(f"{D}/final.py", p_final)
patch(f"{D}/regime.py", p_regime)
patch(f"{D}/write_summary.py", p_summary)
patch(f"{D}/yahoo_enrich.py", p_yahoo)
print("ALL PATCHES OK")
