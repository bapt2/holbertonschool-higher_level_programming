#!/usr/bin/python3
""" class that inherits """



class MyList(list):
    """ class MyList that inherits from list """
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        if not isinstance(MyList, int):
            raise TypeError("MyList must be a int")
        print(sorted(self))
