#!/usr/bin/env python3
"""Render a routine's artifact so the desktop client can show it.

Why: the Minimax Code desktop client supports a narrow subset of markdown —
bold, italics, and ordered/unordered lists. It does not render coloured text,
and flag glyphs either vanish or arrive as tofu. The routines' artifacts are
written for GitHub, where a wide table and an emoji band are exactly right, so
the artifact itself is not wrong. What is wrong is that the same text is also
delivered to the chat, where those two constructs are unavailable.

This produces the client-safe rendering of an artifact: headings become bold
labels, tables become bullet lists, glyphs become the words they stood for,
and long prose is broken into bullets. Nothing is dropped that can be said in a
list — a row that does not fit becomes its own bullet.

The output is a NEW file. No source artifact is modified, and no routine
behaviour changes.

  python3 scripts/render_client_safe.py <artifact.md>            # print to stdout
  python3 scripts/render_client_safe.py <artifact.md> --out X.md # write a file
  python3 scripts/render_client_safe.py --dir daily-briefs       # a whole family
  python3 scripts/render_client_safe.py --dir daily-briefs --out-dir derived/client-safe
"""
import argparse
import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _joinlib as J  # noqa: E402
from check_reply_format import (  # noqa: E402
    GLYPH_RE, GLYPH_WORDS, ANY_EMOJI_RE, HEADING_RE, BULLET_RE, ORDERED_RE,
    TABLE_RE, TABLE_SEP_RE, QUOTE_RE, check, tickers_in,
)

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MAX_WORDS_BULLET = 30
MAX_WORDS_SENTENCE = 30


def glyph_to_words(text, paren=False):
    """Replace each flag glyph with the word it stood for.

    The glyphs that carry a MEANING become that word. The decorative ones -
    the compass on a heading, the pin on a section - are deleted, because
    they carry nothing a reader can act on and the client's font may not have
    them at all.

    `paren` wraps the word in brackets when the glyph was not at the start of
    the string, so a table cell reads "+0.92 (strong)" rather than "+0.92 strong".
    """
    def sub(m):
        g = m.group(0)
        word = GLYPH_WORDS.get(g)
        if word is None:
            return ""
        if paren and m.start() > 0:
            # The glyph usually sits after a space ("+0.92 🟥"). Keep one space,
            # not two: returning " (strong)" on top of that space reads "  (strong)".
            if m.string[m.start() - 1].isspace():
                return "(%s)" % word
            return " (%s)" % word
        return word
    text = GLYPH_RE.sub(sub, text)
    return ANY_EMOJI_RE.sub("", text)


def cap_first(text):
    """Capitalise the first letter, so a replaced glyph reads as a word."""
    for i, ch in enumerate(text):
        if ch.isalpha():
            return text[:i] + ch.upper() + text[i + 1:]
    return text


def split_sentences(text):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]


def table_to_bullets(rows):
    """One bullet per data row.

    Two table shapes appear in this repo's artifacts and they need different
    handling, so the shape is read off the header rather than assumed:

    * A NAMED table - every header cell has a name. The bullet is
      "**Col**: v · **Col2**: v2". A table with more than four columns is
      not readable as a bullet, so the leading columns are kept and the count
      dropped is stated rather than the columns being silently discarded.

    * A LABEL-LED table - one or more header cells are EMPTY, marking the
      columns that name the row rather than a value. A correlation matrix has
      one (the row name); the cross-asset legend has two (it is a table of
      two label/value pairs side by side). Each label cell leads its own
      value, so the bullet is "**row**: value · **other row**: value".
    """
    if len(rows) < 2:
        return []
    header = [c.strip().replace("**", "").strip() for c in J.split_row(rows[0].strip().strip("|"))]
    data = rows[2:] if len(rows) > 2 else []
    if not data:
        return []

    label_cols = [i for i, h in enumerate(header) if not h]
    out = []
    for row in data:
        # Split on unescaped pipes only, so a cell carrying `\|corr\|` stays ONE
        # cell. A naive split made the row longer than its header, and the
        # length check below then DROPPED the row without a word.
        cells = [c.strip() for c in J.split_row(row.strip().strip("|"))]
        if len(cells) != len(header):
            # A row that still does not line up is rendered as far as it goes,
            # with the mismatch stated. Dropping it silently is how the
            # corrupted rows shipped.
            mismatch = len(cells) - len(header)
            cells = cells[:len(header)] + [""] * max(0, -mismatch)
            extra = "  (row has %d cell(s) where the header has %d)" % (
                len(cells), len(header))
        else:
            extra = ""

        if len(label_cols) == 1 and label_cols[0] == 0:
            # A ROW-LABEL table - a correlation matrix. The first cell names
            # the row and the named columns after it are the values.
            lead = glyph_to_words(cells[0].replace("**", "").strip())
            named = header[1:]
            values = cells[1:]
            keep = min(4, len(named))
            parts = []
            for h, c in zip(named[:keep], values[:keep]):
                c = glyph_to_words(c.replace("**", "").strip(), paren=True)
                if not c:
                    continue
                parts.append("**%s**: %s" % (h, c))
            if not parts:
                continue
            bullet = " · ".join(parts)
            if lead:
                bullet = "**%s** — %s" % (lead, bullet)
            dropped = len(named) - keep
            if dropped > 0:
                bullet += "  (+%d more column(s) in the artifact table)" % dropped
            out.append(bullet + extra)
            continue

        if label_cols:
            # A PAIRED table - the cross-asset legend is two label/value pairs
            # side by side, so each label cell leads its own value.
            parts = []
            for i in label_cols:
                if i + 1 >= len(cells):
                    continue
                lead = glyph_to_words(cells[i].replace("**", "").strip())
                value = glyph_to_words(cells[i + 1].replace("**", "").strip(), paren=True)
                if not lead and not value:
                    continue
                if not lead:
                    parts.append(value)
                elif not value:
                    parts.append("**%s**" % lead)
                else:
                    parts.append("**%s**: %s" % (lead, value))
            if not parts:
                continue
            out.append(" · ".join(parts) + extra)
            continue

        keep = min(4, len(header))
        parts = []
        for h, c in zip(header[:keep], cells[:keep]):
            c = glyph_to_words(c.replace("**", "").strip(), paren=True)
            if not c:
                continue
            parts.append("**%s**: %s" % (h, c))
        if not parts:
            continue
        bullet = " · ".join(parts)
        dropped = len(header) - keep
        if dropped > 0:
            bullet += "  (+%d more column(s) in the artifact table)" % dropped
        out.append(bullet + extra)
    return out


def split_long_bullet(text):
    """A bullet over the cap becomes several, split at its ' · ' separators.

    A table row carries one field per column, and joining them makes a bullet
    the client will wrap into an unreadable block. Splitting at the separator
    keeps each field with its own label.
    """
    if len(text.split()) <= MAX_WORDS_BULLET:
        return [text]
    parts = text.split(" · ")
    out, current = [], []
    for p in parts:
        trial = " · ".join(current + [p])
        if len(trial.split()) > MAX_WORDS_BULLET and current:
            out.append(" · ".join(current))
            current = [p]
        else:
            current.append(p)
    if current:
        out.append(" · ".join(current))
    return out


CLAUSE_RE = re.compile(r"(?<=[;:])\s+|\s+([—·])\s+")
COMMA_RE = re.compile(r"(?<![\w)\]\"'])(,)(?=\s)")


def _split_keep(text, pattern):
    """Split on `pattern`, keeping the punctuation that was consumed.

    The delimiter stays with the clause it closes: splitting "0.46% — a narrow
    tape" at the em-dash and dropping the dash leaves "0.46% a narrow tape",
    which reads as a run-on.
    """
    out = []
    last = 0
    for m in pattern.finditer(text):
        chunk = text[last:m.start()]
        if m.lastindex and m.group(1):
            chunk += " " + m.group(1)
        out.append(chunk)
        last = m.end()
    out.append(text[last:])
    return [p.strip() for p in out if p.strip()]


def split_clauses(sentence):
    """Break one long sentence at its clause boundaries.

    The delimiter stays with the clause it closes. Splitting "0.46% — a narrow
    tape" at the em-dash and then dropping the dash leaves "0.46% a narrow
    tape", which reads as a run-on.
    """
    parts = _split_keep(sentence, CLAUSE_RE)
    if len(parts) > 1:
        return parts
    if len(sentence.split()) > MAX_WORDS_BULLET:
        pieces = _split_keep(sentence, COMMA_RE)
        if len(pieces) > 1:
            return pieces
    return [sentence]


def group_to_bullets(parts, cap=MAX_WORDS_BULLET):
    """Group pieces into bullets that each stay under the cap."""
    out, current = [], []
    for p in parts:
        trial = " ".join(current + [p])
        if len(trial.split()) > cap and current:
            out.append(" ".join(current))
            current = [p]
        else:
            current.append(p)
    if current:
        out.append(" ".join(current))
    return out


def prose_to_bullets(text):
    """A long paragraph becomes one bullet per clause group.

    Sentences first, because a sentence is the natural unit. A single sentence
    that is still over the cap is broken at its clause boundaries - a sentence
    is the smallest thing that can be a bullet, but a 60-word sentence is not
    a bullet a reader can scan.
    """
    sentences = split_sentences(text)
    pieces = []
    for s in sentences:
        if len(s.split()) > MAX_WORDS_BULLET:
            pieces.extend(split_clauses(s))
        else:
            pieces.append(s)
    return group_to_bullets(pieces)


def render(text):
    """The client-safe rendering of one document."""
    lines = text.splitlines()
    out = []
    i = 0
    in_front_matter = False
    fm_done = False

    while i < len(lines):
        line = lines[i]

        # YAML front matter is metadata the client cannot show; keep the lines
        # that carry meaning (date, cron, fire time) and drop the rest.
        if not fm_done and line.strip() == "---":
            if not in_front_matter:
                in_front_matter = True
                i += 1
                fm = []
                while i < len(lines) and lines[i].strip() != "---":
                    fm.append(lines[i])
                    i += 1
                i += 1
                keep = []
                for fl in fm:
                    m = re.match(r"^([A-Za-z_][\w]*):\s*(.*)$", fl)
                    if m and m.group(1) in ("date", "cron", "fire_time_et", "snapshot_et",
                                             "data_date", "live_date", "status"):
                        keep.append("%s: %s" % (m.group(1), m.group(2)))
                if keep:
                    out.append("**%s**" % " · ".join(keep))
                    out.append("")
                fm_done = True
                continue
            i += 1
            continue
        fm_done = True

        # A table becomes bullets.
        if TABLE_RE.match(line) and i + 1 < len(lines) and TABLE_SEP_RE.match(lines[i + 1]):
            rows = []
            while i < len(lines) and TABLE_RE.match(lines[i]):
                rows.append(lines[i])
                i += 1
            for b in table_to_bullets(rows):
                for piece in split_long_bullet(b):
                    out.append("- " + piece)
            out.append("")
            continue
        # A heading becomes a bold label.
        m = HEADING_RE.match(line)
        if m:
            title = glyph_to_words(m.group(2).strip())
            title = cap_first(re.sub(r"^#+\s*", "", title).strip())
            if title:
                out.append("**%s**" % title)
                out.append("")
            i += 1
            continue

        # A blockquote becomes a bullet: the client's renderer may not show
        # the quote bar, and a bullet is the one list form it always shows.
        qm = QUOTE_RE.match(line)
        if qm:
            body = glyph_to_words(qm.group(1), paren=True)
            if len(body.split()) > MAX_WORDS_BULLET:
                out.extend("- " + p for p in prose_to_bullets(body))
            else:
                out.append("- " + body)
            i += 1
            continue

        # A bullet stays a bullet, but is split if it is too long.
        bm = BULLET_RE.match(line) or ORDERED_RE.match(line)
        if bm:
            body = glyph_to_words(re.sub(r"^\s*(?:[-*]|\d+[.)])\s+", "", line), paren=True)
            if len(body.split()) > MAX_WORDS_BULLET:
                for part in prose_to_bullets(body):
                    out.append("- " + part)
            else:
                out.append("- " + body)
            i += 1
            continue

        s = line.strip()
        if not s:
            if out and out[-1] != "":
                out.append("")
            i += 1
            continue

        # Prose.
        para = []
        while i < len(lines) and lines[i].strip() and not HEADING_RE.match(lines[i]) \
                and not BULLET_RE.match(lines[i]) and not ORDERED_RE.match(lines[i]) \
                and not TABLE_RE.match(lines[i]):
            para.append(lines[i].strip())
            i += 1
        if not para:
            i += 1
            continue
        body = glyph_to_words(" ".join(para), paren=True)
        if len(body.split()) > MAX_WORDS_BULLET:
            out.extend("- " + b for b in prose_to_bullets(body))
        else:
            out.append(body)
        out.append("")

    # Collapse runs of blank lines, drop a trailing one, and squeeze the
    # double spaces a removed emoji leaves behind.
    cleaned = []
    for l in out:
        if l == "" and cleaned and cleaned[-1] == "":
            continue
        cleaned.append(re.sub(r"[ \t]{2,}", " ", l).rstrip())
    while cleaned and cleaned[-1] == "":
        cleaned.pop()
    return "\n".join(cleaned) + "\n"


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("artifact", nargs="?", help="one artifact to render")
    ap.add_argument("--out", help="write here instead of stdout")
    ap.add_argument("--dir", help="render every .md under this repo-relative dir")
    ap.add_argument("--out-dir", help="write the rendered files here instead of stdout")
    args = ap.parse_args(argv[1:])

    if args.dir:
        src_root = os.path.join(REPO, args.dir)
        if not os.path.isdir(src_root):
            print("no such dir: %s" % args.dir, file=sys.stderr)
            return 2
        n = 0
        for path in sorted(glob.glob(os.path.join(src_root, "**", "*.md"), recursive=True)):
            rel = os.path.relpath(path, REPO)
            text = open(path, encoding="utf-8").read()
            out_text = render(text)
            if args.out_dir:
                dest = os.path.join(REPO, args.out_dir, os.path.relpath(path, src_root))
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                with open(dest, "w", encoding="utf-8", newline="\n") as fh:
                    fh.write(out_text)
            else:
                print("--- %s" % rel)
                print(out_text)
            n += 1
        print("rendered %d file(s)" % n)
        return 0

    if not args.artifact:
        ap.error("give an artifact path or --dir")
    path = args.artifact if os.path.isabs(args.artifact) else os.path.join(REPO, args.artifact)
    if not os.path.exists(path):
        print("no such file: %s" % args.artifact, file=sys.stderr)
        return 2
    text = open(path, encoding="utf-8").read()
    out_text = render(text)
    if args.out:
        os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
        with open(args.out, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(out_text)
        fails = check(out_text, "reply")
        print("wrote %s (%d findings remain under the reply profile)" % (args.out, len(fails)))
        return 0
    print(out_text)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
