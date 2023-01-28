#!/usr/bin/python3
"""This module contains the class Student"""


class Student():
    """class defines a student;
    instantiates with first_name, last_name and age;
    includes method to_json """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance,
        with an optional list of selected attributes"""

        if attrs is not None:
            dic = {}
            for key, value in self.__dict__.items():
                try:
                    attrs.index(key)
                except ValueError:
                    continue
                else:
                    dic.update({key: value})
            return dic
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""

        for key, value in json.items():
            self.__dict__[key] = value
