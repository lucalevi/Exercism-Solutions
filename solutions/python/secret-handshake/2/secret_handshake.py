"""
This module provides a function to convert a binary string into a secret handshake sequence.
"""

def commands(binary_str: str) -> list[str]:
    """
    Converts a binary string (representing a number between 1 and 31)
    into a sequence of secret handshake actions.

    The actions are determined by the rightmost five digits of the binary string,
    starting from the right-most digit and moving left.

    Actions:
    - 00001 (1st bit): wink
    - 00010 (2nd bit): double blink
    - 00100 (3rd bit): close your eyes
    - 01000 (4th bit): jump
    - 10000 (5th bit): Reverse the order of the operations.

    Args:
        binary_str: A string representing a binary number (e.g., "00011").
                    It is assumed to be at most 5 digits long and represent
                    a number between 1 and 31.

    Returns:
        A list of strings, where each string is an action in the secret handshake.

    Examples:
        >>> commands("00001")
        ['wink']
        >>> commands("00011")
        ['wink', 'double blink']
        >>> commands("10010")
        ['jump', 'double blink']
        >>> commands("11010") # 26 in binary
        ['jump', 'double blink']
    """
    actions_map = {
        0: "wink",
        1: "double blink",
        2: "close your eyes",
        3: "jump"
    }

    secret_shake = []
    should_reverse = False

    # Iterate through the binary string from right to left with index
    for i, digit in enumerate(reversed(binary_str)):
        if digit == "1":
            if i < 4:  # For the first four action bits
                secret_shake.append(actions_map[i])
            elif i == 4:  # For the reverse bit
                should_reverse = True

    if should_reverse:
        secret_shake.reverse()  # In-place reversal for efficiency

    return secret_shake
