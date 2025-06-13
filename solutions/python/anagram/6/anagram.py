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
    # Pre-process the input word once
    word_lower = word.lower()
    word_sorted = sorted(word_lower)

    # anagrams = []
    # for candidate in candidates:
    #     candidate_lower = candidate.lower()
    #     # Exclude the original word itself (case-insensitive)
    #     if word_lower == candidate_lower:
    #         continue

    #     candidate_sorted = sorted(candidate_lower)
    #     if word_sorted == candidate_sorted:
    #         anagrams.append(candidate)

    # return anagrams

    return [
        candidate
        for candidate in candidates
        if word_lower != candidate.lower() and word_sorted == sorted(candidate.lower())
    ]
