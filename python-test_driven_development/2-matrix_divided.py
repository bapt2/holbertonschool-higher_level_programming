#!/usr/bin/python3
""" divide a matrix """


def matrix_divided(matrix, div):
    """ divide a matrix """
    n_m = [[]]
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
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) is not int or type(div) is not float:
        raise TypeError("div must be a number")

    for i in range(len(matrix)):
        n_m.append(list(map((lambda x: round(x / div, 2)), matrix[i])))
    return n_m
