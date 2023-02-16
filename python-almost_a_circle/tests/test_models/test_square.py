#!/usr/bin/python3
""" unittest """


import unittest
from models.base import Base
from io import StringIO
from models.square import Square
from contextlib import redirect_stdout
import os

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
        TypeError, "width must be an integer", Square, "6", 4, 2, 18)
        self.assertRaisesRegex(
        TypeError, "x must be an integer", Square, 6, "4", 2, 18)
        self.assertRaisesRegex(
        TypeError, "y must be an integer", Square, 6, 4, "2", 18)
        self.assertRaisesRegex(
        ValueError, "width must be > 0", Square, -1, 4, 2, 18)
        self.assertRaisesRegex(
        ValueError, "x must be >= 0", Square, 6, -1, 2, 18)
        self.assertRaisesRegex(
        ValueError, "y must be >= 0", Square, 6, 4, -1, 18)
        self.assertRaisesRegex(TypeError, "", Square, )

        r1 = Square(2)
        eo = '##\n##\n'
        with StringIO() as buffer, redirect_stdout(buffer):
            r1.display()
            result = buffer.getvalue()
        self.assertEqual(result, eo)
        r1 = Square(2, 1, 1)
        eo = '\n ##\n ##\n'
        with StringIO() as buffer, redirect_stdout(buffer):
            r1.display()
            result = buffer.getvalue()
        self.assertEqual(result, eo)

        r = Square(1, 2, 3, 4)
        r.update(89)
        self.assertEqual(r.id, 89)
        r.update(89, 3)
        self.assertEqual(r.width, 3)

        r = Square(16, 12, 15, 25)
        self.assertEqual(str(r), "[Square] (25) 12/15 - 16")

        r = Square(10, 1, 9, 7)
        self.assertEqual(r.to_dictionary(), {"id": 7, "size": 10, "x": 1, "y": 9})

        r = Square.create(**{"id": 7, "size": 10, "x": 1, "y": 9})
        rep = Square(10, 1, 9, 7)
        self.assertEqual(str(r), str(rep))
        r = Square.create(**{"id": 7, "size": 10, "x": 1})
        rep = Square(10, 1, 0, 7)
        self.assertEqual(str(r), str(rep))
        r = Square.create(**{"id": 7, "size": 10})
        rep = Square(10, 0, 0, 7)
        self.assertEqual(str(r), str(rep))

        r = Square(4, 0, 0, 7)
        Square.save_to_file([r])
        with open("Square.json", "r") as f:
            content = f.read()
        eo = '[{"id": 7, "size": 4, "x": 0, "y": 0}]'
        self.assertEqual(content, eo)
        os.remove("Square.json")

        Square.save_to_file([])
        with open("Square.json", "r") as f:
            content = f.read()
        eo = '[]'
        self.assertEqual(content, eo)
        os.remove("Square.json")

        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            content = f.read()
        eo = '[]'
        self.assertEqual(content, eo)
        os.remove("Square.json")

        r1 = Square(50)
        Square.save_to_file([r1])
        squares = Square.load_from_file()
        self.assertIsInstance(squares[0], Square)
        self.assertEqual(squares[0].size, 50)
        os.remove("Square.json")

        r = Square.load_from_file()
        self.assertTrue(isinstance(r, list))
        self.assertEqual(r, [])
