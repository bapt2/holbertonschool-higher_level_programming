#!/usr/bin/python3
""" unittest """


import unittest
import os
from models.rectangle import Rectangle
from models.base import Base
from io import StringIO
from contextlib import redirect_stdout

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
        r1 = Rectangle(2, 3, 1, 1)
        eo = '\n ##\n ##\n ##\n'
        with StringIO() as buffer, redirect_stdout(buffer):
            r1.display()
            result = buffer.getvalue()
        self.assertEqual(result, eo)

        r = Rectangle(1, 2, 3, 4)
        r.update(89)
        self.assertEqual(r.id, 89)
        r.update(89, 3)
        self.assertEqual(r.width, 3)

        r = Rectangle(14, 16, 12, 15, 25)
        self.assertEqual(str(r), "[Rectangle] (25) 12/15 - 14/16")

        r = Rectangle(10, 2, 1, 9, 7)
        self.assertEqual(r.to_dictionary(), {"id": 7, "width": 10,
                                             "height": 2, "x": 1, "y": 9})

        r = Rectangle.create(**{"id": 7, "width": 10,
                                "height": 2, "x": 1, "y": 9})
        rep = Rectangle(10, 2, 1, 9, 7)
        self.assertEqual(str(r), str(rep))
        r = Rectangle.create(**{"id": 7, "width": 10,
                                "height": 2, "x": 1})
        rep = Rectangle(10, 2, 1, 0, 7)
        self.assertEqual(str(r), str(rep))
        r = Rectangle.create(**{"id": 7, "width": 10,
                                "height": 2,})
        rep = Rectangle(10, 2, 0, 0, 7)
        self.assertEqual(str(r), str(rep))

        r = Rectangle(4, 2)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            content = f.read()
        eo = '[{"id": 7, "width": 4, "height": 2, "x": 0, "y": 0}]'
        self.assertEqual(content, eo)
        os.remove("Rectangle.json")

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            content = f.read()
        eo = '[]'
        self.assertEqual(content, eo)
        os.remove("Rectangle.json")

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            content = f.read()
        eo = '[]'
        self.assertEqual(content, eo)
        os.remove("Rectangle.json")
        
        r = Rectangle.load_from_file()
        self.assertTrue(isinstance(r, list))
        self.assertEqual(r, [])
