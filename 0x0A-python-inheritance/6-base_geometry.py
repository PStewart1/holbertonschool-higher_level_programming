#!/usr/bin/python3
""" Module containing class BaseGeometry """


class BaseGeometry:
    """
    A class defining BaseGeometry.

    Methods
    -------
    area :
        raises an exception
    """

    def area(self):
        """ raises an Exception with the message area() is not implemented """
        raise Exception("area() is not implemented")
