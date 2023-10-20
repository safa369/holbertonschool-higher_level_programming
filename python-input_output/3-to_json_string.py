#!/usr/bin/python3
"""module to JSON representation of an object"""
import json


def to_json_string(my_obj):
    """function that return the JSON representation of an object
    Args:
        my_obj(str):the object to convert it
    Return: JSON object"""
    return json.dumps(my_obj)
