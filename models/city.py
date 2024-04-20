#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from models.place import Place
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy.orm import declarative_base

class City(BaseModel, Base):
    """ The city class, contains state ID and name """


    __tablename__ = "cities"
    id = Column(String(60), primary_key=True)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    name = Column(String(128), nullable=False)

    places = relationship("Place", cascade='all, delete', backref="cities")
#     state = relationship("State", backref="cities")