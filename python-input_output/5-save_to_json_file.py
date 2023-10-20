#!/usr/bin/python3
"""model to write an object to text file"""
import json


def save_to_json_file(my_obj, filename):
    """function that write an object to at ext file using JSON representation
    Args:
        my_obj: object to convert it
        filname: file to write into it"""
    json_obj = json.dumps(my_obj)
    with open(filename, 'w') as f:
        f.write(json_obj)
