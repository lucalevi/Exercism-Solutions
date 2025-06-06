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
    # Step 1: Pre-process the string to extract only valid ISBN characters (digits and X)
    # and immediately identify any invalid characters.
    cleaned_isbn_chars = []
    for char in isbn:
        if char == '-':
            continue # Ignore hyphens
        elif char.isdigit():
            cleaned_isbn_chars.append(char)
        elif char.upper() == 'X':
            # 'X' is a valid character, but its position will be checked later.
            # For now, just add it.
            cleaned_isbn_chars.append('X')
        else:
            # Found a character that is not a digit, hyphen, or 'X'
            return False # Invalid ISBN due to forbidden characters

    # Step 2: Validate the length and check the position of 'X'
    if len(cleaned_isbn_chars) != 10:
        return False # Must have exactly 10 significant characters

    # If 'X' exists, it must be the very last character
    # And if the last character is 'X', convert it to 10.
    # Otherwise, convert all to int.
    processed_digits = []
    for i, char in enumerate(cleaned_isbn_chars):
        if char == 'X':
            if i == 9: # It must be the 10th (last) character
                processed_digits.append(10)
            else:
                return False # 'X' found in an invalid position
        else:
            processed_digits.append(int(char))

    # Step 3: Calculate the weighted sum using sum() with a generator expression
    # The weights go from 10 down to 1 (10-0=10, 10-1=9, ..., 10-9=1)
    total = sum(digit_value * (10 - i) for i, digit_value in enumerate(processed_digits))

    # Step 4: Perform the modulo 11 check
    return total % 11 == 0