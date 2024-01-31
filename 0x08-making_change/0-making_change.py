#!/usr/bin/python3
"""Changes come from within"""


def makeChange(coins, total):
    """makeChange computes the minimum coins needed to reach
     a target total using a given set of coin values."""
    if total <= 0:
        return 0

    # Initialize a list to store the minimum number of coins for each total value
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through each coin value and update the minimum number of coins
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1

def rotate_2d_matrix(matrix):
    """rotate_2d_matrix rotates a 2D matrix clockwise."""
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
