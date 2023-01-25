#!/usr/bin/python3
"""Script that takes GitHub credentials and uses the Github API
    to display id
Usage: ./10-my_github.py <username> <password>
"""
import requests
from sys import argv


if __name__ == "__main__":

    res = requests.get("https://api.github.com/user", auth=(argv[1], argv[2]))

    if res.status_code == 200:
        data = res.json()
        print(data.get("id"))
    else:
        print("None")
