#!/usr/bin/python3
""" a module containing the funtion pascal_triangle """


def pascal_triangle(n):
    """ returns a list of lists of integers
        representing the Pascals triangle of n
    """
    if n <= 0:
        return []
    t = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i+1):
            if j == i:
                row.append(1)
            else:
                row.append(t[i-1][j-1] + t[i-1][j])
        t.append(row)
    return t
