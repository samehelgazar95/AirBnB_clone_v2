#!/usr/bin/python3
"""
The centeralized storage for the application
almost followed the singleton pattern
"""
import json
import os
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.user import User
from models.review import Review


class FileStorage:
    """
    Manipulate the file that's storing data
    Arguments:
        __file_path: to store the JSON format
        __objects: {"ClassName.id": Object, "ClassName.id": Object}
        models_map: mapping the models for easy accessing
    """
    __file_path = "file.json"
    __objects = {}
    models_map = {'BaseModel': BaseModel, 'Amenity': Amenity,
                'City': City, 'Place': Place, 'Review': Review,
                'State': State, 'User': User}

    def all(self, cls=None):
        """Simple function returns the private __objects"""
        if cls:
            temp = {}
            for key, val in FileStorage.__objects.items():
                key_name = str(key.split('.')[0])
                if cls.__name__ == key_name:
                    temp[key] = val
            return temp
        else:
            return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Writing new obj dict to file.json"""
        data = {}
        for key, obj in FileStorage.__objects.items():
            data[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def delete(self, obj=None):
        """Delete object from __objects"""
        if obj:
            key = obj.to_dict()['__class__'] + '.' + obj.id
            del FileStorage.__objects[key]
        self.save()

    def reload(self):
        """Loading the dict from file.json"""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                try:
                    data = json.load(file)
                    if not isinstance(data, dict) or not data:
                        return
                    self.new_objects(data)
                except json.decoder.JSONDecodeError:
                    return

    @staticmethod
    def new_objects(data):
        """Create new __objects with every reload()"""
        FileStorage.__objects = {}
        for key, val in data.items():
            cls_name = val.get('__class__')
            if cls_name:
                new_obj = FileStorage.models_map[cls_name](**val)
                FileStorage.__objects[key] = new_obj
