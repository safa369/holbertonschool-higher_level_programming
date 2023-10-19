#!/usr/bin/python3
"""model of function to check the type of class"""


def is_same_class(obj, a_class):
    """function that returns if an object is an instance of class
    Attributes:
        obj:the object to check it.
        a_class: the class
    Raises: None
    Return: true or false"""
    if type(obj) == a_class:
        return True
    else:
        return False
