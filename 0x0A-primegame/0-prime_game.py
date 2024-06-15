#!/usr/bin/python3
""" Prime Game"""


def isWinner(x, nums):
    if x < 1 or not nums:
        return None

    max_num = max(nums)

    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False

    p = 2
    while (p * p <= max_num):
        if sieve[p]:
            for i in range(p * p, max_num + 1, p):
                sieve[i] = False
        p += 1

    primes = [p for p in range(max_num + 1) if sieve[p]]

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_count = sum(1 for prime in primes if prime <= n)
        if primes_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
