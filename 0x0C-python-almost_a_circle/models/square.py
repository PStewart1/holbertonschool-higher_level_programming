#!/usr/bin/python3
""" Contains the class Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class that defines a Square, which inherits from Rectangle

    Attributes
    ----------
    size : int
        size of the side of a square
    Methods
    -------
    update : *args, **kwargs
        assigns an argument to each attribute
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

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
        """ assigns an argument to each attribute """
        if not args:
            for k, v in kwargs.items():
                if k != 'id' and k != 'size':
                    k = '_Rectangle__' + k
                    self.__dict__.update({k: v})
                elif k == 'size':
                    self.__dict__.update({'_Rectangle__width': v})
                else:
                    self.__dict__.update({k: v})
        else:
            attrs = ['id', '_Rectangle__width',
                     '_Rectangle__x', '_Rectangle__y']
            for i in range(len(args)):
                self.__dict__.update({attrs[i]: args[i]})
