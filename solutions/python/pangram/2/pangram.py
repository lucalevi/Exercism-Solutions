"""
This module provides a function to determine if a given sentence is a pangram.

A pangram is a sentence that uses every letter of the English alphabet at least once.
The check is case-insensitive and ignores non-alphabetic characters.
"""

import string


def is_pangram(sentence: str) -> bool:
    """
    Checks if the given sentence is a pangram.

    A pangram is a sentence that contains every letter of the English alphabet
    at least once. The check is case-insensitive, meaning 'a' and 'A' are
    treated as the same letter. Non-alphabetic characters (numbers, punctuation,
    spaces, etc.) are not part of the alphabet.

    Args:
        sentence (str): The input string to be checked for pangram status.

    Returns:
        bool: True if the sentence is a pangram, False otherwise.
    """
    required_letters = string.ascii_lowercase
    sentence_lower = sentence.lower()

    return all(
        letter in sentence_lower 
        for letter in required_letters
    )
