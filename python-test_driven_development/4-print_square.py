#!/usr/bin/python3
""" print a square """


def print_square(size):
    """ print a square """
    te = TypeError("size must be an integer")
    if type(size) is float and size < 0:
        raise te
    if type(size) is not int:
        raise te
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
