#!/usr/bin/python3
"""Place class model"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
import models


class Place(BaseModel, Base):
    """Place class"""

    if models.storage_type == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        user = relationship('User', back_populates='places')
        city = relationship('City', back_populates='places')
        reviews = relationship('Review', back_populates='place',
                               cascade='all, delete, delete-orphan')
    else:
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

        @property
        def reviews(self):
            from models.review import Review
            all_revs = models.storage.all(Review)
            revs = [r for r in all_revs.values() if r.place_id == self.id]
            return(revs)

            