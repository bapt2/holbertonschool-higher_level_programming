#!/usr/bin/python3
""" Unittest for class Base """
import unittest
from models.base import Base


class Test_Base(unittest.TestCase):
    """ unittest to check the class Base """
    def test_init(self):
        """ tests attribute id """
        j = Base()
        print(j.id, 1)

        j1= Base()
        print(j1.id, 2)

        b = Base()
        print(b.id, 1)

        b = Base(12)
        print(b.id, 12)

        b1 = Base(21)
        print(b1.id, 21)
