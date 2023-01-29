#!/usr/bin/python3
"""This module contains unit tests for Base class"""
import unittest
from models.square import Square
from models.base import Base
import os.path


class TestBase(unittest.TestCase):
    """unit tests for Base class"""

    def test_json(self):
        b6 = Base(12)
        self.assertEqual(Base.to_json_string([b6.__dict__]), '[{"id": 12}]')

    def test_save(self):
        s1 = Square(1)
        Square.save_to_file([s1])
        self.assertTrue(os.path.isfile('Square.json'))

    def test_from_json(self):
        b7 = Base(14)
        self.assertEqual(Base.from_json_string('[{"id": 14}]'), [b7.__dict__])

    def test_create(self):
        s3 = Square(8, 9, 10, 11)
        s3_dic = s3.to_dictionary()
        s4 = Square.create(**s3_dic)
        self.assertEqual(s4.__str__(), '[Square] (11) 9/10 - 8')

    def test_load(self):
        s5 = Square(id=92, size=2, x=0, y=1)
        Square.save_to_file([s5])
        s6 = Square.load_from_file()
        self.assertEqual(s5.__str__(), s6[0].__str__())

    def test_id(self):
        b5 = Base(12)
        self.assertEqual(b5.id, 12)

    def test_new_id(self):
        b3 = Base()
        b4 = Base()
        self.assertNotEqual(b3.id, b4.id)
