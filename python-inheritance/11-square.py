#!/usr/bin/python3
""" Square class that inherit from Rectangle """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class Square that inherit from Rectangle """
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        return (self.__size * self.__size)

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
