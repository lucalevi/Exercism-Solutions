"""
This module provides a function to calculate the score of a dart throw
in a specific Darts game variant.

Points are awarded based on the dart's distance from the center (0,0) of the target:
- 10 points for landing within or on the inner circle (radius 1).
- 5 points for landing within or on the middle circle (radius 5), but outside the inner.
- 1 point for landing within or on the outer circle (radius 10), but outside the middle.
- 0 points for landing outside the target (beyond radius 10).
"""

import math

def score(x: int, y: int) -> int:
    """
    Calculates the points scored in a single toss of a Darts game.

    Args:
        x (float): The x-coordinate of where the dart landed.
        y (float): The y-coordinate of where the dart landed.

    Returns:
        int: The points earned (0, 1, 5, or 10) based on the dart's position.
    """
    # Calculate the distance from the center (0,0) to the dart's landing point
    distance = math.sqrt(x**2 + y**2)

    # Check from the innermost circle outwards to handle boundary cases correctly
    if distance <= 1:
        return 10  # Inner circle
    if distance <= 5:
        return 5   # Middle circle
    if distance <= 10:
        return 1   # Outer circle

    return 0   # Outside target
