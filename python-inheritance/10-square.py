#!/usr/bin/python3
"""model imported from 9-rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class named Square inherits from Rectangle"""
    def __init__(self, size):
        """function initialize new arguments
        Args:
            size(int): the size of square
            """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """function calcul the area of square"""
        return self.__size ** 2

    def __str__(self):
        """function return a string"""
        return "[{}] {:d}/{:d}".format(Rectangle.__name__,
                                       self.__size, self.__size)
