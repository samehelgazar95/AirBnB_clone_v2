#!/usr/bin/python3
"""City class model"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class that inherits
        from BaseModel class
        Arguments:
            state_id: State id
            name: City name
        """

    state_id: str = ''
    name: str = ''
