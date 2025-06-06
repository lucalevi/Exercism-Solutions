"""
This module contains a function to determine Bob's response
based on the input message, following specific rules for
questions, yelling, and silence.
"""

def response(hey_bob: str) -> str:
    """
    Determines Bob's reply based on the given message.

    Args:
        hey_bob (str): The message sent to Bob.

    Returns:
        str: Bob's appropriate response.
    """
    # Strip whitespace first
    hey_bob = hey_bob.strip()

    # Determine characteristics of the input
    is_question = hey_bob.endswith('?')
    # Check for actual letters, not just symbols/numbers, when determining yelling
    is_yelling = hey_bob.isupper() and \
                 any(c.isalpha() for c in hey_bob)

    if not hey_bob: # True if hey_bob is an empty string
        return "Fine. Be that way!"
    if is_yelling and is_question:
        return "Calm down, I know what I'm doing!"
    if is_yelling:
        return "Whoa, chill out!"
    if is_question:
        return "Sure."

    return "Whatever."
