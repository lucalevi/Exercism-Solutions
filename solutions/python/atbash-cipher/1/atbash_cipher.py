"""
Atbash Cipher implementation.
This module provides functions to encode and decode text using the Atbash cipher.
"""

# atbash encoding/decoding dictionary
atbash_cipher = {
    "a": "z",
    "b": "y",
    "c": "x",
    "d": "w",
    "e": "v",
    "f": "u",
    "g": "t",
    "h": "s",
    "i": "r",
    "j": "q",
    "k": "p",
    "l": "o",
    "m": "n",
    "n": "m",
    "o": "l",
    "p": "k",
    "q": "j",
    "r": "i",
    "s": "h",
    "t": "g",
    "u": "f",
    "v": "e",
    "w": "d",
    "x": "c",
    "y": "b",
    "z": "a",
}


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
    # Normalize the input text to lowercase and filter out non-alphanumeric characters
    filtered_text = "".join(char.lower() for char in plain_text if char.isalnum())

    # Encode the filtered text using the Atbash cipher
    encoded_text = "".join(atbash_cipher.get(char, char) for char in filtered_text)

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
    # Normalize the input text to lowercase and filter out non-alphanumeric characters
    filtered_text = "".join(char.lower() for char in ciphered_text if char.isalnum())

    # Decode the filtered text using the Atbash cipher
    decoded_text = "".join(atbash_cipher.get(char, char) for char in filtered_text)

    return decoded_text
