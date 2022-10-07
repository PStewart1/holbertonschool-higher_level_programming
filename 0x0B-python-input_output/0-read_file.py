#!/usr/bin/python3
""" contains the method read_file """


def read_file(filename=""):
    """ reads a text file (UTF8) and prints it to stdout """
    with open(filename, 'r') as f:
        txt = f.read()
        print(txt)
        f.close()
