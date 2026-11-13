#!/usr/bin/env python3
"""Validate relative links in Markdown files without third-party dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", ".github"}
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\((<[^>]+>|[^\s)]+)(?:\s+[^)]*)?\)")


def markdown_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if not any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts)
    )


def check_file(markdown_file: Path) -> list[str]:
    errors: list[str] = []
    content = markdown_file.read_text(encoding="utf-8")
    for line_number, line in enumerate(content.splitlines(), start=1):
        for match in LINK_RE.finditer(line):
            target = match.group(1).strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or target.startswith("//") or not parsed.path:
                continue

            relative_target = unquote(parsed.path)
            resolved = (markdown_file.parent / relative_target).resolve()
            if not resolved.exists():
                relative_file = markdown_file.relative_to(ROOT)
                errors.append(
                    f"{relative_file}:{line_number}: missing local target '{relative_target}'"
                )
    return errors


def main() -> int:
    files = markdown_files()
    errors = [error for path in files for error in check_file(path)]
    if errors:
        print("\n".join(errors), file=sys.stderr)
        print(f"Found {len(errors)} broken local Markdown link(s).", file=sys.stderr)
        return 1

    print(f"Validated local Markdown links in {len(files)} file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
