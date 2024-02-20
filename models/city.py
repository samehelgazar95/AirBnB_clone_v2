#!/usr/bin/python3
"""City class model"""
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """City class that inherits
        from BaseModel class
        Arguments:
            state_id: State id
            name: City name
        """
    storage_type = getenv('HBNB_TYPE_STORAGE')
        
    # if storage_type == 'db':
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    # else:
    state_id: str = ''
    name: str = ''
        
    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
