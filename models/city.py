#!/usr/bin/python3
"""City class model"""
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """City class that inherits from BaseModel class"""
    storage_type = getenv('HBNB_TYPE_STORAGE')
    __tablename__ = 'cities'

    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        state = relationship('State', back_populates='cities')
        # print('+++ city.py <<>> db attributes +++')
    else:
        state_id: str = ''
        name: str = ''
        # print('+++ city.py <<>> file attributes +++')

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
        # print('+++ city.py <<>> __init__() +++')
