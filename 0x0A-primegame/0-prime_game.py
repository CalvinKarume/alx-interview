#!/usr/bin/python3
""" Prime Game """

def isWinner(m, nums):
    if not nums or m < 1:
        return None

    max_num = max(nums)
    sieve = [False] * (max_num + 1)
    primes_count = 0

    for i in range(2, int(max_num ** 0.5) + 1):
        if not sieve[i]:
            for j in range(i * i, max_num + 1, i):
                sieve[j] = True

    for i in range(2, len(sieve)):
        if not sieve[i]:
            primes_count += 1

    maria_primes = sum(1 for n in nums if not sieve[n])
    ben_primes = len(nums) - maria_primes

    if maria_primes > ben_primes:
        return "Maria"
    elif maria_primes < ben_primes:
        return "Ben"
    else:
        return None

