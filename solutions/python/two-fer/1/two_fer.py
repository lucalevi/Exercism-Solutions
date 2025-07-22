"""
Solution for the two-fer problem.
"""


def two_fer(name=None):
    """
    Returns a string formatted for the two-fer problem.
    If a name is provided, it will be included in the string.
    If no name is provided, it defaults to "you".
    """
    return f"One for {name}, one for me." if name else "One for you, one for me."
