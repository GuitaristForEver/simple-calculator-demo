# Project Structure 🏗️

**Why do we organize files into folders?**

Think of it like organizing your room:
- **Toys** go in the toy box
- **Clothes** go in the closet
- **Books** go on the shelf

Same with code! Each folder has a purpose:

## 📁 Folder Guide

### `src/` - The Brain
**What it is**: Where the actual calculator code lives

**Why**: Keeps all the app logic in one place. When the app grows, you know exactly where to find it!

**Contains**:
- `calculator.py` - The Calculator class with all operations
- `__init__.py` - Makes it a Python package (lets other files import it easily)

### `tests/` - The Quality Checker
**What it is**: Where all the test code lives

**Why**: Tests shouldn't mix with app code. It's like having a separate testing lab!

**Contains**:
- `test_calculator.py` - All the tests that make sure the calculator works correctly

### `docs/` - The Library
**What it is**: Where documentation and guides live

**Why**: Keeps detailed docs separate from the main README. Like having a manual separate from the product!

**Contains**:
- This file! (`STRUCTURE.md`) - Explains the folder organization

### `docs/assets/` - The Media Center
**What it is**: Where images, icons, and media files live

**Why**: Keeps binary files separate from code. Makes it easy to find and update visuals!

**Contains**:
- `logo.png` - Our friendly calculator robot

## 🎯 The Root Level

Files in the main folder are "entry points" or "configuration":

- `README.md` - First thing people see (the welcome mat!)
- `.gitignore` - Tells Git what to ignore
- `.copilot-instructions.md` - Tells AI how to help
- `requirements.txt` - Lists what packages to install

## 🧠 Why This Structure?

**Simple Version**: Everything has a home. Easy to find, easy to understand.

**Sophisticated Version**: This follows Python's standard package structure. It makes the project:
- ✅ **Scalable** - Easy to add new features
- ✅ **Maintainable** - Know where everything goes
- ✅ **Professional** - Follows industry conventions
- ✅ **Testable** - Clear separation of concerns

When the project grows to 100 files, this structure still makes sense!
