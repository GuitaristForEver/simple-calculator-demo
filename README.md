# Simple Calculator App

A basic Python calculator to demonstrate simple CI/CD concepts with GitHub Actions.

## Features

- Basic arithmetic operations (add, subtract, multiply, divide)
- Interactive mode for user input
- Automated testing with CI/CD
- Simple and clean codebase

## Quick Start

### Run the Calculator

```bash
python calculator.py
```

This will show a demo and then enter interactive mode where you can perform calculations.

### Run Tests

```bash
python -m unittest test_calculator.py -v
```

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
├── calculator.py          # Main calculator application
├── test_calculator.py     # Unit tests
├── requirements.txt       # Dependencies (currently empty)
├── .github/
│   └── workflows/
│       └── ci.yml        # GitHub Actions CI pipeline
└── README.md             # This file
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run the tests: `python -m unittest test_calculator.py`
5. Submit a pull request

The CI pipeline will automatically run tests on your pull request.

## License

This project is for educational purposes.