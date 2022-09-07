#!/usr/bin/python3
"""
Module containing class Square

Classes:
    Square
"""


class Square:
    """
    A class to represent a Square.

    Attributes:
        size (int): size of square.

    Methods:
        area(): returns the area of the square.
    """

    def __init__(self, size=0):
        """
        Constructs all the necessary attributes for the square object.

        Args:
            size (int): size of square.
        """
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not type(value) is int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2
