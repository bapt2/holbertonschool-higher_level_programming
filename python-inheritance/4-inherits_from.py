#!/usr/bin/python3
""" class that inherited (directly or indirectly) """


def inherits_from(obj, a_class):
    """ class that inherited (directly or indirectly) """
    if type(obj) is not a_class and isinstance(obj, a_class):
        return True
    else:
        return False
