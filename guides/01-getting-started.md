# Guide 1: Getting Started 🚀

**Welcome!** This is your first step in learning how to build a professional Python project.

---

## What You'll Learn

In this guide, you'll:
1. ✅ Install the calculator
2. ✅ Run it for the first time
3. ✅ Do some simple math!

**Time needed**: 5 minutes

---

## Step 1: Install Dependencies

You have two options:

### Option A: Traditional (pip)

```bash
pip install -r requirements.txt
```

This is the classic way. Works everywhere!

### Option B: Modern & Fast (uv) ⚡

```bash
uv sync --dev
```

**What's uv?** A super-fast Python package manager (10-100x faster than pip!). See [`docs/UV.md`](../docs/UV.md) for details.

> **Tip**: If you don't have uv installed, stick with pip for now. You can try uv later!

---

## Step 2: Run the Calculator

```bash
python -m src.calculator
```

**What happens?**

You'll see:
1. A demo showing the calculator in action
2. An interactive prompt where YOU can do math!

**Example output**:

```
Simple Calculator Demo
======================
5 + 3 = 8
10 - 4 = 6
6 * 7 = 42
15 / 3 = 5.0

Interactive Mode (type 'quit' to exit):
Enter operation (add/subtract/multiply/divide): _
```

---

## Step 3: Try It Yourself!

Let's do some calculations:

**Try this:**
```
Enter operation: add
Enter first number: 10
Enter second number: 5
Result: 15.0
```

**Try more:**
- Subtraction: `10 - 3 = ?`
- Multiplication: `7 * 8 = ?`
- Division: `20 / 4 = ?`

**Exit when done:**
```
Enter operation: quit
```

---

## What Just Happened?

You ran a Python **module** (`-m src.calculator`). This means:
- Python found the `src` package
- Ran the `calculator.py` file inside it
- Showed you a demo and interactive mode

---

## Troubleshooting

### Error: "No module named 'calculator'"

**Solution**: Make sure you're in the project root directory:
```bash
cd simple-calculator
python -m src.calculator
```

### Error: "No module named 'pytest'"

**Solution**: Install dependencies first:

**Option A: Using pip**
```bash
pip install -r requirements.txt
```

**Option B: Using uv**
```bash
uv sync --dev
```

---

## ✅ You Did It!

You just:
- ✅ Installed a Python project
- ✅ Ran a Python module
- ✅ Used interactive mode

**Next Step**: [Guide 2: Understanding the Code](02-understanding-the-code.md)
Learn how the calculator actually works under the hood!

---

**Navigation**:
- ⬅️ Back to [README](../README.md)
- ➡️ Next: [Guide 2: Understanding the Code](02-understanding-the-code.md)
