#!/usr/bin/python3
"""This module contains the class MyList"""


class MyList(list):
    """represents a custom list class, inherits from list"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        return print(sorted(self.copy()))
