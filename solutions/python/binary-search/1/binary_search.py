"""
Binary Search Implementation
This module provides a function to perform binary search on a sorted list.
"""


def find(search_list: list, value: int) -> int:
    """Perform binary search to find the index of value in search_list."""
    if value not in search_list:
        raise ValueError("value not in array")
    search_list = sorted(search_list)
    low = 0
    high = len(search_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if search_list[mid] < value:
            low = mid + 1
        elif search_list[mid] > value:
            high = mid - 1
        else:
            return mid
    return -1

    # However, it would be easier to use the `index` method of the list:
    # return search_list.index(value)
