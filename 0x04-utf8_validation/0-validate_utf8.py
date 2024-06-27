#!/usr/bin/python3
"""UTF-8 Validation"""


def count_leading_ones(byte):
    """Count the number of leading 1 bits in the byte"""
    mask = 1 << 7
    count = 0
    while byte & mask:
        count += 1
        mask >>= 1
    return count


def validUTF8(data):
    """Determine if the given dataset represents a valid UTF-8 encoding"""
    bytes_to_check = 0

    for num in data:
        if bytes_to_check == 0:
            if (num >> 5) == 0b110:
                bytes_to_check = 1
            elif (num >> 4) == 0b1110:
                bytes_to_check = 2
            elif (num >> 3) == 0b11110:
                bytes_to_check = 3
            elif (num >> 7) == 0:
                bytes_to_check = 0
            else:
                return False
        else:
            if (num >> 6) != 0b10:
                return False
            bytes_to_check -= 1

    return bytes_to_check == 0


if __name__ == "__main__":
    data_sets = [
        [65],
        [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33],
        [229, 65, 127, 256]
    ]

    for data in data_sets:
        print(validUTF8(data))
