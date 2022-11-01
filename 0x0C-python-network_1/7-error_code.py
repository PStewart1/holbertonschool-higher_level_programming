#!/usr/bin/python3
""" takes in a URL, sends a request to the URL,
and displays the body of the response.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        response = requests.get(url)
        html = response.text
        response.raise_for_status()
        print("{}".format(html))
    except requests.HTTPError as e:
        print("Error code: {}".format(response.status_code))
