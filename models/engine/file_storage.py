#!/usr/bin/python3

""" defines the filestorage class """
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from modes.amenity import Amenity
from models.state import State
from models.review import Review
from models.place import Place


class FileStorage:
    """ Represents a class filestorage """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns a dictionary"""
        return self.__objects
    def new(self, obj):
        """
        sets in __objects the `obj` with key <obj c
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj
    def save(self):
        """
        Serialize __objects to the JSON file
        """
        with open(self.__file_path, mode="w") as f:
            dict_storage = {}
            for key, values in self.__objects.items():
                dict_storage[key] = values.to_dict()
            json.dump(dict_storage, f)
    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, encoding="utf-8") as f:
                for obj in json.load(f).values():
                    self.new(eval(obj["__class__"])(**obj))

        except FileNotFoundError:
            return
