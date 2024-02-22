#!/usr/bin/python3
"""State class model"""
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """State class that inherits from BaseModel class"""
    __tablename__ = 'states'
    storage_type = getenv('HBNB_TYPE_STORAGE')

    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', back_populates='state',
                              cascade='all, delete, delete-orphan')
        # print('+++ state.py <<>> db attributes +++')
    else:
        name: str = ''
        # print('+++ state.py > file attributes +++')

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
        # print('+++ state.py <<>> __init__() +++')

    if storage_type != 'db':
        @property
        def cities(self):
            """ Returns all cities related to this state """
            from models.city import City
            from models.__init__ import storage
            all_c = storage.all(City)
            cities = [c for c in all_c.values() if c.state_id == self.id]
            # print('+++ state.py <<>> cities @property +++')
            return cities
