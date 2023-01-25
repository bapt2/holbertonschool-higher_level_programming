#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n_m = []
    for i in range(len(matrix)):
        n_m.append(list(map((lambda x: x ** 2), matrix[i])))
    return n_m
