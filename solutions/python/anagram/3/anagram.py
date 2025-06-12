"""
This module provides utility functions for working with strings, specifically for
identifying anagrams.

It includes a function `find_anagrams` that takes a word and a list of candidate
words, returning all candidates that are anagrams of the given word.
"""


def find_anagrams(word: str, candidates: list) -> list:
    """
    Finds all anagrams of a given word from a list of candidate words.

    An anagram is a word or phrase formed by rearranging the letters of a
    different word or phrase, typically using all the original letters
    exactly once. This function ignores case and excludes the original word
    itself from the results if it appears in the candidates list.

    Args:
        word (str): The word to find anagrams for.
        candidates (list): A list of strings to check against for anagrams.

    Returns:
        list: A new list containing all strings from `candidates` that are
              anagrams of `word`.
    """
    return [
        candidate
        for candidate in candidates
        if sorted(word.lower()) == sorted(candidate.lower())
        and word.lower() != candidate.lower()
    ]
