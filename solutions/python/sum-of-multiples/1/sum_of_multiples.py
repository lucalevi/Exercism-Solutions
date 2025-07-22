"""
Module for calculating the sum of multiples of given factors below a specified limit.
"""


def sum_of_multiples(limit, multiples):
    """
    Calculate the sum of all unique multiples of given factors below a specified limit.

    :param limit: The upper limit (exclusive) for the multiples.
    :param multiples: A list of factors to consider for finding multiples.
    :return: The sum of all unique multiples of the factors below the limit.
    """
    return sum(
        {
            i
            for i in range(0, limit)
            for mult in multiples
            if mult != 0 and i % mult == 0
        }
    )
