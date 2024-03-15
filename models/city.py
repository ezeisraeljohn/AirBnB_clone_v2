#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from models.place import Place
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalachemy.ext.declarative import declarative_base

class City(BaseModel):
    """ The city class, contains state ID and name """


    __tablename__ = "cities"

    state_id = ""
    name = ""

    places = relatioship("Place", cascade='all, delete', backref="cities")
