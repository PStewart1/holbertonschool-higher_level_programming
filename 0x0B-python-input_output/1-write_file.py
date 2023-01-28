#!/usr/bin/python3
"""This module contains the function write_file"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)
    and returns the number of characters written"""

    with open(filename, 'w') as file:
        chars = file.write(text)
        file.close()
    return chars
