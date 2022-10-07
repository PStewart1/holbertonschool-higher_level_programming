#!/usr/bin/python3
""" Contains the class Student """


class Student:
    """ class that defines a Student

    Attributes
    ----------
    first_name : str
        first name of Student
    last_name : str
        last name of Student
    age : int
        age of Student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ returns the dictionary representation of a Student instance """
        if attrs is not None:
            dics = {}
            for k, v in self.__dict__.items():
                try:
                    attrs.index(k)
                except ValueError:
                    continue
                else:
                    dics.update({k: v})
            return dics
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """ replaces all attributes of the Student instance """
        for k, v in json.items():
            self.__dict__[k] = v
