#!/usr/bin/python3
"""This module contains the class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class defines Square class, inherits from Rectangle;
    instantiates with size, x=0, y=0, and id=None;"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
