#!/usr/bin/python3
"""This module contains a script that adds all arguments to a Python list,
and then save them to a file"""
from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


args = argv[1:]
try:
    my_obj = load_from_json_file("add_item.json")
except FileNotFoundError:
    objs = args
else:
    objs = my_obj + args
finally:
    save_to_json_file(objs, "add_item.json")
