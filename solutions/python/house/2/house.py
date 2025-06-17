"""
The House That Jack Built.
Contains the verses of the nursery rhyme "The House That Jack Built".
The function `recite` returns the verses from a specified start to end verse.
"""

NOUNS = (
    "house",
    "malt",
    "rat",
    "cat",
    "dog",
    "cow with the crumpled horn",
    "maiden all forlorn",
    "man all tattered and torn",
    "priest all shaven and shorn",
    "rooster that crowed in the morn",
    "farmer sowing his corn",
    "horse and the hound and the horn",
)

VERBS = (
    "Jack built.",
    "lay in",
    "ate",
    "killed",
    "worried",
    "tossed",
    "milked",
    "kissed",
    "married",
    "woke",
    "kept",
    "belonged to",
)


def formedVerse(verse):
    """
    Form a verse of the nursery rhyme based on the given verse number.
    Args:
        verse (int): The verse number to form (1-indexed).
    Returns:
        str: The complete verse as a string.
    """
    formed = ["This is the "]
    for phrase in range(verse, 0, -1):
        formed.append(f"{NOUNS[phrase]} that {VERBS[phrase]} the ")
    formed.append("house that Jack built.")
    return "".join(formed)


def recite(start_verse, end_verse):
    """
    Recite the verses of "The House That Jack Built" from start to end verse.
    Args:
        start_verse (int): The starting verse number (1-indexed).
        end_verse (int): The ending verse number (1-indexed).
    Returns:
        list: A list of verses from start to end.
    """
    return [formedVerse(verse) for verse in range(start_verse - 1, end_verse)]
