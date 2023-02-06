#!/usr/bin/python3
""" Same class or inherit from """


def is_kind_of_class(obj, a_class):
    """ Same class or inherit from """
    if type(obj) is a_class or isinstance(obj, a_class):
        return True
    else:
        return False
