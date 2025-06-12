"""This module provides functionality to identify anagrams.

It includes functions to count letter occurrences in words and to find
anagrams from a list of candidates based on specific rules, including
case-insensitivity for comparison and excluding words that are their
own anagrams.
"""


def count_letters(word: str) -> dict:
    """Count the occurrences of each letter in a word, case-insensitively.

    The input word is converted to lowercase before counting. The returned
    dictionary maps each unique letter to its frequency in the word.

    Args:
        word: The input string (word) to count letters from.

    Returns:
        A dictionary where keys are lowercase letters and values are their
        respective counts.
    """
    word = word.lower()
    return {letter: word.count(letter) for letter in word}


def find_anagrams(word: str, candidates: list) -> list:
    """Find anagrams of a target word from a list of candidate words.

    An anagram is defined as a word formed by rearranging the letters of
    another word. This function identifies candidates that are anagrams
    of the target word, adhering to the following rules:

    1.  A word is not considered its own anagram (case-insensitively).
        For example, "stop" is not an anagram of "stop", and "BANANA" is
        not an anagram of "banana".
    2.  Case is ignored when determining if words are anagrams (e.g., "PoTS"
        is an anagram of "sTOp").
    3.  The returned anagrams retain their original casing from the
        `candidates` list.

    Args:
        word: The target word to find anagrams for.
        candidates: A list of strings to check for anagrams.

    Returns:
        A list of strings from `candidates` that are anagrams of the target word.
        The order of anagrams in the returned list matches their order
        in the `candidates` list.
    """
    normalized_target_word = word.lower()
    target_word_letter_counts = count_letters(word)

    return [
        candidate
        for candidate in candidates
        if candidate.lower()
        != normalized_target_word  # Rule 1: Not the same word (case-insensitive)
        and count_letters(candidate)
        == target_word_letter_counts  # Rule 2: Same letter counts
    ]
