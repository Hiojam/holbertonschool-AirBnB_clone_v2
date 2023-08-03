#!/usr/bin/python3
""" City Module for HBNB project """
import os
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.place import Place


class City(BaseModel, Base):
    """Class representing the City table"""
    __tablename__ = 'cities'

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        places = relationship("Place", backref="city", cascade="all, delete")
    else:
        @property
        def places(self):
            from models import storage
            place_list = []
            for place in storage.all(Place).values():
                if place.city_id == self.id:
                    place_list.append(place)
            return place_list
