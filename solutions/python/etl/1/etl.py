"""Contains a module for transforming a dictionary into another dictionary of different structure"""


def transform(legacy_data: dict) -> dict:
    """Transform a dictionary of point-letter type to a dictionary of letter-point type"""
    data = {}

    for key in legacy_data.keys():
        for letter in legacy_data[key]:
            data[letter.lower()] = key

    return data
