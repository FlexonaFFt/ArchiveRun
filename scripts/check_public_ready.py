#!/usr/bin/env python3
"""Report tracked files that deserve review before publishing."""

from __future__ import annotations

import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

BLOCKED_PARTS = {
    ".idea",
    ".venv",
    "venv",
    "env",
    "myenv",
    "__pycache__",
}
BLOCKED_NAMES = {".DS_Store"}
REVIEW_SUFFIXES = {
    ".csv",
    ".db",
    ".docx",
    ".ipynb",
    ".pkl",
    ".pt",
    ".sqlite",
}
REVIEW_NAMES = {"input.txt", "output.txt", "test.txt", "read.txt", "read2.txt"}
LARGE_FILE_BYTES = 1_000_000


def tracked_files() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files"],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    )
    return [ROOT / line for line in result.stdout.splitlines() if line]


def reason_for(path: Path) -> str | None:
    rel = path.relative_to(ROOT)
    parts = set(rel.parts)

    if parts & BLOCKED_PARTS:
        return "tracked local environment or IDE artifact"
    if path.name in BLOCKED_NAMES:
        return "tracked macOS metadata file"
    if path.suffix.lower() in REVIEW_SUFFIXES:
        return "review data/document/binary artifact before publishing"
    if path.name.lower() in REVIEW_NAMES:
        return "review local scratch input/output file"
    if path.exists() and path.stat().st_size > LARGE_FILE_BYTES:
        return "review large tracked file"
    return None


def main() -> int:
    findings: list[tuple[Path, str]] = []
    for path in tracked_files():
        reason = reason_for(path)
        if reason is not None:
            findings.append((path.relative_to(ROOT), reason))

    if not findings:
        print("No tracked publication risks found.")
        return 0

    print("Tracked files to review before publishing:")
    for rel, reason in findings:
        print(f"- {rel}: {reason}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
