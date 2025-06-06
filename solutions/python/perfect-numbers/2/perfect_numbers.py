"""
This module provides functions to calculate the aliquot sum of a positive integer
and to classify numbers as perfect, abundant, or deficient based on their aliquot sum.

The aliquot sum of a number is the sum of its proper divisors (divisors
excluding the number itself).

- A **perfect** number equals its aliquot sum.
- An **abundant** number is less than its aliquot sum.
- A **deficient** number is greater than its aliquot sum.
"""

import math

def aliquot_sum(number: int) -> int:
    """
    Calculates the aliquot sum of a given positive integer.

    The aliquot sum is the sum of all positive divisors of a number,
    excluding the number itself.

    Args:
        number (int): The positive integer for which to calculate the aliquot sum.

    Returns:
        int: The sum of the proper divisors of the input number.

    Raises:
        ValueError: If the input number is not a positive integer.
    """
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Input must be a positive integer.")

    if number == 1:
        # The only proper divisor of 1 is 0 (as per common definition for aliquot sum)
        return 0

    sum_of_divisors = 1  # 1 is always a divisor for any number greater than 1

    # Only check divisors up to the square root of the number.
    # If 'i' is a divisor, then 'number // i' is also a divisor.
    # This significantly reduces the number of checks.
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            sum_of_divisors += i
            # Avoid adding the same divisor twice for perfect squares (e.g., 4, 9, 16)
            if i != number // i:
                sum_of_divisors += (number // i)

    return sum_of_divisors


def classify(number: int) -> str:
    """
    Classifies a positive integer as "perfect", "abundant", or "deficient".

    Classification is based on the comparison of the number to its aliquot sum:
    - "perfect": The number equals its aliquot sum.
    - "abundant": The number is less than its aliquot sum.
    - "deficient": The number is greater than its aliquot sum.

    Args:
        number (int): A positive integer to classify.

    Returns:
        str: The classification of the input integer ("perfect", "abundant", or "deficient").

    Raises:
        ValueError: If the input number is not a positive integer.
    """
    # The aliquot_sum function already validates for positive integers,
    # but for explicit clarity and to conform to the problem's expected error message,
    # we'll keep a dedicated check here as well.
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    aliquot = aliquot_sum(number)

    if number < aliquot:
        return "abundant"
    if number > aliquot:
        return "deficient"

    return "perfect"
