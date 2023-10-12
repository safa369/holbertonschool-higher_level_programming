#!/usr/bin/python3
"""a class model named square"""


class Square:
    """ a class named square
    Attributes:
        attrb1(size): size of square
        attrb2(position): tuple of 2 integers"""

    def __init__(self, size=0, position=(0, 0)):
        """initialise size and position"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (not all(isinstance(x, int) and x > 0 for x in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

    def are(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.position[0], end="")
                print("#" * self.size)
