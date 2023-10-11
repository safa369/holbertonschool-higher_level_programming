#!usr/bin/python3
"""square class"""


class Square:
    """
    Square:
    A class named Square.
    Attributes:
        size(int): size of square
    """

    def __init__(self, size=0):
        """Initialise the size"""
        self.__size = size

    def area(self):
        return (self.__size ** 2)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
