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

    steps_count = 0
    while number > 1:
        if number % 2 == 0:
            number = number // 2  # Use integer division
        else:
            number = number * 3 + 1

        steps_count += 1

    return steps_count
