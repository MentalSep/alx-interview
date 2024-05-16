#!/usr/bin/python3
"""This module solves the N queens problem."""
import sys


if __name__ == "__main__":
    """initializes the program and checks for the correct usage and input"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    def isSafe(board, row, col):
        """Checks if a queen can be placed on board at row, col."""
        for c in range(col):
            if board[c] == row or abs(board[c] - row) == abs(c - col):
                return False
        return True

    def solve(board, col):
        """Solves the N queens problem."""
        if col == n:
            print(str([[c, board[c]] for c in range(n)]))
            return

        for row in range(n):
            if isSafe(board, row, col):
                board[col] = row
                solve(board, col + 1)

    solve([0 for col in range(n)], 0)
