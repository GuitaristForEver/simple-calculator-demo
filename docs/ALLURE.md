# Allure Test Reporting 🎯

## What is Allure? (Simple Version)

Imagine test reports like photos vs movies:
- **pytest-html**: Takes a snapshot photo 📸 of your tests right now
- **Allure**: Records a movie 🎬 showing how your tests change over time!

Allure is an **enterprise-level test reporting framework** used by companies like Google, Microsoft, and Netflix to track test quality over time.

---

## 🆕 Allure 3 - The Next Generation

**This project uses Allure 3** - the completely rewritten version with:
- ✨ **New "Awesome" UI** - Beautiful, modern interface
- 🚀 **TypeScript rewrite** - Faster and more extensible
- 📦 **npm/npx install** - No Java needed!
- 🔌 **Plugin system** - Customizable reports
- 👀 **Real-time watching** - See results as tests run

### Allure 3 vs Allure 2

| Feature | Allure 2 | Allure 3 |
|---------|----------|----------|
| **Install** | Java + brew/scoop | `npx allure` |
| **Language** | Java | TypeScript |
| **UI** | Classic | Awesome (modern) |
| **Single file output** | ❌ | ✅ Option |
| **Watch mode** | ❌ | ✅ Live updates |
| **Plugin system** | Limited | ✅ Extensible |

📚 **Official repo**: https://github.com/allure-framework/allure3

---

## Why Allure? (For This Demo Project)

This calculator demonstrates **well-architected software**:
- 🎯 **Simple outside**: Just 5 basic math operations
- 🚀 **Sophisticated inside**: Enterprise-grade testing infrastructure

Allure shows professional practices:
- 📊 Track test trends over time
- 🔍 Detect flaky tests (unstable tests)
- ⏱️ Monitor test performance
- 🎨 Beautiful visual reports

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
# or
uv pip install -e ".[dev]"
```

### 2. Run Tests with Allure
```bash
pytest --alluredir=allure-results
```

### 3. Generate and View Report (Allure 3)
```bash
# Generate report
npx allure generate allure-results

# Open in browser
npx allure open allure-report/awesome
```

Or use the one-liner:
```bash
npx allure run -- pytest
```

A browser will open with your beautiful test report! 🎉

## Allure 3 Commands Cheat Sheet

```bash
# Run tests and generate report in one command
npx allure run -- pytest

# Generate report from existing results
npx allure generate allure-results

# Open the generated report
npx allure open allure-report/awesome

# Watch mode - live updates as tests run
npx allure watch allure-results
```

## Configuration (allurerc.mjs)

Allure 3 uses a config file in your project root:

```javascript
// allurerc.mjs
import { defineConfig } from "allure";

export default defineConfig({
  name: "Simple Calculator - Test Report",
  output: "./allure-report",
  plugins: {
    awesome: {
      options: {
        singleFile: false,       // Full report or single HTML
        reportLanguage: "en",    // UI language
      },
    },
  },
});
```

---

## What You Get

### 📊 Overview Dashboard
```
Total Tests: 5
✅ Passed: 5
❌ Failed: 0
⏭️  Skipped: 0
⏱️  Duration: 0.15s
```

### 🎯 Test Categories
- **Calculator Operations**: All tests organized by feature
- **Severity Levels**: Critical operations marked
- **Test Status**: Visual pass/fail indicators

### ⏱️ Duration Tracking
See which tests are slow:
```
test_add:      0.001s  🟢 Fast
test_divide:   0.002s  🟢 Fast
test_multiply: 0.001s  🟢 Fast
```

### 📈 Historical Trends (After Multiple Runs)

**Success Rate Over Time**:
```
100%  ●─────●─────●─────●
 90%
 80%
      Run1  Run2  Run3  Run4
```

**Duration Trends**:
```
Test Suite Duration:
0.20s  
0.15s  ●─────●─────●
0.10s
       Run1  Run2  Run3
```

## How to See Trends

Trends appear after running tests **multiple times**. Here's how:

### First Run
```bash
pytest --alluredir=allure-results
npx allure generate allure-results
```
Result: Beautiful report, but no trends yet (only 1 data point)

### Second Run (Next Day or After Code Changes)
```bash
# Preserve history
cp -r allure-report/awesome/history allure-results/history

# Run tests again
pytest --alluredir=allure-results

# Generate with history
npx allure generate allure-results

# Open report
npx allure open allure-report/awesome
```

Now you'll see:
- ✅ Trend graphs comparing runs
- 📊 Success rate over time
- ⏱️ Performance changes
- 🔍 Flaky test detection

## Advanced Features

### 🏷️ Test Categories

Tests are organized by feature:
```python
@allure.feature("Basic Operations")
@allure.story("Addition")
def test_add(calc):
    assert calc.add(2, 3) == 5
```

### 🚨 Severity Levels

Critical tests are marked:
```python
@allure.severity(allure.severity_level.CRITICAL)
def test_divide_by_zero(calc):
    with pytest.raises(ValueError):
        calc.divide(5, 0)
```

### 📝 Test Documentation

Rich descriptions in reports:
```python
@allure.description("""
Test that addition works correctly with:
- Positive numbers
- Negative numbers
- Zero
""")
def test_add(calc):
    # ...
```

### 📸 Screenshots & Attachments

Can attach files to test reports:
```python
@allure.attach("Debug info", attachment_type=allure.attachment_type.TEXT)
def test_something():
    # ...
```

## Allure vs pytest-html

| Feature | pytest-html | Allure |
|---------|-------------|--------|
| **Current run report** | ✅ Simple | ✅ Detailed |
| **Historical trends** | ❌ No | ✅ Yes |
| **Flaky detection** | ❌ No | ✅ Yes |
| **Duration tracking** | ❌ No | ✅ Yes |
| **Test categories** | ❌ No | ✅ Yes |
| **Screenshots** | Limited | ✅ Full support |
| **CI/CD integration** | Basic | ✅ Rich |
| **Visual beauty** | Good | ✅ Excellent |
| **Setup complexity** | Simple | More steps |

## CI/CD Integration

### GitHub Actions with Allure 3
```yaml
- name: Set up Node.js
  uses: actions/setup-node@v4
  with:
    node-version: '20'

- name: Run tests with Allure
  run: pytest --alluredir=allure-results

- name: Generate Allure 3 Report
  run: npx allure generate allure-results

- name: Upload Allure Report
  uses: actions/upload-pages-artifact@v3
  with:
    path: allure-report/awesome
```

## Folder Structure

```
.
├── allurerc.mjs               # Allure 3 configuration
├── allure-results/            # Raw test data (JSON)
│   ├── test-result-1.json
│   ├── test-result-2.json
│   └── history/               # Copied from previous run
├── allure-report/             # Generated reports
│   └── awesome/               # Allure 3 "Awesome" UI
│       ├── index.html
│       └── history/
└── reports/                   # pytest-html reports
    └── test-report.html
```

## Why Both pytest-html AND Allure?

**pytest-html**: Quick, simple, instant feedback (1 command)  
**Allure**: Professional, detailed, trends (uses npx)

Use **pytest-html** for quick checks during development.  
Use **Allure** for demos, presentations, and tracking quality over time.

## Pro Tips

1. **Keep history between runs** to see trends
2. **Use decorators** to organize tests (@allure.feature, @allure.story)
3. **Mark critical tests** with severity levels
4. **Run regularly** to build up historical data
5. **Try watch mode** for real-time feedback: `npx allure watch allure-results`

## The Sophistication

This demonstrates **professional software engineering**:
- ✅ Enterprise tools for a simple calculator
- ✅ "Simple outside, sophisticated inside" philosophy
- ✅ Production-grade testing infrastructure
- ✅ Best practices in action

Even though we're testing basic math, we're using the same tools that test complex systems at major tech companies! 🚀
