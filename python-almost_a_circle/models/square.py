#!/usr/bin/python3
"""model of square"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """class of swquare onherites from Rectanglze"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialize function"""
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str function"""
        return(f'[Square] ({self.id}) {self.x}/{self.y} - {self.height}')

    @property
    def size(self):
        """getter/setter method of size properties
        Raises:
            ValueError if value <= 0 or TypeError if value is not integer
        Return: value"""
        return self.width

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        self.height = value
        self.width = value

    def update(self, *args, **kwargs):
        """update function"""
        att = ["id", "size", "x", "y"]
        for attr, arg in zip(att, args):
            setattr(self, attr, arg)
        for key, value in kwargs.items():
            setattr(self, key, value)
