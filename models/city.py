#!/usr/bin/python3
"""This module defines a City class that inherits from BaseModel"""


from .base_model import BaseModel


class City(BaseModel):
    """A City class"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Instantiates an instance of a City class
        """
        BaseModel.__init__(self, *args, **kwargs)

    def __str__(self):
        """
        Returns the string representation of the User class
        """
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)
