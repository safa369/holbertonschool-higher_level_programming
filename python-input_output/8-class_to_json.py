#!/usr/bin/python3
""" Json module"""


def class_to_json(obj):
    """function return the dictionary descreption 
    Args:
        obj: object
    Return: the descreption"""
    return vars(obj)
