#!/usr/bin/python3
""" 0-main """


class Base():
    """class defines Base class;
    contains private __nb_objects, instantiates with id;"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
