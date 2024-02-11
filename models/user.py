#!/usr/bin/python3
"""
This module defines class User that inherits from BaseModel
"""


from .base_model import BaseModel


class User(BaseModel):
    """
    A User class that inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Instantiates an instance of a User class
        """
        BaseModel.__init__(self, *args, **kwargs)

    def __str__(self):
        """
        Returns the string representation of the User class
        """
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)
