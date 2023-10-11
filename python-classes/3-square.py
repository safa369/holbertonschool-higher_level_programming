#!usr/bin/python3
class Square:
    """Square:
     a class named square.
    Attributes:
    attr1(size): size of square.Args:
        size(int): size for __size attribute of class
        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0."""

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ square value
        Return:
        int: the square value"""
        return self.__size ** 2
