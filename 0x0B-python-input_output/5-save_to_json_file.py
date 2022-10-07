#!/usr/bin/python3
""" contains the method save_to_json_file """
import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file, using a JSON representation """
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
        f.close()
