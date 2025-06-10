COLORS = [
    "black", "brown", "red", "orange", "yellow",
    "green", "blue", "violet", "grey", "white",
]

# Define constants for prefix magnitudes for better readability
KILO = 1000
MEGA = 1_000_000
GIGA = 1_000_000_000

def label(colors: list[str]) -> str:
    """
    Calculates the resistance value from three color bands and formats it with appropriate prefixes.

    Args:
        colors: A list of three strings representing the color bands.

    Returns:
        A string representing the resistance value in ohms, with metric prefixes if applicable.
    """
    # Calculate the base value from the first two bands
    # Use direct integer multiplication and addition
    first_digit = COLORS.index(colors[0])
    second_digit = COLORS.index(colors[1])
    base_value = first_digit * 10 + second_digit

    # Calculate the multiplier from the third band
    multiplier_power = COLORS.index(colors[2])
    resistance_value = base_value * (10 ** multiplier_power)

    # Handle the "0 ohms" case explicitly
    if resistance_value == 0:
        return "0 ohms"

    # Determine the appropriate prefix
    if resistance_value >= GIGA and resistance_value % GIGA == 0:
        return f"{resistance_value // GIGA} gigaohms"
    elif resistance_value >= MEGA and resistance_value % MEGA == 0:
        return f"{resistance_value // MEGA} megaohms"
    elif resistance_value >= KILO and resistance_value % KILO == 0:
        return f"{resistance_value // KILO} kiloohms"
    else:
        return f"{resistance_value} ohms"