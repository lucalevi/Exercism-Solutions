"""matching_brackets.py
This module provides a function to check if all brackets in a given string
are properly paired and nested.
"""


def is_paired(input_string: str) -> bool:
    """Check if all brackets in the input string are properly paired and nested.
    Args:
        input_string (str): The string to check for matching brackets.
    Returns:
        bool: True if all brackets are properly paired and nested, False otherwise.
    """

    stack = []
    brackets = {"(": ")", "{": "}", "[": "]"}

    for char in input_string:
        if char in brackets:
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                return False
    # If stack is empty, all brackets were matched; otherwise, they were not
    return not stack
