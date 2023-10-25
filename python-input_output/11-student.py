#!/usr/bin/python3
"""a module of student"""


class Student:
    """a class named student
    Attributes:
        first_name(str): the first name of student
        last_name(str): the last name of the student
        age(int): the age of the student"""
    def __init__(self, first_name, last_name, age):
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

    def reload_from_json(self, json):
        """method to replace all attributes of student"""
        return json.update()
