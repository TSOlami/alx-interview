#!/usr/bin/python3
"""
Write a method that determines if a given data set
represents a valid UTF-8 encoding.

Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding,
else return False
A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data, therefore you
only need to handle the 8 least significant bits of each integer
"""


def validUTF8(data):
    """Determine if a given data set represents a valid UTF-8 encoding.
    """
    expected_bytes = 0

    # Loop over each byte in the input data
    for byte in data:
        # Check for the leading byte pattern to determine expected bytes
        if (byte & 0b10000000) == 0:  # Single-byte character
            expected_bytes = 0
        elif (byte & 0b11100000) == 0b11000000:  # Two-byte character
            expected_bytes = 1
        elif (byte & 0b11110000) == 0b11100000:  # Three-byte character
            expected_bytes = 2
        elif (byte & 0b11111000) == 0b11110000:  # Four-byte character
            expected_bytes = 3
        else:
            # Invalid leading byte pattern
            return False

        # Check continuation bytes
        if expected_bytes > 0:
            if (byte & 0b11000000) != 0b10000000:
                return False
            expected_bytes -= 1

    # All bytes processed, check if any expected continuation bytes left
    return expected_bytes == 0
