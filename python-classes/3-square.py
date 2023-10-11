#!usr/bin/python3
"""A modele that create a class named square"""


class Square:
    """Square:
     a class named square.
    Attributes:
    attrib1(size): size of square."""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
