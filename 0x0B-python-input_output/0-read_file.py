#!/usr/bin/python3
"""This module contains the function read_file"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout"""

    with open(filename, 'r') as file:
        text = file.read()
        print(text, end='')
        file.close()
