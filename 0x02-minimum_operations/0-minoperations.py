#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
	"""
	Given a text file with a single 'H,'
	 the method 'minOperations' calculates the fewest
	 operations needed (Copy All and Paste) to achieve
	 exactly n 'H' characters. Returns 0 if impossible
	"""
    if n <= 1:
        return 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return minOperations(n // i) + i
    return n
