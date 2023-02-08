#!/usr/bin/python3
""" doc """


def append_write(filename="", text=""):
    """ doc """
    with open(filename, 'a') as f:
        f = f.write(text)
        return f
