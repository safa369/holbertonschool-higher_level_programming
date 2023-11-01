#!/usr/bin/python3
"""module of base"""
import json


class Base:
    """class named Base
    Attribute:
        __nb_objects: integer"""
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionnaries):
        """static method"""
        if list_dictionnaries is None or len(list_dictionnaries) == 0:
            return "[]"
        return json.JSONEncoder().encode(list_dictionnaries)
