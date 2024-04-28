#!/usr/bin/python3
""" This module contains the minOperations function """


def minOperations(n):
    """
    This function calculates the minimum number of operations required
    to break down a positive integer n into smaller positive integers
    using prime factorization.
    """
    operations = 0
    factor = 2

    while n > 1:
      if n % factor == 0:
        operations += factor
        n //= factor
      else:
        factor += 1

    return operations
