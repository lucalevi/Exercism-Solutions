"""
Collatz Conjecture
The Collatz conjecture is a mathematical conjecture that concerns sequences defined as follows:
- Start with any positive integer n.
- If n is even, divide it by 2.
- If n is odd, multiply it by 3 and add 1.
- Repeat the process indefinitely.
The conjecture states that no matter what value of n, the sequence will eventually reach 1
and then continue in the cycle 1, 4, 2, 1, ...
"""


def is_valid_input(number):
    """
    Check if the input is a valid positive integer.

    :param number: The input to check.
    :return: True if the input is a positive integer, False otherwise.
    """
    return isinstance(number, int) and number > 0


def collatz_steps(number):
    """
    Calculate the number of steps to reach 1 in the Collatz sequence starting from a given positive integer.

    :param number: A positive integer to start the Collatz sequence.
    :return: The number of steps taken to reach 1.
    :raises ValueError: If the input number is not a positive integer.
    """
    if number == 1:
        return 0

    # Determine the next number in the sequence and store it in a variable
    next_number = number // 2 if number % 2 == 0 else 3 * number + 1

    # Return 1 plus the result of the recursive call on the next number
    return 1 + collatz_steps(next_number)


def steps(number):
    """
    Calculate the number of steps to reach 1 in the Collatz sequence starting from a given positive integer.

    :param number: A positive integer to start the Collatz sequence.
    :return: The number of steps taken to reach 1.
    :raises ValueError: If the input number is not a positive integer.
    """
    if not is_valid_input(number):
        raise ValueError("Only positive integers are allowed")

    return collatz_steps(number)
