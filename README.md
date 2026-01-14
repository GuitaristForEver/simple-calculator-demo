<div align="center">
  <img src="assets/logo.png" alt="Calculator Robot" width="400">
  
  # Simple Calculator App
  
  A basic Python calculator to demonstrate simple CI/CD concepts with GitHub Actions.
</div>

## Features

- Basic arithmetic operations (add, subtract, multiply, divide)
- Interactive mode for user input
- Automated testing with CI/CD
- Simple and clean codebase

## How It Works (The Simple Version)

Think of the calculator like a **helper robot**. You tell it what to do (add, subtract, multiply, or divide), give it two numbers, and it gives you the answer back.

**Under the Hood**: The calculator is built using a `Calculator` class that keeps all the math operations organized in one place. Each operation is a separate method that knows exactly how to do its job. When you divide by zero, it politely stops you because that would break math!

## Architecture

Here's how the pieces fit together:

```mermaid
flowchart TD
    User[You] -->|Give numbers + operation| Calculator
    Calculator -->|Returns answer| User
    
    subgraph CalculatorBrain[Calculator Brain]
        Add[Add Numbers]
        Subtract[Subtract Numbers]
        Multiply[Multiply Numbers]
        Divide[Divide Numbers]
        SafetyCheck[Division Safety Check]
    end
    
    Calculator --> CalculatorBrain
    Divide --> SafetyCheck
```

**What This Means**: 
- You give the calculator two numbers and tell it what to do
- The calculator has a "brain" (the Calculator class) with different skills
- Each skill does one thing really well
- The division skill has a safety check to prevent math errors

## Feature Tracker

This table shows what the calculator can do and explains each feature simply:

| Feature | Simple Explanation | Tech Details | Status |
|---------|-------------------|--------------|--------|
| **Add** | Puts two numbers together (5 + 3 = 8) | `add(a, b)` returns `a + b` | ✅ Done |
| **Subtract** | Takes one number away from another (10 - 4 = 6) | `subtract(a, b)` returns `a - b` | ✅ Done |
| **Multiply** | Adding a number to itself many times (3 × 4 = 12) | `multiply(a, b)` returns `a * b` | ✅ Done |
| **Divide** | Splitting a number into equal parts (15 ÷ 3 = 5) | `divide(a, b)` returns `a / b` | ✅ Done |
| **Division Safety** | Won't let you divide by zero (that breaks math!) | Raises `ValueError` if `b == 0` | ✅ Done |
| **Interactive Mode** | Type in your own math problems | Command-line interface with input prompts | ✅ Done |
| **pytest Testing** | Modern test framework with simple syntax | 5 test cases using `pytest` with fixtures | ✅ Done |
| **AI Instructions** | Helps AI assistants understand the project rules | `.copilot-instructions.md` with project guidelines | ✅ Done |
| **Logo** | A friendly calculator robot mascot | Image in `assets/logo.png` displayed at top of README | ✅ Done |
| **Git Ignore** | Keeps temporary and personal files out of Git | `.gitignore` blocks Python cache, IDE settings, etc. | ✅ Done |
| **Main Branch** | Uses "main" instead of "master" for the default branch | Modern Git convention, set via GitHub CLI | ✅ Done |
| **Folder Structure** | Organized folders for code, tests, docs, and assets | Professional package layout: `calculator/`, `tests/`, `docs/`, `assets/` | ✅ Done |
| **uv Support** | Modern fast package manager (10-100x faster than pip!) | `pyproject.toml` for modern Python packaging | ✅ Done |
| **Test Reports** | Pretty HTML reports after running tests | Auto-generated in `reports/` folder (git-ignored) | ✅ Done |
| **Allure Reporting** | Enterprise test reporting with trends & history | Track test quality over time, detect flaky tests | ✅ Done |
| **CI/CD Pipeline** | GitHub Actions automatically runs tests & publishes reports | History stored in gh-pages, reports at GitHub Pages URL | ✅ Done |

## Quick Start

### Install Dependencies

**Using pip (traditional)**:
```bash
pip install -r requirements.txt
```

**Using uv (modern & fast)** ⚡:
```bash
uv pip install -e ".[dev]"
```

> **What's uv?** A super-fast Python package manager (10-100x faster than pip!). See [`docs/UV.md`](docs/UV.md) for details.

### Run the Calculator

```bash
python -m calculator.calculator
```

This will show a demo and then enter interactive mode where you can perform calculations.

### Run Tests

**Quick test** (pytest-html):
```bash
pytest
```

**Enterprise reporting** (Allure with trends):
```bash
pytest --alluredir=allure-results
allure serve allure-results
```

For more options:
```bash
pytest -v              # Verbose output
pytest --cov           # With coverage report
```

After running tests, check `reports/test-report.html` for a quick visual report!  
Or use Allure for enterprise-level reporting with trends 📊  

**Automated CI/CD**: Every push to `main` automatically runs tests and publishes Allure reports to GitHub Pages with history tracking!  
See [`docs/ALLURE.md`](docs/ALLURE.md) and [`docs/CI-CD.md`](docs/CI-CD.md) for details.

## Usage Examples

### Basic Operations

```python
from calculator import Calculator

calc = Calculator()

# Addition
result = calc.add(5, 3)        # Returns: 8

# Subtraction  
result = calc.subtract(10, 4)  # Returns: 6

# Multiplication
result = calc.multiply(6, 7)   # Returns: 42

# Division
result = calc.divide(15, 3)    # Returns: 5.0
```

### Interactive Mode

When you run `python calculator.py`, you'll see:

```
Simple Calculator Demo
======================
5 + 3 = 8
10 - 4 = 6
6 * 7 = 42
15 / 3 = 5.0

Interactive Mode (type 'quit' to exit):
Enter operation (add/subtract/multiply/divide): add
Enter first number: 10
Enter second number: 5
Result: 15.0
```

## CI/CD Pipeline

This project uses GitHub Actions for continuous integration:

- **Automated Testing**: Runs unit tests on every push and pull request
- **Multi-Python Support**: Tests against Python 3.8, 3.9, 3.10, and 3.11
- **Simple Workflow**: Just pushes trigger the pipeline automatically

## Project Structure

```
.
├── calculator/              # 🧠 Calculator app package
│   ├── __init__.py         # Makes it a Python package
│   └── calculator.py       # Calculator class and logic
├── tests/                   # ✅ All test files
│   └── test_calculator.py  # Calculator unit tests
├── docs/                    # 📚 Documentation
│   ├── STRUCTURE.md        # Folder structure explained
│   ├── TESTING.md          # pytest guide
│   ├── UV.md               # Modern package management
│   ├── ALLURE.md           # Enterprise test reporting
│   └── CI-CD.md            # GitHub Actions automation
├── .github/
│   └── workflows/
│       └── tests.yml       # Automated testing with Allure
├── assets/                  # 🎨 Images and media
│   └── logo.png            # Calculator robot logo
├── reports/                 # 📊 Test reports (auto-generated, git-ignored)
│   ├── test-report.html    # HTML test report
│   └── junit.xml           # JUnit XML report for CI/CD
├── .copilot-instructions.md # 🤖 AI guidance
├── .gitignore              # 🚫 Git ignore rules
├── pyproject.toml          # 📋 Modern project config (uv, pytest, metadata)
├── pytest.ini              # ⚙️  pytest configuration (legacy)
├── requirements.txt        # 📦 Python dependencies (pip compatible)
└── README.md               # 👋 This file
```

**Why this structure?** Each type of file has its own home - code, tests, docs, and media are all separated. Makes it easy to find things as the project grows! See [`docs/STRUCTURE.md`](docs/STRUCTURE.md) for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run the tests: `pytest`
5. Submit a pull request

The CI pipeline will automatically run tests on your pull request.

## License

This project is for educational purposes.