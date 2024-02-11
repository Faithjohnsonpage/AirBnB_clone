#!/usr/bin/python3
"""This module defines a Review class that inherits from BaseModel"""


from .base_model import BaseModel


class Review(BaseModel):
    """A Review class"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        Instantiates an instance of a Review class
        """
        BaseModel.__init__(self, *args, **kwargs)

    def __str__(self):
        """
        Returns the string representation of the User class
        """
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)
