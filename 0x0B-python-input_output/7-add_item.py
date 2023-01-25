#!/usr/bin/python3
# 7-add_item.py
"""Defines a file creating script from a list of arguments."""
import sys


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        store = load_from_json_file("add_item.json")
    except FileNotFoundError:
        store = []
    store.extend(sys.argv[1:])
    save_to_json_file(store, "add_item.json")
