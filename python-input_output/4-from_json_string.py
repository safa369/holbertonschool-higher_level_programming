#!/usr/bin/python3
"""module to JSON representation of an object"""
import json


def from_json_string(my_str):
    """function that return string from Json
    Args:
        my_str:the object to convert it
    Return: string"""
    return json.loads(my_str)
