#!/usr/bin/python3
"""N queens puzzle"""
import sys


def print_solutions(solutions):
    """Prints the coordinates of the queens"""
    for solution in solutions:
        print(solution)


def is_safe(board, row, col):
    """Checks if a queen can be placed on board at the given position"""
    n = len(board)

    for i in range(row):
        if board[i][col] == 1 or \
           (0 <= col - row + i < n and board[i][col - row + i] == 1) or \
           (0 <= col + row - i < n and board[i][col + row - i] == 1):
            return False

    return True


def backtrack(board, row, solutions):
    """sove the problem by Backtracking"""
    n = len(board)

    if row == n:
        queens = [[i, j] for i in range(n)
                  for j in range(n) if board[i][j] == 1]
        solutions.append(queens)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row][col] = 1
            backtrack(board, row + 1, solutions)
            board[row][col] = 0


def solve_nqueens(n):
    """Solves the problem"""
    solutions = []
    board = [[0 for _ in range(n)] for _ in range(n)]
    backtrack(board, 0, solutions)
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    print_solutions(solutions)

