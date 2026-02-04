# Using uv - The Fast Package Manager ⚡

## What is uv? (Simple Version)

**Think of package managers like delivery services:**
- **pip**: The old reliable mail truck 🚚 (works, but slow)
- **uv**: A rocket ship 🚀 (does the same job, but 10-100x faster!)

`uv` is a super-fast Python package installer written in Rust. It does everything pip does, but way faster!

## Why Use uv? (Sophisticated Version)

### Speed
- **10-100x faster** than pip
- Written in Rust (compiled, not Python)
- Better dependency resolution algorithm
- Smart caching

### Modern Features
- Works with `pyproject.toml` (the modern standard)
- Better error messages
- Lockfile support (like `package-lock.json` in npm)
- Virtual environment management built-in

### Compatibility
- Drop-in replacement for pip
- All your existing commands work
- Compatible with PyPI and all packages

## Installing uv

### macOS/Linux
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Windows
```bash
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Using pip (if you prefer)
```bash
pip install uv
```

## Using uv with This Project

### Create Virtual Environment
```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### Install Dependencies
```bash
# Install development dependencies (includes pytest)
# This creates a virtual environment automatically and installs everything
uv sync --dev
```

### Install Individual Packages
```bash
# Add packages to the project
uv add pytest
uv add pytest-cov

# Or install temporarily without adding to project
uv pip install pytest  # For one-off installs
```

### Run Tests (after installing)
```bash
pytest
```

## pyproject.toml vs requirements.txt

We now have both! Here's why:

### `requirements.txt` (Old Way)
```
pytest>=7.4.0
pytest-cov>=4.1.0
```
- Simple list of packages
- Good for basic projects
- pip understands it

### `pyproject.toml` (Modern Way)
```toml
[project]
name = "simple-calculator"
dependencies = []

[project.optional-dependencies]
dev = ["pytest>=7.4.0", "pytest-cov>=4.1.0"]
```
- Complete project metadata
- Separates runtime vs dev dependencies
- Industry standard (PEP 621)
- Tool configuration in one file

**We keep both** so the project works with both old (`pip`) and new (`uv`) tools!

## Quick Command Comparison

| Task | pip | uv (modern) | uv (legacy) |
|------|-----|-------------|-------------|
| Install from pyproject.toml | `pip install -e ".[dev]"` | `uv sync --dev` | `uv pip install -e ".[dev]"` |
| Install from requirements.txt | `pip install -r requirements.txt` | `uv pip install -r requirements.txt` | Same |
| Add package | `pip install pytest` | `uv add pytest` | `uv pip install pytest` |
| Run command | `pytest` | `uv run pytest` | `pytest` (after install) |
| Create venv | `python -m venv .venv` | `uv venv` | Same |

**Modern uv approach**: Use `uv sync` for project dependencies and `uv run` for commands!

## Why This Matters for Well-Architected Software

1. **Fast CI/CD** - Your tests run faster because dependencies install faster
2. **Modern Standards** - Using `pyproject.toml` is the Python community's direction
3. **Better DX** - Developers get faster feedback
4. **Future-Proof** - Following industry trends

## What We Did

✅ Created `pyproject.toml` with all project metadata
✅ Moved pytest config from `pytest.ini` to `pyproject.toml` (less files!)
✅ Kept `requirements.txt` for backward compatibility
✅ Documented everything clearly

Now you can use either `pip` (traditional) or `uv` (modern fast way)!
