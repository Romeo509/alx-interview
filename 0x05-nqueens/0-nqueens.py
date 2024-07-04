#!/usr/bin/python3
"""
N queens puzzle: Place N queens on an NxN chessboard such
that no two queens attack each other.
This script uses backtracking to find and print
all solutions for the N queens problem.
"""

from sys import argv


def is_valid_queen_placement(current_queen: list) -> bool:
    """
    Check if placing a queen in the current position is valid.
    Returns True if valid, False otherwise.
    """
    row_number = len(current_queen) - 1
    difference = 0
    for index in range(0, row_number):
        difference = current_queen[index] - current_queen[row_number]
        if difference < 0:
            difference *= -1
        if difference == 0 or difference == row_number - index:
            return False
    return True


def solve_n_queens(
    board_size: int, current_row: int, current_queen: list, solution: list
):
    """
    Recursively solve the N queens problem and print all solutions.
    """
    if current_row == board_size:
        print(solution)
    else:
        for column in range(0, board_size):
            current_queen.append(column)
            solution.append([current_row, column])
            if is_valid_queen_placement(current_queen):
                solve_n_queens(
                    board_size, current_row + 1, current_queen, solution
                )
            current_queen.pop()
            solution.pop()


if __name__ == '__main__':
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

    solution = []
    current_queen = 0
    solve_n_queens(board_size, current_queen, [], solution)
