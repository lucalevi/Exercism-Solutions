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
    spaces, etc.) are ignored.

    Args:
        sentence (str): The input string to be checked for pangram status.

    Returns:
        bool: True if the sentence is a pangram, False otherwise.
    """
    # Create a set of all unique letters in the sentence, converted to lowercase
    # and filtering out non-alphabetic characters.
    sentence_letters = {char for char in sentence.lower() if char.isalpha()}

    # The set of all lowercase English alphabet letters
    # string.ascii_lowercase provides 'abcdefghijklmnopqrstuvwxyz'
    alphabet_set = set(string.ascii_lowercase)

    # Check if all letters in the alphabet are present in the sentence's letters
    # This is a set subset check: is alphabet_set a subset of sentence_letters?
    return alphabet_set.issubset(sentence_letters)
