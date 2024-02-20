#!/usr/bin/python3
"""Amenity class model"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class that inherits
        from BaseModel class
        Arguments:
            name: Amenity name
        """

    name: str = ''
