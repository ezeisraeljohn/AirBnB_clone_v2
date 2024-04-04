#!/usr/bin/python3
"""This module defines a class User
    inherits from basemode and
    Base
"""
from models.base_model import BaseModel, Base
from models.place import Place
from models.review import Review
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by
    attributes:
    email,
    password,
    first_name and last_name
    """

    __tablename__ = "users"
    id = Column(String(60), primary_key=True)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    places = relationship("Place", backref="user")

