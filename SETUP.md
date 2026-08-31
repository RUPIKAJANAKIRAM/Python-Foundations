# Setup — do this once, today

Estimated time: 45–60 minutes. Follow top to bottom. Don't research anything; every
decision is already made below.

---

## 1. Local environment

```bash
# check you have Python 3.11 or newer
python3 --version

# put this folder where you keep code, then:
cd python-foundations

# create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

# install the project in editable mode, with dev tools
pip install -e ".[dev]"

# confirm it works
python -m pytest
```

You should see 3 passing tests. If you do, the environment is correct.

---

## 2. Git + GitHub

```bash
git init
git add .
git commit -m "chore: scaffold python foundations repo"
git branch -M main
```

Now create an **empty public repo** on GitHub named `python-foundations`
(no README, no .gitignore — the scaffold already has them), then:

```bash
git remote add origin https://github.com/<your-username>/python-foundations.git
git push -u origin main
```

Go to the **Actions** tab on GitHub. The CI workflow should run and go green
within about a minute. That green check is your Day 1 milestone.

---

## 3. The branch workflow you'll use every day

From now on, nothing goes straight to `main`. Every topic gets a branch and a PR
— to yourself. This feels silly for a solo repo and it is exactly the point:
you're building the muscle memory, and the PR history becomes visible evidence
of how you work.

```bash
git checkout -b feat/two-pointers
# ... write code, write tests ...
pytest
git add .
git commit -m "feat: two-pointer pattern with tests"
git push -u origin feat/two-pointers
```

Then on GitHub: open the PR, wait for CI to pass, write two sentences in the
description about what you learned, merge, delete the branch. Locally:

```bash
git checkout main
git pull
git branch -d feat/two-pointers
```

Commit message prefixes, so the log stays readable: `feat:` `fix:` `test:`
`docs:` `refactor:` `chore:`

---

## 4. Tools, decided for you

| Need | Use | Why |
|---|---|---|
| Editor | VS Code + Python extension | You already use Copilot in it |
| Formatter + linter | `ruff` (already configured) | One tool instead of black + flake8 + isort |
| Testing | `pytest` (already configured) | Standard everywhere |
| Env | `venv` | Boring, built in, zero setup tax |
| CI | GitHub Actions (already configured) | Already in the scaffold |

Run `ruff check . --fix` and `ruff format .` before every commit. CI will fail
you if you forget, which is the point.

---

## 5. Where your progress lives

`PROGRESS.md` in this repo is the single source of truth. Not a note app, not
your head. It's version controlled, it's in the same place as the work, and its
commit history is itself a record of consistency.

Update it every Sunday. Paste it into our check-in chat.
