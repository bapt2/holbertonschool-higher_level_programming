#!/usr/bin/python3
""" pascal triangle """


def pascal_triangle(n):
    """ pascal triangle """
    if n <= 0:
        return []

    a = []
    b = []
    for i in range(n):
        if i == 0:
            a.append([1])
        else:
            b = [1]
            for j in range(i - 1):
                b.append(a[i - 1][j] + a[i - 1][j + 1])
            b.append(1)
            a.append(b)
    return a
