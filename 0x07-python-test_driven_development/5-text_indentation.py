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
    finalist = []
    tempstring = ''
    extraspace = False
    for e in text:
        if e != '.' and e != '?' and e != ':':
            if extraspace and e == ' ':
                extraspace = False
                continue
            else:
                tempstring += e
        else:
            finalist.append(tempstring + e)
            tempstring = ''
            extraspace = True
    finalist.append(tempstring)
    for i in range(len(finalist)):
        print(finalist[i])
        if finalist[i] != finalist[-1]:
            print()
