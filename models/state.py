#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from models.city import City
import models
import os
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship



class State(BaseModel, Base):
    """ State class """

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "states"

        id = Column(String(60), primary_key=True)
        name = Column(String(128), nullable=False)
        # cities = relationship("City", backref="state", cascade="all, delete")
        cities = relationship("City", backref="states")
    else:
        name = ''

        @property
        def cities(self):
            """ Return list of city objecs"""
            all_cities = models.storage.all(City)
            list_cities = []
            for city in all_cities.values():
                if self.id == city.state_id:
                    list_cities.append(city)
            return list_cities

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
