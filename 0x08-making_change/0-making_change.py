#!/usr/bin/python3
"""Change comes from within"""


def makeChange(coins, total):
    count = 0
    coins.sort(reverse=True)
    sum = 0
    if total <= 0:
        return 0
    while sum < total:
        for i in coins:
            if sum + i <= total:
                sum += i
                count += 1
                break
            if i == coins[-1] and sum + i > total:
                return -1
    return count
