"""
This module provides a collection of common list manipulation functions,
reimplemented without relying on Python's built-in functions of the same name
(where applicable). These functions aim to demonstrate fundamental programming
concepts such as mapping, filtering, folding (reducing), and list
transformation.

Functions included:
- `append`: Concatenates two lists.
- `concat`: Flattens a list of lists into a single list.
- `filter`: Selects elements from a list based on a given predicate function.
- `length`: Calculates the number of elements in a list.
- `map`: Applies a function to each element in a list, returning a new list
         with the transformed elements.
- `foldl`: Reduces (folds) a list from left to right using a binary function
           and an initial accumulator value.
- `foldr`: Reduces (folds) a list from right to left using a binary function
           and an initial accumulator value.
- `reverse`: Reverses the order of elements in a list.
"""

from typing import Callable


def append(list1: list, list2: list) -> list:
    """Concatenate two lists"""
    return list1 + list2


def concat(lists: list[list]) -> list:
    """Flatten a list of lists"""
    flattened = []
    for single_list in lists:
        flattened += single_list
    return flattened


def filter(function: Callable, list: list) -> list:
    """Filter the elements of a list according to a function"""
    return [elem for elem in list if function(elem)]


def length(list: list) -> int:
    """Give the length of a list"""
    return sum(1 for elem in list)


def map(function: Callable, list) -> list:
    """Apply a function to all elements of a list"""
    return [function(elem) for elem in list]


def foldl(function: Callable, list: list, initial: int) -> int:
    """Accumulate values of a list, starting from the left and an intial value,
    according to a function"""
    accumulator = initial

    for elem in list:
        accumulator = function(accumulator, elem)

    return accumulator


def foldr(function: Callable, list: list, initial: int) -> int:
    """Accumulate values of a list, starting from the right and an intial value,
    according to a function"""
    accumulator = initial

    for elem in list[::-1]:
        accumulator = function(accumulator, elem)

    return accumulator


def reverse(list: list) -> list:
    """Reverse the order of a list"""
    return list[::-1]
