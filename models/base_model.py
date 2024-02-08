#!/usr/bin/python3
"""
A BaseModel module
"""


import uuid
import datetime


class BaseModel():
    """A class that defines a BaseModel"""
    def __init__(self, name=None, my_number=0, *args, **kwargs):
        """This instantiates the insstance of the class
        Args:
            name: name of model
            number: number of model
            id: string - assign with an uuid when an instance is created
            created_at: datetime - current datetime when an instance is created
            updated_at: datetime - updated every time you change your object
        """
        # Set name and my_number unconditionally
        self.name = name
        self.my_number = my_number

        # Re-create an instance with this dictionary representation.
        if kwargs:
            print(kwargs)
            # Converting created_at and updated_at strings into datetime object
            form = "%Y-%m-%dT%H:%M:%S.%f"
            created_at_dict = kwargs['created_at']
            kwargs['created_at'] = datetime.datetime.strptime(created_at_dict, form)
            updated_at_dict = kwargs['updated_at']
            kwargs['updated_at'] = datetime.datetime.strptime(updated_at_dict, form)

            # Setting the attributes from the dict
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'name':
                    print('name')
                else:
                    setattr(self, key, value)
        else:
            # Create new instance
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def __str__(self):
        """Returns a string representation of the class"""
        return "[{}] ({}) {}".format(BaseModel.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """returns a dictionary containing all
        keys/values of __dict__ of the instance"""
        self.__dict__["__class__"] = self.__class__.__name__
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        return self.__dict__
