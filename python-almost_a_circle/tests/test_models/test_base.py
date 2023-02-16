#!/usr/bin/python3
""" Unittest for class Base """
import unittest
from models.base import Base
from io import StringIO


class Test_Base(unittest.TestCase):
    """ unittest to check the class Base """
    def test_init(self):
        """ tests attribute id """
        b = Base()
        print(b.id, 1)

        b = Base(12)
        print(b.id, 12)

        b1 = Base(21)
        print(b1.id, 21)

        b2 = Base()
        print(b2.id, 1)

        b3= Base()
        print(b3.id, 2)
