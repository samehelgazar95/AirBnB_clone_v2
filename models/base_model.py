#!/usr/bin/python3
"""BaseModel class
as a parent class for other models"""
import uuid
import datetime
import models


class BaseModel:
    """The BaseModel class
        Arguments:
        DATE_FORMAT: The creating and updating date format
    """

    DATE_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'

    def __init__(self, *args, **kwargs):
        """Init method instantiated with 3 attrs"""
        if kwargs:
            for key, val in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    val = datetime.datetime.strptime(val, self.DATE_FORMAT)
                elif key == '__class__':
                    continue
                setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Editing the string representation of the object"""
        class_name = self.__class__.__name__
        string = str("[{}] ({}) {}".format(class_name, self.id, self.__dict__))
        return string

    def save(self):
        """Updating the updated_at attr to current time"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """Editing the __dict__ representation of the object"""
        dict_attr = self.__dict__.copy()
        dict_attr["created_at"] = self.created_at.isoformat()
        dict_attr["updated_at"] = self.updated_at.isoformat()
        dict_attr['__class__'] = self.__class__.__name__
        return dict_attr
