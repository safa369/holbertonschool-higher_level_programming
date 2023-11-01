#!/usr/bin/python3
"""module of rectangle"""
from models.base import Base


class Rectangle(Base):
    """Class named rectangel inherts from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """private variable
        Args:
            width(int): the width of rectangle
            height: the height of rectangle
            x: integer
            y: integer
            id: identifier
        Raises :
            TypeError: if width or height orx or y is not an integer
            ValueError: if width or height or x or y is <= 0"""
        super().__init__(id=id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter/set method of width properties
        Raises:
            ValueError if value <= 0 or TypeError if value is not integer
        Return: value"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """getter/setter method of height properties
        Raises:
            ValueError if value <= 0 or TypeError if value is not integer
        Return: value"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """get/set method of x properties
        Raises:
            ValueError if value < 0
        Return: value"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """get/setter method of y properties
        Raises:
            ValueError if value < 0
        Return: value"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """function that return the area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """function that print the rectangle instance"""
        for _ in range(self.__height):
            print('#' * self.__width)

    def __str__(self):
        res1 = f'[Rectangle] ({self.id}) '
        res2 = f'{self.x}/{self.y} - {self.width}/{self.height}'
        return res1 + res2

    def display(self):
        """function print rectangle with #"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            for _ in range(self.x):
                print(" ", end="")
            print("#" * self.width)

    def update(self, *args, **kwargs):
        """function assign an argument to attributes"""
        att = ["id", "weidth", "height", "x", "y"]
        for attr, arg in zip(att, args):
            setattr((self, attr, arg))
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """return a dictionary representation"""
        return {
            'x': self.x,
            'width': self.width,
            'id': self.id,
            'height': self.height,
            'y': self.y
        }
