#!/usr/bin/python3
"""Solves the N-queens puzzle iteratively using backtracking.

Determines all possible solutions to placing N
non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N

N must be an integer greater than or equal to 4.

Attributes:
    solutions (list): A list of lists containing solutions.

Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""
import sys

def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]."""
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 'Q':
            return False
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    return True

def solve_nqueens(n):
    """Iteratively solve the N-queens problem using backtracking."""
    solutions = []
    stack = [([], 0)]
    while stack:
        board, col = stack.pop()
        if col == n:
            solutions.append(board)
        else:
            for row in range(n):
                if is_safe(board, row, col):
                    new_board = board + [(row, col)]
                    stack.append((new_board, col + 1))
    return solutions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)
    for sol in solutions:
        board = [[' ' for _ in range(n)] for _ in range(n)]
        for row, col in sol:
            board[row][col] = 'Q'
        print(board)
