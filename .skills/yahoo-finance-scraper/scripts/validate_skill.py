#!/usr/bin/env python3
"""
Validation Script for Yahoo Finance Scraper Skill
Validates structure, frontmatter, and references.
"""

import json
import os
import re
import sys
from pathlib import Path


def validate_frontmatter(skill_path: Path) -> tuple[bool, str]:
    """Validate SKILL.md frontmatter format."""
    skill_md = skill_path / "SKILL.md"

    if not skill_md.exists():
        return False, "SKILL.md not found"

    content = skill_md.read_text()

    # Check frontmatter starts correctly
    if not content.startswith("---"):
        return False, "SKILL.md must start with YAML frontmatter (---)"

    # Extract frontmatter
    frontmatter_end = content.find("\n---\n", 4)
    if frontmatter_end == -1:
        return False, "SKILL.md frontmatter not properly closed"

    frontmatter = content[3:frontmatter_end]

    # Check required fields
    if not re.search(r"^name:", frontmatter, re.MULTILINE):
        return False, "Missing 'name' field in frontmatter"

    if not re.search(r"^description:", frontmatter, re.MULTILINE):
        return False, "Missing 'description' field in frontmatter"

    # Validate name format
    name_match = re.search(r"^name:\s*(.+)$", frontmatter, re.MULTILINE)
    if name_match:
        name = name_match.group(1).strip()
        if not re.match(r"^[a-z0-9-]+$", name):
            return False, f"Invalid name format: '{name}'. Use lowercase with hyphens only"

    return True, "Frontmatter valid"


def validate_meta_json(skill_path: Path) -> tuple[bool, str]:
    """Validate _meta.json structure."""
    meta_file = skill_path / "_meta.json"

    if not meta_file.exists():
        return False, "_meta.json not found"

    try:
        meta = json.loads(meta_file.read_text())
    except json.JSONDecodeError as e:
        return False, f"_meta.json is not valid JSON: {e}"

    # Check required fields
    if "id" not in meta:
        return False, "Missing 'id' field in _meta.json"

    if "version" not in meta:
        return False, "Missing 'version' field in _meta.json"

    # Validate id is integer
    if not isinstance(meta["id"], int):
        return False, "'id' must be an integer"

    # Validate version format
    version = meta["version"]
    if not re.match(r"^\d+\.\d+\.\d+$", version):
        return False, f"Invalid version format: '{version}'. Use semantic versioning (x.y.z)"

    return True, "_meta.json valid"


def validate_script(skill_path: Path) -> tuple[bool, str]:
    """Validate script exists and has no obvious errors."""
    script_path = skill_path / "scripts" / "scrape_yfinance.py"

    if not script_path.exists():
        return False, "scrape_yfinance.py not found"

    content = script_path.read_text()

    # Check for main function
    if "def main():" not in content:
        return False, "Missing main() function"

    # Check for key functions
    required_functions = [
        "def get_quote",
        "def get_historical",
        "def get_financials",
    ]

    for func in required_functions:
        if func not in content:
            return False, f"Missing required function: {func}"

    # Check for proper imports
    if "import yfinance" not in content:
        return False, "Missing yfinance import"

    return True, "Script structure valid"


def validate_directory_structure(skill_path: Path) -> tuple[bool, str]:
    """Validate required directories exist."""
    required_dirs = ["scripts", "docs"]

    for dir_name in required_dirs:
        dir_path = skill_path / dir_name
        if not dir_path.exists():
            return False, f"Missing directory: {dir_name}"
        if not dir_path.is_dir():
            return False, f"{dir_name} is not a directory"

    return True, "Directory structure valid"


def run_all_validations(skill_path: Path = None) -> bool:
    """Run all validations and return overall success."""
    if skill_path is None:
        skill_path = Path(__file__).parent.parent

    print(f"Validating skill at: {skill_path}")
    print("=" * 50)

    all_passed = True

    # Run each validation
    validations = [
        ("Frontmatter", validate_frontmatter),
        ("Meta JSON", validate_meta_json),
        ("Directory Structure", validate_directory_structure),
        ("Script", validate_script),
    ]

    for name, validator in validations:
        passed, message = validator(skill_path)
        status = "PASS" if passed else "FAIL"
        print(f"[{status}] {name}: {message}")
        if not passed:
            all_passed = False

    print("=" * 50)

    if all_passed:
        print("All validations passed!")
        return True
    else:
        print("Some validations failed.")
        return False


if __name__ == "__main__":
    skill_path = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    success = run_all_validations(skill_path)
    sys.exit(0 if success else 1)
