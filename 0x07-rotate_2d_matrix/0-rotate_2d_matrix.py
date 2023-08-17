#!/usr/bin/python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """matrix rotator"""
    n = len(matrix)
    # transpose between rows and columns
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # reversing each nested list
    for i in range(n):
        matrix[i] = matrix[i][::-1]
