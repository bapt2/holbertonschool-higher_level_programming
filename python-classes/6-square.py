#!/usr/bin/python3
""" Square """


class Square:
    """ Square """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.position = position
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__size

    @position.setter
    def position(self, value):
        s = "position must be a tuple of 2 positive integers"
        if type(value) is not tuple:
            raise TypeError(s)
        if value[0] < 0:
            raise TypeError(s)
        if value[1] < 0:
            raise TypeError(s)
        if len(value) != 2:
            raise TypeError(s)
        if type(value[0]) is not int:
            raise TypeError(s)
        if type(value[1]) is not int:
            raise TypeError(s)

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()
