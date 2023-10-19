#!/usr/bin/python3
""" model of function to check if an object is an instance of class"""


def inherits_from(obj, a_class):
    """function to check an object
    Attributes:
        obj: the object
        a_class: the class
    Return: True or false"""
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
