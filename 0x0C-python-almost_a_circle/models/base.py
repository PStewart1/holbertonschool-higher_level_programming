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
    Methods
    -------
    to_json_string : list of dictionaries
        returns the JSON string representation of list_dics
    save_to_file : list of object instances
        writes the JSON string representation of list_objs to a file
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

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """
        list_dic = []
        if list_objs is not None:
            for item in list_objs:
                list_dic.append(item.to_dictionary())
        filename = cls.__name__ + '.json'
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(list_dic))
