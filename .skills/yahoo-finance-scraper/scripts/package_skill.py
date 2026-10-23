#!/usr/bin/env python3
"""
Package Yahoo Finance Scraper Skill
Creates a distributable .skill archive.
"""

import json
import os
import shutil
import sys
import tarfile
from pathlib import Path


def package_skill(skill_path: Path, output_dir: Path = None) -> Path:
    """Create a .skill archive from skill directory."""
    skill_path = Path(skill_path)

    if not skill_path.exists():
        raise FileNotFoundError(f"Skill path not found: {skill_path}")

    # Output directory
    if output_dir is None:
        output_dir = Path("/workspace/temp-skills")
    else:
        output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Get skill name from _meta.json
    meta_file = skill_path / "_meta.json"
    if meta_file.exists():
        meta = json.loads(meta_file.read_text())
        archive_name = f"{meta.get('id', 'unknown')}.skill"
    else:
        archive_name = "unknown.skill"

    output_path = output_dir / archive_name

    # Create tar archive
    with tarfile.open(output_path, "w:gz") as tar:
        for item in skill_path.rglob("*"):
            if item.is_file() and not item.name.startswith("."):
                # Calculate archive name (relative path)
                arcname = item.relative_to(skill_path)
                tar.add(item, arcname=arcname)

    print(f"Created skill archive: {output_path}")
    print(f"Size: {output_path.stat().st_size / 1024:.1f} KB")

    return output_path


def main():
    skill_path = Path(__file__).parent.parent

    if len(sys.argv) > 1:
        skill_path = Path(sys.argv[1])

    output_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else None

    try:
        output_path = package_skill(skill_path, output_dir)
        print(f"\nSkill packaged successfully!")
        print(f"Archive: {output_path}")
    except Exception as e:
        print(f"Error packaging skill: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
