# Algorithms Practice Archive

Portfolio-oriented archive of algorithmic practice, contest submissions, SQL tasks, and study notes.

The repository is organized as a curated public archive: the original solutions are preserved, while navigation, indexes, and publication checks make the collection easier to review.

## Highlights

- 350+ LeetCode problem folders in [platforms/leetcode/tasks](platforms/leetcode/tasks)
- LeetCode study-plan solutions in [platforms/leetcode/study-plans](platforms/leetcode/study-plans)
- CodeRun and Yandex-style practice in [platforms/coderun](platforms/coderun)
- Contest submissions in [contests](contests)
- Algorithm notes and handbook exercises in [learning](learning)
- Curated portfolio entry points in [showcase](showcase)

## Repository Map

| Path | Purpose |
| --- | --- |
| [showcase](showcase) | Curated list of representative solutions for portfolio review |
| [platforms/leetcode/tasks](platforms/leetcode/tasks) | Individual LeetCode problem solutions |
| [platforms/leetcode/study-plans](platforms/leetcode/study-plans) | LeetCode quest/study-plan tasks by topic |
| [platforms/leetcode/tracks](platforms/leetcode/tracks) | LeetCode tracks such as pandas/SQL practice |
| [platforms/coderun](platforms/coderun) | CodeRun seasons and standalone tasks |
| [contests](contests) | Contest and selection-round submissions |
| [learning](learning) | Notes, handbook exercises, reusable snippets |
| [docs](docs) | Generated indexes and publication notes |
| [scripts](scripts) | Repository maintenance scripts |

## Generated Index

Run:

```bash
python3 scripts/generate_index.py
```

This writes [docs/INDEX.md](docs/INDEX.md) with current counts and directory summaries.

## Publication Notes

See [docs/PUBLICATION_AUDIT.md](docs/PUBLICATION_AUDIT.md) for the current cleanup policy and remaining manual review items.

The solutions themselves are intentionally left close to their original submission form. Showcase entries point to selected tasks without rewriting archived code.
