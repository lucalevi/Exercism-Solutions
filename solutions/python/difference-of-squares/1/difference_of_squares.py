"""
Calculate the difference between the square of the sum and the sum of the squares
of the first `number` natural numbers.

This module provides functions to compute:
1. The square of the sum of the first `number` natural numbers.
2. The sum of the squares of the first `number` natural numbers.
3. The difference between the two calculated values.
"""


def square_of_sum(number):
    """Calculate the square of the sum of the first `number` natural numbers."""
    return sum(range(1, number + 1)) ** 2


def sum_of_squares(number):
    """Calculate the sum of the squares of the first `number` natural numbers."""
    return sum(num**2 for num in range(1, number + 1))


def difference_of_squares(number):
    """Calculate the difference between the square of the sum and the sum of the squares."""
    return square_of_sum(number) - sum_of_squares(number)
