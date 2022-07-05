#!/usr/bin/python3
""" Module 5-save_to_json_file
Write a function that writes an Object to a text file
using a JSON representation
"""


def save_to_json_file(my_obj, filename):
    import json

    with open(filename, 'w') as f:
        new = json.dumps(my_obj)
        f.write(new)
