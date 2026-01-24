#!/usr/bin/env python3
"""
Simple Calculator App
A basic calculator for demonstration of CI/CD concepts.
"""


class Calculator:
    """A simple calculator class with basic operations."""

    def add(self, a: float, b: float) -> float:
        """Add two numbers."""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Subtract b from a."""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers."""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """Divide a by b."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


def main():
    """Main function to demonstrate calculator usage."""
    calc = Calculator()

    print("Simple Calculator Demo")
    print("======================")

    # Demo calculations
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"6 * 7 = {calc.multiply(6, 7)}")
    print(f"15 / 3 = {calc.divide(15, 3)}")

    # Interactive mode
    print("\nInteractive Mode (type 'quit' to exit):")
    while True:
        try:
            operation = (
                input("Enter operation (add/subtract/multiply/divide): ")
                .strip()
                .lower()
            )
            if operation == "quit":
                break

            if operation not in ["add", "subtract", "multiply", "divide"]:
                print("Invalid operation. Use: add, subtract, multiply, divide")
                continue

            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if operation == "add":
                result = calc.add(a, b)
            elif operation == "subtract":
                result = calc.subtract(a, b)
            elif operation == "multiply":
                result = calc.multiply(a, b)
            elif operation == "divide":
                result = calc.divide(a, b)

            print(f"Result: {result}")

        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()
