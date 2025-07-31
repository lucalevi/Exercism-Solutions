"""
Atbash Cipher implementation.
This module provides functions to encode and decode text using the Atbash cipher.
"""

import string

# atbash encoding/decoding maketrans table
atbash_cipher = str.maketrans(
    string.ascii_lowercase,
    string.ascii_lowercase[::-1],
    " .,",
)


def encode(plain_text):
    """Encodes the given plain text using the Atbash cipher.

    Ciphertext is written out in groups of fixed length, the traditional group
    size being 5 letters, leaving numbers unchanged, and punctuation is excluded.
    All text will be encoded as lowercase letters.

    Args:
        plain_text (str): The text to encode.

    Returns:
        str: The encoded text.
    """
    # Encode the filtered text using the Atbash cipher
    encoded_text = plain_text.lower().translate(atbash_cipher)

    # Group the encoded text into chunks of 5 characters
    grouped_text = " ".join(
        encoded_text[i : i + 5] for i in range(0, len(encoded_text), 5)
    )

    return grouped_text


def decode(ciphered_text):
    """Decodes the given ciphered text using the Atbash cipher.
    No spaces are added in the output, and all text is returned in lowercase.
    Args:
        ciphered_text (str): The text to decode.

    Returns:
        str: The decoded text.
    """
    # Decode the filtered text using the Atbash cipher
    decoded_text = ciphered_text.translate(atbash_cipher)

    return decoded_text
