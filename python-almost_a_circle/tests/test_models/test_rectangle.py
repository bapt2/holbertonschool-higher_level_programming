#!/usr/bin/python3
""" unittest """


import unittest
from models.rectangle import Rectangle
from models.base import Base
from io import StringIO

class test_Rectangle(unittest.TestCase):
    """ unittest """
    def test_init(self):
        """ unittest """
        r = Rectangle(8, 6, 4, 2, 18)
        self.assertEqual(r.id, 18)
        self.assertEqual(r.width, 8)
        self.assertEqual(r.height, 6)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.area(), 48)

        self.assertRaisesRegex(
            TypeError, "width must be an integer", Rectangle, "8", 6, 4, 2, 18)
        self.assertRaisesRegex(
            TypeError, "height must be an integer", Rectangle, 8, "6", 4, 2, 18)
        self.assertRaisesRegex(
            TypeError, "x must be an integer", Rectangle, 8, 6, "4", 2, 18)
        self.assertRaisesRegex(
            TypeError, "y must be an integer", Rectangle, 8, 6, 4, "2", 18)
        self.assertRaisesRegex(
            ValueError, "width must be > 0", Rectangle, 0, 6, 4, 2, 18)
        self.assertRaisesRegex(
            ValueError, "height must be > 0", Rectangle, 8, 0, 4, 2, 18)
        self.assertRaisesRegex(
            ValueError, "x must be >= 0", Rectangle, 8, 6, -1, 2, 18)
        self.assertRaisesRegex(
            ValueError, "y must be >= 0", Rectangle, 8, 6, 4, -1, 18)
        self.assertRaisesRegex(TypeError, "", Rectangle, )


        r1 = Rectangle(2, 3)
        eo = '##\n##\n##\n'
        with StringIO() as buffer, redirect_stdout(buffer):
            r1.display()
            result = buffer.getvalue()
        self.assertEqual(result, eo)

        r = Rectangle(2, 3, 7, 5, 9)
        self.assertEqual(r.update().id, 9)
        self.assertEqual(r.update().width, 2)
        self.assertEqual(r.update().height, 3)
        self.assertEqual(r.update().x, 7)
        self.assertEqual(r.update().y, 5)

        r = Rectangle(14, 16, 12, 15, 25)
        self.assertEqual(str(r), "[Rectangle] (25) 12/15 - 14/16")

        
