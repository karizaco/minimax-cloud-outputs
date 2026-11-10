#!/usr/bin/env python3
"""test_render.py — regression tests for the client-safe renderer.

Why: the renderer turns an artifact written for GitHub into something a chat
client can show. Its failure mode is SILENT DATA LOSS. The renderer used to
drop any table row whose cell count did not match its header, and a naive pipe
split meant a cell holding `\\|corr\\|` made the header two cells longer than
the row - so the rows vanished without a word.

That shipped. `derived/client-safe/cross-asset/2026-11-06.md` published
`**Pair**: uncorrelated SPY–IWM · **Level corr**: +0.00` for a source row that
reads `| \U0001F7E5 **GLD–UUP** | -0.79 | ...`.

The property this file pins: **every data row in a table produces a bullet.**
Not "most of them". All of them.

Offline and dependency-free: the Cloud sandbox has no PyPI access.

  python3 scripts/test_render.py
Exit: 0 = all passed, 1 = a test failed.
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _joinlib as J  # noqa: E402
from render_client_safe import render, table_to_bullets, glyph_to_words  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def table_rows(text):
    """The data rows of the first table in a document."""
    tables = J.md_tables(text)
    if not tables:
        return [], []
    _s, header, rows = tables[0]
    return header, rows


class GlyphToWords(unittest.TestCase):
    def test_a_flag_glyph_becomes_its_word(self):
        self.assertEqual(glyph_to_words("\U0001F7E5"), "strong")
        self.assertEqual(glyph_to_words("+0.92 \U0001F7E5", paren=True), "+0.92 (strong)")

    def test_a_decorative_emoji_is_deleted(self):
        self.assertEqual(glyph_to_words("\U0001F9ED snapshot"), " snapshot")

    def test_a_variation_selector_does_not_survive(self):
        out = glyph_to_words("⚠️ warning")
        self.assertNotIn("️", out)


class TableToBullets(unittest.TestCase):
    def test_escaped_pipe_row_is_not_dropped(self):
        """THE bug: the row's cell count did not match the header, so it went."""
        rows = [
            "| | Pair | Corr | \\|corr\\| | Band |",
            "|---|---|---|---|---|",
            "| \U0001F7E5 | **GLD–UUP** | -0.79 | `███` | strong |",
            "| \U0001F7E6 | **IWM–GLD** | +0.07 | `█` | uncorrelated |",
        ]
        bullets = table_to_bullets(rows)
        self.assertEqual(len(bullets), 2,
                         "a row was dropped: %r" % (bullets,))

    def test_every_source_row_produces_a_bullet(self):
        """The property that would have caught the dropped rows."""
        text = (
            "| Ticker | Close | Change | Gap | Band |\n"
            "|---|---|---|---|---|\n"
            "| AAA | 1.00 | +2.00 | +1.00 | strong |\n"
            "| BBB | 2.00 | -3.00 | -1.00 | mild |\n"
            "| CCC | 3.00 | +4.00 | +2.00 | moderate |\n")
        _header, rows = table_rows(text)
        bullets = table_to_bullets(text.splitlines())
        self.assertEqual(len(bullets), len(rows),
                         "source rows %d, bullets %d" % (len(rows), len(bullets)))

    def test_a_mismatched_row_is_rendered_and_flagged(self):
        """A row that does not line up is rendered as far as it goes.

        It must never vanish without a word.
        """
        rows = [
            "| A | B |",
            "|---|---|",
            "| 1 | 2 | 3 |",
        ]
        bullets = table_to_bullets(rows)
        self.assertEqual(len(bullets), 1, "a mismatched row was dropped")
        self.assertIn("cell", bullets[0])

    def test_a_named_table_renders_col_value_pairs(self):
        rows = [
            "| Ticker | Close | Change |",
            "|---|---|---|",
            "| AAA | 1.00 | +2.00 |",
        ]
        bullets = table_to_bullets(rows)
        self.assertEqual(len(bullets), 1)
        self.assertIn("**Ticker**: AAA", bullets[0])
        self.assertIn("**Change**: +2.00", bullets[0])

    def test_a_row_label_table_leads_with_the_row_name(self):
        """A correlation matrix: the first cell names the row."""
        rows = [
            "| | SPY | QQQ |",
            "|---|---|---|",
            "| **SPY** | +1.00 | +0.92 |",
        ]
        bullets = table_to_bullets(rows)
        self.assertEqual(len(bullets), 1)
        self.assertTrue(bullets[0].startswith("**SPY**"),
                        "the row label did not lead: %r" % bullets[0])

    def test_a_paired_table_pairs_each_label_with_its_value(self):
        """The cross-asset legend: two label/value pairs side by side."""
        rows = [
            "| | Meaning | | Meaning |",
            "|---|---|---|---|",
            "| \U0001F7E5 | 0.70 or more - strong | \U0001F7E6 | under 0.20 - uncorrelated |",
        ]
        bullets = table_to_bullets(rows)
        self.assertEqual(len(bullets), 1)
        self.assertIn("strong", bullets[0])
        self.assertIn("uncorrelated", bullets[0])


class Render(unittest.TestCase):
    def test_a_heading_becomes_a_bold_label(self):
        out = render("# Title\n\nbody\n")
        self.assertIn("**Title**", out)
        self.assertNotIn("# Title", out)

    def test_a_glyph_becomes_a_word_in_the_output(self):
        out = render("| A | B |\n|---|---|\n| \U0001F7E5 | strong |\n")
        self.assertNotIn("\U0001F7E5", out)
        self.assertIn("strong", out)

    def test_a_decorative_emoji_is_removed_from_a_heading(self):
        out = render("## \U0001F9ED Cross-asset\n\nbody\n")
        self.assertNotIn("\U0001F9ED", out)
        self.assertIn("Cross-asset", out)

    def test_a_long_paragraph_becomes_bullets(self):
        body = ("First clause here that is quite long indeed and carries a fact. "
                "Second clause follows along with more detail. "
                "Third clause adds a further point about the same matter. "
                "Fourth clause closes the thought out properly.")
        out = render(body + "\n")
        self.assertIn("- ", out)

    def test_a_blockquote_becomes_a_bullet(self):
        out = render("> a quoted line\n")
        self.assertIn("- a quoted line", out)

    def test_front_matter_is_reduced_to_the_meaningful_keys(self):
        out = render("---\ndate: 2026-11-06\ncron: x\nsession: 99\nstatus: ok\n---\n\nbody\n")
        self.assertIn("date: 2026-11-06", out)
        self.assertNotIn("session: 99", out)


class RealArtifact(unittest.TestCase):
    """The shipped artifacts, against the real corpus."""

    def test_the_cross_asset_twin_keeps_its_pair_names(self):
        """The exact row that was corrupted.

        Source: `| \U0001F7E5 **GLD–UUP** | -0.79 | ...`. The twin published
        `**Pair**: uncorrelated SPY–IWM · **Level corr**: +0.00` for it.
        """
        path = os.path.join(REPO, "cross-asset", "2026-11-06.md")
        if not os.path.exists(path):
            self.skipTest("cross-asset artifact not present")
        out = render(open(path, encoding="utf-8").read())
        self.assertIn("GLD–UUP", out, "the pair name was lost in rendering")
        self.assertIn("-0.79", out, "the pair's value was lost in rendering")

    def test_every_table_row_in_the_corpus_survives(self):
        """No row is dropped, anywhere in the published narrative artifacts."""
        import glob
        patterns = ("daily-screens/*/daily-sweep.md", "daily-briefs/*.md",
                    "us-stocks-in-play/*.md", "weekly/*.md", "earnings/*.md",
                    "ntrt/*.md", "cross-asset/*.md", "options-flow/*.md")
        checked = 0
        for pat in patterns:
            for path in glob.glob(os.path.join(REPO, pat)):
                text = open(path, encoding="utf-8").read()
                lines = text.splitlines()
                for start, _header, rows in J.md_tables(text):
                    if not rows:
                        continue
                    # The table's own lines, from its start line. Scanning the
                    # whole document for pipe-rows would pick up a DIFFERENT
                    # table's rows and compare against the wrong header.
                    raw = []
                    j = start
                    while j < len(lines) and lines[j].startswith("|"):
                        raw.append(lines[j])
                        j += 1
                    if len(raw) < 2:
                        continue
                    bullets = table_to_bullets(raw)
                    data_rows = len(raw) - 2
                    if data_rows <= 0:
                        continue
                    checked += 1
                    self.assertGreaterEqual(
                        len(bullets), data_rows,
                        "%s: %d data rows produced %d bullets"
                        % (os.path.relpath(path, REPO), data_rows, len(bullets)))
        self.assertGreater(checked, 0, "no table was checked - the test is vacuous")


if __name__ == "__main__":
    unittest.main(verbosity=2)
