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
        my_print(): prints in stdout the square with the character #.
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
        """Getter property for constructer."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter property for constructer.
        Size must be interger, greater than 0.
        """
        if not type(value) is int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end='')
                print()
