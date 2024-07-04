#!/usr/bin/env python3

import sys


def is_safe(board, row, col):
    """ Check if it's safe to place a queen at board[row][col] """

    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, row):
    """ Recursive function to solve N queens problem """

    # Base case: If all queens are placed, return true
    if row >= len(board):
        return True

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            if solve_nqueens(board, row + 1):
                return True
            board[row][col] = 0

    return False


def nqueens(n):
    """ Function to solve the N queens problem """

    # Initialize an empty board
    board = [[0 for _ in range(n)] for _ in range(n)]

    if not solve_nqueens(board, 0):
        return []

    # Convert board format from 1s and 0s to list of positions
    result = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                result.append([i, j])

    return result


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

    solutions = nqueens(n)
    for solution in solutions:
        print(solution)
