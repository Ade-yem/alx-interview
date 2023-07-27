#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """UTF-8 Validator"""
    lis = [i for i in range(0, 128)]
    for j in data:
        if j not in lis:
            return False
    return True
