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

    def to_json(self):
        """ returns the dictionary representation of a Student instance """
        return self.__dict__
