#!/usr/bin/python3
"""Module containing funtion text_indentation()

Methods:
    text_indentation(): Prints a text with 2 new lines 
        after each of these characters: ., ? and :
"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these chars: ., ? and :"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    lines = text.split('.,?:')
    for i in range(len(lines)):
        print("{}".format(lines[i]))
