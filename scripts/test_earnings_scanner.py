#!/usr/bin/env python3
"""test_earnings_scanner.py — regression tests for cron #15's pipeline code.

Why this suite exists in THIS repo: `scripts/earnings_reaction_scanner.py`
self-heals - every cron fire fetches this file from `main` and adopts it - so a
push here IS a deploy to the fleet. The pre-commit hook runs this suite, which
means a regression in the scanner now blocks the commit that would ship it.
(The migration repo's `tools/test_reaction_contract.py` covers the session and
pre-market helpers and the artifact checker; this suite covers the rest.)

What it pins, each with the incident that motivated it:

  * YAHOO RATE LIMITS ARE CLASSIFIED BY STATUS. Yahoo's measured 429 bodies
    are `Too Many Requests` and a 23-byte non-JSON body (mcp-health/2026-W46);
    the old test looked for the text "429" in the body, so a real rate limit
    was counted as `yahoo_errors` and `yahoo_429` could never fire.
  * THE CIRCUIT BREAKER. An egress-wide block must cost a bounded number of
    calls, latch, and surface as a banner - while scattered 429s on a healthy
    egress never trip it, and a latched breaker still drops-and-counts rows
    rather than publishing them unverified.
  * THE REGION-MATCHED CATALYST MERGE. DMP on XETR (a German mortgage bank)
    published the ASX DMP's catalyst on 2026-11-12. And the alias table held
    slashed spellings that the normalised labels could never equal, so
    "EU/UK", "APAC", "Gulf" and "Asia-Pacific" catalog cells silently fell to
    the placeholder (fixed 2026-11-15).
  * THE VERDICT FOLLOWS THE RESEARCH. A row whose lookup was not performed
    carries no Y/N verdict (the 2026-11-05 run published "N" beside "lookup
    not performed").
  * THE REGION FIX SURVIVES THE CALENDAR CELL. The pipeline-2026-11-15.1/.2
    commits were built on a pre-fix copy and reverted the region match while
    adding the US calendar cell; the merge keeps both, and a US row whose
    ticker is only another region's must fall through to its calendar line.

HOW THE CODE IS LOADED. The scanner runs its whole pipeline at import time,
self-heal included, so it cannot be imported. Instead the side-effect-free
region between its PURE-HELPERS markers is executed with TRIPWIRES on
subprocess and os: if the region ever performs a side effect at load time the
suite fails loudly instead of re-executing and overwriting the file under test.
Network-touching functions are exercised through a FAKE `_curl` placed in that
namespace, so nothing here leaves the machine.

Offline and dependency-free: the Cloud sandbox has no PyPI access.

  python3 scripts/test_earnings_scanner.py
  EARNINGS_SCANNER=/path/to/copy.py python3 scripts/test_earnings_scanner.py
      (run against another copy - how a mutation check is done: break the
       behaviour in a copy, and the test that covers it must fail)

Exit: 0 = all passed, 1 = a test failed.
"""
import datetime
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
SCANNER = os.environ.get("EARNINGS_SCANNER") or os.path.join(
    HERE, "earnings_reaction_scanner.py")

BEGIN = "# ==== PURE-HELPERS-BEGIN"
END = "# ==== PURE-HELPERS-END"


# ------------------------------------------------------------------- loader

def load_pure(path=SCANNER):
    """Execute the scanner's pure region; return (namespace, side_effects).

    Same contract as the migration repo's loader: subprocess.run, os.execv,
    os.remove and os.makedirs are tripwires that RECORD the attempt and raise,
    so a region that reaches for the network, the filesystem or the process
    table at load time can never actually do so.
    """
    with open(path, encoding="utf-8") as fh:
        src = fh.read()
    if BEGIN not in src or END not in src:
        raise RuntimeError("the scanner has no PURE-HELPERS markers - it cannot be "
                           "loaded without running the pipeline and the self-heal")
    body = src.split(BEGIN, 1)[1].split(END, 1)[0]
    body = "\n".join(body.split("\n")[1:])      # drop the rest of the marker line
    calls = []

    def trip(name):
        def _boom(*_a, **_k):
            calls.append(name)
            raise AssertionError("the pure region called %s" % name)
        return _boom

    class TripSubprocess:
        run = staticmethod(trip("subprocess.run"))
        PIPE = subprocess.PIPE

    class TripOS:
        execv = staticmethod(trip("os.execv"))
        remove = staticmethod(trip("os.remove"))
        makedirs = staticmethod(trip("os.makedirs"))
        path = os.path
        environ = os.environ

    class FakeTime:
        """Records sleeps instead of sleeping, so the breaker's pause is
        observable and the suite stays fast."""
        slept = []

        @staticmethod
        def sleep(s):
            FakeTime.slept.append(s)

    FakeTime.slept = []
    ns = {"json": json, "subprocess": TripSubprocess, "time": FakeTime,
          "datetime": datetime, "os": TripOS, "sys": sys, "re": re,
          "__file__": path, "__name__": "earnings_scanner_pure"}
    exec(compile(body, path, "exec"), ns)
    return ns, calls


class FakeCurl:
    """Stands in for the scanner's `_curl`. Serves (status, body) answers in
    order, repeating the last one, and records every call it was asked for."""

    def __init__(self, answers):
        self.answers = list(answers)
        self.calls = []

    def __call__(self, args, timeout=45):
        self.calls.append(list(args))
        status, body = self.answers[min(len(self.calls), len(self.answers)) - 1]
        if "-w" in args:     # _curl_status appends the status line, as curl does
            out = "%s\n%s" % (body, status)
        else:
            out = body

        class R:
            stdout = out
            stderr = ""
            returncode = 0
        return R()


def bars_body(n=25):
    """A minimal, valid Yahoo daily-chart body with n sessions."""
    t0 = 1761000000
    return json.dumps({"chart": {"result": [{
        "timestamp": [t0 + i * 86400 for i in range(n)],
        "indicators": {"quote": [{"close": [100.0 + i for i in range(n)]}]},
    }]}})


THROTTLE_BODY = "Too Many Requests"       # Yahoo's measured 429 body (W46)
OK = (200, None)                           # placeholder, filled with bars_body()


class ScannerCase(unittest.TestCase):
    """A FRESH namespace per test: health counters and breaker state are
    module globals, so sharing them would make tests depend on order."""

    def setUp(self):
        self.ns, self.load_calls = load_pure()
        self.ns["YAHOO_BREAKER_PAUSE_S"] = 0

    def use_curl(self, answers):
        answers = [(s, bars_body() if b is None else b) for s, b in answers]
        fake = FakeCurl(answers)
        self.ns["_curl"] = fake
        return fake


# ------------------------------------------------------------- the region

class PureRegion(ScannerCase):
    def test_region_loads_without_side_effects(self):
        self.assertEqual(self.load_calls, [],
                         "executing the pure region performed a side effect: %r"
                         % self.load_calls)

    def test_self_heal_call_sits_below_the_end_marker(self):
        """Inside the region the loader would RUN the self-heal, which
        re-execs and overwrites the file under test."""
        with open(SCANNER, encoding="utf-8") as fh:
            src = fh.read()
        call = re.search(r"^_self_heal\(\)\s*$", src, re.M)
        self.assertIsNotNone(call, "the self-heal call was not found")
        self.assertGreater(call.start(), src.index(END),
                           "the self-heal CALL is inside the pure region")

    def test_the_functions_under_test_are_in_the_region(self):
        for name in ("classify_yahoo_response", "_yahoo_get", "yahoo_daily_bars",
                     "cross_check", "reference_close_banner", "record_yahoo_rate_limit",
                     "parse_catalyst_file", "_same_region", "catalyst_cell",
                     "verdict_for", "cal_event_cell", "event_freshness"):
            self.assertIn(name, self.ns, "%s is not defined inside the pure region"
                          % name)


# ----------------------------------------------------- Yahoo classification

class YahooClassification(ScannerCase):
    def test_a_429_status_is_rate_limited(self):
        c = self.ns["classify_yahoo_response"]
        self.assertEqual(c(429, THROTTLE_BODY), "rate_limited")
        self.assertEqual(c(429, ""), "rate_limited",
                         "the 23-byte non-JSON / empty 429 body must still be a 429")

    def test_the_throttle_phrase_is_rate_limited_under_another_status(self):
        """A proxy can relay Yahoo's throttle page as a 200."""
        self.assertEqual(self.ns["classify_yahoo_response"](200, THROTTLE_BODY),
                         "rate_limited")

    def test_a_json_body_that_contains_429_is_ok(self):
        """The old body test read any '429' in the first 200 bytes as a rate
        limit - a price of 429.x would have dropped a healthy row."""
        body = '{"chart":{"result":[{"meta":{"regularMarketPrice":429.5}}]}}'
        self.assertEqual(self.ns["classify_yahoo_response"](200, body), "ok")

    def test_error_statuses_and_empty_bodies_are_errors(self):
        c = self.ns["classify_yahoo_response"]
        for status, body in ((404, '{"chart":{"error":"Not Found"}}'),
                             (500, "oops"), (0, ""), (200, ""), (200, "   ")):
            self.assertEqual(c(status, body), "error", "(%r, %r)" % (status, body))

    def test_a_real_429_counts_as_a_429_not_an_error(self):
        """THE bug: Yahoo's real throttle body has no '429' in it, so the old
        code counted every rate limit as `yahoo_errors`."""
        self.use_curl([(429, THROTTLE_BODY)])
        self.assertIsNone(self.ns["yahoo_daily_bars"]("AAPL"))
        h = self.ns["health"]
        self.assertEqual(h["yahoo_429"], 1, "a real 429 was not counted as a 429")
        self.assertEqual(h["yahoo_errors"], 0, "a real 429 was counted as an error")

    def test_a_good_answer_returns_bars(self):
        self.use_curl([OK])
        bars = self.ns["yahoo_daily_bars"]("AAPL")
        self.assertEqual(len(bars), 25)
        self.assertEqual(self.ns["health"]["yahoo_calls"], 1)


# ------------------------------------------------------------- the breaker

class Breaker(ScannerCase):
    def fetch(self, n):
        return [self.ns["yahoo_daily_bars"]("SYM%d" % i) for i in range(n)]

    def test_an_egress_block_latches_after_the_threshold_and_one_retry(self):
        """Every answer is a 429: the breaker trips at the threshold, pauses
        ONCE, retries ONCE, latches - and makes no further call."""
        fake = self.use_curl([(429, THROTTLE_BODY)])
        th = self.ns["YAHOO_BREAKER_THRESHOLD"]
        results = self.fetch(40)
        br = self.ns["yahoo_breaker"]
        self.assertTrue(all(r is None for r in results))
        self.assertEqual(br["state"], "latched")
        self.assertEqual(len(fake.calls), th + 1,
                         "an egress block cost %d calls; the breaker should stop "
                         "it at %d" % (len(fake.calls), th + 1))
        self.assertEqual(br["skipped"], 40 - th)
        self.assertEqual(self.ns["time"].slept, [0], "expected exactly one pause")

    def test_a_burst_that_clears_recovers_and_keeps_calling(self):
        th = self.ns["YAHOO_BREAKER_THRESHOLD"]
        fake = self.use_curl([(429, THROTTLE_BODY)] * th + [OK])
        results = self.fetch(th + 3)
        br = self.ns["yahoo_breaker"]
        self.assertEqual(br["state"], "closed", "a burst that cleared latched")
        self.assertTrue(br["recovered"])
        # The call that tripped the breaker returns the RETRY's good answer.
        self.assertIsNotNone(results[th - 1])
        self.assertTrue(all(r is not None for r in results[th - 1:]))
        self.assertEqual(len(fake.calls), th + 1 + 3)

    def test_scattered_429s_on_a_healthy_egress_never_trip_it(self):
        """Any non-429 answer proves Yahoo is reachable and resets the count -
        including a 404 for an unknown symbol."""
        th = self.ns["YAHOO_BREAKER_THRESHOLD"]
        pattern = [(429, THROTTLE_BODY)] * (th - 1) + [(404, '{"chart":{"error":{}}}')]
        fake = self.use_curl(pattern * 6)
        self.fetch(len(pattern) * 6)
        br = self.ns["yahoo_breaker"]
        self.assertEqual(br["state"], "closed")
        self.assertFalse(br["retried"], "scattered 429s spent the retry")
        self.assertEqual(len(fake.calls), len(pattern) * 6, "a call was skipped")

    def test_a_second_run_of_429s_latches_without_another_pause(self):
        th = self.ns["YAHOO_BREAKER_THRESHOLD"]
        self.use_curl([(429, THROTTLE_BODY)] * th + [OK] * 3
                      + [(429, THROTTLE_BODY)])
        self.fetch(th + 2 + th + 5)
        br = self.ns["yahoo_breaker"]
        self.assertEqual(br["state"], "latched")
        self.assertEqual(len(self.ns["time"].slept), 1,
                         "the pause-and-retry was spent twice in one run")

    def test_a_latched_breaker_still_drops_and_counts_the_row(self):
        """The hard gate is not relaxed: no row is published unverified, and
        no further network call is made."""
        fake = self.use_curl([(429, THROTTLE_BODY)])
        self.fetch(self.ns["YAHOO_BREAKER_THRESHOLD"])       # latch it
        before_calls = len(fake.calls)
        h = self.ns["health"]
        before_drops = h["rows_dropped_unresolved_ref"]
        meta = self.ns["cross_check"]("SAP", 3.0, 103.0, ".DE", "germany",
                                      live_session=True, venue="germany")
        self.assertIsNone(meta, "a row was published without a reference close")
        self.assertEqual(h["rows_dropped_unresolved_ref"], before_drops + 1,
                         "the dropped row was not counted")
        self.assertEqual(len(fake.calls), before_calls,
                         "a latched breaker still called Yahoo")

    def test_the_banner_appears_only_when_latched(self):
        banner = self.ns["reference_close_banner"]
        self.assertEqual(banner(), [], "a banner was printed with Yahoo answering")
        self.use_curl([(429, THROTTLE_BODY)])
        self.fetch(self.ns["YAHOO_BREAKER_THRESHOLD"] + 2)
        self.ns["health"]["rows_dropped_unresolved_ref"] = 7
        lines = banner()
        text = "\n".join(lines)
        self.assertIn("INCOMPLETE", text)
        self.assertIn("7 row(s) were dropped", text)
        # It must not open a `##` section: the artifact checker enforces the
        # section order, and a new heading would sit outside it.
        for line in lines:
            self.assertTrue(line == "" or line.startswith(">"),
                            "the banner line %r is not part of a blockquote" % line)

    def test_a_small_run_that_was_all_429s_is_still_flagged(self):
        """Found by the end-to-end harness: a 3-row settle pass never reaches
        the threshold, so the breaker never latches - yet all 3 rows were
        dropped. The banner must still appear."""
        self.use_curl([(429, THROTTLE_BODY)])
        self.fetch(self.ns["YAHOO_BREAKER_THRESHOLD"] - 2)
        self.assertEqual(self.ns["yahoo_breaker"]["state"], "closed")
        self.assertTrue(self.ns["reference_close_unverifiable"]())
        self.assertIn("Every one of the 3 Yahoo call(s)",
                      "\n".join(self.ns["reference_close_banner"]()))

    def test_one_429_among_good_answers_is_not_unverifiable(self):
        self.use_curl([(429, THROTTLE_BODY), OK, OK])
        self.fetch(3)
        self.assertFalse(self.ns["reference_close_unverifiable"]())
        self.assertEqual(self.ns["reference_close_banner"](), [])

    def test_a_rate_limit_is_a_degraded_source_with_the_final_counts(self):
        self.use_curl([(429, THROTTLE_BODY), OK, OK, (429, THROTTLE_BODY), OK])
        self.fetch(5)
        self.ns["record_yahoo_rate_limit"]()
        degraded = dict(self.ns["DEGRADED"])
        self.assertIn("yahoo_chart_api.rate_limited", degraded)
        self.assertIn("2 of 5 Yahoo calls answered HTTP 429",
                      degraded["yahoo_chart_api.rate_limited"])

    def test_no_429_means_no_rate_limit_entry(self):
        self.use_curl([OK])
        self.fetch(3)
        self.ns["record_yahoo_rate_limit"]()
        self.assertNotIn("yahoo_chart_api.rate_limited", dict(self.ns["DEGRADED"]))

    def test_the_health_line_names_the_breaker_state(self):
        line = self.ns["yahoo_breaker_line"]
        self.assertIn("yahoo_breaker: closed", line())
        self.use_curl([(429, THROTTLE_BODY)])
        self.fetch(self.ns["YAHOO_BREAKER_THRESHOLD"] + 4)
        self.assertIn("yahoo_breaker: LATCHED", line())
        self.assertIn("4 further Yahoo call(s) were not made", line())


# ------------------------------------------------- region-matched catalysts

class RegionMatchedCatalysts(ScannerCase):
    def setUp(self):
        super().setUp()
        self.tmp = tempfile.mkdtemp(prefix="scanner-test-")

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def catalog(self, rows):
        path = os.path.join(self.tmp, "catalog.md")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write("Catalyst lookups: test.\n\n"
                     "| Ticker | Region | Catalyst | Earnings-driven |\n"
                     "|---|---|---|---|\n")
            for r in rows:
                fh.write("| %s | %s | %s | %s |\n" % r)
        mapping, _note = self.ns["parse_catalyst_file"](path)
        self.ns["catalysts"] = mapping
        return mapping

    def test_the_dmp_case_each_venue_gets_its_own_catalyst(self):
        """THE 2026-11-12 incident: one ticker, two companies."""
        self.catalog([("DMP", "EU", "Deutsche Pfandbriefbank Q3: NII down", "Y"),
                      ("DMP", "AU", "Domino's AGM: same-store sales soft", "N")])
        cell = self.ns["catalyst_cell"]
        self.assertEqual(cell("DMP", "EU"), ("Deutsche Pfandbriefbank Q3: NII down", "Y"))
        self.assertEqual(cell("DMP", "AU"), ("Domino's AGM: same-store sales soft", "N"))

    def test_a_ticker_only_in_another_region_gets_the_placeholder(self):
        self.catalog([("DMP", "AU", "Domino's AGM: same-store sales soft", "N")])
        cat, earn = self.ns["catalyst_cell"]("DMP", "EU")
        self.assertNotIn("Domino", cat, "another company's catalyst was published")
        self.assertEqual(earn, "—", "a placeholder row carried a verdict")

    def test_aliases_match_their_own_region(self):
        """THE 2026-11-15 bug: the slashed aliases could never match."""
        same = self.ns["_same_region"]
        for cat, row in (("EU", "EU"), ("Europe", "EU"), ("EU/UK", "EU"),
                         ("EU & UK", "EU"), ("UK", "EU"),
                         ("ASX", "AU"), ("Australia", "AU"),
                         ("APAC/Gulf", "APAC/Gulf"), ("APAC", "APAC/Gulf"),
                         ("Gulf", "APAC/Gulf"), ("Asia-Pacific", "APAC/Gulf"),
                         ("apac / gulf", "APAC/Gulf"), ("USA", "US")):
            self.assertTrue(same(cat, row), "%r should match a %r row" % (cat, row))

    def test_aliases_never_cross_regions(self):
        same = self.ns["_same_region"]
        for cat, row in (("AU", "EU"), ("ASX", "EU"), ("EU", "APAC/Gulf"),
                         ("EU/UK", "AU"), ("US", "EU"), ("Gulf", "AU"),
                         ("Asia Pacific", "AU"), ("UK", "US"), ("", "EU")):
            self.assertFalse(same(cat, row), "%r must not match a %r row" % (cat, row))

    def test_an_unknown_label_matches_only_itself(self):
        same = self.ns["_same_region"]
        self.assertTrue(same("LatAm", "latam"))
        self.assertFalse(same("LatAm", "EU"))

    def test_an_aliased_catalog_cell_reaches_its_row(self):
        """End to end: before the fix, a catalog cell labelled `APAC` was
        replaced by the placeholder on the APAC/Gulf row."""
        self.catalog([("2222", "APAC", "Aramco Q3 profit beat; dividend held", "Y")])
        self.assertEqual(self.ns["catalyst_cell"]("2222", "APAC/Gulf"),
                         ("Aramco Q3 profit beat; dividend held", "Y"))

    def test_a_regionless_catalog_is_still_used(self):
        """A catalog written before the Region column existed is the only
        research there is; it must not be thrown away."""
        self.catalog([("SAP", "", "SAP Q3 cloud backlog +22%", "Y")])
        self.assertEqual(self.ns["catalyst_cell"]("SAP", "EU"),
                         ("SAP Q3 cloud backlog +22%", "Y"))

    def _calendar(self, symbol, date):
        """Upstream's bulk-calendar run state, as fetch_earnings_calendar builds it."""
        self.ns["CAL"] = {symbol: {"date": date, "time": "time-not-supplied",
                                   "eps": "$0.42", "fiscal": "Sep/2026", "name": symbol}}

    def test_a_us_row_nobody_searched_gets_the_calendar_cell(self):
        """Upstream's 2026-11-15 calendar cell: a fact, no headline, no verdict."""
        self.ns["catalysts"] = {}
        self._calendar("NBIS", self.ns["RUN_DATE"])
        cat, earn = self.ns["catalyst_cell"]("NBIS", "US")
        self.assertIn("report date today (Nasdaq earnings calendar; no headline lookup)", cat)
        self.assertEqual(earn, "—", "a calendar fact carried a verdict")

    def test_the_calendar_cell_is_us_only(self):
        """The Nasdaq calendar reaches no other market."""
        self.ns["catalysts"] = {}
        self._calendar("DMP", self.ns["RUN_DATE"])
        cat, _earn = self.ns["catalyst_cell"]("DMP", "EU")
        self.assertNotIn("Nasdaq earnings calendar", cat)

    def test_a_us_row_whose_ticker_is_another_regions_falls_back_to_the_calendar(self):
        """THE MERGE CASE: the region fix and the calendar cell together. The
        catalog holds the ticker only under EU - a different company - so the
        US row must skip that entry and fall through to its own calendar line,
        not publish the European company's catalyst."""
        self.catalog([("DMP", "EU", "Deutsche Pfandbriefbank Q3: NII down", "Y")])
        self._calendar("DMP", self.ns["RUN_DATE"])
        cat, earn = self.ns["catalyst_cell"]("DMP", "US")
        self.assertNotIn("Pfandbriefbank", cat, "another region's catalyst was published")
        self.assertIn("Nasdaq earnings calendar", cat)
        self.assertEqual(earn, "—")

    def test_a_budget_name_with_no_catalog_entry_is_pending(self):
        self.ns["catalysts"] = {}
        self.ns["TARGET_SET"] = {"SAP"}
        self.assertEqual(self.ns["catalyst_cell"]("SAP", "EU"),
                         ("pending catalyst lookup", "—"))
        self.assertEqual(self.ns["catalyst_cell"]("BMW", "EU"),
                         ("no catalyst lookup (outside the per-run budget)", "—"))


class Verdicts(ScannerCase):
    def test_the_verdict_follows_the_research(self):
        """THE 2026-11-05 bug: "N" beside "catalyst lookup not performed"."""
        v = self.ns["verdict_for"]
        self.assertEqual(v("catalyst lookup not performed", "N"), "—")
        self.assertEqual(v("pending catalyst lookup", "Y"), "—")
        self.assertEqual(v("no catalyst lookup (outside the per-run budget)", "N"), "—")

    def test_a_researched_nothing_is_still_a_verdict(self):
        v = self.ns["verdict_for"]
        self.assertEqual(v("no fresh catalyst found", "N"), "N")
        self.assertEqual(v("Q3 beat, guidance raised", "Y"), "Y")

    def test_an_unknown_flag_is_no_verdict(self):
        self.assertEqual(self.ns["verdict_for"]("Q3 beat", "maybe"), "—")


if __name__ == "__main__":
    unittest.main(verbosity=2 if "-v" in sys.argv else 1,
                  argv=[a for a in sys.argv if a != "-v"])
