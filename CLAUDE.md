# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an **educational CI/CD demonstration repository** that teaches professional CI/CD practices through a simple Python calculator. The codebase is intentionally minimal to focus on CI/CD concepts rather than application complexity.

**Purpose**: Learning repository demonstrating:
- Python project structure and testing
- Pre-commit hooks for code quality
- GitHub Actions CI/CD pipelines
- Enterprise features (Allure reporting, caching, quality gates)

## Development Commands

### Testing

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=src --cov-report=term --cov-report=xml

# Run tests with Allure reporting
pytest --alluredir=allure-results

# View Allure reports locally
allure serve allure-results

# Run a specific test file
pytest tests/test_calculator.py

# Run a specific test function
pytest tests/test_calculator.py::test_add
```

### Code Quality

```bash
# Run all pre-commit hooks
pre-commit run --all-files

# Run specific hook
pre-commit run ruff
pre-commit run ruff-format

# Install pre-commit hooks (one-time setup)
pre-commit install

# Security scanning
bandit -r src/
safety check -r requirements.txt
```

### Running the Calculator

```bash
# Using pip
python -m src.calculator

# Using uv (faster alternative)
uv run python -m src.calculator
```

### Installing Dependencies

```bash
# Option A: Traditional pip
pip install -r requirements.txt

# Option B: Modern uv (recommended)
uv sync --dev
```

### Docker

```bash
# Build Docker image
docker build -t simple-calculator:latest .

# Run inside container
docker run --rm simple-calculator:latest python -c "from src.calculator import Calculator; c = Calculator(); print(c.add(2, 3))"
```

## Project Architecture

### Core Structure

```
src/calculator.py         - Calculator class with basic arithmetic operations
tests/test_calculator.py  - Comprehensive pytest tests with Allure decorators
```

### CI/CD Pipeline Architecture

The `.github/workflows/pr.yml` pipeline implements an **8-job workflow** with two execution stages:

**Stage 1: Parallel Quality Gates** (simultaneous execution)
- `lint` - Ruff linting and formatting checks
- `security` - Bandit and Safety vulnerability scanning
- `test` - pytest with coverage (80% threshold) and Allure reporting

**Stage 2: Sequential Build & Deploy** (executes after Stage 1 passes)
- `check-changes` - Path filtering to detect Docker-related changes
- `docker-build` - Conditional Docker image build (only if Dockerfile/src/requirements.txt changed)
- `smoke-test` - Validates Docker image works correctly
- `report` - Generates Allure HTML reports with historical trends
- `deploy` - Publishes to GitHub Pages (main branch only)

**Key Design Patterns**:
- **Parallel execution** for independent jobs saves ~60 seconds vs sequential
- **Path filtering** skips Docker builds when unnecessary (saves ~90 seconds)
- **Caching strategies**: pip cache (~3x speedup), Docker layer cache (~4x speedup)
- **Always-run reporting**: Test reports generate even if tests fail (`if: always()`)
- **Conditional deployment**: PRs are tested but not deployed; only main branch deploys

### Testing Architecture

**Testing Framework**: pytest with Allure decorators
- All tests use fixtures (`@pytest.fixture`) for clean test isolation
- Allure decorators provide enterprise-level reporting with:
  - Feature/Story organization (`@allure.feature`, `@allure.story`)
  - Severity levels (`@allure.severity`)
  - Step-by-step test visualization (`with allure.step()`)
- Coverage configuration in `pyproject.toml` excludes CLI code (standard practice)

**Coverage Exclusions**: The interactive `main()` function is intentionally excluded from coverage (standard practice for CLI code that requires human interaction).

### Pre-commit Hooks

Configuration in `.pre-commit-config.yaml`:
- **Security**: Gitleaks (secrets detection), detect-private-key
- **Python Quality**: Ruff (linting + formatting), isort (import sorting)
- **File Validation**: YAML/JSON/TOML syntax, trailing whitespace, line endings
- **Safety Checks**: Large file detection, merge conflict markers

## Code Quality Standards

### Python Code Style

- **Type hints required**: All public methods must have type annotations
- **Docstrings required**: All public methods and classes must have docstrings
- **Error handling**: Explicit ValueError for invalid operations (e.g., division by zero)
- **PEP 8 compliance**: Enforced via Ruff
- **Import sorting**: Enforced via isort with black profile

### Testing Standards

- **Test coverage**: Minimum 80% coverage enforced by CI (`--cov-fail-under=80`)
- **Test naming**: Follow `test_*` pattern
- **Allure decorators**: All tests should include `@allure.feature`, `@allure.story`, and `@allure.severity`
- **Test steps**: Use `with allure.step()` for multi-step test visualization
- **Edge cases required**: Tests must cover positive, negative, and zero cases

### What NOT to Flag

- The `main()` function is intentionally excluded from test coverage (CLI code)
- Simple print statements in demo code are acceptable
- This is an educational project - avoid over-engineering suggestions

## Git Workflow

- **Main branch**: `main` (not master)
- **CI triggers**: Runs on push to main, PRs to main, and manual dispatch
- **Deployment**: Only main branch deploys to GitHub Pages
- **Branch protection**: All quality gates must pass before merge

## GitHub Actions Secrets

Required secrets for full CI/CD functionality:
- `CODECOV_TOKEN` - For coverage tracking on codecov.io

## Important Constraints

1. **Keep it simple**: This is an educational repository - resist adding complex features
2. **Preserve CI/CD focus**: Any code changes should maintain the CI/CD teaching value
3. **Documentation first**: Changes to CI/CD workflows require corresponding guide updates
4. **No over-engineering**: Don't add abstractions, helpers, or features beyond the demo scope

## Testing Notes

- Tests use the `allure-pytest` plugin for enhanced reporting
- Coverage reports exclude interactive CLI code (standard practice)
- The Calculator class has 100% test coverage for all operations
- Test results are published to GitHub Pages with historical trends

## Related Documentation

- `README.md` - Main learning guide and project overview
- `guides/` - Step-by-step learning guides (6 guides, ~70 minutes total)
- `docs/reference/ARCHITECTURE.md` - Complete system architecture
- `docs/ci-cd/CI-CD.md` - CI/CD concepts and best practices
- `.github/copilot-instructions.md` - Code review guidelines
