# Windows Bootstrap for the xlsx Skill

Use this reference when the xlsx skill runs on Windows and a required command or Python package is
missing. Detect each dependency first, install only what the current spreadsheet task needs, and
rerun the detection command after installation. Do not install optional tools pre-emptively.

Run the detection and installation commands below in PowerShell. Use `python`, not `python3`, for
native Windows commands.

## Required tools

### Git Bash

Git Bash is required for examples that use Bash syntax, pipes, heredocs, or `/tmp/` paths.

```powershell
bash --version
```

If the command is missing, install Git for Windows:

```powershell
winget install Git.Git --accept-source-agreements --accept-package-agreements
```

If `git` works but `bash` does not, repair the Git installation or add the Git directory containing
`bash.exe` to `PATH`.

### Python 3.9 or newer

```powershell
python --version
```

If Python is missing or older than 3.9:

```powershell
winget install Python.Python.3.12 --accept-source-agreements --accept-package-agreements
```

### Required Python packages

The default xlsx workflow uses `openpyxl` for workbook editing and `pandas` for tabular data.

```powershell
python -c "import openpyxl, pandas; print(openpyxl.__version__, pandas.__version__)"
```

Install the packages only if that import fails:

```powershell
python -m pip install openpyxl pandas
```

Use `python -m pip`, not a bare `pip` command, so the packages are installed into the selected
Python interpreter.

### LibreOffice

`scripts/recalc.py` requires LibreOffice's `soffice` command to recalculate formulas before
delivery.

```powershell
soffice --version
```

If it is missing:

```powershell
winget install TheDocumentFoundation.LibreOffice --accept-source-agreements --accept-package-agreements
```

## Optional Python packages

Install these only when the requested workflow needs them:

| Package | Use |
|---|---|
| `polars` | Faster reading and transformation of very large spreadsheet inputs |
| `xlsxwriter` | High-throughput creation of write-only XLSX output |
| `pyexcel` + `pyexcel-xlsx` | Format-agnostic conversion involving XLSX |

Check and install an optional dependency individually:

```powershell
python -c "import polars"
python -m pip install polars

python -c "import xlsxwriter"
python -m pip install xlsxwriter

python -c "import pyexcel"
python -m pip install pyexcel pyexcel-xlsx
```

## Refresh PATH after installation

The current PowerShell session may not see commands installed by `winget`. Refresh it before
retrying detection:

```powershell
$env:PATH = [System.Environment]::GetEnvironmentVariable('Path','Machine') + ';' + [System.Environment]::GetEnvironmentVariable('Path','User')
```

If the command is still unavailable, start a new PowerShell session and rerun the detection
command.

## Run Bash-based examples

Invoke Bash explicitly from PowerShell:

```powershell
bash -c "python scripts/office/unpack.py input.xlsx /tmp/work/"
bash -c "python scripts/office/pack.py /tmp/work/ output.xlsx"
```

Git Bash maps `/tmp/` to a Windows temporary directory. If a Windows path causes quoting problems,
use forward slashes, for example `C:/Users/me/workbook.xlsx`.

Inside Git Bash, detect the available Python command instead of assuming `python3` exists:

```bash
PY="${PYTHON:-$(command -v python3 || command -v python)}"
```

## recalc.py limitation on Windows

`scripts/recalc.py` currently installs its LibreOffice Basic macro under the Linux path
`~/.config/libreoffice/...`. Native Windows LibreOffice stores macros under
`%APPDATA%\LibreOffice\4\user\basic\Standard\`, so the script cannot find the macro until it is
updated to resolve the Windows directory.

Until that limitation is fixed, open the workbook in the LibreOffice GUI, run
Ctrl+Shift+F9 to recalculate all formulas, and save the workbook. Continue to apply the skill's
formula-error and formula-count checks to the recalculated output.
