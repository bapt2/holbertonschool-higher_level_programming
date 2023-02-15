#!/usr/bin/python3
""" base class """


import json


class Base():
    """ this is the base """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file"""
        jf = []
        if list_objs:
            [jf.append(v.to_dictionary()) for v in list_objs]

        with open("%s.json" % (cls.__name__), 'w') as f:
            f.write(cls.to_json_string(jf))
