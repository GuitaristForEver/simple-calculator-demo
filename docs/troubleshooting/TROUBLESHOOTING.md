# Troubleshooting Guide 🔧

## GitHub Actions Failures

### Common Issues and Solutions

#### 1. **Allure Report Action Fails**

**Symptoms**:
- "Generate Allure Report with History" step fails
- Error about missing allure-results

**Solutions**:

**A. Check if allure-results exists**:
```yaml
- name: Debug - List allure-results
  run: ls -la allure-results || echo "No allure-results found"
```

**B. Ensure pytest runs successfully**:
```yaml
- name: Run tests with Allure
  run: |
    pytest --alluredir=allure-results -v
    ls -la allure-results  # Verify files created
```

**C. Check Allure action version**:
Try updating to latest:
```yaml
uses: simple-elf/allure-report-action@master
```

---

#### 2. **GitHub Pages Deployment Fails**

**Symptoms**:
- "Deploy to GitHub Pages" step fails
- Permission denied errors

**Solutions**:

**A. Check Repository Settings**:
1. Go to **Settings** → **Actions** → **General**
2. Under "Workflow permissions":
   - Select **"Read and write permissions"**
   - Check **"Allow GitHub Actions to create and approve pull requests"**
3. Save

**B. Check if gh-pages branch exists**:
- Go to your repo → **Branches**
- Look for `gh-pages` branch
- If missing, first run will create it

**C. Verify permissions in workflow**:
```yaml
permissions:
  contents: write  # Must be present!
```

---

#### 3. **Cache-Related Failures**

**Symptoms**:
- "Cache pip packages" or "Cache pytest" fails
- Workflow slower than expected

**Solutions**:

**A. Clear cache**:
1. Go to **Actions** → **Caches**
2. Delete old caches
3. Re-run workflow

**B. Simplify caching** (temporary fix):
Remove the extra cache steps, keep only:
```yaml
- name: Set up Python
  uses: actions/setup-python@v5
  with:
    python-version: '3.9'
    cache: 'pip'  # This is enough!
```

---

#### 4. **Dependency Installation Fails**

**Symptoms**:
- "Install dependencies" step fails
- Package not found errors

**Solutions**:

**A. Check requirements.txt**:
```bash
# Locally test
pip install -r requirements.txt
```

**B. Pin versions** (if needed):
```
pytest==7.4.0
allure-pytest==2.13.5
```

**C. Add timeout**:
```yaml
- name: Install dependencies
  timeout-minutes: 10
  run: |
    python -m pip install --upgrade pip
    pip install -r requirements.txt
```

---

#### 5. **CodeQL Security Scan Fails**

**Symptoms**:
- CodeQL workflow shows "Requires authentication" error
- Security tab shows no results

**Solutions**:

**A. Check permissions in workflow**:
```yaml
permissions:
  actions: read        # Required for CodeQL
  contents: read
  security-events: write
```

**B. Verify CodeQL action version**:
Use v4 (v3 is deprecated):
```yaml
uses: github/codeql-action/init@v4
uses: github/codeql-action/analyze@v4
```

**C. Check repository settings**:
1. Go to **Settings** → **Security** → **Code security and analysis**
2. Enable **"CodeQL analysis"**

---

#### 6. **Codecov Upload Fails**

**Symptoms**:
- "Upload coverage to Codecov" step fails
- Badge shows "unknown" or no data

**Solutions**:

**A. Check Codecov token**:
1. Go to [codecov.io](https://codecov.io) and sign in
2. Find your repository
3. Copy the upload token
4. Add to GitHub: **Settings** → **Secrets** → **CODECOV_TOKEN**

**B. Verify coverage.xml exists**:
```yaml
- name: Debug coverage
  run: ls -la coverage.xml
```

**C. Check pytest coverage flags**:
```yaml
pytest --cov=src --cov-report=xml
```

**D. Token not required for public repos**:
For public repos, you can remove the token:
```yaml
- name: Upload coverage to Codecov
  uses: codecov/codecov-action@v4
  with:
    files: ./coverage.xml
    fail_ci_if_error: false
    # token: not needed for public repos
```

---

#### 7. **Coverage Below Threshold (80%)**

**Symptoms**:
- Tests pass but workflow fails
- "FAIL Required test coverage of 80% not reached"

**Solutions**:

**A. Check what's not covered**:
```bash
# Run locally with HTML report
pytest --cov=src --cov-report=html
open htmlcov/index.html  # macOS
# or: xdg-open htmlcov/index.html  # Linux
```

**B. Exclude non-testable code**:
In `pyproject.toml`:
```toml
[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "def main",
    "if __name__ == .__main__.:",
]
```

**C. Lower threshold temporarily** (not recommended):
```yaml
pytest --cov-fail-under=70  # Lower while fixing
```

---

#### 8. **Tests Fail in CI but Pass Locally**

**Symptoms**:
- Tests pass on your machine
- Tests fail in GitHub Actions

**Solutions**:

**A. Check Python version**:
Local vs CI might differ. Match them:
```yaml
python-version: '3.9'  # Same as your local
```

**B. Check for environment differences**:
```yaml
- name: Debug environment
  run: |
    python --version
    pip list
    pwd
    ls -la
```

**C. Check for missing files**:
Ensure all test files are committed:
```bash
git status
git add tests/
```

---

## Quick Fixes

### Fix 1: Minimal Working Workflow

If everything fails, try this minimal version:

```yaml
name: Simple Tests

on: [push]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.9'
          cache: 'pip'

      - name: Install and test
        run: |
          pip install -r requirements.txt
          pytest -v
```

Once this works, add features back one by one.

---

### Fix 2: Skip Allure Temporarily

Comment out Allure steps to isolate the issue:

```yaml
# - name: Generate Allure Report with History
#   uses: simple-elf/allure-report-action@v1.13
#   ...

# - name: Deploy to GitHub Pages
#   uses: peaceiris/actions-gh-pages@v3
#   ...
```

---

### Fix 3: Manual Trigger for Debugging

Add this to test manually:

```yaml
on:
  workflow_dispatch:  # Manual trigger
    inputs:
      debug:
        description: 'Enable debug mode'
        required: false
        default: 'false'
```

Then:
1. Go to **Actions** tab
2. Select workflow
3. Click **"Run workflow"**
4. Watch it run

---

## Checking Workflow Status

### Via GitHub UI

1. Go to: `https://github.com/[username]/[repo]/actions`
2. Click on failing workflow run
3. Click on failed job
4. Expand failed step
5. Read error message

### Via Command Line

```bash
# Using GitHub CLI
gh run list
gh run view [run-id]
gh run view [run-id] --log-failed
```

---

## Common Error Messages

### "Error: Resource not accessible by integration"

**Fix**: Enable write permissions
- Settings → Actions → General → Workflow permissions → Read and write

### "Error: Process completed with exit code 1"

**Fix**: Check the step's logs for actual error
- Usually a command failed
- Look at the output above this message

### "Error: Unable to process file command 'env'"

**Fix**: Update action versions
```yaml
uses: actions/checkout@v4  # Not v2
uses: actions/setup-python@v5  # Not v2
```

### "Error: No space left on device"

**Fix**: Clean up in workflow
```yaml
- name: Free disk space
  run: |
    sudo rm -rf /usr/share/dotnet
    sudo rm -rf /opt/ghc
```

---

## Debug Mode

Enable detailed logging:

```yaml
env:
  ACTIONS_RUNNER_DEBUG: true
  ACTIONS_STEP_DEBUG: true
```

Add to top of workflow file for verbose output.

---

## Getting Help

### 1. Check Workflow Logs
- Most specific error information
- Shows exact command that failed

### 2. Search GitHub Issues
- `simple-elf/allure-report-action` issues
- `peaceiris/actions-gh-pages` issues

### 3. Test Locally
```bash
# Run same commands as CI
pip install -r requirements.txt
pytest --alluredir=allure-results -v
```

### 4. Simplify and Rebuild
- Start with minimal workflow
- Add features one by one
- Test after each addition

---

## Prevention

### Before Pushing

```bash
# Test locally first
pytest -v

# Check YAML syntax
python -c "import yaml; yaml.safe_load(open('.github/workflows/tests.yml'))"

# Verify all files committed
git status
```

### After Pushing

1. Watch Actions tab
2. Check for green checkmark ✅
3. If red ❌, check logs immediately
4. Fix and push again

---

## Still Stuck?

### Provide These Details

When asking for help, include:

1. **Link to failed run**:
   `https://github.com/[user]/[repo]/actions/runs/[id]`

2. **Error message** (exact text)

3. **What you tried** (list fixes attempted)

4. **Local test results**:
   ```bash
   pytest -v  # Does this pass?
   ```

5. **Recent changes**:
   ```bash
   git log --oneline -5
   ```

---

## Quick Checklist

When workflow fails, check:

- [ ] Tests pass locally (`pytest -v`)
- [ ] YAML syntax valid
- [ ] All files committed
- [ ] Workflow permissions enabled (Settings → Actions)
- [ ] Python version matches (local vs CI)
- [ ] Dependencies install (`pip install -r requirements.txt`)
- [ ] No typos in file paths
- [ ] Actions are latest versions (@v4, @v5)
- [ ] Logs reviewed for actual error
- [ ] Simple version works first
- [ ] CodeQL has `actions: read` permission
- [ ] Codecov token set (or remove for public repos)
- [ ] Coverage threshold met (80%)

---

## Success Indicators

Workflow is working when you see:

✅ All steps green
✅ "5 passed" in test output
✅ Allure report generated
✅ Deployed to gh-pages
✅ Report accessible at GitHub Pages URL

---

## Summary

**Most Common Fix**: Enable write permissions in Settings → Actions

**Second Most Common**: Update action versions to latest

**Third Most Common**: Check if gh-pages branch exists

**Always**: Read the actual error message in logs!

Good luck! 🚀
