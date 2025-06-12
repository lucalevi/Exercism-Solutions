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
        >>> commands("01001")
        ['wink', 'jump']
        >>> commands("11010") # 26 in binary
        ['jump', 'double blink']
    """
    actions = ["wink", "double blink", "close your eyes", "jump"] 
    
    secret_shake = [act for bit, act in zip(binary_str[::-1], actions) if bit == "1"]
                
    if binary_str[0] == "1":
        secret_shake = secret_shake[::-1]
        
    return secret_shake