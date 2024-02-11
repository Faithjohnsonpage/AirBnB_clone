#!/usr/bin/python3
"""This module defines a Place class that inherits from BaseModel"""


from .base_model import BaseModel


class Place(BaseModel):
    """A Place class"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = ""

    def __init__(self, *args, **kwargs):
        """
        Instantiates an instance of a Place class
        """
        BaseModel.__init__(self, *args, **kwargs)

    def __str__(self):
        """
        Returns the string representation of the User class
        """
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)
