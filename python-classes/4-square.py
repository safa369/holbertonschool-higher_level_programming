#!usr/bin/python3
"""This module create a class named square"""
class Square:
    """
    Square:
    A class named Square.
    Attributes:
    attrib1(size): size of square"""
    def __init__(self, size=0):
        """ Instance the class Square
        Args:
            size(int): the size of square
        Return:
            None
            """
        self.__size = size

    @property
    def size(self):
        """
        getter of size
        Return:
            size os square
        """
        return self.__size
    
    @size.setter
    def size(self, value):
        """
        Setter of size
        Args:
            size(int): size of a size of square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        Return:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        square area
        Return:
            the current square area (int)"""
        return (self.__size ** 2)
