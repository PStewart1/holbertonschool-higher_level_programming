#!/usr/bin/python3
"""This module contains the function append_write"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8)
    and returns the number of characters added"""

    with open(filename, 'a') as file:
        chars = file.write(text)
        file.close()
    return chars
