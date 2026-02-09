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

## Part 3: Code Quality with Ruff

> "Before code reaches the repo, it passes through Ruff — a fast Python linter."

```bash
ruff check .
ruff format --check .
```

> "Ruff handles linting, formatting, and import sorting in one tool. It's 10-100x faster than traditional Python linters."

---

## Part 4: Security Scanning

> "Security is built into the pipeline, not bolted on."

```bash
bandit -r src/           # Static security analysis
safety check             # Dependency vulnerability scan
```

> "Bandit scans for common security issues in Python code. Safety checks dependencies against known vulnerabilities. Gitleaks detects secrets via pre-commit."

---

## Part 5: Pre-commit Hooks

> "Quality gates start locally, before code is even committed."

**Key file:** `.pre-commit-config.yaml`

```bash
pre-commit run --all-files
```

> "Pre-commit hooks run Ruff, check for secrets with Gitleaks, and validate file formatting. Think of it as airport security for your code."

---

## Part 6: The CI/CD Pipeline

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

## Part 7: Docker Support

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

## Part 8: Caching for Speed

> "CI runs complete in ~2-3 minutes thanks to aggressive caching."

```yaml
- uses: actions/cache@v4
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('requirements.txt') }}
```

> "Dependencies, Allure history, and Docker layers are cached. First run: ~3 minutes. Cached runs: much faster."

---

## Part 9: GitHub Pages Deployment

> "Test reports are publicly accessible at your GitHub Pages URL."

```
https://guitaristforever.github.io/simple-calculator-demo/
```

> "Every merge to main updates the reports. Teams can review test trends, find flaky tests, and track quality over time."

---

## Part 10: Learning Guides

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
2. Automated testing with pytest and coverage gates (80% minimum)
3. Enterprise reporting with Allure
4. Parallel and sequential job orchestration
5. Security scanning with Bandit, Safety, and Gitleaks
6. Docker containerization with smoke testing
7. Caching strategies for faster builds
8. Automated deployment to GitHub Pages

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
