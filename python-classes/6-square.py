#!/usr/bin/python3
"""a class model named square"""


class Square:
    """ a class named square
    Attributtes:
        attr1(size): size of square
        attr2(position): tuple of 2 integers"""

    def __init__(self, size=0, position=(0, 0)):
        """initialise size and position"""
        self.__size = size
        self.__position = position

    def are(self):
        return self.__size ** 2

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

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.position[0], end="")
                print("#" * self.size)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
