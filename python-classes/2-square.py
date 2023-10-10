#!/usr/bin/python3
"""this module creates a class named square"""


class Square:
    """s Square:
    A class named Square
    Attributes:
    attribut1(size): size of square"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
