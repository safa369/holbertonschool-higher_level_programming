#!/usr/bin/python3
"""model of function to check an object"""


def is_kind_of_class(obj, a_class):
    """function is kind of class
    Attributes:
        obj: the object 
        a_class: the class
    Args:None
    Raises: None
    Return True or False"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
