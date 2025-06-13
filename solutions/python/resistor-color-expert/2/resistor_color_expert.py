"""
This module provides a function to decode resistor color codes into human-readable resistance
values with tolerance. It supports 1, 4, and 5-band resistors and formats the output
with appropriate prefixes (ohms, kiloohms, megaohms, gigaohms).
"""

RES_COLORS = [
    "black", "brown", "red", "orange", "yellow",
    "green", "blue", "violet", "grey", "white",
]

TOL_COLORS = {
    "grey": 0.05,
    "violet": 0.1,
    "blue": 0.25,
    "green": 0.5,
    "brown": 1,
    "red": 2,
    "gold": 5,
    "silver": 10
}

# Define constants for prefix magnitudes for better readability
KILO = 1000
MEGA = 1_000_000
GIGA = 1_000_000_000


def _get_base_value(colors: list[str]) -> int:
    """
    Calculates the base resistance value from the first two or three color bands.
    """
    if len(colors) == 5:
        # For five-band resistors, concatenate the first three digits
        digits_str = "".join(str(RES_COLORS.index(color)) for color in colors[0:3])
    else:
        # For four-band resistors, concatenate the first two digits
        digits_str = "".join(str(RES_COLORS.index(color)) for color in colors[0:2])
    return int(digits_str)


def _calculate_resistance(base_value: int, multiplier_band: str) -> float:
    """
    Calculates the total resistance value given the base value and multiplier band.
    """
    multiplier_power = RES_COLORS.index(multiplier_band)
    return base_value * (10 ** multiplier_power)


def _get_tolerance(tolerance_band: str) -> float:
    """
    Retrieves the tolerance percentage from the tolerance color band.
    """
    return TOL_COLORS[tolerance_band]

    
def _format_resistance_output(resistance_value: float, tolerance: float) -> str:
    """
    Formats the resistance value with the appropriate prefix and tolerance.
    """
    if resistance_value >= GIGA:
        value_with_prefix = resistance_value / GIGA
        unit = "gigaohms"
    elif resistance_value >= MEGA:
        value_with_prefix = resistance_value / MEGA
        unit = "megaohms"
    elif resistance_value >= KILO:
        value_with_prefix = resistance_value / KILO
        unit = "kiloohms"
    else:
        value_with_prefix = resistance_value
        unit = "ohms"

    if value_with_prefix == int(value_with_prefix):
        formatted_value = int(value_with_prefix)
    else:
        formatted_value = f"{value_with_prefix:.2f}".rstrip('0').rstrip('.')

    return f"{formatted_value} {unit} ±{tolerance}%"

    
def resistor_label(colors: list[str]) -> str:
    """
    Translates a list of resistor color bands into a human-readable resistance label,
    including the resistance value, appropriate prefix (ohms, kiloohms, megaohms, gigaohms),
    and tolerance.

    This function handles 1-band (black for 0 ohms), 4-band, and 5-band resistors.

    Args:
        colors (list[str]): A list of strings representing the color bands of the resistor.
                            Expected formats:
                            - ["black"] for 0 ohms.
                            - [Band1, Band2, Multiplier, Tolerance] for 4-band resistors.
                            - [Band1, Band2, Band3, Multiplier, Tolerance] for 5-band resistors.

    Returns:
        str: A formatted string representing the resistor's value and tolerance,
             e.g., "33 ohms ±0.5%", "2.54 megaohms ±1%".
    """
    # Handle the "0 ohms" case explicitly for one-band resistors
    if len(colors) == 1 and colors[0] == "black":
        return "0 ohms"

    # Determine the multiplier and tolerance bands based on the number of colors
    if len(colors) == 5:
        multiplier_band = colors[3]  # Fourth band is the multiplier
        tolerance_band = colors[4]   # Fifth band is the tolerance
    elif len(colors) == 4:
        multiplier_band = colors[2]  # Third band is the multiplier
        tolerance_band = colors[3]   # Fourth band is the tolerance
    else:
        # This case should ideally be handled by more robust input validation
        # For this refactoring, we'll assume valid input lengths (1, 4, or 5)
        raise ValueError("Unsupported number of color bands. Expected 1, 4, or 5.")

    base_value = _get_base_value(colors)
    resistance_value = _calculate_resistance(base_value, multiplier_band)
    tolerance = _get_tolerance(tolerance_band)
    
    return _format_resistance_output(resistance_value, tolerance)