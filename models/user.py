#!/usr/bin/python3
""" User class model """
from os import getenv
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """
    User class that inherits
    from BaseModel class
    Arguments:
        email: User email
        password: User password
        first_name: User first name
        last_name: User last name
    """
    storage_type = getenv('HBNB_TYPE_STORAGE')

    if storage_type == 'db':
        print('>>> user.py db tables created <<<')
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
    else:
        print('>>> user.py file_storage attr <<<')
        email: str = ''
        password: str = ''
        first_name: str = ''
        last_name: str = ''

    def __init__(self, *args, **kwargs):
        print('>>> user.py __init__ <<<')
        """initializes state"""
        super().__init__(*args, **kwargs)
