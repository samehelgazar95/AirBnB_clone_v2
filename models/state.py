#!/usr/bin/python3
"""State class model"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import models

class State(BaseModel, Base):
    """State class that inherits from BaseModel class"""

    if models.storage_type == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', back_populates='state',
                              cascade='all, delete, delete-orphan')
    else:
        name: str = ''

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    if models.storage_type != 'db':
        @property
        def cities(self):
            """ Returns all cities related to this state """
            from models.city import City
            all_c = models.storage.all(City)
            cities = [c for c in all_c.values() if c.state_id == self.id]
            return cities
