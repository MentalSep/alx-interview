#!/usr/bin/python3
""" Prime Game"""


def isWinner(x, nums):
    """ Prime Game """
    def is_prime(n):
        """ Check if a number is prime"""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_winner(n):
        """ Get the winner of the game"""
        primes = [i for i in range(2, n + 1) if is_prime(i)]
        if not primes:
            return 'Ben'
        return 'Maria' if len(primes) % 2 != 0 else 'Ben'

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = get_winner(n)
        if winner == 'Maria':
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
