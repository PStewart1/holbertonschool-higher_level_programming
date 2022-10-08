#!/usr/bin/python3
""" Unittests for Base class """
import unittest
from models.square import Square
from models.base import Base
import os.path


class TestBase(unittest.TestCase):
    """ test class for Base class """

    def test_sequence(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, 5)

    def test_diff_id(self):
        b3 = Base()
        b4 = Base()
        self.assertNotEqual(b3.id, b4.id)

    def test_give_id(self):
        b5 = Base(12)
        self.assertEqual(b5.id, 12)

    def test_json(self):
        b6 = Base(12)
        self.assertEqual(Base.to_json_string([b6.__dict__]), '[{"id": 12}]')

    def test_json2(self):
        b6 = Base(13)
        self.assertEqual(Base.to_json_string(None), '[]')

    def test_save(self):
        s1 = Square(1)
        Square.save_to_file([s1])
        self.assertTrue(os.path.isfile('Square.json'))

    def test_save2(self):
        s2 = Square(id=92, size=2, x=0, y=1)
        Square.save_to_file([s2])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(),
                             '[{"id": 92, "size": 2, "x": 0, "y": 1}]')

    def test_from_json(self):
        b7 = Base(14)
        self.assertEqual(Base.from_json_string('[{"id": 14}]'), [b7.__dict__])

    def test_from_json2(self):
        b8 = Base(15)
        self.assertEqual(Base.from_json_string(None), [])
