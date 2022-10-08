#!/usr/bin/python3
""" Contains the class Base """
import json


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

    @staticmethod
    def to_json_string(list_dics):
        """ returns the JSON string representation of list_dics """
        if list_dics is None or len(list_dics) == 0:
            return "[]"
        else:
            return json.dumps(list_dics)
