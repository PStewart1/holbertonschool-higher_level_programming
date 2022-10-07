#!/usr/bin/python3
""" contains the method load_from_json_file """
import json


def load_from_json_file(filename):
    """ creates an Object from a “JSON file” """
    with open(filename, 'r') as f:
        txt = f.read()
        f.close()
    return json.loads(txt)
