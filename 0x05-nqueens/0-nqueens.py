#!/usr/bin/python3
"""
 N queens puzzle
"""

import sys

def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen at board[row][col]
    """
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True

def solve_queens(board, row, N):
    """
    Solve N queens puzzle using backtracking
    """
    if row == N:
        print("Solution:", [[r, c] for r, c in enumerate(board)])
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            solve_queens(board, row + 1, N)

def nqueens(N):
    """
    Main function to solve N queens puzzle
    """
    if not isinstance(N, int):
        print("Error: N must be a number")
        sys.exit(1)

    if N < 4:
        print("Error: N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solve_queens(board, 0, N)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        nqueens(N)
    except ValueError:
        print("Error: N must be a number")
        sys.exit(1)

