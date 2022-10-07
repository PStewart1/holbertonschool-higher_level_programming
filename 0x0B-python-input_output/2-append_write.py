#!/usr/bin/python3
""" contains the method append_write """


def append_write(filename="", text=""):
    """ appends a string at the end of a text file
        and returns the number of characters added
    """
    with open(filename, 'a') as f:
        num = f.write(text)
        f.close()
    return num
