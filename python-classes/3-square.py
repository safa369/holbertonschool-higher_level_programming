#!usr/bin/python3
"""class model named Square"""


class Square:
    """a class named square."""
    def __init__(self, size=0):
        """Initialise size"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """return current square value"""
        return self.__size ** 2
