#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """
    Given a text file with a single 'H,'
    the method 'minOperations' calculates the fewest
    operations needed (Copy All and Paste) to achieve
    exactly n 'H' characters. Returns 0 if impossible.
    """
    if n <= 1:
        return 0

    for x in range(2, n + 1):
        if n % x == 0:
            return minOperations(n // x) + x

    return n

