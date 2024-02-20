#!/usr/bin/python3
"""State class model"""
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City


class State(BaseModel, Base):
    """State class that inherits
        from BaseModel class
        Arguments:
            name: State name
        """
    storage_type = getenv('HBNB_TYPE_STORAGE')

    if storage_type == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)   
        cities = relationship('City', backref='state', cascade='all, delete, delete-orphan')
    else:
        name: str = ''
        
        
    if storage_type != 'db':
        @property
        def cities(self):
            """ Returns all cities related to this state """
            from models.__init__ import storage
            all_cities = storage.all(City)
            cities = [city for city in all_cities.values() if city.state_id == self.id]
            return cities
