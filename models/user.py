#!/usr/bin/python3
"""User class model"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
import models


class User(BaseModel, Base):
    """User class"""

    if models.storage_type == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
    else:
        email: str = ''
        password: str = ''
        first_name: str = ''
        last_name: str = ''
