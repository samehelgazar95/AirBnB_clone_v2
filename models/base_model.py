#!/usr/bin/python3
"""BaseModel class
as a parent class for other models"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
import models



Base = object #declarative_base()


class BaseModel:
    """The BaseModel class
        Arguments:
        DATE_FORMAT: The creating and updating date format
    """

    DATE_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
    if storage_type == 'db':
        id = Column(String(60), nullable=False, primary_key=True)
        created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
        updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Init method instantiated with 3 attrs"""
        if kwargs:
            for key, val in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    val = datetime.strptime(val, self.DATE_FORMAT)
                elif key == '__class__':
                    continue
                setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Editing the string representation of the object"""
        class_name = self.__class__.__name__
        string = str("[{}] ({}) {}".format(class_name, self.id, self.__dict__))
        return string

    def save(self):
        """Updating the updated_at attr to current time
            # Importing the storage here
            # to avoid the circular import 
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()
        
    def delete(self):
        """Deleting current instance by calling the delete method from storage"""
        from models import storage
        storage.delete(self)

    def to_dict(self):
        """Editing the __dict__ representation of the object"""
        dictionary = self.__dict__.copy()
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        dictionary['__class__'] = self.__class__.__name__
        if '_sa_instance_state' in dictionary.keys():
            del dictionary['_sa_instance_state']
        return dictionary
