#!/usr/bin/python3
""" 0-main """
import json
from os import path


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""

        list_dic = []
        if list_objs is not None:
            for item in list_objs:
                list_dic.append(item.to_dictionary())
        filename = cls.__name__ + '.json'
        with open(filename, 'w') as file:
            file.write(cls.to_json_string(list_dic))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string"""

        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""

        if cls.__name__ == 'Rectangle':
            obj = cls(1, 2)
        elif cls.__name__ == 'Square':
            obj = cls(3)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""

        filename = cls.__name__ + '.json'
        if not path.isfile(filename):
            return []
        else:
            with open(filename, "r") as file:
                json_str = file.read()
            list_dics = cls.from_json_string(json_str)
            list_objs = []
            for items in list_dics:
                list_objs.append(cls.create(**items))
        return list_objs
