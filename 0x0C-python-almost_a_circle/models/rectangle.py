#!/usr/bin/python3
""" Contains the class Rectangle """
from models.base import Base


class Rectangle(Base):
    """ class that defines a Rectangle, which inherits from Base

    Attributes
    ----------
    __width : int
        width of rectangle
    __height : int
        height of rectangle
    __x : int

    __y : int

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        # if type(value) is not int:
        #     raise TypeError("width must be an integer")
        # if value < 0:
        #     raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        # if type(value) is not int:
        #     raise TypeError("height must be an integer")
        # if value < 0:
        #     raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        # if type(value) is not int:
        #     raise TypeError("width must be an integer")
        # if value < 0:
        #     raise ValueError("width must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        # if type(value) is not int:
        #     raise TypeError("height must be an integer")
        # if value < 0:
        #     raise ValueError("height must be >= 0")
        self.__y = value