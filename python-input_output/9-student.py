#!/usr/bin/python3
"""modeol of class of student"""
class_to_json = __import__('8-class_to_json').class_to_json


class Student:
    """class of studen
    Attributes:
        first_name: string
        last_name: string
        age: integer"""
    def __init__(self, first_name, last_name, age):
        """function initilazed"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """function retrieves a dictionary repr"""
        return class_to_json(self)
