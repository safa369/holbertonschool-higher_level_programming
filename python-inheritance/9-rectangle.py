#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""model imported from 7-base_geometry"""

class Rectangle(BaseGeometry):
    """class named Rectangle inherits from Base geometry"""
    def __init__(self, width, height):
        """function"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """function calcul the area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """function return a string"""
        return "{} {}/{}".format(Rectangle.__name__, self.__width, self.__height)
