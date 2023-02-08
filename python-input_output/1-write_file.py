#!/usr/bin/python3
""" doc """


def write_file(filename="", text=""):
    """ doc """
    with open(filename, 'w') as f:
        f = f.write(text)
        if f == "":
            return
        return f
