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
