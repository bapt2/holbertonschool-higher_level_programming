#!/usr/bin/python3
""" doc """


def read_file(filename=""):
    """ doc """
    with open(filename, 'r') as f:
        f = f.read()
        if f == "":
            return
        print(f[:-1])
