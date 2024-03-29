#!/usr/bin/python3
"""This module contains the class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """class defines Rectanble class, inherits from Base;
    contains private __width, __height, __x, and __y;
    instantiates with width, height, x=0, y=0, and id=None;"""

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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area value of the Rectangle instance"""
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""

        for i in range(self.y):
            print()
        for i in range(self.height):
            for j in range(self.x):
                print(" ", end='')
            for j in range(self.width):
                print("#", end='')
            print()

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} -"\
                f" {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""

        if not args:
            for key, value in kwargs.items():
                if key != 'id':
                    key = '_Rectangle__' + key
                    self.__dict__.update({key: value})
                else:
                    self.__dict__.update({key: value})
        else:
            attrs = ['id', '_Rectangle__width', '_Rectangle__height',
                     '_Rectangle__x', '_Rectangle__y']
            for i in range(len(args)):
                self.__dict__.update({attrs[i]: args[i]})

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""

        dic = {'id': self.id, 'width': self.width, 'height': self.height,
               'x': self.x, 'y': self.y}
        return dic
