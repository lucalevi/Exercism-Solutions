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
    # 1. Handle empty string immediately (though it will fail length check anyway)
    if not isbn:
        return False

    processed_digits = []
    # Use index to correctly handle the special case of 'X' only at the last position
    for i, char in enumerate(isbn):
        if char == '-':
            # Hyphens are allowed and simply ignored
            continue
        elif char.isdigit():
            processed_digits.append(int(char))
        elif char.upper() == 'X':
            # 'X' is only valid if it's the very last character of the actual ISBN-10 sequence.
            # This means it must be the 10th significant character.
            # So, at the point of processing 'X', the list should have 9 digits already.
            # Check if it's the last character of the *original* string
            if i == len(isbn) - 1 and len(processed_digits) == 9: 
                processed_digits.append(10)
            else:
                # 'X' found in an invalid position, or not enough digits before it
                return False
        else:
            # Any other non-digit, non-hyphen, non-valid-'X' character makes it invalid
            return False

    # 2. Check the length of the processed digits
    if len(processed_digits) != 10:
        return False

    # 3. Calculate the weighted sum
    total = 0
    for i, digit_value in enumerate(processed_digits):
        # The weights go from 10 down to 1
        total += digit_value * (10 - i)

    # 4. Perform the modulo 11 check
    return total % 11 == 0