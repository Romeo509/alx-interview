#!/usr/bin/python3
"""
UTF-8 Validation script
"""


def validUTF8(data):
    """
    Checks if the data represents a valid UTF-8 encoding.

    Args:
    data (list of int): The data to be checked.

    Returns:
    bool: True if data is valid UTF-8, else False.
    """
    num_bytes = 0

    for byte in data:
        if byte > 255:
            return False

        if num_bytes == 0:
            if (byte >> 7) == 0b0:
                num_bytes = 0
            elif (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            else:
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0
