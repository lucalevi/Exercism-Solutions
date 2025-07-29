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


def steps(number):
    """
    Calculate the number of steps to reach 1 in the Collatz sequence starting from a given positive integer.

    :param number: A positive integer to start the Collatz sequence.
    :return: The number of steps taken to reach 1.
    :raises ValueError: If the input number is not a positive integer.
    """
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    if number == 1:
        return 0

    # If the number is not one, we shall see if it is even or odd
    # We will then need a counter to count the steps

    if number % 2 == 0:
        return steps(number // 2) + 1
    else:
        return steps(3 * number + 1) + 1
