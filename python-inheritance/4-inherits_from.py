#!/usr/bin/python3
""" model of function to check if an object is an instance of class"""


def inherits_from(obj, a_class):
    """function to check an object
    Attributes:
        obj: the object
        a_class: the class
    Return: True or false"""
    if issubclass(type(obj), a_class):
        return True
    if not issubclass(type(obj), a_class):
        return False