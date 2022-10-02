#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_first(self):
        self.assertEqual(max_integer([3, 2, 1]), 3)

    def test_max_middle(self):
        self.assertEqual(max_integer([1, 3, 2]), 3)

    def test_max_last(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_negative1(self):
        self.assertEqual(max_integer([3, -2, 1]), 3)

    def test_negatives(self):
        self.assertEqual(max_integer([-3, -2, -1]), -1)

    def test_one_num(self):
        self.assertEqual(max_integer([3]), 3)

    def test_empty(self):
        self.assertIsNone(max_integer())
