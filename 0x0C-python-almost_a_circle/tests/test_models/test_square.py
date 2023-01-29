#!/usr/bin/python3
"""This module contains unit tests for Square class"""
import unittest
from models.square import Square
import unittest.mock
import io


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

    def test_size(self):
        r3 = Square(12)
        self.assertEqual(r3.size, 12)

    def test_size_type(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Square('c')

    def test_size_value(self):
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            Square(0)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_display(self, i, expected_output, mock_stdout):
        r8 = Square(i)
        r8.display()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_display(self):
        self.assert_display(2, '##\n##\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_str(self, expected_output, mock_stdout):
        r9 = Square(id=50, size=1)
        print(r9)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str(self):
        self.assert_str('[Square] (50) 0/0 - 1\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_update(self, expected_output, mock_stdout):
        r10 = Square(1)
        r10.update(89, 2, 4, 5)
        print(r10)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_update(self):
        self.assert_update('[Square] (89) 4/5 - 2\n')

    def test_dic(self):
        r14 = Square(1, 3, 4, 90)
        self.assertEqual(r14.to_dictionary(),
                         {'id': 90, 'size': 1, 'x': 3, 'y': 4})

    def test_save(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), '[]')

    def test_save3(self):
        Square.save_to_file([Square(1, 0, 0, 30)])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(),
                             '[{"id": 30, "size": 1, "x": 0, "y": 0}]')

    def test_save2(self):
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), '[]')

    def test_load_from_file(self):
        """tests load_from_file in square"""
        s1 = Square(8, 7, 6, 5)
        s2 = Square(20, 30, 40, 50)
        test_input = [s1, s2]
        Square.save_to_file(test_input)
        test_output = Square.load_from_file()
        self.assertEqual(str(test_output[0]), '[Square] (5) 7/6 - 8')
        self.assertEqual(str(test_output[1]), '[Square] (50) 30/40 - 20')
