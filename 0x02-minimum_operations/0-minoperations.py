#!/usr/bin/python3
""" This module contains the minOperations function """


def minOperations(n):
    """
    This function calculates the minimum number of operations required
    to break down a positive integer n into smaller positive integers
    using prime factorization.
    """
    if (type(n) is not int or n <= 1):
        return (0)
    operations = 0

    for factor in range(2, n + 1):
        while (n % factor == 0):
            operations += factor
            n = n // factor
        factor += 1

    return (operations)
