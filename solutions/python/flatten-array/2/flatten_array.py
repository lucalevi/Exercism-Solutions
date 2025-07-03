"""
This module provides a function to flatten a nested list into a single list.
"""


def flatten(iterable: list) -> list:
    """
    Flattens a nested list into a single list.
    Args:
        iterable (list): A list that may contain nested lists.
    Returns:
        list: A single flattened list containing all elements.
    """
    flat_list = []

    while len(iterable) > 0:
        popped = iterable.pop()
        if isinstance(popped, list):
            iterable.extend(popped)
        elif popped is not None:
            flat_list.append(popped)

    return flat_list[::-1]
