#!/usr/bin/python3
""" Unittests for Square class """
import unittest
from models.square import Square
import io
import unittest.mock
import os.path


class TestRectangle(unittest.TestCase):
    """ test class for Square class """

    def test_diff_id(self):
        r1 = Square(1)
        r2 = Square(2)
        self.assertNotEqual(r1.id, r2.id)

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

    def test_id_type(self):
        with self.assertRaisesRegex(TypeError, 'id must be an integer'):
            Square(1, 1, 0, 'c')

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
    def assert_display(self, i, x, y, expected_output, mock_stdout):
        r8 = Square(i, x, y)
        r8.display()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_display(self):
        self.assert_display(2, 3, 1, '\n   ##\n   ##\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_update(self, expected_output, mock_stdout):
        r10 = Square(1)
        r10.update(89, 2, 4, 5)
        print(r10)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_update(self):
        self.assert_update('[Square] (89) 4/5 - 2\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_update2(self, expected_output, mock_stdout):
        r11 = Square(1)
        r11.update(x=1, y=3, width=4, id=89)
        print(r11)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_update2(self):
        self.assert_update2('[Square] (89) 1/3 - 4\n')

    def test_size(self):
        r3 = Square(12)
        self.assertEqual(r3.size, 12)

    def test_size_type(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Square('c')

    def test_size_value(self):
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            Square(0)

    def test_dic(self):
        r14 = Square(1, 3, 4, 90)
        self.assertEqual(r14.to_dictionary(),
                         {'id': 90, 'size': 1, 'x': 3, 'y': 4})

    # def test_save(self):
    #     s1 = Square(1, 1)
    #     Square.save_to_file([s1])
    #     self.assertTrue(os.path.isfile('Square.json'))

    def test_save2(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), '[]')

    def test_save3(self):
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), '[]')

    def test_save4(self):
        Square.save_to_file([Square(1)])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(),
                             '[{"id": 35, "size": 1, "x": 0, "y": 0}]')
