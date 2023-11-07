#!/usr/bin/python3
"""The Pascal's Triangle"""


def pascal_triangle(n):
    """
    Represents the Pascal’s
    triangle of size n
    """

    tri = []
    if n <= 0:
        return tri
    if n == 0:
        return [[1]]

    tri = [[1]]
    for i in range(n-1):
        tri.append([a+b for a, b in zip([0] + tri[-1], tri[-1] + [0])])
    return tri
