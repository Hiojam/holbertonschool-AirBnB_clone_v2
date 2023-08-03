#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.place import Place
from models.review import Review
import os


class User(BaseModel, Base):
    """Class representing the User table"""
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        places = relationship("Place", backref="user", cascade="all, delete")
        reviews = relationship("Review", backref="user", cascade="all, delete")
    else:
        @property
        def places(self):
            from models import storage
            place_list = []
            for place in storage.all(Place).values():
                if place.user_id == self.id:
                    place_list.append(place)
            return place_list

        @property
        def reviews(self):
            from models import storage
            review_list = []
            for review in storage.all(Review).values():
                if review.user_id == self.id:
                    review_list.append(review)
            return review_list
