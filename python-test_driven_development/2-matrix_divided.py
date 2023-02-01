#!/usr/bin/python3
""" divide a matrix """


def matrix_divided(matrix, div):
    """ divide a matrix """
    te = TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")

    if len(matrix) == 0 or len(matrix[0]) == 0:
        raise te
    if not isinstance(matrix, list):
        raise te
    for n_m in matrix:
        if not isinstance(n_m, list):
            raise te
    for n_m in matrix:
        for i in n_m:
            if not isinstance(i, int) and not isinstance(i, float):
                raise te

    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    n_m = matrix[:]
    return [[round(i/div, 2) for i in row] for row in n_m]
