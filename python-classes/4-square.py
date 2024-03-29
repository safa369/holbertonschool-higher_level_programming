#!/usr/bin/python3
"""a class model named square """


class Square:
    """a class named Square
    Attributtes:
        attr(size): size of square"""
    def __init__(self, size=0):
        """Initialise the size"""
        self.__size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
