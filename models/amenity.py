#!/usr/bin/python3
"""This module defines a Amenity class that inherits from BaseModel"""


from .base_model import BaseModel


class Amenity(BaseModel):
    """An Amenity class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Instantiates an instance of an Amenity class
        """
        BaseModel.__init__(self, *args, **kwargs)

    def __str__(self):
        """
        Returns the string representation of the User class
        """
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)
