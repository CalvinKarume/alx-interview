#!/usr/bin/python3
"""Changes come from within"""


def rotate_2d_matrix(matrix):
    """makeChange computes the minimum coins needed to reach
     a target total using a given set of coin values.."""
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
