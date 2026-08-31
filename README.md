# python-foundations

Python idioms and classic data structures, implemented from scratch with tests,
complexity analysis, and CI. Part of a six-month structured upskilling programme
moving from backend engineering into AI engineering.

## Why this repo exists

I've written production backend code in Java and C# for years. This repo is where
I rebuilt the same fundamentals in Python — not to learn what a hash map is, but to
learn how Python wants me to express it, and to work in a disciplined way while
doing it: branch per topic, PR per change, tests on everything, green CI.

## Structure

```
src/dsa/        implementations, one module per pattern
tests/          pytest suite, one file per module
notes/          short write-ups of what each pattern is actually for
```

## Running it

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

## Conventions

- Every function: docstring with approach, time complexity, space complexity.
- Every function: full type hints.
- Every module: happy path, edge case, and failure case tests.
- Nothing merges to `main` without green CI.

## Progress

See [PROGRESS.md](PROGRESS.md).
