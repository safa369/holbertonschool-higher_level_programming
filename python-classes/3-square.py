#!usr/bin/python3
"""class square"""


class Square:
    """Square:
     a class named square.
    Attributes:
    attr1(size): size of square."""
    def __init__(self, size=0):
        """
        Args:
            size(int): size for __size attribute of class
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        square value
        Return:
            int: the square value"""
        return self.__size ** 2
    