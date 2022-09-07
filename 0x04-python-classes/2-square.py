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
        self.__size = size
        if not type(size) is int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2
