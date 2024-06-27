#!/usr/bin/python3
"""UTF-8 Validation"""


def get_leading_set_bits(num):
    """Returns the number of leading set bits (1)"""
    helper = 1 << 7
    set_bits = 0
    while helper & num:
        set_bits += 1
        helper = helper >> 1
    return set_bits


def validUTF8(data):
    """Determines if a given dataset represents a valid UTF-8 encoding"""
    bits_count = 0
    i = 0

    while i < len(data):
        if bits_count == 0:
            bits_count = get_leading_set_bits(data[i])

            if bits_count == 0:
                i += 1
                continue

            if bits_count == 1 or bits_count > 4:
                return False
        else:
            if not (data[i] & (1 << 7) and not (data[i] & (1 << 6))):
                return False

        bits_count -= 1
        i += 1

    return bits_count == 0
