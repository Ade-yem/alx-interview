#!/usr/bin/env python3
"""Minimum Operations"""


def minOperations(n):
    """calculates the fewest number of operations needed
    to result in exactly n H characters in the file"""
    init = "H"
    ops = 1
    if n > 0:    
        for _ in range(n):
            # ops += 1
            if (ops % 3 == 0):
                init += init
            else:
                init += "H"
            ops += 1
            if len(init) >= n:
                return ops
    return 0

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

