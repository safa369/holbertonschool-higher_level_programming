#!/usr/bin/python3
def add_integer(a, b=98):
    """function to add two integers
    Args:
        param1(a): integer.
        param2(b): integer.
    Return:
        a + b"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
