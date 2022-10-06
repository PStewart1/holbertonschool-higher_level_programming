#!/usr/bin/python3
""" contains the class MyList, which inherits from list """


class MyList(list):
    """
    a class to represent a list.

    Methods
    -------
    print_sorted
        prints the list, but sorted
    """

    def print_sorted(self):
        """ prints the list, but sorted (ascending sort) """
        print(sorted(self))
