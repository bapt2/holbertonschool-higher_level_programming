#!/usr/bin/python3
""" Unittest for class Base """
import unittest
from models.base import Base


class Test_Base(unittest.TestCase):
    """ unittest to check the class Base """
    def test_init(self):
        """ tests attribute id """
        j = Base()
        self.assertEqual(j.id, 1)

        j1= Base()
        self.assertEqual(j1.id, 2)
        
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

        b2 = Base(21)
        self.assertEqual(b2.id, 21)
