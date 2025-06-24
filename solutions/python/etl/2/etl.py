"""This is a module for transforming a dictionary into another dictionary of different structure."""


def transform(legacy_data: dict[int : list[str]]) -> dict[str:int]:
    """Transform a dictionary of point-letter type to a dictionary of letter-point type."""

    return {letter.lower(): key for key in legacy_data for letter in legacy_data[key]}
