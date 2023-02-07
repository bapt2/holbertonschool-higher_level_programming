#!/usr/bin/python3
""" Rectangle that inherits from BaseGeometry """


BaseGeometry = __import__('7-base_geometry').BaseGeometry
bg = BaseGeometry()
class Rectangle:
    """ Rectangle that inherits from BaseGeometry """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        bg.integer_validator(width, height)
