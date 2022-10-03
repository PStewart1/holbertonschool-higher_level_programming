#!/usr/bin/python3
"""Module containing funtion print_square()

Methods:
    print_square(): Prints a square with the character #.
"""


def print_square(size):
    """ Prints a square with the character #. """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
