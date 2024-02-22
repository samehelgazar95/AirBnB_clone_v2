#!/usr/bin/python3
"""User class model"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits
        from BaseModel class
        Arguments:
            email: User email
            password: User password
            first_name: User first name
            last_name: User last name
        """

    email: str = ''
    password: str = ''
    first_name: str = ''
    last_name: str = ''
