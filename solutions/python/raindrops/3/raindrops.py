"""
This module provides a function to convert a number into a "Raindrop" sound.

The conversion follows specific rules:
- "Pling" if the number is divisible by 3.
- "Plang" if the number is divisible by 5.
- "Plong" if the number is divisible by 7.
- If not divisible by 3, 5, or 7, the number itself is returned as a string.
"""

def convert(number: int) -> str:
    """
    Converts a given integer into its "Raindrop" sound representation.

    Args:
        number (int): The integer to convert.

    Returns:
        str: A string representing the "Raindrop" sound. This will be a
             concatenation of "Pling", "Plang", and/or "Plong" based on
             divisibility by 3, 5, and 7 respectively. If the number is not
             divisible by any of these, the number itself is returned as a string.
    """
    result = []
    if number % 3 == 0:
        result.append("Pling")
    if number % 5 == 0:
        result.append("Plang")
    if number % 7 == 0:
        result.append("Plong")
    if not result:
        return str(number)

    return "".join(result)
