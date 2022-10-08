#!/usr/bin/python3
""" Contains the class Base """


class Base:
    """ class that defines a Base

    Attributes
    ----------
    __nb_objects : int
        number of objects
    id : int
        id of object
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
