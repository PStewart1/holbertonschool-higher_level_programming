#!/usr/bin/python3
"""This module contains the class BaseGeometry"""


class BaseGeometry:
    """class contains methods area(self),
    integer_validator(self, name, value)"""

    def area(self):
        """raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
