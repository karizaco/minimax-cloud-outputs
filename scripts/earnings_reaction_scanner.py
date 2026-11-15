#!/usr/bin/env python3
"""
Cron #15 earnings-reaction-scanner — production pipeline (Cloud).

Replaces the skill's absent MCP tools (mcp__tradingview-advanced__*,
mcp__financekit__*, mcp__stocktwits__*) with the TradingView PUBLIC screener,
which was verified working on 2026-10-24.

Emits the artifact to /workspace/earnings/<date>-reactions.md and a catalyst
target list to /workspace/earnings/<date>-catalyst-targets.json.

ARTIFACT CONTRACT v2 (REACTION_ARTIFACT_V2) — the contract lives in the REPO
skill `cloud-prompts/skills/earnings-reaction-scanner/SKILL.md`, which the cron
fetches at RUN time, so an edit there lands on the next fire with no redeploy.
This file is the executable form of that contract:

  * every published row carries ref_close_source, ref_close_asof and
    us_tradeable, plus a move_vs_avg_daily column;
  * a row whose reference close is older than the previous session is DROPPED
    and the drop is counted in rows_dropped_stale_ref;
  * a `## Actionable read` block sits above the tables;
  * each name appears EXACTLY ONCE, in exactly one table, with its catalyst in
    that row's last column — there is no separate `## Catalysts` section;
  * `degraded_sources` counts each degraded source separately, and the chat
    reply's `errors:` must equal that count.

Verified behaviours this script encodes (see memory topic
`earnings-calendar-data-path`):
  * `change` on ILLIQUID rows is computed against a STALE reference close.
    Tell: `change` == `Perf.W` exactly and `Perf.1D` is null. A volume floor
    removes the bogus rows (MRNA.SIX vol=25 showed +71.77%; the US line
    moved -1.25%).
  * `country` is the reliable primary-listing filter. `exchange` codes in the
    public scanner differ from the skill's priority table (EURONEXT covers
    FR/NL/BE/PT/IE, EUROTLX for IT, BX for CH, OMXCOP for DK, OMXHEX for FI,
    GPW for PL, VIE for AT, ATHEX for GR).
  * `earnings_release_date` = MOST RECENT report date; `earnings_release_next_date`
    = next scheduled. This replaces the absent financekit earnings calendar.
  * A Yahoo daily bar's ET TIME-OF-DAY STAMP SHIFTS BY ONE HOUR ACROSS A DST
    BOUNDARY (a US bar is stamped at the market open: 09:30 ET in summer,
    10:30 ET in winter; an ASX bar is stamped at the session open: 19:00 ET
    before the change, 18:00 ET after). Selecting bars by a modal time-of-day
    therefore keeps the OLDER bars and discards the NEWEST ones. Measured
    2026-11-03: 66 US rows and 21 ASX rows were dropped as `stale_reference`
    purely because of that filter, and 2026-11-04 lost 24 of 25 ASX rows on a
    healthy tape. Session selection is by DATE here, never by stamp.
"""
import json, subprocess, time, datetime, os, sys, re

# ==== PURE-HELPERS-BEGIN ============================================================
# Everything between these two markers is side-effect free: no network call is
# made, no file is written and no process is re-executed (the self-heal CALL
# sits below the END marker). The regression test imports THIS EXACT BLOCK, so
# it tests the shipped code rather than a copy of it - and it can never trigger
# the self-heal, which would otherwise overwrite the file under test. The block
# is SELF-CONTAINED: every name it uses is defined inside it.

# Bump this on every behavioural change. The self-heal guard below compares it
# against the copy in the shared repo.
SCRIPT_VERSION = "2026-11-11.2"
# CAPABILITY MARKER. The fetch ladder must demand it: a stale CDN blob can
# carry an older SCRIPT_VERSION and still parse, so SCRIPT_VERSION alone is
# not a sufficient test for "this copy has the v2 contract".
ARTIFACT_CONTRACT = "REACTION_ARTIFACT_V2"
SELF_HEALED = {"done": False, "from": None, "to": None, "source": None}

RAW_REPO = "https://raw.githubusercontent.com/karizaco/minimax-cloud-outputs"
API_OWNER = "karizaco"
API_REPO = "minimax-cloud-outputs"
SCRIPT_PATH = "scripts/earnings_reaction_scanner.py"


try:  # ET is UTC-5 in winter and UTC-4 in summer. A fixed offset mislabeled
    from zoneinfo import ZoneInfo      # every fire from 2026-11-01 to 2026-03-08
    ET = ZoneInfo("America/New_York")
except Exception:
    ET = datetime.timezone(datetime.timedelta(hours=-4))
UTC = datetime.timezone.utc
RUN_DATE = datetime.datetime.now(ET).strftime("%Y-%m-%d")
OUT_DIR = "/workspace/earnings"
CAT_DIR = "/workspace/catalog/catalysts"

US_VENUES = ["NASDAQ", "NYSE", "AMEX", "NYSEArca", "ARCA", "PCX", "BATS", "IEX"]
US_DROP = {"OTC", "PINK", "OTCBB", "GREY", "OTC MKTS", "OTCM", "CBOE"}

# market -> (home country for the country filter, keep-venue list, Yahoo suffix)
EU_MARKETS = {
    "uk":          ("United Kingdom",   ["LSE"],                              ".L"),
    "germany":     ("Germany",          ["XETR", "FWB", "MUN", "HAM", "HAN", "DUS", "GETTEX", "SWB"], ".DE"),
    "france":      ("France",           ["EURONEXT"],                         ".PA"),
    "netherlands": ("Netherlands",       ["EURONEXT"],                         ".AS"),
    "belgium":     ("Belgium",          ["EURONEXT"],                         ".BR"),
    "portugal":    ("Portugal",         ["EURONEXT"],                         ".LS"),
    "ireland":     ("Ireland",          ["EURONEXT"],                         ".IR"),
    "italy":       ("Italy",            ["EUROTLX", "MIL"],                   ".MI"),
    "switzerland": ("Switzerland",      ["BX", "SIX"],                        ".SW"),
    "spain":       ("Spain",            ["BME"],                              ".MC"),
    "sweden":      ("Sweden",           ["OMXSTO"],                           ".ST"),
    "norway":      ("Norway",           ["OSL"],                              ".OL"),
    "denmark":     ("Denmark",          ["OMXCOP"],                           ".CO"),
    "finland":     ("Finland",          ["OMXHEX"],                           ".HE"),
    "poland":      ("Poland",           ["GPW"],                              ".WA"),
    "austria":     ("Austria",          ["VIE"],                              ".VI"),
    "greece":      ("Greece",           ["ATHEX"],                            ".AT"),
}
ASX_SUFFIX = ".AX"

# ---------------------------------------------------------------- run mode
# "scan"   the 08:00 ET scan (default): US + EU/UK + AU + APAC/Gulf.
# "settle" the 12:15 ET settlement pass: the EU/UK session has CLOSED, so the
#          same rows are republished with their SETTLED close and move, and the
#          08:00 ET scan move is carried alongside so the reader can see how
#          much of the reaction actually survived. The US session is OPEN at
#          12:15 ET, so the US passes are skipped entirely - publishing a live
#          US intraday price as a "close" is worse than publishing nothing.
RUN_MODE = "scan"
if "--mode" in sys.argv:
    _mi = sys.argv.index("--mode")
    if _mi + 1 < len(sys.argv):
        RUN_MODE = sys.argv[_mi + 1]
SETTLE_MODE = (RUN_MODE == "settle")
OUT_NAME = f"{RUN_DATE}-reactions-settled.md" if SETTLE_MODE else f"{RUN_DATE}-reactions.md"
MORNING_ARTIFACT = f"{RUN_DATE}-reactions.md"

# ------------------------------------------------------- APAC / Gulf markets
# Added 2026-11-11. Every market here CLOSES BEFORE the 08:00 ET fire, so they
# take the same SETTLED treatment as ASX and carry no live-session caveat:
#   India 05:00 ET | Thailand 04:30 | Indonesia 04:00 | Singapore 04:00 |
#   China 02:00 | New Zealand 22:45 the previous day | Saudi Arabia 07:00
# (the EU/UK session, by contrast, is still OPEN at 08:00 ET - it closes
# 11:30 ET in winter - which is why the EU rows carry a settlement state).
#
# Screener market slugs verified live on 2026-11-10/11: india, thailand,
# indonesia, china, singapore, newzealand, ksa. Note `ksa`, NOT `saudiarabia`
# (that slug 404s) and `uae` for the Gulf (its session closes 08:00-09:00 ET,
# so it is NOT included - it would be a live row).
APAC_MARKETS = {
    "india":      ("India",       ["NSE", "BSE"],   ".NS"),
    "thailand":   ("Thailand",    ["SET"],          ".BK"),
    "indonesia":  ("Indonesia",   ["IDX"],          ".JK"),
    "china":      ("China",       ["SSE", "SZSE"],  ".SS"),
    "singapore":  ("Singapore",   ["SGX"],          ".SI"),
    "newzealand": ("New Zealand", ["NZX"],          ".NZ"),
    "ksa":        ("Saudi Arabia", ["TADAWUL"],     ".SR"),
}
# The Yahoo suffix follows the VENUE, not the market: a Shenzhen listing is
# .SZ while a Shanghai one is .SS, and an Indian BSE line is .BO while an NSE
# line is .NS. One suffix per market would silently resolve half the rows -
# and a row whose reference close cannot be resolved is DROPPED.
YAHOO_SUFFIX_BY_EXCHANGE = {
    "NSE": ".NS", "BSE": ".BO", "SSE": ".SS", "SZSE": ".SZ",
    "SET": ".BK", "IDX": ".JK", "SGX": ".SI", "NZX": ".NZ", "TADAWUL": ".SR",
}

# The countries a published foreign row can come from. Used to bound the US
# line index (which US-listed line corresponds to a foreign issuer).
FOREIGN_HOME_COUNTRIES = ([v[0] for v in EU_MARKETS.values()] + ["Australia"]
                          + [v[0] for v in APAC_MARKETS.values()])

MIN_VOLUME = 10000          # removes stale-reference rows (validated) - DO NOT LOWER
SCAN_RETRIES = 3
REF_CLOSE_TOLERANCE_PCT = 0.5   # |implied ref - Yahoo ref| above this = stale reference
PREMARKET_OPEN_ET = datetime.time(4, 0)
PREMARKET_CLOSE_ET = datetime.time(9, 30)
AVG_MOVE_WINDOW = 20             # sessions used for the mean absolute daily move
CATALYST_BUDGET = {"US": 5, "EU": 3, "AU": 2, "APAC": 3}
# Rows per market. The EU/UK table was 28% Sweden over nine runs (73 of 264
# rows) while Belgium and Greece never appeared once - the cap makes the table
# a market census instead of a Nordic index. The overall cap still binds.
EU_MARKET_CAP = 4
APAC_MARKET_CAP = 3
# A name is "due to report" when the screener's NEXT-report date falls inside
# this window. The NEXT date is the reliable half of the field: the LAST-report
# date lags (it read 2025-02-13 for a name that reported the previous day).
EARNINGS_DUE_WINDOW_DAYS = 14

SCANNER_COLS = ["name", "close", "change", "change_abs", "volume", "market_cap_basic",
                "exchange", "country", "Perf.W", "currency",
                "premarket_change", "postmarket_change", "premarket_close", "premarket_volume",
                "earnings_release_date", "earnings_release_next_date"]
IDX = {c: i for i, c in enumerate(SCANNER_COLS)}

health = {"scanner_calls": 0, "scanner_errors": 0, "yahoo_calls": 0, "yahoo_errors": 0,
          "yahoo_429": 0, "empty_markets": [], "cross_check": {"agree": 0, "mismatch": 0,
          "unverified": 0, "stale": 0, "drift": [], "by_mode": {}, "mismatch_detail": []},
          "premarket_check": {"checked": 0, "within_1pp": 0, "within_3pp": 0,
                              "outliers": [], "unavailable": 0},
          "rows_dropped_stale_ref": 0, "rows_dropped_unresolved_ref": 0,
          "us_line_index_ok": True}
DEGRADED = []          # list of (source, detail) - each degraded source counted once


def degrade(source, detail):
    """Record a degraded source. The reply's `errors:` equals len(DEGRADED)."""
    for s, d in DEGRADED:
        if s == source:
            return
    DEGRADED.append((source, detail))


# --------------------------------------------------------------------- ET window
def premarket_window_utc(day):
    """(start_utc, end_utc) of the US pre-market window on an ET calendar day.

    04:00-09:30 ET, converted with zoneinfo, so the UTC bounds are 09:00-14:30
    in winter (EST, UTC-5) and 08:00-13:30 in summer (EDT, UTC-4). A hardcoded
    offset silently shifts the window by an hour for half the year.
    """
    start = datetime.datetime.combine(day, PREMARKET_OPEN_ET, tzinfo=ET)
    end = datetime.datetime.combine(day, PREMARKET_CLOSE_ET, tzinfo=ET)
    return (start.astimezone(UTC), end.astimezone(UTC))


def in_premarket_window(dt_et):
    """True when an ET datetime falls inside 04:00-09:30 ET."""
    t = dt_et.timetz().replace(tzinfo=None)
    return PREMARKET_OPEN_ET <= t < PREMARKET_CLOSE_ET


def select_premarket_bars(bars, now_et):
    """Keep the 1-minute bars stamped inside today's 04:00-09:30 ET window.

    bars: [(epoch, close)] oldest -> newest. Returns [(et_datetime, close)].
    The comparison is done in UTC against the DST-correct window bounds, so a
    bar at 09:15 ET IS inside the window (the pre-open auction print) and a bar
    at 03:50 ET is not.
    """
    start, end = premarket_window_utc(now_et.date())
    out = []
    for t, c in bars:
        if c is None:
            continue
        ts = datetime.datetime.fromtimestamp(t, UTC)
        if start <= ts < end:
            out.append((datetime.datetime.fromtimestamp(t, ET), c))
    return out


# --------------------------------------------------------------- session bars
def et_date(epoch):
    return datetime.datetime.fromtimestamp(epoch, ET).strftime("%Y-%m-%d")


def resolve_session_bars(bars, live_session, now_et):
    """Resolve a symbol's session bars into the base the screener's move uses.

    bars: [(epoch, close)] daily, oldest -> newest, one bar per session.

    Returns a dict, or None when there is not enough history:

      last / last_date  the most recent bar. This is the price the screener's
                        `close` column carries - a settled session close for a
                        closed venue, an in-progress price for a live one.
      ref / ref_date    the bar IMMEDIATELY BEFORE `last`. This is the base the
                        screener's `change` is measured against, so it is the
                        reference close of the row.
      prior_close       the most recent COMPLETED session's close - the base an
                        extended-hours (pre-market) percentage is measured
                        against.
      avg_daily_move    the mean absolute close-to-close move (%) over the last
                        AVG_MOVE_WINDOW completed sessions.
      mode              "live" | "closed".

    WHY NO TIME-OF-DAY FILTER: Yahoo stamps a daily bar at the session open in
    the venue's local time, so the ET stamp of the SAME session moves by one
    hour across a DST boundary (a US bar: 09:30 ET summer, 10:30 ET winter; an
    ASX bar: 19:00 ET before the change, 18:00 ET after). Selecting bars by a
    modal time-of-day therefore keeps the OLDER bars and discards the NEWEST
    ones - which silently rolled the base back to the PRIOR-PRIOR session and
    dropped 88 of 130 rows on 2026-11-03 and 24 of 25 ASX rows on 2026-11-04.
    Selection here is by DATE and order, never by stamp.
    """
    if len(bars) < 2:
        return None
    last_t, last_c = bars[-1]
    ref_t, ref_c = bars[-2]
    last_date = et_date(last_t)
    is_live = bool(live_session) and last_date == now_et.strftime("%Y-%m-%d")
    completed = list(bars[:-1]) if is_live else list(bars)
    # The move of the session BEFORE the one the screener reports. For a closed
    # venue the reported session is completed[-1] and the one before it is
    # completed[-2]; for a live venue the reported session is the in-progress
    # bar and the last completed session is completed[-1].
    prev_move = None
    seq = completed if is_live else completed[:-1]
    if len(seq) >= 2 and seq[-2][1]:
        prev_move = (seq[-1][1] - seq[-2][1]) / seq[-2][1] * 100.0
    avg = None
    if len(completed) >= 3:
        window = completed[-AVG_MOVE_WINDOW:]
        moves = []
        for i in range(1, len(window)):
            prev, cur = window[i - 1][1], window[i][1]
            if prev:
                moves.append(abs(cur - prev) / prev * 100.0)
        if moves:
            avg = sum(moves) / len(moves)
    return {
        "last": last_c, "last_date": last_date,
        "ref": ref_c, "ref_date": et_date(ref_t),
        "prior_close": (ref_c if is_live else last_c),
        "prior_close_date": (et_date(ref_t) if is_live else last_date),
        "avg_daily_move": avg,
        "prev_move": prev_move,
        "mode": "live" if is_live else "closed",
        "n_completed": len(completed),
    }



# ------------------------------------------------------- session-date calendar
# The NYSE holidays are the only exchange calendar carried here, because the US
# reference close is the one that must never be older than the previous
# session. EU/UK/AU use the weekday rule (their holidays are not modelled -
# a row whose base crosses a local holiday is still published, because its
# base IS the immediately prior session of that venue).
NYSE_HOLIDAYS_2026 = {
    "2026-01-01", "2026-01-19", "2026-02-16", "2026-04-03", "2026-05-25",
    "2026-06-19", "2026-07-03", "2026-09-07", "2026-11-26", "2026-12-25",
}


def _d(s):
    return datetime.datetime.strptime(s, "%Y-%m-%d").date()


def prior_session_date(date_str, venue="US"):
    """The session immediately before `date_str` for the venue, or None."""
    try:
        d = _d(date_str)
    except Exception:
        return None
    cur = d - datetime.timedelta(days=1)
    for _ in range(12):
        if cur.weekday() < 5:
            if venue != "US" or cur.isoformat() not in NYSE_HOLIDAYS_2026:
                return cur.isoformat()
        cur -= datetime.timedelta(days=1)
    return None


def stale_reference_date(row_ref, venue):
    """True when the row's reference close is older than the previous session.

    Two independent tests:
      * for the US - where the NYSE calendar is known and the bar's ET date IS
        the session date - the base must not be older than the previous session;
      * everywhere, the feed must not have skipped a session: a gap of more
        than 4 days between the base and the reported session means the base is
        not the immediately prior session (a weekend plus a holiday is 4 days).

    The calendar test is US-only on purpose. An ASX bar is dated by its
    session OPEN, which is 19:00 ET the previous day, so the base of the
    session that closed at 02:00 ET on D is dated D-2 - a weekday test would
    read every ASX row as stale and empty the AU table (it did exactly that
    on the first run of this change: 25 of 25 ASX rows dropped).
    """
    base = row_ref.get("ref_close_asof")
    sess = row_ref.get("session_asof")
    if not base or not sess:
        return False, "missing dates"
    if venue == "US":
        prev = prior_session_date(sess, venue)
        if prev and base < prev:
            return True, f"base {base} is older than the previous US session {prev}"
    try:
        gap = (_d(sess) - _d(base)).days
    except Exception:
        return False, "unparsable dates"
    if gap > 4:
        return True, f"the feed skipped a session (base {base} -> session {sess}, {gap} days)"
    if gap < 1:
        return True, f"the base ({base}) is not before the session ({sess})"
    return False, ""



def _valid_script(text):
    """True only for a body that really is this pipeline, at the v2 contract.

    A GitHub 403/404 body is NOT empty. The unauthenticated contents API
    returns one often from this egress IP (measured 2026-11-04: 8 of 20 calls
    were HTTP 403 "API rate limit exceeded for 47.253.4.207"), so saving that
    JSON as the script would break the run. Check the BODY, never the status.

    The CAPABILITY MARKER is required as well as SCRIPT_VERSION: an older but
    perfectly parseable copy of this file carries SCRIPT_VERSION and would
    otherwise pass, and a stale copy silently runs the OLD procedure — which
    is the exact failure this fleet's fetch ladder exists to prevent.
    """
    if not text or "SCRIPT_VERSION" not in text:
        return False
    if ARTIFACT_CONTRACT not in text:
        return False
    try:
        compile(text, "<remote>", "exec")
    except Exception:
        return False
    return True


def _ver_key(v):
    """Comparable key for a YYYY-MM-DD.N version string."""
    return tuple(int(x) for x in re.findall(r"\d+", v or "")) or (0,)


def _fetch_remote_script():
    """Return (text, source) for the current shared-repo copy of this script.

    Ordered by AUTHORITATIVENESS, not speed. Measured 2026-11-04 on a
    same-path modification: the contents API and the GitHub connector served the
    new bytes in 1s, raw.githubusercontent took 284s, and jsDelivr was still
    serving the OLD bytes after 8 minutes (it was 15h stale on a real file
    that day). The CDN copies are the LAST resort, not the default.
    """
    # 1. GitHub connector - authenticated, authoritative, not CDN-cached.
    try:
        args = json.dumps({"owner": API_OWNER, "repo": API_REPO,
                           "path": SCRIPT_PATH, "ref": "refs/heads/main"})
        r = subprocess.run(["mcode-tools", "connector", "call",
                            "connector__github__get_file_contents", "--args", args],
                           capture_output=True, text=True, timeout=90)
        if r.returncode == 0 and r.stdout.strip():
            blocks = json.loads(r.stdout)
            text = ""
            if isinstance(blocks, list):
                for blk in blocks:
                    if isinstance(blk, dict):
                        res = blk.get("resource") or {}
                        if isinstance(res, dict) and res.get("text"):
                            text = res["text"]
            if _valid_script(text):
                return text, "connector"
    except Exception:
        pass
    # 2. contents API with the sandbox token (5000/hr, not 60/hr).
    token = os.environ.get("GITHUB_TOKEN", "")
    if token:
        try:
            r = subprocess.run(["curl", "-sS", "-L", "--max-time", "30",
                                "-H", "Accept: application/vnd.github.raw",
                                "-H", "Authorization: Bearer " + token,
                                f"https://api.github.com/repos/{API_OWNER}/{API_REPO}/contents/{SCRIPT_PATH}?ref=main"],
                               capture_output=True, text=True, timeout=45)
            if _valid_script(r.stdout):
                return r.stdout, "api-token"
        except Exception:
            pass
    # 3. contents API without a token (often 403 from this egress IP).
    try:
        r = subprocess.run(["curl", "-sS", "-L", "--max-time", "30",
                            "-H", "Accept: application/vnd.github.raw",
                            f"https://api.github.com/repos/{API_OWNER}/{API_REPO}/contents/{SCRIPT_PATH}?ref=main"],
                           capture_output=True, text=True, timeout=45)
        if _valid_script(r.stdout):
            return r.stdout, "api"
    except Exception:
        pass
    # 4. CDN copies - last resort; they can serve stale bytes for minutes to hours.
    for ref in ("refs/heads/main", "main"):
        try:
            r = subprocess.run(["curl", "-sS", "-L", "--max-time", "30",
                                f"{RAW_REPO}/{ref}/{SCRIPT_PATH}"],
                               capture_output=True, text=True, timeout=45)
            if _valid_script(r.stdout):
                return r.stdout, "raw-" + ref
        except Exception:
            pass
    return None, None


def _self_heal():
    """Replace this file with the current shared-repo copy when it differs.

    The cron fetches the pipeline over HTTP and a CDN copy can serve stale
    bytes after a push (measured 2026-11-04: raw.githubusercontent was 284s
    behind on a same-path edit, jsDelivr 15h behind). A stale fetch silently
    undoes a fix, so the authoritative copy is fetched and compared
    BYTE-FOR-BYTE.

    The previous guard compared SCRIPT_VERSION first and returned early when the
    versions matched, which made the byte comparison unreachable - so a fix
    pushed WITHOUT a version bump never reached the fleet. Content is compared
    FIRST here. The version only decides whether the remote copy is NEWER (an
    older copy is never adopted). The repo is the source of truth, so an equal
    version with different content IS adopted - that is exactly the case the
    old guard dropped on the floor.
    """
    try:
        here = os.path.abspath(__file__)
        with open(here, "r") as fh:
            local = fh.read()
        remote, source = _fetch_remote_script()
        if not remote or remote == local:
            return
        rver_m = re.search(r'SCRIPT_VERSION\s*=\s*"([^"]+)"', remote)
        lver_m = re.search(r'SCRIPT_VERSION\s*=\s*"([^"]+)"', local)
        rver = rver_m.group(1) if rver_m else ""
        lver = lver_m.group(1) if lver_m else ""
        if lver and rver and _ver_key(rver) < _ver_key(lver):
            return                      # never downgrade to an older copy
        with open(here, "w") as fh:
            fh.write(remote)
        # The re-exec replaces this process, so the flag travels in the env.
        os.environ["_EARNINGS_SELF_HEALED"] = f"{lver or '?'}->{rver or '?'}|{source}"
        os.execv(sys.executable, [sys.executable, here] + sys.argv[1:])
    except Exception:
        return


# ==== PURE-HELPERS-END ============================================================
_self_heal()

_h = os.environ.get("_EARNINGS_SELF_HEALED", "")
if _h:
    _parts = _h.split("|")
    _v = _parts[0].split("->")
    SELF_HEALED["done"] = True
    SELF_HEALED["from"] = _v[0] if len(_v) > 0 else "?"
    SELF_HEALED["to"] = _v[1] if len(_v) > 1 else "?"
    SELF_HEALED["source"] = _parts[1] if len(_parts) > 1 else "?"


# ----------------------------------------------------------------- HTTP helpers
def _curl(args, timeout=45):
    return subprocess.run(["curl", "-sS", "-m", str(timeout)] + args,
                          capture_output=True, text=True)


def scan(market, filters, rng=(0, 200), sort=None, cols=None):
    body = {"filter": filters, "options": {"lang": "en"}, "markets": ["america"],
            "symbols": {"query": {"types": []}, "tickers": []},
            "columns": cols or SCANNER_COLS,
            "sort": sort or {"sortBy": "change", "sortOrder": "desc"},
            "range": list(rng)}
    url = f"https://scanner.tradingview.com/{market}/scan"
    for attempt in range(SCAN_RETRIES):
        r = _curl(["-X", "POST", url, "-H", "Content-Type: application/json",
                   "-d", json.dumps(body)])
        health["scanner_calls"] += 1
        try:
            d = json.loads(r.stdout)
            if "data" in d:
                return d
        except Exception:
            pass
        health["scanner_errors"] += 1
        time.sleep(2 * (attempt + 1))
    return {"data": [], "totalCount": 0}


def scan_or_empty(market, filters, rng=(0, 200), sort=None):
    """scan(), except every pass but the EU/UK one is skipped in the settle pass.

    At 12:15 ET the US cash session is OPEN, so the screener's `close` and
    `change` for a US name are live intraday values. Publishing those as a
    session close would be a fabricated settled price - the settlement pass
    therefore runs the EU/UK passes only, and skips the US, ASX and APAC/Gulf
    passes (their rows belong to the 08:00 ET artifact).
    """
    if SETTLE_MODE and market not in EU_MARKETS:
        return {"data": [], "totalCount": 0}
    return scan(market, filters, rng, sort)


def yahoo_daily_bars(symbol):
    """Yahoo daily chart bars for a symbol: [(epoch, close)] oldest -> newest.

    3 months of daily bars, which also gives the 20-session window the mean
    absolute daily move is computed over.
    """
    r = _curl(["-A", "Mozilla/5.0",
               f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
               "?interval=1d&range=3mo"], timeout=25)
    health["yahoo_calls"] += 1
    if "429" in r.stdout[:200] or not r.stdout.strip():
        health["yahoo_429"] += 1
        return None
    try:
        res = json.loads(r.stdout)["chart"]["result"][0]
        q = res["indicators"]["quote"][0]
        return [(t, c) for t, c in zip(res["timestamp"], q["close"]) if c is not None]
    except Exception:
        health["yahoo_errors"] += 1
        return None


def yahoo_pct(symbol, live_session=False, now_et=None):
    """Independent daily % change from Yahoo, plus the reference close.

    Returns a dict {pct, last_close, ref_close, date, mode, avg_daily_move} or
    None. `ref_close` is the close the move is measured AGAINST - the number a
    stale screener row gets wrong. The cross-check validates that base rather
    than the price, because a live market legitimately moves between two
    snapshots.

    TWO Yahoo feed quirks are handled, both verified against the raw bars:

    1. ASX trailing LIVE-stamp bar. Yahoo's ASX feed appends a trailing bar
       stamped at a different time-of-day than the completed daily bars
       (2026-10-24: SRL.AX had 10 completed bars at 19:00 ET plus one at
       01:10 ET). The bar selection is by DATE and order - see
       resolve_session_bars - never by a modal time-of-day, which is what used
       to discard the newest sessions across a DST boundary.

    2. LIVE EU/UK session bar. On a weekday the EU/UK cash markets are
       mid-session at 08:00 ET, and Yahoo's daily feed carries an in-progress
       bar. The base is then the last COMPLETED session, not the bar before
       that. `live_session` must be set by the CALLER, not inferred from the
       data: an ASX feed's trailing live-stamp bar is also dated today in ET.
    """
    now_et = now_et or datetime.datetime.now(ET)
    bars = yahoo_daily_bars(symbol)
    if not bars:
        return None
    s = resolve_session_bars(bars, live_session, now_et)
    if s is None:
        return None
    pct = (s["last"] - s["ref"]) / s["ref"] * 100 if s["ref"] else None
    return {"pct": round(pct, 3) if pct is not None else None,
            "last_close": round(s["last"], 4),
            "ref_close": round(s["ref"], 4),
            "date": s["last_date"],
            "ref_date": s["ref_date"],
            "prior_close": round(s["prior_close"], 4),
            "prior_close_date": s["prior_close_date"],
            "avg_daily_move": round(s["avg_daily_move"], 3) if s["avg_daily_move"] else None,
            "prev_move": round(s["prev_move"], 3) if s["prev_move"] is not None else None,
            "mode": s["mode"]}


def yahoo_premarket(symbol, prior_close, now_et=None):
    """Independent US pre-market % for a ticker.

    Returns (pct, as_of_ET_time) or None. Uses the 1-minute chart with
    includePrePost, keeping only bars stamped inside today's 04:00-09:30 ET
    window. prior_close is the last COMPLETED session's close - the base the
    pre-market % is measured against.
    """
    if not prior_close:
        return None
    now_et = now_et or datetime.datetime.now(ET)
    r = _curl(["-A", "Mozilla/5.0",
               f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
               "?interval=1m&range=1d&includePrePost=true"], timeout=30)
    health["yahoo_calls"] += 1
    try:
        res = json.loads(r.stdout)["chart"]["result"][0]
        if "timestamp" not in res:
            return None
        q = res["indicators"]["quote"][0]
        raw = list(zip(res["timestamp"], q["close"]))
        pre = select_premarket_bars(raw, now_et)
        if not pre:
            return None
        last_dt, last_c = pre[-1]
        return (round((last_c - prior_close) / prior_close * 100, 3),
                last_dt.strftime("%H:%M"))
    except Exception:
        health["yahoo_errors"] += 1
        return None



def cross_check(name, tv_pct, tv_close, suffix, region, live_session=False, venue="US"):
    """Resolve and validate one row's reference close.

    The screener's `change` and `close` are internally consistent, so the
    implied reference close (close / (1 + change/100)) can be compared with
    Yahoo's own reference close. A match proves the move was measured against
    the TRUE prior close. A mismatch means the row was measured against a
    STALE reference - a phantom move that must not be published.

    This is the HARD GATE. It runs BEFORE any table is built, and a row that
    fails it is dropped and COUNTED (rows_dropped_stale_ref) rather than
    silently filtered.

    The percentages themselves are NOT compared directly on live markets:
    Yahoo's bar is fetched seconds-to-minutes after the screener snapshot, so
    a fast-moving name drifts by design. The drift is recorded, not flagged.

    Returns the row's reference metadata, or None when the row must not be
    published.
    """
    sym = f"{name.replace(' ', '-').replace('_', '-')}{suffix}"
    y = yahoo_pct(sym, live_session=live_session, now_et=NOW_ET)
    if y is None:
        health["cross_check"]["unverified"] += 1
        # The row cannot be published: its base is unverifiable. Count the drop HERE,
        # in the function that decides, so every pass counts it - the US headline,
        # US QUIET, EU and AU passes all drop a row whose cross_check returns None.
        health["rows_dropped_unresolved_ref"] += 1
        degrade("yahoo_chart_api.reference_close_unresolved",
                f"{sym}: the reference close could not be resolved (429 or a bad body)")
        return None
    cc = health["cross_check"]
    drift = tv_pct - y["pct"]
    implied = ref_delta = None
    if tv_close and y["ref_close"]:
        implied = tv_close / (1 + tv_pct / 100.0)
        ref_delta = (implied - y["ref_close"]) / y["ref_close"] * 100
    meta = {"ref_close": y["ref_close"], "ref_close_source": "yahoo_chart_daily",
            "ref_close_asof": y["ref_date"], "session_asof": y["date"],
            "prior_close": y["prior_close"], "prior_close_asof": y["prior_close_date"],
            "avg_daily_move": y["avg_daily_move"], "prev_move": y.get("prev_move"),
            "mode": y["mode"], "yahoo_pct": y["pct"], "drift": round(drift, 3)}
    if ref_delta is not None and abs(ref_delta) > REF_CLOSE_TOLERANCE_PCT:
        cc["stale"] += 1
        cc["mismatch"] += 1
        cc["mismatch_detail"].append(
            {"region": region, "symbol": sym, "tv": round(tv_pct, 3), "yahoo": y["pct"],
             "delta": round(drift, 3), "ref_delta_pct": round(ref_delta, 3),
             "tv_implied_ref": round(implied, 4), "yahoo_ref": y["ref_close"],
             "yahoo_date": y["date"], "yahoo_ref_date": y["ref_date"],
             "verdict": "stale_reference"})
        health["rows_dropped_stale_ref"] += 1
        return None
    stale, why = stale_reference_date(meta, venue)
    if stale:
        cc["stale"] += 1
        cc["mismatch"] += 1
        cc["mismatch_detail"].append(
            {"region": region, "symbol": sym, "tv": round(tv_pct, 3), "yahoo": y["pct"],
             "delta": round(drift, 3), "ref_delta_pct": None,
             "tv_implied_ref": round(implied, 4) if implied else None,
             "yahoo_ref": y["ref_close"], "yahoo_date": y["date"],
             "yahoo_ref_date": y["ref_date"], "verdict": "stale_reference_date",
             "why": why})
        health["rows_dropped_stale_ref"] += 1
        return None
    cc["agree"] += 1
    cc["drift"].append(round(drift, 3))
    cc["by_mode"][y["mode"]] = cc["by_mode"].get(y["mode"], 0) + 1
    return meta


# ------------------------------------------------------------- US line index
LEGAL_SUFFIXES = {
    "inc", "incorporated", "ltd", "limited", "nv", "ag", "sa", "ab", "asa", "oy", "plc",
    "co", "company", "corp", "corporation", "group", "holdings", "holding", "se", "kg",
    "spa", "as", "aps", "is", "ir", "bv", "pty", "gmbh", "sarl", "sl", "kk", "aas", "noh",
}
NAME_NOISE = {
    "new", "york", "registry", "shares", "share", "ordinary", "american", "depositary",
    "receipts", "adr", "sponsored", "unsponsored", "class", "each", "representing", "one",
    "of", "the", "and", "n", "v", "common", "stock", "unit", "units", "per", "a", "b", "c",
}


def name_tokens(name):
    """Normalized token set for a company name.

    Strips legal-form suffixes and ADR descriptors ("- New York Registry Shares")
    so a foreign issuer and its US line reduce to the same token set.
    """
    s = (name or "").lower().replace("&", " and ")
    s = re.sub(r"[^a-z0-9 ]+", " ", s)
    return {t for t in s.split() if t not in LEGAL_SUFFIXES and t not in NAME_NOISE}


def build_us_line_index():
    """Index of US-listed lines for the foreign issuers this routine publishes.

    Two america-scanner calls (type=stock and type=dr) filtered to the 18 home
    countries the foreign tables draw from -> ~2k lines. BOTH types are needed:
    TradingView types most ADRs as `dr` but files others (TotalEnergies NYSE:
    `stock`), and a dr-only index silently reports "no US line" for a name a US
    trader can buy.

    Returns a list of (ticker, exchange, country, token_set).
    """
    idx = []
    for t in ("stock", "dr"):
        d = scan("america",
                 [{"left": "type", "operation": "equal", "right": t},
                  {"left": "country", "operation": "in_range", "right": FOREIGN_HOME_COUNTRIES}],
                 rng=(0, 3000), sort={"sortBy": "name", "sortOrder": "asc"},
                 cols=["name", "description", "exchange", "country"])
        for row in d.get("data", []):
            nm, desc, ex, country = row["d"][0], row["d"][1], row["d"][2], row["d"][3]
            toks = name_tokens(desc or nm)
            if toks:
                idx.append((nm, ex, country, toks))
    health["us_line_index_ok"] = bool(idx)
    if not idx:
        degrade("tradingview_scanner.us_line_index",
                "the US-line index returned no rows; us_tradeable falls back to 'unknown'")
    return idx


def match_us_line(name, country, index):
    """The US line for a foreign issuer, as (ticker, exchange), or None.

    Token-set containment in either direction, preferring a candidate from the
    same issuer country and then the one with the most shared tokens. A real
    exchange listing beats an OTC line at equal score.
    """
    t = name_tokens(name)
    if not t or not index:
        return None
    best = None
    for nm, ex, ct, kt in index:
        if not (t <= kt or kt <= t):
            continue
        score = len(t & kt)
        same_country = 1 if (country and ct and ct == country) else 0
        listed = 1 if ex not in ("OTC", "PINK", "OTCBB", "GREY") else 0
        rank = (same_country, listed, score)
        if best is None or rank > best[0]:
            best = (rank, nm, ex)
    return (best[1], best[2]) if best else None



def g(d, key):
    return d[IDX[key]]


def epoch_date(e):
    if not e:
        return None
    return datetime.datetime.fromtimestamp(e, ET).strftime("%Y-%m-%d")


def next_earn_rank(row):
    """Rank a candidate for a catalyst lookup: DUE TO REPORT soonest first.

    The screener's LAST-report date lags badly - on 2026-11-05 it read
    2025-02-13 for a name that reported the previous day, and 2026-08-06 for
    a name that reported that morning - so "last earnings within 7 days" is
    not a usable earnings test on a foreign row. The NEXT-report date is the
    reliable half of the field, so it drives the lookup order; the size of the
    move breaks the tie.
    """
    d = row["d"]
    nxt = g(d, "earnings_release_next_date")
    days = None
    if nxt:
        try:
            days = (datetime.datetime.fromtimestamp(float(nxt), ET).date()
                    - NOW_ET.date()).days
        except Exception:
            days = None
    due = 0 if (days is not None and -1 <= days <= EARNINGS_DUE_WINDOW_DAYS) else 1
    return (due, days if days is not None else 9999, -abs(g(d, "change")))


TYPE = {"left": "type", "operation": "equal", "right": "stock"}


def flist(*pairs):
    out = [TYPE]
    for left, op, right in pairs:
        out.append({"left": left, "operation": op, "right": right})
    return out


def cap_per_market(rows, cap):
    """Keep at most `cap` rows per market, preserving the incoming order.

    Returns (kept_rows, {market: rows_kept}). The per-market count is
    published in source health so the reader can see how thin the coverage
    really is - the EU/UK table was 28% Sweden over nine runs while Belgium
    and Greece never appeared once.
    """
    seen = {}
    out = []
    for r in rows:
        m = r.get("market", "?")
        if seen.get(m, 0) >= cap:
            continue
        seen[m] = seen.get(m, 0) + 1
        out.append(r)
    return out, seen


# ------------------------------------------------------------------ Pass A
pa = scan_or_empty("america",
          flist(("exchange", "in_range", US_VENUES),
                ("market_cap_basic", "egreater", 20000000000)),
          rng=(0, 250), sort={"sortBy": "market_cap_basic", "sortOrder": "desc"})
a_rows = [r["d"] for r in pa["data"]
          if g(r["d"], "exchange") not in US_DROP
          and "/" not in g(r["d"], "name")]          # drop US preferred (JPM/PC, BAC/PB)
a_dropped_pref = len([r for r in pa["data"]
                       if g(r["d"], "exchange") not in US_DROP
                       and "/" in g(r["d"], "name")])

# ------------------------------------------------------------------ Pass B
pb_up = scan_or_empty("america",
             flist(("exchange", "in_range", US_VENUES),
                   ("change", "egreater", 3),
                   ("market_cap_basic", "egreater", 1000000000),
                   ("close", "egreater", 5),
                   ("volume", "egreater", MIN_VOLUME)),
             rng=(0, 200), sort={"sortBy": "change", "sortOrder": "desc"})
pb_dn = scan_or_empty("america",
             flist(("exchange", "in_range", US_VENUES),
                   ("change", "less", -3),
                   ("market_cap_basic", "egreater", 1000000000),
                   ("close", "egreater", 5),
                   ("volume", "egreater", MIN_VOLUME)),
             rng=(0, 200), sort={"sortBy": "change", "sortOrder": "asc"})
b_up = [r["d"] for r in pb_up["data"] if g(r["d"], "exchange") not in US_DROP]
b_dn = [r["d"] for r in pb_dn["data"] if g(r["d"], "exchange") not in US_DROP]

# ------------------------------------------------------------------ Pass C
eu_rows = []
for mkt, (home, venues, suffix) in EU_MARKETS.items():
    base = flist(("country", "equal", home),
                 ("market_cap_basic", "egreater", 1000000000),
                 ("close", "egreater", 5),
                 ("volume", "egreater", MIN_VOLUME))
    if venues:
        base.append({"left": "exchange", "operation": "in_range", "right": venues})
    for op, thr in (("egreater", 2.5), ("less", -2.5)):
        d = scan_or_empty(mkt, base + [{"left": "change", "operation": op, "right": thr}],
                 rng=(0, 150),
                 sort={"sortBy": "change", "sortOrder": "desc" if op == "egreater" else "asc"})
        if d.get("totalCount", 0) < 5:
            health["empty_markets"].append(f"{mkt}:{op}={d.get('totalCount')}")
        for r in d["data"]:
            eu_rows.append({"market": mkt, "suffix": suffix, "d": r["d"]})

seen = set()
eu_dedup = []
for r in eu_rows:
    n = g(r["d"], "name")
    if n in seen:
        continue
    seen.add(n)
    eu_dedup.append(r)
eu_dedup.sort(key=lambda r: -abs(g(r["d"], "change")))
# Per-market cap BEFORE the overall cap: the pool is diversified first, so the
# top-30 then draws across markets instead of being monopolised by one.
eu_capped, eu_rows_per_market = cap_per_market(eu_dedup, EU_MARKET_CAP)
eu_final = eu_capped[:30]
health["rows_per_market"] = eu_rows_per_market

# ------------------------------------------------------------------ Pass D
pd_up = scan_or_empty("australia",
             flist(("country", "equal", "Australia"),
                   ("exchange", "in_range", ["ASX"]),
                   ("change", "egreater", 2.5),
                   ("market_cap_basic", "egreater", 500000000),
                   ("close", "egreater", 1),
                   ("volume", "egreater", MIN_VOLUME)),
             rng=(0, 200), sort={"sortBy": "change", "sortOrder": "desc"})
pd_dn = scan_or_empty("australia",
             flist(("country", "equal", "Australia"),
                   ("exchange", "in_range", ["ASX"]),
                   ("change", "less", -2.5),
                   ("market_cap_basic", "egreater", 500000000),
                   ("close", "egreater", 1),
                   ("volume", "egreater", MIN_VOLUME)),
             rng=(0, 200), sort={"sortBy": "change", "sortOrder": "asc"})
au = [{"d": r["d"], "suffix": ASX_SUFFIX}
      for r in (pd_up["data"] + pd_dn["data"]) if g(r["d"], "exchange") == "ASX"]
au.sort(key=lambda r: -abs(g(r["d"], "change")))
au_capped, au_rows_per_market = cap_per_market(au, EU_MARKET_CAP)
au = au_capped[:25]

# ------------------------------------------------------------------ Pass E
# APAC / Gulf. Added 2026-11-11. Every one of these markets closes BEFORE the
# 08:00 ET fire, so the rows are SETTLED - no live-session caveat, the same
# treatment ASX gets. The market-cap floor is the ASX floor ($500M), not the
# EU $1B one: most APAC earnings action sits below $1B.
apac_rows = []
for mkt, (home, venues, suffix) in APAC_MARKETS.items():
    base = flist(("country", "equal", home),
                 ("market_cap_basic", "egreater", 500000000),
                 ("close", "egreater", 1),
                 ("volume", "egreater", MIN_VOLUME))
    if venues:
        base.append({"left": "exchange", "operation": "in_range", "right": venues})
    for op, thr in (("egreater", 2.5), ("less", -2.5)):
        d = scan_or_empty(mkt, base + [{"left": "change", "operation": op, "right": thr}],
                 rng=(0, 150),
                 sort={"sortBy": "change", "sortOrder": "desc" if op == "egreater" else "asc"})
        if d.get("totalCount", 0) < 5:
            health["empty_markets"].append(f"{mkt}:{op}={d.get('totalCount')}")
        for r in d["data"]:
            ex = g(r["d"], "exchange")
            apac_rows.append({"market": mkt, "suffix": suffix,
                               "yahoo_suffix": YAHOO_SUFFIX_BY_EXCHANGE.get(ex, suffix),
                               "d": r["d"]})
apac_seen = set()
apac_dedup = []
for r in apac_rows:
    n = g(r["d"], "name")
    if n in apac_seen:
        continue
    apac_seen.add(n)
    apac_dedup.append(r)
apac_dedup.sort(key=lambda r: -abs(g(r["d"], "change")))
apac_capped, apac_rows_per_market = cap_per_market(apac_dedup, APAC_MARKET_CAP)
apac = apac_capped[:25]
health["rows_per_market_apac"] = apac_rows_per_market

# ------------------------------------------------------------------ US merge
us = {}
for d in a_rows + b_up + b_dn:
    sym = d[IDX["name"]]
    if "/" in sym:
        continue
    c = us.setdefault(sym, {"name": g(d, "name"), "ex": g(d, "exchange"),
                             "country": g(d, "country"),
                             "close": g(d, "close"), "change": g(d, "change"),
                             "vol": g(d, "volume"), "mcap": g(d, "market_cap_basic"),
                             "pm": g(d, "premarket_change"), "po": g(d, "postmarket_change"),
                             "pmc": g(d, "premarket_close"),
                             "er": g(d, "earnings_release_date"),
                             "ern": g(d, "earnings_release_next_date"), "pass": set()})
    if d in a_rows:
        c["pass"].add("A")
    if d in b_up:
        c["pass"].add("B_up")
    if d in b_dn:
        c["pass"].add("B_dn")
    for k, key in (("pm", "premarket_change"), ("po", "postmarket_change"),
                   ("pmc", "premarket_close")):
        if c[k] is None and g(d, key) is not None:
            c[k] = g(d, key)

tagged, quiet, bod = [], [], []
for sym, c in us.items():
    pm, po = c["pm"], c["po"]
    if pm is None and po is None:
        tag = "BOD"
    elif po is not None and abs(po) > 3:
        tag = "AMC_REACTION"
    elif pm is not None and abs(pm) > 2:
        tag = "PRE_GAP"
    else:
        tag = "QUIET"
    c["tag"] = tag
    c["mx"] = max(abs(pm) if pm is not None else 0, abs(po) if po is not None else 0)
    if tag == "BOD":
        bod.append((sym, c))
    elif tag == "QUIET":
        quiet.append((sym, c))
    else:
        tagged.append((sym, c))
tagged.sort(key=lambda t: -t[1]["mx"])
quiet.sort(key=lambda t: -t[1]["mx"])
bod.sort(key=lambda t: -t[1]["mx"])

# ------------------------------------------------- reference close, resolved first
# The reference close is resolved BEFORE any table is built, and the candidate
# universe is filtered against it. A row whose screener-implied reference close
# disagrees with the authoritative one is measured against a STALE close - a
# phantom move - and is dropped, with the drop counted and published rather
# than silently filtered.
NOW_ET = datetime.datetime.now(ET)
us_line_index = build_us_line_index()


def attach_us(row, c):
    """Attach the resolved reference close and the US-tradeability to a US row."""
    c["ref"] = row
    c["us_tradeable"] = "US-listed" if c.get("country") in (None, "United States") \
        else "US-listed (ADR)"
    return row


us_ref = {}
tagged_keep = []
for sym, c in tagged:
    r = cross_check(c["name"], c["change"], c["close"], "", "US", live_session=False, venue="US")
    # The reference close is a HARD GATE: a row whose base could not be resolved
    # cannot be published (it would carry '—' in the Ref close / Ref source /
    # Ref asof / US tradeable columns and break ARTIFACT FORMAT CONTRACT v2).
    # The EU and AU passes already filtered their rows on the same gate; the US
    # headline pass did not, so a row whose Yahoo lookup failed was rendered
    # with dashes. It is dropped here instead; cross_check() counts the drop in
    # one place, so every pass counts it the same way.
    if r:
        us_ref[sym] = r
        attach_us(r, c)
        tagged_keep.append((sym, c))
    time.sleep(0.35)
tagged = tagged_keep
quiet_keep = []
for sym, c in quiet[:15]:
    r = cross_check(c["name"], c["change"], c["close"], "", "US", live_session=False, venue="US")
    if r:
        us_ref[sym] = r
        attach_us(r, c)
        quiet_keep.append((sym, c))
    time.sleep(0.35)
quiet = quiet_keep

eu_res, eu_keep = {}, []
for r0 in eu_final:
    d = r0["d"]
    r = cross_check(g(d, "name"), g(d, "change"), g(d, "close"), r0["suffix"],
                    r0["market"], live_session=not SETTLE_MODE, venue=r0["market"])
    if r:
        eu_res[g(d, "name")] = r
        r0["ref"] = r
        eu_keep.append(r0)
    time.sleep(0.35)
eu_final = eu_keep

au_res, au_keep = {}, []
for r0 in au:
    d = r0["d"]
    r = cross_check(g(d, "name"), g(d, "change"), g(d, "close"), r0["suffix"],
                    "AU", live_session=False, venue="AU")
    if r:
        au_res[g(d, "name")] = r
        r0["ref"] = r
        au_keep.append(r0)
    time.sleep(0.35)
au = au_keep

apac_res, apac_keep = {}, []
for r0 in apac:
    d = r0["d"]
    r = cross_check(g(d, "name"), g(d, "change"), g(d, "close"),
                    r0.get("yahoo_suffix") or r0["suffix"],
                    r0["market"], live_session=False, venue=r0["market"])
    if r:
        apac_res[g(d, "name")] = r
        r0["ref"] = r
        apac_keep.append(r0)
    time.sleep(0.35)
apac = apac_keep

# ------------------------------------------------------- one-table rule: dedupe
# Each name appears EXACTLY ONCE in the markdown. A symbol that is both a
# US-venue line and a foreign-primary line keeps the US row: it carries the
# extended-hours columns and it is the line a US reader can trade.
tagged_names = {c["name"] for _, c in tagged} | {c["name"] for _, c in quiet}
cross_region_dropped = []
eu_final2 = []
for r0 in eu_final:
    if g(r0["d"], "name") in tagged_names:
        cross_region_dropped.append(f"{g(r0['d'],'name')}@{r0['market']}")
        continue
    eu_final2.append(r0)
eu_final = eu_final2
au_names = {g(r0["d"], "name") for r0 in au}
cross_region_dropped += [f"{g(r0['d'],'name')}@AU" for r0 in au
                         if g(r0["d"], "name") in tagged_names]
au = [r0 for r0 in au if g(r0["d"], "name") not in tagged_names]

# The APAC/Gulf rows obey the one-table rule too: a name already published as
# a US line (or as a European line) keeps that row and the APAC row is
# dropped and counted, so nothing appears twice in the markdown.
apac_names = {g(r0["d"], "name") for r0 in apac}
foreign_names = {g(r0["d"], "name") for r0 in eu_final} | au_names
cross_region_dropped += [f"{g(r0['d'],'name')}@{r0['market']}" for r0 in apac
                         if g(r0["d"], "name") in tagged_names | foreign_names]
apac = [r0 for r0 in apac
        if g(r0["d"], "name") not in tagged_names | foreign_names]

# ------------------------------------------------------------- pre-market check
# Independent check of the US pre-market column - the headline number of the
# table - using Yahoo's 1-minute pre/post feed as the second source, against
# the IMMEDIATELY PRIOR session's close (not the prior-prior one).
pmc = health["premarket_check"]
for sym, c in tagged[:10]:
    if c["pm"] is None:
        continue
    prior = us_ref.get(sym, {}).get("prior_close")
    v = yahoo_premarket(sym, prior, now_et=NOW_ET)
    if v is None:
        pmc["unavailable"] += 1
        degrade("yahoo_premarket_check.unavailable",
                f"{sym}: Yahoo's 1-minute pre-market feed returned no usable print")
        continue
    pmc["checked"] += 1
    d = abs(v[0] - c["pm"])
    if d <= 1.0:
        pmc["within_1pp"] += 1
    if d <= 3.0:
        pmc["within_3pp"] += 1
    else:
        pmc["outliers"].append({"symbol": sym, "tv": round(c["pm"], 3),
                                 "yahoo": v[0], "delta": round(d, 3),
                                 "yahoo_asof": v[1]})
    time.sleep(0.35)


# ------------------------------------------------------------------- rendering
def pct(v):
    return "—" if v is None else f"{v:.2f}"


def er_cell(c):
    last = epoch_date(c.get("er"))
    nxt = epoch_date(c.get("ern"))
    if not last:
        return "—"
    age = (datetime.datetime.now(ET).date() -
           datetime.datetime.strptime(last, "%Y-%m-%d").date()).days
    return f"{last} ({age}d ago)" if age >= 0 else f"{last}"


def multiple(move, avg):
    """move_vs_avg_daily: the reaction divided by the name's own average move."""
    if move is None or not avg:
        return "n/a"
    return f"{abs(move) / avg:.1f}x"


def ref_cols(r):
    """The reference-close columns every published row must carry."""
    if not r:
        return "—", "—", "—", "—"
    return (f"{r['ref_close']:.2f}", r["ref_close_source"], r["ref_close_asof"],
            r.get("session_asof") or "—")


def settle_state(r):
    """`live` when the row's session bar is an in-progress bar, else `settled`.

    Derived from the SAME Yahoo bar resolution that validates the reference
    close, so it is a measurement and not an assumption. The EU/UK session is
    still open at the 08:00 ET fire (it closes 11:30 ET in winter), so its
    rows read `live` - the reader is told, ON THE ROW, that the move is a
    mid-session snapshot rather than the session's result. Measured over the
    2026-11-05/06/09 runs, about half the EU rows finished more than 1pp away
    from the settled move (worst case 12.7pp).
    """
    if not r:
        return "—"
    return "live" if r.get("mode") == "live" else "settled"


def _settle_summary():
    """One line: how many published foreign rows are live vs settled."""
    rows = ([("EU/UK", r) for r in eu_final] + [("ASX", r) for r in au]
            + [("APAC/Gulf", r) for r in apac])
    live = sum(1 for _, r in rows if settle_state((r or {}).get("ref")) == "live")
    return (f"{len(rows) - live} settled, {live} live (a live row's move is a "
            f"mid-session snapshot, not the session's result)")


def headline_move(c):
    """The move a row is really about: the extended-hours print for a US row."""
    if c.get("pm") is not None and c.get("tag") == "PRE_GAP":
        return c["pm"]
    return c.get("change")


def us_tradeable_foreign(name, country):
    """ADR / US-listed / none for a foreign row."""
    m = match_us_line(name, country, us_line_index)
    if not m:
        return "none"
    return f"ADR ({m[1]}:{m[0]})"


# --------------------------------------------------------------- catalyst merge
# The catalyst rides in the row's last column. The catalog file is READ and
# MERGED by ticker; there is no separate `## Catalysts` section, so a name can
# never appear twice in the markdown.
def parse_catalyst_file(path):
    """Parse /workspace/catalog/catalysts/<date>.md -> (mapping, note)."""
    mapping, note = {}, ""
    if not os.path.exists(path):
        return mapping, note
    with open(path) as fh:
        for line in fh.read().splitlines():
            s = line.strip()
            if s.startswith("|"):
                cells = [c.strip() for c in re.split(r"(?<!\\)\|", s)]
                # A markdown row starts with a pipe, so the FIRST split cell is
                # always empty ("", "SEZL", "US", "...", "Y", ""). The old
                # guard dropped every such row on its empty first cell, so the
                # catalyst merge NEVER ran and every published row carried
                # "pending catalyst lookup" - the agent's researched catalysts
                # were silently discarded on every fire. Strip the leading
                # empty cell before reading the ticker.
                if cells and cells[0] == "":
                    cells = cells[1:]
                if len(cells) < 4:
                    continue
                if cells[0].lower() in ("ticker", "") or set(cells[0]) <= set("-: "):
                    continue
                # An UNFILLED skeleton row (the pipeline writes one when the
                # file is missing) has an empty catalyst cell: it is not a
                # research result, so it must fall through to the honest
                # placeholder instead of publishing an empty cell.
                if not cells[2]:
                    continue
                mapping[cells[0]] = {"catalyst": cells[2],
                                     "earn": cells[3] if cells[3] else "—"}
            elif s and not note and not s.startswith("#"):
                note = s
    return mapping, note


os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs(CAT_DIR, exist_ok=True)
CAT_FILE = f"{CAT_DIR}/{RUN_DATE}.md"


# ------------------------------------------- settlement: the morning run's inputs
# WHY (2026-11-11). The 12:15 ET settlement pass reads TWO files the 08:00 ET
# scan produced: the morning artifact (the `Move @08:00` and `Δ vs scan`
# columns) and the catalyst catalog (the catalyst cell). Both live ONLY in the
# 08:00 run's sandbox - `/workspace` is a per-session mount, so a fresh 12:15
# sandbox starts with NEITHER file. Measured on the 2026-11-11 fire: with no
# morning artifact the slot's headline measurement - the scan-to-close drift -
# was uncomputable, and with no catalog every published row carried "no
# catalyst lookup" even though the morning had researched 14 catalysts (BICO,
# FNM and ENR among them).
#
# The fix RECOVERS them; it does not re-research. The morning artifact IS
# published to the outputs repo, and the catalog's content IS the morning
# artifact's own catalyst column, so the settlement pass fetches the artifact
# and rebuilds the catalog from it - the morning run's research copied
# VERBATIM, under a PROVENANCE note, with no fabricated cell. If the fetch
# fails the run degrades exactly as it did before (empty `Move @08:00`, honest
# placeholder catalyst), so the recovery can never make the artifact worse.
NO_RESEARCH_CATALYST = ("no catalyst lookup", "pending catalyst lookup",
                         "not performed", "outside the per-run budget",
                         "lookup not performed", "no lookup performed")


def _http_get(urls):
    """GET the first URL whose body is usable. urls: [(label, curl_args)]."""
    for label, args in urls:
        try:
            r = subprocess.run(["curl", "-sS", "-L", "--max-time", "30"] + args,
                               capture_output=True, text=True, timeout=45)
            body = r.stdout or ""
            if body and '"message"' not in body[:200]:
                return body, label
        except Exception:
            continue
    return None, None


def _atomic_write(path, text):
    """Write via a temp file + os.replace - /workspace is a shared mount and a
    half-written artifact is worse than no artifact."""
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(text)
    os.replace(tmp, path)


def _fetch_morning_artifact():
    """The 08:00 ET scan's PUBLISHED artifact. Returns (text, source)."""
    token = os.environ.get("GITHUB_TOKEN", "")
    path = f"earnings/{MORNING_ARTIFACT}"
    urls = []
    if token:
        urls.append(("api-token", ["-H", "Accept: application/vnd.github.raw",
                                   "-H", "Authorization: Bearer " + token,
                                   f"https://api.github.com/repos/{API_OWNER}/{API_REPO}/contents/{path}?ref=main"]))
    urls.append(("api", ["-H", "Accept: application/vnd.github.raw",
                          f"https://api.github.com/repos/{API_OWNER}/{API_REPO}/contents/{path}?ref=main"]))
    urls.append(("raw", [f"{RAW_REPO}/main/{path}"]))
    body, src = _http_get(urls)
    if not body:
        return None, None
    # The body must LOOK like the morning scan - a 404 page or an API error
    # body is not a morning artifact, and parsing it would publish nonsense.
    if "Earnings reaction scanner" not in body or "## EU/UK" not in body:
        return None, None
    return body, src


def _rebuild_catalyst_catalog(morning_text):
    """Rebuild the catalyst catalog from the morning artifact's catalyst column.

    Returns the number of researched catalysts recovered, or -1 when there is
    nothing to recover. NEVER overwrites an existing catalog file: that file is
    the agent's research and must survive a re-run.
    """
    region_of = {"US — Headline table": "US", "US — QUIET one-liners": "US",
                 "EU/UK — Headline table": "EU", "AU (ASX) — Headline table": "AU",
                 "APAC/Gulf — Headline table": "APAC/Gulf"}
    rows = []
    for m in re.finditer(r"^## ([^\n]*)\n(.*?)(?=^## |\Z)", morning_text, re.M | re.S):
        region = region_of.get(m.group(1))
        if not region:
            continue
        lines = [l for l in m.group(2).splitlines() if l.strip().startswith("|")]
        if not lines:
            continue
        head = [c.strip() for c in re.split(r"(?<!\\)\|", lines[0].strip())]
        head = head[1:] if head and head[0] == "" else head
        try:
            ti, ei, ci = head.index("Ticker"), head.index("Earn"), head.index("Catalyst")
        except ValueError:
            continue
        for line in lines[2:]:
            cells = [c.strip() for c in re.split(r"(?<!\\)\|", line.strip())]
            cells = cells[1:] if cells and cells[0] == "" else cells
            if len(cells) <= max(ti, ei, ci):
                continue
            tick, cat, earn = cells[ti], cells[ci], cells[ei]
            if not tick or not cat:
                continue
            if any(x in cat.lower() for x in NO_RESEARCH_CATALYST):
                continue
            rows.append((tick, region, cat, earn))
    if not rows:
        return -1
    body = ["Catalyst lookups: the per-run budget of the 08:00 ET scan.",
            "",
            "PROVENANCE: this file was REBUILT by the 12:15 ET settlement pass from",
            f"the 08:00 ET scan's published artifact (earnings/{MORNING_ARTIFACT}),",
            "because the morning run's local catalog file is not carried into this",
            "sandbox. Every cell below is the morning run's own researched catalyst,",
            "copied VERBATIM - no new catalyst research was performed here.",
            "",
            "| Ticker | Region | Catalyst | Earnings-driven |",
            "|---|---|---|---|"]
    for tick, region, cat, earn in rows:
        body.append(f"| {tick} | {region} | {cat} | {earn} |")
    _atomic_write(CAT_FILE, "\n".join(body) + "\n")
    return len(rows)


# Provenance of the two inputs the settlement pass depends on. Published in the
# artifact's source health so the reader knows where they came from.
INPUT_PROV = {"morning": "", "catalog": ""}
if SETTLE_MODE:
    _mpath = os.path.join(OUT_DIR, MORNING_ARTIFACT)
    if os.path.exists(_mpath):
        INPUT_PROV["morning"] = "found locally"
        with open(_mpath, encoding="utf-8") as fh:
            _morning_text = fh.read()
    else:
        _morning_text, _msrc = _fetch_morning_artifact()
        if _morning_text:
            _atomic_write(_mpath, _morning_text)
            INPUT_PROV["morning"] = f"fetched from the outputs repo ({_msrc})"
        else:
            _morning_text = ""
            INPUT_PROV["morning"] = ("NOT FOUND - the scan-to-close comparison is "
                                     "unavailable for this run")
    if os.path.exists(CAT_FILE):
        INPUT_PROV["catalog"] = "found locally"
    elif _morning_text:
        _n = _rebuild_catalyst_catalog(_morning_text)
        INPUT_PROV["catalog"] = (f"rebuilt from the morning artifact ({_n} researched "
                                  f"catalysts recovered)") if _n > 0 else (
            "NOT FOUND - every row publishes the honest placeholder")
    else:
        INPUT_PROV["catalog"] = "NOT FOUND - every row publishes the honest placeholder"

catalysts, catalyst_note = parse_catalyst_file(CAT_FILE)

# The per-run catalyst budget: 5 US + 3 EU + 2 AU. These are the names the
# agent is asked to look up; every other row says so honestly.
amc_rows = [c for _, c in tagged if c["tag"] == "AMC_REACTION"]
gap_rows = [c for _, c in tagged if c["tag"] == "PRE_GAP"]
targets_us = amc_rows[:3] + [c for c in gap_rows if c not in amc_rows][:max(0, 5 - min(3, len(amc_rows)))]
targets_us = targets_us[:CATALYST_BUDGET["US"]]
targets_eu = [g(r0["d"], "name") for r0 in
              sorted(eu_final, key=next_earn_rank)[:CATALYST_BUDGET["EU"]]]
targets_au = [g(r0["d"], "name") for r0 in
              sorted(au, key=next_earn_rank)[:CATALYST_BUDGET["AU"]]]
targets_apac = [g(r0["d"], "name") for r0 in
                sorted(apac, key=next_earn_rank)[:CATALYST_BUDGET["APAC"]]]
TARGET_SET = (set(c["name"] for c in targets_us) | set(targets_eu)
              | set(targets_au) | set(targets_apac))

# The catalog file is the agent's input, so a starter skeleton is written when
# it is missing. It is NEVER overwritten: a re-run must not wipe the agent's
# catalyst research.
if not os.path.exists(CAT_FILE):
    _budget_total = sum(CATALYST_BUDGET.values())
    with open(CAT_FILE, "w") as fh:
        fh.write("Catalyst lookups: "
                 f"{CATALYST_BUDGET['US']} US + {CATALYST_BUDGET['EU']} EU + "
                 f"{CATALYST_BUDGET['AU']} AU + {CATALYST_BUDGET['APAC']} APAC/Gulf = "
                 f"{_budget_total}"
                 " per run, the skill's cap.\n")
        fh.write("Fill the Catalyst cell for every ticker below, then re-run the\n")
        fh.write("pipeline - the catalyst is merged into that ticker's row in the\n")
        fh.write("artifact, so a re-run never wipes this file. Never fabricate a\n")
        fh.write('headline: "no fresh catalyst found" is a valid cell.\n')
        fh.write("A ticker whose lookup you did NOT perform must leave the\n")
        fh.write("Earnings-driven cell EMPTY - the pipeline publishes no verdict\n")
        fh.write('for an unresearched row ("—" is the honest value).\n\n')
        fh.write("| Ticker | Region | Catalyst | Earnings-driven |\n")
        fh.write("|---|---|---|---|\n")
        for c in targets_us:
            fh.write(f"| {c['name']} | US | | |\n")
        for n in targets_eu:
            fh.write(f"| {n} | EU | | |\n")
        for n in targets_au:
            fh.write(f"| {n} | AU | | |\n")
        for n in targets_apac:
            fh.write(f"| {n} | APAC/Gulf | | |\n")
    catalysts, catalyst_note = parse_catalyst_file(CAT_FILE)


def catalyst_cell(name):
    """The catalyst for a row: from the catalog file, or an honest placeholder.

    The verdict follows the RESEARCH, never the other way round. A row whose
    catalyst cell says the lookup was not performed carries NO verdict: the
    2026-11-05 EU run published "N" (not earnings-driven) beside the note
    "catalyst lookup not performed", which is a false verdict on 10% of that
    run's researched EU rows. A researched row that found nothing ("no fresh
    catalyst found") IS a verdict and keeps its N.
    """
    c = catalysts.get(name)
    if c is None:
        for k, v in catalysts.items():
            if k.upper() == name.upper():
                c = v
                break
    if c:
        return c["catalyst"], verdict_for(c["catalyst"], c["earn"])
    if name in TARGET_SET:
        return "pending catalyst lookup", "—"
    return "no catalyst lookup (outside the per-run budget)", "—"


# Markers that mean the catalyst was NOT researched. A row carrying one of
# these has no evidence, so it must not carry a verdict.
NO_RESEARCH_MARKERS = ("no catalyst lookup", "pending catalyst lookup",
                       "not performed", "outside the per-run budget",
                       "lookup not performed", "no lookup performed")


def verdict_for(catalyst_text, flag):
    """Y / N / em-dash, decided by whether the catalyst was actually researched."""
    low = (catalyst_text or "").lower()
    if any(m in low for m in NO_RESEARCH_MARKERS):
        return "—"
    return flag if flag in ("Y", "N") else "—"


# ----------------------------------------------------------------- Actionable
def reaction_rows(region):
    """The published rows of a region, as dicts the actionable layer reads.

    Each row carries the reaction itself (`move`), the name's own average daily
    move (`avg`), and the pair that says whether the reaction is still
    EXTENDING: `ext` is the move that is happening now and `base` is the move
    it follows.
      US    ext = the extended-hours print, base = the regular session's move
      EU/UK ext = the live session's move, base = the last completed session
      AU    ext = the last session's move, base = the one before it
    """
    out = []
    if region == "US":
        for sym, c in tagged:
            r = us_ref.get(sym)
            ext = c["pm"] if c.get("pm") is not None else c.get("po")
            out.append({"name": c["name"], "move": headline_move(c),
                        "avg": (r or {}).get("avg_daily_move"), "ref": r,
                        "session_move": c["change"], "ext": ext,
                        "base": c["change"],
                        "tradeable": c.get("us_tradeable", "—")})
    elif region == "EU":
        for r0 in eu_final:
            d = r0["d"]
            r = r0["ref"]
            out.append({"name": g(d, "name"), "move": g(d, "change"),
                        "avg": (r or {}).get("avg_daily_move"), "ref": r,
                        "session_move": g(d, "change"), "ext": g(d, "change"),
                        "base": (r or {}).get("prev_move"),
                        "tradeable": us_tradeable_foreign(g(d, "name"), g(d, "country"))})
    else:
        for r0 in au:
            d = r0["d"]
            r = r0["ref"]
            out.append({"name": g(d, "name"), "move": g(d, "change"),
                        "avg": (r or {}).get("avg_daily_move"), "ref": r,
                        "session_move": g(d, "change"), "ext": g(d, "change"),
                        "base": (r or {}).get("prev_move"),
                        "tradeable": us_tradeable_foreign(g(d, "name"), g(d, "country"))})
    return out


def not_yet_priced(region, rows):
    """The one name whose reaction looks least settled - a HYPOTHESIS, never a call.

    The test is computable and states its own evidence: the reaction is still
    EXTENDING (the move that is happening now is larger in magnitude than the
    move it follows) and it is large relative to the name's own average daily
    move. The artifact makes no direction or trade statement.
    """
    best = None
    for r in rows:
        mv = r.get("move")
        avg = r.get("avg")
        if mv is None or not avg:
            continue
        mult = abs(mv) / avg
        ext = r.get("ext")
        base = r.get("base")
        extending = (ext is not None and base is not None and abs(ext) > abs(base))
        score = (1 if extending else 0, mult)
        if best is None or score > best[0]:
            best = (score, r, mult, extending)
    if not best:
        return None
    _, r, mult, extending = best
    ev = []
    ev.append(f"{r['move']:+.2f}%")
    if r.get("avg"):
        ev.append(f"{r['avg']:.2f}% mean absolute daily move over the last "
                  f"{AVG_MOVE_WINDOW} completed sessions")
    ev.append(f"{mult:.1f}x that average")
    if r.get("ref"):
        ev.append(f"reference close {r['ref']['ref_close']:.2f} dated "
                  f"{r['ref']['ref_close_asof']}")
    ev.append(f"US access: {r.get('tradeable')}")
    if extending and r.get("ext") is not None and r.get("base") is not None:
        ev.append(f"the move now ({r['ext']:+.2f}%) is larger than the move it follows "
                  f"({r['base']:+.2f}%)")
    return {"name": r["name"], "move": r["move"], "mult": mult, "extending": extending,
            "evidence": ", ".join(ev)}


REGION_LABEL = {"US": "US", "EU": "EU/UK", "AU": "AU (ASX)"}
region_rows = {k: reaction_rows(k) for k in ("US", "EU", "AU")}
hypotheses = {k: not_yet_priced(k, region_rows[k]) for k in ("US", "EU", "AU")}
adr_n = sum(1 for k in ("EU", "AU") for r in region_rows[k] if str(r.get("tradeable")).startswith("ADR"))
foreign_only_n = sum(1 for k in ("EU", "AU") for r in region_rows[k] if r.get("tradeable") == "none")
us_published = len(tagged) + len(quiet)

# ------------------------------------------------------- the settlement pass
# WHY A SECOND SLOT. The 08:00 ET scan publishes the EU/UK session MID-FLIGHT
# (it closes 11:30 ET in winter), so the EU move it prints is a snapshot taken
# minutes after the reaction started. Measured over the 2026-11-05/06/09 runs
# against each session's settled close: the median EU row finished 0.9-2.1pp
# away, the worst 12.7pp, and roughly HALF the rows were more than 1pp off.
# The 12:15 ET pass republishes the same rows with their SETTLED close and
# move, and carries the morning's move beside it, so the reader can see how
# much of the reaction survived - and so the routine MEASURES its own live
# snapshot instead of asking the reader to trust it.
def read_morning_eu():
    """The 08:00 ET scan's EU/UK move per ticker, read from the morning artifact."""
    path = os.path.join(OUT_DIR, MORNING_ARTIFACT)
    if not os.path.exists(path):
        return {}
    try:
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
    except Exception:
        return {}
    m = re.search(r"^## EU/UK[^\n]*\n(.*?)(?=^## )", text, re.M | re.S)
    if not m:
        return {}
    out = {}
    for line in m.group(1).splitlines():
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in re.split(r"(?<!\\)\|", s)]
        if cells and cells[0] == "":
            cells = cells[1:]
        if len(cells) < 5 or cells[0] in ("Ticker", "—", "-"):
            continue
        if set(cells[0]) <= set("-: "):
            continue
        try:
            out[cells[0]] = float(cells[4].replace("%", "").replace("+", ""))
        except Exception:
            continue
    return out


if SETTLE_MODE:
    _now = datetime.datetime.now(ET)
    L2 = []
    B = L2.append
    _morning = read_morning_eu()
    _drifts = []
    B(f"# Earnings reaction scanner — {RUN_DATE} (EU settlement pass)")
    B("")
    B(f"- Cron: `15 12 * * 1-5` America/New_York (weekdays, 12:15 ET)")
    B(f"- Fire time (ET): {_now.strftime('%Y-%m-%d %H:%M:%S %a')}")
    B(f"- Run type: `settlement_pass` — the EU/UK session has closed, so the same rows as")
    B(f"  the 08:00 ET scan are republished with their SETTLED close and move.")
    B(f"- Source: TradingView public screener; Yahoo chart API as the independent")
    B(f"  reference-close source.")
    B(f"- Method: the EU/UK cash session closed at 11:30 ET (16:30 CET in winter; 10:30")
    B(f"  ET in summer). The 08:00 ET scan's move is carried alongside each settled move")
    B(f"  so the reaction can be read as a measurement, not an impression. The US session")
    B(f"  is OPEN at 12:15 ET, so no US rows are published here - a live intraday price")
    B(f"  presented as a close would be a fabricated settle.")
    B(f"- artifact_contract: {ARTIFACT_CONTRACT}")
    B(f"- morning_artifact: earnings/{MORNING_ARTIFACT}"
      + ("" if _morning else " (NOT FOUND - the morning scan move is unavailable)"))
    B(f"- Status: `ok`")
    B("")
    B("## TL;DR")
    B("")
    B(f"- {len(eu_final)} EU/UK rows republished with their SETTLED close and move.")
    if _morning:
        _matched = [(g(r['d'], 'name'), _morning[g(r['d'], 'name')], g(r['d'], 'change'))
                    for r in eu_final if g(r['d'], 'name') in _morning]
        _drifts = [abs(s - c) for _, s, c in _matched]
        _over1 = sum(1 for x in _drifts if x > 1.0)
        if _drifts:
            _med = sorted(_drifts)[len(_drifts) // 2]
            B(f"- {len(_matched)} of them also appear in the 08:00 ET scan: the settled move")
            B(f"  differs from the scan move by a median of {_med:.2f}pp and a maximum of")
            B(f"  {max(_drifts):.2f}pp; {_over1} of {len(_matched)} rows moved more than 1pp")
            B(f"  between the scan and the close.")
    else:
        B(f"- The 08:00 ET scan artifact was not found, so the scan-to-close comparison is")
        B(f"  unavailable for this run.")
    _big = max(eu_final, key=lambda r: abs(g(r['d'], 'change'))) if eu_final else None
    if _big:
        B(f"- Biggest settled EU/UK move: {g(_big['d'], 'name')} "
          f"({g(_big['d'], 'change'):+.2f}%, {_big['market']}).")
    B("")
    B("## EU/UK — Settled table")
    B("")
    B("| Ticker | Market | Venue | Close | Chg % | Move @08:00 | Δ vs scan | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | Session asof | Settle | US tradeable | Last earnings | Earn | Catalyst |")
    B("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for r0 in eu_final:
        d = r0["d"]
        r = r0["ref"]
        rc, rs, ra, sa = ref_cols(r)
        cat, earn = catalyst_cell(g(d, "name"))
        nm = g(d, "name")
        scan_move = _morning.get(nm)
        settled = g(d, "change")
        delta = None if scan_move is None else settled - scan_move
        B(f"| {nm} | {r0['market']} | {g(d,'exchange')} | {g(d,'close')} | "
          f"{settled:+.2f} | "
          f"{'—' if scan_move is None else f'{scan_move:+.2f}'} | "
          f"{'—' if delta is None else f'{delta:+.2f}'} | "
          f"{g(d,'currency')} | {multiple(settled, (r or {}).get('avg_daily_move'))} | "
          f"{rc} | {rs} | {ra} | {sa} | {settle_state(r)} | "
          f"{us_tradeable_foreign(nm, g(d,'country'))} | "
          f"{epoch_date(g(d,'earnings_release_date')) or '—'} | {earn} | {cat} |")
    if not eu_final:
        B("| — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |")
    B("")
    B("## Source health")
    B("")
    B(f"- scanner_calls: {health['scanner_calls']} | scanner_errors: {health['scanner_errors']}")
    B(f"- pipeline_version: {SCRIPT_VERSION}")
    B(f"- settlement: the EU/UK session is CLOSED at this fire, so every row's `Settle`")
    B(f"  cell reads `settled` and its move is the session's own move.")
    B(f"- morning_artifact: {INPUT_PROV['morning']}")
    B(f"- catalyst_catalog: {INPUT_PROV['catalog']}")
    B(f"- scan_to_settle: {len(_drifts)} rows compared with the 08:00 ET scan"
      + (f", median drift {sorted(_drifts)[len(_drifts)//2]:.2f}pp, max {max(_drifts):.2f}pp, "
         f"{sum(1 for x in _drifts if x > 1.0)} rows more than 1pp apart"
         if _drifts else ""))
    cc = health["cross_check"]
    B(f"- reference_close (screener vs Yahoo, resolved BEFORE the table was built): "
      f"agree={cc['agree']} mismatch={cc['mismatch']} unverified={cc['unverified']} "
      f"stale_reference={cc['stale']}")
    B(f"- rows_dropped_stale_ref: {health['rows_dropped_stale_ref']} | "
      f"rows_dropped_unresolved_ref: {health['rows_dropped_unresolved_ref']}")
    B(f"- degraded_sources: {len(DEGRADED)}")
    if DEGRADED:
        B(f"  (the chat reply's `errors:` MUST equal this number - one entry per degraded")
        B(f"  source, not one per run)")
        for i, (s, d) in enumerate(DEGRADED, 1):
            B(f"  {i}. {s} — {d}")
    else:
        B("  (none - every source answered for every published row)")
    B("")
    B("## Audit line")
    B("")
    B(f"`earnings-reaction mode=settle target=earnings-reactions:{RUN_DATE} "
      f"eu_rows={len(eu_final)} scan_matched={len(_drifts)} "
      f"scan_to_settle_median_pp={sorted(_drifts)[len(_drifts)//2] if _drifts else 'n/a'} "
      f"catalyst_lookups={len(catalysts)} "
      f"rows_dropped_stale_ref={health['rows_dropped_stale_ref']} "
      f"degraded_sources={len(DEGRADED)}`")
    B("")
    _out = os.path.join(OUT_DIR, OUT_NAME)
    with open(_out, "w") as fh:
        fh.write("\n".join(L2))
    print(f"WROTE {_out} ({os.path.getsize(_out)} bytes)")
    print(f"REPLY_ERRORS: {len(DEGRADED)}")
    print(json.dumps({"mode": "settle", "eu_rows": len(eu_final),
                      "scan_matched": len(_drifts),
                      "scan_to_settle_max_pp": round(max(_drifts), 3) if _drifts else None,
                      "degraded_sources": len(DEGRADED)}))
    sys.exit(0)


L = []
A = L.append
A(f"# Earnings reaction scanner — {RUN_DATE}")
A("")
_now = datetime.datetime.now(ET)
_weekend = _now.isoweekday() > 5
_offcycle = (_now.hour != 8) or _weekend
A(f"- Cron: `0 8 * * 1-5` America/New_York (weekdays, 08:00 ET)")
A(f"- Fire time (ET): {_now.strftime('%Y-%m-%d %H:%M:%S %a')}")
if _offcycle:
    A(f"- Run type: `validation_run_offcycle` — the fire was NOT at the canonical 08:00 ET")
    A(f"  weekday slot.")
    if _weekend:
        A(f"  It is a weekend, so US/EU/ASX cash markets are closed and the extended-hours")
        A(f"  columns carry the PRIOR session's prints. Treat every pre-market/post-market")
        A(f"  number as a historical value, not a live gap.")
    else:
        A(f"  It fired at {_now.strftime('%H:%M')} ET on a weekday. The pre-market columns are")
        A(f"  live only if the fire was before the 09:30 ET US open; after that they are")
        A(f"  frozen at the open. The 08:00 ET fire is the one the skill is designed for.")
    A(f"  The scheduled weekday fire at 08:00 ET produces the live version.")
else:
    A(f"- Run type: `scheduled_scan`")
A(f"- Source: TradingView public screener (`scanner.tradingview.com/<market>/scan`);")
A(f"  Yahoo chart API as the independent reference-close source.")
A(f"- Method: 5 passes (US top-200 mcap, US prior-session movers, EU/UK movers,")
A(f"  ASX movers, APAC/Gulf movers). Volume floor {MIN_VOLUME:,} on every pass; `country` filter for")
A(f"  primary listings; exchange drop-list applied.")
A(f"- artifact_contract: {ARTIFACT_CONTRACT}")
A(f"- settlement_state: every foreign row carries a `Settle` cell - `live` when the row's")
A(f"  session bar is an in-progress bar, `settled` when it is a completed session. The")
A(f"  EU/UK session is still OPEN at the 08:00 ET fire (it closes 11:30 ET in winter), so")
A(f"  its rows read `live`: the move is a mid-session snapshot, not the session's result.")
A(f"- ref_close_source: yahoo_chart_daily (Yahoo Finance daily chart bars; the base")
A(f"  every published row is measured against)")
A(f"- Status: `ok`")
A("")
A("## TL;DR")
A("")
amc = [c for _, c in tagged if c["tag"] == "AMC_REACTION"]
gaps = [c for _, c in tagged if c["tag"] == "PRE_GAP"]

big_us = max(tagged, key=lambda t: t[1]["mx"]) if tagged else None
big_eu = max(eu_final, key=lambda r: abs(g(r["d"], "change"))) if eu_final else None
big_au = max(au, key=lambda r: abs(g(r["d"], "change"))) if au else None
big_apac = max(apac, key=lambda r: abs(g(r["d"], "change"))) if apac else None
_eu_live = sum(1 for r in eu_final if settle_state(r.get("ref")) == "live")
A(f"- {len(amc)} AMC reactions, {len(gaps)} pre-market gaps, {len(bod)} without extended-hours data; "
  f"{len(eu_final)} EU/UK and {len(au)} ASX movers, {len(apac)} APAC/Gulf movers.")
if big_us:
    A(f"- Biggest US extended-hours move: {big_us[1]['name']} "
      f"{big_us[1]['tag']} ({pct(big_us[1]['mx'])}%).")
if big_eu:
    A(f"- Biggest EU/UK move: {g(big_eu['d'], 'name')} ({g(big_eu['d'], 'change'):+.2f}%, "
      f"{big_eu['market']}).")
if big_au:
    A(f"- Biggest ASX move: {g(big_au['d'], 'name')} ({g(big_au['d'], 'change'):+.2f}%).")
if big_apac:
    A(f"- Biggest APAC/Gulf move: {g(big_apac['d'], 'name')} "
      f"({g(big_apac['d'], 'change'):+.2f}%, {big_apac['market']}).")
A(f"- {len(eu_final) - _eu_live} of the {len(eu_final)} EU/UK rows are SETTLED and "
  f"{_eu_live} are LIVE (mid-session). The 12:15 ET settlement pass publishes where those")
A(f"  live moves actually closed.")
A(f"- EU/AU/APAC earnings-driven tagging is keyword-based on headlines (best-effort). A row")
A(f"  whose lookup was not performed carries NO verdict — only a researched row does.")
A("")
A("## Actionable read")
A("")
A(f"- **Move vs this name's own history.** The `Move vs avg daily` column divides the")
A(f"  reaction by the name's own mean absolute daily move over its last")
A(f"  {AVG_MOVE_WINDOW} completed sessions. A -27% move in a name that averages +-3% is a")
A(f"  different event from a -8% move in a name that averages +-7%.")
A(f"- **US-listed and tradeable vs foreign-only.** {us_published} published US rows are on a")
A(f"  US venue; {adr_n} more foreign reactions have a US ADR line")
A(f"  (the `US tradeable` column carries the ticker); {foreign_only_n} are foreign-only and")
A(f"  cannot be bought directly by a US reader.")
for key in ("US", "EU", "AU"):
    h = hypotheses[key]
    if not h:
        A(f"- **Not yet fully priced — {REGION_LABEL[key]}:** no published row carries the")
        A(f"  average daily move needed to judge this, so no candidate is named.")
        continue
    tail = ("the reaction is still being repriced"
            if h["extending"] else
            "the move is not currently extending beyond the move it follows")
    A(f"- **Not yet fully priced — {REGION_LABEL[key]} (hypothesis, not a recommendation).**")
    A(f"  {h['name']} — {h['evidence']}; {tail}. Hypothesis only: this artifact states no")
    A(f"  direction and no trade.")
A("")
A("## US — Headline table")
A("")
A("| Ticker | Venue | Close | Chg % | Pre-mkt % | Post-mkt % | Move vs avg daily | Ref close | Ref source | Ref asof | US tradeable | Last earnings | Tag | Earn | Catalyst |")
A("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
for sym, c in tagged:
    r = us_ref.get(sym)
    rc, rs, ra, sa = ref_cols(r)
    cat, earn = catalyst_cell(c["name"])
    A(f"| {c['name']} | {c['ex']} | {c['close']} | {c['change']:.2f} | "
      f"{pct(c['pm'])} | {pct(c['po'])} | {multiple(headline_move(c), (r or {}).get('avg_daily_move'))} | "
      f"{rc} | {rs} | {ra} | {c.get('us_tradeable','—')} | {er_cell(c)} | {c['tag']} | {earn} | {cat} |")
A("")
A("## US — QUIET one-liners")
A("")
A("| Ticker | Venue | Chg % | Pre-mkt % | Post-mkt % | Move vs avg daily | Ref close | Ref source | Ref asof | US tradeable | Earn | Catalyst |")
A("|---|---|---|---|---|---|---|---|---|---|---|---|")
for sym, c in quiet[:15]:
    r = us_ref.get(sym)
    rc, rs, ra, sa = ref_cols(r)
    cat, earn = catalyst_cell(c["name"])
    A(f"| {c['name']} | {c['ex']} | {c['change']:.2f} | {pct(c['pm'])} | {pct(c['po'])} | "
      f"{multiple(headline_move(c), (r or {}).get('avg_daily_move'))} | "
      f"{rc} | {rs} | {ra} | {c.get('us_tradeable','—')} | {earn} | {cat} |")
if not quiet:
    A("| — | — | — | — | — | — | — | — | — | — | — | — |")
A("")
A("## EU/UK — Headline table")
A("")
A("| Ticker | Market | Venue | Close | Chg % | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | Session asof | Settle | US tradeable | Last earnings | Earn | Catalyst |")
A("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
for r0 in eu_final:
    d = r0["d"]
    r = r0["ref"]
    rc, rs, ra, sa = ref_cols(r)
    cat, earn = catalyst_cell(g(d, "name"))
    A(f"| {g(d,'name')} | {r0['market']} | {g(d,'exchange')} | {g(d,'close')} | "
      f"{g(d,'change'):+.2f} | {g(d,'currency')} | {multiple(g(d,'change'), (r or {}).get('avg_daily_move'))} | "
      f"{rc} | {rs} | {ra} | {sa} | {settle_state(r)} | {us_tradeable_foreign(g(d,'name'), g(d,'country'))} | "
      f"{epoch_date(g(d,'earnings_release_date')) or '—'} | {earn} | {cat} |")
A("")
A("## AU (ASX) — Headline table")
A("")
A("| Ticker | Venue | Close | Chg % | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | Session asof | Settle | US tradeable | Last earnings | Earn | Catalyst |")
A("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
for r0 in au:
    d = r0["d"]
    r = r0["ref"]
    rc, rs, ra, sa = ref_cols(r)
    cat, earn = catalyst_cell(g(d, "name"))
    A(f"| {g(d,'name')} | {g(d,'exchange')} | {g(d,'close')} | {g(d,'change'):+.2f} | "
      f"{g(d,'currency')} | {multiple(g(d,'change'), (r or {}).get('avg_daily_move'))} | "
      f"{rc} | {rs} | {ra} | {sa} | {settle_state(r)} | {us_tradeable_foreign(g(d,'name'), g(d,'country'))} | "
      f"{epoch_date(g(d,'earnings_release_date')) or '—'} | {earn} | {cat} |")
A("")
A("## APAC/Gulf — Headline table")
A("")
A("| Ticker | Market | Venue | Close | Chg % | Currency | Move vs avg daily | Ref close | Ref source | Ref asof | Session asof | Settle | US tradeable | Last earnings | Earn | Catalyst |")
A("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
for r0 in apac:
    d = r0["d"]
    r = r0["ref"]
    rc, rs, ra, sa = ref_cols(r)
    cat, earn = catalyst_cell(g(d, "name"))
    A(f"| {g(d,'name')} | {r0['market']} | {g(d,'exchange')} | {g(d,'close')} | "
      f"{g(d,'change'):+.2f} | {g(d,'currency')} | {multiple(g(d,'change'), (r or {}).get('avg_daily_move'))} | "
      f"{rc} | {rs} | {ra} | {sa} | {settle_state(r)} | {us_tradeable_foreign(g(d,'name'), g(d,'country'))} | "
      f"{epoch_date(g(d,'earnings_release_date')) or '—'} | {earn} | {cat} |")
if not apac:
    A("| — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |")
A("")
A("## Source health")
A("")
A(f"- scanner_calls: {health['scanner_calls']} | scanner_errors: {health['scanner_errors']}")
A(f"- markets_scanned: US + {len(EU_MARKETS)} EU/UK + ASX + {len(APAC_MARKETS)} APAC/Gulf "
  f"({', '.join(APAC_MARKETS)})")
A(f"- pipeline_version: {SCRIPT_VERSION}" +
  (f" | self-healed at start of run from {SELF_HEALED['from']} to {SELF_HEALED['to']} "
   f"via {SELF_HEALED['source']} (the cron's fetch served a stale copy)"
   if SELF_HEALED["done"] else ""))
A("- et_clock: zoneinfo America/New_York (DST-aware; a fixed UTC-4 mislabels every "
  "winter fire)")
A("- premarket_window: 04:00-09:30 ET, resolved with zoneinfo (09:00-14:30 UTC in "
  "winter, 08:00-13:30 UTC in summer)")
A("- session_selection: by DATE and order, never by a modal time-of-day. Yahoo stamps a "
  "daily bar at the session open, so the ET stamp of the SAME session shifts by one "
  "hour across a DST boundary; a modal filter kept the OLDER bars and discarded the "
  "NEWEST ones, which rolled the base back to the prior-prior session (66 US + 21 ASX "
  "rows lost on 2026-11-03, 24 of 25 ASX rows lost on 2026-11-04).")
A(f"- yahoo_calls: {health['yahoo_calls']} | yahoo_429: {health['yahoo_429']} | "
  f"yahoo_errors: {health['yahoo_errors']}")
cc = health["cross_check"]
A(f"- reference_close (screener vs Yahoo, resolved BEFORE the tables were built): "
  f"agree={cc['agree']} mismatch={cc['mismatch']} unverified={cc['unverified']} "
  f"stale_reference={cc['stale']}")
A(f"  method: the screener's implied reference close (close / (1 + change/100)) is compared")
A(f"  with Yahoo's own reference close. A match proves the move was measured against the")
A(f"  TRUE prior close; a mismatch means the row sits on a STALE reference (phantom move).")
A(f"  Coverage: every row of the US headline, US QUIET, EU/UK and ASX tables is checked.")
A(f"  Yahoo bar mode: {json.dumps(cc['by_mode'])} (closed = last completed session bar;")
A(f"  live = in-progress EU/UK session bar, which is what a weekday 08:00 ET EU move needs)")
if cc["drift"]:
    _dr = sorted(abs(x) for x in cc["drift"])
    A(f"  live drift between the screener snapshot and the later Yahoo print: "
      f"median={_dr[len(_dr)//2]:.2f}pp max={_dr[-1]:.2f}pp (expected on a live market)")
if cc["mismatch_detail"]:
    A(f"- cross_check mismatches: {json.dumps(cc['mismatch_detail'])}")
A(f"- rows_dropped_stale_ref: {health['rows_dropped_stale_ref']} "
  f"(rows whose screener-implied reference close disagreed with Yahoo's by more than "
  f"{REF_CLOSE_TOLERANCE_PCT}%; they are dropped, not published)")
A(f"- rows_dropped_unresolved_ref: {health['rows_dropped_unresolved_ref']} "
  f"(rows whose reference close could not be resolved from Yahoo at all - the base of the "
  f"move is unverifiable, so the row is dropped rather than published with a '—' base)")
if cross_region_dropped:
    A(f"- cross_region_rows_dropped: {cross_region_dropped} (the same name on a US venue "
      f"and a foreign venue - the US row is kept so the name appears exactly once)")
pmc = health["premarket_check"]
A(f"- us_premarket_check (Yahoo 1-min pre/post feed vs the screener pre-market column, "
  f"base = the IMMEDIATELY prior session's close): "
  f"checked={pmc['checked']} within_1pp={pmc['within_1pp']} within_3pp={pmc['within_3pp']} "
  f"unavailable={pmc['unavailable']}")
if pmc["outliers"]:
    A(f"  us_premarket outliers (>3pp; thin pre-market books, not a screener error): "
      f"{json.dumps(pmc['outliers'])}")
A(f"- markets_with_lt5_rows: {health['empty_markets'] or 'none'}")
A(f"  NOTE: this fires per market AND direction, so it is NOT a coverage-failure signal on")
A(f"  its own. A 'less' count of 0-3 means almost nothing fell more than 2.5% that session")
A(f"  (a broad up-day); a small 'egreater' count usually means a small market with few")
A(f"  names above the $1B market-cap floor. Check the median change before calling it a gap.")
A(f"- filters: volume>{MIN_VOLUME} (removes stale-reference rows), country=home for EU/UK/AU,")
A(f"  exchange drop-list for US, US venue allow-list, US preferred (slash ticker) excluded")
A(f"- volume_floor_note: volume>{MIN_VOLUME} removes MOST stale-reference rows, but a row can")
A(f"  still sit on a stale reference when its only volume came from one thin day (verified")
A(f"  2026-10-26: LSE 50GP cleared the floor on 12,000 shares dated 2026-10-15 while Yahoo")
A(f"  showed no bar for the scan date). The reference-close cross-check is what catches")
A(f"  those; rows that fail it are dropped from the tables, not published.")
A(f"- us_preferred_dropped: {a_dropped_pref}")
A(f"- bod_no_extended_hours: {len(bod)} (deferred to the next scan; not in the headline table)")
A(f"- earnings_source: screener `earnings_release_date` (last FULL report) + "
  f"`earnings_release_next_date` (next scheduled)")
A(f"- earnings_caveat: `earnings_release_date` does NOT capture preliminary, guidance or")
A(f"  restructuring releases. On 2026-10-23 LKQ fell 22.47% on a preliminary Q3 miss while")
A(f"  the field still read 2026-07-30. ALWAYS confirm the earnings-driven flag against the")
A(f"  headline itself; the calendar field is a screen, not a verdict.")
A(f"- us_line_index: {'ok' if health['us_line_index_ok'] else 'EMPTY'} "
  f"(US-listed lines for the {len(FOREIGN_HOME_COUNTRIES)} foreign home countries, both "
  f"scanner types; the `US tradeable` column is ADR / US-listed / none)")
A(f"- catalyst_note: {catalyst_note if catalyst_note else 'none'}")
A(f"- catalyst_budget: {CATALYST_BUDGET['US']} US + {CATALYST_BUDGET['EU']} EU + "
  f"{CATALYST_BUDGET['AU']} AU = "
  f"{CATALYST_BUDGET['US']+CATALYST_BUDGET['EU']+CATALYST_BUDGET['AU']} lookups per run")
A(f"- one_table_rule: each name appears exactly once, in exactly one table, with its")
A(f"  catalyst in that row's last column. There is no separate catalysts section.")
A(f"- data_date: US regular session close of the prior trading day; extended-hours columns")
A(f"  carry the prior session's prints")
A(f"- settlement_state: {_settle_summary()}")
A(f"- rows_per_market (EU/UK, cap {EU_MARKET_CAP}/market): "
  f"{health.get('rows_per_market') or {}} — the cap stops one thin market taking the table; "
  f"the EU/UK table was 28% Sweden over nine runs (73 of 264 rows) while Belgium and "
  f"Greece never appeared once.")
A(f"- rows_per_market (APAC/Gulf, cap {APAC_MARKET_CAP}/market): "
  f"{health.get('rows_per_market_apac') or {}}")
A(f"- deprecations: mcp__tradingview-advanced__*, mcp__tradingview__*, mcp__financekit__*,")
A(f"  mcp__stocktwits__* are ABSENT in Cloud sessions (tool_search 0 hits; connector catalog")
A(f"  holds only media + credential tools). The public screener replaces them.")
A("")
A(f"- degraded_sources: {len(DEGRADED)}")
if DEGRADED:
    A(f"  (the chat reply's `errors:` MUST equal this number - one entry per degraded")
    A(f"  source, not one per run)")
    for i, (s, d) in enumerate(DEGRADED, 1):
        A(f"  {i}. {s} — {d}")
else:
    A("  (none - every source answered for every published row)")
A("")
A("## Audit line")
A("")
A(f"`earnings-reaction target=earnings-reactions:{RUN_DATE} candidates={len(us)} "
  f"amc_reactions={len(amc)} pre_gaps={len(gaps)} eu_reactions={len([r for r in eu_final if abs(g(r['d'],'change'))>3])} "
  f"asx_reactions={len([r for r in au if abs(g(r['d'],'change'))>3])} "
  f"apac_reactions={len([r for r in apac if abs(g(r['d'],'change'))>3])} "
  f"catalyst_lookups={len(catalysts)} bod={len(bod)} "
  f"rows_dropped_stale_ref={health['rows_dropped_stale_ref']} "
  f"rows_dropped_unresolved_ref={health['rows_dropped_unresolved_ref']} "
  f"degraded_sources={len(DEGRADED)}`")
A("")

out = os.path.join(OUT_DIR, OUT_NAME)
with open(out, "w") as fh:
    fh.write("\n".join(L))

targets = {"us": [{"name": c["name"], "tag": c["tag"], "last_earnings": epoch_date(c.get("er"))}
                  for c in targets_us],
           "eu": [{"name": n, "chg": next((round(g(r0['d'], 'change'), 2) for r0 in eu_final
                                          if g(r0['d'], 'name') == n), None)}
                  for n in targets_eu],
           "au": [{"name": n, "chg": next((round(g(r0['d'], 'change'), 2) for r0 in au
                                          if g(r0['d'], 'name') == n), None)}
                  for n in targets_au],
           "apac": [{"name": n, "market": next((r0['market'] for r0 in apac
                                                if g(r0['d'], 'name') == n), None),
                     "chg": next((round(g(r0['d'], 'change'), 2) for r0 in apac
                                  if g(r0['d'], 'name') == n), None)}
                    for n in targets_apac],
           "budget": CATALYST_BUDGET,
           "catalyst_file": CAT_FILE}
with open(os.path.join(OUT_DIR, f"{RUN_DATE}-catalyst-targets.json"), "w") as fh:
    json.dump(targets, fh, indent=2)

print(f"WROTE {out} ({os.path.getsize(out)} bytes)")
print(f"WROTE {os.path.join(OUT_DIR, f'{RUN_DATE}-catalyst-targets.json')}")
print(f"REPLY_ERRORS: {len(DEGRADED)}")
print(json.dumps({"us_total": len(us), "tagged": len(tagged), "quiet": len(quiet),
                  "eu": len(eu_final), "au": len(au),
                  "rows_dropped_stale_ref": health["rows_dropped_stale_ref"],
                  "degraded_sources": len(DEGRADED),
                  "cross_check": cc}, indent=2))
