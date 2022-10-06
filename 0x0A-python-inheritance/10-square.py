#!/usr/bin/python3
""" Module containing class Square """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class defining Square, inheriting Rectangle.

    Methods
    -------
    area :
        returns area of Square
    integer_validator :
        validates "value"
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)

    def area(self):
        return self.__size ** 2
