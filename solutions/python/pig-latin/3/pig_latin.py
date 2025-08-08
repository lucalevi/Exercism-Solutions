"""
Pig Latin Translator
This module provides a function to translate English text into Pig Latin.
"""

VOWELS = "aeiou"


def all_are_consonants(text: str) -> bool:
    """Check if all characters in the text are consonants."""
    return all(char not in VOWELS for char in text)


def handle_consonant_cluster(word: str) -> str:
    """
    Move all leading consonants to the end and add 'ay'.
    Example: 'pig' -> 'igpay'
    """
    consonant_cluster = ""
    for char in word:
        if char not in VOWELS:
            consonant_cluster += char
        else:
            break
    return word[len(consonant_cluster) :] + consonant_cluster + "ay"


def handle_qu_word(word: str) -> str:
    """Handle words containing 'qu' according to Pig Latin rules."""
    qu_index = word.index("qu")
    return word[qu_index + 2 :] + word[: qu_index + 2] + "ay"


def handle_y_word(word: str) -> str:
    """Handle words with 'y' after initial consonants."""
    y_index = word.index("y")
    return word[y_index:] + word[:y_index] + "ay"


def translate(text: str) -> str:
    """
    Translate the given text into Pig Latin following specific rules.
    """
    words = text.split()
    pig_latin_words = []

    for word in words:
        if word[0] in VOWELS or word.startswith(("xr", "yt")):
            pig_latin_word = word + "ay"
        elif "qu" in word and all_are_consonants(word[: word.index("qu")]):
            pig_latin_word = handle_qu_word(word)
        elif (
            "y" in word
            and word[0] not in "aeiouy"
            and all_are_consonants(word[: word.index("y")])
        ):
            pig_latin_word = handle_y_word(word)
        else:
            pig_latin_word = handle_consonant_cluster(word)

        pig_latin_words.append(pig_latin_word)

    return " ".join(pig_latin_words)
