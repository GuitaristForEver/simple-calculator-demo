# Testing with pytest 🧪

## Why pytest?

**Simple Version**: pytest is like the "easy mode" of testing - less typing, clearer results, more fun!

**Before (unittest)**:
```python
class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(2, 3), 5)
```

**After (pytest)**:
```python
def test_add(calc):
    assert calc.add(2, 3) == 5
```

Way simpler! No classes, no `self.assertEqual`, just plain Python!

## Why pytest is Better (The Sophisticated Version)

### 1. Simpler Syntax
- Uses plain `assert` instead of `self.assertEqual()`, `self.assertTrue()`, etc.
- No need for test classes (but you can use them if you want)
- Easier to read, easier to write

### 2. Better Fixtures
- `@pytest.fixture` for setup/teardown
- Automatically injected into test functions
- Reusable across tests

### 3. Better Output
- Shows you the actual values when tests fail
- Colorful terminal output
- Clear progress indicators

### 4. More Features
- **Parametrization** - Run same test with different inputs
- **Coverage reports** - See what code is tested
- **Plugins** - Tons of extensions available
- **Markers** - Tag and filter tests easily

## Running Tests

### Basic
```bash
pytest                 # Run all tests
pytest tests/          # Run specific folder
pytest -v              # Verbose (show each test)
```

### With Coverage
```bash
pytest --cov           # Show coverage
pytest --cov-report=html  # Generate HTML report
```

### Selecting Tests
```bash
pytest -k "add"        # Run tests matching "add"
pytest tests/test_calculator.py::test_add  # Run specific test
```

## Our Test Structure

```python
@pytest.fixture
def calc():
    """Create calculator for each test."""
    return Calculator()

def test_add(calc):
    """The 'calc' argument is automatically provided by pytest!"""
    assert calc.add(2, 3) == 5
```

**Why fixtures?** They're like having a robot that sets things up before each test and cleans up after. No manual work needed!

## Configuration

We have `pytest.ini` that sets defaults:
- Where to find tests (`tests/` folder)
- How to display results (verbose, colorful)
- What to name test files (`test_*.py`)

This means you just run `pytest` and it knows what to do!
