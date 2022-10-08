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
    def assert_display(self, i, j, expected_output, mock_stdout):
        r8 = Rectangle(i, j)
        r8.display()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_display(self):
        self.assert_display(3, 1, '###\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_str(self, expected_output, mock_stdout):
        r9 = Rectangle(1, 1)
        print(r9)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str(self):
        self.assert_str('[Rectangle] (13) 0/0 - 1/1\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_display(self, i, j, x, y, expected_output, mock_stdout):
        r8 = Rectangle(i, j, x, y)
        r8.display()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_display(self):
        self.assert_display(4, 2, 3, 1, '\n   ####\n   ####\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_update(self, expected_output, mock_stdout):
        r10 = Rectangle(1, 1)
        r10.update(89, 2, 3, 4, 5)
        print(r10)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_update(self):
        self.assert_update('[Rectangle] (89) 4/5 - 2/3\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_update2(self, expected_output, mock_stdout):
        r11 = Rectangle(1, 1)
        r11.update(x=1, height=2, y=3, width=4, id=89)
        print(r11)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_update2(self):
        self.assert_update2('[Rectangle] (89) 1/3 - 4/2\n')

    def test_dic(self):
        r14 = Rectangle(1, 2, 3, 4, 90)
        self.assertEqual(r14.to_dictionary(),
                         {'id': 90, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
