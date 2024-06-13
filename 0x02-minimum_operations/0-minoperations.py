#!/usr/bin/python3
"""
0-minoperations.py

A function to calculate the fewest number of operations needed to
result in exactly n H characters in the file.

Author: Your Name
"""


def minOperations(n):
    """
    Calculate the minimum number of operations required to
    get exactly n H characters in the file.

    Parameters:
    n (int): The number of H characters desired.

    Returns:
    int: The minimum number of operations required, or 0 if n is
    impossible to achieve.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
