#!/usr/bin/python3
""" Contains the class Base """
import json
import os.path


class Base:
    """ class that defines the Base class

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
    from_json_string : JSON string
        returns the list of the JSON string representation
    create : dictionary
        returns an instance with all attributes already set
    load_from_file :
        returns a list of instances:
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

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if cls.__name__ == 'Rectangle':
            r1 = cls(1, 1)
        elif cls.__name__ == 'Square':
            r1 = cls(1)
        r1.update(**dictionary)
        return r1

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        filename = cls.__name__ + '.json'
        if not os.path.isfile(filename):
            return []
        else:
            with open(filename, "r") as file:
                json_string = file.read()
            list_dicts = cls.from_json_string(json_string)
            list_objs = []
            for items in list_dicts:
                list_objs.append(cls.create(**items))
        return list_objs
