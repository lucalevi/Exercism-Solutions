"""
This module provides a function to validate ISBN-10 strings.
"""


def is_valid(isbn: str) -> bool:
    """
    Checks if the provided string is a valid ISBN-10.

    An ISBN-10 consists of 9 digits (0-9) plus one check character
    (either a digit or 'X'). 'X' represents the value 10.
    The string may contain hyphens, which are ignored.
    Validity is determined by the formula:
    (d1*10 + d2*9 + ... + d10*1) mod 11 == 0.

    Args:
        isbn (str): The potential ISBN-10 string to validate.

    Returns:
        bool: True if the string is a valid ISBN-10, False otherwise.
    """
    # Step 1: Pre-process the string to strip the hyphens
    cleaned_isbn_chars = [char for char in isbn if char != "-"]

    # Step 2: Validate the length and check the position of 'X'
    if len(cleaned_isbn_chars) != 10:
        return False # Must have exactly 10 significant characters

    # If 'X' exists, it must be the very last character
    # If the last character is 'X', convert it to 10.
    if cleaned_isbn_chars[-1] == "X":
        cleaned_isbn_chars[-1] = "10"

    # Check if there are non-digit characters remainig
    # If so, the ISBN is invalid
    if not all(char.isdigit() for char in cleaned_isbn_chars):
        return False

    # Convert the full list into a list of integers
    processed_digits = [int(char) for char in cleaned_isbn_chars]

    # Step 3: Calculate the weighted sum using sum() with a generator expression
    # The weights go from 10 down to 1 (10-0=10, 10-1=9, ..., 10-9=1)
    total = sum(digit_value * (10 - i) for i, digit_value in enumerate(processed_digits))

    # Step 4: Perform the modulo 11 check
    return total % 11 == 0
