#!/usr/bin/python3
"""City class model"""
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.__init__ import storage_type


class City(BaseModel, Base):
    """City class that inherits
        from BaseModel class
        Arguments:
            state_id: State id
            name: City name
        """

    if storage_type == 'db':
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        state = relationship('State', back_populates='cities')
    else:
        state_id: str = ''
        name: str = ''
    
    
        