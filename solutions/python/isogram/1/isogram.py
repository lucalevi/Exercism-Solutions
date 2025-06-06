"""
This module provides a function to determine if a given word or phrase is an isogram.

An isogram is defined as a word or phrase where no letter repeats.
Spaces and hyphens are explicitly allowed to appear multiple times and are ignored
in the uniqueness check. The check is case-insensitive.
"""


def is_isogram(phrase: str) -> bool:
    """
    Determines if a given word or phrase is an isogram.

    An isogram is a word or phrase where no letter repeats.
    Spaces and hyphens are ignored, and the check is case-insensitive.

    Args:
        phrase (str): The word or phrase to check.

    Returns:
        bool: True if the phrase is an isogram, False otherwise.

    Examples:
        >>> is_isogram("lumberjacks")
        True
        >>> is_isogram("background")
        True
        >>> is_isogram("six-year-old")
        True
        >>> is_isogram("isograms")
        False
        >>> is_isogram("Alphabet") # Case-insensitive check
        False
    """
    # 1. Filter out non-alphabetic characters and convert to lowercase.
    #    This creates a new string containing only the letters relevant to the check.
    letters_only = ''.join(char for char in phrase.lower() if char.isalpha())

    # 2. Compare the length of this filtered string to the length of a set
    #    created from these letters. If they are equal, all letters are unique.
    return len(letters_only) == len(set(letters_only))
