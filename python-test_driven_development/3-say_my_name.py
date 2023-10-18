#!/usr/bin/python3
"""Module contain function to print name"""


def say_my_name(first_name, last_name=""):
    """function to print name
    Args:
        first_name(str): first name to print
        last_name: last name
    Returns: None
    Raises:
        if first_name or last_name are not strings"""
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print("My name is {:s} {:s}".format(first_name, last_name))
