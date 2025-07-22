"""
Module for calculating a gigasecond from a given moment in time.
This module provides a function to add one gigasecond (10^9 seconds)
to a given datetime object.
"""

import datetime

GIGA = 10**9


def add(moment):
    """Add one gigasecond to the given moment in time.

    Args:
        moment (datetime): A datetime object representing the moment in time.

    Returns:
        datetime: A new datetime object with one gigasecond added.
    """
    if not isinstance(moment, datetime.datetime):
        raise TypeError("Input must be a datetime object")
    if moment.tzinfo is not None:
        raise ValueError("Input datetime must be timezone-naive")
    if moment.microsecond != 0:
        raise ValueError("Input datetime must have zero microseconds")

    return moment + datetime.timedelta(seconds=GIGA)
