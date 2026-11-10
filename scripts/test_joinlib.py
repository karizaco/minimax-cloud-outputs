#!/usr/bin/env python3
"""test_joinlib.py — regression tests for the shared column-drift reader.

Why this file exists: `_joinlib.py` is what every derived-view builder stands
on. Its whole job is to survive schema drift that no single fixture can
predict - the ticker column has been `symbol`, `ticker` and `name`; the session
change has had five names; sectors arrive in two vocabularies; the sector
column is missing entirely on three dates.

The failure mode is SILENT. A builder that reads the wrong column produces a
plausible-looking artifact with the wrong numbers in it, and nothing in the
repo says so. Two such failures shipped before this file existed:

  - a markdown row split on a naive `|`, so a cell holding `\\|corr\\|` became
    three cells, the row stopped matching its header, and the renderer DROPPED
    the row without a word;
  - a `name` column of company names read as a column of tickers.

Offline and dependency-free: the Cloud sandbox has no PyPI access.

  python3 scripts/test_joinlib.py
Exit: 0 = all passed, 1 = a test failed.
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _joinlib as J  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class SplitRow(unittest.TestCase):
    """A markdown row splits on UNESCAPED pipes only."""

    def test_plain_row(self):
        self.assertEqual(J.split_row("a|b|c"), ["a", "b", "c"])

    def test_escaped_pipe_is_one_cell(self):
        # THE bug. `\|corr\|` is one cell the author wrote, not three.
        self.assertEqual(J.split_row(r"a|\|corr\||b"), ["a", "|corr|", "b"])

    def test_escaped_pipe_at_both_ends(self):
        self.assertEqual(J.split_row(r"\|chg\| >= 3%"), ["|chg| >= 3%"])

    def test_backslash_not_before_pipe_is_kept(self):
        # A lone backslash is data, not an escape.
        self.assertEqual(J.split_row(r"a\nb|c"), ["a\\nb", "c"])

    def test_empty_cells_preserved(self):
        self.assertEqual(J.split_row("a||c"), ["a", "", "c"])


class MdTables(unittest.TestCase):
    def test_escaped_pipe_header_and_row_line_up(self):
        """The header and its data row must produce the SAME cell count.

        This is the property whose violation silently dropped rows: the header
        grew by two cells (one escaped pipe, two of them) and the row did not,
        so the length check failed and the row was skipped.
        """
        text = (
            "| | Pair | Corr | \\|corr\\| | Band |\n"
            "|---|---|---|---|---|\n"
            "| \U0001F7E5 | **SPY-QQQ** | +0.92 | `███████░` | strong |\n"
        )
        tables = J.md_tables(text)
        self.assertEqual(len(tables), 1)
        _start, header, rows = tables[0]
        self.assertEqual(len(header), 5)
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["Pair"], "**SPY-QQQ**")
        self.assertEqual(rows[0]["|corr|"], "`███████░`")
        self.assertEqual(rows[0]["Band"], "strong")

    def test_short_row_is_padded(self):
        text = "| a | b |\n|---|---|\n| 1 |\n"
        _s, _h, rows = J.md_tables(text)[0]
        self.assertEqual(rows[0]["a"], "1")
        self.assertEqual(rows[0]["b"], "")

    def test_no_separator_is_not_a_table(self):
        text = "| a | b |\n| 1 | 2 |\n"
        self.assertEqual(J.md_tables(text), [])

    def test_real_artifact_with_escaped_pipe(self):
        """The actual corpus: the cross-asset flat heatmap."""
        path = os.path.join(REPO, "cross-asset", "2026-11-06.md")
        if not os.path.exists(path):
            self.skipTest("cross-asset artifact not present")
        text = open(path, encoding="utf-8").read()
        found = None
        for _s, header, rows in J.md_tables(text):
            if "Pair" in header and "Level corr" in header:
                found = (header, rows)
                break
        self.assertIsNotNone(found, "the flat-heatmap table was not found")
        header, rows = found
        self.assertEqual(len(header), 4)
        # Two pairs per row, so 28 pairs are 14 rows. The bug turned the
        # escaped-pipe header into more cells than the data rows had.
        self.assertEqual(len(rows), 14, "every pair-row should be parsed")
        self.assertIn("GLD", rows[0]["Pair"])


class TickerColumn(unittest.TestCase):
    def test_symbol_column(self):
        rows = [{"symbol": "AAPL"}, {"symbol": "MSFT"}]
        col, _note = J.ticker_column(rows)
        self.assertEqual(col, "symbol")

    def test_ticker_column(self):
        rows = [{"ticker": "AAPL"}]
        col, _note = J.ticker_column(rows)
        self.assertEqual(col, "ticker")

    def test_name_column_of_tickers(self):
        rows = [{"name": "AAPL"}, {"name": "MSFT"}]
        col, note = J.ticker_column(rows)
        self.assertEqual(col, "name")
        self.assertIn("tickers", note)

    def test_name_column_of_company_names_is_rejected(self):
        """2026-10-23 puts COMPANY NAMES in a column called `name`.

        Reading that as a ticker column makes every lookup fail silently.
        """
        rows = [{"name": "Apple Inc"}, {"name": "Microsoft Corp"}]
        col, _note = J.ticker_column(rows)
        self.assertIsNone(col, "a company-name column was read as a ticker column")

    def test_one_bad_value_does_not_discard_the_board(self):
        """2026-10-26 has one preferred-share line, `HPE/PC`.

        A strict all-or-nothing test discarded a whole 200-row board over it.
        """
        rows = [{"name": "AAA%d" % i} for i in range(20)]
        rows.append({"name": "HPE/PC"})
        col, note = J.ticker_column(rows)
        self.assertEqual(col, "name")
        self.assertIn("1 value(s) not ticker-shaped", note)

    def test_mostly_company_names_is_rejected(self):
        """The risk the majority rule introduces.

        Short company names can all look ticker-shaped. If enough of them do,
        the column must still not be read as tickers.
        """
        rows = [{"name": "ABCD"} for _ in range(95)]
        rows += [{"name": "Apple Inc"} for _ in range(5)]
        col, _note = J.ticker_column(rows)
        self.assertIsNone(col,
                          "a mostly-company-name column was read as a ticker column")


class LeadFloat(unittest.TestCase):
    def test_leading_number_with_a_glyph(self):
        self.assertAlmostEqual(J.lead_float("+0.92 \U0001F7E5"), 0.92)

    def test_negative(self):
        self.assertAlmostEqual(J.lead_float("-0.31"), -0.31)

    def test_no_number(self):
        self.assertIsNone(J.lead_float("n/a"))
        self.assertIsNone(J.lead_float("—"))
        self.assertIsNone(J.lead_float(""))

    def test_thousands_separator(self):
        self.assertAlmostEqual(J.lead_float("1,234.50"), 1234.50)


class ToFloat(unittest.TestCase):
    def test_currency_and_percent(self):
        self.assertAlmostEqual(J.to_float("$1.34"), 1.34)
        self.assertAlmostEqual(J.to_float("-10.8%"), -10.8)

    def test_plain(self):
        self.assertAlmostEqual(J.to_float("1,234.50"), 1234.50)

    def test_non_numeric_is_none(self):
        self.assertIsNone(J.to_float("n/a"))
        self.assertIsNone(J.to_float("—"))
        self.assertIsNone(J.to_float(""))

    def test_scaled_suffix_is_not_a_number(self):
        """`1.2B` is a magnitude, not a value.

        Reading it as 1.2 would silently understate a market cap by a factor
        of a billion, so a suffix must NOT parse.
        """
        self.assertIsNone(J.to_float("1.2B"))
        self.assertIsNone(J.to_float("50M"))


class SectorTaxonomy(unittest.TestCase):
    def test_factset_vocabulary(self):
        values = {"Electronic Technology", "Technology Services", "Health Technology"}
        self.assertEqual(J.sector_taxonomy(values), "factset-like")

    def test_gics_vocabulary(self):
        values = {"Information Technology", "Health Care", "Financials"}
        self.assertEqual(J.sector_taxonomy(values), "gics")

    def test_shared_terms_do_not_decide(self):
        """`Utilities` and `Energy` are in BOTH vocabularies.

        Keying on a shared term labelled every FactSet board `gics`, because
        almost every board carries a utility.
        """
        values = {"Utilities", "Energy", "Industrials"}
        self.assertNotEqual(J.sector_taxonomy(values), "gics")
        self.assertNotEqual(J.sector_taxonomy(values), "factset-like")

    def test_empty(self):
        self.assertIsNone(J.sector_taxonomy(set()))
        self.assertIsNone(J.sector_taxonomy({""}))


class ChangeColumn(unittest.TestCase):
    def test_today_change_wins(self):
        rows = [{"today_change": "1.1", "chg_pct_2026-11-06": "2.2"}]
        col, rule = J.change_column(rows, "2026-11-06")
        self.assertEqual(col, "today_change")
        self.assertEqual(rule, "current schema")

    def test_date_stamped_column(self):
        rows = [{"chg_pct_2026-11-06": "2.2", "chg_pct_2026-10-30": "1.1"}]
        col, rule = J.change_column(rows, "2026-11-06")
        self.assertEqual(col, "chg_pct_2026-11-06")
        self.assertIn("stamped", rule)

    def test_early_schema_fallback(self):
        rows = [{"change_pct": "2.2"}]
        col, rule = J.change_column(rows, "2026-11-06")
        self.assertEqual(col, "change_pct")
        self.assertEqual(rule, "early schema")

    def test_nothing_recognisable(self):
        rows = [{"close": "1.0"}]
        col, _rule = J.change_column(rows, "2026-11-06")
        self.assertIsNone(col)


class StripMd(unittest.TestCase):
    def test_bold_and_code(self):
        self.assertEqual(J.strip_md("**+1.11**"), "+1.11")
        self.assertEqual(J.strip_md("`foo`"), "foo")

    def test_dashes_are_empty(self):
        for cell in ("—", "–", "-", "n/a", "N/A", "None", ""):
            self.assertEqual(J.strip_md(cell), "", "cell %r should read as empty" % cell)


class TickerVariants(unittest.TestCase):
    def test_dash_and_dot_forms(self):
        variants = J.ticker_variants("BRK.B")
        self.assertIn("BRK.B", variants)
        self.assertIn("BRK-B", variants)

    def test_dedup(self):
        variants = J.ticker_variants("AAPL")
        self.assertEqual(len(variants), len(set(variants)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
