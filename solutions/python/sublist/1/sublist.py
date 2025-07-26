"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one, list_two):
    """Determine the relationship between two lists.
    Args:
        list_one (list): The first list to compare.
        list_two (list): The second list to compare.
    Returns:
        int: One of the enumerated constants indicating the relationship.
    """

    def is_sublist(smaller, bigger):
        if not smaller:  # Empty list is a sublist of any list
            return True
        if len(smaller) > len(bigger):
            return False
        return any(
            bigger[i : i + len(smaller)] == smaller
            for i in range(len(bigger) - len(smaller) + 1)
        )  # Check if smaller is a sublist of bigger

    if list_one == list_two:
        return EQUAL
    elif is_sublist(list_two, list_one):
        return SUPERLIST
    elif is_sublist(list_one, list_two):
        return SUBLIST
    else:
        return UNEQUAL
