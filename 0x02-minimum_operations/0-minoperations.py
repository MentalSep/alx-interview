#!/usr/bin/python3
""" This module contains the minOperations function """


def minOperations(n):
    """
    This function calculates the minimum number of operations required
    to break down a positive integer n into smaller positive integers
    using prime factorization.
    """
    # operations = 0

    # for factor in range(2, n + 1):
    #     while (n % factor == 0):
    #         operations += factor
    #         n = n // factor
    #     factor += 1

    # return (operations)
    if n <= 1:
        return 0

    operations = [0] * (n + 1)
    for i in range(2, n + 1):
        if n % i == 0:
            operations[i] = i

    for i in range(2, n + 1):
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                operations[i] = min(operations[i],
                                    operations[j] + operations[i // j])

    return operations[n]
