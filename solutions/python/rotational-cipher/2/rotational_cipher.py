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
    
    # Define the lowercase alphabet for consistent indexing and shifting
    alphabet = string.ascii_lowercase
    alphabet_size = len(alphabet) # 26

    translated_letters = []

    for char in text:
        if not char.isalpha():
            # If the character is not an alphabet letter (e.g., space, punctuation, number),
            # append it directly to the result without modification.
            translated_letters.append(char)
        else:
            # Determine if the original character was uppercase to preserve its case
            is_upper = char.isupper()
            
            # Get the lowercase version of the character to work with the 'alphabet' string
            char_lower = char.lower()
            
            # Find the 0-based index of the character in the lowercase alphabet
            original_index = alphabet.index(char_lower)
            
            # Calculate the new index after applying the key shift.
            # The modulo operator (%) ensures that the index wraps around the alphabet.
            new_index = (original_index + key) % alphabet_size
            
            # Get the translated lowercase letter from the alphabet using the new index
            translated_letter = alphabet[new_index]
            
            # If the original character was uppercase, convert the translated letter to uppercase
            if is_upper:
                translated_letter = translated_letter.upper()
            
            # Add the translated (and possibly case-corrected) letter to our list
            translated_letters.append(translated_letter)
            
    # Join the list of translated characters back into a single string
    return "".join(translated_letters)