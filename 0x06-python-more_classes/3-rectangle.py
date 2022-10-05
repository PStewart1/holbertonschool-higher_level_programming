#!/usr/bin/python3
"""
Module containing class Rectangle

Classes:
    Rectangle
"""


class Rectangle:
    """
    A class to represent a person.

    Attributes
    ----------
    width : int
        width of rectangle
    height : int
        height of rectangle

    Methods
    -------
    area : int
        returns area of rectangle
    perimeter : int
        returns perimeter of rectangle
    __str__
        prints the rectangle with the character #
    """
    def __init__(self, width=0, height=0):
        """
        Constructs all the necessary attributes for the Rectangle object.

        Parameters
        ----------
            width : int
                width of rectangle
            height : int
                height of rectangle
        """
        self.width = width
        self.height = height

    def __str__(self):
        """ prints the rectangle with the character # """
        if self.width == 0 or self.height == 0:
            return ""
        for i in range(self.height):
            for j in range(self.width):
                print("#", end='')
            if i < (self.height - 1):
                print()
        return ""

    def __repr__(self):
        """ returns a string representation of the rectangle """
        return "Rectangle({}, {})".format(self.width, self.height)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns area of rectangle """
        return self.width * self.height

    def perimeter(self):
        """ returns perimeter of rectangle """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)
