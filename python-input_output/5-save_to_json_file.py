#!/usr/bin/python3
""" doc """


import json


def save_to_json_file(my_obj, filename):
    """ doc """
    with open(filename, 'w') as f:
        return json.dump(my_obj, f)
