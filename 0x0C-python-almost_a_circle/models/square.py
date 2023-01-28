#!/usr/bin/python3
"""This module contains the class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class defines Square class, inherits from Rectangle;
    instantiates with size, x=0, y=0, and id=None;"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""

        if not args:
            for key, value in kwargs.items():
                if key != 'id' and key != 'size':
                    key = '_Rectangle__' + key
                    self.__dict__.update({key: value})
                elif key == 'size':
                    self.__dict__.update({'_Rectangle__width': value})
                else:
                    self.__dict__.update({key: value})
        else:
            attrs = ['id', '_Rectangle__width',
                     '_Rectangle__x', '_Rectangle__y']
            for i in range(len(args)):
                self.__dict__.update({attrs[i]: args[i]})
