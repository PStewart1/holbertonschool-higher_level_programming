#!/usr/bin/python3
""" takes your GitHub credentials (username and password),
and uses the GitHub API to display your id
"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    url = f"https://api.github.com/users/{username}"
    password = sys.argv[2]
    headers = {'Authorization': f'token {password}'}
    response = requests.get(url, headers=headers)
    html = dict(response.json())
    print("{}".format(html.get('id')))
