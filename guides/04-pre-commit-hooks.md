# Guide 4: Pre-commit Hooks 🔒

**You've tested your code manually.** Now let's make it automatic!

---

## What You'll Learn

In this guide, you'll:
1. ✅ Understand what pre-commit hooks are
2. ✅ Install and use them
3. ✅ See them catch problems automatically

**Time needed**: 10 minutes

---

## What Are Pre-commit Hooks? (Simple Version)

Think of pre-commit hooks as **airport security for your code**:
- Before code "boards the plane" (gets committed)
- Security checks everything automatically
- Catches secrets, formatting issues, and bad code
- You can't commit until it passes!

**Why this matters:** Prevents bad code from entering your repository.

---

## What Gets Checked?

| Hook | What It Does |
|------|-------------|
| 🔒 Gitleaks | Prevents committing secrets/API keys |
| 🐍 Ruff Linter | Checks Python code quality |
| 🎨 Ruff Formatter | Auto-formats Python code |
| ✂️ Whitespace | Removes trailing spaces |
| 📝 End-of-file | Ensures files end with newline |
| 📦 Import Sort | Organizes Python imports |
| 🔑 Private Keys | Detects SSH/SSL keys |
| 📦 Large Files | Prevents files >500KB |
| 🔀 Merge Conflicts | Catches conflict markers |

**All automatic!** No manual work needed.

---

## Installation (One-Time Setup)

### Step 1: Install pre-commit

```bash
pip install pre-commit
```

### Step 2: Install the hooks

```bash
pre-commit install
```

**That's it!** Now hooks run automatically on every commit.

---

## How It Works

### Before (No hooks):
```bash
git add .
git commit -m "My changes"  # Commits immediately
```

### After (With hooks):
```bash
git add .
git commit -m "My changes"
# Hooks run automatically...
# ✅ All checks pass → Commit succeeds!
# ❌ Something fails → Commit blocked!
```

---

## Running Hooks Manually

Want to check before committing?

```bash
pre-commit run --all-files
```

This runs all hooks on all files. You'll see:

```
Gitleaks........................................Passed
ruff-linter....................................Passed
ruff-formatter.................................Passed
trim trailing whitespace.......................Passed
fix end of files...............................Passed
check for added large files....................Passed
```

**All green = You're good to commit!**

---

## Example: Catching a Secret

Let's say you accidentally add an API key:

```python
# src/calculator.py
API_KEY = "put-your-secret-here"  # Oops! (This is a demo placeholder)
```

### Try to commit:
```bash
git add src/calculator.py
git commit -m "Update calculator"
```

### What happens:
```
Gitleaks........................................Failed
- hook id: gitleaks
- exit code: 1

○
    │╲
    │ ○
    ○ ░
    ░    gitleaks

Finding:     sk-1234567890abcdef
Secret:      Generic API Key
File:        src/calculator.py
Line:        2
Commit:      (unstaged)
```

**Commit is BLOCKED!** You're forced to remove the secret. Crisis averted! 🎉

---

## Example: Auto-Formatting

Let's say you have messy code:

```python
# Before
def   add( a,b ):
    return   a+b
```

### Commit it:
```bash
git add src/calculator.py
git commit -m "Add function"
```

### What happens:
```
ruff-formatter.................................Failed
- hook id: ruff-formatter
- files were modified by this hook

Fixed src/calculator.py
```

**Your code is auto-formatted to:**

```python
# After (automatically fixed!)
def add(a, b):
    return a + b
```

Then you commit again and it passes!

---

## Skipping Hooks (Only When Needed)

Sometimes you need to bypass hooks (rarely!):

```bash
git commit -m "WIP" --no-verify
```

**⚠️ Warning:** Only use this for:
- Work-in-progress commits on your branch
- Emergency fixes
- Never on main/master!

---

## CI Integration

**Bonus:** Pre-commit hooks also run in CI!

Even if someone bypasses hooks locally, they'll catch it in the GitHub Actions workflow. Double protection! 🛡️

---

## Configuration

Hooks are configured in `.pre-commit-config.yaml`. You can:
- Add new hooks
- Adjust settings
- Exclude files

**Example:** Exclude a file from Ruff:
```yaml
- id: ruff-linter
  exclude: ^legacy/
```

See [`.pre-commit-config.yaml`](../.pre-commit-config.yaml) for details.

---

## Try It Yourself!

### Challenge 1: Trigger a Hook
1. Add trailing whitespace to any Python file
2. Try to commit
3. Watch pre-commit fix it automatically!

### Challenge 2: Check Everything
```bash
pre-commit run --all-files
```

See all checks pass ✅

### Challenge 3: Update Hooks
```bash
pre-commit autoupdate
```

This updates hooks to latest versions!

---

## Key Takeaways

1. **Pre-commit hooks = Automatic quality gates**
2. **Runs before every commit** (no manual work)
3. **Catches problems early** (before they reach CI)
4. **Blocks bad commits** (forces you to fix issues)

This is **Stage 2** of professional development! 🎯

---

## ✅ You Did It!

You just:
- ✅ Installed pre-commit hooks
- ✅ Understood automatic quality checks
- ✅ Saw hooks in action

**Next Step**: [Guide 5: CI/CD Basics](05-ci-cd-basics.md)
Learn how GitHub automatically tests your code!

---

**Navigation**:
- ⬅️ Previous: [Guide 3: Running Tests](03-running-tests.md)
- ➡️ Next: [Guide 5: CI/CD Basics](05-ci-cd-basics.md)
- 🏠 Back to [README](../README.md)
