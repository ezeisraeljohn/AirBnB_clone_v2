#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalachemy.ext.declarative import declarative_baseForig
from sqlalachemy.ext.declarative import declarative_base

class Place(BaseModel, Base):
    """ A place to stay
        Atrributes:
        city_id
        user_id
        name
        discription
        number of rooms
        number of bathreooms
        max guests
        price bu night
        latitude
        longitude

    """


    __tablename__ = "places"

    city_id = Column(String(60), nullable=False, ForeignKey("cities.id"))
    user_id = Column(string(60), nullable=False, ForeignKey("users.id"))
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
