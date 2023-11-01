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
            list_dictionnaries = "[]"
        return json.dumps(list_dictionnaries)

    @classmethod
    def save_to_file(cls, list_objs):
        file_name = cls.__name__ + ".json"
        if list_objs is None:
            lis_ob = "[]"
        else:
            lis_ob = [obj.to_dictionary() for obj in list_objs]
        with open(file_name, 'w') as js_file:
            js_file.write(cls.to_json_string(lis_ob))
