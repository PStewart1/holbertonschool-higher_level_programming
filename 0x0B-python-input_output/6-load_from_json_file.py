#!/usr/bin/python3
"""This module contains the function load_from_json_file"""
import json


def load_from_json_file(filename):
    """creates an Object from a 'JSON file'"""

    with open(filename, 'r') as file:
        text = file.read()
        file.close()
    return json.loads(text)
