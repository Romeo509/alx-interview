#!/usr/bin/python3
"""UTF-8 Validation"""


def get_leading_set_bits(num):
    """Returns the number of leading set bits (1)"""
    set_bits = 0
    helper = 1 << 7
    while helper & num:
        set_bits += 1
        helper = helper >> 1
    return set_bits


def validUTF8(data):
    """Determines if a given dataset represents a valid UTF-8 encoding"""
    bits_count = 0

    for i in range(len(data)):
        if not check_byte(data[i], bits_count):
            return False

        bits_count -= 1

    return bits_count == 0


def check_byte(byte, bits_count):
    """Checks if a byte is valid according to UTF-8 encoding rules"""
    if bits_count == 0:
        bits_count = get_leading_set_bits(byte)

        if bits_count == 0:
            return True

        if bits_count == 1 or bits_count > 4:
            return False
    else:
        if not (byte & (1 << 7) and not (byte & (1 << 6))):
            return False

    return True


if __name__ == "__main__":
    data_sets = [
        [65],
        [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33],
        [229, 65, 127, 256]
    ]

    for data in data_sets:
        print(validUTF8(data))
