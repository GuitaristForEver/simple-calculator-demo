#!/usr/bin/env python3
"""
Tests for the Simple Calculator App
Now using pytest with Allure for enterprise-level reporting!
"""

import allure
import pytest

from src import Calculator


@pytest.fixture
def calc():
    """Create a calculator instance for each test."""
    return Calculator()


@allure.feature("Calculator Operations")
@allure.story("Addition")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("""
Test the addition operation with various inputs:
- Positive numbers
- Negative numbers
- Zero
""")
def test_add(calc):
    """Test addition operation."""
    with allure.step("Add positive numbers: 2 + 3"):
        assert calc.add(2, 3) == 5

    with allure.step("Add negative and positive: -1 + 1"):
        assert calc.add(-1, 1) == 0

    with allure.step("Add zeros: 0 + 0"):
        assert calc.add(0, 0) == 0


@allure.feature("Calculator Operations")
@allure.story("Subtraction")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("Test the subtraction operation with various inputs")
def test_subtract(calc):
    """Test subtraction operation."""
    with allure.step("Subtract: 5 - 3"):
        assert calc.subtract(5, 3) == 2

    with allure.step("Subtract same numbers: 1 - 1"):
        assert calc.subtract(1, 1) == 0

    with allure.step("Subtract larger from smaller: 0 - 5"):
        assert calc.subtract(0, 5) == -5


@allure.feature("Calculator Operations")
@allure.story("Multiplication")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("Test the multiplication operation with various inputs")
def test_multiply(calc):
    """Test multiplication operation."""
    with allure.step("Multiply positive numbers: 3 × 4"):
        assert calc.multiply(3, 4) == 12

    with allure.step("Multiply negative and positive: -2 × 3"):
        assert calc.multiply(-2, 3) == -6

    with allure.step("Multiply by zero: 0 × 5"):
        assert calc.multiply(0, 5) == 0


@allure.feature("Calculator Operations")
@allure.story("Division")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Test the division operation with various inputs")
def test_divide(calc):
    """Test division operation."""
    with allure.step("Divide evenly: 10 ÷ 2"):
        assert calc.divide(10, 2) == 5

    with allure.step("Divide with whole result: 9 ÷ 3"):
        assert calc.divide(9, 3) == 3

    with allure.step("Divide negative number: -6 ÷ 2"):
        assert calc.divide(-6, 2) == -3


@allure.feature("Calculator Operations")
@allure.story("Division")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description(
    "Test that division by zero is properly handled and raises ValueError"
)
def test_divide_by_zero(calc):
    """Test division by zero raises ValueError."""
    with allure.step("Attempt to divide 5 by 0"):
        with pytest.raises(ValueError) as exc_info:
            calc.divide(5, 0)

        allure.attach(
            str(exc_info.value),
            name="Error Message",
            attachment_type=allure.attachment_type.TEXT,
        )
