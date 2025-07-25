def square_root(number):
    """Calculate the square root of a number."""
    if number < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    return number**0.5
