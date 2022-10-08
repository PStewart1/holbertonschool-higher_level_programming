#!/usr/bin/python3
""" Unittests for Rectangle class """
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ test class for Rectangle class """

    def test_diff_id(self):
        r1 = Rectangle(0, 0)
        r2 = Rectangle(1, 1)
        self.assertNotEqual(r1.id, r2.id)

    def test_width(self):
        r3 = Rectangle(12, 0)
        self.assertEqual(r3.width, 12)

    def test_height(self):
        r4 = Rectangle(0, 5)
        self.assertEqual(r4.height, 5)

    def test_x(self):
        r5 = Rectangle(0, 5, 3)
        self.assertEqual(r5.x, 3)

    def test_y(self):
        r6 = Rectangle(0, 5, 3, 10)
        self.assertEqual(r6.y, 10)
