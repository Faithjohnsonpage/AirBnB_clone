#!/usr/bin/python3
"""This module defines a State class that inherits from BaseModel"""


from .base_model import BaseModel


class State(BaseModel):
    """A State class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Instantiates an instance of a State class
        """
        BaseModel.__init__(self, *args, **kwargs)

    def __str__(self):
        """
        Returns the string representation of the User class
        """
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)
