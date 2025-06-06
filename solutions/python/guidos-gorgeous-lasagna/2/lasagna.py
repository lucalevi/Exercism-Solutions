"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes.

    :param number_of_layers: int - the number of layers of a lasagna.
    :return: int - the preparation time for all layers specified by the argument.

    Function that calculates the preparation time (in minutes) for a given set of
    layers of the lasagna. 
    """
    return number_of_layers * PREPARATION_TIME



def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed time in minutes of the lasagna preparation.

    :param number_of_layers: int - the number of layers of a lasagna.
    :param elapsed_bake_time: int - the already elapsed bake time of the (in-oven)
    lasagna.
    :return: int - the time used for the preparation of the lasgna, in minutes,
    constituted by the time used for assembling the lasagna and the already 
    elapsed bake time.

    Function that calculates the preparation time (in minutes) for a given set of
    layers of the lasagna. 
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time