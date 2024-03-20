#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from models.place import Place
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy.orm import declarative_base

class City(BaseModel):
    """ The city class, contains state ID and name """


    __tablename__ = "cities"

    state_id = ""
    name = ""

    places = relationship("Place", cascade='all, delete', backref="cities")
    state = relationship("State", backref="cities")
