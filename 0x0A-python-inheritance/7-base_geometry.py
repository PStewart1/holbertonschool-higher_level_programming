#!/usr/bin/python3
""" Module containing class BaseGeometry """


class BaseGeometry:
    """
    A class defining BaseGeometry.

    Methods
    -------
    area :
        raises an exception
    integer_validator :
        validates "value"
    """

    def area(self):
        """ raises an Exception with the message area() is not implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
