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
        if board[i][col] == 1 or board[i][col - (row - i)] == 1 or board[i][col + (row - i)] == 1:
            return False
    return True


def solve_queens(board, row, N, solutions):
    """
    Solve N queens puzzle using backtracking
    """
    if row == N:
        queens = [[r, c] for r, c in enumerate(board)]
        solutions.append(queens)
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_queens(board, row + 1, N, solutions)
            board[row][col] = 0


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

    board = [[0] * N for _ in range(N)]
    solutions = []
    solve_queens(board, 0, N, solutions)

    for solution in solutions:
        print(solution)


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

