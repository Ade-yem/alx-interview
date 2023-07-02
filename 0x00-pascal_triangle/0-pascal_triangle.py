#!/usr/bin/python3
"""Pascal's Triangle"""

def pascal_triangle(n):
    """pascal's triangle"""
    if n <= 0:
        return []
    triangle = []    
    for i in range(n):
        array = [1] * (i + 1)
        for j in range(1, len(array) - 1):
            prev = triangle[i - 1]
            array[j] = prev[j - 1] + prev[j]
        triangle.append(array)
    return triangle