#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    entry = {key: value}
    a_dictionary.update(entry)
    return a_dictionary
