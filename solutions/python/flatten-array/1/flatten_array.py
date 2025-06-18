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
    for item in iterable:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        elif item is not None:
            flat_list.append(item)
    return flat_list
