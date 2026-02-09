# Simple Calculator Demo - Showcase Transcript

## Introduction

> "Welcome! This repository demonstrates how to build a production-grade CI/CD pipeline using a simple Python calculator as the example project. The calculator is intentionally basic — the real value is in the infrastructure around it."

---

## Part 1: The Application

> "Let's start with the calculator itself."

```bash
python -m calculator.calculator
```

> "It's a simple command-line calculator supporting addition, subtraction, multiplication, and division. Clean code with type hints and proper error handling for division by zero."

**Key file:** `calculator/calculator.py`

```python
class Calculator:
    def add(self, a: float, b: float) -> float:
        return a + b

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
```

> "Simple, readable, and testable. That's the point."

---

## Part 2: Testing with Pytest & Allure

> "Every function has corresponding tests."

```bash
pytest tests/ -v
```

> "We use pytest with Allure for enterprise-grade test reporting. Tests are organized with clear descriptions and cover edge cases like division by zero."

**Key file:** `tests/test_calculator.py`

> "After tests run, Allure generates beautiful HTML reports showing pass/fail status, execution time, and historical trends."

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
bandit -r calculator/    # Static security analysis
safety check             # Dependency vulnerability scan
```

> "Bandit scans for common security issues in Python code. Safety checks dependencies against known vulnerabilities. Both run automatically on every push."

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

**Key file:** `.github/workflows/tests.yml`

> "Our pipeline has 5 jobs organized in stages:"

### Stage 1 — Parallel Quality Gates
```
┌─────────────┐    ┌─────────────┐
│    Lint     │    │  Security   │
│   (Ruff)    │    │  (Bandit)   │
└─────────────┘    └─────────────┘
```

> "Lint and Security run in parallel. If either fails, the pipeline stops."

### Stage 2 — Sequential Testing & Reporting
```
       ┌─────────────┐
       │    Test     │
       │  (pytest)   │
       └──────┬──────┘
              │
       ┌──────▼──────┐
       │   Report    │
       │  (Allure)   │
       └──────┬──────┘
              │
       ┌──────▼──────┐
       │   Deploy    │
       │ (GH Pages)  │
       └─────────────┘
```

> "Tests require 80% code coverage. Reports are generated with Allure. On the main branch, reports deploy to GitHub Pages automatically."

---

## Part 7: Caching for Speed

> "CI runs complete in ~15 seconds thanks to aggressive caching."

```yaml
- uses: actions/cache@v4
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('requirements*.txt') }}
```

> "Dependencies, Allure history, and tool caches are preserved between runs. First run: ~45 seconds. Cached runs: ~15 seconds."

---

## Part 8: GitHub Pages Deployment

> "Test reports are publicly accessible at your GitHub Pages URL."

```
https://<username>.github.io/simple-calculator-demo/
```

> "Every merge to main updates the reports. Teams can review test trends, find flaky tests, and track quality over time."

---

## Conclusion

> "That's the Simple Calculator Demo. A 50-line calculator wrapped in production-grade CI/CD infrastructure."

**What you learned:**
1. Local development with pre-commit hooks
2. Automated testing with pytest and coverage gates
3. Enterprise reporting with Allure
4. Parallel and sequential job orchestration
5. Security scanning with Bandit and Safety
6. Caching strategies for faster builds
7. Automated deployment to GitHub Pages

> "Fork this repo, experiment with the workflows, and apply these patterns to your own projects. Happy building!"

---

## Quick Commands Reference

| Task | Command |
|------|---------|
| Run calculator | `python -m calculator.calculator` |
| Run tests | `pytest tests/ -v` |
| Run with coverage | `pytest --cov=calculator --cov-report=term-missing` |
| Lint code | `ruff check .` |
| Format code | `ruff format .` |
| Security scan | `bandit -r calculator/` |
| Pre-commit | `pre-commit run --all-files` |
| Generate Allure report | `pytest --alluredir=reports/allure-results && allure serve reports/allure-results` |
