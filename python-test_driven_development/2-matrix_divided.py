#!/usr/bin/python3
""" divide a matrix """


def matrix_divided(matrix, div):
    """ divide a matrix """
    n_m = [[]]
    te = TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
    
    if type(div) is not int or type(div) is not float:
        raise TypeError("div must be a number")
    if len(matrix) is not int or len(matrix) is not float:
        raise te
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in range(len(matrix)):
        n_m.append(list(map((lambda x: round(x / div, 2)), matrix[i])))
    return n_m
