#!/usr/bin/python3
""" class Student """


class Student:
    """ """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if  isinstance(attrs, list):
            nl = {}
            for key, value in self.__dict__.items():
                for element in attrs:
                    if key == element:
                        nl[key] = value
            return nl
        else:
            return self.__dict__
