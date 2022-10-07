#!/usr/bin/python3
""" contains the method write_file """


def write_file(filename="", text=""):
    """ writes a string to a text file and
    returns the number of characters written
    """
    with open(filename, 'w') as f:
        num = f.write(text)
        f.close()
    return num
