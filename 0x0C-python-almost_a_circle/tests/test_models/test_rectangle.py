#!/usr/bin/python3
""" Unittests for Rectangle class """
import unittest
from models.rectangle import Rectangle
import io
import unittest.mock


class TestRectangle(unittest.TestCase):
    """ test class for Rectangle class """

    def test_diff_id(self):
        r1 = Rectangle(1, 1)
        r2 = Rectangle(2, 2)
        self.assertNotEqual(r1.id, r2.id)

    def test_width(self):
        r3 = Rectangle(12, 1)
        self.assertEqual(r3.width, 12)

    def test_height(self):
        r4 = Rectangle(4, 5)
        self.assertEqual(r4.height, 5)

    def test_x(self):
        r5 = Rectangle(2, 5, 3)
        self.assertEqual(r5.x, 3)

    def test_y(self):
        r6 = Rectangle(1, 5, 3, 10)
        self.assertEqual(r6.y, 10)

    def test_id_type(self):
        with self.assertRaisesRegex(TypeError, 'id must be an integer'):
            Rectangle(1, 1, 0, 0, 'c')

    def test_width_type(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Rectangle('c', 1)

    def test_width_value(self):
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            Rectangle(0, 1)

    def test_height_type(self):
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(1, 'c')

    def test_height_value(self):
        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            Rectangle(1, 0)

    def test_x_type(self):
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Rectangle(1, 1, 'c')

    def test_x_value(self):
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            Rectangle(1, 1, -1)

    def test_y_type(self):
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Rectangle(1, 1, 0, 'c')

    def test_y_value(self):
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            Rectangle(1, 1, 0, -1)

    def test_area(self):
        r7 = Rectangle(4, 5)
        self.assertEqual(r7.area(), 20)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, i, j, expected_output, mock_stdout):
        r8 = Rectangle(i, j)
        r8.display()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_only_numbers(self):
        self.assert_stdout(3, 1, '###\n')
