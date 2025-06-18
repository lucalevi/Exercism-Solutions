"""Calculate the Hamming distance between two DNA strands."""


def distance(strand_a, strand_b):
    """Calculate the Hamming distance between two DNA strands."""
    strands = zip(strand_a, strand_b)

    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    return sum(el_a != el_b for el_a, el_b in strands)

    # Alternative using "1" instead of boolean:
    # return sum(1 for el_a, el_b in strands if el_a != el_b)
