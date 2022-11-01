#!/usr/bin/python3
""" a Python script that fetches a given URL,
and displays the value of the X-Request-Id variable
found in the header of the response.
"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen('{}'.format(sys.argv[1])) as response:
        html = response.info()
        print(html['X-Request-Id'])
