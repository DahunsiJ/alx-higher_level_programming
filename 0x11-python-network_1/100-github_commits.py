#!/usr/bin/python3
""" Lists the 10 most recent commits on a given GitHub repository.

Usage: ./10-github_commits.py <repository name> <repository owner>
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
            argv[1], argv[2])

    res = requests.get(url)
    res_json = res.json()
    try:
        for i in range(0, 10):
            print("{}: {}".format(
                res_json[i].get("sha"),
                res_json[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
