#!/usr/bin/python3
""" Unittests for Base class """
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ test class for Base class """

    def test_diff_id(self):
        b1 = Base()
        b2 = Base()
        self.assertNotEqual(b1.id, b2.id)

    def test_give_id(self):
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

    def test_sequence(self):
        b3 = Base()
        b4 = Base()
        b5 = Base()
        self.assertEqual(b5.id, 5)

    def test_give_id(self):
        b6 = Base(12)
        self.assertEqual(Base.to_json_string([b6.__dict__]), '[{"id": 12}]')
