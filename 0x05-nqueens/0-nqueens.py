#!/usr/bin/python3
"""Solving the Queens Dilemma"""
import sys


def show_queen_positions(queen_arrangements):
    """Displays the coordinates of the queens"""
    for arrangement in queen_arrangements:
        print(arrangement)


def is_safe_placement(chessboard, row, col):
    """Checks if placing a queen at a given position is safe"""
    board_size = len(chessboard)

    for i in range(row):
        if chessboard[i][col] == 1 or \
           (0 <= col - row + i < board_size and chessboard[i][col - row + i] == 1) or \
           (0 <= col + row - i < board_size and chessboard[i][col + row - i] == 1):
            return False

    return True


def explore_board(chessboard, row, solutions):
    """Solves the problem using Backtracking"""
    board_size = len(chessboard)

    if row == board_size:
        queens = [[i, j] for i in range(board_size)
                  for j in range(board_size) if chessboard[i][j] == 1]
        solutions.append(queens)
        return

    for col in range(board_size):
        if is_safe_placement(chessboard, row, col):
            chessboard[row][col] = 1
            explore_board(chessboard, row + 1, solutions)
            chessboard[row][col] = 0


def solve_queens_problem(board_size):
    """Finds solutions to the Queens Dilemma"""
    solutions = []
    chessboard = [[0 for _ in range(board_size)] for _ in range(board_size)]
    explore_board(chessboard, 0, solutions)
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        board_size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if board_size < 4:
        print("N must be at least 4")
        sys.exit(1)

    queen_solutions = solve_queens_problem(board_size)
    show_queen_positions(queen_solutions)


