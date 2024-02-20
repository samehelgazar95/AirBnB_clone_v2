#!/usr/bin/python3
"""Place class model"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Place class that inherits
        from BaseModel class
        Arguments:
            city_id: City id
            user_id: User id
            name: Place name
            description: Place desc
            number_rooms: Place number room
            number_bathrooms: Place number bathrooms
            max_guest: Place max guest
            price_by_night: Place price by night
            latitude: Place lat
            longitude: Place long
            amenity_ids: Amenity id
        """

    city_id: str = ''
    user_id: str = ''
    name: str = ''
    description: str = ''
    number_rooms: int = 0
    number_bathrooms: int = 0
    max_guest: int = 0
    price_by_night: int = 0
    latitude: float = 0.0
    longitude: float = 0.0
    amenity_ids: list = []
