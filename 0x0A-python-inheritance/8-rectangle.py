#!/usr/bin/python3
"""This module contains the class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class inherits from BaseGeometry, instantiates with width and height"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
