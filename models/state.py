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
    __tablename__ = "states"

    id = Column(String(60), primary_key=True)
    name = Column(String(128), nullable=False)
    # cities = relationship("City", backref="state", cascade="all, delete")
    cities = relationship("City", backref="states")

    def cities(self):
        """ Return list of city objecs"""
        if os.getenv("HBNB_TYPE_STORAGE") == "fs":
            all_cities = models.storage.all(City)
            list_cities = []
            for value in all_cities.values():
                if value.state_id == self.id:
                    list_cities.append(value)
            print (list_cities)
            return list_cities
