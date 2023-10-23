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

    def to_json(self):
        """function retrieves a dictionary repr"""
        return self.__dict__
