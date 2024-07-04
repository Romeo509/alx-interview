#!/usr/bin/python3
"""
N-Queens Problem Solver

This program solves the N-Queens problem, which
involves placing N queens on an NxN chessboard
such that no two queens threaten each other. It uses
a recursive backtracking approach to find
all possible solutions.

Usage:
    nqueens.py N

Args:
    N (int): The size of the chessboard and the number of queens.

Constraints:
    N >= 4

Example:
    $ python nqueens.py 4
    [[0, 1], [1, 3], [2, 0], [3, 2]]
    [[0, 2], [1, 0], [2, 3], [3, 1]]

"""

from sys import argv


def is_valid_queen_placement(current_board: list) -> bool:
    """ Check if the current queen placement is valid """
    current_row = len(current_board) - 1
    for prev_row in range(current_row):
        diff = abs(current_board[prev_row] - current_board[current_row])
        if diff == 0 or diff == current_row - prev_row:
            return False
    return True


def solve_nqueens(
    board_size: int, current_row: int, current_board: list, solutions: list
):
    """ Recursively solve the N-Queens problem """
    if current_row == board_size:
        print(solutions)
    else:
        for column in range(board_size):
            current_board.append(column)
            solutions.append([current_row, column])
            if is_valid_queen_placement(current_board):
                solve_nqueens(
                    board_size, current_row + 1, current_board, solutions
                )
            current_board.pop()
            solutions.pop()


if len(argv) != 2:
    print('Usage: nqueens.py N')
    exit(1)

try:
    board_size = int(argv[1])
except ValueError:
    print('N must be a number')
    exit(1)

if board_size < 4:
    print('N must be at least 4')
    exit(1)

else:
    solutions = []
    current_row = 0
    solve_nqueens(board_size, current_row, [], solutions)
