#!/usr/bin/python3
"""This module defines a class User
    inherits from basemode and
    Base
"""
from models.base_model import BaseModel, Base
from models.place import place
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalachemy.ext.declarative import declarative_base


class User(BaseModel, Base):
    """This class defines a user by
    attributes:
    email,
    password,
    first_name and last_name
    """

    __tablename__ = "users"

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128)
    last_name = Column(String(128), nullable)
    places = relationship("Place", cascade='all, delete' backref="user")
