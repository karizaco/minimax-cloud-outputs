# PDF read guide

Use this guide for PDF text, tables, outlines, metadata, page images, and visual inspection. Default
to text extraction. Escalate to page rasterisation only when the requested information depends on
scans, charts, diagrams, complex tables, or visual layout.

## 1. Choose the route

| Input and intent | Route |
| --- | --- |
| Text-native PDF, ordinary paragraphs, simple tables | `pdfplumber` |
| Outline, metadata, page count, encryption, simple page text | `pypdf` |
| Command-line text, metadata, or embedded images | preinstalled Poppler tools |
| Scanned PDF, chart values, layout, complex financial table | rasterise selected pages, then use the host image-reading tool |
| Password-protected or structurally damaged PDF | user-supplied password with `pypdf`, or preinstalled `qpdf` |

Do not send an entire long document through vision. For PDFs over 20 pages when the user wants a
specific fact, build a heading/keyword index first. For PDFs over 200 pages, build that index before
the first extraction pass.

## 2. Locate before extracting

Inspect the outline with `pypdf`:

```python
from pypdf import PdfReader

reader = PdfReader("report.pdf")
print("pages", len(reader.pages))
print(reader.outline)
```

Or create a searchable text index with preinstalled Poppler:

```bash
pdftotext -layout report.pdf /tmp/report.txt
rg -n -i "target phrase|section heading" /tmp/report.txt
```

After locating the relevant section, extract only the required page range. Keep the PDF page number
with every result.

## 3. Text and table extraction

### 3.1 pdfplumber

```python
import pdfplumber

with pdfplumber.open("report.pdf") as doc:
    for page_no, page in enumerate(doc.pages, start=1):
        text = page.extract_text() or ""
        print(f"--- page {page_no} ---")
        print(text)
```

Simple ruled tables:

```python
import pdfplumber

with pdfplumber.open("report.pdf") as doc:
    for page_no, page in enumerate(doc.pages, start=1):
        for table in page.extract_tables():
            print(page_no, table)
```

Coordinate-aware extraction:

```python
import pdfplumber

with pdfplumber.open("invoice.pdf") as doc:
    page = doc.pages[0]
    region = page.within_bbox((100, 100, 400, 200))
    print(region.extract_text())
```

Do not trust table extraction for multi-level headers, merged cells, dotted leaders, footnoted
subtotals, or side-by-side financial tables. Inspect those pages visually.

### 3.2 pypdf

```python
from pypdf import PdfReader

reader = PdfReader("report.pdf")
if reader.is_encrypted:
    reader.decrypt("user-provided-password")

for page_no, page in enumerate(reader.pages, start=1):
    print(page_no, page.extract_text() or "")
```

Never invent or brute-force a password. Ask the user when a password is required.

## 4. Rasterisation and visual inspection

When text extraction returns empty strings, `(cid:NNN)` glyphs, broken reading order, or insufficient
chart/table information, rasterise only the relevant pages.

Run from the Skill root:

```bash
python3 -m scripts.render.page_rasterize report.pdf /tmp/pdf-pages \
  --max-edge 1600 --dpi 200
```

For a single located page with preinstalled Poppler:

```bash
pdftoppm -f 12 -l 12 -png -r 200 report.pdf /tmp/report-page
```

Then inspect the PNG with the host model's image-reading capability. Charts and complex financial
tables must be processed one page per call. Verify units, footnotes, signs, decimal places, periods,
and source dates. If the host model cannot inspect images, return the recoverable text and state
which visual content remains unverified; do not call an undeclared service.

See [`vision-guide.md`](vision-guide.md) for the complete visual quality gate.

## 5. Command-line cookbook

Use these commands only when the runtime already provides them:

```bash
# Preserve visual spacing in extracted text
pdftotext -layout invoice.pdf invoice.txt

# Extract pages 1-3
pdftotext -f 1 -l 3 invoice.pdf snippet.txt

# Extract embedded images at native resolution
pdfimages -all invoice.pdf /tmp/images/img

# Inspect page count, sizes, encryption, and metadata
pdfinfo invoice.pdf

# Check or decrypt with a user-provided password
qpdf --check input.pdf
qpdf --password="$PDF_PASSWORD" --decrypt encrypted.pdf clear.pdf
```

Do not print passwords or retain them in scripts, logs, or the Plugin package.

## 6. Read then write

| User intent | Read step | Write step |
| --- | --- | --- |
| Restyle an existing PDF | extract text/tables; rasterise representative pages for visual cues | REFORMAT or CREATE |
| Fill an unfamiliar form | probe AcroForm metadata; rasterise pages when visible labels are flat | FILL |
| Create a PDF inspired by a reference | rasterise representative pages and identify palette/layout | CREATE |
| Translate while preserving layout | extract text page by page; rasterise only broken/scanned pages | translate-preserve-layout template |
| Verify a generated PDF | read text and inspect representative rendered pages | revise and repeat |

## 7. Troubleshooting

| Symptom | Response |
| --- | --- |
| Empty text or `(cid:NNN)` glyphs | rasterise the relevant page and use host vision |
| Garbled multi-column reading order | extract smaller regions or use visual inspection |
| Complex table columns do not align | inspect one page visually and cross-check totals/footnotes |
| Encrypted PDF | request the password, then decrypt with an available tool |
| `pdftoppm` or `pdfinfo` missing | report that the Poppler-backed route is unavailable |
| `pdfplumber`, `pypdf`, or `pdf2image` import fails | report the missing managed-runtime dependency |
| PDF is corrupt | use preinstalled `qpdf --check`; otherwise report the limitation |

## 8. Runtime dependencies

The relevant route may require Python 3.9+, `pdfplumber`, `pypdf`, `pdf2image`, Pillow,
`pypdfium2`, Poppler, or `qpdf`. These must be supplied by the managed runtime. This Plugin does not
install software, download binaries, call product-internal HTTP services, or mutate the host
environment.
