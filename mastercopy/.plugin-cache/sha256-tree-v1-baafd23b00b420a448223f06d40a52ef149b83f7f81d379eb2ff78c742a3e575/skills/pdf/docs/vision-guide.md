# Vision guide — portable PDF page inspection

Use this route only when text extraction cannot recover the information the user needs, or when the
request depends on charts, diagrams, scanned pages, visual hierarchy, or complex financial tables.
The Plugin does not call a product-internal vision service and does not install OCR or rendering
dependencies. It rasterises selected pages and relies on the host model's available image-reading
capability.

## Capability gate

1. Try the text route in [`read-guide.md`](read-guide.md) first for ordinary text and simple tables.
2. Confirm that the running model can inspect images.
3. If it cannot, return the recoverable text and clearly identify which visual content remains
   unverified. Do not call an undeclared service or install a new dependency.
4. For charts and complex financial or regulatory tables, inspect one page per model call so values
   are not attributed to the wrong page.

## Rasterise pages

Run from the Skill root:

```bash
python3 -m scripts.render.page_rasterize input.pdf /tmp/pdf-pages \
  --max-edge 1600 --dpi 200
```

The command writes `page_1.png`, `page_2.png`, and so on. For a narrow page range, use a
preinstalled PDF renderer such as `pdftoppm` before invoking the host image-reading tool:

```bash
pdftoppm -f 12 -l 12 -png -r 200 input.pdf /tmp/pdf-page
```

Do not rasterise hundreds of pages blindly. Build an outline or text index first, locate the
relevant pages, then render only those pages.

## Inspection prompt

For each page, ask the host model to:

- preserve reading order and section hierarchy;
- transcribe visible labels, units, footnotes, and source dates;
- keep table rows and columns aligned;
- describe charts and report only values that are actually legible;
- distinguish printed content from annotations or form values;
- include the source PDF page number in every extracted result.

When exact values matter, compare the visual reading with `pdfplumber`, `pdftotext`, or the source
table. Disagreements must be reported rather than silently resolved.

## Verification

- Inspect one chart or complex table page at a time.
- Verify units, signs, decimal places, year labels, and footnotes.
- For scanned forms, compare field labels and filled values against the rasterised output.
- For generated PDFs, inspect at least the cover, one representative body page, and every unusual
  layout or chart page.
- Keep temporary page images outside the Plugin package and remove them after delivery when safe.

## Missing dependencies

`page_rasterize.py` requires `pdf2image`, Pillow, and a compatible PDF renderer. The `pdftoppm`
alternative requires Poppler. These dependencies must already exist in the managed runtime. If a
dependency is unavailable, stop that route and report the missing capability; never install it from
this Plugin.
