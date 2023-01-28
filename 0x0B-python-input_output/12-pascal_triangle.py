#!/usr/bin/python3
"""This module contains the funtion pascal_triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers
    representing the Pascal's triangle of n"""

    if n <= 0:
        return []
    tri = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i+1):
            if j == i:
                row.append(1)
            else:
                row.append(tri[i-1][j-1] + tri[i-1][j])
        tri.append(row)
    return tri
