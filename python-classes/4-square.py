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
        """
        Instance the class Square
        Args:
            size(int): the size of square
        """
        self.__size = size

    def area(self):
        """
        square area Return the current square area (int)
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """
        getter of size
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
