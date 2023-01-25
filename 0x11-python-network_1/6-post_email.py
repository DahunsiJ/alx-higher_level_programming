#!/usr/bin/python3
""" Script that takes in a URL and an email address,
    sends a POST request to te passed URL with the email as parameter.

Usage ./6-post_email.py <URL> <email>.
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]
    value = {"email": argv[2]}

    response = requests.post(url, data=value)
    print(response.text)
