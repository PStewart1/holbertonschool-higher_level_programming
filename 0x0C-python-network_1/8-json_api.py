#!/usr/bin/python3
""" takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    response = requests.post(url, data={'q': q})
    if type(response.json()) is not dict:
        print("Not a valid JSON")
    html = dict(response.json())
    if len(html) < 1:
        print("No result")
    else:
        print("[{}] {}".format(html.get('id'), html.get('name')))
