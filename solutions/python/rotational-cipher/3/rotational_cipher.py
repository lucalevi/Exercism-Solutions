"""
This module provides an implementation of the rotational cipher, also known as the Caesar cipher.

The Caesar cipher is a simple substitution cipher where each letter in the plaintext
is replaced by a letter some fixed number of positions down or up the alphabet.
"""

import string

def rotate(text: str, key: int) -> str:
    """
    Applies a rotational cipher (Caesar cipher) to the input text.

    The Caesar cipher shifts each alphabetic character in the text by a given
    integer key. Non-alphabetic characters (spaces, punctuation, numbers) are
    preserved as they are. The key determines the number of positions each letter
    is shifted down the alphabet. The shift wraps around the alphabet (e.g., 'z'
    shifted by 1 becomes 'a').

    Args:
        text: The input string to be encrypted or decrypted.
        key: An integer representing the shift value. A key of 0 or 26 will
             result in the original text due to modular arithmetic.

    Returns:
        The rotated (encrypted or decrypted) string.

    Examples:
        >>> rotate("omg", 5)
        'trl'
        >>> rotate("c", 0)
        'c'
        >>> rotate("Cool", 26)
        'Cool'
        >>> rotate("The quick brown fox jumps over the lazy dog.", 13)
        'Gur dhvpx oebja sbk whzcf bire gur ynml qbt.'
        >>> rotate("Gur dhvpx oebja sbk whzcf bire gur ynml qbt.", 13)
        'The quick brown fox jumps over the lazy dog.'
        >>> rotate("Hello, World! 123", 3)
        'Khoor, Zruog! 123'
    """
    # Ensure the key is within the valid range [0, 25] for modular arithmetic
    # This handles keys larger than 26 or negative keys gracefully.
    key = key % 26

    # Create the original lowercase and uppercase alphabets
    lower_alphabet = string.ascii_lowercase
    upper_alphabet = string.ascii_uppercase

    # Create the shifted lowercase and uppercase alphabets
    # The slicing creates the "wrap around" effect
    shifted_lower_alphabet = lower_alphabet[key:] + lower_alphabet[:key]
    shifted_upper_alphabet = upper_alphabet[key:] + upper_alphabet[:key]

    # Combine the original and shifted alphabets to create the translation table
    # from_chars will be 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # to_chars will be the corresponding shifted characters
    from_chars = lower_alphabet + upper_alphabet
    to_chars = shifted_lower_alphabet + shifted_upper_alphabet

    # Create the translation table using str.maketrans()
    # This table maps each character in 'from_chars' to its corresponding
    # character in 'to_chars'. Characters not in 'from_chars' (e.g., spaces,
    # punctuation, numbers) will be passed through unchanged by translate().
    translation_table = str.maketrans(from_chars, to_chars)

    # Apply the translation to the input text
    return text.translate(translation_table)