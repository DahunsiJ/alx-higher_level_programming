#!/usr/bin/python3
""" Script that takes ina letter and sends a POST
    request to http://0.0.0.0:5000/search_user
Usage ./8-json_api.py <letter>
    - The letter is sent as the value of the variable `q`.
    - If no letter is provided, sends `q=""`.
"""
import requests
from sys import argv


if __name__ == "__main__":
    letter = "" if len(argv) == 1 else argv[1]
    payload = {"q": letter}

    res = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        res_json = res.json()
        if res_json == {}:
            print("No result")
        else:
            print("[{}] {}".format(res_json["id"], res_json["name"]))
    except ValueError:
        print("Not a valid JSON")
