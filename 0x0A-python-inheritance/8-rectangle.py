#!/usr/bin/python3
""" Module containing class BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class defining Rectangle, inheriting BaseGeometry.

    Methods
    -------
    area :
        raises an exception
    integer_validator :
        validates "value"
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
