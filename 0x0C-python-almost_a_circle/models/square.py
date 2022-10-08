#!/usr/bin/python3
""" Contains the class Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class that defines a Square, which inherits from Rectangle

    Attributes
    ----------

    Methods
    -------

    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
