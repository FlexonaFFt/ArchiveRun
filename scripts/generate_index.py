#!/usr/bin/env python3
"""Generate a lightweight repository index for portfolio navigation."""

from __future__ import annotations

from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "docs" / "INDEX.md"
EXCLUDED_DIRS = {".git", ".idea", ".venv", "venv", "env", "myenv", "__pycache__"}
FILE_TYPE_COLUMNS_PER_ROW = 8


def is_excluded(path: Path) -> bool:
    return any(part in EXCLUDED_DIRS for part in path.relative_to(ROOT).parts)


def count_files(path: Path) -> int:
    if not path.exists():
        return 0
    return sum(1 for item in path.rglob("*") if item.is_file() and not is_excluded(item))


def count_dirs(path: Path) -> int:
    if not path.exists():
        return 0
    return sum(1 for item in path.iterdir() if item.is_dir() and not is_excluded(item))


def extension_counts() -> Counter[str]:
    counts: Counter[str] = Counter()
    for item in ROOT.rglob("*"):
        if item.is_file() and not is_excluded(item):
            suffix = item.suffix.lower() or "[no extension]"
            counts[suffix] += 1
    return counts


def section_row(label: str, path: str, description: str) -> str:
    target = ROOT / path
    return (
        f"| [{label}](../{path}) | {description} | "
        f"{count_dirs(target)} | {count_files(target)} |"
    )


def file_type_tables(counts: Counter[str]) -> list[str]:
    lines: list[str] = []
    items = counts.most_common()

    for start in range(0, len(items), FILE_TYPE_COLUMNS_PER_ROW):
        chunk = items[start : start + FILE_TYPE_COLUMNS_PER_ROW]
        headers = " | ".join(f"`{suffix}`" for suffix, _ in chunk)
        alignment = " | ".join("---:" for _ in chunk)
        values = " | ".join(str(amount) for _, amount in chunk)
        lines.extend(
            [
                f"| {headers} |",
                f"| {alignment} |",
                f"| {values} |",
                "",
            ]
        )

    return lines


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    counts = extension_counts()

    lines = [
        "# Repository Index",
        "",
        f"Generated at: {generated_at}",
        "",
        "## Sections",
        "",
        "| Section | Description | Directories | Files |",
        "| --- | --- | ---: | ---: |",
        section_row("Showcase", "showcase", "Curated portfolio entry points"),
        section_row("LeetCode tasks", "platforms/leetcode/tasks", "Individual LeetCode solutions"),
        section_row("LeetCode study plans", "platforms/leetcode/study-plans", "Topic-based LeetCode practice"),
        section_row("LeetCode tracks", "platforms/leetcode/tracks", "SQL, pandas, and platform tracks"),
        section_row("CodeRun", "platforms/coderun", "CodeRun seasons and standalone tasks"),
        section_row("Contests", "contests", "Contest and selection-round submissions"),
        section_row("Learning", "learning", "Notes, handbook exercises, reusable snippets"),
        "",
        "## File Types",
        "",
    ]

    lines.extend(file_type_tables(counts))

    lines.append("")
    OUTPUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
