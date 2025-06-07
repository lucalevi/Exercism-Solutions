"""
Module containing a to_rna function that translates a DNA strand
into the respective RNA equivalent.
"""


def to_rna(dna_strand: str) -> str:
    """
    Converts a DNA strand into an RNA strand.
    Uses a dna_to_rna conversion dictionary and a list comprehension
    to convert the DNA strand into an RNA one.
    
    Args:
        dna_strand (str): the DNA strand to be converted.
    
    Returns:
        str: the converted RNA strand.
    """
    # DNA/RNA conversion dictionary
    dna_to_rna = {
        "G": "C",
        "C": "G",
        "T": "A",
        "A": "U"
    }

    # Make dna_strand from str to list
    dna_list = list(dna_strand)

    # Generate a list of rna nucleotides
    rna_list = [dna_to_rna[nucl] for nucl in dna_strand]

    # Join the rna list into a string
    return "".join(rna_list)
