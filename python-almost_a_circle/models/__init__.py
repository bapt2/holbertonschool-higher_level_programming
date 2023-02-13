#!/usr/bin/python3
""" python package """


def __init__(self, id=None):
    if id != None:
        self.id = id
    else:
        __nb_objects += 1
        id = __nb_objects
