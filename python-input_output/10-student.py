#!/usr/bin/python3
"""modeol of class of student"""


class Student:
    """class of studen
    Attributes:
        first_name(str): first name of student
        last_name(str): last name of student
        age(int): age of student"""
    def __init__(self, first_name, last_name, age):
        """function initilazed"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """function retrieves a dictionary repr"""
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}
