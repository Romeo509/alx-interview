#!/usr/bin/env python3

import sys


def is_safe(board, row, col):
    """ Check if it's safe to place a queen at board[row][col] """

    # Check column
    for i in range(row):
        if board[i] == col:
            return False

        # Check upper diagonal on left side
        if board[i] - i == col - row:
            return False

        # Check upper diagonal on right side
        if board[i] + i == col + row:
            return False

    return True


def solve_nqueens(n):
    """ Recursive function to solve N queens problem """

    board = [-1] * n
    solutions = []

    def backtrack(row):
        """ Backtracking function """

        if row == n:
            solutions.append(board[:])
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    backtrack(0)
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <n>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 1:
            raise ValueError("N must be a positive integer")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    solutions = solve_nqueens(n)
    for solution in solutions:
        print([[i, solution[i]] for i in range(n)])
