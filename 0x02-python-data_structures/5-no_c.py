#!/usr/bin/python3


def no_c(my_string):
    x = ""
    y = ""
    z = "cC"
    string = my_string.maketrans(x, y, z)
    return my_string.translate(string)
