#!/usr/bin/python3
""" function like isinstance """


def is_same_class(obj, a_class):
    """ function like isinstance """
    if type(obj) is a_class:
        return True
    else:
        return False
