#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.place import Place
import os

place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column(
        'place_id', String(60), ForeignKey('places.id'), primary_key=True
        ),
    Column(
        'amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True
        ),
    extend_existing=True
)


class Amenity(BaseModel, Base):
    """Class representing the Amenity table"""
    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)
    
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        places_amenities = relationship(
            "Place",
            secondary=place_amenity,
            back_populates="amenities",
            viewonly=False
        )
    else:
        @property
        def place_amenities(self):
            from models import storage
            place_list = []
            for place in storage.all(Place).values():
                if self in place.amenities:
                    place_list.append(place)
            return place_list
