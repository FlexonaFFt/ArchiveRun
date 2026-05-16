# Publication Audit

This repository has been reorganized for public review without changing solution code.

## Done

- Moved platform-specific material under `platforms/`.
- Moved contest submissions under `contests/`.
- Moved notes and learning material under `learning/`.
- Added `showcase/` as a curated portfolio entry point.
- Added `docs/` and `scripts/` for generated indexes and maintenance checks.
- Removed IDE and macOS artifacts from git tracking.
- Expanded `.gitignore` for virtual environments, caches, local run files, and common private/binary artifacts.

## Manual Review Before Publishing

Review these tracked file types before making the repository public:

| Type | Why review |
| --- | --- |
| `.csv` | May contain contest datasets or generated statistics |
| `.db`, `.sqlite` | May contain local databases or private task data |
| `.docx` | May contain original statements or private contest materials |
| `.ipynb` | May contain outputs, paths, tokens, or personal notes |
| `.pt`, `.pkl` | Usually binary model/data artifacts, rarely useful in a portfolio archive |
| `input.txt`, `test.txt`, `read.txt` | Often local scratch inputs rather than reusable documentation |

Use:

```bash
python3 scripts/check_public_ready.py
```

## Scope Boundary

The refactor deliberately preserves archived solution files. Future cleanup should prefer:

- adding README files around selected solutions;
- adding tests only for showcase entries;
- documenting complexity and approach in separate markdown files;
- avoiding edits to historical contest submissions unless a task is promoted into `showcase/`.
