#!/usr/bin/python3
"""a model class named Rectangle"""


class Rectangle:
    """a class named Rectangle
    Attribute:
        attr1(width): a width of rectangle of type integer
        attr2(height): a height of rectangle of type integer
    """
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("heght must be >= 0")
        else:
            self.__height = value
