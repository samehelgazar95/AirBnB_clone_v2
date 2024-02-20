#!/usr/bin/python3
"""State class model"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class that inherits
        from BaseModel class
        Arguments:
            name: State name
        """

    name: str = ''
