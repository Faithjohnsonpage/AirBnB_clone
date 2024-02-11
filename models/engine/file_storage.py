#!/usr/bin/python3
"""This module serializes instances to a JSON file
and deserializes JSON file to instances
"""


import json


class FileStorage:
    """A FileStorage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary"""
        return self.__class__.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__class__.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        d = {key: obj.to_dict() for key,
             obj in self.__class__.__objects.items()}
        with open(self.__class__.__file_path, "w", encoding="utf-8") as f:
            json.dump(d, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        from models.base_model import BaseModel
        from models.user import User
        if self.__class__.__file_path:
            try:
                with open(self.__class__.__file_path,
                          "r", encoding="utf-8") as f:
                    obj_dict = json.load(f)
                    for k, v in obj_dict.items():
                        class_name, id_ = k.split('.')
                        if class_name == 'BaseModel':
                            obj_dict[k] = BaseModel(**v)
                        elif class_name == 'User':
                            obj_dict[k] = User(**v)
                    self.__class__.__objects = obj_dict
            except FileNotFoundError:
                pass
