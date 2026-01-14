#!/usr/bin/env python3
"""
Tests for the Simple Calculator App
Now using pytest - simpler and more powerful!
"""

import pytest
from calculator import Calculator


@pytest.fixture
def calc():
    """Create a calculator instance for each test."""
    return Calculator()


def test_add(calc):
    """Test addition operation."""
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0


def test_subtract(calc):
    """Test subtraction operation."""
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(1, 1) == 0
    assert calc.subtract(0, 5) == -5


def test_multiply(calc):
    """Test multiplication operation."""
    assert calc.multiply(3, 4) == 12
    assert calc.multiply(-2, 3) == -6
    assert calc.multiply(0, 5) == 0


def test_divide(calc):
    """Test division operation."""
    assert calc.divide(10, 2) == 5
    assert calc.divide(9, 3) == 3
    assert calc.divide(-6, 2) == -3


def test_divide_by_zero(calc):
    """Test division by zero raises ValueError."""
    with pytest.raises(ValueError):
        calc.divide(5, 0)
