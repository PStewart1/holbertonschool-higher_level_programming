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
        self.__width = width
        self.__height = height

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
