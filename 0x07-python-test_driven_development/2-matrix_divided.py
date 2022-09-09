#!/usr/bin/python3
"""Module containing funtion matrix_divided

Methods:
    matrix_divided(): divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix.
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) is int:
        div = float(div)
    if type(div) is not float:
        raise TypeError("div must be a number")
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for i in range(len(matrix)):
        if type(matrix[i]) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    new_matrix = [list(item) for item in matrix]
    n = len(new_matrix[0])
    for i in range(len(new_matrix)):
        if len(new_matrix[i]) != n:
            raise TypeError("Each row of the matrix must have the same size")
        n = len(new_matrix[i])
        for j in range(len(new_matrix[i])):
            if type(new_matrix[i][j]) is int:
                new_matrix[i][j] = float(new_matrix[i][j])
            if type(new_matrix[i][j]) is not float:
                raise TypeError(
                   "matrix must be a matrix (list of lists) of integers/floats"
                        )
            new_matrix[i][j] = round((new_matrix[i][j] / div), 2)
    return new_matrix
