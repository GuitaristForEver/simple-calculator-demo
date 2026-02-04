<div align="center">
  <img src="docs/assets/logo.png" alt="Calculator Robot" width="400">

  # Simple Calculator App

  [![Tests](https://github.com/GuitaristForEver/simple-calculator/actions/workflows/tests.yml/badge.svg)](https://github.com/GuitaristForEver/simple-calculator/actions/workflows/tests.yml)
  [![codecov](https://codecov.io/gh/GuitaristForEver/simple-calculator/graph/badge.svg)](https://codecov.io/gh/GuitaristForEver/simple-calculator)
  [![CodeQL](https://github.com/GuitaristForEver/simple-calculator/actions/workflows/codeql.yml/badge.svg)](https://github.com/GuitaristForEver/simple-calculator/actions/workflows/codeql.yml)

  **A learning repository for modern CI/CD practices**

  [📚 Start Learning](guides/) | [📊 Live Demo](https://guitaristforever.github.io/simple-calculator-demo/) | [📖 Documentation](docs/)
</div>

---

## Executive Summary

> **This is a learning repository** that walks you through a clean, real-world CI/CD flow using a tiny Python calculator.

**Simple Version (ELI5)**: Think of it like a school project with a smart checklist:
1. **Developer Flow**: You make changes on your computer and run the calculator/tests.
2. **Pre-commit Hooks**: A friendly gatekeeper checks your work before it gets saved.
3. **PR Review + CI Workflows**: A robot team re-checks everything in GitHub before merge.
4. **Internal CI Tweaks**: Extra speed + reporting tricks make the robot team fast and helpful.

**Technical Version (for developers)**:
| Stage | What Happens | Tools Used |
|-------|--------------|------------|
| Developer flow | Local dev + tests before push | Python + pytest |
| Pre-commit hooks | Security + linting + formatting | pre-commit + Ruff + Gitleaks |
| PR review & CI workflows | Parallel/sequential jobs, coverage & security gates | GitHub Actions + Codecov + CodeQL + Bandit |
| Internal CI tweaks | Caching + report history + artifacts | Actions cache + Allure + GitHub Pages |

**Live Demo**: [Test Reports on GitHub Pages](https://guitaristforever.github.io/simple-calculator-demo/)

---

## Table of Contents

- [What is This?](#what-is-this)
- [The 4-Stage Learning Path](#the-4-stage-learning-path)
- [📚 Start Learning](#-start-learning)
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [Documentation](#documentation)
- [🛠️ Awesome GitHub Tools](#awesome-github-tools)
- [Contributing](#contributing)

---

## What is This?

> **An instructional repository** that teaches professional CI/CD through hands-on practice with a simple Python calculator.

### You'll Learn

✅ Python project structure and testing
✅ Pre-commit hooks for code quality
✅ GitHub Actions CI/CD pipelines
✅ Enterprise features (Allure, caching, quality gates)

**Perfect for:** Students, bootcamp grads, developers learning DevOps.

---

## The 4-Stage Learning Path

This repository teaches CI/CD in **4 progressive stages**:

```
1. Developer Flow
   → Write code locally, run tests

2. Pre-commit Hooks
   → Automatic quality checks before commits

3. CI/CD Workflows
   → Automated testing in the cloud

4. Advanced Features
   → Enterprise reporting, caching, quality gates
```

**Total learning time:** ~70 minutes

---

## 📚 Start Learning

Follow the **step-by-step guides** in order:

### Stage 1: Developer Flow (25 min)
| # | Guide | Time |
|---|-------|------|
| 1 | **[Getting Started](guides/01-getting-started.md)** | 5 min |
| 2 | **[Understanding the Code](guides/02-understanding-the-code.md)** | 10 min |
| 3 | **[Running Tests](guides/03-running-tests.md)** | 10 min |

### Stage 2: Pre-commit Hooks (10 min)
| # | Guide | Time |
|---|-------|------|
| 4 | **[Pre-commit Hooks](guides/04-pre-commit-hooks.md)** | 10 min |

### Stage 3: CI/CD Workflows (15 min)
| # | Guide | Time |
|---|-------|------|
| 5 | **[CI/CD Basics](guides/05-ci-cd-basics.md)** | 15 min |

### Stage 4: Advanced Features (20 min)
| # | Guide | Time |
|---|-------|------|
| 6 | **[Advanced Features](guides/06-advanced-features.md)** | 20 min |

👉 **[Begin with Guide 1: Getting Started](guides/01-getting-started.md)**

---

## Quick Start

For those who want to jump right in:

### Install & Run

**Option A: Using pip (traditional)**
```bash
# Install dependencies
pip install -r requirements.txt

# Run calculator
python -m src.calculator

# Run tests
pytest
```

**Option B: Using uv (modern & fast) ⚡**
```bash
# Install dependencies (creates venv automatically)
uv sync --dev

# Run calculator
uv run python -m src.calculator

# Run tests
uv run pytest
```

### Pre-commit Hooks

**Option A: Using pip**
```bash
pip install pre-commit
pre-commit install
```

**Option B: Using uv**
```bash
uv sync --dev  # Includes pre-commit
pre-commit install
```

### Allure Reports
```bash
pytest --alluredir=allure-results
allure serve allure-results
```

---

### CI/CD Learning Insights

> **This is a learning repository!** Here are key insights about CI/CD concepts demonstrated in this project.

#### Pipeline Architecture

This project demonstrates a **sophisticated 5-job pipeline** with parallel and sequential stages:

```
┌──────────────────────────────────────────────┐
│          STAGE 1: PARALLEL                   │
│      (both jobs start simultaneously)        │
└──────────────────────────────────────────────┘
        │                    │
        ▼                    ▼
   ┌─────────┐         ┌──────────┐
   │ 🔍 Lint │         │🔒Security│
   └────┬────┘         └────┬─────┘
        │                    │
        └────────┬───────────┘
                 ▼
┌──────────────────────────────────────────────┐
│          STAGE 2: SEQUENTIAL                 │
│     (each job waits for the previous)        │
└──────────────────────────────────────────────┘
                 │
                 ▼
           ┌──────────┐
           │ 🧪 Test  │
           └────┬─────┘
                │
                ▼
           ┌──────────┐
           │📊 Report │
           └────┬─────┘
                │
                ▼
           ┌──────────┐
           │🚀 Deploy │
           └──────────┘
```

<blockquote>
<h4>★ Insight: Quality + Security Gate ─────────────────────────</h4>

| Tool | Focus | Why It Matters |
|------|-------|----------------|
| **Codecov** | Code quality | "Are you testing enough?" - tracks coverage trends |
| **CodeQL** | Security | "Is your code safe?" - finds vulnerabilities automatically |

Together they form a **quality + security gate** that catches both coverage regressions and vulnerabilities before merge.
</blockquote>

---

<blockquote>
<h4>★ Insight: Why Exclude CLI Code from Coverage ────────────</h4>

```python
# These lines are excluded from coverage (standard practice):
if __name__ == "__main__":
    main()
```

**Why?**
- Interactive CLI code (`input()`, `print()`) is meant for human interaction, not unit tests
- Testing these requires mocking stdin/stdout - low value, high complexity
- The core logic (Calculator class) is what matters - and that's at 100%
- This is standard practice in Python projects (Django, Flask, etc.)
</blockquote>

---

<blockquote>
<h4>★ Insight: GitHub Copilot Code Review ─────────────────────</h4>

Custom instructions in `.github/copilot-instructions.md` tell Copilot what's important for YOUR project:

- **Without context**: Copilot reviews can be noisy with false positives
- **With instructions**: Focused reviews on what actually matters
- **Think of it as**: Giving a human reviewer onboarding docs
</blockquote>

---

<blockquote>
<h4>★ Insight: How GitHub Actions Parallelism Works ───────────</h4>

| Concept | How It Works |
|---------|--------------|
| **Parallel jobs** | Jobs without `needs:` start immediately together |
| **Sequential jobs** | Jobs with `needs: [job1, job2]` wait for ALL listed jobs |
| **Runners** | Each parallel job gets its own fresh VM |
| **Total time** | `max(parallel jobs) + sequential jobs` |

**Example from this repo:**
```yaml
# These run in PARALLEL (no needs:)
lint:
  runs-on: ubuntu-latest

security:
  runs-on: ubuntu-latest

# This waits for BOTH to complete
test:
  needs: [lint, security]  # Won't start until both finish
```
</blockquote>

---

<blockquote>
<h4>★ Insight: Caching Strategy (3x Speedup) ──────────────────</h4>

| Cache | What It Stores | Invalidates When |
|-------|---------------|------------------|
| **pip cache** | Downloaded Python packages | `requirements.txt` changes |
| **pytest cache** | Test collection data | Test files change |

**Result**: First run ~45s, subsequent runs ~15s (3x faster!)
</blockquote>

## Project Structure

```
simple-calculator/
├── guides/              # 📖 Step-by-step learning (START HERE!)
├── src/                 # 🧠 Calculator code
├── tests/               # ✅ Test code
├── docs/                # 📚 Deep-dive documentation
│   └── assets/          # 🎨 Images
├── .github/workflows/   # 🤖 CI/CD automation
└── prompts/             # 🧩 Copy-paste CI/CD prompts
```

See [`docs/STRUCTURE.md`](docs/STRUCTURE.md) for details.

---

## Documentation

### For Learners
- 📖 **[Learning Guides](guides/)** - Progressive 6-guide learning path (~70 min)

### For Deep Dives
- 🏗️ **[ARCHITECTURE.md](docs/ARCHITECTURE.md)** - Complete system overview
- 🚀 **[CI-CD.md](docs/CI-CD.md)** - CI/CD insights & best practices
- 📊 **[ALLURE.md](docs/ALLURE.md)** - Enterprise test reporting
- 🌐 **[GITHUB-PAGES.md](docs/GITHUB-PAGES.md)** - Free hosting setup
- 🧪 **[TESTING.md](docs/TESTING.md)** - pytest testing guide
- ⚡ **[UV.md](docs/UV.md)** - Fast package manager
- 🔧 **[TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md)** - Common issues

### For Your Projects
- 🧩 **[Prompts](prompts/)** - Copy-paste CI/CD setup for your repos

---

## Awesome GitHub Tools

Enhance your GitHub workflow with these helpful tools:

- 📱 **[GitHub Mobile App](https://github.com/mobile)** - Official GitHub app for iOS and Android. Manage repositories, review code, and respond to issues on the go.

- 🎨 **[GitHub Material Design Chrome Extension](https://chromewebstore.google.com/detail/material-icons-for-github/bggfcpfjbdkhfhfmkjpbhnkhnpjjeomc)** - Apply Material Design styling to GitHub's interface for a modern, polished look.

- ⚡ **[Refined GitHub](https://github.com/refined-github/refined-github)** - Browser extension that simplifies the GitHub interface and adds 200+ useful features including linkified references, reaction avatars, merge conflict fixers, and more. Available for [Chrome](https://chromewebstore.google.com/detail/refined-github/hlepfoohegkhhmjieoechaddaejaokhf) and [Firefox](https://addons.mozilla.org/en-US/firefox/addon/refined-github/).

- 🤖 **[GitHub MCP](https://github.com/github/github-mcp-server)** - Model Context Protocol server for GitHub integration, enabling AI assistants to interact with GitHub repositories, issues, and pull requests through the MCP framework.

---

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run `pytest` and `pre-commit run --all-files`
5. Submit a pull request

CI will automatically test your changes.

---

## License

This project is for educational purposes.

---

<div align="center">

### Ready to Learn?

**[👉 Start with Guide 1: Getting Started](guides/01-getting-started.md)**

Learn professional CI/CD practices through hands-on experience!

</div>
