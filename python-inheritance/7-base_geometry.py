#!/usr/bin/python3
"""a model of base geometry"""


class BaseGeometry:
    """ class of base geometry"""
    def area(self):
        """function of area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function to validate value is an integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
