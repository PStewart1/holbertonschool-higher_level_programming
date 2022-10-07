#!/usr/bin/python3
""" contains the method class_to_json """


def class_to_json(obj):
    """ returns the dictionary description with simple data structure """
    return obj.__dict__
