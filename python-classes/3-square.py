#!/usr/bin/python3
""" a class model named square"""


class Square:
    """a class named square
    Attributtes:
        attr(size): size of square"""
    def __init__(self, size=0):
        """initialise object"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size ** 2
