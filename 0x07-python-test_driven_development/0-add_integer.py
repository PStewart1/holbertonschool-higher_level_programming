#!/usr/bin/python3
"""Module containing funtion add_integer

Methods:
    add_integer(): adds 2 integers
"""


def add_integer(a, b=98):
    """
    Adds 2 integers a + b
    """
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    return a + b