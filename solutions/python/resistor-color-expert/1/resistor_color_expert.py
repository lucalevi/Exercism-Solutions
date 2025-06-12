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
    
    # Calculate the base value from the first two or three bands
    first_digit = RES_COLORS.index(colors[0])
    second_digit = RES_COLORS.index(colors[1])

    if len(colors) == 5:
        # For five-band resistors, the first three bands determine the base value
        third_digit = RES_COLORS.index(colors[2])
        base_value = first_digit * 100 + second_digit * 10 + third_digit
    else:
        # For four-band resistors, the first two bands determine the base value
        base_value = first_digit * 10 + second_digit

    # The multiplier band is always the second to last band
    multiplier_power = RES_COLORS.index(colors[-2])
    resistance_value = base_value * (10 ** multiplier_power)

    # The tolerance band is always the last band
    tolerance = TOL_COLORS[colors[-1]]
    
    # Determine the appropriate prefix (giga, mega, kilo, or none)
    # We check from largest to smallest to ensure the most appropriate unit is used
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
        # If none of the larger prefixes apply, use ohms directly
        value_with_prefix = resistance_value
        unit = "ohms"

    # Format the resistance value:
    # If the value is a whole number (e.g., 2.0, 33.0), format it as an integer (2, 33).
    # Otherwise, format it as a float, removing trailing zeros (e.g., 2.50 becomes 2.5, 2.54 remains 2.54).
    if value_with_prefix == int(value_with_prefix):
        formatted_value = int(value_with_prefix)
    else:
        # Format to two decimal places, then remove trailing zeros if any
        # This handles cases like 2.54 (remains 2.54) and 3.3 (becomes 3.3)
        formatted_value = f"{value_with_prefix:.2f}".rstrip('0').rstrip('.')

    # Construct and return the final label string
    return f"{formatted_value} {unit} ±{tolerance}%"
