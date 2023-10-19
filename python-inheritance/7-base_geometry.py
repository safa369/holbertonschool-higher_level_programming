#!/usr/bin/python3
"""a model of base geometry"""


class BaseGeometry:
    """ class of base geometry"""
    def area(self):
        """function of area"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Function to validate value is an integer"""
        if type(name) is not str:
            name = str(name)
        if type(value) != int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
