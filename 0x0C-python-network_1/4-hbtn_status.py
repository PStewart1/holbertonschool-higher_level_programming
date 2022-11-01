#!/usr/bin/python3
""" fetches https://intranet.hbtn.io/status
"""
from urllib import request
# import sys


if __name__ == "__main__":
    req = request.Request("https://intranet.hbtn.io/status")
    with request.urlopen(req) as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html.decode())))
        print("\t- content: {}".format(str(html, "utf-8")))

