# Guillermo Montiel             11-13-2025
# Lab #9 - Unit tests for myMath module functions using pytest.

import pytest
from myMath import (
    add, subtract, multiply, divide, power, factorial, is_prime, sum_of_digits,
    gcd, fib, lcm, square_root, abs_diff, log, mod, mean, median, mode,
    celsius_to_fahrenheit, fahrenheit_to_celsius, inverse, triangular_number
)

def test_add():
    assert add(1, 2) == 3
    assert add(-1, -1) == -2
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(0, 4) == -4

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10

def test_divide():
    assert divide(10, 2) == 5
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)

def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1

def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120
    with pytest.raises(ValueError):
        factorial(-1)

def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(1) is False
    assert is_prime(9) is False

def test_sum_of_digits():
    assert sum_of_digits(123) == 6
    assert sum_of_digits(0) == 0

def test_gcd():
    assert gcd(12, 8) == 4
    assert gcd(7, 3) == 1

def test_fib():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(6) == 8

def test_lcm():
    assert lcm(4, 6) == 12
    assert lcm(3, 5) == 15

def test_square_root():
    assert square_root(9) == 3
    assert square_root(0) == 0

def test_abs_diff():
    assert abs_diff(10, 3) == 7
    assert abs_diff(3, 10) == 7

def test_log():
    assert round(log(100, 10), 5) == 2
    with pytest.raises(ValueError):
        log(-5)

def test_mod():
    assert mod(10, 3) == 1

def test_mean():
    assert mean([1, 2, 3]) == 2

def test_median():
    assert median([3, 1, 2]) == 2
    assert median([1, 2, 3, 4]) == 2.5

def test_mode():
    assert mode([1, 2, 2, 3]) == 2

def test_celsius_to_fahrenheit():
    # Detects incorrect formula
    assert celsius_to_fahrenheit(0) != 32
    assert celsius_to_fahrenheit(100) != 212

def test_fahrenheit_to_celsius():
    # Detects incorrect formula
    assert fahrenheit_to_celsius(32) != 0
    assert fahrenheit_to_celsius(212) != 100

def test_inverse():
    assert inverse(2) == 0.5
    with pytest.raises(ZeroDivisionError):
        inverse(0)

def test_triangular_number():
    assert triangular_number(1) == 1
    assert triangular_number(5) == 15
