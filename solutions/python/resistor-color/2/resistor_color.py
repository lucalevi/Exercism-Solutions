"""
This module provides utilities for working with resistor color codes.

It includes functions to look up the numerical value of a color band
and to list all available color bands, based on the standard
electronic color code for resistors.
"""

COLORS = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]


def color_code(color):
    """
    Looks up the numerical value associated with a particular resistor color band.

    This function uses the standard electronic color code where colors map
    to their index in the predefined COLORS list.

    Args:
        color (str): The name of the color band (e.g., "black", "brown").

    Returns:
        int: The numerical value (0-9) corresponding to the input color.

    Raises:
        ValueError: If the input color is not found in the list of valid colors.

    Examples:
        >>> color_code("black")
        0
        >>> color_code("red")
        2
    """
    return colors().index(color)


def colors():
    """
    Returns a list of all valid resistor band colors in their numerical order.

    This list can be used to display available color options or for reference.
    The index of each color in this list corresponds to its numerical value.

    Returns:
        list[str]: A list containing the names of all supported resistor colors.

    Examples:
        >>> colors()
        ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
    """
    return COLORS
