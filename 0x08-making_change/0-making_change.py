#!/usr/bin/python3
"""Change comes from within"""


def makeChange(coins, total):
    count = 0
    coins.sort(reverse=True)
    index = 0
    while total > 0 and index < len(coins) - 1:
        if total - coins[index] >= 0:
            total -= coins[index]
            count += 1
        else:
            index += 1
        if total == 0:
            return count
    return -1
