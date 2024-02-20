#!/usr/bin/python3
"""Review class model"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits
        from BaseModel class
        Arguments:
            place_id: Place id
            user_id: User id
            text: The review text'
        """

    place_id: str = ''
    user_id: str = ''
    text: str = ''
