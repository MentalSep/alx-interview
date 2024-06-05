#!/usr/bin/python3
""" MakeChange Module"""


def makeChange(coins, total):
    """ Given a pile of coins of different values, determine the fewest number
        of coins needed to meet a given amount total"""
    if total <= 0:
        return 0
    if not coins:
        return -1

    coins.sort(reverse=True)

    count = 0
    for coin in coins:
        while total >= coin:
            total -= coin
            count += 1

    return count if total == 0 else -1
