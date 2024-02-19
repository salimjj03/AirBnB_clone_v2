#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls:
            if type(cls) == str:
                cls = eval(cls)
            dic = {}
            objs = self.__objects
            for key, value in objs.items():
                if type(value) == cls:
                    dic[key] = value
            return dic
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ This method delete obj from __objects if it’s inside
        if obj is equal to None, the method should not do anything. """

        if obj:
            key = '{}.{}'.format(type(obj).__name__, obj.id)
            objs = self.__objects
            if key in objs:
                del objs[key]
                self.save()

    def close(self):
        """ This method close the connection."""

        self.reload()
