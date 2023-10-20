#!/usr/bin/python3
"""model to create an object from JSON file"""
import json


def load_from_json_file(filename):
    """function that creatz an object from JSON file using JSON representation
    Args:
        filname: file """
    with open(filename, 'r') as f:
        return json.load(f)
