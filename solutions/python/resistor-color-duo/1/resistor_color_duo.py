"""
Provides a function to color-code two resistance bands.
"""

COLOR_CODES = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
}

def value(colors: list) -> int : 
    """
    Calculates the two-digit resistance value from a list of color bands.

    Args:
        colors: A list of strings representing the color bands.
                Only the first two colors are considered.

    Returns:
        An integer representing the two-digit resistance value.

    Raises:
        KeyError: If any of the first two color names are not recognized.
    """
    # Take only the first two colors from the input list
    first_two_colors = colors[:2]

    # Use a list comprehension to get the string representation of the numeric codes
    # and then join them into a single string.
    numeric_strings = [str(COLOR_CODES[color]) for color in first_two_colors]

    # Join the numeric strings and convert to an integer
    return int("".join(numeric_strings))