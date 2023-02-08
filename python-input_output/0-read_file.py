#!/usr/bin/python3
""" doc """


def read_file(filename=""):
    """ doc """
    with open(filename, 'r') as f:
        if filename == "":
            pass
        f = f.read()
        print(f[:-1])
