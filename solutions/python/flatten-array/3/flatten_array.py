"""
This module provides a function to flatten a nested list into a single list.
"""

import copy


def flatten(iterable: list) -> list:
    """
    Flattens a nested list into a single list.
    Args:
        iterable (list): A list that may contain nested lists.
    Returns:
        list: A single flattened list containing all elements.
    """
    flat_list = []
    stack = copy.copy(iterable)

    while stack:
        popped = stack.pop()
        if isinstance(popped, list):
            stack.extend(popped)
        elif popped is not None:
            flat_list.append(popped)

    flat_list.reverse()
    return flat_list
