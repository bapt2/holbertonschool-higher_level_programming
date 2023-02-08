#!/usr/bin/python3
""" square inherit from rectangle """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ square inherit from rectangle """
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        return(self.__size * self.__size)
