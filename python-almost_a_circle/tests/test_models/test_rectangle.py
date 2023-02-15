 #!/usr/bin/python3
""" unittest """


import unittest
from models.rectangle import Rectangle
from models.base import Base

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
