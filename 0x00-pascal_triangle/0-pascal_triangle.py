#!/usr/bin/python3
"""
0-pascal_triangle
  - Implements the Pascal's Triangle algorithm.
  - Takes an integer 'n' as input.
  - Returns a list of lists representing the first 'n' rows of Pascal's
    Triangle.
  - Returns an empty list if 'n' is less than or equal to zero.

  This function utilizes dynamic programming to efficiently calculate each row
  based on the previous row's values.
"""


def pascal_triangle(n):
    """
     Calculates and returns the first 'n' rows of Pascal's Triangle.

    Args:
        n (int): The number of rows to generate in the Pascal's Triangle.

    Returns:
        list: A list of lists representing the first 'n' rows of Pascal's
              Triangle.
              An empty list is returned if 'n' is less than or equal to zero.
    """
    p = []
    if n <= 0:
        return p
    p = [[1]]
    for i in range(1, n):
        temp = [1]
        for j in range(len(p[i - 1]) - 1):
            curr = p[i - 1]
            temp.append(p[i - 1][j] + p[i - 1][j + 1])
        temp.append(1)
        p.append(temp)
    return p
