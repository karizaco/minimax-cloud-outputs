#!/usr/bin/env python3
"""Render the numbers the routines already compute but never draw.

Why: `cross-asset/<date>.md` carries a complete 8x8 correlation matrix, a ranked
pair table, a regime-shift threshold and the distance to it. It is rendered as a
markdown table with emoji colour bands. That is the right data in the wrong
medium: a correlation matrix is the one genuinely two-dimensional artifact in this
repo, and a table makes a reader scan 28 numbers to see the structure the TL;DR
states in one sentence. The same is true of the regime series - breadth and VIX
are recomputed every session into `_regime.json` and never plotted.

What this writes, into `derived/charts/`:
  correlation-matrix.html   the newest cross-asset matrix as a diverging heatmap
  regime-series.html        breadth % and VIX as two separate charts over time

Design rules this follows, and why they are not negotiable:
  * **No dual-axis chart.** Breadth is a percentage and VIX is an index level.
    Two measures of different scale get two charts, never two y-scales on one -
    a dual axis lets the author choose the crossing point and therefore the
    story. They share one x-axis so a reader can still read them together.
  * **Diverging ramp for correlation, sequential logic for magnitude.** Two hues
    (blue positive, red negative) with a neutral gray midpoint, equal steps per
    arm. Never a rainbow, never a hue at the midpoint.
  * **A gap is drawn as a gap.** Six of the thirteen `_regime.json` files carry
    no breadth figure. The line breaks there rather than interpolating across a
    session the routine did not measure.
  * **Every value is reachable without hover.** Each chart ships a table view,
    because one light palette step sits below 3:1 contrast on the light surface
    and the relief rule requires labels or a table.

Palette: the data-viz reference palette, validated rather than eyeballed.
  categorical light #2a78d6,#eb6834,#1baf7a - all checks pass (one contrast WARN
  on the aqua slot, relieved by the table view); dark #3987e5,#d95926,#199e70 -
  all checks pass. The diverging arms are monotone, single-hue and pass the
  sequential gates; the lightest step is allowed to recede toward the surface
  because it means "near zero".

  python3 scripts/build_charts.py            # write the charts
  python3 scripts/build_charts.py --check    # report the extracted data only
"""
import html
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _joinlib as J  # noqa: E402

CROSS = "cross-asset"
SCREENS = "daily-screens"
OUT_ROOT = os.path.join("derived", "charts")

# ---------------------------------------------------------------- the palette
# Diverging arms. Light-to-dark within each arm; the lightest step is nearest
# the neutral midpoint and means "near zero".
#
# The two arms are LIGHTNESS-MATCHED step for step, so a -0.55 carries the same
# visual weight as a +0.55 and the eye is not told that one sign is louder than
# the other. Measured OKLab L, positive vs negative:
#   light  0.905/0.920  0.812/0.816  0.671/0.678  0.527/0.538  (max gap 0.015)
#   dark   0.385/0.388  0.433/0.430  0.527/0.524  0.622/0.621  (max gap 0.004)
# The dark negative arm was re-solved for this: its first draft was 0.060 lighter
# at the weak end and read as more alarming than the positive arm at equal
# magnitude, which is an authored emphasis rather than a property of the data.
POS_LIGHT = ["#cde2fb", "#9ec5f4", "#5598e7", "#256abf"]
NEG_LIGHT = ["#fbdcdc", "#f3aeae", "#e36f6f", "#c22f2f"]
POS_DARK = ["#104281", "#184f95", "#256abf", "#3987e5"]
NEG_DARK = ["#7d1820", "#8b2822", "#aa4442", "#cb625a"]
MID_LIGHT, MID_DARK = "#f0efec", "#383835"

TOKENS = {
    "light": {
        "surface": "#fcfcfb", "plane": "#f9f9f7", "primary": "#0b0b0b",
        "secondary": "#52514e", "muted": "#898781", "grid": "#e1e0d9",
        "axis": "#c3c2b7", "series1": "#2a78d6", "series2": "#eb6834",
        "series3": "#1baf7a", "warn": "#fab219", "ring": "rgba(11,11,11,0.10)",
    },
    "dark": {
        "surface": "#1a1a19", "plane": "#0d0d0d", "primary": "#f0efec",
        "secondary": "#c3c2b7", "muted": "#898781", "grid": "#2c2c2a",
        "axis": "#383835", "series1": "#3987e5", "series2": "#d95926",
        "series3": "#199e70", "warn": "#fab219", "ring": "rgba(255,255,255,0.10)",
    },
}

BANDS = [0.20, 0.40, 0.60, 0.70]  # the cross-asset artifact's own magnitude bands


def band_index(value):
    """Which of the four magnitude bands |value| falls in."""
    a = abs(value)
    for i, edge in enumerate(BANDS):
        if a < edge:
            return i
    return len(BANDS) - 1


def cell_fill(value, mode):
    if value is None:
        return (MID_LIGHT if mode == "light" else MID_DARK)
    if abs(value) < 0.02:
        return (MID_LIGHT if mode == "light" else MID_DARK)
    arm = (POS_LIGHT if mode == "light" else POS_DARK) if value > 0 else \
          (NEG_LIGHT if mode == "light" else NEG_DARK)
    return arm[band_index(value)]


def cell_ink(value, mode):
    """Label colour inside a filled cell, by the fill's luminance."""
    if value is None:
        return TOKENS[mode]["secondary"]
    dark_fill = band_index(value) >= 2 and abs(value) >= 0.02
    if mode == "light":
        return "#ffffff" if dark_fill else "#0b0b0b"
    return "#ffffff" if dark_fill else TOKENS["dark"]["primary"]


# ------------------------------------------------------------- data extraction

def front_matter(text):
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        return {}
    return dict(re.findall(r"^([A-Za-z_][\w]*):\s*(.*)$", m.group(1), re.M))


def read_matrix(date):
    """The 8x8 correlation matrix from one cross-asset artifact."""
    path = os.path.join(J.REPO, CROSS, date + ".md")
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    fm = front_matter(text)
    for _start, header, rows in J.md_tables(text):
        if "SPY" in header and "QQQ" in header and len(header) >= 8:
            labels = [h for h in header if h]
            grid = {}
            for row in rows:
                cells = list(row.values())
                name = J.strip_md(cells[0])
                if not name:
                    continue
                for col, cell in zip(header[1:], cells[1:]):
                    v = J.lead_float(cell)
                    if v is not None:
                        grid[(name, col)] = v
            if grid:
                return {
                    "date": date,
                    "source": "%s/%s.md" % (CROSS, date),
                    "labels": labels,
                    "grid": grid,
                    "window_start": fm.get("window_start"),
                    "window_end": fm.get("window_end"),
                    "n_sessions": fm.get("n_sessions"),
                    "basis": fm.get("basis"),
                    "regime_shift": fm.get("regime_shift"),
                    "max_pair_move": fm.get("max_pair_move"),
                    "shift_threshold": fm.get("shift_threshold"),
                    "signal_line": fm.get("signal_line"),
                    "partial_note": fm.get("partial_includes_in_progress"),
                }
    return None


def latest_matrix():
    root = os.path.join(J.REPO, CROSS)
    if not os.path.isdir(root):
        return None
    dates = sorted(n[:-3] for n in os.listdir(root)
                   if n.endswith(".md") and J.DATE_RE.match(n[:-3]))
    for date in reversed(dates):
        m = read_matrix(date)
        if m:
            return m
    return None


def read_regime_series():
    """Breadth and VIX per session, with the gaps kept as gaps."""
    out = []
    for date in J.dated_dirs(SCREENS):
        path = os.path.join(J.REPO, SCREENS, date, "_regime.json")
        if not os.path.exists(path):
            continue
        try:
            with open(path, encoding="utf-8") as fh:
                d = json.load(fh)
        except (OSError, ValueError):
            continue
        out.append({
            "date": date,
            "breadth": d.get("breadth_pct_spx"),
            "vix": d.get("vix"),
            "vix3m": d.get("vix3m"),
            "uncertainty": d.get("uncertainty"),
            "schema": d.get("_schema"),
            "source": "%s/%s/_regime.json" % (SCREENS, date),
        })
    return out


# ------------------------------------------------------------------- rendering

def css_vars(mode):
    t = TOKENS[mode]
    return "\n".join("    --%s: %s;" % (k, v) for k, v in t.items())


def page(title, subtitle, provenance_line, body, notes, table_html):
    """One self-contained page: dark mode under both scopes, table view, notes."""
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<style>
  .viz-root {
    color-scheme: light;
%(light)s
  }
  @media (prefers-color-scheme: dark) {
    :root:where(:not([data-theme="light"])) .viz-root {
      color-scheme: dark;
%(dark)s
    }
  }
  :root[data-theme="dark"] .viz-root {
    color-scheme: dark;
%(dark)s
  }
  body { margin: 0; background: var(--plane); }
  .viz-root {
    font: 14px/1.5 system-ui, -apple-system, "Segoe UI", sans-serif;
    background: var(--plane); color: var(--primary);
    padding: 24px; min-height: 100vh; box-sizing: border-box;
  }
  .card {
    background: var(--surface); border: 1px solid var(--ring);
    border-radius: 8px; padding: 20px; margin: 0 auto 20px; max-width: 920px;
  }
  h1 { font-size: 19px; font-weight: 600; margin: 0 0 4px; }
  h2 { font-size: 15px; font-weight: 600; margin: 24px 0 8px; }
  .sub { color: var(--secondary); margin: 0 0 2px; }
  .prov { color: var(--muted); font-size: 12px; margin: 8px 0 0; }
  .notes { color: var(--secondary); font-size: 13px; max-width: 920px;
           margin: 0 auto 20px; }
  .notes li { margin-bottom: 6px; }
  table { border-collapse: collapse; font-size: 12px;
          font-variant-numeric: tabular-nums; }
  .dataview th, .dataview td {
    border-bottom: 1px solid var(--grid); padding: 4px 10px; text-align: right;
    color: var(--primary);
  }
  .dataview th { color: var(--secondary); font-weight: 600; }
  .dataview th:first-child, .dataview td:first-child { text-align: left; }
  details { max-width: 920px; margin: 0 auto 24px; }
  summary { cursor: pointer; color: var(--secondary); font-size: 13px;
            padding: 6px 0; }
  .legend { display: flex; flex-wrap: wrap; gap: 14px; align-items: center;
            margin: 10px 0 0; color: var(--secondary); font-size: 12px; }
  .legend .key { display: inline-block; width: 14px; height: 10px;
                 border-radius: 2px; margin-right: 6px; vertical-align: middle; }
  .legend .line { display: inline-block; width: 16px; height: 2px;
                  margin-right: 6px; vertical-align: middle; }
  .tip {
    position: fixed; pointer-events: none; opacity: 0; transition: opacity .08s;
    background: var(--surface); color: var(--primary);
    border: 1px solid var(--ring); border-radius: 6px; padding: 6px 9px;
    font-size: 12px; box-shadow: 0 2px 10px rgba(0,0,0,.18); z-index: 10;
    font-variant-numeric: tabular-nums;
  }
  .tip b { font-size: 13px; }
  .tip .nm { color: var(--secondary); }
  svg { display: block; max-width: 100%%; height: auto; }
  svg text { font: 11px system-ui, -apple-system, "Segoe UI", sans-serif; }
  .hit { fill: transparent; }
  .hit:hover, .hit:focus { outline: none; }
</style>
</head>
<body>
<div class="viz-root">
  <div class="card">
    <h1>%(title)s</h1>
    <p class="sub">%(subtitle)s</p>
%(body)s
    <p class="prov">%(prov)s</p>
  </div>
  <div class="notes">%(notes)s</div>
  <details>
    <summary>Table view — every value, without hovering</summary>
%(table)s
  </details>
</div>
<div class="tip" id="tip"></div>
<script>
(function () {
  var tip = document.getElementById('tip');
  function show(e, html) {
    tip.innerHTML = html;
    tip.style.opacity = '1';
    var r = tip.getBoundingClientRect();
    var x = e.clientX + 14, y = e.clientY + 14;
    if (x + r.width > window.innerWidth) { x = e.clientX - r.width - 14; }
    if (y + r.height > window.innerHeight) { y = e.clientY - r.height - 14; }
    tip.style.left = x + 'px'; tip.style.top = y + 'px';
  }
  function hide() { tip.style.opacity = '0'; }
  document.querySelectorAll('[data-tip]').forEach(function (el) {
    el.addEventListener('pointermove', function (e) { show(e, el.dataset.tip); });
    el.addEventListener('pointerleave', hide);
    el.addEventListener('focus', function () {
      var b = el.getBoundingClientRect();
      show({ clientX: b.left + b.width / 2, clientY: b.top }, el.dataset.tip);
    });
    el.addEventListener('blur', hide);
  });
})();
</script>
</body>
</html>
""" % {
        "title": html.escape(title),
        "subtitle": subtitle,
        "prov": provenance_line,
        "body": body,
        "notes": notes,
        "table": table_html,
        "light": css_vars("light"),
        "dark": css_vars("dark"),
    }


def render_matrix(m):
    labels = m["labels"]
    n = len(labels)
    cell, gap = 62, 2
    left, top = 54, 30
    w = left + n * cell + 14
    h = top + n * cell + 44

    parts = ['<svg viewBox="0 0 %d %d" role="img" aria-label="Correlation matrix of %d proxies">' % (w, h, n)]
    for j, col in enumerate(labels):
        parts.append('<text x="%d" y="%d" text-anchor="middle" fill="%s">%s</text>'
                     % (left + j * cell + cell / 2, top - 10, "var(--secondary)", html.escape(col)))
    for i, rowname in enumerate(labels):
        parts.append('<text x="%d" y="%d" text-anchor="end" fill="%s">%s</text>'
                     % (left - 10, top + i * cell + cell / 2 + 4, "var(--secondary)", html.escape(rowname)))
        for j, col in enumerate(labels):
            v = m["grid"].get((rowname, col))
            if v is None and rowname == col:
                v = 1.0
            x = left + j * cell + gap / 2
            y = top + i * cell + gap / 2
            size = cell - gap
            fill_l = cell_fill(v, "light")
            fill_d = cell_fill(v, "dark")
            ink_l = cell_ink(v, "light")
            ink_d = cell_ink(v, "dark")
            label = "—" if v is None else ("%+.2f" % v)
            band = "diagonal" if rowname == col else (
                "—" if v is None else
                ["uncorrelated", "mild", "moderate", "elevated/strong"][band_index(v)])
            tip = ("<b>%s</b><br><span class='nm'>%s - %s</span><br>band: %s"
                   % (label, html.escape(rowname), html.escape(col), band))
            parts.append(
                '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="3" '
                'fill="%s" style="fill:light-dark(%s,%s)"/>'
                % (x, y, size, size, fill_l, fill_l, fill_d))
            parts.append(
                '<text x="%.1f" y="%.1f" text-anchor="middle" fill="%s" '
                'style="fill:light-dark(%s,%s)">%s</text>'
                % (x + size / 2, y + size / 2 + 4, ink_l, ink_l, ink_d, label))
            parts.append(
                '<rect class="hit" x="%.1f" y="%.1f" width="%.1f" height="%.1f" '
                'tabindex="0" data-tip="%s"/>'
                % (x, y, size, size, html.escape(tip, quote=True)))
    parts.append("</svg>")

    swatches = []
    for i, edge in enumerate(["< 0.20", "0.20–0.40", "0.40–0.60", "≥ 0.60"]):
        swatches.append(
            '<span><span class="key" style="background:light-dark(%s,%s)"></span>%s</span>'
            % (POS_LIGHT[i], POS_DARK[i], edge))
    legend = (
        '<div class="legend"><span>Positive</span>%s</div>'
        '<div class="legend"><span>Negative</span>%s</div>'
        % ("".join(swatches),
           "".join('<span><span class="key" style="background:light-dark(%s,%s)"></span>%s</span>'
                   % (NEG_LIGHT[i], NEG_DARK[i], e)
                   for i, e in enumerate(["< 0.20", "0.20–0.40", "0.40–0.60", "≥ 0.60"]))))

    rows = ["<table class='dataview'><thead><tr><th>Pair</th>" +
            "".join("<th>%s</th>" % html.escape(c) for c in labels) + "</tr></thead><tbody>"]
    for rowname in labels:
        cells = []
        for col in labels:
            v = m["grid"].get((rowname, col))
            if v is None and rowname == col:
                v = 1.0
            cells.append("<td>%s</td>" % ("—" if v is None else "%+.2f" % v))
        rows.append("<tr><th>%s</th>%s</tr>" % (html.escape(rowname), "".join(cells)))
    rows.append("</tbody></table>")

    notes = """<p><strong>What the picture says that the table does not.</strong> The
block of strong positive cells across SPY / QQQ / IWM / EEM is the equity complex
moving as one thing. The VIX row is its mirror in the opposite hue — that is what a
hedge looks like. The two pale rows, TLT and UUP, are the only parts of this
universe not tied to equity direction.</p>
<p><strong>What it does not say.</strong> Correlation is not causation and this is a
single trailing window, not a forecast. A pair that is uncorrelated over %(sessions)s
sessions can co-move sharply inside any one of them, and the window's own
<code>%(basis)s</code> basis removes shared drift by construction. Read it as regime
context only — the source artifact states no direction and neither does this.</p>
<ul>
<li><strong>Window:</strong> %(ws)s → %(we)s, %(sessions)s aligned sessions, basis
<code>%(basis)s</code>.</li>
<li><strong>Regime shift:</strong> %(shift)s — largest week-over-week pair move
%(move)s against a %(thresh)s threshold.</li>
<li><strong>Colour is magnitude, sign is the hue and the number.</strong> The bands
are the source artifact's own (0.20 / 0.40 / 0.60 / 0.70), so this heatmap and the
markdown table it came from cut the data identically.</li>
<li><strong>Every value is in the table view above</strong>, and each cell carries
its own value as a label — nothing here is reachable only by hovering.</li>
</ul>""" % {
        "sessions": html.escape(m["n_sessions"] or "?"),
        "basis": html.escape(m["basis"] or "?"),
        "ws": html.escape(m["window_start"] or "?"),
        "we": html.escape(m["window_end"] or "?"),
        "shift": html.escape((m["regime_shift"] or "?").upper()),
        "move": html.escape(m["max_pair_move"] or "?"),
        "thresh": html.escape(m["shift_threshold"] or "0.20"),
    }

    body = "".join(parts) + legend
    subtitle = ("Daily log-return correlations across %d proxies · window ending %s"
                % (n, html.escape(m["window_end"] or "?")))
    prov = ("<strong>Source:</strong> <code>%s</code> · <strong>Built:</strong> %s · "
            "<strong>Covers:</strong> the %s window, %s sessions, basis <code>%s</code> · "
            "derived render, the source artifact is not modified"
            % (html.escape(m["source"]), _now(), html.escape(m["window_end"] or "?"),
               html.escape(m["n_sessions"] or "?"), html.escape(m["basis"] or "?")))
    return page("Cross-asset correlation matrix — %s" % m["date"],
                subtitle, prov, body, notes, "".join(rows))


def _now():
    """The build date, to the day - see _joinlib.build_stamp for why not finer."""
    return J.build_stamp()


def nice_axis(lo, hi, target=4):
    """Round axis bounds and a round step, so ticks land on clean numbers.

    An axis stepped straight off the data minimum prints ticks like 57% / 59% /
    62%, which makes a reader do arithmetic to place a value. Step and bounds
    are snapped to 1 / 2 / 2.5 / 5 x 10^k instead.
    """
    import math
    if hi <= lo:
        hi = lo + 1.0
    raw = (hi - lo) / max(1, target)
    mag = 10 ** math.floor(math.log10(raw)) if raw > 0 else 1.0
    for mult in (1, 2, 2.5, 5, 10):
        step = mult * mag
        if raw <= step:
            break
    lo_n = math.floor(lo / step) * step
    hi_n = math.ceil(hi / step) * step
    ticks = []
    v = lo_n
    while v <= hi_n + step * 1e-9:
        ticks.append(round(v, 10))
        v += step
    return lo_n, hi_n, ticks, step


def line_chart(series, title, y_label, color_var, fmt="%.1f", unit="", y_pad=0.08,
               flags=None, flag_label=""):
    """One measure over time. Single series, so no legend box - the title names it.

    `series` is a list of (date, value_or_None). A None breaks the path rather
    than being interpolated across.
    """
    w, h = 880, 230
    left, right, top, bottom = 48, 16, 18, 34
    pts = [(i, v) for i, (_d, v) in enumerate(series) if v is not None]
    if not pts:
        return "<p>No values to plot.</p>"
    vals = [v for _i, v in pts]
    lo, hi = min(vals), max(vals)
    span = (hi - lo) or 1.0
    lo, hi, tick_values, step = nice_axis(lo - span * y_pad, hi + span * y_pad)
    # Tick precision follows the step. A 2.5 step printed with %.0f renders 57.5
    # as "58" - a label that is simply not the value the gridline sits on.
    tick_dec = 0 if abs(step - round(step)) < 1e-9 else 1
    tick_fmt = "%." + str(tick_dec) + "f" + unit.replace("%", "%%")
    n = len(series)

    def px(i):
        if n == 1:
            return left + (w - left - right) / 2
        return left + i * (w - left - right) / (n - 1)

    def py(v):
        return top + (hi - v) * (h - top - bottom) / (hi - lo)

    parts = ['<svg viewBox="0 0 %d %d" role="img" aria-label="%s">'
             % (w, h, html.escape(title))]
    for v in tick_values:
        y = py(v)
        parts.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="var(--grid)" '
                     'stroke-width="1"/>' % (left, y, w - right, y))
        parts.append('<text x="%d" y="%.1f" text-anchor="end" fill="var(--muted)">%s</text>'
                     % (left - 8, y + 3.5, tick_fmt % v))
    parts.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="var(--axis)" '
                 'stroke-width="1"/>' % (left, py(lo), w - right, py(lo)))

    # The regime flag is an annotation, not a series: a short tick under the
    # baseline. Drawn full height it reads as a chart border and competes with
    # the data for the eye.
    if flags:
        base = py(lo)
        for i, (_d, _v) in enumerate(series):
            if flags[i]:
                parts.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" '
                             'stroke="var(--warn)" stroke-width="3" '
                             'stroke-linecap="round"/>'
                             % (px(i), base + 3, px(i), base + 9))

    # Break the path wherever the routine published no value.
    runs, run = [], []
    for i, (_d, v) in enumerate(series):
        if v is None:
            if len(run) > 1:
                runs.append(run)
            run = []
        else:
            run.append((i, v))
    if len(run) > 1:
        runs.append(run)
    for r in runs:
        d = " ".join(("%s%.1f,%.1f" % ("M" if k == 0 else "L", px(i), py(v)))
                     for k, (i, v) in enumerate(r))
        parts.append('<path d="%s" fill="none" stroke="%s" stroke-width="2" '
                     'stroke-linejoin="round" stroke-linecap="round"/>' % (d, color_var))

    for i, v in pts:
        parts.append('<circle cx="%.1f" cy="%.1f" r="4.5" fill="%s" '
                     'stroke="var(--surface)" stroke-width="2"/>' % (px(i), py(v), color_var))

    last_i, last_v = pts[-1]
    parts.append('<text x="%.1f" y="%.1f" text-anchor="end" fill="var(--primary)" '
                 'font-weight="600">%s</text>'
                 % (px(last_i) - 2, py(last_v) - 12, fmt % last_v))

    step = max(1, n // 7)
    for i, (d, _v) in enumerate(series):
        if i % step == 0 or i == n - 1:
            parts.append('<text x="%.1f" y="%d" text-anchor="middle" fill="var(--muted)">%s</text>'
                         % (px(i), h - 8, html.escape(d[5:])))

    for i, (d, v) in enumerate(series):
        label = "no value published" if v is None else (fmt % v)
        extra = ""
        if flags and flags[i]:
            extra = "<br><span class='nm'>%s</span>" % html.escape(flag_label)
        tip = "<b>%s</b><br><span class='nm'>%s · %s</span>%s" % (
            label, html.escape(d), html.escape(y_label), extra)
        bw = (w - left - right) / max(1, n - 1) if n > 1 else 40
        parts.append('<rect class="hit" x="%.1f" y="%d" width="%.1f" height="%d" '
                     'tabindex="0" data-tip="%s"/>'
                     % (px(i) - bw / 2, top, bw, h - top - bottom,
                        html.escape(tip, quote=True)))
    parts.append("</svg>")
    return "".join(parts)


def render_regime(series):
    dates = [s["date"] for s in series]
    breadth = [(s["date"], s["breadth"]) for s in series]
    vix = [(s["date"], s["vix"]) for s in series]
    flags = [bool(s["uncertainty"]) for s in series]

    n_breadth = sum(1 for s in series if s["breadth"] is not None)
    n_vix = sum(1 for s in series if s["vix"] is not None)
    missing = [s["date"] for s in series if s["breadth"] is None]

    body = []
    body.append("<h2>Breadth — share of S&amp;P 500 names above their 20-DMA</h2>")
    body.append(line_chart(breadth, "Breadth percentage by session", "breadth %",
                           "var(--series1)", "%.1f%%", unit="%", flags=flags,
                           flag_label="regime flag: uncertainty"))
    body.append('<div class="legend">'
                '<span><span class="line" style="background:var(--series1)"></span>breadth %</span>'
                '<span><span class="line" style="background:var(--warn)"></span>'
                'session the <code>uncertainty</code> flag was set (tick below the axis)'
                '</span></div>')
    body.append("<h2>VIX — close as the screen recorded it</h2>")
    body.append(line_chart(vix, "VIX level by session", "VIX", "var(--series2)", "%.2f",
                           unit="", flags=flags, flag_label="regime flag: uncertainty"))
    body.append('<div class="legend">'
                '<span><span class="line" style="background:var(--series2)"></span>VIX</span>'
                '<span><span class="line" style="background:var(--warn)"></span>'
                'session the <code>uncertainty</code> flag was set (tick below the axis)'
                '</span></div>')

    rows = ["<table class='dataview'><thead><tr><th>Session</th><th>Breadth %</th>"
            "<th>VIX</th><th>VIX3M</th><th>uncertainty</th></tr></thead><tbody>"]
    for s in series:
        rows.append("<tr><th>%s</th><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (
            html.escape(s["date"]),
            "—" if s["breadth"] is None else "%.2f" % s["breadth"],
            "—" if s["vix"] is None else "%.2f" % s["vix"],
            "—" if s["vix3m"] is None else "%.2f" % s["vix3m"],
            "yes" if s["uncertainty"] else ("no" if s["uncertainty"] is False else "—")))
    rows.append("</tbody></table>")

    notes = """<p><strong>Two charts, not one chart with two axes.</strong> Breadth is a
percentage and VIX is an index level. Putting them on one pair of y-axes would let
whoever drew it choose where the two lines cross, and therefore choose the story. They
share an x-axis instead, so they can still be read together without the crossing point
being an authored artifact.</p>
<p><strong>The gaps are real and are drawn as gaps.</strong> %(n_breadth)s of
%(total)s sessions publish a breadth figure and %(n_vix)s publish a VIX. The line
breaks where the routine published nothing rather than interpolating across a session
it did not measure — %(missing)s carry no breadth value at all, and %(early)s predate
the <code>_schema: 2</code> regime file.</p>
<p><strong>What this does not show.</strong> It is not a market index and not a
return. Breadth here is the screen's own breadth input, which is a share of names
above a moving average, so it says how many names participate — never how much
anything moved. The two charts are regime context for reading a daily brief, and
nothing in them states a direction.</p>
<ul>
<li><strong>Sessions:</strong> %(first)s → %(last)s, %(total)s
<code>_regime.json</code> files.</li>
<li><strong>The amber rules</strong> mark the sessions whose regime file set
<code>uncertainty: true</code> — a flag the screen itself raised, not a
threshold applied here.</li>
<li><strong>Every value is in the table view above</strong>, including the sessions
with no value, which appear as <code>—</code>.</li>
</ul>""" % {
        "n_breadth": n_breadth, "n_vix": n_vix, "total": len(series),
        "missing": html.escape(", ".join(missing[:4]) or "none"),
        "early": html.escape("the files before 2026-11-05"),
        "first": html.escape(dates[0] if dates else "?"),
        "last": html.escape(dates[-1] if dates else "?"),
    }

    prov = ("<strong>Source:</strong> <code>daily-screens/&lt;date&gt;/_regime.json</code> "
            "(%d files) · <strong>Built:</strong> %s · <strong>Covers:</strong> %s → %s · "
            "derived render, no source artifact is modified"
            % (len(series), _now(), html.escape(dates[0] if dates else "?"),
               html.escape(dates[-1] if dates else "?")))
    subtitle = ("Breadth and volatility per session, as the screen recorded them — "
                "%d of %d sessions carry a breadth figure" % (n_breadth, len(series)))
    return page("Regime series — breadth and VIX", subtitle, prov,
                "".join(body), notes, "".join(rows))


def main(argv):
    check_only = "--check" in argv
    m = latest_matrix()
    series = read_regime_series()

    if check_only:
        if m:
            print("matrix %s: %d labels, %d cells, window %s->%s"
                  % (m["date"], len(m["labels"]), len(m["grid"]),
                     m["window_start"], m["window_end"]))
        else:
            print("no correlation matrix found")
        n_b = sum(1 for s in series if s["breadth"] is not None)
        n_v = sum(1 for s in series if s["vix"] is not None)
        print("regime: %d files, %d with breadth, %d with vix" % (len(series), n_b, n_v))
        return 0

    out = os.path.join(J.REPO, OUT_ROOT)
    if m:
        a = J.write_if_changed(os.path.join(out, "correlation-matrix.html"), render_matrix(m))
        print("correlation-matrix.html %s" % a)
    else:
        print("no correlation matrix found - nothing written for it")
    if series:
        b = J.write_if_changed(os.path.join(out, "regime-series.html"), render_regime(series))
        print("regime-series.html %s" % b)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
