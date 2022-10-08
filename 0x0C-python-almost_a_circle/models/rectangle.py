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

    Methods
    -------
    area() :
        returns the area value of the Rectangle instance
    display() :
        prints in stdout the Rectangle instance with the character #
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        if id and type(id) is not int:
            raise TypeError("id must be an integer")
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

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def area(self):
        """ returns the area value of the Rectangle instance """
        return self.width * self.height

    def display(self):
        """ prints in stdout the Rectangle instance with the character # """
        for i in range(self.y):
            print()
        for i in range(self.height):
            for j in range(self.x):
                print(" ", end='')
            for k in range(self.width):
                print("#", end='')
            print()

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute """
        if not args:
            for k, v in kwargs.items():
                if k != 'id':
                    k = '_Rectangle__' + k
                    self.__dict__.update({k: v})
                else:
                    self.__dict__.update({k: v})
        else:
            attrs = ['id', '_Rectangle__width', '_Rectangle__height',
                     '_Rectangle__x', '_Rectangle__y']
            for i in range(len(args)):
                self.__dict__.update({attrs[i]: args[i]})
