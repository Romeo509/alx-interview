#!/usr/bin/env python3
"""
N queens puzzle solution using backtracking.
"""

import sys


def solve_nqueens(N):
    """
    Solve the N queens puzzle using backtracking.

    Args:
        N (int): The size of the chessboard and number of queens.

    Returns:
        list: A list of solutions, where each solution is
        represented as a list of [row, col] indices.
    """
    def is_safe(row, col):
        """ Check if it's safe to place a queen at board[row][col] """
        return not (cols[col] or diags1[row - col] or diags2[row + col])

    def place_queen(row, col):
        """ Place a queen at board[row][col] """
        board[row] = col
        cols[col] = True
        diags1[row - col] = True
        diags2[row + col] = True

    def remove_queen(row, col):
        """ Remove a queen from board[row][col] """
        board[row] = -1
        cols[col] = False
        diags1[row - col] = False
        diags2[row + col] = False

    def backtrack(row=0):
        """ Backtracking function to find all solutions """
        nonlocal solutions
        if row == N:
            solutions.append([(r, board[r]) for r in range(N)])
            return
        for col in range(N):
            if is_safe(row, col):
                place_queen(row, col)
                backtrack(row + 1)
                remove_queen(row, col)

    solutions = []
    board = [-1] * N  # board[row] = col means there is a queen at (row, col)
    cols = [False] * N  # columns attacked by previous queens
    diags1 = [False] * (2 * N - 1)  # diagonal 1 (top-left to bottom-right)
    diags2 = [False] * (2 * N - 1)  # diagonal 2 (top-right to bottom-left)

    backtrack()
    return solutions


if __name__ == "__main__":
    # Validate input
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Solve N queens problem
    solutions = solve_nqueens(N)

    # Print solutions
    for solution in solutions:
        print(solution)
