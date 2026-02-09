# Simple Calculator Demo - Showcase Transcript

## Introduction

> "Welcome! This repository demonstrates how to build a production-grade CI/CD pipeline using a simple Python calculator. The calculator is intentionally basic — the real value is in the infrastructure around it."

---

## Part 1: The Application

> "Let's start with the calculator itself."

```bash
# Traditional approach
python -m src.calculator

# Or with uv (modern & fast)
uv run python -m src.calculator
```

> "It's a command-line calculator supporting five operations: addition, subtraction, multiplication, division, and power. Clean code with type hints and proper error handling."

**Key file:** `src/calculator.py`

```python
class Calculator:
    def add(self, a: float, b: float) -> float:
        return a + b

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def power(self, a: float, b: float) -> float:
        return a ** b
```

> "Simple, readable, and testable. That's the point."

---

## Part 2: Testing with Pytest & Allure

> "Every function has corresponding tests with an 80% coverage requirement."

```bash
# Run tests with coverage
pytest --cov=src --cov-report=term --cov-fail-under=80

# Generate Allure results
pytest --alluredir=allure-results -v
```

> "We use pytest with Allure for enterprise-grade test reporting. Tests cover all operations including edge cases like division by zero."

**Key file:** `tests/test_calculator.py`

---

## Part 3: Code Coverage & Codecov

> "Code coverage measures how much of your code is actually tested. We enforce an 80% minimum threshold."

```bash
# Run tests with coverage report
pytest --cov=src --cov-report=term-missing --cov-fail-under=80

# Generate XML for Codecov
pytest --cov=src --cov-report=xml
```

> "The `--cov-fail-under=80` flag fails the build if coverage drops below 80%. This is your quality gate."

**Sample output:**
```
---------- coverage: platform linux, python 3.9 ----------
Name                  Stmts   Miss  Cover   Missing
---------------------------------------------------
src/calculator.py        25      3    88%   45-47
---------------------------------------------------
TOTAL                    25      3    88%

Required coverage: 80%. Achieved: 88%. PASSED!
```

> "Notice we exclude the CLI code (interactive mode) from coverage. That's intentional — testing user input is complex and low value for a demo."

### Codecov Integration

> "Coverage reports are uploaded to Codecov for tracking trends over time."

```yaml
- name: Upload coverage to Codecov
  uses: codecov/codecov-action@v4
  with:
    files: ./coverage.xml
    token: ${{ secrets.CODECOV_TOKEN }}
```

> "Codecov provides a dashboard showing coverage changes per PR, historical trends, and which files need more tests."

**Badge in README:**
```markdown
[![codecov](https://codecov.io/gh/GuitaristForEver/simple-calculator-demo/graph/badge.svg)](https://codecov.io/gh/GuitaristForEver/simple-calculator-demo)
```

> "The badge shows current coverage at a glance. Green means healthy, red means attention needed."

### Why 80%?

> "100% coverage doesn't mean bug-free code. You can have 100% coverage with terrible tests. Coverage just means 'this line ran' — not 'this line is correct.'"

> "80% is a pragmatic threshold: high enough to catch regressions, low enough to avoid testing boilerplate. Teams typically choose 70-90%."

---

## Part 4: Code Quality with Ruff

> "Before code reaches the repo, it passes through Ruff — a fast Python linter."

```bash
ruff check .
ruff format --check .
```

> "Ruff handles linting, formatting, and import sorting in one tool. It's 10-100x faster than traditional Python linters."

---

## Part 5: Security Scanning

> "Security is built into the pipeline, not bolted on."

```bash
bandit -r src/           # Static security analysis
safety check             # Dependency vulnerability scan
```

> "Bandit scans for common security issues in Python code. Safety checks dependencies against known vulnerabilities. Gitleaks detects secrets via pre-commit."

---

## Part 6: Pre-commit Hooks

> "Quality gates start locally, before code is even committed."

**Key file:** `.pre-commit-config.yaml`

```bash
pre-commit run --all-files
```

> "Pre-commit hooks run Ruff, check for secrets with Gitleaks, and validate file formatting. Think of it as airport security for your code."

---

## Part 7: The CI/CD Pipeline

> "Now the main event — the GitHub Actions workflow."

**Key file:** `.github/workflows/pr.yml`

> "Our pipeline has 8 jobs organized in stages:"

### Stage 1 — Parallel Quality Gates
```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  🔍 Lint    │    │ 🔒 Security │    │  🧪 Test    │
│   (Ruff)    │    │  (Bandit)   │    │  (pytest)   │
└─────────────┘    └─────────────┘    └─────────────┘
        │                 │                  │
        └─────────────────┼──────────────────┘
                          ▼
```

> "Lint, Security, and Test run in parallel — no dependencies between them. This saves ~60 seconds compared to sequential execution."

### Stage 2 — Docker Build & Verification
```
                  ┌───────────────┐
                  │ 🔎 Check      │
                  │   Changes     │
                  └───────┬───────┘
                          │
                  ┌───────▼───────┐
                  │ 🐳 Docker     │  (skipped if no changes)
                  │    Build      │
                  └───────┬───────┘
                          │
                  ┌───────▼───────┐
                  │ 💨 Smoke      │
                  │    Test       │
                  └───────────────┘
```

> "After quality gates pass, we check if Docker-related files changed. If so, build the image and run a smoke test to verify the calculator works inside the container."

### Stage 3 — Reporting & Deployment
```
                  ┌───────────────┐
                  │ 📊 Report     │
                  │  (Allure)     │
                  └───────┬───────┘
                          │
                  ┌───────▼───────┐
                  │ 🌐 Deploy     │  (main branch only)
                  │ (GH Pages)    │
                  └───────────────┘
```

> "Reports are generated with Allure even if tests fail. On the main branch, reports deploy to GitHub Pages automatically."

---

## Part 8: Docker Support

> "The project includes a Dockerfile for containerized deployment."

```bash
# Build the image
docker build -t simple-calculator .

# Run the calculator
docker run --rm simple-calculator python -c "from src.calculator import Calculator; c = Calculator(); print(c.add(2, 3))"
```

**Key file:** `Dockerfile`

> "The CI pipeline automatically builds and smoke-tests the Docker image when Dockerfile, src/**, or requirements.txt change."

---

## Part 9: Caching for Speed

> "CI runs complete in ~2-3 minutes thanks to aggressive caching."

```yaml
- uses: actions/cache@v4
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('requirements.txt') }}
```

> "Dependencies, Allure history, and Docker layers are cached. First run: ~3 minutes. Cached runs: much faster."

---

## Part 10: GitHub Pages Deployment

> "Test reports are publicly accessible at your GitHub Pages URL."

```
https://guitaristforever.github.io/simple-calculator-demo/
```

> "Every merge to main updates the reports. Teams can review test trends, find flaky tests, and track quality over time."

---

## Part 11: GitHub Secrets Protection

> "Secrets like API tokens and credentials must never be committed to code. GitHub provides secure secret management."

### Repository Secrets

> "Secrets are stored encrypted and only exposed to workflows at runtime."

**Settings → Secrets and variables → Actions:**
```
CODECOV_TOKEN          → Coverage reporting
CLAUDE_CODE_OAUTH_TOKEN → AI code review
```

> "Secrets are masked in logs — if a workflow accidentally prints a secret, GitHub replaces it with `***`."

### Secret Scanning

> "GitHub automatically scans commits for accidentally exposed secrets."

```
┌─────────────────────────────────────────────────────┐
│  🔍 Secret Scanning                                 │
│                                                     │
│  Detects: API keys, tokens, passwords, private     │
│  keys from 100+ service providers                  │
│                                                     │
│  ✅ Enabled by default on public repos             │
│  ⚠️  Alerts repo admins when secrets are found     │
└─────────────────────────────────────────────────────┘
```

> "Combined with Gitleaks in pre-commit hooks, you have two layers of protection — local and remote."

### Push Protection

> "Push protection blocks commits containing secrets before they reach the repo."

```
$ git push origin feature-branch
remote: error: GH013: Repository rule violations found
remote:
remote: - Push cannot contain secrets
remote:   - Secret type: GitHub Personal Access Token
remote:   - Location: config.py:15
```

> "This is your last line of defense. Even if pre-commit hooks are bypassed, GitHub catches it."

---

## Part 12: Branch Protection & Rulesets

> "The main branch is sacred. No one — not even admins — should push directly to it."

### Branch Protection Rules

> "Branch protection enforces code review and passing checks before merge."

**Settings → Branches → Add rule for `main`:**

| Rule | Purpose |
|------|---------|
| Require pull request | No direct pushes to main |
| Require approvals (1+) | At least one reviewer must approve |
| Require status checks | CI must pass before merge |
| Require conversation resolution | All review comments must be resolved |
| Require signed commits | Verify commit author identity |
| Include administrators | Even admins follow the rules |

```
┌─────────────────────────────────────────────────────┐
│  🛡️ Main Branch Protection                         │
│                                                     │
│  Direct push to main?     ❌ Blocked               │
│  PR without review?       ❌ Blocked               │
│  PR with failing tests?   ❌ Blocked               │
│  PR with all checks?      ✅ Allowed               │
└─────────────────────────────────────────────────────┘
```

### Required Status Checks

> "Specify which CI jobs must pass before a PR can be merged."

**Required checks for this repo:**
```
✅ 🔍 Lint
✅ 🔒 Security
✅ 🧪 Unit Tests
```

> "If any of these fail, the merge button stays disabled. No exceptions."

### Repository Rulesets (Modern Approach)

> "Rulesets are the newer, more flexible replacement for branch protection rules."

**Settings → Rules → Rulesets → New ruleset:**

```yaml
name: Protect Main Branch
target: branch
enforcement: active
conditions:
  ref_name:
    include: ["refs/heads/main"]
rules:
  - type: pull_request
    parameters:
      required_approving_review_count: 1
      require_last_push_approval: true
  - type: required_status_checks
    parameters:
      required_checks:
        - context: "🔍 Lint"
        - context: "🔒 Security"
        - context: "🧪 Unit Tests"
  - type: non_fast_forward
    # Prevent force pushes
```

> "Rulesets can apply to multiple branches, support bypass lists for emergencies, and are easier to manage at scale."

### Why This Matters

> "Without branch protection, one bad commit can break production. With it, every change goes through the same quality gates — lint, security, tests, review."

> "This isn't bureaucracy. It's professionalism. The 5 minutes spent on review saves hours of debugging in production."

---

## Part 13: Learning Guides

> "The repository includes step-by-step learning guides in the guides/ folder."

| Stage | Guide | Time |
|-------|-------|------|
| 1 | Getting Started | 5 min |
| 2 | Understanding the Code | 10 min |
| 3 | Running Tests | 10 min |
| 4 | Pre-commit Hooks | 10 min |
| 5 | CI/CD Basics | 15 min |
| 6 | Advanced Features | 20 min |

> "Total learning time: ~70 minutes to understand professional CI/CD practices."

---

## Conclusion

> "That's the Simple Calculator Demo. A small Python calculator wrapped in production-grade CI/CD infrastructure."

**What you learned:**
1. Local development with pre-commit hooks
2. Automated testing with pytest
3. Code coverage enforcement (80% minimum) with Codecov integration
4. Enterprise reporting with Allure
5. Parallel and sequential job orchestration
6. Security scanning with Bandit, Safety, and Gitleaks
7. Docker containerization with smoke testing
8. Caching strategies for faster builds
9. Automated deployment to GitHub Pages
10. GitHub secrets protection and push protection
11. Branch protection rules and rulesets to defend main

> "Fork this repo, experiment with the workflows, and apply these patterns to your own projects. Happy building!"

---

## Quick Commands Reference

| Task | Command |
|------|---------|
| Run calculator | `python -m src.calculator` |
| Run calculator (uv) | `uv run python -m src.calculator` |
| Run tests | `pytest -v` |
| Run with coverage | `pytest --cov=src --cov-report=term-missing --cov-fail-under=80` |
| Lint code | `ruff check .` |
| Format code | `ruff format .` |
| Security scan | `bandit -r src/` |
| Pre-commit | `pre-commit run --all-files` |
| Build Docker | `docker build -t simple-calculator .` |
| Generate Allure report | `pytest --alluredir=allure-results && allure serve allure-results` |

---

## Full Pipeline Diagram

```
                    PR / Push to main
                           │
           ┌───────────────┼───────────────┐
           │               │               │
           ▼               ▼               ▼
      ┌─────────┐    ┌──────────┐    ┌─────────┐
      │ 🔍 Lint │    │🔒Security│    │ 🧪 Test │   Stage 1 (parallel)
      └────┬────┘    └────┬─────┘    └────┬────┘
           │              │               │
           └──────────────┼───────────────┘
                          ▼
                   ┌─────────────┐
                   │ 🔎 Check    │
                   │  Changes    │                  Stage 2
                   └──────┬──────┘
                          │
            (if Docker files changed)
                          │
                   ┌──────▼──────┐
                   │ 🐳 Docker   │
                   │   Build     │
                   └──────┬──────┘
                          │
                   ┌──────▼──────┐
                   │ 💨 Smoke    │
                   │   Test      │
                   └──────┬──────┘
                          │
                   ┌──────▼──────┐
                   │ 📊 Report   │                  Stage 3
                   │  (Allure)   │
                   └──────┬──────┘
                          │
               (if main branch)
                          │
                   ┌──────▼──────┐
                   │ 🌐 Deploy   │
                   │ (GH Pages)  │
                   └─────────────┘
```
