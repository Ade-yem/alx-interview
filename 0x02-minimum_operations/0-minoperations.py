#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """calculates the fewest number of operations needed
    to result in exactly n H characters in the file"""
    ops = 0
    div = 2
    if n < 1:
        return 0
    while n > 1:
        while n % div == 0:
            ops += div
            n //= div
        div += 1
    return ops
