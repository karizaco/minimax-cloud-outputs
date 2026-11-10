#!/usr/bin/env python3
"""test_builders.py — regression tests for the derived-view builders.

Why: each builder joins cron artifacts into a view. A builder that reads the
wrong column, or groups two rows that should be one, produces a plausible
artifact with a wrong number in it, and nothing in the repo says so. Three
such failures have shipped:

  - the setup journal grouped the stylist combination by its RAW SPELLING, so
    `peoplewish|qullamaggie` and `qullamaggie|peoplewish` were two groups with
    medians of -7.57 and +2.34. The same people, opposite conclusions, from
    spelling alone;
  - the gap reconciliation picked the session to join against from the
    reactions file's `Ref asof` column, which is the base of the `Chg %` column
    and NOT of the pre-market column. That dated the join two sessions early
    and turned held gaps into false reversals - 141 of 198 "reversed";
  - the run ledger called a routine's first days a "miss", when the fleet was
    still starting up.

Every builder is run against a SYNTHETIC mini-repo in a temp directory, so a
test does not depend on the live archive's shape and never modifies it.

Offline and dependency-free: the Cloud sandbox has no PyPI access.

  python3 scripts/test_builders.py
Exit: 0 = all passed, 1 = a test failed.
"""
import csv
import importlib
import json
import os
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _joinlib as J  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ---------------------------------------------------------------- fixtures

TIER_A_HEADER = ("symbol,stylists,n_stylists,origins,screen_close_resolved,"
                 "chg_pct_resolved,today_close,today_change,today_volume,"
                 "sector,data_date,source\n")

EOD_HEADER = ("date,ticker,name,open,high,low,close,volume,change_pct,"
              "market_cap,sector,currency,exchange,rel_volume,gap_pct,"
              "avg_daily_dollar_volume,data_quality\n")


def write_csv(path, header, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(header)
        for row in rows:
            fh.write(row)


def mini_repo(root):
    """A small but realistic tree: two screen sessions, an EOD file, a brief.

    The two sessions are CONSECUTIVE BOARD DATES with a weekend between them,
    which is what makes the streak rule testable.
    """
    screens = os.path.join(root, "daily-screens")

    # Session 1 (Thursday) and session 2 (Monday). Three calendar days apart,
    # one session apart.
    write_csv(
        os.path.join(screens, "2026-11-05", "tier-a.csv"),
        TIER_A_HEADER,
        [
            "ACME,peoplewish|qullamaggie,2,A|B,10.00,5.0,10.50,5.00,1000,"
            "Technology Services,2026-11-04,mcp+tv\n",
            "BETA,jeff_sun|stockbee,2,C|D,20.00,1.0,20.10,0.50,2000,"
            "Electronic Technology,2026-11-04,mcp+tv\n",
        ])
    write_csv(
        os.path.join(screens, "2026-11-05", "focus.csv"),
        TIER_A_HEADER,
        [
            "ACME,peoplewish|qullamaggie,2,A|B,10.00,5.0,10.50,5.00,1000,"
            "Technology Services,2026-11-04,mcp+tv\n",
            "BETA,jeff_sun|stockbee,2,C|D,20.00,1.0,20.10,0.50,2000,"
            "Electronic Technology,2026-11-04,mcp+tv\n",
            "GAMMA,stockbee,1,E,30.00,2.0,30.10,0.33,3000,"
            "Health Technology,2026-11-04,mcp+tv\n",
        ])

    write_csv(
        os.path.join(screens, "2026-11-06", "tier-a.csv"),
        TIER_A_HEADER,
        [
            # The SAME combination as session 1, spelled in the other order.
            "ACME,qullamaggie|peoplewish,2,B|A,10.50,1.0,11.20,6.67,1500,"
            "Technology Services,2026-11-05,mcp+tv\n",
            # A name that was on session 1 and is gone.
            "OMEGA,stockbee,1,E,40.00,1.0,40.10,0.25,500,"
            "Health Technology,2026-11-05,mcp+tv\n",
        ])
    write_csv(
        os.path.join(screens, "2026-11-06", "focus.csv"),
        TIER_A_HEADER,
        [
            "ACME,qullamaggie|peoplewish,2,B|A,10.50,1.0,11.20,6.67,1500,"
            "Technology Services,2026-11-05,mcp+tv\n",
            "OMEGA,stockbee,1,E,40.00,1.0,40.10,0.25,500,"
            "Health Technology,2026-11-05,mcp+tv\n",
        ])

    # The Stalk board - the skill's SETUP tier, which the tier-a list is not.
    write_csv(
        os.path.join(screens, "2026-11-05", "stalk.csv"),
        TIER_A_HEADER,
        [
            "ACME,peoplewish|qullamaggie,2,A|B,10.00,5.0,10.50,5.00,1000,"
            "Technology Services,2026-11-04,mcp+tv\n",
        ])
    write_csv(
        os.path.join(screens, "2026-11-06", "stalk.csv"),
        TIER_A_HEADER,
        [
            "ACME,qullamaggie|peoplewish,2,B|A,10.50,1.0,11.20,6.67,1500,"
            "Technology Services,2026-11-05,mcp+tv\n",
        ])

    # The settled session after the second screen - the journal's entry session.
    write_csv(
        os.path.join(root, "us-eod", "2026-11-06.csv"),
        EOD_HEADER,
        [
            "2026-11-06,ACME,Acme Corp,10.60,11.40,10.50,11.20,1500,6.667,"
            "1000000,Technology Services,USD,NASDAQ,1.5,1.0,5000000,OK\n",
            "2026-11-06,BETA,Beta Inc,20.20,20.30,19.00,19.20,2000,-4.50,"
            "1000000,Electronic Technology,USD,NASDAQ,1.0,-1.0,5000000,OK\n",
        ])

    # The PRIOR session. The morning file's `Close` column must match this
    # file's closes for the join to be verifiable - that is how the session is
    # resolved, and `Ref asof` is NOT consulted.
    write_csv(
        os.path.join(root, "us-eod", "2026-11-05.csv"),
        EOD_HEADER,
        [
            "2026-11-05,ACME,Acme Corp,10.00,10.60,9.90,10.50,1000,5.00,"
            "1000000,Technology Services,USD,NASDAQ,1.0,0.5,5000000,OK\n",
            "2026-11-05,BETA,Beta Inc,20.00,20.20,19.90,20.10,2000,0.50,"
            "1000000,Electronic Technology,USD,NASDAQ,1.0,-0.5,5000000,OK\n",
        ])

    # A reactions file whose `Close` column matches the 2026-11-05 closes and
    # whose `Ref asof` names an EARLIER session - the two-session-early trap.
    reactions = os.path.join(root, "earnings", "2026-11-06-reactions.md")
    os.makedirs(os.path.dirname(reactions), exist_ok=True)
    with open(reactions, "w", encoding="utf-8") as fh:
        fh.write(
            "# Earnings reaction scanner - 2026-11-06\n\n"
            "## US - Headline table\n\n"
            "| Ticker | Venue | Close | Chg % | Pre-mkt % | Ref close | Ref asof | Tag | "
            "Last earnings | Catalyst |\n"
            "|---|---|---|---|---|---|---|---|---|---|\n"
            "| ACME | NASDAQ | 10.50 | 5.00 | 8.00 | 9.50 | 2026-11-04 | PRE_GAP | "
            "2026-11-01 (5d ago) | Q3 beat, guidance raised |\n"
            "| BETA | NYSE | 20.10 | 0.50 | 3.00 | 19.50 | 2026-11-04 | PRE_GAP | "
            "2026-11-01 (5d ago) | no catalyst lookup (outside the per-run budget) |\n"
            "| ZETA | NYSE | 5.00 | 1.00 | 9.00 | 4.60 | 2026-11-04 | PRE_GAP | "
            "2026-11-01 (5d ago) | no catalyst lookup (outside the per-run budget) |\n")
    return root


def run_builder(module_name, root, extra_argv=()):
    """Run a builder with the shared reader's REPO pointed at the temp tree.

    The builders do not keep their own REPO. They read `J.REPO` at call time,
    and every builder imports the same `_joinlib` module, so patching that one
    object redirects all of them.
    """
    mod = importlib.import_module(module_name)
    original = J.REPO
    J.REPO = root
    try:
        return mod.main([module_name] + list(extra_argv))
    finally:
        J.REPO = original


class BuilderCase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="builders-test-")
        self.root = mini_repo(self.tmp)

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)


class Persistence(BuilderCase):
    def test_streak_counts_board_dates_not_calendar_days(self):
        """ACME is on two boards three CALENDAR days apart.

        A streak must survive the weekend: the gap is one session, not three
        days. The rule is consecutive BOARD DATES.
        """
        run_builder("build_persistence", self.root)
        path = os.path.join(self.root, "derived", "persistence.json")
        self.assertTrue(os.path.exists(path), "persistence.json was not written")
        data = json.load(open(path, encoding="utf-8"))
        acme = data["names"]["ACME"]
        self.assertEqual(acme["tier-a"]["days"], 2)
        self.assertEqual(acme["tier-a"]["streak_current"], 2,
                         "a weekend between two boards must not break a streak")
        self.assertEqual(acme["tier-a"]["streak_longest"], 2)

    def test_departure_is_reported_with_its_exit_streak(self):
        run_builder("build_persistence", self.root)
        data = json.load(open(os.path.join(self.root, "derived", "persistence.json"),
                              encoding="utf-8"))
        # BETA was on the 11-05 board and is gone from the 11-06 board.
        gone = [d for d in data["departures"] if d["ticker"] == "BETA"]
        self.assertTrue(gone, "a name that left the board was not reported")
        self.assertEqual(gone[0]["streak_at_exit"], 1)

    def test_stylist_combination_is_order_independent(self):
        """THE bug: the journal grouped by the raw spelling.

        `peoplewish|qullamaggie` and `qullamaggie|peoplewish` are the same
        combination and must produce one group, not two.
        """
        run_builder("build_setups", self.root)
        path = os.path.join(self.root, "derived", "setup-journal.csv")
        self.assertTrue(os.path.exists(path), "setup-journal.csv was not written")
        rows = list(csv.DictReader(open(path, encoding="utf-8")))
        combos = set()
        for r in rows:
            if r["stylists"]:
                combos.add(r["stylists"])
        self.assertIn("peoplewish|qullamaggie", combos)
        self.assertNotIn("qullamaggie|peoplewish", combos,
                         "the combination was not canonicalised")

    def test_sub_screen_label_folds_into_its_parent(self):
        """`bonde_4pct` is a stockbee sub-screen, not a sixth stylist."""
        build_setups = importlib.import_module("build_setups")
        combo, _unknown = build_setups.canonical_combination(
            ["bonde_4pct", "qullamaggie"])
        self.assertEqual(combo, ("qullamaggie", "stockbee"))

    def test_a_count_is_not_a_stylist_name(self):
        """On 2026-11-02 the `stylists` column holds the COUNT.

        Treating `3` as a name would group every name that hit three
        stylists together.
        """
        build_setups = importlib.import_module("build_setups")
        combo, _unknown = build_setups.canonical_combination(["3"])
        self.assertIsNone(combo)

    def test_unmapped_tokens_are_reported_not_guessed(self):
        build_setups = importlib.import_module("build_setups")
        combo, unknown = build_setups.canonical_combination(["zzzz"])
        self.assertIsNone(combo)
        self.assertEqual(unknown, ["zzzz"])

    def test_a_comma_separated_prose_list_keeps_every_stylist(self):
        """THE bug, found while writing these tests.

        On 2026-10-29 the combination lives in `origins` as a prose list -
        `"RS leader, ADR + velocity, CANSLIM"`. Splitting only on `;` and `|`
        left the whole string as ONE token, and the first marker it matched won,
        so a name that hit three stylists was recorded as hitting one.
        """
        build_setups = importlib.import_module("build_setups")
        row = {"origins": "RS leader, ADR + velocity, CANSLIM"}
        tokens = build_setups.stylist_tokens(row)
        self.assertEqual(len(tokens), 3,
                         "the prose list was not split: %r" % tokens)
        combo, _unknown = build_setups.canonical_combination(tokens)
        self.assertEqual(combo, ("jeff_sun", "peoplewish", "qullamaggie"))

    def test_a_single_token_may_carry_more_than_one_stylist(self):
        """Even unsplit, one token must contribute every bucket it names."""
        build_setups = importlib.import_module("build_setups")
        combo, _unknown = build_setups.canonical_combination(
            ["RS leader, ADR + velocity, CANSLIM"])
        self.assertEqual(combo, ("jeff_sun", "peoplewish", "qullamaggie"))


class GapReconciliation(BuilderCase):
    def test_session_resolved_by_close_column_not_ref_asof(self):
        """THE bug: the join was dated by `Ref asof`.

        `Ref asof` is the base of the `Chg %` column - NOT of the pre-market
        column. Using it dated the join two sessions early and turned held
        gaps into false reversals.
        """
        run_builder("build_gap_reconciliation", self.root)
        path = os.path.join(self.root, "derived", "2026-11-06", "gap-reconciliation.csv")
        self.assertTrue(os.path.exists(path), "gap-reconciliation.csv was not written")
        rows = list(csv.DictReader(open(path, encoding="utf-8")))
        acme = next(r for r in rows if r["ticker"] == "ACME")
        # The pre-market gap was +8% and the session closed +6.67%. Same sign,
        # and 6.67 is at least half of 8 - so the gap HELD. It did not reverse.
        self.assertEqual(acme["outcome"], "held",
                         "a held gap was labelled %r" % acme["outcome"])
        self.assertEqual(acme["settled_change_pct"], "6.667")

    def test_the_session_base_is_verified_against_the_close_column(self):
        """The morning file's `Close` column matches the prior session's closes.

        That match is how the session is resolved, and it is what makes the
        labels trustworthy. A base that matches nothing must be said to be
        unverified rather than used quietly.
        """
        run_builder("build_gap_reconciliation", self.root)
        md = open(os.path.join(self.root, "derived", "2026-11-06",
                               "gap-reconciliation.md"), encoding="utf-8").read()
        self.assertIn("Session resolution is verified", md,
                      "the base was not verified:\n%s" % md[:2000])
        self.assertNotIn("unverified", md.lower(),
                         "a matching base was reported as unverified")

    def test_unverified_base_is_said_so(self):
        """A base that matches no settled session must be marked unverified."""
        # The prior session is what the morning `Close` column is matched against.
        # Replacing only the fire-date file leaves that match intact, so the
        # base stays verified. Both files have to disagree.
        for name in ("2026-11-05.csv", "2026-11-06.csv"):
            write_csv(
                os.path.join(self.root, "us-eod", name),
                EOD_HEADER,
                ["2026-11-06,ZZZ,Zed,1,1,1,1,1,0,1,Tech,USD,NASDAQ,1,0,1,OK\n"])
        run_builder("build_gap_reconciliation", self.root)
        md = open(os.path.join(self.root, "derived", "2026-11-06",
                               "gap-reconciliation.md"), encoding="utf-8").read()
        self.assertIn("unverified", md.lower())

    def test_no_settled_row_is_no_close_not_dropped(self):
        """ZETA has no settled row. It must be labelled, not silently absent."""
        run_builder("build_gap_reconciliation", self.root)
        rows = list(csv.DictReader(open(os.path.join(
            self.root, "derived", "2026-11-06", "gap-reconciliation.csv"),
            encoding="utf-8")))
        tickers = [r["ticker"] for r in rows]
        self.assertIn("ZETA", tickers, "a name with no settled row was dropped")
        zeta = next(r for r in rows if r["ticker"] == "ZETA")
        self.assertEqual(zeta["outcome"], "no_close")


class ThesisScore(BuilderCase):
    def _brief(self, name, body):
        path = os.path.join(self.root, "daily-briefs", name)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(body)

    def test_source_health_partial_is_not_a_thesis_verdict(self):
        """`PARTIAL` in a source-health table means the SOURCE was partial.

        Scoring it as a thesis verdict would invent partial holds.
        """
        self._brief("2026-11-06-pre-market.md",
                    "# Brief\n\n"
                    "## Source health\n\n"
                    "| Source | Status |\n|---|---|\n"
                    "| Yahoo chart API | PARTIAL |\n"
                    "| Some tool | OK |\n")
        run_builder("build_thesis_score", self.root)
        path = os.path.join(self.root, "derived", "thesis-score.csv")
        self.assertTrue(os.path.exists(path), "thesis-score.csv was not written")
        rows = list(csv.DictReader(open(path, encoding="utf-8")))
        self.assertEqual([r for r in rows if r["verdict"] == "PARTIAL"], [],
                         "a source-health PARTIAL was scored as a thesis verdict")

    def test_thesis_verdicts_are_extracted(self):
        self._brief("2026-11-06-pre-market.md",
                    "# Brief\n\n"
                    "## Yesterday's brief - what happened\n\n"
                    "| Name | Setup (yesterday) | Yesterday's close | Today's move | "
                    "Thesis held? |\n|---|---|---|---|---|\n"
                    "| ACME | a setup | 10.50 | +6.67% | HELD (the level held) |\n"
                    "| BETA | a setup | 20.10 | -4.50% | BROKE (traded through) |\n")
        run_builder("build_thesis_score", self.root)
        rows = list(csv.DictReader(open(os.path.join(
            self.root, "derived", "thesis-score.csv"), encoding="utf-8")))
        verdicts = {r["ticker"]: r["verdict"] for r in rows}
        self.assertEqual(verdicts.get("ACME"), "HELD")
        self.assertEqual(verdicts.get("BETA"), "BROKE")

    def test_briefs_with_no_score_are_counted_as_unscored(self):
        self._brief("2026-11-05-pre-market.md", "# Brief\n\nNo verdict table here.\n")
        run_builder("build_thesis_score", self.root)
        md = open(os.path.join(self.root, "derived", "thesis-score.md"),
                  encoding="utf-8").read()
        self.assertIn("published no thesis score", md)


class Confirmation(BuilderCase):
    def test_a_name_in_three_families_counts_three(self):
        """The whole point of the view: agreement is measurable."""
        for name, body in (
            ("ntrt/2026-11-06.md",
             "# Brief\n\n| Ticker | Gap |\n|---|---|\n| ACME | +8.0% |\n"),
            ("options-flow/2026-11-06.md",
             "# Flow\n\n| Ticker | Side |\n|---|---|\n| ACME | C |\n"),
            ("earnings/2026-11-06-reactions.md",
             "# Reactions\n\n| Ticker | Venue | Pre-mkt % | Tag |\n|---|---|---|---|\n"
             "| ACME | NASDAQ | +8.0 | PRE_GAP |\n"),
        ):
            path = os.path.join(self.root, name)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(body)
        run_builder("build_confirmation", self.root)
        rows = list(csv.DictReader(open(os.path.join(
            self.root, "derived", "2026-11-06", "confirmation.csv"), encoding="utf-8")))
        acme = next((r for r in rows if r["ticker"] == "ACME"), None)
        self.assertIsNotNone(acme, "ACME was not found")
        self.assertGreaterEqual(int(acme["n_families"]), 3)


class RunLedger(BuilderCase):
    def test_a_routine_before_its_onset_is_not_a_miss(self):
        """The fleet was still starting up on the first sessions.

        A day before a routine had published anything here is not a miss.
        """
        run_builder("build_run_ledger", self.root)
        rows = list(csv.DictReader(open(os.path.join(
            self.root, "derived", "run-ledger.csv"), encoding="utf-8")))
        states = {r["state"] for r in rows}
        self.assertIn("before_onset", states,
                      "a pre-onset day was classified as a miss")

    def test_calendar_boundaries_are_distinguished(self):
        run_builder("build_run_ledger", self.root)
        rows = list(csv.DictReader(open(os.path.join(
            self.root, "derived", "run-ledger.csv"), encoding="utf-8")))
        for r in rows:
            self.assertIn(r["state"], (
                "published", "published_off_schedule", "published_before_calendar",
                "published_after_calendar", "missing", "before_onset"),
                "unknown state %r" % r["state"])


class Idempotence(BuilderCase):
    def test_running_twice_produces_no_diff(self):
        """The property the post-merge hook depends on.

        A rebuild that changed nothing must write nothing, or the hook
        produces a diff on every merge.
        """
        for module in ("build_persistence", "build_setups", "build_confirmation",
                       "build_thesis_score", "build_run_ledger",
                       "build_gap_reconciliation"):
            run_builder(module, self.root)
        first = snapshot(self.root)
        for module in ("build_persistence", "build_setups", "build_confirmation",
                       "build_thesis_score", "build_run_ledger",
                       "build_gap_reconciliation"):
            run_builder(module, self.root)
        second = snapshot(self.root)
        self.assertEqual(first, second, "a rebuild changed the output")


def snapshot(root):
    """Every file under derived/, by path and content."""
    out = {}
    base = os.path.join(root, "derived")
    for dirpath, _dirs, files in os.walk(base):
        for f in files:
            p = os.path.join(dirpath, f)
            out[os.path.relpath(p, base)] = open(p, encoding="utf-8").read()
    return out


if __name__ == "__main__":
    unittest.main(verbosity=2)
