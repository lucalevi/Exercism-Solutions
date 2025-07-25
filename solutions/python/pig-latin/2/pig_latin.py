"""
Pig Latin Translator
This module provides a function to translate English text into Pig Latin.

Rules:
1. If a word begins with a vowel, or starts with "xr" or "yt", add an "ay" sound
to the end of the word.

2. If a word begins with one or more consonants, first move those consonants to
the end of the word and then add an "ay" sound to the end of the word.

3. If a word starts with zero or more consonants followed by "qu", first move
those consonants (if any) and the "qu" part to the end of the word,
and then add an "ay" sound to the end of the word.

4. If a word starts with one or more consonants followed by "y",
first move the consonants preceding the "y" to the end of the word,
and then add an "ay" sound to the end of the word.
"""


def translate(text: str) -> str:
    """Translate the given text into Pig Latin following specific rules.

    Args:
        text (str): The input text to be translated.
    Returns:
        str: The translated text in Pig Latin.
    """

    def handle_consonant_cluster(word: str) -> str:
        """
        Helper function to handle words starting with consonants.
        Moves all leading consonants to the end and adds 'ay'.
        Example: 'pig' -> 'igpay'
        """
        consonant_cluster = ""
        for char in word:
            if char not in "aeiou":
                consonant_cluster += char
            else:
                break
        return word[len(consonant_cluster) :] + consonant_cluster + "ay"

    words = text.split()
    pig_latin_words = []

    for word in words:
        # Rule 1: Words beginning with vowels or special cases "xr"/"yt"
        # Examples: "apple" -> "appleay", "xray" -> "xrayay"
        if word[0] in "aeiou" or word.startswith(("xr", "yt")):
            pig_latin_word = word + "ay"

        # Rule 2: Words starting with zero or more consonants followed by "qu"
        # Examples: "quick" -> "ickquay", "square" -> "aresquay"
        elif "qu" in word and (
            word.startswith("qu")
            or (
                word.index("qu") > 0
                and all(
                    c not in "aeiou" for c in word[: word.index("qu")]
                )  # Check if all characters before "qu" are consonants
            )
        ):
            qu_index = word.index("qu")
            if qu_index == 0:  # If "qu" is at the start
                # Example: "quick" -> "ickquay"
                pig_latin_word = word[2:] + "quay"
            else:  # If "qu" is preceded by consonants
                # Example: "square" -> "aresquay"
                # Move the consonants and "qu" to the end
                pig_latin_word = word[qu_index + 2 :] + word[: qu_index + 2] + "ay"

        # Rule 3: Words with 'y' after initial consonants
        # Examples: "rhythm" -> "ythmrhay", "my" -> "ymay"
        elif (
            "y" in word
            and word[0] not in "aeiouy"
            and all(c not in "aeiou" for c in word[: word.index("y")])
        ):
            y_index = word.index("y")
            pig_latin_word = word[y_index:] + word[:y_index] + "ay"

        # Rule 4: All other words starting with consonants
        # Example: "latin" -> "atinlay"
        else:
            pig_latin_word = handle_consonant_cluster(word)

        pig_latin_words.append(pig_latin_word)

    return " ".join(pig_latin_words)
