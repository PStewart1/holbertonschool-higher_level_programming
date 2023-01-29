#!/usr/bin/python3
"""This module contains unit tests for Square class"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """unit tests for Square class"""

    def test_width(self):
        r3 = Square(12)
        self.assertEqual(r3.width, 12)

    def test_height(self):
        r4 = Square(5)
        self.assertEqual(r4.height, 5)

    def test_x(self):
        r5 = Square(2, 3)
        self.assertEqual(r5.x, 3)

    def test_y(self):
        r6 = Square(1, 5, 10)
        self.assertEqual(r6.y, 10)

    def test_width_type(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Square('c')

    def test_width_value(self):
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            Square(0)

    def test_width_value2(self):
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            Square(-1)

    def test_x_type(self):
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Square(1, 'c')

    def test_x_value(self):
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            Square(1, -1)

    def test_y_type(self):
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Square(1, 0, 'c')

    def test_y_value(self):
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            Square(1, 0, -1)

    def test_area(self):
        r7 = Square(4)
        self.assertEqual(r7.area(), 16)
