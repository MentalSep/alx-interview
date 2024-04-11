#!/usr/bin/python3
"""Module for pascal_triangle"""


def pascal_triangle(n):
    """Function that returns a list of lists of integers representing
    the Pascal triangle of n"""
    if n <= 0:
        return []
    tringale = []
    for i in range(n):
        if i == 0:
            tringale.append([1])
        elif i == 1:
            tringale.append([1, 1])
        else:
            row = [1]
            for j in range(1, i):
                row.append(tringale[i - 1][j - 1] + tringale[i - 1][j])
            row.append(1)
            tringale.append(row)
    return tringale
