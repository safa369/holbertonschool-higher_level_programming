#!/usr/bin/python3
"""module of rectangle"""
from models.base import Base


class Rectangle(Base):
    """class named rectangel inherts from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """private variable
        Args:
            width: the width of rectangle
            height: the height of rectangle
            x: integer
            y: integer
            id: identifier"""
        super().__init__(id=id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter method of width properties
        Return: value"""
        return self.__width

    @width.setter
    def width(self, value):
        """ setter of width
        Raises:
            ValueError if value <= 0 or TypeError if value is not integer
        Return: Value"""
        if value <= 0:
            raise ValueError('width must be > 0')
        elif type(value) != int:
            raise TypeError('width must be an integer')
        self.__width = value

    @property
    def height(self):
       """getter method of height properties
       Return: value"""
       return self.__height

    @height.setter
    def height(self, value):
        """ setter of height
        Raises:
            ValueError if value <= 0 or TypeError if value is not integer
        Return: Value"""
        if value <= 0:
            raise ValueError('height must be > 0')
        elif type(value) != int:
            raise TypeError('height must be an integer')
        self.__height = value

    @property
    def x(self):
        """getter method of x properties
        Return: value"""
        return self.__x

    @x.setter
    def x(self, value):
        """ setter method of x
        Raises:
            ValueError if value < 0
        Return: Value"""
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """getter method of y properties
        Return: value"""
        return self.__y

    @y.setter
    def y(self, value):
        """ setter method of y
        Raises:
            ValueError if value < 0
        Return: Value"""
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value
