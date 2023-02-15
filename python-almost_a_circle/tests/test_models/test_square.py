#!/usr/bin/python3
""" unittest """


import unittest
from models.rectangle import Rectangle
from models.base import Base
from io import StringIO
from models.square import Square

class test_Square(unittest.TestCase):
    """ unittest """
    def test_init(self):
        """ unittest """
        r = Square(6, 4, 2, 18)
        self.assertEqual(r.id, 18)
        self.assertEqual(r.size, 6)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.area(), 36)

        self.assertRaisesRegex(
            TypeError, "size must be an integer", Rectangle, "6", 4, 2, 18)
        self.assertRaisesRegex(
            TypeError, "x must be an integer", Rectangle, 8, 6, "4", 2, 18)
        self.assertRaisesRegex(
            TypeError, "y must be an integer", Rectangle, 8, 6, 4, "2", 18)
        self.assertRaisesRegex(
            ValueError, "size must be > 0", Rectangle, 8, 0, 4, 2, 18)
        self.assertRaisesRegex(
            ValueError, "x must be >= 0", Rectangle, 8, 6, -1, 2, 18)
        self.assertRaisesRegex(
            ValueError, "y must be >= 0", Rectangle, 8, 6, 4, -1, 18)
        self.assertRaisesRegex(TypeError, "", Rectangle, )

        r1 = Square(2, 2)
        eo = '##\n##\n'
        with StringIO() as buffer, redirect_stdout(buffer):
            r1.display()
            result = buffer.getvalue()
        self.assertEqual(result, eo)

        r = Rectangle(3, 7, 5, 9)
        self.assertEqual(r.update().id, 9)
        self.assertEqual(r.update().size, 3)
        self.assertEqual(r.update().x, 7)
        self.assertEqual(r.update().y, 5)

        r = Rectangle(16, 12, 15, 25)
        self.assertEqual(str(r), "[Rectangle] (25) 12/15 - 16")
