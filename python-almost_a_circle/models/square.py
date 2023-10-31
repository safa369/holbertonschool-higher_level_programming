#!/usr/bin/python3
"""model of square"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=0):
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return(f'[Square] ({self.id}) {self.x}/{self.y} - {self.height}')
