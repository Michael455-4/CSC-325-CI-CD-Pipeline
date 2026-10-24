# CSC 325 — Four-Stage CI/CD Pipeline

A small Django REST Framework backend with two API endpoints and two automated tests.

## Local setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py test --verbosity 2
python manage.py runserver
```

Visit `http://127.0.0.1:8000/api/health/` and `http://127.0.0.1:8000/api/echo/`.

## GitHub Actions

`.github/workflows/csc325_ci_cd.yml` starts on pushes to `main` and on PRs targeting `main`. Jobs run in order: **Setup → Dependencies → Test → Deploy**. `needs: test` blocks deployment when the test job fails. Deploy is only executed for a push to `main` (a feature-branch PR checks setup, dependencies and tests).

**Important:** Deploy is a simulation using an echo statement, as allowed for baseline grading. It does not serve a public application. A public running example requires a hosting provider and a real deployment step.

## Branch protection

After publishing: Settings → Rules → Rulesets → New branch ruleset → target default branch `main` → Active → Require a pull request before merging (and optionally require status checks once the workflow has run). Use a feature branch for changes.

## Video change — deliberately not included

During filming, update `api/views.py` to return `{'message': 'Hello from CSC 325!', 'version': '2.0'}` in `EchoView.get`, and update `api/tests.py` to assert `response.json()['version'] == '2.0'`. Test locally, commit on feature branch, push the branch, open a PR and merge it into protected `main`. This merge creates the required **push to main** workflow run. Do not make or push this change until you are filming.
