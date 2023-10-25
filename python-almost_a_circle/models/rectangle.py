#!/usr/bin/python3
"""module of rectangle"""
from models.base import Base


class Rectangle(Base):
    """class named rectangel inherts from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """private variable
        Attribute:
            width: the width of rectangle
            height: the height of rectangle
            x: integer
            y: integer"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """getter method to get properties"""
        return self.__width

    @width.setter
    def width(self, value):
        """ setter method to change the value"""
        self.__width = value

    @property
    def height(self):
       """getter method to get properties"""
       return self.__height

    @height.setter
    def height(self, value):
        """ setter method to change the value"""
        self.__height = value

    @property
    def x(self):
        """getter method to get properties"""
        return self.__x

    @x.setter
    def x(self, value):
        """ setter method to change the value"""
        self.__x = value

    @property
    def y(self):
        """getter method to get properties"""
        return self.__y

    @y.setter
    def y(self, value):
        """ setter method to change the value"""
        self.__y = value
