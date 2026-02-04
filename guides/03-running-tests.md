# Guide 3: Running Tests 🧪

**Your code works... but how do you KNOW it works?** Let's test it!

---

## What You'll Learn

In this guide, you'll:
1. ✅ Understand what tests are and why they matter
2. ✅ Run tests with pytest
3. ✅ Read test reports

**Time needed**: 10 minutes

---

## What Are Tests? (Simple Version)

Think of tests as a **quality checklist**:
- Does `add(2, 3)` return `5`? ✅
- Does `divide(10, 0)` raise an error? ✅
- Do all operations work correctly? ✅

Tests **automatically check** if your code does what it should!

---

## Why Test?

### Without Tests:
1. You make a change
2. Hope it doesn't break anything
3. 😰 Discover bugs later
4. Debug for hours

### With Tests:
1. You make a change
2. Run tests (1 second)
3. ✅ All green = You're safe!
4. ❌ Something red = Fix before it's a problem

**Tests save you time and headaches!**

---

## Running Your First Test

### Quick Test

```bash
pytest
```

That's it! You'll see:

```
==================== test session starts ====================
collected 5 items

tests/test_calculator.py .....                        [100%]

==================== 5 passed in 0.12s ====================
```

**What this means:**
- ✅ 5 tests ran
- ✅ All passed
- ✅ Took 0.12 seconds

---

## What Just Happened?

pytest found `tests/test_calculator.py` and ran all tests inside. Let's look at one:

```python
def test_add(calc):
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0
```

**Reading this:**
- "Test that add() works correctly"
- Check: `2 + 3 = 5` ✅
- Check: `-1 + 1 = 0` ✅
- Check: `0 + 0 = 0` ✅

If any assertion fails, pytest tells you!

---

## More Test Options

### Verbose Output
See each test by name:
```bash
pytest -v
```

Output:
```
tests/test_calculator.py::test_add PASSED
tests/test_calculator.py::test_subtract PASSED
tests/test_calculator.py::test_multiply PASSED
tests/test_calculator.py::test_divide PASSED
tests/test_calculator.py::test_divide_by_zero PASSED
```

### With Coverage
See which code is tested:
```bash
pytest --cov
```

Output:
```
---------- coverage: platform darwin, python 3.9.7 -----------
Name                       Stmts   Miss  Cover
----------------------------------------------
src/__init__.py         1      0   100%
src/calculator.py      20      5    75%
----------------------------------------------
TOTAL                         21      5    76%
```

**Reading this:** 76% of your code is tested!

---

## Understanding Test Reports

After running `pytest`, check `reports/test-report.html`:

```bash
open reports/test-report.html
```

**You'll see:**
- ✅ Which tests passed (green)
- ❌ Which tests failed (red)
- ⏱️ How long each test took
- 📊 Summary statistics

This is helpful for seeing the big picture!

---

## The 5 Tests Explained

Our calculator has 5 tests:

| Test | What It Checks |
|------|----------------|
| `test_add` | Addition works with positive, negative, and zero |
| `test_subtract` | Subtraction works correctly |
| `test_multiply` | Multiplication works correctly |
| `test_divide` | Division returns correct decimal results |
| `test_divide_by_zero` | Division by zero raises an error (safety!) |

---

## pytest vs unittest

**Why pytest?** It's simpler!

### Old Way (unittest):
```python
import unittest

class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        self.assertEqual(calc.add(2, 3), 5)
```

### New Way (pytest):
```python
def test_add(calc):
    assert calc.add(2, 3) == 5
```

**Much cleaner!** That's why professional projects use pytest.

---

## Try It Yourself!

### Challenge 1: Break a Test
1. Open `src/calculator.py`
2. Change `return a + b` to `return a - b` in the `add` method
3. Run `pytest`
4. See the test fail! 🔴
5. Fix it back and tests pass ✅

### Challenge 2: Watch Test Output
Run with more detail:
```bash
pytest -v --tb=short
```

This shows:
- `-v` = verbose (see each test name)
- `--tb=short` = short error messages

---

## Key Takeaways

1. **Tests = Automated quality checks**
2. **pytest makes testing simple**
3. **Run tests after every change**
4. **Green tests = Confidence**

This is how **professional developers** ensure code quality! 🎯

---

## ✅ You Did It!

You just:
- ✅ Ran automated tests
- ✅ Understood pytest output
- ✅ Saw test reports

**Next Step**: [Guide 4: Pre-commit Hooks](04-pre-commit-hooks.md)
Learn how to run checks automatically before every commit!

---

**Navigation**:
- ⬅️ Previous: [Guide 2: Understanding the Code](02-understanding-the-code.md)
- ➡️ Next: [Guide 4: Pre-commit Hooks](04-pre-commit-hooks.md)
- 🏠 Back to [README](../README.md)
