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
    try:
        dict = response.json()
        if len(dict) < 1:
            print("No result")
        else:
            print("[{}] {}".format(dict.get('id'), dict.get('name')))
    except Exception:
        print("Not a valid JSON")
